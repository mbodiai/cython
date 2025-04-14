from __future__ import annotations


from concurrent.futures import ThreadPoolExecutor

from contextlib import contextmanager, suppress
from functools import partial
from pathlib import Path
from signal import SIGINT
from threading import Thread
from time import time, sleep
from types import new_class

from mbcore import log
from mbcore.display import safe_print
from typing_extensions import Callable, Generic, Iterator, ParamSpec, Self, TypeVar


from mbpy.expect.spawnbase import EOF, SpawnBase
from mbcore.log import debug

P = ParamSpec("P")
R = TypeVar("R", bound=str | Iterator[str])


SpawnT = TypeVar("SpawnT", bound=SpawnBase)


thread_pool = ThreadPoolExecutor(max_workers=10)


class BaseCommand(Generic[SpawnT]):
    process_type: type[SpawnT]
    process: SpawnT | None

    def __init__(
        self,
        cmd: str | list[str],
        args: list[str] | None = None,
        show=False,
        cwd=None,
        timeout=30,
        buffer_size=8192,
    ):
        self.show = show
        cmd = cmd if isinstance(cmd, str) else " ".join(cmd)
        self.cmd: str = f"{cmd} {' '.join(args)}" if args else cmd
        self.buffer_size = buffer_size
        self.timeout = timeout
        log.verbose(f"{self.cmd=}, proc_type={self.process_type}")
        self.callable_cmd: Callable[[], SpawnT] = partial(
            self.process_type, self.cmd, cwd=cwd, maxread=buffer_size, timeout=timeout
        )
        self.args = args or []

        cwd = Path(str(cwd)).resolve() if cwd else Path.cwd()
        self.cwd = cwd if cwd.is_dir() else cwd.parent if cwd.exists() else Path.cwd()
        self.output = []
        self.started = 0
        self.lines = []
        self.thread: Thread | None = None
        self._started = time()
        self._signalstatus = 0
        self.before = None
        self.process: SpawnT | None = None
        log.verbose(f"{cmd=} {args=}, {cwd=}")
        log.verbose(f"self: {self=}, {self.cwd=}")

    def _create_thread(self, target, *args, **kwargs):
        self.thread = Thread(target=partial(target, *args, **kwargs), daemon=True)

        return self.thread

    @property
    def signaled(self) -> bool:
        return self._signalstatus != 0

    @signaled.setter
    def signaled(self, value: bool):
        self._signalstatus = int(value)

    def expect(self, *args, **kwargs) -> str | None:
        raise NotImplementedError

    def sigint(self) -> None:
        self._signalstatus = SIGINT

    @classmethod
    def __class_getitem__(cls, item: type[SpawnT]) -> type[Self]:
        new = new_class(
            f"CommandCtx[{item}]",
            (cls,),
            exec_body=lambda ns: ns.update({"process_type": item}),
        )
        new.process_type = item
        return new

    def getorstart(self) -> SpawnT:
        """Ensure process is running or start it"""
        if self.process is not None:
            return self.process
        self.process = self.start()
        return self.process

    def start(self) -> SpawnT:
        """Start the process"""
        self.started = time()
        self.process = self.callable_cmd()
        return self.process

    def __contains__(self, item):
        return item in " ".join(self.lines)

    @property
    def returncode(self) -> int | None:
        return self.process.returncode if self.process else None


class Command(BaseCommand[SpawnBase[str]]):
    def streamlines(
        self, *, show: bool | None = None, timeout: float | None = None
    ) -> Iterator[str]:
        """Stream lines from process.

        Args:
            show: Whether to print lines to stdout.
            timeout: Timeout for select/kqueue.
            no_select: Whether to disable select.
            no_kqueue: Whether to disable kqueue.

        Returns:
        """

        show = show if show is not None else self.show
        timeout = timeout if timeout is not None else 0.1
        self.process = self.getorstart()

        while True:
            try:
                line = self.process.read_nonblocking()
                if line:
                    if show:
                        safe_print(line)
                    yield line
                else:
                    sleep(timeout)
            except EOF:
                # Process has ended or file descriptor error
                break
            except Exception as e:
                debug(f"Error reading from process: {e}")
                break

    def join(self, timeout=10):
        """Wait for process to complete"""
        if self.thread:
            self.thread.join(timeout)

    @contextmanager
    def inbackground(self, *, show=True, timeout=10):
        """Run process in background without blocking"""
        show = show if show is not None else self.show
        try:
            self.process = self.getorstart()
            self.thread = self._create_thread(target=self.streamlines, show=show)
            self.thread.start()
            yield self
        finally:
            self.thread.join(timeout) if self.thread else None

    inbg = inbackground

    def readlines(self, *, show: bool | None = None) -> list[str]:
        show = show if show is not None else self.show
        return list(self.streamlines(show=show))

    def readtext(self, *, show: bool | None = None) -> str:
        lines = self.readlines(show=show)
        return "\n".join(lines)

    def __iter__(self):
        yield from self.streamlines()

    def __str__(self):
        return self.readtext()

    def __enter__(self):
        return self.readtext()

    def __exit__(self, exc_type, exc_val, exc_tb):
        if hasattr(self, "process") and self.process is not None:
            self.process.terminate()
            self.process = None
        if hasattr(self, "thread") and self.thread is not None:
            self.thread.join()
            with suppress(Exception):
                self.join(timeout=10)


if __name__ == "__main__":
    tic = time()
    cmd = Command("ls -l")
    print(cmd.readtext())
    toc = time()
    print(f"Time taken: {toc - tic} seconds")

    # print("Done")
    # cmd = Command("ls -l",show=True)
    # with cmd.inbg() as proc:
    #     for line in proc:
    #         print(line.strip())
