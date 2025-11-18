# Cython annotation for refnanny.pyx

Raw output: refnanny.c

L1  ⚪  (score=0)
```python
# cython: language_level=3, auto_pickle=False, freethreading_compatible=True
```
L2  ⚪  (score=0)
```python
```
L3  ⚪  (score=0)
```python
cimport cython
```
L4  ⚪  (score=0)
```python
```
L5  ⚪  (score=0)
```python
cdef extern from "Python.h":
```
L6  ⚪  (score=0)
```python
    ctypedef struct PyObject:
```
L7  ⚪  (score=0)
```python
        pass
```
L8  ⚪  (score=0)
```python
    void Py_INCREF(PyObject *o)
```
L9  ⚪  (score=0)
```python
    void Py_CLEAR(PyObject *o)
```
L10  ⚪  (score=0)
```python
    void Py_XDECREF(PyObject *o)
```
L11  ⚪  (score=0)
```python
    void Py_XINCREF(PyObject *o)
```
L12  ⚪  (score=0)
```python
    void PyErr_Fetch(PyObject **ptype, PyObject **pvalue, PyObject **ptraceback)
```
L13  ⚪  (score=0)
```python
    void PyErr_Restore(PyObject *type, PyObject *value, PyObject *traceback)
```
L14  ⚪  (score=0)
```python
    void *PyThreadState_Get()
```
L15  ⚪  (score=0)
```python
```
L16  ⚪  (score=0)
```python
cdef extern from *:
```
L17  ⚪  (score=0)
```python
    """
```
L18  ⚪  (score=0)
```python
    #if CYTHON_COMPILING_IN_CPYTHON_FREETHREADING
```
L19  ⚪  (score=0)
```python
    #define __Pyx_refnanny_mutex PyMutex
```
L20  ⚪  (score=0)
```python
    static CYTHON_INLINE void __Pyx_refnanny_lock_acquire(PyMutex *lock) {
```
L21  ⚪  (score=0)
```python
        PyMutex_Lock(lock);
```
L22  ⚪  (score=0)
```python
    }
```
L23  ⚪  (score=0)
```python
```
L24  ⚪  (score=0)
```python
    static CYTHON_INLINE void __Pyx_refnanny_lock_release(PyMutex *lock) {
```
L25  ⚪  (score=0)
```python
        PyMutex_Unlock(lock);
```
L26  ⚪  (score=0)
```python
    }
```
L27  ⚪  (score=0)
```python
    #else
```
L28  ⚪  (score=0)
```python
    #define __Pyx_refnanny_mutex void*
```
L29  ⚪  (score=0)
```python
    #define __Pyx_refnanny_lock_acquire(lock)
```
L30  ⚪  (score=0)
```python
    #define __Pyx_refnanny_lock_release(lock)
```
L31  ⚪  (score=0)
```python
    #endif
```
L32  ⚪  (score=0)
```python
    """
```
L33  ⚪  (score=0)
```python
    ctypedef void *__Pyx_refnanny_mutex
```
L34  ⚪  (score=0)
```python
    void __Pyx_refnanny_lock_acquire(__Pyx_refnanny_mutex *lock)
```
L35  ⚪  (score=0)
```python
    void __Pyx_refnanny_lock_release(__Pyx_refnanny_mutex *lock)
```
L36  ⚪  (score=0)
```python
```
L37  ⚪  (score=0)
```python
loglevel = 0
```
L38  ⚪  (score=0)
```python
reflog = []
```
L39  ⚪  (score=0)
```python
```
L40  ⚪  (score=0)
```python
cdef int log(int level, action, obj, lineno) except -1:
```
L41  ⚪  (score=0)
```python
    if (<int> loglevel) >= level:
```
L42  ⚪  (score=0)
```python
        if reflog is None:
```
L43  ⚪  (score=0)
```python
            # can happen during finalisation
```
L44  ⚪  (score=0)
```python
            return 0
```
L45  ⚪  (score=0)
```python
        reflog.append((lineno, action, id(obj)))
```
L46  ⚪  (score=0)
```python
    return 0
```
L47  ⚪  (score=0)
```python
```
L48  ⚪  (score=0)
```python
LOG_NONE, LOG_ALL = range(2)
```
L49  ⚪  (score=0)
```python
cdef int _LOG_NONE = LOG_NONE
```
L50  ⚪  (score=0)
```python
cdef int _LOG_ALL = LOG_ALL
```
L51  ⚪  (score=0)
```python
```
L52  ⚪  (score=0)
```python
cdef object NO_REFS = (0, None)
```
L53  ⚪  (score=0)
```python
```
L54  ⚪  (score=0)
```python
```
L55  ⚪  (score=0)
```python
@cython.final
```
L56  ⚪  (score=0)
```python
cdef class Context(object):
```
L57  ⚪  (score=0)
```python
    cdef readonly object name, filename
```
L58  ⚪  (score=0)
```python
    cdef readonly dict refs
```
L59  ⚪  (score=0)
```python
    cdef readonly list errors
```
L60  ⚪  (score=0)
```python
    cdef readonly Py_ssize_t start
```
L61  ⚪  (score=0)
```python
    cdef __Pyx_refnanny_mutex lock
```
L62  ⚪  (score=0)
```python
```
L63  ⚪  (score=0)
```python
    def __cinit__(self, name, line=0, filename=None):
```
L64  ⚪  (score=0)
```python
        self.name = name
```
L65  ⚪  (score=0)
```python
        self.start = line
```
L66  ⚪  (score=0)
```python
        self.filename = filename
```
L67  ⚪  (score=0)
```python
        self.refs = {} # id -> (count, [lineno])
```
L68  ⚪  (score=0)
```python
        self.errors = []
```
L69  ⚪  (score=0)
```python
```
L70  ⚪  (score=0)
```python
    cdef void acquire_lock(self) noexcept:
```
L71  ⚪  (score=0)
```python
        __Pyx_refnanny_lock_acquire(&self.lock)
```
L72  ⚪  (score=0)
```python
```
L73  ⚪  (score=0)
```python
    cdef void release_lock(self) noexcept:
```
L74  ⚪  (score=0)
```python
        __Pyx_refnanny_lock_release(&self.lock)
```
L75  ⚪  (score=0)
```python
```
L76  ⚪  (score=0)
```python
    cdef int regref(self, obj, Py_ssize_t lineno, bint is_null) except -1:
```
L77  ⚪  (score=0)
```python
        log(_LOG_ALL, u'regref', u"<NULL>" if is_null else obj, lineno)
```
L78  ⚪  (score=0)
```python
        if is_null:
```
L79  ⚪  (score=0)
```python
            self.errors.append(f"NULL argument on line {lineno}")
```
L80  ⚪  (score=0)
```python
            return 0
```
L81  ⚪  (score=0)
```python
        id_ = id(obj)
```
L82  ⚪  (score=0)
```python
        count, linenumbers = self.refs.get(id_, NO_REFS)
```
L83  ⚪  (score=0)
```python
        if linenumbers is None:
```
L84  ⚪  (score=0)
```python
            linenumbers = []
```
L85  ⚪  (score=0)
```python
        self.refs[id_] = (count + 1, linenumbers)
```
L86  ⚪  (score=0)
```python
        linenumbers.append(lineno)
```
L87  ⚪  (score=0)
```python
        return 0
```
L88  ⚪  (score=0)
```python
```
L89  ⚪  (score=0)
```python
    cdef bint delref(self, obj, Py_ssize_t lineno, bint is_null) except -1:
```
L90  ⚪  (score=0)
```python
        # returns whether it is ok to do the decref operation
```
L91  ⚪  (score=0)
```python
        log(_LOG_ALL, u'delref', u"<NULL>" if is_null else obj, lineno)
```
L92  ⚪  (score=0)
```python
        if is_null:
```
L93  ⚪  (score=0)
```python
            self.errors.append(f"NULL argument on line {lineno}")
```
L94  ⚪  (score=0)
```python
            return False
```
L95  ⚪  (score=0)
```python
        id_ = id(obj)
```
L96  ⚪  (score=0)
```python
        count, linenumbers = self.refs.get(id_, NO_REFS)
```
L97  ⚪  (score=0)
```python
        if linenumbers is None:
```
L98  ⚪  (score=0)
```python
            linenumbers = []
```
L99  ⚪  (score=0)
```python
        if count == 0:
```
L100  ⚪  (score=0)
```python
            self.errors.append(f"Too many decrefs on line {lineno}, reference acquired on lines {linenumbers!r}")
```
L101  ⚪  (score=0)
```python
            return False
```
L102  ⚪  (score=0)
```python
        if count == 1:
```
L103  ⚪  (score=0)
```python
            del self.refs[id_]
```
L104  ⚪  (score=0)
```python
        else:
```
L105  ⚪  (score=0)
```python
            self.refs[id_] = (count - 1, linenumbers)
```
L106  ⚪  (score=0)
```python
        return True
```
L107  ⚪  (score=0)
```python
```
L108  ⚪  (score=0)
```python
    cdef end(self):
```
L109  ⚪  (score=0)
```python
        if self.refs:
```
L110  ⚪  (score=0)
```python
            msg = u"References leaked:"
```
L111  ⚪  (score=0)
```python
            for count, linenos in self.refs.values():
```
L112  ⚪  (score=0)
```python
                msg += f"\n  ({count}) acquired on lines: {u', '.join([f'{x}' for x in linenos])}"
```
L113  ⚪  (score=0)
```python
            self.errors.append(msg)
```
L114  ⚪  (score=0)
```python
        return u"\n".join([f'REFNANNY: {error}' for error in self.errors]) if self.errors else None
```
L115  ⚪  (score=0)
```python
```
L116  ⚪  (score=0)
```python
```
L117  ⚪  (score=0)
```python
cdef void report_unraisable(filename, Py_ssize_t lineno, object e=None) noexcept:
```
L118  ⚪  (score=0)
```python
    try:
```
L119  ⚪  (score=0)
```python
        if e is None:
```
L120  ⚪  (score=0)
```python
            import sys
```
L121  ⚪  (score=0)
```python
            e = sys.exc_info()[1]
```
L122  ⚪  (score=0)
```python
        print(f"refnanny raised an exception from {filename}:{lineno}: {e}")
```
L123  ⚪  (score=0)
```python
    finally:
```
L124  ⚪  (score=0)
```python
        return  # We absolutely cannot exit with an exception
```
L125  ⚪  (score=0)
```python
```
L126  ⚪  (score=0)
```python
```
L127  ⚪  (score=0)
```python
# All Python operations must happen after any existing
```
L128  ⚪  (score=0)
```python
# exception has been fetched, in case we are called from
```
L129  ⚪  (score=0)
```python
# exception-handling code.
```
L130  ⚪  (score=0)
```python
```
L131  ⚪  (score=0)
```python
cdef PyObject* SetupContext(char* funcname, Py_ssize_t lineno, char* filename) except NULL:
```
L132  ⚪  (score=0)
```python
    if Context is None:
```
L133  ⚪  (score=0)
```python
        # Context may be None during finalize phase.
```
L134  ⚪  (score=0)
```python
        # In that case, we don't want to be doing anything fancy
```
L135  ⚪  (score=0)
```python
        # like caching and resetting exceptions.
```
L136  ⚪  (score=0)
```python
        return NULL
```
L137  ⚪  (score=0)
```python
    cdef (PyObject*) type = NULL, value = NULL, tb = NULL, result = NULL
```
L138  ⚪  (score=0)
```python
    PyThreadState_Get()  # Check that we hold the GIL
```
L139  ⚪  (score=0)
```python
    PyErr_Fetch(&type, &value, &tb)
```
L140  ⚪  (score=0)
```python
    try:
```
L141  ⚪  (score=0)
```python
        ctx = Context.__new__(Context, funcname, lineno, filename)
```
L142  ⚪  (score=0)
```python
        Py_INCREF(<PyObject*>ctx)
```
L143  ⚪  (score=0)
```python
        result = <PyObject*>ctx
```
L144  ⚪  (score=0)
```python
    except Exception, e:
```
L145  ⚪  (score=0)
```python
        report_unraisable(filename, lineno, e)
```
L146  ⚪  (score=0)
```python
    PyErr_Restore(type, value, tb)
```
L147  ⚪  (score=0)
```python
    return result
```
L148  ⚪  (score=0)
```python
```
L149  ⚪  (score=0)
```python
cdef void GOTREF(PyObject* _ctx, PyObject* p_obj, Py_ssize_t lineno):
```
L150  ⚪  (score=0)
```python
    if _ctx == NULL: return
```
L151  ⚪  (score=0)
```python
    cdef (PyObject*) type = NULL, value = NULL, tb = NULL
```
L152  ⚪  (score=0)
```python
    cdef Context ctx = <Context> _ctx
```
L153  ⚪  (score=0)
```python
    ctx.acquire_lock()
```
L154  ⚪  (score=0)
```python
    PyErr_Fetch(&type, &value, &tb)
```
L155  ⚪  (score=0)
```python
    try:
```
L156  ⚪  (score=0)
```python
        ctx.regref(
```
L157  ⚪  (score=0)
```python
            <object>p_obj if p_obj is not NULL else None,
```
L158  ⚪  (score=0)
```python
            lineno,
```
L159  ⚪  (score=0)
```python
            is_null=p_obj is NULL,
```
L160  ⚪  (score=0)
```python
        )
```
L161  ⚪  (score=0)
```python
    except:
```
L162  ⚪  (score=0)
```python
        report_unraisable(ctx.filename, lineno=ctx.start)
```
L163  ⚪  (score=0)
```python
    finally:
```
L164  ⚪  (score=0)
```python
        PyErr_Restore(type, value, tb)
```
L165  ⚪  (score=0)
```python
        ctx.release_lock()
```
L166  ⚪  (score=0)
```python
        return  # swallow any exceptions
```
L167  ⚪  (score=0)
```python
```
L168  ⚪  (score=0)
```python
cdef bint GIVEREF_and_report(PyObject* _ctx, PyObject* p_obj, Py_ssize_t lineno):
```
L169  ⚪  (score=0)
```python
    if _ctx == NULL: return 1
```
L170  ⚪  (score=0)
```python
    cdef (PyObject*) type = NULL, value = NULL, tb = NULL
```
L171  ⚪  (score=0)
```python
    cdef bint decref_ok = False
```
L172  ⚪  (score=0)
```python
    cdef Context ctx = <Context> _ctx
```
L173  ⚪  (score=0)
```python
    ctx.acquire_lock()
```
L174  ⚪  (score=0)
```python
    PyErr_Fetch(&type, &value, &tb)
```
L175  ⚪  (score=0)
```python
    try:
```
L176  ⚪  (score=0)
```python
        decref_ok = ctx.delref(
```
L177  ⚪  (score=0)
```python
            <object>p_obj if p_obj is not NULL else None,
```
L178  ⚪  (score=0)
```python
            lineno,
```
L179  ⚪  (score=0)
```python
            is_null=p_obj is NULL,
```
L180  ⚪  (score=0)
```python
        )
```
L181  ⚪  (score=0)
```python
    except:
```
L182  ⚪  (score=0)
```python
        report_unraisable(ctx.filename, lineno=ctx.start)
```
L183  ⚪  (score=0)
```python
    finally:
```
L184  ⚪  (score=0)
```python
        PyErr_Restore(type, value, tb)
```
L185  ⚪  (score=0)
```python
        ctx.release_lock()
```
L186  ⚪  (score=0)
```python
        return decref_ok  # swallow any exceptions
```
L187  ⚪  (score=0)
```python
```
L188  ⚪  (score=0)
```python
cdef void GIVEREF(PyObject* ctx, PyObject* p_obj, Py_ssize_t lineno):
```
L189  ⚪  (score=0)
```python
    GIVEREF_and_report(ctx, p_obj, lineno)
```
L190  ⚪  (score=0)
```python
```
L191  ⚪  (score=0)
```python
cdef void INCREF(PyObject* ctx, PyObject* obj, Py_ssize_t lineno):
```
L192  ⚪  (score=0)
```python
    Py_XINCREF(obj)
```
L193  ⚪  (score=0)
```python
    PyThreadState_Get()  # Check that we hold the GIL
```
L194  ⚪  (score=0)
```python
    GOTREF(ctx, obj, lineno)
```
L195  ⚪  (score=0)
```python
```
L196  ⚪  (score=0)
```python
cdef void DECREF(PyObject* ctx, PyObject* obj, Py_ssize_t lineno):
```
L197  ⚪  (score=0)
```python
    if GIVEREF_and_report(ctx, obj, lineno):
```
L198  ⚪  (score=0)
```python
        Py_XDECREF(obj)
```
L199  ⚪  (score=0)
```python
    PyThreadState_Get()  # Check that we hold the GIL
```
L200  ⚪  (score=0)
```python
```
L201  ⚪  (score=0)
```python
cdef void FinishContext(PyObject** ctx):
```
L202  ⚪  (score=0)
```python
    if ctx == NULL or ctx[0] == NULL: return
```
L203  ⚪  (score=0)
```python
    cdef (PyObject*) type = NULL, value = NULL, tb = NULL
```
L204  ⚪  (score=0)
```python
    cdef object errors = None
```
L205  ⚪  (score=0)
```python
    cdef Context context
```
L206  ⚪  (score=0)
```python
    PyThreadState_Get()  # Check that we hold the GIL
```
L207  ⚪  (score=0)
```python
    PyErr_Fetch(&type, &value, &tb)
```
L208  ⚪  (score=0)
```python
    try:
```
L209  ⚪  (score=0)
```python
        context = <Context>ctx[0]
```
L210  ⚪  (score=0)
```python
        errors = context.end()
```
L211  ⚪  (score=0)
```python
        if errors:
```
L212  ⚪  (score=0)
```python
            print(f"{context.filename.decode('latin1')}: {context.name.decode('latin1')}()")
```
L213  ⚪  (score=0)
```python
            print(errors)
```
L214  ⚪  (score=0)
```python
        context = None
```
L215  ⚪  (score=0)
```python
    except:
```
L216  ⚪  (score=0)
```python
        report_unraisable(
```
L217  ⚪  (score=0)
```python
            context.filename if context is not None else None,
```
L218  ⚪  (score=0)
```python
            lineno=context.start if context is not None else 0,
```
L219  ⚪  (score=0)
```python
        )
```
L220  ⚪  (score=0)
```python
    finally:
```
L221  ⚪  (score=0)
```python
        Py_CLEAR(ctx[0])
```
L222  ⚪  (score=0)
```python
        PyErr_Restore(type, value, tb)
```
L223  ⚪  (score=0)
```python
        return  # swallow any exceptions
```
L224  ⚪  (score=0)
```python
```
L225  ⚪  (score=0)
```python
ctypedef struct RefNannyAPIStruct:
```
L226  ⚪  (score=0)
```python
    void (*INCREF)(PyObject*, PyObject*, Py_ssize_t)
```
L227  ⚪  (score=0)
```python
    void (*DECREF)(PyObject*, PyObject*, Py_ssize_t)
```
L228  ⚪  (score=0)
```python
    void (*GOTREF)(PyObject*, PyObject*, Py_ssize_t)
```
L229  ⚪  (score=0)
```python
    void (*GIVEREF)(PyObject*, PyObject*, Py_ssize_t)
```
L230  ⚪  (score=0)
```python
    PyObject* (*SetupContext)(char*, Py_ssize_t, char*) except NULL
```
L231  ⚪  (score=0)
```python
    void (*FinishContext)(PyObject**)
```
L232  ⚪  (score=0)
```python
```
L233  ⚪  (score=0)
```python
cdef RefNannyAPIStruct api
```
L234  ⚪  (score=0)
```python
api.INCREF = INCREF
```
L235  ⚪  (score=0)
```python
api.DECREF =  DECREF
```
L236  ⚪  (score=0)
```python
api.GOTREF =  GOTREF
```
L237  ⚪  (score=0)
```python
api.GIVEREF = GIVEREF
```
L238  ⚪  (score=0)
```python
api.SetupContext = SetupContext
```
L239  ⚪  (score=0)
```python
api.FinishContext = FinishContext
```
L240  ⚪  (score=0)
```python
```
L241  ⚪  (score=0)
```python
cdef extern from "Python.h":
```
L242  ⚪  (score=0)
```python
    object PyLong_FromVoidPtr(void*)
```
L243  ⚪  (score=0)
```python
```
L244  ⚪  (score=0)
```python
RefNannyAPI = PyLong_FromVoidPtr(<void*>&api)
```
