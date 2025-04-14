#!/usr/bin/env python3
"""
Debug test for cwd parameter tracing.
"""

import asyncio
import os
import tempfile
from pathlib import Path
import sys
from contextlib import chdir

from mbpy.pkg.dependency import Dependency


async def test_dependency_with_cwd_debug():
    """Test the cwd parameter with debugging."""
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

        print(f"[DEBUG START] Created test pyproject.toml at {pyproject_path}")
        print(f"[DEBUG START] Current dir: {Path.cwd()}")

        # Add a patch to the modify_dependencies function to print cwd
        from mbpy.pkg.mpip import modify_dependencies

        original_modify_dependencies = modify_dependencies

        async def debug_modify_dependencies(*args, **kwargs):
            print(
                f"[DEBUG MIDPOINT 1] modify_dependencies called with cwd={kwargs.get('cwd')}"
            )
            result = await original_modify_dependencies(*args, **kwargs)
            print(
                f"[DEBUG MIDPOINT 1] modify_dependencies returned with cwd={kwargs.get('cwd')}"
            )
            return result

        # Patch the function
        import mbpy.pkg.mpip

        mbpy.pkg.mpip.modify_dependencies = debug_modify_dependencies

        # Also patch the resolve_conflicting function to see what's happening
        from mbpy.pkg.toml import resolve_conflicting

        original_resolve_conflicting = resolve_conflicting

        def debug_resolve_conflicting(primary, alternate=None):
            print(
                f"[DEBUG MIDPOINT 2] resolve_conflicting called with primary={primary}, alternate={alternate}"
            )
            result = original_resolve_conflicting(primary, alternate)
            print(f"[DEBUG MIDPOINT 2] resolve_conflicting returned {result}")
            return result

        # Patch the function
        import mbpy.pkg.toml

        mbpy.pkg.toml.resolve_conflicting = debug_resolve_conflicting

        # Create a dependency and install it with the cwd parameter
        dep = Dependency("pytest")
        print(f"[DEBUG BEFORE INSTALL] Installing pytest with cwd={temp_path}")
        try:
            with chdir(temp_path):
                await dep.install()
        except Exception as e:
            print(f"[DEBUG ERROR] Install failed: {e}")
            raise
        print("[DEBUG AFTER INSTALL] Installation complete")

        # Check both pyproject.toml files
        modified_content = pyproject_path.read_text()
        print(f"[DEBUG END] Temp pyproject.toml content:\n{modified_content}")

        current_pyproject = Path.cwd() / "pyproject.toml"
        if current_pyproject.exists():
            current_content = current_pyproject.read_text()
            print(f"[DEBUG END] Current dir pyproject.toml content head:")
            print(current_content.split("\n")[:5])

        # Unpatch the functions
        mbpy.pkg.mpip.modify_dependencies = original_modify_dependencies
        mbpy.pkg.toml.resolve_conflicting = original_resolve_conflicting


if __name__ == "__main__":
    asyncio.run(test_dependency_with_cwd_debug())
