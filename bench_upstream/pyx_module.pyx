# cython: language_level=3

cpdef int pyx_cpdef(int x):
    return x + 1

cdef int _pyx_cdef_impl(int x):
    return x + 1

def pyx_cdef_wrapper(int x):
    return _pyx_cdef_impl(x)
