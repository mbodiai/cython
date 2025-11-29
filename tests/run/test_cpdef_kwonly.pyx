# cython: language_level=3

cpdef test_cpdef_kwonly(a, *, b, c=10):
    """
    >>> test_cpdef_kwonly(1, b=2)
    (1, 2, 10)
    >>> test_cpdef_kwonly(1, b=2, c=3)
    (1, 2, 3)
    >>> test_cpdef_kwonly(1, 2, 3)  # doctest: +ELLIPSIS
    Traceback (most recent call last):
    TypeError: ...
    """
    return (a, b, c)

cpdef test_cpdef_posonly(a, b, /, c):
    """
    >>> test_cpdef_posonly(1, 2, 3)
    (1, 2, 3)
    >>> test_cpdef_posonly(1, 2, c=3)
    (1, 2, 3)
    >>> test_cpdef_posonly(a=1, b=2, c=3)  # doctest: +ELLIPSIS
    Traceback (most recent call last):
    TypeError: ...positional...
    """
    return (a, b, c)

cpdef test_cpdef_mixed(a, /, b, *, c):
    """
    >>> test_cpdef_mixed(1, 2, c=3)
    (1, 2, 3)
    >>> test_cpdef_mixed(1, b=2, c=3)
    (1, 2, 3)
    >>> test_cpdef_mixed(a=1, b=2, c=3)  # doctest: +ELLIPSIS
    Traceback (most recent call last):
    TypeError: ...positional...
    >>> test_cpdef_mixed(1, 2, 3)  # doctest: +ELLIPSIS
    Traceback (most recent call last):
    TypeError: ...
    """
    return (a, b, c)

cpdef test_cpdef_kwonly_default(a, *, b=5, c=10):
    """
    >>> test_cpdef_kwonly_default(1)
    (1, 5, 10)
    >>> test_cpdef_kwonly_default(1, b=2)
    (1, 2, 10)
    >>> test_cpdef_kwonly_default(1, c=3)
    (1, 5, 3)
    >>> test_cpdef_kwonly_default(1, b=2, c=3)
    (1, 2, 3)
    """
    return (a, b, c)

cpdef test_cpdef_posonly_default(a, b=5, /, c=10):
    """
    >>> test_cpdef_posonly_default(1)
    (1, 5, 10)
    >>> test_cpdef_posonly_default(1, 2)
    (1, 2, 10)
    >>> test_cpdef_posonly_default(1, 2, 3)
    (1, 2, 3)
    >>> test_cpdef_posonly_default(1, 2, c=3)
    (1, 2, 3)
    """
    return (a, b, c)

# Test with typed arguments
cpdef test_cpdef_typed_kwonly(int a, *, int b, int c=10):
    """
    >>> test_cpdef_typed_kwonly(1, b=2)
    (1, 2, 10)
    >>> test_cpdef_typed_kwonly(1, b=2, c=3)
    (1, 2, 3)
    """
    return (a, b, c)

cpdef test_cpdef_typed_posonly(int a, int b, /, int c):
    """
    >>> test_cpdef_typed_posonly(1, 2, 3)
    (1, 2, 3)
    >>> test_cpdef_typed_posonly(1, 2, c=3)
    (1, 2, 3)
    """
    return (a, b, c)
