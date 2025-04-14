from heapq import merge
from itertools import chain, tee

from typing_extensions import Any, Callable, Iterable, Tuple, TypeVar

from mbcore.more import islice_extended, nth

T = TypeVar("T")
U = TypeVar("U")


def contains(item):
    """Return a function that checks if an item is in the given iterable.

    >>> contains_0 = contains(0)
    >>> contains_0(range(5))
    True
    >>> contains_0(range(1, 5))
    False
    """
    return lambda iterable: item in iterable


def peek(iterable: Iterable[T]) -> T | None:
    """Return an iterator that yields the first item then the entire *iterable* or *None* if the *iterable* is empty.

    >>> iterable = [0, 1, 2, 3]
    >>> peeked = peek(iterable)
    >>> next(peeked)
    0
    >>> list(peeked)
    [0, 1, 2, 3]
    """
    try:
        first = next(iter(iterable))
    except StopIteration:
        return None
    return chain([first], iterable)


def first(iterable: Iterable[T]) -> T:
    """Return the first item of the *iterable*.

    >>> iterable = [0, 1, 2, 3]
    >>> first(iterable)
    0
    """
    return next(iter(iterable))


def zip_repeat_last(
    *iterables: Iterable[T], key: Callable[[T], Any] = first, fillvalue: Any = None,
) -> Iterable[Tuple[T, ...]]:
    """Zip multiple iterables together, repeating the last seen value for missing timestamps.

    Args:
        iterables: The input iterables (each must be sorted by key).
        key (function): Function extracting the timestamp or index.
        fillvalue (Any): Default value to use when no prior value exists.

    Returns:
        Generator[Tuple[Any, ...]]: Yields tuples where missing values are filled
        with the last seen value.

    Examples:
        >>> seq1 = [(0, 'a'), (3, 'b'), (6, 'c')]
        >>> seq2 = [(1, 'x'), (4, 'y')]
        >>> seq3 = [(2, 'p'), (5, 'q'), (7, 'r')]
        >>> list(zip_repeat_last(seq1, seq2, seq3))
        [(0, 'a', None, None),
         (1, 'a', 'x', None),
         (2, 'a', 'x', 'p'),
         (3, 'b', 'x', 'p'),
         (4, 'b', 'y', 'p'),
         (5, 'b', 'y', 'q'),
         (6, 'c', 'y', 'q'),
         (7, 'c', 'y', 'r')]

        >>> seqA = [(2, 100), (4, 200)]
        >>> seqB = [(3, 'foo')]
        >>> list(zip_repeat_last(seqA, seqB, fillvalue=0))
        [(2, 100, 0),
         (3, 100, 'foo'),
         (4, 200, 'foo')]

    """
    iterators = [iter(it) for it in iterables]
    buffers = [next(it, None) for it in iterators]
    last_seen = [fillvalue] * len(iterables)

    for timestamp, *values in merge(*iterables, key=key):
        for i, (buffer, iterator) in enumerate(zip(buffers, iterators, strict=False)):
            if buffer is not None and key(buffer) == timestamp:
                last_seen[i] = buffer[1]
                buffers[i] = next(iterator, None)
        yield (timestamp, *last_seen)


def find_preferred(*iterables: " Iterable[T]", is_preferred: "Callable[[T, T], bool]") -> "list[T]":
    """Find preferred items across multiple iterables based on a predicate function.

    Args:
        *iterables: Any number of iterables containing comparable items.
        is_preferred: Function taking two items and returning True if the first is preferred over the second.

    Returns:
        A list of preferred items, where no other item in the input is strictly preferred over them.

    Example:
        >>> nums = ([1, 2], [2, 3], [3, 4])
        >>> find_preferred(*nums, is_preferred=lambda a, b: a > b)
        [4]

    """
    from itertools import chain

    all_items = list(chain.from_iterable(iterables))

    # Keep only elements that are NOT dominated by another
    return [x for x in all_items if not any(is_preferred(y, x) for y in all_items if y != x)]


def pop(iterable: Iterable[T], n: int, default: U = None) -> Iterable[T | U]:
    """Move the nth item of the *iterable* to the beginning and return the *iterable*.

    >>> iterable = [0, 1, 2, 3]
    >>> popped = pop(iterable, 2)
    >>> next(popped)
    2
    >>> list(popped)
    [0, 1, 3]
    """
    return chain[T | U](
        [nth(iterable, n) or default], islice_extended(iterable, n), islice_extended(iterable, n + 1, None),
    )


def pull_out(predicate: Callable[[Any], bool], iterable: Iterable[T]) -> Tuple[Iterable[T], Iterable[T]]:
    """Return a 2-tuple of items that satisfy and don't satisfy *predicate*.

    >>> iterable = range(10)
    >>> even = lambda x: x % 2 == 0
    >>> satisfied, unsatisfied = pull_out(even, iterable)
    >>> list(satisfied)
    [0, 2, 4, 6, 8]
    >>> list(unsatisfied)
    [1, 3, 5, 7, 9]

    >>> empty = ()
    >>> satisfied, unsatisfied = pull_out(even, empty)
    >>> list(satisfied)
    []
    >>> list(unsatisfied)
    []
    """
    satisfied, unsatisfied = tee((predicate(item), item) for item in iterable)
    return (item for pred, item in unsatisfied if pred), (item for pred, item in satisfied if not pred)


def pull_out_front(predicate: Callable[[T], bool], iterable: Iterable[T]) -> Tuple[T | None, Iterable[T]]:
    """Return a 2-tuple of the first item that satisfies *predicate* and the rest of the *iterable*.

    >>> iterable = range(10)
    >>> even = lambda x: x % 2 == 0
    >>> first, rest = pull_out_front(even, iterable)
    >>> first
    0
    >>> list(rest)
    [1, 2, 3, 4, 5, 6, 7, 8, 9]

    >>> empty = ()
    >>> first, rest = pull_out_front(even, empty)
    >>> list(rest)
    []
    >>> first, rest = pull_out_front(lambda x: x==4, range(10))
    >>> first
    4
    >>> list(rest)
    [0, 1, 2, 3, 5, 6, 7, 8, 9]
    """
    iterable = list(iterable)  # Convert to list to avoid iterator exhaustion
    for i, item in enumerate(iterable):
        if predicate(item):
            return item, chain(iterable[:i], iterable[i + 1 :])
    return None, iter([])


if __name__ == "__main__":
    import doctest

    doctest.testmod(optionflags=doctest.NORMALIZE_WHITESPACE)
