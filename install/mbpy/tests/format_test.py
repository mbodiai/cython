#!/usr/bin/env python3
"""Test script to check Git dependency format."""

from pathlib import Path
from mbpy.pkg.dependency import Dependency


def test_git_formats():
    """Show the actual format of Git dependencies."""
    formats = [
        "git+https://github.com/psf/requests.git",
        "git+https://github.com/psf/requests.git@main",
        "git+https://github.com/psf/requests.git@v2.28.0",
        "psf/requests",
    ]

    print("=== ACTUAL GIT DEPENDENCY FORMATS ===\n")
    for git_url in formats:
        # Create a dependency for each format
        dep = Dependency(git_url, git=True)

        # For GitHub shorthand, manually set org and repo
        if "/" in git_url and not git_url.startswith("git+"):
            org, repo = git_url.split("/")
            dep.org = org
            dep.repo = repo

        # Print actual format used
        print(f"Input: {git_url}")
        print(f"Output (project_toml_name): {dep.project_name}")
        print()


if __name__ == "__main__":
    test_git_formats()
