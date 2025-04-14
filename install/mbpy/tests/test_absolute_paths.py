import os
import tempfile
from pathlib import Path
import pytest
import asyncio

from mbpy.pkg.requirements import aget_requirements_file
from mbcore.traverse import asearch_parents_for_file


@pytest.mark.asyncio
async def test_absolute_path_handling():
    """Test that asearch_parents_for_file correctly handles absolute paths."""
    # Save current directory
    original_dir = os.getcwd()

    try:
        # Create a temporary directory structure
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_path = Path(temp_dir)

            # Create nested directories
            proj_dir = temp_path / "project"
            subdir = proj_dir / "subdir"
            subsubdir = subdir / "subsubdir"

            for dir_path in [proj_dir, subdir, subsubdir]:
                dir_path.mkdir(exist_ok=True)

            # Create a requirements.txt file in the project directory
            req_file = proj_dir / "requirements.txt"
            req_file.write_text("# Test requirements file")

            # Test 1: Call from the subsubdir with a non-absolute path
            os.chdir(subsubdir)
            result = await asearch_parents_for_file("requirements.txt")
            assert result.result is not None
            assert result.result.is_absolute(), f"Path should be absolute, got: {result}"
            assert Path(str(result.result)).resolve() == Path(str(req_file)).resolve()

            # Test 2: Call with an absolute path directly
            absolute_req_path = req_file.resolve()
            result = await asearch_parents_for_file(absolute_req_path)
            assert result.result is not None
            assert result.result.is_absolute(), f"Path should be absolute, got: {result}"
            assert Path(str(result.result)).resolve() == Path(str(absolute_req_path)).resolve()

            # Test 3: Test the integration with aget_requirements_file
            os.chdir(subdir)
            result = await aget_requirements_file()
            assert result.result is not None
            assert result.result.is_absolute(), f"Path should be absolute, got: {result}"
            assert result.result.exists(), f"Requirements file should exist: {result}"
            # It should either find the existing requirements.txt or create one in current dir
            assert Path(str(result.result)).resolve() in [
                Path(str(req_file)).resolve(),
                Path(str(subdir / "requirements.txt")).resolve(),
            ]
    finally:
        # Always restore original directory
        os.chdir(original_dir)


@pytest.mark.asyncio
async def test_directory_path_handling():
    """Test the behavior when passing a directory-like path."""
    # Save current directory
    original_dir = os.getcwd()

    try:
        # Create a temporary directory structure
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_path = Path(temp_dir)

            # Create a test file with a custom name
            custom_req = temp_path / "custom.txt"
            custom_req.write_text("# Custom requirements file")

            # Test with a path-like string - should extract 'path' as the filename
            os.chdir(temp_path)
            path_arg = "some/dir/path"
            result = await aget_requirements_file(path_arg)

            # It should either create or find a file named 'path'
            assert result.result is not None
            assert result.result.is_absolute(), f"Path should be absolute, got: {result}"
            assert result.result.name == "requirements.txt", (
                f"Filename should be 'requirements.txt', got: {result.result.name}"
            )
            assert result.result.exists(), f"File should exist: {result.result}"
    finally:
        # Always restore original directory
        os.chdir(original_dir)


@pytest.mark.asyncio
async def test_directory_object_handling():
    """Test the behavior when passing an actual directory Path object."""
    # Save current directory
    original_dir = os.getcwd()

    try:
        # Create a temporary directory structure
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_path = Path(temp_dir)

            # Create a subdirectory to use as the requirements argument
            req_dir = temp_path / "reqdir"
            req_dir.mkdir()

            # Test with an actual directory Path object - no need to change directories
            result = await aget_requirements_file(req_dir)

            # It should create requirements.txt IN the directory
            assert result.result is not None
            assert result.result.is_absolute(), f"Path should be absolute, got: {result}"
            assert result.result.name == "requirements.txt", (
                f"Filename should be 'requirements.txt', got: {result.result.name}"
            )
            # Compare the resolved paths to handle macOS symlinks (/var vs /private/var)
            assert (
                Path(str(result.result)).resolve()
                == Path(str(req_dir / "requirements.txt")).resolve()
            )
            assert result.result.exists(), f"File should exist: {result.result}"
    finally:
        # Always restore original directory
        os.chdir(original_dir)
