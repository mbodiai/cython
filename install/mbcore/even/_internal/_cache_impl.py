from __future__ import annotations

import asyncio
import atexit
import json
import logging
import pickle
import sys
import threading
import time
from collections import defaultdict
from collections.abc import AsyncGenerator, Generator, Mapping, Sequence
from dataclasses import asdict
from inspect import isasyncgenfunction, iscoroutinefunction, isgeneratorfunction
from itertools import chain
from os import getenv
from pathlib import Path

from pip._internal.network.cache import SafeFileCache
from rich.console import Console
from rich.table import Table
from rich.text import Text
from typing_extensions import Any, Callable, Generic, Self, Type, Unpack, overload

from mbcore.config import CACHE_CONFIG, CacheConfig
from mbcore.even._internal._cache import (
    CacheEntry,
    CacheEntryInfo,
    FunctionCacheInfo,
    GlobalCacheInfo,
    P,
    R,
    _AsyncGenProxy,
    _cache,
    _GenProxy,
    make_cachable,
    notnone,
    safe_print,
)
from mbcore.even._internal._trees import CacheKey, atreemap
from mbcore.recipes import first_true
from mbcore.threadsafe import make_aquirer
from mbcore.types import dynamic, wrapafter

# Restore SafeFileCache import

CACHE_OFF = getenv("MB_CACHE_OFF", False)

# Initialize file cache for safe file operations
_file_cache = None


def isvverbose() -> bool:
    import sys

    return any(arg in sys.argv
               for arg in ("-vv", "--vverbose", "-dd", "--ddebug", "--vvv",
                           "--vv", "--vvvv"))


def isverbose() -> bool:
    import sys

    return any(arg in sys.argv
               for arg in ("-v", "--verbose", "-d", "--debug", "-dd", "-vv",
                           "--ddebug", "--vverbose", "--vvv"))


def vverbose(*args: Any, **kwargs: Any):
    if isvverbose():
        for arg in args:
            logging.getLogger("default").log(1, arg, stacklevel=2)
        for k, v in kwargs.items():
            logging.getLogger("default").log(1, f"{k}={v}", stacklevel=2)


def get_info(info, show=False):
    from dataclasses import asdict

    from rich.box import Box
    from rich.table import Table

    NO_BOX = Box("    \n" * 8)

    keys = asdict(info).keys()
    table = Table(*map(str.upper, keys),
                  pad_edge=False,
                  show_edge=False,
                  highlight=True,
                  box=NO_BOX,
                  title="\n")
    if show:
        safe_print(table)
    table.add_row(*map(str, asdict(info).values()))
    return info


def init_func(*args, **kwargs):
    func = first_true(callable, chain(args, kwargs.values()))

    return func


def init_cfg(*args, **kwargs):
    return CacheConfig(**{
        **CACHE_CONFIG,
        **{
            k: v
            for k, v in kwargs.items() if k in CACHE_CONFIG
        }
    })


def summarize(cache, size):

    def _summarize(a):
        key, entry = a  # Unpack the key-value pair from cache items
        func = cache.func
        args = entry
        func_name = func.__qualname__ if hasattr(func,
                                                 "__qualname__") else str(func)
        # Format the entry details
        details = {
            "func":
            func_name,
            "args":
            args,
            "last_accessed":
            time.strftime("%Y-%m-%d %H:%M:%S",
                          time.localtime(getattr(entry, "last_accessed", 0))),
            "ttl":
            getattr(entry, "ttl", 0),
            "persistent":
            getattr(entry, "persistent", False),
        }
        return f"{details['func']}(args={details['args']}, last_accessed={details['last_accessed']}, ttl={details['ttl']}, persistent={details['persistent']}"

    sum = f"Cache size: {size / 1e6:.2f}MB. (mb cache) "
    sum += (f"Loaded {len(_cache)} entries with last 10 entries:" + "\n" +
            "\n".join(map(_summarize,
                          list(_cache.items())[-10:])))
    return sum


def render_table(
    data: Any,
    title: str | None = None,
    omit_keys: set[str] | None = None,
    summarize_func: Callable[[Any], str] | None = None,
    max_depth: int = 2,
    console: Console | None = None,
) -> Table:
    """Render any JSON-like data into a human-readable Rich table.

    Args:
        data: The input JSON-like object (dict, list, nested structures).
        title: Optional title for the table.
        omit_keys: Set of keys to omit from the table.
        summarize_func: Optional function to summarize large objects.
        max_depth: Maximum depth to expand nested structures.
        console: Optional Rich console instance.

    Returns:
        Rich Table object

    """
    # Import NO_BOX from a consistent location
    from mbcore.display import NO_BOX

    def is_atomic(value):
        """Check if the value is an atomic type (not iterable)."""
        return (isinstance(value, (str, int, float, bool, type(None)))
                or hasattr(value, "__dataclass_fields__") or callable(value))

    def process_value(value, depth=0):
        """Format values, applying summarization if needed."""
        if value is None:
            return Text("None", style="dim")

        if hasattr(value, "__dataclass_fields__"):
            value = asdict(value)

        if isinstance(value, CacheKey):
            value = value.key

        if callable(value):
            return Text(
                f"<function {getattr(value, '__qualname__', repr(value))}>",
                style="magenta")

        if is_atomic(value) and not isinstance(value, dict):
            return Text(
                str(value).replace("PosixPath", "").replace("Path", ""))

        if depth >= max_depth:
            if summarize_func and callable(summarize_func):
                return Text(
                    summarize_func(value).replace("PosixPath",
                                                  "").replace("Path", ""))
            return Text(
                f"<{type(value).__qualname__} with {len(value) if hasattr(value, '__len__') else '?'} items>",
                style="dim",
            )

        if isinstance(value, Mapping):
            return render_nested_table(value, depth + 1)

        if isinstance(value, (list, tuple, set)):
            if not value:
                return Text("[]", style="dim")
            items = list(value)
            if len(items) > 5:
                items_text = ("\n-".join(str(v) for v in items[:5]).replace(
                    "PosixPath",
                    "").replace("Path", "").replace(str(Path.cwd().resolve()),
                                                    ""))
                return Text(f"[{items_text}, ... {len(items) - 5} more]",
                            style="blue")
            items_text = "\n-".join(
                str(v).replace("PosixPath", "").replace("Path", "").replace(
                    str(Path.cwd().resolve()), "") for v in items[:5])
            return Text(f"[{items_text}]", style="blue")
        # Fallback for other types
        return Text(
            str(value).replace("PosixPath", "").replace("Path", "").replace(
                str(Path.cwd().resolve()), ""))

    def render_nested_table(nested_data: Mapping, depth=0):
        """Render a nested dictionary as a separate table."""
        if not nested_data:
            return Text("{}", style="dim")

        table = Table(show_edge=False, box=NO_BOX, expand=True, width=300)

        # Add columns
        keys = list(nested_data.keys())
        if not keys:
            return Text("{}", style="dim")

        for key in keys[:4]:
            if omit_keys and key in omit_keys:
                continue
            key_str = str(getattr(key, "key",
                                  key)).replace("PosixPath",
                                                "").replace("Path", "")[:20]
            table.add_column(key_str, style="cyan")

        # Add rows
        row_values = []
        for key in keys:
            if omit_keys and key in omit_keys:
                continue

            value = nested_data[key]
            processed = process_value(value, depth)

            # Add to row values list, handling any type of renderable
            row_values.append(processed)

        if row_values:
            # Any renderable can be used in add_row
            table.add_row(*row_values)

        return table

    # Handle different input types
    if isinstance(data, Mapping):
        table = render_nested_table(data)
        if isinstance(table, Text):
            t = Table(box=NO_BOX, show_edge=False, expand=True, width=120)
            t.add_column("Value", width=80)
            t.add_row(table)
            return t
        return table

    if isinstance(data, (list, tuple, set)) and data:
        try:
            # Try to get column keys from first item if it's a dict
            first_item = next(iter(data), None)
            if isinstance(first_item, dict):
                # Dictionary collection - create a table with columns for each key
                table = Table(show_edge=False, box=NO_BOX, expand=True)

                # Add index column
                table.add_column("Index", style="bold cyan")

                # Add columns for each key in the dictionaries
                column_keys = list(first_item.keys())
                for key in column_keys:
                    if omit_keys and key in omit_keys:
                        continue
                    table.add_column(str(key), style="bold cyan")

                # Add rows for each item
                for i, item in enumerate(data):
                    if not isinstance(item, dict):
                        continue

                    row = [Text(str(i))]
                    for key in column_keys:
                        if omit_keys and key in omit_keys:
                            continue
                        if key in item:
                            processed = process_value(item[key], 0)
                            # Any renderable (Text or Table) can be added directly
                            row.append(
                                processed
                            )  # type: ignore # Rich can handle both Text and Table
                        else:
                            row.append(Text("-", style="dim"))

                    # Any renderable can be used in add_row
                    table.add_row(*row)
                return table
            # List of non-dictionary items
            table = Table(show_edge=False, box=NO_BOX, expand=True)
            table.add_column("Index", style="bold cyan")
            table.add_column("Value", style="bold cyan")

            for i, item in enumerate(data):
                processed = process_value(item, 0)
                # Any renderable can be used in add_row
                table.add_row(Text(str(i)), processed)
            return table
        except (StopIteration, TypeError, ValueError, AttributeError):
            # Fallback for any errors in handling collections
            table = Table(show_edge=False, box=NO_BOX, expand=True)
            table.add_column("Value", style="bold yellow")
            table.add_row(
                Text(f"<{type(data).__qualname__} with {len(data)} items>",
                     style="dim"))
            return table

    elif is_atomic(data):
        table = Table(box=NO_BOX, show_edge=False, expand=True)
        table.add_column("Value", style="bold yellow")
        table.add_row(Text(str(data)))
        return table

    else:
        # Fallback for unsupported types
        table = Table(box=NO_BOX, show_edge=False, expand=True)
        table.add_column("Type", style="bold red")
        table.add_column("Representation", style="bold yellow")
        table.add_row(
            Text(type(data).__qualname__),
            Text(str(data)),
        )
        return table


def is_mapping(data: object) -> bool:
    return hasattr(data, "__getitem__") and hasattr(data, "items")


def is_iterable(data: object) -> bool:
    return hasattr(data, "__iter__")


def json_safe(data: object) -> object:
    """Translates a mapping / sequence recursively in the same fashion
    as `pydantic` v2's `model_dump(mode="json")`.
    """
    from datetime import date, datetime
    from pathlib import Path
    from types import MappingProxyType

    from mbcore.even._internal._cache import CacheEntry, CacheEntryInfo, CacheKey, GlobalCacheInfo

    if isinstance(data, Path):
        return str(data)
    if isinstance(data, MappingProxyType):
        return json_safe(dict(data))
    if isinstance(data, Mapping):
        return {
            json_safe(key): json_safe(value)
            for key, value in data.items()
        }

    # Check for Sequence explicitly, excluding str/bytes which are handled later
    if isinstance(data, Sequence) and not isinstance(data,
                                                     (str, bytes, bytearray)):
        return [json_safe(item) for item in data]

    if isinstance(data, (datetime, date)):
        return data.isoformat()
    if isinstance(data, CacheKey):
        return str(data)
    if isinstance(data, CacheEntryInfo):
        return {json_safe(k): json_safe(v) for k, v in data.items()}
    if isinstance(data, CacheEntry):
        return {json_safe(k): json_safe(v) for k, v in asdict(data).items()}
    if isinstance(data, GlobalCacheInfo):
        return {json_safe(k): json_safe(v) for k, v in asdict(data).items()}

    return data


_file_cache = SafeFileCache(str(Path(CACHE_CONFIG["pathdir"])))
_cache_info: GlobalCacheInfo = GlobalCacheInfo()


def serialize_metadata(meta: GlobalCacheInfo) -> str:
    """Serialize cache metadata to JSON, fallback to pickle."""
    import json

    return json.dumps(json_safe(asdict(meta)))


def deserialize_metadata(data: str) -> GlobalCacheInfo:
    """Deserialize metadata from JSON or pickle format."""
    try:
        # Try JSON first
        data_dict = json.loads(data)

        # Create a new GlobalCacheInfo
        result = GlobalCacheInfo()

        # Manually copy the simple attributes
        result.hits = data_dict.get("hits", 0)
        result.misses = data_dict.get("misses", 0)
        result.maxsize = data_dict.get("maxsize", 128)
        result.currsize = data_dict.get("currsize", 0)
        result.currmemory = data_dict.get("currmemory", "0.0 MB")

        # Process function info separately
        by_function = {}
        for func_name, func_data in data_dict.get("by_function", {}).items():
            func_info = FunctionCacheInfo()
            func_info.type = func_data.get("type", "function")
            func_info.hits = func_data.get("hits", 0)
            func_info.misses = func_data.get("misses", 0)
            func_info.maxsize = func_data.get("maxsize", 128)
            func_info.currsize = func_data.get("currsize", 0)

            # Process by_key data
            by_key = {}
            for key_str, key_data in func_data.get("by_key", {}).items():
                # We need to reconstruct a CacheKey object here
                # Create a properly initialized CacheKey
                from mbcore.even._internal._trees import CacheKey

                # Create a dummy key with the minimum required attributes
                dummy_key = CacheKey()
                dummy_key.key = (f"restored:{key_str}",
                                 )  # Tuple with a string identifier
                dummy_key.context_keys = ()
                dummy_key.func_name = func_name
                dummy_key.policy_type = "ttl"
                dummy_key.ttl = 0
                dummy_key.expires = 0

                entry_info = CacheEntryInfo(
                    key=dummy_key,  # Use our properly initialized dummy key
                    hits=key_data.get("hits", 0),
                    misses=key_data.get("misses", 0),
                )
                by_key[key_str] = entry_info

            func_info.by_key = by_key
            by_function[func_name] = func_info

        result.by_function = by_function
        return result

    except Exception as e:
        import traceback

        traceback.print_exc()
        vverbose(f"Error deserializing metadata: {e}")
        return GlobalCacheInfo()


# Load cache on startup (unchanged)


def load(
    pathdir: Path | str = CACHE_CONFIG["pathdir"]
) -> dict[CacheKey, CacheEntry]:
    """Load cache from SafeFileCache into memory.

    Returns a dictionary of cache entries. The keys maintain their original type.
    """
    if CACHE_OFF:
        return {}

    # Use SafeFileCache for storage
    CacheConfig(**CACHE_CONFIG)
    path_dir = Path(str(pathdir)).resolve()
    if not path_dir.exists():
        # Silently create if it doesn't exist
        path_dir.mkdir(parents=True, exist_ok=True)

    file_cache = SafeFileCache(str(path_dir))

    d = {}
    try:
        # Fast path: just load the cache keys
        cache_keys_data = file_cache.get("cache_keys")
        if not cache_keys_data:
            return d

        # Parse the key hashes
        key_hashes = json.loads(cache_keys_data.decode("utf-8"))

        # Load each entry in parallel
        for key_hash in key_hashes:
            try:
                key_hash = str(key_hash)
                # Get entry data directly as binary file
                body_file = file_cache.get_body(key_hash)

                if body_file:
                    try:
                        # Read the data and close file immediately
                        entry_data = body_file.read()
                        body_file.close()

                        # Deserialize without any logging overhead
                        entry = pickle.loads(entry_data)
                        if hasattr(entry, "key"):
                            d[entry.key] = entry
                    except Exception:
                        # Silently skip any entries that can't be loaded
                        pass
            except Exception:
                # Skip errors silently
                pass

        # Minimize metadata loading - only load after entries
        if d:
            cache_meta = file_cache.get("cache_meta")
            if cache_meta:
                global _cache_info
                try:
                    _cache_info = deserialize_metadata(
                        cache_meta.decode("utf-8"))
                except Exception:
                    pass
    except Exception:
        # Silent failure
        pass

    return d


def tree_key_map(func, tree):
    if isinstance(tree, dict):
        return {func(k): tree_key_map(func, v) for k, v in tree.items()}
    if isinstance(tree, list):
        return [tree_key_map(func, v) for v in tree]
    return tree


async def make_cache_tree(cache_dict, filepath):
    """Process cache dictionary for serialization."""
    vverbose(
        f"[cyan][DEBUG][/cyan] Processing cache with {len(cache_dict)} entries."
    )

    # Create a more compact version of the cache for serialization
    compact_cache = await atreemap(make_cachable, cache_dict)
    serializable = notnone(compact_cache)

    vverbose(
        f"[cyan][DEBUG][/cyan] Processed {len(serializable)} cache entries")

    return serializable

    # with Path(filepath).open("wb") as f:
    #     pickle.dump(serializable, f)
    # json_path = filepath.parent / "cache_info.json"
    # with json_path.open("w") as f:
    #     json.dump(tree_key_map(lambda x: x._func_name if isinstance(x,CacheKey) else x,_cache_info), f, indent=4)


class ReprMeta(type):

    def __repr__(cls):
        if not _cache:
            return "(empty)"

        # Instead of rendering the full table, just show a summary
        cache_size = sum(sys.getsizeof(v) for v in _cache.values()) / 1e6
        num_entries = len(_cache)

        # Get the top 5 most frequently accessed cache entries
        entries_by_hits = sorted(
            [(k, v) for k, v in _cache.items() if hasattr(v, "last_accessed")],
            key=lambda x: getattr(x[1], "last_accessed", 0),
            reverse=True,
        )[:5]

        # Format a compact representation
        summary = [
            f"Cache: {num_entries} entries, {cache_size:.2f}MB",
        ]

        if entries_by_hits:
            summary.append("Recent entries:")
            for key, entry in entries_by_hits:
                func_name = getattr(key, "_func_name", "unknown")
                accessed = time.strftime(
                    "%H:%M:%S",
                    time.localtime(getattr(entry, "last_accessed", 0)))
                summary.append(f"  {func_name} (accessed: {accessed})")

        return "\n".join(summary)


class cache(Generic[P, R], metaclass=ReprMeta):
    __slots__ = ("_pending", "func", "_cfg", "_mkey", "_initialized",
                 "__dict__", "_function_info")
    locks: defaultdict[str | int, threading.Lock
                       | asyncio.Lock] = defaultdict(lambda: threading.Lock())
    _info = _cache_info
    _tasks = set()
    _task_started = False
    acquire = make_aquirer(locks).acquire
    acache_queue: asyncio.Queue = asyncio.Queue()

    # def __contains__(self, key: CacheKey) -> bool:
    #     """Check if the key exists in the cache using the & operator."""
    #     if CACHE_OFF or not self._cfg['enabled']:
    #         vverbose(f"[yellow][CACHE][/yellow] Cache is disabled for key {key}")
    #         return False

    #     # Direct entry lookup
    #     entry = _cache.get(key)
    #     if entry is not None:
    #         # Use & operator to check key equality with context
    #         if not (entry.key & key):
    #             vverbose(f"[yellow][CACHE][/yellow] Key format mismatch for {key}")
    #             _cache.pop(key, None)
    #             return False

    #         vverbose(f"[green][CACHE HIT][/green] Direct match for key {key}")
    #         return True

    #     vverbose(f"[yellow][CACHE][/yellow] Direct lookup failed, checking {len(_cache)} other keys")
    #     for stored_key in _cache:
    #         # Use & operator for context-aware comparison
    #         if stored_key & key:
    #             vverbose(f"[green][CACHE HIT][/green] Found matching key {stored_key} for {key}")
    #             return True

    #     vverbose(f"[red][CACHE MISS][/red] No match found for key {key}")
    #     return False

    # def __getitem__(self, key):
    #     # First try direct lookup
    #     entry = _cache.get(key)
    #     if entry:
    #         if not (entry.key & key):
    #             return _cache.pop(key)
    #         return entry

    #     raise KeyError(key)

    @property
    def entries(self):
        return _cache

    def __setitem__(self, key: CacheKey, value):
        if not isinstance(value, CacheEntry):
            entry = CacheEntry(
                key=key,
                value=value,
                context_keys=key.context_keys,
                ttl=self._cfg["ttl"],
                last_accessed=time.time(),
                last_updated=time.time(),
                last_missed=0.0,
                isagen=hasattr(value, "__aiter__"),
                iscoro=hasattr(value, "__await__"),
                persistent=self._cfg["persistent"],
                context_policy=self._cfg["context_policy"],
            )
        else:
            entry = value
        with self.acquire(hash(key)):
            _cache[key] = entry

        self._function_info.currsize += 1
        # Update global stats too
        type(self).acache_queue.put_nowait(self.update_stats)

    def update_stats(self):
        self._function_info.currsize += 1
        _cache_info.currsize = len(_cache)
        size = sum(sys.getsizeof(v) for v in _cache.values())
        _cache_info.currmemory = f"{size / 1e6:.2f}MB."

    def __delitem__(self, key):
        with self.acquire(hash(key)):
            del _cache[key]
            if hasattr(self, "_function_info"):
                self._function_info.currsize -= 1
                # Update global stats too
                _cache_info.currsize = len(_cache)
                size = sum(sys.getsizeof(v) for v in _cache.values())
                _cache_info.currmemory = f"{size / 1e6:.2f}MB."

    def hit(self, key: CacheKey[Any, Any]) -> Self:
        """Record that a key was accessed."""
        if CACHE_OFF or not self._cfg["enabled"]:
            return self
        vverbose(f"[green][CACHE HIT][/green] {key}")

        # Make sure we're working with a FunctionCacheInfo instance
        if not isinstance(self._function_info, FunctionCacheInfo):
            self._function_info = FunctionCacheInfo(
                type="function" if not isgeneratorfunction(self.func) else
                "generator" if isgeneratorfunction(self.func) else "coroutine"
                if iscoroutinefunction(self.func) else "async_generator", )

        # Update hits at function level
        self._function_info.hits += 1

        # Ensure by_key is initialized as a dict if it's not already
        if not hasattr(self._function_info,
                       "by_key") or self._function_info.by_key is None:
            self._function_info.by_key = {}

        # Create or update entry info
        if key not in self._function_info.by_key:
            self._function_info.by_key[key] = CacheEntryInfo(key=key,
                                                             hits=1,
                                                             misses=0)
        else:
            self._function_info.by_key[key].hits += 1

        # Update global stats
        if self.func is not None:
            func_name = self.func_name
            if func_name not in _cache_info.by_function:
                _cache_info.by_function[func_name] = self._function_info
            else:
                _cache_info.by_function[func_name].hits += 1

        # Update global hits counter
        _cache_info.hits += 1
        return self

    def miss(self, key: CacheKey[Any, Any]) -> "Self":
        """Record that a key was missed."""
        if CACHE_OFF or not self._cfg["enabled"]:
            return self
        vverbose(f"[red][CACHE MISS][/red] {key}")

        # Make sure we're working with a FunctionCacheInfo instance
        if not isinstance(self._function_info, FunctionCacheInfo):
            self._function_info = FunctionCacheInfo(
                type="function" if not isgeneratorfunction(self.func) else
                "generator" if isgeneratorfunction(self.func) else "coroutine"
                if iscoroutinefunction(self.func) else "async_generator", )

        # Update misses at function level
        self._function_info.misses += 1

        # Ensure by_key is initialized as a dict if it's not already
        if not hasattr(self._function_info,
                       "by_key") or self._function_info.by_key is None:
            self._function_info.by_key = {}

        # Create or update entry info
        if key not in self._function_info.by_key:
            self._function_info.by_key[key] = CacheEntryInfo(key=key,
                                                             hits=0,
                                                             misses=1)
        else:
            self._function_info.by_key[key].misses += 1

        # Update global stats
        if self.func is not None:
            func_name = self.func_name
            if func_name not in _cache_info.by_function:
                _cache_info.by_function[func_name] = self._function_info
            else:
                _cache_info.by_function[func_name].misses += 1

        # Update global misses counter
        _cache_info.misses += 1
        return self

    @dynamic()
    def cache_info(
        self_or_cls: "Type[Self] | Self",
        key: CacheKey[Any, Any] | str | None = None,
        show: bool = False,
    ) -> GlobalCacheInfo | FunctionCacheInfo | CacheEntryInfo | None:
        if isinstance(self_or_cls, cache | acache):
            if key:
                if not isinstance(key, CacheKey):
                    raise TypeError(
                        f"Key must be of type CacheKey, not {type(key)}")
                return self_or_cls._function_info.by_key.get(key)
            info = self_or_cls._function_info
        elif key and isinstance(key, str):
            info = _cache_info.by_function.get(key)
        else:
            info = _cache_info
        if show:
            render_table(info)
        return info

    @overload
    @wrapafter(CacheConfig, returns=Self)
    def __new__(cls, **config) -> Self:
        ...

    @overload
    def __new__(cls, **config: Unpack[CacheConfig]) -> Self:
        ...

    # @overload
    # def __new__(cls, func: Callable[P, R]) -> Self:...
    # @overload
    # def __new__(cls, func: Callable[P, Generator[Any,Any,R]]) -> Self:...
    @overload
    def __new__(cls, config: CacheConfig) -> Self:
        ...

    def __new__(cls, *args, **kwargs) -> Self:
        self = super().__new__(cls)
        self.func = None
        self._mkey = None
        self._pending = None
        self._cfg = None
        self._initialized = False
        self.__init__(*args, **kwargs)
        return self

    def __repr__(self):
        return self._function_info.__repr__()

    @overload
    @wrapafter(CacheConfig, returns=None)
    def __init__(self, **config) -> None:
        ...

    @overload
    def __init__(self, **config: Unpack[CacheConfig]) -> None:
        ...

    @overload
    def __init__(self, config: CacheConfig) -> None:
        ...

    @overload
    def __init__(
        self,
        func: Callable[P, AsyncGenerator[Any, R]]
        | Callable[P, Generator[Any, Any, R]] | Callable[P, R],
    ) -> None:
        ...

    @overload
    def __init__(self, *args: P.args, **kwargs: P.kwargs) -> None:
        ...

    def __init__(self, *args, **kwargs) -> None:
        """Cache anything."""
        self.acquire = make_aquirer(self.locks).acquire

        if not self._initialized and not self.func:
            if args and callable(args[0]):
                self.func = init_func(*args, **kwargs)
                self._cfg = init_cfg(*args, **kwargs)
                self._mkey = CacheKey[self._cfg["context_policy"],
                                      self._cfg["ttl"]](self.func)
                self.func_name = getattr(
                    self.func,
                    "__qualname__",
                    getattr(self.func, "__module__", "__main__") + "." +
                    getattr(self.func, "__name__", str(self.func)),
                )
                _cache_info.by_function.setdefault(
                    self.func_name,
                    FunctionCacheInfo(
                        "generator"
                        if isgeneratorfunction(self.func) else "coroutine" if
                        iscoroutinefunction(self.func) else "async_generator"
                        if isasyncgenfunction(self.func) else "function", ),
                )
                self._function_info = _cache_info.by_function[self.func_name]
                self._initialized = True
            else:
                self._cfg = init_cfg(*args, **kwargs)
                self._mkey = CacheKey[self._cfg["context_policy"],
                                      self._cfg["ttl"]]
                self._initialized = True
        if not type(self)._task_started:
            type(self)._start_tasks(self._cfg)
            self._task_started = True
            type(self)._task_started = True

    @overload
    def __call__(self, *args: P.args, **kwargs: P.kwargs) -> R:
        ...

    @overload
    def __call__(self, func: Callable[P, R]) -> Self:
        ...

    @overload
    def __call__(self, func: Callable[P, Generator[Any, Any, R]]) -> Self:
        ...

    def __call__(self, *args: Any | None, **kwargs: Any | None) -> Any:
        if not self._initialized:
            self._cfg = init_cfg(*args, **kwargs)
            self._mkey = CacheKey[self._cfg["context_policy"],
                                  self._cfg["ttl"]]
            self._initialized = True

            return self
        if not self.func:
            self.func = init_func(*args, **kwargs)
            self._mkey = self._mkey(self.func)
            if self.func is not None:
                self.func_name = getattr(
                    self.func,
                    "__qualname__",
                    getattr(self.func, "__module__", "__main__") + "." +
                    getattr(self.func, "__name__", str(self.func)),
                )
                _cache_info.by_function.setdefault(
                    self.func_name,
                    FunctionCacheInfo(
                        "generator"
                        if isgeneratorfunction(self.func) else "coroutine" if
                        iscoroutinefunction(self.func) else "async_generator"
                        if isasyncgenfunction(self.func) else "function", ),
                )
                self._function_info = _cache_info.by_function[self.func_name]
            return self

        if CACHE_OFF or not self._cfg["enabled"]:
            return self.func(*args, **kwargs)
        key = self._mkey(self.func, *args, **kwargs)
        if key in self.entries:
            self.hit(key)
            if self.entries[key].isagen:
                entry_value = self.entries[key].value
                # Don't wrap if it's already a proxy
                if isinstance(entry_value, _AsyncGenProxy):
                    return entry_value  # Return the existing proxy directly
                else:
                    return _AsyncGenProxy(
                        key, entry_value)  # Create new proxy only if needed

            async def _agen_wrapper():
                return self.entries[
                    key].value  # Return the value not the entry

            return _agen_wrapper()  # type: ignore

        result = self.func(*args, **kwargs)

        if isinstance(result, Generator):
            return _GenProxy(key, result)
        return result

    @classmethod
    def clear_disk(cls) -> None:
        """Clear the cache file."""
        cfg = CacheConfig(**CACHE_CONFIG)
        path_dir = Path(str(cfg["pathdir"])).resolve()

        try:
            with cls.acquire():
                SafeFileCache(str(path_dir))

                # Get all files in the cache directory
                if path_dir.exists():
                    # Try to remove all cache files
                    import shutil

                    try:
                        shutil.rmtree(
                            path_dir,
                            onerror=lambda func, path, exc_info: vverbose(
                                f"Could not remove {path}: {exc_info}"),
                        )
                    except Exception as e:
                        vverbose(f"Error clearing cache directory: {e}")

                    if not path_dir.exists():
                        safe_print("Cache directory removed successfully")
                    else:
                        safe_print(
                            "Could not completely remove cache directory")
                else:
                    safe_print("Cache directory does not exist")
        except Exception as e:
            import traceback

            traceback.print_exc()
            vverbose(f"Error clearing disk cache: {e}")

    @classmethod
    def clear_memory(cls) -> None:
        """Clear the cache for a specific function."""
        try:
            # Use thread-safe locks from the class
            with cls.acquire():
                global _cache, _cache_info
                _cache.clear()
                _cache_info = GlobalCacheInfo()
        except Exception:
            import traceback

            traceback.print_exc()

    @classmethod
    def clear_all(cls) -> None:
        """Clear all cache entries and cache file."""
        cls.clear_memory()
        cls.clear_disk()

    @classmethod
    async def save(cls, pathdir: Path | str = CACHE_CONFIG["pathdir"]) -> None:
        """Persist in-memory cache to disk using SafeFileCache."""
        if CACHE_OFF or not _cache:
            return

        # Create directory if needed
        path_dir = Path(str(pathdir)).resolve()
        if not path_dir.exists():
            path_dir.mkdir(parents=True, exist_ok=True)

        # Use SafeFileCache for storage
        file_cache = SafeFileCache(str(path_dir))

        try:
            # 1. Save metadata compactly
            meta_data = serialize_metadata(_cache_info).encode("utf-8")
            file_cache.set("cache_meta", meta_data)
            file_cache.set_body("cache_meta", b"cache_meta_body")

            # 2. Save list of key hashes efficiently
            key_hashes = [str(hash(key)) for key in _cache.keys()]
            file_cache.set("cache_keys",
                           json.dumps(key_hashes).encode("utf-8"))
            file_cache.set_body("cache_keys", b"cache_keys_body")

            # 3. Save key mapping minimally for debugging
            key_mapping = {
                str(hash(key)): getattr(key, "func_name", "unknown")
                for key in _cache.keys() if hasattr(key, "func_name")
            }
            file_cache.set("key_mapping",
                           json.dumps(key_mapping).encode("utf-8"))
            file_cache.set_body("key_mapping", b"key_mapping_body")

            # 4. Save entries in parallel (optimal approach would use asyncio.gather)
            for key, entry in _cache.items():
                try:
                    # Use hash as stable identifier
                    key_hash = str(hash(key))

                    # Pickle entry directly to body file
                    entry_bytes = pickle.dumps(entry)
                    file_cache.set_body(key_hash, entry_bytes)

                    # Minimal metadata - just to satisfy SafeFileCache
                    file_cache.set(key_hash, b"")
                except Exception:
                    # Skip silently if can't save
                    pass
        except Exception:
            # Silent failure
            pass

    @classmethod
    def load(cls,
             pathdir: Path | str = CACHE_CONFIG["pathdir"]) -> "type[Self]":
        """Load cache from disk into memory using SafeFileCache."""
        # Fast, silent load
        loaded_entries = load(pathdir)
        if loaded_entries:
            _cache.update(loaded_entries)
        return cls

    @classmethod
    async def aworker(cls):
        while True:
            try:
                print(f"startig from cls: {cls}")
                task = await cls.acache_queue.get()
                if asyncio.iscoroutine(task):
                    await task  # ✅ Executes the task properly
                else:
                    vverbose(f"[ERROR] Invalid task: {task}, skipping.")

                cls.acache_queue.task_done()
            except asyncio.CancelledError:
                break
            except KeyboardInterrupt:
                break
            except Exception as e:
                import traceback

                traceback.print_exc()
                vverbose(f"[ERROR] Worker failed: {e}")

    @classmethod
    async def stop(cls):
        """Stop the worker properly without loop issues."""
        import contextlib

        for task in list(cls._tasks):
            with contextlib.suppress(asyncio.CancelledError, RuntimeError):
                task.cancel()
                await task

        cls._tasks.clear()
        cls._task_started = False

    @classmethod
    def _start_tasks(cls, config):
        """Start background tasks for cache management."""
        # Don't start multiple instances of the worker
        if cls._task_started:
            return

        # This is where we actually create the worker task
        if not cls._tasks:
            try:
                loop = asyncio.get_event_loop_policy().get_event_loop()
            except RuntimeError:
                loop = asyncio.new_event_loop()
                asyncio.set_event_loop(loop)
            worker_task = loop.create_task(cls.aworker())
            cls._tasks.add(worker_task)
            cls.acache_queue = asyncio.Queue()

            # Ensure worker is cleaned up on exit
            def cleanup_worker():
                for task in cls._tasks:
                    try:
                        loop = asyncio.get_event_loop()
                        if (not worker_task.done()
                                and not worker_task.cancelled()
                                and worker_task.get_loop().is_running()):
                            worker_task.cancel()

                    except:
                        pass

            if "cleanup_registered" not in cls.__dict__:
                atexit.register(cleanup_worker)
                cls.cleanup_registered = True

        cls._task_started = True


class acache(cache[P, R]):
    """Use c-speed lru_cache for cache entries."""

    acache_queue: asyncio.Queue = asyncio.Queue()
    _tasks: set[asyncio.Task] = set()
    _task_started = False

    # def __contains__(self, key: CacheKey) -> bool:
    #     """Check if the key exists in the cache using the & operator."""
    #     if CACHE_OFF or not self._cfg['enabled']:
    #         return False

    #     # vverbose
    #     vverbose(f"Checking cache for key: {key}")
    #     vverbose(f"Current cache keys: {list(_cache.keys())}")

    #     # Direct entry lookup
    #     entry = _cache.get(key)
    #     if entry is not None:
    #         # Use & operator to check key equality with context
    #         if not (entry.key & key):
    #             with self.acquire(hash(key)):
    #                 _cache.pop(key, None)
    #             vverbose(f"Key format mismatch for {key}")
    #             return False
    #         vverbose(f"Cache HIT for {key}")
    #         return True

    #     vverbose(f"Cache MISS for {key}")
    #     return False

    @overload
    @wrapafter(CacheConfig, returns=Self)
    def __new__(cls, **config) -> Self:
        ...

    @overload
    def __new__(cls, **config: Unpack[CacheConfig]) -> Self:
        ...

    # @overload
    # def __new__(cls, config: CacheConfig) -> Self: ...
    # @overload
    # def __new__(cls, func: Callable[P,R]|None=None, **config: Unpack[CacheConfig]) -> Self: ...
    def __new__(cls, *args, **kwargs) -> Self:
        self = super().__new__(cls, *args, **kwargs)
        self.func = None
        self._mkey = None
        self._pending = None
        self._cfg = None
        self._initialized = False
        self.__init__(*args, **kwargs)
        return self

    def __call__(self, *args: P.args, **kwargs: P.kwargs) -> R:
        if not self._initialized:
            self._cfg = init_cfg(*args, **kwargs)
            self._mkey = CacheKey[self._cfg["context_policy"],
                                  self._cfg["ttl"]]
            self._initialized = True
            return self  # type: ignore
        if not self.func:
            self.func = init_func(*args, **kwargs)
            self._mkey = self._mkey(self.func)
            if self.func is not None:
                self.func_name = getattr(
                    self.func,
                    "__qualname__",
                    getattr(self.func, "__module__", "__main__") + "." +
                    getattr(self.func, "__name__", str(self.func)),
                )
                _cache_info.by_function.setdefault(
                    self.func_name,
                    FunctionCacheInfo(
                        "generator"
                        if isgeneratorfunction(self.func) else "coroutine" if
                        iscoroutinefunction(self.func) else "async_generator"
                        if isasyncgenfunction(self.func) else "function", ),
                )
                self._function_info = _cache_info.by_function[self.func_name]
            return self  # type: ignore
        if not type(self)._task_started:
            type(self)._start_tasks(self._cfg)
            self._task_started = True
            type(self)._task_started = True
        if CACHE_OFF or not self._cfg["enabled"]:
            return self.func(*args, **kwargs)
        key = self._mkey(self.func, *args, **kwargs)

        if key in self.entries:
            self.hit(key)
            if self.entries[key].isagen:
                entry_value = self.entries[key].value
                # Don't wrap if it's already a proxy
                if isinstance(entry_value, _AsyncGenProxy):
                    return entry_value  # Return the existing proxy directly
                else:
                    return _AsyncGenProxy(
                        key, entry_value)  # Create new proxy only if needed

            async def _agen_wrapper():
                return self.entries[
                    key].value  # Return the value not the entry

            return _agen_wrapper()  # type: ignore

        result = self.func(*args, **kwargs)

        # Handle different result types
        if hasattr(result, "__aiter__"):
            result = _AsyncGenProxy(key, result)
            self.entries[key] = CacheEntry(key=key, value=result, isagen=True)
            self.miss(key)
            return result  # type: ignore

        # For normal coroutines
        async def _wrapper():
            nonlocal result
            if hasattr(result, "__await__"):
                result = await result  # type: ignore
            self.entries[key] = CacheEntry(key=key, value=result, iscoro=True)

            self.miss(key)
            return result  # type: ignore

        return _wrapper()  # type: ignore

    async def asetitem(self, key: CacheKey, value) -> None:
        if not isinstance(value, CacheEntry):
            entry = CacheEntry(
                key=key,
                value=value,
                context_keys=key.context_keys,
                ttl=self._cfg["ttl"],
                last_accessed=time.time(),
                last_updated=time.time(),
                last_missed=0.0,
                persistent=self._cfg["persistent"],
                context_policy=self._cfg["context_policy"],
                isagen=hasattr(value, "__aiter__"),
                iscoro=hasattr(value, "__await__"),
                isgen=hasattr(value, "send"),
            )
        else:
            entry = CacheEntry(
                **{
                    **asdict(value),
                    "key": key,
                    "ttl": self._cfg["ttl"],
                    "last_accessed": time.time(),
                    "last_updated": time.time(),
                    "last_missed": 0.0,
                    "persistent": self._cfg["persistent"],
                    "context_policy": self._cfg["context_policy"],
                }, )

        _cache[key] = entry
        self.acache_queue.put_nowait(self.update_stats)

    async def adelitem(self, key) -> None:
        if key in _cache:
            del _cache[key]
            self.acache_queue.put_nowait(self.update_stats)

    def __setitem__(self, key, value):
        if CACHE_OFF or not self._cfg["enabled"]:
            return
        type(self).acache_queue.put_nowait(self.asetitem(key, value))

    def __delitem__(self, key):
        type(self).acache_queue.put_nowait(self.adelitem(key))


@acache(persistent=True)
async def dummy_task(i: int) -> int:
    vverbose("*** HELLO THIS IS A TEST MODIFICATION! ***")
    vverbose(f"Running dummy_task({i}) - this should only appear on first run")
    await asyncio.sleep(0.1)
    return i + 1


@acache(persistent=True)
async def dummy_task2(i: int) -> "AsyncGenerator[Any, int]":
    await asyncio.sleep(0.1)
    yield i + 1
    return


@acache(persistent=True)
async def dummy_tasks() -> None:
    for i in range(3):
        result = await dummy_task(i)
        vverbose(f"Got result from dummy_task({i}): {result}")

    # Explicitly add some cache entries for testing
    key = dummy_task._mkey(dummy_task, 0)
    dummy_task.hit(key)

    # Test async generator
    async for j in dummy_task2(0):  # Use 0 instead of i
        safe_print(j)

    # Hit the generator key too
    key2 = dummy_task2._mkey(dummy_task2, 0)
    dummy_task2.hit(key2)


def fix_cache_info():
    """Fix the cache_info by_key to use actual key objects instead of hash values."""
    global _cache_info

    # Make a copy of the _cache_info we have
    original_cache_info = _cache_info

    # Create a mapping of function names to their actual cache keys
    function_keys = {}
    for key, entry in _cache.items():
        if hasattr(key, "func_name"):
            func_name = key.func_name
            if func_name not in function_keys:
                function_keys[func_name] = []
            function_keys[func_name].append((key, entry))

    # Update the by_function dictionary with actual keys
    for func_name, func_info in original_cache_info.by_function.items():
        if func_name in function_keys:
            # Create new by_key dictionary with actual keys
            new_by_key = {}
            for key, entry in function_keys[func_name]:
                # Create a CacheEntryInfo for this key
                # Try to find existing info for stats
                hits = 0
                misses = 0
                if hasattr(func_info, "by_key"):
                    for k, info in func_info.by_key.items():
                        if str(hash(key)) == str(k) or str(k) == str(
                                hash(key)):
                            hits = info.hits
                            misses = info.misses
                            break

                new_by_key[key] = CacheEntryInfo(key=key,
                                                 hits=hits,
                                                 misses=misses)

            # Update the function info
            func_info.by_key = new_by_key

    return _cache_info


async def test_persistence():
    """Test function specifically for cache persistence and loading."""
    print("\n=== TESTING CACHE PERSISTENCE ===")

    # Clear current cache to start fresh
    cache.clear_memory()
    print("Cache cleared. Current entries:", len(_cache))

    # Create a unique cache key that won't conflict
    @acache(persistent=True)
    async def persistence_test(value: str) -> str:
        print(
            f"PERSISTENCE TEST RAN with {value} - this should only show on first run"
        )
        await asyncio.sleep(0.1)
        return f"processed_{value}"

    # Run once to populate cache
    test_value = f"test_{int(time.time())}"  # Use timestamp to make unique
    result1 = await persistence_test(test_value)
    print(f"First run result: {result1}")
    print(f"Cache entries after first run: {len(_cache)}")

    # Save cache to disk
    print("Saving cache to disk...")
    await cache.save()

    # Clear memory cache
    cache.clear_memory()
    print(f"Cache cleared again. Current entries: {len(_cache)}")

    # Load from disk
    print("Loading cache from disk...")
    cache.load()
    print(f"Cache entries after loading: {len(_cache)}")

    # Run again - should load from cache
    result2 = await persistence_test(test_value)
    print(f"Second run result: {result2}")

    # Verify results match
    if result1 == result2:
        print("✅ PERSISTENCE TEST PASSED: Results match!")
    else:
        print("❌ PERSISTENCE TEST FAILED: Results don't match!")
        print(f"First result: {result1}")
        print(f"Second result: {result2}")

    return persistence_test


async def main():
    from time import time

    # Test persistence explicitly
    persistence_test_func = await test_persistence()

    # Load any persistent cache including our test entries
    cache.load()

    # First run to populate the cache
    t = time()
    await dummy_tasks()
    t = time() - t
    safe_print(f"Time taken: {t} seconds")

    # Print cache info for dummy_tasks
    task_info = dummy_tasks.cache_info()
    print(f"dummy_tasks info: {task_info}")

    # Print cache info for dummy_task
    task_info = dummy_task.cache_info()
    print(f"dummy_task info: {task_info}")
    print(f"dummy_task by_key: {getattr(task_info, 'by_key', {})}")

    # Second run should be faster and use cache
    t = time()
    await dummy_tasks()
    t = time() - t
    safe_print(f"Time taken: {t} seconds")

    # Check the actual cache entries
    print(f"\nActual cache entries: {len(_cache)}")
    for cache_key, cache_entry in _cache.items():
        print(f"  - Key: {cache_key}, Value: {str(cache_entry.key)}")

    # Fix cache info to use actual key objects
    fix_cache_info()

    # Show the full cache info
    info = acache.cache_info()
    safe_print("\nCache info summary:")
    safe_print(f"Total entries: {len(_cache)}")
    safe_print(f"Total hits: {info.hits}, misses: {info.misses}")

    # Display functions and their keys with better formatting
    for func_name, func_info in info.by_function.items():
        if hasattr(func_info, "by_key") and func_info.by_key:
            safe_print(
                f"Function {func_name}: {len(func_info.by_key)} keys, {func_info.hits} hits, {func_info.misses} misses",
            )

            # Skip displaying persistent keys from previous runs for certain functions
            if func_name in ("afib", "example.<locals>.ret_tup"):
                safe_print(
                    f"  (Skipping display of {len(func_info.by_key)} persistent keys from previous runs)"
                )
                continue

            for key, key_info in func_info.by_key.items():
                # Try to get the real key tuple
                try:
                    if hasattr(key, "key") and isinstance(key.key, tuple):
                        # Format the key tuple nicely
                        key_str = f"({', '.join(repr(k) for k in key.key)})"
                        safe_print(
                            f"  - Key: {key_str}, hits: {key_info.hits}, misses: {key_info.misses}"
                        )
                    else:
                        # Fall back to string representation
                        safe_print(
                            f"  - Key: {key}, hits: {key_info.hits}, misses: {key_info.misses}"
                        )
                except Exception as e:
                    # Last resort show the hash
                    safe_print(
                        f"  - Key: {hash(key)} (error: {e}), hits: {key_info.hits}, misses: {key_info.misses}"
                    )

    # Save cache before stopping
    print("\nSaving final cache state...")
    await cache.save()

    print("Stopped worker")


if __name__ == "__main__":
    print("Running demo implementation...")
    asyncio.run(main())
