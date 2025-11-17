static PyObject *__Pyx_PyIter_Next2Default(PyObject* defval) {
    PyObject* exc_type;
    __Pyx_PyThreadState_declare
    __Pyx_PyThreadState_assign
    exc_type = __Pyx_PyErr_CurrentExceptionType();
    if (unlikely(exc_type)) {
        if (!defval || unlikely(!__Pyx_PyErr_GivenExceptionMatches(exc_type, PyExc_StopIteration)))
            return NULL;
        __Pyx_PyErr_Clear();
        Py_INCREF(defval);
        return defval;
    }
    if (defval) {
        Py_INCREF(defval);
        return defval;
    }
    __Pyx_PyErr_SetNone(PyExc_StopIteration);
    return NULL;
}
static void __Pyx_PyIter_Next_ErrorNoIterator(PyObject *iterator) {
    __Pyx_TypeName iterator_type_name = __Pyx_PyType_GetFullyQualifiedName(Py_TYPE(iterator));
    PyErr_Format(PyExc_TypeError,
        __Pyx_FMT_TYPENAME " object is not an iterator", iterator_type_name);
    __Pyx_DECREF_TypeName(iterator_type_name);
}
static CYTHON_INLINE PyObject *__Pyx_PyIter_Next2(PyObject* iterator, PyObject* defval) {
    PyObject* next;
#if !CYTHON_COMPILING_IN_LIMITED_API
    iternextfunc iternext = __Pyx_PyObject_TryGetSlot(iterator, tp_iternext, iternextfunc);
    if (likely(iternext)) {
        next = iternext(iterator);
        if (likely(next))
            return next;
    #if CYTHON_COMPILING_IN_CPYTHON && PY_VERSION_HEX < 0x030d0000
        if (unlikely(iternext == &_PyObject_NextNotImplemented))
            return NULL;
    #endif
    } else if (CYTHON_USE_TYPE_SLOTS) {
        __Pyx_PyIter_Next_ErrorNoIterator(iterator);
        return NULL;
    } else
#endif
    if (unlikely(!PyIter_Check(iterator))) {
        __Pyx_PyIter_Next_ErrorNoIterator(iterator);
        return NULL;
    } else {
        next = defval ? PyIter_Next(iterator) : __Pyx_PyIter_Next_Plain(iterator);
        if (likely(next))
            return next;
    }
    return __Pyx_PyIter_Next2Default(defval);
}

