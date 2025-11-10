from __future__ import annotations

import os
import re
import sys
from dataclasses import dataclass
from dataclasses import field as Field
from pathlib import Path
import sysconfig
from typing_extensions import TypedDict, Unpack

from mbcore.display import safe_print





# --- Original Imports ---
import contextlib

from Cython import Utils
from Cython.Compiler import Errors, Options

from Cython.Compiler.Errors import CompileError, PyrexError, error, warning
from Cython.Compiler.Lexicon import (
    unicode_continuation_ch_any,
    unicode_continuation_ch_range,
    unicode_start_ch_any,
    unicode_start_ch_range,
)
from Cython.Compiler.Options import get_directive_defaults
from Cython.Compiler.Scanning import FileSourceDescriptor, PyrexScanner
from Cython.Compiler.StringEncoding import EncodedString
from Cython.Compiler.Symtab import BuiltinScope, ModuleScope

DEBUG = True


def _make_range_re(chrs):
    out = []
    for i in range(0, len(chrs), 2):
        out.append(f"{chrs[i]}-{chrs[i + 1]}")
    return "".join(out)


module_name_pattern = "[{0}{1}][{0}{2}{1}{3}]*".format(
    unicode_start_ch_any,
    _make_range_re(unicode_start_ch_range),
    unicode_continuation_ch_any,
    _make_range_re(unicode_continuation_ch_range),
)
module_name_pattern = re.compile(
    f"{module_name_pattern}(\\.{module_name_pattern})*$")

standard_include_path = os.path.abspath(
    os.path.join(os.path.dirname(os.path.dirname(__file__)), "Includes"))


def find_python_library() -> str | None:
    """Return absolute path to the host CPython shared library.

    The search strategy is intentionally exhaustive because *uv*-managed
    virtual-envs on macOS/Homebrew often break the usual sysconfig hints.
    Logic adapted from ``mb.build`` so that both build helpers rely on the
    same robust implementation.
    """
    import ctypes.util
    import platform
    import subprocess

    def check_path(path: str | os.PathLike) -> str | None:
        p = Path(path)
        return str(p.resolve()) if p.exists() else None

    # 1. Direct hint from sysconfig (works on most Linux distros)
    lib_name = sysconfig.get_config_var("LDLIBRARY") or ""
    lib_dir = Path(sysconfig.get_config_var("LIBDIR") or "")
    if lib_name:
        lib = check_path(lib_dir / lib_name)
        if lib:
            return lib

    # 2. ctypes based lookup (cross-platform)
    found = ctypes.util.find_library(
        f"python{sys.version_info[0]}.{sys.version_info[1]}")
    if found:
        found_lib = check_path(found)
        if found_lib:
            return found_lib

    # 3. macOS: try `otool -L` and framework paths
    if sys.platform == "darwin":
        try:
            output = subprocess.check_output(["otool", "-L", sys.executable], text=True)
            for line in output.splitlines():
                if "libpython" in line:
                    lib = check_path(line.split()[0])
                    if lib:
                        return lib
        except Exception:
            pass  # otool not available or unexpected output
        # Homebrew installs keep the shared library either directly inside the
        # framework directory (…/Versions/<X.Y>/Python) **or** in the sibling
        # ``lib`` sub-directory (…/Versions/<X.Y>/lib/libpythonX.Y.dylib).  Try
        # both locations.
        version_dir = f"{sys.version_info.major}.{sys.version_info.minor}"
        # Determine framework root e.g. /opt/homebrew/opt/python@3.11/Frameworks/Python.framework
        framework_root = Path(sys.base_prefix).parents[1]  # strip .../Versions/<X.Y>
        # ❶ <framework>/Versions/<X.Y>/Python
        framework_lib = framework_root / "Versions" / version_dir / "Python"
        lib = check_path(framework_lib)
        if lib:
            return lib
        # ❷ <framework>/Versions/<X.Y>/lib/libpythonX.Y.dylib
        framework_lib_dylib = Path(sys.base_prefix) / "Python.framework/Versions" / version_dir / "lib" / f"libpython{version_dir}.dylib"
        lib = check_path(framework_lib_dylib)
        if lib:
            return lib

    # 4. Linux: parse `ldd` on the running interpreter
    if sys.platform.startswith("linux"):
        try:
            output = subprocess.check_output(["ldd", sys.executable], text=True)
            for line in output.splitlines():
                if "libpython" in line:
                    lib = check_path(line.split()[0])
                    if lib:
                        return lib
        except Exception:
            pass

    # 5. Windows: common DLL locations
    if sys.platform == "win32":
        py_ver = platform.python_version_tuple()
        for candidate in (
            f"C:\\Windows\\System32\\python{py_ver[0]}{py_ver[1]}.dll",
            f"C:\\Windows\\SysWOW64\\python{py_ver[0]}{py_ver[1]}.dll",
        ):
            lib = check_path(candidate)
            if lib:
                return lib

    # 6. Fallback: scan common lib directories
    common_dirs = [
        Path(getattr(sys, "base_prefix", sys.prefix)) / "lib",
        Path(sys.prefix) / "lib",
        Path("/usr/lib"),
        Path("/usr/local/lib"),
        Path("/opt/homebrew/lib"),
    ]
    for d in common_dirs:
        lib = check_path(d / lib_name)
        if lib:
            return lib

    return None


def validate_path(path: str) -> str:
    return path if path and Path(path).exists() else ""


def get_config_var_wrapper(name, default=""):
    val = sysconfig.get_config_vars().get(name)
    return val if val is not None else default


def get_config_vars_dict():
    base_prefix = getattr(sys, "base_prefix", sys.prefix)
    cfg = {}
    # Use base_prefix for include and library directories:
    cfg["INCDIR"] = validate_path(
        os.path.join(
            base_prefix, "include",
            f"python{sys.version_info.major}.{sys.version_info.minor}"), )
    cfg["LIBDIR1"] = validate_path(os.path.join(base_prefix, "lib"))
    cfg["LIBDIR2"] = validate_path(
        os.path.join(
            base_prefix,
            "lib",
            f"python{sys.version_info.major}.{sys.version_info.minor}",
            f"config-{sys.platform}",
        ), )
    # Get PYLIB and PYLIB_DYN from sysconfig (they might still be filenames)
    cfg["PYLIB"] = get_config_var_wrapper("LIBRARY")
    cfg["PYLIB_DYN"] = get_config_var_wrapper("LDLIBRARY")
    # Use environment or defaults for the rest:
    cfg["CC"] = os.environ.get("CC", get_config_var_wrapper("CC"))
    cfg["CFLAGS"] = (get_config_var_wrapper("CFLAGS") + " " +
                     os.environ.get("CFLAGS", "")).strip()
    cfg["LINKCC"] = os.environ.get("LINKCC",
                                   get_config_var_wrapper("LINKCC", cfg["CC"]))
    cfg["LIBS"] = get_config_var_wrapper("LIBS")
    cfg["SYSLIBS"] = get_config_var_wrapper("SYSLIBS")
    cfg["LINKFORSHARED"] = get_config_var_wrapper("LINKFORSHARED")
    cfg["EXE_EXT"] = get_config_var_wrapper("EXE")
    return cfg


CONFIG = get_config_vars_dict()

INCDIR = CONFIG["INCDIR"]
LIBDIR1 = CONFIG["LIBDIR1"]
LIBDIR2 = CONFIG["LIBDIR2"]
PYLIB = CONFIG["PYLIB"]
PYLIB_DYN = find_python_library() or CONFIG["PYLIB_DYN"]
CC = CONFIG["CC"]
CFLAGS = CONFIG["CFLAGS"]
LINKCC = CONFIG["LINKCC"]
LIBS = CONFIG["LIBS"]
SYSLIBS = CONFIG["SYSLIBS"]
LINKFORSHARED = CONFIG["LINKFORSHARED"]
EXE_EXT = CONFIG["EXE_EXT"]

if not INCDIR:
    raise FileNotFoundError("Python include directory not found.")
if not (LIBDIR1 or LIBDIR2):
    raise FileNotFoundError("Python library directory not found.")
if not PYLIB_DYN:
    raise FileNotFoundError("Python shared library (libpythonX.Y) not found.")


def resolve_mac_executable_path(libpath: str) -> str:
    if libpath.startswith("@executable_path"):
        exe_dir = Path(sys.executable).resolve().parent
        relative_part = libpath.replace("@executable_path/", "")
        resolved = (exe_dir / relative_part).resolve()
        if not resolved.exists():
            raise FileNotFoundError(
                f"Resolved path '{resolved}' does not exist for '{libpath}'.")
        return str(resolved)
    return libpath


def _debug(msg, *args):
    if DEBUG:
        sys.stderr.write((msg % args) + "\n")


def find_all_libpython_paths() -> list:
    candidate_dirs = [
        Path(getattr(sys, "base_prefix", sys.prefix)) / "lib",
        Path(sys.prefix) / "lib",
        Path("/usr/lib"),
        Path("/usr/local/lib"),
        Path("/opt/homebrew/lib"),
    ]
    found_paths = set()
    patterns = [
        f"libpython{sys.version_info.major}.{sys.version_info.minor}*.dylib",
        f"libpython{sys.version_info.major}.{sys.version_info.minor}*.so",
    ]
    for base in candidate_dirs:
        if base.exists():
            for pattern in patterns:
                for lib in base.rglob(pattern):
                    try:
                        if lib.exists():
                            found_paths.add(lib.resolve())
                    except Exception:
                        if DEBUG:
                            pass
    return sorted(found_paths)


def dump_config() -> None:
    _debug("Dumping configuration:")
    for key, value in CONFIG.items():
        _debug("  %s: %s", key, value)
    _debug("Resolved PYLIB_DYN: %s", PYLIB_DYN)
    _debug("")
    libpython_paths = find_all_libpython_paths()
    if libpython_paths:
        _debug("Found dynamic library paths:")
        for p in libpython_paths:
            _debug("  %s", p)
    else:
        _debug("No dynamic library paths found.")


def _parse_args(args):
    cy_args = []
    last_arg = None
    for i, arg in enumerate(args):
        if arg.startswith("-") or last_arg in ("-X", "--directive"):
            cy_args.append(arg)
        else:
            input_file = arg
            remaining = args[i + 1:]
            return input_file, cy_args, remaining
        last_arg = arg
    return None


def runcmd(cmd, shell=False):
    """Run a shell command safely."""
    import subprocess

    cmd_str = " ".join(cmd) if isinstance(cmd, list) else cmd
    _debug(f"🔥 Running: {cmd_str}")

    try:
        result = subprocess.run(
            cmd,
            shell=shell,
            capture_output=True,
            text=True,
            check=False
        )

        if result.stdout:
            safe_print(result.stdout, end="")

        if result.returncode != 0:
            _debug(f"🚨 ERROR: Command failed with exit code {result.returncode}")
            if result.stderr:
                _debug(f"❌ STDERR:\n{result.stderr}")
            sys.exit(result.returncode)

        return result.stdout.strip() if result.stdout else ""
    except Exception as e:
        _debug(f"🚨 ERROR: Failed to run command: {e}")
        sys.exit(1)


def compile_shared(
    cpp_path: Path,
    *,
    install_dir: Path | None = None,
    lib_dir: Path | None = None,
    force: bool = False,
) -> int:
    """Compile *cpp_path* into a shared library (.so/.dylib/.pyd).

    Mirrors the original helper in ``mb.build`` so that both call sites use a
    single implementation. The output path preserves the package directory
    layout when *install_dir*/*lib_dir* are supplied, matching the previous
    behaviour.

    Note: cpp_path can be either a .py file (will look for corresponding .cpp)
    or a .cpp file directly.
    """
    include_dir = Path(sysconfig.get_paths()["include"])
    from mbcore.log import error
    python_lib = Path(find_python_library() or "")
    if not python_lib.exists():
        error("⚠️ Could not locate libpython; aborting shared compilation")
        return 1

    # Handle case where we're passed a .py file instead of .cpp
    actual_cpp_path = cpp_path
    if cpp_path.suffix == ".py":
        # Look for corresponding .cpp file in the same directory
        potential_cpp = cpp_path.with_suffix(".cpp")
        if potential_cpp.exists():
            actual_cpp_path = potential_cpp
        else:
            error(f"⚠️ No corresponding .cpp file found for {cpp_path}")
            return 1

    ext_suffix = sysconfig.get_config_var("EXT_SUFFIX") or ".so"

    if install_dir and lib_dir:
        # Use original cpp_path for relative path calculation
        output_so = Path(lib_dir) / cpp_path.relative_to(install_dir).with_suffix(ext_suffix)
    else:
        output_so = cpp_path.with_suffix(ext_suffix)

    output_so.parent.mkdir(parents=True, exist_ok=True)

    # Skip up-to-date files unless forced
    if (
        output_so.exists()
        and actual_cpp_path.stat().st_mtime <= output_so.stat().st_mtime
        and not force
    ):
        _debug("[SKIP] %s is up-to-date", output_so)
        return 0

    if sys.platform == "darwin":
        compiler = "clang++"
        lib_path = python_lib
        lib_dir_path = lib_path.parent
        # For framework Python, link directly to the framework binary
        cmd = [
            compiler,
            "-shared",
            "-o",
            str(output_so),
            str(actual_cpp_path),
            f"-I{include_dir}",
            str(lib_path),  # Link directly to the framework Python binary
            "-fPIC",
            f"-Wl,-rpath,{lib_dir_path}",
        ]
        runcmd(cmd)

        # Fix install_name on macOS so the library uses an absolute path
        try:
            fix_cmd = [
                "install_name_tool",
                "-change",
                "/install/lib/libpython3.12.dylib",
                str(lib_path),
                str(output_so),
            ]
            runcmd(fix_cmd)
        except Exception:
            # Non-fatal; continue
            _debug("install_name_tool failed – continuing")
            pass
    else:
        compiler = "g++"
        cmd = [
            compiler,
            "-shared",
            "-o",
            str(output_so),
            str(actual_cpp_path),
            f"-I{include_dir}",
            f"-L{python_lib.parent}",
            f"-l{python_lib.stem.replace('lib', '')}",
            "-fPIC",
        ]
        runcmd(cmd)

    return 0


def clink(basename) -> None:
    link_args = [LINKCC, "-o", basename + EXE_EXT, basename + ".o"]

    if LIBDIR1:
        link_args.append("-L" + LIBDIR1)
    if LIBDIR2:
        link_args.append("-L" + LIBDIR2)

    if PYLIB_DYN:
        link_args.append(
            PYLIB_DYN)  # Explicitly add the Python dynamic library
    else:
        _debug("⚠️ WARNING: PYLIB_DYN is missing!")

    if LINKFORSHARED:
        link_args.extend(LINKFORSHARED.split())
    if LIBS:
        link_args.extend(LIBS.split())
    if SYSLIBS:
        link_args.extend(SYSLIBS.split())

    _debug("Final link command: %s", " ".join(link_args))
    runcmd(link_args)


def ccompile(basename) -> None:
    # Determine whether the generated file is C++ (.cpp) or C (.c)
    cpp_file = Path(basename + ".cpp")
    c_file = Path(basename + ".c")
    if cpp_file.exists():
        source_file = str(cpp_file)
        compiler = "clang++"  # Use clang++ for C++ sources
    elif c_file.exists():
        source_file = str(c_file)
        compiler = CC  # Use your configured C compiler
    else:
        raise FileNotFoundError(
            f"Neither {basename + '.cpp'} nor {basename + '.c'} exists.")
    # Compile the source file into an object file.
    cmd = [compiler, "-c", "-o", basename + ".o", source_file, "-I" + INCDIR
           ] + CFLAGS.split()
    _debug("ccompile cmd: %s", " ".join(cmd))
    runcmd(cmd)


def cycompile(input_file, options=()) -> None:
    from Cython.Compiler import CmdLine, Main, Version

    options, sources = CmdLine.parse_command_line(
        list(options) + ["--embed", input_file])
    _debug("Using Cython %s to compile %s", Version.version, input_file)
    result = Main.compile(sources, options)
    if result.num_errors > 0:
        sys.exit(1)


def exec_file(program_name, args=()) -> None:
    runcmd([str(Path(program_name).resolve())] + list(args), shell=False)


def build(input_file, compiler_args=(), force=False):
    basename = os.path.splitext(input_file)[0]
    exe_file = basename + EXE_EXT
    if not force and os.path.abspath(exe_file) == os.path.abspath(input_file):
        raise ValueError(
            "Input and output file names are the same, refusing to overwrite")
    if (not force and os.path.exists(exe_file) and os.path.exists(input_file)
            and os.path.getmtime(input_file) <= os.path.getmtime(exe_file)):
        _debug("File is up to date, not regenerating %s", exe_file)
        return exe_file
    cycompile(input_file, compiler_args)
    ccompile(basename)
    clink(basename)
    return exe_file


class CompilerDerecitves(TypedDict, total=False):
    binding: bool
    embedsignature: bool
    c_string_type: str
    c_string_encoding: str
    c_string_type_encoding: str
    c_string_encoding_errors: str
    c_string_type_errors: str


class CompilationKwargs(TypedDict, total=False):
    show_version: int
    use_listing_file: int
    errors_to_stderr: int
    cplus: int
    output_file: str | None
    depfile: str | None
    annotate: str | None
    annotate_coverage_xml: str | None
    generate_pxi: int
    capi_reexport_cincludes: int
    working_path: str
    timestamps: dict | None
    verbose: int
    quiet: int
    compiler_directives: CompilerDerecitves
    embedded_metadata: dict
    evaluate_tree_assertions: bool
    emit_linenums: bool
    relative_path_in_code_position_comments: bool
    c_line_in_traceback: bool
    language_level: int | None
    formal_grammar: bool
    gdb_debug: bool
    compile_time_env: dict | None
    module_name: str | None
    common_utility_include_dir: str | None
    output_dir: str | None
    build_dir: str | None
    cache: str | None
    create_extension: bool | None
    np_pythran: bool
    legacy_implicit_noexcept: bool | None


@dataclass
class CompilationOptions(dict):
    show_version: int = Field()
    use_listing_file: int = Field()
    errors_to_stderr: int = Field()
    cplus: int = Field()
    output_file: str | None = Field()
    depfile: str | None = Field()
    annotate: str | None = Field()
    annotate_coverage_xml: str | None = Field()
    generate_pxi: int = Field()
    capi_reexport_cincludes: int = Field()
    working_path: str = Field()
    timestamps: dict | None = Field()
    verbose: int = Field()
    quiet: int = Field()
    compiler_directives: CompilerDerecitves = Field()
    embedded_metadata: dict = Field()
    evaluate_tree_assertions: bool = Field()
    emit_linenums: bool = Field()
    relative_path_in_code_position_comments: bool = Field()
    c_line_in_traceback: bool = Field()
    language_level: int | None = Field()
    formal_grammar: bool = Field()
    gdb_debug: bool = Field()
    compile_time_env: dict | None = Field()
    module_name: str | None = Field()
    common_utility_include_dir: str | None = Field()
    output_dir: str | None = Field()
    build_dir: str | None
    cache: str | None = Field()
    create_extension: bool | None = Field()
    np_pythran: bool
    legacy_implicit_noexcept: bool | None = Field()

    def __init__(self,
                 defaults: CompilationKwargs | None = None,
                 **kw: Unpack[CompilationKwargs]):
        self.include_path = []
        if defaults:
            if isinstance(defaults, CompilationOptions):
                defaults = defaults.__dict__
        else:
            defaults = default_options

        options = dict(defaults)
        options.update(kw)

        # let's assume 'default_options' contains a value for most known compiler options
        # and validate against them
        unknown_options = set(options) - set(default_options)
        # ignore valid options that are not in the defaults
        unknown_options.difference_update(["include_path"])
        if unknown_options:
            message = "got unknown compilation option{}, please remove: {}".format(
                "s" if len(unknown_options) > 1 else "",
                ", ".join(unknown_options),
            )
            raise ValueError(message)

        directive_defaults = get_directive_defaults()
        directives = dict(options["compiler_directives"])  # copy mutable field
        # check for invalid directives
        unknown_directives = set(directives) - set(directive_defaults)
        if unknown_directives:
            message = "got unknown compiler directive{}: {}".format(
                "s" if len(unknown_directives) > 1 else "",
                ", ".join(unknown_directives),
            )
            raise ValueError(message)
        options["compiler_directives"] = directives
        if directives.get("np_pythran", False) and not options["cplus"]:
            import warnings

            warnings.warn("C++ mode forced when in Pythran mode!",
                          stacklevel=2)
            options["cplus"] = True
        if "language_level" not in kw and directives.get("language_level"):
            options["language_level"] = directives["language_level"]
        elif not options.get("language_level"):
            options["language_level"] = directive_defaults.get(
                "language_level")
        if "formal_grammar" in directives and "formal_grammar" not in kw:
            options["formal_grammar"] = directives["formal_grammar"]
        if options["cache"] is True:
            options["cache"] = os.path.join(Utils.get_cython_cache_dir(),
                                            "compiler")

        self.__dict__.update(options)

    def configure_language_defaults(self, source_extension: str) -> None:
        if source_extension == "py" and self.compiler_directives.get(
                "binding") is None:
            self.compiler_directives["binding"] = True

    def get_fingerprint(self):
        """Return a string that contains all the options that are relevant for cache invalidation."""
        # Collect only the data that can affect the generated file(s).
        data = {}

        for key, value in self.__dict__.items():
            if key in ["show_version", "errors_to_stderr", "verbose", "quiet"]:
                # verbosity flags have no influence on the compilation result
                continue
            if key in ["output_file", "output_dir"]:
                # ignore the exact name of the output file
                continue
            if key in ["depfile"]:
                # external build system dependency tracking file does not influence outputs
                continue
            if key in ["timestamps"]:
                # the cache cares about the content of files, not about the timestamps of sources
                continue
            if key in ["cache"]:
                # hopefully caching has no influence on the compilation result
                continue
            if key in ["compiler_directives"]:
                # directives passed on to the C compiler do not influence the generated C code
                continue
            if key in ["include_path"]:
                # this path changes which headers are tracked as dependencies,
                # it has no influence on the generated C code
                continue
            if key in ["working_path"]:
                # this path changes where modules and pxd files are found;
                # their content is part of the fingerprint anyway, their
                # absolute path does not matter
                continue
            if key in ["create_extension"]:
                # create_extension() has already mangled the options, e.g.,
                # embedded_metadata, when the fingerprint is computed so we
                # ignore it here.
                continue
            if key in ["build_dir"]:
                # the (temporary) directory where we collect dependencies
                # has no influence on the C output
                continue
            if key in [
                    "use_listing_file", "generate_pxi", "annotate",
                    "annotate_coverage_xml"
            ]:
                # all output files are contained in the cache so the types of
                # files generated must be part of the fingerprint
                data[key] = value
            elif key in ["formal_grammar", "evaluate_tree_assertions"]:
                # these bits can change whether compilation to C passes/fails
                data[key] = value
            elif key in [
                    "embedded_metadata",
                    "emit_linenums",
                    "c_line_in_traceback",
                    "gdb_debug",
                    "relative_path_in_code_position_comments",
            ]:
                # the generated code contains additional bits when these are set
                data[key] = value
            elif key in [
                    "cplus", "language_level", "compile_time_env", "np_pythran"
            ]:
                # assorted bits that, e.g., influence the parser
                data[key] = value
            elif key == ["capi_reexport_cincludes"]:
                if self.capi_reexport_cincludes:
                    # our caching implementation does not yet include fingerprints of all the header files
                    raise NotImplementedError(
                        "capi_reexport_cincludes is not compatible with Cython caching"
                    )
            elif key == ["common_utility_include_dir"]:
                if self.common_utility_include_dir:
                    raise NotImplementedError(
                        "common_utility_include_dir is not compatible with Cython caching yet"
                    )
            else:
                # any unexpected option should go into the fingerprint; it's better
                # to recompile than to return incorrect results from the cache.
                data[key] = value

        def to_fingerprint(item):
            """Recursively turn item into a string, turning dicts into lists with deterministic ordering."""
            if isinstance(item, dict):
                item = sorted([(repr(key), to_fingerprint(value))
                               for key, value in item.items()])
            return repr(item)

        return to_fingerprint(data)


# ------------------------------------------------------------------------
#
#  Set the default options depending on the platform
#
# ------------------------------------------------------------------------

default_options: CompilationKwargs = {
    "show_version": 0,
    "use_listing_file": 0,
    "errors_to_stderr": 1,
    "cplus": 0,
    "output_file": None,
    "depfile": None,
    "annotate": None,
    "annotate_coverage_xml": None,
    "generate_pxi": 0,
    "capi_reexport_cincludes": 0,
    "working_path": "",
    "timestamps": None,
    "verbose": 0,
    "quiet": 0,
    "compiler_directives": {},
    "embedded_metadata": {},
    "evaluate_tree_assertions": False,
    "emit_linenums": False,
    "relative_path_in_code_position_comments": True,
    "c_line_in_traceback": True,
    "language_level": None,  # warn but default to 2
    "formal_grammar": False,
    "gdb_debug": False,
    "compile_time_env": None,
    "module_name": None,
    "common_utility_include_dir": None,
    "output_dir": None,
    "build_dir": None,
    "cache": None,
    "create_extension": None,
    "np_pythran": False,
    "legacy_implicit_noexcept": None,
}


@dataclass
class Context:
    cython_scope: ModuleScope | None = None
    language_level: int | None = None
    future_directives: set = Field(default_factory=set)
    compiler_directives: dict = Field(default_factory=dict)
    include_directories: list = Field(default_factory=list)
    cpp: bool = False
    options: CompilationOptions | None = Field(default=None)
    modules: dict[str,
                  BuiltinScope | CythonScope.CythonScope] = Field(default_factory=dict)
    pxds: dict = Field(default_factory=dict)
    _interned: dict = Field(default_factory=dict)
    legacy_implicit_noexcept: bool = False
    gdb_debug_outputwriter: object | None = None

    def __init__(self,
                 include_directories,
                 compiler_directives,
                 cpp=False,
                 language_level=None,
                 options=None):
        from Cython.Compiler import Builtin, CythonScope

        self.modules = {
            "__builtin__": Builtin.builtin_scope
        }
        self.cython_scope = CythonScope.create_cython_scope(self)
        self.modules["cython"] = self.cython_scope
        self.include_directories = include_directories
        self.future_directives = set()
        self.compiler_directives = compiler_directives
        self.cpp = cpp
        self.options = options
        self.pxds = {}
        self._interned = {}
        if language_level is not None:
            self.set_language_level(language_level)
        self.legacy_implicit_noexcept = self.compiler_directives.get(
            "legacy_implicit_noexcept", False)
        self.gdb_debug_outputwriter = None

    @classmethod
    def from_options(cls, options: CompilationOptions):
        return cls(
            options.include_path,
            options.compiler_directives,
            bool(options.cplus),
            options.language_level,
            options=options,
        )

    def set_language_level(self, level) -> None:
        from Cython.Compiler.Future import absolute_import, division, generator_stop, print_function, unicode_literals

        future_directives = set()
        if level == "3str":
            level = 3
        else:
            level = int(level)
            if level >= 3:
                future_directives.add(unicode_literals)
        if level >= 3:
            future_directives.update(
                [print_function, absolute_import, division, generator_stop])
        self.language_level = level
        self.future_directives = future_directives
        if level >= 3:
            self.modules["builtins"] = self.modules["__builtin__"]

    def intern_ustring(self, value, encoding=None) -> EncodedString:
        key = (EncodedString, value, encoding)
        try:
            return self._interned[key]
        except KeyError:
            pass
        value = EncodedString(value)
        if encoding:
            value.encoding = encoding
        self._interned[key] = value
        return value

    def process_pxd(self, source_desc: FileSourceDescriptor,
                    scope: ModuleScope, module_name: str) -> tuple | None:
        from Cython.Compiler import Pipeline

        if isinstance(
                source_desc,
                FileSourceDescriptor) and source_desc._file_type == "pyx":
            source = CompilationSource(source_desc, module_name, os.getcwd())
            result_sink = create_default_resultobj(source, self.options)
            pipeline = Pipeline.create_pyx_as_pxd_pipeline(self, result_sink)
            result = Pipeline.run_pipeline(pipeline, source)
        else:
            pipeline = Pipeline.create_pxd_pipeline(self, scope, module_name)
            result = Pipeline.run_pipeline(pipeline, source_desc)
        return result

    def nonfatal_error(self, exc):
        return Errors.report_error(exc)

    def _split_qualified_name(self, qualified_name, relative_import=False):
        qualified_name_parts = qualified_name.split(".")
        last_part = qualified_name_parts.pop()
        qualified_name_parts = [(p, True) for p in qualified_name_parts]
        if last_part != "__init__":
            is_package = False
            for suffix in (".py", ".pyx"):
                path = self.search_include_directories(
                    qualified_name,
                    suffix=suffix,
                    source_pos=None,
                    source_file_path=None,
                    sys_path=not relative_import,
                )
                if path:
                    is_package = self._is_init_file(path)
                    break
            qualified_name_parts.append((last_part, is_package))
        return qualified_name_parts

    @staticmethod
    def _is_init_file(path):
        return os.path.basename(path) in ("__init__.pyx", "__init__.py",
                                          "__init__.pxd") if path else False

    @staticmethod
    def _check_pxd_filename(pos, pxd_pathname, qualified_name) -> None:
        if not pxd_pathname:
            return
        pxd_filename = os.path.basename(pxd_pathname)
        if "." in qualified_name and qualified_name == os.path.splitext(
                pxd_filename)[0]:
            warning(
                pos,
                f"Dotted filenames ('{pxd_filename}') are deprecated. Please use the normal Python package directory layout.",
                level=1,
            )

    def find_module(
        self,
        module_name,
        from_module=None,
        pos=None,
        need_pxd=1,
        absolute_fallback=True,
        relative_import=False,
    ):
        debug_find_module = 0
        if debug_find_module:
            pass
        scope = None
        pxd_pathname = None
        if from_module:
            if module_name:
                qualified_name = from_module.qualify_name(module_name)
            else:
                qualified_name = from_module.qualified_name
                scope = from_module
                from_module = None
        else:
            qualified_name = module_name
        if not module_name_pattern.match(qualified_name):
            raise CompileError(pos or (module_name, 0, 0),
                               f"'{module_name}' is not a valid module name")
        if from_module:
            if debug_find_module:
                pass
            scope = from_module.lookup_submodule(module_name)
            if not scope:
                pxd_pathname = self.find_pxd_file(qualified_name,
                                                  pos,
                                                  sys_path=not relative_import)
                self._check_pxd_filename(pos, pxd_pathname, qualified_name)
                if pxd_pathname:
                    is_package = self._is_init_file(pxd_pathname)
                    scope = from_module.find_submodule(module_name,
                                                       as_package=is_package)
        if not scope:
            if debug_find_module:
                pass
            if absolute_fallback:
                qualified_name = module_name
            scope = self
            for name, is_package in self._split_qualified_name(
                    qualified_name, relative_import=relative_import):
                scope = scope.find_submodule(name, as_package=is_package)
        if debug_find_module:
            pass
        if not scope.pxd_file_loaded:
            if debug_find_module:
                pass
            if not pxd_pathname:
                if debug_find_module:
                    pass
                pxd_pathname = self.find_pxd_file(qualified_name,
                                                  pos,
                                                  sys_path=need_pxd
                                                  and not relative_import)
                self._check_pxd_filename(pos, pxd_pathname, qualified_name)
                if debug_find_module:
                    pass
                if not pxd_pathname and need_pxd:
                    scope.pxd_file_loaded = True
                    package_pathname = self.search_include_directories(
                        qualified_name,
                        suffix=".py",
                        source_pos=pos,
                        sys_path=not relative_import,
                    )
                    if package_pathname and package_pathname.endswith(
                            Utils.PACKAGE_FILES):
                        pass
                    else:
                        error(
                            pos, "'{}.pxd' not found".format(
                                qualified_name.replace(".", os.sep)))
            if pxd_pathname:
                scope.pxd_file_loaded = True
                try:
                    if debug_find_module:
                        pass
                    rel_path = module_name.replace(
                        ".", os.sep) + os.path.splitext(pxd_pathname)[1]
                    if not pxd_pathname.endswith(rel_path):
                        rel_path = pxd_pathname
                    source_desc = FileSourceDescriptor(pxd_pathname, rel_path)
                    err, result = self.process_pxd(source_desc, scope,
                                                   qualified_name)
                    if err:
                        raise err
                    (pxd_codenodes, pxd_scope) = result
                    self.pxds[module_name] = (pxd_codenodes, pxd_scope)
                except CompileError:
                    pass
        return scope

    def find_pxd_file(self,
                      qualified_name,
                      pos=None,
                      sys_path=True,
                      source_file_path=None):
        pxd = self.search_include_directories(
            qualified_name,
            suffix=".pxd",
            source_pos=pos,
            sys_path=sys_path,
            source_file_path=source_file_path,
        )
        if pxd is None and Options.cimport_from_pyx:
            return self.find_pyx_file(qualified_name, pos, sys_path=sys_path)
        return pxd

    def find_pyx_file(self,
                      qualified_name,
                      pos=None,
                      sys_path=True,
                      source_file_path=None):
        return self.search_include_directories(
            qualified_name,
            suffix=".pyx",
            source_pos=pos,
            sys_path=sys_path,
            source_file_path=source_file_path,
        )

    def find_include_file(self, filename, pos=None, source_file_path=None):
        path = self.search_include_directories(
            filename,
            source_pos=pos,
            include=True,
            source_file_path=source_file_path,
        )
        if not path:
            error(pos, f"'{filename}' not found")
        return path

    def search_include_directories(
        self,
        qualified_name,
        suffix=None,
        source_pos=None,
        include=False,
        sys_path=False,
        source_file_path=None,
    ):
        include_dirs = self.include_directories
        if sys_path:
            include_dirs = include_dirs + sys.path
        include_dirs = tuple(include_dirs + [standard_include_path])
        return search_include_directories(
            include_dirs,
            qualified_name,
            suffix or "",
            source_pos,
            include,
            source_file_path,
        )

    def find_root_package_dir(self, file_path):
        return Utils.find_root_package_dir(file_path)

    def check_package_dir(self, dir, package_names):
        return Utils.check_package_dir(dir, tuple(package_names))

    def c_file_out_of_date(self, source_path, output_path) -> int:
        if not os.path.exists(output_path):
            return 1
        c_time = Utils.modification_time(output_path)
        if Utils.file_newer_than(source_path, c_time):
            return 1
        pxd_path = Utils.replace_suffix(source_path, ".pxd")
        if os.path.exists(pxd_path) and Utils.file_newer_than(
                pxd_path, c_time):
            return 1
        for kind, name in self.read_dependency_file(source_path):
            if kind == "cimport":
                dep_path = self.find_pxd_file(name,
                                              source_file_path=source_path)
            elif kind == "include":
                dep_path = self.search_include_directories(
                    name, source_file_path=source_path)
            else:
                continue
            if dep_path and Utils.file_newer_than(dep_path, c_time):
                return 1
        return 0

    def find_cimported_module_names(self, source_path):
        return [
            name for kind, name in self.read_dependency_file(source_path)
            if kind == "cimport"
        ]

    def is_package_dir(self, dir_path):
        return Utils.is_package_dir(dir_path)

    def read_dependency_file(self, source_path):
        dep_path = Utils.replace_suffix(source_path, ".dep")
        if os.path.exists(dep_path):
            with open(dep_path, encoding="utf-8") as f:
                return [
                    line.split(" ", 1) for line in (l.strip() for l in f)
                    if " " in line
                ]
        return ()

    def lookup_submodule(self, name):
        return self.modules.get(name, None)

    def find_submodule(self, name, as_package=False):
        scope = self.lookup_submodule(name)
        if not scope:
            scope = ModuleScope(name,
                                parent_module=None,
                                context=self,
                                is_package=as_package)
            self.modules[name] = scope
        return scope

    def parse(self, source_desc, scope, pxd, full_module_name):
        if not isinstance(source_desc, FileSourceDescriptor):
            raise RuntimeError("Only file sources for code supported")
        source_filename = source_desc.filename
        scope.cpp = self.cpp
        num_errors = Errors.get_errors_count()
        try:
            with Utils.open_source_file(source_filename) as f:
                from . import Parsing

                s = PyrexScanner(f,
                                 source_desc,
                                 source_encoding=f.encoding,
                                 scope=scope,
                                 context=self)
                tree = Parsing.p_module(s, pxd, full_module_name)
                if self.options.formal_grammar:
                    try:
                        from ..Parser import ConcreteSyntaxTree
                    except ImportError:
                        raise RuntimeError(
                            "Formal grammar can only be used with compiled Cython with an available pgen.",
                        )
                    ConcreteSyntaxTree.p_module(source_filename)
        except UnicodeDecodeError as e:
            raise self._report_decode_error(source_desc, e)
        if Errors.get_errors_count() > num_errors:
            raise CompileError()
        return tree

    def _report_decode_error(self, source_desc, exc):
        msg = exc.args[-1]
        position = exc.args[2]
        encoding = exc.args[0]
        line = 1
        column = idx = 0
        with open(source_desc.filename, encoding="iso8859-1", newline="") as f:
            for line, data in enumerate(f, 1):
                idx += len(data)
                if idx >= position:
                    column = position - (idx - len(data)) + 1
                    break
        return error(
            (source_desc, line, column),
            f"Decoding error, missing or incorrect coding=<encoding-name> at top of source (cannot decode with encoding {encoding!r}: {msg})",
        )

    def extract_module_name(self, path, options):
        dir, filename = os.path.split(path)
        module_name, _ = os.path.splitext(filename)
        if "." in module_name:
            return module_name
        names = [module_name]
        while self.is_package_dir(dir):
            parent, package_name = os.path.split(dir)
            if parent == dir:
                break
            names.append(package_name)
            dir = parent
        names.reverse()
        return ".".join(names)

    def setup_errors(self, options, result) -> None:
        Errors.init_thread()
        if options.use_listing_file:
            path = result.listing_file = Utils.replace_suffix(
                result.main_source_file, ".lis")
        else:
            path = None
        Errors.open_listing_file(path=path,
                                 echo_to_stderr=options.errors_to_stderr)

    def teardown_errors(self, err, options, result) -> None:
        source_desc = result.compilation_source.source_desc
        if not isinstance(source_desc, FileSourceDescriptor):
            raise RuntimeError("Only file sources for code supported")
        Errors.close_listing_file()
        result.num_errors = Errors.get_errors_count()
        if result.num_errors > 0:
            err = True
        if err and result.c_file:
            with contextlib.suppress(EnvironmentError):
                Utils.castrate_file(result.c_file,
                                    os.stat(source_desc.filename))
            result.c_file = None


def get_output_filename(source_filename: str, cwd: str,
                        options: CompilationOptions) -> str:
    c_suffix = ".cpp" if options.cplus else ".c"
    suggested_file_name = Utils.replace_suffix(source_filename, c_suffix)
    if options.output_file:
        out_path = os.path.join(cwd, options.output_file)
        if os.path.isdir(out_path):
            return os.path.join(out_path,
                                os.path.basename(suggested_file_name))
        return out_path
    return suggested_file_name


def create_default_resultobj(compilation_source: CompilationSource,
                             options: CompilationOptions):
    result = CompilationResult()
    result.main_source_file = compilation_source.source_desc.filename
    result.compilation_source = compilation_source
    source_desc = compilation_source.source_desc
    result.c_file = get_output_filename(source_desc.filename,
                                        compilation_source.cwd, options)
    result.embedded_metadata = options.embedded_metadata
    return result


def run_pipeline(source: str,
                 options: CompilationOptions,
                 full_module_name=None,
                 context=None) -> CompilationResult:
    from Cython.Compiler import Pipeline

    source_ext = os.path.splitext(source)[1]
    options.configure_language_defaults(source_ext[1:])
    if context is None:
        context = Context.from_options(options)
    cwd = os.getcwd()
    abs_path = os.path.abspath(source)
    full_module_name = full_module_name or context.extract_module_name(
        source, options)
    full_module_name = EncodedString(full_module_name)
    Utils.raise_error_if_module_name_forbidden(full_module_name)
    if options.relative_path_in_code_position_comments:
        rel_path = full_module_name.replace(".", os.sep) + source_ext
        if not abs_path.endswith(rel_path):
            rel_path = source
    else:
        rel_path = abs_path
    source_desc = FileSourceDescriptor(abs_path, rel_path)
    source = CompilationSource(source_desc, full_module_name, cwd)
    result = create_default_resultobj(source, options)
    if options.annotate is None:
        html_filename = os.path.splitext(result.c_file)[0] + ".html"
        if os.path.exists(html_filename):
            with open(html_filename, encoding="UTF-8") as html_file:
                if "<!-- Generated by Cython" in html_file.read(100):
                    options.annotate = True
    if source_ext.lower() == ".py" or not source_ext:
        pipeline = Pipeline.create_py_pipeline(context, options, result)
    else:
        pipeline = Pipeline.create_pyx_pipeline(context, options, result)
    context.setup_errors(options, result)
    if "." in full_module_name and "." in os.path.splitext(
            os.path.basename(abs_path))[0]:
        warning(
            (source_desc, 1, 0),
            f"Dotted filenames ('{os.path.basename(abs_path)}') are deprecated. Please use the normal Python package directory layout.",
            level=1,
        )
    err, enddata = Pipeline.run_pipeline(pipeline, source)
    context.teardown_errors(err, options, result)
    if err is None and options.depfile:
        from Cython.Build.Dependencies import create_dependency_tree

        dependencies = create_dependency_tree(context).all_dependencies(
            result.main_source_file)
        Utils.write_depfile(result.c_file, result.main_source_file,
                            dependencies)
    return result


@dataclass
class CompilationSource:
    source_desc: FileSourceDescriptor
    full_module_name: EncodedString
    cwd: str


@dataclass
class CompilationResult:
    main_source_file: str | None = None
    compilation_source: CompilationSource | None = None
    c_file: str | None = None
    embedded_metadata: bool = False
    num_errors: int = 0
    c_file: str | None = None
    h_file: str | None = None
    i_file: str | None = None
    api_file: str | None = None
    listing_file: str | None = None
    object_file: str | None = None
    extension_file: str | None = None


@dataclass
class CompilationResultSet(dict):
    num_errors = 0

    def add(self, source: str, result: CompilationResult) -> None:
        self[source] = result
        self.num_errors += result.num_errors


def compile_single(source: str,
                   options: CompilationOptions,
                   full_module_name=None) -> CompilationResult:
    return run_pipeline(source, options, full_module_name)


def compile_multiple(sources: list[str],
                     options: CompilationOptions) -> CompilationResultSet:
    if len(sources) > 1 and options.module_name:
        raise RuntimeError(
            "Full module name can only be set for single source compilation")
    sources = [os.path.abspath(source) for source in sources]
    processed = set()
    results = CompilationResultSet()
    timestamps = options.timestamps
    verbose = options.verbose
    context = None
    cwd = os.getcwd()
    for source in sources:
        if source not in processed:
            if context is None:
                context = Context.from_options(options)
            output_filename = get_output_filename(source, cwd, options)
            out_of_date = context.c_file_out_of_date(source, output_filename)
            if (not timestamps) or out_of_date:
                if verbose:
                    sys.stderr.write(f"Compiling {source}\n")
                result = run_pipeline(source,
                                      options,
                                      full_module_name=options.module_name,
                                      context=context)
                results.add(source, result)
                context = None
            processed.add(source)
    return results


def compile(
    source: str | list[str],
    options: CompilationOptions,
    full_module_name=None,
    **kwds,
) -> CompilationResult | CompilationResultSet:
    options = CompilationOptions(defaults=options, **kwds)
    if isinstance(source, str):
        if not options.timestamps:
            return compile_single(source, options, full_module_name)
        source = [source]
    return compile_multiple(source, options)


@Utils.cached_function
def search_include_directories(
    dirs: list[str],
    qualified_name: str,
    suffix: str,
    pos: tuple,
    include: bool,
    source_file_path: str,
) -> str | None:
    if pos and not source_file_path:
        file_desc = pos[0]
        if not isinstance(file_desc, FileSourceDescriptor):
            raise RuntimeError("Only file sources for code supported")
        source_file_path = file_desc.filename
    if source_file_path:
        if include:
            dirs = (os.path.dirname(source_file_path), ) + dirs
        else:
            dirs = (Utils.find_root_package_dir(source_file_path), ) + dirs
    dotted_filename = qualified_name
    if suffix:
        dotted_filename += suffix
    for dirname in dirs:
        path = os.path.join(dirname, dotted_filename)
        if os.path.exists(path):
            return path
    if not include:
        names = qualified_name.split(".")
        package_names = tuple(names[:-1])
        module_name = names[-1]
        namespace_dirs = []
        for dirname in dirs:
            package_dir, is_namespace = Utils.check_package_dir(
                dirname, package_names)
            if package_dir is not None:
                if is_namespace:
                    namespace_dirs.append(package_dir)
                    continue
                path = search_module_in_dir(package_dir, module_name, suffix)
                if path:
                    return path
        for package_dir in namespace_dirs:
            path = search_module_in_dir(package_dir, module_name, suffix)
            if path:
                return path
    return None


#


@Utils.cached_function
def search_module_in_dir(package_dir: str, module_name: str,
                         suffix: str) -> str | None:
    path = Utils.find_versioned_file(package_dir, module_name, suffix)
    if not path and suffix:
        path = Utils.find_versioned_file(
            os.path.join(package_dir, module_name), "__init__", suffix)
    return path


def setuptools_main() -> None:
    return main(command_line=1)


def main(command_line=0) -> None:
    args = sys.argv[1:]
    any_failures = 0
    if command_line:
        try:
            from Cython.Compiler import CmdLine
            options, sources = CmdLine.parse_command_line(args)
        except OSError as e:
            import errno

            if e.errno != errno.ENOENT:
                raise
            safe_print(
                f"{sys.argv[0]}: No such file or directory: '{e.filename}'",
                file=sys.stderr)
            sys.exit(1)
    else:
        options = CompilationOptions(**default_options)
        sources = args
    if options.show_version:
        Utils.print_version()
    if options.working_path != "":
        os.chdir(options.working_path)
    try:
        result = compile(sources, options)
        if result.num_errors > 0:
            any_failures = 1
    except (OSError, PyrexError) as e:
        sys.stderr.write(str(e) + "\n")
        any_failures = 1
    if any_failures:
        sys.exit(1)


def _build(args):
    parsed = _parse_args(args)
    if parsed is None:
        raise ValueError(f"No parseable arguments found: {args}")

    dump_config()
    input_file, cy_args, remaining = parsed
    _debug("Input file: %s", input_file)
    _debug("Cython args: %s", cy_args)
    _debug("Remaining args: %s", remaining)
    program_name = build(input_file, cy_args)
    return program_name, remaining


def _main():
    args = sys.argv[1:]
    dump_config()
    _build(args)


if __name__ == "__main__":
    _main()
