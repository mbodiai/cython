#!/usr/bin/env python3
"""
Test that we can install different dependencies in different directories.
"""

import asyncio
import tempfile
from pathlib import Path

from mbpy.pkg.dependency import Dependency
from mbcore.ctx import chdir


async def test_multi_directory_installs():
    """Test installing different dependencies in different directories."""
    # Create two temporary directories
    with (
        tempfile.TemporaryDirectory() as temp_dir1,
        tempfile.TemporaryDirectory() as temp_dir2,
    ):
        temp_path1 = Path(temp_dir1)
        temp_path2 = Path(temp_dir2)

        # Create basic pyproject.toml files in both directories
        pyproject_content = """
[project]
name = "test-project"
version = "0.1.0"
dependencies = []

[build-system]
requires = ["setuptools>=42", "wheel"]
build-backend = "setuptools.build_meta"
        """

        (temp_path1 / "pyproject.toml").write_text(pyproject_content)
        (temp_path2 / "pyproject.toml").write_text(pyproject_content)

        print(f"Created test directories:\n- {temp_path1}\n- {temp_path2}")

        # Install different dependencies in different directories
        dep1 = Dependency("pytest")
        dep2 = Dependency("rich")

        print(f"Installing pytest in {temp_path1}...")
        with chdir(temp_path1):
            await dep1.install()

        print(f"Installing rich in {temp_path2}...")
        with chdir(temp_path2):
            await dep2.install()

        # Read the modified files
        content1 = (temp_path1 / "pyproject.toml").read_text()
        content2 = (temp_path2 / "pyproject.toml").read_text()

        print(f"\nDirectory 1 content:\n{content1}")
        print(f"\nDirectory 2 content:\n{content2}")

        # Verify that each directory has the correct dependency
        success = (
            "pytest" in content1
            and "pytest" not in content2
            and "rich" in content2
            and "rich" not in content1
        )

        print("✅ Test passed!" if success else "❌ Test failed!")
        return success


if __name__ == "__main__":
    asyncio.run(test_multi_directory_installs())
