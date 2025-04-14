# Auto-generated stub file for StubTest
from typing import Any, Dict, List, NamedTuple, Optional, TypedDict, Union

# Original class: __main__.StubTest
class StubTest(object):
    value: str
    count: int

    def as_dict(self) -> 'StubTest.Dict': ...
    def as_kwargs(self) -> 'StubTest.Kwargs': ...
    def as_tuple(self) -> 'StubTest.Tuple': ...

class StubTestDict(TypedDict):
    value: str
    count: int

class StubTestKwargs(TypedDict, total=False):
    value: str
    count: int

class StubTestTuple:
    value: str
    count: int

# Type aliases
StubTest.Dict = StubTestDict
StubTest.Kwargs = StubTestKwargs
StubTest.Tuple = StubTestTuple

