import os

import rich_click as click
# from mbpy import PINK # Temporarily comment out problematic import
from typing_extensions import TYPE_CHECKING, Literal

from mbcore.log import INFO, LevelType, setup_logging, setup_traceback

# from mbpy.cli import AsyncGroup
LIGHT_CYAN_BOLD = "#87d7ff"
CYAN_BOLD = "#00ffff"
PINK_BOLD = "#ffafd7"
LIGHT_BLUE = "#afd7ff"
LIGHT_BLUE_BOLD = "#afd7ff"
RESET = ""  # Resetting the color, no hex value
PINK = "#ffafd7"
PINK_BOLD = "bold #ffd7e5"
GOLD_BOLD = "bold #ffd7af"
WHITE_BOLD = "bold white"
PINK = "#ffd7e5"
GOLD = "#ffd7af"
THEME = {
    "info": f"{LIGHT_CYAN_BOLD}",
    "success": f"{LIGHT_BLUE}",
    "light_blue": f"{LIGHT_BLUE_BOLD}",
    "reset": RESET,
    "pink": f"{PINK}",
}

if TYPE_CHECKING:
    from mbcore.display import safe_print
    from mbcore.types import wrapafter
else:

    def wrapafter(*args, **kwargs):
        return lambda x: x

    from mbcore.display import safe_print

setup_traceback()
setup_logging()


@wrapafter(click.RichHelpConfiguration, returns=click.RichHelpConfiguration)
def get_help_config(*args, **kwargs) -> click.RichHelpConfiguration:
    from dataclasses import asdict, dataclass, field
    from typing import Dict, List

    import rich
    import rich.align
    import rich.style
    from rich.padding import PaddingDimensions
    from rich.text import Text
    from rich_click.rich_help_configuration import RichHelpConfiguration
    from rich_click.utils import CommandGroupDict, OptionGroupDict

    from mbcore._traceback import NO_BOX

    @dataclass
    class RichHelpConfig:
        """Streamlined help configuration with consistent branding."""

        # Fixed strings
        header_text: "Text | str|None" = field(default=None)
        footer_text: "Text | str|None" = field(default=None)
        deprecated_string: str = field(default="(Deprecated) ")
        default_string: str = field(default="[default: {}]")
        envvar_string: str = field(default="[env var: {}]")
        required_short_string: str = field(default="*")
        required_long_string: str = field(default="[required]")
        range_string: str = field(default=" [{}]")
        arguments_panel_title: str = field(default="Arguments")
        options_panel_title: str = field(default="Options")
        commands_panel_title: str = field(default="Commands")
        errors_panel_title: str = field(default="Error")
        errors_suggestion: "Text | str | None" = field(
            default="Try ' --help' for help.")
        """Defaults to Try 'cmd -h' for help. Set to False to disable."""
        errors_epilogue: "Text | str | None" = field(default=None)
        aborted_text: str = field(default="Aborted.")

        # Behaviours
        show_arguments: bool = field(default=False)
        """Show positional arguments"""
        show_metavars_column: bool = field(default=False)
        """Show a column with the option metavar (eg. INTEGER)"""
        append_metavars_help: bool = field(default=False)
        """Append metavar (eg. [TEXT]) after the help text"""
        option_envvar_first: bool = field(default=False)
        """Show env vars before option help text instead of after"""
        text_markup: Literal["ansi", "rich", "markdown", None] = "ansi"

        use_markdown_emoji: bool = field(default=True)
        """Parse emoji codes in markdown :smile:"""
        command_groups: "Dict[str, List[CommandGroupDict]]" = field(
            default_factory=lambda: {
                "CORE": [
                    CommandGroupDict(
                        name="PACKAGING",
                        commands=[
                            "install", "uninstall", "freeze", "list", "search",
                            "show", "upload"
                        ],
                    ),
                ],
            }, )
        """Define sorted groups of panels to display subcommands"""
        option_groups: "Dict[str, List[OptionGroupDict]]" = field(
            default_factory=lambda: {})
        """Define sorted groups of panels to display options and arguments"""
        use_click_short_help: bool = field(default=True)
        """Use click's default function to truncate help text"""

        highlighter_patterns: List[str] = field(default_factory=lambda: [
            r"(^|[^\w\-])(?P<switch>-([^\W0-9][\w\-]*\w|[^\W0-9]))",
            r"(^|[^\w\-])(?P<option>--([^\W0-9][\w\-]*\w|[^\W0-9]))",
            r"(?P<metavar><[^>]+>)",
        ], )
        # Text handling
        text_markup: Literal["ansi", "rich", "markdown", None] = "ansi"

        # Core brand colors
        PINK_BOLD = "bold #ffd7e5"
        GOLD_BOLD = "bold #ffd7af"
        WHITE_BOLD = "bold white"
        PINK = "#ffd7e5"
        GOLD = "#ffd7af"
        style_helptext_first_line: "rich.style.StyleType" = field(
            default="bold dark_slate_gray3")
        style_helptext: "rich.style.StyleType" = field(default="")
        # Essential styles
        style_command: "rich.style.StyleType" = field(default=GOLD_BOLD)
        style_option: "rich.style.StyleType" = field(default=PINK_BOLD)
        style_usage: "rich.style.StyleType" = field(default=PINK_BOLD)
        style_header_text: "rich.style.StyleType" = field(default=WHITE_BOLD)

        # Remove all panels/boxes
        style_options_panel_box: "str | Box | None" = field(default=NO_BOX)
        style_commands_panel_box: "str | Box | None" = field(default=NO_BOX)
        style_errors_panel_box: "str | Box | None " = field(default=NO_BOX)

        # Layout settings
        align_options_panel: "rich.align.AlignMethod" = field(default="left")
        align_commands_panel: "rich.align.AlignMethod" = field(default="left")
        style_options_table_show_lines: bool = field(default=False)
        style_commands_table_show_lines: bool = field(default=False)
        style_options_table_padding: "PaddingDimensions" = field(
            default_factory=lambda: (0, 2))

        # Section titles
        arguments_panel_title: str = field(default="ARGUMENTS:")
        options_panel_title: str = field(default="FLAGS:")
        commands_panel_title: str = field(default="COMMANDS:")

        # Error handling
        style_errors_suggestion: "rich.style.StyleType" = field(
            default=PINK_BOLD)
        style_errors_suggestion_command: "rich.style.StyleType" = field(
            default=PINK_BOLD, )

        # Width settings
        try:
            width: int | None = field(default=os.get_terminal_size().columns)
            max_width: int | None = field(default=120)
        except OSError:
            width: int | None = field(default=120)
            max_width: int | None = field(default=120)

        # Enable command grouping
        group_arguments_options: bool = field(default=True)

    return RichHelpConfiguration(**{**asdict(RichHelpConfig(*args)), **kwargs})


# @click.group("m",cls=AsyncGroup)
# @click.pass_context
# @click.rich_config(get_help_config())
# def _main(ctx: click.Context):
#     ctx.command.no_args_is_help = True
#     if ctx.invoked_subcommand is None:
# safe_print(ctx.get_help())


@click.command("cache", no_args_is_help=True)
@click.argument("function_name", type=str, required=False)
@click.option("-c", "--clear", is_flag=True, help="Clear the cache")
@click.option("-s", "--stats", is_flag=True, help="Show cache statistics")
@click.option("-i", "--info", is_flag=True, help="Show cache information")
@click.option("-v", "--verbose", is_flag=True, hidden=True)
@click.option("-d", "--debug", is_flag=True, hidden=True)
@click.option("-vv", "--very-verbose", is_flag=True, hidden=True)
@click.rich_config(get_help_config())
@click.help_option("-h", "--help")
@click.pass_context
def cache(
    ctx,
    function_name: str | None = None,
    clear: bool = False,
    stats: bool = False,
    info: bool = False,
    **kwargs,
) -> None:
    """Inspect the cache.

    Args:
        function_name (str, optional): Fully qualified name (module.function) of the function to inspect. If none, aggregate statistics are displayed. Defaults to None.

    """
    from rich.console import Console
    from rich.table import Table

    from mbcore.cache import cache as ccache
    from mbcore.import_utils import smart_import

    console = Console()

    # Load cache first
    ccache.load()

    if clear:
        ccache.clear_disk()
        ccache.clear_memory()
        console.print("[bold green]Cache cleared.[/bold green]")
        return

    # Get the cache info
    cache_info = ccache.cache_info()

    # Function-specific info
    if function_name:
        try:
            f = smart_import(function_name)
            func_info = ccache.cache_info(function_name)

            if not func_info:
                console.print(
                    f"[bold red]No cache info found for[/bold red] [bold cyan]{function_name}[/bold cyan]"
                )
                return

            # Create a pretty table for the function
            table = Table(title=f"[bold]Cache info for {function_name}[/bold]",
                          show_header=True,
                          header_style="bold")
            table.add_column("Metric", style="cyan")
            table.add_column("Value", style="green")

            table.add_row("Hits", str(func_info.hits))
            table.add_row("Misses", str(func_info.misses))

            console.print(table)

            # Create a table for the top keys
            if hasattr(func_info, "by_key") and func_info.by_key:
                # Sort keys by hits
                sorted_keys = sorted(func_info.by_key.items(),
                                     key=lambda x: x[1].hits,
                                     reverse=True)[:5]  # Top 5 keys

                keys_table = Table(title="Top Keys by Hits",
                                   show_header=True,
                                   header_style="bold")
                keys_table.add_column("Key", style="cyan")
                keys_table.add_column("Hits", style="green", justify="right")

                for key, key_info in sorted_keys:
                    key_str = str(getattr(key, "key", key))
                    keys_table.add_row(key_str, str(key_info.hits))

                console.print(keys_table)

        except Exception as e:
            console.print(f"[bold red]Error:[/bold red] {e}")
        return

    # Global info with stats or info flag
    if stats or info:
        # Force an update of cache stats before displaying
        if hasattr(cache_info, "update_stats"):
            cache_info.update_stats()

        # Create a pretty table for global stats
        summary = Table(title="[bold]Cache Summary[/bold]",
                        show_header=True,
                        header_style="bold")
        summary.add_column("Metric", style="cyan")
        summary.add_column("Value", style="green")

        # Ensure currsize is updated before displaying
        summary.add_row("Total Entries", str(cache_info.currsize))
        summary.add_row("Total Hits", str(cache_info.hits))
        summary.add_row("Total Misses", str(cache_info.misses))
        summary.add_row("Memory Usage", str(cache_info.currmemory))

        console.print(summary)

        if hasattr(cache_info, "by_function") and cache_info.by_function:
            # Sort functions by hits
            sorted_funcs = sorted(cache_info.by_function.items(),
                                  key=lambda x: x[1].hits,
                                  reverse=True)

            # Create a table for top functions
            funcs_table = Table(title="[bold]Top Functions by Hits[/bold]",
                                show_header=True,
                                header_style="bold")
            funcs_table.add_column("Function", style="cyan")
            funcs_table.add_column("Hits", style="green", justify="right")
            funcs_table.add_column("Misses", style="yellow", justify="right")
            funcs_table.add_column("Keys", style="blue", justify="right")

            for func_name, func_info in sorted_funcs[:5]:  # Top 5 functions
                key_count = len(getattr(func_info, "by_key", {}))
                funcs_table.add_row(func_name, str(func_info.hits),
                                    str(func_info.misses), str(key_count))

            console.print(funcs_table)

            # Create a table for top keys across all functions
            all_keys = []
            for func_name, func_info in cache_info.by_function.items():
                if hasattr(func_info, "by_key"):
                    for key, key_info in func_info.by_key.items():
                        all_keys.append((key, key_info, func_name))

            # Sort all keys by hits
            sorted_keys = sorted(all_keys,
                                 key=lambda x: x[1].hits,
                                 reverse=True)[:5]  # Top 5 keys

            if sorted_keys:
                keys_table = Table(title="[bold]Top Keys by Hits[/bold]",
                                   show_header=True,
                                   header_style="bold")
                keys_table.add_column("Function", style="cyan")
                keys_table.add_column("Key", style="green")
                keys_table.add_column("Hits", style="yellow", justify="right")

                for key, key_info, func_name in sorted_keys:
                    key_str = str(getattr(key, "key", key))
                    keys_table.add_row(func_name, key_str, str(key_info.hits))

                console.print(keys_table)
        else:
            console.print("[bold yellow]No cache entries found.[/bold yellow]")
        return

    # Default behavior with no flags
    if function_name or clear or info or stats:
        # Specific function or action specified, process normally
        console.print(str(cache_info))
    else:
        # Show a more user-friendly message when no parameters provided
        console.print("[bold]MB Cache Commands[/bold]\n")
        console.print("Use one of the following commands:")
        console.print(
            "  [cyan]mb cache --info[/cyan]    View cache statistics in detail"
        )
        console.print(
            "  [cyan]mb cache --stats[/cyan]   View basic cache statistics")
        console.print("  [cyan]mb cache --clear[/cyan]   Clear the cache")
        console.print(
            "  [cyan]mb cache <function>[/cyan]  View info for a specific function"
        )


LOG_EXAMPLES = """ **Examples:**

    ```bash

        # View log files\n

        mb log -p\n

        # Configure logging\n

        mb log -v                         # Set log level to verbose\n
        mb log -d                         # Set log level to debug\n
        mb log -i                         # Set log level to info (default)\n
        mb log -w                         # Set log level to warning\n
        mb log -e                         # Set log level to error\n

        # Search logs\n

        mb log -S Protocol                # Search for "Protocol" in all log files\n
        mb log -S "ERROR Protocol"        # Search for "Protocol" in ERROR level logs\n

        # Filtering options\n

        mb log -S "start=20:30:00 Protocol"   # Only show logs after 8:30 PM\n
        mb log -S "ctx=5 Protocol"            # Show 5 lines of context (default: 2)\n
        mb log -S "n=20 Protocol"             # Limit to 20 results\n
"""


@click.command(
    "log",
    context_settings={
        "allow_extra_args": True,
        "ignore_unknown_options": True
    },
    no_args_is_help=False,
    epilog=LOG_EXAMPLES,
)
@click.option("-S", "--search", is_flag=True, help="Search through logs.")
@click.option("-s",
              "--show",
              is_flag=True,
              help="Show information about the logs.")
@click.option("-p", "--pathdir", is_flag=True, help="Show log directory.")
@click.option("-c", "--clear", is_flag=True, help="Reset log settings.")
@click.option("-r", "--reset", is_flag=True, help="Reset log settings.")
@click.option("-l",
              "--level",
              type=click.Choice(LevelType.__args__, case_sensitive=False),
              help="Set log level.")
@click.option("-t", "--stack", is_flag=True, help="Show stack.")
@click.option("-v", "--verbose", is_flag=True, help="Show verbose output.")
@click.option("-d", "--debug", is_flag=True, help="Show debug output.")
@click.option("-q", "--quiet", is_flag=True, help="Show only errors.")
@click.option("-e", "--error", is_flag=True, help="Show only errors.")
@click.option("-w", "--warning", is_flag=True, help="Show only warnings.")
@click.option("-i", "--info", is_flag=True, help="Show only info.")
@click.option("-f", "--fatal", is_flag=True, help="Show only fatal errors.")
@click.option("-L", "--locals", is_flag=True, help="Show locals in traceback.")
@click.help_option("-h", "--help")
@click.pass_context
@click.rich_config(help_config=get_help_config(style_helptext=f"{PINK}",
                                               text_markup="markdown"))
def log(
    ctx: click.Context,
    *args,
    **kwargs,
) -> None:
    """Configure logging settings and search log files."""
    from itertools import chain

    from mbcore.log import (
        ERROR,
        Log,
        get_workspace_config,
        save_workspace_config,
    )

    # If no args provided, display help text
    if not ctx.args and not any(chain(args, kwargs.values())):
        from rich.console import Console

        console = Console()
        console.print("[bold]MB Log Status[/bold]\n")

        # Show current log level
        settings = get_workspace_config()
        current_level = settings.get("level", "INFO")
        console.print(
            f"Current log level: [bold cyan]{current_level}[/bold cyan]")

        # Show log directory
        log_path = settings.get("pathdir", "~/.mb/logs")
        console.print(f"Log directory: [cyan]{log_path}[/cyan]")

        # Show additional settings
        console.print(
            f"Show stack traces: [cyan]{settings.get('show_stack', False)}[/cyan]"
        )
        console.print(
            f"Show locals in traceback: [cyan]{settings.get('show_locals', False)}[/cyan]\n"
        )

        # Show command hint
        console.print(
            "[dim]Use [bold]mb log -h[/bold] for help with commands[/dim]")
        return
    arglist = list(args)
    search: bool = kwargs.get("search", arglist.pop(0) if arglist else False)
    show: bool = kwargs.get("show", arglist.pop(0) if arglist else False)
    pathdir: bool = kwargs.get("pathdir", arglist.pop(0) if arglist else False)
    clear: bool = kwargs.get("clear", arglist.pop(0) if arglist else False)
    reset: bool = kwargs.get("reset", arglist.pop(0) if arglist else False)
    level: LevelType | None = kwargs.get("level",
                                         arglist.pop(0) if arglist else None)
    locals: bool = kwargs.get("locals", arglist.pop(0) if arglist else False)
    third_party: bool = kwargs.get("third_party",
                                   arglist.pop(0) if arglist else False)
    stack: bool = kwargs.get("stack", arglist.pop(0) if arglist else False)
    verbose: bool = kwargs.get("verbose", arglist.pop(0) if arglist else False)
    debug: bool = kwargs.get("debug", arglist.pop(0) if arglist else False)
    quiet: bool = kwargs.get("quiet", arglist.pop(0) if arglist else False)
    error: bool = kwargs.get("error", arglist.pop(0) if arglist else False)
    warning: bool = kwargs.get("warning", arglist.pop(0) if arglist else False)
    info: bool = kwargs.get("info", arglist.pop(0) if arglist else False)
    fatal: bool = kwargs.get("fatal", arglist.pop(0) if arglist else False)
    if reset:
        save_workspace_config()
        setup_logging()
        Log[INFO]("Log settings cleared.")
        return

    if third_party:
        from mbcore.log import setup_traceback

        setup_traceback(show_locals=locals)

    from datetime import datetime
    from pathlib import Path

    from mbcore.display import confirm

    # Load existing settings
    settings = get_workspace_config()
    log_path = get_workspace_config()["pathdir"]

    if pathdir:
        # Import link_fp from _traceback
        from rich.console import Console

        from mbcore._traceback import link_fp

        console = Console()

        # Collect all log files and sort them by modification time
        log_files = []
        for p in log_path.rglob("**/*.log"):
            modifed = p.stat().st_mtime
            log_files.append((p, modifed))

        # Sort by modification time (oldest first)
        log_files.sort(key=lambda x: x[1])

        # Display sorted files with clickable links
        for p, modifed in log_files:
            now = datetime.now()
            delta = now - datetime.fromtimestamp(modifed)
            days = delta.days
            hours = delta.seconds // 3600
            minutes = (delta.seconds % 3600) // 60

            # Create human-readable time string
            if days > 0:
                human_readable = f"{days}d {hours}h ago"
            elif hours > 0:
                human_readable = f"{hours}h {minutes}m ago"
            else:
                human_readable = f"{minutes}m ago"

            # Format date as a clickable link to the log file
            date_str = datetime.fromtimestamp(modifed).strftime("%m-%d")

            # Display path first
            rel_path = f"~/{p.relative_to(Path.home())}"
            console.print(f"{rel_path} modified: ", end="")

            # Then display clickable date with correct link_fp parameters
            console.print(link_fp(date_str, str(p), 1, showpath=False), end="")

            # Finally display time ago
            console.print(f", {human_readable}")

        return

    if clear:
        save_workspace_config()
        setup_logging(show_locals=locals, ignore_third_party=not third_party)

        if confirm(f"Delete log directory: {log_path}?", default=False):
            # Ensure we're deleting the right directory and all contents
            log_root = log_path
            if not isinstance(log_root, Path):
                log_root = Path(log_root)

            # Make sure the path exists and is a directory before attempting deletion
            if log_root.exists() and log_root.is_dir():
                try:
                    import shutil

                    shutil.rmtree(log_root, ignore_errors=True)
                    # Create empty directory to ensure new logs have somewhere to go
                    log_root.mkdir(parents=True, exist_ok=True)
                    safe_print("Log directory cleared successfully.")
                except Exception as e:
                    safe_print(f"Error clearing logs: {e}")
            else:
                safe_print(
                    f"Log directory {log_root} not found or not a directory.")

        Log[INFO]("Log settings cleared.")
        return

    # Update settings
    if level:
        settings["level"] = level
    elif verbose:
        settings["level"] = "verbose"
    elif debug:
        settings["level"] = "debug"
    elif quiet or error:
        settings["level"] = "error"
    elif warning:
        settings["level"] = "warning"
    elif info:
        settings["level"] = "info"
    elif fatal:
        settings["level"] = "fatal"
    if locals:
        settings["show_locals"] = locals
    if stack:
        settings["show_stack"] = stack

    # Save settings
    save_workspace_config(settings, workspace=False)

    # Apply settings
    if "level" in settings:
        Log[settings["level"]].set()

    if "show_locals" in settings:
        setup_logging(show_locals=settings["show_locals"])

    if search:
        import re
        from datetime import datetime

        from rich.console import Console

        from mbcore._traceback import link_fp
        from mbcore.display import getspinner

        console = Console()
        getspinner().stop()

        # Get the logs directory instead of just the current log file
        log_dir: Path = Path.home() / ".mb" / "logs"
        if not log_dir.exists():
            Log[ERROR].log("No logs directory found")
            return

        try:
            # Get the search query from ctx.args
            query = " ".join(map(str, ctx.args))

            if not query.strip():
                Log[ERROR].log("Please provide a search query")
                return

            # Extract filtering options from query
            level_match = re.search(
                r"(VERBOSE|DEBUG|INFO|WARNING|ERROR|FATAL|verbose|debug|info|warning|error|fatal)",
                query,
            )
            start_time_match = re.search(r"start=(\d{2}:\d{2}:\d{2})", query)
            end_time_match = re.search(r"end=(\d{2}:\d{2}:\d{2})", query)
            context_lines_match = re.search(r"ctx=(\d+)", query)
            max_results_match = re.search(r"n=(\d+)", query)
            include_match = re.search(r"include=([\w/.-]+)", query)
            exclude_match = re.search(r"exclude=([\w/.-]+)", query)

            # Parse filtering options
            level_filter = level_match.group(1) if level_match else None
            start_time = datetime.strptime(
                start_time_match.group(1),
                "%H:%M:%S") if start_time_match else None
            end_time = datetime.strptime(
                end_time_match.group(1),
                "%H:%M:%S") if end_time_match else None
            context_lines = int(
                context_lines_match.group(1)) if context_lines_match else 2
            max_results = int(
                max_results_match.group(1)) if max_results_match else None
            include_pattern = include_match.group(1) if include_match else None
            exclude_pattern = exclude_match.group(1) if exclude_match else None

            # Print diagnostic info
            console.print(
                f"[dim]Searching for [bold]{query}[/bold] in logs directory: {log_dir}[/dim]"
            )
            if level_filter:
                console.print(
                    f"[dim]Filtering by level: [bold]{level_filter}[/bold][/dim]"
                )
            if start_time:
                console.print(
                    f"[dim]From time: [bold]{start_time.strftime('%H:%M:%S')}[/bold][/dim]"
                )
            if end_time:
                console.print(
                    f"[dim]To time: [bold]{end_time.strftime('%H:%M:%S')}[/bold][/dim]"
                )
            if include_pattern:
                console.print(
                    f"[dim]Including files matching: [bold]{include_pattern}[/bold][/dim]"
                )
            if exclude_pattern:
                console.print(
                    f"[dim]Excluding files matching: [bold]{exclude_pattern}[/bold][/dim]"
                )

            # Create clean search pattern (without the filter options)
            clean_query = query
            if level_match:
                clean_query = clean_query.replace(level_match.group(0),
                                                  "").strip()
            if start_time_match:
                clean_query = clean_query.replace(start_time_match.group(0),
                                                  "").strip()
            if end_time_match:
                clean_query = clean_query.replace(end_time_match.group(0),
                                                  "").strip()
            if context_lines_match:
                clean_query = clean_query.replace(context_lines_match.group(0),
                                                  "").strip()
            if max_results_match:
                clean_query = clean_query.replace(max_results_match.group(0),
                                                  "").strip()
            if include_match:
                clean_query = clean_query.replace(include_match.group(0),
                                                  "").strip()
            if exclude_match:
                clean_query = clean_query.replace(exclude_match.group(0),
                                                  "").strip()

            # If all options were stripped out, make sure we have a valid search term
            if not clean_query.strip():
                clean_query = query

            # Search across all log files
            all_results = []

            # Find all log files in the logs directory
            log_files = list(log_dir.rglob("**/*.log"))

            # Apply file path filters
            if include_pattern:
                log_files = [
                    f for f in log_files
                    if re.search(include_pattern, str(f), re.IGNORECASE)
                ]
            if exclude_pattern:
                log_files = [
                    f for f in log_files
                    if not re.search(exclude_pattern, str(f), re.IGNORECASE)
                ]

            if not log_files:
                Log[ERROR].log("No matching log files found")
                return

            console.print(
                f"[dim]Found {len(log_files)} log files to search[/dim]")

            # Simple direct search through files
            for log_file in log_files:
                try:
                    # Simple text-based search
                    with open(log_file) as f:
                        lines = f.readlines()

                    # For context tracking
                    context_buffer = []
                    matches = []

                    for i, line in enumerate(lines):
                        # Extract timestamp from line if present
                        timestamp_match = re.search(r"\[(\d{2}:\d{2}:\d{2})\]",
                                                    line)
                        line_time = None
                        if timestamp_match:
                            try:
                                line_time = datetime.strptime(
                                    timestamp_match.group(1), "%H:%M:%S")
                            except ValueError:
                                pass

                        # Apply time filters
                        if start_time and line_time and line_time < start_time:
                            # Add to context but skip for direct match
                            context_buffer.append((i, line))
                            if len(context_buffer) > context_lines:
                                context_buffer.pop(0)
                            continue

                        if end_time and line_time and line_time > end_time:
                            # Add to context but skip for direct match
                            context_buffer.append((i, line))
                            if len(context_buffer) > context_lines:
                                context_buffer.pop(0)
                            continue

                        # Apply level filter
                        if level_filter:
                            level_in_line = re.search(
                                r"(VERBOSE|DEBUG|INFO|WARNING|ERROR|FATAL)",
                                line)
                            if not level_in_line or level_in_line.group(
                                    1).lower() != level_filter.lower():
                                # Add to context but skip for direct match
                                context_buffer.append((i, line))
                                if len(context_buffer) > context_lines:
                                    context_buffer.pop(0)
                                continue

                        # Check for match
                        if re.search(clean_query, line, re.IGNORECASE):
                            # Get context lines before
                            context_before = []
                            for ctx_i, ctx_line in context_buffer:
                                context_before.append(
                                    {
                                        "file": log_file,
                                        "line": ctx_i + 1,
                                        "content": ctx_line.strip(),
                                        "is_context": True,
                                    }, )

                            # Add the match
                            matches.append(
                                {
                                    "file": log_file,
                                    "line": i + 1,
                                    "content": line.strip(),
                                    "is_match": True,
                                    "context_before": context_before,
                                }, )

                            # Reset context buffer for next match
                            context_buffer = []
                        else:
                            # Not a match, add to context buffer
                            context_buffer.append((i, line))
                            if len(context_buffer) > context_lines:
                                context_buffer.pop(0)

                    # Add context after matches
                    for j, match in enumerate(matches):
                        match_line = match["line"]
                        context_after = []

                        # Look for following matches to find context length
                        next_match_idx = match_line + context_lines
                        if j < len(matches) - 1:
                            next_match_idx = min(next_match_idx,
                                                 matches[j + 1]["line"] - 1)

                        # Get context lines after
                        for k in range(
                                match_line,
                                min(match_line + context_lines, len(lines))):
                            if k < len(lines):
                                context_after.append(
                                    {
                                        "file":
                                        log_file,
                                        "line":
                                        k + 1,
                                        "content":
                                        lines[k].strip()
                                        if k < len(lines) else "",
                                        "is_context":
                                        True,
                                    }, )

                        match["context_after"] = context_after

                    if matches:
                        all_results.extend(matches)

                        # Stop if we hit the max results limit
                        if max_results and len(all_results) >= max_results:
                            console.print(
                                f"[dim]Reached maximum results limit ({max_results})[/dim]"
                            )
                            break

                except Exception as e:
                    # Skip files that cause errors
                    console.print(
                        f"[dim]Error processing {log_file}: {e}[/dim]")
                    continue

            if not all_results:
                Log[ERROR].log("No matches found in logs")
                return

            # Print results with clickable links
            console.print(f"[bold]Search results for:[/bold] {clean_query}")
            console.print(f"[dim]Found {len(all_results)} matches[/dim]")

            # Sort by filename
            all_results.sort(
                key=lambda x: (str(x.get("file")), x.get("line", 0)))

            # Show results by file
            current_file = None
            for result in all_results:
                filepath = result.get("file")
                line_number = result.get("line", 1)
                line_content = result.get("content", "").strip()
                is_match = result.get("is_match", True)
                is_context = result.get("is_context", False)

                if filepath and line_content:
                    # If new file, print header
                    if current_file != filepath:
                        current_file = filepath
                        rel_path = f"~/{filepath.relative_to(Path.home())}"
                        console.print(f"\n[bold cyan]{rel_path}:[/bold cyan]")

                    # Create clickable link to file and line
                    clickable_file = link_fp(f"Line {line_number}",
                                             str(filepath),
                                             line_number,
                                             showpath=False)

                    # Format the line content with appropriate styling
                    if is_match:
                        # Main match line gets bold formatting
                        console.print(
                            f"  {clickable_file} - [bold]{line_content}[/bold]"
                        )
                    elif is_context:
                        # Context lines get dim formatting
                        console.print(
                            f"  {clickable_file} - [dim]{line_content}[/dim]")
                    else:
                        console.print(f"  {clickable_file} - {line_content}")

                    # Show context lines if present
                    if is_match:
                        # Show context before
                        for ctx in result.get("context_before", []):
                            ctx_line = ctx.get("line", 1)
                            ctx_content = ctx.get("content", "").strip()
                            ctx_link = link_fp(f"Line {ctx_line}",
                                               str(filepath),
                                               ctx_line,
                                               showpath=False)
                            console.print(
                                f"      {ctx_link} - [dim]{ctx_content}[/dim]")

                        # Show context after
                        for ctx in result.get("context_after", []):
                            ctx_line = ctx.get("line", 1)
                            ctx_content = ctx.get("content", "").strip()
                            ctx_link = link_fp(f"Line {ctx_line}",
                                               str(filepath),
                                               ctx_line,
                                               showpath=False)
                            console.print(
                                f"      {ctx_link} - [dim]{ctx_content}[/dim]")

        except Exception as e:
            import traceback

            # Just print the stack trace
            traceback.print_exc()
            # Use positional argument for the error message
            Log[ERROR].log(f"Error searching logs: {e}")
        return

    return


# _main.add_command(cache)
# _main.add_command(log)

# def main() -> None:
#     _main()

# if __name__ == "__main__":
# main()
