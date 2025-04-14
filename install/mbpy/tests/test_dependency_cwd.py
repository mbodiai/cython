"""
Test the cwd parameter in Dependency operations.
"""

import asyncio
import os
import tempfile
from pathlib import Path
import sys

from mbpy.pkg.dependency import Dependency
from mbcore.ctx import chdir


async def test_dependency_with_cwd():
    """Test the cwd parameter in dependency operations."""
    # Create a temporary directory
    with tempfile.TemporaryDirectory() as temp_dir:
        temp_path = Path(temp_dir)

        # Create a basic pyproject.toml file
        pyproject_content = """
[project]
name = "test-project"
version = "0.1.0"
dependencies = []

[build-system]
requires = ["setuptools>=42", "wheel"]
build-backend = "setuptools.build_meta"
        """

        pyproject_path = temp_path / "pyproject.toml"
        pyproject_path.write_text(pyproject_content)

        # Save the current directory to compare later
        current_dir = Path.cwd()
        current_pyproject = current_dir / "pyproject.toml"
        current_content = None
        if current_pyproject.exists():
            current_content = current_pyproject.read_text()

        # Create a dependency and install it with cwd parameter
        dep = Dependency("pytest")
        print(f"Installing pytest in {temp_dir}...")
        with chdir(temp_path):
            await dep.install()

        # Read the modified file
        modified_content = pyproject_path.read_text()
        print(f"Modified content in temp dir:\n{modified_content}")

        # Check that the current directory's pyproject.toml hasn't changed
        if current_pyproject.exists():
            after_content = current_pyproject.read_text()
            if current_content == after_content:
                print("✅ Current directory's pyproject.toml was not modified")
            else:
                print("❌ Current directory's pyproject.toml was modified!")
                print(f"Before:\n{current_content}")
                print(f"After:\n{after_content}")

        # Now uninstall with cwd parameter
        print(f"Uninstalling pytest from {temp_dir}...")
        with chdir(temp_path):
            await dep.uninstall()

        # Read the modified file again
        uninstalled_content = pyproject_path.read_text()
        print(f"Content after uninstall:\n{uninstalled_content}")

        # Check that pytest was added and then removed
        success = (
            "pytest" in modified_content
            and "pytest" not in uninstalled_content
            and "dependencies = []" in uninstalled_content
        )

        print("✅ Test passed!" if success else "❌ Test failed!")
        return success


if __name__ == "__main__":
    success = asyncio.run(test_dependency_with_cwd())
    sys.exit(0 if success else 1)
