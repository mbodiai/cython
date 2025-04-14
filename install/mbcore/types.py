import asyncio
import collections.abc
import copy
import errno
import importlib
from importlib.util import module_from_spec, spec_from_file_location
import itertools
import operator
import os
import platform
import re
import shutil
import stat
import subprocess
import sys
import tarfile
import tempfile
import urllib.request
from collections import deque
from collections.abc import Awaitable, Container, Hashable, Iterable, Mapping, Set
from contextlib import (
    AbstractContextManager,
    ContextDecorator,
    closing,
    contextmanager,
)
from contextlib import (
    suppress as ctx_suppress, )
from dataclasses import _MISSING_TYPE, MISSING, dataclass
from functools import lru_cache, partial, reduce
from importlib import import_module
from inspect import Parameter, iscoroutinefunction
from io import BufferedReader
from operator import itemgetter, not_
from pathlib import Path
from random import random
from time import sleep, time
from types import (
    CellType,
    CodeType,
    EllipsisType,
    FrameType,
    ModuleType,
    NoneType,
    new_class,
)
from typing import TypeGuard

from typing_extensions import (
    TYPE_CHECKING,
    Annotated,
    Any,
    Callable,
    ClassVar,
    Concatenate,
    Dict,
    Final,
    Generic,
    Iterator,
    Literal,
    ParamSpec,
    Protocol,
    Self,
    Tuple,
    Type,
    TypeAlias,
    TypeVar,
    TypeVarTuple,
    Union,
    cast,
    overload,
)

from mbcore.proto import SupportsKeysAndGetItem, PredicateType

_RangeMapKT = TypeVar("_RangeMapKT")
_RangeMapVT = TypeVar("_RangeMapVT")

if TYPE_CHECKING:
    parent = property
    from typing_extensions import runtime_checkable
    checkable = runtime_checkable
else:

    class parent:
        ...
    from typing_extensions import runtime_checkable as checkable



P = ParamSpec("P")
_P = ParamSpec("_P")
_R_co = TypeVar("_R_co", covariant=True)
V = TypeVar("V")
U = TypeVar("U")
T = TypeVar("T")
R = TypeVar("R")
_S = TypeVar("_S")
_T = TypeVar("_T")
_R = TypeVar("_R")
Ts = TypeVarTuple("Ts")
WRAPPER_ASSIGNMENTS = ("__module__", "__name__", "__qualname__", "__doc__",
                       "__annotations__")
WRAPPER_UPDATES = ("__dict__", "__doc__", "__annotations__")
AnyType = TypeVar("AnyType")
from threading import Lock

lock = Lock()
try:
    from annotated_types import Len as Len
    from annotated_types import MaxLen as MaxLen
    from annotated_types import MinLen as MinLen
    from typing_extensions import TypeIs as TypeIs
except (ImportError, SyntaxError, ModuleNotFoundError, AttributeError,
        NameError, TypeError):
    if not TYPE_CHECKING:
        def runtime_checkable(cls):
            return cls
        def Len(x):
            return object

        def MaxLen(x):
            return object

        def MinLen(x):
            return object

        def Never(x):
            return object

        try:
            from typing_extensions import TypeIs as TypeIs_
        except (ImportError, SyntaxError, ModuleNotFoundError, AttributeError,
                NameError, TypeError):
            try:
                from typing_extensions import TypeIs as TypeIs_
            except (ImportError, SyntaxError, ModuleNotFoundError,
                    AttributeError, NameError, TypeError):
                TYPE_CHECKING = False
                TypeIs_ = type(tuple[int, ...].__origin__)
        TypeIs = TypeIs_


def first_true(iterable: Iterable[T],
               key: Callable[[T], bool],
               default: T | U = None) -> T | U:
    return next((item for item in iterable if key(item)), default)


def get_package_name(module: ModuleType | Path | str | object) -> str:
    if isinstance(module, ModuleType):
        name = module.__name__
    elif isinstance(module, Path):
        name = first_true(module.parents, lambda p:
                          (p / "__init__.py").exists(), module).stem
    elif isinstance(module, str):
        name = module
    else:
        name = str(
            getattr(module, "__qualname__", getattr(module, "__name__", None))
            or getattr(type(module), "__name__", None), )

    if "." in name:
        return name.rsplit(".", 1)[0]
    return name


def get_module_name(module: ModuleType) -> str:
    return module.__name__.split(".")[1]


@dataclass
class ModulePackage:
    """A data class that attempts to handle all your usage patterns:
    - A single file path (like '/some/path/module.py'),
    - A dotted module path (like 'mbodios.types.ndarray.ndarray'),
    - Automatic fallback if the last segment is actually an attribute instead of a submodule.
    """

    name: str
    package_name: str
    module_name: str
    attr_name: str | None
    attr: Any | None
    obj: Any  # The loaded module or the attribute
    module: ModuleType | None
    path: Path | None

    @overload
    def __init__(self, package: str | ModuleType, module: str | ModuleType,
                 attr: Any, path: Path):
        ...

    @overload
    def __init__(self, name: str):
        ...

    @overload
    def __init__(self, path: Path):
        ...

    def __init__(self, *args, **kwargs):
        """A single dynamic __init__ that:
        - If you pass 1 string with os.sep, treat it as a file path.
        - If you pass 1 string with no os.sep, treat it as a dotted import (with possible fallback to attribute).
        - If multiple args, join them with '.' as a dotted import.
        """
        # Initialize dataclass fields with placeholders
        self.name = ""
        self.package_name = ""
        self.module_name = ""
        self.attr_name = None
        self.attr = None
        self.obj = None
        self.module = None
        self.path = None

        # Decide how to parse args
        if len(args) == 1 and isinstance(args[0], (str, Path)):
            raw = str(args[0])
            if os.path.sep in raw:
                # Single file path
                self._init_from_file(raw)
            else:
                # Single dotted path -> attempt import
                self._init_from_dotted(raw)
        else:
            # Possibly multiple segments => dotted
            dotted = ".".join(str(a) for a in args)
            self._init_from_dotted(dotted)

    def _init_from_file(self, file_path: str):
        """Import from a direct file path, like '/path/to/module.py'."""
        p = Path(file_path).resolve()
        if not p.is_file():
            raise FileNotFoundError(f"Cannot find module file: {p}")

        mod_name = p.stem  # e.g., "module" from "module.py"
        spec = spec_from_file_location(mod_name, str(p))
        if not spec or not spec.loader:
            raise ImportError(f"Could not create import spec for {p}")

        mod = module_from_spec(spec)
        sys.modules[mod_name] = mod
        spec.loader.exec_module(mod)  # type: ignore

        # Fill out fields
        self.module = mod
        self.module_name = mod_name
        self.obj = mod
        self.name = mod_name
        self.path = p

        # "package_name" doesn't really apply if it's just a standalone file, so keep it empty
        self.package_name = ""

    def _init_from_dotted(self, dotted: str):
        """Import a dotted path. First, try to import it entirely as a module.
        If that fails, peel off the last segment as a potential attribute.
        """
        # Attempt full import
        try:
            mod = import_module(dotted)
            # If it succeeds, the entire dotted path is a module.
            self.module = mod
            self.obj = mod
            self.name = dotted.split(".")[-1]  # The final part
            self.module_name = self.name
            self.package_name = ".".join(dotted.split(".")[:-1])
            # Attempt to get __file__ if present
            self.path = None
            if hasattr(mod, "__file__"):
                self.path = Path(mod.__file__).resolve()  # type: ignore
            return

        except ImportError:
            pass  # We'll attempt fallback to attribute

        # fallback: treat the last segment as an attribute
        if "." not in dotted:
            # There's no place to split off a final attribute
            raise ImportError(
                f"Cannot import module '{dotted}' and no fallback attribute possible."
            )

        *mod_parts, last_part = dotted.split(".")
        mod_str = ".".join(mod_parts)

        # Try to import everything except the last dotted piece
        try:
            mod = import_module(mod_str)
        except ImportError as e:
            raise ImportError(
                f"Failed to import '{dotted}' as a module, and also cannot import parent '{mod_str}'.",
            ) from e

        # Now see if that last part is an attribute in the parent module
        if not hasattr(mod, last_part):
            raise ImportError(
                f"Module '{mod_str}' imported ok, but has no attribute '{last_part}'."
            )

        # success: final piece is an attribute
        self.module = mod
        self.module_name = mod_str.split(".")[-1] if mod_parts else mod_str
        self.package_name = ".".join(mod_str.split(".")[:-1])
        if hasattr(mod, "__file__"):
            self.path = Path(mod.__file__).resolve()  # type: ignore

        self.attr_name = last_part
        self.attr = getattr(mod, last_part)
        self.obj = self.attr
        self.name = last_part

    def __repr__(self):
        return (
            f"ModulePackage(name={self.name!r}, package_name={self.package_name!r}, "
            f"module_name={self.module_name!r}, attr_name={self.attr_name!r}, "
            f"obj={self.obj!r}, module={self.module!r}, path={self.path!r})")


class TimeLimitedLock:

    def __init__(self, func_or_obj: Callable[..., Any] | Lock, seconds: int):
        self.func_or_obj = func_or_obj
        self.seconds = seconds

    def __enter__(self):
        self.start_time = time()
        self.func_or_obj.acquire()
        return self.func_or_obj

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.func_or_obj.release()
        elapsed = time() - self.start_time
        if elapsed > self.seconds:
            obj_name = getattr(self.func_or_obj, "__name__", "Lock")
            raise TimeoutError(
                f"{obj_name} held for {elapsed:.2f} seconds, exceeding the limit of {self.seconds} seconds",
            )


def timelimit(
    seconds: int
) -> Callable[[Callable[..., Any] | Lock], AbstractContextManager]:
    """Decorator that limits the execution time of a function or creates a time-limited context manager.

    Can be used in two ways:
    1. As a decorator for context manager functions
    2. Called with an object that has acquire/release methods (like Lock)

    Args:
        seconds: Maximum execution time in seconds

    Returns:
        Either a decorator for context managers or a context manager itself

    """

    def decorator(func_or_obj: Callable[..., Any] | Lock) -> TimeLimitedLock:
        if hasattr(func_or_obj, "acquire") and hasattr(func_or_obj, "release"):
            return TimeLimitedLock(func_or_obj, seconds)
        if iscoroutinefunction(func_or_obj):
            res = None

            async def wrapper(*args, **kwargs):
                global res
                res = await func_or_obj(*args, **kwargs)
                return res

            try:
                loop = asyncio.get_running_loop()
            except RuntimeError:
                loop = asyncio.new_event_loop()
                asyncio.set_event_loop(loop)
            result = asyncio.run_coroutine_threadsafe(
                asyncio.wait_for(wrapper(), seconds), loop)
            while not result.done():
                sleep(seconds / 20.0)
            if result.done():
                return result.result()
            if sys.platform != "win32":
                from signal import alarm

                alarm(0)
            raise TimeoutError(
                f"{func_or_obj.__name__} took {seconds} seconds, exceeding the limit of {seconds} seconds",
            )
        return TimeLimitedLock(func_or_obj, seconds)

    return decorator


def imports(
    *modules: str,
    mode: Literal["eager", "lazy"] = "lazy",
    **module_aliases: str,
) -> Callable[[Callable[P, T]], Callable[P, T]]:
    """Decorator that injects imports into the TYPE_CHECKING block and updates the function globals.

    This decorator:
    1. Updates the function's globals with the specified imports
    2. Modifies the TYPE_CHECKING block in the source file to add static imports

    Args:
        *modules: Module paths to import (e.g., "np.ndarray", "module.Class")
        mode: "eager" to import immediately, "lazy" to delay until needed

    Example:
        @imports("np.ndarray", "module.Class")
        def function():
            # np.ndarray and module.Class are available here

    """

    def decorator(func: Callable[P, T]) -> Callable[P, T]:

        def wrapper(*args: P.args, **kwargs: P.kwargs) -> T:
            imported_modules: dict[str, ModulePackage] = {
                **{
                    mp.name: mp
                    for mp in map(ModulePackage, modules)
                },
                **{
                    k: ModulePackage(v)
                    for k, v in module_aliases.items()
                },
            }
            for name, modpkg in imported_modules.items():
                func.__globals__[name] = modpkg.obj

            return func(*args, **kwargs)

        try:
            pass
        except Exception:
            pass
        return wrapper

    return decorator


@checkable
class DataclassInstance(Protocol):
    __dataclass_fields__: "ClassVar[dict[str, Any]]"


if TYPE_CHECKING:
    import numpy as np

    InstanceOf = Annotated[AnyType, ...]
    SkipValidation = Annotated[AnyType, ...]

    @runtime_checkable
    class PydanticUndefinedType(Protocol):
        """A type used as a sentinel for undefined values."""

        _instance: "PydanticUndefinedType | None" = None

        def __new__(cls):
            if cls._instance is None:
                cls._instance = super().__new__(cls)
            return cls._instance

    PydanticUndefined: PydanticUndefinedType = PydanticUndefinedType.__new__(
        PydanticUndefinedType)

    @runtime_checkable
    class NotGivenType(Protocol):
        _instance = None

        def __new__(cls):
            if cls._instance is None:
                cls._instance = super().__new__(cls)
            return cls._instance

        @classmethod
        def __repr__(cls):
            return "..."

        @classmethod
        def __str__(cls):
            return "..."

        def __init__(self):
            pass

    NotGivenType.__name__ = "..."
    NotGiven: NotGivenType = NotGivenType.__new__(NotGivenType)
    NotGiven.__repr__ = lambda: "..."
    NotGiven.__str__ = lambda: "..."
else:
    import dataclasses

    @dataclasses.dataclass
    class InstanceOf:
        '''Generic type for annotating a type that is an instance of a given class.

        Example:
            ```python
            from pydantic import BaseModel, InstanceOf

            class Foo:
                ...

            class Bar(BaseModel):
                foo: InstanceOf[Foo]

            Bar(foo=Foo())
            try:
                Bar(foo=42)
            except ValidationError as e:
                print(e)
                """
                [
                │   {
                │   │   'type': 'is_instance_of',
                │   │   'loc': ('foo',),
                │   │   'msg': 'Input should be an instance of Foo',
                │   │   'input': 42,
                │   │   'ctx': {'class': 'Foo'},
                │   │   'url': 'https://errors.pydantic.dev/0.38.0/v/is_instance_of'
                │   }
                ]
                """
            ```

        '''

        @classmethod
        def __class_getitem__(cls, item: AnyType) -> AnyType:
            return Annotated[item, cls()]

        __hash__ = object.__hash__

    try:
        from pydantic_core import PydanticUndefined, PydanticUndefinedType
    except ImportError:

        @runtime_checkable
        class PydanticUndefinedType(Protocol):
            """A type used as a sentinel for undefined values."""

            def __init__(self) -> None:
                pass

            def __bool__(self) -> bool:
                return False

        PydanticUndefined: PydanticUndefinedType = PydanticUndefinedType()
    try:
        raise ImportError
    except ImportError:

        @checkable
        class NotGivenType(Protocol):
            _instance = None

            def __new__(cls):
                if cls._instance is None:
                    cls._instance = super().__new__(cls)
                return cls._instance

            @classmethod
            def __repr__(cls):
                return "..."

            @classmethod
            def __str__(cls):
                return "..."

            def __init__(self):
                pass

        NotGivenType.__name__ = "..."
        NotGiven = NotGivenType()
        NotGiven.__repr__ = lambda: "..."
        NotGiven.__str__ = lambda: "..."
    import dataclasses

    @dataclasses.dataclass
    class SkipValidation:
        """If this is applied as an annotation (e.g., via `x: Annotated[int, SkipValidation]`), validation will be
            skipped. You can also use `SkipValidation[int]` as a shorthand for `Annotated[int, SkipValidation]`.

        This can be useful if you want to use a type annotation for documentation/IDE/type-checking purposes,
        and know that it is safe to skip validation for one or more of the fields.

        Because this converts the validation schema to `any_schema`, subsequent annotation-applied transformations
        may not have the expected effects. Therefore, when used, this annotation should generally be the final
        annotation applied to a type.
        """

        def __class_getitem__(cls, item: Any) -> Any:
            return Annotated[item, SkipValidation()]

        __hash__ = object.__hash__


class function(Protocol):

    @property
    def __closure__(self) -> tuple[CellType, ...] | None:
        ...

    __code__: CodeType
    __defaults__: tuple[Any, ...] | None
    __dict__: dict[str, Any]

    @property
    def __globals__(self) -> dict[str, Any]:
        ...

    __name__: str
    __qualname__: str
    __annotations__: dict[str, Any]
    __kwdefaults__: dict[str, Any]
    if sys.version_info >= (3, 10):

        @property
        def __builtins__(self) -> dict[str, Any]:
            ...

    if sys.version_info >= (3, 12):
        __type_params__: "tuple[TypeVar | ParamSpec | TypeVarTuple, ...]"
    __module__: str

    def __get__(self, instance: object, owner: type | None = None, /) -> Any:
        ...


def consume(iterator, n=None):
    """Advance *iterable* by *n* steps. If *n* is ``None``, consume it entirely.

    Efficiently exhausts an iterator without returning values. Defaults to
    consuming the whole iterator, but an optional second argument may be
    provided to limit consumption.

        >>> i = (x for x in range(10))
        >>> next(i)
        0
        >>> consume(i, 3)
        >>> next(i)
        4
        >>> consume(i)
        >>> next(i)
        Traceback (most recent call last):
          File "<stdin>", line 1, in <module>
        StopIteration

    If the iterator has fewer items remaining than the provided limit, the
    whole iterator will be consumed.

        >>> i = (x for x in range(3))
        >>> consume(i, 5)
        >>> next(i)
        Traceback (most recent call last):
          File "<stdin>", line 1, in <module>
        StopIteration

    """
    if n is None:
        deque(iterator, maxlen=0)
    else:
        next(itertools.islice(iterator, n, n), None)


@overload
def identity(f: Callable[P, T]) -> Callable[P, T]:
    ...


@overload
def identity(f: T) -> T:
    ...


def identity(f):
    """Return the first argument passed to it."""
    return f


def makefunc(f, test=False):
    """Return a function from a callable or a value."""
    if callable(f):
        return f
    if f is None:
        return bool if test else lambda x: x
    if isinstance(f, int | slice):
        return itemgetter(f)
    if isinstance(f, Mapping):
        return f.__getitem__
    if isinstance(f, Set):
        return f.__contains__
    raise TypeError(f"Can't make a func from {f.__class__.__name__}")


@overload
def compose(f: Callable[[_T], _R], g: Callable[[_S], _T],
            /) -> Callable[[_S], _R]:
    ...


@overload
def compose(*fs: Callable[..., Any]) -> Callable[..., Any]:
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


first = compose(next, iter)
last = compose(next, iter, lambda x: reversed(x))


def update_wrapper(
    wrapper=identity,
    wrapped=Callable[..., Any],
    assigned=WRAPPER_ASSIGNMENTS,
    updated=WRAPPER_UPDATES,
) -> Callable[..., Any]:
    """Update a wrapper function to look like the wrapped function.

    wrapper is the function to be updated
    wrapped is the original function
    assigned is a tuple naming the attributes assigned directly
    from the wrapped function to the wrapper function (defaults to
    WRAPPER_ASSIGNMENTS)
    updated is a tuple naming the attributes of the wrapper that
    are updated with the corresponding attribute from the wrapped
    function (defaults to WRAPPER_UPDATES)
    """
    if TYPE_CHECKING:
        for attr in assigned:
            try:
                value = getattr(wrapped, attr)
            except AttributeError:
                pass
            else:
                setattr(wrapper, attr, value)
        for attr in updated:
            getattr(wrapper, attr).update(getattr(wrapped, attr, {}))
        wrapper.__wrapped__ = wrapped
        return wrapper
    return wrapper


class ModelType(Protocol):

    def model_dump(self, *args, **kwargs) -> Any:
        ...

    def model_dump_json(self, *args, **kwargs) -> Any:
        ...


class dynamic(Generic[_T, _P, _R_co]):
    """A descriptor that can be used as both a classmethod and instance method.

    Usage:
    ```python
    class MyClass:
        @dynamic()
        def my_method(self_or_cls, arg1, arg2):
            if self_or_cls is MyClass:
                print("Called as class method")
            else:
                print("Called as instance method")

        @dynamic
        def my_property(self_or_cls):
            if self_or_cls is MyClass:
                print("Class property")
            else:
                print("Instance property")

    >>> MyClass.my_method(1, 2)
    Called as class method
    >>> MyClass().my_method(1, 2)
    Called as instance method
    >>> MyClass.my_property
    'Class property'
    >>> MyClass().my_property
    'Instance property'
    ```
    """

    setter: Callable[[_T, _R_co], Any]
    getter: Callable[..., Callable[[_T, _R_co], _R_co]]
    __wrapped__: (Callable[Concatenate[_T, _P], _R_co]
                  | Callable[Concatenate[type[_T], _P], _R_co]
                  | Callable[Concatenate[_T | type[_T], _P], _R_co])
    __func__: (Callable[Concatenate[_T, _P], _R_co]
               | Callable[Concatenate[type[_T], _P], _R_co]
               | Callable[Concatenate[_T | type[_T], _P], _R_co])
    __name__: str
    __qualname__: str
    __doc__: str | None
    __module__: str

    def __call__(
        self,
        wrapped: Callable[Concatenate[_T | Type[_T], _P], _R_co]
        | Callable[Concatenate[_T, _P], _R_co]
        | Callable[Concatenate[type[_T], _P], _R_co]
        | None = None,
    ) -> "dynamic[_T, _P, _R_co]":
        """Dynamic member access. Use @dynamic for properties and @dynamic() for methods.

        Note that properties will return the same class-level object for all instances.
        """
        if wrapped is None:
            raise ValueError("Must provide a callable to @dynamic()")
        self.__prop__ = wrapped
        self.__name__ = getattr(wrapped, "__name__", type(wrapped).__name__)
        self.__qualname__ = getattr(wrapped, "__qualname__",
                                    type(wrapped).__name__)
        self.__doc__ = wrapped.__doc__
        self.__module__ = wrapped.__module__
        self.__wrapped__ = wrapped
        self.__func__ = wrapped
        self.__isabstractmethod__ = bool(
            getattr(wrapped, "__isabstractmethod__", False))
        self._property = False
        return self

    @overload
    def __init__(self, f: Callable[Concatenate[type[_T], _P], _R_co]) -> None:
        ...

    @overload
    def __init__(self, f: Callable[Concatenate[_T, _P], _R_co]) -> None:
        ...

    @overload
    def __init__(self, f: None = None) -> None:
        ...

    def __init__(
            self,
            f: Callable[Concatenate[type[_T], _P], _R_co] | None = None
    ) -> None:
        """Dynamic member access. Use @dynamic for methods and @dynamic() for properties."""
        if f is None:
            return
        self.__func__ = f
        self.__name__ = f.__name__
        self.__qualname__ = f.__qualname__
        self.__doc__ = f.__doc__
        self.__module__ = f.__module__
        self.__wrapped__ = f
        self.__isabstractmethod__ = bool(
            getattr(f, "__isabstractmethod__", False))
        self._property = True
        self.setter = lambda self, func: setattr(self, "__set__", func)
        self.getter = lambda self, *args, **kwargs: self.__get__(
            *args, **kwargs)

    @overload
    def __get__(self, instance: _T, owner: type[_T]) -> _R_co:
        ...

    @overload
    def __get__(self, instance: None, owner: type[_T]) -> _R_co:
        ...

    def __get__(self,
                instance: _T | None,
                owner: type[_T] | None = None) -> _R_co:
        if self._property:
            if instance is None:
                return self.__func__.__get__(owner, type(owner))()
            return self.__func__.__get__(instance, owner)()
        if instance is None:
            return self.__func__.__get__(owner, type(owner))
        return self.__func__.__get__(instance, owner)


NotGivenTypes: TypeAlias = EllipsisType | NotGivenType | PydanticUndefinedType | _MISSING_TYPE | Literal[
    "MISSING"]


class classvar(parent):
    """Decorate a method to be a class variable. Instance calls will automatically be routed to the class.

    Usage:
    ```python
    class MyClass:
        @classvar
        def my_var(cls):
            return "Class variable"

    >>> MyClass.my_var
    'Class variable'
    >>> MyClass().my_var
    'Class variable'
    ```
    """

    fget: Callable[[Any], Any]
    fset: Callable[[Any, Any], None]
    fdel: Callable[[Any], None]
    __isabstractmethod__: bool
    if sys.version_info >= (3, 13):
        __name__: str

    def __init__(
        self,
        fget: Callable[[Any], Any] | NotGivenTypes = ...,
        fset: Callable[[Any, Any], None] | NotGivenType = ...,
        fdel: Callable[[Any], None] | NotGivenType = ...,
        doc: str | NotGivenType = ...,
    ) -> None:
        self.fget = fget if callable(fget) else (
            lambda instance: instance.__dict__[self.__name__])
        self.fset = fset if callable(fset) else (
            lambda instance, value: setattr(instance, self.__name__, value))
        self.fdel = fdel if callable(fdel) else (
            lambda instance: delattr(instance, self.__name__))
        self.doc = doc if isinstance(doc, str) else None

    def getter(self, fget: Callable[[Any], Any], /) -> property:
        return property(fget, self.fset, self.fdel, self.doc)

    def setter(self, fset: Callable[[Any, Any], None], /) -> property:
        return property(self.fget, fset, self.fdel, self.doc)

    def deleter(self, fdel: Callable[[Any], None], /) -> property:
        return property(self.fget, self.fset, fdel, self.doc)

    def __get__(self, instance: Any, owner: type | None = None, /) -> Any:
        return self.fget(instance)

    def __set__(self, instance: Any, value: Any, /) -> None:
        self.fset(instance, value)

    def __delete__(self, instance: Any, /) -> None:
        self.fdel(instance)


Q = ParamSpec("Q")
P = ParamSpec("P")
U = TypeVar("U")
T = TypeVar("T")
R = TypeVar("R")
V = TypeVar("V")
_R_co = TypeVar("_R_co", covariant=True)


@overload
def wraps(
    wrapped: Callable[P, T] | None,
    returns: None = None,
    assigned=WRAPPER_ASSIGNMENTS,
    updated=WRAPPER_UPDATES,
) -> Callable[..., Callable[P, T]]:
    ...


@overload
def wraps(
    wrapped: Callable[P, T],
    returns: type[R] = type[Any],
    assigned=WRAPPER_ASSIGNMENTS,
    updated=WRAPPER_UPDATES,
) -> Callable[..., Callable[P, R]]:
    ...


@overload
def wraps(
    wrapped: Callable[P, T],
    returns: type[R],
    assigned=WRAPPER_ASSIGNMENTS,
    updated=WRAPPER_UPDATES,
) -> Callable[..., Callable[P, R]]:
    ...


@overload
def wraps(
    wrapped: Callable[P, T],
    returns: Awaitable[R],
    assigned=WRAPPER_ASSIGNMENTS,
    updated=WRAPPER_UPDATES,
) -> Callable[..., Callable[P, Awaitable[R]]]:
    ...


def wraps(
    wrapped: Callable[P, T] | Any,
    returns: Any | Type[Any] | None = None,
    assigned=WRAPPER_ASSIGNMENTS,
    updated=WRAPPER_UPDATES,
):
    """Decorator factory to apply update_wrapper() to a wrapper function."""
    uw = cast(Callable[..., Callable[..., Any]], update_wrapper)
    return cast(
        function,
        partial(uw, wrapped=wrapped, assigned=assigned, updated=updated))


class wrap:
    """Manages function wrapping while ensuring global symbol propagation."""

    @staticmethod
    def propagate_globals(func: Callable) -> None:
        """Ensures global symbols from the function's namespace are accessible."""
        caller_globals = globals()
        func_globals = func.__globals__
        for key, value in caller_globals.items():
            if key not in func_globals:
                func_globals[key] = value

    @classmethod
    def after(
        cls,
        base_func: Callable[Concatenate[U, P], T],
    ) -> Callable[[Callable[Concatenate[U, P], T]], Callable[P, T]]:
        """Wraps a function after executing a base function while ensuring global propagation."""

        def decorator(func: Callable[Concatenate[U, P], T]) -> Callable[P, T]:
            cls.propagate_globals(func)

            def wrapper(*args, **kwargs):
                cls.propagate_globals(func)
                return func(*args, **kwargs)

            return cast(Callable[P, T], wrapper)

        return decorator

    @classmethod
    def cat(
        cls,
        base_func: Callable[Concatenate[V, P], Any],
    ) -> Callable[[Callable[Concatenate[U, P], T]], Callable[Concatenate[
            V, U, P], T]]:
        """Concatenates function parameters while ensuring global propagation."""

        def decorator(
            func: Callable[Concatenate[U, P], T]
        ) -> Callable[Concatenate[V, U, P], T]:
            cls.propagate_globals(func)
            wrapped_func = update_wrapper(func,
                                          base_func,
                                          assigned=WRAPPER_ASSIGNMENTS,
                                          updated=WRAPPER_UPDATES)
            return cast(Callable[Concatenate[V, U, P], T], wrapped_func)

        return decorator

    @classmethod
    @overload
    def __call__(
            cls, base_func: Callable[P, T],
            returns: Type[R]) -> Callable[[Callable[P, Any]], Callable[P, R]]:
        ...

    @classmethod
    @overload
    def __call__(
        cls,
        base_func: Callable[P, T],
        returns: None = None,
    ) -> Callable[[Callable[P, T]], Callable[P, T]]:
        ...

    @classmethod
    def __call__(
        cls,
        base_func: Callable[P, T],
        returns: type[R] | None = None,
    ) -> Callable[[Callable[P, T]], Callable[P, R]]:
        """A safer functools.wraps alternative that propagates global imports properly."""

        def decorator(func: Callable[P, T]) -> Callable[P, R]:
            cls.propagate_globals(func)
            wrapped_func = update_wrapper(func,
                                          base_func,
                                          assigned=WRAPPER_ASSIGNMENTS,
                                          updated=WRAPPER_UPDATES)
            return cast(Callable[P, R], wrapped_func)

        return decorator


@overload
def wrapcat(
    wrapped: Callable[Concatenate[V, P], Any],
    ret: type[T] | Any = Any,
    assigned=WRAPPER_ASSIGNMENTS,
    updated=WRAPPER_UPDATES,
) -> Callable[[Callable[Concatenate[U, ...], T]], Callable[Concatenate[V, U,
                                                                       P], T]]:
    ...


@overload
def wrapcat(
    wrapped: Callable[Concatenate[V, P], Any],
    ret: type[T] | T = Any,
    assigned=WRAPPER_ASSIGNMENTS,
    updated=WRAPPER_UPDATES,
) -> Callable[[Callable[Concatenate[U, ...], T]], Callable[Concatenate[V, U,
                                                                       P], T]]:
    ...


@overload
def wrapcat(
    wrapped: Callable[Concatenate[V, P], Any],
    ret: type[T] | type[function] | None = None,
    assigned=WRAPPER_ASSIGNMENTS,
    updated=WRAPPER_UPDATES,
) -> Callable[[Callable[Concatenate[U, Q], T]], Callable[Concatenate[V, U, Q],
                                                         T]]:
    ...


@overload
def wrapcat(
    wrapped: Callable[Concatenate[V, P], T],
    ret=None,
    assigned=WRAPPER_ASSIGNMENTS,
    updated=WRAPPER_UPDATES,
) -> Callable[[Callable[Concatenate[U, Q], Any]], Callable[Concatenate[V, U,
                                                                       Q], T]]:
    ...


@overload
def wrapcat(
    wrapped: Callable[Concatenate[V, ...], T],
    ret=None,
    assigned=WRAPPER_ASSIGNMENTS,
    updated=WRAPPER_UPDATES,
) -> Callable[[Callable[Concatenate[U, Q], Any]], Callable[Concatenate[V, U,
                                                                       Q], T]]:
    ...


def wrapcat(
    wrapped: Callable[Concatenate[V, P], T] | Callable[Concatenate[V, P], Any]
    | Callable[Concatenate[V, P], Any],
    ret: type[T] | type[function] | None = None,
    assigned=WRAPPER_ASSIGNMENTS,
    updated=WRAPPER_UPDATES,
) -> Any:
    """Decorate update_wrapper() to a wrapper function.

    Returns a decorator that invokes update_wrapper() with the decorated
    function as the wrapper argument and the arguments to wraps() as the
    remaining arguments. Default arguments are as for update_wrapper().
    This is a convenience function to simplify applying partial() to
    update_wrapper().
    """
    ret = ret
    uw = cast(Callable[..., Callable[..., Any]], update_wrapper)
    return cast(
        function,
        partial(uw, wrapped=wrapped, assigned=assigned, updated=updated))


@overload
def wrapcatafter(
    wrapped: Callable[Concatenate[V, P], T],
    ret: type[R] | type[function] | None = None,
    assigned=WRAPPER_ASSIGNMENTS,
    updated=WRAPPER_UPDATES,
) -> Callable[[Callable[Concatenate[U, Q], Any]], Callable[Concatenate[V, P],
                                                           R]]:
    ...


@overload
def wrapcatafter(
    wrapped: Callable[P, T],
    ret: type[T] | type[function] | Any = Any,
    assigned=WRAPPER_ASSIGNMENTS,
    updated=WRAPPER_UPDATES,
) -> Callable[[Callable[Concatenate[..., Q], Any]], Callable[P, T]]:
    ...


def wrapcatafter(
    wrapped,
    ret: type[T] | type[function] | Any = Any,
    assigned=WRAPPER_ASSIGNMENTS,
    updated=WRAPPER_UPDATES,
) -> Any:
    """Decorate update_wrapper() to a wrapper function.

    Returns a decorator that invokes update_wrapper() with the decorated
    function as the wrapper argument and the arguments to wraps() as the
    remaining arguments. Default arguments are as for update_wrapper().
    This is a convenience function to simplify applying partial() to
    update_wrapper().
    """
    if not TYPE_CHECKING:
        return lambda f: f
    uw = cast(Callable[..., Callable[..., Any]], update_wrapper)
    return cast(
        function,
        partial(uw, wrapped=wrapped, assigned=assigned, updated=updated))


@overload
def wrapafter(
    wrapped: Callable[Concatenate[..., P], Any] | Type[Any],
    returns: Type[T] | Any = Type[Any],
    assigned=WRAPPER_ASSIGNMENTS,
    updated=WRAPPER_UPDATES,
) -> Callable[[Callable[..., Any]], Callable[P, T]]:
    ...


@overload
def wrapafter(
    wrapped: Callable[Concatenate[..., P], Any] | Type[Any],
    returns: None | NoneType = None,
    assigned=WRAPPER_ASSIGNMENTS,
    updated=WRAPPER_UPDATES,
) -> Callable[[Callable[..., Any]], Callable[P, NoneType]]:
    ...


@overload
def wrapafter(
    wrapped: Callable[Concatenate[V | None, P], U],
    returns: Type[T] | Any = Any,
    assigned=WRAPPER_ASSIGNMENTS,
    updated=WRAPPER_UPDATES,
) -> Callable[[Callable[Concatenate[U | None, Q], Any]], Callable[Concatenate[
        U, P], T]]:
    ...


@overload
def wrapafter(
    wrapped: Callable[Concatenate[Type[V], P], U],
    returns: T = Type[Any],
    assigned=WRAPPER_ASSIGNMENTS,
    updated=WRAPPER_UPDATES,
) -> Callable[[Callable[Concatenate[U | None, Q], Any]], Callable[Concatenate[
        U, P], T]]:
    ...


def wrapafter(
    wrapped: Callable[Concatenate[V | None, P], U]
    | Callable[Concatenate[Type[V], P], U] | Any,
    returns=None,
    assigned=WRAPPER_ASSIGNMENTS,
    updated=WRAPPER_UPDATES,
) -> Any:
    """Decorate update_wrapper() to a wrapper function.

    Returns a decorator that invokes update_wrapper() with the decorated
    function as the wrapper argument and the arguments to wraps() as the
    remaining arguments. Default arguments are as for update_wrapper().
    This is a convenience function to simplify applying partial() to
    update_wrapper().
    """
    returns = returns or [Any]
    uw = cast(Callable[..., Callable[..., Any]], update_wrapper)
    if TYPE_CHECKING:
        return cast(
            function,
            partial(uw, wrapped=wrapped, assigned=assigned, updated=updated))
    return lambda f: f


class _PeekableReader:
    """lightweight stream wrapper that implements peek()."""

    def __init__(self, stream):
        self.stream = stream

    def read(self, n):
        return self.stream.read(n)

    def readline(self):
        return self.stream.readline()

    def tell(self):
        return self.stream.tell()

    def close(self):
        return self.stream.close()

    def peek(self, n):
        stream = self.stream
        try:
            if hasattr(stream, "flush"):
                stream.flush()
            position = stream.tell()
            stream.seek(position)
            chunk = stream.read(n)
            stream.seek(position)
            return chunk
        except (AttributeError, OSError):
            raise NotImplementedError("stream is not peekable: %r",
                                      stream) from None


def once(func):
    """Decorate func so it's only ever called the first time.

    This decorator can ensure that an expensive or non-idempotent function
    will not be expensive on subsequent calls and is idempotent.

    >>> add_three = once(lambda a: a+3)
    >>> add_three(3)
    6
    >>> add_three(9)
    6
    >>> add_three('12')
    6

    To reset the stored value, simply clear the property ``saved_result``.

    >>> del add_three.saved_result
    >>> add_three(9)
    12
    >>> add_three(8)
    12

    Or invoke 'reset()' on it.

    >>> add_three.reset()
    >>> add_three(-3)
    0
    >>> add_three(0)
    0
    """

    @wraps(func)
    def wrapper(*args, **kwargs):
        if not hasattr(wrapper, "saved_result"):
            wrapper.saved_result = func(*args, **kwargs)
        return wrapper.saved_result

    wrapper.reset = lambda: vars(wrapper).__delitem__("saved_result")
    return wrapper


def _make_peekable(stream):
    """Return stream as an object with a peek() method."""
    if hasattr(stream, "peek"):
        return stream
    if not (hasattr(stream, "tell") and hasattr(stream, "seek")):
        with closing(stream):
            return BufferedReader(stream)
    return _PeekableReader(stream)


def instanceproperty(fget=None, fset=None, fdel=None, doc=None, classval=None):
    """Like @property, but returns ``classval`` when used as a class attribute.

    >>> class MyClass(object):
    ...     '''The class docstring'''
    ...
    ...     @instanceproperty(classval=__doc__)
    ...     def __doc__(self):
    ...         return "An object docstring"
    ...
    ...     @instanceproperty
    ...     def val(self):
    ...         return 42
    >>> MyClass.__doc__
    'The class docstring'
    >>> MyClass.val is None
    True
    >>> obj = MyClass()
    >>> obj.__doc__
    'An object docstring'
    >>> obj.val
    42
    """
    if fget is None:
        return partial(instanceproperty,
                       fset=fset,
                       fdel=fdel,
                       doc=doc,
                       classval=classval)
    return InstanceProperty(fget=fget,
                            fset=fset,
                            fdel=fdel,
                            doc=doc,
                            classval=classval)


class InstanceProperty(property):
    """Like @property, but returns ``classval`` when used as a class attribute.

    Should not be used directly.  Use ``instanceproperty`` instead.
    """

    def __init__(self,
                 fget=None,
                 fset=None,
                 fdel=None,
                 doc=None,
                 classval=None):
        self.classval = classval
        property.__init__(self, fget=fget, fset=fset, fdel=fdel, doc=doc)

    def __get__(self, obj, type=None):
        if obj is None:
            return self.classval
        return property.__get__(self, obj, type)

    def __reduce__(self):
        state = (self.fget, self.fset, self.fdel, self.__doc__, self.classval)
        return (InstanceProperty, state)


@contextmanager
def pushd(dir: str | os.PathLike) -> Iterator[str | os.PathLike]:
    """Context manager to change the current working directory.

    Example:
        >>> from tempfile import TemporaryDirectory
        >>> import os
        >>> orig = os.getcwd()
        >>> with TemporaryDirectory() as tmp_path:
        ...     with pushd(tmp_path):
        ...         assert os.getcwd() == os.fspath(tmp_path)
        ...     assert os.getcwd() != os.fspath(tmp_path)
        >>> assert os.getcwd() == os.fspath(orig)

    """
    orig = Path.cwd()
    os.chdir(dir)
    try:
        yield dir
    finally:
        os.chdir(orig)


@contextmanager
def tarball(
    url,
    target_dir: str | os.PathLike | None = None
) -> Iterator[str | os.PathLike]:
    """Get a URL (or file path URI) to a tarball, download, extract, yield, then clean up.

    Assumes everything in the tarball is prefixed with a common
    directory. That common path is stripped and the contents
    are extracted to ``target_dir``, similar to passing
    ``-C {target} --strip-components 1`` to the ``tar`` command.

    Uses the streaming protocol to extract the contents from a
    stream in a single pass without loading the whole file into
    memory.

    >>> import tempfile
    >>> import pathlib
    >>> import tarfile
    >>> import os # Ensure os is imported for path manipulation if needed by tarfile internals
    >>> with tempfile.TemporaryDirectory() as tmpdir:
    ...     # Create a dummy tarball locally
    ...     tmp_path = pathlib.Path(tmpdir)
    ...     dummy_tar_path = tmp_path / "test.tar.gz"
    ...     dummy_content_path = tmp_path / "test-pkg" / "dummy.txt"
    ...     dummy_content_path.parent.mkdir()
    ...     dummy_content_path.write_text("hello world")
    ...     with tarfile.open(dummy_tar_path, "w:gz") as tar:
    ...         # Add file with a leading directory component
    ...         tar.add(dummy_content_path, arcname="test-pkg/dummy.txt")
    ...
    ...     # Test with explicit target_dir
    ...     target_extract_dir = tmp_path / "out"
    ...     local_url = dummy_tar_path.as_uri() # Use file URI
    ...     tb_ctx = tarball(local_url, target_dir=target_extract_dir)
    ...     with tb_ctx as extracted:
    ...         # Check for the dummy file within the extracted contents (should be directly in 'extracted')
    ...         assert pathlib.Path(extracted, "dummy.txt").is_file()
    ...         assert (pathlib.Path(extracted, "dummy.txt").read_text() == "hello world")
    ...     # The target_extract_dir should be removed by the tarball context
    ...     assert not target_extract_dir.exists()
    ...
    ...     # Recreate tarball for the next test case
    ...     with tarfile.open(dummy_tar_path, "w:gz") as tar:
    ...         tar.add(dummy_content_path, arcname="test-pkg/dummy.txt")
    ...
    ...     # Test without explicit target_dir (should extract to dir named 'test' relative to cwd)
    ...     # Ensure pushd is available
    ...     try: pushd
    ...     except NameError: from contextlib import nullcontext; pushd = nullcontext
    ...     with pushd(tmpdir): # Change CWD to tmpdir for relative path testing
    ...         with tarball(local_url) as extracted_dir:
    ...             # tarball should create 'test' dir (from test.tar.gz) and extract into it
    ...             # The yielded path `extracted_dir` is the one created ('test')
    ...             expected_content_file = pathlib.Path(extracted_dir) / "dummy.txt"
    ...             assert expected_content_file.is_file()
    ...             assert expected_content_file.read_text() == "hello world"
    ...         # The 'test' directory should be removed by cleanup
    ...         assert not pathlib.Path("test").exists()

    """
    from urllib.parse import urlparse

    target_path: Path | None = None
    is_local_uri = False
    parsed_url = urlparse(url)
    if parsed_url.scheme == "file":
        is_local_uri = True
        local_file_path = Path(urllib.request.url2pathname(parsed_url.path))
        if not local_file_path.exists():
            raise FileNotFoundError(
                f"Local tarball not found: {local_file_path}")
        if target_dir is None:
            base_name = local_file_path.name
            for ext in [".tar.gz", ".tgz", ".tar.bz2", ".tar.xz", ".tar"]:
                if base_name.endswith(ext):
                    base_name = base_name[:-len(ext)]
                    break
            target_path = Path(base_name)
        else:
            target_path = Path(target_dir)
    elif target_dir is None:
        base_name = Path(parsed_url.path).name
        for ext in [".tar.gz", ".tgz", ".tar.bz2", ".tar.xz", ".tar"]:
            if base_name.endswith(ext):
                base_name = base_name[:-len(ext)]
                break
        target_path = Path(base_name)
    else:
        target_path = Path(target_dir)
    target_path.mkdir(parents=True, exist_ok=True)
    created_path = target_path
    try:
        if is_local_uri:
            stream = open(local_file_path, "rb")
        else:
            stream = urllib.request.urlopen(url)
        with closing(stream) as stream_context:
            peekable_stream = _make_peekable(stream_context)
            with tarfile.open(fileobj=peekable_stream, mode="r|*") as tf:
                tf.extractall(path=created_path, filter=strip_first_component)
        yield created_path
    finally:
        if created_path and created_path.exists():
            shutil.rmtree(created_path)


def strip_first_component(member: tarfile.TarInfo) -> tarfile.TarInfo | None:
    _, member.name = member.name.split("/", 1)
    return member


def _compose(*cmgrs):
    """Compose any number of dependent context managers into a single one.

    The last, innermost context manager may take arbitrary arguments, but
    each successive context manager should accept the result from the
    previous as a single parameter.
    Like compose
    left, so the context manager should be indicated from outermost to
    innermost.

    Example, to create a context manager to change to a temporary
    directory:

    >>> temp_dir_as_cwd = _compose(pushd, temp_dir)
    >>> with temp_dir_as_cwd() as dir:
    ...     assert os.path.samefile(os.getcwd(), dir)
    """

    def compose_two(inner, outer):

        def composed(*args, **kwargs):
            with inner(*args, **kwargs) as saved, outer(saved) as res:
                yield res

        return contextmanager(composed)

    return reduce(compose_two, reversed(cmgrs))


tarball_cwd = _compose(pushd, tarball)
"\nA tarball context with the current working directory pointing to the contents.\n"


def remove_readonly(func, path, exc_info):
    """Add support for removing read-only files on Windows."""
    _, exc, _ = exc_info
    if func in (os.rmdir, os.remove, os.unlink) and exc.errno == errno.EACCES:
        os.chmod(path, stat.S_IRWXU | stat.S_IRWXG | stat.S_IRWXO)
        func(path)
    else:
        raise


def robust_remover() -> Callable[[str | os.PathLike], None]:
    return partial(shutil.rmtree, onerror=remove_readonly) if platform.system(
    ) == "Windows" else shutil.rmtree


@contextmanager
def temp_dir(remover=shutil.rmtree):
    """Create a temporary directory context. Pass a custom remover
    to override the removal behavior.

    >>> import pathlib
    >>> with temp_dir() as the_dir:
    ...     assert os.path.isdir(the_dir)
    >>> assert not os.path.exists(the_dir)
    """
    temp_dir = tempfile.mkdtemp()
    try:
        yield temp_dir
    finally:
        remover(temp_dir)


robust_temp_dir = partial(temp_dir, remover=robust_remover())


@contextmanager
def repo_context(repo: str,
                 branch: str | None = None,
                 quiet: bool = True,
                 dest_ctx=robust_temp_dir):
    """Check out the repo indicated by url.

    If dest_ctx is supplied, it should be a context manager
    to yield the target directory for the check out.

    >>> repo = repo_context("https://github.com/mbodiai/mbcore")
    >>> with repo as dest:
    ...     listing = os.listdir(dest)
    >>> "README.rst" in listing
    True
    """
    exe = "git"
    if repo.startswith("git+"):
        exe = "git"
        repo = repo[4:]
    if not repo.startswith("https://"):
        repo = f"https://github.com/{repo}".encode().decode("ascii")
    with dest_ctx() as repo_dir:
        cmd = [exe, "clone", repo, repo_dir]
        cmd.extend(["--branch", branch] * bool(branch))
        stream = subprocess.DEVNULL if quiet else None
        subprocess.check_call(cmd, stdout=stream, stderr=stream)
        yield repo_dir


METHOD_CACHE_INIT = lru_cache(maxsize=None)


def cache_clear(x) -> None:
    return METHOD_CACHE_INIT(lambda: None).cache_clear.__get__(x, type(x))()


def method_cache(method, cache_wrapper=METHOD_CACHE_INIT):
    """Wrap lru_cache to support storing the cache data in the object instances.

    Abstracts the common paradigm where the method explicitly saves an
    underscore-prefixed protected property on first call and returns that
    subsequently.

    >>> class MyClass:
    ...     calls = 0
    ...
    ...     @method_cache
    ...     def method(self, value):
    ...         self.calls += 1
    ...         return value

    >>> a = MyClass()
    >>> a.method(3)
    3
    >>> for x in range(75):
    ...     res = a.method(x)
    >>> a.calls
    75

    Note that the apparent behavior will be exactly like that of lru_cache
    except that the cache is stored on each instance, so values in one
    instance will not flush values from another, and when an instance is
    deleted, so are the cached values for that instance.

    >>> b = MyClass()
    >>> for x in range(35):
    ...     res = b.method(x)
    >>> b.calls
    35
    >>> a.method(0)
    0
    >>> a.calls
    75

    Note that if method had been decorated with ``lru_cache()``,
    a.calls would have been 76 (due to the cached value of 0 having been
    flushed by the 'b' instance).

    Clear the cache with ``.cache_clear()``

    >>> a.method.cache_clear()

    Same for a method that hasn't yet been called.

    >>> c = MyClass()
    >>> c.method.cache_clear()

    Another cache wrapper may be supplied:

    >>> cache = lru_cache(maxsize=2)
    >>> MyClass.method2 = method_cache(lambda self: 3, cache_wrapper=cache)
    >>> a = MyClass()
    >>> a.method2()
    3

    Caution - do not subsequently wrap the method with another decorator, such
    as ``@property``, which changes the semantics of the function.

    See Also:
    http://code.activestate.com/recipes/577452-a-memoize-decorator-for-instance-methods/
    for another implementation and additional justification.

    """

    class Wrapper:

        def __init__(self):
            self.cache_clear = cache_clear

        def __call__(self, *args, **kwargs):
            import types

            bound_method = types.MethodType(method, self)
            cached_method = cache_wrapper(bound_method)
            setattr(self, method.__name__, cached_method)
            return cached_method(*args, **kwargs)

    wrapper = Wrapper()
    return _special_method_cache(method, cache_wrapper) or wrapper


def _special_method_cache(method, cache_wrapper):
    """Because Python treats special methods differently, it's not
    possible to use instance attributes to implement the cached
    methods.

    Instead, install the wrapper method under a different name
    and return a simple proxy to that wrapper.

    https://github.com/jaraco/jaraco.functools/issues/5
    """
    name = method.__name__
    special_names = ("__getattr__", "__getitem__")
    if name not in special_names:
        return None
    wrapper_name = "__cached" + name

    def proxy(self, /, *args, **kwargs):
        from types import MethodType

        if wrapper_name not in vars(self):
            bound = MethodType(method, self)
            cache = cache_wrapper(bound)
            setattr(self, wrapper_name, cache)
        else:
            cache = getattr(self, wrapper_name)
        return cache(*args, **kwargs)

    return proxy


class Throttler:
    """Rate-limit a function (or other callable)."""

    def __init__(self, func, max_rate=float("Inf")):
        if isinstance(func, Throttler):
            func = func.func
        self.func = func
        self.max_rate = max_rate
        self.reset()

    def reset(self):
        self.last_called = 0

    def __call__(self, *args, **kwargs):
        self._wait()
        return self.func(*args, **kwargs)

    def _wait(self):
        """Ensure at least 1/max_rate seconds from last call."""
        elapsed = time() - self.last_called
        must_wait = 1 / self.max_rate - elapsed
        sleep(max(0, must_wait))
        self.last_called = time()

    def __get__(self, obj, owner=None):
        return first_invoke(self._wait, partial(self.func, obj))


def first_invoke(func1, func2):
    """Return a function that when invoked will invoke func1 without
    any parameters (for its side effect) and then invoke func2
    with whatever parameters were passed, returning its result.
    """

    def wrapper(*args, **kwargs):
        func1()
        return func2(*args, **kwargs)

    return wrapper


def throttle(max_seconds: float):
    """Rate-limit a function (or other callable)."""

    def decorator(func):
        return Throttler(func, max_seconds)

    return decorator


def apply(transform):
    """Decorate a function with a transform function that is
    invoked on results returned from the decorated function.

    >>> @apply(reversed)
    ... def get_numbers(start):
    ...     "doc for get_numbers"
    ...     return range(start, start + 3)
    >>> list(get_numbers(4))
    [6, 5, 4]
    >>> get_numbers.__doc__
    'doc for get_numbers'
    """

    def wrap(func):
        return wraps(func)(compose(transform, func))

    return wrap


def result_invoke(action):
    """Decorate a function with an action function that is
    invoked on the results returned from the decorated
    function (for its side effect), then return the original
    result.

    >>> @result_invoke(print)
    ... def add_two(a, b):
    ...     return a + b
    >>> x = add_two(2, 3)
    5
    >>> x
    5
    """

    def wrap(func):

        @wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            action(result)
            return result

        return wrapper

    return wrap


def invoke(f, /, *args, **kwargs):
    """Call a function for its side effect after initialization.

    The benefit of using the decorator instead of simply invoking a function
    after defining it is that it makes explicit the author's intent for the
    function to be called immediately. Whereas if one simply calls the
    function immediately, it's less obvious if that was intentional or
    incidental. It also avoids repeating the name - the two actions, defining
    the function and calling it immediately are modeled separately, but linked
    by the decorator construct.

    The benefit of having a function construct (opposed to just invoking some
    behavior inline) is to serve as a scope in which the behavior occurs. It
    avoids polluting the global namespace with local variables, provides an
    anchor on which to attach documentation (docstring), keeps the behavior
    logically separated (instead of conceptually separated or not separated at
    all), and provides potential to re-use the behavior for testing or other
    purposes.

    This function is named as a pithy way to communicate, "call this function
    primarily for its side effect", or "while defining this function, also
    take it aside and call it". It exists because there's no Python construct
    for "define and call" (nor should there be, as decorators serve this need
    just fine). The behavior happens immediately and synchronously.

    >>> @invoke
    ... def func():
    ...     print("called")
    called
    >>> func()
    called

    Use partial to pass parameters to the initial call

    >>> @partial(invoke, name="bingo")
    ... def func(name):
    ...     print("called with", name)
    called with bingo
    """
    f(*args, **kwargs)
    return f


_T = TypeVar("_T")
_VT = TypeVar("_VT")
_Matchable = Union[Callable, Container, Iterable, re.Pattern]


def _dispatch(obj: _Matchable) -> Callable:
    if isinstance(obj, re.Pattern):
        return obj.fullmatch
    if not isinstance(obj, Callable):
        if not isinstance(obj, Container):
            obj = set(obj)
        obj = obj.__contains__
    return obj


class Projection(collections.abc.Mapping):
    """Project a set of keys over a mapping.

    >>> sample = {'a': 1, 'b': 2, 'c': 3}
    >>> prj = Projection(['a', 'c', 'd'], sample)
    >>> dict(prj)
    {'a': 1, 'c': 3}

    Projection also accepts an iterable or callable or pattern.

    >>> iter_prj = Projection(iter('acd'), sample)
    >>> call_prj = Projection(lambda k: ord(k) in (97, 99, 100), sample)
    >>> pat_prj = Projection(re.compile(r'[acd]'), sample)
    >>> prj == iter_prj == call_prj == pat_prj
    True

    Keys should only appear if they were specified and exist in the space.
    Order is retained.

    >>> list(prj)
    ['a', 'c']

    Attempting to access a key not in the projection
    results in a KeyError.

    >>> prj['b']
    Traceback (most recent call last):
    ...
    KeyError: 'b'

    Use the projection to update another dict.

    >>> target = {'a': 2, 'b': 2}
    >>> target.update(prj)
    >>> target
    {'a': 1, 'b': 2, 'c': 3}

    Projection keeps a reference to the original dict, so
    modifying the original dict may modify the Projection.

    >>> del sample['a']
    >>> dict(prj)
    {'c': 3}
    """

    def __init__(self, keys: _Matchable, space: Mapping):
        self._match = _dispatch(keys)
        self._space = space

    def __getitem__(self, key):
        if not self._match(key):
            raise KeyError(key)
        return self._space[key]

    def _keys_resolved(self):
        return filter(self._match, self._space)

    def __iter__(self):
        return self._keys_resolved()

    def __len__(self):
        return len(tuple(self._keys_resolved()))


class Mask(Projection):
    """The inverse of a :class:`Projection`, masking out keys.

    >>> sample = {'a': 1, 'b': 2, 'c': 3}
    >>> msk = Mask(['a', 'c', 'd'], sample)
    >>> dict(msk)
    {'b': 2}
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._match = lambda key, orig=self._match: not orig(key)


def mapvalues(function, dictionary):
    """Return a new dict with function applied to values of dictionary.

    >>> mapvalues(lambda x: x+1, dict(a=1, b=2))
    {'a': 2, 'b': 3}
    """
    return {key: function(value) for key, value in dictionary.items()}


class MapInputsToRanges(Dict[_RangeMapKT, _VT]):
    """A dictionary-like object that uses the keys as bounds for a range.
    Inclusion of the value for that range is determined by the
    key_match_comparator, which defaults to less-than-or-equal.
    A value is returned for a key if it is the first key that matches in
    the sorted list of keys.

    One may supply keyword parameters to be passed to the sort function used
    to sort keys (i.e. key, reverse) as sort_params.

    Create a map that maps 1-3 -> 'a', 4-6 -> 'b'

    >>> r = RangeMap({3: 'a', 6: 'b'})  # boy, that was easy
    >>> r[1], r[2], r[3], r[4], r[5], r[6]
    ('a', 'a', 'a', 'b', 'b', 'b')

    Even float values should work so long as the comparison operator
    supports it.

    >>> r[4.5]
    'b'

    Notice that the way rangemap is defined, it must be open-ended
    on one side.

    >>> r[0]
    'a'
    >>> r[-1]
    'a'

    One can close the open-end of the RangeMap by using undefined_value

    >>> r = RangeMap({0: RangeMap.undefined_value, 3: 'a', 6: 'b'})
    >>> r[0]
    Traceback (most recent call last):
    ...
    KeyError: 0

    One can get the first or last elements in the range by using RangeMap.Item

    >>> last_item = RangeMap.Item(-1)
    >>> r[last_item]
    'b'

    .last_item is a shortcut for Item(-1)

    >>> r[RangeMap.last_item]
    'b'

    Sometimes it's useful to find the bounds for a RangeMap

    >>> r.bounds()
    (0, 6)

    RangeMap supports .get(key, default)

    >>> r.get(0, 'not found')
    'not found'

    >>> r.get(7, 'not found')
    'not found'

    One often wishes to define the ranges by their left-most values,
    which requires use of sort params and a key_match_comparator.

    >>> r = RangeMap({1: 'a', 4: 'b'},
    ...     sort_params=dict(reverse=True),
    ...     key_match_comparator=operator.ge)
    >>> r[1], r[2], r[3], r[4], r[5], r[6]
    ('a', 'a', 'a', 'b', 'b', 'b')

    That wasn't nearly as easy as before, so an alternate constructor
    is provided:

    >>> r = RangeMap.left({1: 'a', 4: 'b', 7: RangeMap.undefined_value})
    >>> r[1], r[2], r[3], r[4], r[5], r[6]
    ('a', 'a', 'a', 'b', 'b', 'b')

    """

    def __init__(
        self,
        source: SupportsKeysAndGetItem[_RangeMapKT, _VT]
        | Iterable[tuple[_RangeMapKT, _VT]],
        sort_params: Mapping[str, Any] = {},
        discriminator: Callable[[Any], Hashable] | None = None,
    ):
        dict.__init__(self, source)
        self.sort_params = sort_params
        self.match = discriminator

    def __getitem__(self, item: _RangeMapKT) -> _VT:
        sorted_keys = sorted(self.keys(), **self.sort_params)
        if isinstance(item, MapInputsToRanges.Item):
            result = self.__getitem__(sorted_keys[item])
        else:
            key = self._find_first_match_(sorted_keys, item)
            result = dict.__getitem__(self, key)
            if result is MapInputsToRanges.undefined_value:
                raise KeyError(key)
        return result

    @classmethod
    def LessThan(
        cls, source: SupportsKeysAndGetItem[_RangeMapKT, _VT]
        | Iterable[tuple[_RangeMapKT, _VT]]
    ) -> Self:
        return cls(source,
                   sort_params={"reverse": True},
                   key_match_comparator=operator.lt)

    @classmethod
    def LessThanOrEqualTo(
        cls,
        source: SupportsKeysAndGetItem[_RangeMapKT, _VT]
        | Iterable[tuple[_RangeMapKT, _VT]],
    ) -> Self:
        return cls(source,
                   sort_params={"reverse": True},
                   key_match_comparator=operator.le)

    @classmethod
    def GreaterThan(
        cls, source: SupportsKeysAndGetItem[_RangeMapKT, _VT]
        | Iterable[tuple[_RangeMapKT, _VT]]
    ) -> Self:
        return cls(source,
                   sort_params={"reverse": True},
                   key_match_comparator=operator.gt)

    @classmethod
    def GreaterThanOrEqualTo(
        cls,
        source: SupportsKeysAndGetItem[_RangeMapKT, _VT]
        | Iterable[tuple[_RangeMapKT, _VT]],
    ) -> Self:
        return cls(source,
                   sort_params={"reverse": True},
                   key_match_comparator=operator.ge)

    @classmethod
    def By(
        cls,
        source: SupportsKeysAndGetItem[_RangeMapKT, _VT]
        | Iterable[tuple[_RangeMapKT, _VT]],
        discriminator: Callable[[Any], Hashable],
    ) -> Self:
        return cls(source, discriminator=discriminator)

    @overload
    def get(self, key: _RangeMapKT, default: _T) -> _VT | _T:
        ...

    @overload
    def get(self, key: _RangeMapKT, default: None = None) -> _VT | None:
        ...

    def get(self,
            key: _RangeMapKT,
            default: _T | None = None) -> _VT | _T | None:
        """Return the value for key if key is in the dictionary, else default.
        If default is not given, it defaults to None, so that this method
        never raises a KeyError.
        """
        try:
            return self[key]
        except KeyError:
            return default

    def _find_first_match_(self, keys: Iterable[_RangeMapKT],
                           item: _RangeMapKT) -> _RangeMapKT:
        is_match = partial(self.match, item) if self.match else operator.le
        matches = filter(is_match, keys)
        try:
            return next(matches)
        except StopIteration:
            raise KeyError(item) from None

    def bounds(self) -> tuple[_RangeMapKT, _RangeMapKT]:
        sorted_keys = sorted(self.keys(), **self.sort_params)
        return (sorted_keys[MapInputsToRanges.first_item],
                sorted_keys[MapInputsToRanges.last_item])

    undefined_value = type("RangeValueUndefined", (), {})()

    class Item(int):
        """RangeMap Item."""

    first_item = Item(0)
    last_item = Item(-1)


def __identity(x):
    return x


def sorted_items(d, key=__identity, reverse=False):
    """Return the items of the dictionary sorted by the keys.

    >>> sample = dict(foo=20, bar=42, baz=10)
    >>> tuple(sorted_items(sample))
    (('bar', 42), ('baz', 10), ('foo', 20))

    >>> reverse_string = lambda s: ''.join(reversed(s))
    >>> tuple(sorted_items(sample, key=reverse_string))
    (('foo', 20), ('bar', 42), ('baz', 10))

    >>> tuple(sorted_items(sample, reverse=True))
    (('foo', 20), ('baz', 10), ('bar', 42))
    """

    def pairkey_key(item):
        return key(item[0])

    return sorted(d.items(), key=pairkey_key, reverse=reverse)


class KeyTransformingDict(dict):
    """A dict subclass that transforms the keys before they're used.
    Subclasses may override the default transform_key to customize behavior.
    """

    @staticmethod
    def transform_key(key):
        return key

    def __init__(self, *args, **kargs):
        super().__init__()
        d = dict(*args, **kargs)
        for item in d.items():
            self.__setitem__(*item)

    def __setitem__(self, key, val):
        key = self.transform_key(key)
        super().__setitem__(key, val)

    def __getitem__(self, key):
        key = self.transform_key(key)
        return super().__getitem__(key)

    def __contains__(self, key):
        key = self.transform_key(key)
        return super().__contains__(key)

    def __delitem__(self, key):
        key = self.transform_key(key)
        return super().__delitem__(key)

    def get(self, key, *args, **kwargs):
        key = self.transform_key(key)
        return super().get(key, *args, **kwargs)

    def setdefault(self, key, *args, **kwargs):
        key = self.transform_key(key)
        return super().setdefault(key, *args, **kwargs)

    def pop(self, key, *args, **kwargs):
        key = self.transform_key(key)
        return super().pop(key, *args, **kwargs)

    def matching_key_for(self, key):
        """Given a key, return the actual key stored in self that matches.
        Raise KeyError if the key isn't found.
        """
        try:
            return next(e_key for e_key in self.keys() if e_key == key)
        except StopIteration as err:
            raise KeyError(key) from err


class DictAdapter:
    """Provide a getitem interface for attributes of an object.

    Let's say you want to get at the string.lowercase property in a formatted
    string. It's easy with DictAdapter.

    >>> import string
    >>> print("lowercase is %(ascii_lowercase)s" % DictAdapter(string))
    lowercase is abcdefghijklmnopqrstuvwxyz
    """

    def __init__(self, wrapped_ob):
        self.object = wrapped_ob

    def __getitem__(self, name):
        return getattr(self.object, name)


class NamespaceAdapter:
    """Mix-in class to enable a mapping object to provide items as
    attributes.

    >>> C = type('C', (dict, ItemsAsAttributes), dict())
    >>> i = C()
    >>> i['foo'] = 'bar'
    >>> i.foo
    'bar'

    Natural attribute access takes precedence

    >>> i.foo = 'henry'
    >>> i.foo
    'henry'

    But as you might expect, the mapping functionality is preserved.

    >>> i['foo']
    'bar'

    A normal attribute error should be raised if an attribute is
    requested that doesn't exist.

    >>> i.missing
    Traceback (most recent call last):
    ...
    AttributeError: 'C' object has no attribute 'missing'

    It also works on dicts that customize __getitem__

    >>> missing_func = lambda self, key: 'missing item'
    >>> C = type(
    ...     'C',
    ...     (dict, ItemsAsAttributes),
    ...     dict(__missing__ = missing_func),
    ... )
    >>> i = C()
    >>> i.missing
    'missing item'
    >>> i.foo
    'missing item'
    """

    def __getattr__(self, key):
        try:
            return getattr(super(), key)
        except AttributeError as e:
            noval = object()

            def _safe_getitem(cont, key, missing_result):
                try:
                    return cont[key]
                except KeyError:
                    return missing_result

            result = _safe_getitem(self, key, noval)
            if result is not noval:
                return result
            (message, ) = e.args
            message = message.replace("super", self.__class__.__name__, 1)
            e.args = (message, )
            raise


def invertmap(map):
    """Given a dictionary, return another dictionary with keys and values
    switched. If any of the values resolve to the same key, raises
    a ValueError.

    >>> numbers = dict(a=1, b=2, c=3)
    >>> letters = invertmap(numbers)
    >>> letters[1]
    'a'
    >>> numbers['d'] = 3
    >>> invertmap(numbers)
    Traceback (most recent call last):
    ...
    ValueError: Key conflict in inverted mapping
    """
    res = {v: k for k, v in map.items()}
    if not len(res) == len(map):
        raise ValueError("Key conflict in inverted mapping")
    return res


class IdentityOverrideMap(dict):
    """A dictionary that by default maps each key to itself, but otherwise
    acts like a normal dictionary.

    >>> d = IdentityOverrideMap()
    >>> d[42]
    42
    >>> d['speed'] = 'speedo'
    >>> print(d['speed'])
    speedo
    """

    def __missing__(self, key):
        return key


class Bijection(dict):
    """A Bijective Map (two-way mapping).

    Implemented as a simple dictionary of 2x the size, mapping values back
    to keys.

    Note, this implementation may be incomplete. If there's not a test for
    your use case below, it's likely to fail, so please test and send pull
    requests or patches for additional functionality needed.


    >>> m = BijectiveMap()
    >>> m['a'] = 'b'
    >>> m == {'a': 'b', 'b': 'a'}
    True
    >>> print(m['b'])
    a

    >>> m['c'] = 'd'
    >>> len(m)
    2

    Some weird things happen if you map an item to itself or overwrite a
    single key of a pair, so it's disallowed.

    >>> m['e'] = 'e'
    Traceback (most recent call last):
    ValueError: Key cannot map to itself

    >>> m['d'] = 'e'
    Traceback (most recent call last):
    ValueError: Key/Value pairs may not overlap

    >>> m['e'] = 'd'
    Traceback (most recent call last):
    ValueError: Key/Value pairs may not overlap

    >>> print(m.pop('d'))
    c

    >>> 'c' in m
    False

    >>> m = BijectiveMap(dict(a='b'))
    >>> len(m)
    1
    >>> print(m['b'])
    a

    >>> m = BijectiveMap()
    >>> m.update(a='b')
    >>> m['b']
    'a'

    >>> del m['b']
    >>> len(m)
    0
    >>> 'a' in m
    False
    """

    def __init__(self, *args, **kwargs):
        super().__init__()
        self.update(*args, **kwargs)

    def __setitem__(self, item, value):
        if item == value:
            raise ValueError("Key cannot map to itself")
        overlap = item in self and self[item] != value or (value in self and
                                                           self[value] != item)
        if overlap:
            raise ValueError("Key/Value pairs may not overlap")
        super().__setitem__(item, value)
        super().__setitem__(value, item)

    def __delitem__(self, item):
        self.pop(item)

    def __len__(self):
        return super().__len__() // 2

    def pop(self, key, *args, **kwargs):
        mirror = self[key]
        super().__delitem__(mirror)
        return super().pop(key, *args, **kwargs)

    def update(self, *args, **kwargs):
        d = dict(*args, **kwargs)
        for item in d.items():
            self.__setitem__(*item)


class FrozenDict(collections.abc.Mapping, collections.abc.Hashable):
    """An immutable mapping.

    >>> a = FrozenDict(a=1, b=2)
    >>> b = FrozenDict(a=1, b=2)
    >>> a == b
    True

    >>> a == dict(a=1, b=2)
    True
    >>> dict(a=1, b=2) == a
    True
    >>> 'a' in a
    True
    >>> type(hash(a)) is type(0)
    True
    >>> set(iter(a)) == {'a', 'b'}
    True
    >>> len(a)
    2
    >>> a['a'] == a.get('a') == 1
    True

    >>> a['c'] = 3
    Traceback (most recent call last):
    ...
    TypeError: 'FrozenDict' object does not support item assignment

    >>> a.update(y=3)
    Traceback (most recent call last):
    ...
    AttributeError: 'FrozenDict' object has no attribute 'update'

    Copies should compare equal

    >>> copy.copy(a) == a
    True

    Copies should be the same type

    >>> isinstance(copy.copy(a), FrozenDict)
    True

    FrozenDict supplies .copy(), even though
    collections.abc.Mapping doesn't demand it.

    >>> a.copy() == a
    True
    >>> a.copy() is not a
    True
    """

    __slots__ = ["__data"]

    def __new__(cls, *args, **kwargs):
        self = super().__new__(cls)
        self.__data = dict(*args, **kwargs)
        return self

    def __contains__(self, key):
        return key in self.__data

    def __hash__(self):
        return hash(tuple(sorted(self.__data.items())))

    def __iter__(self):
        return iter(self.__data)

    def __len__(self):
        return len(self.__data)

    def __getitem__(self, key):
        return self.__data[key]

    def get(self, *args, **kwargs):
        return self.__data.get(*args, **kwargs)

    def __eq__(self, other):
        if isinstance(other, FrozenDict):
            other = other.__data
        return self.__data.__eq__(other)

    def copy(self):
        """Return a shallow copy of self."""
        return copy.copy(self)


class Enumerate(NamespaceAdapter, Bijection):
    """A convenient way to provide enumerated values.

    >>> e = Enumeration('a b c')
    >>> e['a']
    0

    >>> e.a
    0

    >>> e[1]
    'b'

    >>> set(e.names) == set('abc')
    True

    >>> set(e.codes) == set(range(3))
    True

    >>> e.get('d') is None
    True

    Codes need not start with 0

    >>> e = Enumeration('a b c', range(1, 4))
    >>> e['a']
    1

    >>> e[3]
    'c'
    """

    def __init__(self, names, codes=None):
        if isinstance(names, str):
            names = names.split()
        if codes is None:
            codes = itertools.count()
        super().__init__(zip(names, codes, strict=True))

    @property
    def names(self):
        return (key for key in self if isinstance(key, str))

    @property
    def codes(self):
        return (self[name] for name in self.names)


class Everything:
    """A collection "containing" every possible thing.

    >>> 'foo' in Everything()
    True

    >>> import random
    >>> random.randint(1, 999) in Everything()
    True

    >>> random.choice([None, 'foo', 42, ('a', 'b', 'c')]) in Everything()
    True
    """

    def __contains__(self, other):
        return True


class InstrumentedDict(collections.UserDict):
    """Instrument an existing dictionary with additional functionality.

    But always reference and mutate
    the original dictionary.

    >>> orig = {'a': 1, 'b': 2}
    >>> inst = InstrumentedDict(orig)
    >>> inst['a']
    1
    >>> inst['c'] = 3
    >>> orig['c']
    3
    >>> inst.keys() == orig.keys()
    True
    """

    def __init__(self, data):
        super().__init__()
        self.data = data


class Least:
    """A value that is always lesser than any other.

    >>> least = Least()
    >>> 3 < least
    False
    >>> 3 > least
    True
    >>> least < 3
    True
    >>> least <= 3
    True
    >>> least > 3
    False
    >>> 'x' > least
    True
    >>> None > least
    True
    """

    def __le__(self, other):
        return True

    __lt__ = __le__

    def __ge__(self, other):
        return False

    __gt__ = __ge__


class Greatest:
    """A value that is always greater than any other.

    >>> greatest = Greatest()
    >>> 3 < greatest
    True
    >>> 3 > greatest
    False
    >>> greatest < 3
    False
    >>> greatest > 3
    True
    >>> greatest >= 3
    True
    >>> 'x' > greatest
    False
    >>> None > greatest
    False
    """

    def __ge__(self, other):
        return True

    __gt__ = __ge__

    def __le__(self, other):
        return False

    __lt__ = __le__


def popall(items):
    """Clear items in place and return a copy of items.

    >>> items = [1, 2, 3]
    >>> popped = popall(items)
    >>> popped is items
    False
    >>> popped
    [1, 2, 3]
    >>> items
    []
    """
    result, items[:] = (items[:], [])
    return result


class FreezableDefaultDict(collections.defaultdict):
    """Often it is desirable to prevent the mutation of
    a default dict after its initial construction, such
    as to prevent mutation during iteration.

    >>> dd = FreezableDefaultDict(list)
    >>> dd[0].append('1')
    >>> dd.freeze()
    >>> dd[1]
    []
    >>> len(dd)
    1
    """

    def __missing__(self, key):
        return getattr(self, "_frozen", super().__missing__)(key)

    def freeze(self):
        self._frozen = lambda key: self.default_factory(
        ) if self.default_factory is not None else None


class Accumulator:

    def __init__(self, initial=0):
        self.val = initial

    def __call__(self, val):
        self.val += val
        return self.val


class WeightedLookup(MapInputsToRanges):
    """Given parameters suitable for a dict representing keys
    and a weighted proportion, return a RangeMap representing
    spans of values proportial to the weights:

    >>> even = WeightedLookup(a=1, b=1)

    [0, 1) -> a
    [1, 2) -> b

    >>> lk = WeightedLookup(a=1, b=2)

    [0, 1) -> a
    [1, 3) -> b

    >>> lk[.5]
    'a'
    >>> lk[1.5]
    'b'

    Adds ``.random()`` to select a random weighted value:

    >>> lk.random() in ['a', 'b']
    True

    >>> choices = [lk.random() for x in range(1000)]

    Statistically speaking, choices should be .5 a:b
    >>> ratio = choices.count('a') / choices.count('b')
    >>> .4 < ratio < .6
    True
    """

    def __init__(self, *args, **kwargs):
        raw = dict(*args, **kwargs)
        indexes = map(Accumulator(), raw.values())
        super().__init__(zip(indexes, raw.keys(), strict=False),
                         discriminator=operator.lt)

    def random(self):
        lower, upper = self.bounds()
        selector = random() * (upper - lower) + lower
        return self[selector]


def caller(depth=1, default="__main__") -> "FrameType | None":
    from inspect import currentframe
    try:
        return currentframe().f_globals.get("__name__", default)
    except AttributeError:
        pass
    try:
        return currentframe().f_globals.get("__name__", default)
    except (AttributeError, ValueError):
        pass
    return None


PositiveInteger: TypeAlias = Literal[
    1,
    2,
    3,
    4,
    5,
    6,
    7,
    8,
    9,
    10,
    11,
    12,
    13,
    14,
    15,
    16,
    17,
    18,
    19,
    20,
    21,
    22,
    23,
    24,
    25,
]
NegativeInteger: TypeAlias = Literal[
    -1,
    -2,
    -3,
    -4,
    -5,
    -6,
    -7,
    -8,
    -9,
    -10,
    -11,
    -12,
    -13,
    -14,
    -15,
    -16,
    -17,
    -18,
    -19,
    -20,
]
Countable: TypeAlias = PositiveInteger | NegativeInteger | Literal[0]
_T_co = TypeVar("_T_co", covariant=True)


class structseq(Protocol[_T_co]):
    n_fields: Final[int]
    n_unnamed_fields: Final[int]
    n_sequence_fields: Final[int]

    def __new__(cls: type[Self],
                sequence: Iterable[_T_co],
                dict: dict[str, Any] = ...) -> Self:
        ...

    if sys.version_info >= (3, 13):

        def __replace__(self: Self, **kwargs: Any) -> Self:
            ...


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

class ExceptionTrap:
    """A context manager that will catch certain exceptions and provide and provide an indication that it occurred.

    >>> with ExceptionTrap() as trap:
    ...     raise Exception()
    >>> bool(trap)
    True

    >>> with ExceptionTrap() as trap:
    ...     pass
    >>> bool(trap)
    False

    >>> with ExceptionTrap(ValueError) as trap:
    ...     raise ValueError("1 + 1 is not 3")
    >>> bool(trap)
    True
    >>> trap.value
    ValueError('1 + 1 is not 3')
    >>> trap.tb
    <traceback object at ...>

    >>> with ExceptionTrap(ValueError) as trap:
    ...     raise Exception()
    Traceback (most recent call last):
    ...
    Exception

    >>> bool(trap)
    False
    """

    exc_info = (None, None, None)

    def __init__(self, exceptions=(Exception, )):
        self.exceptions = exceptions

    def __enter__(self):
        return self

    @property
    def type(self):
        return self.exc_info[0]

    @property
    def value(self):
        return self.exc_info[1]

    @property
    def tb(self):
        return self.exc_info[2]

    def __exit__(self, *exc_info):
        type = exc_info[0]
        matches = type and issubclass(type, self.exceptions)
        if matches:
            self.exc_info = exc_info
        return matches

    def __bool__(self):
        return bool(self.type)

    def raises(self, func, *, _test=bool):
        """Wrap func and replace the result with the truth value of the trap.

        First, give the decorator an alias to support Python 3.8
        Syntax.

        >>> raises = ExceptionTrap(ValueError).raises

        Now decorate a function that always fails.

        >>> @raises
        ... def fail():
        ...     raise ValueError('failed')
        >>> fail()
        True
        """

        @wraps(func)
        def wrapper(*args, **kwargs):
            with ExceptionTrap(self.exceptions) as trap:
                func(*args, **kwargs)
            return _test(trap)

        return wrapper

    def passes(self, func):
        """Wrap func and replace the result with the truth value of the trap (True if no exception).

        First, give the decorator an alias to support Python 3.8
        Syntax.

        >>> passes = ExceptionTrap(ValueError).passes

        Now decorate a function that always fails.

        >>> @passes
        ... def fail():
        ...     raise ValueError('failed')

        >>> fail()
        False
        """
        return self.raises(func, _test=not_)


class suppress(ctx_suppress, ContextDecorator):
    """A version of contextlib.suppress with decorator support.

    >>> @suppress(KeyError)
    ... def key_error():
    ...     {}['']
    >>> key_error()
    """


class on_interrupt(ContextDecorator):
    """Replace a KeyboardInterrupt with SystemExit(1).

    Useful in conjunction with console entry point functions.

    >>> def do_interrupt():
    ...     raise KeyboardInterrupt()
    >>> on_interrupt('error')(do_interrupt)()
    Traceback (most recent call last):
    ...
    SystemExit: 1
    >>> on_interrupt('error', code=255)(do_interrupt)()
    Traceback (most recent call last):
    ...
    SystemExit: 255
    >>> on_interrupt('suppress')(do_interrupt)()
    >>> with __import__('pytest').raises(KeyboardInterrupt):
    ...     on_interrupt('ignore')(do_interrupt)()
    """

    def __init__(self, action="error", /, code=1):
        self.action = action
        self.code = code

    def __enter__(self):
        return self

    def __exit__(self, exctype, excinst, exctb):
        if exctype is not KeyboardInterrupt or self.action == "ignore":
            return None
        if self.action == "error":
            raise SystemExit(self.code) from excinst
        return self.action == "suppress"


def retry_call(func: Callable[[], Any], trap: Type[BaseException],
               retries: int, cleanup: Callable[[], None]) -> Any:
    """Given a callable func, trap the indicated exceptions
    for up to 'retries' times, invoking cleanup on the
    exception. On the final attempt, allow any exceptions
    to propagate.
    """
    attempts = itertools.count() if retries == float("inf") else range(retries)
    for _ in attempts:
        try:
            return func()
        except trap:
            cleanup()
    return func()


def retry(r_args: Any,
          r_kwargs: Any) -> Callable[[Callable[P, R]], Callable[P, R]]:
    """Decorator wrapper for retry_call. Accepts arguments to retry_call
    except func and then returns a decorator for the decorated function.

    Ex:

    >>> @retry(retries=3)
    ... def my_func(a, b):
    ...     "this is my funk"
    ...     print(a, b)
    >>> my_func.__doc__
    'this is my funk'
    """

    def decorate(func):

        @wraps(func)
        def wrapper(*f_args, **f_kwargs):
            bound = partial(func, *f_args, **f_kwargs)
            return retry_call(bound, *r_args, **r_kwargs)

        return wrapper

    return cast(Callable[[Callable[P, R]], Callable[P, R]], decorate)


def print_yielded(func):
    """Convert a generator into a function that prints all yielded elements.

    >>> @print_yielded
    ... def x():
    ...     yield 3; yield None
    >>> x()
    3
    None
    """
    print_all = partial(map, print)
    print_results = compose(consume, print_all, func)
    return wraps(func)(print_results)


def passnone(func):
    """Wrap func so it's not called if its first param is None.

    >>> print_text = passnone(print)
    >>> print_text('text')
    text
    >>> print_text(None)
    """

    @wraps(func)
    def wrapper(param, /, *args, **kwargs):
        if param is not None:
            return func(param, *args, **kwargs)
        return None

    return wrapper


def chain(
    method: Callable[Concatenate[Any, P],
                     R]) -> Callable[Concatenate[Any, P], R]:
    """Wrap None-returning method to return self for chaining.

    >>> class Dingus:
    ...     @chain
    ...     def set_attr(self, name, val):
    ...         setattr(self, name, val)
    >>> d = Dingus().set_attr('a', 'eh!')
    >>> d.a
    'eh!'
    >>> d2 = Dingus().set_attr('a', 'eh!').set_attr('b', 'bee!')
    >>> d2.a + d2.b
    'eh!bee!'

    Enforces that the return value is null.

    >>> class BorkedDingus:
    ...     @chain
    ...     def set_attr(self, name, val):
    ...         setattr(self, name, val)
    ...         return len(name)
    >>> BorkedDingus().set_attr('a', 'eh!')
    Traceback (most recent call last):
    ...
    AssertionError
    """

    @wraps(method)
    def wrapper(self, *args: P.args, **kwargs: P.kwargs) -> R:
        if method(self, *args, **kwargs) is not None:
            raise AssertionError("Method must return None")
        return self

    return wrapper


def extract_python(docstring: str | None) -> tuple[str, list[str], list[str]]:
    """Extract Python code and examples from docstring."""
    if not docstring:
        return ("", [], [])
    code = ""
    in_code_block = False
    ident = 0
    for line in docstring.split("\n"):
        if line.strip().startswith("```"):
            in_code_block = not in_code_block
            continue
        if in_code_block:
            if not ident:
                ident = len(line) - len(line.lstrip())
            code += (line.rstrip() + "\n")[ident:]
    class_def = ""
    examples = []
    responses = []
    for block in code.split(">>>"):
        block = block.strip()
        if not block:
            continue
        if block.startswith("class "):
            class_def = block
        else:
            examples.extend([block.splitlines()[0]] + [
                l.removeprefix(">>> ").replace("...", "   ")
                for l in block.split("\n") if ">>>" in l
            ], )
            r = [
                l.removeprefix(">>>") for l in block.split("\n")
                if ">>>" not in l
            ]
            responses.extend(r)
    return (class_def, examples, responses)


_SupportsNextT = TypeVar("_SupportsNextT", bound=Iterator)
MISSING_TYPES = (NotGivenType, EllipsisType, _MISSING_TYPE,
                 PydanticUndefinedType)
MISSING_VALUES = (NotGiven, ..., _MISSING_TYPE, PydanticUndefined, MISSING)


@checkable
class Exists(Protocol):

    def __bool__(self) -> Literal[True]:
        return True


def ismissing(
    value: "Any"
) -> "TypeIs[_MISSING_TYPE | EllipsisType | PydanticUndefinedType | NotGivenType]":
    """Represents a value that is not specified. Excludes None."""
    if hasattr(value, "__iter__"):
        return False
    if isinstance(value, PydanticUndefinedType):
        return True
    return any(value == missing
               for missing in (*MISSING_VALUES, *MISSING_TYPES)) or any(
                   isinstance(missing, type) and isinstance(value, missing)
                   for missing in MISSING_TYPES)


def isnotgiven(
    value: Any
) -> TypeIs[NotGivenType | EllipsisType | _MISSING_TYPE
            | PydanticUndefinedType]:
    """Represents a value that is not specified. Excludes None."""
    return ismissing(value) or value is None


@imports(ndarray="mbodios.types.ndarray.ndarray", np="numpy")
def exists(
    value: Any | NoneType | NotGivenType | EllipsisType | PydanticUndefinedType
    | _MISSING_TYPE | Literal["MISSING"],
) -> TypeIs[Exists]:
    """Represents a value that is not None and not missing."""
    if ndarray is not None and np is not None and (isinstance(
            value, np.ndarray) or isinstance(value, ndarray)):
        return True
    return (not ismissing(value) and value is not None and (value != "MISSING")
            and (not isinstance(value, NotGivenType))
            and (not isinstance(value, EllipsisType))
            and (not isinstance(value, PydanticUndefinedType)))


@overload
def isgiven(value: Callable) -> TypeGuard[Callable]:
    ...


@overload
def isgiven(value: object) -> TypeIs[Exists]:
    ...


@imports(np="numpy")
def isgiven(value: Any) -> Any:
    if np is not None and hasattr(np, "ndarray") and isinstance(
            value, np.ndarray):
        return True
    if isinstance(value, NotGivenType) or getattr(
            value, "__name__", getattr(type(value), "__name__", None)) in (
                "NotGiven",
                "NotGivenType",
            ):
        return False
    if value is Parameter.empty:
        return False
    if isinstance(value, Parameter.empty):
        return False
    if ("MISSING" in str(value) or isinstance(value, _MISSING_TYPE)
            or isinstance(value, PydanticUndefinedType) or
        (getattr(value, "__name__", getattr(type(value), "__name__", None))
         in ("MISSING", "PydanticUndefinedType"))):
        return False
    if value is ...:
        return False
    return True


if __name__ == "__main__":
    import doctest
    import sys

    doctest.testmod()
