# cython: language_level=3
import cython


cpdef make_cpdef_closure(x):
    def inner(y):
        return x + y
    return inner


@cython.ccall
def make_ccall_closure(x):
    def inner(y):
        return x * y
    return inner


@cython.cfunc
def make_cfunc_closure(x):
    def inner(y):
        return (x, y)
    return inner


def test_run():
    f = make_cpdef_closure(2)
    g = make_ccall_closure(3)
    h = make_cfunc_closure(4)
    assert f(5) == 7
    assert g(6) == 18
    assert h(7) == (4, 7)
    return "ok"
