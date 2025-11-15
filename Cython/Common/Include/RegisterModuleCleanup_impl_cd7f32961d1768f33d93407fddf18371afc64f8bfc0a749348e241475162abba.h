#if CYTHON_COMPILING_IN_PYPY
static PyObject* __pyx_module_cleanup_atexit(PyObject *module, PyObject *unused) {
    CYTHON_UNUSED_VAR(unused);
    __pyx_module_cleanup(module);
    Py_INCREF(Py_None); return Py_None;
}
static int __Pyx_RegisterCleanup(void) {
    static PyMethodDef cleanup_def = {
        "__cleanup", (PyCFunction)__pyx_module_cleanup_atexit, METH_NOARGS, 0};
    PyObject *cleanup_func = 0;
    PyObject *atexit = 0;
    PyObject *reg = 0;
    PyObject *args = 0;
    PyObject *res = 0;
    int ret = -1;
    cleanup_func = PyCFunction_New(&cleanup_def, 0);
    if (!cleanup_func)
        goto bad;
    atexit = PyImport_ImportModule("atexit");
    if (!atexit)
        goto bad;
    reg = PyObject_GetAttrString(atexit, "_exithandlers");
    if (reg && PyList_Check(reg)) {
        PyObject *a, *kw;
        a = PyTuple_New(0);
        kw = PyDict_New();
        if (!a || !kw) {
            Py_XDECREF(a);
            Py_XDECREF(kw);
            goto bad;
        }
        args = PyTuple_Pack(3, cleanup_func, a, kw);
        Py_DECREF(a);
        Py_DECREF(kw);
        if (!args)
            goto bad;
        ret = PyList_Insert(reg, 0, args);
    } else {
        if (!reg)
            PyErr_Clear();
        Py_XDECREF(reg);
        reg = PyObject_GetAttrString(atexit, "register");
        if (!reg)
            goto bad;
        args = PyTuple_Pack(1, cleanup_func);
        if (!args)
            goto bad;
        res = PyObject_CallObject(reg, args);
        if (!res)
            goto bad;
        ret = 0;
    }
bad:
    Py_XDECREF(cleanup_func);
    Py_XDECREF(atexit);
    Py_XDECREF(reg);
    Py_XDECREF(args);
    Py_XDECREF(res);
    return ret;
}
#endif

