import os
import sys
import shutil
import tempfile
import json
import platform
import subprocess
from collections import defaultdict
from typing import TypedDict, List, Dict, Optional, Any, Union, Literal, Set
from os.path import isdir, exists, dirname, join, islink, realpath

# Config directory and file for OpenMP preferences
def get_openmp_config():
    """Get the OpenMP configuration file path and ensure the directory exists."""
    config_dir = os.path.join(os.path.expanduser("~"), ".config", "cython")
    if not os.path.exists(config_dir):
        os.makedirs(config_dir, exist_ok=True)
    return os.path.join(config_dir, "openmp_config.json")

# Check for OpenMP support on the system
def check_openmp_support():
    """Check if OpenMP is supported on this system and return info."""
    openmp_supported = True
    clang_path = None
    compiler_info = ""
    
    # On macOS, check for LLVM clang with OpenMP support
    if platform.system() == "Darwin":
        compiler_info += "Detecting LLVM/Clang with OpenMP support on macOS...\n"
        # Try to find clang++ from LLVM (installed via Homebrew or similar)
        clang_candidates = ["clang++-mp-15", "clang++-15", "clang++-mp-14", "clang++-14", "clang++-mp", "clang++"]
        for clang in clang_candidates:
            path = shutil.which(clang)
            compiler_info += f"Checking for {clang}: {'Found at ' + path if path else 'Not found'}\n"
        
        # Check if any of these are available in PATH
        for clang in clang_candidates:
            if shutil.which(clang):
                try:
                    # Try to run the compiler with OpenMP flag to see if it works
                    compiler_info += f"Testing {clang} for OpenMP support...\n"
                    subprocess.check_call(
                        [clang, "-fopenmp", "-dM", "-E", "-"], 
                        stdin=subprocess.PIPE, 
                        stdout=subprocess.PIPE, 
                        stderr=subprocess.PIPE
                    )
                    clang_path = shutil.which(clang)
                    # Found a working clang with OpenMP
                    compiler_info += f"Found {clang} with OpenMP support at {clang_path}\n"
                    break
                except (subprocess.SubprocessError, OSError) as e:
                    compiler_info += f"Failed to validate OpenMP support for {clang}: {str(e)}\n"
                    pass
        
        if not clang_path:
            compiler_info += "No suitable clang with OpenMP support found. OpenMP will be disabled on macOS.\n"
            openmp_supported = False
    elif platform.system() == "Windows":
        # Windows: MSVC typically supports OpenMP
        try:
            subprocess.check_call(
                ["cl", "/openmp", "/E", "NUL"], 
                stdout=subprocess.PIPE, 
                stderr=subprocess.PIPE
            )
            compiler_info += "MSVC with OpenMP support detected.\n"
        except (subprocess.SubprocessError, OSError):
            try:
                # Check for MinGW/GCC
                subprocess.check_call(
                    ["gcc", "-fopenmp", "-E", "-"], 
                    stdin=subprocess.PIPE,
                    stdout=subprocess.PIPE, 
                    stderr=subprocess.PIPE
                )
                compiler_info += "MinGW/GCC with OpenMP support detected.\n"
            except (subprocess.SubprocessError, OSError):
                compiler_info += "No compatible compiler with OpenMP support found on Windows.\n"
                openmp_supported = False
    else:
        # Linux and other Unix-like systems: typically GCC supports OpenMP
        try:
            subprocess.check_call(
                ["gcc", "-fopenmp", "-E", "-"], 
                stdin=subprocess.PIPE,
                stdout=subprocess.PIPE, 
                stderr=subprocess.PIPE
            )
            compiler_info += "GCC with OpenMP support detected.\n"
        except (subprocess.SubprocessError, OSError):
            compiler_info += "No compatible compiler with OpenMP support found.\n"
            openmp_supported = False
    
    return openmp_supported, clang_path, compiler_info

# Fix Python's library paths function
def fix_python_library_paths():
    """
    Fix Python's library paths to ensure the correct dynamic library is found
    during compilation, regardless of platform, architecture or Python version.
    """
    import sysconfig
    
    # Get key paths from sysconfig
    config_libdir = sysconfig.get_config_var('LIBDIR')
    prefix = sysconfig.get_config_var('prefix')
    exec_prefix = sysconfig.get_config_var('exec_prefix') or prefix
    ldlibrary = sysconfig.get_config_var('LDLIBRARY')
    
    # Find the actual lib directory where Python's dynamic library is located
    actual_lib_dirs = []
    
    # First, check if we're running from a real Python installation or a virtual env
    real_executable = sys.executable
    if islink(real_executable):
        real_executable = realpath(real_executable)
    
    # Try to find the library based on the executable path
    exe_dir = dirname(real_executable)
    potential_lib_dirs = [
        # Standard layouts
        join(dirname(exe_dir), 'lib'),            # ../lib from bin
        join(dirname(dirname(exe_dir)), 'lib'),   # ../../lib from bin
        # For macOS framework builds
        join(dirname(exe_dir), 'lib'),
        # For Windows
        join(dirname(exe_dir), 'libs'),
        exe_dir,  # Sometimes libraries are right next to the executable
    ]
    
    # Also try the configured lib directory
    if config_libdir and isdir(config_libdir):
        potential_lib_dirs.append(config_libdir)
    
    # Add lib dirs relative to sys.prefix and exec_prefix
    if prefix:
        potential_lib_dirs.append(join(prefix, 'lib'))
    if exec_prefix and exec_prefix != prefix:
        potential_lib_dirs.append(join(exec_prefix, 'lib'))
    
    # Look for the Python library in potential directories
    for lib_dir in potential_lib_dirs:
        if not isdir(lib_dir):
            continue
            
        # Look for the library file
        if ldlibrary:
            full_path = join(lib_dir, ldlibrary)
            if exists(full_path):
                actual_lib_dirs.append(lib_dir)
        
        # On Windows, we also check for the Python DLL
        if sys.platform == 'win32':
            dll_name = f'python{sys.version_info.major}{sys.version_info.minor}.dll'
            if exists(join(lib_dir, dll_name)):
                actual_lib_dirs.append(lib_dir)
    
    # Remove duplicates while preserving order
    actual_lib_dirs = list(dict.fromkeys(actual_lib_dirs))
    
    # Add the real library directory to environment variables
    if actual_lib_dirs:
        # Update the library search path environment variables
        if sys.platform == 'win32':
            path = os.environ.get('PATH', '')
            paths = path.split(os.pathsep)
            for lib_dir in actual_lib_dirs:
                if lib_dir not in paths:
                    paths.insert(0, lib_dir)
            os.environ['PATH'] = os.pathsep.join(paths)
        elif sys.platform == 'darwin':
            # macOS uses DYLD_LIBRARY_PATH
            dyld_path = os.environ.get('DYLD_LIBRARY_PATH', '')
            paths = dyld_path.split(os.pathsep) if dyld_path else []
            for lib_dir in actual_lib_dirs:
                if lib_dir not in paths:
                    paths.insert(0, lib_dir)
            if paths:
                os.environ['DYLD_LIBRARY_PATH'] = os.pathsep.join(paths)
        else:
            # Linux and most other UNIX-like systems use LD_LIBRARY_PATH
            ld_path = os.environ.get('LD_LIBRARY_PATH', '')
            paths = ld_path.split(os.pathsep) if ld_path else []
            for lib_dir in actual_lib_dirs:
                if lib_dir not in paths:
                    paths.insert(0, lib_dir)
            if paths:
                os.environ['LD_LIBRARY_PATH'] = os.pathsep.join(paths)
    
    # Now patch the compiler's link method
    def patch_compiler_link():
        import distutils.ccompiler
        
        # Store the original link function
        original_link = distutils.ccompiler.CCompiler.link
        
        # Override with our fixed version
        def fixed_link(self, *args, **kwargs):
            if len(args) > 2 and 'library_dirs' in kwargs:
                # Filter out non-existent directories
                library_dirs = [
                    lib_dir for lib_dir in kwargs['library_dirs'] 
                    if exists(lib_dir)
                ]
                
                # Add our actual library directories
                for lib_dir in actual_lib_dirs:
                    if lib_dir not in library_dirs:
                        library_dirs.append(lib_dir)
                
                kwargs['library_dirs'] = library_dirs
            
            return original_link(self, *args, **kwargs)
        
        # Apply the patch
        distutils.ccompiler.CCompiler.link = fixed_link
    
    return patch_compiler_link

# Apply the patch immediately
_patch_compiler = fix_python_library_paths()

import rich_click as click
from Cython.Build.Dependencies import cythonize, extended_iglob
from Cython.Utils import is_package_dir
from Cython.Compiler import Options
from Cython.Compiler.Options import CompilerDirectivesDict, CompileTimeEnvDict
from rich.box import Box
from dataclasses import dataclass, field
from rich_click.rich_help_configuration import RichHelpConfiguration

try:
    import multiprocessing
    parallel_compiles = int(multiprocessing.cpu_count() * 1.5)
except ImportError:
    multiprocessing = None
    parallel_compiles = 0


# Cythonize options TypedDict
class CythonizeOptionsDict(TypedDict, total=False):
    """TypedDict for Cythonize options."""
    directives: CompilerDirectivesDict
    options: Dict[str, Any]
    compile_time_env: CompileTimeEnvDict
    language: Optional[str]
    cxx_flags: Optional[str]
    annotate: Optional[Union[bool, str]]
    build: bool
    build_inplace: bool
    force: bool
    quiet: bool
    keep_going: bool
    no_docstrings: bool
    exclude: List[str]  # Changed from 'excludes' to 'exclude'
    parallel: int
    benchmark: Optional[str]
    benchmark_setup: Optional[str]
    depfile: bool
    language_level: Optional[Union[int, str]]
    lenient: bool
    sources: List[str]
    openmp: Optional[str]


# For Pydantic with kwargs
class CythonizeOptions:
    """Pydantic BaseModel equivalent for Cythonize options with kwargs."""
    def __init__(self, **kwargs):
        self.directives: Dict[str, Any] = kwargs.get('directives', {})
        self.options: Dict[str, Any] = kwargs.get('options', {})
        self.compile_time_env: Dict[str, Any] = kwargs.get('compile_time_env', {})
        self.language: Optional[str] = kwargs.get('language', None)
        self.cxx_flags: Optional[str] = kwargs.get('cxx_flags', None)
        self.annotate: Optional[Union[bool, str]] = kwargs.get('annotate', None)
        self.build: bool = kwargs.get('build', False)
        self.build_inplace: bool = kwargs.get('build_inplace', False)
        self.force: bool = kwargs.get('force', False)
        self.quiet: bool = kwargs.get('quiet', False)
        self.keep_going: bool = kwargs.get('keep_going', False)
        self.no_docstrings: bool = kwargs.get('no_docstrings', False)
        self.exclude: List[str] = kwargs.get('exclude', [])
        self.parallel: int = kwargs.get('parallel', parallel_compiles)
        self.benchmark: Optional[str] = kwargs.get('benchmark', None)
        self.benchmark_setup: Optional[str] = kwargs.get('benchmark_setup', None)
        self.depfile: bool = kwargs.get('depfile', False)
        self.language_level: Optional[Union[int, str]] = kwargs.get('language_level', None)
        self.lenient: bool = kwargs.get('lenient', False)
        self.sources: List[str] = kwargs.get('sources', [])
        self.openmp: Optional[str] = kwargs.get('openmp', 'auto')  # 'auto', 'enable', 'disable'


class _FakePool:
    def map_async(self, func, args):
        for _ in map(func, args):
            pass

    def close(self):
        pass

    def terminate(self):
        pass

    def join(self):
        pass


def find_package_base(path):
    base_dir, package_path = os.path.split(path)
    while is_package_dir(base_dir):
        base_dir, parent = os.path.split(base_dir)
        package_path = '%s/%s' % (parent, package_path)
    return base_dir, package_path


def cython_compile(path_pattern, options):
    all_paths = map(os.path.abspath, extended_iglob(path_pattern))
    ext_modules_by_basedir = _cython_compile_files(all_paths, options)
    _build(list(ext_modules_by_basedir.items()), options.parallel)
    return ext_modules_by_basedir


def _cython_compile_files(all_paths, options):
    ext_modules_to_build = defaultdict(list)

    for path in all_paths:
        if options.build_inplace:
            base_dir = path
            while not os.path.isdir(base_dir) or is_package_dir(base_dir):
                base_dir = os.path.dirname(base_dir)
        else:
            base_dir = None

        if os.path.isdir(path):
            # recursively compiling a package
            paths = [os.path.join(path, '**', '*.{py,pyx}')]
        else:
            # assume it's a file(-like thing)
            paths = [path]

        ext_modules = cythonize(
            paths,
            nthreads=options.parallel,
            exclude_failures=options.keep_going,
            exclude=options.exclude,
            compiler_directives=options.directives,
            compile_time_env=options.compile_time_env,
            force=options.force,
            quiet=options.quiet,
            depfile=options.depfile,
            language=options.language,
            **options.options)

        if ext_modules and options.build:
            ext_modules_to_build[base_dir].extend(ext_modules)

    return dict(ext_modules_to_build)


def _build(ext_modules, parallel):
    modcount = sum(len(modules) for _, modules in ext_modules)
    if not modcount:
        return
    if modcount == 1 or parallel < 2:
        run_distutils(ext_modules[0])
        return

    try:
        pool = multiprocessing.Pool(parallel)
    except OSError:
        pool = _FakePool()
    try:
        pool.map_async(run_distutils, [
            (base_dir, [ext]) for base_dir, modules in ext_modules for ext in modules])
    except:
        pool.terminate()
        raise
    else:
        pool.close()
        pool.join()


def run_distutils(args):
    try:
        from distutils.core import setup
    except ImportError:
        try:
            from setuptools import setup
        except ImportError:
            raise ImportError("'distutils' is not available. Please install 'setuptools' for binary builds.")

    base_dir, ext_modules = args
    script_args = ['build_ext', '-i']
    cwd = os.getcwd()
    temp_dir = None
    try:
        if base_dir:
            os.chdir(base_dir)
            temp_dir = tempfile.mkdtemp(dir=base_dir)
            script_args.extend(['--build-temp', temp_dir])
        setup(
            script_name='setup.py',
            script_args=script_args,
            ext_modules=ext_modules,
        )
    finally:
        if base_dir:
            os.chdir(cwd)
            if temp_dir and os.path.isdir(temp_dir):
                shutil.rmtree(temp_dir)


def benchmark(code, setup_code=None, import_module=None, directives=None):
    from Cython.Build.Inline import cymeit

    timings, number = cymeit(code, setup_code, import_module, directives, repeat=9)

    # Based on 'timeit.main()' in CPython 3.13.
    units = {"nsec": 1e-9, "usec": 1e-6, "msec": 1e-3, "sec": 1.0}
    scales = [(scale, unit) for unit, scale in reversed(units.items())]  # biggest first

    def format_time(t):
        for scale, unit in scales:
            if t >= scale:
                break
        else:
            raise RuntimeError("Timing is below nanoseconds: {t:f}")
        return f"{t / scale :.3f} {unit}"

    timings.sort()
    assert len(timings) & 1 == 1  # odd number of timings, for median position
    fastest, median, slowest = timings[0], timings[len(timings) // 2], timings[-1]

    print(f"{number} loops, best of {len(timings)}: {format_time(fastest)} per loop (median: {format_time(median)})")

    if slowest > fastest * 4:
        print(
            "The timings are likely unreliable. "
            f"The worst time ({format_time(slowest)}) was more than four times "
            f"slower than the best time ({format_time(fastest)}).")


def config_from_setup_cfg(filepath="setup.cfg"):
    """
    Read configuration from setup.cfg file.
    
    Returns a dictionary with configuration values for cythonize.
    """
    import configparser
    from os.path import exists
    
    defaults = {
        "directives": {},
        "options": {"compiler_directives": {}, "compile_time_env": {}},
        "compile_time_env": {},
        "language": None,
        "cxx_flags": None,
        "annotate": None,
        "build": False,
        "build_inplace": False,
        "force": False,
        "quiet": False,
        "keep_going": False,
        "no_docstrings": False, 
        "exclude": [],
        "parallel": parallel_compiles,
        "benchmark": None,
        "benchmark_setup": None,
        "depfile": False,
        "language_level": None,
        "lenient": False,
        "sources": [],
    }
    
    if not exists(filepath):
        return defaults
    
    config = configparser.ConfigParser()
    config.read(filepath)
    
    # Read build_ext section
    if "build_ext" in config:
        build_ext = config["build_ext"]
        if "cplus" in build_ext and build_ext["cplus"].lower() in ("true", "yes", "1", "y"):
            defaults["language"] = "c++"
        if "cxxflags" in build_ext:
            defaults["cxx_flags"] = build_ext["cxxflags"]
            # Also add to compile_time_env
            defaults["compile_time_env"]["CXX_FLAGS"] = build_ext["cxxflags"]
    
    # Read cython section
    if "cython" in config:
        cython_section = config["cython"]
        if "language_level" in cython_section:
            defaults["language_level"] = cython_section["language_level"]
            defaults["options"]["language_level"] = cython_section["language_level"]
        
        if "annotate" in cython_section:
            annotate_val = cython_section["annotate"].lower()
            if annotate_val in ("true", "yes", "1", "y"):
                defaults["annotate"] = "default"
            elif annotate_val == "fullc":
                defaults["annotate"] = "fullc"
        
        # Read compiler directives
        directive_keys = [
            "boundscheck", "wraparound", "initializedcheck", "nonecheck",
            "overflowcheck", "cdivision", "cdivision_warnings", "always_allow_keywords",
            "profile", "linetrace", "infer_types", "language_level"
        ]
        
        for key in directive_keys:
            if key in cython_section:
                value = cython_section[key]
                if value.lower() in ("true", "yes", "1", "y"):
                    defaults["directives"][key] = True
                elif value.lower() in ("false", "no", "0", "n"):
                    defaults["directives"][key] = False
                else:
                    try:
                        defaults["directives"][key] = int(value)
                    except ValueError:
                        defaults["directives"][key] = value
    
    return defaults


# Configure rich-click settings
NO_BOX = Box("    \n" * 8)

@dataclass
class CythonizeHelpConfig(RichHelpConfiguration):
    """Custom help configuration to remove borders from output."""
    
    # Remove all panels/boxes
    style_options_panel_box: "str | Box | None" = field(default=NO_BOX)
    style_commands_panel_box: "str | Box | None" = field(default=NO_BOX)
    style_errors_panel_box: "str | Box | None" = field(default=NO_BOX)
    style_options_table_show_lines: bool = field(default=False)
    style_commands_table_show_lines: bool = field(default=False)
    
    # Basic configuration
    show_arguments: bool = field(default=False)  # Hide the arguments panel
    group_arguments_options: bool = field(default=True)
    text_markup: str = field(default='rich')
    align_options_panel: str = field(default="left")
    
    # Style settings for headers - make them gray
    style_option_groups_headers: "rich.style.StyleType" = field(default="dim")
    
    # Keep option groups
    option_groups: dict = field(default_factory=lambda: {
        "main": [
            {
                "name": "GENERAL OPTIONS",
                "options": ["--3str", "--help"],
            },
            {
                "name": "BUILD OPTIONS",
                "options": ["--build", "--inplace", "--force", "--quiet", "--keep-going", "--parallel"],
            },
            {
                "name": "C/C++ OPTIONS", 
                "options": ["--cplus", "--cxxflags"],
            },
            {
                "name": "PYTHON OPTIONS",
                "options": ["--language-level", "--no-docstrings", "--lenient"],
            },
            {
                "name": "OUTPUT OPTIONS",
                "options": ["--annotate", "--annotate-fullc", "--depfile"],
            },
            {
                "name": "CONFIGURATION OPTIONS",
                "options": ["--directive", "--compile-time-env", "--option", "--exclude"],
            },
            {
                "name": "BENCHMARK OPTIONS",
                "options": ["--timeit", "--setup"],
            }
        ]
    })

# Apply basic rich-click styling options
click.rich_click.USE_RICH_MARKUP = True

# Helper class for directives
class DirectivesParamType(click.ParamType):
    name = "directive"

    def convert(self, value, param, ctx):
        try:
            name, val = value.split("=", 1)
            if val.lower() in ('true', 'yes', '1'):
                val = True
            elif val.lower() in ('false', 'no', '0'):
                val = False
            else:
                try:
                    val = int(val)
                except ValueError:
                    pass
            return name, val
        except ValueError:
            self.fail(f"Invalid directive format: {value}. Use NAME=VALUE format.", param, ctx)


# Helper class for env vars
class EnvVarParamType(click.ParamType):
    name = "env_var"

    def convert(self, value, param, ctx):
        try:
            name, val = value.split("=", 1)
            return name, val
        except ValueError:
            self.fail(f"Invalid environment format: {value}. Use NAME=VALUE format.", param, ctx)


@click.command(
    help="Compile Cython code to C/C++ and build extensions",
    context_settings={"max_content_width": 100}
)
@click.rich_config(help_config=CythonizeHelpConfig())
@click.argument("sources", nargs=-1, metavar="SOURCE")
@click.option("-b", "--build", is_flag=True, help="Build extension modules using setuptools")
@click.option("-i", "--inplace", "build_inplace", is_flag=True, help="Build extension modules in place (implies --build)")
@click.option("-f", "--force", is_flag=True, help="Force recompilation regardless of timestamps")
@click.option("-q", "--quiet", is_flag=True, help="Be less verbose during compilation")
@click.option("-k", "--keep-going", is_flag=True, help="Keep going after errors")
@click.option("-j", "--parallel", default=parallel_compiles, type=int, help=f"Run builds in parallel (default: {parallel_compiles or 1})")
@click.option("-+", "--cplus", "language", flag_value="c++", help="Output C++ rather than C files")
@click.option("--cxxflags", "cxx_flags", help="Additional C++ compiler flags")
@click.option("-2", "--language-level", flag_value=2, help="Use Python 2 syntax mode")
@click.option("-3", "--language-level", flag_value=3, help="Use Python 3 syntax mode (default)")
@click.option("--3str", "language_level", flag_value="3str", help="Use Python 3 syntax mode with str literals (deprecated)")
@click.option("-a", "--annotate", flag_value="default", help="Create annotated HTML version of the source")
@click.option("--annotate-fullc", "annotate", flag_value="fullc", help="Include full generated C code in the annotations")
@click.option("--no-docstrings", is_flag=True, help="Strip docstrings")
@click.option("--lenient", is_flag=True, help="Increase Python compatibility by ignoring some errors")
@click.option("-X", "--directive", "directives", multiple=True, type=DirectivesParamType(), help="Compiler directive, e.g. boundscheck=False")
@click.option("-E", "--compile-time-env", "compile_time_env_items", multiple=True, type=EnvVarParamType(), help="Compile-time environment, e.g. CXX_FLAGS='-std=c++17'")
@click.option("-s", "--option", "option_items", multiple=True, type=DirectivesParamType(), help="Set cythonize option")
@click.option("-M", "--depfile", is_flag=True, help="Produce depfiles for sources")
@click.option("-x", "--exclude", multiple=True, help="Exclude pattern for files/directories")
@click.option("--timeit", "benchmark", help="Benchmark the given code snippet")
@click.option("--setup", "benchmark_setup", help="Setup code for benchmark")
@click.option("--openmp", type=click.Choice(['auto', 'enable', 'disable']), default='auto', 
              help="OpenMP support: auto (detect), enable (required), disable (never)")
@click.option("--force-openmp-check", is_flag=True, 
              help="Force recheck for OpenMP support, ignoring cached configuration")
def main(sources, build, build_inplace, force, quiet, keep_going, parallel, language, 
         language_level, cxx_flags, annotate, no_docstrings, lenient, directives, 
         compile_time_env_items, option_items, depfile, exclude, benchmark, benchmark_setup,
         openmp, force_openmp_check):
    """
    [bold]Cython[/bold] compiler for code written in the Cython language.
    """
    if not sources:
        click.secho("Error: No source files provided", fg="red")
        ctx = click.get_current_context()
        click.echo(ctx.get_help())
        return 1
    
    # Handle OpenMP configuration
    config_file = get_openmp_config()
    config = {}
    use_openmp = False
    
    # Check if we're running interactively (can prompt user)
    is_interactive = sys.stdout.isatty() and not any(arg in ['--quiet', '-q'] for arg in sys.argv)
    
    # Load previous configuration if available
    if os.path.exists(config_file) and not force_openmp_check:
        try:
            with open(config_file, 'r') as f:
                config = json.load(f)
            if not quiet:
                click.echo(f"Loaded cached OpenMP configuration: {config}")
        except Exception as e:
            if not quiet:
                click.echo(f"Error loading OpenMP config file: {e}")
            config = {}
    
    # Check if we have a remembered preference
    has_saved_preference = 'openmp_enabled' in config and 'openmp_supported' in config
    
    # Determine OpenMP support and ask user preference if needed
    if openmp == 'disable':
        # User explicitly disabled OpenMP
        use_openmp = False
        if not quiet:
            click.echo("OpenMP support explicitly disabled via command line")
    elif force_openmp_check or not has_saved_preference:
        # Need to check OpenMP support
        openmp_supported, clang_path, compiler_info = check_openmp_support()
        
        if not quiet:
            click.echo(compiler_info)
        
        # Interactive prompt for OpenMP if running in terminal and not quiet
        if is_interactive and openmp == 'auto' and openmp_supported:
            click.echo("\n" + "=" * 80)
            click.echo("OpenMP Support Configuration")
            click.echo("=" * 80)
            click.echo("OpenMP is a parallel programming standard that can speed up computation.")
            click.echo("It's supported on your system, but using it requires additional setup on some platforms.")
            
            # Ask for user preference
            choice = click.prompt(
                "\nWould you like to enable OpenMP support?", 
                type=click.Choice(['yes', 'no', 'auto']), 
                default='auto'
            )
                
            if choice == 'yes':
                use_openmp = True
            elif choice == 'no':
                use_openmp = False
            else:  # auto
                use_openmp = openmp_supported
            
            # Print confirmation
            if use_openmp:
                click.echo("\nOpenMP support is ENABLED.")
            else:
                click.echo("\nOpenMP support is DISABLED.")
        else:
            # Non-interactive - use command line setting
            if openmp == 'enable':
                use_openmp = True
                if not openmp_supported:
                    click.secho("ERROR: OpenMP was explicitly requested but is not supported on your system.", fg="red")
                    click.echo("You might need to install LLVM/Clang with OpenMP support.")
                    click.echo("On macOS: brew install llvm libomp")
                    click.echo("Then add to your environment: export CC=/opt/homebrew/opt/llvm/bin/clang")
                    click.echo("                              export CXX=/opt/homebrew/opt/llvm/bin/clang++")
                    return 1
            else:  # auto
                use_openmp = openmp_supported
        
        # Save preference to config
        config['openmp_supported'] = openmp_supported
        config['openmp_enabled'] = use_openmp
        with open(config_file, 'w') as f:
            json.dump(config, f)
    else:
        # Use saved preference
        use_openmp = config['openmp_enabled']
        if not quiet:
            click.echo(f"Using saved OpenMP preference: {'ENABLED' if use_openmp else 'DISABLED'}")
    
    # Set up OpenMP compile flags if enabled
    if use_openmp:
        if not quiet:
            click.echo("Adding OpenMP flags to compilation")
        
        # Create compile time env if not exists
        if not compile_time_env:
            compile_time_env = {}
        
        # Set the CYTHON_USE_OPENMP flag to enable OpenMP directives
        compile_time_env['CYTHON_USE_OPENMP'] = '1'
        
        # Process directives into a dictionary
        directives_dict = {}
        for name, value in directives:
            directives_dict[name] = value
        
        # Process compile time env into a dictionary
        compile_time_env = {}
        for name, value in compile_time_env_items:
            compile_time_env[name] = value
        
        # Add OpenMP flag to compile time env if enabled
        compile_time_env['CYTHON_USE_OPENMP'] = '1'
        
        # Process options into a dictionary
        options_dict = {}
        for name, value in option_items:
            options_dict[name] = value
        
        # Set up options for cythonize
        options = CythonizeOptions(
            build=build,
            build_inplace=build_inplace,
            force=force,
            quiet=quiet,
            keep_going=keep_going,
            directives=directives_dict,
            compile_time_env=compile_time_env,
            options=options_dict,
            exclude=list(exclude),
            depfile=depfile,
            language=language,
            parallel=parallel,
            cxx_flags=cxx_flags,
            annotate=annotate,
            no_docstrings=no_docstrings,
            lenient=lenient,
            language_level=language_level,
            benchmark=benchmark,
            benchmark_setup=benchmark_setup,
            sources=list(sources),
            openmp=openmp
        )
    
    # Build implies inplace
    if options.build_inplace:
        options.build = True
        
    # Add language_level to options if specified
    if options.language_level is not None:
        options.options['language_level'] = options.language_level

    # Handle CXX_FLAGS
    if options.cxx_flags:
        if not options.compile_time_env:
            options.compile_time_env = {}
        options.compile_time_env['CXX_FLAGS'] = options.cxx_flags
        
    # Environment variables for CXX_FLAGS
    cxx_flags_env = os.environ.get('CXX_FLAGS')
    if cxx_flags_env and not options.cxx_flags:
        if not options.compile_time_env:
            options.compile_time_env = {}
        options.compile_time_env['CXX_FLAGS'] = cxx_flags_env
    
    # Apply lenient options
    if options.lenient:
        # increase Python compatibility by ignoring compile time errors
        Options.error_on_unknown_names = False
        Options.error_on_uninitialized = False

    # Apply annotation settings
    if options.annotate:
        Options.annotate = options.annotate

    # Apply docstring settings
    if options.no_docstrings:
        Options.docstrings = False

    # Gather all source files
    all_paths = []
    for path in options.sources:
        expanded_paths = [os.path.abspath(p) for p in extended_iglob(path)]
        if not expanded_paths:
            click.secho(f"Error: No file found matching '{path}'", fg="red")
            return 1
        all_paths.extend(expanded_paths)
    
    # Show what we're doing unless quiet mode
    if not options.quiet:
        click.secho(f"Cythonizing {len(all_paths)} file(s):", fg="green")
        for path in all_paths:
            click.echo(f"  {os.path.basename(path)}")
        if options.language == "c++":
            click.secho("Using C++ mode", fg="blue")
        if options.cxx_flags:
            click.secho(f"With C++ flags: {options.cxx_flags}", fg="blue")
    
    # Perform cythonization
    try:
        ext_modules_by_basedir = _cython_compile_files(all_paths, options)

        if ext_modules_by_basedir and options.build:
            _build(list(ext_modules_by_basedir.items()), options.parallel)

        if options.benchmark is not None:
            base_dir = import_module = None
            if ext_modules_by_basedir:
                base_dir, first_extensions = next(iter(ext_modules_by_basedir.items()))
                if first_extensions:
                    import_module = first_extensions[0].name

            if base_dir is not None:
                sys.path.insert(0, base_dir)

            benchmark(
                options.benchmark, 
                options.benchmark_setup,
                import_module=import_module,
                directives=options.directives
            )

            if base_dir is not None:
                sys.path.remove(base_dir)
        
        if not options.quiet:
            click.secho(f"Successfully cythonized {len(all_paths)} file(s)", fg="green")
            if options.build:
                click.secho("Built extension modules", fg="green")
        
        return 0
    except Exception as e:
        click.secho(f"Error: {str(e)}", fg="red")
        import traceback
        if not options.quiet:
            traceback.print_exc()
        return 1


if __name__ == '__main__':
    sys.exit(main())
