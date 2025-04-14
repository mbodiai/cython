# Tests for MB Project

This directory contains tests for various components of the MB project.

## Running Tests

To run the tests, use the following command from the project root:

```bash
python -m pytest tests
```

Or to run a specific test file:

```bash
python -m pytest tests/test_vendoring.py
```

## Vendoring Tests

The `test_vendoring.py` file contains tests for the vendoring functionality. These tests verify:

1. Path replacements (absolute to relative paths)
2. Creation of portable pyproject.toml files
3. Copying of dependencies to the vendored directory
4. Handling dependencies from multiple workspaces

### Requirements

The vendoring tests require:
- pytest
- tomlkit

If these dependencies are not installed, the test will attempt to install them automatically.

### Test Structure

The vendoring tests use temporary directories to create mock workspaces with development dependencies. This ensures the tests can be run without modifying your actual codebase.

Each test sets up a different scenario to verify different aspects of the vendoring process:

- `test_replace_file_path`: Tests conversion of file:/// paths to git URLs
- `test_replace_abs_path`: Tests conversion of absolute paths to relative paths
- `test_create_portable_pyproject`: Tests creation of a portable pyproject.toml file
- `test_ensure_vendored`: Tests copying of dependencies to the vendored directory
- `test_ensure_vendored_no_update_needed`: Tests skipping vendoring when no updates are needed
- `test_multiple_workspace_handling`: Tests handling dependencies across multiple workspaces 