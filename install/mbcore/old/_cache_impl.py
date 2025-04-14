# from __future__ import annotations

# import asyncio
# import pickle
# import sys
# import threading
# import time
# from collections import defaultdict
# from collections.abc import Mapping,AsyncGenerator
# from dataclasses import asdict
# from inspect import iscoroutinefunction
# from itertools import chain
# from os import getenv
# from pathlib import Path
# import json
# import base64
# import atexit
# from rich.console import Console
# from rich.table import Table
# from rich.text import Text
# from typing_extensions import Any, Callable, Generic, Self, Type, Unpack, cast, overload

# from mbcore.config import DEFAULT_CACHE_CONFIG as CACHE_CONFIG
# from mbcore.config import CacheConfig
# from mbcore.even._internal._cache import (
#     AR,
#     GR,
#     CacheEntry,
#     CacheEntryInfo,
#     FunctionCacheInfo,
#     GlobalCacheInfo,
#     Hash,
#     P,
#     R,
#     _AsyncGenProxy,
#     _cache,
#     make_cachable,
#     notnone,
#     safe_print,
# )
# from mbcore.even._internal._trees import CacheKey, atreemap
# from mbcore.recipes import first_true
# from mbcore.threadsafe import make_aquirer


# # Restore SafeFileCache import
# from pip._internal.network.cache import SafeFileCache

# CACHE_OFF = getenv("MB_CACHE_OFF",False)

# # Initialize file cache for safe file operations
# _file_cache = None

# def isvverbose() -> bool:
#     import sys

#     return any(arg in sys.argv for arg in ("-vv", "--vverbose", "-dd", "--ddebug"))


# def isverbose() -> bool:
#     import sys

#     return any(arg in sys.argv for arg in ("-v", "--verbose", "-d", "--debug","-dd","-vv","--ddebug","--vverbose"))


# def get_info(info,show=False):
#         from dataclasses import asdict

#         from rich.box import Box
#         from rich.table import Table
#         NO_BOX = Box("    \n" * 8)

#         keys = asdict(info).keys()
#         table = Table(*map(str.upper,keys),pad_edge=False,show_edge=False,highlight=True,box=NO_BOX,title="\n")
#         if show:
#             safe_print(table)
#         table.add_row(*map(str,asdict(info).values()))
#         return info

# def init_func(*args, **kwargs):

#     func = first_true(callable,chain(args,kwargs.values()))

#     return func

# def init_cfg(*args, **kwargs):
#     return CacheConfig(**{**CACHE_CONFIG,**{k: v for k, v in kwargs.items() if k in CACHE_CONFIG}})


# def summarize(cache,size):
#     def _summarize(a):
#         key, entry = a  # Unpack the key-value pair from cache items
#         func = cache.func
#         args = entry
#         func_name = func.__qualname__ if hasattr(func, '__qualname__') else str(func)
#         # Format the entry details
#         details = {
#             'func': func_name,
#             'args': args,
#             'last_accessed': time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(getattr(entry, 'last_accessed', 0))),
#             'ttl': getattr(entry, 'ttl', 0),
#             'persistent': getattr(entry, 'persistent', False),
#         }
#         return f"{details['func']}(args={details['args']}, last_accessed={details['last_accessed']}, ttl={details['ttl']}, persistent={details['persistent']}"

#     sum = (f"Cache size: {size / 1e6:.2f}MB. (mb cache) ")
#     sum += (f"Loaded {len(_cache)} entries with last 10 entries:" + '\n' + '\n'.join(map(_summarize, list(_cache.items())[-10:])))
#     return sum

# def render_table(
#     data: Any,
#     title: str | None = None,
#     omit_keys: set[str] | None = None,
#     summarize_func: Callable[[Any], str] | None = None,
#     max_depth: int = 2,
#     console: Console | None = None,
# ) -> Table:
#     """Render any JSON-like data into a human-readable Rich table.

#     Args:
#         data: The input JSON-like object (dict, list, nested structures).
#         title: Optional title for the table.
#         omit_keys: Set of keys to omit from the table.
#         summarize_func: Optional function to summarize large objects.
#         max_depth: Maximum depth to expand nested structures.
#         console: Optional Rich console instance.

#     Returns:
#         Rich Table object

#     """
#     # Import NO_BOX from a consistent location
#     from mbcore.display import NO_BOX

#     def is_atomic(value):
#         """Check if the value is an atomic type (not iterable)."""
#         return (
#             isinstance(value, (str, int, float, bool, type(None))) or
#             hasattr(value, "__dataclass_fields__") or
#             callable(value)
#         )

#     def process_value(value, depth=0):
#         """Format values, applying summarization if needed."""
#         if value is None:
#             return Text("None", style="dim")

#         if hasattr(value, "__dataclass_fields__"):
#             value = asdict(value)

#         if isinstance(value, CacheKey):
#             value = value.key

#         if callable(value):
#             return Text(f"<function {getattr(value, '__qualname__', repr(value))}>", style="magenta")

#         if is_atomic(value) and not isinstance(value, dict):
#             return Text(str(value).replace("PosixPath","").replace("Path",""))

#         if depth >= max_depth:
#             if summarize_func and callable(summarize_func):
#                 return Text(summarize_func(value).replace("PosixPath","").replace("Path",""))
#             return Text(f"<{type(value).__qualname__} with {len(value) if hasattr(value, '__len__') else '?'} items>", style="dim")

#         if isinstance(value, Mapping):
#             return render_nested_table(value, depth + 1)

#         if isinstance(value, (list, tuple, set)):
#             if not value:
#                 return Text("[]", style="dim")
#             items = list(value)
#             if len(items) > 5:
#                 items_text = "\n-".join(str(v) for v in items[:5]).replace("PosixPath","").replace("Path","").replace(str(Path.cwd().resolve()),"")
#                 return Text(f"[{items_text}, ... {len(items)-5} more]", style="blue")
#             items_text = "\n-".join(str(v).replace("PosixPath","").replace("Path","").replace(str(Path.cwd().resolve()),"") for v in items[:5])
#             return Text(f"[{items_text}]", style="blue")
#         # Fallback for other types
#         return Text(str(value).replace("PosixPath","").replace("Path","").replace(str(Path.cwd().resolve()),""))

#     def render_nested_table(nested_data: Mapping, depth=0):
#         """Render a nested dictionary as a separate table."""
#         if not nested_data:
#             return Text("{}", style="dim")

#         table = Table(show_edge=False, box=NO_BOX, expand=True,width=300)

#         # Add columns
#         keys = list(nested_data.keys())
#         if not keys:
#             return Text("{}", style="dim")

#         for key in keys[:4]:
#             if omit_keys and key in omit_keys:
#                 continue
#             key_str = str(getattr(key, "key", key)).replace("PosixPath","").replace("Path","")[:20]
#             table.add_column(key_str, style="cyan")

#         # Add rows
#         row_values = []
#         for key in keys:
#             if omit_keys and key in omit_keys:
#                 continue

#             value = nested_data[key]
#             processed = process_value(value, depth)

#             # Add to row values list, handling any type of renderable
#             row_values.append(processed)

#         if row_values:
#             # Any renderable can be used in add_row
#             table.add_row(*row_values)

#         return table

#     # Handle different input types
#     if isinstance(data, Mapping):
#         table = render_nested_table(data)
#         if isinstance(table, Text):
#             t = Table(box=NO_BOX, show_edge=False, expand=True,width=120)
#             t.add_column("Value",width=80)
#             t.add_row(table)
#             return t
#         return table

#     if isinstance(data, (list, tuple, set)) and data:
#         try:
#             # Try to get column keys from first item if it's a dict
#             first_item = next(iter(data), None)
#             if isinstance(first_item, dict):
#                 # Dictionary collection - create a table with columns for each key
#                 table = Table(show_edge=False, box=NO_BOX, expand=True)

#                 # Add index column
#                 table.add_column("Index", style="bold cyan")

#                 # Add columns for each key in the dictionaries
#                 column_keys = list(first_item.keys())
#                 for key in column_keys:
#                     if omit_keys and key in omit_keys:
#                         continue
#                     table.add_column(str(key), style="bold cyan")

#                 # Add rows for each item
#                 for i, item in enumerate(data):
#                     if not isinstance(item, dict):
#                         continue

#                     row = [Text(str(i))]
#                     for key in column_keys:
#                         if omit_keys and key in omit_keys:
#                             continue
#                         if key in item:
#                             processed = process_value(item[key], 0)
#                             # Any renderable (Text or Table) can be added directly
#                             row.append(processed)  # type: ignore # Rich can handle both Text and Table
#                         else:
#                             row.append(Text("-", style="dim"))

#                     # Any renderable can be used in add_row
#                     table.add_row(*row)
#                 return table
#             # List of non-dictionary items
#             table = Table(show_edge=False, box=NO_BOX, expand=True)
#             table.add_column("Index", style="bold cyan")
#             table.add_column("Value", style="bold cyan")

#             for i, item in enumerate(data):
#                 processed = process_value(item, 0)
#                 # Any renderable can be used in add_row
#                 table.add_row(Text(str(i)), processed)
#             return table
#         except (StopIteration, TypeError, ValueError, AttributeError):
#             # Fallback for any errors in handling collections
#             table = Table(show_edge=False, box=NO_BOX, expand=True)
#             table.add_column("Value", style="bold yellow")
#             table.add_row(Text(f"<{type(data).__qualname__} with {len(data)} items>", style="dim"))
#             return table

#     elif is_atomic(data):
#         table = Table(box=NO_BOX, show_edge=False, expand=True)
#         table.add_column("Value", style="bold yellow")
#         table.add_row(Text(str(data)))
#         return table

#     else:
#         # Fallback for unsupported types
#         table = Table(box=NO_BOX, show_edge=False, expand=True)
#         table.add_column("Type", style="bold red")
#         table.add_column("Representation", style="bold yellow")
#         table.add_row(
#             Text(type(data).__qualname__),
#             Text(str(data)),
#         )
#         return table


# _file_cache = SafeFileCache(str(Path(CACHE_CONFIG['pathdir'])))
# _cache_info: GlobalCacheInfo = GlobalCacheInfo()

# def serialize_metadata(meta: GlobalCacheInfo) -> bytes:
#     """Serialize metadata to JSON-compatible format."""
#     try:
#         # Convert to dict for JSON serialization
#         meta_dict = {
#             "hits": meta.hits,
#             "misses": meta.misses,
#             "currsize": meta.currsize,
#             "currmemory": meta.currmemory,
#             "by_function": {
#                 k: {
#                     "hits": v.hits,
#                     "misses": v.misses,
#                     "currsize": v.currsize,
#                     "type": v.type
#                 } for k, v in meta.by_function.items()
#             }
#         }
#         return json.dumps(meta_dict).encode('utf-8')
#     except:
#         # Fall back to pickle if JSON fails
#         return base64.b64encode(pickle.dumps(meta))

# def deserialize_metadata(data):
#     """Deserialize metadata from JSON or pickle format."""
#     try:
#         # Try JSON first
#         data_dict = json.loads(data)
#         # Convert to GlobalCacheInfo
#         result = GlobalCacheInfo()
#         result.hits = data_dict.get("hits", 0)
#         result.misses = data_dict.get("misses", 0)
#         result.currsize = data_dict.get("currsize", 0)
#         result.currmemory = data_dict.get("currmemory", "0MB")
#         # Create function info entries
#         for func_name, func_data in data_dict.get("by_function", {}).items():
#             result.by_function[func_name] = FunctionCacheInfo(
#                 func_data.get("type", "function"),
#                 hits=func_data.get("hits", 0),
#                 misses=func_data.get("misses", 0),
#                 currsize=func_data.get("currsize", 0)
#             )
#         return result
#     except:
#         # Fall back to pickle
#         try:
#             data_obj = pickle.loads(base64.b64decode(data))
#             if isinstance(data_obj, GlobalCacheInfo):
#                 return data_obj
#             # If we got a dict from pickle, convert it
#             result = GlobalCacheInfo()
#             # Copy attributes if they exist
#             for attr in ["hits", "misses", "currsize", "currmemory"]:
#                 if hasattr(data_obj, attr):
#                     setattr(result, attr, getattr(data_obj, attr))
#             # Copy function info
#             if hasattr(data_obj, "by_function"):
#                 for func_name, func_data in data_obj.by_function.items():
#                     result.by_function[func_name] = func_data
#             return result
#         except:
#             # If all fails, return an empty GlobalCacheInfo
#             return GlobalCacheInfo()

# # Load cache on startup (unchanged)

# def load(pathdir: Path | str = CACHE_CONFIG['pathdir']) -> dict[Hash, CacheEntry]:
#     """Load cache from SafeFileCache into memory.

#     Returns a dictionary of cache entries. The keys maintain their original type.
#     """
#     if CACHE_OFF:
#         return {}

#     # Use SafeFileCache for storage
#     CacheConfig(**CACHE_CONFIG)
#     path_dir = Path(str(pathdir)).resolve()
#     file_cache = SafeFileCache(str(path_dir))

#     d = {}
#     try:
#         # 1. Load global metadata
#         cache_meta = file_cache.get("cache_meta")
#         if cache_meta:
#             global _cache_info
#             try:
#                 _cache_info = deserialize_metadata(cache_meta.decode('utf-8'))
#                 if isverbose():
#                     safe_print("[cyan][DEBUG][/cyan] Loaded cache metadata successfully")
#             except Exception as e:
#                 if isverbose():
#                     safe_print(f"[yellow][WARN][/yellow] Could not load cache metadata: {e}")

#         # 2. Load the key hashes
#         cache_keys_data = file_cache.get("cache_keys")
#         if cache_keys_data:
#             try:
#                 key_hashes = json.loads(cache_keys_data.decode('utf-8'))
#                 if isverbose():
#                     safe_print(f"[cyan][DEBUG][/cyan] Found {len(key_hashes)} keys in cache")

#                 # 3. Load key mapping for debugging
#                 mapping_data = file_cache.get("key_mapping")
#                 if mapping_data:
#                     try:
#                         json.loads(mapping_data.decode('utf-8'))
#                     except:
#                         if isverbose():
#                             safe_print("[yellow][WARN][/yellow] Could not load key mapping")

#                 # 4. Load each entry by its hash key
#                 for key_hash in key_hashes:
#                     try:
#                         # Get metadata
#                         metadata = file_cache.get(key_hash)
#                         # Get entry data as binary file
#                         body_file = file_cache.get_body(key_hash)

#                         if metadata and body_file:
#                             try:
#                                 # Read the full body data
#                                 entry_data = body_file.read()
#                                 body_file.close()

#                                 # Deserialize the full entry
#                                 entry = pickle.loads(entry_data)

#                                 # The key is stored in the entry itself
#                                 if hasattr(entry, 'key'):
#                                     key = entry.key
#                                     d[key] = entry

#                             except Exception as e:
#                                 if isverbose():
#                                     safe_print(f"[red][ERROR][/red] Could not load cache entry {key_hash}: {e}")
#                     except Exception as e:
#                         if isverbose():
#                             safe_print(f"[red][ERROR][/red] Error accessing key {key_hash}: {e}")
#             except Exception as e:
#                 if isverbose():
#                     safe_print(f"[red][ERROR][/red] Could not load cache keys: {e}")

#         if d:
#             if isverbose():
#                 safe_print(f"Loaded {len(d)} cache entries")
#         elif isvverbose():
#             safe_print(f"[yellow][WARN][/yellow] No cache entries loaded from {pathdir}")
#     except Exception as e:
#         safe_print(f"[red][ERROR][/red] Could not load cache: {e}")
#         if isverbose():
#             import traceback
#             traceback.print_exc()

#     return d


# def tree_key_map(func, tree):
#     if isinstance(tree, dict):
#         return {func(k): tree_key_map(func, v) for k, v in tree.items()}
#     if isinstance(tree, list):
#         return [tree_key_map(func, v) for v in tree]
#     return tree

# async def make_cache_tree(cache_dict, filepath):
#     """Process cache dictionary for serialization."""
#     if isvverbose():
#         safe_print(f"[cyan][DEBUG][/cyan] Processing cache with {len(cache_dict)} entries.")

#     # Create a more compact version of the cache for serialization
#     compact_cache = await atreemap(make_cachable, cache_dict)
#     serializable = notnone(compact_cache)

#     if isverbose():
#         safe_print(f"[cyan][DEBUG][/cyan] Processed {len(serializable)} cache entries")

#     return serializable

#     # with Path(filepath).open("wb") as f:
#     #     pickle.dump(serializable, f)
#     # json_path = filepath.parent / "cache_info.json"
#     # with json_path.open("w") as f:
#     #     json.dump(tree_key_map(lambda x: x._func_name if isinstance(x,CacheKey) else x,_cache_info), f, indent=4)


# class ReprMeta(type):
#     def __repr__(cls):

#         if not _cache:
#             return "(empty)"

#         # Instead of rendering the full table, just show a summary
#         cache_size = sum(sys.getsizeof(v) for v in _cache.values()) / 1e6
#         num_entries = len(_cache)

#         # Get the top 5 most frequently accessed cache entries
#         entries_by_hits = sorted(
#             [(k, v) for k, v in _cache.items() if hasattr(v, "last_accessed")],
#             key=lambda x: getattr(x[1], "last_accessed", 0),
#             reverse=True
#         )[:5]

#         # Format a compact representation
#         summary = [
#             f"Cache: {num_entries} entries, {cache_size:.2f}MB",
#         ]

#         if entries_by_hits:
#             summary.append("Recent entries:")
#             for key, entry in entries_by_hits:
#                 func_name = getattr(key, "_func_name", "unknown")
#                 accessed = time.strftime("%H:%M:%S", time.localtime(getattr(entry, "last_accessed", 0)))
#                 summary.append(f"  {func_name} (accessed: {accessed})")

#         return "\n".join(summary)


# class cache(Generic[P, R],metaclass=ReprMeta):
#     __slots__ = ("acquire", "_pending", "func", "_cfg", "_mkey","_initialized","__dict__","_function_info")
#     locks: defaultdict[str|int,threading.Lock | asyncio.Lock] = defaultdict(lambda: threading.Lock())
#     _info = _cache_info
#     _tasks = set()
#     _task_started = False
#     acache_queue = asyncio.Queue()

#     def __contains__(self, key: CacheKey) -> bool:
#         """Check if the key exists in the cache using the & operator."""
#         if CACHE_OFF or not self._cfg['enabled']:
#             if isverbose():
#                 safe_print(f"[yellow][CACHE][/yellow] Cache is disabled for key {key}")
#             return False

#         # Direct entry lookup
#         entry = _cache.get(key)
#         if entry is not None:
#             # Use & operator to check key equality with context
#             if not (entry.key & key):
#                 if isverbose():
#                     safe_print(f"[yellow][CACHE][/yellow] Key format mismatch for {key}")
#                 _cache.pop(key, None)
#                 return False
#             if isverbose():
#                 safe_print(f"[green][CACHE HIT][/green] Direct match for key {key}")
#             return True

#         # If direct lookup fails, check other keys
#         if isverbose():
#             safe_print(f"[yellow][CACHE][/yellow] Direct lookup failed, checking {len(_cache)} other keys")
#         for stored_key in _cache:
#             # Use & operator for context-aware comparison
#             if stored_key & key:
#                 if isverbose():
#                     safe_print(f"[green][CACHE HIT][/green] Found matching key {stored_key} for {key}")
#                 return True

#         if isverbose():
#             safe_print(f"[red][CACHE MISS][/red] No match found for key {key}")
#         return False


#     def __getitem__(self, key):
#         # First try direct lookup
#         entry = _cache.get(key)
#         if entry:
#             if not (entry.key & key):
#                 return _cache.pop(key)
#             return entry

#         raise KeyError(key)

#     @property
#     def entries(self):
#         return _cache

#     def __setitem__(self, key: CacheKey, value):
#         if not isinstance(value, CacheEntry):
#             entry = CacheEntry(
#                 key=key,
#                 value=value,
#                 context_keys=key.context_keys,
#                 ttl=self._cfg['ttl'],
#                 last_accessed=time.time(),
#                 last_updated=time.time(),
#                 last_missed=0.0,
#                 isagen=hasattr(value, "__aiter__"),
#                 iscoro=hasattr(value, "__await__"),
#                 persistent=self._cfg['persistent'],
#                 context_policy=self._cfg['context_policy'],
#             )
#         else:
#             entry = value
#         with self.acquire(hash(key)):
#             _cache[key] = entry
#         if hasattr(self, '_function_info'):
#             self._function_info.currsize += 1
#             # Update global stats too
#             _cache_info.currsize = len(_cache)
#             size = sum(sys.getsizeof(v) for v in _cache.values())
#             _cache_info.currmemory = f"{size / 1e6:.2f}MB."

#     def __delitem__(self, key):
#         with self.acquire(hash(key)):
#             del _cache[key]
#             if hasattr(self, '_function_info'):
#                 self._function_info.currsize -= 1
#                 # Update global stats too
#                 _cache_info.currsize = len(_cache)
#                 size = sum(sys.getsizeof(v) for v in _cache.values())
#                 _cache_info.currmemory = f"{size / 1e6:.2f}MB."


#     def hit(self, key: CacheKey[Any,Any]) -> Self:
#         """Record that a key was accessed."""
#         if CACHE_OFF or not self._cfg['enabled']:
#             return self
#         self._function_info.by_key.setdefault(key, CacheEntryInfo(key=key)).hits += 1
#         self._function_info.hits += 1
#         if self.func is not None:
#             _cache_info.by_function.setdefault(f"{self.func.__qualname__}", self._function_info).hits += 1
#         _cache_info.hits += 1
#         return self

#     def miss(self, key: CacheKey[Any,Any]) -> "Self":
#         """Record that a key was missed."""
#         if CACHE_OFF or not self._cfg['enabled']:
#             return self
#         self._function_info.by_key.setdefault(key, CacheEntryInfo(key=key)).misses += 1
#         self._function_info.misses += 1
#         if self.func is not None:
#             _cache_info.by_function.setdefault(f"{self.func.__qualname__}", self._function_info).misses += 1
#         _cache_info.misses += 1
#         return self


#     @dynamic()
#     def cache_info(self_or_cls: "Type[Self] | Self", key: CacheKey[Any,Any]|str|None = None,show:bool=False) -> GlobalCacheInfo | FunctionCacheInfo | CacheEntryInfo | None:
#         if isinstance(self_or_cls, cache|acache):

#             if key:
#                 if not isinstance(key, CacheKey):
#                     raise TypeError(f"Key must be of type CacheKey, not {type(key)}")
#                 return self_or_cls._function_info.by_key.get(key)
#             info = self_or_cls._function_info
#         elif key:
#             if not isinstance(key, str):
#                 raise TypeError(f"Key must be of type str, not {type(key)}")

#             info = _cache_info.by_function.get(key)
#         else:
#             info = _cache_info
#         if show:
#             render_table(info)
#         return info


#     @overload
#     @wrapafter(CacheConfig,returns=Self)
#     def __new__(cls, **config: Unpack[CacheConfig]) -> Self: ...
#     @overload
#     def __new__(cls,**config: Unpack[CacheConfig]) -> Self: ...
#     @overload
#     def __new__(cls, func: Callable[P, AR[R] | R | GR[R]]) -> Self: ...

#     def __new__(cls, *args, **kwargs) -> Self:

#         self = super().__new__(cls)
#         self.func = None
#         self._mkey = None
#         self._pending = None
#         self._cfg = None
#         self._initialized = False

#         self.__init__(*args, **kwargs)
#         return self


#     def __repr__(self):
#         return self._function_info.__repr__()

#     @overload
#     def __init__(self, **config) -> None: ...
#     @overload
#     def __init__(self, func: Callable[P, AR[R] | R | GR[R]]) -> None: ...
#     def __init__(self, *args, **kwargs) -> None:
#         """Cache anything."""
#         self.acquire = make_aquirer(self.locks).acquire
#         if not self._initialized and not self.func:
#             if args and callable(args[0]):
#                 self.func = init_func(*args, **kwargs)
#                 self._cfg = init_cfg(*args, **kwargs)
#                 self._mkey = CacheKey[self._cfg['context_policy'],self._cfg["ttl"]](self.func)
#                 _cache_info.by_function[f"{self.func.__qualname__}"]  = FunctionCacheInfo("function" if not hasattr(self.func,"send") else "generator")
#                 self._function_info = _cache_info.by_function[f"{self.func.__qualname__}"]
#                 self._initialized = True
#             else:

#                 self._cfg = init_cfg(*args, **kwargs)
#                 self._mkey = CacheKey[self._cfg['context_policy'],self._cfg["ttl"]]
#                 self._initialized = True


#     @overload
#     def __call__(self: Callable[P, R], *args: P.args, **kwargs: P.kwargs) -> R: ...
#     @overload
#     def __call__(self: Callable[P, AR], *args: P.args, **kwargs: P.kwargs) -> AR[R]: ...
#     @overload
#     def __call__(self: Callable[P, GR], *args: P.args, **kwargs: P.kwargs) -> GR[R]: ...
#     def __call__(self, *args: P.args, **kwargs: P.kwargs):


#         if not self._initialized:
#             self._cfg = init_cfg(*args, **kwargs)
#             self._mkey = CacheKey[self._cfg['context_policy'],self._cfg["ttl"]]
#             self._initialized = True
#             return self
#         if not self.func:

#             self.func = init_func(*args, **kwargs)
#             self._mkey = self._mkey(self.func)
#             if self.func is not None:
#                 func_name = getattr(self.func, "__qualname__", "unknown")
#                 _cache_info.by_function[func_name] = FunctionCacheInfo(
#                     "function" if not iscoroutinefunction(self.func) and not hasattr(self.func, "__await__")
#                     and not hasattr(self.func, "__aiter__") else "async_generator"
#                     if hasattr(self.func, "__aiter__") else "coroutine"
#                 )
#                 self._function_info = _cache_info.by_function[func_name]
#             return self

#         if CACHE_OFF or not self._cfg['enabled']:
#             return self.func(*args, **kwargs)
#         key = self._mkey(self.func, *args, **kwargs)

#         if key in self:

#             self.hit(key)
#             if self.entries[key].isagen and not hasattr(self[key], "__aiter__"):
#                 return _AsyncGenProxy(key, self[key].value)

#             async def _agen_wrapper():
#                 return self[key].value  # Return the value not the entry

#             return _agen_wrapper()

#         # Cache miss path
#         print(f"Executing uncached function: {self.func.__qualname__}")
#         result = self.func(*args, **kwargs)

#         # Handle different result types
#         if hasattr(result, "__aiter__"):
#             print(f"Caching async generator for {key}")
#             result = _AsyncGenProxy(key, result)
#             self[key] = result
#             self.miss(key)
#             return result

#         # For normal coroutines
#         async def _wrapper():
#             nonlocal result
#             if hasattr(result, "__await__"):
#                 print(f"Awaiting coroutine for {key}")
#                 result = await result  # type: ignore

#             # Directly add to the cache synchronously for immediate use
#             print(f"Directly adding {key} to cache")
#             entry = CacheEntry(
#                 key=key,
#                 value=result,
#                 context_keys=key.context_keys,
#                 ttl=self._cfg['ttl'],
#                 last_accessed=time.time(),
#                 last_updated=time.time(),
#                 last_missed=0.0,
#                 isagen=hasattr(result, "__aiter__"),
#                 iscoro=hasattr(result, "__await__"),
#                 persistent=self._cfg['persistent'],
#                 context_policy=self._cfg['context_policy'],
#             )
#             with self.acquire(str(hash(key))):
#                 _cache[key] = entry

#             self.miss(key)
#             return result

#         return _wrapper()

#     @classmethod
#     def clear_disk(cls) -> None:
#         """Clear the cache file."""
#         cfg = CacheConfig(**CACHE_CONFIG)
#         path_dir = Path(str(cfg['pathdir'])).resolve()

#         try:
#             with make_aquirer(cls.locks).acquire():
#                 SafeFileCache(str(path_dir))

#                 # Get all files in the cache directory
#                 if path_dir.exists():
#                     # Try to remove all cache files
#                     import shutil
#                     try:
#                         shutil.rmtree(path_dir, onerror=lambda func, path, exc_info:
#                             safe_print(f"Could not remove {path}: {exc_info}"))
#                     except Exception as e:
#                         safe_print(f"Error clearing cache directory: {e}")

#                     if not path_dir.exists():
#                         safe_print("Cache directory removed successfully")
#                     else:
#                         safe_print("Could not completely remove cache directory")
#         except Exception as e:
#             import traceback
#             traceback.print_exc()
#             safe_print(f"Error clearing disk cache: {e}")


#     @classmethod
#     def clear_memory(cls) -> None:
#         """Clear the cache for a specific function."""
#         try:
#             # Use thread-safe locks from the class
#             with make_aquirer(cls.locks).acquire():
#                 global _cache, _cache_info
#                 _cache.clear()
#                 _cache_info = GlobalCacheInfo()
#         except Exception:
#             import traceback
#             traceback.print_exc()

#     @classmethod
#     def clear_all(cls) -> None:
#         """Clear all cache entries and cache file."""
#         cls.clear_memory()
#         cls.clear_disk()


#     @classmethod
#     async def save(cls, pathdir: Path | str = CACHE_CONFIG['pathdir']) -> None:
#         """Persist in-memory cache to disk using SafeFileCache."""
#         if CACHE_OFF:
#             return

#         # Check if there's anything to save
#         if not _cache:
#             if isvverbose():
#                 safe_print("[yellow][WARN][/yellow] No cache entries to save")
#             return

#         # Create a default configuration
#         path_dir = Path(str(pathdir)).resolve()
#         if not path_dir.exists():
#             path_dir.mkdir(parents=True, exist_ok=True)
#             if isverbose():
#                 safe_print(f"[cyan][DEBUG][/cyan] Created cache directory: {path_dir}")

#         # Use SafeFileCache for storage
#         file_cache = SafeFileCache(str(path_dir))

#         try:
#             # 1. Save metadata as JSON where possible
#             try:
#                 meta_data = serialize_metadata(_cache_info)
#                 file_cache.set("cache_meta", meta_data)
#                 # Add body file which is required by SafeFileCache
#                 file_cache.set_body("cache_meta", b'cache_meta_body')

#             except Exception as e:
#                 if isverbose():
#                     safe_print(f"[red][ERROR][/red] Could not save cache metadata: {e}")

#             # 2. Save list of key hashes for loading
#             try:
#                 key_hashes = [str(hash(key)) for key in _cache.keys()]
#                 # Save as a simple JSON list
#                 file_cache.set("cache_keys", json.dumps(key_hashes).encode('utf-8'))
#                 # Add body file which is required by SafeFileCache
#                 file_cache.set_body("cache_keys", b'cache_keys_body')

#             except Exception as e:
#                 if isverbose():
#                     safe_print(f"[red][ERROR][/red] Could not save cache keys: {e}")

#             # 3. Save a mapping of key hash to original key for reconstruction
#             try:
#                 key_mapping = {}
#                 for key in _cache.keys():
#                     key_hash = str(hash(key))
#                     # Store function name and args for debugging
#                     if hasattr(key, "func_name"):
#                         key_mapping[key_hash] = key.func_name

#                 file_cache.set("key_mapping", json.dumps(key_mapping).encode('utf-8'))
#                 # Add body file which is required by SafeFileCache
#                 file_cache.set_body("key_mapping", b'key_mapping_body')
#             except Exception as e:
#                 if isverbose():
#                     safe_print(f"[red][ERROR][/red] Could not save key mapping: {e}")

#             # 4. Process and save each entry
#             # We need pickle for the actual entry values
#             saved_count = 0

#             for key, entry in _cache.items():
#                 try:

#                     metadata = {
#                         "key": key,
#                         "context_keys": getattr(key, "context_keys", None),
#                         "func_name": getattr(key, "func_name", "unknown"),
#                         "last_accessed": entry.last_accessed,
#                         "ttl": getattr(entry, "ttl", 0),
#                         "persistent": getattr(entry, "persistent", False),
#                         "currsize": getattr(entry, "currsize", 0)
#                     }

#                     # Store the metadata
#                     file_cache.set(str(hash(key)), json.dumps(metadata).encode('utf-8'))

#                     # Store the actual value as the body file
#                     entry_bytes = pickle.dumps(entry)
#                     file_cache.set_body(str(hash(key)), entry_bytes)

#                     saved_count += 1

#                 except Exception as e:
#                     if isverbose():
#                         safe_print(f"[red][ERROR][/red] Could not save cache entry for key {key}: {e}")

#             if isverbose():
#                 safe_print(f"[green][SUCCESS][/green] Cache saved with {saved_count} entries to {path_dir}")
#         except Exception as e:
#             safe_print(f"[red][ERROR][/red] Could not save cache: {e}")
#             if isverbose():
#                 import traceback
#                 traceback.print_exc()

#     @classmethod
#     def load(cls, pathdir: Path | str = CACHE_CONFIG['pathdir']) -> None:
#         """Load cache from disk into memory using SafeFileCache."""
#         if CACHE_OFF:
#             return

#         global _cache, _cache_info

#         # Create a default configuration if needed
#         path_dir = Path(str(pathdir)).resolve()

#         # Validate cache directory
#         if not path_dir.exists():
#             if isverbose():
#                 safe_print(f"[yellow][WARN][/yellow] Cache directory {path_dir} does not exist")
#             return

#         # Clear existing cache data first
#         _cache.clear()
#         _cache_info = GlobalCacheInfo()

#         # Use SafeFileCache for loading
#         file_cache = SafeFileCache(str(path_dir))

#         # Load metadata
#         try:
#             meta_data = file_cache.get("cache_meta")
#             if meta_data:
#                 _cache_info = deserialize_metadata(meta_data.decode('utf-8'))
#         except Exception as e:
#             safe_print(f"[red][ERROR][/red] Could not load cache metadata: {e}")
#             return

#         # Load key hashes
#         try:
#             cache_keys = file_cache.get("cache_keys")
#             if cache_keys is None:
#                 if isverbose():
#                     safe_print("[yellow][WARN][/yellow] No cache keys found")
#                 return

#             key_hashes = json.loads(cache_keys.decode('utf-8'))
#             for key_hash in key_hashes:
#                 key_data = file_cache.get(key_hash)
#                 if key_data:
#                     body = file_cache.get_body(key_hash)
#                     if not body:
#                         safe_print(f"[red][ERROR][/red] Could not load cache entry for key {key_hash}")
#                         continue
#                     value: CacheEntry = pickle.loads(body.read())
#                     key = value.key

#                     _cache[key] = value
#         except Exception as e:
#             safe_print(f"[red][ERROR][/red] Could not load cache: {e}")
#             import traceback
#             traceback.print_exc()


# class acache(cache[P, R]):
#     """Use c-speed lru_cache for cache entries."""

#     acache_queue: asyncio.Queue
#     _tasks: set[asyncio.Task] = set()
#     _task_started = False

#     def __contains__(self, key: CacheKey) -> bool:
#         """Check if the key exists in the cache using the & operator."""
#         if CACHE_OFF or not self._cfg['enabled']:
#             return False


#         # Direct entry lookup
#         entry = _cache.get(key)
#         if entry is not None:
#             # Use & operator to check key equality with context
#             if not (entry.key & key):
#                 with self.acquire(hash(key)):
#                     _cache.pop(key, None)
#                 print(f"Key format mismatch for {key}")
#                 return False
#             print(f"Cache HIT for {key}")
#             return True

#         print(f"Cache MISS for {key}")
#         return False

#     @overload
#     @wrapafter(CacheConfig,returns=Self)
#     def __new__(cls, **config: Unpack[CacheConfig]) -> Self: ...
#     @overload
#     def __new__(cls, func: Callable[P, AR[R] | R | GR[R]]) -> Self: ...
#     def __new__(cls, *args, **kwargs) -> Self:
#         cls._tasks = set()
#         cls._task_started = False
#         cls.acache_queue = asyncio.Queue()
#         self = super().__new__(cls, *args, **kwargs)
#         type(self)._tasks = cls._tasks
#         type(self)._task_started = cls._task_started
#         type(self).acache_queue = cls.acache_queue
#         self.func = None
#         self._mkey = None
#         self._pending = None
#         self._cfg = None
#         self._initialized = False
#         self.__init__(*args, **kwargs)
#         return self


#     @overload
#     def __call__(self: Callable[P, R], *args: P.args, **kwargs: P.kwargs) -> R: ...
#     @overload
#     def __call__(self: Callable[P, AR], *args: P.args, **kwargs: P.kwargs) -> AR[R]: ...
#     @overload
#     def __call__(self: Callable[P, GR], *args: P.args, **kwargs: P.kwargs) -> GR[R]: ...
#     def __call__(self, *args: P.args, **kwargs: P.kwargs):


#         if not self._initialized:
#             self._cfg = init_cfg(*args, **kwargs)
#             self._mkey = CacheKey[self._cfg['context_policy'],self._cfg["ttl"]]
#             self._initialized = True
#             return self
#         if not self.func:

#             self.func = init_func(*args, **kwargs)
#             self._mkey = self._mkey(self.func)
#             if self.func is not None:
#                 func_name = getattr(self.func, "__qualname__", "unknown")
#                 _cache_info.by_function[func_name] = FunctionCacheInfo(
#                     "function" if not iscoroutinefunction(self.func) and not hasattr(self.func, "__await__")
#                     and not hasattr(self.func, "__aiter__") else "async_generator"
#                     if hasattr(self.func, "__aiter__") else "coroutine"
#                 )
#                 self._function_info = _cache_info.by_function[func_name]
#             return self
#         if not type(self)._task_started:
#                type(self)._start_tasks(self._cfg)
#                self._task_started = True
#                type(self)._task_started = True
#         if CACHE_OFF or not self._cfg['enabled']:
#             return self.func(*args, **kwargs)
#         key = self._mkey(self.func, *args, **kwargs)

#         if key in self:

#             self.hit(key)
#             if self.entries[key].isagen and not hasattr(self[key], "__aiter__"):
#                 return _AsyncGenProxy(key, self[key].value)

#             async def _agen_wrapper():
#                 return self[key].value  # Return the value not the entry

#             return _agen_wrapper()

#         result = self.func(*args, **kwargs)

#         # Handle different result types
#         if hasattr(result, "__aiter__"):
#             result = _AsyncGenProxy(key, result)
#             self[key] = result
#             self.miss(key)
#             return result

#         # For normal coroutines
#         async def _wrapper():
#             nonlocal result
#             if hasattr(result, "__await__"):
#                 result = await result  # type: ignore

#             # Directly add to the cache synchronously for immediate use
#             entry = CacheEntry(
#                 key=key,
#                 value=result,
#                 context_keys=key.context_keys,
#                 ttl=self._cfg['ttl'],
#                 last_accessed=time.time(),
#                 last_updated=time.time(),
#                 last_missed=0.0,
#                 isagen=hasattr(result, "__aiter__"),
#                 iscoro=hasattr(result, "__await__"),
#                 persistent=self._cfg['persistent'],
#                 context_policy=self._cfg['context_policy'],
#             )
#             with self.acquire(str(hash(key))):
#                 _cache[key] = entry

#             self.miss(key)
#             return result

#         return _wrapper()


#     async def asetitem(self, key:CacheKey, value) -> None:
#         if not isinstance(value, CacheEntry):
#             entry = CacheEntry(
#                 key=key,
#                 value=value,
#                 context_keys=key.context_keys,
#                 ttl=self._cfg['ttl'],
#                 last_accessed=time.time(),
#                 last_updated=time.time(),
#                 last_missed=0.0,
#                 persistent=self._cfg['persistent'],
#                 context_policy=self._cfg['context_policy'],
#             )
#         else:
#             entry = value

#         _cache[key] = entry
#         print(f"Added to cache: {key}")
#         if hasattr(self, '_function_info'):
#             _cache_info.by_function[f"{self.func.__qualname__}"] .currsize += 1


#     async def adelitem(self, key) -> None:
#         if key in _cache:

#             del _cache[key]

#             _cache_info.by_function[f"{self.func.__qualname__}"].currsize -= 1

#     def __setitem__(self, key, value):
#         if CACHE_OFF or not self._cfg['enabled']:
#             return
#         print(f"Adding to cache queue: {key}")
#         type(self).acache_queue.put_nowait(self.asetitem(key, value))

#     def __getitem__(self, key: CacheKey):
#         entry = _cache.get(key)
#         if entry is None:
#             raise KeyError(key)

#         if not (entry.key & key):
#             type(self).acache_queue.put_nowait(self.adelitem(key))
#             raise KeyError(key)
#         entry.last_accessed = time.time()
#         return entry

#     def __delitem__(self, key):
#         type(self).acache_queue.put_nowait(self.adelitem(key))


#     @classmethod
#     async def aworker(cls):
#         while True:
#             try:
#                 task = await cls.acache_queue.get()

#                 if asyncio.iscoroutine(task):
#                     await task
#                 else:
#                     print(f"[ERROR] Invalid task: {task}, skipping.")

#                 cls.acache_queue.task_done()
#             except asyncio.CancelledError:
#                 break
#             except KeyboardInterrupt:
#                 break
#             except Exception as e:
#                 import traceback
#                 traceback.print_exc()
#                 print(f"[ERROR] Worker failed: {e}")


#     @classmethod
#     async def stop(cls):
#         """Stop the worker properly without loop issues."""
#         import contextlib
#         for task in list(cls._tasks):
#             task.cancel()
#             with contextlib.suppress(asyncio.CancelledError):
#                 await task

#         cls._tasks.clear()
#         cls._task_started = False


#     @classmethod
#     def _start_tasks(cls, config):
#         """Start background tasks for cache management."""
#         # Don't start multiple instances of the worker
#         if cls._task_started:
#             return

#         # This is where we actually create the worker task
#         if not cls._tasks:
#             loop = asyncio.get_event_loop_policy().get_event_loop()
#             worker_task = loop.create_task(cls.aworker())
#             cls._tasks.add(worker_task)

#             # Ensure worker is cleaned up on exit
#             def cleanup_worker():
#                 if not worker_task.done():
#                     worker_task.cancel()

#             atexit.register(cleanup_worker)

#         cls._task_started = True


# @acache(persistent=True)
# async def dummy_task(i: int) -> int:
#     print("*** HELLO THIS IS A TEST MODIFICATION! ***")
#     print(f"Running dummy_task({i}) - this should only appear on first run")
#     await asyncio.sleep(0.1)
#     return i+1

# @acache(persistent=True)
# async def dummy_task2(i: int) -> "AsyncGenerator[Any, int]":
#     await asyncio.sleep(0.1)
#     yield i+1
#     return

# @acache(persistent=True)
# async def dummy_tasks():
#     for i in range(3):
#         await dummy_task(i)
#     async for j in dummy_task2(0):  # Use 0 instead of i
#         print(j)

# async def main():
#     from time import time


#     t = time()
#     await dummy_tasks()
#     t = time() - t
#     print(f"Time taken: {t} seconds")


#     t = time()
#     await dummy_tasks()
#     t = time() - t
#     print(f"Time taken: {t} seconds")

#     print(acache.cache_info())

#     # Save cache before stopping and exiting
#     await cache.save()

#     await dummy_task.stop()
#     await dummy_task2.stop()

#     print("Stopped worker")

# if __name__ == "__main__":
#     print("Running demo implementation...")
#     asyncio.run(main())
