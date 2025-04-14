from __future__ import annotations

import asyncio
import atexit
import collections
import collections.abc
from collections.abc import Hashable, Coroutine, Generator
import logging
import os
from pathlib import Path
import pickle
import sys
import time
import traceback
import types
from typing import NewType
import weakref
from collections import defaultdict
from dataclasses import Field as DataclassField
from dataclasses import asdict, dataclass, field
from functools import partial
from inspect import getmembers, isclass, isfunction, ismethod, ismethoddescriptor, ismodule
from asyncio import Queue
from queue import Queue
from types import ModuleType
from mbcore.even._internal._trees import CacheKey, ishashable, treemap
from rich.console import Console

from dataclasses import dataclass
from typing import Any

TYPE_CHECKING = False

try:
    from typing_extensions import TypeIs
except ImportError:
    if not TYPE_CHECKING:
        # Only define the fallback if not type checking
        class TypeIs:

            @classmethod
            def __class_getitem__(cls, item):
                return Any

            def __call__(self, *args, **kwargs):
                return True


def safe_print(*args, **kwargs):
    Console().print(*args, **kwargs)


from typing_extensions import (
    cast,
    AsyncGenerator,
    Callable,
    Coroutine,
    Generator,
    Generic,
    Literal,
    ParamSpec,
    Protocol,
    TypeVar,
    runtime_checkable,
)

T = TypeVar("T")
AnyOwner = TypeVar("AnyOwner", bound="CacheEntry")
R_co = TypeVar("R_co", covariant=True)

P = ParamSpec("P")
R = TypeVar("R")
_R = TypeVar("_R")
__R = TypeVar("__R")
AR = AsyncGenerator[None, _R]
GR = Generator[None, _R, None]
CR = Coroutine[None, None, __R]


def ismethodwrapper(object) -> "TypeIs[types.MethodWrapperType]":
    """Return true if the object is a method wrapper."""
    return isinstance(object, types.MethodWrapperType)


_cache: "dict[CacheKey[Any,Any], CacheEntry]" = {}
_console = Console()
cache_len = _cache.__len__

# Declare _cache_info at module level
_cache_info = None


class LazyModule(ModuleType):
    """A subclass of the module type which triggers loading upon attribute access."""

    def __setstate__(self, state):
        """Allow pickling and unpickling of the module."""
        self.__dict__.update(state)

    def __reduce__(self):
        """Allow pickling and unpickling of the module."""
        return (self.__class__, (), self.__dict__)

    def __getattribute__(self, attr):
        """Trigger the load of the module and return the attribute."""
        __spec__ = object.__getattribute__(self, "__spec__")
        loader_state = __spec__.loader_state
        with loader_state["lock"]:
            # Only the first thread to get the lock should trigger the load
            # and reset the module's class. The rest can now getattr().
            if getattr(object.__getattribute__(self, "__class__"), "__name__",
                       None) == "LazyModule":
                # Reentrant calls from the same thread must be allowed to proceed without
                # triggering the load again.
                # exec_module() and self-referential imports are the primary ways this can
                # happen, but in any case we must return something to avoid deadlock.
                if loader_state["is_loading"]:
                    return object.__getattribute__(self, attr)
                loader_state["is_loading"] = True

                __dict__ = object.__getattribute__(self, "__dict__")

                # All module metadata must be gathered from __spec__ in order to avoid
                # using mutated values.
                # Get the original name to make sure no object substitution occurred
                # in sys.modules.
                original_name = __spec__.name
                # Figure out exactly what attributes were mutated between the creation
                # of the module and now.
                attrs_then = loader_state["__dict__"]
                attrs_now = __dict__
                attrs_updated = {}
                for key, value in attrs_now.items():
                    # Code that set an attribute may have kept a reference to the
                    # assigned object, making identity more important than equality.
                    if key not in attrs_then or id(attrs_now[key]) != id(
                            attrs_then[key]):
                        attrs_updated[key] = value
                __spec__.loader.exec_module(self)
                # If exec_module() was used directly there is no guarantee the module
                # object was put into sys.modules.
                if original_name in sys.modules and id(self) != id(
                        sys.modules[original_name]):
                    raise ValueError(
                        f"module object for {original_name!r} substituted in sys.modules during a lazy load"
                    )
                # Update after loading since that's what would happen in an eager
                # loading situation.
                __dict__.update(attrs_updated)
                # Finally, stop triggering this method.
                self.__class__ = ModuleType

        return getattr(self, attr)

    def __delattr__(self, attr):
        """Trigger the load and then perform the deletion."""
        # To trigger the load and raise an exception if the attribute
        # doesn't exist.
        self.__getattribute__(attr)
        delattr(self, attr)


Y = TypeVar("Y")
_acache_queue: dict[Hashable,
                    Queue[AsyncGenerator[Any, Any] | None]] = defaultdict(
                        partial(Queue, maxsize=10))
_gen_cache_queue: dict[Hashable,
                       Queue[Generator[Any, Any, Any] | None]] = defaultdict(
                           partial(Queue, maxsize=10))


class _GenProxy(Generator[Any, Any, Any]):
    __module__ = "mbcore.cache"

    def __init__(self, key, gen: Generator[Any, Any, Any] | None):
        self.key = key
        self.items = None
        _gen_cache_queue[key].put_nowait(gen)
        self.read_queue = Queue[Any]()

    def send(self, value):
        items = self.items
        if isinstance(items, list):
            self.read_queue.put_nowait(value)
            return
        if isinstance(items, Generator):
            return items.send(value)
        raise ValueError(f"Invalid generator: {items}")

    def __setstate__(self, state):
        self.items = state["items"]
        self.read_queue = state["read_queue"]
        self.key = state["key"]

    def __reduce__(self):
        return (self.__class__, (self.key, self.items, self.read_queue))

    def __iter__(self) -> Generator[Any, Any, None]:
        if self.items is not None:
            for item in self.items:
                if self.read_queue.empty():
                    yield item
                else:
                    yield item
                    item = self.read_queue.get(block=True)

            return

        if self.key in _gen_cache_queue:
            self.items = []
            _gen = _gen_cache_queue[self.key].get()
            if _gen is not None:
                for item in _gen:
                    self.items.append(item)
                    yield item
                return
        raise ValueError(f"Invalid generator: {self.items}")


class _AsyncGenProxy(AsyncGenerator[Any, Any]):
    __module__ = "mbcore.even._internal._cache"

    async def athrow(self, exc: BaseException):
        items = self.items
        if isinstance(items, list):
            items.append(exc)
            return
        if hasattr(items, "athrow"):
            return await items.athrow(exc)
        raise ValueError(f"Invalid async generator: {items}")

    def __init__(self, key, async_gen=None):
        self.key = key
        self.items = None  # Will store the collected items after first iteration
        if async_gen is not None:
            if isinstance(async_gen, list):
                self.items = async_gen.copy(
                )  # Make a copy to avoid modifying the original

        # Store in queue if not already there
        if key not in _acache_queue or _acache_queue[key].empty():
            _acache_queue[key].put_nowait(async_gen)

    def __reduce__(self):
        return (self.__class__, (self.key, self.items))

    def __setstate__(self, state):
        self.items = state["items"]
        self.key = state["key"]

    def __getstate__(self):
        return {"items": self.items, "key": self.key}

    async def __anext__(self):
        if isinstance(self.items, list):
            if not self.items:
                raise StopAsyncIteration
            return self.items.pop(0)
        if hasattr(self.items, "__anext__"):
            return await self.items.__anext__()
        raise StopAsyncIteration

    async def asend(self, value):
        if isinstance(self.items, list):
            self.items.append(value)
            return value
        if hasattr(self.items, "asend"):
            return await self.items.asend(value)
        raise ValueError(f"Invalid async generator: {self.items}")

    async def __aiter__(self):
        # If we already have collected items from a previous run, use them
        if isinstance(self.items, list):
            # Make a copy so we don't consume the original items
            items_copy = self.items.copy()
            for item in items_copy:
                yield item
            return

        # No items yet, try to get from queue
        if self.key in _acache_queue:
            queue = _acache_queue[self.key]
            _gen = queue.get_nowait()

            if hasattr(_gen, "__await__"):
                _gen = await _gen

            # Put the generator back for future uses
            queue.put_nowait(_gen)

            if _gen is not None:
                # Initialize items list if needed
                if self.items is None:
                    self.items = []

                if hasattr(_gen, "__aiter__"):
                    # It's an async generator - collect and yield items
                    async for item in _gen:
                        self.items.append(item)  # Store for future
                        yield item
                    return
                elif isinstance(_gen, list):
                    # It's a list - yield all items
                    for item in _gen:
                        self.items.append(item)  # Store for future
                        yield item
                    return

        # No cache entry found, just return empty generator
        return


def collect_info(module: ModuleType) -> dict[str, Any]:
    """Collect information about a module."""
    if not isinstance(module, ModuleType):
        return module
    return {
        "name": module.__name__,
        "file": module.__file__,
        "path": module.__path__,
        "loader": module.__loader__,
        "spec": module.__spec__,
        "package": module.__package__,
        "doc": module.__doc__,
        "members": treemap(collect_info, getmembers(module)),
    }


# Sentinel object for unloaded values
VALUE_NOT_LOADED = object()


@dataclass
class CacheEntry:
    key: CacheKey
    value: Any
    context_keys: Hashable | tuple[Hashable, ...] = field(
        default_factory=tuple)
    ttl: int = 24 * 60 * 60 * 7  # 1 week
    last_accessed: float = field(default_factory=time.time)
    last_updated: float = field(default_factory=time.time)
    last_missed: float = field(default_factory=float)
    isgen: bool = False
    iscoro: bool = False
    isagen: bool = False
    isweak: bool = False
    persistent: bool = False
    context_policy: str = "ttl"

    # def __post_init__(self):
    #     value = self.value

    #     # Handle generators and coroutines
    #     if hasattr(self.value, "__aiter__"):
    #         self.isagen = True
    #         self.value = _AsyncGenProxy(self.key, value)
    #     elif isinstance(value, collections.abc.Coroutine) or hasattr(value, "__await__"):
    #         self.iscoro = True
    #     elif isinstance(value, collections.abc.Generator) or hasattr(value, "send"):
    #         self.isgen = True
    #         self.value = _GenProxy(self.key, value)

    def __repr__(self):
        if not self.key and not self.value:
            return ""
        return (
            "Entry(\n" + f"\tkey={self.key},\n" + f"\tvalue={self.value},"
            if self.value else "" + f"\tcontext_keys={self.context_keys},\n" +
            f"\tttl={self.ttl},\n" if self.ttl else "" +
            f"\tlast_accessed={self.last_accessed},\n" if self.last_accessed
            else "" + f"\tlast_updated={self.last_updated},\n" if self.
            last_updated else "" +
            f"\tlast_missed={self.last_missed},\n" if self.
            last_missed else "" +
            f"\tisgen={self.isgen},\n" if self.isgen else "" +
            f"\tiscoro={self.iscoro},\n" if self.iscoro else "" +
            f"\tisagen={self.isagen},\n" if self.isagen else "" +
            f"\tisweak={self.isweak},\n" if self.isweak else "" +
            f"\tpersistent={self.persistent},\n" if self.persistent else "" +
            f"\tcontext_policy={self.context_policy},\n" if self.
            context_policy else "" + "\t)")

    __str__ = __repr__


@dataclass(unsafe_hash=True, eq=True)
class GlobalCacheInfo(dict):
    """Global cache information."""

    hits: int = 0
    misses: int = 0
    maxsize: int = 128
    currsize: int = 0
    currmemory: str = "0.0 MB"
    by_function: "dict[str, FunctionCacheInfo]" = field(default_factory=dict)

    def __post_init__(self):
        # Calculate current size and memory usage
        self.update_stats()

        # Also update the dict values to ensure consistency
        self["currsize"] = self.currsize
        self["currmemory"] = self.currmemory
        self["hits"] = self.hits
        self["misses"] = self.misses
        self["maxsize"] = self.maxsize
        self["by_function"] = self.by_function

    def __setattr__(self, name, value):
        """Override to ensure that both attribute and dict values are updated."""
        super().__setattr__(name, value)
        if name in [
                "hits", "misses", "maxsize", "currsize", "currmemory",
                "by_function"
        ]:
            self[name] = value

    def update_stats(self):
        """Update the cache statistics to reflect the current state."""
        self.currsize = len(_cache)
        # Calculate memory usage more accurately
        total_size = 0
        for key, value in _cache.items():
            # Size of the key
            total_size += sys.getsizeof(key)
            # Size of the value object itself
            total_size += sys.getsizeof(value)
            # Size of the value's content if it has a value attribute
            if hasattr(value, 'value') and value.value is not None:
                total_size += sys.getsizeof(value.value)

        self.currmemory = f"{total_size / 1024 / 1024:.2f} MB"
        # Dict values are updated via __setattr__

    def __getattribute__(self, name):
        """Update stats when someone tries to access certain attributes."""
        if name in ['currsize', 'currmemory'] and object.__getattribute__(
                self, name) == 0:
            self.update_stats()
        return object.__getattribute__(self, name)

    def __repr__(self):
        # Always update stats before reporting
        self.update_stats()

        if not self.hits and not self.misses and not self.currsize:
            return "(empty)"

        # Use a single, more concise format
        result = f"Cache: {self.currsize} entries, {self.currmemory}\n"
        if self.by_function:
            result += "Recent entries:\n"
            for func_name, func_info in sorted(self.by_function.items(),
                                               key=lambda x: x[1].hits,
                                               reverse=True)[:5]:
                for key_info in list(func_info.by_key.values())[:1]:
                    result += f"  {func_name} (accessed: {time.strftime('%H:%M:%S')})\n"
        return result

    __str__ = __repr__


def place_holder(v: Any) -> Any:
    """Return a placeholder value."""
    return v


CacheKeyString = NewType("CacheKeyString", str)


@dataclass(unsafe_hash=True, eq=True)
class FunctionCacheInfo(dict):
    """Cache information for a function."""

    type: Literal["function", "coroutine", "generator",
                  "async_generator"] = "function"
    by_key: dict[CacheKey, CacheEntryInfo] = field(default_factory=dict)
    hits: int = 0
    misses: int = 0
    maxsize: int = 128
    currsize: int = 0

    def __repr__(self) -> str:
        try:
            if not self.by_key and not self.hits and not self.misses and not self.currsize:
                return "(empty)"

            return f"""FunctionCache(
            \t\thits={self.hits},
            \t\tmisses={self.misses},
            \t\tmaxsize={self.maxsize},
            \t\tcurrsize={self.currsize},
            \t\ttop_keys:
            """ + ("\t\t\t" + "\n\t\t\t".join(
                map(
                    str,
                    list(x[1] for x in sorted(self.by_key.items(),
                                              key=lambda x: x[1].hits,
                                              reverse=True))[:3])) +
                   "\n" if self.by_key else "")
        except Exception as e:
            from pprint import pformat

            return pformat(asdict(self), compact=True, width=100)

    __str__ = __repr__


@dataclass(unsafe_hash=True, eq=True)
class CacheEntryInfo(dict):
    """Cache information for a single entry."""

    key: CacheKey
    hits: int = 0
    misses: int = 0

    def __repr__(self):
        if not self.hits and not self.misses and not self.key:
            return "(empty)"
        return f"""Entry(
        \t\t\t\tkey={tuple(map(lambda p: cast(Path,p[0]).relative_to(cast(Path,p[0]).parent.parent).name if isinstance(p, tuple) and hasattr(p[0], "name") else getattr(p, "name", str(p)), (*self.key.key, *self.key.context_keys)))},
        \t\t\t\thits={self.hits},
       \t\t\t\t\tmisses={self.misses}
        \t\t\t)"""

    __str__ = __repr__


def notnone(v: dict[str, Any]) -> dict[str, Any]:
    """Return the value if it is not None."""
    return {k: v for k, v in v.items() if v is not None}


def isgenerator(val: Any, isgen_flag=False) -> TypeIs[Generator]:
    """Return True if the value is a generator."""
    return (isinstance(val, Generator) or isgen_flag
            or isinstance(val, Generator)
            or hasattr(val, "send") and not isinstance(val, type))


def istype(v: Any, t: type = CacheEntry) -> bool:
    """Return True if the value is an instance of the given type."""
    return isinstance(v, t) or str(t) in str(v.__class__.__name__)


def is_serializable_member(val):
    return (not ismethod(val) and not isfunction(val)
            and not ismethoddescriptor(val) and not ismodule(val)
            and not isclass(val) and not isinstance(
                val,
                types.BuiltinFunctionType
                | types.BuiltinMethodType
                | types.MethodWrapperType
                | types.WrapperDescriptorType
                | types.MethodDescriptorType
                | types.MemberDescriptorType
                | type
                | ModuleType,
            ))


async def make_cachable(v: "CacheEntry| dict",
                        persistent: bool | None = None) -> "CacheEntry | None":
    """Make a value cachable by converting it to a serializable format."""
    from mbcore.even._internal._cache import CacheEntry

    key = getattr(v, "key", None)
    persistent = getattr(v, "persistent", persistent or False)
    if not persistent and isinstance(v, CacheEntry):
        # Don't cache non-persistent entries
        return None

    val = v.value if hasattr(v, "value") and istype(v, CacheEntry) else v
    if hasattr(val, "__dataclass_fields__"):  # Check for dataclass directly
        try:
            val = asdict(val)
        except Exception:
            return v
    if hasattr(val, "model_dump"):
        val = val.model_dump()
    if hasattr(v, "dict"):
        val = val.dict()
    if hasattr(val, "unwrap"):
        val = val.unwrap()

    if not ishashable(val):
        val = map(
            collapse,
            ((k, val) for (k, val) in getmembers(val, is_serializable_member)
             if val is not None and persistent),
        )
    if isinstance(val, weakref.ref):
        val = val()

    if isinstance(val, dict):
        val = collapse(val.items())
    iscoro = getattr(v, "iscoro", False)
    isgen = getattr(v, "isgen", False)
    isweak = getattr(v, "isweak",
                     isinstance(val, weakref.ref | weakref.ReferenceType))
    isagen = getattr(v, "isagen", False)

    if isinstance(val, weakref.ref):
        val = val()
    else:
        val = v.value if hasattr(
            v, "value") and type(v).__name__ == "CacheEntry" else v

    if hasattr(val, "__await__"):
        val = await val
    if hasattr(val, "__aiter__"):
        val = [x async for x in val]

    if isgenerator(val, isgen):
        val = list(val)

    if isinstance(val, asyncio.Future):
        val = val.result()
    if isinstance(val, ModuleType):
        val = collect_info(val)

    if hasattr(v, "value"):
        v.value = val
    try:
        p = pickle.dumps(val, -1)
    except Exception as e:
        traceback.print_exc()
        print(f"Error: {e}")
    if isinstance(v, CacheEntry):
        v.value = val
        return v

    return (CacheEntry(
        key=key,
        value=val,
        context_keys=getattr(v, "context_keys", tuple()),
        ttl=getattr(v, "ttl", 0),
        last_accessed=getattr(v, "last_accessed", time.time()),
        last_updated=getattr(v, "last_updated", time.time()),
        last_missed=getattr(v, "last_missed", 0.0),
        iscoro=iscoro,
        isgen=isgen,
        isagen=isagen,
        isweak=isweak,
        persistent=persistent or False,
        context_policy=getattr(v, "context_policy", "none"),
    ) if not isinstance(v, CacheEntry) else v)


# Now at the end of the file, after all class definitions

# Initialize cache info with an instance
if _cache_info is None:
    _cache_info = GlobalCacheInfo()
    _cache_info.update_stats()
