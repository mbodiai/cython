from __future__ import annotations

import os
from collections import deque
from collections.abc import Hashable
from dataclasses import asdict
from functools import partial, reduce
from inspect import _empty, signature
from itertools import chain, repeat
from pathlib import Path
from site import getsitepackages
from time import time
from types import FunctionType, new_class

from typing_extensions import Generic, Literal, Protocol, TypeVar

from mbcore.import_utils import smart_import, imports


TYPE_CHECKING = False
if TYPE_CHECKING:
    import mbcore.proto.Is
TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing_extensions import (
        Any,
        AsyncGenerator,
        Callable,
        Coroutine,
        Final,
        Generator,
        Iterable,
        Literal,
        NewType,
        ParamSpec,
        Protocol,
        TypeAlias,
        TypeIs,
        TypeVar,
        overload,
    )

    from mbcore.proto import AFuncP, FuncP,Is
    from mbcore.types import DataclassInstance

    T = TypeVar("T")
    _T = TypeVar("_T")
    _R_co = TypeVar("_R_co", covariant=True)

    P = ParamSpec("P")
    R = TypeVar("R")
    _R = TypeVar("_R")
    __R = TypeVar("__R")
    AR = AsyncGenerator[None, _R]
    GR = Generator[None, _R, None]

    class Hash(Protocol):

        def __hash__(self) -> int:
            ...

    CR = Coroutine[None, None, __R]
    GenFunc = Callable[P, GR]
    Func = Callable[P, R]
    CoroFunc = Callable[P, CR]
    AsyncGenFunc = Callable[P, AR]
    FuncTs: TypeAlias = Func | GenFunc | AsyncGenFunc | CoroFunc
    FuncT = TypeVar("FuncT", bound=FuncP | AFuncP)

else:

    def overload(*args, **kwargs):
        return lambda f: f

    Any = CR = GenFunc = Func = CoroFunc = AsyncGenFunc = FuncTs = ContextPolicyType = ContextPolicyT = (
        ContextPolicyT_co) = Hash = object

    def NewType(name, tp):
        return tp

    def TypeIs(self, parameters):
        return object


ContextPolicyType = Literal["mtime", "site_packages", "ttl", "all"]
ContextPolicyT = TypeVar("ContextPolicyT",
                         bound=Literal["mtime", "site_packages", "ttl", "all"])
ContextPolicyT_co = TypeVar("ContextPolicyT_co",
                            bound=ContextPolicyType,
                            covariant=True)


def flatten(v):
    """Flatten a nested data structure."""
    if hasattr(v, "items") and callable(v.items):
        return chain.from_iterable(flatten(x) for x in v.items())
    if hasattr(v, "__iter__") and not isinstance(v, (str, bytes, bytearray)):
        return chain.from_iterable(flatten(x) for x in v)
    return (v, )


def ishashable(v) -> "TypeIs[Hashable]":
    """Check if a value is hashable."""
    try:
        hash(v)
        return True
    except TypeError:
        return False


@overload
def flatmap(*vs: "Any | Iterable[Any]", func: "Callable[[Any], Any]"):
    ...


@overload
def flatmap(*vs: "Iterable[Any]", func: "Callable[[Any], Any]|None" = None):
    ...


def flatmap(*vs: "Iterable[Any]", func: "Callable[[Any], Any]|None" = None):
    """Flatten nested structures and apply `func` at the base level."""
    if not callable(func) and func is not None:
        vv = vs, func
        f = None
    elif not vs and callable(func):
        return ()
    else:
        vv = vs
        f = func
    if func is None:

        def f(v):
            return v

    return tuple(
        f(v) if not hasattr(v, "__iter__") or isinstance(
            v, (str, bytes, bytearray, Path)) else flatmap(*v.values(
            ), func=f) if hasattr(v, "items") else flatmap(*v, func=f)
        for v in flatten(vv))


def treemap(func, mp):
    """Map a function over a nested data structure."""
    if mp is None:
        return None
    if isinstance(mp, str | bytes | bytearray | int | float):
        return func(mp)
    if isinstance(mp, list | tuple):
        return {i: func(v) for i, v in enumerate(mp)}
    if not hasattr(mp, "items"):
        return func(mp)
    return {
        k:
        treemap(func, v) if isinstance(v, dict | list | tuple)
        and not isinstance(v, str | bytes) else func(v)
        for k, v in mp.items()
    }


async def amap(func, mp):
    """Map a function asynchronously over a nested data structure."""
    if mp is None:
        return None
    if isinstance(mp, str | bytes | bytearray | int | float):
        return await func(mp)
    if isinstance(mp, list | tuple):
        return {i: await func(v) for i, v in enumerate(mp)}
    if not hasattr(mp, "items"):
        return await func(mp)
    return {
        k:
        await amap(func, v) if isinstance(v, dict | list | tuple)
        and not isinstance(v, str | bytes) else await func(v)
        for k, v in mp.items()
    }


async def atreemap(func, mp: dict | Any) -> dict | Any:
    """Map a function asynchronously over a nested data structure."""
    if callable(mp) and not callable(func):
        mp, func = func, mp
    elif callable(mp) and callable(func):
        mp = f"{getattr(mp, '__qualname__', mp)}"

    if mp is None:
        return None
    if hasattr(mp, "__dataclass_fields__"):
        mp = asdict(mp) if isinstance(mp, DataclassInstance) else getattr(
            mp, "__dict__", mp)
    if isinstance(mp, str | bytes | bytearray | int | float):
        return await func(mp)
    if isinstance(mp, list | tuple):
        return {i: await func(v) for i, v in enumerate(mp)}
    if not hasattr(mp, "items"):
        return await func(mp)

    return {
        k:
        await atreemap(func, v) if isinstance(v, dict | list | tuple)
        and not isinstance(v, str | bytes) else await func(v)
        for k, v in mp.items()
    }


def iscallable(v: "Any") -> "TypeIs[FunctionType]":
    """Check if a value is callable."""
    return (isinstance(v, FunctionType) or callable(v)
            or hasattr(v, "__func__") or callable(v)
            or isinstance(v, (type, classmethod, staticmethod)))


def sitepackages() -> float:
    """Get the site-packages directory."""
    return Path(getsitepackages()[0]).stat().st_mtime


_defaults_cache: dict[str, tuple[Any, ...]] = {}


# Proper handling of negative hashes while minimizing collisions
def twos_complement(h: int) -> int:
    # Convert negative values to positive using 2's complement with 64-bit integers
    if h < 0:
        h = (1 << 64) + h
    return h


def collapse(iterable, base_type=None, levels=None):
    """Flatten an iterable with multiple levels of nesting (e.g., a list of
    lists of tuples) into non-iterable types.

        >>> iterable = [(1, 2), ([3, 4], [[5], [6]])]
        >>> list(collapse(iterable))
        [1, 2, 3, 4, 5, 6]

    Binary and text strings are not considered iterable and
    will not be collapsed.

    To avoid collapsing other types, specify *base_type*:

        >>> iterable = ['ab', ('cd', 'ef'), ['gh', 'ij']]
        >>> list(collapse(iterable, base_type=tuple))
        ['ab', ('cd', 'ef'), 'gh', 'ij']

    Specify *levels* to stop flattening after a certain level:

    >>> iterable = [('a', ['b']), ('c', ['d'])]
    >>> list(collapse(iterable))  # Fully flattened
    ['a', 'b', 'c', 'd']
    >>> list(collapse(iterable, levels=1))  # Only one level flattened
    ['a', ['b'], 'c', ['d']]

    """
    stack = deque()
    # Add our first node group, treat the iterable as a single node
    stack.appendleft((0, repeat(iterable, 1)))

    while stack:
        node_group = stack.popleft()
        level, nodes = node_group

        # Check if beyond max level
        if levels is not None and level > levels:
            yield from nodes
            continue

        for node in nodes:
            # Check if done iterating
            if isinstance(node,
                          (str, bytes)) or ((base_type is not None)
                                            and isinstance(node, base_type)):
                yield node
            # Otherwise try to create child nodes
            else:
                try:
                    tree = iter(node)
                except TypeError:
                    yield node
                else:
                    # Save our current location
                    stack.appendleft(node_group)
                    # Append the new child node
                    stack.appendleft((level + 1, tree))
                    # Break to process child node
                    break


class twocint(int):

    def __str__(self) -> str:
        return str(twos_complement(self))

    def __hash__(self) -> int:
        # Ensure we always return a positive hash
        return twos_complement(super().__hash__())


def compose(func, *funcs):
    """Compose a function with multiple functions."""
    return reduce(lambda f, g: lambda x: f(g(x)), funcs, func)


def attrgetter(attr):
    """Get an attribute of an object."""
    return lambda x: getattr(x, attr)


# Define the sentinel value
DEFAULT_MISSING_SENTINEL: Final[
    Literal["<DEFAULT_MISSING>"]] = "<DEFAULT_MISSING>"

FunctionName = NewType("FunctionName", str)
ArgKwargHash = NewType("ArgKwargHash", tuple[Hashable, ...])
TTL = TypeVar("TTL")


class CacheKey(Generic[ContextPolicyT, TTL]):
    """A cache key for invalidating cache entries based on external factors.

    such as file modification time or site-packages directory changes.

    This can be extended to far more intelligent caching. Currently, the following context keys are supported:

    - `mtime_aware`: Invalidate cache entries based on file modification time.
    - `site_aware`: Invalidate cache entries based on changes to the site-packages directory.
    - `ttl`: Time-to-live for cache entries.
    """

    policy_type: Literal["mtime", "site_packages", "ttl", "all"]
    ttl: Any
    expires: float
    key: tuple[FunctionName, ArgKwargHash]
    context_keys: tuple[Hashable, ...]
    func_name: str
    param_names: tuple[str, ...]
    defaults: dict[str, Any]

    def __init__(self, func: Callable | None = None) -> None:
        if func is None:
            return
        self.func_name = func.__qualname__

        self.param_names = tuple(signature(func).parameters.keys())
        self.defaults = {}
        for k, v in signature(func).parameters.items():
            if v.default is _empty:
                # Use the defined sentinel value
                self.defaults[k] = DEFAULT_MISSING_SENTINEL
            else:
                self.defaults[k] = v.default
        self.policy_type = type(self).policy_type
        self.ttl = type(self).ttl
        self.expires = time() + self.ttl
        self.context_keys = ()

    def make(self, *args: Any, **kwds: Any):
        arglist = list(args)[1:] if args else []
        kwargs = {
            k: kwds.get(k,
                        arglist.pop(0) if arglist else self.defaults[k])
            for k in self.param_names
        }
        key = _make_key(**kwargs)

        context_keys = self.context_keys

        if self.policy_type in ("mtime",
                                "all") and "mtime" not in (*key,
                                                           *context_keys):
            context_keys = (*context_keys, *_mtime_key(**kwargs))
        if self.policy_type in ("site_packages",
                                "all") and "site" not in (*key, *context_keys):
            context_keys = (*context_keys, *_site_key())

        # Store the function name and key elements directly, without nesting
        self.key = (FunctionName(self.func_name), ArgKwargHash(key))
        self.expires = self.ttl + time()
        c = CacheKey()
        c.context_keys = context_keys  # Use the updated context_keys, not self.context_keys
        c.key = self.key
        c.policy_type = self.policy_type
        c.expires = self.expires
        c.func_name = self.func_name
        c.param_names = self.param_names
        c.defaults = self.defaults
        c.ttl = self.ttl

        return c

    __call__ = make

    def __repr__(self) -> str:
        return f"CacheKey({self.func_name}: {', '.join(map(repr, self.key))})"

    def __eq__(self, other: "Any") -> bool:
        return self.key == getattr(other, "key", object())

    def __str__(self) -> str:
        # Show function name and key tuple for better identification
        return f"{self.func_name}({', '.join(repr(k) for k in self.key)})"

    def __and__(self, other: Any) -> bool:
        """Check if two cache keys are equal along with their context keys."""
        if time() > self.expires:
            return False
        if not hasattr(other, "key") or not hasattr(self, "context_keys"):
            return False
        return self.key == other.key and all(k == c for k, c in zip(
            self.context_keys, other.context_keys, strict=False))

    @classmethod
    def __class_getitem__(
            cls, params: tuple[ContextPolicyT, Any]) -> "type[CacheKey]":
        if len(params) == 1:
            raise ValueError(
                f"Invalid number of parameters: {len(params)}. Expected  both policy and ttl. Got only {params}",
            )

        policy, ttl = params
        new_cls = new_class(
            f"CacheKey[{','.join(map(str, [policy, ttl]))}]",
            (CacheKey, ),
            exec_body=lambda ns: ns.update({
                "policy_type": policy,
                "ttl": ttl
            }),
        )
        return new_cls

    def __hash__(self) -> int:
        # Always return a positive hash value
        return twos_complement(hash(self.key))


def make_key(*args: Any, **kwds: Any) -> tuple[Hashable | str, ...]:
    kwds.update(dict(map((lambda ix: (f"arg{ix[0]}", ix[1])),
                         enumerate(args))))
    return _make_key(**kwds)


def _make_key(**kwds: Any) -> tuple[Hashable | str, ...]:
    """Generate a fully flattened, immutable hashable dictionary for caching."""
    from mbcore.more import collapse, zip_longest

    return (*zip_longest(kwds.keys(), collapse(kwds.values())), )


def _get_mtimes(args: Iterable[Path]) -> Iterable[float]:
    """Return all modification times of paths in args and kwds."""
    return map(
        compose(attrgetter("st_mtime"), partial(os.stat,
                                                follow_symlinks=False)), args)

@imports(Is="mbcore.proto.Is")
def _mtime_key(**kwds: Any) -> tuple[str | float, ...]:
    """Invalidates cache entries based on file modification time."""
    # Use collapse directly on values, then filter for existing Paths
    paths = filter(Is[Path] & Path.exists, collapse(kwds.values()))
    mtimes = _get_mtimes(paths)
    return ("mtime", *mtimes)


def _site_key() -> tuple[str, float]:
    """Invalidates cache entries based on file modification time, including site-packages."""
    return ("site", sitepackages())
def safe_print(v: Any):
    from rich.console import Console
    console = Console()
    console.print(v)

if __name__ == "__main__":
    from time import sleep

    t = time()

    def func(a, b, c=1, d=Path("test1.txt"), e=Path(getsitepackages()[0])):
        return a + b + c

    # Create a test file we can modify
    test_file = Path("test1.txt")
    if test_file.exists():
        test_file.unlink()

    new_file = Path("test2.txt")
    if new_file.exists():
        new_file.unlink()
    test_file.touch()

    # Create keys with the test file as a parameter - use literal strings for policy type
    policy_type: Literal["mtime"] = "mtime"
    ttl: int = 1
    keyfactory = CacheKey[policy_type, ttl](func)
    key1 = keyfactory(func, 1, 2, c=3, d=Path(), e=Path(getsitepackages()[0]))
    assert key1 is not None and key1.policy_type == "mtime"
    safe_print(key1)
    # Create a second key with the same parameters
    key2 = keyfactory(func, 1, 2, c=3, d=Path())
    assert key1 & key2, f"ERROR: key1: {key1} & key2: {key2} should be True"

    # Modify the file to change its mtime

    new_file.touch()

    # Create a new key after modification
    key3 = keyfactory(func, 1, 2, c=3, d=Path())
    try:
        assert not key1 & key3, f"ERROR: key1: {key1} & key3: {key3} should be False"
    except AssertionError as e:
        print(e)
        if test_file.exists():
            test_file.unlink()
        if new_file.exists():
            new_file.unlink()
        exit(1)

    try:
        assert key1 & key2, f"ERROR: key1: {key1} & key2: {key2} should be True"
    except AssertionError as e:
        print(e)
        # Clean up
        if test_file.exists():
            test_file.unlink()
        if new_file.exists():
            new_file.unlink()
        exit(1)

    t = time() - t

    sleep(1)
    assert not key1 & key1, f"ERROR: key1: {key1} & key1: {key1} should be False"

    print(key1)
    print(key2)
    print(key3)
    print("All tests passed!")
    print(f"Time taken: {t} seconds")
