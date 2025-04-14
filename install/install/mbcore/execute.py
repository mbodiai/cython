from __future__ import annotations

import asyncio
import logging
import os
import sys
import threading
import traceback
from asyncio import events, exceptions, tasks
from itertools import chain
from logging import getLogger
from types import TracebackType

from rich_click import Command
from typing_extensions import (
    TYPE_CHECKING,
    Any,
    AsyncIterator,
    Callable,
    Coroutine,
    Generic,
    Iterable,
    Literal,
    ParamSpec,
    Self,
    TypeVar,
    cast,
    overload,
)

from mbcore.even.more import pull_out_front
from mbcore.more import Is, first_true

debug = getLogger("default").debug
info = getLogger("default").info
error = getLogger("default").error


def getlevel():
    return getLogger("default").level


if TYPE_CHECKING:
    from concurrent.futures import Future, ProcessPoolExecutor, ThreadPoolExecutor

    ExecutorT = TypeVar("ExecutorT", ThreadPoolExecutor, ProcessPoolExecutor)
else:
    ExecutorT = TypeVar("ExecutorT")

P = ParamSpec("P")
R = TypeVar("R")
T = TypeVar("T")
_AnyCallable = Callable[..., Any]
FC = TypeVar("FC", bound=_AnyCallable | Command)


def _set_task_name(task, name):
    if name is not None:
        try:
            set_name = task.set_name
        except AttributeError:
            import warnings

            warnings.warn(
                "Task.set_name() was added in Python 3.8, "
                "the method support will be mandatory for third-party "
                "task implementations since 3.13.",
                DeprecationWarning,
                stacklevel=3,
            )
        else:
            set_name(name)


class enqueue_work(Generic[P, R]):
    func: Callable[P, R] | None
    future: "Future[R] | None"
    executor: "ThreadPoolExecutor | ProcessPoolExecutor"

    @overload
    def __init__(
        self,
        executor: 'ThreadPoolExecutor | ProcessPoolExecutor | Literal["process","thread","as_completed"]',
        num_workers: int | None = None,
    ) -> None: ...
    @overload
    def __init__(self, func: Callable[P, R] | None = None) -> None: ...
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor

        func, *vals = pull_out_front(callable, chain(args, kwargs.values()))
        executor, *vals = pull_out_front(
            lambda x: isinstance(x, ThreadPoolExecutor | ProcessPoolExecutor | str), chain(args, kwargs.values()),
        )
        num_workers, *vals = pull_out_front(Is[int], chain(args, kwargs.values()))

        if executor is not None and isinstance(executor, str):
            executor = get_executor(cast(Literal["process", "thread", "as_completed"], executor), num_workers)
            self.future = None
            return
        self.func = func
        self.executor = executor or ThreadPoolExecutor(num_workers)
        self.future = None

    @overload
    def __call__(self, func: Callable[P, R]) -> "Self": ...
    @overload
    def __call__(self, *args: P.args, **kwargs: P.kwargs) -> "Future[R]": ...
    def __call__(self, *args, **kwargs) -> "Future[R] | Self":
        if self.func is None:
            f = first_true(callable, chain(args, kwargs.values()))
            if f is None:
                raise ValueError(f"Expected a callable, got {args} and {kwargs}")
            self.func = f
            return self
        self.future = self.executor.submit(self.func, *args, **kwargs)
        return self.future


class TaskGroup:
    """Asynchronous context manager for managing groups of tasks.

    Example use:

        async with asyncio.TaskGroup() as group:
            task1 = group.create_task(some_coroutine(...))
            task2 = group.create_task(other_coroutine(...))
        print("Both tasks have completed now.")

    All tasks are awaited when the context manager exits.

    Any exceptions other than `asyncio.CancelledError` raised within
    a task will cancel all remaining tasks and wait for them to exit.
    The exceptions are then combined and raised as an `ExceptionGroup`.
    """

    def __init__(self):
        self._entered = False
        self._exiting = False
        self._aborting = False
        self._loop: asyncio.AbstractEventLoop | None = None
        self._parent_task: asyncio.Task | None = None
        self._parent_cancel_requested = False
        self._tasks: set[asyncio.Task] = set()
        self._errors: list[BaseException] = []
        self._base_error = None
        self._on_completed_fut = None

    def __repr__(self):
        info = [""]
        if self._tasks:
            info.append(f"tasks={len(self._tasks)}")
        if self._errors:
            info.append(f"errors={len(self._errors)}")
        if self._aborting:
            info.append("cancelling")
        elif self._entered:
            info.append("entered")

        info_str = " ".join(info)
        return f"<TaskGroup{info_str}>"

    async def __aenter__(self):
        if self._entered:
            raise RuntimeError(f"TaskGroup {self!r} has already been entered")
        if self._loop is None:
            self._loop = events.get_running_loop()
        self._parent_task = tasks.current_task(self._loop)
        if self._parent_task is None:
            raise RuntimeError(f"TaskGroup {self!r} cannot determine the parent task")
        self._entered = True

        return self

    async def __aexit__(
        self, et: type[BaseException] | None, exc: BaseException | None, tb: TracebackType | None, /,
    ) -> "Coroutine[Any, Any, None]":
        self._exiting = True

        if exc is not None and self._is_base_error(exc) and self._base_error is None:
            self._base_error = exc

        propagate_cancellation_error = exc if et is exceptions.CancelledError else None
        if self._parent_cancel_requested:  # noqa: SIM102
            # If this flag is set we *must* call uncancel().
            if self._parent_task.uncancel() == 0:
                # If there are no pending cancellations left,
                # don't propagate CancelledError.
                propagate_cancellation_error = None

        if et is not None and not self._aborting:
            # Our parent task is being cancelled:
            #
            #    async with TaskGroup() as g:
            #        g.create_task(...)
            #        await ...  # <- CancelledError
            #
            # or there's an exception in "async with":
            #
            #    async with TaskGroup() as g:
            #        g.create_task(...)
            #        1 / 0
            #
            self._abort()

        # We use while-loop here because "self._on_completed_fut"
        # can be cancelled multiple times if our parent task
        # is being cancelled repeatedly (or even once, when
        # our own cancellation is already in progress)
        while self._tasks:
            if self._on_completed_fut is None:
                self._on_completed_fut = self._loop.create_future()

            try:
                await self._on_completed_fut
            except exceptions.CancelledError as ex:
                if not self._aborting:
                    # Our parent task is being cancelled:
                    #
                    #    async def wrapper():
                    #        async with TaskGroup() as g:
                    #            g.create_task(foo)
                    #
                    # "wrapper" is being cancelled while "foo" is
                    # still running.
                    propagate_cancellation_error = ex
                    self._abort()

            self._on_completed_fut = None

        assert not self._tasks

        if self._base_error is not None:
            raise self._base_error

        # Propagate CancelledError if there is one, except if there
        # are other errors -- those have priority.
        if propagate_cancellation_error and not self._errors:
            raise propagate_cancellation_error

        if et is not None and et is not exceptions.CancelledError:
            self._errors.append(exc)

        if self._errors:
            # Exceptions are heavy objects that can have object
            # cycles (bad for GC); let's not keep a reference to
            # a bunch of them.
            try:
                me = Exception("unhandled errors in a TaskGroup", self._errors)
                from mbcore.display import safe_print
                from mbcore.log import caller

                for e in self._errors:
                    traceback.print_exception(type(e), e, e.__traceback__, file=sys.stderr)
                    safe_print(caller(n=10, depth=2))

                raise me from None
            finally:
                self._errors = None

    def create_task(self, coro, *, name=None, context=None):
        """Create a new task in this group and return it.

        Similar to `asyncio.create_task`.
        """
        if not self._entered:
            raise RuntimeError(f"TaskGroup {self!r} has not been entered")
        if self._exiting and not self._tasks:
            raise RuntimeError(f"TaskGroup {self!r} is finished")
        if self._aborting:
            raise RuntimeError(f"TaskGroup {self!r} is shutting down")
        if context is None and self._loop is not None:
            task = self._loop.create_task(coro)
        elif self._loop is not None:
            task = self._loop.create_task(coro, name=name)
        else:
            raise RuntimeError("TaskGroup cannot determine the event loop")
        _set_task_name(task, name)
        task.add_done_callback(self._on_task_done)
        self._tasks.add(task)
        return task

    # Since Python 3.8 Tasks propagate all exceptions correctly,
    # except for KeyboardInterrupt and SystemExit which are
    # still considered special.

    def _is_base_error(self, exc: BaseException) -> bool:
        assert isinstance(exc, BaseException)
        return isinstance(exc, SystemExit | KeyboardInterrupt)

    def _abort(self):
        self._aborting = True

        for t in self._tasks:
            if not t.done():
                t.cancel()

    def _on_task_done(self, task: asyncio.Task):
        self._tasks.discard(task)

        if self._on_completed_fut is not None and not self._tasks and not self._on_completed_fut.done():
            self._on_completed_fut.set_result(True)

        if task.cancelled():
            return

        exc = task.exception()
        if exc is None:
            return

        import traceback

        formatted_tb = "".join(traceback.format_exception(type(exc), exc, exc.__traceback__))
        self._errors.append(exc)

        self._loop.call_exception_handler(
            {"message": f"Task {task!r} raised an exception", "exception": exc, "task": task, "traceback": formatted_tb},
        )

        if self._is_base_error(exc) and self._base_error is None:
            self._base_error = exc
        if logging.getLogger().isEnabledFor(logging.DEBUG):
            from mbcore.display import getconsole, getspinner

            console = getconsole()
            spinner = getspinner()
            spinner.stop()
            console.print(f"Task {task!r} raised an exception\n{formatted_tb}", file=sys.stderr)
        if self._parent_task.done():
            # Not sure if this case is possible, but we want to handle
            # it anyways.
            if logging.getLogger().isEnabledFor(logging.DEBUG):
                formatted_tb = "".join(traceback.format_exception(type(exc), exc, exc.__traceback__))
                self._loop.call_exception_handler(
                    {
                        "message": f"Task {task!r} has errored out but its parent "
                        f"task {self._parent_task} is already completed",
                        "exception": exc,
                        "task": task,
                        "traceback": formatted_tb,
                    },
                )
                console.print(
                    f"Task {task!r} has errored out but its parent "
                    f"task {self._parent_task} is already completed\n"
                    f"{formatted_tb}",
                    file=sys.stderr,
                )
            return

        if not self._aborting and not self._parent_cancel_requested:
            # If parent task *is not* being cancelled, it means that we want
            # to manually cancel it to abort whatever is being run right now
            # in the TaskGroup.  But we want to mark parent task as
            # "not cancelled" later in __aexit__.  Example situation that
            # we need to handle:
            #
            #    async def foo():
            #        try:
            #            async with TaskGroup() as g:
            #                g.create_task(crash_soon())
            #                await something  # <- this needs to be canceled
            #                                 #    by the TaskGroup, e.g.
            #                                 #    foo() needs to be cancelled
            #        except Exception:
            #            # Ignore any exceptions raised in the TaskGroup
            #            pass
            #        await something_else     # this line has to be called
            #                                 # after TaskGroup is finished.
            self._abort()
            self._parent_cancel_requested = True
            self._parent_task.cancel()


T = TypeVar("T")


def _cleanup(executor: "ThreadPoolExecutor | ProcessPoolExecutor"):
    try:
        executor.shutdown(wait=False, cancel_futures=True)
    except Exception:
        import traceback

        traceback.print_exc()
        raise


def get_process_executor(max_workers: int | None = None) -> "ProcessPoolExecutor":
    """Get an optimized ProcessPoolExecutor."""
    from concurrent.futures import ProcessPoolExecutor

    max_workers = min(max_workers or ((os.cpu_count() or 1) * 2), 32)

    executor = ProcessPoolExecutor(
        max_workers=max_workers,
        mp_context=None,  # Removed `fork` for compatibility
    )

    return executor


async def process_tasks(tasks: Iterable[Coroutine[Any, Any, T] | Callable[..., T]]) -> AsyncIterator[T]:
    """Process tasks and yield as they complete."""
    from inspect import iscoroutine, iscoroutinefunction

    pending = [
        asyncio.create_task(
            task if iscoroutine(task) else task() if iscoroutinefunction(task) else asyncio.to_thread(task),
        )
        for task in tasks
    ]

    try:
        for coro in asyncio.as_completed(pending):
            yield await coro
    finally:
        # Ensure cleanup runs even if iterator isn't fully consumed
        for task in pending:
            if not task.done():
                task.cancel()
        await asyncio.gather(*pending, return_exceptions=True)


@overload
def get_executor(kind: Literal["process"], max_workers: int | None = None) -> ProcessPoolExecutor: ...
@overload
def get_executor(kind: Literal["thread"], max_workers: int | None = None) -> ThreadPoolExecutor: ...
@overload
def get_executor(
    kind: Literal["as_completed"], max_workers: int | None = None,
) -> Callable[[Iterable[Coroutine[Any, Any, T]]], AsyncIterator[T]]: ...


def get_executor(kind: Literal["process", "thread", "as_completed"], max_workers: int | None = None) -> Any:
    """Get cached executor instance."""
    max_workers = max_workers or min(12, (os.cpu_count() or 1) * 4)
    if kind == "thread":
        return ThreadPoolExecutor(max_workers=max_workers)
    if kind == "process":
        return get_process_executor(max_workers=max_workers)
    if kind == "as_completed":
        return process_tasks
    raise ValueError(f"Invalid executor kind: {kind}")


def run_async(coro: Coroutine[Any, Any, T] | Callable[..., Coroutine[Any, Any, T]]) -> T | Future[T]:
    """Run an async coroutine in an existing event loop or create a new one.

    - If no event loop exists, creates a new one.
    - If an event loop is already running, schedules the coroutine as a task.

    Returns:
        T: The coroutine's result.

    """
    loop = events._get_running_loop()
    if loop is None:
        loop = events.new_event_loop()
        asyncio.set_event_loop(loop)
        return loop.run_until_complete(coro)

    return asyncio.run_coroutine_threadsafe(coro() if callable(coro) else coro, loop)


async def _signal_handler():
    """Handle termination signals to gracefully shut down the event loop."""
    loop = asyncio.get_running_loop()
    loop.stop()


def kill_hanging_threads():
    """Terminate all non-main threads."""
    for t in threading.enumerate():
        if t is not threading.main_thread():
            print(f"Killing thread: {t.name}")
            t.join(timeout=0.3)
            del t  # Remove reference


if __name__ == "__main__":
    # Example usage
    import time

    idents = []

    async def example_task(sleep):
        global idents
        idents.append(ident := len(idents))
        tic = time.perf_counter()
        print(f"Task {ident} is starting")
        await asyncio.sleep(sleep)
        print("Task is done")
        toc = time.perf_counter()
        print(f"Task {ident} took {toc - tic:0.4f} seconds")

    async def main():
        async for p in process_tasks([example_task(2), example_task(3), example_task(1)]):
            pass

    run_async(main())
    import threading

    print(f"Active threads: {threading.enumerate()}")
