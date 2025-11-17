from __future__ import annotations

from ast import (
    AST,
    AsyncFunctionDef,
    Attribute,
    Call,
    FunctionDef,
    Name,
    NodeVisitor,
    arg,
    arguments,
    iter_child_nodes,
    keyword,
    literal_eval,
    parse,
    walk,
)
from collections.abc import Callable
from typing import Any, Generic, Literal, TypeVar, cast, overload

from typing_extensions import TypedDict, Unpack

ASTType = TypeVar("ASTType",bound=AST)

def replace(node:ASTType,**kwargs:Any) -> ASTType:
    return type(node)(**{**node.__dict__,**kwargs})
def args(args:list[NameAnnotation]) -> list[arg]:
    return [arg_def(name,annotation) for name,annotation in args]
def arg_def(name:str,annotation:type) -> arg:
    return arg(name,literal_eval(f"{annotation.__module__}.{annotation.__name__}"))
def kwargs(kwargs:dict[str,Any]) -> list[keyword]:
    return [keyword(k,literal_eval(v)) for k,v in kwargs.items()]

def call(string:str,*a:Any,**kw:Any) -> Call:
    call_= cast(Call, next(iter_child_nodes(parse(string))))
    return replace(call_,args=arguments(posonlyargs=[],args=args(a),kwonlyargs=kwargs(kw))) # type: ignore[arg-type, call-overload]
    

T = TypeVar("T", bound=Literal["name","node"])
NodeT = TypeVar("NodeT", bound=AST)
T_co = TypeVar("T_co", covariant=True, bound=AST)
NameAnnotation = tuple[str,type] 


class FunctionDefParams(TypedDict):
    posonlyargs: list[NameAnnotation]
    args: list[NameAnnotation]
    kwonlyargs: list[NameAnnotation]
    vararg: NameAnnotation|None
    kwarg: NameAnnotation|None
    defaults: dict[str,Any]

class FunctionDefParamsKwargs(TypedDict,total=False):
    posonlyargs: list[NameAnnotation]
    args: list[NameAnnotation]
    kwonlyargs: list[NameAnnotation]
    vararg: NameAnnotation|None
    kwarg: NameAnnotation|None
    defaults: dict[str,Any]

def args_def(**kwargs:Unpack[FunctionDefParams]) -> arguments:
    args = [args(name,annotation) for name,annotation in kwargs["args"]]
    kwonlyargs = [arg(name,annotation) for name,annotation in kwargs["kwonlyargs"]]

    vararg = arg(*kwargs["vararg"]) if kwargs["vararg"] else None
    kwarg = arg(*kwargs["kwarg"]) if kwargs["kwarg"] else None
    posonlyargs = [arg(name,annotation) for name,annotation in kwargs["posonlyargs"]]
    kw_defaults = [literal_eval(value) for value in kwargs["defaults"].values()]
    defaults_nodes = [literal_eval(value) for name,value in kwargs["defaults"].items()]
    return arguments(
        posonlyargs=posonlyargs,
        args=args,
        vararg=vararg,
        kwonlyargs=kwonlyargs,
        kw_defaults=kw_defaults,
        kwarg=kwarg,
        defaults=defaults_nodes,
    )
def func_def(name: str,**kwargs:Unpack[FunctionDefParamsKwargs]) -> FunctionDef:
    args = args_def(**kwargs)
    return FunctionDef(name=name,
                    args=args,
                    body=[],
                    decorator_list=[],
                    returns=None,
                    type_comment=None)
class MatchAST(NodeVisitor, Generic[NodeT,T]):
    """Callable for matching AST node or name or boolean callable."""
    match: NodeT | str|None
    matcher: Callable[[NodeT], bool]|str|NodeT
    return_type: T

    def __init__(self, target: Callable[[NodeT], bool]|str|NodeT,return_type:T="name"):
        self.matcher = target
        self.match = None
        self.return_type = return_type

    def generic_visit(self, node: NodeT) -> NodeT: # type: ignore
        node = super().generic_visit(node)
        if self.match:
            return cast(NodeT, self.match)
        if callable(self.matcher) and self.matcher(node):
            self.match = node
            return cast(NodeT, node)
        attr, attr_value = self.matcher.split('.', 1) if isinstance(self.matcher, str) else (None, self.matcher)
        if attr and isinstance(node, Attribute) and node.attr == attr and isinstance(node.value, Name) and node.value.id == attr_value:
            self.match = node
            return cast(NodeT, node)

        match node:
            case self.matcher:
                self.match = node
                return cast(NodeT, node)
            case FunctionDef(name=self.matcher):
                self.match = node
            case AsyncFunctionDef(name=self.matcher):
                self.match = node
            case Name(id=self.matcher):
                self.match = node
        return cast(NodeT, node)
    @overload
    def __call__(self:MatchAST[NodeT,Literal['node']], node:AST|str) -> NodeT:...
    @overload
    def __call__(self:MatchAST[NodeT,Literal['name']], node:AST|str) -> str:...
    @overload
    def __call__(self:MatchAST[NodeT,T], node:AST|str) -> T:...
    def __call__(self, node:AST|str) -> Any:
        node = parse(node) if isinstance(node, str) else node
        self.match = None
        self.visit(node)
        if self.match:
            if self.return_type == "name":
                return self.match.name
            return self.match
        raise ValueError(f"No match found for {node}")

def match_ast(node:AST,target:AST|str) -> AST|None:
    match = MatchAST(target)
    return match(node)

class Matcher(NodeVisitor):
    """Minimal matcher to find a FunctionDef/AsyncFunctionDef by name."""

    target: str
    match: AST | None

    def __init__(self, name: str):
        self.target = name
        self.match = None

    def visit(self, node: AST) -> Matcher:
        super().visit(node)
        return self

    def visit_FunctionDef(self, node: FunctionDef) -> None:
        if node.name == self.target:
            self.match = node
            return
        super().generic_visit(node)

    def visit_AsyncFunctionDef(self, node: AsyncFunctionDef) -> None:
        if node.name == self.target:
            self.match = node
            return
        super().generic_visit(node)

    def generic_visit(self, node: AST) -> None:  # type: ignore[override]
        super().generic_visit(node)

    @property
    def result(self) -> AST | None:
        return self.match


def hasname(name: str) -> Callable[[AST], bool]:
    """Return True if the AST contains a Name with the given id."""

    def _hasname(node: AST) -> bool:
        return any(isinstance(n, Name) and n.id == name for n in walk(node))

    return _hasname


def ast_match(node: AST, pattern: str) -> AST | None:
    return Matcher(pattern).visit(node).result