"""Copied and modified to work with asyncio and windows from pexpect."""

import codecs

import os
import re
from signal import signal
import subprocess
import sys
import tempfile
from collections.abc import Awaitable, Callable, Iterable
from io import BytesIO, StringIO
from pathlib import Path
from re import Match
from types import new_class
from typing import (
    Any,
    Literal,
    Protocol,
    TextIO,
    Type,
    TypeVar,
    cast,
    overload,
)


from mbcore.log import debug

from mbpy.expect.exceptions import EOF, TIMEOUT
from mbpy.expect.expect import Expecter
from mbpy.expect.searcher import SearcherStringT, searcher_string
from mbpy.expect.selector import Selector
from typing_extensions import IO, BinaryIO, TextIO


# Define type aliases
string_types = (str, bytes)
AnyStrT = TypeVar("AnyStrT", str, bytes)
AnyStrT_co = TypeVar("AnyStrT_co", str, bytes, covariant=True)
AnyStr = str | bytes
LogFile = Path | None


class _NullCoder:
    """Pass bytes through unchanged."""

    @staticmethod
    def encode(b, final=False) -> bytes:
        return b

    @staticmethod
    def decode(b, final=False) -> bytes:
        return b


class SpawnBaseT(Protocol[AnyStrT]):
    encoding: str | None
    pid: int | None
    flag_eof: bool
    stdin: TextIO | BinaryIO | IO[AnyStrT]
    stdout: TextIO | BinaryIO | IO[AnyStrT]
    stderr: TextIO | BinaryIO | IO[AnyStrT]
    searcher_type: type[SearcherStringT[AnyStrT]]
    expecter_type: type[Expecter]
    selector_type: type[Selector]

    ignorecase: bool
    match_index: int | None
    terminated: bool
    exitstatus: int | None
    signalstatus: int | None
    status: int | None
    child_fd: int | None
    timeout: float | None
    delimiter: type[EOF]
    maxread: int
    searchwindowsize: int | None
    softspace: bool
    name: str
    closed: bool
    codec_errors: str
    string_type: type[AnyStrT]
    buffer_type: Type[BinaryIO] | Type[StringIO]
    crlf: AnyStr
    allowed_string_types: tuple[type[AnyStrT], ...]
    linesep: AnyStr
    write_to_stdout: Callable[[AnyStr], int] | Any
    _buffer: BytesIO | StringIO
    _before: AnyStrT
    _after: AnyStrT
    _match: AnyStrT | Match[AnyStrT] | EOF | TIMEOUT | None | Any

    def read_nonblocking(
        self, size: int = 1, timeout: float | None = None
    ) -> AnyStrT: ...

    @overload
    def expect(
        self,
        pattern: Any | list[Any],
        timeout: float | None = -1,
        searchwindowsize: int | None = -1,
        async_: Literal[False] = False,
    ) -> int: ...
    @overload
    def expect(
        self,
        pattern: Any | list[Any],
        timeout: float | None = -1,
        searchwindowsize: int | None = -1,
        *,
        async_: Literal[True],
    ) -> Awaitable[int]: ...
    @overload
    def expect_list(
        self,
        pattern_list: list[Any],
        timeout: float | None = -1,
        searchwindowsize: int | None = -1,
        async_: Literal[False] = False,
    ) -> int: ...
    @overload
    def expect_list(
        self,
        pattern_list: list[Any],
        timeout: float | None = -1,
        searchwindowsize: int | None = -1,
        *,
        async_: Literal[True],
    ) -> Awaitable[int]: ...
    @overload
    def expect_exact(
        self,
        pattern_list: Any | Iterable[Any],
        timeout: float | None = -1,
        searchwindowsize: int | None = -1,
        async_: Literal[False] = False,
    ) -> int: ...
    @overload
    def expect_exact(
        self,
        pattern_list: Any | Iterable[Any],
        timeout: float | None = -1,
        searchwindowsize: int | None = -1,
        *,
        async_: Literal[True],
    ) -> Awaitable[int]: ...
    def expect_loop(
        self,
        searcher_type: type[SearcherStringT[AnyStrT]],
        timeout: float | None = -1,
        searchwindowsize: int | None = -1,
    ) -> int: ...
    def read(self, size: int = -1) -> AnyStr: ...
    def readline(self, size: int = -1) -> AnyStr: ...
    def __iter__(self): ...
    def readlines(self, sizehint: int = -1) -> list[AnyStr]: ...
    def fileno(self) -> int | None: ...
    def flush(self) -> None: ...
    def isatty(self) -> bool: ...
    def __enter__(self): ...
    def __exit__(self, etype, evalue, tb) -> None: ...
    def close(self) -> None: ...

    @property
    def buffer(self):
        return self._buffer

    @buffer.setter
    def buffer(self, value: AnyStrT) -> None:
        import io

        if isinstance(self._buffer, io.BytesIO):
            self._buffer.write(cast(bytes, value))
        else:
            self._buffer.write(cast(str, value))

    @property
    def before(self):
        return self._before

    @before.setter
    def before(self, value: AnyStrT) -> None:
        self._before = value

    @property
    def after(self):
        return self._after

    @after.setter
    def after(self, value: AnyStrT) -> None:
        self._after = value

    @property
    def match(self) -> Match[AnyStrT]:
        return cast(Match[AnyStrT], self._match)

    @match.setter
    def match(self, value: Match[AnyStrT] | EOF | TIMEOUT | None | Any) -> None:
        self._match = cast(Match[AnyStrT], value)


def get_selector_type() -> "type[Selector]":
    from mbpy.expect.selector import WinSelector, KQueueSelector, EpollSelector

    if sys.platform == "win32":
        return WinSelector
    elif sys.platform == "darwin":
        return KQueueSelector
    else:
        return EpollSelector


class SpawnBase(SpawnBaseT[AnyStrT]):
    encoding: str | None = None
    pid: int | None = None
    flag_eof: bool = False
    string_type: type[AnyStrT]
    buffer_type: Type[BytesIO] | Type[StringIO]
    process: subprocess.Popen

    @property
    def returncode(self) -> int | None:
        return self.process.returncode if self.process else None

    def __init__(
        self,
        command: str | None = None,
        args: list[str] | None = None,
        timeout: int | float = 30,
        maxread: int = 512,
        searchwindowsize: int | None = None,
        cwd: str | None = None,
        encoding: str | None = None,
        codec_errors: str = "strict",
        stdio: tuple[IO[AnyStrT], IO[AnyStrT], IO[AnyStrT]] = (
            sys.stdin,
            sys.stdout,
            sys.stderr,
        ),
    ):
        # Initialize private attributes for properties
        self._before_value: AnyStrT | None = None
        self._after_value: AnyStrT | None = None
        self._match_value: AnyStrT | Match[AnyStrT] | EOF | TIMEOUT | None | Any = None
        self.string_type = (
            type(self).string_type
            if hasattr(self, "string_type")
            else cast(type[AnyStrT], str)
        )
        self.buffer_type = (
            type(self).buffer_type
            if hasattr(self, "buffer_type")
            else cast(Type[BytesIO], StringIO)
        )
        self.allowed_string_types = (
            type(self).allowed_string_types
            if hasattr(self, "allowed_string_types")
            else cast(tuple[type[AnyStrT]], (str,))
        )
        self.stdin, self.stdout, self.stderr = stdio
        self.command = command
        self.args = args or []
        self.searcher_type = searcher_string[AnyStrT]
        self.ignorecase: bool = False
        self.match_index: int | None = None
        self.terminated: bool = True
        self.exitstatus: int | None = None
        self.signalstatus: int | None = None
        self.status: int | None = None
        self.child_fd: int = -1
        self.timeout: int | float = timeout
        self.delimiter: type[EOF] = EOF
        self.maxread: int = maxread
        self.searchwindowsize: int | None = searchwindowsize
        self.delaybeforesend: float | None = 0.05
        self.delayafterclose: float = 0.1
        self.delayafterterminate: float = 0.1
        self.delayafterread: float | None = 0.0001
        self.softspace: bool = False
        self.name: str = "<" + repr(self) + ">"
        self.closed: bool = True
        self.cwd = Path(cwd).resolve() if cwd else Path.cwd()

        # If string_type is str but no encoding is provided, set a default
        if self.string_type is str and encoding is None:
            encoding = "utf-8"

        self.encoding: str | None = encoding
        self.codec_errors: str = codec_errors
        self._selector: Selector | None = None
        if encoding is None:
            self._encoder = _NullCoder()
            self._decoder = _NullCoder()
            self.crlf = b"\r\n"

            self.linesep = os.linesep.encode("ascii")

            def write_to_stdout(b):
                try:
                    return sys.stdout.buffer.write(b)
                except AttributeError:
                    return sys.stdout.write(b.decode("ascii", "replace"))

            self.write_to_stdout = write_to_stdout
        else:
            self._encoder = codecs.getincrementalencoder(encoding)(codec_errors)
            self._decoder = codecs.getincrementaldecoder(encoding)(codec_errors)
        self.string_type = (
            type(self).string_type
            if hasattr(type(self), "string_type")
            else cast(type[AnyStrT], str)
        )
        self.allowed_string_types = (
            type(self).allowed_string_types
            if hasattr(type(self), "allowed_string_types")
            else cast(tuple[type[AnyStrT]], (str,))
        )
        self.crlf = "\r\n"
        self.linesep = os.linesep

        self.write_to_stdout = sys.stdout.write
        self._before = self.string_type()
        self._after = self.string_type()
        self._match = self.string_type()
        self._buffer = self.buffer_type()  # type: ignore

        self.expecter_type = Expecter
        self.selector_type = get_selector_type()

        # Platform specific initializations
        self.platform_is_windows = sys.platform == "win32"

        # Handle line endings properly per platform
        if self.platform_is_windows:
            self.linesep = "\r\n" if encoding else b"\r\n"
        else:
            self.linesep = os.linesep if encoding else os.linesep.encode("ascii")
        # Default encoding if none specified (use utf-8 on Windows, locale on Unix)
        if encoding is None and self.string_type is str:
            if self.platform_is_windows:
                self.encoding = "utf-8"
            else:
                import locale

                self.encoding = locale.getpreferredencoding(False)
        if self.command is not None:
            self.cmd = self.command
            self()

    def __call__(
        self,
        cmd: str | list[str] | None = None,
        args: list[str] | None = None,
        cwd: str | Path | None = None,
        env: dict[str, str] | None = None,
        show: bool = False,
        **kwargs: Any,
    ) -> "subprocess.Popen":
        """Starts the process and sets up non-blocking I/O."""
        from mbcore.log import verbose

        cmd = self.cmd if isinstance(self.cmd, str) else " ".join(self.cmd)
        args = args or self.args
        cwd = cwd or self.cwd
        env = env or None
        cmd = f"{cmd} {' '.join(args)}" if args else cmd
        verbose(f"Running command: {self.cmd}")
        try:
            self.process = subprocess.Popen(
                cmd,
                cwd=cwd,
                env=env,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                stdin=subprocess.PIPE,
                shell=True,
                text=issubclass(self.string_type, str),
            )
        except Exception:
            if debug():
                import traceback

                traceback.print_exc()
            self.process = subprocess.Popen(
                cmd,
                cwd=cwd,
                env=env,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                stdin=subprocess.PIPE,
                shell=False,
                text=issubclass(self.string_type, str),
            )
        self.pid = self.process.pid
        self.terminated = False
        self.flag_eof = False
        if self.searchwindowsize is None:
            self.searchwindowsize = 2000

        self.stdout = cast(IO[AnyStrT], self.process.stdout)
        self.stderr = cast(IO[AnyStrT], self.process.stderr)

        # Set file descriptor from stdout or stderr
        if self.process.stdout:
            self.child_fd = self.process.stdout.fileno()
        elif self.process.stderr:
            self.child_fd = self.process.stderr.fileno()

        return self.process

    def poll(self) -> int | None:
        """Returns process return code if it has terminated, else None."""
        if self.process:
            return self.process.poll()
        return None

    @classmethod
    def __class_getitem__(cls, item: type[AnyStrT]) -> "Type[SpawnBaseT[AnyStrT_co]]":
        return new_class(
            cls.__name__,
            (cls,),
            exec_body=lambda ns: ns.update(
                {
                    "string_type": item,
                    "buffer_type": BytesIO if item is bytes else StringIO,
                    "allowed_string_types": (item,),
                }
            ),
        )

    def terminate(self) -> None:
        """Terminate the child process."""
        if self.pid is None:
            debug("No child process to terminate.")
            return

        try:
            if sys.platform == "win32":
                # Windows-specific termination
                import subprocess

                subprocess.Popen(f"taskkill /F /PID {self.pid}", shell=True)
            else:
                # Unix-like termination
                os.kill(self.pid, signal.SIGTERM)
        except OSError as e:
            debug(f"Error terminating process {self.pid}: {e}")

    def read_nonblocking(self, size=512, timeout: float = -1) -> AnyStrT:
        # Use a balanced default buffer size
        if size is None:
            size = min(512, self.maxread)

        timeout = min(timeout, 0.1) if timeout is not None and timeout > 0 else 0.1
        self._selector = self._selector or self.selector_type(self)
        return self._selector.select(size, timeout)

    def _coerce_send_string(self, s):
        if self.encoding is None and not isinstance(s, bytes):
            return s.encode("utf-8")
        return s

    def wait(self):
        if self.terminated:
            return self.status
        status = self.process.wait()
        self.status = status
        self.terminated = True
        return status

    def expect(self, pattern, timeout=-1, searchwindowsize=-1):
        return self.expect_list(pattern, timeout, searchwindowsize)

    def expect_list(self, pattern_list, timeout=-1, searchwindowsize=-1):
        exp = self.expecter_type(
            self,
            self.searcher_type(pattern_list, exact=False, ignore_case=self.ignorecase),
            searchwindowsize,
        )
        return exp.expect_loop(timeout)

    def expect_exact(
        self,
        pattern_list: AnyStrT | list[AnyStrT],
        timeout: int | float = -1,
        searchwindowsize=-1,
    ):
        exp = self.expecter_type(
            self,
            self.searcher_type(pattern_list, exact=True, ignore_case=self.ignorecase),
            searchwindowsize,
            timeout,
        )

        return exp.expect_loop(timeout)

    def expect_loop(self, searcher, timeout: int = -1, searchwindowsize=-1):
        exp = self.expecter_type(self, searcher, searchwindowsize)
        return exp.expect_loop(timeout)

    def _coerce_expect_string(self, s: str):
        if isinstance(s, self.string_type):
            return cast(
                AnyStrT,
                s.encode("ascii")
                if not isinstance(s, bytes | bytearray | memoryview)
                else s,
            )
        return s

    def read(self, size=-1):
        if size == 0:
            return self.string_type()
        if size < 0:
            self.expect(self.delimiter)
            return self.before

        cre = re.compile(self._coerce_expect_string(".{%d}" % size), re.DOTALL)
        index = self.expect([cre, self.delimiter])
        if index == 0:
            return self.after
        return self.before

    def readline(self, size=-1):
        if size == 0:
            return self.string_type()
        index = self.expect([self.crlf, self.delimiter])
        if index == 0:
            return cast(str, self.before) + cast(str, self.crlf)

        return self.before

    def __iter__(self):
        return iter(self.readline, self.string_type())

    def readlines(self, sizehint=-1):
        lines = []
        while True:
            line = self.readline()
            if not line:
                break
            lines.append(line)
        return lines

    def fileno(self):
        return self.child_fd

    def flush(self) -> None:
        pass

    def isatty(self) -> bool:
        return False

    def __enter__(self):
        return self

    def __exit__(self, etype, evalue, tb):
        self.close()

    def close(self):
        """Close the file descriptor if it exists."""
        if self._selector:
            self._selector.close()

            if self._selector._validate_fd():
                try:
                    # Use os.close for both Windows and Unix platforms
                    if self.child_fd is not None and self.child_fd >= 0:
                        os.close(cast(int, self.child_fd))
                except OSError:
                    pass

        self.child_fd = -1
        self.closed = True

    def __del__(self):
        """Destructor to ensure proper cleanup."""
        if not getattr(self, "closed", True):
            try:
                self.close()
            except:
                pass


if __name__ == "__main__":

    class TestSpawn(SpawnBase):
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
    print(f"File descriptor valid: {test.selector_type(test)._validate_fd()}")

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
