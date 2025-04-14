"""Copied and modified to work with asyncio and windows from pexpect."""

import asyncio
import os
import re
import shutil
import signal
import subprocess
import sys
import traceback
from multiprocessing import Process
from pathlib import Path

from typing_extensions import (
    LiteralString,
    Union,
)

from mbpy.expect.asyncspawn import AsyncSpawn


def get_shell_aliases(home_dir="~"):
    try:
        # Determine the shell and the appropriate initialization file
        shell = os.environ.get("SHELL", "")
        mbdir = Path(os.getenv("MB_WS", Path.home()))
        home_dirs = {Path.home(), Path(home_dir).expanduser(), mbdir}
        results = []

        for home_dir in home_dirs:
            if "bash" in shell:
                init_file = home_dir / ".bashrc"
            elif "zsh" in shell:
                init_file = home_dir / ".zshrc"
            else:
                raise ValueError(f"Unsupported shell: {shell}")

            # Check if the initialization file exists
            if not init_file.exists():
                continue  # Skip if the file doesn't exist

            # Source the shell configuration file and list aliases
            command = f"source {init_file}; alias"
            result = subprocess.run(
                command,
                shell=True,
                capture_output=True,
                text=True,
                executable=shell,
                check=False,
            )

            if result.returncode == 0:
                results.append(result.stdout.strip())
            else:
                raise ValueError(f"{result.stderr.strip()}")

        # Resolve aliases and dependencies
        return resolve_aliases_and_dependencies("\n".join(results).splitlines())
    except Exception as e:
        traceback.print_exc()
        return f"Error: {e}"


def resolve_aliases_and_dependencies(aliases, shell="bash"):
    """Resolves shell aliases, expands environment variables, and checks dependencies."""
    try:
        out = {}
        missing_dependencies = []
        for line in aliases:
            match = re.match(r"(\w+)=['\"]?(.+?)['\"]?$", line)
            if match:
                alias_name, alias_command = match.groups()
                resolved_command = os.path.expandvars(
                    alias_command,
                )  # Expand env variables

                # Check for missing dependencies
                command_parts = re.split(
                    r"[;|& ]+",
                    resolved_command,
                )  # Robust splitting
                md = [
                    part
                    for part in command_parts
                    if not shutil.which(part)
                    and not part.startswith("$")
                    and not part.startswith("(")
                ]
                missing_dependencies.extend(md)
                out[alias_name] = resolved_command

        return out, missing_dependencies
    except Exception as e:
        traceback.print_exc()
        return {"error": str(e)}


aliases, md = get_shell_aliases()


async def repl_run_command_async(
    repl: "REPLWrapper",
    cmdlines,
    timeout=-1,
) -> LiteralString:
    res = []
    repl.child.sendline(cmdlines[0])
    for line in cmdlines[1:]:
        await repl._expect_prompt(timeout=timeout, async_=True)
        res.append(repl.child.before)
        repl.child.sendline(line)

    prompt_idx = await repl._expect_prompt(timeout=timeout, async_=True)
    if prompt_idx == 1:
        repl.child.kill(signal.SIGINT)
        await repl._expect_prompt(timeout=1, async_=True)
        raise ValueError("Continuation prompt found - input was incomplete:")
    return "".join(res + [repl.child.before])


basestring = str

PEXPECT_PROMPT = "[PEXPECT_PROMPT>"
PEXPECT_CONTINUATION_PROMPT = "[PEXPECT_PROMPT+"


class REPLWrapper:
    """Wrapper for a REPL.

    :param cmd_or_spawn: This can either be an instance of :class:`pexpect.spawn`
      in which a REPL has already been started, or a str command to start a new
      REPL process.
    :param str orig_prompt: The prompt to expect at first.
    :param str prompt_change: A command to change the prompt to something more
      unique. If this is ``None``, the prompt will not be changed. This will
      be formatted with the new and continuation prompts as positional
      parameters, so you can use ``{}`` style formatting to insert them into
      the command.
    :param str new_prompt: The more unique prompt to expect after the change.
    :param str extra_init_cmd: Commands to do extra initialisation, such as
      disabling pagers.
    """

    def __init__(
        self,
        cmd_or_spawn: Union[str, "AsyncSpawn[Process]"],
        orig_prompt,
        prompt_change,
        new_prompt=PEXPECT_PROMPT,
        continuation_prompt=PEXPECT_CONTINUATION_PROMPT,
        extra_init_cmd=None,
    ):
        if isinstance(cmd_or_spawn, basestring):
            self.child = AsyncSpawn(cmd_or_spawn, echo=False, encoding="utf-8")
        else:
            self.child = cmd_or_spawn

        self.orig_prompt = orig_prompt
        self.prompt_change = prompt_change

        self.continuation_prompt = continuation_prompt

        self.extra_init_cmd = extra_init_cmd

    async def ainit(self):
        if self.prompt_change:
            await self.set_prompt(
                self.orig_prompt,
                self.prompt_change.format(self.orig_prompt, self.continuation_prompt),
            )
            self.prompt = self.prompt_change
        else:
            self.prompt = self.orig_prompt
        if self.extra_init_cmd:
            await self.child.sendline(self.extra_init_cmd)
            await self._expect_prompt()

    async def set_prompt(self, orig_prompt, prompt_change) -> None:
        self.child.expect(orig_prompt)
        await self.child.sendline(prompt_change)

    async def _expect_prompt(self, timeout=-1, async_=False):
        return await self.child.expect_exact(
            [self.prompt, self.continuation_prompt],
            timeout=timeout,
            async_=async_,
        )

    async def run_command(self, command, timeout=-1, async_=False):
        """Send a command to the REPL, wait for and return output.

        :param str command: The command to send. Trailing newlines are not needed.
          This should be a complete block of input that will trigger execution;
          if a continuation prompt is found after sending input, :exc:`ValueError`
          will be raised.
        :param int timeout: How long to wait for the next prompt. -1 means the
          default from the :class:`pexpect.spawn` object (default 30 seconds).
          None means to wait indefinitely.
        :param bool async_: On Python 3.4, or Python 3.3 with asyncio
          installed, passing ``async_=True`` will make this return an
          :mod:`asyncio` Future, which you can yield from to get the same
          result that this method would normally give directly.
        """
        # Split up multiline commands and feed them in bit-by-bit
        cmdlines = command.splitlines()
        # splitlines ignores trailing newlines - add it back in manually
        if command.endswith("\n"):
            cmdlines.append("")
        if not cmdlines:
            raise ValueError("No command was given")

        res = []
        await self.child.sendline(cmdlines[0])
        for line in cmdlines[1:]:
            await self._expect_prompt(timeout=timeout)
            res.append(self.child.before)
            await self.child.sendline(line)

        if self._expect_prompt(timeout=timeout) == 1:
            self.child.process.kill() if self.child.process is not None else None
            await self._expect_prompt(timeout=1)
            raise ValueError(
                "Continuation prompt found - input was incomplete:\n" + command,
            )
        return "".join(res + [self.child.before])


def python(command=sys.executable):
    """Start a Python shell and return a :class:`REPLWrapper` object."""
    return REPLWrapper(command, ">>> ", "import sys; sys.ps1={0!r}; sys.ps2={1!r}")


def _repl_sh(command, args, non_printable_insert):
    child = AsyncSpawn[Process](command, args, echo=False, encoding="utf-8")

    ps1 = PEXPECT_PROMPT[:5] + non_printable_insert + PEXPECT_PROMPT[5:]
    ps2 = (
        PEXPECT_CONTINUATION_PROMPT[:5]
        + non_printable_insert
        + PEXPECT_CONTINUATION_PROMPT[5:]
    )
    prompt_change = f"PS1='{ps1}' PS2='{ps2}' PROMPT_COMMAND=''"

    return REPLWrapper(child, "\\$", prompt_change, extra_init_cmd="export PAGER=cat")


def bash(command="bash"):
    """Start a bash shell and return a :class:`REPLWrapper` object."""
    bashrc = os.path.join(os.path.dirname(__file__), "bashrc.sh")
    return _repl_sh(command, ["--rcfile", bashrc], non_printable_insert="\\[\\]")


def zsh(command="zsh", args=("--no-rcs", "-V", "+Z")):
    """Start a zsh shell and return a :class:`REPLWrapper` object."""
    return _repl_sh(command, list(args), non_printable_insert="%(!..)")


if __name__ == "__main__":
    import asyncio

    async def main():
        repl = python()
        await repl.ainit()
        print(await repl.run_command("print('Hello, world!')"))

    asyncio.run(main())
