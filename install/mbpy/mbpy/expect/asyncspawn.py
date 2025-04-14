import asyncio
from asyncio.subprocess import Process
import shlex
import re
import sys
from io import StringIO
from pathlib import Path
from typing import AsyncIterator, Pattern
from mbcore.log import debug
from mbcore import ctx
from mbcore.display import safe_print


# def _load_cache():
#     print("Loading cache")
#     p = Path("~/.mb/pcache.pkl")
#     if p.exists():
#         with p.open("rb") as f:
#             return pickle.load(f)
#     return {}
# _cache =   _load_cache()
# _proc = DummyProcess(
#     group=None,
#     target=None,
#     name="",
#     args=(),
#     kwargs={},
# )
# def _save_cache():
#     print("Saving cache")
#     p = Path("~/.mb/pcache.pkl")
#     p.parent.mkdir(parents=True, exist_ok=True)
#     p.touch(exist_ok=True)
#     with p.open("wb") as f:
#         pickle.dump(_cache, f)
# atexit.register(_save_cache)

from typing_extensions import Protocol, TypeVar

from mbpy.expect import Expecter
from mbpy.expect.expect import APatternWaiter
from mbpy.expect.spawnbase import SpawnBase
from mbpy.expect.searcher import EOF, TIMEOUT, searcher_re, searcher_string


class ProcessTransportP(Protocol): ...


TransportT = TypeVar("TransportT", bound=Process)


class AsyncSpawn(SpawnBase[str]):
    """Async-native process spawner with expect-like functionality."""

    pw: APatternWaiter
    pw_transport: tuple[asyncio.BaseProtocol, asyncio.Transport] | None

    def __init__(
        self,
        command: str | list[str],
        show: bool = False,
        cwd=None,
        shell=False,
        **kwargs,
    ):
        self.command = command if isinstance(command, str) else " ".join(command)
        # self.key =_mtime_key(self.start,*command if not isinstance(command, str) else command.split())
        # self.cached =  _cache.get(self.key)
        self.kwargs = kwargs
        self.allowed_string_types = (str,)
        self.show = show
        self.process: Process | None = None
        self._buffer = StringIO()
        self.before = ""
        self.after = ""
        self.match = None
        self.cwd = Path(cwd).resolve() if cwd else Path.cwd().resolve()
        self.shell = shell
        self.entered = False
        self.stdout = StringIO()
        self.stdout.name = "stdout"
        self.stderr = StringIO()
        self.stderr.name = "stderr"
        self._overflow = False
        self.MAX_BUFFER = 8192
        self.timeout = kwargs.get("timeout", 30)
        self.pw = APatternWaiter()
        self.pw_transport = None

    async def astart(self) -> "Process":
        debug(
            f"Running command: {self.command} in {self.cwd} with caller: {ctx.caller(3)}"
        )
        if self.shell:
            self.process = await asyncio.create_subprocess_shell(
                self.command,
                stdin=asyncio.subprocess.PIPE,
                stdout=asyncio.subprocess.PIPE,
                stderr=asyncio.subprocess.PIPE,
                **self.kwargs,
            )
            # self.stdout,self.stderr = await self.process.communicate()
            return self.process

        args = shlex.split(self.command)
        if not args:
            raise ValueError("Empty command")
        try:
            self.process = await asyncio.create_subprocess_exec(
                args[0],
                *args[1:],
                stdin=asyncio.subprocess.PIPE,
                stdout=asyncio.subprocess.PIPE,
                stderr=asyncio.subprocess.PIPE,
                **self.kwargs,
            )  # type: ignore

            # self.stdout,self.stderr = await self.process.communicate()
            return self.process
        except Exception:
            debug(
                f"Failed to run command: {self.command} in {self.cwd} with caller: {ctx.caller(3)}"
            )
            # Fallback to shell if exec fails
            self.process = await asyncio.create_subprocess_shell(
                f"bash -c {shlex.quote(self.command)}",
                stdin=asyncio.subprocess.PIPE,
                stdout=asyncio.subprocess.PIPE,
                stderr=asyncio.subprocess.PIPE,
                **self.kwargs,
            )  # type: ignore
            # self.stdout,self.stderr = await self.process.communicate()
            return self.process

    async def __aenter__(self):
        """Start process when entering context."""
        self.entered = True
        self.process = await self.agetorstart()

        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        """Cleanup process on exit."""
        if self.process:
            try:
                await self.aterminate()
            except ProcessLookupError:
                from mbcore.log import debug, error

                if debug():
                    import traceback

                    traceback.print_exc()
                    error(f"Process {self.process.pid} not found")
        if hasattr(self.stdout, "close"):
            self.stdout.close()
        if hasattr(self.stderr, "close"):
            self.stderr.close()
        self.process = None
        self.entered = False

    async def agetorstart(self) -> "Process":
        """Get existing process or start a new one."""
        if self.process:
            return self.process
        return await self.astart()

    async def aterminate(self) -> None:
        """Safely terminate the process."""
        if self.process:
            try:
                # Check if process is still running before attempting to terminate
                if self.process.returncode is None:
                    try:
                        self.process.terminate()
                        # Give process time to terminate gracefully
                        try:
                            await asyncio.wait_for(self.process.wait(), timeout=1.0)
                        except asyncio.TimeoutError:
                            # Force kill if graceful termination fails
                            self.process.kill()
                            await self.process.wait()
                    except ProcessLookupError:
                        # Process already terminated
                        pass
            finally:
                self.process = None

    async def areadline(self) -> str:
        """Read a single line from the process output."""
        process = self.process or await self.astart()
        stdout, stderr = process.stdout, process.stderr
        if not stdout or stdout.at_eof():
            return ""

        try:
            # Read both streams with a timeout
            stdout_task = asyncio.create_task(stdout.readline())
            tasks = [stdout_task]
            if stderr:
                stderr_task = asyncio.create_task(stderr.readline())
                tasks.append(stderr_task)

            # Wait for either stream with timeout
            done, pending = await asyncio.wait(
                tasks, return_when=asyncio.FIRST_COMPLETED
            )

            # Cancel pending tasks
            for task in pending:
                task.cancel()

            # Get results
            line = ""
            sterr = ""

            for task in done:
                if task is stdout_task:
                    line = task.result().decode().strip("\n")
                else:
                    sterr = task.result().decode().strip("\n")

            if line and not sterr:
                return line
            if sterr and not line:
                return sterr
            if line and sterr:
                return line + sterr
            if stdout.at_eof() and (not stderr or stderr.at_eof()):
                return ""
            return ""

        except asyncio.TimeoutError:
            raise

    async def areadtext(self) -> str:
        """Read the entire output from the process."""
        return "\n".join(await self.areadlines())

    async def areadlines(self, show=False) -> list[str]:
        """Async generator that yields lines from the process output."""
        out = []
        async for line in self.streamlines(show=show):
            out.append(line.rstrip("\n").rstrip("\r"))

        return out

    async def streamlines(self, show=False) -> AsyncIterator[str]:
        """Async generator that yields lines from the process output."""
        show = show or self.show
        while True:
            line = (await self.areadline()).strip("\n")
            if not line:
                break
            if show:
                safe_print(line)
            yield str(line)

    def expect_list(
        self, pattern_list, timeout: float | None = -1, searchwindowsize=-1
    ):
        if timeout == -1:
            timeout = self.timeout

        exp = Expecter(self, searcher_re(pattern_list), searchwindowsize)
        return exp.expect_loop(timeout)

    def expect_exact(
        self, pattern_list, timeout: float | None = -1, searchwindowsize=-1, **kw
    ):
        if timeout == -1:
            exp = Expecter(self, searcher_string(pattern_list), searchwindowsize)
            timeout = exp.timeout()

        if isinstance(pattern_list, self.allowed_string_types) or pattern_list in (
            TIMEOUT,
            EOF,
        ):
            pattern_list = [pattern_list]

        def prepare_pattern(pattern):
            if pattern in (TIMEOUT, EOF):  # noqa: F821
                return pattern
            if isinstance(pattern, self.allowed_string_types):
                return self._coerce_expect_string(pattern)
            self._pattern_type_err(pattern)
            return None

        try:
            pattern_list = iter(pattern_list)
        except TypeError:
            self._pattern_type_err(pattern_list)
        pattern_list = [prepare_pattern(p) for p in pattern_list]

        exp = Expecter(self, searcher_string(pattern_list), searchwindowsize)

        return exp.expect_loop(timeout)

    def expect_loop(self, searcher, timeout: float | None = -1, searchwindowsize=-1):
        exp = Expecter(self, searcher, searchwindowsize)
        return exp.expect_loop(timeout)

    @property
    def buffer_overflow(self) -> bool:
        """Check if buffer overflow occurred during processing."""
        return self._overflow

    async def aexpect(
        self,
        pattern: str | bytes | Pattern | list[str | bytes | Pattern],
        timeout: float = 30,
        buffer_size: int = 8192,
    ) -> AsyncIterator[int]:
        """Async generator that yields matches against the pattern with buffer management."""
        patterns = (
            [re.compile(pattern)]
            if isinstance(pattern, str | bytes | memoryview | bytearray)
            else [re.compile(p) if isinstance(p, str | bytes) else p for p in pattern]
            if isinstance(pattern, list)
            else [pattern]
        )

        if sys.version_info >= (3, 11):
            async with asyncio.timeout(timeout):
                while True:
                    if not self.process:
                        break
                    stdout = self.process.stdout
                    if not stdout or stdout.at_eof():
                        break

                    # Check buffer size
                    if len(self._buffer) >= self.MAX_BUFFER:
                        self._overflow = True
                        # Keep last window of data
                        self._buffer = self._buffer[-self.MAX_BUFFER // 2 :]

                    try:
                        data = await asyncio.wait_for(
                            stdout.read(buffer_size),
                            timeout=self.timeout,
                        )
                    except asyncio.TimeoutError:
                        # Check patterns on timeout too
                        current = self._buffer.decode()
                        for i, p in enumerate(patterns):
                            if match := p.search(current):
                                self.before = current[: match.start()]
                                self.after = current[match.end() :]
                                self.match = match
                                self._buffer = self._buffer[match.end() :]
                                yield i
                        continue

                    if not data:
                        break

                    self._buffer.extend(data)

                    # Process in smaller windows if buffer is large
                    window_size = min(len(self._buffer), buffer_size * 2)
                    current = self._buffer[:window_size].decode()

                    for i, p in enumerate(patterns):
                        if match := p.search(current):
                            self.before = current[: match.start()]
                            self.after = current[match.end() :]
                            self.match = match
                            self._buffer = self._buffer[match.end() :]
                            yield i
                            break
                    else:
                        # No match, slide window if buffer is large
                        if len(self._buffer) > buffer_size:
                            self._buffer = self._buffer[buffer_size // 2 :]

        else:
            while True:
                if not self.process or self.process.stdout.at_eof():
                    break
                data = await self.process.stdout.read(1024)
                if not data:
                    break
                self._buffer.extend(data)
                current = self._buffer.decode()
                for i, p in enumerate(patterns):
                    if match := p.search(current):
                        self.before = current[: match.start()]
                        self.after = current[match.end() :]
                        self.match = match
                        self._buffer[:] = self.after.encode()
                        yield i
                        break

    async def send(self, data: str):
        """Send data to process with backpressure handling."""
        process = self.process or await self.astart()

        # Break large writes into chunks to avoid buffer overflow
        chunk_size = 8192  # 8KB chunks
        data_bytes = data.encode()

        for i in range(0, len(data_bytes), chunk_size):
            chunk = data_bytes[i : i + chunk_size]
            process = self.process or await self.astart()
            stdin = process.stdin
            if stdin is None:
                raise ValueError("Process has no stdin")
            stdin.write(chunk)
            try:
                await asyncio.wait_for(stdin.drain(), timeout=1.0)
            except asyncio.TimeoutError:
                await self.areadline()
                await stdin.drain()

    async def sendline(self, data: str = ""):
        """Send a line of data with proper newline handling."""
        await self.send(data + "\n")

    __iter__ = None

    def __aiter__(self):
        return self

    async def __anext__(self):
        """Make AsyncSpawn iterable with `async for`."""
        line = await self.areadline()
        if not line:
            raise StopAsyncIteration
        return line


if __name__ == "__main__":

    async def main():
        async with AsyncSpawn("ls -l") as proc:
            async for line in proc:
                print(line.strip())

            # await proc.sendline("echo 'Hello World'")
            WHITE_SPACE = re.compile(r"tmp")
            async for i in proc.aexpect(WHITE_SPACE):
                print("Full match info:")
                print(f"Match: {proc.match.group()}")
                print(f"Before: '{proc.before}'")  # Will show content before 'tmp'
                print(f"After: '{proc.after}'")  # Will show content after 'tmp'
                print(f"Full line: '{proc.before + proc.match.group() + proc.after}'")

    asyncio.run(main())
