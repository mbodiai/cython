#!/usr/bin/env python3

"""
ACTUAL GIT DEPENDENCY FORMATS AND TESTS

Shows the actual formats for Git dependencies in TOML files based on real installations.
"""

import pytest
import os
import tempfile
import shutil
from pathlib import Path
import re
import tomlkit
from mbpy.pkg.dependency import Dependency, get_toml_name
from mbpy.env import git_devws

# ACTUAL GIT DEPENDENCY FORMATS BASED ON REAL INSTALLATION
# For dependencies that haven't been cloned locally yet
STANDARD_GIT_URL_FORMAT = "git+https://github.com/psf/requests.git"
GIT_BRANCH_FORMAT = "git+https://github.com/psf/requests.git@main"
GIT_TAG_FORMAT = "git+https://github.com/psf/requests.git@v2.28.0"
GITHUB_SHORTHAND_FORMAT = "git+https://github.com/psf/requests"

# For dependencies that have been cloned locally
# These use @ file:// syntax pointing to the local clone
LOCAL_CLONE_FORMAT = "requests @ file://.dev/psf/requests"  # This is simplified - actual path will differ

# Real TOML with Standard Git URL
STANDARD_GIT_URL_TOML = """
[project]
name = "test-project"
version = "0.1.0"
description = "Test project for git dependency formats"
dependencies = ["git+https://github.com/psf/requests.git"]

[build-system]
requires = ["setuptools>=42", "wheel"]
build-backend = "setuptools.build_meta"
"""

# Real TOML with Git URL with tag
GIT_TAG_TOML = """
[project]
name = "test-project"
version = "0.1.0"
description = "Test project for git dependency formats"
dependencies = ["git+https://github.com/psf/requests.git@v2.28.0"]

[build-system]
requires = ["setuptools>=42", "wheel"]
build-backend = "setuptools.build_meta"
"""

# Real TOML with Git URL with branch
GIT_BRANCH_TOML = """
[project]
name = "test-project"
version = "0.1.0"
description = "Test project for git dependency formats"
dependencies = ["git+https://github.com/psf/requests.git@main"]

[build-system]
requires = ["setuptools>=42", "wheel"]
build-backend = "setuptools.build_meta"
"""

# Real TOML with GitHub shorthand
GITHUB_SHORTHAND_TOML = """
[project]
name = "test-project"
version = "0.1.0"
description = "Test project for git dependency formats"
dependencies = ["git+https://github.com/psf/requests"]

[build-system]
requires = ["setuptools>=42", "wheel"]
build-backend = "setuptools.build_meta"
"""

# Multiple Git dependencies in one TOML file
MULTIPLE_GIT_DEPS_TOML = """
[project]
name = "test-project"
version = "0.1.0"
description = "Test project for git dependency formats"
dependencies = [
    "git+https://github.com/psf/requests.git",
    "git+https://github.com/psf/requests.git@v2.28.0",
    "git+https://github.com/psf/requests"
]

[build-system]
requires = ["setuptools>=42", "wheel"]
build-backend = "setuptools.build_meta"
"""


def get_package_version(package_name, default=""):
    """Extract the installed version of a package from pip"""
    import subprocess

    try:
        result = subprocess.run(
            ["pip", "show", package_name], capture_output=True, text=True
        )
        if result.returncode == 0:
            for line in result.stdout.splitlines():
                if line.startswith("Version:"):
                    return line.split(":", 1)[1].strip()
    except Exception:
        pass
    return default


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
def test_git_dependency_formats(git_url, expected_format):
    """Test that different git URL formats are handled correctly."""

    # Mock git_devws to return a path that doesn't exist
    # This simulates the scenario where the repo hasn't been cloned yet
    def mock_git_devws(org, repo):
        return Path(f"/tmp/nonexistent/{org}/{repo}")

    # Create a dependency with the git URL - using a real repo
    dep = Dependency(git_url, git=True)

    # For GitHub shorthand, manually set org and repo as this would normally
    # be done during the async initialization
    if "/" in git_url and not git_url.startswith("git+"):
        org, repo = git_url.split("/")
        dep.org = org
        dep.repo = repo

    # Reset cached properties to force recalculation with our fixed implementation
    dep._project_toml_name = None

    # Force direct calculation with get_toml_name
    actual_format = get_toml_name(dep)

    # Check the format matches expected format
    assert actual_format == expected_format, (
        f"Incorrect format for {git_url}: got {actual_format}, expected {expected_format}"
    )

    print(f"\nEXACT LITERAL FORMAT for {git_url}:")
    print(actual_format)


# Add a new test for local clone format
def test_local_git_dependency_format(tmp_path):
    """Test Git dependency format when the repo has been cloned locally."""
    # Create a mock local repo
    local_repo = tmp_path / ".dev" / "psf" / "requests"
    local_repo.mkdir(parents=True)

    # Mock git_devws to return our temp path
    def mock_git_devws(org, repo):
        return local_repo

    # Create a dependency with a Git URL
    dep = Dependency("git+https://github.com/psf/requests.git", git=True)
    dep.org = "psf"
    dep.repo = "requests"
    dep._base = "requests"  # Set the base name

    # Reset cached properties
    dep._project_toml_name = None

    # Get the format
    actual_format = get_toml_name(dep)

    # Expected format with the actual path
    expected_format = f"requests @ file://{str(local_repo)}"

    # Check it has the correct format
    assert actual_format == expected_format, (
        f"Incorrect local format: got {actual_format}, expected {expected_format}"
    )

    print(f"\nEXACT LITERAL FORMAT for local clone:")
    print(actual_format)


# Fast test that runs the original format display without pytest
def run_formats_only():
    """Run just the formats display without running tests (for when pytest isn't available)."""
    print("=== ACTUAL GIT DEPENDENCY FORMATS ===\n")
    print(f"Standard Git URL: {STANDARD_GIT_URL_FORMAT}")
    print(f"Git URL with branch: {GIT_BRANCH_FORMAT}")
    print(f"Git URL with tag: {GIT_TAG_FORMAT}")
    print(f"GitHub shorthand: {GITHUB_SHORTHAND_FORMAT}")

    print("\n=== COMPLETE TOML FILES WITH ACTUAL FORMATS ===\n")
    print("Standard Git URL TOML:")
    print(STANDARD_GIT_URL_TOML)
    print("\nGit URL with Branch TOML:")
    print(GIT_BRANCH_TOML)
    print("\nGit URL with Tag TOML:")
    print(GIT_TAG_TOML)
    print("\nGitHub Shorthand TOML:")
    print(GITHUB_SHORTHAND_TOML)
    print("\nMultiple Git Dependencies TOML:")
    print(MULTIPLE_GIT_DEPS_TOML)


if __name__ == "__main__":
    # Always run the function to display formats when run directly
    run_formats_only()

    # Optional: Add a note about running with pytest for tests
    print("\n\nNote: Run this file with 'pytest' to execute the actual tests.")
