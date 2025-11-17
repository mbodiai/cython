#! mode: run
#! tag: closures

ctypedef object (*cfuncptr_t)(object)
cdef object call_cfuncptr(cfuncptr_t f):
    def wrap(s):
        return f(s)
    return wrap("X")


cdef object cf(object s):
    return "ok-" + s


def test_cfuncptr_closure_param():
    """
    >>> test_cfuncptr_closure_param()
    'ok-X'
    """
    return call_cfuncptr(cf)


