static void __Pyx_Generator_Replace_StopIteration(int in_async_gen) {
    PyObject *exc, *val, *tb, *cur_exc, *new_exc;
    __Pyx_PyThreadState_declare
    int is_async_stopiteration = 0;
    CYTHON_MAYBE_UNUSED_VAR(in_async_gen);
    __Pyx_PyThreadState_assign
    cur_exc = __Pyx_PyErr_CurrentExceptionType();
    if (likely(!__Pyx_PyErr_GivenExceptionMatches(cur_exc, PyExc_StopIteration))) {
        if (in_async_gen && unlikely(__Pyx_PyErr_GivenExceptionMatches(cur_exc, PyExc_StopAsyncIteration))) {
            is_async_stopiteration = 1;
        } else {
            return;
        }
    }
    __Pyx_GetException(&exc, &val, &tb);
    Py_XDECREF(exc);
    Py_XDECREF(tb);
    new_exc = PyObject_CallFunction(PyExc_RuntimeError, "s",
        is_async_stopiteration ? "async generator raised StopAsyncIteration" :
        in_async_gen ? "async generator raised StopIteration" :
        "generator raised StopIteration");
    if (!new_exc) {
        Py_XDECREF(val);
        return;
    }
    PyException_SetCause(new_exc, val); // steals ref to val
    PyErr_SetObject(PyExc_RuntimeError, new_exc);
}

