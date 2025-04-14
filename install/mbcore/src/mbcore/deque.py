import asyncio
import contextlib
import threading
from asyncio import QueueEmpty, QueueFull, locks
from asyncio.events import _get_running_loop
from collections import deque
from itertools import compress, repeat
from types import GenericAlias

from typing_extensions import Literal

try:
    from _collections import deque
except ImportError:
    from collections import deque

_global_lock = threading.Lock()

# Used as a sentinel for loop parameter
_marker = object()


def ilen(iterable):
    """Return the number of items in *iterable*.

        >>> ilen(x for x in range(1000000) if x % 3 == 0)
        333334

    This consumes the iterable, so handle with care.

    """
    # This is the "most beautiful of the fast variants" of this function.
    # If you think you can improve on it, please ensure that your version
    # is both 10x faster and 10x more beautiful.
    return sum(compress(repeat(1), zip(iterable, strict=False)))


class _LoopBoundMixin:
    _loop = None

    def __init__(self, *, loop=_marker):
        if loop is not _marker:
            raise TypeError(
                f"As of 3.10, the *loop* parameter was removed from "
                f"{type(self).__name__}() since it is no longer necessary",
            )

    def _get_loop(self):
        loop = _get_running_loop()

        if self._loop is None:
            with _global_lock:
                if self._loop is None:
                    self._loop = loop
        if loop is not self._loop:
            raise RuntimeError(f"{self!r} is bound to a different event loop")
        return loop


class AsyncDeque(_LoopBoundMixin):
    """A queue, useful for coordinating producer and consumer coroutines.

    If maxsize is less than or equal to zero, the queue size is infinite. If it
    is an integer greater than 0, then "await put()" will block when the
    queue reaches maxsize, until an item is removed by get().

    Unlike the standard library Queue, you can reliably know this Queue's size
    with qsize(), since your single-threaded asyncio application won't be
    interrupted between calling qsize() and doing an operation on the Queue.
    """

    def __init__(self, maxsize=0):
        self._maxsize = maxsize

        # Futures.
        self._getters = deque()
        # Futures.
        self._putters = deque()
        self._unfinished_tasks = 0
        self._finished = locks.Event()
        self._finished.set()
        self._init(maxsize)

    def interrupt(self, item):
        """Interrupt all pending get and put operations and put item at the front of the queue."""
        return self.put_nowait(item, "right")

    def _init(self, maxsize):
        self._queue = deque()

    def _get(self, from_direction: Literal["left", "right"] = "right"):
        return self._queue.popleft() if from_direction == "left" else self._queue.pop()

    def _put(self, item, direction_from: Literal["left", "right"] = "right"):
        return self._queue.append(item) if direction_from == "right" else self._queue.appendleft(item)

    def _wakeup_next(self, waiters: deque[asyncio.Future]):
        """ "Wake up the next waiter that isn't cancelled."""
        while waiters:
            waiter = waiters.popleft()
            if not waiter.done():
                waiter.set_result(None)
                break

    def __repr__(self):
        return f"<{type(self).__name__} at {id(self):#x} {self._format()}>"

    def __str__(self):
        return f"<{type(self).__name__} {self._format()}>"

    __class_getitem__ = classmethod(GenericAlias)

    def _format(self):
        result = f"maxsize={self._maxsize!r}"
        if getattr(self, "_queue", None):
            result += f" queue={list(self._queue)!r}"
        if self._getters:
            result += f" _getters[{len(self._getters)}]"
        if self._putters:
            result += f" _putters[{len(self._putters)}]"
        if self._unfinished_tasks:
            result += f" tasks={self._unfinished_tasks}"
        return result

    def qsize(self):
        """Number of items in the queue."""
        return len(self._queue)

    @property
    def maxsize(self):
        """Number of items allowed in the queue."""
        return self._maxsize

    def empty(self):
        """Return True if the queue is empty, False otherwise."""
        return not self._queue

    def full(self):
        """Return True if there are maxsize items in the queue.

        Note: if the Queue was initialized with maxsize=0 (the default),
        then full() is never True.
        """
        if self._maxsize <= 0:
            return False
        return self.qsize() >= self._maxsize

    async def put(self, item):
        """Put an item into the queue.

        Put an item into the queue. If the queue is full, wait until a free
        slot is available before adding item.
        """
        while self.full():
            putter = self._get_loop().create_future()
            self._putters.append(putter)
            try:
                await putter
            except:
                # The putter could be removed from self._putters by a
                # previous get_nowait call.

                putter.cancel()  # Just in case putter is not done yet.
                # Clean self._putters from canceled putters.
                with contextlib.suppress(ValueError):
                    self._putters.remove(putter)
                if not self.full() and not putter.cancelled():
                    # We were woken up by get_nowait(), but can't take
                    # the call.  Wake up the next in line.
                    self._wakeup_next(self._putters)
                raise
        return self.put_nowait(item)

    def put_nowait(self, item, direction_from: Literal["left", "right"] = "right"):
        """Put an item into the queue without blocking.

        If no free slot is immediately available, raise QueueFull.
        """
        if self.full():
            raise QueueFull
        self._put(item, direction_from)
        self._unfinished_tasks += 1
        self._finished.clear()
        self._wakeup_next(self._getters)

    async def get(self, direction: Literal["left", "right"] = "right"):
        """Remove and return an item from the queue.

        If queue is empty, wait until an item is available.
        """
        while self.empty():
            getter = self._get_loop().create_future()
            self._getters.append(getter)
            try:
                await getter
            except:
                getter.cancel()  # Just in case getter is not done yet.
                with contextlib.suppress(ValueError):
                    self._getters.remove(getter)
                if not self.empty() and not getter.cancelled():
                    # We were woken up by put_nowait(), but can't take
                    # the call.  Wake up the next in line.
                    self._wakeup_next(self._getters)
                raise
        return self.get_nowait(direction)

    def get_nowait(self, direction: Literal["left", "right"] = "right"):
        """Remove and return an item from the queue.

        Return an item if one is immediately available, else raise QueueEmpty.
        """
        if self.empty():
            raise QueueEmpty
        item = self._get(direction)
        self._wakeup_next(self._putters)
        return item

    def task_done(self):
        """Indicate that a formerly enqueued task is complete.

        Used by queue consumers. For each get() used to fetch a task,
        a subsequent call to task_done() tells the queue that the processing
        on the task is complete.

        If a join() is currently blocking, it will resume when all items have
        been processed (meaning that a task_done() call was received for every
        item that had been put() into the queue).

        Raises ValueError if called more times than there were items placed in
        the queue.
        """
        if self._unfinished_tasks <= 0:
            raise ValueError("task_done() called too many times")
        self._unfinished_tasks -= 1
        if self._unfinished_tasks == 0:
            self._finished.set()

    async def join(self):
        """Block until all items in the queue have been gotten and processed.

        The count of unfinished tasks goes up whenever an item is added to the
        queue. The count goes down whenever a consumer calls task_done() to
        indicate that the item was retrieved and all work on it is complete.
        When the count of unfinished tasks drops to zero, join() unblocks.
        """
        if self._unfinished_tasks > 0:
            await self._finished.wait()

    async def get_left(self):
        """Remove and return an item from the left end of the deque asynchronously."""
        return await self.get("left")

    __len__ = qsize
