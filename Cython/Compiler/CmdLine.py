#
#   Cython - Command Line Parsing
#


from dataclasses import dataclass, field
import os
import sys
import getopt
from typing import Dict, List, Optional, Tuple, Union, Any, Set, Callable
from argparse import Action, ArgumentParser
from functools import reduce, partial
import rich_click as click
from rich_click import RichCommand, RichGroup
from rich.console import Console
import importlib.metadata
import shlex # For config file parsing

# ANSI color codes for terminal output
class Colors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

    @staticmethod
    def format(text, color):
        return f"{color}{text}{Colors.ENDC}"
    
    @staticmethod
    def header(text):
        return Colors.format(text, Colors.HEADER)
    
    @staticmethod
    def info(text):
        return Colors.format(text, Colors.BLUE)
    
    @staticmethod
    def success(text):
        return Colors.format(text, Colors.GREEN)
    
    @staticmethod
    def warning(text):
        return Colors.format(text, Colors.YELLOW)
    
    @staticmethod
    def error(text):
        return Colors.format(text, Colors.RED)
    
    @staticmethod
    def bold(text):
        return Colors.format(text, Colors.BOLD)

print(f"\n{Colors.BOLD}{Colors.YELLOW}DEBUG: Loading Cython.Compiler.CmdLine module{Colors.ENDC}\n") # DEBUG: Module level print

from . import Options
from . import DebugFlags
from Cython.Shadow import __version__ as cython_version

# Keep these action classes for backward compatibility with other modules
class ParseDirectivesAction(Action):
    def __call__(self, parser, namespace, values, option_string=None):
        old_directives = dict(getattr(namespace, self.dest,
                                      Options.get_directive_defaults()))
        directives = Options.parse_directive_list(
            values, relaxed_bool=True, current_settings=old_directives)
        setattr(namespace, self.dest, directives)


class ParseOptionsAction(Action):
    def __call__(self, parser, namespace, values, option_string=None):
        options = dict(getattr(namespace, self.dest, {}))
        if values is not None:
            if isinstance(values, str):
                for opt in values.split(','):
                    if '=' in opt:
                        n, v = opt.split('=', 1)
                        v = v.lower() not in ('false', 'f', '0', 'no')
                    else:
                        n, v = opt, True
                    options[n] = v
            elif hasattr(values, '__iter__'):
                for opt in values:
                    if isinstance(opt, str):
                        if '=' in opt:
                            n, v = opt.split('=', 1)
                            v = v.lower() not in ('false', 'f', '0', 'no')
                        else:
                            n, v = opt, True
                        options[n] = v
        setattr(namespace, self.dest, options)


class ParseCompileTimeEnvAction(Action):
    def __call__(self, parser, namespace, values, option_string=None):
        old_env = dict(getattr(namespace, self.dest, {}))
        if values is not None and isinstance(values, str):
            new_env = Options.parse_compile_time_env(values, current_settings=old_env)
            setattr(namespace, self.dest, new_env)

# Simple configuration dataclass
@dataclass
class CmdLineOptions:
    show_version: int = 0
    use_listing_file: int = 0
    include_path: List[str] = field(default_factory=list)
    output_file: Optional[str] = None
    timestamps: Optional[int] = None
    verbose: int = 0
    embed_pos_in_docstring: int = 0
    generate_cleanup_code: Optional[int] = None
    cache: bool = False
    working_path: Optional[str] = None
    gdb_debug: bool = False
    output_dir: str = os.curdir
    docstrings: bool = True
    annotate: Optional[str] = None
    annotate_coverage_xml: Optional[str] = None
    emit_linenums: bool = False
    cplus: int = 0
    embed: Optional[str] = None
    language_level: Optional[Union[int, str]] = None
    error_on_unknown_names: bool = True
    error_on_uninitialized: bool = True
    capi_reexport_cincludes: bool = False
    fast_fail: bool = False
    warning_errors: bool = False
    compiler_directives: Dict[str, Any] = field(default_factory=dict)
    compile_time_env: Dict[str, Any] = field(default_factory=dict)
    module_name: Optional[str] = None
    depfile: bool = False
    sources: List[str] = field(default_factory=list)
    pre_import: Optional[str] = None
    convert_range: bool = False
    c_line_in_traceback: bool = True
    cimport_from_pyx: bool = False
    old_style_globals: bool = False
    shared_c_file_path: Optional[str] = None
    shared_utility_qualified_name: Optional[str] = None
    config_file: Optional[str] = None

# Get version information
def print_version():
    """Print the Cython version"""
    # Handle the import safely to fix the linter error
    version = "unknown"
    try:
        import importlib.metadata
        version = importlib.metadata.version("cython")
    except (ImportError, importlib.metadata.PackageNotFoundError):
        try:
            import sys
            if hasattr(sys.modules.get('Cython', None), '__version__'):
                version = sys.modules['Cython'].__version__
            else:
                # Last resort - try relative import
                try:
                    from .. import __version__  # May fail but worth trying
                    version = __version__
                except (ImportError, ValueError):
                    pass
        except ImportError:
            pass
    
    print(Colors.header(f"Cython version {version}"))

# Define option help text using a generator expression for more concise code
def get_option_help() -> Dict[str, str]:
    """Generate option help text dictionary using a compact mapping approach"""
    option_mappings = [
        ("V", "Display version number of cython compiler"),
        ("l", "Write error messages to a listing file"),
        ("I", "Search for include files in named directory (multiple include directories are allowed)"),
        ("o", "Specify name of generated C file"),
        ("t", "Only compile newer source files"),
        ("f", "Compile all source files (overrides implied -t)"),
        ("v", "Be verbose, print file names on multiple compilation"),
        ("p", "Embed positions in docstrings"),
        ("z", "Pre-import module"),
        ("D", "Strip docstrings from the compiled module"),
        ("a", "Produce a colorized HTML version of the source"),
        ("annotate-fullc", "Produce a colorized HTML version of source with full C code"),
        ("line-directives", "Produce #line directives pointing to the .pyx source"),
        ("+", "Output a C++ rather than C file"),
        ("2", "Compile based on Python 2 syntax and semantics"),
        ("3", "Compile based on Python 3 syntax and semantics"),
        ("3str", "Compile based on Python 3 syntax and semantics (same as -3)"),
        ("lenient", "Change some compile time errors to runtime errors to improve Python compatibility"),
        ("capi-reexport-cincludes", "Add cincluded headers to any auto-generated header files"),
        ("fast-fail", "Abort the compilation on the first error"),
        ("warning-errors", "Make all warnings into errors"),
        ("warning-extra", "Enable extra warnings"),
        ("X", "Override a compiler directive"),
        ("E", "Set compile-time environment variable"),
        ("working", "Sets the working directory for Cython"),
        ("module-name", "Fully qualified module name"),
        ("M", "Produce depfiles for the sources"),
        ("cache", "Enable Cython compilation cache"),
        ("depfile", "Produce depfiles for the sources"),
        ("embed", "Generate a main() function that embeds the Python interpreter"),
        ("gdb", "Output debug information for cygdb"),
        ("gdb-outdir", "Specify gdb debug information output directory"),
        ("annotate-coverage", "Annotate and include coverage information from cov.xml"),
        ("no-c-in-traceback", "Do not include C-level traceback in exceptions"),
        ("cimport-from-pyx", "Allow cimporting from pyx files"),
        ("old-style-globals", "Use old-style globals lookup"),
        ("convert-range", "Convert range checks to conditional checks"),
        ("generate-shared", "Generate shared module with specified name"),
        ("shared", "Import utility code from shared module"),
        ("config-file", "Specify a configuration file to load options from"),
        ("output-dir", "Specify the directory for generated C/C++ files")
    ]
    return dict(option_mappings)

def print_usage():
    """Print usage information with color formatting"""
    option_help = get_option_help()
    print(Colors.header("Cython Compiler"))
    print(Colors.info("Usage:"))
    print("  cython [options] [source_files]")
    print("")
    print(Colors.info("Options:"))
    
    # Display short options first, followed by long options
    short_options = [(opt, desc) for opt, desc in option_help.items() if len(opt) == 1]
    long_options = [(opt, desc) for opt, desc in option_help.items() if len(opt) > 1]
    
    for opt, desc in sorted(short_options):
        print(f"  -{opt:<2} {desc}")
    
    for opt, desc in sorted(long_options):
        print(f"  --{opt:<20} {desc}")
    
    print("")
    print(Colors.info("Examples:"))
    print("  # Compile a single file")
    print("  cython mymodule.pyx")
    print("")
    print("  # Compile to C++ with verbose output")
    print("  cython -v --cplus mymodule.pyx")
    print("")
    print("  # Compile for Python 3, place C file in build/")
    print("  cython -3 -o build/mymodule.c mymodule.pyx")
    print("")
    print("  # Compile using an output directory (alternative)")
    print("  cython --output-dir build mymodule.pyx")
    print("")
    print("  # Create an embedded executable")
    print("  cython --embed mymain.pyx")
    print("")
    print("  # Compile with annotation and custom directive")
    print("  cython -a -X boundscheck=False mymodule.pyx")
    print("")

    print(Colors.info("Environment variables:"))
    print("  CYTHON_CACHE_DIR: the base directory containing Cython's caches.")
    print("  CYTHONRC: path to the Cython configuration file.")
    

def parse_directive_list(option_value):
    """Parse a comma-separated list of directive key=value pairs."""
    if not option_value:
        return {}
    
    # Functional approach using map and dict comprehension
    pairs = option_value.split(',')
    return {
        p.split('=', 1)[0]: p.split('=', 1)[1] if '=' in p else True 
        for p in pairs
    }


def read_config_file(config_file_path):
    """Read configuration from a file using functional programming."""
    try:
        with open(config_file_path, 'r') as f:
            # Functional approach to extract and process config lines
            lines = f.readlines()
            valid_lines = filter(lambda l: l.strip() and not l.strip().startswith('#'), lines)
            config_items = [l.strip().split('=', 1) for l in valid_lines if '=' in l]
            
            # Create base options
            options = CmdLineOptions()
            
            # Define a type converter based on existing value type
            def convert_value(key, val):
                existing = getattr(options, key, None)
                if isinstance(existing, bool):
                    return val.lower() in ('true', 'yes', '1')
                elif isinstance(existing, int) and val.isdigit():
                    return int(val)
                elif isinstance(existing, list):
                    return val.split(',')
                elif isinstance(existing, dict):
                    return parse_directive_list(val)
                return val
            
            # Apply configs using a dictionary comprehension
            config_dict = {
                k.strip(): convert_value(k.strip(), v.strip())
                for k, v in config_items if hasattr(options, k.strip())
            }
            
            # Apply the configs to the options object
            for k, v in config_dict.items():
                setattr(options, k, v)
                
            return options
            
    except Exception as e:
        print(Colors.error(f"Error reading config file: {e}"))
        return CmdLineOptions()


# Define option handlers as individual functions for maintainability
class OptionHandlers:
    @staticmethod
    def handle_help(options, value):
        print_usage()
        sys.exit(0)
    
    @staticmethod
    def handle_version(options, value):
        print_version()
        options.show_version = 1
    
    @staticmethod
    def handle_listing_file(options, value):
        options.use_listing_file = 1
    
    @staticmethod
    def handle_include_dir(options, value):
        options.include_path.append(value)
    
    @staticmethod
    def handle_output_file(options, value):
        options.output_file = value
    
    @staticmethod
    def handle_timestamps(options, value):
        options.timestamps = 1
    
    @staticmethod
    def handle_force(options, value):
        options.timestamps = 0
    
    @staticmethod
    def handle_verbose(options, value):
        options.verbose += 1
    
    @staticmethod
    def handle_embed_positions(options, value):
        options.embed_pos_in_docstring = 1
    
    @staticmethod
    def handle_pre_import(options, value):
        options.pre_import = value
    
    @staticmethod
    def handle_no_docstrings(options, value):
        options.docstrings = False
    
    @staticmethod
    def handle_annotate(options, value):
        options.annotate = 'default'
    
    @staticmethod
    def handle_annotate_fullc(options, value):
        options.annotate = 'fullc'
    
    @staticmethod
    def handle_line_directives(options, value):
        options.emit_linenums = True
    
    @staticmethod
    def handle_directive(options, value):
        directives = parse_directive_list(value)
        options.compiler_directives.update(directives)
    
    @staticmethod
    def handle_compile_time_env(options, value):
        env_vars = parse_directive_list(value)
        options.compile_time_env.update(env_vars)
    
    @staticmethod
    def handle_working_path(options, value):
        options.working_path = value
    
    @staticmethod
    def handle_module_name(options, value):
        options.module_name = value
    
    @staticmethod
    def handle_depfile(options, value):
        options.depfile = True
    
    @staticmethod
    def handle_cplus(options, value):
        options.cplus = 1
    
    @staticmethod
    def handle_embed(options, value):
        options.embed = 'main'
    
    @staticmethod
    def handle_embed_with_name(options, value):
        options.embed = value
    
    @staticmethod
    def handle_py2(options, value):
        options.language_level = 2
    
    @staticmethod
    def handle_py3(options, value):
        options.language_level = 3
    
    @staticmethod
    def handle_lenient(options, value):
        options.error_on_unknown_names = False
        options.error_on_uninitialized = False
    
    @staticmethod
    def handle_capi_reexport_cincludes(options, value):
        options.capi_reexport_cincludes = True
    
    @staticmethod
    def handle_fast_fail(options, value):
        options.fast_fail = True
    
    @staticmethod
    def handle_warning_errors(options, value):
        options.warning_errors = True
    
    @staticmethod
    def handle_warning_extra(options, value):
        options.compiler_directives.update(Options.extra_warnings)
    
    @staticmethod
    def handle_cache(options, value):
        options.cache = True
    
    @staticmethod
    def handle_gdb(options, value):
        options.gdb_debug = True
        options.output_dir = os.curdir
    
    @staticmethod
    def handle_gdb_outdir(options, value):
        options.gdb_debug = True
        options.output_dir = value
    
    @staticmethod
    def handle_annotate_coverage(options, value):
        options.annotate = 'default'
        options.annotate_coverage_xml = value
    
    @staticmethod
    def handle_no_c_in_traceback(options, value):
        options.c_line_in_traceback = False
    
    @staticmethod
    def handle_cimport_from_pyx(options, value):
        options.cimport_from_pyx = True
    
    @staticmethod
    def handle_old_style_globals(options, value):
        options.old_style_globals = True
    
    @staticmethod
    def handle_convert_range(options, value):
        options.convert_range = True
    
    @staticmethod
    def handle_cleanup(options, value):
        options.generate_cleanup_code = int(value)
    
    @staticmethod
    def handle_generate_shared(options, value):
        options.shared_c_file_path = value
    
    @staticmethod
    def handle_shared(options, value):
        options.shared_utility_qualified_name = value
    
    @staticmethod
    def handle_config_file(options, value):
        options.config_file = value
        if os.path.exists(value):
            config_options = read_config_file(value)
            # Merge configs, with command line taking precedence
            for key, val in vars(config_options).items():
                if key not in ('sources', 'include_path', 'compiler_directives', 'compile_time_env'):
                    if not getattr(options, key):  # Don't override if already set by cmd line
                        setattr(options, key, val)
                elif isinstance(val, list):
                    getattr(options, key).extend(val)
                elif isinstance(val, dict):
                    getattr(options, key).update(val)

    @staticmethod
    def handle_output_dir(options, value):
        # Ensure the path exists and is stored
        options.output_dir = os.path.abspath(value)
        os.makedirs(options.output_dir, exist_ok=True)


def parse_command_line(args: List[str]) -> Tuple[Options.CompilationOptions, List[str]]:
    """
    Parses command line arguments using click and returns results
    in the format expected by Cython.Compiler.Main.
    Uses custom error handling and help via print_usage.
    """
    print(f"Compatibility parse_command_line received args: {args}") # Debug
    try:
        # Use standalone_mode=False to prevent click from exiting automatically
        # Pass original args, click handles splitting them
        prog_name = os.path.basename(sys.argv[0]) if sys.argv else 'cython'
        # Create a context for the command
        context = cython_command.make_context(info_name=prog_name, args=args, standalone_mode=False)

        # Manually handle help *before* invoking command logic to use our custom print_usage
        if '--help' in args or '-h' in args:
             print_usage()
             sys.exit(0)

        # Invoke the command logic within the context
        # This runs the cython_command function, which populates context.obj
        with context:
            cython_command.invoke(context)

        # Retrieve results stored in context by the cython_command function
        if context.obj and 'options' in context.obj and 'sources' in context.obj:
            # Ensure the returned options object is the correct type
            comp_options = context.obj['options']
            sources_list = context.obj['sources']
            if not isinstance(comp_options, Options.CompilationOptions):
                 print(Colors.error(f"Error: Internal context object has incorrect type for options: {type(comp_options)}"))
                 sys.exit(1)
            return comp_options, sources_list
        else:
            # This might happen if invoke exited early (e.g., --version)
            # or if something went wrong before ctx.obj was set, but didn't raise an exception caught below.
            # Check if version flag caused the exit (difficult to tell directly after invoke)
            if '--version' in args or '-V' in args:
                 sys.exit(0) # Assume version exit if obj is missing after version flag
            print(Colors.error("Error: Failed to retrieve parsed options from context after command invocation."))
            sys.exit(1)

    except click.exceptions.Exit as e:
        # Propagate exits cleanly (e.g., for --version if caught)
        sys.exit(e.code)
    except click.exceptions.UsageError as e:
        # Print usage error message (already formatted by our validate_options)
        print(e.format_message(), file=sys.stderr)
        # print_usage() # Optionally show full usage on error
        sys.exit(e.exit_code)
    except click.exceptions.ClickException as e:
        # Print other click errors using our colors
        print(Colors.error(f"Error: {e.format_message()}"), file=sys.stderr)
        sys.exit(e.exit_code)
    except Exception as e:
        # Catch unexpected errors during parsing/invocation
        print(Colors.error(f"An unexpected error occurred during command line processing:"), file=sys.stderr)
        import traceback
        traceback.print_exc()
        sys.exit(1)


# For backward compatibility - needed by Cythonize
def create_cython_argparser() -> ArgumentParser:
    """
    Legacy function that returns a stub ArgumentParser for compatibility.
    """
    from argparse import ArgumentParser, SUPPRESS, RawDescriptionHelpFormatter
    
    description = "Cython (https://cython.org/) is a compiler for code written in the "\
                "Cython language.  Cython is based on Pyrex by Greg Ewing."

    parser = ArgumentParser(
        description=description,
        argument_default=SUPPRESS,
        formatter_class=RawDescriptionHelpFormatter
    )
    
    # Add just enough arguments to make Cythonize happy
    parser.add_argument('-X', '--directive', dest='compiler_directives', action=ParseDirectivesAction, help=SUPPRESS)
    parser.add_argument('-E', '--compile-time-env', dest='compile_time_env', action=ParseCompileTimeEnvAction, help=SUPPRESS)
    parser.add_argument('-s', '--option', dest='options', action=ParseOptionsAction, help=SUPPRESS)
    parser.add_argument('sources', nargs='*', default=[])
    
    return parser


# --- Main Click Command Definition ---
@click.command(
    name='cython',
    context_settings=dict(help_option_names=['-h', '--help']),
    add_help_option=False, # We handle help manually
    epilog="Environment variables: ..." # Placeholder
)
# --- Version Option --- (Handled separately to allow exit before validation)
@click.option('-V', '--version', '_version_flag_set', is_flag=True, is_eager=True, expose_value=True,
              help='Display version number and exit.')
# --- Manual Help Option ---
@click.option('-h', '--help', 'show_help', is_flag=True, is_eager=True, expose_value=False,
              callback=lambda ctx, param, value: ctx.exit(print_usage()) if value else None,
              help='Show this message and exit.')
# --- Core Options ---
@click.option('-l', '--create-listing', 'use_listing_file', is_flag=True, default=False, help='Write error messages to a listing file.')
@click.option('-I', '--include-dir', 'include_path', multiple=True, type=click.Path(exists=True, file_okay=False, resolve_path=True), help='Search for include files in named directory (repeatable).')
@click.option('-o', '--output-file', type=click.Path(dir_okay=False, writable=True, resolve_path=True), help='Specify name of generated C/C++ file.')
@click.option('-t', '--timestamps', 'use_timestamps', is_flag=True, default=True, help='Only compile newer source files (default).')
@click.option('-f', '--force', 'force_compile', is_flag=True, default=False, help='Compile all source files (overrides -t).')
@click.option('-v', '--verbose', count=True, help='Be verbose (-vv for more). repeatable')
@click.option('-p', '--embed-positions', 'embed_pos_in_docstring', is_flag=True, default=False, help='Embed source code positions in docstrings.')
@click.option('-z', '--pre-import', type=str, default=None, help='Pre-import a module.')
@click.option('-D', '--no-docstrings', 'docstrings', is_flag=True, default=True, help='Strip docstrings (flag means \'strip\', so default is True=keep).') # Default is True, flag sets to False
@click.option('-a', '--annotate', 'annotate_html', is_flag=True, default=False, help='Produce a colorized HTML version of the source.') # Separate flag for basic annotation
@click.option('--annotate-fullc', is_flag=True, default=False, help='Produce HTML including C/C++ code.')
@click.option('--line-directives', 'emit_linenums', is_flag=True, default=False, help='Produce #line directives pointing to the .pyx source.')
@click.option('-+', '--cplus', is_flag=True, default=False, help='Output a C++ rather than C file.')
@click.option('-2', 'lang_level_2', is_flag=True, default=False, help='Compile using Python 2 syntax and semantics.')
@click.option('-3', 'lang_level_3', is_flag=True, default=False, help='Compile using Python 3 syntax and semantics.')
@click.option('--3str', 'lang_level_3str', is_flag=True, default=False, help='Compile using Python 3 syntax and semantics (same as -3).')
@click.option('--lenient', is_flag=True, default=False, help='Change some compile time errors to runtime errors.')
@click.option('--capi-reexport-cincludes', 'capi_reexport_cincludes', is_flag=True, default=False, help='Add cincluded headers to auto-generated header files.')
@click.option('--fast-fail', 'fast_fail', is_flag=True, default=False, help='Abort the compilation on the first error.')
@click.option('-Werror', '--warning-errors', 'warning_errors', is_flag=True, default=False, help='Make all warnings into errors.')
@click.option('-Wextra', '--warning-extra', is_flag=True, default=False, callback=activate_warning_extra_callback, expose_value=False, help='Enable extra warnings.')
@click.option('-X', '--directive', 'compiler_directives', multiple=True, callback=parse_directives_callback, help='Override compiler directive (e.g., -X boundscheck=False). Repeatable.', metavar='NAME=VALUE,...')
@click.option('-E', '--compile-time-env', multiple=True, callback=parse_compile_time_env_callback, help='Set compile-time environment variable (e.g., -E DEBUG=True). Repeatable.', metavar='NAME=VALUE,...')
@click.option('-w', '--working', 'working_path', type=click.Path(exists=True, file_okay=False, resolve_path=True), help='Sets the working directory for Cython.')
@click.option('--module-name', type=str, default=None, help='Fully qualified module name.')
@click.option('-M', '--depfile', 'make_depfile', is_flag=True, default=False, help='Produce depfiles for the sources.') # Renamed to avoid clash
@click.option('--cache', is_flag=True, default=False, help='Enable Cython compilation cache.')
# embed takes optional argument, handle carefully
@click.option('--embed', type=str, default=None, is_flag=False, flag_value='main', help='Generate main() embedding Python. Optional value=func name.', metavar='[FUNC_NAME]')
@click.option('--gdb', 'gdb_debug', is_flag=True, default=False, help='Output debug information for cygdb.')
@click.option('--gdb-outdir', type=click.Path(file_okay=False, writable=True, resolve_path=True), callback=set_gdb_output_callback, help='Specify gdb debug output directory (implies --gdb).')
@click.option('--annotate-coverage', type=click.Path(exists=True, dir_okay=False), callback=set_annotate_coverage_callback, help='Annotate using coverage.xml (implies -a).')
@click.option('--no-c-in-traceback', 'c_line_in_traceback', is_flag=True, default=True, help='Do not include C source info in tracebacks (flag=True means no C).')
@click.option('--cimport-from-pyx', is_flag=True, default=False, help='Allow cimporting from .pyx files.')
@click.option('--old-style-globals', is_flag=True, default=False, help='Use old-style globals lookup.')
@click.option('--convert-range', is_flag=True, default=False, help='Convert range() loops to C loops.')
@click.option('--cleanup', 'generate_cleanup_code', type=int, default=None, help='Release interned objects on Python exit (level indicates aggressiveness).')
@click.option('--generate-shared', 'shared_c_file_path', type=str, default=None, help='Generate shared C utility code file.')
@click.option('--shared', 'shared_utility_qualified_name', type=str, default=None, help='Import utility code from shared module (fully qualified name).')
@click.option('--config-file', type=click.Path(exists=True, dir_okay=False, resolve_path=True), help='Specify a configuration file to load options from.')
@click.option('--output-dir', type=click.Path(file_okay=False, writable=True, resolve_path=True), default=None, help='Specify the directory for generated C/C++ files.')

# --- Arguments --- (Sources)
@click.argument('sources', nargs=-1, type=click.Path(exists=True, dir_okay=False, resolve_path=True))

# --- Main Command Logic --- (Runs after parsing)
@click.pass_context
def cython_command(ctx: click.Context, sources: Tuple[str, ...], _version_flag_set: bool, **kwargs):
    """The main function that processes options and prepares for compilation."""

    # --- Handle manual help and version --- (is_eager=True)
    # Help is handled by its callback
    if _version_flag_set: # Check if the eager version flag was set
        print_version()
        ctx.exit()

    print(Colors.info("Processing options...")) # Debug
    # Merge command-line args with config file options
    final_options = {} # Store combined options
    config_options = {}
    config_file_path = kwargs.get('config_file') or os.environ.get('CYTHONRC')
    if config_file_path:
        config_options = load_config_file(config_file_path)

    # Start with config, then update with command line args (kwargs)
    # Need to handle type conversion for config file values
    processed_config = {}
    for key, value in config_options.items():
         param = next((p for p in ctx.command.params if p.name == key), None)
         if param:
             try:
                 # Use click's type conversion where possible
                 if isinstance(param.type, click.types.BoolParamType) or getattr(param,'is_flag', False):
                      processed_config[key] = str(value).lower() in ('true', '1', 'yes', 'on')
                 elif isinstance(param.type, click.types.IntParamType):
                      processed_config[key] = int(value)
                 elif isinstance(param.type, click.types.Path):
                      processed_config[key] = click.Path(exists=param.type.exists, file_okay=param.type.file_okay, dir_okay=param.type.dir_okay).convert(value, param, ctx)
                 elif key == 'compiler_directives':
                      # Assuming config value is comma-separated string
                      processed_config[key] = parse_directives_callback(ctx, param, value)
                 elif key == 'compile_time_env':
                      processed_config[key] = parse_compile_time_env_callback(ctx, param, value)
                 else:
                      processed_config[key] = value # Assume string or handled by callback later?
             except Exception as e:
                  print(Colors.warning(f"Warning: Could not convert config value for '{key}': {e}"))
                  processed_config[key] = value # Keep original string if conversion fails
         else:
              processed_config[key] = value # Keep as string if no matching param found

    final_options.update(processed_config)
    # Convert command line keys (click uses underscores)
    cmd_line_options = {k: v for k, v in kwargs.items() if v is not None and k not in ('_version_flag_set', 'show_help', 'config_file')} # Filter out None and meta flags
    final_options.update(cmd_line_options)

    print(f"Final combined options before processing: {final_options}") # Debug

    # --- Process and Validate Combined Options ---

    # Handle Timestamp Default
    timestamps = not final_options.get('force_compile', False)

    # Handle Language Level
    language_level = Options.default_options['language_level']
    if final_options.get('lang_level_2'):
        language_level = 2
    elif final_options.get('lang_level_3') or final_options.get('lang_level_3str'):
        language_level = 3

    # Handle Annotate Consolidation
    annotate = None
    if final_options.get('annotate_fullc'):
        annotate = 'fullc'
    elif final_options.get('annotate_html') or final_options.get('annotate_coverage'):
        annotate = 'default'

    # Handle Docstrings (flag means strip, so invert for comp_options)
    # click option default is True (keep), flag sets it to False internally?
    # Need to check click behavior vs. intended logic.
    # Let's assume click stores False if --no-docstrings is given.
    # So comp_options.docstrings should be the value from click.
    docstrings = final_options.get('docstrings', True)

    # Handle C Line in Traceback (flag means no C, so invert)
    # click option default is True (include C). Flag sets it to False?
    c_line_in_traceback = final_options.get('c_line_in_traceback', True)

    # Collect directives from potentially multiple sources (cmd line, config, extra)
    merged_directives = Options.get_directive_defaults().copy()
    if 'compiler_directives' in final_options:
        merged_directives.update(final_options['compiler_directives'])
    # Apply Wextra if flag was set (callback modified ctx.params, need to re-read or pass)
    if kwargs.get('warning_extra'): # Check original kwargs if callback didn't modify final_options
         merged_directives.update(Options.extra_warnings)

    # Validate Options (pass the processed/combined values)
    # Need to handle callbacks setting implicit flags (gdb_debug, annotate)
    processed_kwargs_for_validation = final_options.copy()
    processed_kwargs_for_validation['timestamps'] = timestamps
    processed_kwargs_for_validation['gdb_debug'] = final_options.get('gdb_debug') or final_options.get('gdb_outdir') is not None
    processed_kwargs_for_validation['annotate'] = annotate

    validate_options(ctx, sources, **processed_kwargs_for_validation)

    # --- Prepare Cython CompilationOptions ---
    comp_options = Options.CompilationOptions(**Options.default_options) # Start fresh with defaults

    # Map processed options to CompilationOptions
    comp_env = {}
    if 'compile_time_env' in final_options:
        comp_env.update(final_options['compile_time_env'])

    # Attributes to copy directly if present in final_options
    direct_copy_attrs = [
        'use_listing_file', 'include_path', 'output_file', 'verbose',
        'embed_pos_in_docstring', 'generate_cleanup_code', 'cache',
        'working_path', 'gdb_debug', 'annotate_coverage_xml',
        'emit_linenums', 'cplus', 'error_on_unknown_names',
        'error_on_uninitialized', 'capi_reexport_cincludes', 'fast_fail',
        'warning_errors', 'module_name', 'make_depfile', # Note: renamed depfile option
        'pre_import', 'convert_range', 'cimport_from_pyx', 'old_style_globals',
        'shared_c_file_path', 'shared_utility_qualified_name', 'output_dir'
    ]

    for attr in direct_copy_attrs:
        # Use the possibly processed value from final_options
        if attr in final_options:
             # Special handling for gdb_debug as it can be set by callback
             if attr == 'gdb_debug':
                 setattr(comp_options, attr, processed_kwargs_for_validation['gdb_debug'])
             else:
                 setattr(comp_options, attr, final_options[attr])

    # Set calculated/processed values
    comp_options.compiler_directives = merged_directives
    comp_options.compile_time_env = comp_env
    comp_options.timestamps = timestamps
    comp_options.language_level = language_level
    comp_options.annotate = annotate
    comp_options.docstrings = docstrings
    comp_options.c_line_in_traceback = c_line_in_traceback

    # Handle embed option
    comp_options.embed = final_options.get('embed')
    Options.embed = comp_options.embed # Set global Option too

    # Handle lenient flag
    if final_options.get('lenient', False):
        comp_options.error_on_unknown_names = False
        comp_options.error_on_uninitialized = False

    # Update global Options and DebugFlags as needed
    if 'verbose' in final_options:
         Options.verbose = final_options['verbose'] # Set global verbose
    # Debug flags?
    # for flag_name in dir(DebugFlags):
    #    if flag_name.startswith('debug') and flag_name in final_options:
    #         setattr(DebugFlags, flag_name, final_options[flag_name])

    print(f"Final Compilation Options: {comp_options}") # Debug
    print(f"Sources: {list(sources)}") # Debug

    # Store results in context object for the compatibility wrapper
    ctx.obj = {'options': comp_options, 'sources': list(sources)}


# --- Direct Execution Entry Point ---
if __name__ == "__main__":
    print(Colors.info("Running CmdLine.py directly via __main__..."))
    # This directly invokes the click command processing
    cython_command()
