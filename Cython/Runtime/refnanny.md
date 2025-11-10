# Cython annotation for refnanny.pyx

Raw output: refnanny.c

L1  🟠  (score=8)
```python
# cython: language_level=3, auto_pickle=False
```
<details><summary>Show generated C (score=8)</summary>

```c
  __pyx_t_2 = __Pyx_PyDict_NewPresized(0); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 1, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  if (PyDict_SetItem(__pyx_mstate_global->__pyx_d, __pyx_mstate_global->__pyx_n_u_test, __pyx_t_2) < (0)) __PYX_ERR(0, 1, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
```

</details>

L2  ⚪  (score=0)
```python
```
L3  ⚪  (score=0)
```python
from cpython.ref cimport PyObject, Py_INCREF, Py_CLEAR, Py_XDECREF, Py_XINCREF
```
L4  ⚪  (score=0)
```python
from cpython.exc cimport PyErr_Fetch, PyErr_Restore
```
L5  ⚪  (score=0)
```python
from cpython.pystate cimport PyThreadState_Get
```
L6  ⚪  (score=0)
```python
```
L7  ⚪  (score=0)
```python
cimport cython
```
L8  ⚪  (score=0)
```python
```
L9  ⚪  (score=0)
```python
cdef extern from *:
```
L10  ⚪  (score=0)
```python
    """
```
L11  ⚪  (score=0)
```python
    #if CYTHON_COMPILING_IN_CPYTHON_FREETHREADING
```
L12  ⚪  (score=0)
```python
    #define __Pyx_refnanny_mutex PyMutex
```
L13  ⚪  (score=0)
```python
    static CYTHON_INLINE void __Pyx_refnanny_lock_acquire(PyMutex *lock) {
```
L14  ⚪  (score=0)
```python
        PyMutex_Lock(lock);
```
L15  ⚪  (score=0)
```python
    }
```
L16  ⚪  (score=0)
```python
```
L17  ⚪  (score=0)
```python
    static CYTHON_INLINE void __Pyx_refnanny_lock_release(PyMutex *lock) {
```
L18  ⚪  (score=0)
```python
        PyMutex_Unlock(lock);
```
L19  ⚪  (score=0)
```python
    }
```
L20  ⚪  (score=0)
```python
    #else
```
L21  ⚪  (score=0)
```python
    #define __Pyx_refnanny_mutex void*
```
L22  ⚪  (score=0)
```python
    #define __Pyx_refnanny_lock_acquire(lock)
```
L23  ⚪  (score=0)
```python
    #define __Pyx_refnanny_lock_release(lock)
```
L24  ⚪  (score=0)
```python
    #endif
```
L25  ⚪  (score=0)
```python
    """
```
L26  ⚪  (score=0)
```python
    ctypedef void *__Pyx_refnanny_mutex
```
L27  ⚪  (score=0)
```python
    void __Pyx_refnanny_lock_acquire(__Pyx_refnanny_mutex *lock)
```
L28  ⚪  (score=0)
```python
    void __Pyx_refnanny_lock_release(__Pyx_refnanny_mutex *lock)
```
L29  ⚪  (score=0)
```python
```
L30  🟠  (score=5)
```python
loglevel = 0
```
<details><summary>Show generated C (score=5)</summary>

```c
  if (PyDict_SetItem(__pyx_mstate_global->__pyx_d, __pyx_mstate_global->__pyx_n_u_loglevel, __pyx_mstate_global->__pyx_int_0) < (0)) __PYX_ERR(0, 30, __pyx_L1_error)
```

</details>

L31  🔴  (score=11)
```python
reflog = []
```
<details><summary>Show generated C (score=11)</summary>

```c
  __pyx_t_2 = PyList_New(0); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 31, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  if (PyDict_SetItem(__pyx_mstate_global->__pyx_d, __pyx_mstate_global->__pyx_n_u_reflog, __pyx_t_2) < (0)) __PYX_ERR(0, 31, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
```

</details>

L32  ⚪  (score=0)
```python
```
L33  🟠  (score=5)
```python
cdef int log(int level, action, obj, lineno) except -1:
```
<details><summary>Show generated C (score=5)</summary>

```c
static int __pyx_f_6Cython_7Runtime_8refnanny_log(int __pyx_v_level, PyObject *__pyx_v_action, PyObject *__pyx_v_obj, PyObject *__pyx_v_lineno) {
  int __pyx_r;
/* … */
  /* function exit code */
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_t_1);
  __Pyx_XDECREF(__pyx_t_4);
  __Pyx_XDECREF(__pyx_t_5);
  __Pyx_AddTraceback("Cython.Runtime.refnanny.log", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_r = -1;
  __pyx_L0:;
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}
```

</details>

L34  🟠  (score=5)
```python
    if (<int> loglevel) >= level:
```
<details><summary>Show generated C (score=5)</summary>

```c
  __Pyx_GetModuleGlobalName(__pyx_t_1, __pyx_mstate_global->__pyx_n_u_loglevel); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 34, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __pyx_t_2 = __Pyx_PyLong_As_int(__pyx_t_1); if (unlikely((__pyx_t_2 == (int)-1) && PyErr_Occurred())) __PYX_ERR(0, 34, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __pyx_t_3 = (((int)__pyx_t_2) >= __pyx_v_level);
  if (__pyx_t_3) {
/* … */
  }
```

</details>

L35  🟡  (score=3)
```python
        if reflog is None:
```
<details><summary>Show generated C (score=3)</summary>

```c
    __Pyx_GetModuleGlobalName(__pyx_t_1, __pyx_mstate_global->__pyx_n_u_reflog); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 35, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_1);
    __pyx_t_3 = (__pyx_t_1 == Py_None);
    __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
    if (__pyx_t_3) {
/* … */
    }
```

</details>

L36  ⚪  (score=0)
```python
            # can happen during finalisation
```
L37  ⚪  (score=0)
```python
            return 0
```
<details><summary>Show generated C (score=0)</summary>

```c
      __pyx_r = 0;
      goto __pyx_L0;
```

</details>

L38  🔴  (score=22)
```python
        reflog.append((lineno, action, id(obj)))
```
<details><summary>Show generated C (score=22)</summary>

```c
    __Pyx_GetModuleGlobalName(__pyx_t_1, __pyx_mstate_global->__pyx_n_u_reflog); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 38, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_1);
    __pyx_t_5 = NULL;
    __pyx_t_6 = 1;
    {
      PyObject *__pyx_callargs[2] = {__pyx_t_5, __pyx_v_obj};
      __pyx_t_4 = __Pyx_PyObject_FastCall((PyObject*)__pyx_builtin_id, __pyx_callargs+__pyx_t_6, (2-__pyx_t_6) | (__pyx_t_6*__Pyx_PY_VECTORCALL_ARGUMENTS_OFFSET));
      __Pyx_XDECREF(__pyx_t_5); __pyx_t_5 = 0;
      if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 38, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_4);
    }
    __pyx_t_5 = PyTuple_New(3); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 38, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_5);
    __Pyx_INCREF(__pyx_v_lineno);
    __Pyx_GIVEREF(__pyx_v_lineno);
    if (__Pyx_PyTuple_SET_ITEM(__pyx_t_5, 0, __pyx_v_lineno) != (0)) __PYX_ERR(0, 38, __pyx_L1_error);
    __Pyx_INCREF(__pyx_v_action);
    __Pyx_GIVEREF(__pyx_v_action);
    if (__Pyx_PyTuple_SET_ITEM(__pyx_t_5, 1, __pyx_v_action) != (0)) __PYX_ERR(0, 38, __pyx_L1_error);
    __Pyx_GIVEREF(__pyx_t_4);
    if (__Pyx_PyTuple_SET_ITEM(__pyx_t_5, 2, __pyx_t_4) != (0)) __PYX_ERR(0, 38, __pyx_L1_error);
    __pyx_t_4 = 0;
    __pyx_t_7 = __Pyx_PyObject_Append(__pyx_t_1, __pyx_t_5); if (unlikely(__pyx_t_7 == ((int)-1))) __PYX_ERR(0, 38, __pyx_L1_error)
    __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
    __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
```

</details>

L39  ⚪  (score=0)
```python
    return 0
```
<details><summary>Show generated C (score=0)</summary>

```c
  __pyx_r = 0;
  goto __pyx_L0;
```

</details>

L40  ⚪  (score=0)
```python
```
L41  🔴  (score=31)
```python
LOG_NONE, LOG_ALL = range(2)
```
<details><summary>Show generated C (score=31)</summary>

```c
  __pyx_t_3 = NULL;
  __pyx_t_4 = 1;
  {
    PyObject *__pyx_callargs[2] = {__pyx_t_3, __pyx_mstate_global->__pyx_int_2};
    __pyx_t_2 = __Pyx_PyObject_FastCall((PyObject*)(&PyRange_Type), __pyx_callargs+__pyx_t_4, (2-__pyx_t_4) | (__pyx_t_4*__Pyx_PY_VECTORCALL_ARGUMENTS_OFFSET));
    __Pyx_XDECREF(__pyx_t_3); __pyx_t_3 = 0;
    if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 41, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_2);
  }
  {
    Py_ssize_t index = -1;
    __pyx_t_6 = PyObject_GetIter(__pyx_t_2); if (unlikely(!__pyx_t_6)) __PYX_ERR(0, 41, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_6);
    __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
    __pyx_t_7 = (CYTHON_COMPILING_IN_LIMITED_API) ? PyIter_Next : __Pyx_PyObject_GetIterNextFunc(__pyx_t_6);
    index = 0; __pyx_t_3 = __pyx_t_7(__pyx_t_6); if (unlikely(!__pyx_t_3)) goto __pyx_L2_unpacking_failed;
    __Pyx_GOTREF(__pyx_t_3);
    index = 1; __pyx_t_5 = __pyx_t_7(__pyx_t_6); if (unlikely(!__pyx_t_5)) goto __pyx_L2_unpacking_failed;
    __Pyx_GOTREF(__pyx_t_5);
    if (__Pyx_IternextUnpackEndCheck(__pyx_t_7(__pyx_t_6), 2) < (0)) __PYX_ERR(0, 41, __pyx_L1_error)
    __pyx_t_7 = NULL;
    __Pyx_DECREF(__pyx_t_6); __pyx_t_6 = 0;
    goto __pyx_L3_unpacking_done;
    __pyx_L2_unpacking_failed:;
    __Pyx_DECREF(__pyx_t_6); __pyx_t_6 = 0;
    __pyx_t_7 = NULL;
    if (__Pyx_IterFinish() == 0) __Pyx_RaiseNeedMoreValuesError(index);
    __PYX_ERR(0, 41, __pyx_L1_error)
    __pyx_L3_unpacking_done:;
  }
  if (PyDict_SetItem(__pyx_mstate_global->__pyx_d, __pyx_mstate_global->__pyx_n_u_LOG_NONE, __pyx_t_3) < (0)) __PYX_ERR(0, 41, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
  if (PyDict_SetItem(__pyx_mstate_global->__pyx_d, __pyx_mstate_global->__pyx_n_u_LOG_ALL, __pyx_t_5) < (0)) __PYX_ERR(0, 41, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
```

</details>

L42  🟠  (score=5)
```python
cdef int _LOG_NONE = LOG_NONE
```
<details><summary>Show generated C (score=5)</summary>

```c
  __Pyx_GetModuleGlobalName(__pyx_t_2, __pyx_mstate_global->__pyx_n_u_LOG_NONE); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 42, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __pyx_t_8 = __Pyx_PyLong_As_int(__pyx_t_2); if (unlikely((__pyx_t_8 == (int)-1) && PyErr_Occurred())) __PYX_ERR(0, 42, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __pyx_v_6Cython_7Runtime_8refnanny__LOG_NONE = __pyx_t_8;
```

</details>

L43  🟠  (score=5)
```python
cdef int _LOG_ALL = LOG_ALL
```
<details><summary>Show generated C (score=5)</summary>

```c
  __Pyx_GetModuleGlobalName(__pyx_t_2, __pyx_mstate_global->__pyx_n_u_LOG_ALL); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 43, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __pyx_t_8 = __Pyx_PyLong_As_int(__pyx_t_2); if (unlikely((__pyx_t_8 == (int)-1) && PyErr_Occurred())) __PYX_ERR(0, 43, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __pyx_v_6Cython_7Runtime_8refnanny__LOG_ALL = __pyx_t_8;
```

</details>

L44  ⚪  (score=0)
```python
```
L45  🟡  (score=2)
```python
cdef object NO_REFS = (0, None)
```
<details><summary>Show generated C (score=2)</summary>

```c
  __Pyx_INCREF(__pyx_mstate_global->__pyx_tuple[1]);
  __Pyx_XGOTREF(__pyx_v_6Cython_7Runtime_8refnanny_NO_REFS);
  __Pyx_DECREF_SET(__pyx_v_6Cython_7Runtime_8refnanny_NO_REFS, __pyx_mstate_global->__pyx_tuple[1]);
  __Pyx_GIVEREF(__pyx_mstate_global->__pyx_tuple[1]);
```

</details>

L46  ⚪  (score=0)
```python
```
L47  ⚪  (score=0)
```python
```
L48  ⚪  (score=0)
```python
@cython.final
```
<details><summary>Show generated C (score=0)</summary>

```c
struct __pyx_obj_6Cython_7Runtime_8refnanny_Context {
  PyObject_HEAD
  struct __pyx_vtabstruct_6Cython_7Runtime_8refnanny_Context *__pyx_vtab;
  PyObject *name;
  PyObject *filename;
  PyObject *refs;
  PyObject *errors;
  Py_ssize_t start;
  __Pyx_refnanny_mutex lock;
};



struct __pyx_vtabstruct_6Cython_7Runtime_8refnanny_Context {
  void (*acquire_lock)(struct __pyx_obj_6Cython_7Runtime_8refnanny_Context *);
  void (*release_lock)(struct __pyx_obj_6Cython_7Runtime_8refnanny_Context *);
  int (*regref)(struct __pyx_obj_6Cython_7Runtime_8refnanny_Context *, PyObject *, Py_ssize_t, int);
  int (*delref)(struct __pyx_obj_6Cython_7Runtime_8refnanny_Context *, PyObject *, Py_ssize_t, int);
  PyObject *(*end)(struct __pyx_obj_6Cython_7Runtime_8refnanny_Context *);
};
static struct __pyx_vtabstruct_6Cython_7Runtime_8refnanny_Context *__pyx_vtabptr_6Cython_7Runtime_8refnanny_Context;
```

</details>

L49  ⚪  (score=0)
```python
cdef class Context(object):
```
L50  🟠  (score=8)
```python
    cdef readonly object name, filename
```
<details><summary>Show generated C (score=8)</summary>

```c
/* Python wrapper */
static PyObject *__pyx_pw_6Cython_7Runtime_8refnanny_7Context_4name_1__get__(PyObject *__pyx_v_self); /*proto*/
static PyObject *__pyx_pw_6Cython_7Runtime_8refnanny_7Context_4name_1__get__(PyObject *__pyx_v_self) {
  CYTHON_UNUSED PyObject *const *__pyx_kwvalues;
  PyObject *__pyx_r = 0;
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("__get__ (wrapper)", 0);
  __pyx_kwvalues = __Pyx_KwValues_VARARGS(__pyx_args, __pyx_nargs);
  __pyx_r = __pyx_pf_6Cython_7Runtime_8refnanny_7Context_4name___get__(((struct __pyx_obj_6Cython_7Runtime_8refnanny_Context *)__pyx_v_self));

  /* function exit code */
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}

static PyObject *__pyx_pf_6Cython_7Runtime_8refnanny_7Context_4name___get__(struct __pyx_obj_6Cython_7Runtime_8refnanny_Context *__pyx_v_self) {
  PyObject *__pyx_r = NULL;
  __Pyx_XDECREF(__pyx_r);
  __Pyx_INCREF(__pyx_v_self->name);
  __pyx_r = __pyx_v_self->name;
  goto __pyx_L0;

  /* function exit code */
  __pyx_L0:;
  __Pyx_XGIVEREF(__pyx_r);
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}

/* Python wrapper */
static PyObject *__pyx_pw_6Cython_7Runtime_8refnanny_7Context_8filename_1__get__(PyObject *__pyx_v_self); /*proto*/
static PyObject *__pyx_pw_6Cython_7Runtime_8refnanny_7Context_8filename_1__get__(PyObject *__pyx_v_self) {
  CYTHON_UNUSED PyObject *const *__pyx_kwvalues;
  PyObject *__pyx_r = 0;
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("__get__ (wrapper)", 0);
  __pyx_kwvalues = __Pyx_KwValues_VARARGS(__pyx_args, __pyx_nargs);
  __pyx_r = __pyx_pf_6Cython_7Runtime_8refnanny_7Context_8filename___get__(((struct __pyx_obj_6Cython_7Runtime_8refnanny_Context *)__pyx_v_self));

  /* function exit code */
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}

static PyObject *__pyx_pf_6Cython_7Runtime_8refnanny_7Context_8filename___get__(struct __pyx_obj_6Cython_7Runtime_8refnanny_Context *__pyx_v_self) {
  PyObject *__pyx_r = NULL;
  __Pyx_XDECREF(__pyx_r);
  __Pyx_INCREF(__pyx_v_self->filename);
  __pyx_r = __pyx_v_self->filename;
  goto __pyx_L0;

  /* function exit code */
  __pyx_L0:;
  __Pyx_XGIVEREF(__pyx_r);
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}
```

</details>

L51  🟡  (score=4)
```python
    cdef readonly dict refs
```
<details><summary>Show generated C (score=4)</summary>

```c
/* Python wrapper */
static PyObject *__pyx_pw_6Cython_7Runtime_8refnanny_7Context_4refs_1__get__(PyObject *__pyx_v_self); /*proto*/
static PyObject *__pyx_pw_6Cython_7Runtime_8refnanny_7Context_4refs_1__get__(PyObject *__pyx_v_self) {
  CYTHON_UNUSED PyObject *const *__pyx_kwvalues;
  PyObject *__pyx_r = 0;
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("__get__ (wrapper)", 0);
  __pyx_kwvalues = __Pyx_KwValues_VARARGS(__pyx_args, __pyx_nargs);
  __pyx_r = __pyx_pf_6Cython_7Runtime_8refnanny_7Context_4refs___get__(((struct __pyx_obj_6Cython_7Runtime_8refnanny_Context *)__pyx_v_self));

  /* function exit code */
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}

static PyObject *__pyx_pf_6Cython_7Runtime_8refnanny_7Context_4refs___get__(struct __pyx_obj_6Cython_7Runtime_8refnanny_Context *__pyx_v_self) {
  PyObject *__pyx_r = NULL;
  __Pyx_XDECREF(__pyx_r);
  __Pyx_INCREF(__pyx_v_self->refs);
  __pyx_r = __pyx_v_self->refs;
  goto __pyx_L0;

  /* function exit code */
  __pyx_L0:;
  __Pyx_XGIVEREF(__pyx_r);
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}
```

</details>

L52  🟡  (score=4)
```python
    cdef readonly list errors
```
<details><summary>Show generated C (score=4)</summary>

```c
/* Python wrapper */
static PyObject *__pyx_pw_6Cython_7Runtime_8refnanny_7Context_6errors_1__get__(PyObject *__pyx_v_self); /*proto*/
static PyObject *__pyx_pw_6Cython_7Runtime_8refnanny_7Context_6errors_1__get__(PyObject *__pyx_v_self) {
  CYTHON_UNUSED PyObject *const *__pyx_kwvalues;
  PyObject *__pyx_r = 0;
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("__get__ (wrapper)", 0);
  __pyx_kwvalues = __Pyx_KwValues_VARARGS(__pyx_args, __pyx_nargs);
  __pyx_r = __pyx_pf_6Cython_7Runtime_8refnanny_7Context_6errors___get__(((struct __pyx_obj_6Cython_7Runtime_8refnanny_Context *)__pyx_v_self));

  /* function exit code */
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}

static PyObject *__pyx_pf_6Cython_7Runtime_8refnanny_7Context_6errors___get__(struct __pyx_obj_6Cython_7Runtime_8refnanny_Context *__pyx_v_self) {
  PyObject *__pyx_r = NULL;
  __Pyx_XDECREF(__pyx_r);
  __Pyx_INCREF(__pyx_v_self->errors);
  __pyx_r = __pyx_v_self->errors;
  goto __pyx_L0;

  /* function exit code */
  __pyx_L0:;
  __Pyx_XGIVEREF(__pyx_r);
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}
```

</details>

L53  🔴  (score=11)
```python
    cdef readonly Py_ssize_t start
```
<details><summary>Show generated C (score=11)</summary>

```c
/* Python wrapper */
static PyObject *__pyx_pw_6Cython_7Runtime_8refnanny_7Context_5start_1__get__(PyObject *__pyx_v_self); /*proto*/
static PyObject *__pyx_pw_6Cython_7Runtime_8refnanny_7Context_5start_1__get__(PyObject *__pyx_v_self) {
  CYTHON_UNUSED PyObject *const *__pyx_kwvalues;
  PyObject *__pyx_r = 0;
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("__get__ (wrapper)", 0);
  __pyx_kwvalues = __Pyx_KwValues_VARARGS(__pyx_args, __pyx_nargs);
  __pyx_r = __pyx_pf_6Cython_7Runtime_8refnanny_7Context_5start___get__(((struct __pyx_obj_6Cython_7Runtime_8refnanny_Context *)__pyx_v_self));

  /* function exit code */
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}

static PyObject *__pyx_pf_6Cython_7Runtime_8refnanny_7Context_5start___get__(struct __pyx_obj_6Cython_7Runtime_8refnanny_Context *__pyx_v_self) {
  PyObject *__pyx_r = NULL;
  __Pyx_XDECREF(__pyx_r);
  __pyx_t_1 = PyLong_FromSsize_t(__pyx_v_self->start); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 53, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __pyx_r = __pyx_t_1;
  __pyx_t_1 = 0;
  goto __pyx_L0;

  /* function exit code */
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_t_1);
  __Pyx_AddTraceback("Cython.Runtime.refnanny.Context.start.__get__", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_r = NULL;
  __pyx_L0:;
  __Pyx_XGIVEREF(__pyx_r);
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}
```

</details>

L54  ⚪  (score=0)
```python
    cdef __Pyx_refnanny_mutex lock
```
L55  ⚪  (score=0)
```python
```
L56  🔴  (score=41)
```python
    def __cinit__(self, name, line=0, filename=None):
```
<details><summary>Show generated C (score=41)</summary>

```c
/* Python wrapper */
static int __pyx_pw_6Cython_7Runtime_8refnanny_7Context_1__cinit__(PyObject *__pyx_v_self, PyObject *__pyx_args, PyObject *__pyx_kwds); /*proto*/
static int __pyx_pw_6Cython_7Runtime_8refnanny_7Context_1__cinit__(PyObject *__pyx_v_self, PyObject *__pyx_args, PyObject *__pyx_kwds) {
  PyObject *__pyx_v_name = 0;
  PyObject *__pyx_v_line = 0;
  PyObject *__pyx_v_filename = 0;
  CYTHON_UNUSED Py_ssize_t __pyx_nargs;
  CYTHON_UNUSED PyObject *const *__pyx_kwvalues;
  int __pyx_r;
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("__cinit__ (wrapper)", 0);
  #if CYTHON_ASSUME_SAFE_SIZE
  __pyx_nargs = PyTuple_GET_SIZE(__pyx_args);
  #else
  __pyx_nargs = PyTuple_Size(__pyx_args); if (unlikely(__pyx_nargs < 0)) return -1;
  #endif
  __pyx_kwvalues = __Pyx_KwValues_VARARGS(__pyx_args, __pyx_nargs);
  {
    PyObject ** const __pyx_pyargnames[] = {&__pyx_mstate_global->__pyx_n_u_name,&__pyx_mstate_global->__pyx_n_u_line,&__pyx_mstate_global->__pyx_n_u_filename,0};
  PyObject* values[3] = {0,0,0};
    const Py_ssize_t __pyx_kwds_len = (__pyx_kwds) ? __Pyx_NumKwargs_VARARGS(__pyx_kwds) : 0;
    if (unlikely(__pyx_kwds_len) < 0) __PYX_ERR(0, 56, __pyx_L3_error)
    if (__pyx_kwds_len > 0) {
      switch (__pyx_nargs) {
        case  3:
        values[2] = __Pyx_ArgRef_VARARGS(__pyx_args, 2);
        if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[2])) __PYX_ERR(0, 56, __pyx_L3_error)
        CYTHON_FALLTHROUGH;
        case  2:
        values[1] = __Pyx_ArgRef_VARARGS(__pyx_args, 1);
        if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[1])) __PYX_ERR(0, 56, __pyx_L3_error)
        CYTHON_FALLTHROUGH;
        case  1:
        values[0] = __Pyx_ArgRef_VARARGS(__pyx_args, 0);
        if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[0])) __PYX_ERR(0, 56, __pyx_L3_error)
        CYTHON_FALLTHROUGH;
        case  0: break;
        default: goto __pyx_L5_argtuple_error;
      }
      const Py_ssize_t kwd_pos_args = __pyx_nargs;
      if (__Pyx_ParseKeywords(__pyx_kwds, __pyx_kwvalues, __pyx_pyargnames, 0, values, kwd_pos_args, __pyx_kwds_len, "__cinit__", 0) < (0)) __PYX_ERR(0, 56, __pyx_L3_error)
      if (!values[1]) values[1] = __Pyx_NewRef(((PyObject *)__pyx_mstate_global->__pyx_int_0));
      if (!values[2]) values[2] = __Pyx_NewRef(((PyObject *)Py_None));
      for (Py_ssize_t i = __pyx_nargs; i < 1; i++) {
        if (unlikely(!values[i])) { __Pyx_RaiseArgtupleInvalid("__cinit__", 0, 1, 3, i); __PYX_ERR(0, 56, __pyx_L3_error) }
      }
    } else {
      switch (__pyx_nargs) {
        case  3:
        values[2] = __Pyx_ArgRef_VARARGS(__pyx_args, 2);
        if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[2])) __PYX_ERR(0, 56, __pyx_L3_error)
        CYTHON_FALLTHROUGH;
        case  2:
        values[1] = __Pyx_ArgRef_VARARGS(__pyx_args, 1);
        if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[1])) __PYX_ERR(0, 56, __pyx_L3_error)
        CYTHON_FALLTHROUGH;
        case  1:
        values[0] = __Pyx_ArgRef_VARARGS(__pyx_args, 0);
        if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[0])) __PYX_ERR(0, 56, __pyx_L3_error)
        break;
        default: goto __pyx_L5_argtuple_error;
      }
      if (!values[1]) values[1] = __Pyx_NewRef(((PyObject *)__pyx_mstate_global->__pyx_int_0));
      if (!values[2]) values[2] = __Pyx_NewRef(((PyObject *)Py_None));
    }
    __pyx_v_name = values[0];
    __pyx_v_line = values[1];
    __pyx_v_filename = values[2];
  }
  goto __pyx_L6_skip;
  __pyx_L5_argtuple_error:;
  __Pyx_RaiseArgtupleInvalid("__cinit__", 0, 1, 3, __pyx_nargs); __PYX_ERR(0, 56, __pyx_L3_error)
  __pyx_L6_skip:;
  goto __pyx_L4_argument_unpacking_done;
  __pyx_L3_error:;
  for (Py_ssize_t __pyx_temp=0; __pyx_temp < (Py_ssize_t)(sizeof(values)/sizeof(values[0])); ++__pyx_temp) {
    Py_XDECREF(values[__pyx_temp]);
  }
  __Pyx_AddTraceback("Cython.Runtime.refnanny.Context.__cinit__", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __Pyx_RefNannyFinishContext();
  return -1;
  __pyx_L4_argument_unpacking_done:;
  __pyx_r = __pyx_pf_6Cython_7Runtime_8refnanny_7Context___cinit__(((struct __pyx_obj_6Cython_7Runtime_8refnanny_Context *)__pyx_v_self), __pyx_v_name, __pyx_v_line, __pyx_v_filename);

  /* function exit code */
  for (Py_ssize_t __pyx_temp=0; __pyx_temp < (Py_ssize_t)(sizeof(values)/sizeof(values[0])); ++__pyx_temp) {
    Py_XDECREF(values[__pyx_temp]);
  }
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}

static int __pyx_pf_6Cython_7Runtime_8refnanny_7Context___cinit__(struct __pyx_obj_6Cython_7Runtime_8refnanny_Context *__pyx_v_self, PyObject *__pyx_v_name, PyObject *__pyx_v_line, PyObject *__pyx_v_filename) {
  int __pyx_r;
/* … */
  /* function exit code */
  __pyx_r = 0;
  goto __pyx_L0;
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_t_2);
  __Pyx_AddTraceback("Cython.Runtime.refnanny.Context.__cinit__", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_r = -1;
  __pyx_L0:;
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}
```

</details>

L57  🟡  (score=2)
```python
        self.name = name
```
<details><summary>Show generated C (score=2)</summary>

```c
  __Pyx_INCREF(__pyx_v_name);
  __Pyx_GIVEREF(__pyx_v_name);
  __Pyx_GOTREF(__pyx_v_self->name);
  __Pyx_DECREF(__pyx_v_self->name);
  __pyx_v_self->name = __pyx_v_name;
```

</details>

L58  🟡  (score=2)
```python
        self.start = line
```
<details><summary>Show generated C (score=2)</summary>

```c
  __pyx_t_1 = __Pyx_PyIndex_AsSsize_t(__pyx_v_line); if (unlikely((__pyx_t_1 == (Py_ssize_t)-1) && PyErr_Occurred())) __PYX_ERR(0, 58, __pyx_L1_error)
  __pyx_v_self->start = __pyx_t_1;
```

</details>

L59  🟡  (score=2)
```python
        self.filename = filename
```
<details><summary>Show generated C (score=2)</summary>

```c
  __Pyx_INCREF(__pyx_v_filename);
  __Pyx_GIVEREF(__pyx_v_filename);
  __Pyx_GOTREF(__pyx_v_self->filename);
  __Pyx_DECREF(__pyx_v_self->filename);
  __pyx_v_self->filename = __pyx_v_filename;
```

</details>

L60  🟡  (score=3)
```python
        self.refs = {} # id -> (count, [lineno])
```
<details><summary>Show generated C (score=3)</summary>

```c
  __pyx_t_2 = __Pyx_PyDict_NewPresized(0); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 60, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_GIVEREF(__pyx_t_2);
  __Pyx_GOTREF(__pyx_v_self->refs);
  __Pyx_DECREF(__pyx_v_self->refs);
  __pyx_v_self->refs = ((PyObject*)__pyx_t_2);
  __pyx_t_2 = 0;
```

</details>

L61  🟠  (score=6)
```python
        self.errors = []
```
<details><summary>Show generated C (score=6)</summary>

```c
  __pyx_t_2 = PyList_New(0); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 61, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_GIVEREF(__pyx_t_2);
  __Pyx_GOTREF(__pyx_v_self->errors);
  __Pyx_DECREF(__pyx_v_self->errors);
  __pyx_v_self->errors = ((PyObject*)__pyx_t_2);
  __pyx_t_2 = 0;
```

</details>

L62  ⚪  (score=0)
```python
```
L63  ⚪  (score=0)
```python
    cdef void acquire_lock(self) noexcept:
```
<details><summary>Show generated C (score=0)</summary>

```c
static void __pyx_f_6Cython_7Runtime_8refnanny_7Context_acquire_lock(struct __pyx_obj_6Cython_7Runtime_8refnanny_Context *__pyx_v_self) {
/* … */
  /* function exit code */
}
```

</details>

L64  ⚪  (score=0)
```python
        __Pyx_refnanny_lock_acquire(&self.lock)
```
<details><summary>Show generated C (score=0)</summary>

```c
  __Pyx_refnanny_lock_acquire((&__pyx_v_self->lock));
```

</details>

L65  ⚪  (score=0)
```python
```
L66  ⚪  (score=0)
```python
    cdef void release_lock(self) noexcept:
```
<details><summary>Show generated C (score=0)</summary>

```c
static void __pyx_f_6Cython_7Runtime_8refnanny_7Context_release_lock(struct __pyx_obj_6Cython_7Runtime_8refnanny_Context *__pyx_v_self) {
/* … */
  /* function exit code */
}
```

</details>

L67  ⚪  (score=0)
```python
        __Pyx_refnanny_lock_release(&self.lock)
```
<details><summary>Show generated C (score=0)</summary>

```c
  __Pyx_refnanny_lock_release((&__pyx_v_self->lock));
```

</details>

L68  ⚪  (score=0)
```python
```
L69  🟠  (score=9)
```python
    cdef int regref(self, obj, Py_ssize_t lineno, bint is_null) except -1:
```
<details><summary>Show generated C (score=9)</summary>

```c
static int __pyx_f_6Cython_7Runtime_8refnanny_7Context_regref(struct __pyx_obj_6Cython_7Runtime_8refnanny_Context *__pyx_v_self, PyObject *__pyx_v_obj, Py_ssize_t __pyx_v_lineno, int __pyx_v_is_null) {
  PyObject *__pyx_v_id_ = NULL;
  PyObject *__pyx_v_count = NULL;
  PyObject *__pyx_v_linenumbers = NULL;
  int __pyx_r;
/* … */
  /* function exit code */
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_t_1);
  __Pyx_XDECREF(__pyx_t_2);
  __Pyx_XDECREF(__pyx_t_6);
  __Pyx_XDECREF(__pyx_t_7);
  __Pyx_AddTraceback("Cython.Runtime.refnanny.Context.regref", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_r = -1;
  __pyx_L0:;
  __Pyx_XDECREF(__pyx_v_id_);
  __Pyx_XDECREF(__pyx_v_count);
  __Pyx_XDECREF(__pyx_v_linenumbers);
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}
```

</details>

L70  🟠  (score=9)
```python
        log(_LOG_ALL, u'regref', u"<NULL>" if is_null else obj, lineno)
```
<details><summary>Show generated C (score=9)</summary>

```c
  if (__pyx_v_is_null) {
    __Pyx_INCREF(__pyx_mstate_global->__pyx_kp_u_NULL);
    __pyx_t_1 = __pyx_mstate_global->__pyx_kp_u_NULL;
  } else {
    __Pyx_INCREF(__pyx_v_obj);
    __pyx_t_1 = __pyx_v_obj;
  }
  __pyx_t_2 = PyLong_FromSsize_t(__pyx_v_lineno); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 70, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __pyx_t_3 = __pyx_f_6Cython_7Runtime_8refnanny_log(__pyx_v_6Cython_7Runtime_8refnanny__LOG_ALL, __pyx_mstate_global->__pyx_n_u_regref, __pyx_t_1, __pyx_t_2); if (unlikely(__pyx_t_3 == ((int)-1))) __PYX_ERR(0, 70, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
```

</details>

L71  ⚪  (score=0)
```python
        if is_null:
```
<details><summary>Show generated C (score=0)</summary>

```c
  if (__pyx_v_is_null) {
/* … */
  }
```

</details>

L72  🔴  (score=13)
```python
            self.errors.append(f"NULL argument on line {lineno}")
```
<details><summary>Show generated C (score=13)</summary>

```c
    if (unlikely(__pyx_v_self->errors == Py_None)) {
      PyErr_Format(PyExc_AttributeError, "'NoneType' object has no attribute '%.30s'", "append");
      __PYX_ERR(0, 72, __pyx_L1_error)
    }
    __pyx_t_2 = __Pyx_PyUnicode_From_Py_ssize_t(__pyx_v_lineno, 0, ' ', 'd'); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 72, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_2);
    __pyx_t_1 = __Pyx_PyUnicode_Concat(__pyx_mstate_global->__pyx_kp_u_NULL_argument_on_line, __pyx_t_2); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 72, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_1);
    __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
    __pyx_t_4 = __Pyx_PyList_Append(__pyx_v_self->errors, __pyx_t_1); if (unlikely(__pyx_t_4 == ((int)-1))) __PYX_ERR(0, 72, __pyx_L1_error)
    __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
```

</details>

L73  ⚪  (score=0)
```python
            return 0
```
<details><summary>Show generated C (score=0)</summary>

```c
    __pyx_r = 0;
    goto __pyx_L0;
```

</details>

L74  🟡  (score=3)
```python
        id_ = id(obj)
```
<details><summary>Show generated C (score=3)</summary>

```c
  __pyx_t_2 = NULL;
  __pyx_t_5 = 1;
  {
    PyObject *__pyx_callargs[2] = {__pyx_t_2, __pyx_v_obj};
    __pyx_t_1 = __Pyx_PyObject_FastCall((PyObject*)__pyx_builtin_id, __pyx_callargs+__pyx_t_5, (2-__pyx_t_5) | (__pyx_t_5*__Pyx_PY_VECTORCALL_ARGUMENTS_OFFSET));
    __Pyx_XDECREF(__pyx_t_2); __pyx_t_2 = 0;
    if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 74, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_1);
  }
  __pyx_v_id_ = __pyx_t_1;
  __pyx_t_1 = 0;
```

</details>

L75  🔴  (score=57)
```python
        count, linenumbers = self.refs.get(id_, NO_REFS)
```
<details><summary>Show generated C (score=57)</summary>

```c
  if (unlikely(__pyx_v_self->refs == Py_None)) {
    PyErr_Format(PyExc_AttributeError, "'NoneType' object has no attribute '%.30s'", "get");
    __PYX_ERR(0, 75, __pyx_L1_error)
  }
  __pyx_t_1 = __Pyx_PyDict_GetItemDefault(__pyx_v_self->refs, __pyx_v_id_, __pyx_v_6Cython_7Runtime_8refnanny_NO_REFS); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 75, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  if ((likely(PyTuple_CheckExact(__pyx_t_1))) || (PyList_CheckExact(__pyx_t_1))) {
    PyObject* sequence = __pyx_t_1;
    Py_ssize_t size = __Pyx_PySequence_SIZE(sequence);
    if (unlikely(size != 2)) {
      if (size > 2) __Pyx_RaiseTooManyValuesError(2);
      else if (size >= 0) __Pyx_RaiseNeedMoreValuesError(size);
      __PYX_ERR(0, 75, __pyx_L1_error)
    }
    #if CYTHON_ASSUME_SAFE_MACROS && !CYTHON_AVOID_BORROWED_REFS
    if (likely(PyTuple_CheckExact(sequence))) {
      __pyx_t_2 = PyTuple_GET_ITEM(sequence, 0);
      __Pyx_INCREF(__pyx_t_2);
      __pyx_t_6 = PyTuple_GET_ITEM(sequence, 1);
      __Pyx_INCREF(__pyx_t_6);
    } else {
      __pyx_t_2 = __Pyx_PyList_GetItemRefFast(sequence, 0, __Pyx_ReferenceSharing_SharedReference);
      if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 75, __pyx_L1_error)
      __Pyx_XGOTREF(__pyx_t_2);
      __pyx_t_6 = __Pyx_PyList_GetItemRefFast(sequence, 1, __Pyx_ReferenceSharing_SharedReference);
      if (unlikely(!__pyx_t_6)) __PYX_ERR(0, 75, __pyx_L1_error)
      __Pyx_XGOTREF(__pyx_t_6);
    }
    #else
    __pyx_t_2 = __Pyx_PySequence_ITEM(sequence, 0); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 75, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_2);
    __pyx_t_6 = __Pyx_PySequence_ITEM(sequence, 1); if (unlikely(!__pyx_t_6)) __PYX_ERR(0, 75, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_6);
    #endif
    __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  } else {
    Py_ssize_t index = -1;
    __pyx_t_7 = PyObject_GetIter(__pyx_t_1); if (unlikely(!__pyx_t_7)) __PYX_ERR(0, 75, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_7);
    __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
    __pyx_t_8 = (CYTHON_COMPILING_IN_LIMITED_API) ? PyIter_Next : __Pyx_PyObject_GetIterNextFunc(__pyx_t_7);
    index = 0; __pyx_t_2 = __pyx_t_8(__pyx_t_7); if (unlikely(!__pyx_t_2)) goto __pyx_L4_unpacking_failed;
    __Pyx_GOTREF(__pyx_t_2);
    index = 1; __pyx_t_6 = __pyx_t_8(__pyx_t_7); if (unlikely(!__pyx_t_6)) goto __pyx_L4_unpacking_failed;
    __Pyx_GOTREF(__pyx_t_6);
    if (__Pyx_IternextUnpackEndCheck(__pyx_t_8(__pyx_t_7), 2) < (0)) __PYX_ERR(0, 75, __pyx_L1_error)
    __pyx_t_8 = NULL;
    __Pyx_DECREF(__pyx_t_7); __pyx_t_7 = 0;
    goto __pyx_L5_unpacking_done;
    __pyx_L4_unpacking_failed:;
    __Pyx_DECREF(__pyx_t_7); __pyx_t_7 = 0;
    __pyx_t_8 = NULL;
    if (__Pyx_IterFinish() == 0) __Pyx_RaiseNeedMoreValuesError(index);
    __PYX_ERR(0, 75, __pyx_L1_error)
    __pyx_L5_unpacking_done:;
  }
  __pyx_v_count = __pyx_t_2;
  __pyx_t_2 = 0;
  __pyx_v_linenumbers = __pyx_t_6;
  __pyx_t_6 = 0;
```

</details>

L76  ⚪  (score=0)
```python
        if linenumbers is None:
```
<details><summary>Show generated C (score=0)</summary>

```c
  __pyx_t_9 = (__pyx_v_linenumbers == Py_None);
  if (__pyx_t_9) {
/* … */
  }
```

</details>

L77  🟠  (score=6)
```python
            linenumbers = []
```
<details><summary>Show generated C (score=6)</summary>

```c
    __pyx_t_1 = PyList_New(0); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 77, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_1);
    __Pyx_DECREF_SET(__pyx_v_linenumbers, __pyx_t_1);
    __pyx_t_1 = 0;
```

</details>

L78  🔴  (score=23)
```python
        self.refs[id_] = (count + 1, linenumbers)
```
<details><summary>Show generated C (score=23)</summary>

```c
  __pyx_t_1 = __Pyx_PyLong_AddObjC(__pyx_v_count, __pyx_mstate_global->__pyx_int_1, 1, 0, 0); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 78, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __pyx_t_6 = PyTuple_New(2); if (unlikely(!__pyx_t_6)) __PYX_ERR(0, 78, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_6);
  __Pyx_GIVEREF(__pyx_t_1);
  if (__Pyx_PyTuple_SET_ITEM(__pyx_t_6, 0, __pyx_t_1) != (0)) __PYX_ERR(0, 78, __pyx_L1_error);
  __Pyx_INCREF(__pyx_v_linenumbers);
  __Pyx_GIVEREF(__pyx_v_linenumbers);
  if (__Pyx_PyTuple_SET_ITEM(__pyx_t_6, 1, __pyx_v_linenumbers) != (0)) __PYX_ERR(0, 78, __pyx_L1_error);
  __pyx_t_1 = 0;
  if (unlikely(__pyx_v_self->refs == Py_None)) {
    PyErr_SetString(PyExc_TypeError, "'NoneType' object is not subscriptable");
    __PYX_ERR(0, 78, __pyx_L1_error)
  }
  if (unlikely((PyDict_SetItem(__pyx_v_self->refs, __pyx_v_id_, __pyx_t_6) < 0))) __PYX_ERR(0, 78, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_6); __pyx_t_6 = 0;
```

</details>

L79  🟠  (score=8)
```python
        linenumbers.append(lineno)
```
<details><summary>Show generated C (score=8)</summary>

```c
  __pyx_t_6 = PyLong_FromSsize_t(__pyx_v_lineno); if (unlikely(!__pyx_t_6)) __PYX_ERR(0, 79, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_6);
  __pyx_t_4 = __Pyx_PyObject_Append(__pyx_v_linenumbers, __pyx_t_6); if (unlikely(__pyx_t_4 == ((int)-1))) __PYX_ERR(0, 79, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_6); __pyx_t_6 = 0;
```

</details>

L80  ⚪  (score=0)
```python
        return 0
```
<details><summary>Show generated C (score=0)</summary>

```c
  __pyx_r = 0;
  goto __pyx_L0;
```

</details>

L81  ⚪  (score=0)
```python
```
L82  🟠  (score=9)
```python
    cdef bint delref(self, obj, Py_ssize_t lineno, bint is_null) except -1:
```
<details><summary>Show generated C (score=9)</summary>

```c
static int __pyx_f_6Cython_7Runtime_8refnanny_7Context_delref(struct __pyx_obj_6Cython_7Runtime_8refnanny_Context *__pyx_v_self, PyObject *__pyx_v_obj, Py_ssize_t __pyx_v_lineno, int __pyx_v_is_null) {
  PyObject *__pyx_v_id_ = NULL;
  PyObject *__pyx_v_count = NULL;
  PyObject *__pyx_v_linenumbers = NULL;
  int __pyx_r;
/* … */
  /* function exit code */
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_t_1);
  __Pyx_XDECREF(__pyx_t_2);
  __Pyx_XDECREF(__pyx_t_6);
  __Pyx_XDECREF(__pyx_t_7);
  __Pyx_AddTraceback("Cython.Runtime.refnanny.Context.delref", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_r = -1;
  __pyx_L0:;
  __Pyx_XDECREF(__pyx_v_id_);
  __Pyx_XDECREF(__pyx_v_count);
  __Pyx_XDECREF(__pyx_v_linenumbers);
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}
```

</details>

L83  ⚪  (score=0)
```python
        # returns whether it is ok to do the decref operation
```
L84  🟠  (score=9)
```python
        log(_LOG_ALL, u'delref', u"<NULL>" if is_null else obj, lineno)
```
<details><summary>Show generated C (score=9)</summary>

```c
  if (__pyx_v_is_null) {
    __Pyx_INCREF(__pyx_mstate_global->__pyx_kp_u_NULL);
    __pyx_t_1 = __pyx_mstate_global->__pyx_kp_u_NULL;
  } else {
    __Pyx_INCREF(__pyx_v_obj);
    __pyx_t_1 = __pyx_v_obj;
  }
  __pyx_t_2 = PyLong_FromSsize_t(__pyx_v_lineno); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 84, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __pyx_t_3 = __pyx_f_6Cython_7Runtime_8refnanny_log(__pyx_v_6Cython_7Runtime_8refnanny__LOG_ALL, __pyx_mstate_global->__pyx_n_u_delref, __pyx_t_1, __pyx_t_2); if (unlikely(__pyx_t_3 == ((int)-1))) __PYX_ERR(0, 84, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
```

</details>

L85  ⚪  (score=0)
```python
        if is_null:
```
<details><summary>Show generated C (score=0)</summary>

```c
  if (__pyx_v_is_null) {
/* … */
  }
```

</details>

L86  🔴  (score=13)
```python
            self.errors.append(f"NULL argument on line {lineno}")
```
<details><summary>Show generated C (score=13)</summary>

```c
    if (unlikely(__pyx_v_self->errors == Py_None)) {
      PyErr_Format(PyExc_AttributeError, "'NoneType' object has no attribute '%.30s'", "append");
      __PYX_ERR(0, 86, __pyx_L1_error)
    }
    __pyx_t_2 = __Pyx_PyUnicode_From_Py_ssize_t(__pyx_v_lineno, 0, ' ', 'd'); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 86, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_2);
    __pyx_t_1 = __Pyx_PyUnicode_Concat(__pyx_mstate_global->__pyx_kp_u_NULL_argument_on_line, __pyx_t_2); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 86, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_1);
    __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
    __pyx_t_4 = __Pyx_PyList_Append(__pyx_v_self->errors, __pyx_t_1); if (unlikely(__pyx_t_4 == ((int)-1))) __PYX_ERR(0, 86, __pyx_L1_error)
    __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
```

</details>

L87  ⚪  (score=0)
```python
            return False
```
<details><summary>Show generated C (score=0)</summary>

```c
    __pyx_r = 0;
    goto __pyx_L0;
```

</details>

L88  🟡  (score=3)
```python
        id_ = id(obj)
```
<details><summary>Show generated C (score=3)</summary>

```c
  __pyx_t_2 = NULL;
  __pyx_t_5 = 1;
  {
    PyObject *__pyx_callargs[2] = {__pyx_t_2, __pyx_v_obj};
    __pyx_t_1 = __Pyx_PyObject_FastCall((PyObject*)__pyx_builtin_id, __pyx_callargs+__pyx_t_5, (2-__pyx_t_5) | (__pyx_t_5*__Pyx_PY_VECTORCALL_ARGUMENTS_OFFSET));
    __Pyx_XDECREF(__pyx_t_2); __pyx_t_2 = 0;
    if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 88, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_1);
  }
  __pyx_v_id_ = __pyx_t_1;
  __pyx_t_1 = 0;
```

</details>

L89  🔴  (score=57)
```python
        count, linenumbers = self.refs.get(id_, NO_REFS)
```
<details><summary>Show generated C (score=57)</summary>

```c
  if (unlikely(__pyx_v_self->refs == Py_None)) {
    PyErr_Format(PyExc_AttributeError, "'NoneType' object has no attribute '%.30s'", "get");
    __PYX_ERR(0, 89, __pyx_L1_error)
  }
  __pyx_t_1 = __Pyx_PyDict_GetItemDefault(__pyx_v_self->refs, __pyx_v_id_, __pyx_v_6Cython_7Runtime_8refnanny_NO_REFS); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 89, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  if ((likely(PyTuple_CheckExact(__pyx_t_1))) || (PyList_CheckExact(__pyx_t_1))) {
    PyObject* sequence = __pyx_t_1;
    Py_ssize_t size = __Pyx_PySequence_SIZE(sequence);
    if (unlikely(size != 2)) {
      if (size > 2) __Pyx_RaiseTooManyValuesError(2);
      else if (size >= 0) __Pyx_RaiseNeedMoreValuesError(size);
      __PYX_ERR(0, 89, __pyx_L1_error)
    }
    #if CYTHON_ASSUME_SAFE_MACROS && !CYTHON_AVOID_BORROWED_REFS
    if (likely(PyTuple_CheckExact(sequence))) {
      __pyx_t_2 = PyTuple_GET_ITEM(sequence, 0);
      __Pyx_INCREF(__pyx_t_2);
      __pyx_t_6 = PyTuple_GET_ITEM(sequence, 1);
      __Pyx_INCREF(__pyx_t_6);
    } else {
      __pyx_t_2 = __Pyx_PyList_GetItemRefFast(sequence, 0, __Pyx_ReferenceSharing_SharedReference);
      if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 89, __pyx_L1_error)
      __Pyx_XGOTREF(__pyx_t_2);
      __pyx_t_6 = __Pyx_PyList_GetItemRefFast(sequence, 1, __Pyx_ReferenceSharing_SharedReference);
      if (unlikely(!__pyx_t_6)) __PYX_ERR(0, 89, __pyx_L1_error)
      __Pyx_XGOTREF(__pyx_t_6);
    }
    #else
    __pyx_t_2 = __Pyx_PySequence_ITEM(sequence, 0); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 89, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_2);
    __pyx_t_6 = __Pyx_PySequence_ITEM(sequence, 1); if (unlikely(!__pyx_t_6)) __PYX_ERR(0, 89, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_6);
    #endif
    __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  } else {
    Py_ssize_t index = -1;
    __pyx_t_7 = PyObject_GetIter(__pyx_t_1); if (unlikely(!__pyx_t_7)) __PYX_ERR(0, 89, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_7);
    __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
    __pyx_t_8 = (CYTHON_COMPILING_IN_LIMITED_API) ? PyIter_Next : __Pyx_PyObject_GetIterNextFunc(__pyx_t_7);
    index = 0; __pyx_t_2 = __pyx_t_8(__pyx_t_7); if (unlikely(!__pyx_t_2)) goto __pyx_L4_unpacking_failed;
    __Pyx_GOTREF(__pyx_t_2);
    index = 1; __pyx_t_6 = __pyx_t_8(__pyx_t_7); if (unlikely(!__pyx_t_6)) goto __pyx_L4_unpacking_failed;
    __Pyx_GOTREF(__pyx_t_6);
    if (__Pyx_IternextUnpackEndCheck(__pyx_t_8(__pyx_t_7), 2) < (0)) __PYX_ERR(0, 89, __pyx_L1_error)
    __pyx_t_8 = NULL;
    __Pyx_DECREF(__pyx_t_7); __pyx_t_7 = 0;
    goto __pyx_L5_unpacking_done;
    __pyx_L4_unpacking_failed:;
    __Pyx_DECREF(__pyx_t_7); __pyx_t_7 = 0;
    __pyx_t_8 = NULL;
    if (__Pyx_IterFinish() == 0) __Pyx_RaiseNeedMoreValuesError(index);
    __PYX_ERR(0, 89, __pyx_L1_error)
    __pyx_L5_unpacking_done:;
  }
  __pyx_v_count = __pyx_t_2;
  __pyx_t_2 = 0;
  __pyx_v_linenumbers = __pyx_t_6;
  __pyx_t_6 = 0;
```

</details>

L90  ⚪  (score=0)
```python
        if linenumbers is None:
```
<details><summary>Show generated C (score=0)</summary>

```c
  __pyx_t_9 = (__pyx_v_linenumbers == Py_None);
  if (__pyx_t_9) {
/* … */
  }
```

</details>

L91  🟠  (score=6)
```python
            linenumbers = []
```
<details><summary>Show generated C (score=6)</summary>

```c
    __pyx_t_1 = PyList_New(0); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 91, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_1);
    __Pyx_DECREF_SET(__pyx_v_linenumbers, __pyx_t_1);
    __pyx_t_1 = 0;
```

</details>

L92  🟡  (score=2)
```python
        if count == 0:
```
<details><summary>Show generated C (score=2)</summary>

```c
  __pyx_t_9 = (__Pyx_PyLong_BoolEqObjC(__pyx_v_count, __pyx_mstate_global->__pyx_int_0, 0, 0)); if (unlikely((__pyx_t_9 < 0))) __PYX_ERR(0, 92, __pyx_L1_error)
  if (__pyx_t_9) {
/* … */
  }
```

</details>

L93  🔴  (score=27)
```python
            self.errors.append(f"Too many decrefs on line {lineno}, reference acquired on lines {linenumbers!r}")
```
<details><summary>Show generated C (score=27)</summary>

```c
    if (unlikely(__pyx_v_self->errors == Py_None)) {
      PyErr_Format(PyExc_AttributeError, "'NoneType' object has no attribute '%.30s'", "append");
      __PYX_ERR(0, 93, __pyx_L1_error)
    }
    __pyx_t_1 = __Pyx_PyUnicode_From_Py_ssize_t(__pyx_v_lineno, 0, ' ', 'd'); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 93, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_1);
    __pyx_t_6 = __Pyx_PyObject_FormatSimpleAndDecref(PyObject_Repr(__pyx_v_linenumbers), __pyx_mstate_global->__pyx_empty_unicode); if (unlikely(!__pyx_t_6)) __PYX_ERR(0, 93, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_6);
    __pyx_t_10[0] = __pyx_mstate_global->__pyx_kp_u_Too_many_decrefs_on_line;
    __pyx_t_10[1] = __pyx_t_1;
    __pyx_t_10[2] = __pyx_mstate_global->__pyx_kp_u_reference_acquired_on_lines;
    __pyx_t_10[3] = __pyx_t_6;
    __pyx_t_2 = __Pyx_PyUnicode_Join(__pyx_t_10, 4, 25 + __Pyx_PyUnicode_GET_LENGTH(__pyx_t_1) + 30 + __Pyx_PyUnicode_GET_LENGTH(__pyx_t_6), 127 | __Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_6));
    if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 93, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_2);
    __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
    __Pyx_DECREF(__pyx_t_6); __pyx_t_6 = 0;
    __pyx_t_4 = __Pyx_PyList_Append(__pyx_v_self->errors, __pyx_t_2); if (unlikely(__pyx_t_4 == ((int)-1))) __PYX_ERR(0, 93, __pyx_L1_error)
    __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
```

</details>

L94  ⚪  (score=0)
```python
            return False
```
<details><summary>Show generated C (score=0)</summary>

```c
    __pyx_r = 0;
    goto __pyx_L0;
```

</details>

L95  🟡  (score=2)
```python
        if count == 1:
```
<details><summary>Show generated C (score=2)</summary>

```c
  __pyx_t_9 = (__Pyx_PyLong_BoolEqObjC(__pyx_v_count, __pyx_mstate_global->__pyx_int_1, 1, 0)); if (unlikely((__pyx_t_9 < 0))) __PYX_ERR(0, 95, __pyx_L1_error)
  if (__pyx_t_9) {
/* … */
    goto __pyx_L8;
  }
```

</details>

L96  🔴  (score=10)
```python
            del self.refs[id_]
```
<details><summary>Show generated C (score=10)</summary>

```c
    if (unlikely(__pyx_v_self->refs == Py_None)) {
      PyErr_SetString(PyExc_TypeError, "'NoneType' object is not subscriptable");
      __PYX_ERR(0, 96, __pyx_L1_error)
    }
    if (unlikely((PyDict_DelItem(__pyx_v_self->refs, __pyx_v_id_) < 0))) __PYX_ERR(0, 96, __pyx_L1_error)
```

</details>

L97  ⚪  (score=0)
```python
        else:
```
L98  🔴  (score=23)
```python
            self.refs[id_] = (count - 1, linenumbers)
```
<details><summary>Show generated C (score=23)</summary>

```c
  /*else*/ {
    __pyx_t_2 = __Pyx_PyLong_SubtractObjC(__pyx_v_count, __pyx_mstate_global->__pyx_int_1, 1, 0, 0); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 98, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_2);
    __pyx_t_6 = PyTuple_New(2); if (unlikely(!__pyx_t_6)) __PYX_ERR(0, 98, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_6);
    __Pyx_GIVEREF(__pyx_t_2);
    if (__Pyx_PyTuple_SET_ITEM(__pyx_t_6, 0, __pyx_t_2) != (0)) __PYX_ERR(0, 98, __pyx_L1_error);
    __Pyx_INCREF(__pyx_v_linenumbers);
    __Pyx_GIVEREF(__pyx_v_linenumbers);
    if (__Pyx_PyTuple_SET_ITEM(__pyx_t_6, 1, __pyx_v_linenumbers) != (0)) __PYX_ERR(0, 98, __pyx_L1_error);
    __pyx_t_2 = 0;
    if (unlikely(__pyx_v_self->refs == Py_None)) {
      PyErr_SetString(PyExc_TypeError, "'NoneType' object is not subscriptable");
      __PYX_ERR(0, 98, __pyx_L1_error)
    }
    if (unlikely((PyDict_SetItem(__pyx_v_self->refs, __pyx_v_id_, __pyx_t_6) < 0))) __PYX_ERR(0, 98, __pyx_L1_error)
    __Pyx_DECREF(__pyx_t_6); __pyx_t_6 = 0;
  }
  __pyx_L8:;
```

</details>

L99  ⚪  (score=0)
```python
        return True
```
<details><summary>Show generated C (score=0)</summary>

```c
  __pyx_r = 1;
  goto __pyx_L0;
```

</details>

L100  ⚪  (score=0)
```python
```
L101  🔴  (score=12)
```python
    cdef end(self):
```
<details><summary>Show generated C (score=12)</summary>

```c
static PyObject *__pyx_f_6Cython_7Runtime_8refnanny_7Context_end(struct __pyx_obj_6Cython_7Runtime_8refnanny_Context *__pyx_v_self) {
  PyObject *__pyx_v_msg = NULL;
  PyObject *__pyx_v_count = NULL;
  PyObject *__pyx_v_linenos = NULL;
  PyObject *__pyx_7genexpr__pyx_v_x = NULL;
  PyObject *__pyx_8genexpr1__pyx_v_error = NULL;
  PyObject *__pyx_r = NULL;
/* … */
  /* function exit code */
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_t_2);
  __Pyx_XDECREF(__pyx_t_6);
  __Pyx_XDECREF(__pyx_t_8);
  __Pyx_XDECREF(__pyx_t_9);
  __Pyx_XDECREF(__pyx_t_10);
  __Pyx_AddTraceback("Cython.Runtime.refnanny.Context.end", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_r = 0;
  __pyx_L0:;
  __Pyx_XDECREF(__pyx_v_msg);
  __Pyx_XDECREF(__pyx_v_count);
  __Pyx_XDECREF(__pyx_v_linenos);
  __Pyx_XDECREF(__pyx_7genexpr__pyx_v_x);
  __Pyx_XDECREF(__pyx_8genexpr1__pyx_v_error);
  __Pyx_XGIVEREF(__pyx_r);
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}
```

</details>

L102  🟡  (score=2)
```python
        if self.refs:
```
<details><summary>Show generated C (score=2)</summary>

```c
  __pyx_t_1 = __Pyx_PyObject_IsTrue(__pyx_v_self->refs); if (unlikely((__pyx_t_1 < 0))) __PYX_ERR(0, 102, __pyx_L1_error)
  if (__pyx_t_1) {
/* … */
  }
```

</details>

L103  🟡  (score=1)
```python
            msg = u"References leaked:"
```
<details><summary>Show generated C (score=1)</summary>

```c
    __Pyx_INCREF(__pyx_mstate_global->__pyx_kp_u_References_leaked);
    __pyx_v_msg = __pyx_mstate_global->__pyx_kp_u_References_leaked;
```

</details>

L104  🔴  (score=58)
```python
            for count, linenos in self.refs.values():
```
<details><summary>Show generated C (score=58)</summary>

```c
    __pyx_t_3 = 0;
    if (unlikely(__pyx_v_self->refs == Py_None)) {
      PyErr_Format(PyExc_AttributeError, "'NoneType' object has no attribute '%.30s'", "values");
      __PYX_ERR(0, 104, __pyx_L1_error)
    }
    __pyx_t_6 = __Pyx_dict_iterator(__pyx_v_self->refs, 1, __pyx_mstate_global->__pyx_n_u_values, (&__pyx_t_4), (&__pyx_t_5)); if (unlikely(!__pyx_t_6)) __PYX_ERR(0, 104, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_6);
    __Pyx_XDECREF(__pyx_t_2);
    __pyx_t_2 = __pyx_t_6;
    __pyx_t_6 = 0;
    while (1) {
      __pyx_t_7 = __Pyx_dict_iter_next(__pyx_t_2, __pyx_t_4, &__pyx_t_3, NULL, &__pyx_t_6, NULL, __pyx_t_5);
      if (unlikely(__pyx_t_7 == 0)) break;
      if (unlikely(__pyx_t_7 == -1)) __PYX_ERR(0, 104, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_6);
      if ((likely(PyTuple_CheckExact(__pyx_t_6))) || (PyList_CheckExact(__pyx_t_6))) {
        PyObject* sequence = __pyx_t_6;
        Py_ssize_t size = __Pyx_PySequence_SIZE(sequence);
        if (unlikely(size != 2)) {
          if (size > 2) __Pyx_RaiseTooManyValuesError(2);
          else if (size >= 0) __Pyx_RaiseNeedMoreValuesError(size);
          __PYX_ERR(0, 104, __pyx_L1_error)
        }
        #if CYTHON_ASSUME_SAFE_MACROS && !CYTHON_AVOID_BORROWED_REFS
        if (likely(PyTuple_CheckExact(sequence))) {
          __pyx_t_8 = PyTuple_GET_ITEM(sequence, 0);
          __Pyx_INCREF(__pyx_t_8);
          __pyx_t_9 = PyTuple_GET_ITEM(sequence, 1);
          __Pyx_INCREF(__pyx_t_9);
        } else {
          __pyx_t_8 = __Pyx_PyList_GetItemRefFast(sequence, 0, __Pyx_ReferenceSharing_SharedReference);
          if (unlikely(!__pyx_t_8)) __PYX_ERR(0, 104, __pyx_L1_error)
          __Pyx_XGOTREF(__pyx_t_8);
          __pyx_t_9 = __Pyx_PyList_GetItemRefFast(sequence, 1, __Pyx_ReferenceSharing_SharedReference);
          if (unlikely(!__pyx_t_9)) __PYX_ERR(0, 104, __pyx_L1_error)
          __Pyx_XGOTREF(__pyx_t_9);
        }
        #else
        __pyx_t_8 = __Pyx_PySequence_ITEM(sequence, 0); if (unlikely(!__pyx_t_8)) __PYX_ERR(0, 104, __pyx_L1_error)
        __Pyx_GOTREF(__pyx_t_8);
        __pyx_t_9 = __Pyx_PySequence_ITEM(sequence, 1); if (unlikely(!__pyx_t_9)) __PYX_ERR(0, 104, __pyx_L1_error)
        __Pyx_GOTREF(__pyx_t_9);
        #endif
        __Pyx_DECREF(__pyx_t_6); __pyx_t_6 = 0;
      } else {
        Py_ssize_t index = -1;
        __pyx_t_10 = PyObject_GetIter(__pyx_t_6); if (unlikely(!__pyx_t_10)) __PYX_ERR(0, 104, __pyx_L1_error)
        __Pyx_GOTREF(__pyx_t_10);
        __Pyx_DECREF(__pyx_t_6); __pyx_t_6 = 0;
        __pyx_t_11 = (CYTHON_COMPILING_IN_LIMITED_API) ? PyIter_Next : __Pyx_PyObject_GetIterNextFunc(__pyx_t_10);
        index = 0; __pyx_t_8 = __pyx_t_11(__pyx_t_10); if (unlikely(!__pyx_t_8)) goto __pyx_L6_unpacking_failed;
        __Pyx_GOTREF(__pyx_t_8);
        index = 1; __pyx_t_9 = __pyx_t_11(__pyx_t_10); if (unlikely(!__pyx_t_9)) goto __pyx_L6_unpacking_failed;
        __Pyx_GOTREF(__pyx_t_9);
        if (__Pyx_IternextUnpackEndCheck(__pyx_t_11(__pyx_t_10), 2) < (0)) __PYX_ERR(0, 104, __pyx_L1_error)
        __pyx_t_11 = NULL;
        __Pyx_DECREF(__pyx_t_10); __pyx_t_10 = 0;
        goto __pyx_L7_unpacking_done;
        __pyx_L6_unpacking_failed:;
        __Pyx_DECREF(__pyx_t_10); __pyx_t_10 = 0;
        __pyx_t_11 = NULL;
        if (__Pyx_IterFinish() == 0) __Pyx_RaiseNeedMoreValuesError(index);
        __PYX_ERR(0, 104, __pyx_L1_error)
        __pyx_L7_unpacking_done:;
      }
      __Pyx_XDECREF_SET(__pyx_v_count, __pyx_t_8);
      __pyx_t_8 = 0;
      __Pyx_XDECREF_SET(__pyx_v_linenos, __pyx_t_9);
      __pyx_t_9 = 0;
```

</details>

L105  🔴  (score=85)
```python
                msg += f"\n  ({count}) acquired on lines: {u', '.join([f'{x}' for x in linenos])}"
```
<details><summary>Show generated C (score=85)</summary>

```c
      __pyx_t_6 = __Pyx_PyObject_FormatSimple(__pyx_v_count, __pyx_mstate_global->__pyx_empty_unicode); if (unlikely(!__pyx_t_6)) __PYX_ERR(0, 105, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_6);
      { /* enter inner scope */
        __pyx_t_9 = PyList_New(0); if (unlikely(!__pyx_t_9)) __PYX_ERR(0, 105, __pyx_L10_error)
        __Pyx_GOTREF(__pyx_t_9);
        if (likely(PyList_CheckExact(__pyx_v_linenos)) || PyTuple_CheckExact(__pyx_v_linenos)) {
          __pyx_t_8 = __pyx_v_linenos; __Pyx_INCREF(__pyx_t_8);
          __pyx_t_12 = 0;
          __pyx_t_13 = NULL;
        } else {
          __pyx_t_12 = -1; __pyx_t_8 = PyObject_GetIter(__pyx_v_linenos); if (unlikely(!__pyx_t_8)) __PYX_ERR(0, 105, __pyx_L10_error)
          __Pyx_GOTREF(__pyx_t_8);
          __pyx_t_13 = (CYTHON_COMPILING_IN_LIMITED_API) ? PyIter_Next : __Pyx_PyObject_GetIterNextFunc(__pyx_t_8); if (unlikely(!__pyx_t_13)) __PYX_ERR(0, 105, __pyx_L10_error)
        }
        for (;;) {
          if (likely(!__pyx_t_13)) {
            if (likely(PyList_CheckExact(__pyx_t_8))) {
              {
                Py_ssize_t __pyx_temp = __Pyx_PyList_GET_SIZE(__pyx_t_8);
                #if !CYTHON_ASSUME_SAFE_SIZE
                if (unlikely((__pyx_temp < 0))) __PYX_ERR(0, 105, __pyx_L10_error)
                #endif
                if (__pyx_t_12 >= __pyx_temp) break;
              }
              __pyx_t_10 = __Pyx_PyList_GetItemRefFast(__pyx_t_8, __pyx_t_12, __Pyx_ReferenceSharing_OwnStrongReference);
              ++__pyx_t_12;
            } else {
              {
                Py_ssize_t __pyx_temp = __Pyx_PyTuple_GET_SIZE(__pyx_t_8);
                #if !CYTHON_ASSUME_SAFE_SIZE
                if (unlikely((__pyx_temp < 0))) __PYX_ERR(0, 105, __pyx_L10_error)
                #endif
                if (__pyx_t_12 >= __pyx_temp) break;
              }
              #if CYTHON_ASSUME_SAFE_MACROS && !CYTHON_AVOID_BORROWED_REFS
              __pyx_t_10 = __Pyx_NewRef(PyTuple_GET_ITEM(__pyx_t_8, __pyx_t_12));
              #else
              __pyx_t_10 = __Pyx_PySequence_ITEM(__pyx_t_8, __pyx_t_12);
              #endif
              ++__pyx_t_12;
            }
            if (unlikely(!__pyx_t_10)) __PYX_ERR(0, 105, __pyx_L10_error)
          } else {
            __pyx_t_10 = __pyx_t_13(__pyx_t_8);
            if (unlikely(!__pyx_t_10)) {
              PyObject* exc_type = PyErr_Occurred();
              if (exc_type) {
                if (unlikely(!__Pyx_PyErr_GivenExceptionMatches(exc_type, PyExc_StopIteration))) __PYX_ERR(0, 105, __pyx_L10_error)
                PyErr_Clear();
              }
              break;
            }
          }
          __Pyx_GOTREF(__pyx_t_10);
          __Pyx_XDECREF_SET(__pyx_7genexpr__pyx_v_x, __pyx_t_10);
          __pyx_t_10 = 0;
          __pyx_t_10 = __Pyx_PyObject_FormatSimple(__pyx_7genexpr__pyx_v_x, __pyx_mstate_global->__pyx_empty_unicode); if (unlikely(!__pyx_t_10)) __PYX_ERR(0, 105, __pyx_L10_error)
          __Pyx_GOTREF(__pyx_t_10);
          if (unlikely(__Pyx_ListComp_Append(__pyx_t_9, (PyObject*)__pyx_t_10))) __PYX_ERR(0, 105, __pyx_L10_error)
          __Pyx_DECREF(__pyx_t_10); __pyx_t_10 = 0;
        }
        __Pyx_DECREF(__pyx_t_8); __pyx_t_8 = 0;
        __Pyx_XDECREF(__pyx_7genexpr__pyx_v_x); __pyx_7genexpr__pyx_v_x = 0;
        goto __pyx_L14_exit_scope;
        __pyx_L10_error:;
        __Pyx_XDECREF(__pyx_7genexpr__pyx_v_x); __pyx_7genexpr__pyx_v_x = 0;
        goto __pyx_L1_error;
        __pyx_L14_exit_scope:;
      } /* exit inner scope */
      __pyx_t_8 = PyUnicode_Join(__pyx_mstate_global->__pyx_kp_u__2, __pyx_t_9); if (unlikely(!__pyx_t_8)) __PYX_ERR(0, 105, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_8);
      __Pyx_DECREF(__pyx_t_9); __pyx_t_9 = 0;
      __pyx_t_14[0] = __pyx_mstate_global->__pyx_kp_u_;
      __pyx_t_14[1] = __pyx_t_6;
      __pyx_t_14[2] = __pyx_mstate_global->__pyx_kp_u_acquired_on_lines;
      __pyx_t_14[3] = __pyx_t_8;
      __pyx_t_9 = __Pyx_PyUnicode_Join(__pyx_t_14, 4, 4 + __Pyx_PyUnicode_GET_LENGTH(__pyx_t_6) + 21 + __Pyx_PyUnicode_GET_LENGTH(__pyx_t_8), 127 | __Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_6) | __Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_8));
      if (unlikely(!__pyx_t_9)) __PYX_ERR(0, 105, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_9);
      __Pyx_DECREF(__pyx_t_6); __pyx_t_6 = 0;
      __Pyx_DECREF(__pyx_t_8); __pyx_t_8 = 0;
      __pyx_t_8 = __Pyx_PyUnicode_Concat__Pyx_ReferenceSharing_OwnStrongReferenceInPlace(__pyx_v_msg, __pyx_t_9); if (unlikely(!__pyx_t_8)) __PYX_ERR(0, 105, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_8);
      __Pyx_DECREF(__pyx_t_9); __pyx_t_9 = 0;
      __Pyx_DECREF_SET(__pyx_v_msg, ((PyObject*)__pyx_t_8));
      __pyx_t_8 = 0;
    }
    __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
```

</details>

L106  🟠  (score=7)
```python
            self.errors.append(msg)
```
<details><summary>Show generated C (score=7)</summary>

```c
    if (unlikely(__pyx_v_self->errors == Py_None)) {
      PyErr_Format(PyExc_AttributeError, "'NoneType' object has no attribute '%.30s'", "append");
      __PYX_ERR(0, 106, __pyx_L1_error)
    }
    __pyx_t_15 = __Pyx_PyList_Append(__pyx_v_self->errors, __pyx_v_msg); if (unlikely(__pyx_t_15 == ((int)-1))) __PYX_ERR(0, 106, __pyx_L1_error)
```

</details>

L107  🔴  (score=37)
```python
        return u"\n".join([f'REFNANNY: {error}' for error in self.errors]) if self.errors else None
```
<details><summary>Show generated C (score=37)</summary>

```c
  __Pyx_XDECREF(__pyx_r);
  if (__pyx_v_self->errors == Py_None) __pyx_t_1 = 0;
  else
  {
    Py_ssize_t __pyx_temp = __Pyx_PyList_GET_SIZE(__pyx_v_self->errors);
    if (unlikely(((!CYTHON_ASSUME_SAFE_SIZE) && __pyx_temp < 0))) __PYX_ERR(0, 107, __pyx_L1_error)
    __pyx_t_1 = (__pyx_temp != 0);
  }

  if (__pyx_t_1) {
    { /* enter inner scope */
      __pyx_t_8 = PyList_New(0); if (unlikely(!__pyx_t_8)) __PYX_ERR(0, 107, __pyx_L17_error)
      __Pyx_GOTREF(__pyx_t_8);
      if (unlikely(__pyx_v_self->errors == Py_None)) {
        PyErr_SetString(PyExc_TypeError, "'NoneType' object is not iterable");
        __PYX_ERR(0, 107, __pyx_L17_error)
      }
      __pyx_t_9 = __pyx_v_self->errors; __Pyx_INCREF(__pyx_t_9);
      __pyx_t_4 = 0;
      for (;;) {
        {
          Py_ssize_t __pyx_temp = __Pyx_PyList_GET_SIZE(__pyx_t_9);
          #if !CYTHON_ASSUME_SAFE_SIZE
          if (unlikely((__pyx_temp < 0))) __PYX_ERR(0, 107, __pyx_L17_error)
          #endif
          if (__pyx_t_4 >= __pyx_temp) break;
        }
        __pyx_t_6 = __Pyx_PyList_GetItemRefFast(__pyx_t_9, __pyx_t_4, __Pyx_ReferenceSharing_OwnStrongReference);
        ++__pyx_t_4;
        if (unlikely(!__pyx_t_6)) __PYX_ERR(0, 107, __pyx_L17_error)
        __Pyx_GOTREF(__pyx_t_6);
        __Pyx_XDECREF_SET(__pyx_8genexpr1__pyx_v_error, __pyx_t_6);
        __pyx_t_6 = 0;
        __pyx_t_6 = __Pyx_PyObject_FormatSimple(__pyx_8genexpr1__pyx_v_error, __pyx_mstate_global->__pyx_empty_unicode); if (unlikely(!__pyx_t_6)) __PYX_ERR(0, 107, __pyx_L17_error)
        __Pyx_GOTREF(__pyx_t_6);
        __pyx_t_10 = __Pyx_PyUnicode_Concat(__pyx_mstate_global->__pyx_kp_u_REFNANNY, __pyx_t_6); if (unlikely(!__pyx_t_10)) __PYX_ERR(0, 107, __pyx_L17_error)
        __Pyx_GOTREF(__pyx_t_10);
        __Pyx_DECREF(__pyx_t_6); __pyx_t_6 = 0;
        if (unlikely(__Pyx_ListComp_Append(__pyx_t_8, (PyObject*)__pyx_t_10))) __PYX_ERR(0, 107, __pyx_L17_error)
        __Pyx_DECREF(__pyx_t_10); __pyx_t_10 = 0;
      }
      __Pyx_DECREF(__pyx_t_9); __pyx_t_9 = 0;
      __Pyx_XDECREF(__pyx_8genexpr1__pyx_v_error); __pyx_8genexpr1__pyx_v_error = 0;
      goto __pyx_L21_exit_scope;
      __pyx_L17_error:;
      __Pyx_XDECREF(__pyx_8genexpr1__pyx_v_error); __pyx_8genexpr1__pyx_v_error = 0;
      goto __pyx_L1_error;
      __pyx_L21_exit_scope:;
    } /* exit inner scope */
    __pyx_t_9 = PyUnicode_Join(__pyx_mstate_global->__pyx_kp_u__3, __pyx_t_8); if (unlikely(!__pyx_t_9)) __PYX_ERR(0, 107, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_9);
    __Pyx_DECREF(__pyx_t_8); __pyx_t_8 = 0;
    __pyx_t_2 = __pyx_t_9;
    __pyx_t_9 = 0;
  } else {
    __Pyx_INCREF(Py_None);
    __pyx_t_2 = Py_None;
  }
  __pyx_r = __pyx_t_2;
  __pyx_t_2 = 0;
  goto __pyx_L0;
```

</details>

L108  ⚪  (score=0)
```python
```
L109  ⚪  (score=0)
```python
```
L110  🟡  (score=3)
```python
cdef void report_unraisable(filename, Py_ssize_t lineno, object e=None) noexcept:
```
<details><summary>Show generated C (score=3)</summary>

```c
static void __pyx_f_6Cython_7Runtime_8refnanny_report_unraisable(PyObject *__pyx_v_filename, Py_ssize_t __pyx_v_lineno, struct __pyx_opt_args_6Cython_7Runtime_8refnanny_report_unraisable *__pyx_optional_args) {
  PyObject *__pyx_v_e = ((PyObject *)Py_None);
  PyObject *__pyx_v_sys = NULL;
  if (__pyx_optional_args) {
    if (__pyx_optional_args->__pyx_n > 0) {
      __pyx_v_e = __pyx_optional_args->e;
    }
  }
  __Pyx_INCREF(__pyx_v_e);
/* … */
  /* function exit code */
  __pyx_L0:;
  __Pyx_XDECREF(__pyx_v_sys);
  __Pyx_XDECREF(__pyx_v_e);
  __Pyx_RefNannyFinishContext();
}
/* … */
struct __pyx_opt_args_6Cython_7Runtime_8refnanny_report_unraisable {
  int __pyx_n;
  PyObject *e;
};
```

</details>

L111  ⚪  (score=0)
```python
    try:
```
<details><summary>Show generated C (score=0)</summary>

```c
  /*try:*/ {
```

</details>

L112  ⚪  (score=0)
```python
        if e is None:
```
<details><summary>Show generated C (score=0)</summary>

```c
    __pyx_t_1 = (__pyx_v_e == Py_None);
    if (__pyx_t_1) {
/* … */
    }
```

</details>

L113  🟡  (score=2)
```python
            import sys
```
<details><summary>Show generated C (score=2)</summary>

```c
      __pyx_t_3 = __Pyx_Import(__pyx_mstate_global->__pyx_n_u_sys, 0, 0, NULL, 0); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 113, __pyx_L4_error)
      __pyx_t_2 = __pyx_t_3;
      __Pyx_GOTREF(__pyx_t_2);
      __pyx_v_sys = __pyx_t_2;
      __pyx_t_2 = 0;
```

</details>

L114  🟠  (score=8)
```python
            e = sys.exc_info()[1]
```
<details><summary>Show generated C (score=8)</summary>

```c
      __pyx_t_4 = __pyx_v_sys;
      __Pyx_INCREF(__pyx_t_4);
      __pyx_t_5 = 0;
      {
        PyObject *__pyx_callargs[2] = {__pyx_t_4, NULL};
        __pyx_t_2 = __Pyx_PyObject_FastCallMethod((PyObject*)__pyx_mstate_global->__pyx_n_u_exc_info, __pyx_callargs+__pyx_t_5, (1-__pyx_t_5) | (1*__Pyx_PY_VECTORCALL_ARGUMENTS_OFFSET));
        __Pyx_XDECREF(__pyx_t_4); __pyx_t_4 = 0;
        if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 114, __pyx_L4_error)
        __Pyx_GOTREF(__pyx_t_2);
      }
      __pyx_t_4 = __Pyx_GetItemInt(__pyx_t_2, 1, long, 1, __Pyx_PyLong_From_long, 0, 0, 1, 1, __Pyx_ReferenceSharing_OwnStrongReference); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 114, __pyx_L4_error)
      __Pyx_GOTREF(__pyx_t_4);
      __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
      __Pyx_DECREF_SET(__pyx_v_e, __pyx_t_4);
      __pyx_t_4 = 0;
```

</details>

L115  🔴  (score=26)
```python
        print(f"refnanny raised an exception from {filename}:{lineno}: {e}")
```
<details><summary>Show generated C (score=26)</summary>

```c
    __pyx_t_2 = NULL;
    __pyx_t_6 = __Pyx_PyObject_FormatSimple(__pyx_v_filename, __pyx_mstate_global->__pyx_empty_unicode); if (unlikely(!__pyx_t_6)) __PYX_ERR(0, 115, __pyx_L4_error)
    __Pyx_GOTREF(__pyx_t_6);
    __pyx_t_7 = __Pyx_PyUnicode_From_Py_ssize_t(__pyx_v_lineno, 0, ' ', 'd'); if (unlikely(!__pyx_t_7)) __PYX_ERR(0, 115, __pyx_L4_error)
    __Pyx_GOTREF(__pyx_t_7);
    __pyx_t_8 = __Pyx_PyObject_FormatSimple(__pyx_v_e, __pyx_mstate_global->__pyx_empty_unicode); if (unlikely(!__pyx_t_8)) __PYX_ERR(0, 115, __pyx_L4_error)
    __Pyx_GOTREF(__pyx_t_8);
    __pyx_t_9[0] = __pyx_mstate_global->__pyx_kp_u_refnanny_raised_an_exception_fro;
    __pyx_t_9[1] = __pyx_t_6;
    __pyx_t_9[2] = __pyx_mstate_global->__pyx_kp_u__4;
    __pyx_t_9[3] = __pyx_t_7;
    __pyx_t_9[4] = __pyx_mstate_global->__pyx_kp_u__5;
    __pyx_t_9[5] = __pyx_t_8;
    __pyx_t_10 = __Pyx_PyUnicode_Join(__pyx_t_9, 6, 34 + __Pyx_PyUnicode_GET_LENGTH(__pyx_t_6) + 1 + __Pyx_PyUnicode_GET_LENGTH(__pyx_t_7) + 2 + __Pyx_PyUnicode_GET_LENGTH(__pyx_t_8), 127 | __Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_6) | __Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_8));
    if (unlikely(!__pyx_t_10)) __PYX_ERR(0, 115, __pyx_L4_error)
    __Pyx_GOTREF(__pyx_t_10);
    __Pyx_DECREF(__pyx_t_6); __pyx_t_6 = 0;
    __Pyx_DECREF(__pyx_t_7); __pyx_t_7 = 0;
    __Pyx_DECREF(__pyx_t_8); __pyx_t_8 = 0;
    __pyx_t_5 = 1;
    {
      PyObject *__pyx_callargs[2] = {__pyx_t_2, __pyx_t_10};
      __pyx_t_4 = __Pyx_PyObject_FastCall((PyObject*)__pyx_builtin_print, __pyx_callargs+__pyx_t_5, (2-__pyx_t_5) | (__pyx_t_5*__Pyx_PY_VECTORCALL_ARGUMENTS_OFFSET));
      __Pyx_XDECREF(__pyx_t_2); __pyx_t_2 = 0;
      __Pyx_DECREF(__pyx_t_10); __pyx_t_10 = 0;
      if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 115, __pyx_L4_error)
      __Pyx_GOTREF(__pyx_t_4);
    }
    __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
  }
```

</details>

L116  ⚪  (score=0)
```python
    finally:
```
L117  🔴  (score=17)
```python
        return  # We absolutely cannot exit with an exception
```
<details><summary>Show generated C (score=17)</summary>

```c
  /*finally:*/ {
    /*normal exit:*/{
      goto __pyx_L0;
    }
    __pyx_L4_error:;
    /*exception exit:*/{
      __Pyx_PyThreadState_declare
      __Pyx_PyThreadState_assign
      __pyx_t_3 = 0; __pyx_t_11 = 0; __pyx_t_12 = 0; __pyx_t_13 = 0; __pyx_t_14 = 0; __pyx_t_15 = 0;
      __Pyx_XDECREF(__pyx_t_10); __pyx_t_10 = 0;
      __Pyx_XDECREF(__pyx_t_2); __pyx_t_2 = 0;
      __Pyx_XDECREF(__pyx_t_4); __pyx_t_4 = 0;
      __Pyx_XDECREF(__pyx_t_6); __pyx_t_6 = 0;
      __Pyx_XDECREF(__pyx_t_7); __pyx_t_7 = 0;
      __Pyx_XDECREF(__pyx_t_8); __pyx_t_8 = 0;
       __Pyx_ExceptionSwap(&__pyx_t_13, &__pyx_t_14, &__pyx_t_15);
      if ( unlikely(__Pyx_GetException(&__pyx_t_3, &__pyx_t_11, &__pyx_t_12) < 0)) __Pyx_ErrFetch(&__pyx_t_3, &__pyx_t_11, &__pyx_t_12);
      __Pyx_XGOTREF(__pyx_t_3);
      __Pyx_XGOTREF(__pyx_t_11);
      __Pyx_XGOTREF(__pyx_t_12);
      __Pyx_XGOTREF(__pyx_t_13);
      __Pyx_XGOTREF(__pyx_t_14);
      __Pyx_XGOTREF(__pyx_t_15);
      {
        goto __pyx_L7_return;
      }
      __pyx_L7_return:;
      __Pyx_XGIVEREF(__pyx_t_13);
      __Pyx_XGIVEREF(__pyx_t_14);
      __Pyx_XGIVEREF(__pyx_t_15);
      __Pyx_ExceptionReset(__pyx_t_13, __pyx_t_14, __pyx_t_15);
      __Pyx_XDECREF(__pyx_t_3); __pyx_t_3 = 0;
      __Pyx_XDECREF(__pyx_t_11); __pyx_t_11 = 0;
      __Pyx_XDECREF(__pyx_t_12); __pyx_t_12 = 0;
      __pyx_t_13 = 0; __pyx_t_14 = 0; __pyx_t_15 = 0;
      goto __pyx_L0;
    }
  }
```

</details>

L118  ⚪  (score=0)
```python
```
L119  ⚪  (score=0)
```python
```
L120  ⚪  (score=0)
```python
# All Python operations must happen after any existing
```
L121  ⚪  (score=0)
```python
# exception has been fetched, in case we are called from
```
L122  ⚪  (score=0)
```python
# exception-handling code.
```
L123  ⚪  (score=0)
```python
```
L124  🟠  (score=8)
```python
cdef PyObject* SetupContext(char* funcname, Py_ssize_t lineno, char* filename) except NULL:
```
<details><summary>Show generated C (score=8)</summary>

```c
static PyObject *__pyx_f_6Cython_7Runtime_8refnanny_SetupContext(char *__pyx_v_funcname, Py_ssize_t __pyx_v_lineno, char *__pyx_v_filename) {
  PyObject *__pyx_v_type;
  PyObject *__pyx_v_value;
  PyObject *__pyx_v_tb;
  PyObject *__pyx_v_result;
  PyObject *__pyx_v_ctx = NULL;
  PyObject *__pyx_v_e = NULL;
  PyObject *__pyx_r;
/* … */
  /* function exit code */
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_t_5);
  __Pyx_XDECREF(__pyx_t_6);
  __Pyx_XDECREF(__pyx_t_7);
  __Pyx_XDECREF(__pyx_t_8);
  __Pyx_AddTraceback("Cython.Runtime.refnanny.SetupContext", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_r = NULL;
  __pyx_L0:;
  __Pyx_XDECREF(__pyx_v_ctx);
  __Pyx_XDECREF(__pyx_v_e);
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}
```

</details>

L125  ⚪  (score=0)
```python
    if Context is None:
```
<details><summary>Show generated C (score=0)</summary>

```c
  __pyx_t_1 = (__pyx_mstate_global->__pyx_ptype_6Cython_7Runtime_8refnanny_Context == ((PyTypeObject*)Py_None));
  if (__pyx_t_1) {
/* … */
  }
```

</details>

L126  ⚪  (score=0)
```python
        # Context may be None during finalize phase.
```
L127  ⚪  (score=0)
```python
        # In that case, we don't want to be doing anything fancy
```
L128  ⚪  (score=0)
```python
        # like caching and resetting exceptions.
```
L129  ⚪  (score=0)
```python
        return NULL
```
<details><summary>Show generated C (score=0)</summary>

```c
    __pyx_r = NULL;
    goto __pyx_L0;
```

</details>

L130  ⚪  (score=0)
```python
    cdef (PyObject*) type = NULL, value = NULL, tb = NULL, result = NULL
```
<details><summary>Show generated C (score=0)</summary>

```c
  __pyx_v_type = NULL;
  __pyx_v_value = NULL;
  __pyx_v_tb = NULL;
  __pyx_v_result = NULL;
```

</details>

L131  ⚪  (score=0)
```python
    PyThreadState_Get()  # Check that we hold the GIL
```
<details><summary>Show generated C (score=0)</summary>

```c
  (void)(PyThreadState_Get());
```

</details>

L132  🟠  (score=5)
```python
    PyErr_Fetch(&type, &value, &tb)
```
<details><summary>Show generated C (score=5)</summary>

```c
  PyErr_Fetch((&__pyx_v_type), (&__pyx_v_value), (&__pyx_v_tb));
```

</details>

L133  🔴  (score=11)
```python
    try:
```
<details><summary>Show generated C (score=11)</summary>

```c
  {
    /*try:*/ {
/* … */
    }
    __Pyx_XDECREF(__pyx_t_2); __pyx_t_2 = 0;
    __Pyx_XDECREF(__pyx_t_3); __pyx_t_3 = 0;
    __Pyx_XDECREF(__pyx_t_4); __pyx_t_4 = 0;
    goto __pyx_L9_try_end;
    __pyx_L4_error:;
    __Pyx_XDECREF(__pyx_t_5); __pyx_t_5 = 0;
    __Pyx_XDECREF(__pyx_t_6); __pyx_t_6 = 0;
    __Pyx_XDECREF(__pyx_t_7); __pyx_t_7 = 0;
    __Pyx_XDECREF(__pyx_t_8); __pyx_t_8 = 0;
/* … */
    __pyx_L6_except_error:;
    __Pyx_XGIVEREF(__pyx_t_2);
    __Pyx_XGIVEREF(__pyx_t_3);
    __Pyx_XGIVEREF(__pyx_t_4);
    __Pyx_ExceptionReset(__pyx_t_2, __pyx_t_3, __pyx_t_4);
    goto __pyx_L1_error;
    __pyx_L5_exception_handled:;
    __Pyx_XGIVEREF(__pyx_t_2);
    __Pyx_XGIVEREF(__pyx_t_3);
    __Pyx_XGIVEREF(__pyx_t_4);
    __Pyx_ExceptionReset(__pyx_t_2, __pyx_t_3, __pyx_t_4);
    __pyx_L9_try_end:;
  }
```

</details>

L134  🔴  (score=21)
```python
        ctx = Context.__new__(Context, funcname, lineno, filename)
```
<details><summary>Show generated C (score=21)</summary>

```c
      __pyx_t_5 = __Pyx_PyBytes_FromString(__pyx_v_funcname); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 134, __pyx_L4_error)
      __Pyx_GOTREF(__pyx_t_5);
      __pyx_t_6 = PyLong_FromSsize_t(__pyx_v_lineno); if (unlikely(!__pyx_t_6)) __PYX_ERR(0, 134, __pyx_L4_error)
      __Pyx_GOTREF(__pyx_t_6);
      __pyx_t_7 = __Pyx_PyBytes_FromString(__pyx_v_filename); if (unlikely(!__pyx_t_7)) __PYX_ERR(0, 134, __pyx_L4_error)
      __Pyx_GOTREF(__pyx_t_7);
      __pyx_t_8 = PyTuple_New(3); if (unlikely(!__pyx_t_8)) __PYX_ERR(0, 134, __pyx_L4_error)
      __Pyx_GOTREF(__pyx_t_8);
      __Pyx_GIVEREF(__pyx_t_5);
      if (__Pyx_PyTuple_SET_ITEM(__pyx_t_8, 0, __pyx_t_5) != (0)) __PYX_ERR(0, 134, __pyx_L4_error);
      __Pyx_GIVEREF(__pyx_t_6);
      if (__Pyx_PyTuple_SET_ITEM(__pyx_t_8, 1, __pyx_t_6) != (0)) __PYX_ERR(0, 134, __pyx_L4_error);
      __Pyx_GIVEREF(__pyx_t_7);
      if (__Pyx_PyTuple_SET_ITEM(__pyx_t_8, 2, __pyx_t_7) != (0)) __PYX_ERR(0, 134, __pyx_L4_error);
      __pyx_t_5 = 0;
      __pyx_t_6 = 0;
      __pyx_t_7 = 0;
      __pyx_t_7 = ((PyObject *)__pyx_tp_new_6Cython_7Runtime_8refnanny_Context(((PyTypeObject *)__pyx_mstate_global->__pyx_ptype_6Cython_7Runtime_8refnanny_Context), __pyx_t_8, NULL)); if (unlikely(!__pyx_t_7)) __PYX_ERR(0, 134, __pyx_L4_error)
      __Pyx_GOTREF((PyObject *)__pyx_t_7);
      __Pyx_DECREF(__pyx_t_8); __pyx_t_8 = 0;
      __pyx_v_ctx = ((PyObject *)__pyx_t_7);
      __pyx_t_7 = 0;
```

</details>

L135  ⚪  (score=0)
```python
        Py_INCREF(ctx)
```
<details><summary>Show generated C (score=0)</summary>

```c
      Py_INCREF(__pyx_v_ctx);
```

</details>

L136  ⚪  (score=0)
```python
        result = <PyObject*>ctx
```
<details><summary>Show generated C (score=0)</summary>

```c
      __pyx_v_result = ((PyObject *)__pyx_v_ctx);
```

</details>

L137  🟠  (score=7)
```python
    except Exception, e:
```
<details><summary>Show generated C (score=7)</summary>

```c
    __pyx_t_9 = __Pyx_PyErr_ExceptionMatches(((PyObject *)(((PyTypeObject*)PyExc_Exception))));
    if (__pyx_t_9) {
      __Pyx_AddTraceback("Cython.Runtime.refnanny.SetupContext", __pyx_clineno, __pyx_lineno, __pyx_filename);
      if (__Pyx_GetException(&__pyx_t_7, &__pyx_t_8, &__pyx_t_6) < 0) __PYX_ERR(0, 137, __pyx_L6_except_error)
      __Pyx_XGOTREF(__pyx_t_7);
      __Pyx_XGOTREF(__pyx_t_8);
      __Pyx_XGOTREF(__pyx_t_6);
      __Pyx_INCREF(__pyx_t_8);
      __pyx_v_e = __pyx_t_8;
```

</details>

L138  🟠  (score=6)
```python
        report_unraisable(filename, lineno, e)
```
<details><summary>Show generated C (score=6)</summary>

```c
      __pyx_t_5 = __Pyx_PyBytes_FromString(__pyx_v_filename); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 138, __pyx_L6_except_error)
      __Pyx_GOTREF(__pyx_t_5);
      __pyx_t_10.__pyx_n = 1;
      __pyx_t_10.e = __pyx_v_e;
      __pyx_f_6Cython_7Runtime_8refnanny_report_unraisable(__pyx_t_5, __pyx_v_lineno, &__pyx_t_10); 
      __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
      __Pyx_XDECREF(__pyx_t_7); __pyx_t_7 = 0;
      __Pyx_XDECREF(__pyx_t_8); __pyx_t_8 = 0;
      __Pyx_XDECREF(__pyx_t_6); __pyx_t_6 = 0;
      goto __pyx_L5_exception_handled;
    }
    goto __pyx_L6_except_error;
```

</details>

L139  🟠  (score=5)
```python
    PyErr_Restore(type, value, tb)
```
<details><summary>Show generated C (score=5)</summary>

```c
  PyErr_Restore(__pyx_v_type, __pyx_v_value, __pyx_v_tb);
```

</details>

L140  ⚪  (score=0)
```python
    return result
```
<details><summary>Show generated C (score=0)</summary>

```c
  __pyx_r = __pyx_v_result;
  goto __pyx_L0;
```

</details>

L141  ⚪  (score=0)
```python
```
L142  🟡  (score=1)
```python
cdef void GOTREF(PyObject* _ctx, PyObject* p_obj, Py_ssize_t lineno):
```
<details><summary>Show generated C (score=1)</summary>

```c
static void __pyx_f_6Cython_7Runtime_8refnanny_GOTREF(PyObject *__pyx_v__ctx, PyObject *__pyx_v_p_obj, Py_ssize_t __pyx_v_lineno) {
  PyObject *__pyx_v_type;
  PyObject *__pyx_v_value;
  PyObject *__pyx_v_tb;
  struct __pyx_obj_6Cython_7Runtime_8refnanny_Context *__pyx_v_ctx = 0;
/* … */
  /* function exit code */
  __pyx_L0:;
  __Pyx_XDECREF((PyObject *)__pyx_v_ctx);
  __Pyx_RefNannyFinishContext();
}
```

</details>

L143  ⚪  (score=0)
```python
    if _ctx == NULL: return
```
<details><summary>Show generated C (score=0)</summary>

```c
  __pyx_t_1 = (__pyx_v__ctx == NULL);
  if (__pyx_t_1) {
    goto __pyx_L0;
  }
```

</details>

L144  ⚪  (score=0)
```python
    cdef (PyObject*) type = NULL, value = NULL, tb = NULL
```
<details><summary>Show generated C (score=0)</summary>

```c
  __pyx_v_type = NULL;
  __pyx_v_value = NULL;
  __pyx_v_tb = NULL;
```

</details>

L145  🟡  (score=1)
```python
    cdef Context ctx = <Context> _ctx
```
<details><summary>Show generated C (score=1)</summary>

```c
  __pyx_t_2 = ((PyObject *)__pyx_v__ctx);
  __Pyx_INCREF(__pyx_t_2);
  __pyx_v_ctx = ((struct __pyx_obj_6Cython_7Runtime_8refnanny_Context *)__pyx_t_2);
  __pyx_t_2 = 0;
```

</details>

L146  ⚪  (score=0)
```python
    ctx.acquire_lock()
```
<details><summary>Show generated C (score=0)</summary>

```c
  __pyx_f_6Cython_7Runtime_8refnanny_7Context_acquire_lock(__pyx_v_ctx);
```

</details>

L147  🟠  (score=5)
```python
    PyErr_Fetch(&type, &value, &tb)
```
<details><summary>Show generated C (score=5)</summary>

```c
  PyErr_Fetch((&__pyx_v_type), (&__pyx_v_value), (&__pyx_v_tb));
```

</details>

L148  🟠  (score=8)
```python
    try:
```
<details><summary>Show generated C (score=8)</summary>

```c
  /*try:*/ {
    {
      /*try:*/ {
/* … */
      }
      __Pyx_XDECREF(__pyx_t_3); __pyx_t_3 = 0;
      __Pyx_XDECREF(__pyx_t_4); __pyx_t_4 = 0;
      __Pyx_XDECREF(__pyx_t_5); __pyx_t_5 = 0;
      goto __pyx_L12_try_end;
      __pyx_L7_error:;
      __Pyx_XDECREF(__pyx_t_2); __pyx_t_2 = 0;
/* … */
      __pyx_L9_except_error:;
      __Pyx_XGIVEREF(__pyx_t_3);
      __Pyx_XGIVEREF(__pyx_t_4);
      __Pyx_XGIVEREF(__pyx_t_5);
      __Pyx_ExceptionReset(__pyx_t_3, __pyx_t_4, __pyx_t_5);
      goto __pyx_L5_error;
      __pyx_L8_exception_handled:;
      __Pyx_XGIVEREF(__pyx_t_3);
      __Pyx_XGIVEREF(__pyx_t_4);
      __Pyx_XGIVEREF(__pyx_t_5);
      __Pyx_ExceptionReset(__pyx_t_3, __pyx_t_4, __pyx_t_5);
      __pyx_L12_try_end:;
    }
  }
```

</details>

L149  🟡  (score=1)
```python
        ctx.regref(
```
<details><summary>Show generated C (score=1)</summary>

```c
        __pyx_t_6 = __pyx_f_6Cython_7Runtime_8refnanny_7Context_regref(__pyx_v_ctx, __pyx_t_2, __pyx_v_lineno, (__pyx_v_p_obj == NULL)); if (unlikely(__pyx_t_6 == ((int)-1))) __PYX_ERR(0, 149, __pyx_L7_error)
        __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
```

</details>

L150  🟡  (score=2)
```python
            <object>p_obj if p_obj is not NULL else None,
```
<details><summary>Show generated C (score=2)</summary>

```c
        __pyx_t_1 = (__pyx_v_p_obj != NULL);
        if (__pyx_t_1) {
          __Pyx_INCREF(((PyObject *)__pyx_v_p_obj));
          __pyx_t_2 = ((PyObject *)__pyx_v_p_obj);
        } else {
          __Pyx_INCREF(Py_None);
          __pyx_t_2 = Py_None;
        }
```

</details>

L151  ⚪  (score=0)
```python
            lineno,
```
L152  ⚪  (score=0)
```python
            is_null=p_obj is NULL,
```
L153  ⚪  (score=0)
```python
        )
```
L154  🟡  (score=4)
```python
    except:
```
<details><summary>Show generated C (score=4)</summary>

```c
      /*except:*/ {
        __Pyx_AddTraceback("Cython.Runtime.refnanny.GOTREF", __pyx_clineno, __pyx_lineno, __pyx_filename);
        if (__Pyx_GetException(&__pyx_t_2, &__pyx_t_7, &__pyx_t_8) < 0) __PYX_ERR(0, 154, __pyx_L9_except_error)
        __Pyx_XGOTREF(__pyx_t_2);
        __Pyx_XGOTREF(__pyx_t_7);
        __Pyx_XGOTREF(__pyx_t_8);
```

</details>

L155  🟠  (score=5)
```python
        report_unraisable(ctx.filename, lineno=ctx.start)
```
<details><summary>Show generated C (score=5)</summary>

```c
        __pyx_t_9 = __pyx_v_ctx->filename;
        __Pyx_INCREF(__pyx_t_9);
        __pyx_f_6Cython_7Runtime_8refnanny_report_unraisable(__pyx_t_9, __pyx_v_ctx->start, NULL);
        __Pyx_DECREF(__pyx_t_9); __pyx_t_9 = 0;
        __Pyx_XDECREF(__pyx_t_2); __pyx_t_2 = 0;
        __Pyx_XDECREF(__pyx_t_7); __pyx_t_7 = 0;
        __Pyx_XDECREF(__pyx_t_8); __pyx_t_8 = 0;
        goto __pyx_L8_exception_handled;
      }
```

</details>

L156  ⚪  (score=0)
```python
    finally:
```
L157  🔴  (score=10)
```python
        PyErr_Restore(type, value, tb)
```
<details><summary>Show generated C (score=10)</summary>

```c
  /*finally:*/ {
    /*normal exit:*/{
      PyErr_Restore(__pyx_v_type, __pyx_v_value, __pyx_v_tb);
/* … */
        PyErr_Restore(__pyx_v_type, __pyx_v_value, __pyx_v_tb);
```

</details>

L158  ⚪  (score=0)
```python
        ctx.release_lock()
```
<details><summary>Show generated C (score=0)</summary>

```c
      __pyx_f_6Cython_7Runtime_8refnanny_7Context_release_lock(__pyx_v_ctx);
/* … */
        __pyx_f_6Cython_7Runtime_8refnanny_7Context_release_lock(__pyx_v_ctx);
```

</details>

L159  🔴  (score=15)
```python
        return  # swallow any exceptions
```
<details><summary>Show generated C (score=15)</summary>

```c
      goto __pyx_L0;
    }
    __pyx_L5_error:;
    /*exception exit:*/{
      __Pyx_PyThreadState_declare
      __Pyx_PyThreadState_assign
      __pyx_t_5 = 0; __pyx_t_4 = 0; __pyx_t_3 = 0; __pyx_t_10 = 0; __pyx_t_11 = 0; __pyx_t_12 = 0;
      __Pyx_XDECREF(__pyx_t_2); __pyx_t_2 = 0;
      __Pyx_XDECREF(__pyx_t_7); __pyx_t_7 = 0;
      __Pyx_XDECREF(__pyx_t_8); __pyx_t_8 = 0;
      __Pyx_XDECREF(__pyx_t_9); __pyx_t_9 = 0;
       __Pyx_ExceptionSwap(&__pyx_t_10, &__pyx_t_11, &__pyx_t_12);
      if ( unlikely(__Pyx_GetException(&__pyx_t_5, &__pyx_t_4, &__pyx_t_3) < 0)) __Pyx_ErrFetch(&__pyx_t_5, &__pyx_t_4, &__pyx_t_3);
      __Pyx_XGOTREF(__pyx_t_5);
      __Pyx_XGOTREF(__pyx_t_4);
      __Pyx_XGOTREF(__pyx_t_3);
      __Pyx_XGOTREF(__pyx_t_10);
      __Pyx_XGOTREF(__pyx_t_11);
      __Pyx_XGOTREF(__pyx_t_12);
      {
/* … */
        goto __pyx_L15_return;
      }
      __pyx_L15_return:;
      __Pyx_XGIVEREF(__pyx_t_10);
      __Pyx_XGIVEREF(__pyx_t_11);
      __Pyx_XGIVEREF(__pyx_t_12);
      __Pyx_ExceptionReset(__pyx_t_10, __pyx_t_11, __pyx_t_12);
      __Pyx_XDECREF(__pyx_t_5); __pyx_t_5 = 0;
      __Pyx_XDECREF(__pyx_t_4); __pyx_t_4 = 0;
      __Pyx_XDECREF(__pyx_t_3); __pyx_t_3 = 0;
      __pyx_t_10 = 0; __pyx_t_11 = 0; __pyx_t_12 = 0;
      goto __pyx_L0;
    }
  }
```

</details>

L160  ⚪  (score=0)
```python
```
L161  🟡  (score=1)
```python
cdef bint GIVEREF_and_report(PyObject* _ctx, PyObject* p_obj, Py_ssize_t lineno):
```
<details><summary>Show generated C (score=1)</summary>

```c
static int __pyx_f_6Cython_7Runtime_8refnanny_GIVEREF_and_report(PyObject *__pyx_v__ctx, PyObject *__pyx_v_p_obj, Py_ssize_t __pyx_v_lineno) {
  PyObject *__pyx_v_type;
  PyObject *__pyx_v_value;
  PyObject *__pyx_v_tb;
  int __pyx_v_decref_ok;
  struct __pyx_obj_6Cython_7Runtime_8refnanny_Context *__pyx_v_ctx = 0;
  int __pyx_r;
/* … */
  /* function exit code */
  __pyx_L0:;
  __Pyx_XDECREF((PyObject *)__pyx_v_ctx);
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}
```

</details>

L162  ⚪  (score=0)
```python
    if _ctx == NULL: return 1
```
<details><summary>Show generated C (score=0)</summary>

```c
  __pyx_t_1 = (__pyx_v__ctx == NULL);
  if (__pyx_t_1) {
    __pyx_r = 1;
    goto __pyx_L0;
  }
```

</details>

L163  ⚪  (score=0)
```python
    cdef (PyObject*) type = NULL, value = NULL, tb = NULL
```
<details><summary>Show generated C (score=0)</summary>

```c
  __pyx_v_type = NULL;
  __pyx_v_value = NULL;
  __pyx_v_tb = NULL;
```

</details>

L164  ⚪  (score=0)
```python
    cdef bint decref_ok = False
```
<details><summary>Show generated C (score=0)</summary>

```c
  __pyx_v_decref_ok = 0;
```

</details>

L165  🟡  (score=1)
```python
    cdef Context ctx = <Context> _ctx
```
<details><summary>Show generated C (score=1)</summary>

```c
  __pyx_t_2 = ((PyObject *)__pyx_v__ctx);
  __Pyx_INCREF(__pyx_t_2);
  __pyx_v_ctx = ((struct __pyx_obj_6Cython_7Runtime_8refnanny_Context *)__pyx_t_2);
  __pyx_t_2 = 0;
```

</details>

L166  ⚪  (score=0)
```python
    ctx.acquire_lock()
```
<details><summary>Show generated C (score=0)</summary>

```c
  __pyx_f_6Cython_7Runtime_8refnanny_7Context_acquire_lock(__pyx_v_ctx);
```

</details>

L167  🟠  (score=5)
```python
    PyErr_Fetch(&type, &value, &tb)
```
<details><summary>Show generated C (score=5)</summary>

```c
  PyErr_Fetch((&__pyx_v_type), (&__pyx_v_value), (&__pyx_v_tb));
```

</details>

L168  🟠  (score=8)
```python
    try:
```
<details><summary>Show generated C (score=8)</summary>

```c
  /*try:*/ {
    {
      /*try:*/ {
/* … */
      }
      __Pyx_XDECREF(__pyx_t_3); __pyx_t_3 = 0;
      __Pyx_XDECREF(__pyx_t_4); __pyx_t_4 = 0;
      __Pyx_XDECREF(__pyx_t_5); __pyx_t_5 = 0;
      goto __pyx_L12_try_end;
      __pyx_L7_error:;
      __Pyx_XDECREF(__pyx_t_2); __pyx_t_2 = 0;
/* … */
      __pyx_L9_except_error:;
      __Pyx_XGIVEREF(__pyx_t_3);
      __Pyx_XGIVEREF(__pyx_t_4);
      __Pyx_XGIVEREF(__pyx_t_5);
      __Pyx_ExceptionReset(__pyx_t_3, __pyx_t_4, __pyx_t_5);
      goto __pyx_L5_error;
      __pyx_L8_exception_handled:;
      __Pyx_XGIVEREF(__pyx_t_3);
      __Pyx_XGIVEREF(__pyx_t_4);
      __Pyx_XGIVEREF(__pyx_t_5);
      __Pyx_ExceptionReset(__pyx_t_3, __pyx_t_4, __pyx_t_5);
      __pyx_L12_try_end:;
    }
  }
```

</details>

L169  🟡  (score=1)
```python
        decref_ok = ctx.delref(
```
<details><summary>Show generated C (score=1)</summary>

```c
        __pyx_t_1 = __pyx_f_6Cython_7Runtime_8refnanny_7Context_delref(__pyx_v_ctx, __pyx_t_2, __pyx_v_lineno, (__pyx_v_p_obj == NULL)); if (unlikely(__pyx_t_1 == ((int)-1))) __PYX_ERR(0, 169, __pyx_L7_error)
        __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
        __pyx_v_decref_ok = __pyx_t_1;
```

</details>

L170  🟡  (score=2)
```python
            <object>p_obj if p_obj is not NULL else None,
```
<details><summary>Show generated C (score=2)</summary>

```c
        __pyx_t_1 = (__pyx_v_p_obj != NULL);
        if (__pyx_t_1) {
          __Pyx_INCREF(((PyObject *)__pyx_v_p_obj));
          __pyx_t_2 = ((PyObject *)__pyx_v_p_obj);
        } else {
          __Pyx_INCREF(Py_None);
          __pyx_t_2 = Py_None;
        }
```

</details>

L171  ⚪  (score=0)
```python
            lineno,
```
L172  ⚪  (score=0)
```python
            is_null=p_obj is NULL,
```
L173  ⚪  (score=0)
```python
        )
```
L174  🟡  (score=4)
```python
    except:
```
<details><summary>Show generated C (score=4)</summary>

```c
      /*except:*/ {
        __Pyx_AddTraceback("Cython.Runtime.refnanny.GIVEREF_and_report", __pyx_clineno, __pyx_lineno, __pyx_filename);
        if (__Pyx_GetException(&__pyx_t_2, &__pyx_t_6, &__pyx_t_7) < 0) __PYX_ERR(0, 174, __pyx_L9_except_error)
        __Pyx_XGOTREF(__pyx_t_2);
        __Pyx_XGOTREF(__pyx_t_6);
        __Pyx_XGOTREF(__pyx_t_7);
```

</details>

L175  🟠  (score=5)
```python
        report_unraisable(ctx.filename, lineno=ctx.start)
```
<details><summary>Show generated C (score=5)</summary>

```c
        __pyx_t_8 = __pyx_v_ctx->filename;
        __Pyx_INCREF(__pyx_t_8);
        __pyx_f_6Cython_7Runtime_8refnanny_report_unraisable(__pyx_t_8, __pyx_v_ctx->start, NULL);
        __Pyx_DECREF(__pyx_t_8); __pyx_t_8 = 0;
        __Pyx_XDECREF(__pyx_t_2); __pyx_t_2 = 0;
        __Pyx_XDECREF(__pyx_t_6); __pyx_t_6 = 0;
        __Pyx_XDECREF(__pyx_t_7); __pyx_t_7 = 0;
        goto __pyx_L8_exception_handled;
      }
```

</details>

L176  ⚪  (score=0)
```python
    finally:
```
L177  🔴  (score=10)
```python
        PyErr_Restore(type, value, tb)
```
<details><summary>Show generated C (score=10)</summary>

```c
  /*finally:*/ {
    /*normal exit:*/{
      PyErr_Restore(__pyx_v_type, __pyx_v_value, __pyx_v_tb);
/* … */
        PyErr_Restore(__pyx_v_type, __pyx_v_value, __pyx_v_tb);
```

</details>

L178  ⚪  (score=0)
```python
        ctx.release_lock()
```
<details><summary>Show generated C (score=0)</summary>

```c
      __pyx_f_6Cython_7Runtime_8refnanny_7Context_release_lock(__pyx_v_ctx);
/* … */
        __pyx_f_6Cython_7Runtime_8refnanny_7Context_release_lock(__pyx_v_ctx);
```

</details>

L179  🔴  (score=15)
```python
        return decref_ok  # swallow any exceptions
```
<details><summary>Show generated C (score=15)</summary>

```c
      __pyx_r = __pyx_v_decref_ok;
      goto __pyx_L0;
    }
    __pyx_L5_error:;
    /*exception exit:*/{
      __Pyx_PyThreadState_declare
      __Pyx_PyThreadState_assign
      __pyx_t_5 = 0; __pyx_t_4 = 0; __pyx_t_3 = 0; __pyx_t_9 = 0; __pyx_t_10 = 0; __pyx_t_11 = 0;
      __Pyx_XDECREF(__pyx_t_2); __pyx_t_2 = 0;
      __Pyx_XDECREF(__pyx_t_6); __pyx_t_6 = 0;
      __Pyx_XDECREF(__pyx_t_7); __pyx_t_7 = 0;
      __Pyx_XDECREF(__pyx_t_8); __pyx_t_8 = 0;
       __Pyx_ExceptionSwap(&__pyx_t_9, &__pyx_t_10, &__pyx_t_11);
      if ( unlikely(__Pyx_GetException(&__pyx_t_5, &__pyx_t_4, &__pyx_t_3) < 0)) __Pyx_ErrFetch(&__pyx_t_5, &__pyx_t_4, &__pyx_t_3);
      __Pyx_XGOTREF(__pyx_t_5);
      __Pyx_XGOTREF(__pyx_t_4);
      __Pyx_XGOTREF(__pyx_t_3);
      __Pyx_XGOTREF(__pyx_t_9);
      __Pyx_XGOTREF(__pyx_t_10);
      __Pyx_XGOTREF(__pyx_t_11);
      {
/* … */
        __pyx_r = __pyx_v_decref_ok;
        goto __pyx_L15_return;
      }
      __pyx_L15_return:;
      __Pyx_XGIVEREF(__pyx_t_9);
      __Pyx_XGIVEREF(__pyx_t_10);
      __Pyx_XGIVEREF(__pyx_t_11);
      __Pyx_ExceptionReset(__pyx_t_9, __pyx_t_10, __pyx_t_11);
      __Pyx_XDECREF(__pyx_t_5); __pyx_t_5 = 0;
      __Pyx_XDECREF(__pyx_t_4); __pyx_t_4 = 0;
      __Pyx_XDECREF(__pyx_t_3); __pyx_t_3 = 0;
      __pyx_t_9 = 0; __pyx_t_10 = 0; __pyx_t_11 = 0;
      goto __pyx_L0;
    }
  }
```

</details>

L180  ⚪  (score=0)
```python
```
L181  🟡  (score=2)
```python
cdef void GIVEREF(PyObject* ctx, PyObject* p_obj, Py_ssize_t lineno):
```
<details><summary>Show generated C (score=2)</summary>

```c
static void __pyx_f_6Cython_7Runtime_8refnanny_GIVEREF(PyObject *__pyx_v_ctx, PyObject *__pyx_v_p_obj, Py_ssize_t __pyx_v_lineno) {
/* … */
  /* function exit code */
  goto __pyx_L0;
  __pyx_L1_error:;
  __Pyx_AddTraceback("Cython.Runtime.refnanny.GIVEREF", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_L0:;
}
```

</details>

L182  ⚪  (score=0)
```python
    GIVEREF_and_report(ctx, p_obj, lineno)
```
<details><summary>Show generated C (score=0)</summary>

```c
  __pyx_t_1 = __pyx_f_6Cython_7Runtime_8refnanny_GIVEREF_and_report(__pyx_v_ctx, __pyx_v_p_obj, __pyx_v_lineno); if (unlikely(__pyx_t_1 == ((int)-1) && PyErr_Occurred())) __PYX_ERR(0, 182, __pyx_L1_error)
```

</details>

L183  ⚪  (score=0)
```python
```
L184  🟡  (score=2)
```python
cdef void INCREF(PyObject* ctx, PyObject* obj, Py_ssize_t lineno):
```
<details><summary>Show generated C (score=2)</summary>

```c
static void __pyx_f_6Cython_7Runtime_8refnanny_INCREF(PyObject *__pyx_v_ctx, PyObject *__pyx_v_obj, Py_ssize_t __pyx_v_lineno) {
/* … */
  /* function exit code */
  goto __pyx_L0;
  __pyx_L1_error:;
  __Pyx_AddTraceback("Cython.Runtime.refnanny.INCREF", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_L0:;
}
```

</details>

L185  ⚪  (score=0)
```python
    Py_XINCREF(obj)
```
<details><summary>Show generated C (score=0)</summary>

```c
  Py_XINCREF(__pyx_v_obj);
```

</details>

L186  ⚪  (score=0)
```python
    PyThreadState_Get()  # Check that we hold the GIL
```
<details><summary>Show generated C (score=0)</summary>

```c
  (void)(PyThreadState_Get());
```

</details>

L187  ⚪  (score=0)
```python
    GOTREF(ctx, obj, lineno)
```
<details><summary>Show generated C (score=0)</summary>

```c
  __pyx_f_6Cython_7Runtime_8refnanny_GOTREF(__pyx_v_ctx, __pyx_v_obj, __pyx_v_lineno); if (unlikely(PyErr_Occurred())) __PYX_ERR(0, 187, __pyx_L1_error)
```

</details>

L188  ⚪  (score=0)
```python
```
L189  🟡  (score=2)
```python
cdef void DECREF(PyObject* ctx, PyObject* obj, Py_ssize_t lineno):
```
<details><summary>Show generated C (score=2)</summary>

```c
static void __pyx_f_6Cython_7Runtime_8refnanny_DECREF(PyObject *__pyx_v_ctx, PyObject *__pyx_v_obj, Py_ssize_t __pyx_v_lineno) {
/* … */
  /* function exit code */
  goto __pyx_L0;
  __pyx_L1_error:;
  __Pyx_AddTraceback("Cython.Runtime.refnanny.DECREF", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_L0:;
}
```

</details>

L190  ⚪  (score=0)
```python
    if GIVEREF_and_report(ctx, obj, lineno):
```
<details><summary>Show generated C (score=0)</summary>

```c
  __pyx_t_1 = __pyx_f_6Cython_7Runtime_8refnanny_GIVEREF_and_report(__pyx_v_ctx, __pyx_v_obj, __pyx_v_lineno); if (unlikely(__pyx_t_1 == ((int)-1) && PyErr_Occurred())) __PYX_ERR(0, 190, __pyx_L1_error)
  if (__pyx_t_1) {
/* … */
  }
```

</details>

L191  ⚪  (score=0)
```python
        Py_XDECREF(obj)
```
<details><summary>Show generated C (score=0)</summary>

```c
    Py_XDECREF(__pyx_v_obj);
```

</details>

L192  ⚪  (score=0)
```python
    PyThreadState_Get()  # Check that we hold the GIL
```
<details><summary>Show generated C (score=0)</summary>

```c
  (void)(PyThreadState_Get());
```

</details>

L193  ⚪  (score=0)
```python
```
L194  ⚪  (score=0)
```python
cdef void FinishContext(PyObject** ctx):
```
<details><summary>Show generated C (score=0)</summary>

```c
static void __pyx_f_6Cython_7Runtime_8refnanny_FinishContext(PyObject **__pyx_v_ctx) {
  PyObject *__pyx_v_type;
  PyObject *__pyx_v_value;
  PyObject *__pyx_v_tb;
  PyObject *__pyx_v_errors = 0;
  struct __pyx_obj_6Cython_7Runtime_8refnanny_Context *__pyx_v_context = 0;
```

</details>

L195  ⚪  (score=0)
```python
    if ctx == NULL or ctx[0] == NULL: return
```
<details><summary>Show generated C (score=0)</summary>

```c
  __pyx_t_2 = (__pyx_v_ctx == NULL);
  if (!__pyx_t_2) {
  } else {
    __pyx_t_1 = __pyx_t_2;
    goto __pyx_L4_bool_binop_done;
  }
  __pyx_t_2 = ((__pyx_v_ctx[0]) == NULL);
  __pyx_t_1 = __pyx_t_2;
  __pyx_L4_bool_binop_done:;
  if (__pyx_t_1) {
    goto __pyx_L0;
  }
```

</details>

L196  ⚪  (score=0)
```python
    cdef (PyObject*) type = NULL, value = NULL, tb = NULL
```
<details><summary>Show generated C (score=0)</summary>

```c
  __pyx_v_type = NULL;
  __pyx_v_value = NULL;
  __pyx_v_tb = NULL;
```

</details>

L197  🟡  (score=1)
```python
    cdef object errors = None
```
<details><summary>Show generated C (score=1)</summary>

```c
  __Pyx_INCREF(Py_None);
  __pyx_v_errors = Py_None;
```

</details>

L198  ⚪  (score=0)
```python
    cdef Context context
```
L199  ⚪  (score=0)
```python
    PyThreadState_Get()  # Check that we hold the GIL
```
<details><summary>Show generated C (score=0)</summary>

```c
  (void)(PyThreadState_Get());
```

</details>

L200  🟠  (score=5)
```python
    PyErr_Fetch(&type, &value, &tb)
```
<details><summary>Show generated C (score=5)</summary>

```c
  PyErr_Fetch((&__pyx_v_type), (&__pyx_v_value), (&__pyx_v_tb));
```

</details>

L201  🔴  (score=12)
```python
    try:
```
<details><summary>Show generated C (score=12)</summary>

```c
  /*try:*/ {
    {
      /*try:*/ {
/* … */
      }
      __Pyx_XDECREF(__pyx_t_3); __pyx_t_3 = 0;
      __Pyx_XDECREF(__pyx_t_4); __pyx_t_4 = 0;
      __Pyx_XDECREF(__pyx_t_5); __pyx_t_5 = 0;
      goto __pyx_L14_try_end;
      __pyx_L9_error:;
      __Pyx_XDECREF(__pyx_t_10); __pyx_t_10 = 0;
      __Pyx_XDECREF(__pyx_t_6); __pyx_t_6 = 0;
      __Pyx_XDECREF(__pyx_t_7); __pyx_t_7 = 0;
      __Pyx_XDECREF(__pyx_t_8); __pyx_t_8 = 0;
      __Pyx_XDECREF(__pyx_t_9); __pyx_t_9 = 0;
/* … */
      __pyx_L11_except_error:;
      __Pyx_XGIVEREF(__pyx_t_3);
      __Pyx_XGIVEREF(__pyx_t_4);
      __Pyx_XGIVEREF(__pyx_t_5);
      __Pyx_ExceptionReset(__pyx_t_3, __pyx_t_4, __pyx_t_5);
      goto __pyx_L7_error;
      __pyx_L10_exception_handled:;
      __Pyx_XGIVEREF(__pyx_t_3);
      __Pyx_XGIVEREF(__pyx_t_4);
      __Pyx_XGIVEREF(__pyx_t_5);
      __Pyx_ExceptionReset(__pyx_t_3, __pyx_t_4, __pyx_t_5);
      __pyx_L14_try_end:;
    }
  }
```

</details>

L202  🟡  (score=1)
```python
        context = <Context>ctx[0]
```
<details><summary>Show generated C (score=1)</summary>

```c
        __pyx_t_6 = ((PyObject *)(__pyx_v_ctx[0]));
        __Pyx_INCREF(__pyx_t_6);
        __pyx_v_context = ((struct __pyx_obj_6Cython_7Runtime_8refnanny_Context *)__pyx_t_6);
        __pyx_t_6 = 0;
```

</details>

L203  🟡  (score=1)
```python
        errors = context.end()
```
<details><summary>Show generated C (score=1)</summary>

```c
        __pyx_t_6 = __pyx_f_6Cython_7Runtime_8refnanny_7Context_end(__pyx_v_context); if (unlikely(!__pyx_t_6)) __PYX_ERR(0, 203, __pyx_L9_error)
        __Pyx_GOTREF(__pyx_t_6);
        __Pyx_DECREF_SET(__pyx_v_errors, __pyx_t_6);
        __pyx_t_6 = 0;
```

</details>

L204  🟡  (score=2)
```python
        if errors:
```
<details><summary>Show generated C (score=2)</summary>

```c
        __pyx_t_1 = __Pyx_PyObject_IsTrue(__pyx_v_errors); if (unlikely((__pyx_t_1 < 0))) __PYX_ERR(0, 204, __pyx_L9_error)
        if (__pyx_t_1) {
/* … */
        }
```

</details>

L205  🔴  (score=38)
```python
            print(f"{context.filename.decode('latin1')}: {context.name.decode('latin1')}()")
```
<details><summary>Show generated C (score=38)</summary>

```c
          __pyx_t_7 = NULL;
          __pyx_t_8 = __Pyx_PyObject_GetAttrStr(__pyx_v_context->filename, __pyx_mstate_global->__pyx_n_u_decode); if (unlikely(!__pyx_t_8)) __PYX_ERR(0, 205, __pyx_L9_error)
          __Pyx_GOTREF(__pyx_t_8);
          __pyx_t_9 = __Pyx_PyObject_Call(__pyx_t_8, __pyx_mstate_global->__pyx_tuple[0], NULL); if (unlikely(!__pyx_t_9)) __PYX_ERR(0, 205, __pyx_L9_error)
          __Pyx_GOTREF(__pyx_t_9);
          __Pyx_DECREF(__pyx_t_8); __pyx_t_8 = 0;
          __pyx_t_8 = __Pyx_PyObject_FormatSimple(__pyx_t_9, __pyx_mstate_global->__pyx_empty_unicode); if (unlikely(!__pyx_t_8)) __PYX_ERR(0, 205, __pyx_L9_error)
          __Pyx_GOTREF(__pyx_t_8);
          __Pyx_DECREF(__pyx_t_9); __pyx_t_9 = 0;
          __pyx_t_9 = __Pyx_PyObject_GetAttrStr(__pyx_v_context->name, __pyx_mstate_global->__pyx_n_u_decode); if (unlikely(!__pyx_t_9)) __PYX_ERR(0, 205, __pyx_L9_error)
          __Pyx_GOTREF(__pyx_t_9);
          __pyx_t_10 = __Pyx_PyObject_Call(__pyx_t_9, __pyx_mstate_global->__pyx_tuple[0], NULL); if (unlikely(!__pyx_t_10)) __PYX_ERR(0, 205, __pyx_L9_error)
          __Pyx_GOTREF(__pyx_t_10);
          __Pyx_DECREF(__pyx_t_9); __pyx_t_9 = 0;
          __pyx_t_9 = __Pyx_PyObject_FormatSimple(__pyx_t_10, __pyx_mstate_global->__pyx_empty_unicode); if (unlikely(!__pyx_t_9)) __PYX_ERR(0, 205, __pyx_L9_error)
          __Pyx_GOTREF(__pyx_t_9);
          __Pyx_DECREF(__pyx_t_10); __pyx_t_10 = 0;
          __pyx_t_11[0] = __pyx_t_8;
          __pyx_t_11[1] = __pyx_mstate_global->__pyx_kp_u__5;
          __pyx_t_11[2] = __pyx_t_9;
          __pyx_t_11[3] = __pyx_mstate_global->__pyx_kp_u__6;
          __pyx_t_10 = __Pyx_PyUnicode_Join(__pyx_t_11, 4, __Pyx_PyUnicode_GET_LENGTH(__pyx_t_8) + 2 * 2 + __Pyx_PyUnicode_GET_LENGTH(__pyx_t_9), 127 | __Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_8) | __Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_9));
          if (unlikely(!__pyx_t_10)) __PYX_ERR(0, 205, __pyx_L9_error)
          __Pyx_GOTREF(__pyx_t_10);
          __Pyx_DECREF(__pyx_t_8); __pyx_t_8 = 0;
          __Pyx_DECREF(__pyx_t_9); __pyx_t_9 = 0;
          __pyx_t_12 = 1;
          {
            PyObject *__pyx_callargs[2] = {__pyx_t_7, __pyx_t_10};
            __pyx_t_6 = __Pyx_PyObject_FastCall((PyObject*)__pyx_builtin_print, __pyx_callargs+__pyx_t_12, (2-__pyx_t_12) | (__pyx_t_12*__Pyx_PY_VECTORCALL_ARGUMENTS_OFFSET));
            __Pyx_XDECREF(__pyx_t_7); __pyx_t_7 = 0;
            __Pyx_DECREF(__pyx_t_10); __pyx_t_10 = 0;
            if (unlikely(!__pyx_t_6)) __PYX_ERR(0, 205, __pyx_L9_error)
            __Pyx_GOTREF(__pyx_t_6);
          }
          __Pyx_DECREF(__pyx_t_6); __pyx_t_6 = 0;
/* … */
  __pyx_mstate_global->__pyx_tuple[0] = PyTuple_Pack(1, __pyx_mstate_global->__pyx_n_u_latin1); if (unlikely(!__pyx_mstate_global->__pyx_tuple[0])) __PYX_ERR(0, 205, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_mstate_global->__pyx_tuple[0]);
  __Pyx_GIVEREF(__pyx_mstate_global->__pyx_tuple[0]);
```

</details>

L206  🟡  (score=4)
```python
            print(errors)
```
<details><summary>Show generated C (score=4)</summary>

```c
          __pyx_t_10 = NULL;
          __pyx_t_12 = 1;
          {
            PyObject *__pyx_callargs[2] = {__pyx_t_10, __pyx_v_errors};
            __pyx_t_6 = __Pyx_PyObject_FastCall((PyObject*)__pyx_builtin_print, __pyx_callargs+__pyx_t_12, (2-__pyx_t_12) | (__pyx_t_12*__Pyx_PY_VECTORCALL_ARGUMENTS_OFFSET));
            __Pyx_XDECREF(__pyx_t_10); __pyx_t_10 = 0;
            if (unlikely(!__pyx_t_6)) __PYX_ERR(0, 206, __pyx_L9_error)
            __Pyx_GOTREF(__pyx_t_6);
          }
          __Pyx_DECREF(__pyx_t_6); __pyx_t_6 = 0;
```

</details>

L207  🟡  (score=2)
```python
        context = None
```
<details><summary>Show generated C (score=2)</summary>

```c
        __Pyx_INCREF(Py_None);
        __Pyx_DECREF_SET(__pyx_v_context, ((struct __pyx_obj_6Cython_7Runtime_8refnanny_Context *)Py_None));
```

</details>

L208  🟡  (score=4)
```python
    except:
```
<details><summary>Show generated C (score=4)</summary>

```c
      /*except:*/ {
        __Pyx_AddTraceback("Cython.Runtime.refnanny.FinishContext", __pyx_clineno, __pyx_lineno, __pyx_filename);
        if (__Pyx_GetException(&__pyx_t_6, &__pyx_t_10, &__pyx_t_7) < 0) __PYX_ERR(0, 208, __pyx_L11_except_error)
        __Pyx_XGOTREF(__pyx_t_6);
        __Pyx_XGOTREF(__pyx_t_10);
        __Pyx_XGOTREF(__pyx_t_7);
```

</details>

L209  🟡  (score=4)
```python
        report_unraisable(
```
<details><summary>Show generated C (score=4)</summary>

```c
        __pyx_f_6Cython_7Runtime_8refnanny_report_unraisable(__pyx_t_9, __pyx_t_13, NULL);
        __Pyx_DECREF(__pyx_t_9); __pyx_t_9 = 0;
        __Pyx_XDECREF(__pyx_t_6); __pyx_t_6 = 0;
        __Pyx_XDECREF(__pyx_t_10); __pyx_t_10 = 0;
        __Pyx_XDECREF(__pyx_t_7); __pyx_t_7 = 0;
        goto __pyx_L10_exception_handled;
      }
```

</details>

L210  🟠  (score=6)
```python
            context.filename if context is not None else None,
```
<details><summary>Show generated C (score=6)</summary>

```c
        if (unlikely(!__pyx_v_context)) { __Pyx_RaiseUnboundLocalError("context"); __PYX_ERR(0, 210, __pyx_L11_except_error) }
        __pyx_t_1 = (((PyObject *)__pyx_v_context) != Py_None);
        if (__pyx_t_1) {
          if (unlikely(!__pyx_v_context)) { __Pyx_RaiseUnboundLocalError("context"); __PYX_ERR(0, 210, __pyx_L11_except_error) }
          __Pyx_INCREF(__pyx_v_context->filename);
          __pyx_t_9 = __pyx_v_context->filename;
        } else {
          __Pyx_INCREF(Py_None);
          __pyx_t_9 = Py_None;
        }
```

</details>

L211  🟡  (score=4)
```python
            lineno=context.start if context is not None else 0,
```
<details><summary>Show generated C (score=4)</summary>

```c
        if (unlikely(!__pyx_v_context)) { __Pyx_RaiseUnboundLocalError("context"); __PYX_ERR(0, 211, __pyx_L11_except_error) }
        __pyx_t_1 = (((PyObject *)__pyx_v_context) != Py_None);
        if (__pyx_t_1) {
          if (unlikely(!__pyx_v_context)) { __Pyx_RaiseUnboundLocalError("context"); __PYX_ERR(0, 211, __pyx_L11_except_error) }
          __pyx_t_13 = __pyx_v_context->start;
        } else {
          __pyx_t_13 = 0;
        }
```

</details>

L212  ⚪  (score=0)
```python
        )
```
L213  ⚪  (score=0)
```python
    finally:
```
L214  ⚪  (score=0)
```python
        Py_CLEAR(ctx[0])
```
<details><summary>Show generated C (score=0)</summary>

```c
  /*finally:*/ {
    /*normal exit:*/{
      Py_CLEAR((__pyx_v_ctx[0]));
/* … */
        Py_CLEAR((__pyx_v_ctx[0]));
```

</details>

L215  🔴  (score=10)
```python
        PyErr_Restore(type, value, tb)
```
<details><summary>Show generated C (score=10)</summary>

```c
      PyErr_Restore(__pyx_v_type, __pyx_v_value, __pyx_v_tb);
/* … */
        PyErr_Restore(__pyx_v_type, __pyx_v_value, __pyx_v_tb);
```

</details>

L216  🔴  (score=16)
```python
        return  # swallow any exceptions
```
<details><summary>Show generated C (score=16)</summary>

```c
      goto __pyx_L0;
    }
    __pyx_L7_error:;
    /*exception exit:*/{
      __Pyx_PyThreadState_declare
      __Pyx_PyThreadState_assign
      __pyx_t_5 = 0; __pyx_t_4 = 0; __pyx_t_3 = 0; __pyx_t_14 = 0; __pyx_t_15 = 0; __pyx_t_16 = 0;
      __Pyx_XDECREF(__pyx_t_10); __pyx_t_10 = 0;
      __Pyx_XDECREF(__pyx_t_6); __pyx_t_6 = 0;
      __Pyx_XDECREF(__pyx_t_7); __pyx_t_7 = 0;
      __Pyx_XDECREF(__pyx_t_8); __pyx_t_8 = 0;
      __Pyx_XDECREF(__pyx_t_9); __pyx_t_9 = 0;
       __Pyx_ExceptionSwap(&__pyx_t_14, &__pyx_t_15, &__pyx_t_16);
      if ( unlikely(__Pyx_GetException(&__pyx_t_5, &__pyx_t_4, &__pyx_t_3) < 0)) __Pyx_ErrFetch(&__pyx_t_5, &__pyx_t_4, &__pyx_t_3);
      __Pyx_XGOTREF(__pyx_t_5);
      __Pyx_XGOTREF(__pyx_t_4);
      __Pyx_XGOTREF(__pyx_t_3);
      __Pyx_XGOTREF(__pyx_t_14);
      __Pyx_XGOTREF(__pyx_t_15);
      __Pyx_XGOTREF(__pyx_t_16);
      {
/* … */
        goto __pyx_L18_return;
      }
      __pyx_L18_return:;
      __Pyx_XGIVEREF(__pyx_t_14);
      __Pyx_XGIVEREF(__pyx_t_15);
      __Pyx_XGIVEREF(__pyx_t_16);
      __Pyx_ExceptionReset(__pyx_t_14, __pyx_t_15, __pyx_t_16);
      __Pyx_XDECREF(__pyx_t_5); __pyx_t_5 = 0;
      __Pyx_XDECREF(__pyx_t_4); __pyx_t_4 = 0;
      __Pyx_XDECREF(__pyx_t_3); __pyx_t_3 = 0;
      __pyx_t_14 = 0; __pyx_t_15 = 0; __pyx_t_16 = 0;
      goto __pyx_L0;
    }
  }
```

</details>

L217  ⚪  (score=0)
```python
```
L218  ⚪  (score=0)
```python
ctypedef struct RefNannyAPIStruct:
```
<details><summary>Show generated C (score=0)</summary>

```c
struct __pyx_t_6Cython_7Runtime_8refnanny_RefNannyAPIStruct {
  void (*INCREF)(PyObject *, PyObject *, Py_ssize_t);
  void (*DECREF)(PyObject *, PyObject *, Py_ssize_t);
  void (*GOTREF)(PyObject *, PyObject *, Py_ssize_t);
  void (*GIVEREF)(PyObject *, PyObject *, Py_ssize_t);
  PyObject *(*SetupContext)(char *, Py_ssize_t, char *);
  void (*FinishContext)(PyObject **);
};
```

</details>

L219  ⚪  (score=0)
```python
    void (*INCREF)(PyObject*, PyObject*, Py_ssize_t)
```
L220  ⚪  (score=0)
```python
    void (*DECREF)(PyObject*, PyObject*, Py_ssize_t)
```
L221  ⚪  (score=0)
```python
    void (*GOTREF)(PyObject*, PyObject*, Py_ssize_t)
```
L222  ⚪  (score=0)
```python
    void (*GIVEREF)(PyObject*, PyObject*, Py_ssize_t)
```
L223  ⚪  (score=0)
```python
    PyObject* (*SetupContext)(char*, Py_ssize_t, char*) except NULL
```
L224  ⚪  (score=0)
```python
    void (*FinishContext)(PyObject**)
```
L225  ⚪  (score=0)
```python
```
L226  ⚪  (score=0)
```python
cdef RefNannyAPIStruct api
```
L227  ⚪  (score=0)
```python
api.INCREF = INCREF
```
<details><summary>Show generated C (score=0)</summary>

```c
  __pyx_v_6Cython_7Runtime_8refnanny_api.INCREF = __pyx_f_6Cython_7Runtime_8refnanny_INCREF;
```

</details>

L228  ⚪  (score=0)
```python
api.DECREF =  DECREF
```
<details><summary>Show generated C (score=0)</summary>

```c
  __pyx_v_6Cython_7Runtime_8refnanny_api.DECREF = __pyx_f_6Cython_7Runtime_8refnanny_DECREF;
```

</details>

L229  ⚪  (score=0)
```python
api.GOTREF =  GOTREF
```
<details><summary>Show generated C (score=0)</summary>

```c
  __pyx_v_6Cython_7Runtime_8refnanny_api.GOTREF = __pyx_f_6Cython_7Runtime_8refnanny_GOTREF;
```

</details>

L230  ⚪  (score=0)
```python
api.GIVEREF = GIVEREF
```
<details><summary>Show generated C (score=0)</summary>

```c
  __pyx_v_6Cython_7Runtime_8refnanny_api.GIVEREF = __pyx_f_6Cython_7Runtime_8refnanny_GIVEREF;
```

</details>

L231  ⚪  (score=0)
```python
api.SetupContext = SetupContext
```
<details><summary>Show generated C (score=0)</summary>

```c
  __pyx_v_6Cython_7Runtime_8refnanny_api.SetupContext = __pyx_f_6Cython_7Runtime_8refnanny_SetupContext;
```

</details>

L232  ⚪  (score=0)
```python
api.FinishContext = FinishContext
```
<details><summary>Show generated C (score=0)</summary>

```c
  __pyx_v_6Cython_7Runtime_8refnanny_api.FinishContext = __pyx_f_6Cython_7Runtime_8refnanny_FinishContext;
```

</details>

L233  ⚪  (score=0)
```python
```
L234  ⚪  (score=0)
```python
cdef extern from "Python.h":
```
L235  ⚪  (score=0)
```python
    object PyLong_FromVoidPtr(void*)
```
L236  ⚪  (score=0)
```python
```
L237  🔴  (score=11)
```python
RefNannyAPI = PyLong_FromVoidPtr(<void*>&api)
```
<details><summary>Show generated C (score=11)</summary>

```c
  __pyx_t_2 = PyLong_FromVoidPtr(((void *)(&__pyx_v_6Cython_7Runtime_8refnanny_api))); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 237, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  if (PyDict_SetItem(__pyx_mstate_global->__pyx_d, __pyx_mstate_global->__pyx_n_u_RefNannyAPI, __pyx_t_2) < (0)) __PYX_ERR(0, 237, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
```

</details>

