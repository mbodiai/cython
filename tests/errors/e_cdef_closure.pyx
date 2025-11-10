# mode: run

cpdef cpdef_closure(x):
    def inner():
        return x
    return inner

def test():
    """
    >>> f = cpdef_closure(7)
    >>> f()
    7
    """
    pass
