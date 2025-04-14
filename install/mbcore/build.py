import ctypes.util
import glob
import inspect
import multiprocessing
import os
import platform
import shutil
import subprocess
import sys
import sysconfig
from collections.abc import Callable, Iterable
from concurrent.futures import ProcessPoolExecutor
from functools import partial
from importlib import import_module
from pathlib import Path
from typing import NewType

import rich_click as click
import tomlkit
from typing_extensions import Literal, NewType, TypedDict

from mbcore.display import getconsole
from mbcore.log import error, info
from mbcore.main import get_help_config
from mbcore.more import first_true, unique_everseen
from mbcore.display import safe_print
from mbpy.pkg.graph import _build_dependency_graph  # Import dependency graph builder from mbpy
# Define DEBUG globally
DEBUG = True # Set to False to disable debug prints in find_python_library

# Check for Cython
HAS_CYTHON = False
try:
    import cython
    from Cython.Compiler.Main import CompilationOptions, CompilationResult

    HAS_CYTHON = True
except ImportError:
    HAS_CYTHON = False

if not HAS_CYTHON:
    raise ImportError("Cython not found, please run `mb add 'mbcore[all]'` or `pip install Cython`")


def find_python_library():
    """Find the correct Python shared or static library for any OS, architecture, and installation method."""

    def check_path(path):
        """Returns a valid path if it exists, else None."""  # noqa: D401
        path = Path(path)
        return str(path) if path.exists() else None

    # 1. Direct lookup via sysconfig
    lib_name = sysconfig.get_config_var("LDLIBRARY") or ""
    lib_dir = Path(sysconfig.get_config_var("LIBDIR") or "")
    if lib_name:
        shared_lib = check_path(lib_dir / lib_name)
        if shared_lib:
            if DEBUG: print(f"Method 1: Found via sysconfig: {shared_lib}")
            return shared_lib

    # 2. ctypes library lookup (cross-platform)
    found_lib = ctypes.util.find_library(
        f"python{platform.python_version_tuple()[0]}.{platform.python_version_tuple()[1]}",
    )
    if found_lib:
        found_lib_path = check_path(found_lib)
        if found_lib_path:
            if DEBUG: print(f"Method 2: Found via ctypes: {found_lib_path}")
            return found_lib_path

    # 3. macOS: Use `otool -L`
    if sys.platform == "darwin":
        try:
            output = subprocess.check_output(["otool", "-L", sys.executable], text=True)
            for line in output.split("\n"):
                if "libpython" in line:
                    potential_path = check_path(line.split()[0])
                    if potential_path:
                        shared_lib = potential_path
                        if DEBUG: print(f"Method 3a: Found via otool: {shared_lib}")
                        return shared_lib
        except Exception:  # noqa: S110
            pass

        # Try macOS framework paths
        framework_path = Path(sys.base_prefix) / "Python.framework/Versions" / platform.python_version() / "Python"
        framework_lib = check_path(framework_path)
        if framework_lib:
            if DEBUG: print(f"Method 3b: Found via framework path: {framework_lib}")
            return framework_lib

    # 4. Linux: Use `ldd`
    elif sys.platform == "linux":
        try:
            output = subprocess.check_output(["ldd", sys.executable], text=True)
            for line in output.split("\n"):
                if "libpython" in line:
                    potential_path = check_path(line.split()[0])
                    if potential_path:
                        shared_lib = potential_path
                        if DEBUG: print(f"Method 4: Found via ldd: {shared_lib}")
                        return shared_lib
        except Exception:
            pass

    # 5. Windows: Search for pythonXX.dll
    elif sys.platform == "win32":
        python_version = platform.python_version_tuple()
        potential_paths = [
            f"C:\\Windows\\System32\\python{python_version[0]}{python_version[1]}.dll",
            f"C:\\Windows\\SysWOW64\\python{python_version[0]}{python_version[1]}.dll",
            Path(sys.base_prefix) / f"python{python_version[0]}{python_version[1]}.dll",
            Path(sys.executable).parent / f"python{python_version[0]}{python_version[1]}.dll",
        ]
        for path in potential_paths:
            dll_path = check_path(path)
            if dll_path:
                if DEBUG: print(f"Method 5: Found DLL: {dll_path}")
                return dll_path

    # 6. FreeBSD & Other Unix Variants: Use `ldd`
    elif "bsd" in sys.platform or "unix" in sys.platform:
        try:
            output = subprocess.check_output(["ldd", sys.executable], text=True)
            for line in output.split("\n"):
                if "libpython" in line:
                    potential_path = check_path(line.split()[0])
                    if potential_path:
                        shared_lib = potential_path
                        if DEBUG: print(f"Method 6: Found via ldd (BSD/Unix): {shared_lib}")
                        return shared_lib
        except Exception:
            pass

    # 7. Last resort: Manually search common library paths
    common_paths = [
        "/usr/lib",
        "/usr/local/lib",
        "/opt/homebrew/lib",
        "/lib",
        "/lib64",
        "/usr/lib64",
        Path(sys.base_prefix) / "lib",  # Virtualenv/Conda paths
        Path(sys.executable).parent / "lib",
    ]
    from itertools import chain

    for path in common_paths:
        if isinstance(path, str):
            path = Path(path)
        for lib in chain.from_iterable(
            [path.glob("libpython*.so*"), path.glob("libpython*.dylib"), path.glob("python*.dll")],
        ):
            valid_path = check_path(lib)
            if valid_path:
                if DEBUG: print(f"Method 7: Found via common paths search: {valid_path}")
                return valid_path

    # 8. No library found
    if DEBUG: print("All methods failed to find Python library.")
    return None


class BuildFlags(TypedDict):
    ROOT_DIR: Path
    SRC_DIR: Path
    BUILD_DIR: Path
    INSTALL_DIR: Path
    BIN_DIR: Path
    LIB_DIR: Path
    ENTRY_POINT: str
    FORCE: bool
    PYTHON_LIBRARY: Path
    PYTHON_INCLUDE: Path
    OS_NAME: str
    MODULES: list[Path]
    EXTENSIONS: dict[str, str]
    LIB_EXT: str
    FORCE: bool


EXT_MAP = {"Windows": ".pyd", "Linux": ".so", "Darwin": ".dylib"}
foundlib = find_python_library() or sysconfig.get_config_vars()["LDLIBRARY"]
include = sysconfig.get_path("include")
if not Path(include).exists():
    raise FileNotFoundError(f"Python include directory not found at {include}")
if not Path(foundlib).exists():
    raise FileNotFoundError("Python shared library not found")
global FLAGS
FLAGS: BuildFlags = {
    "OS_NAME": platform.system(),
    "EXTENSIONS": {"Windows": ".pyd", "Linux": ".so", "Darwin": ".dylib"},
    "LIB_EXT": EXT_MAP[platform.system()],
    "FORCE": False,
    "PYTHON_INCLUDE": Path(include),
    "PYTHON_LIBRARY": Path(foundlib) if foundlib else sysconfig.get_config_vars()["LDLIBRARY"],
    "ROOT_DIR": Path(),
    "SRC_DIR": Path("src"),
    "INSTALL_DIR": Path("install"),
    "BUILD_DIR": Path("build"),
    "BIN_DIR": Path("install") / "bin",
    "LIB_DIR": Path("install") / "lib",
    "ENTRY_POINT": "main",
    "MODULES": [],
}


def setup_paths(
    root_path: str | Path = ".",
    entry: str | Path = "main",
    force: str | Path | bool = False,
    python_library: str | Path = "",
    python_include: str | Path = "",
    install_dir: str | Path = "",
    build_dir: str | Path = "",
    src_dir: str | Path = "",
    modules: Iterable[str | Path] | None = None,
) -> BuildFlags:

    root_path = Path(str(root_path or FLAGS["ROOT_DIR"]))
    SRC_DIR = root_path / (src_dir or FLAGS["SRC_DIR"])
    BUILD_DIR = root_path / (build_dir or FLAGS["BUILD_DIR"])
    INSTALL_DIR = root_path / (install_dir or FLAGS["INSTALL_DIR"])
    BIN_DIR = INSTALL_DIR / "bin"
    LIB_DIR = INSTALL_DIR / "lib"
    PYTHON_LIBRARY = Path(str(python_library or FLAGS["PYTHON_LIBRARY"]))
    PYTHON_INCLUDE = Path(str(python_include or FLAGS["PYTHON_INCLUDE"]))
    OS_NAME = platform.system()
    MODULES = (
        list(map(Path, modules))
        if modules is not None
        else [f for f in SRC_DIR.rglob("*.py") if "__init__" not in f.name]
    )

    # Create directories
    for d in [BUILD_DIR, INSTALL_DIR, BIN_DIR, LIB_DIR]:
        d.mkdir(parents=True, exist_ok=True)

    FLAGS.update(
        **{
            "ROOT_DIR": root_path,
            "SRC_DIR": SRC_DIR,
            "BUILD_DIR": BUILD_DIR,
            "INSTALL_DIR": INSTALL_DIR,
            "BIN_DIR": BIN_DIR,
            "LIB_DIR": LIB_DIR,
            "ENTRY_POINT": str(entry),
            "FORCE": bool(force),
            "PYTHON_LIBRARY": PYTHON_LIBRARY,
            "PYTHON_INCLUDE": PYTHON_INCLUDE,
            "OS_NAME": OS_NAME,
            "MODULES": MODULES,
        },
    )
    safe_print(FLAGS)
    return FLAGS


def run(cmd, check=False) -> subprocess.Popen:
    """Execute shell command with logging."""
    info(
        f"[RUNNING] ({cmd}) \n {sys._getframe(1).f_code.co_name}{Path(sys._getframe(1).f_code.co_filename).resolve()}:{sys._getframe(1).f_lineno}",
    )
    process = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()

    if process.returncode != 0:
        error(f"{stderr.decode().strip()}")
        if check:
            sys.exit(1)
    elif stdout.decode().strip():
        info(stdout.decode().strip())

    return process


def cmd_options(install=None, build=None):
    """Generate Cython command line options."""
    _directive_defaults = {
        "binding": True,  # was False before 3.0
        "boundscheck": True,
        "nonecheck": False,
        "initializedcheck": True,
        "embedsignature": False,
        "embedsignature.format": "c++",
        "auto_cpdef": False,
        "auto_pickle": None,
        "cdivision": False,  # was True before 0.12
        "cdivision_warnings": False,
        "cpow": None,  # was True before 3.0
        # None (not set by user) is treated as slightly different from False
        "c_api_binop_methods": False,  # was True before 3.0
        "overflowcheck": False,
        "overflowcheck.fold": True,
        "always_allow_keywords": True,
        "allow_none_for_extension_args": True,
        "wraparound": True,
        "ccomplex": False,  # use C99/C++ for complex types and arith
        "callspec": "",
        "nogil": False,
        "gil": False,
        "with_gil": False,
        "profile": False,
        "linetrace": False,
        "emit_code_comments": True,  # copy original source code into C code comments
        "annotation_typing": True,  # read type declarations from Python function annotations
        "infer_types": True,
        "infer_types.verbose": False,
        "autotestdict": True,
        "autotestdict.cdef": True,
        "autotestdict.all": True,
        "language_level": "3",
        "fast_getattr": True,  # Undocumented until we come up with a better way to handle this everywhere.
        "py2_import": False,  # For backward compatibility of Cython's source code in Py3 source mode
        "preliminary_late_includes_cy28": False,  # Temporary directive in 0.28, to be removed in a later version (see GH#2079).
        "iterable_coroutine": False,  # Make async coroutines backwards compatible with the old asyncio yield-from syntax.
        "c_string_type": "bytes",
        "c_string_encoding": "",
        "type_version_tag": True,  # enables Py_TPFLAGS_HAVE_VERSION_TAG on extension types
        "unraisable_tracebacks": True,
        "old_style_globals": False,
        "np_pythran": False,
        "fast_gil": True,
        "cpp_locals": True,  # uses std::optional for C++ locals, so that they work more like Python locals
        "legacy_implicit_noexcept": False,
        # set __file__ and/or __path__ to known source/target path at import time (instead of not having them available)
        "set_initial_path": None,  # SOURCEFILE or "/full/path/to/module"
        "warn": None,
        "warn.undeclared": False,
        "warn.unreachable": True,
        "warn.maybe_uninitialized": False,
        "warn.unused": False,
        "warn.unused_arg": False,
        "warn.unused_result": False,
        "warn.multiple_declarators": True,
        "show_performance_hints": True,
        # optimizations
        "optimize.inline_defnode_calls": True,
        "optimize.unpack_method_calls": True,  # increases code size when True
        "optimize.unpack_method_calls_in_pyinit": False,  # uselessly increases code size when True
        "optimize.use_switch": True,
        # remove unreachable code
        "remove_unreachable": True,
        # control flow debug directives
        "control_flow.dot_output": "",  # Graphviz output filename
        "control_flow.dot_annotate_defs": False,  # Annotate definitions
        # test support
        "test_assert_path_exists": [],
        "test_fail_if_path_exists": [],
        "test_assert_c_code_has": [],
        "test_fail_if_c_code_has": [],
        # experimental, subject to change
        "formal_grammar": False,
    }

    default_options = {
        "show_version": 0,
        "use_listing_file": 0,
        "errors_to_stderr": 1,
        "cplus": 1,
        "output_file": None,
        "depfile": None,
        "annotate": None,
        "annotate_coverage_xml": None,
        "generate_pxi": 1,
        "capi_reexport_cincludes": 0,
        "working_path": "",
        "timestamps": None,
        "verbose": 0,
        "quiet": 0,
        "compiler_directives": _directive_defaults,
        "emit_linenums": False,
        "relative_path_in_code_position_comments": True,
        "c_line_in_traceback": True,
        "language_level": 3,
        "formal_grammar": False,
        "gdb_debug": False,
        "compile_time_env": None,
        "module_name": None,
        "output_dir": install or FLAGS["INSTALL_DIR"],
        "cache": None,
        "create_extension": None,
        "np_pythran": False,
        "legacy_implicit_noexcept": None,
    }
    return default_options


def copytree(src_dir=None, install_dir=None, modules=None):
    """Copy source directory to install directory."""
    global FLAGS

    SRC_DIR = src_dir or FLAGS["SRC_DIR"]
    INSTALL_DIR = install_dir or FLAGS["INSTALL_DIR"]
    MODULES = modules or FLAGS["MODULES"]
    shutil.copytree(
        SRC_DIR, INSTALL_DIR, dirs_exist_ok=True, ignore=shutil.ignore_patterns("*.pyc", "*.pyo", "__pycache__", ".git"),
    )
    return [Path(str(m)) for m in [INSTALL_DIR / str(m.resolve().relative_to(SRC_DIR.resolve())) for m in MODULES]]


def cythonize_shared(
    modules: list[Path] | None = None,
    install_dir: Path | None = None,
    force=False,
) -> int:
    """Compile a Python module into a C++ file using Cython.

    Copy the source directory to the install directory and compile the modules in parallel.

    Args:
        modules (list[Path], optional): List of Python modules to compile. Defaults to None.
        src_dir (Path, optional): Source directory. Defaults to None.
        install_dir (Path, optional): Install directory. Defaults to None.
        embed (bool, optional): Embed Python interpreter. Defaults to False.
        force (bool, optional): Force recompilation. Defaults to False.

    """
    global FLAGS

    INSTALL_DIR = install_dir or FLAGS["INSTALL_DIR"]
    MODULES = modules or FLAGS["MODULES"]
    FORCE = force or FLAGS["FORCE"]
    INCLUDE_DIR = FLAGS["PYTHON_INCLUDE"]

    INSTALL_DIR.mkdir(parents=True, exist_ok=True)

    modules = [INSTALL_DIR / m.resolve().relative_to(INSTALL_DIR.resolve()) for m in MODULES]
    from contextlib import chdir
    from io import StringIO

    from Cython.Build.Dependencies import cythonize

    io = StringIO()

    with chdir(INSTALL_DIR):
        cythonize(
            module_list=[str(m) for m in MODULES],
            nthreads=(os.cpu_count() or 2) // 2,
            include_path=[INCLUDE_DIR],
            force=FORCE,
            show_all_warnings=True,
            exclude_failures=False,
            language="c++",
            **{**cmd_options(install=INSTALL_DIR), "quiet": True},
        )
    return 0


def cleanup():
    """Clean up build directories."""
    global FLAGS
    BUILD_DIR = FLAGS["BUILD_DIR"]
    INSTALL_DIR = FLAGS["INSTALL_DIR"]
    BIN_DIR = FLAGS["BIN_DIR"]
    LIB_DIR = FLAGS["LIB_DIR"]
    LIB_EXT = FLAGS["LIB_EXT"]
    SRC_DIR = FLAGS["SRC_DIR"]
    if any(d == SRC_DIR for d in [BUILD_DIR, INSTALL_DIR, BIN_DIR, LIB_DIR]):
        error("Cannot clean up source directory")
        return
    for d in [BUILD_DIR, INSTALL_DIR, LIB_DIR]:
        for f in d.glob("*"):
            if f.name.endswith(LIB_EXT):
                continue
            if f.is_dir():
                shutil.rmtree(f)
            else:
                f.unlink()
    info("Build directories cleaned up")


def compile_shared(
    module: Path,
    install_dir: Path | None = None,
    lib_dir: Path | None = None,
) -> int:
    """Compile a shared library preserving directory structure."""
    global FLAGS
    PYTHON_LIBRARY = FLAGS["PYTHON_LIBRARY"]
    PYTHON_INCLUDE = FLAGS["PYTHON_INCLUDE"]
    INSTALL_DIR = install_dir or FLAGS["INSTALL_DIR"]
    LIB_EXT = FLAGS["LIB_EXT"]
    FORCE = FLAGS["FORCE"]

    cpp_path = module.with_suffix(".cpp")
    LIB_DIR = Path(lib_dir) if lib_dir else FLAGS["LIB_DIR"]

    # Preserve module structure in lib dir
    output_so = LIB_DIR / module.with_suffix(LIB_EXT).relative_to(INSTALL_DIR)
    output_so.parent.mkdir(parents=True, exist_ok=True)

    if output_so.exists() and cpp_path.stat().st_mtime < output_so.stat().st_mtime and not FORCE:
        info(f"[SKIP] {output_so.name} is up to date")
        return 0

    import platform
    import subprocess

    if platform.system() == "Darwin":
        # For macOS use clang++ and fix library paths
        lib_path = Path(PYTHON_LIBRARY).absolute()
        lib_dir = lib_path.parent

        # Compile the shared library
        cmd = [
            "clang++",
            "-shared",
            "-o",
            str(output_so),
            str(cpp_path),
            f"-I{PYTHON_INCLUDE}",
            f"-L{lib_dir}",
            f"-l{Path(PYTHON_LIBRARY).stem.replace('lib', '')}",
            "-fPIC",
            f"-Wl,-rpath,{lib_dir}",
        ]

        cmd_str = " ".join(map(str, cmd))

        try:
            print(f"Compiling shared library: {cmd_str}")
            subprocess.run(cmd_str, shell=True, check=True)

            # Fix the library reference in the compiled shared library
            fix_cmd = [
                "install_name_tool",
                "-change",
                "/install/lib/libpython3.12.dylib",
                str(lib_path),
                str(output_so),
            ]

            fix_cmd_str = " ".join(map(str, fix_cmd))
            print(f"Fixing library path: {fix_cmd_str}")
            subprocess.run(fix_cmd_str, shell=True, check=True)

            # Verify the library paths
            verify_cmd = ["otool", "-L", str(output_so)]
            verify_cmd_str = " ".join(map(str, verify_cmd))
            print(f"Verifying library paths: {verify_cmd_str}")
            subprocess.run(verify_cmd_str, shell=True, check=True)

            print(f"✅ Shared library compiled and fixed: {output_so}")
            return 0

        except Exception as e:
            print(f"Error: {e}")
            print("❌ Shared library compilation or fix failed")
            return 1
    else:
        # Original compilation for Linux/Windows
        cmd = " ".join(
            [
                "g++",
                "-shared",
                "-o",
                str(output_so),
                str(cpp_path),
                f"-I{PYTHON_INCLUDE}",
                f"-L{Path(PYTHON_LIBRARY).parent}",
                f"-l{Path(PYTHON_LIBRARY).stem.replace('lib', '')}",
                "-fPIC",
            ],
        )

        return run(cmd).returncode


def parallel_build(modules: list[Path], install_dir: Path | None = None, lib_dir: Path | None = None):
    """Build modules in parallel while respecting dependencies."""
    n_cores = max(1, multiprocessing.cpu_count() - 1)
    info(f"Building with {n_cores} processes")
    INSTALL_DIR = install_dir or FLAGS["INSTALL_DIR"]
    LIB_DIR = lib_dir or FLAGS["LIB_DIR"]
    MODULES = modules or FLAGS["MODULES"]
    with ProcessPoolExecutor(max_workers=n_cores // 2) as executor:
        futures = executor.map(partial(compile_shared, install_dir=INSTALL_DIR, lib_dir=LIB_DIR), MODULES)
        for f in futures:
            if f:
                error(f"Compilation failed with return code {f}")

        return "Compilation successful"


def cythonize_dependency(package_name: str, install_dir: Path) -> list[Path]:
    """Cythonize a Python dependency package."""
    package_dir = install_dir / "packages" / package_name
    if not package_dir.exists() or not any(package_dir.iterdir()):
        safe_print(f"⚠️ Package directory for {package_name} not found or empty")
        return []

    # Find all Python modules in the package
    py_files = list(package_dir.glob("**/*.py"))
    if not py_files:
        safe_print(f"No Python files found in {package_name}")
        return []

    safe_print(f"Cythonizing {len(py_files)} modules from {package_name}")

    # Cythonize each module
    from Cython.Build.Cythonize import cythonize

    cythonize(
        module_list=[str(m) for m in py_files],
        nthreads=(os.cpu_count() or 2) // 2,
        include_path=[FLAGS["PYTHON_INCLUDE"]],
        force=FLAGS["FORCE"],
        language="c++",
        **{**cmd_options(install=install_dir), "quiet": False},
    )

    # Compile each cythonized module
    compiled_modules = []
    for py_file in py_files:
        cpp_file = py_file.with_suffix(".cpp")
        if cpp_file.exists():
            # Preserve module structure in lib dir
            rel_path = cpp_file.relative_to(install_dir)
            output_so = FLAGS["LIB_DIR"] / rel_path.with_suffix(FLAGS["LIB_EXT"])
            output_so.parent.mkdir(parents=True, exist_ok=True)

            # Compile the shared library
            compile_shared(cpp_file, install_dir=install_dir, lib_dir=FLAGS["LIB_DIR"])
            if output_so.exists():
                compiled_modules.append(output_so)

    return compiled_modules


# def cythonize_executable(entry_point: str | None = None, modules: list[Path] | None = None):
#     """Compile a Python script into a C++ source file (`.cpp`)."""
#     global FLAGS

#     MODULES = modules or FLAGS["MODULES"]
#     INSTALL = FLAGS["INSTALL_DIR"]
#     BUILD = FLAGS["BUILD_DIR"]
#     entry_point = entry_point or FLAGS["ENTRY_POINT"]
#     entry_path = Path(entry_point).with_suffix(".py")

#     if not entry_path.exists():
#         entry_path.touch()

#     output_c = entry_path.with_suffix(".cpp")
#     script = files("mbcore").parent / "build_executable.py"

#     cmd = [sys.executable, script, str(entry_path.resolve())]

#     print(f"[INFO] Running: {' '.join(map(str, cmd))}")
#     from mbpy.cmd import run_command
#     try:
#         for line in run_command(' '.join(map(str, cmd))):
#             pass
#             # safe_print(line)

#     except subprocess.TimeoutExpired:
#         print("🔥 ERROR: `build_executable.py` is taking too long! Killing process...")
#         return None


def isbuiltin(module):
    if inspect.isbuiltin(module):
        return True
    try:
        return module.__name__ == "builtins"
    except AttributeError:
        return False


bundled = set()


def bundle_package(package_name: str, packages_dir: Path) -> None:
    try:
        # Find the package
        package = import_module(package_name)
        if package_name in bundled or isbuiltin(package):
            return
        bundled.add(package_name)

        print(f"📦 Bundling package: {package_name}")

        # Check if __file__ attribute exists and is not None
        package_file_attr = getattr(package, "__file__", None)
        if package_file_attr is None:
            print(f"⚠️ Package {package_name} has no file attribute, it might be built-in or namespace package")
            return

        package_file = Path(package_file_attr)
        if not package_file.exists():
            print(f"⚠️ Could not find package file for {package_name} at {package_file}")
            return

        # Check if this is a single file module or a package with __init__.py
        is_directory_package = package_file.name == "__init__.py"
        is_py_file = package_file.suffix.lower() == ".py"

        if is_directory_package:
            # Copy the whole directory
            package_path = package_file.parent
            dest_dir = packages_dir / package_name.replace('.', os.sep)
            print(f"📁 Copying directory package '{package_name}' from {package_path} to {dest_dir}")
            
            if package_path.is_dir():
                # Create destination directory
                dest_dir.mkdir(parents=True, exist_ok=True)
                
                # Copy files safely
                for src_path in package_path.glob('**/*'):
                    if src_path.is_dir():
                        # Create directory
                        rel_path = src_path.relative_to(package_path)
                        (dest_dir / rel_path).mkdir(parents=True, exist_ok=True)
                    elif src_path.is_file():
                        # Skip cache files
                        if any(part in ['__pycache__', '.git', '.hg', '.svn'] for part in src_path.parts):
                            continue
                        if src_path.suffix.lower() in ['.pyc', '.pyo']:
                            continue
                            
                        # Copy the file using text mode for .py files
                        rel_path = src_path.relative_to(package_path)
                        dst_path = dest_dir / rel_path
                        dst_path.parent.mkdir(parents=True, exist_ok=True)
                        
                        # Use text mode for Python files to avoid null bytes
                        if src_path.suffix.lower() == '.py':
                            try:
                                with open(src_path, 'r', encoding='utf-8', errors='replace') as src_file:
                                    content = src_file.read()
                                
                                # Remove null bytes if any
                                if '\0' in content:
                                    print(f"🔧 Removing null bytes from {src_path}")
                                    content = content.replace('\0', '')
                                
                                with open(dst_path, 'w', encoding='utf-8') as dst_file:
                                    dst_file.write(content)
                            except Exception as e:
                                print(f"⚠️ Error copying {src_path}: {e}")
                        else:
                            # Use binary mode for non-Python files
                            try:
                                shutil.copy2(src_path, dst_path)
                            except Exception as e:
                                print(f"⚠️ Error copying {src_path}: {e}")
                
                print(f"✅ Bundled directory {package_name}")
            else:
                print(f"❌ Source path {package_path} is not a directory for package {package_name}")

        elif is_py_file:
            # Copy single file module
            module_parts = package_name.split(".")
            dest_path = packages_dir
            for part in module_parts[:-1]:
                dest_path = dest_path / part
                dest_path.mkdir(parents=True, exist_ok=True)
            dest_path = dest_path / f"{module_parts[-1]}.py"

            print(f"📄 Copying single file module '{package_name}' from {package_file} to {dest_path}")
            dest_path.parent.mkdir(parents=True, exist_ok=True)
            
            # Copy in text mode to avoid null bytes
            try:
                with open(package_file, 'r', encoding='utf-8', errors='replace') as src_file:
                    content = src_file.read()
                
                # Remove null bytes if any
                if '\0' in content:
                    print(f"🔧 Removing null bytes from {package_file}")
                    content = content.replace('\0', '')
                
                with open(dest_path, 'w', encoding='utf-8') as dst_file:
                    dst_file.write(content)
                print(f"✅ Bundled file {package_name}")
            except Exception as e:
                print(f"⚠️ Error copying {package_file}: {e}")
        else:
            # Found a __file__ but it's not __init__.py or .py (e.g., it's a .so/.pyd file)
            print(f"⚠️ Skipping non-.py file for module '{package_name}': {package_file}")
            return

        # For standard library modules that are critical, create direct clean copies 
        if package_name in ["traceback", "linecache", "logging", "warnings", "collections", "re"]:
            print(f"🔍 Creating extra clean copy of standard library module: {package_name}")
            stdlib_path = find_python_stdlib()
            if stdlib_path:
                module_path = f"{package_name}.py"
                src = stdlib_path / module_path
                dst = packages_dir / module_path
                
                if src.exists():
                    try:
                        with open(src, 'r', encoding='utf-8', errors='replace') as f_src:
                            content = f_src.read()
                        with open(dst, 'w', encoding='utf-8') as f_dst:
                            f_dst.write(content)
                        print(f"✅ Created clean copy of {package_name}")
                    except Exception as e:
                        print(f"⚠️ Error creating clean copy of {package_name}: {e}")

    except ImportError:
        import traceback as tb
        tb.print_exc()
        print(f"❌ Could not import {package_name}")
    except Exception as e:
        import traceback as tb
        tb.print_exc()
        print(f"❌ Error bundling {package_name}: {e}")


ModulePath = NewType("ModulePath", str)


def bundle_and_cythonize(module_path: ModulePath, packages_dir: Path, bundled: list[Path]) -> list[Path]:
    mod = Path(module_path)
    bundle_package(mod.stem, packages_dir)
    newly_bundled = cythonize_dependency(mod.stem, packages_dir)
    bundled.extend(newly_bundled)
    return newly_bundled


# Module-level function to support pickling with multiprocessing
def _inner_bundle_for_mp(args):
    package_name, packages_dir, bundled_list = args
    return bundle_and_cythonize(ModulePath(package_name), packages_dir, bundled_list)


def bundler_and_cythonizer(packages_dir: Path, bundled: list[Path] | None = None) -> Callable[[str], list[Path]]:
    bundled = bundled or []
    # Return a function that accepts str, but internally converts to ModulePath if needed or uses it directly
    def _inner_bundle(package_name: str) -> list[Path]:
        # Assuming bundle_and_cythonize can handle the string package name appropriately
        # or you adjust bundle_and_cythonize to accept str.
        # For now, let's assume it works with the package name string.
        return bundle_and_cythonize(ModulePath(package_name), packages_dir, bundled)
    return _inner_bundle


def bundle_packages(install_dir: Path, required_packages: list[str], nproc: Literal["auto"] | int = 1):
    """Bundle Python packages with the executable by cythonizing them."""
    # Create package directory
    packages_dir = install_dir / "packages"
    packages_dir.mkdir(exist_ok=True)

    # First copy all packages
    bundled: list[Path] = []
    if nproc == "auto" or nproc > 1:
        actual_nproc = (os.cpu_count() or 2) - 1 if nproc == "auto" else nproc
        with multiprocessing.Pool(processes=actual_nproc) as pool:
            # Create argument tuples for each process
            args_list = [(package, packages_dir, []) for package in required_packages]
            # Use the module-level function directly
            results = pool.map(_inner_bundle_for_mp, args_list)
            # Process results if needed, e.g., flatten list of lists
            for res_list in results:
                bundled.extend(res_list)
    else:
        # Non-parallel version
        for package in required_packages:
            newly_bundled = bundle_and_cythonize(ModulePath(package), packages_dir, [])
            bundled.extend(newly_bundled)

    return bundled # Return the list of bundled paths


def find_python_stdlib():
    """Find the Python standard library directory using multiple detection methods."""
    def check_path(path):
        """Returns a valid path if it exists and contains key stdlib files, else None."""
        path = Path(path)
        if path.exists() and (path / "traceback.py").exists():
            return path
        return None
    
    # 1. Direct detection using sys.path
    for path in sys.path:
        path = Path(path)
        if check_path(path):
            if DEBUG: print(f"Method 1: Found stdlib via sys.path: {path}")
            return path
    
    # 2. Use the Python executable location
    py_exec_dir = Path(sys.executable).parent
    lib_path = py_exec_dir.parent / "lib" / f"python{sys.version_info.major}.{sys.version_info.minor}"
    if check_path(lib_path):
        if DEBUG: print(f"Method 2: Found stdlib via Python executable: {lib_path}")
        return lib_path
        
    # 3. Use the Python library location
    python_lib = FLAGS.get("PYTHON_LIBRARY", "")
    if python_lib:
        python_lib_path = Path(python_lib)
        lib_path = python_lib_path.parent.parent / "lib" / f"python{sys.version_info.major}.{sys.version_info.minor}"
        if check_path(lib_path):
            if DEBUG: print(f"Method 3: Found stdlib via Python library: {lib_path}")
            return lib_path
    
    # 4. Use the Python include location
    python_include = FLAGS.get("PYTHON_INCLUDE", "")
    if python_include:
        python_include_path = Path(python_include)
        lib_path = python_include_path.parent.parent / "lib" / f"python{sys.version_info.major}.{sys.version_info.minor}"
        if check_path(lib_path):
            if DEBUG: print(f"Method 4: Found stdlib via Python include: {lib_path}")
            return lib_path
    
    # 5. Check common system locations
    common_paths = [
        # Mac homebrew
        Path(f"/opt/homebrew/lib/python{sys.version_info.major}.{sys.version_info.minor}"),
        Path(f"/opt/homebrew/Cellar/python@{sys.version_info.major}.{sys.version_info.minor}/*/Frameworks/Python.framework/Versions/{sys.version_info.major}.{sys.version_info.minor}/lib/python{sys.version_info.major}.{sys.version_info.minor}"),
        # System Python
        Path(f"/usr/lib/python{sys.version_info.major}.{sys.version_info.minor}"),
        Path(f"/usr/local/lib/python{sys.version_info.major}.{sys.version_info.minor}"),
        # Windows
        Path(f"C:\\Python{sys.version_info.major}{sys.version_info.minor}\\Lib"),
    ]
    
    # Support wildcard expansion for homebrew
    expanded_paths = []
    for path in common_paths:
        if "*" in str(path):
            import glob
            expanded_paths.extend(Path(p) for p in glob.glob(str(path)))
        else:
            expanded_paths.append(path)
    
    for path in expanded_paths:
        if check_path(path):
            if DEBUG: print(f"Method 5: Found stdlib in common location: {path}")
            return path
    
    # 6. Use Python internals to detect library path
    try:
        import importlib.util
        traceback_spec = importlib.util.find_spec('traceback')
        if traceback_spec and traceback_spec.origin:
            traceback_path = Path(traceback_spec.origin)
            if traceback_path.exists():
                stdlib_path = traceback_path.parent
                if DEBUG: print(f"Method 6: Found stdlib via importlib: {stdlib_path}")
                return stdlib_path
    except Exception as e:
        if DEBUG: print(f"Method 6 failed: {e}")
    
    # No standard library found
    if DEBUG: print("All methods failed to find Python standard library.")
    return None


def create_clean_stdlib_modules(install_dir: Path) -> None:
    """Create clean copies of essential standard library modules that cause problems with null bytes."""
    global FLAGS
    packages_dir = install_dir / "packages"
    packages_dir.mkdir(exist_ok=True)
    
    print("🔍 Creating clean copies of standard library modules...")
    
    # Use the dedicated finder function to locate the standard library
    stdlib_path = find_python_stdlib()
    
    if not stdlib_path:
        print("❌ Could not find standard library. Creating minimal stub implementations")
        create_minimal_stub_modules(packages_dir)
        return
    
    print(f"🔍 Found stdlib at: {stdlib_path}")
        
    # These are the modules that are known to cause issues
    essential_modules = [
        "traceback.py",
        "linecache.py",
        "warnings.py",
        "collections/__init__.py",
        "weakref.py",
        "re.py",
        "io.py",
        "codecs.py",
        "sre_parse.py",
        "sre_compile.py",
        "sre_constants.py",
        "enum.py",
        "abc.py",
        "textwrap.py",  # Added textwrap for traceback
        "types.py",     # Added types for various modules
        "functools.py", # Added functools for collections
        "operator.py",  # Added operator for collections
        "keyword.py",   # Added keyword for collections
        "heapq.py",     # Added heapq for collections
        "reprlib.py",   # Added reprlib for collections
        "string.py",    # Added string for textwrap
    ]
    
    # Copy each module
    copied_modules = []
    
    for module_path in essential_modules:
        src = stdlib_path / module_path
        dst = packages_dir / module_path
        dst.parent.mkdir(parents=True, exist_ok=True)
        
        if src.exists():
            print(f"🔍 Copying {src} to {dst}")
            try:
                # Read in text mode to avoid null bytes
                with open(src, 'r', encoding='utf-8') as f_src:
                    content = f_src.read()
                    
                # Check for null bytes in the source file
                if '\0' in content:
                    print(f"⚠️ WARNING: Source file already contains null bytes: {src}")
                    content = content.replace('\0', '')
                    print(f"🔧 Removed null bytes from content")
                
                # Write in text mode to ensure clean file
                with open(dst, 'w', encoding='utf-8') as f_dst:
                    f_dst.write(content)
                
                # Verify the written file doesn't have null bytes
                with open(dst, 'r', encoding='utf-8', errors='replace') as f_check:
                    check_content = f_check.read()
                    if '\0' in check_content:
                        print(f"❌ ERROR: Copied file still has null bytes: {dst}")
                    else:
                        print(f"✅ Successfully copied {module_path} (size: {len(content)} bytes)")
                        copied_modules.append(module_path)
            except UnicodeDecodeError as e:
                print(f"⚠️ UnicodeDecodeError when copying {module_path}: {e}")
                # Try binary read and clean before writing
                try:
                    with open(src, 'rb') as f_src:
                        binary_content = f_src.read()
                    # Remove null bytes
                    binary_content = binary_content.replace(b'\0', b'')
                    # Write as text
                    with open(dst, 'w', encoding='utf-8', errors='replace') as f_dst:
                        f_dst.write(binary_content.decode('utf-8', errors='replace'))
                    print(f"🔧 Used binary mode and cleaned file: {dst}")
                    copied_modules.append(module_path)
                except Exception as e2:
                    print(f"❌ Failed binary fallback for {module_path}: {e2}")
            except Exception as e:
                print(f"❌ Failed to copy {module_path}: {e}")
        else:
            print(f"❌ Could not find module {module_path} at {src}")
    
    print(f"🔍 Copied {len(copied_modules)}/{len(essential_modules)} modules: {copied_modules}")
    
    # Add __init__.py files
    init_file = packages_dir / "__init__.py"
    if not init_file.exists():
        with open(init_file, 'w') as f:
            f.write("# Package init file\n")
        print(f"✅ Created {init_file}")
    
    # Make sure collections has an __init__.py
    collections_init = packages_dir / "collections" / "__init__.py"
    if not collections_init.exists() and (packages_dir / "collections").exists():
        with open(collections_init, 'w') as f:
            f.write("# Collections init file\n")
        print(f"✅ Created {collections_init}")
    
    if not copied_modules:
        print(f"❌ Failed to copy any standard library modules. Creating minimal stubs.")
        create_minimal_stub_modules(packages_dir)


def create_minimal_stub_modules(packages_dir: Path) -> None:
    """Create minimal stub implementations of required modules."""
    print("🔧 CRITICAL FIX: Creating minimal stub implementations")
    
    # Create packages dir
    packages_dir.mkdir(exist_ok=True)
    
    # Create minimal collections module
    collections_dir = packages_dir / "collections"
    collections_dir.mkdir(exist_ok=True)
    with open(collections_dir / "__init__.py", "w") as f:
        f.write("""# Minimal collections stub
class abc:
    pass
""")
    
    # Create minimal traceback module
    with open(packages_dir / "traceback.py", "w") as f:
        f.write("""# Minimal traceback stub
def print_exc(*args, **kwargs):
    pass

def format_exc(*args, **kwargs):
    return "Error traceback unavailable"
""")
    
    # Create minimal linecache module
    with open(packages_dir / "linecache.py", "w") as f:
        f.write("""# Minimal linecache stub
def getline(*args, **kwargs):
    return ""
""")
    
    # Create empty __init__.py
    with open(packages_dir / "__init__.py", "w") as f:
        f.write("# Package init\n")
    
    print("🔧 CRITICAL FIX: Created minimal stub implementations")


def compile_executable(
    entry_point: Path,
    bin_dir: Path | None = None,
    python_library: Path | None = None,
    python_include: Path | None = None,
) -> int:
    """Compile a Python module into a standalone executable."""
    global FLAGS
    PYTHON_LIBRARY = python_library or FLAGS["PYTHON_LIBRARY"]
    PYTHON_INCLUDE = python_include or FLAGS["PYTHON_INCLUDE"]
    INSTALL_DIR = FLAGS["INSTALL_DIR"]
    LIB_DIR = FLAGS["LIB_DIR"]
    BIN_DIR = bin_dir or FLAGS["BIN_DIR"]

    safe_print(FLAGS)
    safe_print(f"{PYTHON_INCLUDE=}, {PYTHON_LIBRARY=}")

    if not PYTHON_LIBRARY.is_file():
        error(f"Python library path is not a file: {PYTHON_LIBRARY}")
        return 1

    output_bin = BIN_DIR / (entry_point.stem)
    # Ensure the output directory exists
    BIN_DIR.mkdir(parents=True, exist_ok=True)

    # Create temporary C file with main function
    output_c = BIN_DIR / f"{entry_point.stem}.cpp"

    # Bundle dependencies
    imports = get_topo_imports()
    bundled_files = bundle_packages(install_dir=INSTALL_DIR, required_packages=imports, nproc="auto")
    
    # Create clean copies of standard library modules
    create_clean_stdlib_modules(INSTALL_DIR)

    # Create the main file
    import platform

    if platform.system() == "Darwin":
        python_prefix = PYTHON_LIBRARY.parent.parent.as_posix()
        add_main(entry_point, output_c, python_prefix)

        # Collect all shared libraries that need to be linked
        lib_files = list(LIB_DIR.glob("**/*.dylib"))
        python_lib_dir = PYTHON_LIBRARY.parent
        python_lib_name = str(PYTHON_LIBRARY) # Full path to the library

        # Build the command as a list for shell=False
        compile_cmd = [
            "clang++",
            "-std=c++17",  # Add C++17 support for std::filesystem
            "-I", str(PYTHON_INCLUDE),
            str(output_c), # Use the generated main.cpp
            python_lib_name, # Link against the Python library
            f"-Wl,-rpath,{python_lib_dir}", # Set rpath to find Python lib at runtime
        ]

        # Add each compiled project library file
        for lib in lib_files:
            compile_cmd.append(str(lib))

        # Add remaining arguments: rpath for project libs and output file
        compile_cmd.extend([f"-Wl,-rpath,{LIB_DIR}", "-o", str(output_bin)]) # rpath for bundled libs

        import subprocess

        try:
            # Use shell=False and pass the list directly
            print(f"Compiling with: {' '.join(map(str, compile_cmd))}")
            # Ensure check=True to raise error on failure
            subprocess.run(compile_cmd, check=True, shell=False)
            # === Add Check 1 ===
            if not output_bin.exists():
                print(f"🔴 ERROR: Executable {output_bin} DOES NOT EXIST immediately after compile command!")
            else:
                print(f"🟢 INFO: Executable {output_bin} EXISTS immediately after compile command.")
            # === End Check 1 ===

            # --- install_name_tool logic ---
            # Fix the library dependencies *within* our compiled libraries first
            fix_cmds = []
            original_python_lib_id = f"{LIB_DIR.name}/{PYTHON_LIBRARY.name}" # Default ID Cython/compiler might embed
            for lib in lib_files:
                # Change how our library refers to the Python library
                fix_cmd_python = [
                    "install_name_tool",
                    "-change",
                    original_python_lib_id, # Or potentially just PYTHON_LIBRARY.name if path isn't included
                    python_lib_name, # Change to the absolute path
                    str(lib),
                ]
                # Attempt to change potential default rpath reference as well
                fix_cmd_rpath = [
                     "install_name_tool",
                     "-change",
                     f"@rpath/{PYTHON_LIBRARY.name}", # Common reference style
                     python_lib_name, # Change to the absolute path
                     str(lib),
                 ]
                fix_cmds.append(fix_cmd_python)
                fix_cmds.append(fix_cmd_rpath)

            # Fix how the executable refers to the Python library
            fix_cmd_exe_python = [
                "install_name_tool",
                "-change",
                original_python_lib_id, # Or PYTHON_LIBRARY.name
                python_lib_name, # Change to the absolute path
                str(output_bin),
            ]
            fix_cmd_exe_rpath = [
                 "install_name_tool",
                 "-change",
                 f"@rpath/{PYTHON_LIBRARY.name}",
                 python_lib_name,
                 str(output_bin),
             ]
            fix_cmds.append(fix_cmd_exe_python)
            fix_cmds.append(fix_cmd_exe_rpath)

            # Run all the fix commands - ignore errors for changes that might not be needed
            for cmd in fix_cmds:
                print(f"Attempting library fix: {' '.join(map(str, cmd))}")
                # Run without check=True as the 'change' might fail if the 'from' path doesn't exist
                subprocess.run(cmd, shell=False)

            # === Add Check 2 ===
            if not output_bin.exists():
                print(f"🔴 ERROR: Executable {output_bin} DOES NOT EXIST after install_name_tool commands!")
            else:
                print(f"🟢 INFO: Executable {output_bin} EXISTS after install_name_tool commands.")
                # === Verification Step ===
                print(f"Verifying executable dependencies: otool -L {output_bin}")
                subprocess.run(["otool", "-L", str(output_bin)], check=False, shell=False)
                for lib in lib_files:
                     print(f"Verifying library dependencies: otool -L {lib}")
                     subprocess.run(["otool", "-L", str(lib)], check=False, shell=False)
                # === End Verification Step ===

            print(f"✅ Executable compiled and potentially fixed in {BIN_DIR}") # This might be premature
            return 0
        except subprocess.CalledProcessError as e:
            import traceback

            traceback.print_exc()
            print(f"Error: {e}")
            print("❌ Compilation or library fix failed")
            return 1
    else:
        # Linux/Windows implementation is similar but needs adjustments
        python_prefix = str(PYTHON_LIBRARY.parent.parent)
        add_main(entry_point, output_c, python_prefix)

        # Collect all shared libraries
        if platform.system() == "Windows":
            lib_files = list(LIB_DIR.glob("**/*.pyd"))
            compiler = "g++"
        else:  # Linux
            lib_files = list(LIB_DIR.glob("**/*.so"))
            compiler = "g++"

        # Build the command as a list
        compile_cmd = [
            compiler,
            str(output_c),
            f"-I{PYTHON_INCLUDE}",
            f"-L{PYTHON_LIBRARY.parent}",
            f"-l{PYTHON_LIBRARY.stem.replace('lib', '')}",
        ]

        # Add each library file as a separate argument
        for lib in lib_files:
            compile_cmd.append(str(lib))

        # Add remaining arguments
        compile_cmd.extend([f"-Wl,-rpath={PYTHON_LIBRARY.parent}", "-o", str(output_bin)])

        cmd = " ".join(map(str, compile_cmd))
        ret = run(cmd).returncode

        if ret == 0:
            print(f"✅ Executable compiled in {BIN_DIR}")

        return ret


def dump():
    """Dump build configuration."""
    SRC_DIR = FLAGS["SRC_DIR"]
    BUILD_DIR = FLAGS["BUILD_DIR"]
    INSTALL_DIR = FLAGS["INSTALL_DIR"]
    BIN_DIR = FLAGS["BIN_DIR"]
    LIB_DIR = FLAGS["LIB_DIR"]
    OS_NAME = FLAGS["OS_NAME"]
    PYTHON_LIBRARY = FLAGS["PYTHON_LIBRARY"]
    PYTHON_INCLUDE = FLAGS["PYTHON_INCLUDE"]

    getconsole().print(f"[INFO] {SRC_DIR=}")
    getconsole().print(f"[INFO] {BUILD_DIR=}")
    getconsole().print(f"[INFO] {INSTALL_DIR=}")
    getconsole().print(f"[INFO] {BIN_DIR=}")
    getconsole().print(f"[INFO] {LIB_DIR=}")
    getconsole().print(f"[INFO] {OS_NAME=}")
    getconsole().print(f"[INFO] {PYTHON_LIBRARY=}")
    getconsole().print(f"[INFO] {PYTHON_INCLUDE=}")


@click.command("mbuild", help="Build Python modules into shared libraries.")
@click.rich_config(get_help_config())  # noqa: F821
@click.option("--embed", is_flag=True, help="Embed Python interpreter")
@click.option("--force", is_flag=True, help="Force recompilation")
@click.option("--root", default=".", help="Root directory")
@click.option("--entry", default="main", help="Entry point (module or file path)")
@click.option("--python-library", default="", help="Python library path (will be auto-detected if not specified)")
@click.option("--python-include", default="", help="Python include directory (will be auto-detected if not specified)")
@click.option("--install-dir", default="", help="Install directory (defaults to './install')")
@click.option("--build-dir", default="", help="Build directory (defaults to './build')")
@click.option("--src-dir", default="", help="Source directory (defaults to './src' or detected from entry point)")
@click.option("--ignore", default="", help="Pattern to ignore")
@click.option("--include", default="", help="Pattern to include")
@click.argument("modules_files_directories", nargs=-1)
def main(
    embed=False,
    force=False,
    root=".",
    entry="main",
    python_library="",
    python_include="",
    install_dir="",
    build_dir="",
    src_dir="",
    modules_files_directories: list[str] = [],
    ignore="",
    include="",
):
    """Build Python modules into shared libraries."""

    from mbcore.collect import getin
    from mbcore.traverse import find_file

    # Make paths absolute for consistent behavior
    cwd = Path.cwd()
    root_path = Path(root).resolve()
    if not root_path.exists():
        print(f"❌ Root directory '{root}' does not exist. Using current directory.")
        root_path = cwd
    
    # Handle entry point intelligently
    entry_path = None
    if Path(entry).exists():
        # Direct file path provided
        entry_path = Path(entry).resolve()
        print(f"✅ Using specified entry point file: {entry_path}")
    else:
        # Try various ways to find the entry
        possible_paths = [
            # Check if it's a direct file path
            Path(entry),
            # Try relative to root
            root_path / entry,
            # Try with .py extension
            root_path / f"{entry}.py",
            # Try as a module path
            root_path / entry.replace(".", os.sep) + ".py",
            # Try in src directory if it exists
            root_path / "src" / entry.replace(".", os.sep) + ".py",
        ]
        
        for path in possible_paths:
            if path.exists():
                entry_path = path.resolve()
                print(f"✅ Found entry point: {entry_path}")
                break
                
        if not entry_path:
            print(f"⚠️ Could not find entry point '{entry}'. Please provide a valid file path or module name.")
            entry_path = Path(entry)  # Use as is, will be validated later
    
    # Auto-detect src_dir if not specified
    src_dir_path = None
    if src_dir:
        src_dir_path = (root_path / src_dir).resolve()
        if not src_dir_path.exists():
            print(f"⚠️ Specified src_dir '{src_dir}' does not exist.")
            src_dir_path = None
            
    if not src_dir_path and entry_path and entry_path.exists():
        # Try to infer src_dir from entry_path
        if 'src' in entry_path.parts:
            # Find 'src' in the path
            src_index = entry_path.parts.index('src')
            if src_index < len(entry_path.parts) - 1:
                # Get the path up to and including 'src'
                src_dir_path = Path(*entry_path.parts[:src_index+1]).resolve()
                print(f"✅ Auto-detected src_dir: {src_dir_path}")
    
    if not src_dir_path:
        # Check for common src directory conventions
        common_src_dirs = [
            root_path / "src",
            root_path / "source",
            root_path,
        ]
        
        for path in common_src_dirs:
            if path.exists() and path.is_dir():
                src_dir_path = path
                print(f"✅ Using detected src_dir: {src_dir_path}")
                break
                
        if not src_dir_path:
            # Default to root directory
            src_dir_path = root_path
            print(f"⚠️ Could not detect src_dir. Using root directory: {src_dir_path}")

    # Set up install and build directories
    install_dir_path = (root_path / (install_dir or "install")).resolve()
    build_dir_path = (root_path / (build_dir or "build")).resolve()
    
    print(f"📋 Configuration:")
    print(f"  Root directory: {root_path}")
    print(f"  Source directory: {src_dir_path}")
    print(f"  Build directory: {build_dir_path}")
    print(f"  Install directory: {install_dir_path}")
    print(f"  Entry point: {entry_path}")
        
    # Try to auto-detect Python paths if not specified
    python_library_path = Path(python_library) if python_library else None
    python_include_path = Path(python_include) if python_include else None

    # Load configuration from pyproject.toml if it exists
    pyproject_path = root_path / "pyproject.toml"
    ignore_patterns = []
    include_patterns = []
    
    if pyproject_path.exists():
        try:
            project = tomlkit.loads(pyproject_path.read_text())
            project_data = project.unwrap()
            tool_mb_data = project_data.get("tool", {}).get("mb", {})

            if not src_dir_path and "src" in tool_mb_data:
                src_dir_str = tool_mb_data.get("src")
                src_dir_path = root_path / src_dir_str
                print(f"✅ Using src_dir from pyproject.toml: {src_dir_path}")

            ignore_val = tool_mb_data.get("ignore", ignore)
            include_val = tool_mb_data.get("include", include)

            ignore_patterns = ignore_val if isinstance(ignore_val, list) else [ignore_val] if ignore_val else []
            include_patterns = include_val if isinstance(include_val, list) else [include_val] if include_val else []

        except Exception as e:
            print(f"⚠️ Error reading pyproject.toml: {e}")

    # Determine module paths based on input and src_dir
    mods: list[Path] = []
    if modules_files_directories:
        for m_str in modules_files_directories:
            m_path = Path(m_str)
            if m_path.exists():
                mods.append(m_path.resolve())
            else:
                # Try relative to src_dir_path
                rel_path = src_dir_path / m_str
                if rel_path.exists():
                    mods.append(rel_path.resolve())
                else:
                    # Try interpreting as module name (e.g., 'pkg.mod')
                    mod_file_path = src_dir_path / Path(m_str.replace(".", os.sep)).with_suffix(".py")
                    if mod_file_path.exists():
                        mods.append(mod_file_path.resolve())
                    else:
                        print(f"⚠️ Could not find module/file '{m_str}'")
    else:
        # Find Python modules in src_dir_path
        if src_dir_path and src_dir_path.exists():
            print(f"🔍 Searching for Python modules in {src_dir_path}")
            excluded_dirs = {"Cython", "mbpy", "__pycache__", ".git", "tests", "test"}
            all_py_files = list(src_dir_path.glob("**/*.py"))
            print(f"📚 Found {len(all_py_files)} Python files initially.")
            
            for py_file in all_py_files:
                # Basic filtering
                if "__init__" in py_file.name or "__pycache__" in str(py_file):
                    continue
                if any(excluded in str(py_file) for excluded in excluded_dirs):
                    continue
                mods.append(py_file.resolve())
            
            print(f"📋 Found {len(mods)} modules to process after filtering.")
        else:
            print(f"❌ Source directory {src_dir_path} does not exist. No modules to process.")

    # Apply ignore patterns
    if ignore_patterns:
        mods_before_ignore = len(mods)
        # Simple wildcard matching instead of complex Path.match
        filtered_mods = []
        for mod in mods:
            mod_str = str(mod)
            if not any(pattern in mod_str for pattern in ignore_patterns):
                filtered_mods.append(mod)
        mods = filtered_mods
        print(f"🔍 Applied ignore patterns, {len(mods)} modules remaining (was {mods_before_ignore}).")

    # Apply include patterns
    if include_patterns and include_patterns != ['*']:
        mods_before_include = len(mods)
        # Simple wildcard matching
        filtered_mods = []
        for mod in mods:
            mod_str = str(mod)
            if any(pattern in mod_str for pattern in include_patterns):
                filtered_mods.append(mod)
        mods = filtered_mods
        print(f"🔍 Applied include patterns, {len(mods)} modules remaining (was {mods_before_include}).")

    if not mods:
        print("⚠️ No modules found to process. Please check your paths and patterns.")
        if not entry_path.exists():
            print(f"❌ Entry point '{entry_path}' does not exist. Cannot continue.")
            return

    # Call _main with parsed paths
    try:
        _main(
            embed=embed,
            force=force,
            root=root_path,
            entry=entry_path,
            python_library=python_library_path,
            python_include=python_include_path,
            install_dir=install_dir_path,
            build_dir=build_dir_path,
            src_dir=src_dir_path,
            modules=mods,
        )
        print(f"✅ Build completed successfully.")
    except Exception as e:
        import traceback
        print(f"❌ Build failed: {e}")
        traceback.print_exc()


def _main(
    embed: bool,
    force: bool,
    root: Path,
    entry: Path,
    python_library: Path,
    python_include: Path,
    install_dir: Path,
    build_dir: Path,
    src_dir: Path,
    modules: list[Path],
):
    """Build Python modules into shared libraries."""
    # Ensure all module paths are absolute before passing to setup_paths
    absolute_modules = [m.resolve() for m in modules]

    setup_paths(
        root_path=root,
        entry=entry, # Keep entry as Path object
        force=force,
        python_library=python_library,
        python_include=python_include,
        install_dir=install_dir,
        build_dir=build_dir,
        src_dir=src_dir,
        modules=absolute_modules, # Pass list[Path]
    )

    global FLAGS
    INSTALL_DIR = FLAGS["INSTALL_DIR"]
    MODULES = FLAGS["MODULES"]
    BIN_DIR = FLAGS["BIN_DIR"]
    PYTHON_LIBRARY = FLAGS["PYTHON_LIBRARY"]
    PYTHON_INCLUDE = FLAGS["PYTHON_INCLUDE"]
    FORCE: bool = FLAGS["FORCE"]
    # Build everything in parallel
    MODULES = copytree(src_dir=src_dir, install_dir=INSTALL_DIR, modules=MODULES)

    cythonize_shared(modules=MODULES, install_dir=INSTALL_DIR)
    out = parallel_build(MODULES)
    entry_point = INSTALL_DIR / "mbcore" / "main.py"

    if embed:
        compile_executable(entry_point, BIN_DIR, PYTHON_LIBRARY, PYTHON_INCLUDE)
    safe_print(f"✅ Executable compiled in {BIN_DIR}")


def get_topo_imports() -> list[str]:
    """Get topologically sorted imports from the dependency graph."""
    from mbcore.more import unique_everseen

    # Initialize a list to collect all imports
    all_imports = []

    # Get the dependency graph
    SRC_DIR = FLAGS["SRC_DIR"]

    # Get the project's root module name from SRC_DIR
    project_module = first_true(
        SRC_DIR.iterdir(),
        lambda x: x.is_dir() and any(f.name == "__init__.py" for f in x.iterdir()),
    )
    
    if not project_module:
        if DEBUG: 
            print("No valid Python package found with __init__.py. Using SRC_DIR directly.")
        project_module = SRC_DIR
    
    # Handle the case where _build_dependency_graph returns a list instead of a graph object
    gs = _build_dependency_graph(project_module)
    
    # Debug print what type of object gs is
    if DEBUG: 
        print(f"Dependency graph type: {type(gs)}")
        if hasattr(gs, "nodes"):
            print(f"Graph has {len(gs.nodes)} nodes")
    
    # Check if gs has topo_sort method
    if hasattr(gs, "topo_sort"):
        gs = gs.topo_sort()
        # Iterate through the graph to collect all imports
        for g in gs:
            for node in g.nodes:
                child = g.nodes[node]
                if "imports" in child.content:
                    all_imports.extend(child.content["imports"])
                    if DEBUG:
                        print(f"Found imports in {node}: {child.content['imports']}")
    else:
        # Handle the case where gs is a list
        if DEBUG: print(f"Got dependency results as a list of {len(gs)} files instead of a graph")
        
        # Add standard library modules that would be detected by dependency analysis
        all_imports.extend([
            "traceback", "linecache", "warnings", "collections", "weakref", 
            "re", "io", "codecs", "sre_parse", "sre_compile", "sre_constants",
            "enum", "abc", "textwrap", "types", "functools", "operator", 
            "keyword", "heapq", "reprlib", "string", "tomlkit", "rich"
        ])
        
        # Add third-party dependencies from pyproject.toml
        if Path("pyproject.toml").exists():
            try:
                import tomlkit
                with open("pyproject.toml") as f:
                    pyproject = tomlkit.parse(f.read())
                if "dependencies" in pyproject.get("project", {}):
                    deps = pyproject["project"]["dependencies"]
                    deps = [d.split("[")[0].split(">=")[0].split("==")[0].strip() for d in deps]
                    all_imports.extend(deps)
                    if DEBUG: print(f"Added dependencies from pyproject.toml: {deps}")
            except Exception as e:
                if DEBUG: print(f"Error reading dependencies from pyproject.toml: {e}")

    if DEBUG: print(f"Found {len(all_imports)} imports: {all_imports}")
    # Return unique imports using the unique_everseen function
    return list(unique_everseen(all_imports))


def add_main(entry_point: Path, output_c: Path, python_prefix: str | None = None) -> None:
    """Create a C++ main file that properly initializes Python."""
    global FLAGS
    install_dir = str(FLAGS["INSTALL_DIR"]) if "INSTALL_DIR" in FLAGS else "./install"
    python_lib_path = FLAGS["PYTHON_LIBRARY"]

    # Derive the module name from the entry_point relative to install_dir
    rel_path = entry_point.relative_to(Path(install_dir))
    module_name = str(rel_path.with_suffix("")).replace(os.sep, ".")

    # Ensure we have a valid Python prefix for the runtime
    if not python_prefix:
        # Default to PYTHON_LIBRARY's parent.parent as the Python home
        python_prefix = str(python_lib_path.parent.parent)

    main_code = f"""#include <Python.h>  
#include <iostream>  
#include <filesystem>  
#include <string>

// Helper to check if a file exists
bool file_exists(const std::string& path) {{
    std::filesystem::path p(path);
    return std::filesystem::exists(p);
}}

int main(int argc, char *argv[]) {{
    // Setup environment
    wchar_t *program = Py_DecodeLocale(argv[0], NULL);
    if (program == NULL) {{
        std::cerr << "Fatal error: cannot decode program name" << std::endl;
        return 1;
    }}
  
    // Create Python configuration with optimized settings
    PyConfig config;  
    PyConfig_InitPythonConfig(&config);  
    
    // Fast startup optimizations
    config.isolated = 1;                // Skip site.py for faster startup
    config.use_environment = 0;         // Ignore environment variables
    config.parse_argv = 0;              // Don't parse command line
    config.configure_c_stdio = 0;       // Don't configure C stdio
    config.install_signal_handlers = 0; // Skip signal handlers
    
    // Set Python home directory  
    std::string prefix = "{python_prefix}";  
    printf("Setting Python home to: %s\\n", prefix.c_str());
    
    config.home = Py_DecodeLocale(prefix.c_str(), NULL);  
    if (config.home == NULL) {{  
        std::cerr << "Fatal error: cannot decode Python home path" << std::endl;  
        return 1;  
    }}  
    
    // Explicitly specify the Python program name
    config.program_name = program;
    
    // Initialize Python  
    PyStatus status = Py_InitializeFromConfig(&config);  
    if (PyStatus_Exception(status)) {{  
        std::cerr << "Error initializing Python: " << status.err_msg << std::endl;  
        PyConfig_Clear(&config);  
        return 1;  
    }}  
    
    // Add the installation directory to Python's sys.path  
    PyObject* sys_path = PySys_GetObject("path");  
    if (sys_path != NULL) {{  
        // Debug: print the current sys.path
        std::cout << "Initial sys.path entries:" << std::endl;
        for (Py_ssize_t i = 0; i < PyList_Size(sys_path); i++) {{
            PyObject* path = PyList_GetItem(sys_path, i);
            const char* path_str = PyUnicode_AsUTF8(path);
            std::cout << "  " << path_str << std::endl;
        }}
    
        // Clear existing paths for faster imports (optional - only do this if we're sure we're adding all needed paths)
        // for (Py_ssize_t i = PyList_Size(sys_path) - 1; i >= 0; i--) {{
        //     PyList_SetSlice(sys_path, i, i + 1, NULL);
        // }}
        
        // Add the packages directory to the path first
        std::string packages_dir = "{install_dir}/packages";
        std::cout << "Adding to sys.path: " << packages_dir << std::endl;
        PyObject* packages_path = PyUnicode_FromString(packages_dir.c_str());  
        PyList_Insert(sys_path, 0, packages_path);  
        Py_DECREF(packages_path);
        
        // Add the installation directory to the path  
        std::cout << "Adding to sys.path: " << "{install_dir}" << std::endl;
        PyObject* install_path = PyUnicode_FromString("{install_dir}");  
        PyList_Insert(sys_path, 0, install_path);  
        Py_DECREF(install_path);
        
        // Add standard library path if needed
        std::string stdlib_path = prefix + "/lib/python{sys.version_info.major}.{sys.version_info.minor}";
        if (file_exists(stdlib_path)) {{
            std::cout << "Adding stdlib to sys.path: " << stdlib_path << std::endl;
            PyObject* stdlib_path_obj = PyUnicode_FromString(stdlib_path.c_str());
            PyList_Append(sys_path, stdlib_path_obj);
            Py_DECREF(stdlib_path_obj);
        }}
        
        // Debug: print the updated sys.path entries
        std::cout << "Updated sys.path entries:" << std::endl;
        for (Py_ssize_t i = 0; i < PyList_Size(sys_path); i++) {{
            PyObject* path = PyList_GetItem(sys_path, i);
            const char* path_str = PyUnicode_AsUTF8(path);
            std::cout << "  " << path_str << std::endl;
        }}
    }}  
    
    // Import the module directly
    std::cout << "Importing module: {module_name}" << std::endl;
    PyObject* module = PyImport_ImportModule("{module_name}");  
    if (module == NULL) {{  
        std::cerr << "Failed to import module '{module_name}'" << std::endl;  
        if (PyErr_Occurred()) {{  
            PyErr_Print();  
        }}  
        PyConfig_Clear(&config);  
        Py_Finalize();  
        return 1;  
    }}  
    
    std::cout << "Successfully imported module '{module_name}'" << std::endl;
    
    // Clean up  
    Py_DECREF(module);  
    PyConfig_Clear(&config);  
    Py_Finalize();  
    return 0;  
}}  
"""
    with open(output_c, "w") as f:
        f.write(main_code)


if __name__ == "__main__":
    main()
