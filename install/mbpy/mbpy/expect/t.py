"""Copied and modified to work with asyncio and windows from pexpect."""

import time
import os
import re
import select
import subprocess
import sys
import tempfile
from collections.abc import Callable, Iterable
from io import BytesIO, StringIO
from re import Match, Pattern
from typing_extensions import (
    TYPE_CHECKING,
    Any,
    Protocol,
    Type,
    TypeVar,
    Sequence,
    IO,
)

from mbpy.expect.exceptions import EOF, TIMEOUT
from mbpy.expect.searcher import SearcherStringT, searcher_re

# Define type aliases
string_types = (str, bytes)
AnyStrT = TypeVar("AnyStrT", str, bytes)
AnyStrT_co = TypeVar("AnyStrT_co", str, bytes, covariant=True)
AnyStr = str | bytes
LogFile = Any | None

if TYPE_CHECKING:
    from mbpy.expect.searcher import SearcherStringT


class _NullCoder:
    """Pass bytes through unchanged."""

    @staticmethod
    def encode(b, final=False):
        return b

    @staticmethod
    def decode(b, final=False):
        return b


class SpawnBaseT(Protocol[AnyStrT]):
    encoding: str
    pid: int | None
    flag_eof: bool
    stdin: IO[AnyStrT] | None
    stdout: IO[AnyStrT] | None
    stderr: IO[AnyStrT] | None
    searcher: None | SearcherStringT
    ignorecase: bool
    before: AnyStrT | None
    after: Any | None
    match: AnyStrT | Match[str] | Match[bytes] | EOF | TIMEOUT | None
    match_index: int | None
    terminated: bool
    exitstatus: int | None
    signalstatus: int | None
    status: int | None
    child_fd: int | None
    timeout: float | None
    delimiter: type[EOF]
    logfile: LogFile
    logfile_read: LogFile
    logfile_send: LogFile
    maxread: int
    searchwindowsize: int
    delaybeforesend: float | None
    delayafterclose: float
    delayafterterminate: float
    delayafterread: float
    softspace: bool
    name: str
    closed: bool
    codec_errors: str
    string_type: Type[AnyStrT]
    buffer_type: Type[BytesIO] | Type[StringIO]
    crlf: AnyStr
    allowed_string_types: tuple[type, ...]
    linesep: AnyStr
    write_to_stdout: Callable[[AnyStr], int] | Any

    @property
    def buffer(self) -> bytearray: ...
    @buffer.setter
    def buffer(self, value: bytearray): ...
    def read_nonblocking(
        self, size: int = 1, timeout: float | None = None
    ) -> AnyStr: ...
    def compile_pattern_list(
        self,
        patterns: Any | list[Any],
    ) -> list[Any]: ...

    def expect(
        self,
        pattern: Any | Sequence[Any],
        timeout: float | None = -1,
        searchwindowsize: int | None = -1,
    ) -> int: ...

    def expect_list(
        self,
        pattern_list: list[Any],
        timeout: float | None = -1,
        searchwindowsize: int | None = -1,
    ) -> int: ...

    def expect_exact(
        self,
        pattern_list: Any | Iterable[Any],
        timeout: float | None = -1,
        searchwindowsize: int | None = -1,
    ) -> int: ...
    def expect_loop(
        self,
        searcher: SearcherStringT,
        timeout: float | None = -1,
        searchwindowsize: int | None = -1,
    ) -> int: ...
    def read(self, size: int = -1) -> AnyStrT: ...
    def readline(self, size: int = -1) -> AnyStrT_co: ...
    def __iter__(self) -> Any: ...
    def readlines(self, sizehint: int = -1) -> Sequence[AnyStrT_co]: ...
    def fileno(self) -> int: ...
    def flush(self) -> None: ...
    def isatty(self) -> bool: ...
    def __enter__(self) -> Any: ...
    def __exit__(self, etype, evalue, tb) -> None: ...
    def close(self) -> None: ...
    def __init__(
        self,
        command: str | None,
        args: Sequence[str] | None = None,
        timeout: int | float | None = 30,
        maxread: int = 2000,
        searchwindowsize: int | None = None,
        logfile: Any | None = None,
        cwd: str | None = None,
        env: dict[str, str] | None = None,
        ignore_sighup: bool = False,
        echo: bool = True,
        preexec_fn: Callable[[], None] | None = None,
        encoding: str | None = None,
        codec_errors: str = "strict",
        dimensions: tuple[int, int] | None = None,
        use_poll: bool = False,
    ): ...
    def __call__(
        self, command: str, args: Sequence[str] | None = None, **kwargs
    ) -> None: ...


text_type = str


class SpawnProcess:
    def __init__(
        self,
        cmd: AnyStrT | None = None,
        args: list[AnyStrT] | None = None,
        encoding="utf-8",
        timeout: float | None = 30,
        searchwindowsize: int | None = None,
        **kwargs,
    ):
        self.cmd = cmd
        self.args = args or []
        self.encoding = encoding
        self.timeout = timeout or 30
        self.searchwindowsize = searchwindowsize or 2000
        self.process = None
        self.buffer = bytearray()
        self.start_time = None
        self.closed = True
        self.before = None
        self.after = None
        self.match = None
        self.encoding = encoding or "utf-8"
        self.pid = None
        self.after = None
        self.match = None
        self.terminated = False
        self.exitstatus = None
        self.signalstatus = None
        self.status = None
        self.child_fd = None
        self.delimiter = EOF
        self.logfile = None
        self.logfile_read = None
        self.logfile_send = None
        self.maxread = 2000
        self.stdin = None
        self.stdout = None
        self.stderr = None
        self.searcher = None
        self.ignorecase = False

    def start(self, cmd: str | None = None, args: list[str] | None = None):
        self.cmd = cmd or self.cmd
        self.args = args or self.args
        if self.cmd is None:
            raise ValueError("No command given")
        self.process = subprocess.Popen(
            [self.cmd] + self.args,
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            bufsize=0,
        )
        self.pid = self.process.pid
        self.start_time = time.monotonic()
        self.closed = False
        self.stdin = self.process.stdin
        self.stdout = self.process.stdout
        self.status = self.process.poll()

    def _read_nonblocking(self, size=1, timeout=None) -> bytes:
        if not self.process or not self.process.stdout:
            raise EOFError("Process not started")

        rlist, _, _ = select.select([self.process.stdout], [], [], timeout)
        if not rlist:
            raise TimeoutError("Timeout expired")

        chunk = os.read(self.process.stdout.fileno(), size)
        if not chunk:
            raise EOFError("EOF reached")

        self.buffer.extend(chunk)
        if self.searchwindowsize and len(self.buffer) > self.searchwindowsize:
            self.buffer = self.buffer[-self.searchwindowsize :]

        return chunk

    def expect(
        self,
        pattern: list[Pattern],
        timeout: float | None = -1,
        searchwindowsize: int | None = -1,
    ) -> int:
        self.timeout = timeout or self.timeout
        self.searchwindowsize = searchwindowsize or self.searchwindowsize
        compiled = [
            re.compile(p.encode(self.encoding) if isinstance(p, str) else p)
            for p in pattern
        ]
        return self._expect_loop(compiled)

    def _expect_loop(self, patterns: list[Pattern]) -> int:
        if not self.process:
            raise EOFError("Process not started")
        if not patterns:
            raise ValueError("No patterns given")
        if not self.start_time:
            raise RuntimeError("Expect called before process started")
        while True:
            elapsed = time.monotonic() - self.start_time
            if self.timeout and elapsed > self.timeout:
                raise TimeoutError("Timeout expired")

            self._read_nonblocking(self.searchwindowsize, timeout=self.timeout)
            buffer_str = self.buffer.decode(self.encoding, errors="replace")

            for idx, pattern in enumerate(patterns):
                match = pattern.search(buffer_str)
                if match:
                    self.before = buffer_str[: match.start()]
                    self.after = buffer_str[match.end() :]
                    self.match = match
                    return idx

    def send(self, data: str):
        if not self.process or not self.process.stdin:
            raise EOFError("Process not started")
        self.process.stdin.write(data.encode(self.encoding))
        self.process.stdin.flush()

    def sendline(self, data: str):
        self.send(data + "\n")

    def sendeof(self):
        if not self.process or not self.process.stdin:
            raise EOFError("Process not started")
        self.process.stdin.close()

    def terminate(self):
        if not self.process:
            raise EOFError("Process not started")
        self.process.terminate()
        self.terminated = True

    def kill(self):
        if not self.process:
            raise EOFError("Process not started")
        self.process.kill()
        self.terminated = True

    def wait(self):
        if not self.process:
            raise EOFError("Process not started")
        self.process.wait()
        self.exitstatus = self.process.returncode
        self.status = self.exitstatus

    def close(self):
        if self.process:
            self.process.terminate()
            self.process.wait()
        self.closed = True

    def __enter__(self):
        self.start()
        return self

    def __exit__(self, etype, evalue, tb):
        self.close()

    def __del__(self):
        self.close()

    def __repr__(self):
        return f"<{self.__class__.__name__} pid={self.pid}>"

    def __str__(self):
        return repr(self)

    def __iter__(self):
        return self


class SpawnBase(SpawnBaseT[AnyStrT]):
    def __init__(
        self,
        cmd: AnyStrT | None = None,
        args: list[AnyStrT] | None = None,
        encoding: str = "utf-8",
        timeout: float = 30,
        searchwindowsize: int | None = None,
        logfile: Any | None = None,
    ):
        self.process = SpawnProcess(
            cmd,
            args,
            encoding=encoding,
            timeout=timeout,
            searchwindowsize=searchwindowsize,
        )
        self._before = None
        self._after = None
        self._match = None
        self.encoding = encoding
        self._buffer = BytesIO() if self.string_type is bytes else StringIO()
        self.searcher = None
        self.ignorecase = False
        self.closed = True
        self._before = self.string_type()

    @classmethod
    def __class_getitem__(cls, item: type[bytes]) -> type[SpawnBaseT]:
        new = type(f"SpawnBase[{item}]", (cls,), {})
        new.string_type = item  # type: ignore
        new.buffer_type = BytesIO if item is bytes else StringIO
        new.crlf = b"\r\n" if item is bytes else "\r\n"
        new.allowed_string_types = (item,)
        new.linesep = item(b"\n") if item is bytes else "\n"
        new.write_to_stdout = (
            sys.stdout.buffer.write if item is bytes else sys.stdout.write
        )
        return new

    def start(self):
        self.process.start()

    def read_nonblocking(self, size: int = 1, timeout: float | None = None) -> AnyStrT:
        out = self.process._read_nonblocking(size, timeout)
        return self.string_type(out)

    def compile_pattern_list(self, patterns: Any | list[Any]) -> list[Any]:
        if not isinstance(patterns, list):
            patterns = [patterns]
        return patterns

    def expect(
        self,
        pattern: Any | list[Any],
        timeout: float | None = -1,
        searchwindowsize: int | None = -1,
    ) -> int:
        patterns = self.compile_pattern_list(pattern)
        return self.process.expect(patterns)

    def expect_exact(
        self,
        pattern_list: Any | Iterable[Any],
        timeout: float | None = -1,
        searchwindowsize: int | None = -1,
    ) -> int:
        return self.expect(pattern_list, timeout, searchwindowsize)

    def expect_list(
        self,
        pattern_list: list[Any],
        timeout: float | None = -1,
        searchwindowsize: int | None = -1,
    ) -> int:
        return self.expect(pattern_list, timeout, searchwindowsize)

    def expect_loop(
        self,
        searcher: searcher_re,
        timeout: float | None = -1,
        searchwindowsize: int | None = -1,
    ) -> int:
        return self.process._expect_loop(searcher._strings)

    def read(self, size: int = -1) -> AnyStrT:
        if size < 0:
            return self.string_type(self.process.buffer)
        return self.string_type(self.process.buffer[:size])

    def readline(self, size: int = -1) -> AnyStrT:
        buffer_str = self.process.buffer
        line_end = buffer_str.find("\n")
        if line_end == -1:
            return ""
        line = buffer_str[: line_end + 1]
        self.process.buffer = self.process.buffer[line_end + 1 :]
        return self.string_type(line)

    def readlines(self, sizehint: int = -1) -> Sequence[AnyStrT_co]:
        return self.read().splitlines()

    def fileno(self) -> int:
        if not self.process.process or not self.process.process.stdout:
            raise RuntimeError("Process not started")
        return self.process.process.stdout.fileno()

    def flush(self) -> None:
        pass

    def isatty(self) -> bool:
        return False

    def __enter__(self):
        self.start()
        return self

    def __exit__(self, etype, evalue, tb):
        self.close()

    def close(self) -> None:
        self.process.close()

    @property
    def before(self):
        return self.process.before

    @property
    def after(self):
        return self.process.after


if __name__ == "__main__":

    class TestSpawn(SpawnBase[bytes]):
        def __init__(self):
            super().__init__(encoding="utf-8")
            # Create temporary file with text mode for proper line endings
            self._test_file = tempfile.TemporaryFile(mode="w+b")
            self.child_fd = self._test_file.fileno()
            self.closed = False

            # Write test data with explicit line endings and proper encoding
            test_data = "test data\r\nmore data\r\nfinal line".encode("utf-8")
            self._test_file.write(test_data)
            self._test_file.flush()
            self._test_file.seek(0)

        def close(self):
            # Ensure we close both the base class resources and our temp file
            if hasattr(self, "_test_file") and not self._test_file.closed:
                self._test_file.close()
            super().close()

    # Run basic tests
    test = TestSpawn()
    print(f"Platform: {sys.platform}")
    print(f"Encoding: {test.encoding}")
    print(f"Line separator: {repr(test.linesep)}")
    print(f"File descriptor: {test.child_fd}")
    print(f"File descriptor valid: {test._validate_fd()}")

    try:
        # Test basic read first
        data = test.read_nonblocking(size=4)
        print(f"Initial read: {repr(data)}")

        # Test expect functionality
        status = test.expect("data")
        print(f"Expect 'data' status: {status}")
        print(f"Before: {repr(test.before)}")
        print(f"After: {repr(test.after)}")

        # Test readline
        line = test.readline()
        print(f"Readline result: {repr(line)}")

        # Test expect_exact
        status = test.expect_exact("final")
        print(f"Expect_exact 'final' status: {status}")
        print("All tests completed successfully!")

    except Exception as e:
        print(f"Test error: {type(e).__name__}: {str(e)}")
        import traceback

        traceback.print_exc()
    finally:
        test.close()
