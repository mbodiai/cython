static void __Pyx__ReturnWithStopIteration(PyObject* value, int async);
static CYTHON_INLINE void __Pyx_ReturnWithStopIteration(PyObject* value, int async, int iternext) {
    if (value == Py_None) {
        if (async || !iternext)
            PyErr_SetNone(async ? PyExc_StopAsyncIteration : PyExc_StopIteration);
        return;
    }
    __Pyx__ReturnWithStopIteration(value, async);
}
static void __Pyx__ReturnWithStopIteration(PyObject* value, int async) {
#if CYTHON_COMPILING_IN_CPYTHON
    __Pyx_PyThreadState_declare
#endif
    PyObject *exc;
    PyObject *exc_type = async ? PyExc_StopAsyncIteration : PyExc_StopIteration;
#if CYTHON_COMPILING_IN_CPYTHON
    if ((PY_VERSION_HEX >= (0x030C00A6)) || unlikely(PyTuple_Check(value) || PyExceptionInstance_Check(value))) {
        if (PY_VERSION_HEX >= (0x030e00A1)) {
            exc = __Pyx_PyObject_CallOneArg(exc_type, value);
        } else {
            PyObject *args_tuple = PyTuple_New(1);
            if (unlikely(!args_tuple)) return;
            Py_INCREF(value);
            PyTuple_SET_ITEM(args_tuple, 0, value);
            exc = PyObject_Call(exc_type, args_tuple, NULL);
            Py_DECREF(args_tuple);
        }
        if (unlikely(!exc)) return;
    } else {
        Py_INCREF(value);
        exc = value;
    }
    #if CYTHON_FAST_THREAD_STATE
    __Pyx_PyThreadState_assign
    #if CYTHON_USE_EXC_INFO_STACK
    if (!__pyx_tstate->exc_info->exc_value)
    #else
    if (!__pyx_tstate->exc_type)
    #endif
    {
        Py_INCREF(exc_type);
        __Pyx_ErrRestore(exc_type, exc, NULL);
        return;
    }
    #endif
#else
    exc = __Pyx_PyObject_CallOneArg(exc_type, value);
    if (unlikely(!exc)) return;
#endif
    PyErr_SetObject(exc_type, exc);
    Py_DECREF(exc);
}

