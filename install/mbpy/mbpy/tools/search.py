from __future__ import annotations
import rich_click as click
import json
import logging
import re

import backoff
from mbcore.import_utils import smart_import
from mbcore.types import wraps
from mbpy.cli import check_install_prompt, AsyncGroup, AsyncCommand
from mbcore.cache import acache
from typing_extensions import (
    TYPE_CHECKING,
    Literal,
    Required,
    TypedDict,
)

from mbpy.decorators.cli import to_click_options_args


@click.group("f", invoke_without_command=True, cls=AsyncGroup)
@click.pass_context
def cli(ctx: click.RichContext):
    ctx.ensure_object(dict)
    ctx.obj["cache"] = {}


class PackageInfo(TypedDict, total=False):
    repo: str
    name: "Required[str]"
    org: str
    github_url: str
    updated_at: str
    description: str
    summary: str
    version: str
    stars: int
    forks: int
    urls: dict[str, list[str]]


class GitError(Exception):
    pass


log = logging.getLogger(__name__)

REF_TAG_RE = re.compile(r"(?<=\btag: )([^,]+)\b")
DESCRIBE_UNSUPPORTED = "%(describe"

# If testing command in shell make sure to quote the match argument like
# '*[0-9]*' as it will expand before being sent to git if there are any matching
# files in current directory.
DEFAULT_DESCRIBE = [
    "git",
    "describe",
    "--dirty",
    "--tags",
    "--long",
    "--match",
    "*[0-9]*",
]

if TYPE_CHECKING:
    pass

GitHubURL = str


@to_click_options_args
async def search_repos(
    query: str,
    repo: str = "",
    org: str = "",
    language: str = "",
    stars: int = 0,
    forks: int = 0,
    sort: Literal["stars", "forks", "updated", "best_match"] = "best_match",
    limit: int = 10,
    mode: Literal["code", "repos"] = "code",
) -> list[PackageInfo]:
    """Search GitHub repositories and return results a  s PackageInfo objects."""
    return await _search_repos(
        query, repo, org, language, stars, forks, sort, limit, mode
    )


# @acache(ttl=3600)
@backoff.on_exception(backoff.expo, GitError, max_time=60)
async def _search_repos(
    query: str,
    repo: str = "",
    org: str = "",
    language: str = "",
    stars: int = 0,
    forks: int = 0,
    sort: Literal["stars", "forks", "updated", "best_match"] = "best_match",
    limit: int = 10,
    mode: Literal["code", "repos"] = "code",
) -> list[PackageInfo]:
    """Search GitHub repositories and return results as PackageInfo objects."""
    from mbcore.log import debug
    from mbpy.cmd import arun
    from mbpy.env import org_and_repo

    org, repo = await org_and_repo(query)
    # Build GitHub search query
    search_query = f'"{query}"'
    if org:
        search_query += f" org:{org}"
    if repo:
        search_query += f" repo:{repo}"
    if language:
        search_query += f" language:{language}"
    if stars > 0:
        stars = int(stars)
        search_query += f" 'stars:>={stars}'"
    if forks > 0:
        forks = int(forks)
        search_query += f" forks:>={forks}"

    repo_fields = "name,url,updatedAt,stargazerCount,forkCount,description,createdAt"
    code_fields = "path,repository,textMatches,url"
    fields = repo_fields if mode == "repos" else code_fields
    cmd = f"gh search {mode} {search_query} --json {fields} --limit {limit}"
    from mbcore.log import verbose

    verbose(f"Searching GitHub repositories with query: {search_query}")

    from difflib import SequenceMatcher

    try:
        output = await arun(cmd, show=debug())
        if (
            not output
            or "no repositories matched your search" in output.lower()
            or "API rate limit exceeded " in output
        ):
            raise GitError("No repositories matched your search")

        results: list[dict] = json.loads(output)
        for r in results:
            if "repository" in r and mode == "code":
                rout = await arun(
                    f"gh search repos {r['repository']['name']} --json {repo_fields}",
                    show=debug(),
                )
                r.update(json.loads(rout)[0])
        if sort:
            results = sorted(
                results,
                key=lambda x: x[sort]
                if sort != "best_match"
                else SequenceMatcher(None, x["name"], query).ratio()
                if mode == "repos"
                else 0,
                reverse=True,
            )
        return [
            PackageInfo(
                **{
                    "name": r["name"],
                    "github_url": r["url"],
                    "updated_at": r["updatedAt"],
                    "description": r["description"],
                    "created_at": r["createdAt"],
                    "summary": r["description"]
                    if r["description"]
                    else await arun(
                        f"gh repo view {r['org']}/{r['name']}", show=debug()
                    ),
                    "stars": r["stargazerCount"],
                    "forks": r["forkCount"],
                }
            )
            for r in results
        ]

    except Exception as e:
        from mbcore.log import error

        if debug():
            import traceback

            traceback.print_exc()
            error(f"Error searching repositories: {str(e)} for query: {search_query}")
        return []


def uv_error(line) -> bool:
    line = str(line)
    return (
        line.lower().strip().startswith("error")
        or "failed" in line.lower()
        or "error" in line.lower()
        or "fatal" in line.lower()
        or "ERROR" in line
    )


async def check_repo(repo: str, version=None, quiet=True) -> GitHubURL:
    """Check if a repository exists and return the GitHub URL."""
    if TYPE_CHECKING:
        from mbcore.display import getconsole

        from mbpy.cmd import arun

        getconsole()
    else:
        smart_import("mbcore.display.getconsole")()
        arun = smart_import("mbpy.cmd").arun
        smart_import("mbpy.ctx", debug=True)
    await check_install_prompt("gh", no_pypi=True)
    repo = repo.split("@")[0]
    if "==" in repo:
        repo = repo.split("==")[0]
        version = repo.split("==")[1]
    if "==" in repo:
        repo = repo.split("==")[0]
        version = repo.split("==")[1]
    if "@" in repo:
        version = repo.split("@")[1]
        repo = repo.split("@")[0]

    # Fix command string construction
    branch_part = f"--branch {version}" if version else ""
    out = str(
        await arun(
            f"gh repo view {repo} --json name --json url {branch_part}", show=not quiet
        )
    ).lower()

    if not out or "could not resolve to a repository" in out:
        return ""
    return json.loads(out)["url"]


if __name__ == "__main__":
    cli()
