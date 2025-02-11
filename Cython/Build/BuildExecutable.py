"""Compile a Python script into an executable that embeds CPython.

Requires CPython to be built as a shared library ('libpythonX.Y').

Basic usage:

    python -m Cython.Build.BuildExecutable [ARGS] somefile.py
"""

import os
import sys
from pathlib import Path
from typing import Any, List, Optional, Tuple

import rich_click as click

DEBUG: bool = True

if sys.version_info < (3, 9):
    from distutils import sysconfig as _sysconfig

    class sysconfig:
        @staticmethod
        def get_path(name: str) -> str:
            assert name == 'include'
            return _sysconfig.get_python_inc()

        get_config_var = staticmethod(_sysconfig.get_config_var)
else:
    import sysconfig


def collect_python_files(directory: str) -> List[str]:
    """Recursively collect all Python files in a directory."""
    return [str(f) for f in Path(directory).rglob("*.py")]

def get_config_var(name: str, default: str = '') -> str:
    return sysconfig.get_config_var(name) or default

INCDIR: str = sysconfig.get_path('include')
LIBDIR1: str = get_config_var('LIBDIR')
LIBDIR2: str = get_config_var('LIBPL')
PYLIB: str = get_config_var('LIBRARY')
PYLIB_DYN: str = get_config_var('LDLIBRARY')
PYLIB_DYN = '' if PYLIB_DYN == PYLIB else Path(PYLIB_DYN).suffix

CC: str = get_config_var('CC', os.environ.get('CC', ''))
CFLAGS: str = get_config_var('CFLAGS') + ' ' + os.environ.get('CFLAGS', '')
LINKCC: str = get_config_var('LINKCC', os.environ.get('LINKCC', CC))
LINKFORSHARED: str = get_config_var('LINKFORSHARED')
LIBS: str = get_config_var('LIBS')
SYSLIBS: str = get_config_var('SYSLIBS')
EXE_EXT: str = sysconfig.get_config_var('EXE')


def _debug(msg: str, *args: Any) -> None:
    if DEBUG:
        if args:
            msg = msg % args
        sys.stderr.write(msg + '\n')


def dump_config() -> None:
    _debug('INCDIR: %s', INCDIR)
    _debug('LIBDIR1: %s', LIBDIR1)
    _debug('LIBDIR2: %s', LIBDIR2)
    _debug('PYLIB: %s', PYLIB)
    _debug('PYLIB_DYN: %s', PYLIB_DYN)
    _debug('CC: %s', CC)
    _debug('CFLAGS: %s', CFLAGS)
    _debug('LINKCC: %s', LINKCC)
    _debug('LINKFORSHARED: %s', LINKFORSHARED)
    _debug('LIBS: %s', LIBS)
    _debug('SYSLIBS: %s', SYSLIBS)
    _debug('EXE_EXT: %s', EXE_EXT)


def _parse_args(args: List[str]) -> Tuple[str, List[str], List[str]]:
    cy_args: List[str] = []
    last_arg: Optional[str] = None
    for i, arg in enumerate(args):
        if arg.startswith('-') or last_arg in ('-X', '--directive'):
            cy_args.append(arg)
        else:
            input_file = arg
            args = args[i+1:]
            break
        last_arg = arg
    else:
        raise ValueError('no input file provided')

    return input_file, cy_args, args


def runcmd(cmd: List[str], shell: bool = True) -> None:
    if shell:
        cmd_str = ' '.join(cmd)
        _debug(cmd_str)
    else:
        _debug(' '.join(cmd))

    import subprocess
    returncode = subprocess.call(cmd if not shell else ' '.join(cmd), shell=shell)

    if returncode:
        sys.exit(returncode)



def clink(basename: str) -> None:
    runcmd([LINKCC, '-o', basename + EXE_EXT, basename+'.o', '-L'+LIBDIR1, '-L'+LIBDIR2]
           + [PYLIB_DYN and ('-l'+PYLIB_DYN) or Path(LIBDIR1) / PYLIB]
           + LIBS.split() + SYSLIBS.split() + LINKFORSHARED.split())


def ccompile(basename: str) -> None:
    runcmd([CC, '-c', '-o', basename+'.o', basename+'.c', '-I' + INCDIR] + CFLAGS.split())


def cycompile(input_file: str, options: Tuple[str, ...] = ()) -> None:
    from ..Compiler import CmdLine, Main, Version
    options, sources = CmdLine.parse_command_line(list(options or ()) + ['--embed', input_file])
    _debug('Using Cython %s to compile %s', Version.version, input_file)
    result = Main.compile(sources, options)
    if result.num_errors > 0:
        sys.exit(1)


def exec_file(program_name: str, args: Tuple[str, ...] = ()) -> None:
    runcmd([Path(program_name).resolve()] + list(args), shell=False)


def build_one(input_file: str, compiler_args: List[str] = [], force: bool = False) -> str:
    """Build an executable program from a Cython module.

    Returns the name of the executable file.
    """
    p = Path(str(input_file))
    exe_file = p.with_suffix(EXE_EXT)
    if not force and input_file == exe_file:
        raise ValueError("Input and output file names are the same, refusing to overwrite")
    if (not force and  exe_file.exists() and p.exists()
            and p.stat().st_mtime < exe_file.stat().st_mtime):
        _debug("File is up to date, not regenerating %s", exe_file)
        return exe_file
    cycompile(input_file, tuple(compiler_args))
    ccompile(p.name)
    clink(p.name)
    return exe_file


def build(input_path: str, compiler_args: List[str] = [], force: bool = False) -> str:
    """Build an executable from a single Python file or an entire directory."""
    p = Path(input_path)
    py_files = list(p.rglob("*.py")) if p.is_dir() else [p]

    c_files = []
    obj_files = []
    for py_file in py_files:
        basename = py_file.with_suffix("")
        c_file = str(basename) + ".c"
        obj_file = str(basename) + ".o"
        c_files.append(c_file)
        obj_files.append(obj_file)

        cycompile(str(py_file), tuple(compiler_args))
        ccompile(str(basename))

    exe_file = str(input_path.stem) + EXE_EXT
    clink(exe_file, obj_files)

    return exe_file


@click.command()
@click.argument('input_file', type=click.Path(exists=True))
@click.option('--force', is_flag=True, help='Force rebuild even if file is up to date')
@click.option('--debug', is_flag=True, help='Enable debug output')
def main(input_file: str, force: bool = False, debug: bool = False) -> None:
    """Build an executable program from a Cython module."""
    global DEBUG
    DEBUG = debug
    if debug:
        dump_config()
    program_name = build(input_file, force=force)
    console = click.get_console()
    console.print(f"[green]Successfully built:[/green] {program_name}")


if __name__ == '__main__':
    main()
