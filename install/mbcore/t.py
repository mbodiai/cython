import ctypes.util
import inspect
import multiprocessing
import os
import platform
import shutil
import site
import subprocess
import sys
import sysconfig
from concurrent.futures import ProcessPoolExecutor
from functools import partial
from importlib import import_module
from inspect import isbuiltin
from pathlib import Path

import rich_click as click
from mbpy.pkg.graph import _build_dependency_graph, print_graph
from typing_extensions import Literal, TypedDict

from mbcore.cache import safe_print
from mbcore.collect import Sequence
from mbcore.display import getconsole
from mbcore.log import error, info
from mbcore.main import get_help_config
from mbcore.more import first_true

# Check for Cython
HAS_CYTHON = False
try:
    import cython
    from Cython.Compiler.Main import CompilationOptions, CompilationResult

    HAS_CYTHON = True
except ImportError:
    HAS_CYTHON = False

    def ccompile(
        source: list[str] | str, options: "CompilationOptions|None" = None, full_module_name: str | None = None, **kwds,
    ) -> "CompilationResult":
        """compile(source [, options], [, <option> = <value>]...).

        Compile one or more Pyrex implementation files, with optional timestamp
        checking and recursing on dependencies.  The source argument may be a string
        or a sequence of strings.  If it is a string and no recursion or timestamp
        checking is requested, a CompilationResult is returned, otherwise a
        CompilationResultSet is returned.
        """  # noqa: D402
        from Cython import basestring
        from Cython.Compiler.Main import CompilationOptions, compile_multiple, compile_single

        options = CompilationOptions(defaults=options, **kwds)
        if isinstance(source, basestring):
            if not options.timestamps:
                return compile_single(source, options, full_module_name)
            source = [source]
        return compile_multiple(source, options)


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
        f"python{platform.python_version_tuple()[0]}.{platform.python_version_tuple()[1]}",
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
            [path.glob("libpython*.so*"), path.glob("libpython*.dylib"), path.glob("python*.dll")],
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
    root_path: str = ".",
    entry: str = "main",
    force: str | bool = False,
    python_library: str = "",
    python_include: str = "",
    install_dir: str = "",
    build_dir: str = "",
    src_dir: str = "",
    modules: Sequence[str | Path] | None = None,
) -> BuildFlags:
    PYTHON_LIBRARY = python_library or find_python_library()
    PYTHON_INCLUDE = python_include or sysconfig.get_path("include")
    ROOT_DIR = Path(root_path).absolute()
    SRC_DIR = ROOT_DIR / (src_dir or f"src/{Path(root_path).stem}")
    BUILD_DIR = ROOT_DIR / (build_dir or "build")
    INSTALL_DIR = ROOT_DIR / (install_dir or "install")
    BIN_DIR = INSTALL_DIR / "bin"
    LIB_DIR = INSTALL_DIR / "lib"
    MODULES = [f for f in SRC_DIR.rglob("*.py") if "__init__" not in f.name]
    OS_NAME = platform.system()
    MODULES = (
        list(map(Path, modules))
        if modules is not None
        else [f for f in SRC_DIR.rglob("*.py") if "__init__" not in f.name]
    )

    # Create directories
    for d in [BUILD_DIR, INSTALL_DIR, BIN_DIR, LIB_DIR]:
        d.mkdir(parents=True, exist_ok=True)
    global FLAGS
    FLAGS.update(
        **{
            "ROOT_DIR": ROOT_DIR,
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

    from Cython.Build.Cythonize import cythonize

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
        package_path = Path(package.__file__).parent
        # Destination path
        dest_path = packages_dir / package_name
        safe_print(f"Copying {package_name} from {package_path} to {dest_path}")

        # Copy the package directory
        if package_path.exists():
            shutil.copytree(package_path, dest_path, dirs_exist_ok=True)
            safe_print(f"✅ Bundled {package_name}")
        else:
            safe_print(f"❌ Could not find package directory for {package_name}")
    except ImportError:
        import traceback

        traceback.print_exc()
        safe_print(f"❌ Could not import {package_name}")
    except Exception as e:
        import traceback

        traceback.print_exc()
        safe_print(f"❌ Error bundling {package_name}: {e}")


def bundle_packages(install_dir: Path, required_packages: list[str], nproc: Literal["auto"] | int = 1):
    """Bundle Python packages with the executable."""
    # Create package directory
    nproc = nproc if nproc != "auto" else (os.cpu_count() or 2) - 1
    packages_dir = install_dir / "packages"
    packages_dir.mkdir(exist_ok=True)

    # Site-packages directories
    site_packages = site.getsitepackages()

    safe_print(f"Looking for packages in: {site_packages}")

    if nproc > 1:
        with multiprocessing.Pool(nproc) as pool:
            pool.map(partial(bundle_package, packages_dir=packages_dir), required_packages)

    else:
        for package in required_packages:
            bundle_package(package, packages_dir)
    return packages_dir


def get_topo_imports() -> list[str]:
    """Get topologically sorted imports from the dependency graph."""
    from mbcore.more import unique_everseen

    # Initialize a list to collect all imports
    all_imports = []

    # Get the dependency graph
    ROOT_DIR = FLAGS["ROOT_DIR"]
    SRC_DIR = FLAGS["SRC_DIR"]
    entry = FLAGS["ENTRY_POINT"]

    # Get the project's root module name from SRC_DIR
    project_module = first_true(
        SRC_DIR.iterdir(),
        lambda x: x.is_dir() and any(f.name == "__init__.py" for f in x.iterdir()),
    )
    gs = _build_dependency_graph(project_module)
    print_graph(gs)
    gs = gs.topo_sort()

    # Iterate through the graph to collect all imports
    for g in gs:
        for node in g.nodes:
            child = g.nodes[node]
            if "imports" in child.content:
                all_imports.extend(child.content["imports"])

    safe_print(f"Found {len(all_imports)} imports")
    safe_print(f"Project module: {project_module}")
    # Return unique imports using the unique_everseen function
    return list(unique_everseen(filter(lambda x: not x.startswith(entry), all_imports)))


def add_main(entry_point: Path, output_c: Path, python_prefix: str = None):
    """Create a C++ main file that properly initializes Python."""
    install_dir = str(FLAGS["INSTALL_DIR"]) if "INSTALL_DIR" in FLAGS else "./install"

    # Derive the module name from the entry_point relative to install_dir
    rel_path = entry_point.relative_to(Path(install_dir))
    module_name = str(rel_path.with_suffix("")).replace(os.sep, ".")

    main_code = f"""#include <Python.h>  
#include <iostream>  
#include <filesystem>  

int main(int argc, char *argv[]) {{  
    PyConfig config;  
    PyConfig_InitPythonConfig(&config);  
    
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
    
    // Add the installation directory to Python's sys.path  
    PyObject* sys_path = PySys_GetObject("path");  
    if (sys_path != NULL) {{  
        // Add the installation directory to the path  
        PyObject* install_path = PyUnicode_FromString("{install_dir}");  
        PyList_Insert(sys_path, 0, install_path);  
        Py_DECREF(install_path);  
        
        // Add the packages directory to the path
        std::string packages_dir = "{install_dir}/packages";
        PyObject* packages_path = PyUnicode_FromString(packages_dir.c_str());  
        PyList_Insert(sys_path, 0, packages_path);  
        Py_DECREF(packages_path);
    }}  
    
    // Import the module  
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
    PYTHON_LIBRARY = python_library if python_library else FLAGS["PYTHON_LIBRARY"]
    PYTHON_INCLUDE = python_include if python_include else FLAGS["PYTHON_INCLUDE"]
    INSTALL_DIR = FLAGS["INSTALL_DIR"]
    BIN_DIR = Path(bin_dir) if bin_dir else FLAGS["BIN_DIR"]

    py_lib_path = Path(PYTHON_LIBRARY)
    if not py_lib_path.is_file():
        error(f"Python library path is not a file: {PYTHON_LIBRARY}")
        return 1

    output_bin = BIN_DIR / (entry_point.stem)
    # Ensure the output directory exists
    BIN_DIR.mkdir(parents=True, exist_ok=True)

    # Create temporary C file with main function
    output_c = BIN_DIR / f"{entry_point.stem}.cpp"

    imports = get_topo_imports()
    bundle_packages(install_dir=INSTALL_DIR, required_packages=imports, nproc="auto")
    import platform

    if platform.system() == "Darwin":
        python_prefix = py_lib_path.parent.parent.as_posix()
        add_main(entry_point, output_c, python_prefix)

        # Compile the executable
        compile_cmd = [
            "clang++",
            str(output_c),
            f"-I{PYTHON_INCLUDE}",
            "-std=c++17",
            str(PYTHON_LIBRARY),
            f"-Wl,-rpath,{py_lib_path.parent}",
            "-o",
            str(output_bin),
        ]

        import subprocess

        try:
            print(f"Compiling with: {' '.join(map(str, compile_cmd))}")
            subprocess.run(compile_cmd, check=True)

            # Check the library paths
            print("Checking library paths before fixing:")
            otool_cmd = ["otool", "-L", str(output_bin)]
            subprocess.run(otool_cmd, check=True)

            # Fix any hardcoded references
            # IMPORTANT: Make sure this path exactly matches what we see in the otool output
            # The path needs to be exactly as it appears in the binary
            fix_cmd = [
                "install_name_tool",
                "-change",
                "/install/lib/libpython3.12.dylib",  # This is the exact path we need to change
                str(PYTHON_LIBRARY),  # This is what we want to change it to
                str(output_bin),
            ]
            print(f"Fixing library path: {' '.join(map(str, fix_cmd))}")
            subprocess.run(fix_cmd, check=True)

            # Verify the fix worked
            print("Checking library paths after fixing:")
            subprocess.run(otool_cmd, check=True)

            print(f"✅ Executable compiled and fixed in {BIN_DIR}")
            return 0
        except subprocess.CalledProcessError as e:
            import traceback

            traceback.print_exc()
            print(f"Error: {e}")
            print("❌ Compilation or library fix failed")
            return 1
    else:
        # Original compilation for Linux/Windows
        python_prefix = str(py_lib_path.parent.parent)
        add_main(entry_point, output_c, python_prefix)

        cmd = " ".join(
            [
                "g++",
                str(output_c),
                f"-I{PYTHON_INCLUDE}",
                f"-L{py_lib_path.parent}",
                f"-l{py_lib_path.stem.replace('lib', '')}",
                f"-Wl,-rpath={py_lib_path.parent}",
                "-o",
                str(output_bin),
            ],
        )

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
@click.option("--entry", default="main", help="Entry point")
@click.option("--python-library", default="", help="Python library")
@click.option("--python-include", default="", help="Python include directory")
@click.option("--install-dir", default="", help="Install directory")
@click.option("--build-dir", default="", help="Build directory")
@click.option("--src-dir", default="", help="Source directory")
@click.option("--ignore", default="", help="Pattern to ignore")
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
    modules_files_directories=[],
    ignore="",
    include="",
):
    """Build Python modules into shared libraries."""
    from mbpy.pkg.toml import load_toml

    from mbcore.collect import getin
    from mbcore.traverse import find_file

    root = Path(root).resolve() if Path(root).exists() else Path.cwd().resolve()
    try:
        project = load_toml(root / "pyproject.toml")
        src_dir = Path(getin(project.unwrap(), "tool.mb.src"))
        ignore = getin(project.unwrap(), "tool.mb.ignore")
        include = getin(project.unwrap(), "tool.mb.include")

    except (FileNotFoundError, KeyError, TypeError):
        try:
            src = find_file("__init__.py", root)
            src_dir = src.parent
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

    mods = [
        Path(m)
        for m in glob.glob(f"{src_dir}/**/*.py", recursive=True)
        if "__init__" not in m and not any(m.match("./.*") for m in mods)
    ]
    if ignore:
        mods = [m for m in mods if not any(m.match(i) for i in ignore)]
    if include and "*" not in include:
        include = [f"*{i}/**/*" if Path(i).is_dir() else f"*{i}*" for i in include]
    mods = [
        m
        for m in mods
        if ".git" not in str(m)
        and not any(p == "tests" for p in m.parts)
        and str(m.resolve()) != str(Path(__file__).resolve())
        and "build_executable" not in str(m)
    ]

    src_dir = src_dir or FLAGS["SRC_DIR"]
    install_dir = install_dir or FLAGS["INSTALL_DIR"]
    build_dir = build_dir or FLAGS["BUILD_DIR"]
    python_library = python_library or FLAGS["PYTHON_LIBRARY"]
    python_include = python_include or FLAGS["PYTHON_INCLUDE"]
    entry = Path(entry.split(":")[0].replace(".", os.sep)).resolve().relative_to(root.resolve()).with_suffix(".py")

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
    FORCE = FLAGS["FORCE"]
    # Build everything in parallel
    MODULES = copytree(src_dir=src_dir, install_dir=INSTALL_DIR, modules=MODULES)

    cythonize_shared(modules=MODULES, install_dir=INSTALL_DIR)
    out = parallel_build(MODULES)
    entry_point = INSTALL_DIR / "mbcore" / "main.py"
    if embed:
        compile_executable(entry_point, BIN_DIR, PYTHON_LIBRARY, PYTHON_INCLUDE)
    safe_print(f"✅ Executable compiled in {BIN_DIR}")


if __name__ == "__main__":
    # safe_print(get_topo_imports("mbcore"))
    main()
