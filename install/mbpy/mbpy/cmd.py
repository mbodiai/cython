import asyncio
from pathlib import Path
import sys
from collections.abc import Coroutine, Iterable
from typing import TYPE_CHECKING, Any

from mbcore.import_utils import smart_import
from mbcore.cache import cache, acache

from typing import AsyncGenerator, Generator

from mbpy.expect.asyncspawn import AsyncSpawn
from mbpy.helpers._cmd import Command

if TYPE_CHECKING:
    from mbpy.helpers._cmd import Command
    from mbpy.expect.spawnbase import SpawnBase as Process


def run_command(
    command: str | list[str] | tuple[str, list[str]],
    cwd: str | None = None,
    *,
    show=False,
) -> "Command":
    """Run command and return Command object."""
    from mbpy.helpers._cmd import Command
    from mbcore.more import collapse

    return Command(
        " ".join(collapse([command] if isinstance(command, str) else command, str)),
        cwd=cwd,
        show=show,
    )


async def arun_command(
    command: str | list[str],
    cwd: str | Path | None = None,
    *,
    shell=False,
    show=False,
) -> "AsyncSpawn":
    """Run command and return AsyncCommand object."""
    from mbcore.more import collapse

    from mbpy.expect.asyncspawn import AsyncSpawn

    return AsyncSpawn(
        " ".join(collapse([command], str)), shell=shell, cwd=cwd, show=show
    )


def run(
    command: str | list[str],
    cwd: str | None = None,
    *,
    show=True,
) -> str:
    """Run command and return output as a string."""
    return run_command(command, cwd=cwd, show=show).readtext()


# Cached version of run
@cache(persistent=True, context_policy="site_packages")
def run_cached(
    command: str | list[str],
    cwd: str | None = None,
    *,
    show=True,
) -> str:
    """Cached version of run. Returns output as a string.

    WARNING: Only use for commands with no side effects!
    Uses persistent cache with site-packages context policy.
    """
    # Call the original run function to execute if not cached
    return run(command, cwd=cwd, show=show)


async def arun(cmd: str | list[str], show=True, shell=True, **kwargs) -> str:
    """Run a command asynchronously and return its output."""
    async with await arun_command(cmd, show=show, shell=shell, **kwargs) as p:
        return await p.areadtext()


# Cached version of arun
@acache(persistent=True, context_policy="site_packages")
async def arun_cached(cmd: str | list[str], show=True, shell=True, **kwargs) -> str:
    """Cached version of arun. Returns output as a string.

    WARNING: Only use for commands with no side effects!
    Uses persistent cache with site-packages context policy.
    """
    # Call the original arun function to execute if not cached
    return await arun(cmd, show=show, shell=shell, **kwargs)


# Usage example:


def sigwinch_passthrough(sig, data, p: "Process") -> None:
    """Signal handler for window size change."""
    import struct

    if sys.platform != "win32":
        from fcntl import ioctl

        s = struct.pack("HHHH", 0, 0, 0, 0)
        a = struct.unpack("hhhh", ioctl(s))  # type: ignore
        if not p.closed:
            p.setwinsize(a[0], a[1])  # type: ignore


def contains_exec(cmd: list[str] | str) -> bool:
    """Check if command contains an executable."""
    if not TYPE_CHECKING:
        Path = smart_import("pathlib.Path")  # noqa
        shlex = smart_import("shlex")
    else:
        import shlex
        from pathlib import Path
    if isinstance(cmd, str):
        cmd = shlex.split(cmd)
    return any(Path(i).exists() for i in cmd)


def resolve(cmd: list[str] | str) -> list[str]:
    """Resolve commands to their full path."""
    if not TYPE_CHECKING:
        Path = smart_import("pathlib.Path")  # noqa
    else:
        from pathlib import Path
    cmd = [cmd] if not isinstance(cmd, list) else cmd
    out = []
    for i in cmd:
        if i.startswith("~"):
            out.append(str(Path(i).expanduser().resolve()))
        elif i.startswith("."):
            out.append(str(Path(i).resolve()))
        else:
            out.append(i)
    return out


def run_local(
    cmd: str | list[str],
    *,
    interact=False,
    cwd=None,
    timeout=10,
    show=True,
    **kwargs,
) -> "Generator[str, str, None]":
    """Run command, yield single response, and close."""
    PtyCommand = smart_import("mbpy.helpers._cmd.Command")
    EOF = smart_import("mbpy.helpers._cmd.EOF")
    signal = smart_import("signal")
    console = smart_import("mbcore.display.console")()
    collapse = smart_import("more_itertools").collapse
    partial = smart_import("functools").partial
    Text = smart_import("rich.text").Text
    cast = smart_import("typing").cast
    if interact:
        cmd = " ".join(collapse(cmd, str)) if not isinstance(cmd, str) else cmd
        p = PtyCommand(cmd, cwd=cwd, timeout=timeout, **kwargs)
        signal.signal(signal.SIGWINCH, partial(sigwinch_passthrough, p=p))
        p.process.interact()
        if response := p.process.before:
            response = response.decode() if isinstance(response, bytes) else response
        else:
            return
        response = cast(str, response)
        console = smart_import("mbcore.display.console")()
        console.print(Text.from_ansi(response.decode())) if show else None
        yield response
    else:
        p = PtyCommand(
            " ".join(collapse([cmd], str)), cwd=cwd, timeout=timeout, **kwargs
        )
        p.process.expect(EOF, timeout=10)
        if response := p.process.before:
            response = response.decode() if isinstance(response, bytes) else response
            response = cast(str, response)
            console.print(Text.from_ansi(response)) if show else None
            yield response
        else:
            return
        p.process.close()
    p.process.close() if p else None
    return


def interact(
    cmd: "str | Iterable[str] | tuple[str, list[str]]",
    *,
    cwd: str | None = None,
    timeout: int = 10,
    show: bool = True,
    **kwargs,
) -> "Generator[str, str, None]":
    """Run comand, recieve output and wait for user input.

    Example:
    >>> terminal = commands.interact("Choose an option", choices=[str(i) for i in range(1, len(results) + 1)] + ["q"])
    >>> choice = next(terminal)
    >>> choice.terminal.send("exit")

    """
    collapse = smart_import("more_itertools").collapse
    usr_input = cmd
    repl = run_local(
        cmd,  # type: ignore
        interact=True,
        cwd=cwd,
        timeout=timeout,
        show=show,
        **kwargs,
    )
    msg = next(repl)
    while usr_input not in ("exit", "quit", "q"):
        while (msg := next(repl)) != "EOF":
            yield msg
        usr_input = yield "> "
        msg = repl.send(" ".join(list(*collapse(usr_input))))


async def arun_local(
    cmd: str | list[str],
    *,
    interact=False,
    cwd=None,
    show=True,
    **kwargs,
) -> "AsyncGenerator[str, str]":
    """Run command, yield single response, and close."""
    asyncio = smart_import("asyncio")
    for resp in await asyncio.to_thread(
        run_local,
        cmd,
        interact=interact,
        cwd=cwd,
        show=show,
        **kwargs,
    ):
        yield resp


async def ainteract(
    cmd: str | list[str],
    *,
    cwd: str | None = None,
    show: bool = True,
    **kwargs,
) -> "AsyncGenerator[str, str]":
    """Run comand, recieve output and wait for user input."""
    usr_input = cmd
    repl = arun_local(cmd, interact=True, cwd=cwd, show=show, **kwargs)
    async for msg in repl:
        if msg.strip() == "EOF":
            break
        yield msg
        usr_input = yield "> "
        async for resp in arun_local(
            usr_input, interact=False, cwd=cwd, show=show, **kwargs
        ):
            yield resp


async def aconsume(cmd: Coroutine[Any, Any, Any]):
    async for resp in await cmd:
        print(resp)


async def arun_pip_command(
    command_class, command_args, progress_tid=None, show=True, style=""
):
    """Run a pip command asynchronously and capture the output."""
    import io
    import sys
    from pip._internal.cli.main import main as pip_main
    from rich.progress import Progress, TaskID
    from mbcore.display import safe_print

    # Create a custom output capture for pip
    original_stdout = sys.stdout
    original_stderr = sys.stderr

    # Create our custom IO capture that supports progress updates
    output_capture = io.StringIO()

    try:
        # Prepare command instance with our capture
        command_instance = command_class()

        # Redirect stdout/stderr to our capture
        sys.stdout = output_capture
        sys.stderr = output_capture

        # Run the command
        exit_code = command_instance.main(command_args)

        # Get the captured output
        output = output_capture.getvalue()

        # Parse any structured results if available
        parsed_results = getattr(command_instance, "results", {})

        if show and output:
            safe_print(output, style=style)

        return exit_code, output, parsed_results
    except Exception as e:
        return 1, f"Error running pip command: {str(e)}", {}
    finally:
        # Restore original stdout/stderr
        sys.stdout = original_stdout
        sys.stderr = original_stderr


if __name__ == "__main__":
    cmd = "git status --porcelain=v1 -z -uall "
    # print(run(cmd))
    # print(list(run_command(cmd)))
    # asyncio.run(arun(cmd))
    asyncio.run(aconsume(arun_command(cmd)))
