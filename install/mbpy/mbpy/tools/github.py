import os
import html2text
import httpx
import base64
import json
import sys
from typing import Dict, Any, Tuple, List, Optional
from pathlib import Path
from mbpy.decorators.cli import to_click_options_args
from mbcore.cache import cache
from mbcore.even._internal._cache_impl import render_table
from mbcore.log import warning, debug
from rich.console import Console
from rich.syntax import Syntax
from rich.table import Table
from mbcore import safe_print


@cache(ttl=600, persistent=True)
def repo(
    org: str,
    repo_name: str,
    branch: str = "main",
    max_depth: int = 2,
    format_output: bool = True,
):
    """Fetch repository information from GitHub API.

    Args:
        org: Organization name
        repo_name: Repository name
        branch: Branch name
        max_depth: Maximum depth for directory structure (default: 2)
        format_output: Whether to format the output (default: True)

    Returns:
        Tuple of readme text and repository contents
    """
    base_url = f"https://api.github.com/repos/{org}/{repo_name}"
    headers = {"Accept": "application/vnd.github+json"}

    # Use GH_TOKEN or GIT_TOKEN or GITHUB_TOKEN for authentication
    token = os.getenv("GH_TOKEN") or os.getenv("GIT_TOKEN") or os.getenv("GITHUB_TOKEN")
    if token:
        headers["Authorization"] = f"Bearer {token}"
        debug(f"Using GitHub token for API calls to {org}/{repo_name}")

    with httpx.Client(headers=headers, timeout=30.0) as client:
        # Fetch README content specifically
        debug(f"Fetching README for {org}/{repo_name}")
        readme_response = client.get(f"{base_url}/readme?ref={branch}")
        readme_content = ""

        if readme_response.status_code == 200:
            try:
                readme_data = readme_response.json()
                if "content" in readme_data and readme_data["content"]:
                    # GitHub returns base64 encoded content
                    readme_content = base64.b64decode(readme_data["content"]).decode(
                        "utf-8"
                    )
            except Exception as e:
                warning(f"Failed to decode README content: {e}")
                readme_content = f"Error parsing README: {e}"
        else:
            warning(f"Failed to fetch README: {readme_response.status_code}")
            readme_content = "No README found or unable to access it."

        # Fetch recursive directory structure
        directories = _get_recursive_contents(
            client, base_url, branch, max_depth=max_depth
        )

    if format_output:
        # Format the README content to be more readable
        readme_content = _format_readme(readme_content)

    return readme_content, directories


def _format_readme(content: str) -> str:
    """Format README content to be more readable.

    Args:
        content: Raw README content

    Returns:
        Formatted README content
    """
    if not content or content == "No README found or unable to access it.":
        return content

    # Convert markdown to readable text
    h = html2text.HTML2Text()
    h.ignore_links = False
    h.ignore_images = False
    h.body_width = 0  # No wrapping

    try:
        return h.handle(content)
    except Exception:
        # If html2text fails, return the original content
        return content


def _get_recursive_contents(
    client: httpx.Client,
    base_url: str,
    branch: str,
    path: str = "",
    max_depth: int = 2,
    current_depth: int = 0,
) -> List[Dict[str, Any]]:
    """Recursively fetch directory contents up to max_depth.

    Args:
        client: HTTP client
        base_url: Base API URL
        branch: Branch name
        path: Current path
        max_depth: Maximum depth to recurse
        current_depth: Current recursion depth

    Returns:
        List of directory contents
    """
    if current_depth >= max_depth:
        return []

    url = f"{base_url}/contents"
    if path:
        url += f"/{path}"
    url += f"?ref={branch}"

    debug(f"Fetching contents for {url}")
    response = client.get(url)

    if response.status_code != 200:
        warning(f"Failed to fetch contents for {url}: {response.status_code}")
        return []

    try:
        contents = response.json()
        if not isinstance(contents, list):
            return []

        # For each directory, recursively get its contents
        for item in contents:
            if item.get("type") == "dir" and current_depth < max_depth - 1:
                item_path = path + "/" + item["name"] if path else item["name"]
                item["contents"] = _get_recursive_contents(
                    client, base_url, branch, item_path, max_depth, current_depth + 1
                )

        return contents
    except Exception as e:
        warning(f"Error parsing contents: {e}")
        return []


def print_directory_structure(contents, prefix=""):
    """Print directory structure in a tree-like format.

    Args:
        contents: Directory contents
        prefix: Prefix for indentation
    """
    # Sort contents: directories first, then files
    sorted_contents = sorted(
        contents, key=lambda x: (x.get("type", "") != "dir", x.get("name", ""))
    )

    for i, item in enumerate(sorted_contents):
        is_last = i == len(sorted_contents) - 1
        symbol = "└── " if is_last else "├── "

        item_name = item.get("name", "")
        item_type = item.get("type", "")

        if item_type == "dir":
            # Print directory with blue color and trailing slash
            safe_print(f"{prefix}{symbol}[blue]{item_name}/[/blue]")

            # Calculate new prefix for children
            new_prefix = prefix + ("    " if is_last else "│   ")

            # Print children if present
            if "contents" in item and item["contents"]:
                print_directory_structure(item["contents"], new_prefix)
        else:
            # For files, add size information if available
            size = item.get("size", 0)
            size_str = ""
            if size:
                if size < 1024:
                    size_str = f"({size} B)"
                elif size < 1024 * 1024:
                    size_str = f"({size / 1024:.1f} KB)"
                else:
                    size_str = f"({size / (1024 * 1024):.1f} MB)"

            safe_print(f"{prefix}{symbol}{item_name} [dim]{size_str}[/dim]")


def display_repo_info(
    org: str, repo_name: str, branch: str = "main", max_depth: int = 2
):
    """Display repository information.

    Args:
        org: Organization name
        repo_name: Repository name
        branch: Branch name
        max_depth: Maximum depth for directory structure
    """
    readme, contents = repo(org, repo_name, branch, max_depth, True)

    safe_print(
        f"[bold green]Repository:[/bold green] {org}/{repo_name} [dim](branch: {branch})[/dim]"
    )

    if readme and readme != "No README found or unable to access it.":
        safe_print("\n[bold blue]README[/bold blue]")
        safe_print(readme)
    else:
        safe_print("\n[yellow]No README found for this repository[/yellow]")

    if contents:
        safe_print("\n[bold blue]Directory Structure[/bold blue]")
        print_directory_structure(contents)

    return readme, contents


# Backward compatibility for CLI
def main(org: str, repo_name: str, branch: str = "main", max_depth: int = 2):
    return display_repo_info(org, repo_name, branch, max_depth)


if __name__ == "__main__":
    # Example usage
    from mbpy.cmd import run_cached

    try:
        # Get repository info from git remote
        out = run_cached("git remote get-url origin", show=False).strip()
        if "github.com" not in out:
            sys.exit(safe_print(f"Could not find GitHub repo from: {out}"))

        # Parse org/repo from remote URL
        if out.startswith("git@github.com:"):
            # SSH format: git@github.com:owner/repo.git
            parts = (
                out.replace("git@github.com:", "")
                .replace(".git", "")
                .strip()
                .split("/")
            )
        else:
            # HTTPS format: https://github.com/owner/repo.git
            parts = (
                out.replace("https://github.com/", "")
                .replace(".git", "")
                .strip()
                .split("/")
            )

        org, repo_name = parts[0], parts[1]
        branch = run_cached("git branch --show-current", show=False).strip()

        # Display repository information (default max_depth=3)
        display_repo_info(org, repo_name, branch, 3)
    except Exception as e:
        import traceback

        traceback.print_exc()
        sys.exit(safe_print(f"Error: {str(e)}"))
