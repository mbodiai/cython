# Cython TypedDict and Type Annotation Issues

<details><summary><h2>Current Problems</h2></summary>

1. **`pip install -e .` Failure:**
   - The local Cython package fails to build and install in editable mode.
   - Errors include `Cython.pxd not found` and various C/C++ compilation errors (e.g., `Assignment to non-lvalue` previously, other linking/compilation issues).
   - Reverting files (`setup.py`, `Code.py`) and cleaning directories (`typings`, `install`) has not resolved the core issue.

2. **Cython/Compiler/Options.py**:
   - Issues with TypedDict compatibility across Python versions
   - Dynamic key assignment in TypedDict causing linter errors
   - Return type mismatches with empty dictionaries vs TypedDict

3. **Cython/Shadow.py**:
   - Missing `_Optimization` class which caused runtime errors
   - TypeVar import issues
   - Attribute errors in `_Optimization` and other classes
   - Module type compatibility issues with the module registration

4. **Running stdlib.pxd**:
   - Cannot properly compile/run stdlib.pxd due to issues in the core modules
   - Cascading errors when trying different compilation approaches
</details>

<details><summary><h2>Attempted Fixes</h2></summary>

1. Replaced TypedDict with regular dict subclasses:
   ```python
   # Before:
   class DirectiveScopeKwargs(DirectiveScopeDict, total=False):
       """TypedDict for directive scopes with optional fields."""
       
   # After:
   class DirectiveScopeKwargs(DirectiveScopeDict):
       """Dict for directive scopes with optional fields."""
   ```

2. Added `_Optimization` class to Shadow.py:
   ```python
   class _Optimization:
       """Empty class used for optimization attributes."""
       def __call__(self, *args, **kwargs):
           return _EmptyDecoratorAndManager()
       
       def __getattr__(self, name):
           return lambda arg: _EmptyDecoratorAndManager()
   ```

3. Fixed TypeVar imports:
   ```python
   try:
       from typing import TypeVar
   except ImportError:
       TypeVar = lambda name: None
   ```
</details>

<details><summary><h2>Todo Items</h2></summary>

1. **Resolve `pip install -e .` Build Failure:**
   - Investigate the root cause of the `Cython.pxd not found` and C compilation errors.
   - Determine if the issue lies in `setup.py`, environment configuration, build tool versions, or source code interactions.

2. **Complete `Cython/Compiler/CmdLine.py` Refactor:**
   - Successfully replace the old command-line parsing with the new `click`-based structure.
   - Integrate with the Pydantic models in `Cython/Compiler/Options.py`.
   - Resolve issues with applying large edits via the `edit_file` tool.

3. Fix remaining lint errors in Shadow.py:
   - Add proper type annotations for classes that have missing attributes
   - Fix `ModuleType` compatibility issues with custom module classes

4. Fix parsing of compiler directives with dynamic keys
   - Currently using `# type: ignore` which is not ideal

5. Complete the proper TypedDict setup for Python 3.8+ compatibility
   - Ensure conditional typing imports work correctly
   - Create proper typing hierarchy

6. Test the stdlib.pxd compilation after all fixes

7. Add compatibility for py.typed annotation in the package

8. Review and enhance type definitions for better IDE support
</details>

<details><summary><h2>mbcore Build System Improvements</h2>

<h3>Learnings from mbcore/src/mbcore/build.py Refactoring:</h3>
</summary>

<details><summary><h3>compile_executable (macOS)</h3></summary>

- Removed hardcoded `libpython3.12.dylib` path.
- Dynamically used the `PYTHON_LIBRARY` variable for paths.
- Constructed `clang++` and `install_name_tool` commands as lists for safer `subprocess.run(..., shell=False)` execution.
- Made `install_name_tool` logic more robust by attempting fixes for multiple potential original references (`@rpath/...`, `lib/...`).
- Added verification steps using `otool -L` to check library linkage after compilation and fixing.
</details>

<details><summary><h3>main Function Refactoring</h3></summary>

- Improved overall readability and logic flow.
- Made `pyproject.toml` loading more robust, handling missing keys gracefully.
- Refined source directory (`src_dir`) detection, prioritizing `pyproject.toml`, then CLI args, then defaults.
- Clarified module path resolution logic to handle:
  - Absolute/relative file paths.
  - Module names (e.g., `pkg.mod`) relative to `src_dir`.
- Improved file globbing (`glob.glob`) and filtering (ignore/include patterns, standard excludes).
- Ensured consistent use of `pathlib.Path` objects for path manipulations.
</details>

<details><summary><h3>Linter Fixes & Type Hinting</h3></summary>

- Handled potential `None` return from `package.__file__` using `getattr`.
- Corrected type hints for multiprocessing (`multiprocessing.Pool.map`).
- Updated function signatures (e.g., `setup_paths`) to accept `Iterable` instead of just `list` for flexibility.
- Added necessary imports (`glob`, placeholder for `_build_dependency_graph`).
- Resolved type errors related to `Path` object operations.
</details>

<details><summary><h3>TODO Items</h3></summary>

1. Fix the missing import for `_build_dependency_graph` - determine its actual location in the project.
2. Add explicit `import glob` at the top of the file.
3. Consider making the `excluded_dirs` list configurable via `pyproject.toml`.
4. Add more comprehensive error handling in the compilation process.
5. Create tests to verify the library linking works correctly across platforms.
6. Document the expected structure of `pyproject.toml` for `[tool.mb]` configuration.
</details>
</details> 