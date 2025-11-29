//////////////////// DispatchProbe.proto ////////////////////

typedef int (*__Pyx_Dispatcher_t)(
    const char* qualified_name,
    PyObject *self,
    PyObject *const *args,
    Py_ssize_t nargs,
    PyObject *kwnames,
    PyObject **p_result
);

static __Pyx_Dispatcher_t __Pyx__global_c_dispatcher = NULL;

/*
 * Prototype for an optional, externally provided fast dispatcher.
 * Return values:
 *  - 0  => not handled, continue with normal argument parsing
 *  - >0 => handled, *p_result set (success)
 *  - <0 => error, Python exception set
 */
static CYTHON_INLINE int __Pyx_Dispatch_Probe(
    const char* qualified_name,
    PyObject *self,
    PyObject *const *args,
    Py_ssize_t nargs,
    PyObject *kwnames,
    PyObject **p_result
); /*proto*/

static CYTHON_INLINE int __Pyx_SetCDispatcherFromCapsule(PyObject *capsule); /*proto*/
static CYTHON_INLINE void __Pyx_TrySetupCDispatcher(void); /*proto*/

//////////////////// DispatchProbe ////////////////////

static CYTHON_INLINE int __Pyx_Dispatch_Probe(
    const char* qualified_name,
    PyObject *self,
    PyObject *const *args,
    Py_ssize_t nargs,
    PyObject *kwnames,
    PyObject **p_result
)
{
    __Pyx_Dispatcher_t f = __Pyx__global_c_dispatcher;
    if (f) {
        return f(qualified_name, self, args, nargs, kwnames, p_result);
    }
    CYTHON_UNUSED_VAR(qualified_name); CYTHON_UNUSED_VAR(self);
    CYTHON_UNUSED_VAR(args); CYTHON_UNUSED_VAR(nargs);
    CYTHON_UNUSED_VAR(kwnames); CYTHON_UNUSED_VAR(p_result);
    return 0;
}

static CYTHON_INLINE int __Pyx_SetCDispatcherFromCapsule(PyObject *capsule)
{
#if PY_VERSION_HEX >= 0x02070000
    void *ptr = PyCapsule_GetPointer(capsule, "cython.cdispatcher.v1");
    if (unlikely(!ptr)) return -1;
    __Pyx__global_c_dispatcher = (__Pyx_Dispatcher_t) ptr;
    return 0;
#else
    CYTHON_UNUSED_VAR(capsule);
    return -1;
#endif
}

static CYTHON_INLINE void __Pyx_TrySetupCDispatcher(void)
{
    PyObject *mod = NULL, *capsule = NULL;
    if (__Pyx__global_c_dispatcher) return;
    mod = PyImport_ImportModule("mbcore.utils.func_utils");
    if (unlikely(!mod)) { PyErr_Clear(); return; }
    capsule = PyObject_GetAttrString(mod, "_c_dispatcher");
    if (likely(capsule)) {
        (void)__Pyx_SetCDispatcherFromCapsule(capsule);
        Py_DECREF(capsule);
    } else {
        PyErr_Clear();
    }
    Py_DECREF(mod);
}
