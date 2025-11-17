#if CYTHON_USE_TYPE_SLOTS
static void __Pyx_PyIter_CheckErrorAndDecref(PyObject *source) {
    __Pyx_TypeName source_type_name = __Pyx_PyType_GetFullyQualifiedName(Py_TYPE(source));
    PyErr_Format(PyExc_TypeError,
        "iter() returned non-iterator of type '" __Pyx_FMT_TYPENAME "'", source_type_name);
    __Pyx_DECREF_TypeName(source_type_name);
    Py_DECREF(source);
}
#endif
static CYTHON_INLINE __Pyx_PySendResult __Pyx_Generator_Yield_From(__pyx_CoroutineObject *gen, PyObject *source, PyObject **retval) {
    PyObject *source_gen;
    __Pyx_PySendResult result;
#ifdef __Pyx_Coroutine_USED
    if (__Pyx_Coroutine_Check(source)) {
        Py_INCREF(source);
        source_gen = source;
        result = __Pyx_Coroutine_AmSend(source, Py_None, retval);
    } else
#endif
    {
#if CYTHON_USE_TYPE_SLOTS
        if (likely(Py_TYPE(source)->tp_iter)) {
            source_gen = Py_TYPE(source)->tp_iter(source);
            if (unlikely(!source_gen)) {
                *retval = NULL;
                return PYGEN_ERROR;
            }
            if (unlikely(!PyIter_Check(source_gen))) {
                __Pyx_PyIter_CheckErrorAndDecref(source_gen);
                *retval = NULL;
                return PYGEN_ERROR;
            }
        } else
#endif
        {
            source_gen = PyObject_GetIter(source);
            if (unlikely(!source_gen)) {
                *retval = NULL;
                return PYGEN_ERROR;
            }
        }
        *retval = __Pyx_PyIter_Next_Plain(source_gen);
        result = __Pyx_Coroutine_status_from_result(retval);
    }
    if (likely(result == PYGEN_NEXT)) {
        __Pyx_Coroutine_Set_Owned_Yield_From(gen, source_gen);
        return PYGEN_NEXT;
    }
    Py_DECREF(source_gen);
    return result;
}

