import importlib
import os
import subprocess
import sys

import rich_click as click

TYPE_CHECKING = False

if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing_extensions import (
        ParamSpec,
        TypeVar,
        Callable,
        Literal,
        overload,
        Any,
        cast,
        Generic,
    )

    T = TypeVar("T")
    P = ParamSpec("P")
    from mbcore.types import wrapafter
    from mbcore.import_utils import smart_import
    from mbcore.proto import Is
    from rich_click import (
        RichContext,
        RichGroup,
        RichHelpConfiguration,
        RichCommandCollection,
    )
    from rich_click.utils import CommandGroupDict, OptionGroupDict
    from rich_click.rich_help_formatter import RichHelpFormatter
    from rich.console import Console
    from mbcore.more import filter
else:

    def wrapafter(*args, **kwargs):
        return lambda x: x

    class obj:

        def __init__(self, *args, **kwargs):
            pass

        def __call__(self, *args, **kwargs):
            return self

        @classmethod
        def __class_getitem__(cls, *args, **kwargs):
            return cls

        def __getitem__(self, *args, **kwargs):
            return self

        def __iter__(self):
            return self

        def __next__(self):
            return self

    Path = object
    smart_import = object
    Is = object
    RichHelpConfiguration = object
    RichContext = object

    Dependency = object
    afind_toml = object

    Path = object
    smart_import = wrapafter
    overload = wrapafter
    TypeVar = ParamSpec = obj
    cast = obj()
    Any = object
    Generic = obj
    Callable = type(tuple[int, ...].__origin__)

_initial_missing = object()


def reduce(
    function: Callable[[Any, Any], Any],
    sequence: "Iterable[Any]",
    initial=_initial_missing,
) -> Any:
    """
    reduce(function, iterable[, initial]) -> value

    Apply a function of two arguments cumulatively to the items of a sequence
    or iterable, from left to right, so as to reduce the iterable to a single
    value.  For example, reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]) calculates
    ((((1+2)+3)+4)+5).  If initial is present, it is placed before the items
    of the iterable in the calculation, and serves as a default when the
    iterable is empty.
    """

    it = iter(sequence)

    if initial is _initial_missing:
        try:
            value = next(it)
        except StopIteration:
            raise TypeError(
                "reduce() of empty iterable with no initial value") from None
    else:
        value = initial

    for element in it:
        value = function(value, element)

    return value


try:
    from _functools import reduce
except ImportError:
    pass

R = TypeVar("R")
P = ParamSpec("P")
_T = TypeVar("_T")
_R = TypeVar("_R")
_S = TypeVar("_S")


def has_failure(line: str) -> bool:
    line = str(getattr(line, "error", line))
    return (line.lower().strip().startswith("error")
            or "failed" in line.lower() or "error" in line.lower()
            or "fatal" in line.lower() or "ERROR" in line)


async def check_install_prompt(
    program: str,
    unix: str | None = None,
    windows: str | None = None,
    linux: str | None = None,
    mac: str | None = None,
    no_prompt: bool = False,
    no_pypi: bool = False,
    python: bool = False,
) -> bool:
    """Check if a program is installed and prompt to install it if not."""
    if not TYPE_CHECKING:
        from mbcore.import_utils import smart_import

        os = smart_import("os")
        confirm = smart_import("mbcore.display.confirm")
        arun = smart_import("mbpy.cmd.arun")
        get_package_info = smart_import("mbpy.pkg.pypi.get_package_info")
        getexecutable = smart_import("mbpy.env.getexecutable")
    else:
        import os

        from mbcore.display import confirm

        from mbpy.cmd import arun
        from mbpy.env import getexecutable
        from mbpy.pkg.pypi import get_package_info
    try:
        lib = importlib.import_module(program)
        if lib:
            return True
    except Exception:
        pass
    # Sanitize program name
    program = str(program).strip()
    if not program:
        return False

    # Determine installation command
    cmd = None
    match os.name:
        case "posix":
            cmd = unix
        case "nt":
            cmd = windows
        case "linux":
            cmd = linux
        case "darwin":
            cmd = mac

    # Default to pip if no specific command provided
    if not any([unix, windows, linux, mac]) and not no_pypi:
        python = True

    if python:
        cmd = f"{getexecutable()} -m pip install {program}"
        try:
            check_result = await arun(
                f"{getexecutable()} -m pip show {program}", show=False)
            if "warning" in check_result.lower():
                if no_prompt or not confirm(
                        f"{program} is not installed. Install now?"):
                    return False
                await arun(cmd)

            try:
                return bool(smart_import(program, "reload"))
            except (
                    ImportError,
                    ModuleNotFoundError,
                    ValueError,
                    AttributeError,
                    NameError,
            ):
                if program == "scikit-learn":
                    return bool(smart_import("scipy", "reload"))
                pkg_info = await get_package_info(program)
                if not pkg_info:
                    return False
                return bool(smart_import(pkg_info["name"], "reload"))
        except Exception:
            return False

    try:
        found = await arun(f"which {program}")
        if not found:
            if no_prompt or not confirm(
                    f"{program} is not installed. Install now?"):
                return False
            if not cmd:
                return False
            result = await arun(cmd)
            return not has_failure(result)
        return True
    except Exception:
        return False


def get_similar_commands(name: str, cli: "RichGroup") -> str | None:
    """Command name auto-correct."""
    from difflib import get_close_matches

    name = name.lower()

    close_commands = get_close_matches(name, cli.commands)

    if close_commands:
        return close_commands[0]

    return None


def source_content(source_target: str,
                   shell: 'Literal["bash", "zsh", "fish"]'):
    if shell == "zsh":
        return f"""autoload -Uz compinit && compinit
zstyle ':completion:*' menu select
source {source_target}
zstyle ':completion:*:*:mb:*' file-patterns '*:files' '*(/):directories'
"""
    elif shell == "bash":
        return f"source {source_target}\n"
    else:  # Should not happen due to outer check, but keeps linter happy
        return ""


def source_block(source_target: str, shell: 'Literal["bash", "zsh", "fish"]'):
    source_line_content = source_content(source_target, shell)
    return f"""
# mb completion start
{source_line_content}# mb completion end"""


COMPLETION_SCRIPTS = {
    "bash": ("_MB_COMPLETE", "bash_source", "~/.bashrc", "bash"),
    "zsh": ("_MB_COMPLETE", "zsh_source", "~/.zshrc", "zsh"),
    "fish": (
        "_MB_COMPLETE",
        "fish_source",
        "~/.config/fish/completions/mb.fish",
        "fish",
    ),
}


def setup_completion(shell: "Literal['bash', 'zsh', 'fish']",
                     add_to_rc: bool = False) -> None:
    """Generate and setup shell completion for mb CLI."""  # noqa: D401
    from pathlib import Path
    from mbcore.display import safe_print
    from mbcore.log import error, warning, debug

    # Import main here to ensure subcommands are registered when the subprocess runs
    # This import needs to happen in the *parent* process before launching the child
    try:
        import mbpy.main
    except ImportError as e:
        error(f"Failed to import mbpy.main, cannot generate completions: {e}")
        return

    config_dir = Path.home() / ".mb" / "config"
    config_dir.mkdir(parents=True, exist_ok=True)

    if shell not in COMPLETION_SCRIPTS:
        error(f"Unsupported shell for completion: {shell}")
        return

    env_var, source_type, rc_file, suffix = COMPLETION_SCRIPTS[shell]

    # Fish convention is different for the filename vs the source file path
    if shell == "fish":
        # Fish completions usually go directly into a specific directory with a .fish suffix
        completion_file = Path(rc_file).expanduser()
        completion_file.parent.mkdir(
            parents=True, exist_ok=True)  # Ensure completions dir exists
    else:
        # Bash/Zsh: place script in our config dir
        completion_file = config_dir / f"mb-complete.{suffix}"

    # Prepare environment for subprocess
    completion_env = os.environ.copy()
    completion_env[env_var] = source_type

    # Determine the command to run - try 'mb' first, fallback to python -m
    mb_command = ["mb"]
    try:
        # Check if 'mb' exists (just check if it's in the path)
        which_process = subprocess.run(
            ["which", mb_command[0]]
            if sys.platform != "win32" else ["where", mb_command[0]],
            check=True,
            capture_output=True,
            text=True,
        )
        if which_process.stdout.strip():
            debug(f"Found '{mb_command[0]}' at {which_process.stdout.strip()}")
        else:
            raise FileNotFoundError(f"Command '{mb_command[0]}' not found")

    except (FileNotFoundError, subprocess.CalledProcessError):
        warning(
            f"Command '{mb_command[0]}' not found. Falling back to 'python -m mbpy'."
        )
        # Find the python executable that's running *this* script
        python_executable = sys.executable
        if not python_executable:
            error(
                "Could not determine Python executable path. Cannot generate completions via module."
            )
            return
        # Assuming mbpy/main.py is the entry point when running as a module
        mb_command = [python_executable, "-m", "mbpy.main"]
        debug(f"Using '{' '.join(mb_command)}' for completion generation.")

    debug(f"Generating completion script for {shell}...")
    debug(f"  Command: {' '.join(mb_command)}")
    debug(f"  Environment: {env_var}={source_type}")
    debug(f"  Output file: {completion_file}")

    # Generate completion script using subprocess
    try:
        result = subprocess.run(
            mb_command,
            env=completion_env,
            capture_output=True,
            text=True,
            check=True,  # Raise exception on non-zero exit code
        )

        # Write the captured stdout (the completion script) to the file
        # For Zsh, inject custom path completion logic for specific commands
        if shell == "zsh":
            # Original script from Click
            original_script = result.stdout

            # Check if the script already contains our custom code
            if ("Check if we're in a command that should fall back to path completion"
                    in original_script):
                debug(
                    "Completion script already contains our custom path completion logic"
                )
                completion_file.write_text(original_script)
            else:
                # Add our custom path completion logic for mb add, mb remove, mb git add
                # First, remove any existing variable declarations we'll be adding
                enhanced_script = original_script.replace(
                    "local -a completions\n    local -a completions_with_descriptions\n    local -a response",
                    "# Variables will be declared in our custom block",
                )

                # Add our custom path completion logic
                enhanced_script = enhanced_script.replace(
                    "_mb_completion() {",
                    """_mb_completion() {
    local -a completions
    local -a completions_with_descriptions
    local -a response
    
    # Check if we're in a command that should fall back to path completion
    local current_command="${words[1]}"
    local second_command="${words[2]:-}"
    local third_command="${words[3]:-}"
    local cmd_needs_files=0
    local mb_cmd="mb"
    
    # Fall back to python -m mbpy if mb command isn't found
    if ! command -v mb &> /dev/null; then
        mb_cmd="python -m mbpy"
    fi
    
    # Check for commands that should do path completion
    if [[ "$current_command" == "mb" ]]; then
        if [[ "$second_command" == "add" || "$second_command" == "remove" ]]; then
            # mb add/remove should fall back to path completion
            cmd_needs_files=1
        elif [[ "$second_command" == "git" && "$third_command" == "add" ]]; then
            # mb git add should fall back to path completion
            cmd_needs_files=1
        fi
    fi""",
                )

                # Also update the actual command execution to use the variable instead of hardcoded 'mb'
                enhanced_script = enhanced_script.replace(
                    'response=("${(@f)$(env COMP_WORDS="${words[*]}" COMP_CWORD=$((CURRENT-1)) _MB_COMPLETE=zsh_complete mb)}")',
                    'response=("${(@f)$(env COMP_WORDS="${words[*]}" COMP_CWORD=$((CURRENT-1)) _MB_COMPLETE=zsh_complete $mb_cmd)}")',
                )

                # Remove the check for mb command that causes early return
                enhanced_script = enhanced_script.replace(
                    "(( ! $+commands[mb] )) && return 1",
                    "# Using dynamic command: $mb_cmd",
                )

                # Make sure we don't add duplicate fallback code by removing any existing fallback
                if "Fall back to path completion for empty results" in enhanced_script:
                    debug(
                        "Script already has fallback code, not adding duplicate fallback"
                    )
                else:
                    # Add fallback section at the end of the function, carefully making sure
                    # we don't break the function structure
                    if 'if [ -n "$completions" ]; then' in enhanced_script:
                        # Find the last closing brace and add our fallback before it
                        last_brace_pos = enhanced_script.rfind("}")
                        if last_brace_pos > 0:
                            # Insert our fallback code just before the last closing brace
                            enhanced_script = (
                                enhanced_script[:last_brace_pos] + """
    # Fall back to path completion for empty results on relevant commands
    if [[ ${#completions} -eq 0 && ${#completions_with_descriptions} -eq 0 && $cmd_needs_files -eq 1 ]]; then
        _path_files
    fi
""" + enhanced_script[last_brace_pos:])

                # Only replace the script with our enhanced version for Zsh
                completion_file.write_text(enhanced_script)
        else:
            # For other shells, write the original script
            completion_file.write_text(result.stdout)

        debug(f"Successfully wrote completion script to {completion_file}")

    except subprocess.CalledProcessError as e:
        error(f"Error generating completion script for '{shell}':")
        error(f"  Command: {' '.join(mb_command)}")
        error(f"  Exit code: {e.returncode}")
        error(f"  Stderr: {e.stderr.strip()}")
        if e.stdout:  # Show stdout too if it contains anything useful
            error(f"  Stdout: {e.stdout.strip()}")
        return  # Stop execution
    except FileNotFoundError:
        error(f"Error: The command '{mb_command[0]}' was not found.")
        error(
            "Please ensure 'mb' (or the Python executable) is installed and in your PATH."
        )
        return  # Stop execution
    except Exception as e:
        error(
            f"An unexpected error occurred during completion script generation: {str(e)}"
        )
        # Consider adding traceback here if debug is enabled
        return  # Stop execution

    # Add source line to RC file (if requested and not fish)
    if add_to_rc and shell != "fish":
        rc_path = Path(rc_file).expanduser()
        source_target = (
            completion_file  # For bash/zsh, we source the file in .mb/config
        )

        # Define the source block for bash/zsh
        if shell == "zsh":
            # Use a multi-line triple-quoted string with actual newlines instead of escaped \n
            source_line_content = source_content(source_target, shell)

        try:
            if rc_path.exists():
                text = rc_path.read_text()
                start_marker = "# mb completion start"
                end_marker = "# mb completion end"

                if start_marker in text:
                    # Remove existing blocks with a more robust approach
                    import re

                    # First, try to clean up any malformed blocks with literal \n characters
                    text = text.replace("\\n", "\n")

                    # Use a more specific pattern to match blocks (including the markers)
                    pattern = re.compile(
                        f"{re.escape(start_marker)}.*?{re.escape(end_marker)}",
                        re.DOTALL,
                    )

                    # Replace all matches (could be multiple blocks) with empty string
                    text = pattern.sub("", text)

                    # Also remove any consecutive newlines (more than 2)
                    text = re.sub(r"\n{3,}", "\n\n", text)

                # Append new block
                with rc_path.open("w") as f:  # Use 'w' to write from scratch
                    # End with a newline
                    if text and not text.endswith("\n"):
                        text = text + "\n"

                    # Ensure there's at most one blank line before our block
                    text = text.rstrip() + "\n\n"

                    # Write the cleaned file plus our new block
                    f.write(text + source_block.strip() + "\n")

                safe_print(f"Updated completion setup in {rc_path}")
            else:
                warning(
                    f"{rc_path} not found. Creating it and adding completion setup."
                )
                with rc_path.open("w") as f:
                    f.write(source_block.strip() + "\n")
                safe_print(f"Created {rc_path} and added completion setup.")

        except IOError as e:
            error(f"Error updating {rc_path}: {e}")
            safe_print(
                "\nPlease manually add the following block to your RC file:")
            safe_print(source_block)
        except Exception as e:
            error(
                f"An unexpected error occurred while updating {rc_path}: {e}")

    safe_print(f"Completion script generated successfully for {shell}.")
    if shell == "fish":
        safe_print(f"  Script installed at: {completion_file}")
        safe_print(
            "  Fish should pick it up automatically. Restart your shell if needed."
        )
    elif not add_to_rc:
        safe_print(
            "\nTo enable completion, add the following block to your RC file ({rc_file}):"
        )
        safe_print(source_block)
    elif add_to_rc:
        safe_print(
            f"  Run 'source {rc_path}' or restart your shell to apply changes."
        )


@click.command()
@click.argument("shell",
                type=click.Choice(["bash", "zsh", "fish"]),
                required=False)
@click.option("--zsh", is_flag=True, help="Shell to generate completion for")
@click.option("--bash", is_flag=True, help="Shell to generate completion for")
@click.option("--fish", is_flag=True, help="Shell to generate completion for")
@click.option(
    "--add-to-rc/--no-add-to-rc",
    default=True,
    help="Whether to add source command to shell rc file",
)
@click.option("--reload/--no-reload",
              default=True,
              help="Reload shell configuration after setup")
def completion(
    shell: 'Literal["bash", "zsh", "fish"] | None' = None,
    zsh: bool = False,
    bash: bool = False,
    fish: bool = False,
    add_to_rc: bool = True,
    reload: bool = True,
) -> None:
    """Generate shell completion script for mbpy CLI.

    For best results with ZSH, use: mbpy completion --shell=zsh --add-to-rc
    Then restart your shell or run: source ~/.zshrc

    If file completion doesn't work, manually add to ~/.zshrc:
    zstyle ':completion:*:*:mbpy:*:*' file-patterns '*'
    """
    # Import Path here to ensure it's not the placeholder object
    from pathlib import Path

    shell = shell or ("zsh"
                      if zsh else "bash" if bash else "fish" if fish else None)
    if shell is None:
        raise click.ClickException(
            "No shell provided. Use --zsh, --bash, or --fish.")
    setup_completion(shell, add_to_rc)

    # Optional: remind user to reload
    if reload and add_to_rc and shell != "fish":
        _, _, rc_file, _ = COMPLETION_SCRIPTS[shell]
        # Correctly use the expanded rc_file path here
        click.echo(
            f"\nTo apply changes, run: source {Path(rc_file).expanduser()}")
    elif reload and shell == "fish":
        click.echo("\nRestart your fish shell for completions to take effect.")


command_groups = {
    "PACKAGE": [
        "install/add",
        "uninstall/remove",
        "list/show",
        "search",
        "upload",
        "publish",
    ],
    "DEVELOP": ["build", "clean", "log", "git", "sync", "undo", "docs"],
    "ANALYZE": ["graph", "run", "time", "log"],
}

option_groups = dict(
    name="GLOBAL",
    options=[
        "--debug",
        "--env",
        "--no-third-party",
        "--verbose",
        "--quiet",
        "--vverbose",
    ],
)


class AsyncCommand(click.Command):
    """Custom Click Command that supports asynchronous command callbacks."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def invoke(self, ctx: click.RichContext, *args, **kwargs) -> Any:
        """Override the invoke method to handle async commands."""

        from mbcore.display import getspinner, safe_print
        from mbcore.execute import run_async
        from mbcore.log import debug

        try:
            coro = super().invoke(ctx)
            if hasattr(coro, "__await__"):
                return run_async(coro)
            return coro
        except Exception as e:
            if debug():
                import traceback

                traceback.print_exc()
            if isinstance(e, click.ClickException):
                if str(e).strip() and "No such command" not in str(e):
                    safe_print(f"Error: {e}")
                    return ctx
            if "-h" not in ctx.args and "--help" not in ctx.args:
                getspinner().start()


def identity(ctx: click.RichContext, *args, **kwargs) -> Any:
    """Identity function."""
    return ctx


class AsyncGroup(click.RichGroup):
    """Custom Click Group that supports asynchronous command callbacks."""

    def __call__(self, *args, **kwargs):

        c = super().__call__(*args, **kwargs)

        return c

    def invoke(self, ctx: click.RichContext, *args, **kwargs) -> Any:
        """Override the invoke method to handle async commands."""
        coro = super().invoke(ctx)
        from mbcore.execute import run_async

        if hasattr(coro, "__await__"):
            return run_async(coro)
        return coro


@wrapafter(RichHelpConfiguration, returns=RichHelpConfiguration)
def get_help_config(*args, **kwargs):
    from mbpy.style import RichHelpConfig

    return RichHelpConfig(*args, **kwargs)


@overload
def compose(f: Callable[[_T], _R], g: Callable[[_S], _T],
            /) -> Callable[[_S], _R]:
    ...


@overload
def compose(*fs: Callable[..., Any]) -> Callable[..., Any]:
    ...


def compose(*fs: Callable[..., Any]) -> Callable[..., Any]:
    """Composes passed functions.

    Examples:
        >>> inc = lambda x: x + 1
        >>> double = lambda x: x * 2
        >>> inc_then_double = compose(double, inc)
        >>> inc_then_double(3)  # (3 + 1) * 2
        8

    """
    if fs:

        def pair(f: Callable[..., Any], g: Callable[..., Any]):
            return lambda *a, **kw: f(g(*a, **kw))

        return reduce(pair, fs)
    return identity


@overload
def base_args(
        func: "Callable[P, Any]|None" = None) -> "Callable[P, click.Command]":
    ...


@overload
def base_args(
    env: bool = True,
    debug: bool = True,
    help: bool = True,
    no_third_party: bool = True,
) -> "Callable[[Callable[P, Any]], Callable[P, click.Command]]":
    ...


def base_args(
    *args: bool | Callable[P, Any] | None,
    **kwargs: Any,
) -> Any:
    """Apply base arguments to a command."""
    a0, *rest = args

    if len(args) == 1 and callable(a0):
        return _apply_base_args(a0,
                                env=True,
                                debug=True,
                                help=True,
                                no_third_party=True)
    return _apply_base_args(cast(CallableCommand[P, Any], a0),
                            *filter(Is[bool], rest), **kwargs)


class CallableCommand(click.RichCommand, Generic[P, R]):

    def __call__(self, *args, **kwargs):
        return super().__call__(*args, **kwargs)


def _apply_base_args(
    func: "CallableCommand[P, Any] | Any",
    env: bool = True,
    debug: bool = True,
    help: bool = True,  # noqa
    no_third_party: bool = True,
) -> "Callable[P, click.Command]":
    """Apply Click options with signature safety."""

    from inspect import signature

    existing_params = set(signature(func).parameters.keys())

    if hasattr(func, "params"):
        existing_params = set(existing_params) | set(
            tuple([q for p in func.params for q in p.opts]))
    wrapper = ()

    def add_option_if_missing(name: str, option: Callable):
        nonlocal wrapper
        wrapper += (option, )

    if env:
        add_option_if_missing(
            "env",
            click.option(
                "-E",
                "--env",
                default=None,
                required=False,
                help="Specify the python, hatch, conda, or mb environment",
            ),
        )

    if debug:
        add_option_if_missing(
            "debug",
            click.option(
                "-d",
                "--debug",
                is_flag=True,
                required=False,
                help="Enable debug logging",
            ),
        )
        add_option_if_missing(
            "verbose",
            click.option(
                "-v",
                "--verbose",
                is_flag=True,
                required=False,
                help="Enable verbose logging",
                hidden=True,
            ),
        )
        add_option_if_missing(
            "quiet",
            click.option(
                "-q",
                "--quiet",
                is_flag=True,
                required=False,
                help="Disable logging",
                hidden=True,
            ),
        )
        add_option_if_missing(
            "vverbose",
            click.option(
                "-vv",
                "--vverbose",
                is_flag=True,
                required=False,
                help="Enable trace logging",
                hidden=True,
            ),
        )

    if no_third_party:
        add_option_if_missing(
            "no_third_party",
            click.option(
                "-nt",
                "--no-third-party",
                is_flag=True,
                required=False,
                help="Disable third-party traceback in errors",
            ),
        )

    if help:
        add_option_if_missing("help",
                              click.help_option("-h", "--help", is_flag=True))

    return compose(*wrapper)(func)


@click.group(cls=AsyncGroup )
@click.rich_config(help_config=get_help_config())
@click.pass_context
@base_args
def cli(
    ctx: RichContext,
    env=None,
    debug=None,
    verbose=None,
    quiet=None,
    vverbose=None,
    no_third_party=None,
    help=None,
) -> None:
    if debug:
        click.echo("Debugging enabled.")


cli.add_command(completion)
cli.allow_extra_args = True
cli.no_args_is_help = True
cli.invoke_without_command = True

if __name__ == "__main__":
    cli()

