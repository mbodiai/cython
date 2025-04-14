# cython: annotation_typing=False
import asyncio
import sys
from abc import ABC, abstractmethod
from collections.abc import AsyncGenerator, Awaitable, Generator, Iterable, Mapping, MutableSequence
from collections.abc import ItemsView as _ItemsView
from collections.abc import KeysView as _KeysView
from collections.abc import ValuesView as _ValuesView
from importlib.machinery import ModuleSpec
from types import GenericAlias, UnionType, new_class
import typing
from typing import Tuple
from typing_extensions import (
    AbstractSet,
    Any,
    Callable,
    ClassVar,
    Generic,
    Literal,
    ParamSpec,
    Self,
    TypeAlias,
    TypeIs,
    TypeVar,
    Union,
    cast,
    final,
    overload,
    runtime_checkable,
)
import typing_extensions

MaybeNone: TypeAlias = Any
_S = TypeVar("_S")

_T_co = TypeVar("_T_co", covariant=True)
_KT_co = TypeVar("_KT_co", covariant=True)
_VT_co = TypeVar("_VT_co", covariant=True)
_KT = TypeVar("_KT")
_VT = TypeVar("_VT")

_YieldT_co = TypeVar("_YieldT_co", covariant=True)
_SendT_contra = TypeVar("_SendT_contra", contravariant=True, default=None)
_ReturnT_co = TypeVar("_ReturnT_co", covariant=True, default=None)

_AwaitableLike: TypeAlias = Generator[Any, None, _T_co] | Awaitable[_T_co]

P = ParamSpec("P")
Q = ParamSpec("Q")
_Q = ParamSpec("_Q")
_P = ParamSpec("_P")
_T1 = TypeVar("_T1")
_T2 = TypeVar("_T2")


_T = TypeVar("_T")
_T_co = TypeVar("_T_co", covariant=True)
_R = TypeVar("_R")
_R_co = TypeVar("_R_co", covariant=True)
TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing_extensions import Protocol
    from typing import _ProtocolMeta
else:
    from typing_extensions import _ProtocolMeta,TypeVarTuple
    Ts = TypeVarTuple("Ts")
    class Protocol(Generic[*Ts]):...
    def runtime_checkable(cls):
        return cls

    import typing
    import typing_extensions


class PredicateMeta(_ProtocolMeta, Generic[_P, _T]):

    def __and__(
        self: "PredicateMeta[_P, bool]", other: "PredicateType[...,bool] | Callable[...,bool]",
    ) -> "PredicateType[...,bool]":
        def andfunc(*args: _P.args, **kwargs: _P.kwargs) -> bool:
            return  self(*args, **kwargs) and other(*args, **kwargs)

        return Predicate(andfunc)
    def __new__(cls,name,bases,namespace):
        bases = tuple(filter(lambda b: b not in (typing.Protocol,typing_extensions.Protocol),bases))
        return super().__new__(cls, name, bases, namespace)     

class FuncP(Protocol[_P, _R_co]):
    def __call__(self: "FuncP[_P, _R_co]", *args: _P.args, **kwargs: _P.kwargs) -> _R_co: ...


class AFuncP(Protocol[_P, _R_co]):
    async def __call__(self: "AFuncP[_P, _R_co]", *args: _P.args, **kwargs: _P.kwargs) -> _R_co: ...


@runtime_checkable
class AsyncGenP(Protocol[_P, _R_co]):
    def __aiter__(self: "AsyncGenP[_P, _R]") -> AsyncGenerator[Any, _R]: ...
    async def __anext__(self: "AsyncGenP[_P, _R_co]") -> _R_co: ...
    async def asend(self: "AsyncGenP[_P, _R_co]", value: Any) -> _R_co: ...


@runtime_checkable
class GenP(Protocol[_P, _R]):
    def __iter__(self: "GenP[_P, _R]") -> Generator[Any, _R, None]: ...
    def __next__(self: "GenP[_P, _R]") -> _R: ...
    def send(self: "GenP[_P, _R]", value: Any) -> _R: ...
    def throw(self: "GenP[_P, _R]", exc: BaseException) -> _R: ...
    def close(self: "GenP[_P, _R]") -> None: ...

class MissingType:
    def __bool__(self) -> bool:
        raise Exception("MissingType")

MISSING = MissingType()

@runtime_checkable
class PredicateType(Protocol[_P, _T],metaclass=PredicateMeta):
    fn: Callable[_P, _T]
    result: _T|MissingType = MISSING

    def __init__(self, fn: Callable[_P, _T]) -> None:
        self.fn = fn

    def __call__(self, *args: _P.args, **kwargs: _P.kwargs) -> _T:
        self.result = self.fn(*args, **kwargs)
        return self.result

    def __mul__(
        self: "PredicateType[_P, _T]", other: "Callable[_Q, _R] | PredicateType[_Q, _R]",
    ) -> "PredicateType[_Q,_T]":
        from mbcore.collect import compose

        return cast(PredicateType[_Q, _T], type(self)(cast(Callable[_P, _T], compose(other, self.fn))))

    def __rmul__(
        self: "PredicateType[_P, _T]", other: "Callable[_Q, _R] | PredicateType[_Q, _R]",
    ) -> "PredicateType[_P,_R]":
        from mbcore.collect import compose

        return cast(PredicateType[_P, _R], type(self)(cast(Callable[_P, _T], compose(self.fn, other))))

    def __imul__(self, other: Union[Callable[[_S], _R], "PredicateType[[_S], _R]"]) -> "PredicateType[_P, _T]":
        from mbcore.collect import compose

        self.fn = compose(self.fn, other)
        return self

    def __or__(self, other: Union[Callable[[_S], _R], "PredicateType[[_S], _R]"]) -> "PredicateType[_P, _T]":
        from mbcore.collect import compose

        self.fn = compose(self.fn, other)
        return self

    def __and__(self, other: "Callable[...,bool] | 'PredicateType[...,bool]'") -> "PredicateType[...,bool]":
        def andfunc(*args: _P.args, **kwargs: _P.kwargs) -> bool:
            return self.fn(*args, **kwargs) and other(*args, **kwargs)

        return cast(PredicateType[..., bool], type(self)(cast(Callable[_P, _T], andfunc)))


class Predicate(PredicateType[_P, bool]): ...



_TypeT = TypeVar("_TypeT", bound=type | UnionType | GenericAlias|Tuple[Any, ...]  | Any)
class Is(PredicateType[[_TypeT], bool]):
    """Predicate that checks if a value is an instance of one or more types.

    Example:
        >>> is_int = Is[int]
        >>> is_int(1)
        True
        >>> is_int('1')
        False
        >>> is_int(1.0)
        False
        >>> is_int(1j)
        False

    """

    _types: Tuple[_TypeT, ...] = ()
    result: bool|MissingType = MISSING
    def __new__(cls, *args: Any | Tuple[Any, ...], **kwargs) -> "TypeIs[_TypeT]":
        cls.result = any(isinstance(t,cls._types) for t in args)
        inst = super().__new__(cls)
        
        inst.__init__()
        return inst.result
    

    def __init__(self, *args: Tuple[_TypeT, ...]|_TypeT, **kwargs) -> None:
        """Initializes the Is predicate instance.

        Relies on the _types attribute being set on the class by __class_getitem__.
        """

        def check(*value: Any) -> bool:
            """Checks if the value is an instance of the types stored in the class."""
            # Check if the value is an instance of any of the types stored in the class
        
        super().__init__(lambda *args: check(*args)) # Pass the correct check function
    @classmethod
    def __class_getitem__(
            cls: type[Self],
                item: _T | Tuple[_T, ...]) -> "Callable[[Any], TypeIs[_T]]":
        if not isinstance(item, tuple):
            types = (item, )
        else:
            types = item
        types = tuple(map(lambda x: getattr(x, "__origin__", x), types))
        return new_class(
            f"Is[{','.join(map(lambda x: getattr(x, '__name__', str(x)), types))}]",
            (cls, ),
            exec_body=lambda ns: ns.update({"_types": types}),
        )

    def __repr__(self) -> str:
        types = ", ".join(t.__name__ for t in self._types)
        return f"Is[{types}]"


@runtime_checkable
class IterableP(Protocol[_T_co]):
    @abstractmethod
    def __iter__(self) -> "IteratorP[_T_co]": ...


@runtime_checkable
class IteratorP(IterableP[_T_co], Protocol[_T_co]):
    @abstractmethod
    def __next__(self) -> _T_co: ...
    def __iter__(self) -> "IteratorP[_T_co]": ...


@runtime_checkable
class Indexable(Protocol[_T_co]):
    if sys.version_info >= (3, 10):

        def __index__(self) -> int: ...

    def __len__(self) -> int: ...
    def __getitem__(self, index: int, /) -> _T_co: ...


@runtime_checkable
class SupportsKeysAndGetItem(Protocol[_KT_co, _VT_co]):
    def keys(self: "SupportsKeysAndGetItem[_KT, _VT]", /) -> AbstractSet[_KT]: ...
    def __getitem__(self: "SupportsKeysAndGetItem[_KT, _VT]", key: _KT, /) -> _VT: ...
    def update(self: "SupportsKeysAndGetItem[_KT, _VT]", other: dict[_KT, _VT], /) -> None: ...
    def get(self: "SupportsKeysAndGetItem[_KT, _VT]", key: _KT, default: _VT, /) -> _VT: ...


@runtime_checkable
class SupportsKeysItems(Protocol[_KT_co, _VT_co]):
    def keys(
        self: "SupportsKeysItems[_KT, _VT] | Mapping[_KT,_VT]", /,
    ) -> AbstractSet[_KT] | _KeysView[_KT] | IteratorP[_KT]: ...
    def __getitem__(self: "SupportsKeysItems[_KT, _VT] | Mapping[_KT,_VT]", key: _KT, /) -> _VT: ...
    def update(self: "SupportsKeysItems[_KT, _VT] | Mapping[_KT,_VT]", other: dict[_KT, _VT], /) -> None: ...
    def get(self: "SupportsKeysItems[_KT, _VT] | Mapping[_KT,_VT]", key: _KT, default: _VT, /) -> _VT: ...
    def items(self) -> _ItemsView[str, _VT_co] | IteratorP[tuple[str, _VT_co]]: ...
    def values(self) -> _ValuesView[_VT_co] | IteratorP[_VT_co]: ...
    def __iter__(self) -> _KeysView[str] | IteratorP[str]: ...
    def __contains__(self, x: Any, /) -> bool: ...
    def __len__(self) -> int: ...
    def setdefault(self, key: _KT, default: _VT, /) -> _VT: ...
    def pop(self, key: _KT, default: _VT, /) -> _VT: ...
    def popitem(self) -> tuple[_KT, _VT]: ...
    def clear(self) -> None: ...


@final
class MappingProxyType(Mapping[_KT, _VT_co], ABC):
    __hash__: ClassVar[None]  # type: ignore[assignment]

    def __new__(cls, mapping: SupportsKeysAndGetItem[_KT, _VT_co]) -> Self: ...
    def __getitem__(self, key: _KT, /) -> _VT_co: ...
    def __iter__(self) -> IteratorP[_KT]: ...
    def __len__(self) -> int: ...
    def __eq__(self, value: object, /) -> bool: ...
    def copy(self) -> dict[_KT, _VT_co]: ...
    def keys(self) -> _KeysView[_KT]: ...
    def values(self) -> _ValuesView[_VT_co]: ...
    def items(self) -> _ItemsView[_KT, _VT_co]: ...

    @abstractmethod
    @overload
    def get(self, key: _KT, /) -> _VT_co | None: ...

    @abstractmethod
    @overload
    def get(self, key: _KT, default: _VT_co | _T2, /) -> _VT_co | _T2: ...

    if sys.version_info >= (3, 9):

        def __class_getitem__(cls, item: Any, /) -> GenericAlias: ...
        def __reversed__(self) -> IteratorP[_KT]: ...
        def __or__(self, value: Mapping[_T1, _T2], /) -> dict[_KT | _T1, _VT_co | _T2]: ...
        def __ror__(self, value: Mapping[_T1, _T2], /) -> dict[_KT | _T1, _VT_co | _T2]: ...


class SimpleNamespaceP(Protocol):
    __hash__: ClassVar[None]  # type: ignore[assignment]
    if sys.version_info >= (3, 13):

        def __init__(
            self, mapping_or_iterable: Mapping[str, Any] | Iterable[tuple[str, Any]] = (), /, **kwargs: Any,
        ) -> None: ...
    else:

        def __init__(self, **kwargs: Any) -> None: ...

    def __eq__(self, value: object, /) -> bool: ...
    def __getattribute__(self, name: str, /) -> Any: ...
    def __setattr__(self, name: str, value: Any, /) -> None: ...
    def __delattr__(self, name: str, /) -> None: ...

    if sys.version_info >= (3, 13):

        def __replace__(self, **kwargs: Any) -> Self: ...


class LoaderProtocol(Protocol):
    def load_module(self, fullname: str, /) -> "ModuleP": ...


class ModuleP:
    __name__: str
    __file__: str | None

    @property
    def __dict__(self) -> dict[str, Any]: ...  # type: ignore[override]

    __loader__: LoaderProtocol | None
    __package__: str | None
    __path__: MutableSequence[str]
    __spec__: ModuleSpec | None
    # N.B. Although this is the same type as `builtins.object.__doc__`,
    # it is deliberately redeclared here. Most symbols declared in the namespace
    # of `types.ModuleType` are available as "implicit globals" within a module's
    # namespace, but this is not true for symbols declared in the namespace of `builtins.object`.
    # Redeclaring `__doc__` here helps some type checkers understand that `__doc__` is available
    # as an implicit global in all modules, similar to `__name__`, `__file__`, `__spec__`, etc.
    __doc__: str | None

    def __init__(self, name: str, doc: str | None = ...) -> None: ...
    # __getattr__ doesn't exist at runtime,
    # but having it here in typeshed makes dynamic imports
    # using `builtins.__import__` or `importlib.import_module` less painful
    def __getattr__(self, name: str) -> Any: ...


class CellP(Protocol):
    def __new__(cls, contents: object = ..., /) -> Self: ...

    __hash__: ClassVar[None]  # type: ignore[assignment]
    cell_contents: Any


_YieldT_co = TypeVar("_YieldT_co", covariant=True)
_SendT_contra = TypeVar("_SendT_contra", contravariant=True)
_ReturnT_co = TypeVar("_ReturnT_co", covariant=True)

CodeP = Any


class GeneratorP(Protocol[_YieldT_co, _SendT_contra, _ReturnT_co]):
    @property
    def gi_code(self) -> CodeP: ...
    @property
    def gi_frame(self) -> "FrameP": ...
    @property
    def gi_running(self) -> bool: ...
    @property
    def gi_yieldfrom(self) -> "GeneratorP[_YieldT_co, _SendT_contra, Any] | None": ...

    if sys.version_info >= (3, 11):

        @property
        def gi_suspended(self) -> bool: ...

    __name__: str
    __qualname__: str

    def __iter__(self) -> Self: ...
    def __next__(self) -> _YieldT_co: ...
    def send(self, arg: _SendT_contra, /) -> _YieldT_co: ...
    @overload
    def throw(
        self, typ: type[BaseException], val: BaseException | object = ..., tb: "TracebackP | None" = ..., /,
    ) -> _YieldT_co: ...
    @overload
    def throw(self, typ: BaseException, val: None = None, tb: "TracebackP | None" = ..., /) -> _YieldT_co: ...

    if sys.version_info >= (3, 13):

        def __class_getitem__(cls, item: Any, /) -> Any: ...


@final
class AsyncGeneratorP(Protocol[_YieldT_co, _SendT_contra]):
    @property
    def ag_await(self) -> Awaitable[Any] | None: ...
    @property
    def ag_code(self) -> CodeP: ...
    @property
    def ag_frame(self) -> "FrameP": ...
    @property
    def ag_running(self) -> bool: ...

    __name__: str
    __qualname__: str
    if sys.version_info >= (3, 12):

        @property
        def ag_suspended(self) -> bool: ...

    def __aiter__(self) -> Self: ...
    def __anext__(self) -> "Coroutine[Any, Any, _YieldT_co]": ...
    def asend(self, val: _SendT_contra, /) -> "Coroutine[Any, Any, _YieldT_co]": ...
    @overload
    async def athrow(
        self, typ: type[BaseException], val: BaseException | object = ..., tb: "TracebackP | None" = ..., /,
    ) -> _YieldT_co: ...
    @overload
    async def athrow(self, typ: BaseException, val: None = None, tb: "TracebackP | None" = ..., /) -> _YieldT_co: ...
    def aclose(self) -> "CoroutineP[Any, Any, None]": ...

    if sys.version_info >= (3, 9):

        def __class_getitem__(cls, item: Any, /) -> GenericAlias: ...


@runtime_checkable
class CoroutineP(Protocol[_YieldT_co, _SendT_contra, _ReturnT_co]):
    __name__: str
    __qualname__: str

    @property
    def cr_await(self) -> Any | None: ...
    @property
    def cr_code(self) -> "CodeP": ...
    @property
    def cr_frame(self) -> "FrameP": ...
    @property
    def cr_running(self) -> bool: ...
    @property
    def cr_origin(self) -> tuple[tuple[str, int, str], ...] | None: ...

    if sys.version_info >= (3, 11):

        @property
        def cr_suspended(self) -> bool: ...

    def close(self) -> None: ...
    def __await__(self) -> Generator[Any, None, _ReturnT_co]: ...
    def send(self, arg: _SendT_contra, /) -> _YieldT_co: ...
    @overload
    def throw(
        self, typ: type[BaseException], val: BaseException | object = ..., tb: "TracebackP | None " = ..., /,
    ) -> _YieldT_co: ...
    @overload
    def throw(self, typ: BaseException, val: None = None, tb: "TracebackP | None" = ..., /) -> _YieldT_co: ...

    if sys.version_info >= (3, 13):

        def __class_getitem__(cls, item: Any, /) -> Any: ...


@runtime_checkable
class MethodP(Protocol):
    @property
    def __closure__(self) -> "tuple[CellP, ...] | None": ...  # inherited from the added function
    @property
    def __code__(self) -> "CodeP": ...  # inherited from the added function
    @property
    def __defaults__(self) -> tuple[Any, ...] | None: ...  # inherited from the added function
    @property
    def __func__(self) -> Callable[..., Any]: ...
    @property
    def __self__(self) -> object: ...
    @property
    def __name__(self) -> str: ...  # inherited from the added function

    __qualname__: str

    def __new__(cls, func: Callable[..., Any], instance: object, /) -> Self: ...
    def __call__(self, *args: Any, **kwargs: Any) -> Any: ...
    def __eq__(self, value: object, /) -> bool: ...
    def __hash__(self) -> int: ...


@runtime_checkable
class BuiltinFunctionP(Protocol):
    @property
    def __self__(self) -> object | ModuleP: ...
    @property
    def __name__(self) -> str: ...

    __qualname__: str

    def __call__(self, *args: Any, **kwargs: Any) -> Any: ...
    def __eq__(self, value: object, /) -> bool: ...
    def __hash__(self) -> int: ...


BuiltinMethodP = BuiltinFunctionP


@runtime_checkable
class WrapperDescriptorP(Protocol):
    @property
    def __name__(self) -> str: ...

    __qualname__: str

    @property
    def __objclass__(self) -> type: ...
    def __call__(self, *args: Any, **kwargs: Any) -> Any: ...
    def __get__(self, instance: Any, owner: type | None = None, /) -> Any: ...


@runtime_checkable
class MethodWrapperP(Protocol):
    @property
    def __self__(self) -> object: ...
    @property
    def __name__(self) -> str: ...

    __qualname__: str

    @property
    def __objclass__(self) -> type: ...
    def __call__(self, *args: Any, **kwargs: Any) -> Any: ...
    def __eq__(self, value: object, /) -> bool: ...
    def __ne__(self, value: object, /) -> bool: ...
    def __hash__(self) -> int: ...


@runtime_checkable
class MethodDescriptorP(Protocol):
    @property
    def __name__(self) -> str: ...

    __qualname__: str

    @property
    def __objclass__(self) -> type: ...
    def __call__(self, *args: Any, **kwargs: Any) -> Any: ...
    def __get__(self, instance: Any, owner: type | None = None, /) -> Any: ...


@runtime_checkable
class ClassMethodDescriptorP(Protocol):
    @property
    def __name__(self) -> str: ...

    __qualname__: str

    @property
    def __objclass__(self) -> type: ...
    def __call__(self, *args: Any, **kwargs: Any) -> Any: ...
    def __get__(self, instance: Any, owner: type | None = None, /) -> Any: ...


@runtime_checkable
class TracebackP(Protocol):
    def __new__(cls, tb_next: "TracebackP | None", tb_frame: "FrameP", tb_lasti: int, tb_lineno: int) -> Self: ...

    tb_next: "TracebackP | None"

    # the rest are read-only
    @property
    def tb_frame(self) -> "FrameP": ...
    @property
    def tb_lasti(self) -> int: ...
    @property
    def tb_lineno(self) -> int: ...


@runtime_checkable
class FrameP(Protocol):
    @property
    def f_back(self) -> "FrameP | None": ...
    @property
    def f_builtins(self) -> dict[str, Any]: ...
    @property
    def f_code(self) -> "CodeP": ...
    @property
    def f_globals(self) -> dict[str, Any]: ...
    @property
    def f_lasti(self) -> int: ...
    # see discussion in #6769: f_lineno *can* sometimes be None,
    # but you should probably file a bug report with CPython if you encounter it being None in the wild.
    # An `int | None` annotation here causes too many false-positive errors, so applying `int | Any`.
    @property
    def f_lineno(self) -> int | MaybeNone: ...
    @property
    def f_locals(self) -> dict[str, Any]: ...

    f_trace: "Callable[[FrameP, str, Any], Any] | None"
    f_trace_lines: bool
    f_trace_opcodes: bool

    def clear(self) -> None: ...


@runtime_checkable
class GetSetDescriptorP(Protocol):
    @property
    def __name__(self) -> str: ...

    __qualname__: str

    @property
    def __objclass__(self) -> type: ...
    def __get__(self, instance: Any, owner: type | None = None, /) -> Any: ...
    def __set__(self, instance: Any, value: Any, /) -> None: ...
    def __delete__(self, instance: Any, /) -> None: ...


@runtime_checkable
class MemberDescriptorP(Protocol):
    @property
    def __name__(self) -> str: ...

    __qualname__: str

    @property
    def __objclass__(self) -> type: ...
    def __get__(self, instance: Any, owner: type | None = None, /) -> Any: ...
    def __set__(self, instance: Any, value: Any, /) -> None: ...
    def __delete__(self, instance: Any, /) -> None: ...


@runtime_checkable
class _SupportsNext(Protocol[_T_co]):
    def __next__(self) -> _T_co: ...


# This protocol is generic over the iterator type, while Iterable is
# generic over the type that is iterated over.
class SupportsIter(Protocol[_T_co]):
    def __iter__(self) -> _T_co: ...


class GetItemIterable(Protocol[_T_co]):
    def __iter__(self) -> IteratorP[_T_co]: ...
    def __getitem__(self, k: int, /) -> _T_co: ...


# This protocol is generic over the iterator type, while AsyncIterable is
# generic over the type that is iterated over.
class SupportsAiter(Protocol[_T_co]):
    def __aiter__(self) -> _T_co: ...


class SupportsLenAndGetItem(Protocol[_T_co]):
    def __len__(self) -> int: ...
    def __getitem__(self, k: int, /) -> _T_co: ...


@runtime_checkable
class GeneratorType(IteratorP[_YieldT_co], Generic[_YieldT_co, _SendT_contra, _ReturnT_co]):
    def __next__(self) -> _YieldT_co: ...
    @abstractmethod
    def send(self, value: _SendT_contra, /) -> _YieldT_co: ...
    @overload
    @abstractmethod
    def throw(
        self, typ: type[BaseException], val: BaseException | object = None, tb: "TracebackP | None" = None, /,
    ) -> _YieldT_co: ...
    @overload
    @abstractmethod
    def throw(self, typ: BaseException, val: None = None, tb: "TracebackP | None" = None, /) -> _YieldT_co: ...
    def close(self) -> None: ...
    def __iter__(self) -> "GeneratorP[_YieldT_co, _SendT_contra, _ReturnT_co]": ...
    @property
    def gi_code(self) -> CodeP: ...
    @property
    def gi_frame(self) -> FrameP: ...
    @property
    def gi_running(self) -> bool: ...
    @property
    def gi_yieldfrom(self) -> "GeneratorP[Any, Any, Any] | None": ...


@runtime_checkable
class CoroutineType(Protocol[_YieldT_co, _SendT_contra, _ReturnT_co]):
    __name__: str
    __qualname__: str

    @property
    def cr_origin(self) -> tuple[tuple[str, int, str], ...] | None: ...

    if sys.version_info >= (3, 11):

        @property
        def cr_suspended(self) -> bool: ...

    def close(self) -> None: ...
    def __await__(self) -> GeneratorP[_YieldT_co, _SendT_contra, _ReturnT_co]: ...
    def send(self, arg: _SendT_contra, /) -> _YieldT_co: ...
    @overload
    def throw(
        self, typ: type[BaseException], val: BaseException | object = ..., tb: "TracebackP | None" = ..., /,
    ) -> _YieldT_co: ...
    @overload
    def throw(self, typ: BaseException, val: None = None, tb: "TracebackP | None " = ..., /) -> _YieldT_co: ...

    if sys.version_info >= (3, 13):

        def __class_getitem__(cls, item: Any, /) -> Any: ...


_CoroutineLike: TypeAlias = "Generator[Any, None, _T_co] | CoroutineP[Any, Any, _T_co]"


@runtime_checkable
class AsyncGeneratorType(Protocol[_YieldT_co, _SendT_contra]):
    @property
    def ag_await(self) -> Awaitable[Any] | None: ...

    __name__: str
    __qualname__: str
    if sys.version_info >= (3, 12):

        @property
        def ag_suspended(self) -> bool: ...

    def __aiter__(self) -> Self: ...
    def __anext__(self) -> "_CoroutineLike[_YieldT_co]": ...
    def asend(self, val: "_SendT_contra", /) -> "_CoroutineLike[_YieldT_co]": ...


class Coroutine(CoroutineP[_YieldT_co, _SendT_contra, _ReturnT_co], Generic[_YieldT_co, _SendT_contra, _ReturnT_co]):
    def __init__(self) -> None:
        self.closed = False
        self._value: _ReturnT_co | None = None
        self._last_sent: _SendT_contra | None = None
        self._state: Literal["INITIAL", "RUNNING", "SUSPENDED", "CLOSED"] = "INITIAL"
        self.__name__ = self.__class__.__name__
        self.__qualname__ = self.__class__.__qualname__
        # Get the creation frame info for debugging
        if hasattr(sys, "_getframe"):
            frame = sys._getframe(1)
            self._cr_origin = ((frame.f_code.co_filename, frame.f_lineno, frame.f_code.co_name),)
        else:
            self._cr_origin = None
        self._loop = asyncio.get_running_loop()
        self._current_future: asyncio.Future[Any] | None = None

    @property
    def cr_running(self) -> bool:
        return self._state == "RUNNING"

    @property
    def cr_frame(self) -> FrameP:
        from inspect import currentframe

        return currentframe()  # type: ignore

    @property
    def cr_suspended(self) -> bool:
        return self._state == "SUSPENDED"

    @property
    def cr_origin(self) -> tuple[tuple[str, int, str], ...] | None:
        """Return a tuple of (filename, line_number, function_name) tuples.

        Provides information where the coroutine was created, or None if
        this info is not available.
        """
        return self._cr_origin

    @property
    def cr_await(self) -> Any | None:
        while self._state == "RUNNING":
            pass
        return None

    @property
    def cr_code(self) -> CodeP:
        from inspect import getsource

        return getsource(self.__class__)

    def __await__(self) -> Generator[asyncio.Future[_YieldT_co], None, _ReturnT_co]:
        if self.closed:
            raise StopIteration(self._value)

        try:
            self._state = "RUNNING"
            # Handle yield before yielding the future to record the event
            yield_value = self._handle_yield(None)  # Record the yield event
            print("Yielding first Future with result:", yield_value)

            # Create and complete the Future before yielding
            self._current_future = self._loop.create_future()
            self._current_future.set_result(yield_value)  # Complete the future
            yield self._current_future  # Yielding a completed Future
            print("First Future yielded and completed")

            self._state = "SUSPENDED"

            # Handle send and set result for the next future
            result = self._handle_send(self._last_sent)
            self._current_future = self._loop.create_future()
            self._current_future.set_result(result)  # Set result immediately instead of scheduling
            yield self._current_future  # Yielding a completed Future

            if self._value is None:
                raise RuntimeError("No return value set")
            return self._value
        finally:
            self._state = "CLOSED"
            self.closed = True

    def send(self, arg: _SendT_contra, /) -> _YieldT_co:
        if self.closed:
            raise StopIteration(self._value)
        if self._state == "INITIAL" and arg is not None:
            raise TypeError("can't send non-None value to a just-started coroutine")

        self._state = "RUNNING"
        self._last_sent = arg  # Store sent value
        try:
            result = self._handle_send(arg)
            if self._current_future and not self._current_future.done():
                # Schedule the Future's result to be set asynchronously
                self._loop.call_soon_threadsafe(self._current_future.set_result, result)
            self._state = "SUSPENDED"
            return result
        except StopIteration as e:
            self._state = "CLOSED"
            self.closed = True
            self._value = e.value  # Capture return value from StopIteration
            raise

    def _handle_yield(self, send_value: _SendT_contra | None = None) -> _YieldT_co:
        """Override to control the yielded value."""
        raise NotImplementedError

    def _handle_send(self, arg: _SendT_contra) -> _YieldT_co:
        raise NotImplementedError

    def close(self) -> None:
        self._state = "CLOSED"
        self.closed = True

    @overload
    def throw(
        self, typ: type[BaseException], val: BaseException | object = None, tb: TracebackP | None = None, /,
    ) -> _YieldT_co: ...

    @overload
    def throw(self, typ: BaseException, val: None = None, tb: TracebackP | None = None, /) -> _YieldT_co: ...

    def throw(
        self, typ: type[BaseException] | BaseException, val: Any = None, tb: TracebackP | None = None, /,
    ) -> _YieldT_co:
        if self.closed:
            raise StopIteration(self._value)

        self._state = "RUNNING"
        exc = typ if isinstance(typ, BaseException) else typ(val)
        if tb is not None:
            exc.__traceback__ = tb

        self._state = "CLOSED"
        self.closed = True
        raise exc


@runtime_checkable
class SupportsLen(Protocol[_T_co]):
    def __len__(self) -> int: ...


@runtime_checkable
class SupportsLenAndGetSetItem(Protocol[_T_co]):
    def __len__(self) -> int: ...

    def __getitem__(self: "SupportsLenAndGetSetItem[_T]", k: int | slice, /) -> _T: ...

    def __setitem__(self: "SupportsLenAndGetSetItem[_T]", k: int | slice, v: _T) -> None: ...

    def __add__(self: "SupportsLenAndGetSetItem[_T]", __iterable: "Any") -> "SupportsLenAndGetSetItem[_T]": ...

    def __iadd__(self: "SupportsLenAndGetSetItem[_T]", __iterable: "Any") -> "SupportsLenAndGetSetItem[_T]": ...


@runtime_checkable
class SupportsClearAndExtends(Protocol[_T]):
    def clear(self: "SupportsClearAndExtends[_T]") -> None: ...

    def extend(self: "SupportsClearAndExtends[_T]", __iterable: "Iterable[_T]") -> None: ...


SupportsIterType: TypeAlias = (
    list
    | tuple
    | set
    | frozenset
    | dict
    | str
    | bytes
    | bytearray
    | memoryview
    | range
    | _ItemsView
    | _KeysView
    | _ValuesView
    | IteratorP
    | Generator
)

if __name__ == "__main__":
    import asyncio  # Ensure asyncio is imported

    async def main():
        # Example usage
        class ProtocolTestCoro(Coroutine[str, None, dict]):
            def __init__(self):
                super().__init__()
                self.yields = []
                self.sends = []

            def _handle_yield(self, send_value: None = None) -> str:
                self.yields.append(("yield", send_value))
                return "yield_value"

            def _handle_send(self, arg: None) -> str:
                self.sends.append(("send", arg))
                self._value = {"final": "value"}
                return "send_value"

        coro = ProtocolTestCoro()
        gen = coro.__await__()

        try:
            f1 = next(gen)
            print(f"Yielded value: {f1}")

            f2 = gen.send(None)
            print(f"Yielded value after send(None): {f2}")

            result = gen.send(None)
            print(f"Returned result: {result}")

            assert result == {"final": "value"}, f"Expected {{'final': 'value'}}, got {result}"
            assert coro.closed, "Coroutine should be closed after completion"
            assert coro._state == "CLOSED", f"Expected state 'CLOSED' after completion, got {coro._state}"
            assert len(coro.yields) == 1, f"Expected 1 yield, got {len(coro.yields)}"
            assert len(coro.sends) == 1, f"Expected 1 send, got {len(coro.sends)}"
            assert coro.sends[0][0] == "send", f"Expected first send action to be 'send', got {coro.sends[0][0]}"
            assert coro.yields[0][0] == "yield", f"Expected first yield action to be 'yield', got {coro.yields[0][0]}"
            print("All assertions passed!")
        except StopIteration as e:
            print(f"Coroutine completed with return value: {e.value}")
        except Exception as ex:
            print(f"An unexpected exception occurred: {ex}")

    asyncio.run(main())
