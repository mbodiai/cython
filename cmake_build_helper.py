#!/usr/bin/env python3
import sys
import os
import subprocess
import sysconfig
import ctypes.util
from pathlib import Path
import argparse

# --- Robust Python Library Finding (adapted from mbcore/build.py) ---


def find_python_library():
    """Find the correct Python shared or static library for any OS, architecture, and installation method."""

    def check_path(path):
        """Returns a valid path if it exists, else None."""
        try:
            path_obj = Path(path)
            return str(path_obj.resolve()) if path_obj.exists() else None
        except (OSError, ValueError):  # Handle potential resolution errors or invalid paths
            return None

    # 1. Direct lookup via sysconfig
    lib_name = sysconfig.get_config_var("LDLIBRARY") or ""
    lib_dir = Path(sysconfig.get_config_var("LIBDIR") or "")
    if lib_name:
        # Handle framework path potentially included in LDLIBRARY on macOS
        if sys.platform == "darwin" and "Python.framework" in lib_name:
            # Try constructing path relative to framework dir if LDLIBRARY seems relative
            framework_dir = sysconfig.get_config_var("PYTHONFRAMEWORKDIR")
            if framework_dir and framework_dir != "no-framework":
                potential_path = Path(framework_dir) / lib_name
                shared_lib = check_path(potential_path)
                if shared_lib:
                    return shared_lib
        elif lib_dir:  # Check relative to LIBDIR only if not a framework path in name
            shared_lib = check_path(lib_dir / lib_name)
            if shared_lib:
                return shared_lib

        # Check if lib_name itself is an absolute path
        if Path(lib_name).is_absolute():
            shared_lib = check_path(lib_name)
            if shared_lib:
                return shared_lib

    # 2. ctypes library lookup (cross-platform)
    try:
        ctypes_name = f"python{sys.version_info.major}.{sys.version_info.minor}"
        found_lib = ctypes.util.find_library(ctypes_name)
        if found_lib:
            found_lib_path = check_path(found_lib)
            if found_lib_path:
                return found_lib_path
    except Exception:
        pass  # Ignore errors during ctypes lookup

    # 3. macOS: Use `otool -L` (carefully)
    if sys.platform == "darwin":
        try:
            output = subprocess.check_output(
                ["otool", "-L", sys.executable], text=True, stderr=subprocess.DEVNULL
            )
            for line in output.split("\n"):
                line = line.strip()
                if "libpython" in line or "Python.framework" in line:
                    # First word is usually the path
                    potential_path = line.split()[0]
                    # Resolve @rpath, @executable_path etc.
                    if potential_path.startswith("@executable_path"):
                        exe_dir = Path(sys.executable).parent
                        potential_path = str(exe_dir / potential_path.split("/", 1)[1])
                    elif potential_path.startswith("@loader_path"):
                        # Less common for python executable itself, but possible
                        # For now, skip this complex case for simplicity
                        continue
                    elif potential_path.startswith("@rpath"):
                        # Resolving rpath is complex, skip for simplicity here
                        continue

                    shared_lib = check_path(potential_path)
                    if shared_lib:
                        return shared_lib
        except (Exception, FileNotFoundError):
            pass

        # Try macOS framework paths based on prefix (might be redundant with otool but good fallback)
        try:
            prefix = sysconfig.get_config_var("PYTHONFRAMEWORKPREFIX")
            if prefix and prefix != "/usr/local":
                framework_path = (
                    Path(prefix)
                    / "Python.framework"
                    / "Versions"
                    / f"{sys.version_info.major}.{sys.version_info.minor}"
                    / "Python"
                )
                shared_lib = check_path(framework_path)
                if shared_lib:
                    return shared_lib
                alt_framework_path = Path(prefix) / "Python.framework" / "Python"
                shared_lib = check_path(alt_framework_path)
                if shared_lib:
                    return shared_lib
        except Exception:
            pass

    # 4. Linux: Use `ldd` (carefully)
    elif sys.platform == "linux":
        try:
            output = subprocess.check_output(
                ["ldd", sys.executable], text=True, stderr=subprocess.DEVNULL
            )
            for line in output.split("\n"):
                line = line.strip()
                if "libpython" in line:
                    parts = line.split()
                    # Typically "libpythonX.Y.so.Z => /path/to/libpythonX.Y.so.Z (0x...)" or "/path/to/..."
                    path_index = -1
                    for i, part in enumerate(parts):
                        if part.startswith(("/", "libpython")):
                            path_index = i
                            break
                    if path_index != -1:
                        potential_path = parts[path_index]
                        shared_lib = check_path(potential_path)
                        if shared_lib:
                            return shared_lib
        except (Exception, FileNotFoundError):
            pass

    # 5. Windows: Search for pythonXX.dll
    elif sys.platform == "win32":
        python_version = sys.version_info
        potential_paths = [
            # Prefer using sys.base_prefix locations
            Path(sys.base_prefix) / f"python{python_version.major}{python_version.minor}.dll",
            Path(sys.executable).parent / f"python{python_version.major}{python_version.minor}.dll",
            # System locations (less reliable, might not match venv)
            Path(os.environ.get("SystemRoot", "C:\\Windows"))
            / "System32"
            / f"python{python_version.major}{python_version.minor}.dll",
            Path(os.environ.get("SystemRoot", "C:\\Windows"))
            / "SysWOW64"
            / f"python{python_version.major}{python_version.minor}.dll",
        ]
        for path in potential_paths:
            dll_path = check_path(path)
            if dll_path:
                return dll_path

    # 6. Last resort: Manually search common library paths using LDLIBRARY name if available
    if lib_name:
        common_paths = [
            Path(sys.base_prefix) / "lib",
            Path(sys.prefix) / "lib",
            Path("/usr/lib"),
            Path("/usr/local/lib"),
            Path("/opt/homebrew/lib"),
            Path("/lib"),
            Path("/lib64"),
            Path("/usr/lib64"),
        ]
        for path in common_paths:
            if path.is_dir():
                # Search for exact name first
                candidate = path / lib_name
                shared_lib = check_path(candidate)
                if shared_lib:
                    return shared_lib
                # Search for related patterns (less reliable)
                patterns = [
                    f"libpython{sys.version_info.major}.{sys.version_info.minor}*.so*",
                    f"libpython{sys.version_info.major}.{sys.version_info.minor}*.dylib",
                    f"python{sys.version_info.major}{sys.version_info.minor}*.dll",
                ]
                for pattern in patterns:
                    for lib in path.glob(pattern):
                        shared_lib = check_path(lib)
                        if shared_lib:
                            return shared_lib

    return None  # Not found


# --- Basic Cython runner ---
def run_cython(source_file, output_dir, embed=False, language="c"):
    from Cython.Compiler.Main import compile as cython_compile
    from Cython.Compiler.CmdLine import parse_command_line

    source_path = Path(source_file)
    output_dir_path = Path(output_dir)
    # Ensure output directory exists
    output_dir_path.mkdir(parents=True, exist_ok=True)

    # Construct the output C/C++ file path
    c_suffix = ".cpp" if language == "c++" else ".c"
    output_c_file = output_dir_path / source_path.with_suffix(c_suffix).name

    args = []
    # Use -o to specify output file path
    args.extend(["-o", str(output_c_file)])
    if embed:
        args.append("--embed")
    if language == "c++":
        args.append("--cplus")
    args.append(str(source_file))

    options, sources = parse_command_line(args)
    print(f"Running Cython on: {source_file} -> {output_c_file}")
    # Use vars() for dataclasses or check type
    options_dict = vars(options) if hasattr(options, "__dict__") else options
    print(f"  Options: {options_dict}")
    result = cython_compile(sources, options)
    if result.num_errors > 0:
        print(f"ERROR: Cython compilation failed for {source_file}", file=sys.stderr)
        sys.exit(1)
    # The actual output file is now in options.output_file
    generated_file = options.output_file
    print(f"  Generated: {generated_file}")
    return generated_file  # Return path to generated C/C++ file


# --- Generate main.cpp ---
def generate_main(output_path, install_dir, module_name):
    """Generate a simple main C++ file to embed Python and run the module."""
    # Normalize paths for C++ string literals
    install_dir_str = str(Path(install_dir).resolve()).replace("\\", "\\\\")

    main_code = f"""#include <Python.h>
#include <iostream>
#include <string>
#include <vector>

#ifdef _WIN32
#include <windows.h>
#endif

int main(int argc, char *argv[]) {{
    wchar_t *program;

#ifdef _WIN32
    // Ensure correct path handling on Windows
    wchar_t wpath[MAX_PATH];
    // Use GetModuleFileNameW for wide char path, NULL gets executable path
    if (GetModuleFileNameW(NULL, wpath, MAX_PATH) == 0) {{
         std::cerr << "Fatal error: Cannot get executable path" << std::endl;
         return 1;
    }}
    program = wpath;
#else
    program = Py_DecodeLocale(argv[0], NULL);
    if (program == NULL) {{
        std::cerr << "Fatal error: cannot decode argv[0]" << std::endl;
        return 1;
    }}
#endif

    Py_SetProgramName(program); // Need to call this before Py_Initialize

    // --- Use Config API for setting Python Home and Path ---
    PyStatus status;
    PyConfig config;
    PyConfig_InitPythonConfig(&config);

    // Configure Python path: Add install dir first
    std::wstring install_dir_w = L"{install_dir_str}"; // Use L prefix for wide string
    status = PyConfig_SetString(&config, &config.program_name, program);
    if (PyStatus_Exception(status)) goto config_error;

    status = PyWideStringList_Insert(&config.module_search_paths, 0, install_dir_w.c_str());
    if (PyStatus_Exception(status)) goto config_error;
    config.module_search_paths_set = 1;

    status = Py_InitializeFromConfig(&config);
    if (PyStatus_Exception(status)) goto init_error;

    PyConfig_Clear(&config);
    // --- End Config API ---

    PyObject* module_name_obj = PyUnicode_FromString("{module_name}");
    if (!module_name_obj) {{
         std::cerr << "Failed to create module name string" << std::endl;
         if (PyErr_Occurred()) PyErr_Print();
         Py_Finalize();
         return 1;
    }}

    PyObject* module = PyImport_Import(module_name_obj);
    Py_DECREF(module_name_obj);

    if (module == NULL) {{
        std::cerr << "Failed to import module '{module_name}'" << std::endl;
        if (PyErr_Occurred()) {{
            PyErr_Print();
        }}
        Py_Finalize();
        return 1;
    }}

    Py_DECREF(module);

    if (Py_FinalizeEx() < 0) {{
        return 120;
    }}

#ifndef _WIN32
    PyMem_RawFree(program);
#endif
    return 0;

config_error:
    std::cerr << "Configuration error: " << status.err_msg << std::endl;
    PyConfig_Clear(&config);
#ifndef _WIN32
    PyMem_RawFree(program);
#endif
    return 1;

init_error:
    std::cerr << "Initialization error: " << status.err_msg << std::endl;
    PyConfig_Clear(&config);
#ifndef _WIN32
    PyMem_RawFree(program);
#endif
    return 1;
}}
"""
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, "w") as f:
        f.write(main_code)
    print(f"Generated main file: {output_path}")


# --- Main Execution Logic ---
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Cython Build Helper for CMake")
    parser.add_argument(
        "--find-python-lib",
        action="store_true",
        help="Find and print absolute path to Python library",
    )
    parser.add_argument(
        "--find-python-include", action="store_true", help="Find and print Python include path"
    )
    parser.add_argument("--cythonize", help="Path to the .pyx file to compile")
    parser.add_argument("--output-dir", help="Directory for generated C/C++ files")
    parser.add_argument("--embed", action="store_true", help="Enable embedding mode for Cython")
    parser.add_argument(
        "--language",
        choices=["c", "c++"],
        default="c",
        help="Output language for Cython (c or c++)",
    )
    parser.add_argument("--generate-main", help="Path to generate the main C++ file")
    parser.add_argument("--install-dir", help="Install directory (used for Python path in main)")
    parser.add_argument("--module-name", help="Python module name of the entry point (for main)")

    args = parser.parse_args()

    output_data = {}

    if args.find_python_lib:
        lib_path = find_python_library()
        if not lib_path:
            print("ERROR: Python library not found!", file=sys.stderr)
            sys.exit(1)
        output_data["python_library"] = lib_path

    if args.find_python_include:
        inc_path = sysconfig.get_path("include")
        if not inc_path or not Path(inc_path).is_dir():
            print("ERROR: Python include path not found or invalid!", file=sys.stderr)
            sys.exit(1)
        output_data["python_include"] = str(Path(inc_path).resolve())

    if args.cythonize:
        if not args.output_dir:
            print("ERROR: --output-dir is required with --cythonize", file=sys.stderr)
            sys.exit(1)
        c_file = run_cython(args.cythonize, args.output_dir, args.embed, args.language)
        output_data["generated_c_file"] = str(Path(c_file).resolve())

    if args.generate_main:
        if not args.install_dir or not args.module_name:
            print(
                "ERROR: --install-dir and --module-name are required with --generate-main",
                file=sys.stderr,
            )
            sys.exit(1)
        main_cpp_path = Path(args.generate_main)
        generate_main(main_cpp_path, args.install_dir, args.module_name)
        output_data["generated_main_file"] = str(main_cpp_path.resolve())

    # Print results for CMake
    for key, value in output_data.items():
        print(f"CMAKE_HELPER_OUTPUT_{key.upper()}:{value}")
