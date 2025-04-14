import ctypes.util
import subprocess
import sys
import sysconfig
from pathlib import Path


def resolve_mac_executable_path(libpath: str) -> str:
    """Convert a macOS dynamic linker placeholder (@executable_path)
    into an absolute path using the location of sys.executable.
    """
    if libpath.startswith("@executable_path"):
        exe_dir = Path(sys.executable).resolve().parent
        relative_part = libpath.replace("@executable_path/", "")
        resolved = (exe_dir / relative_part).resolve()
        if not resolved.exists():
            raise FileNotFoundError(f"Resolved path '{resolved}' does not exist for libpath '{libpath}'.")
        return str(resolved)
    return libpath


def find_python_include() -> str:
    """Locate the Python include directory.
    First, try sysconfig; if that fails, search common fallback directories.
    """
    include_dir = sysconfig.get_paths().get("include")
    if include_dir and Path(include_dir).exists():
        return str(Path(include_dir).resolve())

    fallback_dirs = [
        Path(sys.prefix) / "include",
        Path(getattr(sys, "base_prefix", sys.prefix)) / "include",
        Path(f"/usr/include/python{sys.version_info.major}"),
        Path(f"/usr/local/include/python{sys.version_info.major}"),
        Path(f"/opt/homebrew/include/python{sys.version_info.major}"),  # macOS ARM/M1/M2
    ]
    for inc in fallback_dirs:
        if inc.exists():
            return str(inc.resolve())

    raise FileNotFoundError("Python include directory not found.")


def find_python_library() -> str:
    """Locate the Python shared library (libpython) in a robust, universal manner.
    The search order is:
      1. Directories relative to sys.prefix and sys.base_prefix (covers virtual environments)
      2. Common system library directories.
      3. sysconfig's LIBDIR (if valid).
      4. ctypes.util.find_library() as a fallback.
      5. Finally, inspect the linked libraries of sys.executable.

    macOS's @executable_path placeholders are resolved to absolute paths.
    """
    candidate_dirs = [
        Path(sys.prefix) / "lib",
        Path(getattr(sys, "base_prefix", sys.prefix)) / "lib",
        Path(sys.prefix) / "libs",  # Windows typical location.
        Path("/usr/lib"),
        Path("/usr/local/lib"),
        Path("/opt/homebrew/lib"),
    ]

    # Search for shared libraries (dylib on macOS, so on Linux)
    for libdir in candidate_dirs:
        if libdir.exists():
            for ext in [".dylib", ".so"]:
                pattern = f"libpython{sys.version_info.major}.{sys.version_info.minor}*{ext}"
                for lib in libdir.glob(pattern):
                    resolved_lib = resolve_mac_executable_path(str(lib.resolve()))
                    if Path(resolved_lib).exists():
                        return resolved_lib
            # On Windows, check for .lib files
            for lib in libdir.glob(f"python{sys.version_info.major}{sys.version_info.minor}.lib"):
                resolved_lib = str(lib.resolve())
                if Path(resolved_lib).exists():
                    return resolved_lib

    # Fallback: Try sysconfig's LIBDIR
    libdir = sysconfig.get_config_var("LIBDIR")
    if libdir:
        libdir_path = Path(libdir)
        if libdir_path.exists():
            for ext in [".dylib", ".so"]:
                pattern = f"libpython{sys.version_info.major}.{sys.version_info.minor}*{ext}"
                for lib in libdir_path.glob(pattern):
                    resolved_lib = resolve_mac_executable_path(str(lib.resolve()))
                    if Path(resolved_lib).exists():
                        return resolved_lib

    # Fallback: ctypes.util.find_library()
    libpython = ctypes.util.find_library(f"python{sys.version_info.major}.{sys.version_info.minor}")
    if libpython:
        resolved_lib = resolve_mac_executable_path(libpython)
        if Path(resolved_lib).exists():
            return resolved_lib

    # Last resort: inspect linked libraries of sys.executable
    python_bin = Path(sys.executable).resolve()
    try:
        if sys.platform.startswith("linux"):
            result = subprocess.run(["ldd", str(python_bin)], capture_output=True, text=True, check=True)
            for line in result.stdout.splitlines():
                if "libpython" in line:
                    parts = line.split()
                    if len(parts) >= 3 and Path(parts[2]).exists():
                        return resolve_mac_executable_path(parts[2])
        elif sys.platform == "darwin":
            result = subprocess.run(["otool", "-L", str(python_bin)], capture_output=True, text=True, check=True)
            for line in result.stdout.splitlines():
                if "libpython" in line:
                    candidate = line.split()[0]
                    if Path(candidate).exists():
                        return resolve_mac_executable_path(candidate)
        elif sys.platform == "win32":
            result = subprocess.run(
                ["dumpbin", "/DEPENDENTS", str(python_bin)], capture_output=True, text=True, check=True,
            )
            for line in result.stdout.splitlines():
                if "python" in line and line.strip().endswith(".dll"):
                    candidate = line.strip()
                    # On Windows, you might need further resolution here.
                    return candidate
    except Exception:
        pass

    raise FileNotFoundError("Python shared library not found. Rebuild Python with --enable-shared if necessary.")


if __name__ == "__main__":
    incdir = find_python_include()
    libpython = find_python_library()
    print("Python include directory:", incdir)
    print("Python library:", libpython)
