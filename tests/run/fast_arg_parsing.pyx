# mode: run

def _raises_typeerror(func, *args, **kwargs):
    """
    Helper that reports whether calling ``func`` raises ``TypeError``.
    """
    try:
        func(*args, **kwargs)
    except TypeError:
        return True
    else:
        return False


def pos_and_kwonly(a, /, b, *, c, d=4):
    """
    >>> pos_and_kwonly(1, 2, c=3)
    (1, 2, 3, 4)
    >>> pos_and_kwonly(1, 2, c=3, d=5)
    (1, 2, 3, 5)
    >>> _raises_typeerror(pos_and_kwonly, a=1, b=2, c=3)
    True
    >>> _raises_typeerror(pos_and_kwonly, 1, 2)
    True
    """
    return a, b, c, d


def kw_only_defaults(*, x, y=5):
    """
    >>> kw_only_defaults(x=1)
    (1, 5)
    >>> kw_only_defaults(x=1, y=2)
    (1, 2)
    >>> _raises_typeerror(kw_only_defaults, y=2)
    True
    """
    return x, y


def pos_defaults(a, b=2):
    """
    >>> pos_defaults(1)
    (1, 2)
    >>> pos_defaults(1, 5)
    (1, 5)
    """
    return a, b


def forbid_extra(a, b):
    """
    >>> forbid_extra(1, 2)
    (1, 2)
    >>> _raises_typeerror(forbid_extra, 1, c=3)
    True
    """
    return a, b



