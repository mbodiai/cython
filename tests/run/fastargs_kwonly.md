# Cython annotation for fastargs_kwonly.pyx

Raw output: fastargs_kwonly.c

L1  🔴  (score=83)
```python
# mode: run
```
<details><summary>Show generated C (score=83)</summary>

```c
  __pyx_t_3 = __Pyx_PyDict_NewPresized(3); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 1, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_3);
  #if defined(PyDict_SetItem) && (defined(CYTHON_COMPILING_IN_CPYTHON))
  #if PY_VERSION_HEX >= 0x030A0000 /* CPython 3.10+ exposes KnownHash APIs */
  /* Use CPython's KnownHash APIs when available */
  extern int _PyDict_SetItem_KnownHash(PyObject*, PyObject*, PyObject*, Py_hash_t);
  {
    Py_hash_t __pyx_hash = PyObject_Hash(__pyx_mstate_global->__pyx_kp_u_fastargs_positional_line_19); if (unlikely(__pyx_hash == -1)) __PYX_ERR(0, 1, __pyx_L1_error);
    if (unlikely(_PyDict_SetItem_KnownHash(__pyx_t_3, __pyx_mstate_global->__pyx_kp_u_fastargs_positional_line_19, __pyx_mstate_global->__pyx_kp_u_fastargs_positional_1_2_3_1_2_3, __pyx_hash) < 0)) __PYX_ERR(0, 1, __pyx_L1_error);
  }
  #else
  if (PyDict_SetItem(__pyx_t_3, __pyx_mstate_global->__pyx_kp_u_fastargs_positional_line_19, __pyx_mstate_global->__pyx_kp_u_fastargs_positional_1_2_3_1_2_3) < (0)) __PYX_ERR(0, 1, __pyx_L1_error)
  #endif
  #else
  if (PyDict_SetItem(__pyx_t_3, __pyx_mstate_global->__pyx_kp_u_fastargs_positional_line_19, __pyx_mstate_global->__pyx_kp_u_fastargs_positional_1_2_3_1_2_3) < (0)) __PYX_ERR(0, 1, __pyx_L1_error)
  #endif
  #if defined(PyDict_SetItem) && (defined(CYTHON_COMPILING_IN_CPYTHON))
  #if PY_VERSION_HEX >= 0x030A0000 /* CPython 3.10+ exposes KnownHash APIs */
  /* Use CPython's KnownHash APIs when available */
  extern int _PyDict_SetItem_KnownHash(PyObject*, PyObject*, PyObject*, Py_hash_t);
  {
    Py_hash_t __pyx_hash = PyObject_Hash(__pyx_mstate_global->__pyx_kp_u_fastargs_kwonly_line_33); if (unlikely(__pyx_hash == -1)) __PYX_ERR(0, 1, __pyx_L1_error);
    if (unlikely(_PyDict_SetItem_KnownHash(__pyx_t_3, __pyx_mstate_global->__pyx_kp_u_fastargs_kwonly_line_33, __pyx_mstate_global->__pyx_kp_u_fastargs_kwonly_a_1_b_2_1_2__ch, __pyx_hash) < 0)) __PYX_ERR(0, 1, __pyx_L1_error);
  }
  #else
  if (PyDict_SetItem(__pyx_t_3, __pyx_mstate_global->__pyx_kp_u_fastargs_kwonly_line_33, __pyx_mstate_global->__pyx_kp_u_fastargs_kwonly_a_1_b_2_1_2__ch) < (0)) __PYX_ERR(0, 1, __pyx_L1_error)
  #endif
  #else
  if (PyDict_SetItem(__pyx_t_3, __pyx_mstate_global->__pyx_kp_u_fastargs_kwonly_line_33, __pyx_mstate_global->__pyx_kp_u_fastargs_kwonly_a_1_b_2_1_2__ch) < (0)) __PYX_ERR(0, 1, __pyx_L1_error)
  #endif
  #if defined(PyDict_SetItem) && (defined(CYTHON_COMPILING_IN_CPYTHON))
  #if PY_VERSION_HEX >= 0x030A0000 /* CPython 3.10+ exposes KnownHash APIs */
  /* Use CPython's KnownHash APIs when available */
  extern int _PyDict_SetItem_KnownHash(PyObject*, PyObject*, PyObject*, Py_hash_t);
  {
    Py_hash_t __pyx_hash = PyObject_Hash(__pyx_mstate_global->__pyx_kp_u_fastargs_mixed_line_45); if (unlikely(__pyx_hash == -1)) __PYX_ERR(0, 1, __pyx_L1_error);
    if (unlikely(_PyDict_SetItem_KnownHash(__pyx_t_3, __pyx_mstate_global->__pyx_kp_u_fastargs_mixed_line_45, __pyx_mstate_global->__pyx_kp_u_fastargs_mixed_1_b_2_1_2_0_fast, __pyx_hash) < 0)) __PYX_ERR(0, 1, __pyx_L1_error);
  }
  #else
  if (PyDict_SetItem(__pyx_t_3, __pyx_mstate_global->__pyx_kp_u_fastargs_mixed_line_45, __pyx_mstate_global->__pyx_kp_u_fastargs_mixed_1_b_2_1_2_0_fast) < (0)) __PYX_ERR(0, 1, __pyx_L1_error)
  #endif
  #else
  if (PyDict_SetItem(__pyx_t_3, __pyx_mstate_global->__pyx_kp_u_fastargs_mixed_line_45, __pyx_mstate_global->__pyx_kp_u_fastargs_mixed_1_b_2_1_2_0_fast) < (0)) __PYX_ERR(0, 1, __pyx_L1_error)
  #endif
  if (PyDict_SetItem(__pyx_mstate_global->__pyx_d, __pyx_mstate_global->__pyx_n_u_test, __pyx_t_3) < (0)) __PYX_ERR(0, 1, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
```

</details>

L2  ⚪  (score=0)
```python
# tag: fastargs, kwargs, cyfunction
```
L3  ⚪  (score=0)
```python
# cython: binding=True
```
L4  ⚪  (score=0)
```python
```
L5  ⚪  (score=0)
```python
cimport cython
```
L6  ⚪  (score=0)
```python
```
L7  ⚪  (score=0)
```python
```
L8  🔴  (score=69)
```python
@cython.cfunc
```
<details><summary>Show generated C (score=69)</summary>

```c
/* Python wrapper */
static PyObject *__pyx_pw_15fastargs_kwonly_3pyx_1_check_raises(PyObject *__pyx_self, 
#if CYTHON_METH_FASTCALL
PyObject *const *__pyx_args, Py_ssize_t __pyx_nargs, PyObject *__pyx_kwds
#else
PyObject *__pyx_args, PyObject *__pyx_kwds
#endif
); /*proto*/
PyDoc_STRVAR(__pyx_doc_15fastargs_kwonly_3pyx__check_raises, "File: tests/run/fastargs_kwonly.pyx (starting at line 8)");
static PyMethodDef __pyx_mdef_15fastargs_kwonly_3pyx_1_check_raises = {"_check_raises", (PyCFunction)(void(*)(void))(__Pyx_PyCFunction_FastCallWithKeywords)__pyx_pw_15fastargs_kwonly_3pyx_1_check_raises, __Pyx_METH_FASTCALL|METH_KEYWORDS, __pyx_doc_15fastargs_kwonly_3pyx__check_raises};
static PyObject *__pyx_pw_15fastargs_kwonly_3pyx_1_check_raises(PyObject *__pyx_self, 
#if CYTHON_METH_FASTCALL
PyObject *const *__pyx_args, Py_ssize_t __pyx_nargs, PyObject *__pyx_kwds
#else
PyObject *__pyx_args, PyObject *__pyx_kwds
#endif
) {
  PyObject *__pyx_v_func = 0;
  PyObject *__pyx_v_args = 0;
  PyObject *__pyx_v_kwargs = 0;
  PyObject *__pyx_v_exc_type = 0;
  #if !CYTHON_METH_FASTCALL
  CYTHON_UNUSED Py_ssize_t __pyx_nargs;
  #endif
  CYTHON_UNUSED PyObject *const *__pyx_kwvalues;
  PyObject *__pyx_r = 0;
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("_check_raises (wrapper)", 0);
  #if !CYTHON_METH_FASTCALL
  #if CYTHON_ASSUME_SAFE_SIZE
  __pyx_nargs = PyTuple_GET_SIZE(__pyx_args);
  #else
  __pyx_nargs = PyTuple_Size(__pyx_args); if (unlikely(__pyx_nargs < 0)) return NULL;
  #endif
  #endif
  __pyx_kwvalues = __Pyx_KwValues_FASTCALL(__pyx_args, __pyx_nargs);
  PyObject* values[4] = {0,0,0,0};
  #if CYTHON_METH_FASTCALL
  {
    PyObject **__pyx_fastlocals[4] = {&values[0], &values[1], &values[2], &values[3]};
    int __pyx_fastparse_result = __Pyx_FastParseKeywords(&__pyx_pi___pyx_pw_15fastargs_kwonly_3pyx_1_check_raises, __pyx_args, __pyx_nargs, __pyx_kwds, __pyx_fastlocals);
    if (likely(__pyx_fastparse_result == __PYX_FASTPARSE_SUCCESS)) {
      goto __pyx_L4_argument_unpacking_done;
    }
    if (__pyx_fastparse_result == __PYX_FASTPARSE_ERROR) goto __pyx_L3_error;
  }
  #else
  {
    PyObject ** const __pyx_pyargnames[] = {&__pyx_mstate_global->__pyx_n_u_func,&__pyx_mstate_global->__pyx_n_u_args,&__pyx_mstate_global->__pyx_n_u_kwargs,&__pyx_mstate_global->__pyx_n_u_exc_type,0};
    const Py_ssize_t __pyx_kwds_len = (__pyx_kwds) ? __Pyx_NumKwargs_FASTCALL(__pyx_kwds) : 0;
    if (unlikely(__pyx_kwds_len) < 0) __PYX_ERR(0, 8, __pyx_L3_error)
    if (__pyx_kwds_len > 0) {
      switch (__pyx_nargs) {
        case  4:
        values[3] = __Pyx_ArgRef_FASTCALL(__pyx_args, 3);
        if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[3])) __PYX_ERR(0, 8, __pyx_L3_error)
        CYTHON_FALLTHROUGH;
        case  3:
        values[2] = __Pyx_ArgRef_FASTCALL(__pyx_args, 2);
        if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[2])) __PYX_ERR(0, 8, __pyx_L3_error)
        CYTHON_FALLTHROUGH;
        case  2:
        values[1] = __Pyx_ArgRef_FASTCALL(__pyx_args, 1);
        if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[1])) __PYX_ERR(0, 8, __pyx_L3_error)
        CYTHON_FALLTHROUGH;
        case  1:
        values[0] = __Pyx_ArgRef_FASTCALL(__pyx_args, 0);
        if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[0])) __PYX_ERR(0, 8, __pyx_L3_error)
        CYTHON_FALLTHROUGH;
        case  0: break;
        default: goto __pyx_L5_argtuple_error;
      }
      const Py_ssize_t kwd_pos_args = __pyx_nargs;
      if (__Pyx_ParseKeywords(__pyx_kwds, __pyx_kwvalues, __pyx_pyargnames, 0, values, kwd_pos_args, __pyx_kwds_len, "_check_raises", 0) < (0)) __PYX_ERR(0, 8, __pyx_L3_error)
      for (Py_ssize_t i = __pyx_nargs; i < 4; i++) {
        if (unlikely(!values[i])) { __Pyx_RaiseArgtupleInvalid("_check_raises", 1, 4, 4, i); __PYX_ERR(0, 8, __pyx_L3_error) }
      }
    } else if (unlikely(__pyx_nargs != 4)) {
      goto __pyx_L5_argtuple_error;
    } else {
      values[0] = __Pyx_ArgRef_FASTCALL(__pyx_args, 0);
      if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[0])) __PYX_ERR(0, 8, __pyx_L3_error)
      values[1] = __Pyx_ArgRef_FASTCALL(__pyx_args, 1);
      if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[1])) __PYX_ERR(0, 8, __pyx_L3_error)
      values[2] = __Pyx_ArgRef_FASTCALL(__pyx_args, 2);
      if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[2])) __PYX_ERR(0, 8, __pyx_L3_error)
      values[3] = __Pyx_ArgRef_FASTCALL(__pyx_args, 3);
      if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[3])) __PYX_ERR(0, 8, __pyx_L3_error)
    }
    __pyx_v_func = values[0];
    __pyx_v_args = values[1];
    __pyx_v_kwargs = values[2];
    __pyx_v_exc_type = values[3];
  }
  goto __pyx_L6_skip;
  __pyx_L5_argtuple_error:;
  __Pyx_RaiseArgtupleInvalid("_check_raises", 1, 4, 4, __pyx_nargs); __PYX_ERR(0, 8, __pyx_L3_error)
  __pyx_L6_skip:;
  #endif
  goto __pyx_L4_argument_unpacking_done;
  __pyx_L3_error:;
  for (Py_ssize_t __pyx_temp=0; __pyx_temp < (Py_ssize_t)(sizeof(values)/sizeof(values[0])); ++__pyx_temp) {
    Py_XDECREF(values[__pyx_temp]);
  }
  __Pyx_AddTraceback("fastargs_kwonly.pyx._check_raises", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __Pyx_RefNannyFinishContext();
  return NULL;
  __pyx_L4_argument_unpacking_done:;
  __pyx_r = __pyx_pf_15fastargs_kwonly_3pyx__check_raises(__pyx_self, __pyx_v_func, __pyx_v_args, __pyx_v_kwargs, __pyx_v_exc_type);
  int __pyx_lineno = 0;
  const char *__pyx_filename = NULL;
  int __pyx_clineno = 0;

  /* function exit code */
  for (Py_ssize_t __pyx_temp=0; __pyx_temp < (Py_ssize_t)(sizeof(values)/sizeof(values[0])); ++__pyx_temp) {
    Py_XDECREF(values[__pyx_temp]);
  }
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}
#if CYTHON_METH_FASTCALL && CYTHON_VECTORCALL
static PyObject *__pyx_vectorcall___pyx_pw_15fastargs_kwonly_3pyx_1_check_raises(PyObject *func, PyObject *const *args, size_t nargsf, PyObject *kwnames) {
  PyObject *__pyx_v_func = 0;
  PyObject *__pyx_v_args = 0;
  PyObject *__pyx_v_kwargs = 0;
  PyObject *__pyx_v_exc_type = 0;
  #if !CYTHON_METH_FASTCALL
  CYTHON_UNUSED Py_ssize_t __pyx_nargs;
  #endif
  CYTHON_UNUSED PyObject *const *__pyx_kwvalues;
  PyObject *__pyx_r = 0;
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("_check_raises (vectorcall)", 0);
  __pyx_CyFunctionObject *cyfunc = (__pyx_CyFunctionObject *)func;
  PyObject *__pyx_self = NULL;
  PyObject *const *__pyx_args = args;
  Py_ssize_t __pyx_nargs = PyVectorcall_NARGS(nargsf);
  PyObject *__pyx_kwds = kwnames;
  __pyx_kwvalues = NULL;
  switch (__Pyx_CyFunction_Vectorcall_CheckArgs(cyfunc, __pyx_nargs, __pyx_kwds)) {
    case 1:
        __pyx_self = __pyx_args[0];
        __pyx_args += 1;
        __pyx_nargs -= 1;
        break;
    case 0:
    #if CYTHON_COMPILING_IN_LIMITED_API
        __pyx_self = PyCFunction_GetSelf(((__pyx_CyFunctionObject*)cyfunc)->func);
        if (unlikely(!__pyx_self) && PyErr_Occurred()) __PYX_ERR(0, 8, __pyx_L1_error)
    #else
        __pyx_self = ((PyCFunctionObject*)cyfunc)->m_self;
    #endif
        break;
    default:
        return NULL;
  }
  PyObject* values[4] = {0,0,0,0};
  __pyx_kwvalues = __Pyx_KwValues_FASTCALL(__pyx_args, __pyx_nargs);
  {
    PyObject **__pyx_fastlocals[4] = {&values[0], &values[1], &values[2], &values[3]};
    int __pyx_fastparse_result = __Pyx_FastParseKeywords(&__pyx_pi___pyx_pw_15fastargs_kwonly_3pyx_1_check_raises, __pyx_args, __pyx_nargs, __pyx_kwds, __pyx_fastlocals);
    if (likely(__pyx_fastparse_result == __PYX_FASTPARSE_SUCCESS)) {
      goto __pyx_L4_vectorcall_argument_unpacking_done;
    }
    if (__pyx_fastparse_result == __PYX_FASTPARSE_ERROR) goto __pyx_L1_error;
  }
  __pyx_r = __pyx_pf_15fastargs_kwonly_3pyx__check_raises(__pyx_self, __pyx_v_func, __pyx_v_args, __pyx_v_kwargs, __pyx_v_exc_type);
  int __pyx_lineno = 0;
  const char *__pyx_filename = NULL;
  int __pyx_clineno = 0;

  /* vectorcall exit code */
  goto __pyx_L0;
  __pyx_L1_error:;
  __pyx_r = NULL;
  for (Py_ssize_t __pyx_temp=0; __pyx_temp < (Py_ssize_t)(sizeof(values)/sizeof(values[0])); ++__pyx_temp) {
    Py_XDECREF(values[__pyx_temp]);
  }
  goto __pyx_L5_vectorcall_cleaned_up;
  __pyx_L0:;
  for (Py_ssize_t __pyx_temp=0; __pyx_temp < (Py_ssize_t)(sizeof(values)/sizeof(values[0])); ++__pyx_temp) {
    Py_XDECREF(values[__pyx_temp]);
  }
  __pyx_L5_vectorcall_cleaned_up:;
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
  return Py_None;
}
#endif /* CYTHON_METH_FASTCALL && CYTHON_VECTORCALL */

static PyObject *__pyx_pf_15fastargs_kwonly_3pyx__check_raises(CYTHON_UNUSED PyObject *__pyx_self, PyObject *__pyx_v_func, PyObject *__pyx_v_args, PyObject *__pyx_v_kwargs, PyObject *__pyx_v_exc_type) {
  PyObject *__pyx_r = NULL;
/* … */
  /* function exit code */
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_t_4);
  __Pyx_XDECREF(__pyx_t_5);
  __Pyx_XDECREF(__pyx_t_6);
  __Pyx_AddTraceback("fastargs_kwonly.pyx._check_raises", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_r = NULL;
  __pyx_L0:;
  __Pyx_XGIVEREF(__pyx_r);
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}
/* … */
  __pyx_t_2 = __Pyx_CyFunction_New(&__pyx_mdef_15fastargs_kwonly_3pyx_1_check_raises, __Pyx_CYFUNCTION_VECTORCALL_KEYWORDS, __pyx_mstate_global->__pyx_n_u_check_raises, NULL, __pyx_mstate_global->__pyx_n_u_fastargs_kwonly_pyx, __pyx_mstate_global->__pyx_d, ((PyObject *)__pyx_mstate_global->__pyx_codeobj_tab[0])); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 8, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  #if CYTHON_COMPILING_IN_CPYTHON && PY_VERSION_HEX >= 0x030E0000
  PyUnstable_Object_EnableDeferredRefcount(__pyx_t_2);
  #endif
  #if CYTHON_METH_FASTCALL && CYTHON_VECTORCALL
  __Pyx_CyFunction_func_vectorcall(__pyx_t_2) = __pyx_vectorcall___pyx_pw_15fastargs_kwonly_3pyx_1_check_raises;
  #endif
  if (PyDict_SetItem(__pyx_mstate_global->__pyx_d, __pyx_mstate_global->__pyx_n_u_check_raises, __pyx_t_2) < (0)) __PYX_ERR(0, 8, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
```

</details>

L9  ⚪  (score=0)
```python
@cython.inline
```
L10  ⚪  (score=0)
```python
def _check_raises(func, args, kwargs, exc_type):
```
L11  🟡  (score=4)
```python
    try:
```
<details><summary>Show generated C (score=4)</summary>

```c
  {
    /*try:*/ {
/* … */
    }
/* … */
    __pyx_L5_except_error:;
    __Pyx_XGIVEREF(__pyx_t_1);
    __Pyx_XGIVEREF(__pyx_t_2);
    __Pyx_XGIVEREF(__pyx_t_3);
    __Pyx_ExceptionReset(__pyx_t_1, __pyx_t_2, __pyx_t_3);
    goto __pyx_L1_error;
    __pyx_L6_except_return:;
    __Pyx_XGIVEREF(__pyx_t_1);
    __Pyx_XGIVEREF(__pyx_t_2);
    __Pyx_XGIVEREF(__pyx_t_3);
    __Pyx_ExceptionReset(__pyx_t_1, __pyx_t_2, __pyx_t_3);
    goto __pyx_L0;
  }
```

</details>

L12  🔴  (score=24)
```python
        func(*args, **kwargs)
```
<details><summary>Show generated C (score=24)</summary>

```c
      __pyx_t_4 = __Pyx_PySequence_Tuple(__pyx_v_args); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 12, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_4);
      if (unlikely(__pyx_v_kwargs == Py_None)) {
        PyErr_SetString(PyExc_TypeError, "argument after ** must be a mapping, not NoneType");
        __PYX_ERR(0, 12, __pyx_L3_error)
      }
      if (likely(PyDict_CheckExact(__pyx_v_kwargs))) {
        __pyx_t_5 = PyDict_Copy(__pyx_v_kwargs); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 12, __pyx_L3_error)
        __Pyx_GOTREF(__pyx_t_5);
      } else {
        __pyx_t_5 = __Pyx_PyObject_CallOneArg((PyObject*)&PyDict_Type, __pyx_v_kwargs); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 12, __pyx_L3_error)
        __Pyx_GOTREF(__pyx_t_5);
      }
      __pyx_t_6 = __Pyx_PyObject_Call(__pyx_v_func, __pyx_t_4, __pyx_t_5); if (unlikely(!__pyx_t_6)) __PYX_ERR(0, 12, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_6);
      __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
      __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
      __Pyx_DECREF(__pyx_t_6); __pyx_t_6 = 0;
```

</details>

L13  🟡  (score=4)
```python
    except exc_type:
```
<details><summary>Show generated C (score=4)</summary>

```c
    __pyx_t_7 = __Pyx_PyErr_ExceptionMatches(__pyx_v_exc_type);
    if (__pyx_t_7) {
      __Pyx_ErrRestore(0,0,0);
```

</details>

L14  🟡  (score=2)
```python
        return True
```
<details><summary>Show generated C (score=2)</summary>

```c
      __Pyx_XDECREF(__pyx_r);
      __Pyx_INCREF(Py_True);
      __pyx_r = Py_True;
      goto __pyx_L6_except_return;
    }
    goto __pyx_L5_except_error;
```

</details>

L15  ⚪  (score=0)
```python
    else:
```
L16  🟠  (score=5)
```python
        return False
```
<details><summary>Show generated C (score=5)</summary>

```c
    /*else:*/ {
      __Pyx_XDECREF(__pyx_r);
      __Pyx_INCREF(Py_False);
      __pyx_r = Py_False;
      goto __pyx_L6_except_return;
    }
    __pyx_L3_error:;
    __Pyx_XDECREF(__pyx_t_4); __pyx_t_4 = 0;
    __Pyx_XDECREF(__pyx_t_5); __pyx_t_5 = 0;
    __Pyx_XDECREF(__pyx_t_6); __pyx_t_6 = 0;
```

</details>

L17  ⚪  (score=0)
```python
```
L18  ⚪  (score=0)
```python
```
L19  🔴  (score=63)
```python
def fastargs_positional(a, b, c):
```
<details><summary>Show generated C (score=63)</summary>

```c
/* Python wrapper */
static PyObject *__pyx_pw_15fastargs_kwonly_3pyx_3fastargs_positional(PyObject *__pyx_self, 
#if CYTHON_METH_FASTCALL
PyObject *const *__pyx_args, Py_ssize_t __pyx_nargs, PyObject *__pyx_kwds
#else
PyObject *__pyx_args, PyObject *__pyx_kwds
#endif
); /*proto*/
PyDoc_STRVAR(__pyx_doc_15fastargs_kwonly_3pyx_2fastargs_positional, "File: tests/run/fastargs_kwonly.pyx (starting at line 19)\n\n    >>> fastargs_positional(1, 2, 3)\n    (1, 2, 3)\n    >>> _check_raises(fastargs_positional, (), {}, TypeError)\n    True\n    >>> _check_raises(fastargs_positional, (1,), {}, TypeError)\n    True\n    >>> _check_raises(fastargs_positional, (1, 2, 3, 4), {}, TypeError)\n    True\n    ");
static PyMethodDef __pyx_mdef_15fastargs_kwonly_3pyx_3fastargs_positional = {"fastargs_positional", (PyCFunction)(void(*)(void))(__Pyx_PyCFunction_FastCallWithKeywords)__pyx_pw_15fastargs_kwonly_3pyx_3fastargs_positional, __Pyx_METH_FASTCALL|METH_KEYWORDS, __pyx_doc_15fastargs_kwonly_3pyx_2fastargs_positional};
static PyObject *__pyx_pw_15fastargs_kwonly_3pyx_3fastargs_positional(PyObject *__pyx_self, 
#if CYTHON_METH_FASTCALL
PyObject *const *__pyx_args, Py_ssize_t __pyx_nargs, PyObject *__pyx_kwds
#else
PyObject *__pyx_args, PyObject *__pyx_kwds
#endif
) {
  PyObject *__pyx_v_a = 0;
  PyObject *__pyx_v_b = 0;
  PyObject *__pyx_v_c = 0;
  #if !CYTHON_METH_FASTCALL
  CYTHON_UNUSED Py_ssize_t __pyx_nargs;
  #endif
  CYTHON_UNUSED PyObject *const *__pyx_kwvalues;
  PyObject *__pyx_r = 0;
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("fastargs_positional (wrapper)", 0);
  #if !CYTHON_METH_FASTCALL
  #if CYTHON_ASSUME_SAFE_SIZE
  __pyx_nargs = PyTuple_GET_SIZE(__pyx_args);
  #else
  __pyx_nargs = PyTuple_Size(__pyx_args); if (unlikely(__pyx_nargs < 0)) return NULL;
  #endif
  #endif
  __pyx_kwvalues = __Pyx_KwValues_FASTCALL(__pyx_args, __pyx_nargs);
  PyObject* values[3] = {0,0,0};
  #if CYTHON_METH_FASTCALL
  {
    PyObject **__pyx_fastlocals[3] = {&values[0], &values[1], &values[2]};
    int __pyx_fastparse_result = __Pyx_FastParseKeywords(&__pyx_pi___pyx_pw_15fastargs_kwonly_3pyx_3fastargs_positional, __pyx_args, __pyx_nargs, __pyx_kwds, __pyx_fastlocals);
    if (likely(__pyx_fastparse_result == __PYX_FASTPARSE_SUCCESS)) {
      goto __pyx_L4_argument_unpacking_done;
    }
    if (__pyx_fastparse_result == __PYX_FASTPARSE_ERROR) goto __pyx_L3_error;
  }
  #else
  {
    PyObject ** const __pyx_pyargnames[] = {&__pyx_mstate_global->__pyx_n_u_a,&__pyx_mstate_global->__pyx_n_u_b,&__pyx_mstate_global->__pyx_n_u_c,0};
    const Py_ssize_t __pyx_kwds_len = (__pyx_kwds) ? __Pyx_NumKwargs_FASTCALL(__pyx_kwds) : 0;
    if (unlikely(__pyx_kwds_len) < 0) __PYX_ERR(0, 19, __pyx_L3_error)
    if (__pyx_kwds_len > 0) {
      switch (__pyx_nargs) {
        case  3:
        values[2] = __Pyx_ArgRef_FASTCALL(__pyx_args, 2);
        if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[2])) __PYX_ERR(0, 19, __pyx_L3_error)
        CYTHON_FALLTHROUGH;
        case  2:
        values[1] = __Pyx_ArgRef_FASTCALL(__pyx_args, 1);
        if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[1])) __PYX_ERR(0, 19, __pyx_L3_error)
        CYTHON_FALLTHROUGH;
        case  1:
        values[0] = __Pyx_ArgRef_FASTCALL(__pyx_args, 0);
        if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[0])) __PYX_ERR(0, 19, __pyx_L3_error)
        CYTHON_FALLTHROUGH;
        case  0: break;
        default: goto __pyx_L5_argtuple_error;
      }
      const Py_ssize_t kwd_pos_args = __pyx_nargs;
      if (__Pyx_ParseKeywords(__pyx_kwds, __pyx_kwvalues, __pyx_pyargnames, 0, values, kwd_pos_args, __pyx_kwds_len, "fastargs_positional", 0) < (0)) __PYX_ERR(0, 19, __pyx_L3_error)
      for (Py_ssize_t i = __pyx_nargs; i < 3; i++) {
        if (unlikely(!values[i])) { __Pyx_RaiseArgtupleInvalid("fastargs_positional", 1, 3, 3, i); __PYX_ERR(0, 19, __pyx_L3_error) }
      }
    } else if (unlikely(__pyx_nargs != 3)) {
      goto __pyx_L5_argtuple_error;
    } else {
      values[0] = __Pyx_ArgRef_FASTCALL(__pyx_args, 0);
      if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[0])) __PYX_ERR(0, 19, __pyx_L3_error)
      values[1] = __Pyx_ArgRef_FASTCALL(__pyx_args, 1);
      if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[1])) __PYX_ERR(0, 19, __pyx_L3_error)
      values[2] = __Pyx_ArgRef_FASTCALL(__pyx_args, 2);
      if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[2])) __PYX_ERR(0, 19, __pyx_L3_error)
    }
    __pyx_v_a = values[0];
    __pyx_v_b = values[1];
    __pyx_v_c = values[2];
  }
  goto __pyx_L6_skip;
  __pyx_L5_argtuple_error:;
  __Pyx_RaiseArgtupleInvalid("fastargs_positional", 1, 3, 3, __pyx_nargs); __PYX_ERR(0, 19, __pyx_L3_error)
  __pyx_L6_skip:;
  #endif
  goto __pyx_L4_argument_unpacking_done;
  __pyx_L3_error:;
  for (Py_ssize_t __pyx_temp=0; __pyx_temp < (Py_ssize_t)(sizeof(values)/sizeof(values[0])); ++__pyx_temp) {
    Py_XDECREF(values[__pyx_temp]);
  }
  __Pyx_AddTraceback("fastargs_kwonly.pyx.fastargs_positional", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __Pyx_RefNannyFinishContext();
  return NULL;
  __pyx_L4_argument_unpacking_done:;
  __pyx_r = __pyx_pf_15fastargs_kwonly_3pyx_2fastargs_positional(__pyx_self, __pyx_v_a, __pyx_v_b, __pyx_v_c);
  int __pyx_lineno = 0;
  const char *__pyx_filename = NULL;
  int __pyx_clineno = 0;

  /* function exit code */
  for (Py_ssize_t __pyx_temp=0; __pyx_temp < (Py_ssize_t)(sizeof(values)/sizeof(values[0])); ++__pyx_temp) {
    Py_XDECREF(values[__pyx_temp]);
  }
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}
#if CYTHON_METH_FASTCALL && CYTHON_VECTORCALL
static PyObject *__pyx_vectorcall___pyx_pw_15fastargs_kwonly_3pyx_3fastargs_positional(PyObject *func, PyObject *const *args, size_t nargsf, PyObject *kwnames) {
  PyObject *__pyx_v_a = 0;
  PyObject *__pyx_v_b = 0;
  PyObject *__pyx_v_c = 0;
  #if !CYTHON_METH_FASTCALL
  CYTHON_UNUSED Py_ssize_t __pyx_nargs;
  #endif
  CYTHON_UNUSED PyObject *const *__pyx_kwvalues;
  PyObject *__pyx_r = 0;
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("fastargs_positional (vectorcall)", 0);
  __pyx_CyFunctionObject *cyfunc = (__pyx_CyFunctionObject *)func;
  PyObject *__pyx_self = NULL;
  PyObject *const *__pyx_args = args;
  Py_ssize_t __pyx_nargs = PyVectorcall_NARGS(nargsf);
  PyObject *__pyx_kwds = kwnames;
  __pyx_kwvalues = NULL;
  switch (__Pyx_CyFunction_Vectorcall_CheckArgs(cyfunc, __pyx_nargs, __pyx_kwds)) {
    case 1:
        __pyx_self = __pyx_args[0];
        __pyx_args += 1;
        __pyx_nargs -= 1;
        break;
    case 0:
    #if CYTHON_COMPILING_IN_LIMITED_API
        __pyx_self = PyCFunction_GetSelf(((__pyx_CyFunctionObject*)cyfunc)->func);
        if (unlikely(!__pyx_self) && PyErr_Occurred()) __PYX_ERR(0, 19, __pyx_L1_error)
    #else
        __pyx_self = ((PyCFunctionObject*)cyfunc)->m_self;
    #endif
        break;
    default:
        return NULL;
  }
  PyObject* values[3] = {0,0,0};
  __pyx_kwvalues = __Pyx_KwValues_FASTCALL(__pyx_args, __pyx_nargs);
  {
    PyObject **__pyx_fastlocals[3] = {&values[0], &values[1], &values[2]};
    int __pyx_fastparse_result = __Pyx_FastParseKeywords(&__pyx_pi___pyx_pw_15fastargs_kwonly_3pyx_3fastargs_positional, __pyx_args, __pyx_nargs, __pyx_kwds, __pyx_fastlocals);
    if (likely(__pyx_fastparse_result == __PYX_FASTPARSE_SUCCESS)) {
      goto __pyx_L4_vectorcall_argument_unpacking_done;
    }
    if (__pyx_fastparse_result == __PYX_FASTPARSE_ERROR) goto __pyx_L1_error;
  }
  __pyx_r = __pyx_pf_15fastargs_kwonly_3pyx_2fastargs_positional(__pyx_self, __pyx_v_a, __pyx_v_b, __pyx_v_c);
  int __pyx_lineno = 0;
  const char *__pyx_filename = NULL;
  int __pyx_clineno = 0;

  /* vectorcall exit code */
  goto __pyx_L0;
  __pyx_L1_error:;
  __pyx_r = NULL;
  for (Py_ssize_t __pyx_temp=0; __pyx_temp < (Py_ssize_t)(sizeof(values)/sizeof(values[0])); ++__pyx_temp) {
    Py_XDECREF(values[__pyx_temp]);
  }
  goto __pyx_L5_vectorcall_cleaned_up;
  __pyx_L0:;
  for (Py_ssize_t __pyx_temp=0; __pyx_temp < (Py_ssize_t)(sizeof(values)/sizeof(values[0])); ++__pyx_temp) {
    Py_XDECREF(values[__pyx_temp]);
  }
  __pyx_L5_vectorcall_cleaned_up:;
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
  return Py_None;
}
#endif /* CYTHON_METH_FASTCALL && CYTHON_VECTORCALL */

static PyObject *__pyx_pf_15fastargs_kwonly_3pyx_2fastargs_positional(CYTHON_UNUSED PyObject *__pyx_self, PyObject *__pyx_v_a, PyObject *__pyx_v_b, PyObject *__pyx_v_c) {
  PyObject *__pyx_r = NULL;
/* … */
  /* function exit code */
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_t_1);
  __Pyx_AddTraceback("fastargs_kwonly.pyx.fastargs_positional", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_r = NULL;
  __pyx_L0:;
  __Pyx_XGIVEREF(__pyx_r);
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}
/* … */
  __pyx_t_2 = __Pyx_CyFunction_New(&__pyx_mdef_15fastargs_kwonly_3pyx_3fastargs_positional, __Pyx_CYFUNCTION_VECTORCALL_KEYWORDS, __pyx_mstate_global->__pyx_n_u_fastargs_positional, NULL, __pyx_mstate_global->__pyx_n_u_fastargs_kwonly_pyx, __pyx_mstate_global->__pyx_d, ((PyObject *)__pyx_mstate_global->__pyx_codeobj_tab[1])); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 19, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  #if CYTHON_COMPILING_IN_CPYTHON && PY_VERSION_HEX >= 0x030E0000
  PyUnstable_Object_EnableDeferredRefcount(__pyx_t_2);
  #endif
  #if CYTHON_METH_FASTCALL && CYTHON_VECTORCALL
  __Pyx_CyFunction_func_vectorcall(__pyx_t_2) = __pyx_vectorcall___pyx_pw_15fastargs_kwonly_3pyx_3fastargs_positional;
  #endif
  if (PyDict_SetItem(__pyx_mstate_global->__pyx_d, __pyx_mstate_global->__pyx_n_u_fastargs_positional, __pyx_t_2) < (0)) __PYX_ERR(0, 19, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
```

</details>

L20  ⚪  (score=0)
```python
    """
```
L21  ⚪  (score=0)
```python
    >>> fastargs_positional(1, 2, 3)
```
L22  ⚪  (score=0)
```python
    (1, 2, 3)
```
L23  ⚪  (score=0)
```python
    >>> _check_raises(fastargs_positional, (), {}, TypeError)
```
L24  ⚪  (score=0)
```python
    True
```
L25  ⚪  (score=0)
```python
    >>> _check_raises(fastargs_positional, (1,), {}, TypeError)
```
L26  ⚪  (score=0)
```python
    True
```
L27  ⚪  (score=0)
```python
    >>> _check_raises(fastargs_positional, (1, 2, 3, 4), {}, TypeError)
```
L28  ⚪  (score=0)
```python
    True
```
L29  ⚪  (score=0)
```python
    """
```
L30  🔴  (score=15)
```python
    return a, b, c
```
<details><summary>Show generated C (score=15)</summary>

```c
  __Pyx_XDECREF(__pyx_r);
  __pyx_t_1 = PyTuple_New(3); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 30, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_INCREF(__pyx_v_a);
  __Pyx_GIVEREF(__pyx_v_a);
  if (__Pyx_PyTuple_SET_ITEM(__pyx_t_1, 0, __pyx_v_a) != (0)) __PYX_ERR(0, 30, __pyx_L1_error);
  __Pyx_INCREF(__pyx_v_b);
  __Pyx_GIVEREF(__pyx_v_b);
  if (__Pyx_PyTuple_SET_ITEM(__pyx_t_1, 1, __pyx_v_b) != (0)) __PYX_ERR(0, 30, __pyx_L1_error);
  __Pyx_INCREF(__pyx_v_c);
  __Pyx_GIVEREF(__pyx_v_c);
  if (__Pyx_PyTuple_SET_ITEM(__pyx_t_1, 2, __pyx_v_c) != (0)) __PYX_ERR(0, 30, __pyx_L1_error);
  __pyx_r = __pyx_t_1;
  __pyx_t_1 = 0;
  goto __pyx_L0;
```

</details>

L31  ⚪  (score=0)
```python
```
L32  ⚪  (score=0)
```python
```
L33  🔴  (score=53)
```python
def fastargs_kwonly(*, a, b):
```
<details><summary>Show generated C (score=53)</summary>

```c
/* Python wrapper */
static PyObject *__pyx_pw_15fastargs_kwonly_3pyx_5fastargs_kwonly(PyObject *__pyx_self, 
#if CYTHON_METH_FASTCALL
PyObject *const *__pyx_args, Py_ssize_t __pyx_nargs, PyObject *__pyx_kwds
#else
PyObject *__pyx_args, PyObject *__pyx_kwds
#endif
); /*proto*/
PyDoc_STRVAR(__pyx_doc_15fastargs_kwonly_3pyx_4fastargs_kwonly, "File: tests/run/fastargs_kwonly.pyx (starting at line 33)\n\n    >>> fastargs_kwonly(a=1, b=2)\n    (1, 2)\n    >>> _check_raises(fastargs_kwonly, (1, 2), {}, TypeError)  # unexpected kwargs / no kwargs\n    True\n    >>> _check_raises(fastargs_kwonly, (), {\"a\": 1}, TypeError)  # missing required kw-only\n    True\n    ");
static PyMethodDef __pyx_mdef_15fastargs_kwonly_3pyx_5fastargs_kwonly = {"fastargs_kwonly", (PyCFunction)(void(*)(void))(__Pyx_PyCFunction_FastCallWithKeywords)__pyx_pw_15fastargs_kwonly_3pyx_5fastargs_kwonly, __Pyx_METH_FASTCALL|METH_KEYWORDS, __pyx_doc_15fastargs_kwonly_3pyx_4fastargs_kwonly};
static PyObject *__pyx_pw_15fastargs_kwonly_3pyx_5fastargs_kwonly(PyObject *__pyx_self, 
#if CYTHON_METH_FASTCALL
PyObject *const *__pyx_args, Py_ssize_t __pyx_nargs, PyObject *__pyx_kwds
#else
PyObject *__pyx_args, PyObject *__pyx_kwds
#endif
) {
  PyObject *__pyx_v_a = 0;
  PyObject *__pyx_v_b = 0;
  #if !CYTHON_METH_FASTCALL
  CYTHON_UNUSED Py_ssize_t __pyx_nargs;
  #endif
  CYTHON_UNUSED PyObject *const *__pyx_kwvalues;
  PyObject *__pyx_r = 0;
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("fastargs_kwonly (wrapper)", 0);
  #if !CYTHON_METH_FASTCALL
  #if CYTHON_ASSUME_SAFE_SIZE
  __pyx_nargs = PyTuple_GET_SIZE(__pyx_args);
  #else
  __pyx_nargs = PyTuple_Size(__pyx_args); if (unlikely(__pyx_nargs < 0)) return NULL;
  #endif
  #endif
  __pyx_kwvalues = __Pyx_KwValues_FASTCALL(__pyx_args, __pyx_nargs);
  PyObject* values[2] = {0,0};
  #if CYTHON_METH_FASTCALL
  {
    PyObject **__pyx_fastlocals[2] = {&values[0], &values[1]};
    int __pyx_fastparse_result = __Pyx_FastParseKeywords(&__pyx_pi___pyx_pw_15fastargs_kwonly_3pyx_5fastargs_kwonly, __pyx_args, __pyx_nargs, __pyx_kwds, __pyx_fastlocals);
    if (likely(__pyx_fastparse_result == __PYX_FASTPARSE_SUCCESS)) {
      goto __pyx_L4_argument_unpacking_done;
    }
    if (__pyx_fastparse_result == __PYX_FASTPARSE_ERROR) goto __pyx_L3_error;
  }
  #else
  {
    PyObject ** const __pyx_pyargnames[] = {&__pyx_mstate_global->__pyx_n_u_a,&__pyx_mstate_global->__pyx_n_u_b,0};
    const Py_ssize_t __pyx_kwds_len = (__pyx_kwds) ? __Pyx_NumKwargs_FASTCALL(__pyx_kwds) : 0;
    if (unlikely(__pyx_kwds_len) < 0) __PYX_ERR(0, 33, __pyx_L3_error)
    if (likely(__pyx_kwds_len > 0)) {
      switch (__pyx_nargs) {
        case  0: break;
        default: goto __pyx_L5_argtuple_error;
      }
      if (__Pyx_ParseKeywords(__pyx_kwds, __pyx_kwvalues, __pyx_pyargnames, 0, values, 0, __pyx_kwds_len, "fastargs_kwonly", 0) < (0)) __PYX_ERR(0, 33, __pyx_L3_error)
      for (Py_ssize_t i = 0; i < 2; i++) {
        if (unlikely(!values[i])) { __Pyx_RaiseKeywordRequired("fastargs_kwonly", *(__pyx_pyargnames[i - 0])); __PYX_ERR(0, 33, __pyx_L3_error) }
      }
    } else if (unlikely(__pyx_nargs != 0)) {
      goto __pyx_L5_argtuple_error;
    } else {
      __Pyx_RaiseKeywordRequired("fastargs_kwonly", __pyx_mstate_global->__pyx_n_u_a); __PYX_ERR(0, 33, __pyx_L3_error)
    }
    __pyx_v_a = values[0];
    __pyx_v_b = values[1];
  }
  goto __pyx_L6_skip;
  __pyx_L5_argtuple_error:;
  __Pyx_RaiseArgtupleInvalid("fastargs_kwonly", 1, 0, 0, __pyx_nargs); __PYX_ERR(0, 33, __pyx_L3_error)
  __pyx_L6_skip:;
  #endif
  goto __pyx_L4_argument_unpacking_done;
  __pyx_L3_error:;
  for (Py_ssize_t __pyx_temp=0; __pyx_temp < (Py_ssize_t)(sizeof(values)/sizeof(values[0])); ++__pyx_temp) {
    Py_XDECREF(values[__pyx_temp]);
  }
  __Pyx_AddTraceback("fastargs_kwonly.pyx.fastargs_kwonly", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __Pyx_RefNannyFinishContext();
  return NULL;
  __pyx_L4_argument_unpacking_done:;
  __pyx_r = __pyx_pf_15fastargs_kwonly_3pyx_4fastargs_kwonly(__pyx_self, __pyx_v_a, __pyx_v_b);
  int __pyx_lineno = 0;
  const char *__pyx_filename = NULL;
  int __pyx_clineno = 0;

  /* function exit code */
  for (Py_ssize_t __pyx_temp=0; __pyx_temp < (Py_ssize_t)(sizeof(values)/sizeof(values[0])); ++__pyx_temp) {
    Py_XDECREF(values[__pyx_temp]);
  }
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}
#if CYTHON_METH_FASTCALL && CYTHON_VECTORCALL
static PyObject *__pyx_vectorcall___pyx_pw_15fastargs_kwonly_3pyx_5fastargs_kwonly(PyObject *func, PyObject *const *args, size_t nargsf, PyObject *kwnames) {
  PyObject *__pyx_v_a = 0;
  PyObject *__pyx_v_b = 0;
  #if !CYTHON_METH_FASTCALL
  CYTHON_UNUSED Py_ssize_t __pyx_nargs;
  #endif
  CYTHON_UNUSED PyObject *const *__pyx_kwvalues;
  PyObject *__pyx_r = 0;
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("fastargs_kwonly (vectorcall)", 0);
  __pyx_CyFunctionObject *cyfunc = (__pyx_CyFunctionObject *)func;
  PyObject *__pyx_self = NULL;
  PyObject *const *__pyx_args = args;
  Py_ssize_t __pyx_nargs = PyVectorcall_NARGS(nargsf);
  PyObject *__pyx_kwds = kwnames;
  __pyx_kwvalues = NULL;
  switch (__Pyx_CyFunction_Vectorcall_CheckArgs(cyfunc, __pyx_nargs, __pyx_kwds)) {
    case 1:
        __pyx_self = __pyx_args[0];
        __pyx_args += 1;
        __pyx_nargs -= 1;
        break;
    case 0:
    #if CYTHON_COMPILING_IN_LIMITED_API
        __pyx_self = PyCFunction_GetSelf(((__pyx_CyFunctionObject*)cyfunc)->func);
        if (unlikely(!__pyx_self) && PyErr_Occurred()) __PYX_ERR(0, 33, __pyx_L1_error)
    #else
        __pyx_self = ((PyCFunctionObject*)cyfunc)->m_self;
    #endif
        break;
    default:
        return NULL;
  }
  PyObject* values[2] = {0,0};
  __pyx_kwvalues = __Pyx_KwValues_FASTCALL(__pyx_args, __pyx_nargs);
  {
    PyObject **__pyx_fastlocals[2] = {&values[0], &values[1]};
    int __pyx_fastparse_result = __Pyx_FastParseKeywords(&__pyx_pi___pyx_pw_15fastargs_kwonly_3pyx_5fastargs_kwonly, __pyx_args, __pyx_nargs, __pyx_kwds, __pyx_fastlocals);
    if (likely(__pyx_fastparse_result == __PYX_FASTPARSE_SUCCESS)) {
      goto __pyx_L4_vectorcall_argument_unpacking_done;
    }
    if (__pyx_fastparse_result == __PYX_FASTPARSE_ERROR) goto __pyx_L1_error;
  }
  __pyx_r = __pyx_pf_15fastargs_kwonly_3pyx_4fastargs_kwonly(__pyx_self, __pyx_v_a, __pyx_v_b);
  int __pyx_lineno = 0;
  const char *__pyx_filename = NULL;
  int __pyx_clineno = 0;

  /* vectorcall exit code */
  goto __pyx_L0;
  __pyx_L1_error:;
  __pyx_r = NULL;
  for (Py_ssize_t __pyx_temp=0; __pyx_temp < (Py_ssize_t)(sizeof(values)/sizeof(values[0])); ++__pyx_temp) {
    Py_XDECREF(values[__pyx_temp]);
  }
  goto __pyx_L5_vectorcall_cleaned_up;
  __pyx_L0:;
  for (Py_ssize_t __pyx_temp=0; __pyx_temp < (Py_ssize_t)(sizeof(values)/sizeof(values[0])); ++__pyx_temp) {
    Py_XDECREF(values[__pyx_temp]);
  }
  __pyx_L5_vectorcall_cleaned_up:;
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
  return Py_None;
}
#endif /* CYTHON_METH_FASTCALL && CYTHON_VECTORCALL */

static PyObject *__pyx_pf_15fastargs_kwonly_3pyx_4fastargs_kwonly(CYTHON_UNUSED PyObject *__pyx_self, PyObject *__pyx_v_a, PyObject *__pyx_v_b) {
  PyObject *__pyx_r = NULL;
/* … */
  /* function exit code */
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_t_1);
  __Pyx_AddTraceback("fastargs_kwonly.pyx.fastargs_kwonly", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_r = NULL;
  __pyx_L0:;
  __Pyx_XGIVEREF(__pyx_r);
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}
/* … */
  __pyx_t_2 = __Pyx_CyFunction_New(&__pyx_mdef_15fastargs_kwonly_3pyx_5fastargs_kwonly, __Pyx_CYFUNCTION_VECTORCALL_KEYWORDS, __pyx_mstate_global->__pyx_n_u_fastargs_kwonly, NULL, __pyx_mstate_global->__pyx_n_u_fastargs_kwonly_pyx, __pyx_mstate_global->__pyx_d, ((PyObject *)__pyx_mstate_global->__pyx_codeobj_tab[2])); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 33, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  #if CYTHON_COMPILING_IN_CPYTHON && PY_VERSION_HEX >= 0x030E0000
  PyUnstable_Object_EnableDeferredRefcount(__pyx_t_2);
  #endif
  #if CYTHON_METH_FASTCALL && CYTHON_VECTORCALL
  __Pyx_CyFunction_func_vectorcall(__pyx_t_2) = __pyx_vectorcall___pyx_pw_15fastargs_kwonly_3pyx_5fastargs_kwonly;
  #endif
  if (PyDict_SetItem(__pyx_mstate_global->__pyx_d, __pyx_mstate_global->__pyx_n_u_fastargs_kwonly, __pyx_t_2) < (0)) __PYX_ERR(0, 33, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
```

</details>

L34  ⚪  (score=0)
```python
    """
```
L35  ⚪  (score=0)
```python
    >>> fastargs_kwonly(a=1, b=2)
```
L36  ⚪  (score=0)
```python
    (1, 2)
```
L37  ⚪  (score=0)
```python
    >>> _check_raises(fastargs_kwonly, (1, 2), {}, TypeError)  # unexpected kwargs / no kwargs
```
L38  ⚪  (score=0)
```python
    True
```
L39  ⚪  (score=0)
```python
    >>> _check_raises(fastargs_kwonly, (), {"a": 1}, TypeError)  # missing required kw-only
```
L40  ⚪  (score=0)
```python
    True
```
L41  ⚪  (score=0)
```python
    """
```
L42  🔴  (score=12)
```python
    return a, b
```
<details><summary>Show generated C (score=12)</summary>

```c
  __Pyx_XDECREF(__pyx_r);
  __pyx_t_1 = PyTuple_New(2); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 42, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_INCREF(__pyx_v_a);
  __Pyx_GIVEREF(__pyx_v_a);
  if (__Pyx_PyTuple_SET_ITEM(__pyx_t_1, 0, __pyx_v_a) != (0)) __PYX_ERR(0, 42, __pyx_L1_error);
  __Pyx_INCREF(__pyx_v_b);
  __Pyx_GIVEREF(__pyx_v_b);
  if (__Pyx_PyTuple_SET_ITEM(__pyx_t_1, 1, __pyx_v_b) != (0)) __PYX_ERR(0, 42, __pyx_L1_error);
  __pyx_r = __pyx_t_1;
  __pyx_t_1 = 0;
  goto __pyx_L0;
```

</details>

L43  ⚪  (score=0)
```python
```
L44  ⚪  (score=0)
```python
```
L45  🔴  (score=90)
```python
def fastargs_mixed(a, *, b, c=0):
```
<details><summary>Show generated C (score=90)</summary>

```c
/* Python wrapper */
static PyObject *__pyx_pw_15fastargs_kwonly_3pyx_7fastargs_mixed(PyObject *__pyx_self, 
#if CYTHON_METH_FASTCALL
PyObject *const *__pyx_args, Py_ssize_t __pyx_nargs, PyObject *__pyx_kwds
#else
PyObject *__pyx_args, PyObject *__pyx_kwds
#endif
); /*proto*/
PyDoc_STRVAR(__pyx_doc_15fastargs_kwonly_3pyx_6fastargs_mixed, "File: tests/run/fastargs_kwonly.pyx (starting at line 45)\n\n    >>> fastargs_mixed(1, b=2)\n    (1, 2, 0)\n    >>> fastargs_mixed(1, b=2, c=3)\n    (1, 2, 3)\n    >>> _check_raises(fastargs_mixed, (), {\"b\": 2}, TypeError)  # missing positional\n    True\n    >>> _check_raises(fastargs_mixed, (1,), {}, TypeError)  # missing required kw-only\n    True\n    >>> _check_raises(fastargs_mixed, (1,), {\"b\": 2, \"d\": 4}, TypeError)  # unexpected kw\n    True\n    ");
static PyMethodDef __pyx_mdef_15fastargs_kwonly_3pyx_7fastargs_mixed = {"fastargs_mixed", (PyCFunction)(void(*)(void))(__Pyx_PyCFunction_FastCallWithKeywords)__pyx_pw_15fastargs_kwonly_3pyx_7fastargs_mixed, __Pyx_METH_FASTCALL|METH_KEYWORDS, __pyx_doc_15fastargs_kwonly_3pyx_6fastargs_mixed};
static PyObject *__pyx_pw_15fastargs_kwonly_3pyx_7fastargs_mixed(PyObject *__pyx_self, 
#if CYTHON_METH_FASTCALL
PyObject *const *__pyx_args, Py_ssize_t __pyx_nargs, PyObject *__pyx_kwds
#else
PyObject *__pyx_args, PyObject *__pyx_kwds
#endif
) {
  PyObject *__pyx_v_a = 0;
  PyObject *__pyx_v_b = 0;
  PyObject *__pyx_v_c = 0;
  #if !CYTHON_METH_FASTCALL
  CYTHON_UNUSED Py_ssize_t __pyx_nargs;
  #endif
  CYTHON_UNUSED PyObject *const *__pyx_kwvalues;
  PyObject *__pyx_r = 0;
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("fastargs_mixed (wrapper)", 0);
  #if !CYTHON_METH_FASTCALL
  #if CYTHON_ASSUME_SAFE_SIZE
  __pyx_nargs = PyTuple_GET_SIZE(__pyx_args);
  #else
  __pyx_nargs = PyTuple_Size(__pyx_args); if (unlikely(__pyx_nargs < 0)) return NULL;
  #endif
  #endif
  __pyx_kwvalues = __Pyx_KwValues_FASTCALL(__pyx_args, __pyx_nargs);
  PyObject* values[3] = {0,0,0};
  #if CYTHON_METH_FASTCALL
  {
    PyObject **__pyx_fastlocals[3] = {&values[0], &values[1], &values[2]};
    int __pyx_fastparse_result = __Pyx_FastParseKeywords(&__pyx_pi___pyx_pw_15fastargs_kwonly_3pyx_7fastargs_mixed, __pyx_args, __pyx_nargs, __pyx_kwds, __pyx_fastlocals);
    if (likely(__pyx_fastparse_result == __PYX_FASTPARSE_SUCCESS)) {
      if (!values[2]) values[2] = __Pyx_NewRef(((PyObject *)((PyObject*)__pyx_mstate_global->__pyx_int_0)));
      goto __pyx_L4_argument_unpacking_done;
    }
    if (__pyx_fastparse_result == __PYX_FASTPARSE_ERROR) goto __pyx_L3_error;
  }
  #else
  {
    PyObject ** const __pyx_pyargnames[] = {&__pyx_mstate_global->__pyx_n_u_a,&__pyx_mstate_global->__pyx_n_u_b,&__pyx_mstate_global->__pyx_n_u_c,0};
    const Py_ssize_t __pyx_kwds_len = (__pyx_kwds) ? __Pyx_NumKwargs_FASTCALL(__pyx_kwds) : 0;
    if (unlikely(__pyx_kwds_len) < 0) __PYX_ERR(0, 45, __pyx_L3_error)
    if (likely(__pyx_kwds_len > 0)) {
      switch (__pyx_nargs) {
        case  1:
        values[0] = __Pyx_ArgRef_FASTCALL(__pyx_args, 0);
        if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[0])) __PYX_ERR(0, 45, __pyx_L3_error)
        CYTHON_FALLTHROUGH;
        case  0: break;
        default: goto __pyx_L5_argtuple_error;
      }
      const Py_ssize_t kwd_pos_args = __pyx_nargs;
      if (__Pyx_ParseKeywords(__pyx_kwds, __pyx_kwvalues, __pyx_pyargnames, 0, values, kwd_pos_args, __pyx_kwds_len, "fastargs_mixed", 0) < (0)) __PYX_ERR(0, 45, __pyx_L3_error)
      if (!values[2]) values[2] = __Pyx_NewRef(((PyObject *)((PyObject*)__pyx_mstate_global->__pyx_int_0)));
      for (Py_ssize_t i = __pyx_nargs; i < 1; i++) {
        if (unlikely(!values[i])) { __Pyx_RaiseArgtupleInvalid("fastargs_mixed", 1, 1, 1, i); __PYX_ERR(0, 45, __pyx_L3_error) }
      }
      for (Py_ssize_t i = 1; i < 2; i++) {
        if (unlikely(!values[i])) { __Pyx_RaiseKeywordRequired("fastargs_mixed", *(__pyx_pyargnames[i - 0])); __PYX_ERR(0, 45, __pyx_L3_error) }
      }
    } else if (unlikely(__pyx_nargs != 1)) {
      goto __pyx_L5_argtuple_error;
    } else {
      __Pyx_RaiseKeywordRequired("fastargs_mixed", __pyx_mstate_global->__pyx_n_u_b); __PYX_ERR(0, 45, __pyx_L3_error)
    }
    __pyx_v_a = values[0];
    __pyx_v_b = values[1];
    __pyx_v_c = values[2];
  }
  goto __pyx_L6_skip;
  __pyx_L5_argtuple_error:;
  __Pyx_RaiseArgtupleInvalid("fastargs_mixed", 1, 1, 1, __pyx_nargs); __PYX_ERR(0, 45, __pyx_L3_error)
  __pyx_L6_skip:;
  #endif
  goto __pyx_L4_argument_unpacking_done;
  __pyx_L3_error:;
  for (Py_ssize_t __pyx_temp=0; __pyx_temp < (Py_ssize_t)(sizeof(values)/sizeof(values[0])); ++__pyx_temp) {
    Py_XDECREF(values[__pyx_temp]);
  }
  __Pyx_AddTraceback("fastargs_kwonly.pyx.fastargs_mixed", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __Pyx_RefNannyFinishContext();
  return NULL;
  __pyx_L4_argument_unpacking_done:;
  __pyx_r = __pyx_pf_15fastargs_kwonly_3pyx_6fastargs_mixed(__pyx_self, __pyx_v_a, __pyx_v_b, __pyx_v_c);
  int __pyx_lineno = 0;
  const char *__pyx_filename = NULL;
  int __pyx_clineno = 0;

  /* function exit code */
  for (Py_ssize_t __pyx_temp=0; __pyx_temp < (Py_ssize_t)(sizeof(values)/sizeof(values[0])); ++__pyx_temp) {
    Py_XDECREF(values[__pyx_temp]);
  }
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}
#if CYTHON_METH_FASTCALL && CYTHON_VECTORCALL
static PyObject *__pyx_vectorcall___pyx_pw_15fastargs_kwonly_3pyx_7fastargs_mixed(PyObject *func, PyObject *const *args, size_t nargsf, PyObject *kwnames) {
  PyObject *__pyx_v_a = 0;
  PyObject *__pyx_v_b = 0;
  PyObject *__pyx_v_c = 0;
  #if !CYTHON_METH_FASTCALL
  CYTHON_UNUSED Py_ssize_t __pyx_nargs;
  #endif
  CYTHON_UNUSED PyObject *const *__pyx_kwvalues;
  PyObject *__pyx_r = 0;
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("fastargs_mixed (vectorcall)", 0);
  __pyx_CyFunctionObject *cyfunc = (__pyx_CyFunctionObject *)func;
  PyObject *__pyx_self = NULL;
  PyObject *const *__pyx_args = args;
  Py_ssize_t __pyx_nargs = PyVectorcall_NARGS(nargsf);
  PyObject *__pyx_kwds = kwnames;
  __pyx_kwvalues = NULL;
  switch (__Pyx_CyFunction_Vectorcall_CheckArgs(cyfunc, __pyx_nargs, __pyx_kwds)) {
    case 1:
        __pyx_self = __pyx_args[0];
        __pyx_args += 1;
        __pyx_nargs -= 1;
        break;
    case 0:
    #if CYTHON_COMPILING_IN_LIMITED_API
        __pyx_self = PyCFunction_GetSelf(((__pyx_CyFunctionObject*)cyfunc)->func);
        if (unlikely(!__pyx_self) && PyErr_Occurred()) __PYX_ERR(0, 45, __pyx_L1_error)
    #else
        __pyx_self = ((PyCFunctionObject*)cyfunc)->m_self;
    #endif
        break;
    default:
        return NULL;
  }
  PyObject* values[3] = {0,0,0};
  __pyx_kwvalues = __Pyx_KwValues_FASTCALL(__pyx_args, __pyx_nargs);
  {
    PyObject **__pyx_fastlocals[3] = {&values[0], &values[1], &values[2]};
    int __pyx_fastparse_result = __Pyx_FastParseKeywords(&__pyx_pi___pyx_pw_15fastargs_kwonly_3pyx_7fastargs_mixed, __pyx_args, __pyx_nargs, __pyx_kwds, __pyx_fastlocals);
    if (likely(__pyx_fastparse_result == __PYX_FASTPARSE_SUCCESS)) {
      if (!values[2]) values[2] = __Pyx_NewRef(((PyObject *)((PyObject*)__pyx_mstate_global->__pyx_int_0)));
      goto __pyx_L4_vectorcall_argument_unpacking_done;
    }
    if (__pyx_fastparse_result == __PYX_FASTPARSE_ERROR) goto __pyx_L1_error;
  }
  __pyx_r = __pyx_pf_15fastargs_kwonly_3pyx_6fastargs_mixed(__pyx_self, __pyx_v_a, __pyx_v_b, __pyx_v_c);
  int __pyx_lineno = 0;
  const char *__pyx_filename = NULL;
  int __pyx_clineno = 0;

  /* vectorcall exit code */
  goto __pyx_L0;
  __pyx_L1_error:;
  __pyx_r = NULL;
  for (Py_ssize_t __pyx_temp=0; __pyx_temp < (Py_ssize_t)(sizeof(values)/sizeof(values[0])); ++__pyx_temp) {
    Py_XDECREF(values[__pyx_temp]);
  }
  goto __pyx_L5_vectorcall_cleaned_up;
  __pyx_L0:;
  for (Py_ssize_t __pyx_temp=0; __pyx_temp < (Py_ssize_t)(sizeof(values)/sizeof(values[0])); ++__pyx_temp) {
    Py_XDECREF(values[__pyx_temp]);
  }
  __pyx_L5_vectorcall_cleaned_up:;
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
  return Py_None;
}
#endif /* CYTHON_METH_FASTCALL && CYTHON_VECTORCALL */

static PyObject *__pyx_pf_15fastargs_kwonly_3pyx_6fastargs_mixed(CYTHON_UNUSED PyObject *__pyx_self, PyObject *__pyx_v_a, PyObject *__pyx_v_b, PyObject *__pyx_v_c) {
  PyObject *__pyx_r = NULL;
/* … */
  __pyx_t_2 = __Pyx_PyDict_NewPresized(1); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 45, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  #if defined(PyDict_SetItem) && (defined(CYTHON_COMPILING_IN_CPYTHON))
  #if PY_VERSION_HEX >= 0x030A0000 /* CPython 3.10+ exposes KnownHash APIs */
  /* Use CPython's KnownHash APIs when available */
  extern int _PyDict_SetItem_KnownHash(PyObject*, PyObject*, PyObject*, Py_hash_t);
  {
    Py_hash_t __pyx_hash = PyObject_Hash(__pyx_mstate_global->__pyx_n_u_c); if (unlikely(__pyx_hash == -1)) __PYX_ERR(0, 45, __pyx_L1_error);
    if (unlikely(_PyDict_SetItem_KnownHash(__pyx_t_2, __pyx_mstate_global->__pyx_n_u_c, ((PyObject*)__pyx_mstate_global->__pyx_int_0), __pyx_hash) < 0)) __PYX_ERR(0, 45, __pyx_L1_error);
  }
  #else
  if (PyDict_SetItem(__pyx_t_2, __pyx_mstate_global->__pyx_n_u_c, ((PyObject*)__pyx_mstate_global->__pyx_int_0)) < (0)) __PYX_ERR(0, 45, __pyx_L1_error)
  #endif
  #else
  if (PyDict_SetItem(__pyx_t_2, __pyx_mstate_global->__pyx_n_u_c, ((PyObject*)__pyx_mstate_global->__pyx_int_0)) < (0)) __PYX_ERR(0, 45, __pyx_L1_error)
  #endif
  __pyx_t_3 = __Pyx_CyFunction_New(&__pyx_mdef_15fastargs_kwonly_3pyx_7fastargs_mixed, __Pyx_CYFUNCTION_VECTORCALL_KEYWORDS, __pyx_mstate_global->__pyx_n_u_fastargs_mixed, NULL, __pyx_mstate_global->__pyx_n_u_fastargs_kwonly_pyx, __pyx_mstate_global->__pyx_d, ((PyObject *)__pyx_mstate_global->__pyx_codeobj_tab[3])); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 45, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_3);
  #if CYTHON_COMPILING_IN_CPYTHON && PY_VERSION_HEX >= 0x030E0000
  PyUnstable_Object_EnableDeferredRefcount(__pyx_t_3);
  #endif
  __Pyx_CyFunction_SetDefaultsKwDict(__pyx_t_3, __pyx_t_2);
  #if CYTHON_METH_FASTCALL && CYTHON_VECTORCALL
  __Pyx_CyFunction_func_vectorcall(__pyx_t_3) = __pyx_vectorcall___pyx_pw_15fastargs_kwonly_3pyx_7fastargs_mixed;
  #endif
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  if (PyDict_SetItem(__pyx_mstate_global->__pyx_d, __pyx_mstate_global->__pyx_n_u_fastargs_mixed, __pyx_t_3) < (0)) __PYX_ERR(0, 45, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
```

</details>

L46  ⚪  (score=0)
```python
    """
```
L47  ⚪  (score=0)
```python
    >>> fastargs_mixed(1, b=2)
```
L48  ⚪  (score=0)
```python
    (1, 2, 0)
```
L49  ⚪  (score=0)
```python
    >>> fastargs_mixed(1, b=2, c=3)
```
L50  ⚪  (score=0)
```python
    (1, 2, 3)
```
L51  ⚪  (score=0)
```python
    >>> _check_raises(fastargs_mixed, (), {"b": 2}, TypeError)  # missing positional
```
L52  ⚪  (score=0)
```python
    True
```
L53  ⚪  (score=0)
```python
    >>> _check_raises(fastargs_mixed, (1,), {}, TypeError)  # missing required kw-only
```
L54  ⚪  (score=0)
```python
    True
```
L55  ⚪  (score=0)
```python
    >>> _check_raises(fastargs_mixed, (1,), {"b": 2, "d": 4}, TypeError)  # unexpected kw
```
L56  ⚪  (score=0)
```python
    True
```
L57  ⚪  (score=0)
```python
    """
```
L58  🔴  (score=15)
```python
    return a, b, c
```
<details><summary>Show generated C (score=15)</summary>

```c
  __Pyx_XDECREF(__pyx_r);
  __pyx_t_1 = PyTuple_New(3); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 58, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_INCREF(__pyx_v_a);
  __Pyx_GIVEREF(__pyx_v_a);
  if (__Pyx_PyTuple_SET_ITEM(__pyx_t_1, 0, __pyx_v_a) != (0)) __PYX_ERR(0, 58, __pyx_L1_error);
  __Pyx_INCREF(__pyx_v_b);
  __Pyx_GIVEREF(__pyx_v_b);
  if (__Pyx_PyTuple_SET_ITEM(__pyx_t_1, 1, __pyx_v_b) != (0)) __PYX_ERR(0, 58, __pyx_L1_error);
  __Pyx_INCREF(__pyx_v_c);
  __Pyx_GIVEREF(__pyx_v_c);
  if (__Pyx_PyTuple_SET_ITEM(__pyx_t_1, 2, __pyx_v_c) != (0)) __PYX_ERR(0, 58, __pyx_L1_error);
  __pyx_r = __pyx_t_1;
  __pyx_t_1 = 0;
  goto __pyx_L0;
```

</details>

L59  ⚪  (score=0)
```python
```
L60  ⚪  (score=0)
```python
```
