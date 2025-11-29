# cython: language_level=3

cdef test_cdef_kwonly(a, *, b, c=10):
    return (a, b, c)

cdef test_cdef_posonly(a, b, /, c):
    return (a, b, c)

cdef test_cdef_mixed(a, /, b, *, c):
    return (a, b, c)

def call_kwonly():
    """
    >>> call_kwonly()
    (1, 2, 10)
    """
    return test_cdef_kwonly(1, b=2)

def call_posonly():
    """
    >>> call_posonly()
    (1, 2, 3)
    """
    return test_cdef_posonly(1, 2, 3)

def call_mixed():
    """
    >>> call_mixed()
    (1, 2, 3)
    """
    return test_cdef_mixed(1, 2, c=3)
