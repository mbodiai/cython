# 7.17 Common definitions <stddef.h>

cdef extern from "<stddef.h>":

    ctypedef signed int ptrdiff_t

    ctypedef unsigned int size_t

    ctypedef int wchar_t

    # CPython defines Py_ssize_t in pyport.h; expose here for static analyzers
    ctypedef signed long Py_ssize_t
