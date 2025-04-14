# Auto-generated stub file for DirectiveOption
from typing import Any, Dict, List, List[str], NamedTuple, Optional, TypedDict, Union

# Original class: __main__.DirectiveOption
class DirectiveOption(object):
    name: str
    type: typing.Any
    default: typing.Any
    doc: str
    scope: typing.List[str]

    def as_dict(self) -> 'DirectiveOption.Dict': ...
    def as_kwargs(self) -> 'DirectiveOption.Kwargs': ...
    def as_tuple(self) -> 'DirectiveOption.Tuple': ...

class DirectiveOptionDict(TypedDict):
    name: str
    type: typing.Any
    default: typing.Any
    doc: str
    scope: typing.List[str]

class DirectiveOptionKwargs(TypedDict, total=False):
    name: str
    type: typing.Any
    default: typing.Any
    doc: str
    scope: typing.List[str]

class DirectiveOptionTuple:
    name: str
    type: typing.Any
    default: typing.Any
    doc: str
    scope: typing.List[str]

# Type aliases
DirectiveOption.Dict = DirectiveOptionDict
DirectiveOption.Kwargs = DirectiveOptionKwargs
DirectiveOption.Tuple = DirectiveOptionTuple

