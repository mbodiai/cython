#
#   Cython - Command Line Parsing
#


from dataclasses import dataclass, field
import os
import sys
from typing import Dict, List, Optional, Tuple, Union, Any
from argparse import Action, ArgumentParser
import rich_click as click

from Cython import Utils
from Cython.Compiler import Options, Directives


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


def print_usage():
    """Print usage information with color formatting."""
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


def _coerce_env_value(value: str) -> Any:
    value = value.strip()
    if not value:
        raise ValueError("Empty compile-time env value")

    if value[0] in "\"'":
        if len(value) < 2 or value[-1] != value[0]:
            raise ValueError("Unmatched quotes in compile-time env value")
        inner = value[1:-1]
        inner = inner.replace("\\\\", "\\")
        inner = inner.replace("\\\"", "\"")
        inner = inner.replace("\\'", "'")
        return inner

    if value.isdigit() or (value.startswith("-") and value[1:].isdigit()):
        try:
            return int(value)
        except ValueError:
            pass

    try:
        return float(value)
    except ValueError:
        pass

    lowered = value.lower()
    if lowered in ("true", "yes"):
        return True
    if lowered in ("false", "no"):
        return False
    if lowered in ("none", "null"):
        return None

    return value


def _parse_compile_time_env_string(spec: str, env: Dict[str, Any]) -> Dict[str, Any]:
    for item in spec.split(","):
        item = item.strip()
        if not item:
            continue
        if "=" not in item:
            raise ValueError(f'Expected "=" in option "{item}"')
        name, value = [part.strip() for part in item.split("=", 1)]
        env[name] = _coerce_env_value(value)
    return env


def _coerce_directive_value(name: str, raw_value: str, relaxed_bool: bool) -> Any:
    type_info = Directives.directive_types.get(name)
    if type_info is bool:
        text = raw_value if not relaxed_bool else raw_value.lower()
        truthy = {"true", "yes", "1"} if relaxed_bool else {"True"}
        falsy = {"false", "no", "0"} if relaxed_bool else {"False"}
        if text in truthy:
            return True
        if text in falsy:
            return False
        raise ValueError(
            f"{name} directive must be set to True or False, got '{raw_value}'"
        )
    if type_info is int:
        try:
            return int(raw_value)
        except ValueError:
            raise ValueError(
                f"{name} directive must be set to an integer, got '{raw_value}'"
            ) from None
    if type_info is str:
        return raw_value
    if callable(type_info):
        return type_info(name, raw_value)
    return raw_value


def _parse_directives_string(
    spec: str,
    *,
    relaxed_bool: bool = False,
    ignore_unknown: bool = False,
    current_settings: Optional[Dict[str, Any]] = None,
) -> Dict[str, Any]:
    directives = Directives()
    result: Dict[str, Any] = dict(current_settings or {})
    for item in spec.split(","):
        item = item.strip()
        if not item:
            continue
        if "=" not in item:
            raise ValueError(f'Expected "=" in option "{item}"')
        name, raw_value = [s.strip() for s in item.split("=", 1)]
        if name.endswith(".all"):
            prefix = name[:-3]
            found_any = False
            for directive in directives:
                if directive.startswith(prefix):
                    found_any = True
                    result[directive] = _coerce_directive_value(
                        directive, raw_value, relaxed_bool=relaxed_bool
                    )
            if not found_any and not ignore_unknown:
                raise ValueError(f'Unknown option: "{name}"')
            continue

        if name not in directives:
            if not ignore_unknown:
                raise ValueError(f'Unknown option: "{name}"')
            continue

        dtype = Directives.directive_types.get(name)
        if dtype is list:
            if name in result and isinstance(result[name], list):
                result[name].append(raw_value)
            else:
                result[name] = [raw_value]
        else:
            result[name] = _coerce_directive_value(name, raw_value, relaxed_bool)
    return result


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
        Utils.print_version()
        options.show_version = 1

    # ---- option callbacks ----
    @staticmethod
    def handle_directive(ctx, param:click.Parameter, value:str):
        try:
            return _parse_directives_string(
                value,
                relaxed_bool=True,
                current_settings=ctx.params.get('compiler_directives', {}),
            )
        except ValueError as exc:
            raise click.BadParameter(str(exc), ctx=ctx, param=param) from exc

    @staticmethod
    def handle_compile_time_env(ctx, param, value):
        env = dict(ctx.params.get('compile_time_env', {}))
        if not value:
            return env
        try:
            for env_str in value:
                env = _parse_compile_time_env_string(env_str, env)
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
            ctx.params['compiler_directives'] = Directives.DIRECTIVE_DEFAULTS.copy()
        ctx.params['compiler_directives'].update(Directives.extra_warnings)

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
            raise click.BadParameter(f"Invalid path for --gdb-outdir: {e}", ctx=ctx, param=param) from None

    @staticmethod
    def handle_annotate_coverage(ctx, param, value):
        if value is not None:
            ctx.params['annotate_html'] = True
            return value
        return None

class ParseDirectivesAction(Action):
    def __call__(self, parser, namespace, values, option_string=None):
        base = getattr(namespace, self.dest, None) or Directives.DIRECTIVE_DEFAULTS.copy()
        parsed = _parse_directives_string(values, relaxed_bool=True, current_settings=base)
        setattr(namespace, self.dest, parsed)


class ParseCompileTimeEnvAction(Action):
    def __call__(self, parser, namespace, values, option_string=None):
        base = getattr(namespace, self.dest, None) or {}
        env = dict(base)
        env = _parse_compile_time_env_string(values, env)
        setattr(namespace, self.dest, env)


class ParseOptionsAction(Action):
    def __call__(self, parser, namespace, values, option_string=None):
        opts = getattr(namespace, self.dest, None) or {}
        if '=' not in values:
            raise ValueError('Expected "=" in option "%s"' % values)
        name, value = [s.strip() for s in values.split('=', 1)]
        opts[name] = value
        setattr(namespace, self.dest, opts)


@click.command(
    name='cython',
    context_settings=dict(help_option_names=['-h', '--help']),
    epilog="Environment variables: …",
)
@click.option('-V', '--version', '_version_flag_set', is_flag=True, is_eager=True, expose_value=True,
              help='Display version number and exit.')
@click.option('-l', '--create-listing', 'use_listing_file', is_flag=True, default=False)
@click.option('-I', '--include-dir', 'include_path', multiple=True, type=click.Path(exists=True, file_okay=False, resolve_path=True))
@click.option('-o', '--output-file', type=click.Path(dir_okay=False, writable=True, resolve_path=True))
@click.option('-t', '--timestamps', 'use_timestamps', is_flag=True, default=True)
@click.option('-f', '--force', 'force_compile', is_flag=True, default=False)
@click.option('-v', '--verbose', count=True)
@click.option('-p', '--embed-positions', 'embed_pos_in_docstring', is_flag=True, default=False)
@click.option('-z', '--pre-import', type=str, default=None)
@click.option('-D', '--no-docstrings', 'strip_docstrings', is_flag=True, default=False)
@click.option('-a', '--annotate', 'annotate_html', is_flag=True, default=False)
@click.option('--annotate-fullc', is_flag=True, default=False)
@click.option('--line-directives', 'emit_linenums', is_flag=True, default=False)
@click.option('-+', '--cplus', is_flag=True, default=False)
@click.option('-2', 'lang_level_2', is_flag=True, default=False)
@click.option('-3', 'lang_level_3', is_flag=True, default=False)
@click.option('--3str', 'lang_level_3str', is_flag=True, default=False)
@click.option('--lenient', is_flag=True, default=False)
@click.option('--capi-reexport-cincludes', 'capi_reexport_cincludes', is_flag=True, default=False)
@click.option('--fast-fail', 'fast_fail', is_flag=True, default=False)
@click.option('-Werror', '--warning-errors', 'warning_errors', is_flag=True, default=False)
@click.option('-Wextra', '--warning-extra', is_flag=True, default=False, callback=OptionHandlers.handle_warning_extra, expose_value=False)
@click.option('-X', '--directive', 'compiler_directives', multiple=True, callback=OptionHandlers.handle_directive, metavar='NAME=VALUE,...')
@click.option('-E', '--compile-time-env', multiple=True, callback=OptionHandlers.handle_compile_time_env, metavar='NAME=VALUE,...')
@click.option('-w', '--working', 'working_path', type=click.Path(exists=True, file_okay=False, resolve_path=True))
@click.option('--module-name', type=str, default=None)
@click.option('-M', '--depfile', 'make_depfile', is_flag=True, default=False)
@click.option('--cache', is_flag=True, default=False)
@click.option('--embed', type=str, default=None, is_flag=True, flag_value='main', metavar='[FUNC_NAME]')
@click.option('--gdb', 'gdb_debug', is_flag=True, default=False)
@click.option('--gdb-outdir', type=click.Path(file_okay=False, writable=True, resolve_path=True), callback=OptionHandlers.handle_gdb_outdir)
@click.option('--annotate-coverage', type=click.Path(exists=True, dir_okay=False), callback=OptionHandlers.handle_annotate_coverage)
@click.option('--no-c-in-traceback', 'c_line_in_traceback', is_flag=True, default=True)
@click.option('--cimport-from-pyx', is_flag=True, default=False)
@click.option('--old-style-globals', is_flag=True, default=False)
@click.option('--convert-range', is_flag=True, default=False)
@click.option('--cleanup', 'generate_cleanup_code', type=int, default=None)
@click.option('--generate-shared', 'shared_c_file_path', type=str, default=None)
@click.option('--shared', 'shared_utility_qualified_name', type=str, default=None)
@click.option('--config-file', type=click.Path(exists=True, dir_okay=False, resolve_path=True))
@click.option('--output-dir', type=click.Path(file_okay=False, writable=True, resolve_path=True), default=None)
@click.argument('sources', nargs=-1, type=click.Path(exists=True, dir_okay=False, resolve_path=True))
@click.pass_context
def cython_command(ctx: click.Context, sources, _version_flag_set, **kw):
    if _version_flag_set:
        Utils.print_version()
        from .build_executable import default_options
        opts = default_options
        opts.show_version = True
        ctx.obj = {'options': opts, 'sources': list(sources)}
        return
    from .build_executable import default_options
    opts = default_options
    opts.use_listing_file = kw.get('use_listing_file') or False
    includes = list(kw.get('include_path') or [])
    if includes:
        opts.include_path = list(includes)
    out_file = kw.get('output_file')
    if out_file:
        opts.output_file = out_file
    force = kw.get('force_compile') or False
    use_ts = kw.get('use_timestamps') if 'use_timestamps' in kw else True
    opts.timestamps = bool(use_ts and not force)
    opts.verbose = int(kw.get('verbose') or 0)
    if kw.get('embed_pos_in_docstring'):
        Directives.embed_pos_in_docstring = True
    preimp = kw.get('pre_import')
    if preimp is not None:
        Directives.pre_import = preimp
    if kw.get('strip_docstrings'):
        Directives.docstrings = False
    if kw.get('annotate_html'):
        Directives.annotate = 'default'
    if kw.get('annotate_fullc'):
        Directives.annotate = 'fullc'
    opts.emit_linenums = bool(kw.get('emit_linenums'))
    opts.cplus = bool(kw.get('cplus'))
    if kw.get('lang_level_2'):
        opts.language_level = 2
    if kw.get('lang_level_3'):
        opts.language_level = 3
    if kw.get('lang_level_3str'):
        opts.language_level = '3'
    if kw.get('lenient'):
        Directives.error_on_unknown_names = False
        Directives.error_on_uninitialized = False
    if kw.get('capi_reexport_cincludes'):
        opts.capi_reexport_cincludes = True
    if kw.get('fast_fail'):
        Directives.fast_fail = True
    if kw.get('warning_errors'):
        Directives.warning_errors = True
    directives = kw.get('compiler_directives')
    if isinstance(directives, dict):
        opts.compiler_directives = directives
    env = kw.get('compile_time_env')
    if isinstance(env, dict):
        opts.compile_time_env = env
    work = kw.get('working_path')
    if work:
        opts.working_path = work
    modname = kw.get('module_name')
    if modname:
        opts.module_name = modname
    if kw.get('make_depfile'):
        opts.make_depfile = True
    if kw.get('cache'):
        opts.cache = True
    embed = kw.get('embed')
    if embed is not None:
        Directives.embed = embed
    if kw.get('gdb_debug'):
        opts.gdb_debug = True
    outdir = kw.get('output_dir')
    if outdir:
        opts.output_dir = outdir
    if kw.get('c_line_in_traceback') is False:
        opts.c_line_in_traceback = False
    if kw.get('cimport_from_pyx'):
        Directives.cimport_from_pyx = True
    if kw.get('old_style_globals'):
        Directives.old_style_globals = True
    if kw.get('convert_range'):
        Directives.convert_range = True
    cleanup = kw.get('generate_cleanup_code')
    if cleanup is not None:
        Directives.generate_cleanup_code = cleanup
    shared_c = kw.get('shared_c_file_path')
    if shared_c:
        opts.shared_c_file_path = shared_c
    shared_qual = kw.get('shared_utility_qualified_name')
    if shared_qual:
        opts.shared_utility_qualified_name = shared_qual
    cfg = kw.get('config_file')
    if cfg:
        opts.config_file = cfg
    if kw.get('gdb_debug') and not opts.output_dir:
        opts.output_dir = os.curdir
    ctx.obj = {'options': opts, 'sources': list(sources)}


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

def comma_list(string):
    return string.split(',')

def parse_command_line_raw(parser, args):
    # special handling for --embed and --embed=xxxx as they aren't correctly parsed
    def filter_out_embed_options(args):
        with_embed, without_embed = [], []
        for x in args:
            if x == '--embed' or x.startswith('--embed='):
                with_embed.append(x)
            else:
                without_embed.append(x)
        return with_embed, without_embed

    with_embed, args_without_embed = filter_out_embed_options(args)

    arguments, unknown = parser.parse_known_args(args_without_embed)

    sources = arguments.sources
    del arguments.sources

    # unknown can be either debug, embed or input files or really unknown
    for option in unknown:
        if option.startswith('-'):
            parser.error("unknown option " + option)
        else:
            sources.append(option)

    # embed-stuff must be handled extra:
    for x in with_embed:
        if x == '--embed':
            name = 'main'  # default value
        else:
            name = x[len('--embed='):]
        setattr(arguments, 'embed', name)

    return arguments, sources


def parse_command_line(args):
    parser = create_cython_argparser()
    arguments, sources = parse_command_line_raw(parser, args)

    work_dir = getattr(arguments, 'working_path', '')
    for source in sources:
        if work_dir and not os.path.isabs(source):
            source = os.path.join(work_dir, source)
        if not os.path.exists(source):
            import errno
            raise FileNotFoundError(errno.ENOENT, os.strerror(errno.ENOENT), source)

    from .build_executable import default_options
    options = Options.CompilationOptions(**default_options)
    for name, value in vars(arguments).items():
        if name.startswith('debug'):
            from . import DebugFlags
            if name in dir(DebugFlags):
                setattr(DebugFlags, name, value)
            else:
                parser.error("Unknown debug flag: %s\n" % name)
        elif hasattr(Options, name):
            setattr(Options, name, value)
        else:
            setattr(options, name, value)

    if options.use_listing_file and len(sources) > 1:
        parser.error("cython: Only one source file allowed when using -o\n")
    if options.shared_c_file_path:
        if len(sources) > 0:
            parser.error("cython: Source file not allowed when using --generate-shared\n")
    elif len(sources) == 0 and not options.show_version:
        parser.error("cython: Need at least one source file\n")
    from .Directives import embed as global_embed
    if global_embed and len(sources) > 1:
        parser.error("cython: Only one source file allowed when using --embed\n")
    if options.module_name:
        if options.timestamps:
            parser.error("cython: Cannot use --module-name with --timestamps\n")
        if len(sources) > 1:
            parser.error("cython: Only one source file allowed when using --module-name\n")
    return options, sources
