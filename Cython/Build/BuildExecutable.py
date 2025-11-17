"""
Compile a Python script into an executable that embeds CPython.
Requires CPython to be built as a shared library ('libpythonX.Y').

Basic usage:

    python -m Cython.Build.BuildExecutable [ARGS] somefile.py
"""

from __future__ import annotations

import os
import sys
from dataclasses import asdict, dataclass
from pathlib import Path
import sysconfig
from typing import IO, Sequence

from Cython.Compiler import CmdLine, Main as CompilerMain, Version

DEBUG = True


@dataclass(frozen=True)
class PythonBuildConfig:
    """Snapshot of interpreter build settings needed for embedding."""

    include_dir: str
    libdir1: str
    libdir2: str
    static_lib: str
    shared_lib: str
    cc: str
    cflags: str
    linkcc: str
    libs: str
    syslibs: str
    link_for_shared: str
    exe_ext: str


def find_python_library() -> str | None:
    """Return absolute path to the host CPython shared library, if present.

    The search strategy is intentionally exhaustive because *uv*-managed
    virtual-envs on macOS/Homebrew often break the usual sysconfig hints.
    Logic adapted from ``mb.build``/``mbcore.findpython`` so that all build
    helpers rely on a single robust implementation.
    """
    import ctypes.util
    import subprocess

    def check_path(path: str | os.PathLike) -> str | None:
        p = Path(path)
        return str(p.resolve()) if p.exists() else None

    major, minor = sys.version_info[:2]
    version = f"{major}.{minor}"

    # 1. Direct hint from sysconfig (works on most CPython builds)
    lib_name = sysconfig.get_config_var("LDLIBRARY") or ""
    lib_dir = Path(sysconfig.get_config_var("LIBDIR") or "")
    if lib_name:
        lib = check_path(lib_dir / lib_name)
        if lib:
            return lib

    # 2. Search prefix-relative library dirs (handles venvs, uv, Homebrew, etc.)
    base_prefix = Path(getattr(sys, "base_prefix", sys.prefix))
    candidate_dirs: list[Path] = [
        base_prefix / "lib",
        Path(sys.prefix) / "lib",
    ]
    if sys.platform == "win32":
        candidate_dirs.extend(
            [
                base_prefix / "libs",
                Path(sys.prefix) / "libs",
                Path(sys.executable).resolve().parent,
            ]
        )
    else:
        candidate_dirs.extend(
            [
                Path("/usr/lib"),
                Path("/usr/local/lib"),
                Path("/lib"),
                Path("/lib64"),
                Path("/usr/lib64"),
                Path("/opt/homebrew/lib"),
            ]
        )

    for libdir in candidate_dirs:
        if not libdir.exists():
            continue
        if sys.platform == "win32":
            for name in (
                f"python{major}{minor}.dll",
                f"python{major}{minor}m.dll",
                f"python{major}{minor}.lib",
            ):
                lib = check_path(libdir / name)
                if lib:
                    return lib
        else:
            for pattern in (
                f"libpython{version}*.dylib",
                f"libpython{version}*.so",
            ):
                for libpath in libdir.glob(pattern):
                    lib = check_path(libpath)
                    if lib:
                        return lib

    # 3. ctypes-based lookup (cross-platform, but can return bare soname)
    found = ctypes.util.find_library(f"python{major}.{minor}")
    if found:
        lib = check_path(found)
        if lib:
            return lib

    # 4. Platform-specific inspection of the running interpreter
    exe = sys.executable

    if sys.platform == "darwin":
        # 4a. `otool -L` on the interpreter binary
        try:
            output = subprocess.check_output(["otool", "-L", exe], text=True)
        except Exception:
            output = ""
        for line in output.splitlines():
            if "libpython" in line:
                candidate = line.split()[0]
                lib = check_path(candidate)
                if lib:
                    return lib

        # 4b. macOS framework layouts (Homebrew etc.)
        try:
            framework_root = base_prefix.parents[1]
        except IndexError:
            framework_root = base_prefix
        framework_ver = framework_root / "Versions" / version
        # <framework>/Versions/<X.Y>/Python
        framework_bin = framework_ver / "Python"
        lib = check_path(framework_bin)
        if lib:
            return lib
        # <framework>/Versions/<X.Y>/lib/libpythonX.Y.dylib
        framework_dylib = (
            framework_ver / "lib" / f"libpython{version}.dylib"
        )
        lib = check_path(framework_dylib)
        if lib:
            return lib

    elif sys.platform.startswith("linux") or "bsd" in sys.platform or "unix" in sys.platform:
        # 4c. `ldd` on the interpreter binary
        try:
            output = subprocess.check_output(["ldd", exe], text=True)
        except Exception:
            output = ""
        for line in output.splitlines():
            if "libpython" not in line:
                continue
            parts = line.split()
            # Typical lines look like:
            #   libpython3.12.so.1.0 => /usr/lib/.... (0x...)
            for token in parts[1:]:
                if "/" in token:
                    lib = check_path(token)
                    if lib:
                        return lib
                    break

    if sys.platform == "win32":
        # 4d. Search common DLL locations (system + prefix + alongside exe)
        import platform as _platform

        python_version = _platform.python_version_tuple()
        potential_paths = [
            f"C:\\Windows\\System32\\python{python_version[0]}{python_version[1]}.dll",
            f"C:\\Windows\\SysWOW64\\python{python_version[0]}{python_version[1]}.dll",
            Path(getattr(sys, "base_prefix", sys.prefix))
            / f"python{python_version[0]}{python_version[1]}.dll",
            Path(exe).resolve().parent
            / f"python{python_version[0]}{python_version[1]}.dll",
        ]
        for candidate in potential_paths:
            lib = check_path(candidate)
            if lib:
                return lib

    # 5. Last-resort: manually scan common library locations
    common_paths: list[os.PathLike | str] = [
        "/usr/lib",
        "/usr/local/lib",
        "/opt/homebrew/lib",
        "/lib",
        "/lib64",
        "/usr/lib64",
        Path(getattr(sys, "base_prefix", sys.prefix)) / "lib",
        Path(sys.executable).resolve().parent / "lib",
    ]
    from itertools import chain

    for base in common_paths:
        base_path = Path(base)
        if not base_path.exists():
            continue
        patterns = [
            "libpython*.so*",
            "libpython*.dylib",
            "python*.dll",
        ]
        for lib in chain.from_iterable(base_path.glob(pat) for pat in patterns):
            lib_path = check_path(lib)
            if lib_path:
                return lib_path

    # 6. No shared libpython found (e.g. static-build CPython)
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
            base_prefix,
            "include",
            f"python{sys.version_info.major}.{sys.version_info.minor}",
        ),
    )
    cfg["LIBDIR1"] = validate_path(os.path.join(base_prefix, "lib"))
    cfg["LIBDIR2"] = validate_path(
        os.path.join(
            base_prefix,
            "lib",
            f"python{sys.version_info.major}.{sys.version_info.minor}",
            f"config-{sys.platform}",
        ),
    )
    # Get PYLIB and PYLIB_DYN from sysconfig (they might still be filenames)
    cfg["PYLIB"] = get_config_var_wrapper("LIBRARY")
    cfg["PYLIB_DYN"] = get_config_var_wrapper("LDLIBRARY")
    # Use environment or defaults for the rest:
    cfg["CC"] = os.environ.get("CC", get_config_var_wrapper("CC"))
    cfg["CFLAGS"] = (
        get_config_var_wrapper("CFLAGS") + " " + os.environ.get("CFLAGS", "")
    ).strip()
    cfg["LINKCC"] = os.environ.get(
        "LINKCC",
        get_config_var_wrapper("LINKCC", cfg["CC"]),
    )
    cfg["LIBS"] = get_config_var_wrapper("LIBS")
    cfg["SYSLIBS"] = get_config_var_wrapper("SYSLIBS")
    cfg["LINKFORSHARED"] = get_config_var_wrapper("LINKFORSHARED")
    cfg["EXE_EXT"] = get_config_var_wrapper("EXE")
    return cfg


def load_python_build_config() -> PythonBuildConfig:
    cfg = get_config_vars_dict()
    shared_lib = find_python_library() or cfg["PYLIB_DYN"]
    if not cfg["INCDIR"]:
        raise FileNotFoundError("Python include directory not found.")
    if not (cfg["LIBDIR1"] or cfg["LIBDIR2"]):
        raise FileNotFoundError("Python library directory not found.")
    if not shared_lib:
        raise FileNotFoundError("Python shared library (libpythonX.Y) not found.")
    return PythonBuildConfig(
        include_dir=cfg["INCDIR"],
        libdir1=cfg["LIBDIR1"],
        libdir2=cfg["LIBDIR2"],
        static_lib=cfg["PYLIB"],
        shared_lib=shared_lib,
        cc=cfg["CC"],
        cflags=cfg["CFLAGS"],
        linkcc=cfg["LINKCC"],
        libs=cfg["LIBS"],
        syslibs=cfg["SYSLIBS"],
        link_for_shared=cfg["LINKFORSHARED"],
        exe_ext=cfg["EXE_EXT"],
    )


PYTHON_BUILD_CONFIG = load_python_build_config()

INCDIR = PYTHON_BUILD_CONFIG.include_dir
LIBDIR1 = PYTHON_BUILD_CONFIG.libdir1
LIBDIR2 = PYTHON_BUILD_CONFIG.libdir2
PYLIB = PYTHON_BUILD_CONFIG.static_lib
PYLIB_DYN = PYTHON_BUILD_CONFIG.shared_lib
CC = PYTHON_BUILD_CONFIG.cc
CFLAGS = PYTHON_BUILD_CONFIG.cflags
LINKCC = PYTHON_BUILD_CONFIG.linkcc
LIBS = PYTHON_BUILD_CONFIG.libs
SYSLIBS = PYTHON_BUILD_CONFIG.syslibs
LINKFORSHARED = PYTHON_BUILD_CONFIG.link_for_shared
EXE_EXT = PYTHON_BUILD_CONFIG.exe_ext


def resolve_mac_executable_path(libpath: str) -> str:
    if libpath.startswith("@executable_path"):
        exe_dir = Path(sys.executable).resolve().parent
        relative_part = libpath.replace("@executable_path/", "")
        resolved = (exe_dir / relative_part).resolve()
        if not resolved.exists():
            raise FileNotFoundError(
                f"Resolved path '{resolved}' does not exist for '{libpath}'.",
            )
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
    for key, value in asdict(PYTHON_BUILD_CONFIG).items():
        _debug("  %s: %s", key.upper(), value)
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
            remaining = args[i + 1 :]
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
            check=False,
        )

        if result.stdout:
            safe_print(result.stdout, end="")

        if result.returncode != 0:
            _debug(f"🚨 ERROR: Command failed with exit code {result.returncode}")
            if result.stderr:
                _debug(f"❌ STDERR:\n{result.stderr}")
            sys.exit(result.returncode)

        return result.stdout.strip() if result.stdout else ""
    except Exception as e:  # pragma: no cover - defensive
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
        output_so = Path(lib_dir) / cpp_path.relative_to(install_dir).with_suffix(
            ext_suffix,
        )
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
        link_args.append(PYLIB_DYN)  # Explicitly add the Python dynamic library
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
            f"Neither {basename + '.cpp'} nor {basename + '.c'} exists.",
        )
    # Compile the source file into an object file.
    cmd = [compiler, "-c", "-o", basename + ".o", source_file, "-I" + INCDIR] + (
        CFLAGS.split()
    )
    _debug("ccompile cmd: %s", " ".join(cmd))
    runcmd(cmd)


def cycompile(input_file, options=()) -> None:
    options, sources = CmdLine.parse_command_line(
        list(options) + ["--embed", input_file],
    )
    _debug("Using Cython %s to compile %s", Version.version, input_file)
    result = CompilerMain.compile(sources, options)  # type: ignore[arg-type]
    if result.num_errors > 0:
        sys.exit(1)


def exec_file(program_name, args=()) -> None:
    runcmd([str(Path(program_name).resolve())] + list(args), shell=False)


def safe_print(message: str, file: IO[str] = sys.stderr, end: str = "\n") -> None:
    print(message, file=file, end=end)


def build(input_file, compiler_args=(), force=False):
    basename = os.path.splitext(input_file)[0]
    exe_file = basename + EXE_EXT
    if not force and os.path.abspath(exe_file) == os.path.abspath(input_file):
        raise ValueError(
            "Input and output file names are the same, refusing to overwrite",
        )
    if (
        not force
        and os.path.exists(exe_file)
        and os.path.exists(input_file)
        and os.path.getmtime(input_file) <= os.path.getmtime(exe_file)
    ):
        _debug("File is up to date, not regenerating %s", exe_file)
        return exe_file
    cycompile(input_file, compiler_args)
    ccompile(basename)
    clink(basename)
    return exe_file


def build_from_argv(args: Sequence[str] | None = None) -> tuple[str, list[str]]:
    arg_list = list(args) if args is not None else sys.argv[1:]
    parsed = _parse_args(arg_list)
    if parsed is None:
        raise ValueError(f"No parseable arguments found: {arg_list}")

    input_file, cy_args, remaining = parsed
    _debug("Input file: %s", input_file)
    _debug("Cython args: %s", cy_args)
    _debug("Remaining args: %s", remaining)
    program_name = build(input_file, cy_args)
    return program_name, remaining


def build_and_run(args):
    """
    Build an executable program from a Cython module and run it.

    Arguments after the module name will be passed verbatimly to the program.
    """
    dump_config()
    program_name, args = build_from_argv(args)
    exec_file(program_name, args)


def _build(args):
    """Backward compatible alias for old helper."""
    return build_from_argv(args)


def main(args: Sequence[str] | None = None, *, run_program: bool = False) -> str:
    dump_config()
    program_name, remaining = build_from_argv(args)
    if run_program and remaining:
        exec_file(program_name, remaining)
    return program_name


__all__ = [
    "DEBUG",
    "PythonBuildConfig",
    "PYTHON_BUILD_CONFIG",
    "INCDIR",
    "LIBDIR1",
    "LIBDIR2",
    "PYLIB",
    "PYLIB_DYN",
    "CC",
    "CFLAGS",
    "LINKCC",
    "LIBS",
    "SYSLIBS",
    "LINKFORSHARED",
    "EXE_EXT",
    "find_python_library",
    "resolve_mac_executable_path",
    "find_all_libpython_paths",
    "runcmd",
    "ccompile",
    "clink",
    "cycompile",
    "compile_shared",
    "exec_file",
    "build",
    "build_and_run",
    "build_from_argv",
    "_build",
    "_parse_args",
    "safe_print",
    "dump_config",
    "main",
]


if __name__ == "__main__":
    main()
