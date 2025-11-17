# cython: auto_cpdef=True, infer_types=True

import cython
import dataclasses
from typing import Any


@cython.dataclasses.dataclass
class Ctx:
    level: str = 'other'
    visibility: str = 'private'
    cdef_flag: bool = False
    typedef_flag: bool = False
    api: bool = False
    overridable: bool = False
    nogil: bool = False
    namespace: str | None = None
    templates: list[str] | None = None
    allow_struct_enum_decorator: bool = False
    modifiers: Any = None

    __call__ = clone = dataclasses.replace


