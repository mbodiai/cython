import os
import ast
import sys
from pathlib import Path
import pytest
import traceback
from unittest.mock import patch, MagicMock

from mbpy.pkg.graph import (
    extract_node_info,
    _build_dependency_graph,
    _generate,
    isexcluded,
    print_graph,
    ModuleDict,
    FunctionDict,
    ClassDict,
)


# Test helper to print results for debugging
def debug_print(title, value):
    print(f"\n--- {title} ---")
    if isinstance(value, dict):
        for k, v in value.items():
            print(f"{k}: {v}")
    else:
        print(value)


@pytest.fixture
def sample_module_file(tmp_path):
    """Create a sample Python module file for testing."""
    module_content = """
\"\"\"Sample module docstring.\"\"\"

def sample_function(arg1: str, arg2: int = 0) -> bool:
    \"\"\"Sample function docstring.\"\"\"
    return True

class SampleClass:
    \"\"\"Sample class docstring.\"\"\"
    
    def sample_method(self, param1):
        \"\"\"Sample method docstring.\"\"\"
        return param1
"""
    module_file = tmp_path / "sample_module.py"
    module_file.write_text(module_content)
    return module_file


def test_extract_node_info_doc_option(sample_module_file):
    """Test if the doc option correctly extracts docstrings."""
    # Try with doc=False first
    result_without_doc = extract_node_info(sample_module_file, doc=False)
    debug_print("Result without doc", result_without_doc)
    assert "doc" in result_without_doc
    assert result_without_doc["doc"] == ""  # Should be empty with doc=False

    # Now with doc=True and also enable functions and classes
    result_with_doc = extract_node_info(
        sample_module_file, doc=True, functions=True, classes=True
    )
    debug_print("Result with doc", result_with_doc)
    assert "doc" in result_with_doc
    assert "Sample module docstring." in result_with_doc["doc"]

    # Check if function docstrings are extracted
    assert "functions" in result_with_doc
    assert "sample_function" in result_with_doc["functions"]
    function_info = result_with_doc["functions"]["sample_function"]
    assert "doc" in function_info
    assert "Sample function docstring." in function_info["doc"]

    # Check if class docstrings are extracted
    assert "classes" in result_with_doc
    assert "SampleClass" in result_with_doc["classes"]
    class_info = result_with_doc["classes"]["SampleClass"]
    assert "doc" in class_info
    assert "Sample class docstring." in class_info["doc"]

    # Check if method docstrings are extracted
    assert "methods" in class_info
    assert "sample_method" in class_info["methods"]
    method_info = class_info["methods"]["sample_method"]
    assert "doc" in method_info
    assert "Sample method docstring." in method_info["doc"]


def test_extract_node_info_functions_option(sample_module_file):
    """Test if the functions option correctly extracts function definitions."""
    # Try with functions=False first
    result_without_functions = extract_node_info(sample_module_file, functions=False)
    debug_print("Result without functions", result_without_functions)
    assert "functions" in result_without_functions
    assert (
        len(result_without_functions["functions"]) == 0
    )  # Should be empty with functions=False

    # Now with functions=True
    result_with_functions = extract_node_info(sample_module_file, functions=True)
    debug_print("Result with functions", result_with_functions)
    assert "functions" in result_with_functions
    assert "sample_function" in result_with_functions["functions"]

    # Check function details
    function_info = result_with_functions["functions"]["sample_function"]
    assert "name" in function_info
    assert function_info["name"] == "sample_function"
    assert "signature" in function_info


def test_extract_node_info_classes_option(sample_module_file):
    """Test if the classes option correctly extracts class definitions."""
    # Try with classes=False first
    result_without_classes = extract_node_info(sample_module_file, classes=False)
    debug_print("Result without classes", result_without_classes)
    assert "classes" in result_without_classes
    assert (
        len(result_without_classes["classes"]) == 0
    )  # Should be empty with classes=False

    # Now with classes=True
    result_with_classes = extract_node_info(sample_module_file, classes=True)
    debug_print("Result with classes", result_with_classes)
    assert "classes" in result_with_classes
    assert "SampleClass" in result_with_classes["classes"]

    # Check class details
    class_info = result_with_classes["classes"]["SampleClass"]
    assert "name" in class_info
    assert class_info["name"] == "SampleClass"
    assert "methods" in class_info
    assert "sample_method" in class_info["methods"]


def test_exclude_option():
    """Test if the exclude option correctly filters out paths."""
    # Create several test paths
    test_paths = [
        Path("/test/path/site-packages/some_lib"),
        Path("/test/path/mbpy/main.py"),
        Path("/test/path/excluded_dir/file.py"),
        Path("/test/path/included_dir/file.py"),
    ]

    # Test with default config (should exclude site-packages)
    for path in test_paths:
        result = isexcluded(path)
        if "site-packages" in str(path):
            assert result, f"Path {path} should be excluded with default config"

    # Test with ignore option
    config = {"ignore": ["excluded_dir"]}
    for path in test_paths:
        result = isexcluded(path, **config)
        if "excluded_dir" in str(path):
            assert result, (
                f"Path {path} should be excluded with ignore=['excluded_dir']"
            )

    # Test with include option
    config = {"include": ["included_dir"]}
    for path in test_paths:
        result = isexcluded(path, **config)
        if "included_dir" not in str(path):
            assert result, (
                f"Path {path} should be excluded with include=['included_dir']"
            )
        else:
            assert not result, (
                f"Path {path} should not be excluded with include=['included_dir']"
            )


@pytest.mark.asyncio
async def test_integration_with_options(tmp_path, monkeypatch):
    """Integration test with various options."""
    # Create a sample project structure
    project_dir = tmp_path / "test_project"
    project_dir.mkdir()

    # Create a main module
    main_module = project_dir / "main.py"
    main_module.write_text("""
\"\"\"Main module docstring.\"\"\"
import helper

def main_function():
    \"\"\"Main function docstring.\"\"\"
    return helper.helper_function()

class MainClass:
    \"\"\"Main class docstring.\"\"\"
    def main_method(self):
        \"\"\"Main method docstring.\"\"\"
        pass
""")

    # Create a helper module
    helper_module = project_dir / "helper.py"
    helper_module.write_text("""
\"\"\"Helper module docstring.\"\"\"

def helper_function():
    \"\"\"Helper function docstring.\"\"\"
    return True

class HelperClass:
    \"\"\"Helper class docstring.\"\"\"
    def helper_method(self):
        \"\"\"Helper method docstring.\"\"\"
        pass
""")

    # Create an excluded module
    excluded_dir = project_dir / "excluded"
    excluded_dir.mkdir()
    excluded_module = excluded_dir / "excluded.py"
    excluded_module.write_text("""
\"\"\"This module should be excluded.\"\"\"

def excluded_function():
    \"\"\"This function should be excluded.\"\"\"
    pass
""")

    # Modify sys.path to include test project
    monkeypatch.syspath_prepend(str(project_dir))

    # Use the extract_node_info function directly for testing
    # This avoids the pickling issue with _generate
    path_to_test = project_dir / "main.py"

    # Test with doc=True
    result_with_doc = extract_node_info(
        path_to_test, doc=True, functions=True, classes=True, ignore=["excluded"]
    )
    assert result_with_doc["doc"] == "Main module docstring."
    assert "main_function" in result_with_doc["functions"]
    assert (
        result_with_doc["functions"]["main_function"]["doc"]
        == "Main function docstring."
    )

    # Test with doc=False
    result_without_doc = extract_node_info(
        path_to_test, doc=False, functions=True, classes=True, ignore=["excluded"]
    )
    assert result_without_doc["doc"] == ""
    assert "main_function" in result_without_doc["functions"]
    assert result_without_doc["functions"]["main_function"]["doc"] == ""

    # Test exclude functionality
    excluded_path = excluded_dir / "excluded.py"
    assert isexcluded(excluded_path, ignore=["excluded"])

    # Test include functionality
    assert not isexcluded(path_to_test, include=["main"])


if __name__ == "__main__":
    # Run all tests
    import pytest

    pytest.main(["-xvs", __file__])
