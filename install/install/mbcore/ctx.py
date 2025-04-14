import inspect
import logging
import os
import sys
import traceback
from contextlib import AbstractContextManager
from functools import reduce
from inspect import currentframe, getmodule, signature
from pathlib import Path
from pydoc import (
    HTMLDoc,
    allmethods,
    describe,
    locate,
    safeimport,
    source_synopsis,
    splitdoc,
    synopsis,
)
from time import time
from types import FrameType, ModuleType, SimpleNamespace, TracebackType

from rich.console import Console
from rich.traceback import Traceback
from typing_extensions import (
    Any,
    AsyncGenerator,
    Callable,
    Final,
    Generator,
    Generic,
    Iterable,
    Literal,
    ParamSpec,
    Tuple,
    Type,
    TypeVar,
    TypeVarTuple,
    cast,
)

from mbcore import import_utils
from mbcore._traceback import is_third_party
from mbcore.proto import Awaitable

P = ParamSpec("P")
T = TypeVar("T")
R = TypeVar("R")
Y = TypeVar("Y")


def caller(depth=1, default="__main__") -> "str | None":
    try:
        return sys._getframemodulename(depth + 1) or default
    except AttributeError:  # For platforms without _getframemodulename()
        pass
    try:
        return sys._getframe(depth + 1).f_globals.get("__name__", default)
    except (AttributeError, ValueError):  # For platforms without _getframe()
        pass
    return None


_T = TypeVar("_T")


class chdir(AbstractContextManager):
    """Non thread-safe context manager to change the current working directory."""

    def __init__(self, path):
        self.path = path
        self._old_cwd = []

    def __call__(self, func):
        def wrapper(*args, **kwargs):
            with self:
                return func(*args, **kwargs)

        return wrapper

    def __aenter__(self):
        self.__enter__()

    def __aexit__(self, *excinfo):
        return self.__exit__(*excinfo)

    def __enter__(self):
        self._old_cwd.append(Path.cwd())
        os.chdir(os.path.dirname(self.path) if self.path and not Path(str(self.path)).is_dir() else self.path)

    def __exit__(self, *excinfo):
        os.chdir(self._old_cwd.pop())


def onlyone(iterable: Iterable[T] | T) -> T:
    if not isinstance(iterable, Iterable):
        return iterable
    return next(iter(iterable))


def walk_parents(traceback: TracebackType) -> Generator[tuple[FrameType, str, int], None, None]:
    """Walk the parent frames of a traceback."""
    frames = inspect.getinnerframes(traceback)
    for frame, filename, lineno, _, _, _ in frames:
        yield frame, filename, lineno


def surrounding_ctx(frame, filename, lineno, num_lines=5) -> list[str]:
    """Grab the context of a frame."""
    lines = [""] + Path(filename).read_text().splitlines()

    return lines[max(0, lineno - num_lines) : lineno + num_lines]


def get_window(frames: Iterable[Tuple[FrameType, str, int]], num_lines=5):
    for frame, filename, lineno in frames:
        yield from surrounding_ctx(frame, filename, lineno, num_lines=num_lines)
        yield f"at {filename}:{lineno}"


async def aserve(
    client: Generator[T, Y, R] | AsyncGenerator[T, Y | R],
    server: "Callable[[T],Y]| AsyncGenerator[Y,T] | Generator[Y,T,Any]",
    timeout: float = float("inf"),
) -> R:
    if isinstance(client, AsyncGenerator) or isinstance(server, AsyncGenerator):
        return await aserve_client(client, server.send if isinstance(server, Iterable) else server, timeout)

    return serve(client, server, timeout)


def serve(
    client: Generator[T, Y, R], server: Callable[[T], Y] | Generator[Y, T, Any], timeout: float = float("inf"),
) -> R:
    server_handler = server if not isinstance(server, Iterable) else server.send
    return serve_client(client, server_handler, timeout)


async def aserve_client(
    client: AsyncGenerator[T, Y] | Generator[T, Y, R],
    server: Callable[[T], Y | Awaitable[Y]] | AsyncGenerator[Y, T],
    timeout: float = float("inf"),
) -> R:
    async def client_wrapper() -> AsyncGenerator[T, Y]:
        if isinstance(client, AsyncGenerator):
            val = yield await anext(client)
            async for val in client:
                val = yield await client.asend((yield val))
        elif isinstance(client, Generator):
            val = yield next(client)
            while True:
                try:
                    val = yield client.send((yield val))
                except StopIteration as e:
                    yield e.value

    import asyncio

    ttl = asyncio.get_running_loop().time() + timeout
    wrapped_client = client_wrapper()
    val = await anext(wrapped_client)

    while asyncio.get_running_loop().time() < ttl:
        try:
            if isinstance(server, AsyncGenerator):
                val = await wrapped_client.asend(await server.asend(val))
            else:
                resp = await asyncio.to_thread(server, val)
                if isinstance(resp, Awaitable):
                    val = await asyncio.wait_for(
                        asyncio.ensure_future(resp), timeout=max(0, ttl - asyncio.get_running_loop().time()),
                    )
                else:
                    val = cast(Y, resp)

                val = await wrapped_client.asend(val)

        except StopAsyncIteration:
            return cast(R, val)
        except StopIteration as e:
            return e.value
        except asyncio.TimeoutError:
            raise TimeoutError("Server function timed out.")

    raise TimeoutError("Generator did not complete within the timeout period.")


def serve_client(client: Generator[T, Y, R], server: Callable[[T], Y], timeout: float = float("inf")) -> R:
    ttl = time() + timeout
    val = next(client)

    while time() < ttl:
        try:
            val = client.send(server(val))
        except StopIteration as e:
            return e.value
    raise TimeoutError("Generator did not complete within the timeout period.")


class ResultExceptionHolder(Exception, Generic[T]):
    def __init__(self, step: int = 0):
        self.exc: BaseException | None = None
        self.tb: TracebackType | None = None  # Store traceback
        self.result: T | None = None

    def set_exception(self, exc: BaseException | None, tb: TracebackType | None = None) -> None:
        self.exc = exc
        self.tb = tb
        object.__setattr__(self, "__traceback__", tb)
        object.__setattr__(self, "__name__", getattr(exc.__class__, "__name__", None))
        object.__setattr__(self, "__module__", getattr(exc.__class__, "__module__", None))
        object.__setattr__(self, "__qualname__", getattr(exc.__class__, "__qualname__", None))
        object.__setattr__(self, "__package__", getattr(exc.__class__, "__package__", None))
        self.__dict__.update(exc.__dict__)
        self.__class__.__name__ = exc.__class__.__name__

    def __getattr__(self, attr):
        if self.exc and attr not in ("__dict__", "__class__"):
            return getattr(self.exc, attr)
        raise AttributeError(f"'ExceptionHolder' object has no attribute '{attr}'")

    def __bool__(self):
        return self.exc is not None

    def windowed(self, windowsize: int = 5, step=-1):
        """Print a window of code around each parent frame in the traceback."""
        if self.tb:
            yield from list(get_window(reversed(list(walk_parents(self.tb))), num_lines=windowsize))[:step]
        return "None"

    def __str__(self):
        if self.exc and self.tb:
            return str(str(self.exc))
        return "None"

    def __repr__(self):
        if self.exc:
            return repr(self.exc)
        return "None"

    def windowed_repr(self, windowsize: int = 5):
        """Print a window of code around each parent frame in the traceback."""
        if self.tb:
            return "\n".join(list(self.windowed(windowsize)))
        return "None"

    def __await__(self):
        return self


class FakeException(BaseException):
    pass


Ts = TypeVarTuple("Ts")


CRITICAL = 50
FATAL = CRITICAL
ERROR = 40
WARNING = 30
WARN = WARNING
INFO = 20
DEBUG = 10
NOTSET = 0

LOGLEVEL = Literal["CRITICAL", "FATAL", "ERROR", "WARNING", "WARN", "INFO", "DEBUG", "NOTSET"]


class nullcontext(AbstractContextManager):
    def __enter__(self):
        return self

    def __exit__(self, *excinfo):
        return False


class suppress(AbstractContextManager, Generic[P, T]):  # noqa
    """Context manager to suppress specified exceptions and capture them.
    ```
    Usage:
        with suppress(Exception) as ex:
            some_problematic_code()
        if ex:
           handle_problematic_code(ex).

        with supress.logignore(Exception) as ex:
            some_problematic_code()
    ```
    Args:
        exceptions: Exception types to suppress. Defaults to all exceptions.
        dontignore: Exception types not to suppress.
        log: Log the suppressed exception.
        windowsize: Number of lines of code to display around the exception.
        step: Number of lines to step through the traceback.

    Class Initializers:
        logignore: Suppress exceptions and log them.
        noncritical: Suppress all exceptions except KeyboardInterrupt.
        windowed: Suppress exceptions with a limited traceback window size.
        step: Suppress exceptions and return a generator to step through the traceback.
        then: Suppress exceptions then run a function that accepts the exception.

    """  # noqa: D205

    callbacks: list[Callable[[BaseException | None], Any] | Callable[[], Any]]

    def __init__(
        self,
        *exceptions: Type[BaseException],
        dontignore: Type[BaseException] | None = None,
        log: bool | LOGLEVEL = False,
        windowsize: int = 0,
        step: int = 0,
    ) -> None:
        """Suppress exceptions and capture them.

        Args:
            exceptions: Exception types to suppress. Defaults to all exceptions.
            dontignore: Exception types not to suppress.
            log: Log the suppressed exception.
            windowsize: Number of lines of code to display around the exception.
            step: Number of lines to step through the traceback.

        """
        self._exceptions = exceptions or (Exception,)
        self.log = log
        self.holder = ResultExceptionHolder(step=step)
        self.dontignore = dontignore or FakeException
        self.windowsize = windowsize
        self._step = step
        self.callbacks: list[Callable[[BaseException | None], Any] | Callable[[], Any]] = []
        self.filters = []
        self.result: T | BaseException | None = None

    def __enter__(self) -> ResultExceptionHolder[T] | Iterable[str]:
        if self._step:
            return self.holder.windowed(self._step)
        return self.holder

    def __aenter__(self) -> ResultExceptionHolder[T] | Iterable[str]:
        return self.__enter__()

    def __aexit__(self, exc_type, exc_value, tb) -> bool:
        return self.__exit__(exc_type, exc_value, tb)

    def __await__(self):
        return self

    def __exit__(
        self,
        exc_type: Type[BaseException] | None,
        exc_value: BaseException | None,
        tb: TracebackType | None,
    ) -> bool:
        if exc_type and issubclass(exc_type, self._exceptions) and not issubclass(exc_type, self.dontignore):
            self.holder.set_exception(exc_value, tb)  # Store both exception and traceback
            if self.log is True and (
                self.log is not False
                or not any(f(exc_value) for f in self.filters)
                and logging.getLogger().isEnabledFor(self.log)
            ):
                logging.error(f"{exc_type.__name__}: {exc_value}")
                if self.windowsize:
                    logging.error("".join(traceback.format_exception(exc_type, exc_value, tb, limit=self.windowsize)))
                else:
                    logging.exception(exc_value)

                logging.warning("The above exception was suppressed.")
            if getattr(self, "callbacks", None):

                def maybe_call(fn) -> Callable[[BaseException | None], Any]:
                    if signature(fn).parameters:
                        return fn
                    return lambda _: fn()

                self.result = reduce(lambda acc, fn: maybe_call(fn)(acc), self.callbacks, exc_value)
            return True  # Suppress the exception
        return False  # Do not suppress other exceptions

    def add_filter(self, filter: Callable[..., bool]) -> None:  # noqa
        self.filters.append(filter)

    @classmethod
    def logignore(cls, *exceptions: Type[BaseException], when: LOGLEVEL = "DEBUG") -> "suppress[P,T]":
        """Ignore exceptions and log them."""
        return cls(*exceptions, log=when)

    @classmethod
    def noncritical(cls) -> "suppress[P,T]":
        """Suppress all exceptions except KeyboardInterrupt."""
        return cls(BaseException, dontignore=KeyboardInterrupt)

    @classmethod
    def windowed(cls, windowsize: int = 5) -> "suppress[P,T]":
        """Suppress exceptions with a limited traceback window size."""
        return cls(BaseException, dontignore=KeyboardInterrupt, windowsize=windowsize)

    @classmethod
    def step(cls, step: int = 5) -> "suppress[P,T]":
        """Return a suppress context manager that returns a generator to step through the traceback."""
        return cls(BaseException, dontignore=KeyboardInterrupt, step=step).step()

    @classmethod
    def no_third_party(cls, *exceptions: Type[BaseException]) -> "suppress[P,T]":
        cl = cls(*exceptions)
        cl.add_filter(is_third_party)
        return cl

    @classmethod
    def then(cls, *funcs: Callable[[BaseException | None], T] | Callable[[], T]) -> "suppress[P,T]":
        """Suppress exceptions then run a function that accepts the exception. Can be chained."""
        ctx = cls(Exception)
        ctx.callbacks.extend(funcs)

        class ResultOrExceptionHolder(suppress[P, _T], Generic[P, _T]):
            def __init__(self, ctx: suppress):
                self.ctx = ctx
                super().__init__(Exception)

            def __enter__(self):
                if self.ctx.__enter__() is not None:
                    return self.ctx
                return self.ctx.result

            def __exit__(self, exc_type, exc_value, tb):
                self.ctx.__exit__(exc_type, exc_value, tb)

            def then(
                self, func: Callable[[BaseException | None], _T] | Callable[[], _T],
            ) -> "ResultOrExceptionHolder[P,_T]":
                self.ctx.callbacks.append(func)
                return self

        return ResultOrExceptionHolder(ctx)


console = Console()


def test_pydoc_methods() -> None:
    import mbpy
    import mrender
    from mrender import Markdown

    console.print(
        f"allmethods: {allmethods(Markdown)}\n",
    )
    # YES BELOW GOOD!
    # console.print(
    #     f"apropos: {apropos('Markdown')}\n"
    # )
    console.print(
        "classify_class_attrs:",
    )
    # pprint(classify_class_attrs(Markdown))
    console.print(
        f"synopsis: {synopsis(mrender.__file__)}\n",
    )
    console.print(
        f"synopsis: {synopsis(mbpy.__file__)}\n",
    )
    console.print(
        f"synopsis: {synopsis(mbpy.__file__)}\n",
    )
    console.print(
        f"source_synopsis: {source_synopsis(Path(mrender.__file__).open())}\n",
    )
    console.print(
        f"splitdoc: {splitdoc(Markdown.__doc__)}\n",
    )
    console.print(
        f"safeimport: {safeimport('mrender')}\n",
    )
    console.print(
        f"describe: {describe(Markdown)}\n",
    )
    console.print(
        f"locate: {locate('mrender')}\n",
    )
    Path("html").write_text(HTMLDoc().docmodule(Markdown))


def third_party_packages() -> list[str]:
    return [mod.__name__ for mod in sys.modules.values() if is_third_party(mod)]


def currentmodule() -> ModuleType | SimpleNamespace:
    return getmodule(currentframe()) or SimpleNamespace(**{"__file__": "Unknown"})


def parentmodule() -> ModuleType:
    return sys.modules[caller() or "__main__"]


def string(iterable) -> str:
    return "".join(iterable)


def main() -> None:
    BaseT: Final = cast(type, import_utils.smart_import("pydantic.BaseModel", "lazy") or dict)

    class RequestModel(BaseT):
        args: list
        kwargs: dict

    console = Console()
    test_pydoc_methods()
    with suppress.step() as ex:
        RequestModel.model_json_schema(mode=32)
    if ex:
        for line in ex:
            console.print(line)
        exit()
        tb = Traceback.from_exception(type(ex), ex, ex.tb)
        console.print(tb)
        # logging.error("6Third party packages: %s", third_party_packages())
        # console.print(Traceback.from_exception(type(ex), ex, ex.__traceback__))
        # logging.error("8Current module: %s", currentmodule())
        # logging.error("9Parent module: %s", "")
        # console.print("hello")
        # console.print(
        #     Traceback.from_exception(type(ex), ex, ex.__traceback__,width=console.width)
        # )
        console.print(f"Current module:[link]{currentmodule().__file__}[/link]")
    else:
        console.print("No exception")


if __name__ == "__main__":
    main()
