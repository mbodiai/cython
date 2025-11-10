static long __Pyx__PyObject_Ord(PyObject* c) {
    Py_ssize_t size;
    if (PyBytes_Check(c)) {
        size = __Pyx_PyBytes_GET_SIZE(c);
        if (likely(size == 1)) {
#if CYTHON_ASSUME_SAFE_MACROS
            return (unsigned char) PyBytes_AS_STRING(c)[0];
#else
            char *data = PyBytes_AsString(c);
            if (unlikely(!data)) return -1;
            return (unsigned char) data[0];
#endif
        }
#if !CYTHON_ASSUME_SAFE_SIZE
        else if (unlikely(size < 0)) return -1;
#endif
    } else if (PyByteArray_Check(c)) {
        size = __Pyx_PyByteArray_GET_SIZE(c);
        if (likely(size == 1)) {
#if CYTHON_ASSUME_SAFE_MACROS
            return (unsigned char) PyByteArray_AS_STRING(c)[0];
#else
            char *data = PyByteArray_AsString(c);
            if (unlikely(!data)) return -1;
            return (unsigned char) data[0];
#endif
        }
#if !CYTHON_ASSUME_SAFE_SIZE
        else if (unlikely(size < 0)) return -1;
#endif
    } else {
        __Pyx_TypeName c_type_name = __Pyx_PyType_GetFullyQualifiedName(Py_TYPE(c));
        PyErr_Format(PyExc_TypeError,
            "ord() expected string of length 1, but " __Pyx_FMT_TYPENAME " found",
            c_type_name);
        __Pyx_DECREF_TypeName(c_type_name);
        return (long)(Py_UCS4)-1;
    }
    PyErr_Format(PyExc_TypeError,
        "ord() expected a character, but string of length %zd found", size);
    return (long)(Py_UCS4)-1;
}

