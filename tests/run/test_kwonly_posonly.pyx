# cython: language_level=3

def test_posonly(a, b, /, c):
    """
    >>> test_posonly(1, 2, 3)
    (1, 2, 3)
    >>> test_posonly(1, 2, c=3)
    (1, 2, 3)
    >>> test_posonly(a=1, b=2, c=3)  # doctest: +ELLIPSIS
    Traceback (most recent call last):
    TypeError: ...positional...
    """
    return (a, b, c)

def test_kwonly(a, *, b, c):
    """
    >>> test_kwonly(1, b=2, c=3)
    (1, 2, 3)
    >>> test_kwonly(1, 2, 3)  # doctest: +ELLIPSIS
    Traceback (most recent call last):
    TypeError: ...
    """
    return (a, b, c)

def test_mixed(a, /, b, *, c):
    """
    >>> test_mixed(1, 2, c=3)
    (1, 2, 3)
    >>> test_mixed(1, b=2, c=3)
    (1, 2, 3)
    >>> test_mixed(a=1, b=2, c=3)  # doctest: +ELLIPSIS
    Traceback (most recent call last):
    TypeError: ...positional...
    >>> test_mixed(1, 2, 3)  # doctest: +ELLIPSIS
    Traceback (most recent call last):
    TypeError: ...
    """
    return (a, b, c)

def test_kwonly_with_default(a, *, b, c=10):
    """
    >>> test_kwonly_with_default(1, b=2)
    (1, 2, 10)
    >>> test_kwonly_with_default(1, b=2, c=3)
    (1, 2, 3)
    >>> test_kwonly_with_default(1)  # doctest: +ELLIPSIS
    Traceback (most recent call last):
    TypeError: ...keyword...b...
    """
    return (a, b, c)

def test_posonly_with_default(a, b=5, /, c=10):
    """
    >>> test_posonly_with_default(1)
    (1, 5, 10)
    >>> test_posonly_with_default(1, 2)
    (1, 2, 10)
    >>> test_posonly_with_default(1, 2, 3)
    (1, 2, 3)
    >>> test_posonly_with_default(1, 2, c=3)
    (1, 2, 3)
    """
    return (a, b, c)

def test_only_kwonly(*, a, b):
    """
    >>> test_only_kwonly(a=1, b=2)
    (1, 2)
    >>> test_only_kwonly(1, 2)  # doctest: +ELLIPSIS
    Traceback (most recent call last):
    TypeError: ...positional...
    """
    return (a, b)

def test_only_posonly(a, b, /):
    """
    >>> test_only_posonly(1, 2)
    (1, 2)
    >>> test_only_posonly(a=1, b=2)  # doctest: +ELLIPSIS
    Traceback (most recent call last):
    TypeError: ...positional...
    """
    return (a, b)
