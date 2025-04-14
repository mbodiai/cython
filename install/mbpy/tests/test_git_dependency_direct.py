#!/usr/bin/env python3
"""
Test file for directly testing git dependency formats
"""

import pytest
from pathlib import Path
import tempfile
import shutil
import os
from mbpy.pkg.dependency import Dependency, get_toml_name


def test_git_remote_deps():
    """Test direct git URLs without local clones."""
    # Create direct git dependencies
    dep1 = Dependency("git+https://github.com/psf/requests.git")
    dep2 = Dependency("git+https://github.com/psf/requests.git@main")
    dep3 = Dependency("git+https://github.com/psf/requests.git@v2.28.0")
    dep4 = Dependency("psf/requests")

    assert dep1.git == True
    assert dep2.git == True
    assert dep3.git == True
    assert dep4.git == True

    assert dep1.source == "git+https://github.com/psf/requests.git"
    assert dep2.source == "git+https://github.com/psf/requests.git@main"
    assert dep3.source == "git+https://github.com/psf/requests.git@v2.28.0"
    assert dep4.source == "git+https://github.com/psf/requests.git"

    assert dep1.base == "requests"
    assert dep2.base == "requests"
    assert dep3.base == "requests"
    assert dep4.base == "requests"

    # Make sure we get expected formats
    assert dep1.project_name == "requests @ git+https://github.com/psf/requests.git", (
        f"Expected 'requests @ git+https://github.com/psf/requests.git' but got '{dep1.project_name}'"
    )
    assert (
        dep2.project_name == "requests @ git+https://github.com/psf/requests.git@main"
    ), (
        f"Expected 'requests @ git+https://github.com/psf/requests.git@main' but got '{dep2.project_name}'"
    )
    assert (
        dep3.project_name
        == "requests @ git+https://github.com/psf/requests.git@v2.28.0"
    ), (
        f"Expected 'requests @ git+https://github.com/psf/requests.git@v2.28.0' but got '{dep3.project_name}'"
    )
    assert dep4.project_name == "requests @ git+https://github.com/psf/requests.git", (
        f"Expected 'requests @ git+https://github.com/psf/requests.git' but got '{dep4.project_name}'"
    )

    assert (
        dep1.requirements_name == "requests @ git+https://github.com/psf/requests.git"
    ), (
        f"Expected 'requests @ git+https://github.com/psf/requests.git' but got '{dep1.requirements_name}'"
    )
    assert (
        dep2.requirements_name
        == "requests @ git+https://github.com/psf/requests.git@main"
    ), (
        f"Expected 'requests @ git+https://github.com/psf/requests.git@main' but got '{dep2.requirements_name}'"
    )
    assert (
        dep3.requirements_name
        == "requests @ git+https://github.com/psf/requests.git@v2.28.0"
    ), (
        f"Expected 'requests @ git+https://github.com/psf/requests.git@v2.28.0' but got '{dep3.requirements_name}'"
    )
    assert (
        dep4.requirements_name == "requests @ git+https://github.com/psf/requests.git"
    ), (
        f"Expected 'requests @ git+https://github.com/psf/requests.git' but got '{dep4.requirements_name}'"
    )

    assert dep1.org == "psf"
    assert dep2.org == "psf"
    assert dep3.org == "psf"
    assert dep4.org == "psf"

    assert dep1.repo == "requests"
    assert dep2.repo == "requests"
    assert dep3.repo == "requests"
    assert dep4.repo == "requests"


def test_git_local_clone_deps():
    """Test local git clones with @ file:// syntax."""
    # Create a temp directory to simulate a local repo clone
    temp_dir_obj = tempfile.TemporaryDirectory()
    temp_dir = temp_dir_obj.name
    original_cwd = os.getcwd()
    try:
        # Create a simulated local git repo inside the temp dir
        local_clone = Path(temp_dir) / ".dev" / "psf" / "requests"
        local_clone.mkdir(parents=True)

        # Change directory into the temp dir
        os.chdir(temp_dir)

        # Create dependency with local clone (should now detect it relative to cwd)
        dep = Dependency("psf/requests", editable=True)

        # When local clone exists, should use @ file:// syntax with local path
        # Expected path needs to be absolute for comparison
        expected = f"requests @ file://{local_clone.resolve()}"
        actual = dep.project_name
        assert actual == expected, f"Expected '{expected}' but got '{actual}'"
    finally:
        # Change back to original directory and clean up temp dir
        os.chdir(original_cwd)
        temp_dir_obj.cleanup()


if __name__ == "__main__":
    test_git_remote_deps()
    test_git_local_clone_deps()
    print("All tests passed!")
