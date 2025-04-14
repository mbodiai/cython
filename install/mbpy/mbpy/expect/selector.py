import contextlib
import os
import select
import sys
from time import sleep
from typing import Optional, Union, Any

from typing_extensions import Protocol, TYPE_CHECKING

from mbpy.expect.exceptions import EOF
from mbpy.expect.searcher import AnyStrT, AnyStrT_co

if TYPE_CHECKING:
    from mbpy.expect.spawnbase import SpawnBase


class Selector(Protocol[AnyStrT_co]):
    spawn: "SpawnBase"
    child_fd: int
    encoding: Optional[str]
    flag_eof: bool

    def select(self, size: int, timeout: float) -> AnyStrT: ...
    def close(self): ...

    def _validate_fd(self):
        """Validate that the file descriptor is in a valid state and update if needed."""
        # Ensure we're using the latest fd from the spawn object
        if self.spawn.child_fd is not None and self.spawn.child_fd >= 0:
            self.child_fd = self.spawn.child_fd
            return True

        # Try to find a valid fd from connected process
        if self.spawn.process:
            if self.spawn.process.stdout and self.spawn.process.stdout.fileno() != -1:
                self.spawn.child_fd = self.spawn.process.stdout.fileno()
                self.child_fd = self.spawn.child_fd
                return True
            elif self.spawn.process.stderr and self.spawn.process.stderr.fileno() != -1:
                self.spawn.child_fd = self.spawn.process.stderr.fileno()
                self.child_fd = self.spawn.child_fd
                return True

        # No valid fd found
        self.spawn.flag_eof = True
        self.flag_eof = True
        return False

    def __init__(self, spawn: "SpawnBase"):
        self.spawn = spawn
        self.child_fd = self.spawn.child_fd
        self.encoding = self.spawn.encoding
        self.flag_eof = self.spawn.flag_eof

    def coerce_output(self, s: bytes) -> Union[str, bytes]:
        """Process the output, decoding if necessary."""
        if s in (b"", ""):
            self.flag_eof = True
            raise EOF("End Of File (EOF)")

        if self.spawn.encoding is not None:
            return self.spawn._decoder.decode(s, final=False)
        return s


class KQueueSelector(Selector):
    kq: Any
    spawn: "SpawnBase"

    def __init__(self, spawn: "SpawnBase"):
        super().__init__(spawn)
        self.kq = select.kqueue()

    def select(self, size=512, timeout: float = -1) -> Union[str, bytes]:
        if size is None:
            size = min(512, self.spawn.maxread)
        self.kq = self.kq or select.kqueue()
        timeout = min(timeout, 0.1) if timeout is not None and timeout > 0 else 0.1
        if not self._validate_fd():
            raise EOF("Invalid file descriptor")
        streams = [self.child_fd]

        try:
            events = [
                select.kevent(
                    fd,
                    filter=select.KQ_FILTER_READ,
                    flags=select.KQ_EV_ADD,
                    fflags=0,
                    data=0,
                    udata=0,
                )
                for fd in streams
            ]
            self.kq.control(events, 0, timeout)

            # Wait for events
            triggered = self.kq.control(None, len(streams), timeout)

            # Check process exit
            if not triggered:
                if self.spawn.terminated:
                    self.flag_eof = True
                    raise EOF("Process has exited")
                return "" if self.encoding is not None else b""

            for event in triggered:
                fd = event.ident
                try:
                    # Use event.data to determine how many bytes are available
                    available_bytes = (
                        event.data
                        if hasattr(event, "data") and event.data > 0
                        else size
                    )
                    s = os.read(fd, min(available_bytes, size))
                    if not s:
                        self.flag_eof = True
                        raise EOF("End Of File (EOF)")
                    return self.coerce_output(s)
                except (BlockingIOError, BrokenPipeError):
                    continue

            # No data read from any event
            return "" if self.encoding is not None else b""
        except OverflowError:
            # Handle negative file descriptor
            self.flag_eof = True
            raise EOF("File descriptor error")

    def close(self):
        if self.kq is not None:
            try:
                # Clean up kqueue resources
                events = [
                    select.kevent(
                        self.child_fd,
                        filter=select.KQ_FILTER_READ,
                        flags=select.KQ_EV_DELETE,
                    )
                ]
                self.kq.control(events, 0)
                self.kq.close()
                self.kq = None
            except:
                pass


class EpollSelector(Selector):
    epoll: Any
    EPOLLIN: int

    def __init__(self, spawn: "SpawnBase"):
        super().__init__(spawn)
        # Check if we're on Linux and epoll is available
        if sys.platform != "linux" or not hasattr(select, "epoll"):
            raise ImportError("epoll is not available on this platform")

        # Get platform-specific components using getattr to avoid linter errors
        self.epoll = getattr(select, "epoll")()
        self.EPOLLIN = getattr(select, "EPOLLIN")
        self.epoll.register(self.child_fd, self.EPOLLIN)

    def select(self, size, timeout) -> Union[str, bytes]:
        events = self.epoll.poll(timeout)
        if not events:
            return "" if self.encoding is not None else b""

        s = os.read(self.child_fd, size)
        return self.coerce_output(s)

    def close(self):
        try:
            self.epoll.unregister(self.child_fd)
            self.epoll.close()
        except:
            pass


class WinSelector(Selector):
    def __init__(self, spawn: "SpawnBase"):
        super().__init__(spawn)
        self._initialize_win_imports()

    def _initialize_win_imports(self):
        if sys.platform == "win32":
            try:
                import _winapi
                import msvcrt

                self._winapi = _winapi
                self._msvcrt = msvcrt
            except ImportError:
                self._winapi = None
                self._msvcrt = None
        else:
            self._winapi = None
            self._msvcrt = None

    def select(self, size, timeout) -> Union[str, bytes]:
        if not self._validate_fd():
            raise EOF("Invalid file descriptor")
        if sys.platform != "win32" or not self._winapi or not self._msvcrt:
            raise ImportError("Windows-specific modules not available")

        try:
            # Use PeekNamedPipe to check for data without blocking
            handle = self._msvcrt.get_osfhandle(self.child_fd)
            peek_result = self._winapi.PeekNamedPipe(handle, 0)
            bytes_available = peek_result[1] if peek_result else 0

            if bytes_available > 0:
                s = os.read(self.child_fd, min(bytes_available, size))
            else:
                sleep(timeout)
                # Check again after timeout
                peek_result = self._winapi.PeekNamedPipe(handle, 0)
                bytes_available = peek_result[1] if peek_result else 0
                if bytes_available > 0:
                    s = os.read(self.child_fd, min(bytes_available, size))
                else:
                    return "" if self.encoding is not None else b""

            return self.coerce_output(s)

        except Exception:
            self.flag_eof = True
            raise EOF("End Of File (EOF) or invalid pipe")

    def close(self):
        # No specific resources to close for WinSelector
        pass


class DefaultSelector(Selector):
    def __init__(self, spawn: "SpawnBase"):
        super().__init__(spawn)
        self.pipe = os.pipe()

    def select(self, size, timeout) -> Union[str, bytes]:
        if not self._validate_fd():
            raise EOF("Invalid file descriptor")
        events = select.select([self.pipe[0]], [], [], timeout)
        if not events:
            return "" if self.encoding is not None else b""

        s = os.read(self.pipe[0], size)
        return self.coerce_output(s)

    def close(self):
        with contextlib.suppress(Exception):
            os.close(self.pipe[0])
            os.close(self.pipe[1])
