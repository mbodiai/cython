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
    """Parse command-line arguments using functional programming."""
    print(f"Received raw args: {args}") # DEBUG: Print args as early as possible
    # Start with clean options
    options = CmdLineOptions()
    
    # Check for config file in environment
    config_file = os.environ.get('CYTHONRC')
    if config_file and os.path.exists(config_file):
        options = read_config_file(config_file)
    
    # Define getopt options
    short_opts = "VlI:o:tfvpz:DaXE:hM+23"
    long_opts = [
        "version", "create-listing", "include-dir=", "output-file=", "timestamps", 
        "force", "verbose", "embed-positions", "pre-import=", "no-docstrings",
        "annotate", "annotate-fullc", "directive=", "compile-time-env=",
        "working=", "module-name=", "depfile", "cplus", "help",
        "embed", "embed=", "lenient", "capi-reexport-cincludes", "fast-fail",
        "warning-errors", "warning-extra", "line-directives", "cache",
        "gdb", "gdb-outdir=", "annotate-coverage=", "no-c-in-traceback",
        "cimport-from-pyx", "old-style-globals", "convert-range", "cleanup=",
        "generate-shared=", "shared=", "3str", "config-file=", "output-dir="
    ]
    
    try:
        opts, args = getopt.getopt(args, short_opts, long_opts)
        print(f"Parsed options: {opts}")
        print(f"Remaining args: {args}")
    except getopt.GetoptError as e:
        print(Colors.error(f"Error: {e}"))
        print_usage()
        sys.exit(2)
    
    # Process special --embed= options first with a filter
    embed_opts = list(filter(lambda x: x[0].startswith('--embed='), opts))
    if embed_opts:
        # Extract the name from the first matching option
        options.embed = embed_opts[0][0][8:]  # Remove '--embed=' prefix
    
    # Strip optional -- and - prefixes from option names for uniform handling
    def strip_prefix(opt):
        return opt[2:] if opt.startswith('--') else (opt[1:] if opt.startswith('-') else opt)
    
    # Map options to handler functions
    option_map = {
        # Short options
        'h': lambda o, v: (print_usage(), sys.exit(0)),
        'V': lambda o, v: (print_version(), setattr(o, 'show_version', 1), o)[2],
        'l': lambda o, v: setattr(o, 'use_listing_file', 1) or o,
        'I': lambda o, v: o.include_path.append(v) or o,
        'o': lambda o, v: setattr(o, 'output_file', v) or o,
        't': lambda o, v: setattr(o, 'timestamps', 1) or o,
        'f': lambda o, v: setattr(o, 'timestamps', 0) or o,
        'v': lambda o, v: setattr(o, 'verbose', o.verbose + 1) or o,
        'p': lambda o, v: setattr(o, 'embed_pos_in_docstring', 1) or o,
        'z': lambda o, v: setattr(o, 'pre_import', v) or o,
        'D': lambda o, v: setattr(o, 'docstrings', False) or o,
        'a': lambda o, v: setattr(o, 'annotate', 'default') or o,
        'X': lambda o, v: o.compiler_directives.update(parse_directive_list(v)) or o,
        'E': lambda o, v: o.compile_time_env.update(parse_directive_list(v)) or o,
        'M': lambda o, v: setattr(o, 'depfile', True) or o,
        '+': lambda o, v: setattr(o, 'cplus', 1) or o,
        '2': lambda o, v: setattr(o, 'language_level', 2) or o,
        '3': lambda o, v: setattr(o, 'language_level', 3) or o,
        
        # Long options - using the stripped names
        'help': lambda o, v: (print_usage(), sys.exit(0)),
        'version': lambda o, v: (print_version(), setattr(o, 'show_version', 1), o)[2],
        'create-listing': lambda o, v: setattr(o, 'use_listing_file', 1) or o,
        'include-dir': lambda o, v: o.include_path.append(v) or o,
        'output-file': lambda o, v: setattr(o, 'output_file', v) or o,
        'timestamps': lambda o, v: setattr(o, 'timestamps', 1) or o,
        'force': lambda o, v: setattr(o, 'timestamps', 0) or o,
        'verbose': lambda o, v: setattr(o, 'verbose', o.verbose + 1) or o,
        'embed-positions': lambda o, v: setattr(o, 'embed_pos_in_docstring', 1) or o,
        'pre-import': lambda o, v: setattr(o, 'pre_import', v) or o,
        'no-docstrings': lambda o, v: setattr(o, 'docstrings', False) or o,
        'annotate': lambda o, v: setattr(o, 'annotate', 'default') or o,
        'annotate-fullc': lambda o, v: setattr(o, 'annotate', 'fullc') or o,
        'line-directives': lambda o, v: setattr(o, 'emit_linenums', True) or o,
        'directive': lambda o, v: o.compiler_directives.update(parse_directive_list(v)) or o,
        'compile-time-env': lambda o, v: o.compile_time_env.update(parse_directive_list(v)) or o,
        'working': lambda o, v: setattr(o, 'working_path', v) or o,
        'module-name': lambda o, v: setattr(o, 'module_name', v) or o,
        'depfile': lambda o, v: setattr(o, 'depfile', True) or o,
        'cplus': lambda o, v: setattr(o, 'cplus', 1) or o,
        'embed': lambda o, v: setattr(o, 'embed', 'main') or o,
        '3str': lambda o, v: setattr(o, 'language_level', 3) or o,
        'lenient': lambda o, v: (setattr(o, 'error_on_unknown_names', False), setattr(o, 'error_on_uninitialized', False), o)[2],
        'capi-reexport-cincludes': lambda o, v: setattr(o, 'capi_reexport_cincludes', True) or o,
        'fast-fail': lambda o, v: setattr(o, 'fast_fail', True) or o,
        'warning-errors': lambda o, v: setattr(o, 'warning_errors', True) or o,
        'warning-extra': lambda o, v: o.compiler_directives.update(Options.extra_warnings) or o,
        'cache': lambda o, v: setattr(o, 'cache', True) or o,
        'gdb': lambda o, v: (setattr(o, 'gdb_debug', True), setattr(o, 'output_dir', os.curdir), o)[2],
        'gdb-outdir': lambda o, v: (setattr(o, 'gdb_debug', True), setattr(o, 'output_dir', v), o)[2],
        'annotate-coverage': lambda o, v: (setattr(o, 'annotate', 'default'), setattr(o, 'annotate_coverage_xml', v), o)[2],
        'no-c-in-traceback': lambda o, v: setattr(o, 'c_line_in_traceback', False) or o,
        'cimport-from-pyx': lambda o, v: setattr(o, 'cimport_from_pyx', True) or o,
        'old-style-globals': lambda o, v: setattr(o, 'old_style_globals', True) or o,
        'convert-range': lambda o, v: setattr(o, 'convert_range', True) or o,
        'cleanup': lambda o, v: setattr(o, 'generate_cleanup_code', int(v)) or o,
        'generate-shared': lambda o, v: setattr(o, 'shared_c_file_path', v) or o,
        'shared': lambda o, v: setattr(o, 'shared_utility_qualified_name', v) or o,
        'config-file': lambda o, v: process_config_file(o, v),
        'output-dir': lambda o, v: setattr(o, 'output_dir', os.path.abspath(v)) or o
    }
    
    # Helper function for config file
    def process_config_file(o, value):
        o.config_file = value
        if os.path.exists(value):
            config_options = read_config_file(value)
            # Merge configs, using a dictionary comprehension for clarity
            for key, val in vars(config_options).items():
                if key not in ('sources', 'include_path', 'compiler_directives', 'compile_time_env'):
                    if not getattr(o, key):  # Don't override if already set by cmd line
                        setattr(o, key, val)
                elif isinstance(val, list):
                    getattr(o, key).extend(val)
                elif isinstance(val, dict):
                    getattr(o, key).update(val)
        return o
    
    # Process options using reduce and functional handlers
    print(f"Initial options: {options}") # DEBUG
    print(f"Received opts: {opts}") # DEBUG
    
    options = reduce(
        lambda o, opt_pair: option_map.get(strip_prefix(opt_pair[0]), lambda o, v: o)(o, opt_pair[1]),
        filter(lambda o: not o[0].startswith('--embed='), opts),  # Skip --embed= (handled above)
        options
    )
    
    # Re-process the options to set global flags correctly after reduce
    if options.embed:
        Options.embed = options.embed
    if options.annotate:
        Options.annotate = options.annotate
        print(f"Set Options.annotate = {Options.annotate}")  # Debug
    if options.verbose:
        if hasattr(Options, 'verbose'):
            Options.verbose = options.verbose
    # We'll set output_file later when compilation_options is defined

    # Update sources
    options.sources = args
    
    # Define validation rules as (condition, error_message) pairs
    validations = [
        (options.use_listing_file and len(options.sources) > 1, 
         "Error: Only one source file allowed when using -o"),
        
        (options.shared_c_file_path and len(options.sources) > 0,
         "Error: Source file not allowed when using --generate-shared"),
        
        (len(options.sources) == 0 and not options.show_version,
         "Error: Need at least one source file"),
        
        (options.embed and len(options.sources) > 1,
         "Error: Only one source file allowed when using --embed"),
        
        (options.module_name and options.timestamps,
         "Error: Cannot use --module-name with --timestamps"),
        
        (options.module_name and len(options.sources) > 1,
         "Error: Only one source file allowed when using --module-name")
    ]
    
    # Apply validations using any() and list comprehension
    invalid_conditions = list(filter(lambda x: x[0], validations))
    if invalid_conditions:
        condition, error_message = invalid_conditions[0]
        print(Colors.error(error_message))
        if "Need at least one source file" in error_message:
            print_usage()
        sys.exit(1)

    # Create a CompilationOptions instance from default_options
    compilation_options = Options.CompilationOptions(**Options.default_options)
    
    # Set output_file if specified
    if options.output_file:
        compilation_options.output_file = options.output_file
    
    # Group attributes into appropriate destination objects using dictionary operations
    debug_attrs = {k: v for k, v in vars(options).items() if k.startswith('debug')}
    options_attrs = {k: v for k, v in vars(options).items() if hasattr(Options, k)}
    compilation_attrs = {k: v for k, v in vars(options).items() 
                         if not k.startswith('debug') and not hasattr(Options, k)}
    
    # Apply each group to its appropriate destination
    for k, v in debug_attrs.items():
        from . import DebugFlags
        if k in dir(DebugFlags):
            setattr(DebugFlags, k, v)
            
    for k, v in options_attrs.items():
        if hasattr(Options, k):
            setattr(Options, k, v)
        
    for k, v in compilation_attrs.items():
        if hasattr(compilation_options, k):
            setattr(compilation_options, k, v)
            
    # Process include paths
    include_path = getattr(Options, 'include_path', None)
    if include_path and compilation_options.include_path:
        compilation_options.include_path = include_path + compilation_options.include_path
    
    # Remove custom attributes that CompilationOptions doesn't accept
    for attr in ['config_file', 'sources']:
        if hasattr(compilation_options, attr):
            delattr(compilation_options, attr)
    
    return compilation_options, options.sources


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


if __name__ == "__main__":
    """Allow running the CmdLine module directly for testing."""
    print(Colors.info("Running CmdLine.py directly..."))
    try:
        options, sources = parse_command_line(sys.argv[1:])
        print("")
        print(Colors.success("Parsing successful!"))
        print(f"  {Colors.bold('Compilation Options:')} {options}")
        print(f"  {Colors.bold('Source Files:')} {sources}")
    except SystemExit as e:
        # Catch SystemExit from --help or errors in parsing
        if e.code != 0:
            print(Colors.error(f"Exited with code {e.code}"))
    except Exception as e:
        print(Colors.error(f"An unexpected error occurred: {e}"))
        import traceback
        traceback.print_exc()
