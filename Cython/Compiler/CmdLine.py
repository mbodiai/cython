#
#   Cython - Command Line Parsing
#


from dataclasses import dataclass, field
import os
import sys
from typing import Dict, List, Optional, Tuple, Union, Any
from argparse import Action, ArgumentParser
import rich_click as click
import importlib.metadata

from Cython.Compiler import Options


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

                    else:
                        n, v = opt, True
                    options[n] = v
            elif hasattr(values, '__iter__'):
                for opt in values:
                    if isinstance(opt, str):
                        if '=' in opt:
                            n, v = opt.split('=', 1)
                        else:
                            n, v = opt, opt
                        options[n] = v
        setattr(namespace, self.dest, options)


class ParseCompileTimeEnvAction(Action):
    def __call__(self, parser, namespace, values, option_string=None):
        old_env = dict(getattr(namespace, self.dest, {}))
        if values is not None and isinstance(values, str):
            new_env = Options.parse_compile_time_env(values, current_settings=old_env)
            setattr(namespace, self.dest, new_env)

# Simple configuration dataclass (May be removable if fully replaced by click)
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
    version = "unknown"
    try:
        version = importlib.metadata.version("cython")
    except (ImportError, importlib.metadata.PackageNotFoundError):
        try:
            if hasattr(sys.modules.get('Cython', None), '__version__'):
                version = sys.modules['Cython'].__version__
            else:
                try:
                    from .. import __version__
                    version = __version__
                except (ImportError, ValueError):
                    pass
        except ImportError:
            pass    
    print(Colors.header(f"Cython version {version}"))

def get_option_help() -> Dict[str, str]:
    """Generate option help text dictionary."""
    # ... (content unchanged) ...
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
    """Print usage information with color formatting."""
    # ... (content unchanged) ...
    option_help = get_option_help()
    print(Colors.header("Cython Compiler"))
    print(Colors.info("Usage:"))
    print("  cython [options] [source_files]")
    print("")
    print(Colors.info("Options:"))
    
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


# Trimmed handlers: only callbacks actually used by click
class OptionHandlers:
    """Minimal click callback helpers; extraneous no-op handlers removed."""

    # ---- global helpers ----
    @staticmethod
    def handle_help(options, value):
        print_usage()
        sys.exit(0)

    @staticmethod
    def handle_version(options, value):
        print_version()
        options.show_version = 1

    # ---- option callbacks ----
    @staticmethod
    def handle_directive(ctx, param, value):
        directives = Options.get_directive_defaults().copy()
        current = ctx.params.get('compiler_directives', {})
        if current:
            directives.update(current)
        if not value:
            return directives
        try:
            for directive_str in value:
                directives = Options.parse_directive_list(
                    directive_str, relaxed_bool=True, current_settings=directives
                )
            return directives
        except ValueError as e:
            raise click.BadParameter(f"Error parsing directives (-X): {e}", ctx=ctx, param=param)

    @staticmethod
    def handle_compile_time_env(ctx, param, value):
        env = dict(ctx.params.get('compile_time_env', {}))
        if not value:
            return env
        try:
            for env_str in value:
                env = Options.parse_compile_time_env(env_str, current_settings=env)
            return env
        except ValueError as e:
            raise click.BadParameter(
                f"Error parsing compile-time environment (-E): {e}", ctx=ctx, param=param
            ) from e

    @staticmethod
    def handle_warning_extra(ctx, param, value):
        if not value or ctx.resilient_parsing:
            return
        if 'compiler_directives' not in ctx.params:
            ctx.params['compiler_directives'] = Options.get_directive_defaults().copy()
        ctx.params['compiler_directives'].update(Options.extra_warnings)

    @staticmethod
    def handle_gdb_outdir(ctx, param, value):
        if value is None:
            return None
        ctx.params['gdb_debug'] = True
        from pathlib import Path
        try:
            path_obj = Path(value).resolve()
            os.makedirs(path_obj, exist_ok=True)
            return str(path_obj)
        except Exception as e:
            raise click.BadParameter(f"Invalid path for --gdb-outdir: {e}", ctx=ctx, param=param)

    @staticmethod
    def handle_annotate_coverage(ctx, param, value):
        if value is not None:
            ctx.params['annotate_html'] = True
            return value
        return None

# --- legacy handlers kept only for reference; no longer used by click ---

def parse_command_line(args: List[str]) -> Tuple[Options.CompilationOptions, List[str]]:
    """
    Parses command line arguments using click and returns results
    in the format expected by Cython.Compiler.Main.
    Uses custom error handling and help via print_usage.
    """
    # print(f"Compatibility parse_command_line received args: {args}") # Debug
    try:
        prog_name = os.path.basename(sys.argv[0]) if sys.argv else 'cython'
        context = cython_command.make_context(info_name=prog_name, args=args)

        if '--help' in args or '-h' in args:
             print_usage()
             sys.exit(0)

        with context:
            cython_command.invoke(context)

        if context.obj and 'options' in context.obj and 'sources' in context.obj:
            comp_options = context.obj['options']
            sources_list = context.obj['sources']
            if not isinstance(comp_options, Options.CompilationOptions):
                 print(Colors.error(f"Error: Internal context object has incorrect type for options: {type(comp_options)}"))
                 sys.exit(1)
            return comp_options, sources_list
        else:
            if '--version' in args or '-V' in args:
                 sys.exit(0) 
            print(Colors.error("Error: Failed to retrieve parsed options from context after command invocation."))
            sys.exit(1)

    except click.exceptions.Exit as e:
        sys.exit(e)
    except click.exceptions.UsageError as e:
        print(e.format_message(), file=sys.stderr)
        sys.exit(e.exit_code)
    except click.exceptions.ClickException as e:
        print(Colors.error(f"Error: {e.format_message()}"), file=sys.stderr)
        sys.exit(e.exit_code)
    except Exception:
        print(Colors.error("An unexpected error occurred during command line processing:"), file=sys.stderr)
        import traceback
        traceback.print_exc()
        sys.exit(1)

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
    
    parser.add_argument('-X', '--directive', dest='compiler_directives', action=ParseDirectivesAction, help=SUPPRESS)
    parser.add_argument('-E', '--compile-time-env', dest='compile_time_env', action=ParseCompileTimeEnvAction, help=SUPPRESS)
    parser.add_argument('-s', '--option', dest='options', action=ParseOptionsAction, help=SUPPRESS)
    parser.add_argument('sources', nargs='*', default=[])
    
    return parser


# --- Main Click Command Definition --- 
@click.command(
    name='cython',
    context_settings=dict(help_option_names=['-h', '--help']),
    add_help_option=False, 
    epilog="Environment variables: ..." 
)
@click.option('-V', '--version', '_version_flag_set', is_flag=True, is_eager=True, expose_value=True,
              help='Display version number and exit.')
@click.option('-h', '--help', 'show_help', is_flag=True, is_eager=True, expose_value=False,
              callback=lambda ctx, param, value: ctx.exit(print_usage()) if value else None,
              help='Show this message and exit.')
@click.option('-l', '--create-listing', 'use_listing_file', is_flag=True, default=False, help='Write error messages to a listing file.')
@click.option('-I', '--include-dir', 'include_path', multiple=True, type=click.Path(exists=True, file_okay=False, resolve_path=True), help='Search for include files in named directory (repeatable).')
@click.option('-o', '--output-file', type=click.Path(dir_okay=False, writable=True, resolve_path=True), help='Specify name of generated C/C++ file.')
@click.option('-t', '--timestamps', 'use_timestamps', is_flag=True, default=True, help='Only compile newer source files (default).')
@click.option('-f', '--force', 'force_compile', is_flag=True, default=False, help='Compile all source files (overrides -t).')
@click.option('-v', '--verbose', count=True, help='Be verbose (-vv for more). repeatable')
@click.option('-p', '--embed-positions', 'embed_pos_in_docstring', is_flag=True, default=False, help='Embed source code positions in docstrings.')
@click.option('-z', '--pre-import', type=str, default=None, help='Pre-import a module.')
@click.option('-D', '--no-docstrings', 'docstrings', is_flag=True, default=True, help='Strip docstrings (flag means \'strip\', so default is True=keep).') 
@click.option('-a', '--annotate', 'annotate_html', is_flag=True, default=False, help='Produce a colorized HTML version of the source.') 
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
@click.option('-Wextra', '--warning-extra', is_flag=True, default=False, callback=OptionHandlers.handle_warning_extra, expose_value=False, help='Enable extra warnings.')
@click.option('-X', '--directive', 'compiler_directives', multiple=True, callback=OptionHandlers.handle_directive, help='Override compiler directive (e.g., -X boundscheck=False). Repeatable.', metavar='NAME=VALUE,...')
@click.option('-E', '--compile-time-env', multiple=True, callback=OptionHandlers.handle_compile_time_env, help='Set compile-time environment variable (e.g., -E DEBUG=True). Repeatable.', metavar='NAME=VALUE,...')
@click.option('-w', '--working', 'working_path', type=click.Path(exists=True, file_okay=False, resolve_path=True), help='Sets the working directory for Cython.')
@click.option('--module-name', type=str, default=None, help='Fully qualified module name.')
@click.option('-M', '--depfile', 'make_depfile', is_flag=True, default=False, help='Produce depfiles for the sources.') 
@click.option('--cache', is_flag=True, default=False, help='Enable Cython compilation cache.')
@click.option('--embed', type=str, default=None, is_flag=True, flag_value='main', help='Generate main() embedding Python. Optional value=FUNC_NAME.', metavar='[FUNC_NAME]')
@click.option('--gdb', 'gdb_debug', is_flag=True, default=False, help='Output debug information for cygdb.')
@click.option('--gdb-outdir', type=click.Path(file_okay=False, writable=True, resolve_path=True), callback=OptionHandlers.handle_gdb_outdir, help='Specify gdb debug output directory (implies --gdb).')
@click.option('--annotate-coverage', type=click.Path(exists=True, dir_okay=False), callback=OptionHandlers.handle_annotate_coverage, help='Annotate using coverage.xml (implies -a).')
@click.option('--no-c-in-traceback', 'c_line_in_traceback', is_flag=True, default=True, help='Do not include C source info in tracebacks (flag=True means no C).')
@click.option('--cimport-from-pyx', is_flag=True, default=False, help='Allow cimporting from .pyx files.')
@click.option('--old-style-globals', is_flag=True, default=False, help='Use old-style globals lookup.')
@click.option('--convert-range', is_flag=True, default=False, help='Convert range() loops to C loops.')
@click.option('--cleanup', 'generate_cleanup_code', type=int, default=None, help='Release interned objects on Python exit (level indicates aggressiveness).')
@click.option('--generate-shared', 'shared_c_file_path', type=str, default=None, help='Generate shared C utility code file.')
@click.option('--shared', 'shared_utility_qualified_name', type=str, default=None, help='Import utility code from shared module (fully qualified name).')
@click.option('--config-file', type=click.Path(exists=True, dir_okay=False, resolve_path=True), help='Specify a configuration file to load options from.')
@click.option('--output-dir', type=click.Path(file_okay=False, writable=True, resolve_path=True), default=None, help='Specify the directory for generated C/C++ files.')

@click.argument('sources', nargs=-1, type=click.Path(exists=True, dir_okay=False, resolve_path=True))

@click.pass_context
def cython_command(ctx: click.Context, sources: Tuple[str, ...], _version_flag_set: bool, **kwargs):
    """The main function that processes options and prepares for compilation."""

    if _version_flag_set:
        print_version()
        ctx.exit()

    # Fail fast if the user did not supply any sources.  Historically the
    # compiler would happily exit with success in that case, which is usually
    # an error due to a mis-typed option (e.g. ``--embed`` eating the first
    # filename).  We treat *zero* sources as a usage error unless a specialised
    # action (such as ``--shared``) explicitly allows it.
    if not sources:
        print(Colors.error("Error: No source files supplied."), file=sys.stderr)
        ctx.exit(1)

    # print(Colors.info("Processing options...")) # Debug
    final_options = {} 
    config_options = {}
    # Prioritize command line, then env var, then default path?
    config_file_path = kwargs.get('config_file') or os.environ.get('CYTHONRC') # .cythonrc in cwd?
    # TODO: Add default config file lookup logic (.cythonrc in cwd or home?)

    # Define load_config_file locally or ensure it's imported/available
    def load_config_file(path):
        # Dummy implementation - replace with actual logic if needed here
        # Or ensure it's defined globally
        print(f"DEBUG: Trying to load config: {path}")
        if not path or not os.path.exists(path):
             return {}
        # Actual loading logic...
        loaded_cfg = {}
        try:
             with open(path, 'r') as f:
                  lines = f.readlines()
                  valid_lines = filter(lambda l: l.strip() and not l.strip().startswith('#'), lines)
                  config_items = [l.strip().split('=', 1) for l in valid_lines if '=' in l]
                  loaded_cfg = {k.strip().replace('-', '_'): v.strip() for k, v in config_items}
                  print(f"DEBUG: Loaded config file {path}: {loaded_cfg}")
        except Exception as e:
             print(Colors.warning(f"Warning: Error reading config file '{path}': {e}"))
        return loaded_cfg

    if config_file_path:
        config_options = load_config_file(config_file_path)

    processed_config = {}
    for key, value in config_options.items():
         param = next((p for p in ctx.command.params if p.name == key), None)
         if param:
             try:
                 if isinstance(param.type, click.types.BoolParamType) or getattr(param,'is_flag', False):
                      processed_config[key] = str(value).lower() in ('true', '1', 'yes', 'on')
                 elif isinstance(param.type, click.types.IntParamType):
                      processed_config[key] = int(value)
                 elif isinstance(param.type, click.types.Path):
                      # Use the param's own converter
                      processed_config[key] = param.type.convert(value, param, ctx)
                 elif key in ('compiler_directives', 'compile_time_env'):
                      # Assume callback handles parsing string list/dict
                      # Call the handler directly to parse the config value string
                      handler = getattr(OptionHandlers, f"handle_{key}", None)
                      if handler:
                          # Handler expects (ctx, param, value_tuple) - fake it for config string
                          # We need to pass the *parsed* value from config, not the string itself
                          # Re-evaluate how config directives/env are handled
                          # Let's just store the raw string for now and parse later
                          processed_config[key] = value 
                      else:
                          processed_config[key] = value
                 else:
                      processed_config[key] = value 
             except Exception as e:
                  print(Colors.warning(f"Warning: Could not convert config value for '{key}': {e}"))
                  processed_config[key] = value 
         else:
              processed_config[key] = value 

    final_options.update(processed_config)
    cmd_line_options = {k: v for k, v in kwargs.items() if v is not None and k not in ('_version_flag_set', 'show_help', 'config_file')} 
    final_options.update(cmd_line_options)

    # print(f"Final combined options before processing: {final_options}") # Debug

    # --- Prepare Cython CompilationOptions ---
    comp_options = Options.CompilationOptions(**Options.default_options) 

    comp_env = {}
    # Parse compile_time_env from config string if present
    if 'compile_time_env' in final_options and isinstance(final_options['compile_time_env'], str):
        try:
            comp_env.update(Options.parse_compile_time_env(final_options['compile_time_env']))
        except ValueError as e:
            print(Colors.warning(f"Warning: Invalid compile_time_env in config: {e}"))
    # Update/overwrite with cmd line env if provided (already parsed by callback)
    if 'compile_time_env' in cmd_line_options and isinstance(cmd_line_options['compile_time_env'], dict):
         comp_env.update(cmd_line_options['compile_time_env'])

    merged_directives = Options.get_directive_defaults().copy()
    # Parse directives from config string if present
    if 'compiler_directives' in final_options and isinstance(final_options['compiler_directives'], str):
        try:
            merged_directives.update(Options.parse_directive_list(final_options['compiler_directives'], relaxed_bool=True))
        except ValueError as e:
             print(Colors.warning(f"Warning: Invalid compiler_directives in config: {e}"))
    # Update/overwrite with cmd line directives if provided (already parsed by callback)
    if 'compiler_directives' in cmd_line_options and isinstance(cmd_line_options['compiler_directives'], dict):
         merged_directives.update(cmd_line_options['compiler_directives'])
    # Apply Wextra if flag was set (check original kwargs as callback has expose_value=False)
    if kwargs.get('warning_extra'):
         merged_directives.update(Options.extra_warnings)

    # Map processed options to CompilationOptions
    direct_copy_attrs = [
        'use_listing_file', 'include_path', 'output_file', 'verbose',
        'embed_pos_in_docstring', 'generate_cleanup_code', 'cache',
        'working_path', 'gdb_debug', 'annotate_coverage_xml',
        'emit_linenums', 'cplus', 'error_on_unknown_names',
        'error_on_uninitialized', 'capi_reexport_cincludes', 'fast_fail',
        'warning_errors', 'module_name', 'make_depfile', 
        'pre_import', 'convert_range', 'cimport_from_pyx', 'old_style_globals',
        'shared_c_file_path', 'shared_utility_qualified_name', 'output_dir'
    ]

    for attr in direct_copy_attrs:
        if attr in final_options:
             # Handle gdb_debug implicitly set by gdb_outdir callback
             if attr == 'gdb_debug' and 'gdb_outdir' in final_options and final_options['gdb_outdir'] is not None:
                 setattr(comp_options, attr, True)
             else:
                 setattr(comp_options, attr, final_options[attr])

    comp_options.compiler_directives = merged_directives
    comp_options.compile_time_env = comp_env
    comp_options.timestamps = not final_options.get('force_compile', False)
    # Determine language level
    comp_options.language_level = Options.default_options['language_level']
    if final_options.get('lang_level_2'):
        comp_options.language_level = 2
    elif final_options.get('lang_level_3') or final_options.get('lang_level_3str'):
        comp_options.language_level = 3
    # Determine annotation level
    annotate = None
    if final_options.get('annotate_fullc'):
        annotate = 'fullc'
    elif final_options.get('annotate_html') or final_options.get('annotate_coverage_xml'):
        annotate = 'default'
    comp_options.annotate = annotate
    comp_options.docstrings = final_options.get('docstrings', True)
    comp_options.c_line_in_traceback = final_options.get('c_line_in_traceback', True)

    comp_options.embed = final_options.get('embed')
    Options.embed = comp_options.embed 

    if final_options.get('lenient', False):
        comp_options.error_on_unknown_names = False
        comp_options.error_on_uninitialized = False

    if 'verbose' in final_options:
         # Assuming Options.verbose is intended to be a global setting
         try:
             Options.verbose = int(final_options['verbose'])
         except (ValueError, TypeError):
             Options.verbose = 1 if final_options['verbose'] else 0
    
  
    ctx.obj = {'options': comp_options, 'sources': list(sources)}


if __name__ == "__main__":
    # print(Colors.info("Running CmdLine.py directly via __main__..."))
    cython_command()
