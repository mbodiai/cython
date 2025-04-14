import pytest
from pathlib import Path
import sys
import tempfile
import os


@pytest.mark.asyncio
async def test_all_dependency_formats():
    """Test all supported dependency formats."""
    from mbpy.pkg.dependency import Dependency
    from mbcore.traverse import has_error

    # A list of all supported formats to test
    formats = [
        # Package name
        {"input": "pytest", "expected_base": "pytest"},
        
        # Package name with version
        {"input": "pytest>=7.0.0", "expected_base": "pytest"},
        
        # Package with extras
        {"input": "pandas[excel,parquet]", "expected_base": "pandas", "expected_extras": ["excel", "parquet"]},
        
        # Editable path
        {"input": "-e /path/to/package", "expected_base": "/path/to/package", "expected_editable": True},
        
        # GitHub org/repo
        {"input": "org/repo", "expected_base": "repo", "expected_git": True},
        
        # Git URL
        {"input": "git+https://github.com/org/repo.git", "expected_base": "repo", "expected_git": True},
        
        # Git URL with branch
        {"input": "git+https://github.com/org/repo.git@branch", "expected_base": "repo", "expected_git": True, "expected_ref": "branch"},
        
        # Local path
        {"input": "./local/path", "expected_base": "./local/path"},
    ]
    
    for fmt in formats:
        print(f"Testing format: {fmt['input']}", file=sys.stderr)
        dep = Dependency(fmt["input"])
        
        # Test basic properties
        if "expected_base" in fmt:
            assert dep.base == fmt["expected_base"], f"Base mismatch for {fmt['input']}: expected {fmt['expected_base']}, got {dep.base}"
        
        # Test git flag if specified
        if "expected_git" in fmt:
            assert dep.git == fmt["expected_git"], f"Git flag mismatch for {fmt['input']}: expected {fmt['expected_git']}, got {dep.git}"
        
        # Test editable flag if specified
        if "expected_editable" in fmt:
            assert dep.editable == fmt["expected_editable"], f"Editable flag mismatch for {fmt['input']}: expected {fmt['expected_editable']}, got {dep.editable}"
        
        # Test extras if specified
        if "expected_extras" in fmt:
            assert set(dep.extras) == set(fmt["expected_extras"]), f"Extras mismatch for {fmt['input']}: expected {fmt['expected_extras']}, got {dep.extras}"
            
        # Test git ref if specified
        if "expected_ref" in fmt and hasattr(dep, 'git_ref'):
            assert dep.git_ref == fmt["expected_ref"], f"Git ref mismatch for {fmt['input']}: expected {fmt['expected_ref']}, got {dep.git_ref}"
        
        print(f"Successfully validated: {fmt['input']}", file=sys.stderr)


@pytest.mark.asyncio
async def test_dependency_from_requirements_file():
    """Test parsing packages from a temporary requirements.txt file."""
    from mbpy.pkg.dependency import Dependency
    from mbpy.pkg.requirements import aget_requirements_packages
    from mbcore.traverse import has_error
    
    # Create a temporary requirements.txt with multiple formats
    with tempfile.NamedTemporaryFile(suffix='.txt', delete=False) as tmp:
        content = """
pytest>=7.0.0
-e ./local/package
git+https://github.com/org/repo.git
org/repo
pandas[excel,parquet]
        """
        tmp.write(content.encode('utf-8'))
        tmp_path = tmp.name
    
    try:
        # Test with astype="deps"
        result = await aget_requirements_packages(astype="deps", requirements=tmp_path)
        if has_error(result):
            raise result.error
        deps = result.result
        
        # Verify we have the expected number of dependencies
        assert len(deps) == 5, f"Expected 5 dependencies, got {len(deps)}"
        
        # Verify each dependency has the correct properties
        for dep in deps:
            assert isinstance(dep, Dependency), f"Expected Dependency object, got {type(dep)}"
            
            # Verify editable flag for the local package
            if "./local/package" in str(dep):
                assert dep.editable, f"Expected editable=True for {dep}, got {dep.editable}"
            
            # Verify git flag for the git URL
            if "git+https://" in str(dep):
                assert dep.git, f"Expected git=True for {dep}, got {dep.git}"
            
            # Verify extras for pandas
            if "pandas" in str(dep):
                assert "excel" in dep.extras and "parquet" in dep.extras, f"Expected extras ['excel', 'parquet'] for {dep}, got {dep.extras}"
        
        # Test with astype="list"
        result = await aget_requirements_packages(astype="list", requirements=tmp_path)
        if has_error(result):
            raise result.error
        deps_list = result.result
        
        # Verify we have the expected number of dependencies as strings
        assert len(deps_list) == 5, f"Expected 5 dependencies, got {len(deps_list)}"
        assert all(isinstance(d, str) for d in deps_list), "Expected all items to be strings"
        
        # Test with astype="set"
        result = await aget_requirements_packages(astype="set", requirements=tmp_path)
        if has_error(result):
            raise result.error
        deps_set = result.result
        
        # Verify we have the expected number of dependencies as a set of strings
        assert len(deps_set) == 5, f"Expected 5 dependencies in set, got {len(deps_set)}"
        assert isinstance(deps_set, set), "Expected a set result"
        assert all(isinstance(d, str) for d in deps_set), "Expected all items in set to be strings"
    
    finally:
        # Clean up the temporary file
        os.unlink(tmp_path) 