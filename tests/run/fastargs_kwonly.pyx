# mode: run
# tag: fastargs, kwargs, cyfunction
# cython: optimize.fast_arg_fallback=False
# cython: binding=True

cimport cython


@cython.cfunc
@cython.inline
def _check_raises(func, args, kwargs, exc_type):
    try:
        func(*args, **kwargs)
    except exc_type:
        return True
    else:
        return False


def fastargs_positional(a, b, c):
    """
    >>> fastargs_positional(1, 2, 3)
    (1, 2, 3)
    >>> _check_raises(fastargs_positional, (), {}, TypeError)
    True
    >>> _check_raises(fastargs_positional, (1,), {}, TypeError)
    True
    >>> _check_raises(fastargs_positional, (1, 2, 3, 4), {}, TypeError)
    True
    """
    return a, b, c


def fastargs_kwonly(*, a, b):
    """
    >>> fastargs_kwonly(a=1, b=2)
    (1, 2)
    >>> _check_raises(fastargs_kwonly, (1, 2), {}, TypeError)  # unexpected kwargs / no kwargs
    True
    >>> _check_raises(fastargs_kwonly, (), {"a": 1}, TypeError)  # missing required kw-only
    True
    """
    return a, b


def fastargs_mixed(a, *, b, c=0):
    """
    >>> fastargs_mixed(1, b=2)
    (1, 2, 0)
    >>> fastargs_mixed(1, b=2, c=3)
    (1, 2, 3)
    >>> _check_raises(fastargs_mixed, (), {"b": 2}, TypeError)  # missing positional
    True
    >>> _check_raises(fastargs_mixed, (1,), {}, TypeError)  # missing required kw-only
    True
    >>> _check_raises(fastargs_mixed, (1,), {"b": 2, "d": 4}, TypeError)  # unexpected kw
    True
    """
    return a, b, c


