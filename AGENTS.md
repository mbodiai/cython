# Repository Guidelines

## Project Structure & Module Organization

- A custom fork of the Cython compiler with modernized code and optimizations and feature support beyond the upstream version.

## Build and Type-Check


## Coding Style & Naming Conventions

- Indent 4 spaces; line length 100.
- Prefer type hints on public APIs when practical; keep internal helpers lightweight.
- Naming: modules/functions `snake_case`; classes `PascalCase`; constants `UPPER_SNAKE_CASE`.
- Tools
  - Pyright using venv’s Python: `PY=.venv/bin/python; VER=$($PY -c 'import sys;print(f"{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}")'); pyright --pythonversion "$VER" Cython`.


- Activate venv: `source .venv/bin/activate` (pyright is configured with `venvPath = ".venv"`).
- Type-check with the venv interpreter (micro version supported): `PY=.venv/bin/python; VER=$($PY -c 'import sys; print(f"{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}")'); pyright --pythonversion "$VER" Cython`.

## Verification

- Type-check: `pyright --pythonversion "$VER" Cython` returns without errors of interest.

## Local Changes Overview (observed vs upstream/master)

- CI and repo config
  - Workflows updated in `.github/workflows/*`; removed `dependabot.yml`.
  - `.gitignore`, `.readthedocs.yaml` adjusted; `CHANGES.md` added.
  - `CMakePresets.json` added.

- Build, packaging, and CLI
  - `pyproject.toml`, `setup.cfg`, `setup.py` modified; `requirements*.txt` added.
  - New helpers: `cli.py`, `cmake_build_helper.py`, `configure_openmp.py`, `build_test.py`.
  - Distutils/build integrations updated (`Cython/Distutils/build_ext.py`, `Cython/Build/*`).

- Typing and stubs
  - `py.typed` added; `.pyi` stubs introduced/updated (e.g., `Cython/typings/__main__.pyi`, `stubs/__main__.pyi`).
  - Typing tests and tools added/updated (`Tools/test_typing.py`, `Tools/test_typing.py_typed.py`, `Cython/Compiler/test_typings`).

- Compiler internals
  - `Cython/Compiler/Pipeline.py`: added `TYPE_CHECKING` guard imports; cycle-safe utility-code sorting; light annotations.
  - New modules: `Cython/Compiler/DirectiveTypes.py`, `directive_options.py`, `oldoptions.py`.
  - Various updates across `Main.py`, `Options.py`, `MemoryView.py`, `Pythran.py`, `StringEncoding.py`, `Annotate.py`, `ModuleNode.py`, `Visitor.py`.

- Includes and runtime
  - Updates in `Cython/Includes/cpython/*` and `Cython/Includes/libc/*`.
  - Several `libcpp` concurrency pxds removed (e.g., `barrier.pxd`, `condition_variable.pxd`, `future.pxd`, `latch.pxd`, `semaphore.pxd`, `stop_token.pxd`); others adjusted (e.g., `shared_mutex.pxd`, `string_view.pxd`).
  - Runtime/utility C sources updated; new `Cython/Utility/Dataclasses.py`; removed `FusedFunction.pyx`, `TString.c`.

- Vendored tooling
  - Added `jedi/` package with supporting modules.

- Tests and demos
  - Numerous `tests/*` updates; several legacy `*.srctree` tests removed; new/updated `run/` and feature tests (e.g., `_cython_inline_*.pyx`, `test_stdlib.pyx`).
  - Demos/benchmarks pruned and refreshed.

- Misc
  - `bin/*` scripts updated; `cython.py`, `cythonize.py`, `cygdb.py` adjusted.
  - Repo docs refreshed (`README.rst`, docs config and examples).
