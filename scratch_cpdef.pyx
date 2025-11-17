cpdef double dot(double[:] a, double[:] b):
    cdef Py_ssize_t i, n = a.shape[0]
    cdef double acc = 0
    for i in range(n):
        acc += a[i] * b[i]
    return acc
