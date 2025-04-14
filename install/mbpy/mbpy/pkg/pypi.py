"""Synchronizes requirements and hatch pyproject."""

import logging
import re
import sys
import traceback
from copy import deepcopy
from pathlib import Path
from time import time

from mbcore.even._internal._cache_impl import acache
from typing_extensions import (
    TYPE_CHECKING,
    AsyncGenerator,
    Dict,
    List,
    Literal,
    TypedDict,
)


InfoKey = Literal[
    "author",
    "author_email",
    "bugtrack_url",
    "classifiers",
    "description",
    "description_content_type",
    "docs_url",
    "download_url",
    "downloads",
    "dynamic",
    "home_page",
    "keywords",
    "license",
    "maintainer",
    "maintainer_email",
    "name",
    "package_url",
    "platform",
    "project_url",
    "project_urls",
    "provides_extra",
    "release_url",
    "requires_dist",
    "requires_python",
    "summary",
    "version",
    "yanked",
    "yanked_reason",
]
INFO_KEYS: List[InfoKey] = [
    "author",
    "author_email",
    "bugtrack_url",
    "classifiers",
    "description",
    "description_content_type",
    "docs_url",
    "download_url",
    "downloads",
    "dynamic",
    "home_page",
    "keywords",
    "license",
    "maintainer",
    "maintainer_email",
    "name",
    "package_url",
    "platform",
    "project_url",
    "project_urls",
    "provides_extra",
    "release_url",
    "requires_dist",
    "requires_python",
    "summary",
    "version",
    "yanked",
    "yanked_reason",
]
AdditionalKeys = Literal["last_serial", "releases", "urls", "vulnerabilities"]
ADDITONAL_KEYS: list[Literal[AdditionalKeys]] = [
    "last_serial",
    "releases",
    "urls",
    "vulnerabilities",
]
if TYPE_CHECKING:
    from asyncio import Task

    from aiohttp import ClientSession as Client
    from mbcore.display import safe_print
    from mbcore.import_utils import smart_import
    from mbcore.log import debug, error
    from mrender.md import Markdown
    from playwright.async_api import Response as PWResponse
    from typing_extensions import Any, AsyncGenerator, Dict, List, Literal, TypedDict

    from mbpy.cli import check_install_prompt
    from mbpy.tools.search import PackageInfo as GitPackageInfo
    from mbpy.pkg.dependency import PyPackageInfo as PackageInfo
    from mbpy.pkg.dependency import Dependency
else:
    try:
        from asyncio import Task

        from aiohttp import ClientSession as Client
        from playwright.async_api import Response as PWResponse

    except Exception:
        if debug():
            import traceback

            traceback.print_exc()
        PWResponse = object
        Client = object


class Response(PWResponse):
    _links: List[str] = []
    _status: int = 0
    _text: str = ""
    _task: "Task[str]"

    def __new__(cls, text="", links=None, response=None):
        import asyncio

        if links is None:
            links = []
        create_task = asyncio.create_task
        cls = super().__new__(cls)
        cls.__init__(
            text=text, links=links, task_factory=create_task, response=response
        )
        return cls

    def __init__(
        self,
        text=None,
        links=None,
        task_factory=None,
        response: "PWResponse | None" = None,
    ):
        if links is None:
            links = []
        if text:
            self._text = text
        if links:
            self._links = links
        if response:
            self._status = response.status
            create_task = smart_import("asyncio.create_task")
            task_factory = task_factory or create_task
            self._task = create_task(super().text())

            super().__init__(response)

            def set_text(fut: "Task[str]"):
                self._text = fut.result()

            self._task.add_done_callback(set_text)
        else:
            self._status = 0

    @property
    def links(self):
        return self._links

    @property
    def ok(self):
        return self.status == 200

    @property
    def status(self):
        return self._status

    @property
    def waited(self):
        last_coro = self._task.get_coro()
        cr_frame = last_coro.cr_frame if last_coro else None
        sttime = cr_frame.f_lasti if cr_frame else None

        return (time() - sttime) if sttime else -1

    @property
    def text(self):
        self._task = getattr(self, "_task", None)
        if self._text:
            return self._text
        while not (not self._task or self._task.done()) and self.waited < 5:
            pass
        return self._text


_client = None


def get_client(reuse=False):
    if not reuse:
        return Client()
    global _client
    if not _client:
        _client = Client()
    return _client


_browser = None
_context = None


async def get_browser(url="", headers=None):
    global _browser, _context
    if not _browser:
        if not TYPE_CHECKING:
            from mbpy.cli import check_install_prompt

            playwright = await check_install_prompt("playwright")
            if not playwright:
                raise ImportError(
                    "Playwright not installed. Please install it using `pip install playwright`"
                )
        import playwright.async_api as pw

        # Configure browser based on URL
        config = {
            "headless": True,
            "args": ["--no-sandbox", "--disable-setuid-sandbox"],
        }

        async_playwright = pw.async_playwright
        p = await async_playwright().start()
        _browser = await p.chromium.launch(**config)

        # Set context with appropriate headers
        ctx_config = {
            "user_agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
            "extra_http_headers": headers or {"Accept-Language": "en-US,en;q=0.9"},
        }

        _context = await _browser.new_context(**ctx_config)

        # Route handlers for performance
        if "pypi" in url:
            await _context.route(
                "**/*.{png,jpg,jpeg,gif,svg,css,woff,woff2}",
                lambda route: route.abort(),
            )

    return _context


async def browse_web(url, headers=None) -> str:
    """Browse web with improved HTML parsing and error handling."""
    context = await get_browser(url, headers)
    if context is None:
        raise ValueError("Failed to create browser context")

    page = await context.new_page()

    try:
        # Configure timeout and navigation
        timeout = 5000  # 5 seconds
        await page.goto(url, wait_until="commit", timeout=timeout)

        try:
            await page.wait_for_load_state("networkidle", timeout=timeout)
        except Exception as e:
            logging.debug(f"Networkidle timeout for {url}: {e}")

        return await page.content()

    finally:
        await page.close()


def save_results_to_file(results, filename="search_results.txt") -> None:
    with Path(filename).open("w") as f:
        for item in results:
            f.write(f"{item['title']} - {item['url']}\n")


async def browse(urls, headers={}, timeout=25, interactive=False) -> "list[Result]":
    """Browse web with improved error handling and rate limiting."""
    import asyncio
    import random

    from bs4 import BeautifulSoup
    from html2text import html2text
    from mrender.md import Markdown
    from mrender.web2md import html_to_markdown_with_depth

    urls = [urls] if isinstance(urls, str) else urls
    results = []

    # Default fallback headers if none provided
    if not headers:
        headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
            "Accept-Language": "en-US,en;q=0.5",
            "Accept-Encoding": "gzip, deflate, br",
            "DNT": "1",
            "Connection": "keep-alive",
            "Upgrade-Insecure-Requests": "1",
            "Sec-Fetch-Dest": "document",
            "Sec-Fetch-Mode": "navigate",
            "Sec-Fetch-Site": "none",
            "Cache-Control": "max-age=0",
        }

    for _i, url in enumerate(urls):
        try:
            # Add random delay between requests
            if _i > 0:
                await asyncio.sleep(random.uniform(2, 5))

            # Retry logic with exponential backoff
            max_retries = 3
            for attempt in range(max_retries):
                try:
                    # Increase delay with each retry
                    if attempt > 0:
                        await asyncio.sleep(2**attempt)

                    response = await browse_web(url)
                    debug(f"Response : {response}")

                    # Check for rate limiting/CAPTCHA indicators
                    rate_limit_indicators = [
                        "please email us",
                        "unusual traffic",
                        "enable javascript",
                        "captcha",
                        "automated requests",
                        "rate limit",
                    ]

                    if any(
                        indicator in response.lower()
                        for indicator in rate_limit_indicators
                    ):
                        if attempt == max_retries - 1:
                            raise ValueError(
                                f"Rate limit detected after {max_retries} attempts"
                            )
                        continue

                    # Parse content with BeautifulSoup
                    soup = BeautifulSoup(response, "html.parser")
                    title = soup.title.string if soup.title else "No title found"

                    # Extract main content with fallbacks
                    main_content = (
                        soup.find("main")
                        or soup.find("div", {"id": "content"})
                        or soup.find("div", {"class": "content"})
                        or soup.find("article")
                        or soup.find("body")
                        or soup
                    )

                    # Extract links
                    links = [
                        a.get("href") for a in main_content.find_all("a", href=True)
                    ]

                    # Create result with all available data
                    result = {
                        "url": url,
                        "title": title,
                        "content": main_content.get_text(strip=True)
                        if main_content
                        else "",
                        "html": str(main_content) if main_content else "",
                        "text": html2text(str(main_content)) if main_content else "",
                        "md": Markdown(html_to_markdown_with_depth(soup))
                        if main_content
                        else Markdown(""),
                        "links": links,
                        "status": 200,
                        "ok": True,
                    }

                    results.append(result)
                    debug(f"Successfully processed: {url}")
                    break

                except ValueError as ve:
                    from mbcore.log import warning

                    warning(f"Attempt {attempt + 1} failed: {str(ve)}")
                    if attempt == max_retries - 1:
                        raise
                    continue

        except Exception as e:
            error(f"Error fetching the webpage {url}: {str(e)}")
            if debug():
                traceback.print_exc()

            results.append(
                {
                    "url": url,
                    "error": str(e),
                    "status": getattr(e, "status", 500),
                    "text": f"Error fetching the webpage {url}: {str(e)}",
                    "md": Markdown(f"Error fetching the webpage {url}: {str(e)}"),
                    "ok": False,
                    "links": [],
                }
            )

    return results


class Result(TypedDict, total=False):
    title: str
    url: str
    content: str
    html: str
    md: "Markdown"
    links: List[str]
    error: str
    status: int
    waited: float
    ok: bool
    text: str


async def search_online(
    query: str, source: str = "ddg", save_to_file: bool = False, attempt: int = 0
) -> "list[Result]":
    """Search online with proper fallback and recursion control."""
    # Prevent infinite recursion
    if attempt > 2:
        logging.warning(f"Max retry attempts reached for query: {query}")
        return []

    results = []
    # Make DuckDuckGo the primary search engine
    base_url = {
        "ddg": f"https://lite.duckduckgo.com/lite?kd=-1&kp=-1&k1=-1&q={query}",
        "github": f"https://github.com/search?q={query}&type=repositories",
        "google": f"https://www.google.com/search?q={query}",
    }.get(source, f"https://html.duckduckgo.com/html/?q={query}")

    try:
        headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
            "Accept-Language": "en-US,en;q=0.5",
            "Accept-Encoding": "gzip, deflate, br",
            "DNT": "1",
            "Connection": "keep-alive",
            "Upgrade-Insecure-Requests": "1",
        }

        results = await browse(base_url, headers)

        if not results and source != "ddg":
            safe_print(f"No results found with {source}, trying DuckDuckGo")
            return await search_online(query, "ddg", save_to_file, attempt + 1)

        if save_to_file:
            save_results_to_file(results)

        return results

    except Exception as e:
        error(f"Error in search_online: {e}")
        if attempt < 2:
            # Try next source in priority order
            next_source = {"google": "ddg", "ddg": "github", "github": "google"}[source]
            await asyncio.sleep(1)
            return await search_online(query, next_source, save_to_file, attempt + 1)

        return []


async def get_latest_version(package_name: str) -> str | None:
    """Get the latest version of the specified package from PyPI.

    Args:
        package_name (str): The name of the package to fetch the latest version for.

    Returns:
        Optional[str]: The latest version of the package, or None if not found or on error.

    """
    try:
        client = Client()

        response = await client.get(f"https://pypi.org/pypi/{package_name}/json")
        data = await response.json()
        return data["info"]["version"]
    except (KeyError, ValueError) as e:
        logging.exception(f"Error parsing response for {package_name}: {e}")
    except Exception as e:
        logging.exception(
            f"Unexpected error fetching latest version for {package_name}: {e}",
        )
    return ""


def extract_suggested_package(suggestion: str) -> str | None:
    """Extract package name from PyPI suggestion HTML."""
    # Match pattern: href="/search/\?q=package_name"
    pattern = r'href="/search/\?q=([^"]+)"'
    match = re.search(pattern, suggestion)

    if match:
        return match.group(1)

    # Fallback for plain text
    pattern = r'Did you mean [\'"]([^\'"]+)[\'"]'
    match = re.search(pattern, suggestion)

    return match.group(1) if match else None


async def get_package_names(
    query_key,
    verbosity: "Literal[0,1, 2, 3]" = 0,
    include: "list[InfoKey] |InfoKey | None | Literal['all']" = None,
    release: "Any | None" = None,
    client: "Client | None" = None,
) -> List[str]:
    """Fetch package names from PyPI search results."""
    search_url = f"https://pypi.org/search/?q={query_key}"
    response = None

    try:
        response = await browse_web(search_url)
    except Exception:
        from mbcore.log import debug
        from mbcore.display import safe_print

        if debug():
            traceback.print_exc()
        if (
            "Looks like Playwright was just installed or updated."
            in traceback.format_exc()
        ):
            safe_print(
                (
                    "Looks like Playwright was just installed or updated."
                    + traceback.format_exc()
                    .split("Looks like Playwright was just installed or updated.")[-1]
                    .strip()
                )
                .replace("║", "")
                .replace("═", "")
                .replace("╚╝", "")
            )
    finally:
        pkg = await get_package_info(query_key, verbosity, include, release, client)
    from mbcore.log import verbose

    verbose(f"Response: {response or pkg}")
    page_content = response or ""

    if 'Did you mean \'<a class="link" href="/search/?q=' in page_content:
        suggestion = extract_suggested_package(page_content)
        if suggestion:
            client = client or get_client()
            response = await client.get(
                f"https://pypi.org/search/?q={suggestion}",
            )
            page_content = await response.text()
    # Extract package names from search results
    start_token = '<a class="package-snippet"'  # noqa
    end_token = "</a>"  # noqa
    name_token = '<span class="package-snippet__name">'  # noqa

    package_names = []
    start = 0
    while True:
        start = page_content.find(start_token, start)
        if start == -1:
            break
        end = page_content.find(end_token, start)
        snippet = page_content[start:end]
        name_start = snippet.find(name_token)
        if name_start != -1:
            name_start += len(name_token)
            name_end = snippet.find("</span>", name_start)
            package_name = snippet[name_start:name_end].strip()
            package_names.append(package_name)
        start = end
    return package_names


def ensure_backticks(text: str) -> str:
    """Ensure that backticks are completed in the given text."""
    open_backticks = text.count("\n```")
    close_backticks = text.count("```\n")
    while open_backticks > close_backticks:
        text += "`"
        close_backticks += 1
    while close_backticks > open_backticks:
        text = "`" + text
        open_backticks += 1
    # Single quotes next
    open_backticks = text.count(" `")
    close_backticks = text.count("` ")
    while open_backticks > close_backticks:
        text += "`"
        close_backticks += 1
    while close_backticks > open_backticks:
        text = "`" + text
        open_backticks += 1
    return text


async def top_github_match(package_name: str) -> "GitPackageInfo":
    from mbpy.tools.search import PackageInfo as GitPackageInfo
    from mbpy.tools.search import _search_repos

    # Extract just the base name if it's a path and fix lowercase conversion
    if isinstance(package_name, str) and ("/" in package_name or "\\" in package_name):
        # Get just the filename without path
        import os

        package_name = os.path.basename(package_name)
    return next(
        iter(await _search_repos(package_name, sort="best_match", limit=1)),
        GitPackageInfo(name=package_name),
    )


@acache(ttl=3600)
async def get_package_info(
    package_name: "str | Path | Dependency",
    verbosity: "Literal[0,1, 2, 3]" = 0,
    include=None,
    release=None,
    client=None,
    once=None,
) -> "PackageInfo | GitPackageInfo":
    """Retrieve detailed package information from PyPI JSON API."""
    from datetime import datetime

    from mbcore.display import safe_print
    from mbcore.log import debug, error, verbose

    from mbpy.pkg.dependency import Dependency

    if isinstance(package_name, Dependency):
        package_name = package_name.name
    package_name = (
        str(package_name).strip() if isinstance(package_name, Path) else package_name
    )

    if not client:
        if once is None:
            once = True
        client = get_client()

    package_url = f"https://pypi.org/pypi/{package_name}/json"
    response = await client.get(package_url)
    if response.status != 200:
        from mbcore.log import debug

        debug("Failed to fetch package info for " + str(package_name))
        import atexit
        import asyncio

        atexit.register(lambda: asyncio.run(client.close()))
        return await top_github_match(package_name)

    package_data: dict = deepcopy(await response.json())

    verbose(f"{package_name} keys: {getattr(package_data, 'keys', lambda: [])()}")
    info: Dict = package_data.get("info", {})
    include = [include] if isinstance(include, str) else include or []
    release_info = {}
    try:
        if release or "all" in include:
            release = release or info.get("version", "")
            release_found = False
            for key in package_data.get("releases", {}):
                if release in key:
                    release_found = True
                    release_info = package_data.get("releases", {}).get(key, [{}])[0]
                    break
            if not release_found:
                releases = package_data.get("releases", {}).keys()
                preview = 4 if len(releases) > 8 else 2 if len(releases) > 4 else 1
                first = ", ".join(list(releases)[:preview])
                last = ", ".join(list(releases)[-preview:])
                color = "spring_green1"
                safe_print(
                    f"[bold {color}]{package_name}[/bold {color}] release `{release}` not found in  {first} ... {last}",
                )
    except Exception as e:
        from mbcore.log import isverbose

        if isverbose():
            traceback.print_exc()
        error(f"Error fetching release {release} for {package_name}: {e}")

    finally:
        import atexit
        import asyncio

        atexit.register(lambda: asyncio.run(client.close()))

    if release or "all" in include:
        if not release_info:
            debug(f"Release info not found for {package_name} {release}")
            return PackageInfo(name="not found")
        info.update({k: v for k, v in release_info.items() if v})

    releases = package_data.get("releases", {})

    if releases:
        releases = sorted(
            releases.items(),
            key=lambda x: x[1][0]["upload_time"] if len(x[1]) > 0 else "zzzzzzz",
            reverse=True,
        )

        if releases and len(releases[0][1]) > 0 and len(releases[-1][1]) > 0:
            latest, earliest = releases[0], releases[-1]
        else:
            latest, earliest = None, None

    else:
        latest, earliest = None, None

    package_info: "PackageInfo" = {
        "name": info.get("name", ""),
        "version": info.get("version", "").replace("-", "."),
        "summary": info.get("summary", ""),
        "latest_release": datetime.strptime(
            latest[1][0]["upload_time"], "%Y-%m-%dT%H:%M:%S"
        ).strftime("%b %d, %Y %I:%M %p")
        if latest
        else "",
        "author": info.get("author", ""),
        "earliest_release": {
            "version": earliest[0].replace("-", ".") if earliest else "",
            "upload_time": datetime.strptime(
                earliest[1][0]["upload_time"], "%Y-%m-%dT%H:%M:%S"
            ).strftime("%b %d, %Y %I:%M %p"),
            "requires_python": earliest[1][0].get("requires_python", ""),
        }
        if earliest
        else {},
        "urls": info.get("project_urls", info.get("urls", {})),
        "description": ensure_backticks(info.get("description", ""))[: verbosity * 250]
        if verbosity > 0
        else "",
        "requires_python": info.get("requires_python", ""),
        "releases": [
            {
                release[0]: {
                    "upload_time": datetime.strptime(
                        release[1][0]["upload_time"], "%Y-%m-%dT%H:%M:%S"
                    ).strftime("%b %d, %Y %I:%M %p")
                }
            }
            for release in releases
        ]
        if releases and len(releases[0][1]) > 0
        else [],
    }

    if verbosity > 2 or "all" in include:
        package_info["description"] = info.get("description", "")

    project_urls: Dict[str, str] = info.get("project_urls", info.get("urls", {}))
    try:
        package_info["github_url"] = (
            next(
                (url for _, url in project_urls.items() if "github.com" in url.lower()),
                None,
            )
            or ""
        )
    except (StopIteration, TypeError, AttributeError):
        package_info["github_url"] = ""

    include = [include] if isinstance(include, str) else include or []
    if include and "all" in include:
        include = INFO_KEYS + ADDITONAL_KEYS

    for key in include:
        if key in ("releases", "release"):
            continue
        if key in ADDITONAL_KEYS:
            package_info.setdefault("extras", {})[key] = package_data.get(key, {})
        elif key in INFO_KEYS:
            package_info.setdefault("extras", {})[key] = info.get(key, "")
        else:
            raise ValueError(f"Invalid key: {key}")

    if not any(i in include for i in ("releases", "release", "all")):
        package_info.pop("releases", None)
    return package_info


async def find_and_sort(
    query_key: str,
    limit: int = 7,
    verbosity: Literal[0, 1, 2, 3] = 0,
    include: "Literal['all']  | InfoKey | list[InfoKey] | None" = None,
    release: str | None = None,
    github: bool = True,
    pypi: bool = False,
    sort: "Literal['downloads', 'stars', 'forks', 'updated']" = "downloads",
) -> "AsyncGenerator[PackageInfo, None]":
    """Find and sort packages concurrently with proper context handling."""
    if not str(verbosity).isnumeric() or int(verbosity) not in range(4):
        raise ValueError("Verbosity must be an integer between 0 and 3")
    verbosity = int(verbosity)
    try:
        import asyncio
        import contextlib
        import traceback

        from mbcore.execute import TaskGroup

        if "aiohttp" not in sys.modules:
            aiohttp = await check_install_prompt("aiohttp", python=True)
            if not aiohttp:
                raise ImportError(
                    "aiohttp not installed. Please install it using `pip install aiohttp`"
                )
        if "playwright" not in sys.modules:
            playwright = await check_install_prompt("playwright", python=True)
            if not playwright:
                raise ImportError(
                    "Playwright not installed. Please install it using `pip install playwright`"
                )
        if not TYPE_CHECKING:
            pass

        # class Client(ClientSession):
        #     aclose = ClientSession.close

        async with contextlib.AsyncExitStack() as stack:
            tg: TaskGroup = await stack.enter_async_context(TaskGroup())  # type: ignore
            client = await stack.enter_async_context(get_client())
            package_names = []

            if pypi:
                # Start package info retrieval
                query_task = tg.create_task(
                    get_package_info(
                        query_key,
                        verbosity=verbosity,
                        include=include,
                        release=release,
                        client=None,
                    ),
                    name=f"query_{query_key}",
                )
                names_task = tg.create_task(
                    get_package_names(
                        query_key=query_key,
                        verbosity=verbosity,
                        include=include,
                        release=release,
                        client=None,
                    ),
                    name="get_names",
                )

                # Ensure query package is fetched first
                package = await query_task
                if package:
                    yield package
                else:
                    safe_print(f"No package info for '{query_key}'.")

                # Get package names from search
                package_names = await names_task
                if not package_names:
                    from mbcore.display import safe_print

                    safe_print(
                        f"No related package names found for query '{query_key}'"
                    )
                    import atexit
                    import asyncio

                    atexit.register(lambda: asyncio.run(client.close()))
                    return

                # Get package info for each package name
                tasks = [
                    tg.create_task(
                        get_package_info(
                            package_name=name,
                            verbosity=verbosity,
                            include=include,
                            release=release,
                            client=None,
                            once=False,
                        ),
                        name=f"package_{name}",
                    )
                    for name in package_names
                    if name != query_key
                ]
                for task in asyncio.as_completed(tasks):
                    try:
                        package = await task
                        if package:
                            yield package
                    except Exception as e:
                        from mbcore.log import error

                        error(f"[ERROR] Failed retrieving package info: {e}")
                        traceback.print_exc()

            if github:
                from mbpy.tools.search import search_repos

                package_names = (
                    [query_key] + package_names if package_names else [query_key]
                )
                for task in asyncio.as_completed(
                    map(
                        tg.create_task,
                        [
                            search_repos(n, stars=True, limit=limit)
                            for n in [query_key] + package_names
                        ],
                    )
                ):
                    try:
                        package = await task
                        if package:
                            for p in package:
                                yield p
                    except Exception as e:
                        from mbcore.log import error

                        error(f"[ERROR] Failed retrieving package info: {e}")
                        traceback.print_exc()
    except Exception as e:
        import traceback
        from mbcore.log import error

        error(f"Error in find_and_sort: {e}")
        traceback.print_exc()
    finally:
        await client.close()


if __name__ == "__main__":
    import asyncio

    from mbcore.display import prompt_ask
    from mrender.md import Markdown
    from rich.console import Console
    from rich.table import Table

    async def main() -> None:
        args = list(sys.argv[1:])
        query = args[0] if len(args) > 1 else "python"
        source = args[1] if len(args) > 2 else "ddg"  # Changed default to ddg

        console = Console()

        try:
            results = await search_online(query, source)

            safe_print(results[-1]["text"])
            if not results:
                console.print(
                    f"\n[yellow]No results found for '[bold]{query}[/bold]' on any search engine[/yellow]"
                )
                return

            table = Table(show_header=True, header_style="bold magenta")
            table.add_column("Title", style="cyan", no_wrap=False)
            table.add_column("URL", style="green", no_wrap=False)
            table.add_column("Content", style="blue", no_wrap=False)

            for result in results:
                if result.get("title") and result.get("url"):
                    table.add_row(
                        result["title"][:100]
                        + ("..." if len(result["title"]) > 100 else ""),
                        result["url"][:100]
                        + ("..." if len(result["url"]) > 100 else ""),
                        result["text"][:1000]
                        + ("..." if len(result["text"]) > 100 else ""),
                    )

                Markdown(result["text"]).stream()
            console.print("\n")
            console.print(table)
            console.print("\n")
            if (
                a := prompt_ask(
                    "Select Row:", choices=[str(i) for i in range(len(results))] + ["q"]
                )
            ) != "q":
                results[int(a)]["md"].stream()
        except KeyboardInterrupt:
            safe_print("\n[magenta]Exiting...[/magenta]")
            for task in asyncio.all_tasks():
                task.cancel()
            asyncio.get_event_loop().stop()

        except Exception as e:
            console.print(f"\n[red]Error searching for '{query}': {str(e)}[/red]")
            traceback.print_exc()
            if debug():
                console.print_exception()

    asyncio.run(main())
