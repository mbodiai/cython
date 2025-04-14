"""Script to search with Google

Usage:
    python3 google.py [search terms]
"""

from collections.abc import AsyncGenerator
from io import StringIO
from pathlib import Path
import re
from re import Match
import sys
from typing import TYPE_CHECKING, Generator, Any, Tuple, Dict, Optional
import urllib.parse
import rich_click as click
from mbcore.display import safe_print
from mbpy.decorators.cli import to_click_options_args
from rich.markdown import Markdown
from typing_extensions import TypedDict, Unpack
from mbpy.parse.oldonline import build_text_hierarchy
from mbcore.types import wraps
from mbpy.serve import aserve, serve

if TYPE_CHECKING:
    from playwright.sync_api import sync_playwright
    from playwright.async_api import async_playwright
    from playwright.async_api import Response
    from playwright.sync_api import Response as SyncResponse
    from html2text import html2text

else:
    try:
        from playwright.sync_api import sync_playwright
        from playwright.async_api import async_playwright
        from playwright.async_api import Response
        from playwright.sync_api import Response as SyncResponse
        from html2text import html2text
    except ImportError:
        safe_print(
            "playwright and html2text are required for google search. Install with `pip install playwright html2text`"
        )
        sys.exit(1)

USER_AGENT = """Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"""


class Config(TypedDict):
    screenshot: Optional[Path] | bool
    text: bool
    html: bool
    json: bool
    links: bool
    summarize: bool
    markdown: bool


class ConfigKwargs(TypedDict, total=False):
    screenshot: Optional[Path] | bool
    text: bool
    html: bool
    json: bool
    links: bool
    summarize: bool
    markdown: bool


DEFAULT_CONFIG: Config = {
    "screenshot": False,
    "text": True,
    "html": False,
    "json": False,
    "links": True,
    "summarize": False,
    "markdown": False,
}


def google_client(
    query: str, **kwargs: "Unpack[ConfigKwargs]"
) -> Generator[
        Tuple[str, Config],  # Yield type
        Tuple[str, Any],  # Send type
        Dict[str, Any],  # Return type
]:
    config = Config(**{**DEFAULT_CONFIG, **kwargs})
    url = f"https://html.duckduckgo.com/html/?q={urllib.parse.quote(query)}"
    content, resp = yield (url, config)
    return process_response(content, config)


def google_server(
        request: tuple[str, Config]) -> tuple[str, SyncResponse | None]:
    """Handle tuple-based requests"""
    url, config = request  # Unpack tuple
    with sync_playwright() as p:
        browser = p.firefox.launch()
        page = browser.new_page()
        resp = page.goto(url)

        if config.get("screenshot"):
            path = (config["screenshot"] if isinstance(
                config["screenshot"], Path) else Path("google.png"))
            page.screenshot(path=path)

        return page.content(), resp


def describe_keys(json: dict | list) -> str:
    """Describe keys of a json object"""
    if isinstance(json, list):
        return "\n".join(describe_keys(item) for item in json)
    if not isinstance(json, dict):
        return ""
    return "\n".join(f"{k}: {describe_keys(v)}" for k, v in json.items())


LINKS_PATTERN = re.compile(r'<a href="([^"]+)"')


def get_links(content: str) -> list[str]:
    """Get links from content"""
    return re.findall(LINKS_PATTERN, content)


def process_response(content: str, **kwargs: Unpack[ConfigKwargs]) -> Dict[str, Any]:
    """Ensure non-empty output with fallback"""

    config = Config(**{**DEFAULT_CONFIG, **kwargs})
    result = {
        "text": html2text(content) if config["text"] else None,
        "html": content if config["html"] else None,
        "links": get_links(content) if config["links"] else None,
        "markdown": Markdown(content) if config["markdown"] else None,
    }
    json = None
    if config["summarize"]:
        json = json or build_text_hierarchy(StringIO(content))
        result["summarize"] = describe_keys(json)
    if config["json"]:
        json = json or build_text_hierarchy(StringIO(content))
        result["json"] = json
    if config["links"]:
        result["links"] = get_links(content)
    if config["markdown"]:
        result["markdown"] = Markdown(content)
    if config["text"]:
        result["text"] = html2text(content)

    # Fallback to text if no output selected
    if not any(result.values()):
        result["text"] = html2text(content)

    return {k: v for k, v in result.items() if v is not None}


async def agoogle_server(request: Tuple[str, dict]) -> Tuple[str, Any]:
    """Asynchronous server implementation"""
    url, config = request
    async with async_playwright() as p:
        browser = await p.firefox.launch()
        page = await browser.new_page()
        resp = await page.goto(url)
        return await page.content(), resp


async def agoogle(query: str, **kwargs: ConfigKwargs):
    """Asynchronous Google search function"""
    config: Config = Config(**{**DEFAULT_CONFIG, **kwargs})
    result = await anext(aserve(google_client(query, **config),
                                agoogle_server))
    return result

def consume(result: Generator[Tuple[str, Config], Tuple[str, Any], Dict[str, Any]]):
    """Consume a generator"""
    accumulator = {}

def google(query: str, **kwargs: ConfigKwargs):
    """Search Google and display results in terminal, markdown, json, text, or screenshot.

    Args:
        query: The search query.
        config: The configuration for the search.

    Returns:
        Dictionary containing search results in requested formats
    """
    config: Config = Config(**{**DEFAULT_CONFIG, **kwargs})
    result = serve(google_client(query, **config), google_server)
    return consume(result)


@to_click_options_args("query", command_name="google")
async def google_command(text: bool, html: bool, screenshot: Optional[Path],
                         query: str):
    """Command for asynchronous Google search"""
    config = {
        "text": text,
        "html": html,
        "screenshot": screenshot if screenshot else False,
    }
    return await agoogle(query, **config)



@click.command()
@click.option("--text", is_flag=True, help="Show text output")
@click.option("--html", is_flag=True, help="Show raw HTML")
@click.option("--screenshot",
              type=click.Path(path_type=Path),
              help="Save screenshot to path")
@click.argument("query")
@click.option("-j", "--json", is_flag=True, help="Show json output")
@click.option("-l", "--links", is_flag=True, help="Show links")
@click.option("-s", "--summarize", is_flag=True, help="Show summarize")
@click.option("-m", "--markdown", is_flag=True, help="Show markdown")
@click.option("-d", "--debug", is_flag=True, help="Show debug output")
@click.option("-vv", "--verbose", is_flag=True, help="Show verbose output")
def google_cli(query: str,
               text: bool,
               html: bool,
               screenshot: Optional[Path] = None,
               json: bool = False,
               links: bool = False,
               summarize: bool = False,
               markdown: bool = False,
               debug: bool = False,
               verbose: bool = False):
    """Command-line interface for Google search"""
    config = {
        "text": text,
        "html": html,
        "screenshot": screenshot if screenshot else False,
        "json": json,
        "links": links,
    }
    result = serve(google_client(query, **config), google_server)


if __name__ == "__main__":
    google_cli()
