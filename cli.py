from collections.abc import Callable
import ctypes.util
import inspect
import multiprocessing
import os
import platform
import shutil
import subprocess
import sys
import sysconfig
from concurrent.futures import ProcessPoolExecutor
from functools import partial
from importlib import import_module
from pathlib import Path
from typing import NewType

import rich_click as click
from typing_extensions import Literal, TypedDict, NewType

from mbcore.more import first_true
from mbcore.display import safe_print, getconsole
from mbcore.collect import Sequence
from mbcore.log import error, info
from mbcore.main import get_help_config
from mb.pkg.graph import _build_dependency_graph  # type: ignore

# Check for Cython
HAS_CYTHON = False
try:
    import cython


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
            return shared_lib

    # 2. ctypes library lookup (cross-platform)
    found_lib = ctypes.util.find_library(
        f"python{platform.python_version_tuple()[0]}.{platform.python_version_tuple()[1]}"
    )
    if found_lib:
        found_lib_path = check_path(found_lib)
        if found_lib_path:
            return found_lib_path

    # 3. macOS: Use `otool -L`
    if sys.platform == "darwin":
        try:
            output = subprocess.check_output(["otool", "-L", sys.executable], text=True)
            for line in output.split("\n"):
                if "libpython" in line:
                    potential_path = check_path(line.split()[0])
                    if potential_path:
                        return potential_path
        except Exception:  # noqa: S110
            pass

        # Try macOS framework paths
        framework_path = Path(sys.base_prefix) / "Python.framework/Versions" / platform.python_version() / "Python"
        framework_lib = check_path(framework_path)
        if framework_lib:
            return framework_lib

    # 4. Linux: Use `ldd`
    elif sys.platform == "linux":
        try:
            output = subprocess.check_output(["ldd", sys.executable], text=True)
            for line in output.split("\n"):
                if "libpython" in line:
                    potential_path = check_path(line.split()[0])
                    if potential_path:
                        return potential_path
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
                return dll_path

    # 6. FreeBSD & Other Unix Variants: Use `ldd`
    elif "bsd" in sys.platform or "unix" in sys.platform:
        try:
            output = subprocess.check_output(["ldd", sys.executable], text=True)
            for line in output.split("\n"):
                if "libpython" in line:
                    potential_path = check_path(line.split()[0])
                    if potential_path:
                        return potential_path
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
            [path.glob("libpython*.so*"), path.glob("libpython*.dylib"), path.glob("python*.dll")]
        ):
            valid_path = check_path(lib)
            if valid_path:
                return valid_path

    # 8. No library found
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
    root_path: str| Path = ".",
    entry: str| Path = "main",
    force: str| Path | bool = False,
    python_library: str| Path = "",
    python_include: str| Path = "",
    install_dir: str| Path = "",
    build_dir: str| Path = "",
    src_dir: str| Path = "",
    modules: Sequence[str | Path] | None = None,
) -> BuildFlags:
    # ROOT_DIR = Path(root_path).absolute()
    # SRC_DIR = ROOT_DIR / (src_dir or f"src/{Path(root_path).stem}")
    # BUILD_DIR = ROOT_DIR / (build_dir or "build")
    # INSTALL_DIR = ROOT_DIR / (install_dir or "install")
    # BIN_DIR = INSTALL_DIR / "bin"
    # LIB_DIR = INSTALL_DIR / "lib"
    # MODULES = [f for f in SRC_DIR.rglob("*.py") if "__init__" not in f.name]

    # OS_NAME = platform.system()


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
    info(f"[RUNNING] ({cmd}) \n {sys._getframe(1).f_code.co_name}{Path(sys._getframe(1).f_code.co_filename).resolve()}:{sys._getframe(1).f_lineno}")
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
    # Removed debug input call to prevent blocking during CLI execution
    # print(f"Hello??? output_dir: {install or FLAGS['INSTALL_DIR']}")
    return default_options


def copytree(src_dir=None, install_dir=None, modules=None):
    """Copy source directory to install directory."""
    global FLAGS

    SRC_DIR = src_dir or FLAGS["SRC_DIR"]
    INSTALL_DIR = install_dir or FLAGS["INSTALL_DIR"]
    MODULES = modules or FLAGS["MODULES"]

    # Preserve the package folder (e.g. "mproc") inside *install/* so that
    # `import mproc` works at runtime.  We copy the **contents** into
    # INSTALL_DIR / SRC_DIR.name.

    pkg_dest = INSTALL_DIR / SRC_DIR.name
    shutil.copytree(
        SRC_DIR,
        pkg_dest,
        dirs_exist_ok=True,
        ignore=shutil.ignore_patterns("*.pyc", "*.pyo", "__pycache__", ".git"),
    )

    # Re-map module file paths to their new location under *install/pkg/*
    return [
        pkg_dest / m.resolve().relative_to(SRC_DIR.resolve())
        for m in MODULES
    ]


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

    modules = [INSTALL_DIR/ m.resolve().relative_to(INSTALL_DIR.resolve()) for m in MODULES]
    from Cython.Build.Dependencies import cythonize
    from contextlib import redirect_stdout, chdir
    from io import StringIO
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
            **{**cmd_options(install=INSTALL_DIR), "quiet": False},
        )
    # output = io.getvalue()
    # input("Output? y/n")
    # if output:
    #     info(output.replace("\install","\src"))
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
        # Copy libpython into the bundle so upgrades on the host system do
        # not break the executable.  We place it under install/lib/ and
        # always link via rpath relative to the executable.

        lib_path_host = Path(PYTHON_LIBRARY).absolute()
        lib_dir = FLAGS["LIB_DIR"]
        lib_dir.mkdir(parents=True, exist_ok=True)

        local_lib = lib_dir / lib_path_host.name
        if not local_lib.exists():
            shutil.copy2(lib_path_host, local_lib)
        lib_path = local_lib

        # Compile the shared library
        cmd = [
            "clang++",
            "-shared",
            "-o", str(output_so),
            str(cpp_path),
            f"-I{PYTHON_INCLUDE}",
            f"-L{lib_dir}",
            f"-l{Path(PYTHON_LIBRARY).stem.replace('lib', '')}",
            "-fPIC",
            f"-Wl,-rpath,{lib_dir}"
        ]

        cmd_str = ' '.join(map(str, cmd))

        try:
            print(f"Compiling shared library: {cmd_str}")
            subprocess.run(cmd_str, shell=True, check=True)

            # Fix the library reference in the compiled shared library
            fix_cmd = [
                "install_name_tool",
                "-change",
                "/install/lib/" + lib_path.name,
                "@rpath/" + lib_path.name,
                str(output_so)
            ]

            fix_cmd_str = ' '.join(map(str, fix_cmd))
            print(f"Fixing library path: {fix_cmd_str}")
            subprocess.run(fix_cmd_str, shell=True, check=True)

            # Verify the library paths
            verify_cmd = ["otool", "-L", str(output_so)]
            verify_cmd_str = ' '.join(map(str, verify_cmd))
            print(f"Verifying library paths: {verify_cmd_str}")
            subprocess.run(verify_cmd_str, shell=True, check=True)

            print(f"✅ Shared library compiled and fixed: {output_so}")
            return 0

        except Exception as e:
            print(f"Error: {e}")
            print(f"❌ Shared library compilation or fix failed")
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

from mbcore.traverse import with_err
@with_err
def parallel_build(modules: list[Path], install_dir: Path | None = None, lib_dir: Path | None = None):
    """Build modules in parallel while respecting dependencies."""
    n_cores = max(1, multiprocessing.cpu_count() - 1)
    info(f"Building with {n_cores} processes")
    INSTALL_DIR = install_dir or FLAGS["INSTALL_DIR"]
    LIB_DIR = lib_dir or FLAGS["LIB_DIR"]
    MODULES = modules or FLAGS["MODULES"]
    with ProcessPoolExecutor(max_workers=n_cores//2) as executor:
        futures = executor.map(partial(compile_shared, install_dir=INSTALL_DIR, lib_dir=LIB_DIR), MODULES)
        for f in futures:
            if f:
                error(f"Compilation failed with return code {f}")

    return 0


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
        **{**cmd_options(install=install_dir),"quiet": False},
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

        if not hasattr(package, '__file__'):
            safe_print(f"⚠️ Package {package_name} has no file attribute, it might be built-in")
            return

        package_file = Path(getattr(package, '__file__', ""))
        if not package_file.exists():
            safe_print(f"⚠️ Could not find package file for {package_name}")
            return

        # Check if this is a single file module or a package with __init__.py
        if package_file.name == '__init__.py':
            # This is a directory package (has __init__.py)
            package_path = package_file.parent
            dest_path = packages_dir / package_name
            safe_print(f"Copying directory package {package_name} from {package_path} to {dest_path}")

            if package_path.exists():
                shutil.copytree(package_path, dest_path, dirs_exist_ok=True)
                safe_print(f"✅ Bundled {package_name}")
            else:
                safe_print(f"❌ Could not find package directory for {package_name}")
        else:
            # Handle single-file modules.  The file can be either a pure-Python
            # ``.py`` *or* a compiled extension module such as ``.so``, ``.pyd``
            # (Windows) or ``.dylib`` (macOS).  We must preserve the original
            # suffix so that the Python import machinery recognises it.

            module_parts = package_name.split('.')
            if len(module_parts) > 1:
                # Create parent dirs for submodules
                parent_path = packages_dir
                for part in module_parts[:-1]:
                    parent_path = parent_path / part
                    parent_path.mkdir(exist_ok=True)
                    # Create __init__.py in parent directory
                    init_file = parent_path / "__init__.py"
                    if not init_file.exists():
                        init_file.touch()

                # Final module file goes in the last directory
                dest_path = parent_path / f"{module_parts[-1]}{package_file.suffix}"
            else:
                # Direct module in root packages dir
                dest_path = packages_dir / f"{package_name}{package_file.suffix}"

            safe_print(f"Copying single file module {package_name} from {package_file} to {dest_path}")

            # Ensure parent directory exists
            dest_path.parent.mkdir(parents=True, exist_ok=True)

            # Copy the module file
            shutil.copy2(package_file, dest_path)

            # Try to copy dist-info directory if it exists
            try:
                # Find site-packages directory
                site_pkg_dir = package_file.parent
                if "site-packages" not in str(site_pkg_dir):
                    for path in sys.path:
                        if "site-packages" in path and Path(path).exists():
                            site_pkg_dir = Path(path)
                            break

                # Look for dist-info directory
                base_name = module_parts[-1] if len(module_parts) > 1 else package_name
                dist_info_pattern = f"{base_name}-*.dist-info"
                dist_info_dirs = list(site_pkg_dir.glob(dist_info_pattern))

                if dist_info_dirs:
                    dist_info_dir = dist_info_dirs[0]
                    dist_info_dest = packages_dir / dist_info_dir.name

                    safe_print(f"Copying dist-info: {dist_info_dir} to {dist_info_dest}")

                    if dist_info_dir.exists():
                        shutil.copytree(dist_info_dir, dist_info_dest, dirs_exist_ok=True)
                        safe_print(f"✅ Bundled dist-info for {package_name}")
            except Exception as e:
                safe_print(f"⚠️ Could not copy dist-info for {package_name}: {e}")

            safe_print(f"✅ Bundled {package_name}")

    except ImportError:
        import traceback
        traceback.print_exc()
        safe_print(f"❌ Could not import {package_name}")
    except Exception as e:
        import traceback
        traceback.print_exc()
        safe_print(f"❌ Error bundling {package_name}: {e}")

ModulePath = NewType("ModulePath",str)
def bundle_and_cythonize(module_path: ModulePath,packages_dir:Path,bundled:list[Path]) -> list[Path]:
        mod = Path(module_path)
        bundle_package(mod.stem, packages_dir)
        newly_bundled = cythonize_dependency(mod.stem, packages_dir)
        bundled.extend(newly_bundled)
        return newly_bundled
def bundler_and_cythonizer(packages_dir: Path,bundled:list[Path]|None=None)-> Callable[[ModulePath], list[Path]]:
    bundled = bundled or []


    return partial(bundle_and_cythonize,packages_dir=packages_dir,bundled=bundled)

def bundle_packages(install_dir: Path, required_packages: list[str], nproc: Literal["auto"]|int=1):
    """Bundle Python packages with the executable by cythonizing them."""
    # Create package directory
    packages_dir = install_dir / "packages"

    # Ensure the directory exists – we no longer purge it here to avoid
    # deleting previously bundled dependencies when *bundle_packages* is
    # invoked multiple times within the same build.

    packages_dir.mkdir(parents=True, exist_ok=True)

    # First copy all packages
    bundled = []
    import sys

    def _should_bundle(name: str) -> bool:
        """Return *True* for third-party / local packages only.

        We consider the *root* import segment when checking against
        ``sys.stdlib_module_names`` so that sub-modules such as
        ``asyncio.base_events`` are correctly recognised as part of the
        standard library.
        """

        root = name.split(".", 1)[0]
        return root not in sys.stdlib_module_names

    # Bundle only the *root* segment of each import so that we copy the full
    # distribution and not just individual sub-modules such as ``click.core``.
    to_bundle = {p.split(".", 1)[0] for p in required_packages if _should_bundle(p)}

    if nproc == "auto" or nproc > 1:
        with multiprocessing.Pool(nproc if nproc != "auto" else (os.cpu_count() or 2) - 1) as pool:
            pool.map(
                bundler_and_cythonizer(packages_dir, bundled),
                [ModulePath(p) for p in sorted(to_bundle)],
            )
    else:
        for package in sorted(to_bundle):
            bundle_package(package, packages_dir)



    return bundled

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

    target_dir = project_module if project_module is not None else SRC_DIR

    # Build the dependency graph.  On some third-party packages (editable
    # installs without a *pyproject.toml*, binary wheels, etc.) the helper in
    # *mbpy* raises ``FileNotFoundError`` or even ``UnicodeDecodeError`` while
    # trying to parse their metadata.  Catch *any* exception so the build
    # continues – we can still collect the project-local imports.

    try:
        # We still want runtime imports inside *site-packages* so transitive
        # dependencies like ``click`` used by ``rich_click`` are discovered.
        gs = _build_dependency_graph(
            str(target_dir),
            site_packages=True,
            inspect_runtime=True,
        )
    except Exception as exc:  # pragma: no cover – defensive catch-all
        safe_print(
            f"⚠️  mbpy.pkg.graph._build_dependency_graph failed: {exc}\n"
            "    Falling back to a source-only graph (site-packages ignored).",
        )

        try:
            gs = _build_dependency_graph(
                str(target_dir),
                site_packages=False,   # skip troublesome third-party dists
                inspect_runtime=False,
            )
        except Exception as exc2:  # last resort
            safe_print(
                f"❌ Graph builder failed again ({exc2}).  Returning no imports.",
            )
            return []

    gs = gs.topo_sort()

    # Iterate through the graph to collect all imports
    for g in gs:
        for node in g.nodes:
            child = g.nodes[node]
            if "imports" in child.content:
                all_imports.extend(child.content["imports"])

    # Post-process: the dependency builder prefixes every external import with
    # the root module name (e.g. "mproc.click").  We strip that prefix so the
    # bundler gets the real top-level package name.

    root_prefix = f"{project_module.name}." if project_module is not None else ""

    cleaned = []
    for imp in all_imports:
        if root_prefix and imp.startswith(root_prefix):
            imp = imp[len(root_prefix):]
        cleaned.append(imp)

    cleaned_unique = list(unique_everseen(cleaned))

    safe_print(f"Found {len(cleaned_unique)} unique imports (after cleaning)")
    safe_print(f"Project module: {project_module}")

    return cleaned_unique


def add_main(entry_point: Path, output_c: Path, python_prefix: str |None = None) -> None:
    """Create a C++ main file that properly initializes Python."""
    install_dir = str(FLAGS["INSTALL_DIR"]) if "INSTALL_DIR" in FLAGS else "./install"

    # Derive the module name from the entry_point relative to install_dir
    rel_path = entry_point.relative_to(Path(install_dir))
    module_name = str(rel_path.with_suffix('')).replace(os.sep, '.')

    main_code = f"""#include <Python.h>
#include <iostream>
#include <filesystem>

int main(int argc, char *argv[]) {{
    // Prepare interpreter configuration.  We keep defaults so that Python
    // sets up its std-lib paths but still override *home*.

    PyConfig config;
    PyConfig_InitPythonConfig(&config);  // zero-initialise structure

    // Set Python home directory
    std::string prefix = "{python_prefix}";
    config.home = Py_DecodeLocale(prefix.c_str(), NULL);
    if (config.home == NULL) {{
        std::cerr << "Fatal error: cannot decode Python home path" << std::endl;
        return 1;
    }}

    // Initialize Python
    PyStatus status = Py_InitializeFromConfig(&config);
    if (PyStatus_Exception(status)) {{
        std::cerr << "Error initializing Python: " << status.err_msg << std::endl;
        PyConfig_Clear(&config);
        return 1;
    }}

    // Prepend our packages and install directories so they take
    // precedence, but keep the standard-library entries that Python
    // initialises – otherwise built-in modules such as *contextlib* or
    // *signal* cannot be imported.

    // Add the packages directory to the path first
    PyObject* sys_path = PySys_GetObject("path");
    if (sys_path != NULL) {{
        // Add the packages directory to the path first
        std::string packages_dir = "{install_dir}/packages";
        PyObject* packages_path = PyUnicode_FromString(packages_dir.c_str());
        PyList_Insert(sys_path, 0, packages_path);
        Py_DECREF(packages_path);

        // Add the installation directory and the compiled-lib directory
        PyObject* install_path = PyUnicode_FromString("{install_dir}");
        PyList_Insert(sys_path, 0, install_path);
        Py_DECREF(install_path);

        std::string lib_dir = "{install_dir}/lib";
        PyObject* lib_path = PyUnicode_FromString(lib_dir.c_str());
        PyList_Insert(sys_path, 0, lib_path);
        Py_DECREF(lib_path);

        // ---- DEBUG: print sys.path to stderr so we can verify search order
        PyObject* repr = PyObject_Repr(sys_path);
        if (repr) {{
            PyObject* bytes = PyUnicode_AsEncodedString(repr, "utf-8", "surrogateescape");
            if (bytes) {{
                fprintf(stderr, "sys.path = %s\n", PyBytes_AS_STRING(bytes));
                Py_DECREF(bytes);
            }}
            Py_DECREF(repr);
        }}
    }}

    // Import the module directly
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

    // Clean up
    Py_DECREF(module);
    PyConfig_Clear(&config);
    Py_Finalize();
    return 0;
}}
"""
    with open(output_c, "w") as f:
        f.write(main_code)


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

    # Start from a clean *packages/* directory once per build.
    pkg_dir = INSTALL_DIR / "packages"
    if pkg_dir.exists():
        shutil.rmtree(pkg_dir)

    bundle_packages(install_dir=INSTALL_DIR, required_packages=imports, nproc="auto")

    # Create the main file
    import platform
    if platform.system() == "Darwin":
        # -----------------------------------------------------------------
        # Bundle libpython so the executable is self-contained
        # -----------------------------------------------------------------

        lib_dir = LIB_DIR
        lib_dir.mkdir(parents=True, exist_ok=True)
        lib_path_host = PYTHON_LIBRARY.resolve()
        lib_path = lib_dir / lib_path_host.name
        if not lib_path.exists():
            shutil.copy2(lib_path_host, lib_path)

        python_prefix = lib_path.parent.parent.as_posix()
        add_main(entry_point, output_c, python_prefix)

        # Collect all shared libraries that need to be linked
        lib_files = list(LIB_DIR.glob("**/*.dylib"))

        # -----------------------------------------------------------------
        # Ensure Python standard library is bundled – required at runtime
        # for codecs and many built-ins.  We copy it once per build.
        # -----------------------------------------------------------------

        import sysconfig

        stdlib_host = Path(sysconfig.get_path("stdlib"))
        stdlib_dest = INSTALL_DIR / "lib" / f"python{sys.version_info.major}.{sys.version_info.minor}"
        if not stdlib_dest.exists():
            shutil.copytree(stdlib_host, stdlib_dest, dirs_exist_ok=True)

        # Build the compiler invocation so that *each* argument is a separate
        # list entry – this avoids the earlier ``FileNotFoundError`` that
        # happened when the entire command string was treated as the
        # executable path.

        compile_cmd: list[str] = [
            "clang++",
            f"-I{PYTHON_INCLUDE}",                # header search path
            str(output_c),                         # main.cpp generated by add_main()
            str(lib_path),                         # link against bundled libpython
            "-Wl,-rpath,@executable_path/../lib",  # look next to executable
        ]

        # Add each package/shim dylib produced earlier.
        compile_cmd.extend(str(lib) for lib in lib_files)

        # Runtime rpath so the executable can find sibling libs + output file
        compile_cmd.extend([
            f"-Wl,-rpath,{INSTALL_DIR}",
            "-o",
            str(output_bin),
        ])

        import subprocess

        try:
            print(f"Compiling with: {' '.join(map(str, compile_cmd))}")
            subprocess.run(compile_cmd, check=True)

            # Fix library references for Python library and all dylibs
            fix_cmds = []
            for lib in lib_files:
                fix_cmd = [
                    "install_name_tool",
                    "-change",
                    "/install/lib/" + lib.name,
                    "@rpath/" + lib.name,
                    str(lib)
                ]
                fix_cmds.append(fix_cmd)

            # Fix the executable itself
            fix_cmd = [
                "install_name_tool",
                "-change",
                "/install/lib/" + lib.name,
                "@rpath/" + lib.name,
                str(output_bin)
            ]
            fix_cmds.append(fix_cmd)

            # Run all the fix commands
            for cmd in fix_cmds:
                print(f"Fixing library path: {' '.join(map(str, cmd))}")
                subprocess.run(cmd, check=True)

            print(f"✅ Executable compiled and fixed in {BIN_DIR}")
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
        compile_cmd.extend([
            f"-Wl,-rpath={PYTHON_LIBRARY.parent}",
            "-o", str(output_bin)
        ])

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
@click.option("--entry", default="main", help="Entry point")
@click.option("--python-library", default="", help="Python library")
@click.option("--python-include", default="", help="Python include directory")
@click.option("--install-dir", default="", help="Output install directory")
@click.option("--build-dir", default="", help="Output build directory")
@click.option("--src-dir", default="", help="Output source directory")
@click.option("--ignore", default="", help="Pattern to ignore")
@click.option("-v", "--verbose", is_flag=True, help="Verbose output")
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
    **kwargs
):
    """Build Python modules into shared libraries."""
    # Prefer the helper from "mbpy" if available, otherwise fall back to
    # Python 3.11+ standard-library "tomllib" so that we do not depend on the
    # optional external package.
    try:
        from mbpy.pkg.toml import load_toml  # type: ignore
    except ImportError:  # pragma: no cover – optional dependency
        import tomllib  # Python 3.11+

        def load_toml(path: Path):  # type: ignore
            """Light-weight replacement for ``mbpy.pkg.toml.load_toml``."""
            with open(path, "rb") as _fp:
                return tomllib.load(_fp)

    from mbcore.collect import getin
    from mbcore.traverse import find_file

    root = Path(root).resolve() if Path(root).exists() else Path.cwd().resolve()
    try:
        project_raw = load_toml(root / "pyproject.toml")

        # Support both the original Result-like return type (with ``unwrap``)
        # and a plain ``dict`` that our fallback loader returns.
        if hasattr(project_raw, "unwrap"):
            _project_cfg = project_raw.unwrap()  # type: ignore[attr-defined]
        else:
            _project_cfg = project_raw  # already a mapping

        src_val = getin(_project_cfg, "tool.mb.src")
        if src_val:
            src_dir = Path(src_val)

        ignore_val = getin(_project_cfg, "tool.mb.ignore")
        if ignore_val is not None:
            ignore = ignore_val

        include_val = getin(_project_cfg, "tool.mb.include")
        if include_val is not None:
            include = include_val

    except (FileNotFoundError, KeyError, TypeError):
        try:
            result = find_file("__init__.py", root)
            if result.error is not None:
                raise result.error
            src_dir = result.result.parent
        except FileNotFoundError:
            error(f"Could not find source directory in {root}. An __init__.py file or pyproject.toml is required.")
            sys.exit(1)
    global FLAGS
    mods = [
        Path(m)
        if Path(m).exists()
        else (Path(src_dir) / m)
        if Path(m).exists()
        else Path(m.replace(".", os.sep)).with_suffix(".py")
        if Path(m.replace(".", os.sep)).with_suffix(".py").exists()
        else Path(src_dir) / Path(m.replace(".", os.sep)).with_suffix(".py")
        for m in modules_files_directories
    ]
    import glob

    # Find all Python modules in the source directory
    mods = [
        Path(m)
        for m in glob.glob(f"{src_dir}/**/*.py", recursive=True)
        if "__init__" not in m and not any(m.match("./.*") for m in mods)
    ]

    # Filter out ignored modules
    if ignore:
        mods = [m for m in mods if not any(m.match(i) for i in ignore)]

    # Include all modules if "*" is specified
    if include and "*" not in include:
        include = [f"*{i}/**/*" if Path(i).is_dir() else f"*{i}*" for i in include]

    # Filter out .git and tests directories
    mods = [
        m
        for m in mods
        if ".git" not in str(m)
        and not any(p == "tests" for p in m.parts)
        and str(m.resolve()) != str(Path(__file__).resolve())
        and "build_executable" not in str(m)
    ]

    # Ensure "src_dir" is always a *Path* instance for the type checker and runtime
    src_dir = Path(str(src_dir or FLAGS["SRC_DIR"]))
    install_dir = Path(str(install_dir or FLAGS["INSTALL_DIR"]))
    build_dir = Path(str(build_dir or FLAGS["BUILD_DIR"]))
    python_library = Path(python_library or FLAGS["PYTHON_LIBRARY"])
    python_include = Path(python_include or FLAGS["PYTHON_INCLUDE"])
    entry = (
        Path(entry.split(":")[0].replace(".", os.sep)).resolve().relative_to(root.resolve()).with_suffix(".py")
    )

    _main(
        embed=embed,
        force=force,
        root=root,
        entry=entry,
        python_library=python_library,
        python_include=python_include,
        install_dir=install_dir,
        build_dir=build_dir,
        src_dir=src_dir,
        modules=mods,
    )


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
    setup_paths(
        root_path=root,
        entry=entry,
        force=force,
        python_library=python_library,
        python_include=python_include,
        install_dir=install_dir,
        build_dir=build_dir,
        src_dir=src_dir,
        modules=modules,
    )

    global FLAGS
    INSTALL_DIR = FLAGS["INSTALL_DIR"]
    MODULES = FLAGS["MODULES"]
    BIN_DIR = FLAGS["BIN_DIR"]
    PYTHON_LIBRARY = FLAGS["PYTHON_LIBRARY"]
    PYTHON_INCLUDE = FLAGS["PYTHON_INCLUDE"]
    MODULES = copytree(src_dir=src_dir, install_dir=INSTALL_DIR, modules=MODULES)

    cythonize_shared(modules=MODULES, install_dir=INSTALL_DIR)
    out = parallel_build(MODULES)
    if out.error is not None:
        # Surface build failure immediately
        raise out.error

    # Construct the path to the entry module **inside** the copied install
    # tree so that ``add_main`` computes the correct dotted module name
    # (e.g. "mproc.main") instead of the previously broken
    # "protocols.py.main".
    entry_point = INSTALL_DIR / entry  # entry already has .py suffix

    if embed:
        compile_executable(entry_point, BIN_DIR, PYTHON_LIBRARY, PYTHON_INCLUDE)

    safe_print(f"✅ Executable compiled in {BIN_DIR}")


if __name__ == "__main__":
    main()