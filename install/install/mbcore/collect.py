import re
import sys
from collections import defaultdict, deque
from collections.abc import AsyncIterable, Callable, MutableMapping
from contextlib import contextmanager
from copy import copy
from dataclasses import _MISSING_TYPE, MISSING
from datetime import datetime, timedelta
from functools import reduce
from inspect import signature
from itertools import (
    accumulate,
    chain,
    count,
    islice,
    repeat,
    tee,
)
from itertools import (
    dropwhile as _dropwhile, )
from itertools import (
    takewhile as _takewhile, )
from operator import add, attrgetter, itemgetter, methodcaller, not_
from re import Pattern
from time import time
from types import EllipsisType, FunctionType, MethodType, NoneType, SimpleNamespace
from typing import TYPE_CHECKING, AsyncIterator

from typing_extensions import (
    Any,
    Concatenate,
    Dict,
    Generic,
    Literal,
    Mapping,
    ParamSpec,
    Protocol,
    Self,
    Sequence,
    Set,
    Tuple,
    Type,
    TypeVar,
    TypeVarTuple,
    Unpack,
    cast,
    overload,
    runtime_checkable,
)

from mbcore.more import Is, SequenceView, collapse, consume, locate, replace, spy
from mbcore.more import seekable as Seekable
from mbcore.proto import (
    CoroutineType,
    GeneratorType,
    GetItemIterable,
    Indexable,
    PredicateType,
    SupportsIter,
    SupportsIterType,
    SupportsKeysItems,
    _SupportsNext,
)
from mbcore.proto import (
    IterableP as Iterable, )
from mbcore.proto import (
    IteratorP as Iterator, )
from mbcore.types import PydanticUndefined, wrapafter, wraps

_filter = filter
_map = map
now = datetime.now

_T = TypeVar("_T")
_T_co = TypeVar("_T_co", covariant=True)
_S = TypeVar("_S")
_PWrapped = ParamSpec("_PWrapped")
_RWrapped = TypeVar("_RWrapped")
_PWrapper = ParamSpec("_PWrapper")
_RWrapper = TypeVar("_RWrapper")

_R = TypeVar("_R")
P = ParamSpec("P")
R = TypeVar("R")

try:
    import cython

    HAS_CYTHON = True
except (ImportError, ModuleNotFoundError):
    HAS_CYTHON = False

if not HAS_CYTHON:
    cython = SimpleNamespace(**{"embed": lambda x: x})

_SupportsNextT = TypeVar("_SupportsNextT", bound=_SupportsNext | Sequence[str])


class Empty(Iterator):

    def __iter__(self):
        return self

    def __next__(self) -> Any:
        return None

    def __new__(cls):
        try:
            return cls._instance
        except AttributeError:
            cls._instance = super().__new__(cls)
            return cls._instance

    def __bool__(self):
        return False

    def __repr__(self):
        return "EMPTY"

    def __str__(self):
        return "EMPTY"

    def __lt__(self, other):
        return True

    def __le__(self, other):
        return True

    def __gt__(self, other):
        return False

    def __ge__(self, other):
        return other is self

    def __eq__(self, other):
        return other is self

    def __ne__(self, other):
        return other is not self


EMPTY = Empty()


class namespace(Mapping, Generic[_T]):
    """A simple namespace class."""

    def __getitem__(self, key: str) -> _T:
        if not key.startswith("__"):
            return getattr(self, key)
        raise KeyError(key)

    def __len__(self) -> int:
        return len(self.__dict__)

    def keys(self):
        return self.__dict__.keys()

    def values(self):
        return self.__dict__.values()

    def items(self):
        return self.__dict__.items()

    def __setitem__(self, key: str, value: _T) -> None:
        setattr(self, key, value)

    def __call__(self, *args, **kwargs):
        return namespace(**kwargs)

    def setdefault(self,
                   key: str,
                   delimeter: str = ".",
                   default: Any = None) -> Any:
        """Set a default value for a key in a nested namespace."""
        keys = key.split(delimeter)
        obj = self
        for k in keys[:-1]:
            if not hasattr(obj, k):
                setattr(obj, k, namespace())
            obj = getattr(obj, k)
        if not hasattr(obj, keys[-1]):
            setattr(obj, keys[-1], default)
        return getattr(obj, keys[-1])

    def delin(self, key: str, delimeter: str = ".") -> None:
        """Delete a key in a nested namespace."""
        keys = key.split(delimeter)
        obj = self
        for k in keys[:-1]:
            obj = getattr(obj, k)
        delattr(obj, keys[-1])

    def pop(self, key: str, default: _T | None = None) -> _T | None:
        """Pop a key in a namespace."""
        if hasattr(self, key):
            value = getattr(self, key)
            delattr(self, key)
            return value
        return default

    def popin(self,
              key: str,
              delimeter: str = ".",
              default: _T | None = None) -> _T | None:
        """Pop a key in a nested namespace."""
        keys = key.split(delimeter)
        obj = self
        for k in keys[:-1]:
            obj = getattr(obj, k)
        return obj.pop(keys[-1], default)

    def __hash__(self):
        return hash(tuple(collapse(self.__dict__.items())))

    def update(self, **kwargs: "_T | dict[str, _T]") -> None:
        for k, v in kwargs.items():
            setattr(self, k, v)

    def get(self, key: str, default: _T | None = None) -> _T | None:
        return getattr(self, key, default)

    def __contains__(self, key: str) -> bool:
        return hasattr(self, key)

    def __iter__(self):
        return iter(self.__dict__)

    def getin(self,
              key: str,
              delimeter: str = ".",
              default: "U|_T" = None) -> "U |_T":
        """Get a value from a nested namespace.

        Retrieves a value from a nested namespace structure using dot notation.

        Args:
            key: Dot-separated path to the value (e.g., "a.b.c")
            delimeter: Character used to separate path components (default ".")
            default: Value returned if the path doesn't exist

        Returns:
            The value at the specified path, or the default value if not found

        Examples:
            >>> ns = namespace(a=namespace(b=1, c=False))
            >>> ns.getin("a.b")
            1
            >>> ns.getin("a.c")  # Returns False, not the default
            False
            >>> ns.getin("a.d", default="not found")
            'not found'

        """
        keys = key.split(delimeter)
        obj = cast(_T, self)
        try:
            for k in keys:
                if hasattr(obj, k):
                    obj = cast(_T, getattr(obj, k))
                else:
                    return default
            if obj == self:
                return default
            return obj
        except AttributeError:
            return default

    def setin(self, key: str, value: _T, delimeter: str = ".") -> None:
        keys = key.split(delimeter)
        if len(keys) == 1:
            setattr(self, key, value)
        else:
            obj = self
            for k in keys[:-1]:
                if not hasattr(obj, k):
                    setattr(obj, k, namespace())
                obj = getattr(obj, k)
            setattr(obj, keys[-1], value)

    def __init__(self, **kwargs: Any):
        for k, v in kwargs.items():
            setattr(self, k, v)


WRAPPER_UPDATES = ("__dict__", )
if sys.version_info >= (3, 12):
    WRAPPER_ASSIGNMENTS: tuple[
        Literal["__module__"],
        Literal["__name__"],
        Literal["__qualname__"],
        Literal["__doc__"],
        Literal["__annotations__"],
        Literal["__type_params__"],
    ] = (
        "__module__",
        "__name__",
        "__qualname__",
        "__doc__",
        "__annotations__",
        "__type_params__",
    )
else:
    WRAPPER_ASSIGNMENTS: tuple[
        Literal["__module__"],
        Literal["__name__"],
        Literal["__qualname__"],
        Literal["__doc__"],
        Literal["__annotations__"],
    ] = (
        "__module__",
        "__name__",
        "__qualname__",
        "__doc__",
        "__annotations__",
    )


class NotGivenType:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __repr__(self):
        return "..."

    def __str__(self):
        return "..."

    def __bool__(self):
        return False


NotGiven = NotGivenType()


@overload
def isgiven(
    value: "EllipsisType | PydanticUndefinedType | Literal['MISSING']"
) -> Literal[False]:
    ...


@overload
def isgiven(value: Any) -> bool:
    ...


def isgiven(value: Any):
    return (value is not NotGiven and value is not ... and value is not MISSING
            and value is not NotGivenType and value is not PydanticUndefined
            and not isinstance(value, _MISSING_TYPE))


@overload
def isnotgiven(
    value:
    "NotGivenType | EllipsisType | PydanticUndefinedType | Literal['MISSING']"
) -> Literal[True]:
    ...


@overload
def isnotgiven(value: Any) -> bool:
    ...


def isnotgiven(value: Any) -> bool:
    return value is NotGiven or value is ... or value is MISSING or value is PydanticUndefined


@overload
def exists(
    value:
    "NoneType | NotGivenType | EllipsisType | PydanticUndefinedType | Literal['MISSING']",
) -> Literal[False]:
    ...


@overload
def exists(value: Any) -> bool:
    ...


def exists(value: Any):
    """Not missing, not None, not NotGiven, not Any, not ..."""
    return value is not None and isgiven(value) and value != Any


P = ParamSpec("P")
V = TypeVar("V")
U = TypeVar("U")
T = TypeVar("T")
R = TypeVar("R")


@overload
def identity(f: Callable[P, T]) -> Callable[P, T]:
    ...


@overload
def identity(f: T) -> T:
    ...


def identity(f):
    return f


_P = ParamSpec("_P")

IterableT = TypeVar("IterableT",
                    bound=Iterable | Mapping | Sequence | Set | Tuple
                    | AsyncIterable | AsyncIterator)
_marker = object()
_VT = TypeVar("_VT")
_VT_co = TypeVar("_VT_co", covariant=True)
_KT = TypeVar("_KT")
_KT_co = TypeVar("_KT_co", covariant=True)
_T_co = TypeVar("_T_co", covariant=True)
if TYPE_CHECKING:
    from builtins import function

    @runtime_checkable
    class BaseClass(Iterator[_T_co], SupportsKeysItems[_KT_co, _VT_co],
                    Protocol[_KT_co, _VT_co, _T_co]):
        ...
else:

    class BaseClass(Generic[_KT, _VT, _T]):
        ...


class CollectIterator(BaseClass[_KT, _VT, _T], Generic[_KT, _VT, _T]):
    vit: Iterator[_VT]
    avit: AsyncIterator[_VT]
    _source: Iterable[_VT] | AsyncIterable[_VT] | AsyncIterator[
        _VT] | Iterator[_VT] | MutableMapping[_KT, _VT]
    kit: Iterator[_KT]
    akit: AsyncIterator[_KT]

    def __str__(self):
        if isinstance(self.it, AsyncIterator):
            return super().__str__()
        return str(list(self.it))

    def __init__(
        self,
        iterable: Iterable[_VT] | AsyncIterable[_VT] | AsyncIterator[_VT]
        | Iterator[_VT] | MutableMapping[_KT, _VT],
        maxlen: int | None = None,
    ) -> None:
        if isinstance(iterable, AsyncIterable):
            self.avit = aiter(iterable)
        elif isinstance(iterable, AsyncIterator):
            self.ait = iterable
        elif isinstance(iterable, MutableMapping):
            self.kit = iter(iterable.keys())  # type: ignore
            self.vit = iter(iterable.values())

        elif isinstance(iterable, Iterable):
            self.vit = iter(iterable)
        else:
            raise TypeError(
                f"Expected Iterable, AsyncIterable, AsyncIterator, Iterator, or MutableMapping, got {type(iterable)}",
            )
        if maxlen is None:
            self._cache = []
        else:
            self._cache = deque([], maxlen)
        self._index = None
        self._source = iterable
        self._cache = []

        if maxlen is None:
            self._cache = []
        else:
            self._cache = deque([], maxlen)
        self._index = None

    def __iter__(self):  # type: ignore
        return self

    def __len__(self) -> int:
        return ilen(self)

    def get(self, key: _KT, default: _VT | None = None) -> _VT | None:
        if isinstance(self._source, MutableMapping):
            return self._source.get(key, default)
        return default

    def update(self, **other: _VT) -> Self:
        if isinstance(self._source, MutableMapping):
            self._source.update(*other)
            self.kit = iter(self._source.keys())
            self.vit = iter(self._source.values())
            self._cache = []
        else:
            raise TypeError(f"{self.__name__} is not a MutableMapping.")
        return self

    def clear(self):
        self.it = self.mapit = []
        self.ait = self.amapit = self.avit = None
        return self

    def pop(self, key: _KT, default: _VT | None = None) -> _VT | None:
        if isinstance(self._source, MutableMapping):
            return self._source.pop(key, default)
        return default

    def popitem(self) -> tuple[_KT, _VT]:
        if isinstance(self._source, MutableMapping):
            return self._source.popitem()
        raise TypeError(f"{self.__name__} is not a MutableMapping.")

    @wraps(consume)
    def consume(self, n: int = -1) -> Self:
        consume(self.vit, n)
        return self

    async def aconsume(self):
        if isinstance(self.avit, AsyncIterator):
            (_ async for _ in self.avit)
        else:
            consume(self.vit)
        return self

    def tolist(self) -> list[_T | _VT]:
        return list(self.vit)

    def keys(self) -> Self:
        if isinstance(self._source, MutableMapping):
            self.it = iter(self._source.keys())
            return self
        self.it = iter(map(first, self.it))
        return self

    def values(self):
        if isinstance(self._source, MutableMapping):
            self.it = iter(self._source.values())
            return self
        self.it = iter(map(second, self.it))
        return self

    def items(self) -> Self:
        if isinstance(self._source, MutableMapping):
            self.it = iter(self._source.items())
            return self

        self.it = iter(map(lambda x: (first(x), second(x)), self.it))
        return self

    def __contains__(self, x: Any, /) -> bool:
        exists = x in self.it
        self.seek(0)
        return exists

    def __next__(self) -> _VT | _KT | tuple[_KT, _VT]:
        if self._index is not None:
            try:
                item = self._cache[self._index]
            except IndexError:
                self._index = None
            else:
                self._index += 1
                return item

        item = next(self.it)
        self._cache.append(item)
        return item

    def __bool__(self):
        try:
            self.peek()
        except StopIteration:
            return False
        return True

    def peek(self,
             default=_marker) -> object | Any | _KT | _VT | tuple[str, Any]:
        try:
            peeked = next(self)
        except StopIteration:
            if default is _marker:
                raise
            return default
        if self._index is None:
            self._index = len(self._cache)
        self._index -= 1
        return peeked

    def elements(self) -> SequenceView:
        return SequenceView(self._cache)

    def seek(self, index) -> Self:
        self._index = index
        remainder = index - len(self._cache)
        if remainder > 0:
            consume(self, remainder)
        return self

    def relative_seek(self, count) -> Self:
        if self._index is None:
            self._index = len(self._cache)

        self.seek(max(self._index + count, 0))
        return self

    @property
    def it(
        self
    ) -> Iterator[_VT | _KT | tuple[
            _KT, _VT]] | AsyncIterator[_VT | _KT | tuple[_KT, _VT]]:
        if self.vit is not None:
            return self.vit
        if self.kit is not None:
            return self.kit
        if self.avit is not None:
            return self.avit
        if self.ait is not None:
            return self.ait
        if self._it is None:
            self._it = iter(self._source)
        return self._it

    @it.setter
    def it(self, value: Iterator[_VT | _KT | tuple[_KT, _VT]]) -> None:
        self._it = value

    if not TYPE_CHECKING:

        def __getattr__(self, name):
            if hasattr(self.it, name):
                return getattr(object.__getattribute__(self, "it"), name)
            if hasattr(self._source, name):
                return getattr(object.__getattribute__(self, "_source"), name)

            return object.__getattribute__(self, name)
    else:

        @property
        def __getitem__(self):
            return self._source.__getitem__

        @property
        def __setitem__(self):
            return self._source.__setitem__

        @property
        def __getattr__(self):
            return self._source.__getattribute__

        @property
        def __setattr__(self):
            return self._source.__setattr__

    __name__ = "CollectIterator"

    def send(self, value: Any) -> _VT:
        if isinstance(self.avit, CoroutineType):
            return self.avit.send(value)
        if isinstance(self.vit, GeneratorType):
            return self.vit.send(value)
        raise TypeError(f"{self.__name__} is not a coroutine or generator.")

    def throw(self, exc: BaseException) -> _VT:
        if isinstance(self.avit, CoroutineType):
            return self.avit.throw(exc)
        if isinstance(self.vit, GeneratorType):
            return self.vit.throw(exc)
        raise TypeError(f"{self.__name__} is not a coroutine or generator.")

    def close(self) -> None:
        if isinstance(self.avit, CoroutineType):
            return self.avit.close()
        if isinstance(self.vit, GeneratorType):
            return self.vit.close()
        raise TypeError(f"{self.__name__} is not a coroutine or generator.")

    def containing(self, key: str) -> Callable[[str], bool]:
        return lambda e: e is not None and key in e


def seekable(iterable: Iterable[_T]) -> Seekable[_T]:
    it = Seekable(iterable)
    return it


def rpartial(func, *args, **kwargs):
    """Partially applies last arguments.

    New keyworded arguments extend and override kwargs.
    """  # noqa: D401
    return lambda *a, **kw: func(*(a + args), **dict(kwargs, **kw))


class MissingT:
    pass


_initial_missing = MissingT()


def insort_right(
    a: list[_T],
    x: _T,
    lo: int = 0,
    hi: int | None = None,
    key: Callable[[_T], Any] | None = None,
) -> None:
    """Insert item x in list a, and keep it sorted assuming a is sorted.

    If x is already in a, insert it to the right of the rightmost x.

    Optional args lo (default 0) and hi (default len(a)) bound the
    slice of a to be searched.

    A custom key function can be supplied to customize the sort order.
    """
    lo = bisect_right(a, x, lo, hi) if key is None else bisect_right(
        a, key(x), lo, hi, key=key)
    a.insert(lo, x)


def bisect_right(a: list[_T],
                 x: _T,
                 lo: int = 0,
                 hi: int | None = None,
                 key: Callable[[_T], Any] | None = None) -> int:
    """Return the index where to insert item x in list a, assuming a is sorted.

    The return value i is such that all e in a[:i] have e <= x, and all e in
    a[i:] have e > x.  So if x already appears in the list, a.insert(i, x) will
    insert just after the rightmost x already there.

    Optional args lo (default 0) and hi (default len(a)) bound the
    slice of a to be searched.

    A custom key function can be supplied to customize the sort order.
    """
    if lo < 0:
        raise ValueError("lo must be non-negative")
    if hi is None:
        hi = len(a)
    # Note, the comparison uses "<" to match the
    # __lt__() logic in list.sort() and in heapq.
    if key is None:
        while lo < hi:
            mid = (lo + hi) // 2
            if x < a[mid]:
                hi = mid
            else:
                lo = mid + 1
    else:
        while lo < hi:
            mid = (lo + hi) // 2
            if x < key(a[mid]):
                hi = mid
            else:
                lo = mid + 1
    return lo


def insort_left(a: list[_T],
                x: _T,
                lo: int = 0,
                hi: int | None = None,
                key: Callable[[_T], Any] | None = None) -> None:
    """Insert item x in list a, and keep it sorted assuming a is sorted.

    If x is already in a, insert it to the left of the leftmost x.

    Optional args lo (default 0) and hi (default len(a)) bound the
    slice of a to be searched.

    A custom key function can be supplied to customize the sort order.
    """
    lo = bisect_left(a, x, lo, hi) if key is None else bisect_left(
        a, key(x), lo, hi, key=key)
    a.insert(lo, x)


def bisect_left(a: list[_T],
                x: _T,
                lo: int = 0,
                hi: int | None = None,
                key: Callable[[_T], Any] | None = None) -> int:
    """Return the index where to insert item x in list a, assuming a is sorted.

    The return value i is such that all e in a[:i] have e < x, and all e in
    a[i:] have e >= x.  So if x already appears in the list, a.insert(i, x) will
    insert just before the leftmost x already there.

    Optional args lo (default 0) and hi (default len(a)) bound the
    slice of a to be searched.

    A custom key function can be supplied to customize the sort order.
    """
    if lo < 0:
        raise ValueError("lo must be non-negative")
    if hi is None:
        hi = len(a)
    # Note, the comparison uses "<" to match the
    # __lt__() logic in list.sort() and in heapq.
    if key is None:
        while lo < hi:
            mid = (lo + hi) // 2
            if a[mid] < x:
                lo = mid + 1
            else:
                hi = mid
    else:
        while lo < hi:
            mid = (lo + hi) // 2
            if key(a[mid]) < x:
                lo = mid + 1
            else:
                hi = mid
    return lo


# ### Error handling utilities


def raiser(exception_or_class=Exception, *args, **kwargs):
    """Construct function that raises the given exception with given arguments on any invocation."""
    if isinstance(exception_or_class, str):
        exception_or_class = Exception(exception_or_class)

    def _raiser(*a, **kw):
        if args or kwargs:
            raise exception_or_class(*args, **kwargs)
        raise exception_or_class

    return _raiser


# Not using @decorator here for speed,
# since @ignore and @silent should be used for very simple and fast functions
def ignore(errors, default=None):
    """Alters function to ignore given errors, returning default instead."""
    errors = _ensure_exceptable(errors)

    def decorator(func):

        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except errors:
                return default

        return wrapper

    return decorator


def silent(func):
    """Alters function to ignore all exceptions."""
    return ignore(Exception)(func)


# ### Backport of Python 3.7 nullcontext
try:
    from contextlib import nullcontext
except ImportError:

    class nullcontext:
        """Context manager that does no additional processing.

        Used as a stand-in for a normal context manager, when a particular
        block of code is only sometimes used with a normal context manager:

        cm = optional_cm if condition else nullcontext()
        with cm:
            # Perform operation, using optional_cm if condition is True
        """

        def __init__(self, enter_result=None):
            self.enter_result = enter_result

        def __enter__(self):
            return self.enter_result

        def __exit__(self, *excinfo):
            pass


@contextmanager
def reraise(errors, into):
    """Reraises errors as other exception."""
    errors = _ensure_exceptable(errors)
    try:
        yield
    except errors as e:
        if callable(into) and not _is_exception_type(into):
            into = into(e)
        raise into from e


def _decorator(func: Callable[P, R], default: Any = None) -> Callable[P, R]:

    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception:
            import traceback

            print(traceback.format_exc())
            return default

    return wrapper


class _Wrapper(Protocol[P, R]):
    func: Callable[P, R]
    blocked: datetime | None
    fails: int

    def __init__(self, func: Callable[P, R]) -> None:
        self.func = func
        self.blocked = None
        self.fails = 0

    def __call__(self, *args: Any, **kwds: Any) -> Any:
        return self.func(*args, **kwds)


class Wrapper(Generic[P, R], _Wrapper[P, R]):
    ...


decorator = Wrapper(_decorator)


@decorator
def retry(call,
          tries,
          errors=Exception,
          timeout=0,
          filter_errors=None) -> Any | None:
    """Make decorated function retry up to tries times.

    Retries only on specified errors.
    Sleeps timeout or timeout(attempt) seconds between tries.
    """
    errors = _ensure_exceptable(errors)
    for attempt in range(tries):
        try:
            return call()
        except errors as e:
            if not (filter_errors is None or filter_errors(e)):
                raise

            # Reraise error on last attempt
            if attempt + 1 == tries:
                raise
            timeout_value = timeout(attempt) if callable(timeout) else timeout
            if timeout_value > 0:
                time.sleep(timeout_value)
    return None


def fallback(
    *approaches: tuple[Callable[[], R],
                       type[BaseException] | tuple[type[BaseException], ...]]
) -> R | None:
    """Try several approaches until one works.

    Each approach has a form of (callable, expected_errors).
    """
    for approach in approaches:
        func, catch = (approach,
                       BaseException) if callable(approach) else approach
        catch = _ensure_exceptable(catch)
        try:
            return func()
        except catch:
            pass
    return None


def _is_exception_type(value):
    return isinstance(value, type) and issubclass(value, BaseException)


def _ensure_exceptable(
    errors: type[BaseException] | tuple[type[BaseException], ...],
) -> tuple[type[BaseException], ...] | type[BaseException]:
    """Ensure that errors are passable to except clause.

    I.e. should be BaseException subclass or a tuple.
    """
    return errors if _is_exception_type(errors) else tuple(
        [errors] if isinstance(errors, type) else errors)


class ErrorRateExceededError(Exception):
    pass


def limit_error_rate(fails: int, timeout: int | timedelta,
                     exception: Exception):
    """If function fails to complete fails times in a row, calls to it will be intercepted for timeout.

    Raises the specified exception during the timeout period.
    """
    if isinstance(timeout, int):
        timeout = timedelta(seconds=timeout)

    def decorator(func: Callable[P, R]) -> Wrapper[P, R]:
        wrapper = Wrapper(func)

        @wraps(func)
        def wrapped(*args: P.args, **kwargs: P.kwargs) -> R:
            if wrapper.blocked:
                if now() - wrapper.blocked < timeout:
                    raise exception
                wrapper.blocked = None

            try:
                result = func(*args, **kwargs)
            except:  # noqa
                wrapper.fails += 1
                if wrapper.fails >= fails:
                    wrapper.blocked = now()
                raise
            else:
                wrapper.fails = 0
                return result

        # Modify the wrapper instance to use our wrapped function
        wrapper.__call__ = wrapped
        wrapper.fails = 0
        wrapper.blocked = None
        return wrapper

    return decorator


def throttle(period):
    """Allow only one run in a period, the rest is skipped."""
    if isinstance(period, timedelta):
        period = period.total_seconds()

    def decorator(func):

        @wraps(func)
        def wrapper(*args, **kwargs):
            now = time()
            if wrapper.blocked_until and wrapper.blocked_until > now:
                return None
            wrapper.blocked_until = now + period

            return func(*args, **kwargs)

        wrapper.blocked_until = None
        return wrapper

    return decorator


def athrottle(period):
    """Async version of throttle."""
    if isinstance(period, timedelta):
        period = period.total_seconds()

    def decorator(func):

        @wraps(func)
        async def wrapper(*args, **kwargs):
            now = time()
            if wrapper.blocked_until and wrapper.blocked_until > now:
                return None
            wrapper.blocked_until = now + period

            return await func(*args, **kwargs)


# ### Post processing decorators


@decorator
def post_processing(call: Callable[[], R],
                    func: Callable[[R], U] | None = None) -> U | Callable:
    """Post processes decorated function result with func."""
    if func is None:
        return lambda: call()
    return func(call())


collecting = post_processing(list)
collecting.__name__ = "collecting"
collecting.__doc__ = "Transforms a generator into list returning function."

post_processes = post_processing


@decorator
def joining(call, sep):
    """Join decorated function results with sep."""
    return sep.join(map(sep.__class__, call()))


class cached_property(Generic[_T]):
    """Decorator that converts a method with a single self argument into a property cached on the instance."""

    fset = fdel = None

    def __init__(self, fget: FunctionType) -> None:
        self.fget = fget
        self.__doc__ = fget.__doc__
        self.__signature__ = signature(fget)

    def __get__(self,
                instance: _T,
                owner: Type[_T] | None = None) -> _T | Self:
        if instance is None:
            return self
        res = instance.__dict__[self.fget.__name__] = self.fget(instance)
        return res


class cached_readonly(cached_property):
    """Same as @cached_property, but protected against rewrites."""

    def __set__(self, instance, value):
        raise AttributeError("property is read-only")


def wrap_prop(ctx):
    """Wrap a property accessors with a context manager."""

    def decorator(prop: property):

        class WrapperProp:

            def __repr__(self):
                return repr(prop)

            def __get__(self, instance, type=None):
                if instance is None:
                    return self

                with ctx:
                    return prop.__get__(instance, type)

            if hasattr(prop, "__set__"):

                def __set__(self, name, value):
                    with ctx:
                        return prop.__set__(name, value)

            if hasattr(prop, "__del__"):

                def __del__(self, name):
                    with ctx:
                        return prop.__delete__(name)

            if hasattr(prop, "__delete__"):

                def __delete__(self, name):
                    with ctx:
                        return prop.__delete__(name)

        return WrapperProp()

    return decorator


class Predicate(PredicateType[P, _T], Generic[P, _T]):
    ...


def _filterfalse(iterable: Iterable[_T], predicate=None) -> Iterable[_T]:
    if predicate is None:
        predicate = bool
    return (item for item in iterable if not predicate(item))


def _equals(*values: T) -> Callable[Concatenate[T, ...], bool]:
    return lambda x: x in values


def _nonzero(d):
    return {k: v for k, v in d.items() if v}


def _notequals(*values: T) -> Callable[Concatenate[T, ...], bool]:
    return lambda x: x not in values


def _isnone(x):
    return x is None


def _notnone(x):
    return x is not None


def _inc(x):
    return x + 1


def _dec(x):
    return x - 1


def _even(x):
    return x % 2 == 0


def _odd(x):
    return x % 2 == 1


IterT = TypeVar("IterT", bound=SupportsIter | Iterable | Indexable)
MappingT = TypeVar("MappingT", bound=dict)


@overload
def notnone(d: MappingT) -> MappingT:
    ...


@overload
def notnone(d: IterT) -> IterT:
    ...


def notnone(d: IterT | MappingT) -> MappingT | IterT:
    """Remove None values from mappings or iterables.

    For mappings, removes keys with None values.
    For iterables, removes None elements.
    For other types, returns unchanged.
    """
    if not isinstance(d, (Mapping, Iterator, SupportsIter)) or isinstance(
            d, (str, bytes)):
        return d

    if isinstance(d, Mapping | MutableMapping | SupportsKeysItems):
        return type(d)(**{k: v for k, v in d.items() if v is not None})

    return type(d)([x for x in d if x is not None]) if hasattr(
        d, "__iter__") else d  # type: ignore


filterfalse = Predicate(_filterfalse)
equals = Predicate(_equals)
eq = Predicate(_equals)
nonzero = Predicate(_nonzero)
notequals = Predicate(_notequals)
isnone = Predicate(_isnone)
isnotnone = Predicate(_notnone)
inc = Predicate(_inc)
dec = Predicate(_dec)
even = Predicate(_even)
odd = Predicate(_odd)

ismapping = Is[Mapping]
isset = Is[Set]
isseq = Is[Sequence]
islist = Is[list]
istuple = Is[tuple]

istuplist = Is[tuple, list]

iscountable = wrapafter(Is[list, tuple, Iterator, range].__call__,
                        returns=bool)(Is[list, tuple, Iterator,
                                         range].__call__, )

iterable = Is[Iterable]
isiterator = Is[Iterator]


def iscollection(x):
    return bool(hasattr(x, "__iter__")
                and not isinstance(x, str)) or isinstance(x, SimpleNamespace)


@overload
def copyiter(iterable: Iterable[_T]) -> tuple[Iterable[_T], Iterable[_T]]:
    ...


@overload
def copyiter(iterable: Any) -> tuple[Any, Any]:
    ...


def copyiter(
    iterable
):  # -> tuple[list[Any], seekable[Any]] | tuple[Any | str, Any | str]:
    """Copy an iterable into a list."""
    if hasattr(iterable, "as_string"):
        return iterable, iterable
    if hasattr(iterable, "__iter__") and not isinstance(iterable, str):
        x = seekable(iterable)
        x.seek(0)
        cp, sec = tee(x)
        cp = list(sec)
        x.seek(0)
        return cp, x
    return iterable, iterable


@overload
def tap(
    loglevel: "LOGLEVEL | LevelType " = "debug",
    stack_info=False,
    inspect_all=False,
    pause=False,
) -> Callable[[Callable[P, _T]], Callable[P, _T]]:
    ...


@overload
def tap(func: Callable[P, _T]) -> Callable[P, _T]:
    ...


def tap(
    *args: "Callable[P, _T] | LOGLEVEL | LevelType | bool",
    **kwargs,
) -> Callable[P, _T] | Callable[[Callable[P, _T]], Callable[P, _T]]:
    """Print arguments of function and return value."""
    a = list(args)
    func = kwargs.pop("func",
                      a.pop(0) if callable(next(iter(a), None)) else None)
    loglevel = kwargs.pop(
        "loglevel",
        a.pop(0) if isinstance(next(iter(a), None), str) else "debug")
    stack_info = kwargs.pop(
        "stack_info",
        a.pop(0) if isinstance(next(iter(a), None), bool) else False)
    pause = kwargs.pop(
        "pause",
        a.pop(0) if isinstance(next(iter(a), None), bool) else False)

    def decorator(func):

        @wraps(func)
        def wrapper(*args: P.args, **kwargs: P.kwargs) -> _T:
            from mbcore.display import safe_print
            from mbcore.log import callstack, log, to_log_level

            if stack_info:
                for c in callstack(3):
                    safe_print(c)
            if not TYPE_CHECKING:
                args = list(args)
            cp_args = []
            argslist = list(args)
            for i, x in enumerate(argslist):
                if hasattr(x, "__iter__") and not isinstance(x, str):
                    cp, out = copyiter(x)
                    argslist[i] = out
                    cp_args.append(cp)
            cp_args = cp_args or argslist
            cp_kwargs = {}
            for k, v in kwargs.items():
                if hasattr(v, "__iter__") and not isinstance(v, str):
                    cp, out = copyiter(v)
                    kwargs[k] = out
                    cp_kwargs[k] = cp
            cp_kwargs = cp_kwargs or kwargs

            cp_x, x = copyiter(func(*argslist, **kwargs))
            log(
                to_log_level[loglevel],
                f"\n\ndef {func.__name__} (args={tuple(cp_args)}, kwargs={cp_kwargs}) -> {cp_x}\n\n",
                stack_info=stack_info,
                stacklevel=1,
            )

            if pause:
                input("Press Enter to continue...")
            return x

        return wrapper

    return decorator(func) if callable(func) else decorator


def alias(d: MutableMapping[_KT, _VT],
          keymap: Mapping[_KT, _KT]) -> MutableMapping[_KT, _VT]:
    """Map keys in a dictionary."""
    return {keymap.get(k, k): v for k, v in d.items()}


def calling(callable_attr: str, *args, **kwargs) -> Callable[..., Any]:
    """Create a function calling a method of the object with given args and kwargs."""
    return lambda obj: getattr(obj, callable_attr)(*args, **kwargs)


def accessing(attr: str) -> Callable[..., Any]:
    """Create a function accessing an attribute of the object."""
    return lambda obj: getattr(obj, attr)


async def asyncaccessing(attr: str) -> Callable[..., Any]:
    """Create a function accessing an attribute of the object."""

    async def _accessing(obj):
        return await getattr(obj, attr)

    return _accessing


accesses = accessing


def mapkeys(func: Callable[[_KT], _KT] | Mapping[_KT, _KT],
            d: Mapping[_KT, _VT]) -> dict[_KT, _VT]:
    """Map keys in a dictionary."""
    if not isinstance(d, Mapping):
        return d
    if callable(func):
        return {func(k): mapkeys(func, v) for k, v in d.items()}
    if isinstance(func, Mapping):
        return {func.get(k, k): mapkeys(func, v) for k, v in d.items()}


def repeatedly(f: Callable[[], _T], n: int | Empty = EMPTY) -> Iterable[_T]:
    """Return Iterator that yields the result of f() endlessly or up to n times.

    Takes a function of no args, presumably with side effects,
    and returns an infinite (or length n) iterator of calls to it.
    """
    _repeat = repeat(None) if n is EMPTY else repeat(None, n)
    return (f() for _ in _repeat)


def iterate(f: Callable[[_T], _T], x: _T) -> Iterable[_T]:
    """Return an infinite iterator of `x, f(x), f(f(x)), ...`."""
    while True:
        yield x
        x = f(x)


def take(n: int, seq: Iterable[_T]) -> Iterable[_T]:
    """Return  a list of first n items in the sequence, or less if the sequence is shorter."""
    return list(islice(seq, n))


def drop(n: int, seq: Iterable[_T]) -> Iterable[_T]:
    """Skips first n items in the sequence, yields the rest."""
    return islice(seq, n, None)


def _make_getter(regex: Pattern):
    if regex.groups == 0:
        return methodcaller("group")
    if regex.groups == 1 and regex.groupindex == {}:
        return methodcaller("group", 1)
    if regex.groupindex == {}:
        return methodcaller("groups")
    if regex.groups == len(regex.groupindex):
        return methodcaller("groupdict")
    return lambda m: m


class _WrapperType(Protocol):
    __wrapped__: "function | MethodType | FunctionType"


def unwrap(func: "_RW") -> "_RW":
    while hasattr(func, "__wrapped__"):
        func = func.__wrapped__
    return func


def get_argnames(func: "FunctionType") -> Iterable[str]:
    func = getattr(func, "__original__", None) or unwrap(func)
    return func.__code__.co_varnames[:func.__code__.co_argcount]


def _prepare(regex, flags):
    if not isinstance(regex, re.Match):
        regex = re.compile(regex, flags)
    return regex, _make_getter(regex)


def re_iter(regex: Pattern, s, flags=0):
    """Iterate over matches of regex in s, presents them in simplest possible form."""
    regex, getter = _prepare(regex, flags)
    return map(getter, regex.finditer(s))


def re_all(regex, s, flags=0):
    """List all matches of regex in s, presents them in simplest possible form."""
    return list(re_iter(regex, s, flags))


def re_finder(regex, flags=0):
    """Create a function finding regex in passed string."""
    regex, _getter = _prepare(regex, flags)
    getter = lambda m: _getter(m) if m else None
    return lambda s: getter(regex.search(s))


def re_find(regex, s, flags=0):
    """Match regex against the given string, return the match in the simplest possible form."""
    return re_finder(regex, flags)(s)


def str_join(sep, seq=EMPTY):
    """Join the given sequence with sep. Forces stringification of seq items."""
    if seq is EMPTY:
        return str_join("", sep)
    return sep.join(map(sep.__class__, seq))


def cut_prefix(s, prefix):
    """Cuts prefix from given string if it's present."""
    return s[len(prefix):] if s.startswith(prefix) else s


def cut_suffix(s, suffix):
    """Cuts suffix from given string if it's present."""
    return s[:-len(suffix)] if s.endswith(suffix) else s


def re_tester(regex, flags=0):
    """Create a predicate testing passed string with regex."""
    if not isinstance(regex, re.Match):
        regex = re.compile(regex, flags)
    return lambda s: bool(regex.search(s))


def re_test(regex, s, flags=0):
    """Test whether regex matches against s."""
    return re_tester(regex, flags)(s)


def makefunc(f, test=False):
    """Convert various types of inputs into callable functions.

    This utility function creates a callable function from different types of inputs,
    useful for filtering, mapping, and testing operations.

    Args:
        f: Input to be converted to a function. Can be one of:
            - callable: Returns the callable as-is
            - None: Returns bool if test=True, or identity function if test=False
            - str/bytes/regex: Returns regex tester if test=True, or finder if test=False
            - int/slice: Returns an itemgetter function
            - dict-like: Returns the __getitem__ method
            - set-like: Returns the __contains__ method
        test (bool, optional): Flag to modify behavior for None and regex inputs.
            Defaults to False.

    Returns:
        callable: A function that can be used for filtering, mapping or testing.

    Raises:
        TypeError: If the input type cannot be converted to a function.

    Examples:
        >>> makefunc(lambda x: x > 5)  # Returns the function as-is
        <function <lambda> at ...>

        >>> makefunc(None)  # Returns identity function
        <function <lambda> at ...>

        >>> makefunc(None, test=True)  # Returns bool function
        <built-in function bool>

        >>> makefunc('pattern')  # Returns regex finder
        <function re_finder at ...>

        >>> makefunc('pattern', test=True)  # Returns regex tester
        <function re_tester at ...>

        >>> makefunc(2)  # Returns itemgetter(2)
        <operator.itemgetter at ...>

        >>> makefunc({'a': 1})  # Returns dict.__getitem__
        <built-in method __getitem__ of dict object at ...>

        >>> makefunc({1, 2, 3})  # Returns set.__contains__
        <built-in method __contains__ of set object at ...>

    """
    if callable(f):
        return f
    if f is None:
        # pass None to builtin as predicate or mapping function for speed
        return bool if test else lambda x: x
    if isinstance(f, bytes | str | re.Match):
        return re_tester(f) if test else re_finder(f)
    if isinstance(f, int | slice):
        return itemgetter(f)
    if isinstance(f, Mapping):
        return f.__getitem__
    if isinstance(f, Set):
        return f.__contains__
    raise TypeError(f"Can't make a func from {f.__class__.__name__}")


def make_pred(pred):
    return makefunc(pred, test=True)


def safe_next(iterable, default=None):
    """Return the next item from the iterator, or default if the iterator is exhausted."""
    try:
        it = iterable if hasattr(iterable, "__next__") else iter(iterable)
        return next(it)
    except StopIteration:
        return default


def safe_one(iterable, default=None):
    """Return the first item from the iterable, or default on failure."""
    return safe_next(iterable, default=default)


@overload
def first(iterable: SupportsIter[_T], default: _T | None = None) -> _T:
    ...


@overload
def first(iterable: SupportsIter[_T],
          pred: Callable[[_T], bool],
          default: _T | None = None) -> _T | None:
    ...


@overload
def first(pred: Callable[[_T], bool],
          iterable: SupportsIter[_T],
          default: _T | None = None) -> _T | None:
    ...


def first(*args, **kwargs):
    """Return the first item in the sequence or the first item passing the predicate.

    Returns None if the sequence is empty.
    """
    from mbcore.even.more import pull_out

    clbls, args = pull_out(callable, chain(args, kwargs.values()))
    pred = safe_one(clbls)
    from mbcore.more import collapse

    args = list(collapse(args))

    iterable, default = args if ilen_view(args, False) == 2 else (args, None)
    if not pred:
        return next(iter(iterable), default)
    return next(_filter(pred, iterable), default)


@overload
def first_remaining(
    iterable: GetItemIterable[_SupportsNextT]
) -> tuple[_SupportsNextT, Iterator[_SupportsNextT]]:
    ...


@overload
def first_remaining(
    iterable: SupportsIter[_SupportsNextT]
) -> tuple[_SupportsNextT, Iterator[_SupportsNextT]]:
    ...


def first_remaining(
    iterable: SupportsIter | GetItemIterable[_SupportsNextT],
) -> tuple[_SupportsNextT, Iterator[_SupportsNextT]]:
    """Return the first item and the remaining iterator."""
    iterator = iter(iterable)
    first_item = next(iterator)
    return first_item, iterator


@overload
def safe_first(iterable: SupportsIter[_SupportsNextT],
               default: U = None) -> U | _SupportsNextT:
    ...


@overload
def safe_first(iterable: GetItemIterable[_SupportsNextT],
               default: U = None) -> U | _SupportsNextT:
    ...


def safe_first(iterable: SupportsIter[_SupportsNextT]
               | GetItemIterable[_SupportsNextT],
               default: U = None):
    """Return the first item in an iterable or None if it's empty."""
    return first(iterable, default=default)


def safe_second(iterable: GetItemIterable[_SupportsNextT],
                default: U | _SupportsNextT = None) -> U | _SupportsNextT:
    """Return the second item in an iterable or None if it's empty."""
    try:
        iterator = iter(iterable)
        next(iterator)
        return next(iterator)
    except StopIteration:
        return default


def second(seq):
    """Return second item in the sequence.

    Return None if there are less than two items in it.
    """
    return first(rest(seq))


def nth(n, seq):
    """Return nth item in the sequence or None if no such item exists."""
    try:
        return seq[n]
    except IndexError:
        return None
    except TypeError:
        return next(islice(seq, n, None), None)


def last(seq):
    """Return the last item in the sequence or iterator.

    Return None if the sequence is empty.
    """
    try:
        return seq[-1]
    except IndexError:
        return None
    except TypeError:
        item = None
        for x in seq:
            item = x
        return item


def rest(seq):
    """Skips first item in the sequence, yields the rest."""
    return drop(1, seq)


def butlast(seq):
    """Iterate over all elements of the sequence but last."""
    it = iter(seq)
    try:
        prev = next(it)
    except StopIteration:
        pass
    else:
        for item in it:
            yield prev
            prev = item


def filter(pred, seq):
    """List filter results.

    Derives a predicate from string, int, slice, dict or set.
    """
    return _filter(make_pred(pred), seq)


def map(f, *seqs):
    """Map each item in the sequence(s) through the function.

    Derives a mapper from string, int, slice, dict or set.

    Example:
        map("name", users)  # Returns a list of names from users

    """
    if ilen_view(seqs, consume=False) == 1:
        out = _map(makefunc(f), seqs[0])
        return out
    _map(makefunc(f), *seqs)
    return (*seqs, )


def remove(pred, seq):
    """Iterate items passing given predicate."""
    return filterfalse(seq, make_pred(pred))


def keep(f: Callable[..., Any] | None,
         seq: Iterable[_T] | Empty = EMPTY) -> Iterator[_T]:
    """Filter items that are truthy after applying f.

    When called with single argument, acts as a filter for truthy values.

    Examples:
        >>> list(keep(lambda x: x > 0, [-1, 0, 1, 2]))
        [1, 2]

        >>> list(keep([0, 1, '', 'x']))
        [1, 'x']

    """
    if seq is EMPTY:
        return filter(bool, f)
    return filter(bool, map(f, seq))


def without(seq: Iterable[_T], *items: _T) -> Iterator[_T]:
    """Iterate over sequence skipping specified items.

    Examples:
        >>> list(without([1,2,3,4], 2, 4))
        [1, 3]

        >>> list(without('abcde', 'b', 'd'))
        ['a', 'c', 'e']

    """
    for value in seq:
        if value not in items:
            yield value


concat: Callable[..., Iterator[Any]] = chain
"""Concatenate arbitrary number of iterables into one.

Examples:
    >>> list(concat([1, 2], [3, 4], [5, 6]))
    [1, 2, 3, 4, 5, 6]
    >>> list(concat([], [1], [2, 3]))
    [1, 2, 3]
"""

cat: Callable[[Iterable[Iterable[_T]]], Iterator[Any]] = chain.from_iterable
"""Concatenate multiple iterables into one.

Examples:
    >>> list(cat([[1, 2], [3, 4], [5, 6]]))
    [1, 2, 3, 4, 5, 6]
    >>> list(cat([[[], [1]], [[2], [3]]]))
    [[], [1], [2], [3]]
"""


def caller(*args: _P.args,
           **kwargs: _P.kwargs) -> Callable[[Callable[_P, _T]], _T]:
    """Create a function calling its argument with given args and kwargs.

    Examples:
        >>> call_with_5 = caller(5)
        >>> call_with_5(lambda x: x * 2)
        10

        >>> greet = caller('Hello', name='World')
        >>> greet(lambda x, name: f'{x} {name}!')
        'Hello World!'

    """
    return lambda f: f(*args, **kwargs)


def partial(func: "Callable[Concatenate[...,_P], _R]", *args: _P.args,
            **kwargs: _P.kwargs) -> Callable[..., _R]:
    """Return a real partial function that can be used as method.

    Examples:
        >>> add5 = partial(int.__add__, 5)
        >>> add5(10)
        15

        >>> format_with_name = partial(str.format, name='World')
        >>> format_with_name('Hello {name}!')
        'Hello World!'

    """
    if not args:
        return lambda *a, **kw: func(*a, **dict(kwargs, **kw))
    return lambda *a, **kw: func(*(args + a), **dict(kwargs, **kw))


def doesnot(func: Callable[..., Any]) -> Callable[..., bool]:
    """Return a function that negates the result of the input function.

    Examples:
        >>> is_even = lambda x: x % 2 == 0
        >>> is_odd = doesnot(is_even)
        >>> is_odd(3)
        True

    """
    return compose(not_, func)


def isnot(value: _T) -> Callable[[_T], bool]:
    """Create a function checking inequality with the given value.

    Examples:
        >>> not_none = isnot(None)
        >>> not_none(5)
        True
        >>> not_none(None)
        False

    """
    return lambda x: x != value


P = ParamSpec("P")
_R = TypeVar("_R")
_Ts = TypeVarTuple("_Ts")


@overload
def compose(f: Callable[..., _R], g: Callable[[Unpack[_Ts]], _T],
            /) -> Callable[[Unpack[_Ts]], _R]:
    ...


@overload
def compose():
    ...


def compose(*fs):
    """Composes passed functions.

    Examples:
        >>> inc = lambda x: x + 1
        >>> double = lambda x: x * 2
        >>> inc_then_double = compose(double, inc)
        >>> inc_then_double(3)  # (3 + 1) * 2
        8

    """
    if fs:

        def pair(f, g):
            return lambda *a, **kw: f(g(*a, **kw))

        return reduce(pair, map(makefunc, fs))
    return identity


@overload
def rcompose(f: Callable[[Any], _T], g: Callable[[_T], _S],
             h: Callable[[_S], _R], /) -> Callable[[Any], _R]:
    ...


@overload
def rcompose(f: Callable[[Any], _T], g: Callable[[_T], _S],
             /) -> Callable[[Any], _S]:
    ...


def rcompose(*fs):
    """Composes functions, calling them from left to right."""
    return compose(*reversed(fs))


def isa(*types: Type) -> Callable[[Any], bool]:
    """Create a function checking if its argument is of any of given types."""
    return lambda x: isinstance(x, types)


T = TypeVar("T")

from typing import (  # noqa: E402
    Any, Callable, Iterable, Iterator, Mapping, TypeVar, overload,
)

_T = TypeVar("_T")
_KT = TypeVar("_KT")
_VT = TypeVar("_VT")

_KT = TypeVar("_KT")
_VT = TypeVar("_VT")
_T = TypeVar("_T")


def constantly(x):
    """Create a function accepting any args, but always returning x."""
    return lambda *a, **kw: x


def flatten(seq, follow=iscountable):
    """Flattens arbitrary nested sequence.

    Unpacks an item if follow(item) is truthy.
    """
    for item in seq:
        if follow(item):
            yield from flatten(item, follow)
        else:
            yield item


def mapcat(f, *seqs):
    """Map given sequence(s) and chains the results."""
    return cat(map(f, *seqs))


def interleave(*seqs):
    """Yield first item of each sequence, then second one and so on."""
    return cat(zip(*seqs, strict=False))


def interpose(sep, seq):
    """Yield items of the sequence alternating with sep."""
    return drop(1, interleave(repeat(sep), seq))


def takewhile(pred, seq=EMPTY):
    """Yield sequence items until first predicate fail.

    Stops on first falsy value in one argument version.
    """
    if seq is EMPTY:
        pred, seq = bool, pred
    else:
        pred = make_pred(pred)
    return _takewhile(pred, seq)


def dropwhile(pred, seq=EMPTY):
    """Skip the start of the sequence passing pred (or just truthy), yield the rest."""
    if seq is EMPTY:
        pred, seq = bool, pred
    else:
        pred = make_pred(pred)
    return _dropwhile(pred, seq)


def distinct(seq, key=EMPTY):
    """Iterate over sequence skipping duplicates."""
    seen = set()
    # check if key is supplied out of loop for efficiency
    if key is EMPTY:
        for item in seq:
            if item not in seen:
                seen.add(item)
                yield item
    else:
        key = makefunc(key)
        for item in seq:
            k = key(item)
            if k not in seen:
                seen.add(k)
                yield item


def split(pred, seq):
    """Lazily split items which pass the predicate from the ones that don't.

    Returns a pair (passed, failed) of respective iterators.
    """
    pred = make_pred(pred)
    yes, no = deque(), deque()
    splitter = (yes.append(item) if pred(item) else no.append(item)
                for item in seq)

    def _split(q):
        while True:
            while q:
                yield q.popleft()
            try:
                next(splitter)
            except StopIteration:
                return

    return _split(yes), _split(no)


def split_at(n, seq):
    """Lazily splits the sequence at given position, returning a pair of iterators over its start and tail."""
    a, b = tee(seq)
    return islice(a, n), islice(b, n, None)


def split_by(pred, seq):
    """Lazily split the start of the sequence, consisting of items passing pred, from the rest of it."""
    a, b = tee(seq)
    return takewhile(pred, a), dropwhile(pred, b)


def groupby(f, seq):
    """Group given sequence items into a mapping f(item) -> [item, ...]."""
    f = makefunc(f)
    result = defaultdict(list)
    for item in seq:
        result[f(item)].append(item)
    return result


def groupby_keys(get_keys, seq):
    """Group items having multiple keys into a mapping key -> [item, ...].

    Item might be repeated under several keys.
    """
    get_keys = makefunc(get_keys)
    result = defaultdict(list)
    for item in seq:
        for k in get_keys(item):
            result[k].append(item)
    return result


def groupvals(seq):
    """Take a sequence of (key, value) pairs and groups values by keys."""
    result = defaultdict(list)
    for key, value in seq:
        result[key].append(value)
    return result


def countby(f, seq):
    """Count numbers of occurrences of values of f() on elements of given sequence."""
    f = makefunc(f)
    result = defaultdict(int)
    for item in seq:
        result[f(item)] += 1
    return result


def count_reps(seq):
    """Count number occurrences of each value in the sequence."""
    result = defaultdict(int)
    for item in seq:
        result[item] += 1
    return result


def _cut_seq(drop_tail, n, step, seq):
    limit = len(seq) - n + 1 if drop_tail else len(seq)
    return (seq[i:i + n] for i in range(0, limit, step))


def _cut_iter(drop_tail, n, step, seq):
    it = iter(seq)
    pool = take(n, it)
    while True:
        if len(pool) < n:
            break
        yield pool
        pool = pool[step:]
        pool.extend(islice(it, step))
    if not drop_tail:
        yield from _cut_seq(drop_tail, n, step, pool)


def _cut(drop_tail, n, step, seq=EMPTY):
    if seq is EMPTY:
        step, seq = n, step
    if isinstance(seq, Sequence):
        return _cut_seq(drop_tail, n, step, seq)
    return _cut_iter(drop_tail, n, step, seq)


def partition(n, step, seq=EMPTY):
    """Lazily partition seq into parts of length n.

    Skips step items between parts if passed. Non-fitting tail is ignored.
    """
    return _cut(True, n, step, seq)


def chunks(n, step, seq=EMPTY):
    """Lazily chunk seq into parts of length n or less.

    Skips step items between parts if passed.
    """
    return _cut(False, n, step, seq)


def partition_by(f, seq):
    """Lazily partition seq into continuous chunks with constant value of f."""
    f = makefunc(f)
    for _, items in groupby(seq, f):
        yield items


def with_prev(seq, fill=None):
    """Yield each item paired with its preceding: (item, prev)."""
    a, b = tee(seq)
    return zip(a, chain([fill], b), strict=False)


def with_next(seq, fill=None):
    """Yield each item paired with its following: (item, next)."""
    a, b = tee(seq)
    next(b, None)
    return zip(a, chain(b, [fill]), strict=False)


# An itertools recipe
# NOTE: this is the same as ipartition(2, 1, seq) only faster and with distinct name
def pairwise(seq):
    """Yield all pairs of neighboring items in seq."""
    a, b = tee(seq)
    next(b, None)
    return zip(a, b, strict=False)


def _reductions(f, seq, acc):
    last = acc
    for x in seq:
        last = f(last, x)
        yield last


def reductions(f, seq, acc=EMPTY):
    """Yield intermediate reductions of seq by f."""
    if acc is EMPTY:
        return accumulate(seq) if f is add else accumulate(seq, f)
    return _reductions(f, seq, acc)


def sums(seq, acc=EMPTY):
    """Yield partial sums of seq."""
    return reductions(add, seq, acc)


def isdistinct(iterable, key=EMPTY):
    """Check if all elements in the iterable are different."""
    if key is EMPTY:
        return len(iterable) == len(set(iterable))
    return len(iterable) == len(set(xmap(key, iterable)))


def all(pred, seq: Iterator = EMPTY):
    """Check if all items in seq pass pred (or are truthy)."""
    if seq is EMPTY:
        return _all(pred)
    return _all(xmap(pred, seq))


def any(pred, seq: Iterator = EMPTY):  # noqa
    """Check if any item in seq passes pred (or is truthy)."""
    if seq is EMPTY:
        return _any(pred)
    return _any(xmap(pred, seq))


def noneof(pred, seq: Iterator = EMPTY):
    """Check if none of the items in seq pass pred (or are truthy)."""
    return not any(pred, seq)


def oneof(pred, seq: Iterator = EMPTY):
    """Check whether exactly one item in seq passes pred (or is truthy)."""
    if seq is EMPTY:
        return oneof(bool, pred)
    return len(take(2, filter(pred, seq))) == 1


# Not same as in clojure! returns value found not pred(value)
def some(pred, seq: Iterator | Empty = EMPTY):
    """Find first item in seq passing pred or first that is truthy."""
    if seq is EMPTY:
        return some(bool, pred)
    return next(filter(pred, seq), None)


def _ilen(iterable: Iterable[T], consume=True):

    def _ilen(seq):
        """Consumes an iterable not reading it into memory; return the number of items.

        NOTE: implementation borrowed from http://stackoverflow.com/a/15112059/753382
        """
        counter = count()
        deque(zip(seq, counter, strict=False),
              maxlen=0)  # (consume at C speed)
        return next(counter)

    if consume:
        return _ilen(iterable)
    _cp, iterable = spy(iterable, _ilen(seekable(iterable)))
    return _ilen(iterable)


@wraps(_ilen)
def ilen_view(iterable, consume=True):
    return _ilen(iterable, consume)


@wraps(spy)
def _spy(iterable: Iterable,
         length: int = 1) -> tuple[_T | Iterable[_T], Iterable[_T]]:
    return spy(
        iterable,
        ilen_view(iterable, consume=False) if length is None else length)


@wraps(spy)
def spy_view(iterable: Iterable[_T],
             length: int = 1) -> tuple[_T | Iterable[_T], Iterable[_T]]:
    return _spy(iterable, length)


def _locate(
    iterable: Iterable[_T],
    pred: Callable[[_T], bool] | _T,
    window: int | None = None,
    consume=True,
) -> Iterator[int]:
    """Replace patterns in an iterable based on predicate, with optional window size.

    Parameters
    ----------
    iterable : Iterable[_T]
        The input iterable to search through
    pred : callable
        The predicate function to match elements
    window : int or None, optional
        Size of window for considering matches. If None, matches single elements.
    consume : bool, optional
        Whether to consume the iterable during search. Default True.

    Returns
    -------
    Iterable[int]
        Iterator yielding indices where matches were found

    Examples
    --------
    >>> list(locate([1,2,3,2,1], lambda x: x == 2))
    [1, 3]

    >>> list(locate([1,2,3,2,1], lambda x: x == 9))
    []

    >>> list(locate([1,1,1], lambda x: x == 1, window=2))
    [0, 1]

    """
    pred = pred if callable(pred) else lambda x: x == pred
    if window is not None and window < 1:
        raise ValueError("window size must be at least 1")
    if not consume:
        it, copy = spy(iterable)
        return locate(copy, pred, window)
    return locate(iterable, pred, window)


@wraps(_locate)
def locate_view(iterable, pred, window: int | None = None, consume=True):
    return collect(iterable).locate(pred, window, consume)


def zipvalues(*dicts):
    """Yield tuples of corresponding values of several dicts."""
    if len(dicts) < 1:
        raise TypeError("zip_values expects at least one argument")
    keys = set.intersection(*map(set, dicts))
    for key in keys:
        yield tuple(d[key] for d in dicts)


def zipdicts(*dicts):
    """Yield tuples like (key, (val1, val2, ...)) for each common key in all given dicts."""
    if len(dicts) < 1:
        raise TypeError("zip_dicts expects at least one argument")
    keys = set.intersection(*map(set, dicts))
    for key in keys:
        yield key, tuple(d[key] for d in dicts)


def getgetter(
    key: str | int,
    iterable: "Mapping|Iterable",
    default_getter: "Callable[[Mapping|Iterable, str|int], Any]|None" = None,
):
    if default_getter is not None:
        return default_getter, key

    if isinstance(key, str) and not key.isnumeric() and hasattr(iterable, key):
        return setdefaultattr, key
    if hasattr(iterable, "__getitem__"):
        return setdefault, key

    return setdefaultattr, key


@overload
def getin(
    iterable: MutableMapping | Iterable,
    path: list[str | int] | str | int,
    default=None,
    delimeter=".",
    getter=None,
) -> Any:
    ...


@overload
def getin(
    path: list[str | int] | str | int,
    iterable: MutableMapping | Iterable,
    default=None,
    delimeter=".",
    getter=None,
) -> Any:
    ...


def getin(*args, **kwargs):
    """Return a value at path in the given nested iterable or set a default value and return it. The first list[str|int] | str | int is the path, the second is the iterable."""
    from mbcore.even.more import pull_out_front

    args_ = list(args)

    path_, args_ = ((kwargs.get("path"),
                     args_) if "path" in kwargs else pull_out_front(
                         lambda x: (isinstance(x, list) and isinstance(
                             first(x), str | int)) or isinstance(x, str | int),
                         args_ or [],
                     ))
    iterable_, args_ = ((kwargs.get("iterable"), args_) if "iterable" in kwargs
                        else pull_out_front(iscollection, args_ or []))

    default, args_ = ((kwargs.get("default"),
                       args_) if "default" in kwargs else pull_out_front(
                           lambda x: x is not None, args_ or []))
    delimeter, args_ = ((kwargs.get("delimeter"),
                         args_) if "delimeter" in kwargs else pull_out_front(
                             lambda x: isinstance(x, str), args_ or (".", )))
    delimeter = delimeter or "."
    getter_, args_ = (kwargs.get("getter"),
                      args_) if "getter" in kwargs else pull_out_front(
                          callable, args_ or [])
    if not isinstance(path_, str | int) and isinstance(iterable_, str | int):
        path__, iterable_ = iterable_, path_
    else:
        path__ = path_
    iterable = cast(MutableMapping | Iterable, iterable_)

    path = path__.split(delimeter) if isinstance(
        path__, str) else path__ if isinstance(path__, list) else [path__]
    *idx, end = path
    out = iterable

    for i in idx:
        setdef, key = getgetter(i, out, getter_)
        out = setdef(out, key, default=default)

    setdef, end = getgetter(end, out, getter_)
    return setdef(out, end, default=default)


def setdefaultattr(iterable: namespace[_T],
                   key: str,
                   default: U = None) -> _T | U:
    """Return a value at path in the given nested iterable."""
    if not isinstance(key, str):
        raise TypeError(
            f"key must be a string, not {key.__class__.__name__}: {key}")
    if hasattr(iterable, key):
        return getattr(iterable, key)
    setattr(iterable, key, default)

    return default


def setdefault(iterable: MutableMapping[_KT, _VT | U],
               key: _KT,
               default: U = None) -> _VT | U:
    """Return a value at path in the given nested iterable."""
    return iterable.setdefault(key, default)


def getlax(iterable, path, default=None):
    """Return a value at path in the given nested iterable.

    Does not raise on a wrong iterable type along the way, but returns default.
    """
    for key in path:
        try:
            iterable = iterable[key]
        except (KeyError, IndexError, TypeError):
            return default
    return iterable


def updatein(
    iterable: MappingT | list[_T],
    path: list[str | int] | str,
    update: Callable[[Any], Any] | Any = None,
    default=None,
    delimeter=".",
) -> MappingT | list[_T]:
    """Create a copy of iterable with a value updated at path.

    Parameters
    ----------
    iterable : MappingT
        The nested structure to update
    path : list[str | int] | str
        Path to the value to update, either as a list of keys or as a delimited string
    update : Callable[[Any], Any] | Any
        Function to update the value, or new value if not callable
    default : Any
        Default value to use if path doesn't exist
    delimeter : str
        Delimiter to use if path is a string

    Returns
    -------
    MappingT
        A copy of the iterable with the value at path updated

    """

    # Handle the update parameter
    def identity_func(x: Any) -> Any:
        return x

    def constant_func(val: Any) -> Callable[[Any], Any]:

        def _inner(_: Any) -> Any:
            return val

        return _inner

    if update is None:
        # Default to identity function if None
        update_func = identity_func
    elif not callable(update):
        # If not callable, replace with the update value
        update_func = constant_func(update)
    else:
        update_func = update

    # Convert string path to list if needed
    path_list = path.split(delimeter) if isinstance(path, str) else path

    # Base case: empty path
    if not path_list:
        return update_func(iterable)

    # Handle different container types
    if isinstance(iterable, dict):
        result = dict(iterable)
        key = path_list[0]

        if len(path_list) == 1:
            # Last path element, apply update function
            current = result.get(key, default)
            result[key] = update_func(current)
        else:
            # Not at leaf yet, continue recursion
            next_val = result.get(key, {})
            if next_val is None:
                next_val = {}
            result[key] = updatein(next_val, path_list[1:], update_func,
                                   default, delimeter)

        return result

    if isinstance(iterable, list):
        result = iterable.copy()
        try:
            index = int(path_list[0]) if isinstance(path_list[0],
                                                    str) else path_list[0]

            if len(path_list) == 1:
                if 0 <= index < len(result):
                    result[index] = update_func(result[index])
            else:
                if 0 <= index < len(result):
                    next_val = result[index]
                    if next_val is None:
                        next_val = {}
                    result[index] = updatein(next_val, path_list[1:],
                                             update_func, default, delimeter)
        except (IndexError, ValueError, TypeError):
            pass

        return result

    # For other types, just return a new copy with the update applied
    return update_func(iterable)


def delin(iterable, path):
    """Create a copy of iterable with a nested key or index deleted."""
    if not path:
        return iterable
    try:
        next_iterable = iterable[path[0]]
    except (KeyError, IndexError):
        return iterable

    iterable_copy = copy(iterable)
    if len(path) == 1:
        del iterable_copy[path[0]]
    else:
        iterable_copy[path[0]] = delin(next_iterable, path[1:])
    return iterable_copy


def haspath(iterable: MappingT,
            path: list[str | int] | str,
            delimeter=".") -> bool:
    """Check if path exists in the given nested iterable."""
    for p in path.split(delimeter) if isinstance(
            path, str) else path if isinstance(path, list) else [path]:
        try:
            iterable = getattr(iterable, p) if isinstance(p, str) and hasattr(
                iterable, p) else iterable[p]
        except (KeyError, IndexError):
            return False
    return True


def getter(path, default=None, delimeter="."):
    """Create a getter function for a nested value at path."""
    return lambda iterable: getin(iterable, path, default, delimeter)


def where(mappings, **cond):
    """Iterate over mappings containing all pairs in cond."""
    items = cond.items()
    match = lambda m: all(k in m and m[k] == v for k, v in items)
    return filter(match, mappings)


def pluck(key, mappings):
    """Iterate over values for key in mappings."""
    return _map(itemgetter(key), mappings)


def _pluckattr(attr, objects):
    """Iterate over values of given attribute of given objects."""
    return _map(attrgetter(attr), objects)


def pluckattr(attr, objects):
    if isinstance(objects, str) and not isinstance(attr, str):
        attr, objects = objects, attr
    return collect(objects).pluckattr(attr)


def invoke(objects, name, *args, **kwargs):
    """Yield results of the obj.name(*args, **kwargs) for each object in objects."""
    return _map(methodcaller(name, *args, **kwargs), objects)


def aliaskeys(d: dict, keymap: dict) -> dict:
    """Map keys in a dictionary according to the given keymap."""
    return {keymap.get(k, k): v for k, v in d.items()}


def replace_append(
    iterable: Iterable[T],
    substitutes: T | Tuple[T, ...],
    pred: Callable[[T], bool],
    window: int = -1,
    if_notfound: str = "ignore",
) -> Iterable[T]:
    """Replace and optionally append if not found.

    Return seekable iterable.
    """
    sub = (
        substitutes, ) if not isinstance(substitutes, tuple) else substitutes

    copy, iterable = tee(iterable)
    found = ilen_view(locate_view(copy, pred, window), consume=False) > 0

    if found:
        return tee(replace(copy, pred, sub, window))[1]

    if if_notfound == "append":
        return tee(chain(copy, sub))[1]
    if if_notfound == "forbid":
        raise ValueError("Replacement pattern not found")
    # "ignore"
    return tee(list(copy))[1]


# Generic ops
FACTORY_REPLACE = {
    type(object.__dict__): dict,
    type({}.keys()): list,
    type({}.values()): list,
    type({}.items()): list,
}


def _factory(iterable: Iterable[_T] | Iterator[_T],
             mapper: Type[MappingT] | None = None):
    iterable_type = type(iterable)
    # Hack for defaultdicts overridden constructor
    if isinstance(iterable, defaultdict):
        item_factory = (compose(mapper, iterable.default_factory)
                        if mapper and iterable.default_factory else
                        iterable.default_factory)
        return partial(defaultdict, cast(Callable, item_factory))
    if isinstance(iterable, Iterator):
        return iter
    if isinstance(iterable, bytes | str):
        return type(iterable).join
    if iterable_type in FACTORY_REPLACE:
        return FACTORY_REPLACE[iterable_type]

    return cast(Callable[..., Iterable | Iterator], iterable_type)


def empty(iterable: Iterable[_T] | Iterator[_T]):
    """Creates an empty iterable of the same type."""
    if isinstance(iterable, SupportsIterType):
        return type(iterable)()
    return _factory(iterable)()


def iterkeys(iterable: "SupportsKeysItems"):
    """Yield keys of the given iterable."""
    return iterable.keys() if hasattr(iterable, "keys") else iterable


def iteritems(iterable: "SupportsKeysItems"):
    """Yield (key, value) pairs of the given iterable."""
    return iterable.items() if hasattr(iterable, "items") else iterable


def itervalues(iterable: "SupportsKeysItems"):
    """Yield values of the given iterable."""
    return iterable.values() if hasattr(iterable, "values") else iterable


_KVT = TypeVar("_KVT")


def join(
    iterables: Iterable[dict[_KVT, _T]] | Iterable[Iterable[_T]]
) -> dict[_KVT, _T] | Iterable[_T]:
    """Join several iterables of same type into one.

    This function combines multiple iterables of the same type into a single iterable,
    preserving the iterable type where possible. It handles various iterable types
    including dictionaries, sets, strings, and other iterables.

    Parameters
    ----------
    iterables : Iterable[dict[_KVT, _T]] | Iterable[Iterable[_T]]
        An iterable of iterables to join. All iterables must be of the same type.
        Type of first iterable determines output type.

    Returns
    -------
    dict[_KVT, _T] | Iterable[_T]
        A single iterable containing all elements from input iterables.
        Return type determined by type of first iterable:
        - dict: Updates with subsequent dicts, later values take precedence
        - str/bytes: Concatenates using empty string/bytes join
        - set: Returns union of all sets
        - list/tuple: Concatenates into new list/tuple
        - iterator: Chains together into iterator
        None if iterables is empty

    Examples
    --------
    # Heterogeneous types merged based on first type:
    >>> join([{'a':1}, ['b'], {2}])
    {'a':1, '0':'b', '0':2}  # Everything coerced to dict

    >>> join([[1], {'a':2}, {3}])
    [1, 2, 3]  # Everything flattened to list

    >>> join(['abc', [1,2], {'d'}])
    'abc12d'  # Everything string joined

    Raises
    ------
    TypeError
        If the first iterable type is not supported for joining

    """
    iterables, iterables_copy = tee(iterables)
    it = iter(iterables_copy)
    try:
        dest = next(it)
    except StopIteration:
        return None
    cls = dest.__class__

    if isinstance(dest, bytes | str):
        return "".join(iterables)
    if isinstance(dest, Dict):
        result = dest.copy()
        for d in it:
            result.update(d)
        return result
    if isinstance(dest, set):
        return dest.union(*it)
    if isinstance(dest, Iterator | range):
        return chain.from_iterable(iterables)
    if isinstance(dest, Iterable):
        # NOTE: this could be reduce(concat, ...),
        #       more effective for low count
        return cls(chain.from_iterable(iterables))
    raise TypeError(f"Don't know how to join {cls.__name__}")


@overload
def merge(*iterables: Mapping[_KT, _T]) -> Mapping[_KT, _T]:
    ...


@overload
def merge(*iterables: Iterable[_T]) -> Iterable[_T]:
    ...


def merge(*iterables):
    """Merge several iterables of same type into one.

    Works with dicts, sets, lists, tuples, iterators and strings.
    For dicts later values take precedence.

    Args:
        *iterables: Variable number of iterables to merge. All iterables must be of the same type.
                Supported types are: dict, set, list, tuple, iterator, str

    Returns:
        Merged iterable of the same type as input iterables

    Examples:
        >>> merge({'a': 1}, {'b': 2})  # Merging dictionaries
        {'a': 1, 'b': 2}

        >>> merge({'a': 1}, {'a': 2})  # Dict values from later args take precedence
        {'a': 2}

        >>> merge([1, 2], [3, 4])  # Merging lists
        [1, 2, 3, 4]

        >>> merge({1, 2}, {2, 3})  # Merging sets
        {1, 2, 3}

        >>> merge('hello', 'world')  # Merging strings
        'helloworld'

        >>> merge((1, 2), (3, 4))  # Merging tuples
        (1, 2, 3, 4)

        >>> merge(range(2), range(2, 4))  # Merging iterators
        [0, 1, 2, 3]

    """
    return join(iterables)


def joinwith(
    f: Callable[[Unpack[Tuple[Mapping[_KT, _T], ...]]], U],
    *dicts: Mapping[_KT, _T],
    strict=False,
) -> dict[_KT, U]:
    """Join several dictionaries, combining values with a given function.

    This function merges multiple dictionaries by applying a combining function to values with matching keys.

    Args:
        f (Callable): Function to combine values from different dictionaries. Takes a tuple of values and returns combined result.
        *dicts (Mapping[_KVT, _T]): Variable number of dictionaries to join.
        strict (bool, optional): If False and only one dictionary provided, returns it unchanged. Defaults to False.

    Returns:
        dict[_KVT, U]: New dictionary with combined values.

    Examples:
        >>> # Sum values for matching keys
        >>> d1 = {'a': 1, 'b': 2}
        >>> d2 = {'a': 3, 'c': 4}
        >>> joinwith(sum, d1, d2)
        {'a': 4, 'b': 2, 'c': 4}

        >>> # Join strings for matching keys
        >>> d1 = {'x': 'hello', 'y': 'world'}
        >>> d2 = {'x': ' there', 'z': '!'}
        >>> joinwith(lambda x: ''.join(x), d1, d2)
        {'x': 'hello there', 'y': 'world', 'z': '!'}

        >>> # Create lists of values (using list as combining function)
        >>> d1 = {'key': 1}
        >>> d2 = {'key': 2}
        >>> d3 = {'key': 3}
        >>> joinwith(list, d1, d2, d3)
        {'key': [1, 2, 3]}

    Notes:
        - If no dictionaries are provided, returns an empty dictionary
        - If strict=False and only one dictionary is provided, returns it unchanged
        - Keys present in any input dictionary will be present in output
        - The combining function f must handle variable number of inputs

    """
    dicts = list(dicts)
    if not dicts:
        return {}
    if not strict and len(dicts) == 1:
        return dicts[0]

    lists = {}
    for c in dicts:
        for k, v in iteritems(c):
            if k in lists:
                lists[k].append(v)
            else:
                lists[k] = [v]

    if f is not list:
        # kind of walk_values() inplace
        for k, v in iteritems(lists):
            lists[k] = f(v)

    return lists


def mergewith(f: Callable, dicts: Mapping[_KT, _T]) -> dict[_KT, _T]:
    """Merge several dicts, combining values with given function."""
    return joinwith(f, dicts)


def walk(f: Callable[[U], T], iterable: Iterable[U]) -> Iterable[T]:
    """Walk the iterable transforming its elements with f.

    Same as map, but preserves iterable type.
    """
    return _factory(iterable)(xmap(f, iteritems(iterable)))


def walkkeys(f, iterable):
    """Walk keys of the iterable, mapping them with f."""
    f = makefunc(f)

    def pair_f(pair):
        k, v = pair
        return f(k), v

    return walk(pair_f, iterable)


def walkvals(f, iterable):
    """Walk values of the iterable, mapping them with f."""
    f = makefunc(f)

    # NOTE: we use this awkward construct instead of lambda to be Python 3 compatible
    def pair_f(pair):
        k, v = pair
        return k, f(v)

    return _factory(iterable, mapper=f)(xmap(pair_f, iteritems(iterable)))


def prewalk(f, iterable):
    """Walks the iterable transforming its elements with f.

    Same as map, but preserves iterable type.
    """
    return _factory(iterable)(xmap(f, iterable))


def select(pred, iterable):
    """Same as filter but preserves iterable type."""
    return _factory(iterable)(filter(pred, iteritems(iterable)))


def select_keys(pred, iterable):
    """Select part of the iterable with keys passing pred."""
    pred = make_pred(pred)
    return select(lambda pair: pred(pair[0]), iterable)


def select_values(pred, iterable):
    """Select part of the iterable with values passing pred."""
    pred = make_pred(pred)
    return select(lambda pair: pred(pair[1]), iterable)


def clean(iterable):
    """Remove falsy values from the iterable."""
    if isinstance(iterable, Mapping):
        return select_values(bool, iterable)
    return select(bool, iterable)


# ### Content tests
_all = all
_any = any
xmap = map

# # TODO: a variant of some that returns mapped value,
# #       one can use some(map(f, seq)) or first(keep(f, seq)) for now.

# # TODO: vector comparison tests - ascending, descending and such
# # def chain_test(compare, seq):
# #     return all(compare, zip(seq, rest(seq))


def zipdict(keys, vals):
    """Create a dict with keys mapped to the corresponding vals."""
    return dict(zip(keys, vals, strict=False))


def flip(mapping):
    """Flip passed dict or iterable of pairs swapping its keys and values."""

    def flip_pair(pair):
        k, v = pair
        return v, k

    return walk(flip_pair, mapping)


def _project(
        mapping: "MappingT",
        keys: Iterable[str] | dict[str, Callable[[Any], Any] | None]
) -> MappingT:
    """Leave only given keys in mapping.

    If a dict of Callables is passed, apply them to the values with None indicating identity function.

    Examples
    --------
    >>> project({'a': 1, 'b': 2, 'c': 3}, ['a', 'c'])
    {'a': 1, 'c': 3}

    >>> project({'a': 1, 'b': 2, 'c': 3}, {'a': None, 'c': lambda x: x * 2})
    {'a': 1, 'c': 6}



    """
    res = _factory(mapping)((k, mapping[k]) for k in keys if k in mapping)
    if isinstance(keys, Mapping | dict) and callable(
            first(keys.values(), default=None)):
        for k, f in keys.items():
            if f is not None:
                res[k] = f(res[k])
    return res


@wraps(_project)
def project(mapping: MappingT, keys) -> MappingT:
    return _project(mapping, keys)


def _omit(mapping: Mapping[str, Any],
          keys: Iterable[str]) -> Mapping[str, Any]:
    """Remove given keys from mapping."""
    return _factory(mapping)(
        (k, v) for k, v in iteritems(mapping) if k not in keys)


@wraps(_omit)
def omit(mapping: MappingT, keys: Iterable[str]) -> MappingT:
    return collect(mapping).omit(keys)


class collect(CollectIterator):

    @wraps(where)
    def where(self, **cond):
        return type(self)(where(self, **cond))

    @wraps(pluck)
    def pluck(self, key):
        return type(self)(pluck(key, self.it))

    @wraps(_pluckattr)
    def pluckattr(self, key):
        return type(self)(_pluckattr(key, self.it))

    @wraps(haspath)
    def haspath(self, path):
        return type(self)(haspath(self.it, path))

    @wraps(delin)
    def delin(self, path):
        return type(self)(delin(self.it, path))

    @wraps(getin)
    def getin(self, path, default=None):
        return type(self)(getin(self.it, path, default))

    @wraps(updatein)
    def updatein(self, path, update, default=None):
        return type(self)(updatein(self.it, path, update, default))

    @wraps(setdefault)
    def setdefault(self, key, default=None, delimeter="."):
        return type(self)(setdefault(self.it, key, default, delimeter))

    @wraps(getlax)
    def getlax(self, path, default=None):
        return type(self)(getlax(self.it, path, default))

    @wraps(walk)
    def walk(self, f):
        return type(self)(walk(f, self.it))

    @wraps(walkkeys)
    def walkkeys(self, f):
        return type(self)(walkkeys(f, self.it))

    @wraps(walkvals)
    def walk_values(self, f):
        return type(self)(walkvals(f, self.it))

    @wraps(select)
    def select(self, pred):
        return type(self)(select(pred, self.it))

    @wraps(select_keys)
    def select_keys(self, pred):
        return type(self)(select_keys(pred, self.it))

    @wraps(select_values)
    def select_values(self, pred):
        return type(self)(select_values(pred, self.it))

    @wraps(clean)
    def clean(self):
        return type(self)(clean(self.it))

    @wraps(zipvalues)
    def zipvalues(self, *others):
        return type(self)(zipvalues(self.it, *others))

    @wraps(zipdicts)
    def zipdicts(self, *others):
        return type(self)(zipdicts(self.it, *others))

    @wraps(flip)
    def flip(self):
        return type(self)(flip(self.it))

    @wraps(_project)
    def project(self, keys):
        return type(self)(_project(self._source, keys))

    @wrapafter(_omit)
    def omit(self, keys):
        return type(self)(_omit(self.mapit, keys))

    @wraps(zipdict)
    def zipdict(self, keys):
        return type(self)(zipdict(keys, self.it))

    @wraps(some)
    def some(self, pred):
        return type(self)(some(pred, self.it))

    @wraps(_all)
    def all(self, pred):
        return type(self)(_all(pred, self.it))

    @wraps(_any)
    def any(self, pred):
        return type(self)(_any(pred, self.it))

    @wraps(noneof)
    def noneof(self, pred):
        return type(self)(noneof(pred, self.it))

    @wraps(oneof)
    def oneof(self, pred):
        return type(self)(oneof(pred, self.it))

    @wraps(isdistinct)
    def isdistinct(self, key=EMPTY):
        return type(self)(isdistinct(self.it, key))

    @wraps(_ilen)
    def ilen(self, consume=False):
        return _ilen(self.it, consume)

    @wraps(_spy)
    def spy(self, length=None):
        return type(self)(_spy(self.it, length))

    @wraps(_locate)
    def locate(self, pred, window=None, consume=True):
        return type(self)(_locate(self.it, pred, window, consume))

    @wraps(replace)
    def replace(self,
                pred,
                sub,
                window=1,
                if_notfound: Literal["append", "forbid", "ignore"] = "append"):
        return type(self)(replace(self.it, pred, sub, window, if_notfound))

    @wraps(join)
    def join(self):
        return type(self)(join(self.it))

    @wraps(merge)
    def merge(self):
        return type(self)(merge(self.it))

    @wraps(joinwith)
    def joinwith(self, f, strict=False):
        return type(self)(joinwith(f, self.it, strict))

    @wraps(mergewith)
    def mergewith(self, f):
        return type(self)(mergewith(f, self.it))

    @wraps(flatten)
    def flatten(self):
        return type(self)(flatten(self.it))

    @wraps(take)
    def take(self, n):
        return type(self)(take(n, self.it))

    @wraps(drop)
    def drop(self, n):
        return type(self)(drop(n, self.it))

    @wraps(first)
    def first(self, default=None):
        return type(self)(first(self.it, default))

    @wraps(last)
    def last(self):
        return type(self)(last(self.it))

    @wraps(butlast)
    def butlast(self):
        return type(self)(butlast(self.it))

    @wraps(rest)
    def rest(self):
        return type(self)(rest(self.it))

    @wraps(distinct)
    def distinct(self):
        return type(self)(distinct(self.it))

    @wraps(map)
    def map(self, f):
        return type(self)(_map(f, self.it))

    @wraps(filter)
    def filter(self, pred):
        return type(self)(_filter(pred, self.it))

    @wraps(keep)
    def keep(self, pred) -> Self:
        return type(self)(keep(pred, self.it))

    @wraps(remove)
    def remove(self, pred) -> Self:
        return type(self)(remove(pred, self.it))

    @wraps(mapcat)
    def mapcat(self, f) -> Self:
        return type(self)(mapcat(f, self.it))

    @wraps(collapse)
    def collapse(self, isscalar=Is[str, bytes], maxdepth=None):
        return type(self)(collapse(self, isscalar, levels=maxdepth))


def keyexists(key: str) -> Callable[[str], bool]:
    return lambda e: e is not None and key in e


if __name__ == "__main__":
    import doctest

    doctest.testmod()
