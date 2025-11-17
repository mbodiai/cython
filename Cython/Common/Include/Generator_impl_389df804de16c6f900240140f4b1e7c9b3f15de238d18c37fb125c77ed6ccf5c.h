static PyMethodDef __pyx_Generator_methods[] = {
    {"send", (PyCFunction) __Pyx_Coroutine_Send, METH_O,
     PyDoc_STR("send(arg) -> send 'arg' into generator,\nreturn next yielded value or raise StopIteration.")},
    {"throw", (PyCFunction) __Pyx_Coroutine_Throw, METH_VARARGS,
     PyDoc_STR("throw(typ[,val[,tb]]) -> raise exception in generator,\nreturn next yielded value or raise StopIteration.")},
    {"close", (PyCFunction) __Pyx_Coroutine_Close_Method, METH_NOARGS,
     PyDoc_STR("close() -> raise GeneratorExit inside generator.")},
    {"__reduce_ex__", (PyCFunction) __Pyx_Coroutine_fail_reduce_ex, METH_O, 0},
    {"__reduce__", (PyCFunction) __Pyx_Coroutine_fail_reduce_ex, METH_NOARGS, 0},
    {0, 0, 0, 0}
};
static PyMemberDef __pyx_Generator_memberlist[] = {
    {"gi_yieldfrom", T_OBJECT, offsetof(__pyx_CoroutineObject, yieldfrom), READONLY,
     PyDoc_STR("object being iterated by 'yield from', or None")},
    {"gi_code", T_OBJECT, offsetof(__pyx_CoroutineObject, gi_code), READONLY, NULL},
    {"__module__", T_OBJECT, offsetof(__pyx_CoroutineObject, gi_modulename), 0, 0},
#if PY_VERSION_HEX < 0x030C0000 || CYTHON_COMPILING_IN_LIMITED_API
    {"__weaklistoffset__", T_PYSSIZET, offsetof(__pyx_CoroutineObject, gi_weakreflist), READONLY, 0},
#endif
    {0, 0, 0, 0, 0}
};
static PyGetSetDef __pyx_Generator_getsets[] = {
    {"__name__", (getter)__Pyx_Coroutine_get_name, (setter)__Pyx_Coroutine_set_name,
     PyDoc_STR("name of the generator"), 0},
    {"__qualname__", (getter)__Pyx_Coroutine_get_qualname, (setter)__Pyx_Coroutine_set_qualname,
     PyDoc_STR("qualified name of the generator"), 0},
    {"gi_frame", (getter)__Pyx_Coroutine_get_frame, NULL,
     PyDoc_STR("Frame of the generator"), 0},
    {"gi_running", __Pyx_Coroutine_get_is_running_getter, NULL, NULL, NULL},
    {0, 0, 0, 0, 0}
};
static PyType_Slot __pyx_GeneratorType_slots[] = {
    {Py_tp_dealloc, (void *)__Pyx_Coroutine_dealloc},
    {Py_tp_traverse, (void *)__Pyx_Coroutine_traverse},
    {Py_tp_iter, (void *)PyObject_SelfIter},
    {Py_tp_iternext, (void *)__Pyx_Generator_Next},
    {Py_tp_methods, (void *)__pyx_Generator_methods},
    {Py_tp_members, (void *)__pyx_Generator_memberlist},
    {Py_tp_getset, (void *)__pyx_Generator_getsets},
    {Py_tp_getattro, (void *) PyObject_GenericGetAttr},
#if CYTHON_USE_TP_FINALIZE
    {Py_tp_finalize, (void *)__Pyx_Coroutine_del},
#endif
#if __PYX_HAS_PY_AM_SEND == 1
    {Py_am_send, (void *)__Pyx_Coroutine_AmSend},
#endif
    {0, 0},
};
static PyType_Spec __pyx_GeneratorType_spec = {
    __PYX_TYPE_MODULE_PREFIX "generator",
    sizeof(__pyx_CoroutineObject),
    0,
#if PY_VERSION_HEX >= 0x030C0000 && !CYTHON_COMPILING_IN_LIMITED_API
    Py_TPFLAGS_MANAGED_WEAKREF |
#endif
    Py_TPFLAGS_IMMUTABLETYPE | Py_TPFLAGS_DISALLOW_INSTANTIATION |
    Py_TPFLAGS_DEFAULT | Py_TPFLAGS_HAVE_GC | __Pyx_TPFLAGS_HAVE_AM_SEND,
    __pyx_GeneratorType_slots
};
#if __PYX_HAS_PY_AM_SEND == 2
static __Pyx_PyAsyncMethodsStruct __pyx_Generator_as_async;
#endif
static int __pyx_Generator_init(PyObject *module) {
    __pyx_mstatetype *mstate = __Pyx_PyModule_GetState(module);
    mstate->__pyx_GeneratorType = __Pyx_FetchCommonTypeFromSpec(
        mstate->__pyx_CommonTypesMetaclassType, module, &__pyx_GeneratorType_spec, NULL);
    if (unlikely(!mstate->__pyx_GeneratorType)) {
        return -1;
    }
#if __PYX_HAS_PY_AM_SEND == 2
    __Pyx_SetBackportTypeAmSend(mstate->__pyx_GeneratorType, &__pyx_Generator_as_async, &__Pyx_Coroutine_AmSend);
#endif
    return 0;
}
static PyObject *__Pyx_Generator_GetInlinedResult(PyObject *self) {
    __pyx_CoroutineObject *gen = (__pyx_CoroutineObject*) self;
    PyObject *retval = NULL;
    if (unlikely(__Pyx_Coroutine_test_and_set_is_running(gen))) {
        return __Pyx_Coroutine_AlreadyRunningError(gen);
    }
    __Pyx_PySendResult result = __Pyx_Coroutine_SendEx(gen, Py_None, &retval, 0);
    __Pyx_Coroutine_unset_is_running(gen);
    (void) result;
    assert (result == PYGEN_RETURN || result == PYGEN_ERROR);
    assert ((result == PYGEN_RETURN && retval != NULL) || (result == PYGEN_ERROR && retval == NULL));
    return retval;
}

