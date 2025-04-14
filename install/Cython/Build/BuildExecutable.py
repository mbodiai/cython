"""
Compile a Python script into an executable that embeds CPython.
Requires CPython to be built as a shared library ('libpythonX.Y').

Basic usage:

    python -m Cython.Build.BuildExecutable [ARGS] somefile.py
"""


DEBUG = True

from pathlib import Path
import sys
import os
import ctypes.util
import sysconfig
import platform

if sys.version_info < (3, 9):
    from distutils import sysconfig as _sysconfig

    class sysconfig:

        @staticmethod
        def get_path(name):
            assert name == 'include'
            return _sysconfig.get_python_inc()

        get_config_var = staticmethod(_sysconfig.get_config_var)
else:
    # sysconfig can be trusted from cpython >= 3.8.7
    import sysconfig

def _debug(msg, *args):
    if DEBUG:
        if args:
            msg = msg % args
        sys.stderr.write(msg + '\n')

def find_python_library() -> str | None:
    """Find the correct Python shared library.

    Handles standard installs, virtualenvs, and macOS Framework builds.
    """

    def check_path(path):
        p = Path(path)
        return str(p.resolve()) if p.exists() else None

    # --- Try macOS Framework Path First ---
    if sys.platform == 'darwin':
        # Use PYTHONFRAMEWORKPREFIX to get the base install location
        prefix = sysconfig.get_config_var('PYTHONFRAMEWORKPREFIX')
        if prefix and prefix != '/usr/local': # Avoid standard prefixes where it might not be a framework
            # Expected path within the prefix
            framework_path = Path(prefix) / 'Python.framework' / 'Versions' / f'{sys.version_info.major}.{sys.version_info.minor}' / 'Python'
            if DEBUG: print(f"Checking framework path based on prefix: {framework_path}")
            shared_lib = check_path(framework_path)
            if shared_lib:
                if DEBUG: print(f"Found framework library (prefix): {shared_lib}")
                return shared_lib
            # Try alternative structure
            alt_framework_path = Path(prefix) / 'Python.framework' / 'Python'
            if DEBUG: print(f"Checking alt framework path based on prefix: {alt_framework_path}")
            shared_lib = check_path(alt_framework_path)
            if shared_lib:
                 if DEBUG: print(f"Found alt framework library (prefix): {shared_lib}")
                 return shared_lib

    # --- Try standard sysconfig path (might be relative or absolute) ---
    lib_name = sysconfig.get_config_var('LDLIBRARY') or ''
    lib_dir = sysconfig.get_config_var('LIBDIR') or ''
    if DEBUG: print(f"Sysconfig LDLIBRARY: {lib_name}")
    if DEBUG: print(f"Sysconfig LIBDIR: {lib_dir}")
    if lib_name and lib_dir:
        # Check if lib_name is already absolute
        if Path(lib_name).is_absolute():
             shared_lib = check_path(lib_name)
             if shared_lib:
                 if DEBUG: print(f"Found absolute LDLIBRARY: {shared_lib}")
                 return shared_lib
        # Check relative to LIBDIR
        shared_lib = check_path(Path(lib_dir) / lib_name)
        if shared_lib:
            if DEBUG: print(f"Found LDLIBRARY relative to LIBDIR: {shared_lib}")
            return shared_lib

    # --- Try ctypes.util.find_library ---
    ctypes_lib_name = f"python{sys.version_info.major}.{sys.version_info.minor}"
    found = ctypes.util.find_library(ctypes_lib_name)
    if DEBUG: print(f"Checking ctypes.util.find_library({ctypes_lib_name!r}): {found}")
    if found:
        shared_lib = check_path(found)
        if shared_lib:
             if DEBUG: print(f"Found via ctypes: {shared_lib}")
             return shared_lib

    # --- Fallback: Search common candidate directories for lib_name ---
    if lib_name: # Only search if we have a name from sysconfig
        candidate_dirs = [
            Path(getattr(sys, 'base_prefix', sys.prefix)) / 'lib', # Venv/prefix lib
            Path(sys.prefix) / 'lib', # Should be same as above in venv
            Path('/usr/lib'),
            Path('/usr/local/lib'),
            Path('/opt/homebrew/lib'), # For Homebrew on Apple Silicon
        ]
        if DEBUG: print(f"Checking candidate dirs for {lib_name}...")
        for d in candidate_dirs:
            if not d.is_dir(): continue
            candidate = d / lib_name
            if DEBUG: print(f"  Checking candidate: {candidate}")
            if candidate.exists():
                shared_lib = str(candidate.resolve())
                if DEBUG: print(f"  Found candidate: {shared_lib}")
                return shared_lib

    if DEBUG: print("Library search exhausted.")
    return None # Not found

def get_config_var(name, default=''):
    """Retrieve config variable dynamically, ensuring compatibility."""
    value = sysconfig.get_config_vars().get(name)
    return value if value is not None else default

# Replace SO with EXT_SUFFIX
EXT_SUFFIX = get_config_var('EXT_SUFFIX')

INCDIR = sysconfig.get_path('include')
LIBDIR1 = get_config_var('LIBDIR')
LIBDIR2 = get_config_var('LIBPL') or sysconfig.get_path('stdlib')  # Fallback

PYLIB = get_config_var('LIBRARY')
# Use the new function to find the dynamic library path
PYLIB_DYN = find_python_library() 

if not PYLIB_DYN:
    # Fallback or raise error if library not found
    _debug("WARNING: Could not find Python shared library using find_python_library(). Falling back to sysconfig.")
    PYLIB_DYN = get_config_var('LDLIBRARY')
    if not PYLIB_DYN:
         raise FileNotFoundError("Python shared library not found by any method.")

CC = get_config_var('CC', os.environ.get('CC', ''))
CFLAGS = get_config_var('CFLAGS') + ' ' + os.environ.get('CFLAGS', '')
LINKCC = get_config_var('LINKCC', os.environ.get('LINKCC', CC))
LINKFORSHARED = get_config_var('LINKFORSHARED')
LIBS = get_config_var('LIBS')
SYSLIBS = get_config_var('SYSLIBS')
EXE_EXT = get_config_var('EXE')

# Ensure debug output reflects the updates
def dump_config():
    _debug('INCDIR: %s', INCDIR)
    _debug('LIBDIR1: %s', LIBDIR1)
    _debug('LIBDIR2: %s', LIBDIR2)
    _debug('PYLIB (static): %s', PYLIB)
    _debug('PYLIB_DYN (dynamic): %s', PYLIB_DYN)
    _debug('CC: %s', CC)
    _debug('CFLAGS: %s', CFLAGS)
    _debug('LINKCC: %s', LINKCC)
    _debug('LINKFORSHARED: %s', LINKFORSHARED)
    _debug('LIBS: %s', LIBS)
    _debug('SYSLIBS: %s', SYSLIBS)
    _debug('EXE_EXT: %s', EXE_EXT)

def _parse_args(args):
    cy_args = []
    last_arg = None
    for i, arg in enumerate(args):
        if arg.startswith('-'):
            cy_args.append(arg)
        elif last_arg in ('-X', '--directive'):
            cy_args.append(arg)
        else:
            input_file = arg
            args = args[i+1:]
            break
        last_arg = arg
    else:
        raise ValueError('no input file provided')
    
    return input_file, cy_args, args

def runcmd(cmd, shell=True):
    if shell:
        cmd = ' '.join(cmd)
        _debug(cmd)
    else:
        _debug(' '.join(cmd))

    import subprocess
    returncode = subprocess.call(cmd, shell=shell)

    if returncode:
        sys.exit(returncode)


def clink(basename):
    is_msvc = platform.system() == "Windows" and "cl" in LINKCC.lower()
    obj_ext = '.obj' if is_msvc else '.o'
    input_obj = basename + obj_ext
    output_exe = basename + EXE_EXT # EXE_EXT should be correct for platform via sysconfig

    if is_msvc:
        # MSVC command: link /OUT:<exe> <obj> /LIBPATH:<dir1> <lib1> <lib2> ... [LINKFORSHARED] [LIBS] [SYSLIBS]
        cmd = [LINKCC, f'/OUT:{output_exe}', input_obj]
        # Add library paths
        if LIBDIR1: cmd.append(f'/LIBPATH:{LIBDIR1}')
        if LIBDIR2: cmd.append(f'/LIBPATH:{LIBDIR2}')

        # Add Python library - MUST find the .lib import library
        # Assuming find_python_library finds the DLL, we need the corresponding .lib
        # This requires enhancing find_python_library or adding a new function
        python_lib_file = 'pythonXY.lib' # Placeholder - Needs correct finding logic!
        # Potential logic: Use sysconfig.get_config_var('python_lib') or search near DLL
        cmd.append(python_lib_file)

        # Add other libraries (split and potentially map names/flags)
        if LIBS: cmd.extend(LIBS.split()) # May need adjustment for MSVC
        if SYSLIBS: cmd.extend(SYSLIBS.split()) # May need adjustment for MSVC
        if LINKFORSHARED: cmd.extend(LINKFORSHARED.split()) # May need adjustment for MSVC

        # Prepend /link for cl.exe if LINKCC is cl
        if LINKCC.lower().endswith('cl.exe') or LINKCC == 'cl':
             cmd.insert(1, '/link')
    else:
        # GCC/Clang command: linkcc -o <exe> <obj> -L<dir1> -L<dir2> <abs_python_lib> [LIBS] [SYSLIBS] [LINKFORSHARED]
        cmd = [LINKCC, '-o', output_exe, input_obj]
        if LIBDIR1: cmd.append(f'-L{LIBDIR1}')
        if LIBDIR2: cmd.append(f'-L{LIBDIR2}')
        
        # Add the found absolute path to the dynamic library (PYLIB_DYN)
        cmd.append(PYLIB_DYN)
        
        # Add other libraries
        if LIBS: cmd.extend(LIBS.split())
        if SYSLIBS: cmd.extend(SYSLIBS.split())
        if LINKFORSHARED: cmd.extend(LINKFORSHARED.split())

    runcmd(cmd)


def ccompile(basename):
    compiler = CC
    is_msvc = platform.system() == "Windows" and "cl" in compiler.lower()

    c_file = Path(basename + ".c")
    cpp_file = Path(basename + ".cpp")

    if cpp_file.exists():
        source_file = str(cpp_file)
        # Use CXX or deduce from CC if possible for C++
        compiler = LINKCC # Usually CXX compiler is same as Linker CXX
        is_msvc = platform.system() == "Windows" and "cl" in compiler.lower()
        if not is_msvc and not compiler.endswith("++"):
             # Simple guess if LINKCC wasn't C++ specific
             if compiler.endswith("clang"): compiler += "++"
             elif compiler.endswith("gcc"): compiler += "g++"
    elif c_file.exists():
        source_file = str(c_file)
    else:
        raise FileNotFoundError(f"Neither {cpp_file} nor {c_file} exist.")

    output_obj = basename + '.obj' if is_msvc else basename + '.o'

    if is_msvc:
        # MSVC command: cl /c /Fo<obj> /I<inc> <src> [CFLAGS]
        cmd = [compiler, '/c', f'/Fo{output_obj}', f'/I{INCDIR}', source_file]
        # Need to parse CFLAGS appropriately for MSVC (e.g., /O2, /MD, etc.)
        # This is simplified - a robust solution would parse/translate flags
        if CFLAGS: cmd.extend(CFLAGS.split()) # Basic split, may not be correct
    else:
        # GCC/Clang command: cc -c -o <obj> -I<inc> <src> [CFLAGS]
        cmd = [compiler, '-c', '-o', output_obj, f'-I{INCDIR}', source_file]
        if CFLAGS: cmd.extend(CFLAGS.split())

    runcmd(cmd)


def cycompile(input_file, options=()):
    from ..Compiler import Version, CmdLine, Main
    options, sources = CmdLine.parse_command_line(list(options or ()) + ['--embed', input_file])
    _debug('Using Cython %s to compile %s', Version.version, input_file)
    result = Main.compile(sources, options)
    if result.num_errors > 0:
        sys.exit(1)


def exec_file(program_name, args=()):
    runcmd([os.path.abspath(program_name)] + list(args), shell=False)


def build(input_file, compiler_args=(), force=False):
    """
    Build an executable program from a Cython module.

    Returns the name of the executable file.
    """
    basename = os.path.splitext(input_file)[0]
    exe_file = basename + EXE_EXT
    if not force and os.path.abspath(exe_file) == os.path.abspath(input_file):
        raise ValueError("Input and output file names are the same, refusing to overwrite")
    if (not force and os.path.exists(exe_file) and os.path.exists(input_file)
            and os.path.getmtime(input_file) <= os.path.getmtime(exe_file)):
        _debug("File is up to date, not regenerating %s", exe_file)
        return exe_file
    cycompile(input_file, compiler_args)
    ccompile(basename)
    clink(basename)
    return exe_file


def build_and_run(args):
    """
    Build an executable program from a Cython module and run it.

    Arguments after the module name will be passed verbatimly to the program.
    """
    program_name, args = _build(args)
    exec_file(program_name, args)


def _build(args):
    input_file, cy_args, args = _parse_args(args)
    program_name = build(input_file, cy_args)
    return program_name, args


if __name__ == '__main__':
    dump_config()
    _build(sys.argv[1:])
