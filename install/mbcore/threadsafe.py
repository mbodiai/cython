import asyncio
import threading
from collections import defaultdict
from contextlib import AbstractContextManager, contextmanager

from typing_extensions import Any, Callable


class make_aquirer:
    def __new__(cls, locks: "defaultdict[str|int, threading.Lock | asyncio.Lock]"):
        """Threadsafe lock acquisition for a shared dictionary of locks. Defaults to a regular threading.Lock if no type is provided.

        Usage:
        ```python
        locks = defaultdict(Lock)
        acquire = make_aquirer(locks
        wtih acquire("key") as lock:
            # Do something with the lock

        locks = defaultdict(asyncio.Lock)
        acquire = make_aquirer(locks)
        async with acquire("key") as lock:
            # Do something with the lock
        ```
        """
        # Ensure a default lock factory exists

        cls.locks = locks
        inst = super().__new__(cls)
        return inst

    @contextmanager
    def acquire(self, key: str | int | None = None) -> Any:
        """Return an existing or new lock."""
        if key is None:
            locked: list[threading.Lock | asyncio.Lock] = []
            try:
                for lock in self.locks.values():
                    lock.acquire()
                    locked.append(lock)
                yield locked
            except Exception as e:
                raise RuntimeError("Failed to acquire lock") from e
            finally:
                for lock in locked:
                    lock.release()

        else:
            fact = self.locks.default_factory
            lock = self.locks.setdefault(key, fact())
            try:
                lock.acquire()
                yield lock
            except Exception as e:
                raise RuntimeError("Failed to acquire lock") from e
            finally:
                lock.release()


# Async version
amake_aquirer: Callable[..., AbstractContextManager[asyncio.Lock]] = make_aquirer(defaultdict(asyncio.Lock))
