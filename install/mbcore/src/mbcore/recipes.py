"""Imported from the recipes section of the itertools documentation.

All functions taken from the recipes section of the itertools library docs
[1]_.
Some backward-compatible usability improvements have been made.

.. [1] http://docs.python.org/library/itertools.html#recipes

"""

import math
import operator
from collections import deque
from collections.abc import Container, Iterator, Sequence, Sized
from functools import lru_cache, partial
from itertools import (
    chain,
    combinations,
    compress,
    count,
    cycle,
    groupby,
    islice,
    product,
    repeat,
    starmap,
    tee,
    zip_longest,
)
from random import choice, randrange, sample
from sys import hexversion

from typing_extensions import (
    TYPE_CHECKING,
    Any,
    Callable,
    Generic,
    Iterable,
    Literal,
    Protocol,
    TypeVar,
    cast,
    overload,
)

__all__ = [
    "all_equal",
    "batched",
    "before_and_after",
    "consume",
    "convolve",
    "dotproduct",
    "first_true",
    "factor",
    "flatten",
    "grouper",
    "is_prime",
    "iter_except",
    "iter_index",
    "loops",
    "matmul",
    "ncycles",
    "nth",
    "nth_combination",
    "padnone",
    "pad_none",
    "pairwise",
    "partition",
    "polynomial_eval",
    "polynomial_from_roots",
    "polynomial_derivative",
    "powerset",
    "prepend",
    "quantify",
    "reshape",
    "random_combination_with_replacement",
    "random_combination",
    "random_permutation",
    "random_product",
    "repeatfunc",
    "roundrobin",
    "seekable",
    "SequenceView",
    "sieve",
    "sliding_window",
    "subslices",
    "sum_of_squares",
    "spy",
    "tabulate",
    "tail",
    "take",
    "totient",
    "transpose",
    "triplewise",
    "unique",
    "unique_everseen",
    "unique_justseen",
]

if TYPE_CHECKING:
    _marker = None
else:
    _marker = object()

T = TypeVar("T")
U = TypeVar("U")
_T = TypeVar("_T")
# zip with strict is available for Python 3.10+
try:
    zip(strict=True)
except TypeError:
    _zip_strict = zip
else:
    _zip_strict = partial(zip, strict=True)

# math.sumprod is available for Python 3.12+
_sumprod = getattr(math, "sumprod", lambda x, y: dotproduct(x, y))


def spy(iterable: "Iterable[_T]", n: int | None = 1) -> "tuple[_T | Iterable[_T], Iterator[_T]]":
    """Return a 2-tuple with a list containing the first *n* elements of
    *iterable*, and an iterator with the same items as *iterable*.
    This allows you to "look ahead" at the items in the iterable without
    advancing it.

    There is one item in the list by default:

        >>> iterable = 'abcdefg'
        >>> head, iterable = spy(iterable)
        >>> head
        ['a']
        >>> list(iterable)
        ['a', 'b', 'c', 'd', 'e', 'f', 'g']

    You may use unpacking to retrieve items instead of lists:

        >>> (head,), iterable = spy('abcdefg')
        >>> head
        'a'
        >>> (first, second), iterable = spy('abcdefg', 2)
        >>> first
        'a'
        >>> second
        'b'

    The number of items requested can be larger than the number of items in
    the iterable:

        >>> iterable = [1, 2, 3, 4, 5]
        >>> head, iterable = spy(iterable, 10)
        >>> head
        [1, 2, 3, 4, 5]
        >>> list(iterable)
        [1, 2, 3, 4, 5]

    """
    if n is None:
        p, q = tee_view(iterable)
        return p, q

    p, q = tee(iterable, 2)
    return take(n, p), q


def tee_view(iterable: Iterable[T], n: int = 2) -> "tuple[seekable[T], ...]":
    """Return *n* independent iterators from a single iterable.

    This is similar
    to the standard :func:`itertools.tee`, but the iterators returned are
    seekable. This means that you can use :meth:`seek` on the returned
    iterators to move them to a specific position in the source iterable.

        >>> t1, t2 = tee_view('abcdefg', 2)
        >>> next(t1)
        'a'
        >>> next(t1)
        'b'
        >>> next(t2)
        'a'
        >>> t= t1.seek(0)
        >>> next(t1)
        'a'

    """
    iters = tee(iterable, n)
    out = tuple(seekable(it) if not isinstance(it, seekable) else it for it in iters)
    (it.seek(0) for it in out)
    return out


def _ilen(iterable: Iterable[T], consume=False):
    def _ilen(seq):
        """Consumes an iterable not reading it into memory; return the number of items.

        NOTE: implementation borrowed from http://stackoverflow.com/a/15112059/753382
        """
        counter = count()
        deque(zip(seq, counter, strict=False), maxlen=0)  # (consume at C speed)
        return next(counter)

    if consume:
        return _ilen(iterable)
    # iterable.__iter__ = lambda x: seekable(iterable).seek(0).__iter__
    _cp, result = tee_view(iterable)

    out = _ilen(result)
    result.seek(0)
    _cp.seek(0)
    return out


def ilen_view(iterable: Iterable[T], consume=False) -> int:
    """Return the number of items in *iterable*.

    If *consume* is ``True``, the iterable will be fully exhausted.

        >>> ilen_view(range(10))
        10
        >>> ilen_view(range(10), consume=True)
        10

    """
    iterfunc = lambda x: seekable(x).seek(0).__iter__
    it, _ = tee_view(iterable)

    out = _ilen(iterable, consume=consume)

    it.seek(0)
    _.seek(0)
    return out


def ilen(iterable: Iterable[T], consume=True):
    def _ilen(seq):
        """Consumes an iterable not reading it into memory; return the number of items.

        NOTE: implementation borrowed from http://stackoverflow.com/a/15112059/753382
        """
        counter = count()
        deque(zip(seq, counter, strict=False), maxlen=0)  # (consume at C speed)
        return next(counter)

    if consume:
        return _ilen(iterable)
    # Delegate to ilen_view for non-consuming length calculation
    return ilen_view(iterable)


def _spy(iterable: Iterable, length: int | None = None) -> tuple[_T | Iterable[_T], Iterable[_T]]:
    if length is None:
        iterable, _ = tee_view(iterable)
    return spy(iterable, length)


def spy_view(iterable: Iterable[_T], length: int = 1) -> tuple[_T | Iterable[_T], Iterable[_T]]:
    return _spy(iterable, length)


class SequenceView(Sequence):
    """Return a read-only view of the sequence object *target*.

    :class:`SequenceView` objects are analogous to Python's built-in
    "dictionary view" types. They provide a dynamic view of a sequence's items,
    meaning that when the sequence updates, so does the view.

        >>> seq = ['0', '1', '2']
        >>> view = SequenceView(seq)
        >>> view
        SequenceView(['0', '1', '2'])
        >>> seq.append('3')
        >>> view
        SequenceView(['0', '1', '2', '3'])

    Sequence views support indexing, slicing, and length queries. They act
    like the underlying sequence, except they don't allow assignment:

        >>> view[1]
        '1'
        >>> view[1:-1]
        ['1', '2']
        >>> len(view)
        4

    Sequence views are useful as an alternative to copying, as they don't
    require (much) extra storage.

    """

    def __init__(self, target):
        if not isinstance(target, Sequence):
            raise TypeError
        self._target = target

    def __getitem__(self, index):
        return self._target[index]

    def __len__(self):
        return len(self._target)

    def __repr__(self):
        return f"{self.__class__.__name__}({self._target!r})"


class seekable(Iterator[_T], Generic[_T]):  # noqa
    """Wrap an iterator to allow for seeking backward and forward.

    This progressively caches the items in the source iterable so they can be
    re-visited.

    Call :meth:`seek` with an index to seek to that position in the source
    iterable.

    To "reset" an iterator, seek to ``0``:

        >>> from itertools import count
        >>> it = seekable((str(n) for n in count()))
        >>> next(it), next(it), next(it)
        ('0', '1', '2')
        >>> i = it.seek(0)
        >>> next(it), next(it), next(it)
        ('0', '1', '2')

    You can also seek forward:

        >>> it = seekable((str(n) for n in range(20)))
        >>> i = it.seek(10)
        >>> next(it)
        '10'
        >>> i = it.seek(20)  # Seeking past the end of the source isn't a problem
        >>> list(it)
        []
        >>> i = it.seek(0)  # Resetting works even after hitting the end
        >>> next(it)
        '0'

    Call :meth:`relative_seek` to seek relative to the source iterator's
    current position.

        >>> it = seekable((str(n) for n in range(20)))
        >>> next(it), next(it), next(it)
        ('0', '1', '2')
        >>> i = it.relative_seek(2)
        >>> next(it)
        '5'
        >>> i = it.relative_seek(-3)  # Source is at '6', we move back to '3'
        >>> next(it)
        '3'
        >>> i = it.relative_seek(-3)  # Source is at '4', we move back to '1'
        >>> next(it)
        '1'


    Call :meth:`peek` to look ahead one item without advancing the iterator:

        >>> it = seekable('1234')
        >>> it.peek()
        '1'
        >>> list(it)
        ['1', '2', '3', '4']
        >>> it.peek(default='empty')
        'empty'

    Before the iterator is at its end, calling :func:`bool` on it will return
    ``True``. After it will return ``False``:

        >>> it = seekable('5678')
        >>> bool(it)
        True
        >>> list(it)
        ['5', '6', '7', '8']
        >>> bool(it)
        False

    You may view the contents of the cache with the :meth:`elements` method.
    That returns a :class:`SequenceView`, a view that updates automatically:

        >>> it = seekable((str(n) for n in range(10)))
        >>> next(it), next(it), next(it)
        ('0', '1', '2')
        >>> elements = it.elements()
        >>> elements
        SequenceView(['0', '1', '2'])
        >>> next(it)
        '3'
        >>> elements
        SequenceView(['0', '1', '2', '3'])

    By default, the cache grows as the source iterable progresses, so beware of
    wrapping very large or infinite iterables. Supply *maxlen* to limit the
    size of the cache (this of course limits how far back you can seek).

        >>> from itertools import count
        >>> it = seekable((str(n) for n in count()), maxlen=2)
        >>> next(it), next(it), next(it), next(it)
        ('0', '1', '2', '3')
        >>> list(it.elements())
        ['2', '3']
        >>> i = it.seek(0)
        >>> next(it), next(it), next(it), next(it)
        ('2', '3', '4', '5')
        >>> next(it)
        '6'

    """

    def __init__(self, iterable, maxlen=None):
        self._original_iterable = iterable
        self._source = iter(iterable)
        if maxlen is None:
            self._cache = []
        else:
            self._cache = deque([], maxlen)
        self._index = None

    def __iter__(self):
        return self

    def __next__(self):
        if self._index is not None:
            try:
                item = self._cache[self._index]
            except IndexError:
                self._index = None
            else:
                self._index += 1
                return item

        item = next(self._source)
        self._cache.append(item)
        return item

    def __bool__(self):
        try:
            self.peek()
        except StopIteration:
            return False
        return True

    def peek(self, default=_marker):
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

    def elements(self):
        return SequenceView(self._cache)

    def seek(self, index):
        self._index = index
        remainder = index - len(self._cache)
        if remainder > 0:
            consume(self, remainder)
        return self

    def __len__(self):
        if self._index is not None:
            return len(self._cache) - self._index
        return len(self._cache)

    def relative_seek(self, count):
        if self._index is None:
            self._index = len(self._cache)

        self.seek(max(self._index + count, 0))

    def __getattr__(self, name):  # -> Any:
        if name in ("_source", "_cache", "_index", "_original_iterable", "elements", "seek", "relative_seek", "peek"):
            return super().__getattribute__(name)
        return getattr(self._original_iterable, name)

    def __setattr__(self, name: str, value: Any) -> None:
        if name in ("_source", "_cache", "_index", "_original_iterable", "elements", "seek", "relative_seek", "peek"):
            super().__setattr__(name, value)
        else:
            setattr(self._original_iterable, name, value)

    def __repr__(self):
        # Show only cached items and current index, avoid consuming _source
        # Use list() on the cache deque/list for representation
        cached_repr = repr(list(self._cache))
        # Check if source *might* have more items by trying to peek WITHOUT advancing the cache read index (_index)
        # This requires a careful check to not alter the iteration state unintentionally
        has_more = False
        current_internal_index = self._index  # Remember current read position in cache
        try:
            # Peek ahead from the *end* of the cache to see if the source has items
            # We need to access the raw _source iterator carefully
            # Let's simplify: just indicate if the cache doesn't contain everything potentially iterated
            # A truly reliable check is hard without potentially consuming.
            # We can check if the internal index is None (meaning cache hasn't been read from after potential source consumption)
            # or if _source is not None (though it might be an empty iterator)
            status = "..."  # Assume more unless proven otherwise by full consumption later
        except StopIteration:
            status = ""  # Source is definitely exhausted if peek fails (peek itself consumes)

        # Restore internal index in case peek modified it (it shouldn't in the fixed version)
        self._index = current_internal_index

        # Represent based on cache only
        return f"{self.__class__.__name__}(cache={cached_repr}{status}, index={self._index})"


def take(n: int, iterable: Iterable[T]) -> list[T]:
    """Return first *n* items of the iterable as a list.

        >>> take(3, range(10))
        [0, 1, 2]

    If there are fewer than *n* items in the iterable, all of them are
    returned.

        >>> take(10, range(3))
        [0, 1, 2]

    """
    if n is None or n < 0:
        return list(iterable)
    return list(islice(iterable, n))


def tabulate(function, start=0):
    """Return an iterator over the results of ``func(start)``,
    ``func(start + 1)``, ``func(start + 2)``...

    *func* should be a function that accepts one integer argument.

    If *start* is not specified it defaults to 0. It will be incremented each
    time the iterator is advanced.

        >>> square = lambda x: x ** 2
        >>> iterator = tabulate(square, -3)
        >>> take(4, iterator)
        [9, 4, 1, 0]

    """
    return map(function, count(start))


def tail(n, iterable: "Iterable[T]") -> "Iterable[T]":
    """Return an iterator over the last *n* items of *iterable*.

    >>> t = tail(3, 'ABCDEFG')
    >>> list(t)
    ['E', 'F', 'G']

    """
    # If the given iterable has a length, then we can use islice to get its
    # final elements. Note that if the iterable is not actually Iterable,
    # either islice or deque will throw a TypeError. This is why we don't
    # check if it is Iterable.
    if isinstance(iterable, Sized):
        yield from islice(iterable, max(0, len(iterable) - n), None)
    else:
        yield from iter(deque(iterable, maxlen=n))


def consume(iterator, n: int | None = None):
    """Advance *iterable* by *n* steps. If *n* is ``None``, consume it
    entirely.

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
    # Use functions that consume iterators at C speed.
    if n is None:
        # feed the entire iterator into a zero-length deque
        deque(iterator, maxlen=0)
    else:
        # advance to the empty slice starting at position n
        next(islice(iterator, n, n), None)


def nth(iterable: "Iterable[T]", n: int, default: U = None) -> T | U:
    """Returns the nth item or a default value.

    >>> l = range(10)
    >>> nth(l, 3)
    3
    >>> nth(l, 20, "zebra")
    'zebra'

    """
    return next(islice(iterable, n, None), default)


def all_equal(iterable: "Iterable[T]", key=None) -> bool:
    """Returns ``True`` if all the elements are equal to each other.

        >>> all_equal('aaaa')
        True
        >>> all_equal('aaab')
        False

    A function that accepts a single argument and returns a transformed version
    of each input item can be specified with *key*:

        >>> all_equal('AaaA', key=str.casefold)
        True
        >>> all_equal([1, 2, 3], key=lambda x: x < 10)
        True

    """
    iterator = groupby(iterable, key)
    for first in iterator:
        for second in iterator:
            return False
        return True
    return True


def quantify(iterable: "Iterable[T]", pred: "Callable[[Any],bool]" = bool):
    """Return the how many times the predicate is true.

    >>> quantify([True, False, True])
    2

    """
    return sum(map(pred, iterable))


def pad_none(iterable):
    """Returns the sequence of elements and then returns ``None`` indefinitely.

        >>> take(5, pad_none(range(3)))
        [0, 1, 2, None, None]

    Useful for emulating the behavior of the built-in :func:`map` function.

    See also :func:`padded`.

    """
    return chain(iterable, repeat(None))


padnone = pad_none


def ncycles(iterable: Iterable[T], n):
    """Returns the sequence elements *n* times

    >>> list(ncycles(["a", "b"], 3))
    ['a', 'b', 'a', 'b', 'a', 'b']

    """
    return chain.from_iterable(repeat(tuple(iterable), n))


def dotproduct(vec1, vec2):
    """Returns the dot product of the two iterables.

    >>> dotproduct([10, 10], [20, 20])
    400

    """
    return sum(map(operator.mul, vec1, vec2))


def flatten(listOfLists: Iterable[Iterable[T]]) -> Iterable[T]:
    """Return an iterator flattening one level of nesting in a list of lists.

        >>> list(flatten([[0, 1], [2, 3]]))
        [0, 1, 2, 3]

    See also :func:`collapse`, which can flatten multiple levels of nesting.

    """
    return chain.from_iterable(listOfLists)


def repeatfunc(func, times=None, *args):
    """Call *func* with *args* repeatedly, returning an iterable over the
    results.

    If *times* is specified, the iterable will terminate after that many
    repetitions:

        >>> from operator import add
        >>> times = 4
        >>> args = 3, 5
        >>> list(repeatfunc(add, times, *args))
        [8, 8, 8, 8]

    If *times* is ``None`` the iterable will not terminate:

        >>> from random import randrange
        >>> times = None
        >>> args = 1, 11
        >>> take(6, repeatfunc(randrange, times, *args))  # doctest:+SKIP
        [2, 4, 8, 1, 8, 4]

    """
    if times is None:
        return starmap(func, repeat(args))
    return starmap(func, repeat(args, times))


if TYPE_CHECKING:
    from typing_extensions import Self

    _T_co = TypeVar("_T_co", covariant=True)

    class Pairwise(Protocol[_T_co]):
        def __new__(cls, iterable: Iterable[_T], /) -> "Pairwise[tuple[_T, _T]]": ...
        def __iter__(self) -> Self: ...
        def __next__(self) -> _T_co: ...


def _pairwise(iterable: Iterable[T]) -> "zip[tuple[T, T]] | Pairwise[tuple[T, T]]":
    """Returns an iterator of paired items, overlapping, from the original.

    >>> take(4, pairwise(count()))
    [(0, 1), (1, 2), (2, 3), (3, 4)]

    On Python 3.10 and above, this is an alias for :func:`itertools.pairwise`.

    """
    a, b = tee(iterable)
    next(b, None)
    return zip(a, b, strict=False)


try:
    if not TYPE_CHECKING:
        from itertools import pairwise as itertools_pairwise

        def pairwise(iterable) -> "Pairwise[tuple[T, T]] | zip[tuple[T, T]]":
            return itertools_pairwise(iterable)
except ImportError:
    from mbcore.types import wraps

    pairwise = wraps(_pairwise)(_pairwise)


class UnequalIterablesError(ValueError):
    def __init__(self, details=None):
        msg = "Iterables have different lengths"
        if details is not None:
            msg += (": index 0 has length {}; index {} has length {}").format(
                *details,
            )

        super().__init__(msg)


def _zip_equal_generator(iterables: Iterable[Iterable[T | U | Any]]) -> Iterable[tuple[T | U | Any, ...]]:
    for combo in zip_longest(*iterables, fillvalue=_marker):
        for val in combo:
            if val is _marker:
                raise UnequalIterablesError()
        yield combo


def _zip_equal(*iterables: Iterable[T | U | Any]) -> Iterable[tuple[T | U | Any, ...]]:
    # Check whether the iterables are all the same size.
    try:
        first_size = ilen_view(iterables[0], consume=False)
        for i, it in enumerate(iterables[1:], 1):
            size = ilen_view(it, consume=False)
            if size != first_size:
                raise UnequalIterablesError(details=(first_size, i, size))
        # All sizes are equal, we can use the built-in zip.
        return zip(*iterables, strict=False)
    # If any one of the iterables didn't have a length, start reading
    # them until one runs out.
    except TypeError:
        return _zip_equal_generator(iterables)


def grouper(
    iterable: Iterable[T | U], n: int, incomplete: "Literal['fill','ignore','strict']" = "fill", fillvalue: U = None,
) -> Iterable[tuple[T | U, ...]]:
    """Group elements from *iterable* into fixed-length groups of length *n*.

    >>> list(grouper('ABCDEF', 3))
    [('A', 'B', 'C'), ('D', 'E', 'F')]

    The keyword arguments *incomplete* and *fillvalue* control what happens for
    iterables whose length is not a multiple of *n*.

    When *incomplete* is `'fill'`, the last group will contain instances of
    *fillvalue*.

    >>> list(grouper('ABCDEFG', 3, incomplete='fill', fillvalue='x'))
    [('A', 'B', 'C'), ('D', 'E', 'F'), ('G', 'x', 'x')]

    When *incomplete* is `'ignore'`, the last group will not be emitted.

    >>> list(grouper('ABCDEFG', 3, incomplete='ignore', fillvalue='x'))
    [('A', 'B', 'C'), ('D', 'E', 'F')]

    When *incomplete* is `'strict'`, a subclass of `ValueError` will be raised.

    >>> list(grouper('ABCDEFG', 3, incomplete='strict'))  # doctest: +IGNORE_EXCEPTION_DETAIL
    Traceback (most recent call last):
    ...
    UnequalIterablesError

    """
    args = [iter(iterable)] * n
    if incomplete == "fill":
        return zip_longest(*args, fillvalue=fillvalue)
    if incomplete == "strict":
        return _zip_equal(*args)
    if incomplete == "ignore":
        return zip(*args, strict=False)
    raise ValueError("Expected fill, strict, or ignore")


def roundrobin(*iterables: Iterable[T]) -> Iterable[T]:
    """Yields an item from each iterable, alternating between them.

        >>> list(roundrobin('ABC', 'D', 'EF'))
        ['A', 'D', 'E', 'B', 'F', 'C']

    This function produces the same output as :func:`interleave_longest`, but
    may perform better for some inputs (in particular when the number of
    iterables is small).

    """
    # Algorithm credited to George Sakkis
    iterators = map(iter, iterables)
    for num_active in range(len(iterables), 0, -1):
        iterators = cycle(islice(iterators, num_active))
        yield from map(next, iterators)


def partition(pred: Callable[[T], bool], iterable: Iterable[U | T]) -> tuple[Iterable[T], Iterable[U]]:
    """Returns a 2-tuple of iterables derived from the input iterable.
    The first yields the items that have ``pred(item) == False``.
    The second yields the items that have ``pred(item) == True``.

        >>> is_odd = lambda x: x % 2 != 0
        >>> iterable = range(10)
        >>> even_items, odd_items = partition(is_odd, iterable)
        >>> list(even_items), list(odd_items)
        ([0, 2, 4, 6, 8], [1, 3, 5, 7, 9])

    If *pred* is None, :func:`bool` is used.

        >>> iterable = [0, 1, False, True, '', ' ']
        >>> false_items, true_items = partition(None, iterable)
        >>> list(false_items), list(true_items)
        ([0, False, ''], [1, True, ' '])

    """
    if pred is None:
        pred = bool

    t1, t2, p = tee(iterable, 3)
    p1, p2 = tee(map(pred, p))
    return (compress(t1, map(operator.not_, p1)), compress(t2, p2))


def powerset(iterable: Iterable[T]) -> chain[Iterable[T]]:
    """Yields all possible subsets of the iterable.

        >>> list(powerset([1, 2, 3]))
        [(), (1,), (2,), (3,), (1, 2), (1, 3), (2, 3), (1, 2, 3)]

    :func:`powerset` will operate on iterables that aren't :class:`set`
    instances, so repeated elements in the input will produce repeated elements
    in the output.

        >>> seq = [1, 1, 0]
        >>> list(powerset(seq))
        [(), (1,), (1,), (0,), (1, 1), (1, 0), (1, 0), (1, 1, 0)]

    For a variant that efficiently yields actual :class:`set` instances, see
    :func:`powerset_of_sets`.
    """
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s) + 1))


def unique_everseen(iterable: Iterable[T], key=None) -> Iterable[T]:
    """Yield unique elements, preserving order.

        >>> list(unique_everseen('AAAABBBCCDAABBB'))
        ['A', 'B', 'C', 'D']
        >>> list(unique_everseen('ABBCcAD', str.lower))
        ['A', 'B', 'C', 'D']

    Sequences with a mix of hashable and unhashable items can be used.
    The function will be slower (i.e., `O(n^2)`) for unhashable items.

    Remember that ``list`` objects are unhashable - you can use the *key*
    parameter to transform the list to a tuple (which is hashable) to
    avoid a slowdown.

        >>> iterable = ([1, 2], [2, 3], [1, 2])
        >>> list(unique_everseen(iterable))  # Slow
        [[1, 2], [2, 3]]
        >>> list(unique_everseen(iterable, key=tuple))  # Faster
        [[1, 2], [2, 3]]

    Similarly, you may want to convert unhashable ``set`` objects with
    ``key=frozenset``. For ``dict`` objects,
    ``key=lambda x: frozenset(x.items())`` can be used.

    """
    seenset = set()
    seenset_add = seenset.add
    seenlist = []
    seenlist_add = seenlist.append
    use_key = key is not None

    for element in iterable:
        k = key(element) if use_key else element
        try:
            if k not in seenset:
                seenset_add(k)
                yield element
        except TypeError:
            if k not in seenlist:
                seenlist_add(k)
                yield element


def unique_justseen(iterable: Iterable[T], key=None) -> Iterable[T]:
    """Yield elements in order, ignoring serial duplicates.

    >>> list(unique_justseen('AAAABBBCCDAABBB'))
    ['A', 'B', 'C', 'D', 'A', 'B']
    >>> list(unique_justseen('ABBCcAD', str.lower))
    ['A', 'B', 'C', 'A', 'D']

    """
    if key is None:
        return map(operator.itemgetter(0), groupby(iterable))

    return map(next, map(operator.itemgetter(1), groupby(iterable, key)))


def unique(iterable: Iterable[T], key=None, reverse=False) -> Iterable[T]:
    """Yield unique elements in sorted order.

    >>> list(unique([[1, 2], [3, 4], [1, 2]]))
    [[1, 2], [3, 4]]

    *key* and *reverse* are passed to :func:`sorted`.

    >>> list(unique('ABBcCAD', str.casefold))
    ['A', 'B', 'c', 'D']
    >>> list(unique('ABBcCAD', str.casefold, reverse=True))
    ['D', 'c', 'B', 'A']

    The elements in *iterable* need not be hashable, but they must be
    comparable for sorting to work.
    """
    return unique_justseen(sorted(iterable, key=key, reverse=reverse), key=key)  # type: ignore


def iter_except(
    func: Callable[[], T], exception: "type[BaseException]", first: Callable[[], T] | None = None,
) -> Iterable[T]:
    """Yield results from a function repeatedly until an exception is raised.

    Converts a call-until-exception interface to an iterator interface.
    Like ``iter(func, sentinel)``, but uses an exception instead of a sentinel
    to end the loop.

        >>> l = [0, 1, 2]
        >>> list(iter_except(l.pop, IndexError))
        [2, 1, 0]

    Multiple exceptions can be specified as a stopping condition:

        >>> l = [1, 2, 3, '...', 4, 5, 6]
        >>> list(iter_except(lambda: 1 + l.pop(), (IndexError, TypeError)))
        [7, 6, 5]
        >>> list(iter_except(lambda: 1 + l.pop(), (IndexError, TypeError)))
        [4, 3, 2]
        >>> list(iter_except(lambda: 1 + l.pop(), (IndexError, TypeError)))
        []

    """
    try:
        if first is not None:
            yield first()
        while 1:
            yield func()
    except exception:
        pass


@overload
def first_true(
    iterable: Iterable[T], pred: Callable[[T], bool] | Container[T] | None = None, default: U = None,
) -> U | T: ...


@overload
def first_true(
    pred: Callable[[T], bool] | Container[T] | None = None, iterable: Iterable[T] | None = None, default: U = None,
) -> U | T: ...


def first_true(*args, **kwargs):
    """Return the first true value in the iterable.

    Args:
        iterable: The iterable to search through
        pred: Optional predicate function to test items
        default: Value to return if no true value is found

    Returns:
        First item where pred(item) is True, or default if none found

    """
    args = list(args)
    iterable = kwargs.pop("iterable", args.pop(0)) if len(args) > 0 else None
    pred = kwargs.pop("pred", args.pop(0)) if len(args) > 0 else None
    default = kwargs.pop("dev", args.pop(0)) if len(args) > 0 else None
    if iterable is None and pred is None:
        raise ValueError("iterable cannot be None in `first_true`")
    if not hasattr(iterable, "__iter__"):
        it, p = cast(Iterable, pred), cast(Callable[[Any], bool] | Container, iterable)
    else:
        it = cast(Iterable, iterable)
        p = pred
    if it is None:
        raise ValueError("iterable cannot be None in `first_true`")

    if p is None:
        predicate = bool
    elif isinstance(p, Container):
        predicate = p.__contains__
    else:
        predicate = p

    try:
        return next(filter(predicate, it), default)
    except TypeError as e:
        if "not callable" in str(e):
            # Handle case where iterable is actually the predicate
            if callable(it):
                return first_true(it, pred, default)
            raise
        raise


def random_product(*args, repeat=1):
    """Draw an item at random from each of the input iterables.

        >>> random_product('abc', range(4), 'XYZ')  # doctest:+SKIP
        ('c', 3, 'Z')

    If *repeat* is provided as a keyword argument, that many items will be
    drawn from each iterable.

        >>> random_product('abcd', range(4), repeat=2)  # doctest:+SKIP
        ('a', 2, 'd', 3)

    This equivalent to taking a random selection from
    ``itertools.product(*args, **kwarg)``.

    """
    pools = [tuple(pool) for pool in args] * repeat
    return tuple(choice(pool) for pool in pools)


def random_permutation(iterable: Iterable[T], r=None):
    """Return a random *r* length permutation of the elements in *iterable*.

    If *r* is not specified or is ``None``, then *r* defaults to the length of
    *iterable*.

        >>> random_permutation(range(5))  # doctest:+SKIP
        (3, 4, 0, 1, 2)

    This equivalent to taking a random selection from
    ``itertools.permutations(iterable, r)``.

    """
    pool = tuple(iterable)
    r = len(pool) if r is None else r
    return tuple(sample(pool, r))


def random_combination(iterable: Iterable[T], r):
    """Return a random *r* length subsequence of the elements in *iterable*.

        >>> random_combination(range(5), 3)  # doctest:+SKIP
        (2, 3, 4)

    This equivalent to taking a random selection from
    ``itertools.combinations(iterable, r)``.

    """
    pool = tuple(iterable)
    n = len(pool)
    indices = sorted(sample(range(n), r))
    return tuple(pool[i] for i in indices)


def random_combination_with_replacement(iterable: Iterable[T], r):
    """Return a random *r* length subsequence of elements in *iterable*,
    allowing individual elements to be repeated.

        >>> random_combination_with_replacement(range(3), 5) # doctest:+SKIP
        (0, 0, 1, 2, 2)

    This equivalent to taking a random selection from
    ``itertools.combinations_with_replacement(iterable, r)``.

    """
    pool = tuple(iterable)
    n = len(pool)
    indices = sorted(randrange(n) for i in range(r))
    return tuple(pool[i] for i in indices)


def nth_combination(iterable: Iterable[T], r, index):
    """Equivalent to ``list(combinations(iterable, r))[index]``.

    The subsequences of *iterable* that are of length *r* can be ordered
    lexicographically. :func:`nth_combination` computes the subsequence at
    sort position *index* directly, without computing the previous
    subsequences.

        >>> nth_combination(range(5), 3, 5)
        (0, 3, 4)

    ``ValueError`` will be raised If *r* is negative or greater than the length
    of *iterable*.
    ``IndexError`` will be raised if the given *index* is invalid.
    """
    pool = tuple(iterable)
    n = len(pool)
    if (r < 0) or (r > n):
        raise ValueError

    c = 1
    k = min(r, n - r)
    for i in range(1, k + 1):
        c = c * (n - k + i) // i

    if index < 0:
        index += c

    if (index < 0) or (index >= c):
        raise IndexError

    result = []
    while r:
        c, n, r = c * r // n, n - 1, r - 1
        while index >= c:
            index -= c
            c, n = c * (n - r) // n, n - 1
        result.append(pool[-1 - n])

    return tuple(result)


def prepend(value, iterator):
    """Yield *value*, followed by the elements in *iterator*.

        >>> value = '0'
        >>> iterator = ['1', '2', '3']
        >>> list(prepend(value, iterator))
        ['0', '1', '2', '3']

    To prepend multiple values, see :func:`itertools.chain`
    or :func:`value_chain`.

    """
    return chain([value], iterator)


def convolve(signal, kernel):
    """Convolve the iterable *signal* with the iterable *kernel*.

        >>> signal = (1, 2, 3, 4, 5)
        >>> kernel = [3, 2, 1]
        >>> list(convolve(signal, kernel))
        [3, 8, 14, 20, 26, 14, 5]

    Note: the input arguments are not interchangeable, as the *kernel*
    is immediately consumed and stored.

    """
    # This implementation intentionally doesn't match the one in the itertools
    # documentation.
    kernel = tuple(kernel)[::-1]
    n = len(kernel)
    window = deque([0], maxlen=n) * n
    for x in chain(signal, repeat(0, n - 1)):
        window.append(x)
        yield _sumprod(kernel, window)


def before_and_after(predicate, it):
    """A variant of :func:`takewhile` that allows complete access to the
    remainder of the iterator.

         >>> it = iter('ABCdEfGhI')
         >>> all_upper, remainder = before_and_after(str.isupper, it)
         >>> ''.join(all_upper)
         'ABC'
         >>> ''.join(remainder) # takewhile() would lose the 'd'
         'dEfGhI'

    Note that the first iterator must be fully consumed before the second
    iterator can generate valid results.
    """
    it = iter(it)
    transition = []

    def true_iterator():
        for elem in it:
            if predicate(elem):
                yield elem
            else:
                transition.append(elem)
                return

    # Note: this is different from itertools recipes to allow nesting
    # before_and_after remainders into before_and_after again. See tests
    # for an example.
    remainder_iterator = chain(transition, it)

    return true_iterator(), remainder_iterator


def triplewise(iterable):
    """Return overlapping triplets from *iterable*.

    >>> list(triplewise('ABCDE'))
    [('A', 'B', 'C'), ('B', 'C', 'D'), ('C', 'D', 'E')]

    """
    # This deviates from the itertools documentation reciple - see
    # https://github.com/more-itertools/more-itertools/issues/889
    t1, t2, t3 = tee(iterable, 3)
    next(t3, None)
    next(t3, None)
    next(t2, None)
    return zip(t1, t2, t3, strict=False)


def _sliding_window_islice(iterable: Iterable[T], n):
    # Fast path for small, non-zero values of n.
    iterators = tee(iterable, n)
    for i, iterator in enumerate(iterators):
        next(islice(iterator, i, i), None)
    return zip(*iterators, strict=False)


def _sliding_window_deque(iterable: Iterable[T], n):
    # Normal path for other values of n.
    it = iter(iterable)
    window = deque(islice(it, n - 1), maxlen=n)
    for x in it:
        window.append(x)
        yield tuple(window)


def sliding_window(iterable: Iterable[T], n):
    """Return a sliding window of width *n* over *iterable*.

        >>> list(sliding_window(range(6), 4))
        [(0, 1, 2, 3), (1, 2, 3, 4), (2, 3, 4, 5)]

    If *iterable* has fewer than *n* items, then nothing is yielded:

        >>> list(sliding_window(range(3), 4))
        []

    For a variant with more features, see :func:`windowed`.
    """
    if n > 20:
        return _sliding_window_deque(iterable, n)
    if n > 2:
        return _sliding_window_islice(iterable, n)
    if n == 2:
        return pairwise(iterable)
    if n == 1:
        return zip(iterable, strict=False)
    raise ValueError(f"n should be at least one, not {n}")


def subslices(iterable):
    """Return all contiguous non-empty subslices of *iterable*.

        >>> list(subslices('ABC'))
        [['A'], ['A', 'B'], ['A', 'B', 'C'], ['B'], ['B', 'C'], ['C']]

    This is similar to :func:`substrings`, but emits items in a different
    order.
    """
    seq = list(iterable)
    slices = starmap(slice, combinations(range(len(seq) + 1), 2))
    return map(operator.getitem, repeat(seq), slices)


def polynomial_from_roots(roots):
    """Compute a polynomial's coefficients from its roots.

    >>> roots = [5, -4, 3]  # (x - 5) * (x + 4) * (x - 3)
    >>> polynomial_from_roots(roots)  # x^3 - 4 * x^2 - 17 * x + 60
    [1, -4, -17, 60]
    """
    poly = [1]
    for root in roots:
        poly = list(convolve(poly, (1, -root)))
    return poly


def iter_index(iterable: Iterable[T], value, start=0, stop=None):
    """Yield the index of each place in *iterable* that *value* occurs,
    beginning with index *start* and ending before index *stop*.


    >>> list(iter_index('AABCADEAF', 'A'))
    [0, 1, 4, 7]
    >>> list(iter_index('AABCADEAF', 'A', 1))  # start index is inclusive
    [1, 4, 7]
    >>> list(iter_index('AABCADEAF', 'A', 1, 7))  # stop index is not inclusive
    [1, 4]

    The behavior for non-scalar *values* matches the built-in Python types.

    >>> list(iter_index('ABCDABCD', 'AB'))
    [0, 4]
    >>> list(iter_index([0, 1, 2, 3, 0, 1, 2, 3], [0, 1]))
    []
    >>> list(iter_index([[0, 1], [2, 3], [0, 1], [2, 3]], [0, 1]))
    [0, 2]

    See :func:`locate` for a more general means of finding the indexes
    associated with particular values.

    """
    seq_index = getattr(iterable, "index", None)
    if seq_index is None:
        # Slow path for general iterables
        it = islice(iterable, start, stop)
        for i, element in enumerate(it, start):
            if element is value or element == value:
                yield i
    else:
        # Fast path for sequences
        stop = len(cast(Sequence[T], iterable)) if stop is None else stop
        i = start - 1
        try:
            while True:
                yield (i := seq_index(value, i + 1, stop))
        except ValueError:
            pass


def sieve(n):
    """Yield the primes less than n.

    >>> list(sieve(30))
    [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
    """
    if n > 2:
        yield 2
    start = 3
    data = bytearray((0, 1)) * (n // 2)
    limit = math.isqrt(n) + 1
    for p in iter_index(data, 1, start, limit):
        yield from iter_index(data, 1, start, p * p)
        data[p * p : n : p + p] = bytes(len(range(p * p, n, p + p)))
        start = p * p
    yield from iter_index(data, 1, start)


def _batched(iterable: Iterable[T], n, *, strict=False):
    """Batch data into tuples of length *n*. If the number of items in
    *iterable* is not divisible by *n*:
    * The last batch will be shorter if *strict* is ``False``.
    * :exc:`ValueError` will be raised if *strict* is ``True``.

    >>> list(batched('ABCDEFG', 3))
    [('A', 'B', 'C'), ('D', 'E', 'F'), ('G',)]

    On Python 3.13 and above, this is an alias for :func:`itertools.batched`.
    """
    if n < 1:
        raise ValueError("n must be at least one")
    it = iter(iterable)
    while batch := tuple(islice(it, n)):
        if strict and len(batch) != n:
            raise ValueError("batched(): incomplete batch")
        yield batch


if hexversion >= 0x30D00A2:
    from itertools import batched as itertools_batched

    def batched(iterable: Iterable[T], n, *, strict=False):
        return itertools_batched(iterable, n, strict=strict)

else:
    batched = _batched

    batched.__doc__ = _batched.__doc__


def transpose(it):
    """Swap the rows and columns of the input matrix.

    >>> list(transpose([(1, 2, 3), (11, 22, 33)]))
    [(1, 11), (2, 22), (3, 33)]

    The caller should ensure that the dimensions of the input are compatible.
    If the input is empty, no output will be produced.
    """
    return _zip_strict(*it)


def reshape(matrix, cols):
    """Reshape the 2-D input *matrix* to have a column count given by *cols*.

    >>> matrix = [(0, 1), (2, 3), (4, 5)]
    >>> cols = 3
    >>> list(reshape(matrix, cols))
    [(0, 1, 2), (3, 4, 5)]
    """
    return batched(chain.from_iterable(matrix), cols)


def matmul(m1, m2):
    """Multiply two matrices.

    >>> list(matmul([(7, 5), (3, 5)], [(2, 5), (7, 9)]))
    [(49, 80), (41, 60)]

    The caller should ensure that the dimensions of the input matrices are
    compatible with each other.
    """
    n = len(m2[0])
    return batched(starmap(_sumprod, product(m1, transpose(m2))), n)


def _factor_pollard(n):
    # Return a factor of n using Pollard's rho algorithm
    gcd = math.gcd
    for b in range(1, n - 2):
        x = y = 2
        d = 1
        while d == 1:
            x = (x * x + b) % n
            y = (y * y + b) % n
            y = (y * y + b) % n
            d = gcd(x - y, n)
        if d != n:
            return d
    raise ValueError("prime or under 5")


_primes_below_211 = tuple(sieve(211))


def factor(n):
    """Yield the prime factors of n.

    >>> list(factor(360))
    [2, 2, 2, 3, 3, 5]

    Finds small factors with trial division.  Larger factors are
    either verified as prime with ``is_prime`` or split into
    smaller factors with Pollard's rho algorithm.
    """
    # Corner case reduction
    if n < 2:
        return

    # Trial division reduction
    for prime in _primes_below_211:
        while not n % prime:
            yield prime
            n //= prime

    # Pollard's rho reduction
    primes = []
    todo = [n] if n > 1 else []
    for n in todo:
        if n < 211**2 or is_prime(n):
            primes.append(n)
        else:
            fact = _factor_pollard(n)
            todo += (fact, n // fact)
    yield from sorted(primes)


def polynomial_eval(coefficients, x):
    """Evaluate a polynomial at a specific value.

    Example: evaluating x^3 - 4 * x^2 - 17 * x + 60 at x = 2.5:

    >>> coefficients = [1, -4, -17, 60]
    >>> x = 2.5
    >>> polynomial_eval(coefficients, x)
    8.125
    """
    n = len(coefficients)
    if n == 0:
        return x * 0  # coerce zero to the type of x
    powers = map(pow, repeat(x), reversed(range(n)))
    return _sumprod(coefficients, powers)


def sum_of_squares(it):
    """Return the sum of the squares of the input values.

    >>> sum_of_squares([10, 20, 30])
    1400
    """
    return _sumprod(*tee(it))


def polynomial_derivative(coefficients):
    """Compute the first derivative of a polynomial.

    Example: evaluating the derivative of x^3 - 4 * x^2 - 17 * x + 60

    >>> coefficients = [1, -4, -17, 60]
    >>> derivative_coefficients = polynomial_derivative(coefficients)
    >>> derivative_coefficients
    [3, -8, -17]
    """
    n = len(coefficients)
    powers = reversed(range(1, n))
    return list(map(operator.mul, coefficients, powers))


def totient(n):
    """Return the count of natural numbers up to *n* that are coprime with *n*.

    >>> totient(9)
    6
    >>> totient(12)
    4
    """
    for prime in set(factor(n)):
        n -= n // prime
    return n


# Miller–Rabin primality test: https://oeis.org/A014233
_perfect_tests = [
    (2047, (2,)),
    (9080191, (31, 73)),
    (4759123141, (2, 7, 61)),
    (1122004669633, (2, 13, 23, 1662803)),
    (2152302898747, (2, 3, 5, 7, 11)),
    (3474749660383, (2, 3, 5, 7, 11, 13)),
    (18446744073709551616, (2, 325, 9375, 28178, 450775, 9780504, 1795265022)),
    (
        3317044064679887385961981,
        (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41),
    ),
]


@lru_cache
def _shift_to_odd(n):
    """Return s, d such that 2**s * d == n"""
    s = ((n - 1) ^ n).bit_length() - 1
    d = n >> s
    assert (1 << s) * d == n and d & 1 and s >= 0
    return s, d


def _strong_probable_prime(n, base):
    assert (n > 2) and (n & 1) and (2 <= base < n)

    s, d = _shift_to_odd(n - 1)

    x = pow(base, d, n)
    if x == 1 or x == n - 1:
        return True

    for _ in range(s - 1):
        x = x * x % n
        if x == n - 1:
            return True

    return False


def is_prime(n):
    """Return ``True`` if *n* is prime and ``False`` otherwise.

    >>> is_prime(37)
    True
    >>> is_prime(3 * 13)
    False
    >>> is_prime(18_446_744_073_709_551_557)
    True

    This function uses the Miller-Rabin primality test, which can return false
    positives for very large inputs. For values of *n* below 10**24
    there are no false positives. For larger values, there is less than
    a 1 in 2**128 false positive rate. Multiple tests can further reduce the
    chance of a false positive.
    """
    if n < 17:
        return n in {2, 3, 5, 7, 11, 13}
    if not (n & 1 and n % 3 and n % 5 and n % 7 and n % 11 and n % 13):
        return False
    for limit, bases in _perfect_tests:
        if n < limit:
            break
    else:
        bases = [randrange(2, n - 1) for i in range(64)]
    return all(_strong_probable_prime(n, base) for base in bases)


def loops(n):
    """Returns an iterable with *n* elements for efficient looping.
    Like ``range(n)`` but doesn't create integers.

    >>> i = 0
    >>> for _ in loops(5):
    ...     i += 1
    >>> i
    5

    """
    return repeat(None, n)


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
