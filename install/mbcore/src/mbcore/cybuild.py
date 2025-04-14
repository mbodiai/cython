DEBUG = True

import os
import sys
from pathlib import Path

# For Python < 3.9, fallback to distutils.sysconfig.
if sys.version_info < (3, 9):
    from distutils import sysconfig as _sysconfig

    class sysconfig:
        @staticmethod
        def get_path(name):
            assert name == "include"
            return _sysconfig.get_python_inc()

        get_config_var = staticmethod(_sysconfig.get_config_var)
        get_config_vars = staticmethod(_sysconfig.get_config_vars)
else:
    import sysconfig


def validate_path(path: str) -> str:
    return path if path and Path(path).exists() else ""


def get_config_var_wrapper(name, default=""):
    val = sysconfig.get_config_var(name)
    return val if val is not None else default


def get_config_vars_dict():
    cfg = {}
    cfg["INCDIR"] = validate_path(sysconfig.get_path("include"))
    cfg["LIBDIR1"] = validate_path(get_config_var_wrapper("LIBDIR"))
    cfg["LIBDIR2"] = validate_path(get_config_var_wrapper("LIBPL"))
    cfg["PYLIB"] = get_config_var_wrapper("LIBRARY")
    cfg["PYLIB_DYN"] = get_config_var_wrapper("LDLIBRARY")
    if not cfg["LIBDIR1"]:
        cfg["LIBDIR1"] = validate_path(f"{sys.prefix}/lib")
    if not cfg["LIBDIR2"]:
        cfg["LIBDIR2"] = validate_path(
            f"{sys.prefix}/lib/python{sys.version_info.major}.{sys.version_info.minor}/config-{sys.platform}",
        )
    cfg["CC"] = os.environ.get("CC", get_config_var_wrapper("CC"))
    cfg["CFLAGS"] = (get_config_var_wrapper("CFLAGS") + " " + os.environ.get("CFLAGS", "")).strip()
    cfg["LINKCC"] = os.environ.get("LINKCC", get_config_var_wrapper("LINKCC", cfg["CC"]))
    cfg["LIBS"] = get_config_var_wrapper("LIBS")
    cfg["SYSLIBS"] = get_config_var_wrapper("SYSLIBS")
    cfg["LINKFORSHARED"] = get_config_var_wrapper("LINKFORSHARED")
    cfg["EXE_EXT"] = get_config_var_wrapper("EXE")
    return cfg


def resolve_dyn_lib_path(pylib_dyn: str) -> str:
    # If already absolute or a placeholder, return as is.
    if os.path.isabs(pylib_dyn) or pylib_dyn.startswith("@"):
        return pylib_dyn

    candidate_dirs = [
        Path(getattr(sys, "base_prefix", sys.prefix)) / "lib",  # Use base_prefix explicitly.
        Path(sys.prefix) / "lib",
        Path("/usr/lib"),
        Path("/usr/local/lib"),
        Path("/opt/homebrew/lib"),
    ]
    for d in candidate_dirs:
        candidate = d / pylib_dyn
        if DEBUG:
            print(f"Checking candidate: {candidate}")
        if candidate.exists():
            resolved_candidate = candidate.resolve()
            if DEBUG:
                print(f"Found candidate: {resolved_candidate}")
            return str(resolved_candidate)
    if DEBUG:
        print("No candidate found for:", pylib_dyn)
    return pylib_dyn


CONFIG = get_config_vars_dict()

# Module-level variables.
INCDIR = CONFIG["INCDIR"]
LIBDIR1 = CONFIG["LIBDIR1"]
LIBDIR2 = CONFIG["LIBDIR2"]
PYLIB = CONFIG["PYLIB"]
PYLIB_DYN = resolve_dyn_lib_path(CONFIG["PYLIB_DYN"])
CC = CONFIG["CC"]
CFLAGS = CONFIG["CFLAGS"]
LINKCC = CONFIG["LINKCC"]
LIBS = CONFIG["LIBS"]
SYSLIBS = CONFIG["SYSLIBS"]
LINKFORSHARED = CONFIG["LINKFORSHARED"]
EXE_EXT = CONFIG["EXE_EXT"]


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
                    except Exception as e:
                        if DEBUG:
                            print(f"Error resolving {lib}: {e}")
    return sorted(found_paths)


def dump_config():
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
            remaining = args[i + 1 :]
            return input_file, cy_args, remaining
        last_arg = arg
    return None


def runcmd(cmd, shell=True):
    if shell:
        cmd_str = " ".join(cmd)
        _debug(cmd_str)
    else:
        _debug(" ".join(cmd))
    import subprocess

    returncode = subprocess.call(cmd, shell=shell)
    if returncode:
        sys.exit(returncode)


def clink(basename):
    link_args = [LINKCC, "-o", basename + EXE_EXT, basename + ".o"]
    if LIBDIR1:
        link_args.append("-L" + LIBDIR1)
    if LIBDIR2:
        link_args.append("-L" + LIBDIR2)
    if LINKFORSHARED:
        link_args.extend(LINKFORSHARED.split())
    if LIBS:
        link_args.extend(LIBS.split())
    if SYSLIBS:
        link_args.extend(SYSLIBS.split())
    _debug("Final link command: %s", " ".join(link_args))
    runcmd(link_args)


def ccompile(basename):
    runcmd([CC, "-c", "-o", basename + ".o", basename + ".c", "-I" + INCDIR] + CFLAGS.split())


def cycompile(input_file, options=()):
    from Cython.Compiler import CmdLine, Main, Version

    options, sources = CmdLine.parse_command_line(list(options) + ["--embed", input_file])
    _debug("Using Cython %s to compile %s", Version.version, input_file)
    result = Main.compile(sources, options)
    if result.num_errors > 0:
        sys.exit(1)


def exec_file(program_name, args=()):
    runcmd([str(Path(program_name).resolve())] + list(args), shell=False)


def build(input_file, compiler_args=(), force=False):
    basename = os.path.splitext(input_file)[0]
    exe_file = basename + EXE_EXT
    if not force and os.path.abspath(exe_file) == os.path.abspath(input_file):
        raise ValueError("Input and output file names are the same, refusing to overwrite")
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


def _build(args):
    parsed = _parse_args(args)
    if parsed is None:
        dump_config()
        sys.exit(0)
    input_file, cy_args, remaining = parsed
    program_name = build(input_file, cy_args)
    return program_name, remaining


if __name__ == "__main__":
    # If no arguments are provided, dump configuration and exit.
    if len(sys.argv) < 2:
        dump_config()
        sys.exit(0)
    else:
        _build(sys.argv[1:])
