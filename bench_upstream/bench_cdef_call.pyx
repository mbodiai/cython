# cython: language_level=3

cdef int _cdef_impl(int x):
    return x + 1

cpdef run_cdef_loop(int n):
    cdef int i, res = 0
    for i in range(n):
        res = _cdef_impl(1)
    return res
