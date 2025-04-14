import asyncio
from collections.abc import AsyncIterable
import heapq
import json as orjson
from difflib import SequenceMatcher
from typing_extensions import Literal

from mbcore import ctx
from mbcore.display import getconsole
from mbcore.more import unique_everseen

from mbpy.cmd import arun
from mbpy.env import isgit, org_and_repo
from mbpy.pkg.pypi import find_and_sort
from mbcore.log import debug

console = getconsole()


async def get_close_matches(word, possibilities, n=3, cutoff=0.6):
    """Use SequenceMatcher to return list of the best "good enough" matches.

    word is a sequence for which close matches are desired (typically a
    string).

    possibilities is a list of sequences against which to match word
    (typically a list of strings).

    Optional arg n (default 3) is the maximum number of close matches to
    return.  n must be > 0.

    Optional arg cutoff (default 0.6) is a float in [0, 1].  Possibilities
    that don't score at least that similar to word are ignored.

    The best (no more than n) matches among the possibilities are returned
    in a list, sorted by similarity score, most similar first.

    >>> get_close_matches("appel", ["ape", "apple", "peach", "puppy"])
    ['apple', 'ape']
    >>> import keyword as _keyword
    >>> get_close_matches("wheel", _keyword.kwlist)
    ['while']
    >>> get_close_matches("Apple", _keyword.kwlist)
    []
    >>> get_close_matches("accept", _keyword.kwlist)
    ['except']
    """

    if not n > 0:
        raise ValueError("n must be > 0: %r" % (n,))
    if not 0.0 <= cutoff <= 1.0:
        raise ValueError("cutoff must be in [0.0, 1.0]: %r" % (cutoff,))
    result = []
    s = SequenceMatcher()
    s.set_seq2(word)
    async for x in possibilities:
        s.set_seq1(x)
        if (
            s.real_quick_ratio() >= cutoff
            and s.quick_ratio() >= cutoff
            and s.ratio() >= cutoff
        ):
            result.append((s.ratio(), x))

    # Move the best scorers to head of list
    result = heapq.nlargest(n, result)
    # Strip scores for the best n matches
    for score, x in result:
        yield x


async def suggest_similar(
    package: str,
    name_field: str = "name",
    limit: int = 10,
    sources: list[Literal["pypi", "github"]] | None = None,
    additional_sort_fields: list[str] | None = None,
    reverse_fields: list[bool] | None = None,
    include_fields: list[str] | None = None,
    exclude_fields: list[str] | None = None,
) -> "AsyncIterable[dict[str, str]]":
    """Find similar items based on name similarity and additional sorting criteria.

    This asynchronous function combines local package search results with GitHub repository
    results and sorts them based on name similarity and additional criteria. It supports
    flexible field selection and sorting options.
        package: Target name to compare against (e.g., "requests" or "org/repo")
        name_field: Field to use for name comparison (defaults to "name")
        additional_sort_fields: Additional fields to use for sorting (e.g., ["stargazersCount", "updatedAt"])
        reverse_fields: Whether to reverse sort for each additional field (e.g., [True, False])
    Returns:
        An iterable of dictionaries containing the sorted and filtered results
    Examples:
        >>> import asyncio
        >>> async def example():
        ...     results = [result async for result in suggest_similar(
        ...         "requests",
        ...         additional_sort_fields=["stargazersCount"],
        ...         reverse_fields=[True],
        ...         include_fields=["name", "stargazersCount"]
        ...     )]
        ...     return results
        >>> results = asyncio.run(example())
        >>> len(results) > 0
        True
        >>> all(isinstance(r, dict) for r in results)
        True
        >>> all("name" in r and "stargazersCount" in r for r in results)
        True
        >>> async def example_exclude():
        ...     results = [result async for result in suggest_similar(
        ...         "fastapi",
        ...         exclude_fields=["description"]
        ...     )]
        ...     return results
        >>> result = asyncio.run(example_exclude())
        >>> "description" not in result[0]
        True
    Notes:
        - Results are sorted using online algorithms from more.py for memory efficiency
        - Combines both local package search and GitHub repository search results
        - Removes duplicates while preserving sort order
        - GitHub results include repository metadata like star count and last update time
    """
    from aiostream.stream.combine import map

    packages = find_and_sort(package, github=True, pypi=True, limit=limit)
    async for similar in get_close_matches(
        package, map(packages, lambda x, *args: x["name"])
    ):
        yield similar
    return
    sources = sources or ["pypi", "github"]
    queue = asyncio.Queue()

    async def fetch_pypi():
        if "pypi" in sources:
            async for pkg in find_and_sort(package, github=False, pypi=True):
                await queue.put(pkg)

    async def fetch_github():
        if "github" in sources:
            if isgit(package):
                org, repo = await org_and_repo(package)
                search = f"org:{org} {repo}" if org else repo
            else:
                search = package

            out1 = str(
                await arun(
                    f"gh search repos --json name --json updatedAt --json url --json stargazersCount --json description {search}"
                )
            ).lower()
            out2 = str(
                await arun(
                    f"gh search repos --json name --json updatedAt --json url --json stargazersCount --json description {package}"
                )
            ).lower()

            with ctx.suppress() if not debug() else ctx.nullcontext():
                if out1 and "could not resolve to a repository" not in out1:
                    out1 = out1[out1.find("[") : out1.rfind("]")].strip()
                if out2 and "could not resolve to a repository" not in out2:
                    out2 = out2[out2.find("[") : out2.rfind("]")].strip()

            gh_results = []
            for out in (out1, out2):
                if out and "[" in out:
                    gh_results.extend(
                        orjson.loads(o[o.find("{") :].strip().rstrip("}") + "}")
                        for o in out.split("},")
                        if o and "{" in o
                    )
            for result in gh_results:
                await queue.put(result)

    async def worker():
        task = None
        while task is not None and not queue.empty():
            task = queue.get()
            if task is None:
                break

        if task is not None:
            await task
        return task

    results = []
    heapq.heapify([])
    for task in asyncio.as_completed(
        [asyncio.ensure_future(worker()) for _ in range(limit)]
    ):
        result = await task
        if result is not None:
            heapq.heappush(results, result)

    await queue.put(None)  # Sentinel to indicate completion

    # Create sort key function
    sort_key = create_similarity_sort_key(
        package,
        name_field,
        additional_sort_fields or [],
        reverse_fields=reverse_fields or [],
    )

    # Sort and filter results
    sorted_results = heapq.nsmallest(limit, results, key=sort_key)
    filtered_results = filter_and_transform_items(
        sorted_results, include_fields, exclude_fields
    )

    for result in unique_everseen(filtered_results, key=sort_key):
        yield result


if __name__ == "__main__":
    import asyncio

    async def main():
        async for item in suggest_similar("pandas"):
            console.print(item)

    asyncio.run(main())
