#!/usr/bin/env python3
"""
Test that gets git dependency formats directly from get_toml_name.
"""

import pytest
from pathlib import Path
from mbpy.pkg.dependency import Dependency, get_toml_name

# ACTUAL GIT DEPENDENCY FORMATS BASED ON REAL INSTALLATION
STANDARD_GIT_URL_FORMAT = "git+https://github.com/psf/requests.git"
GIT_BRANCH_FORMAT = "git+https://github.com/psf/requests.git@main"
GIT_TAG_FORMAT = "git+https://github.com/psf/requests.git@v2.28.0"
GITHUB_SHORTHAND_FORMAT = "git+https://github.com/psf/requests"


@pytest.mark.parametrize(
    "git_url,expected_format",
    [
        # Standard git URL
        ("git+https://github.com/psf/requests.git", STANDARD_GIT_URL_FORMAT),
        # With branch specification
        ("git+https://github.com/psf/requests.git@main", GIT_BRANCH_FORMAT),
        # With tag specification
        ("git+https://github.com/psf/requests.git@v2.28.0", GIT_TAG_FORMAT),
        # GitHub shorthand
        ("psf/requests", GITHUB_SHORTHAND_FORMAT),
    ],
)
def test_get_toml_name_git(git_url, expected_format):
    """Test that different git URL formats are handled correctly by calling get_toml_name directly."""
    # Create a dependency with the git URL
    dep = Dependency(git_url, git=True)

    # For GitHub shorthand, manually set org and repo
    if "/" in git_url and not git_url.startswith("git+"):
        org, repo = git_url.split("/")
        dep.org = org
        dep.repo = repo

    # Get the format directly from get_toml_name function
    actual_format = get_toml_name(dep)

    # Check the format
    assert actual_format == expected_format, (
        f"Incorrect format for {git_url}: got {actual_format}, expected {expected_format}"
    )

    print(f"\nEXACT LITERAL FORMAT for {git_url}:")
    print(actual_format)


if __name__ == "__main__":
    for git_url, expected_format in [
        ("git+https://github.com/psf/requests.git", STANDARD_GIT_URL_FORMAT),
        ("git+https://github.com/psf/requests.git@main", GIT_BRANCH_FORMAT),
        ("git+https://github.com/psf/requests.git@v2.28.0", GIT_TAG_FORMAT),
        ("psf/requests", GITHUB_SHORTHAND_FORMAT),
    ]:
        print(f"Testing {git_url}...")
        test_get_toml_name_git(git_url, expected_format)
