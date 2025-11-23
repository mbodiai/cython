#! mode: run
# tag: annotation_typing, pure3.0
# cython: language_level=3

import cython
from typing import Optional, Union


@cython.annotation_typing(True)
@cython.ccall
def sum_or_default(values: list[int], extra: Optional[int] = None) -> int:
    """
    >>> sum_or_default([1, 2, 3])
    6
    >>> sum_or_default([4, 5], 10)
    19
    >>> sum_or_default([], None)
    0
    """
    total: int = 0
    for value in values:
        total += value
    if extra is not None:
        total += extra
    return total


@cython.annotation_typing(True)
@cython.cfunc
def pick_from_union(flag: bool | None, options: Union[tuple[int, int], tuple[int, int, int]]) -> int:
    """
    >>> pick_from_union(True, (1, 2))
    1
    >>> pick_from_union(False, (1, 2))
    2
    >>> pick_from_union(None, (5, 6, 7))
    7
    """
    if flag:
        return options[0]
    if flag is False:
        return options[1]
    return options[-1]
