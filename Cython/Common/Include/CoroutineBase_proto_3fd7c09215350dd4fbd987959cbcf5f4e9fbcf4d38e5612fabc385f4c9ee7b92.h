struct __pyx_CoroutineObject;
typedef PyObject *(*__pyx_coroutine_body_t)(struct __pyx_CoroutineObject *, PyThreadState *, PyObject *);
#if CYTHON_USE_EXC_INFO_STACK
#define __Pyx_ExcInfoStruct  _PyErr_StackItem
#else
typedef struct {
    PyObject *exc_type;
    PyObject *exc_value;
    PyObject *exc_traceback;
} __Pyx_ExcInfoStruct;
#endif
typedef struct __pyx_CoroutineObject {
    PyObject_HEAD
    __pyx_coroutine_body_t body;
    PyObject *closure;
    __Pyx_ExcInfoStruct gi_exc_state;
#if PY_VERSION_HEX < 0x030C0000 || CYTHON_COMPILING_IN_LIMITED_API
    PyObject *gi_weakreflist;
#endif
    PyObject *classobj;
    PyObject *yieldfrom;
    __Pyx_pyiter_sendfunc yieldfrom_am_send;
    PyObject *gi_name;
    PyObject *gi_qualname;
    PyObject *gi_modulename;
    PyObject *gi_code;
    PyObject *gi_frame;
#if CYTHON_USE_SYS_MONITORING && (CYTHON_PROFILE || CYTHON_TRACE)
    PyMonitoringState __pyx_pymonitoring_state[__Pyx_MonitoringEventTypes_CyGen_count];
    uint64_t __pyx_pymonitoring_version;
#endif
    int resume_label;
    char is_running;
} __pyx_CoroutineObject;
static __pyx_CoroutineObject *__Pyx__Coroutine_New(
    PyTypeObject *type, __pyx_coroutine_body_t body, PyObject *code, PyObject *closure,
    PyObject *name, PyObject *qualname, PyObject *module_name);
static __pyx_CoroutineObject *__Pyx__Coroutine_NewInit(
            __pyx_CoroutineObject *gen, __pyx_coroutine_body_t body, PyObject *code, PyObject *closure,
            PyObject *name, PyObject *qualname, PyObject *module_name);
static CYTHON_INLINE void __Pyx_Coroutine_ExceptionClear(__Pyx_ExcInfoStruct *self);
static int __Pyx_Coroutine_clear(PyObject *self);
static __Pyx_PySendResult __Pyx_Coroutine_AmSend(PyObject *self, PyObject *value, PyObject **retval);
static PyObject *__Pyx_Coroutine_Send(PyObject *self, PyObject *value);
static __Pyx_PySendResult __Pyx_Coroutine_Close(PyObject *self, PyObject **retval);
static PyObject *__Pyx_Coroutine_Throw(PyObject *gen, PyObject *args);
#if CYTHON_USE_EXC_INFO_STACK
#define __Pyx_Coroutine_SwapException(self)
#define __Pyx_Coroutine_ResetAndClearException(self)  __Pyx_Coroutine_ExceptionClear(&(self)->gi_exc_state)
#else
#define __Pyx_Coroutine_SwapException(self) {\
    __Pyx_ExceptionSwap(&(self)->gi_exc_state.exc_type, &(self)->gi_exc_state.exc_value, &(self)->gi_exc_state.exc_traceback);\
    __Pyx_Coroutine_ResetFrameBackpointer(&(self)->gi_exc_state);\
    }
#define __Pyx_Coroutine_ResetAndClearException(self) {\
    __Pyx_ExceptionReset((self)->gi_exc_state.exc_type, (self)->gi_exc_state.exc_value, (self)->gi_exc_state.exc_traceback);\
    (self)->gi_exc_state.exc_type = (self)->gi_exc_state.exc_value = (self)->gi_exc_state.exc_traceback = NULL;\
    }
#endif
#if CYTHON_FAST_THREAD_STATE
#define __Pyx_PyGen_FetchStopIterationValue(pvalue)\
    __Pyx_PyGen__FetchStopIterationValue(__pyx_tstate, pvalue)
#else
#define __Pyx_PyGen_FetchStopIterationValue(pvalue)\
    __Pyx_PyGen__FetchStopIterationValue(__Pyx_PyThreadState_Current, pvalue)
#endif
static int __Pyx_PyGen__FetchStopIterationValue(PyThreadState *tstate, PyObject **pvalue);
static CYTHON_INLINE void __Pyx_Coroutine_ResetFrameBackpointer(__Pyx_ExcInfoStruct *exc_state);
static char __Pyx_Coroutine_test_and_set_is_running(__pyx_CoroutineObject *gen);
static void __Pyx_Coroutine_unset_is_running(__pyx_CoroutineObject *gen);
static char __Pyx_Coroutine_get_is_running(__pyx_CoroutineObject *gen);
static PyObject *__Pyx_Coroutine_get_is_running_getter(PyObject *gen, void *closure);
#if __PYX_HAS_PY_AM_SEND == 2
static void __Pyx_SetBackportTypeAmSend(PyTypeObject *type, __Pyx_PyAsyncMethodsStruct *static_amsend_methods, __Pyx_pyiter_sendfunc am_send);
#endif
static PyObject *__Pyx_Coroutine_fail_reduce_ex(PyObject *self, PyObject *arg);

