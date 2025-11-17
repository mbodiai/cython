# Cython annotation for Scanning.py

Raw output: Scanning.c

L1  🟠  (score=8)
```python
# cython: infer_types=True
```
<details><summary>Show generated C (score=8)</summary>

```c
  __pyx_t_4 = __Pyx_PyDict_NewPresized(0); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 1, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_4);
  if (PyDict_SetItem(__pyx_mstate_global->__pyx_d, __pyx_mstate_global->__pyx_n_u_test, __pyx_t_4) < (0)) __PYX_ERR(0, 1, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
```

</details>

L2  ⚪  (score=0)
```python
#
```
L3  ⚪  (score=0)
```python
#   Cython Scanner
```
L4  ⚪  (score=0)
```python
#
```
L5  ⚪  (score=0)
```python
```
L6  ⚪  (score=0)
```python
```
L7  ⚪  (score=0)
```python
import cython
```
L8  ⚪  (score=0)
```python
```
L9  ⚪  (score=0)
```python
cython.declare(make_lexicon=object, lexicon=object,
```
L10  ⚪  (score=0)
```python
               print_function=object, error=object, warning=object,
```
L11  ⚪  (score=0)
```python
               os=object, platform=object)
```
L12  🟡  (score=3)
```python
import os
```
<details><summary>Show generated C (score=3)</summary>

```c
  __pyx_t_1 = __Pyx_Import(__pyx_mstate_global->__pyx_n_u_os, 0, 0, NULL, 0); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 12, __pyx_L1_error)
  __pyx_t_2 = __pyx_t_1;
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_XGOTREF(__pyx_v_6Cython_8Compiler_8Scanning_os);
  __Pyx_DECREF_SET(__pyx_v_6Cython_8Compiler_8Scanning_os, __pyx_t_2);
  __Pyx_GIVEREF(__pyx_t_2);
  __pyx_t_2 = 0;
```

</details>

L13  🟡  (score=3)
```python
import platform
```
<details><summary>Show generated C (score=3)</summary>

```c
  __pyx_t_1 = __Pyx_Import(__pyx_mstate_global->__pyx_n_u_platform, 0, 0, NULL, 0); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 13, __pyx_L1_error)
  __pyx_t_2 = __pyx_t_1;
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_XGOTREF(__pyx_v_6Cython_8Compiler_8Scanning_platform);
  __Pyx_DECREF_SET(__pyx_v_6Cython_8Compiler_8Scanning_platform, __pyx_t_2);
  __Pyx_GIVEREF(__pyx_t_2);
  __pyx_t_2 = 0;
```

</details>

L14  🔴  (score=26)
```python
from contextlib import contextmanager
```
<details><summary>Show generated C (score=26)</summary>

```c
  {
    PyObject* const __pyx_imported_names[] = {__pyx_mstate_global->__pyx_n_u_contextmanager};
    __pyx_t_1 = __Pyx_Import(__pyx_mstate_global->__pyx_n_u_contextlib, __pyx_imported_names, 1, NULL, 0); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 14, __pyx_L1_error)
  }
  __pyx_t_2 = __pyx_t_1;
  __Pyx_GOTREF(__pyx_t_2);
  {
    PyObject* const __pyx_imported_names[] = {__pyx_mstate_global->__pyx_n_u_contextmanager};
    for (__pyx_t_3=0; __pyx_t_3 < 1; __pyx_t_3++) {
      __pyx_t_4 = __Pyx_ImportFrom(__pyx_t_2, __pyx_imported_names[__pyx_t_3]); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 14, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_4);
      switch (__pyx_t_3) {
        case 0:
        #if CYTHON_COMPILING_IN_CPYTHON && PY_VERSION_HEX >= 0x030A0000 && !CYTHON_COMPILING_IN_LIMITED_API
        extern int _PyDict_SetItem_KnownHash(PyObject*, PyObject*, PyObject*, Py_hash_t);
        {
              Py_hash_t __pyx_hash = PyObject_Hash(__pyx_imported_names[__pyx_t_3]);
              if (unlikely(__pyx_hash == -1)) __PYX_ERR(0, 14, __pyx_L1_error);
          if (_PyDict_SetItem_KnownHash(__pyx_mstate_global->__pyx_d, __pyx_imported_names[__pyx_t_3], __pyx_t_4, __pyx_hash) < (0)) __PYX_ERR(0, 14, __pyx_L1_error)
        }
        #else
        if (PyDict_SetItem(__pyx_mstate_global->__pyx_d, __pyx_imported_names[__pyx_t_3], __pyx_t_4) < (0)) __PYX_ERR(0, 14, __pyx_L1_error)
        #endif
        break;
      }
      __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
    }
  }
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
```

</details>

L15  🔴  (score=26)
```python
from pathlib import Path
```
<details><summary>Show generated C (score=26)</summary>

```c
  {
    PyObject* const __pyx_imported_names[] = {__pyx_mstate_global->__pyx_n_u_Path};
    __pyx_t_1 = __Pyx_Import(__pyx_mstate_global->__pyx_n_u_pathlib, __pyx_imported_names, 1, NULL, 0); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 15, __pyx_L1_error)
  }
  __pyx_t_2 = __pyx_t_1;
  __Pyx_GOTREF(__pyx_t_2);
  {
    PyObject* const __pyx_imported_names[] = {__pyx_mstate_global->__pyx_n_u_Path};
    for (__pyx_t_3=0; __pyx_t_3 < 1; __pyx_t_3++) {
      __pyx_t_4 = __Pyx_ImportFrom(__pyx_t_2, __pyx_imported_names[__pyx_t_3]); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 15, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_4);
      switch (__pyx_t_3) {
        case 0:
        #if CYTHON_COMPILING_IN_CPYTHON && PY_VERSION_HEX >= 0x030A0000 && !CYTHON_COMPILING_IN_LIMITED_API
        extern int _PyDict_SetItem_KnownHash(PyObject*, PyObject*, PyObject*, Py_hash_t);
        {
              Py_hash_t __pyx_hash = PyObject_Hash(__pyx_imported_names[__pyx_t_3]);
              if (unlikely(__pyx_hash == -1)) __PYX_ERR(0, 15, __pyx_L1_error);
          if (_PyDict_SetItem_KnownHash(__pyx_mstate_global->__pyx_d, __pyx_imported_names[__pyx_t_3], __pyx_t_4, __pyx_hash) < (0)) __PYX_ERR(0, 15, __pyx_L1_error)
        }
        #else
        if (PyDict_SetItem(__pyx_mstate_global->__pyx_d, __pyx_imported_names[__pyx_t_3], __pyx_t_4) < (0)) __PYX_ERR(0, 15, __pyx_L1_error)
        #endif
        break;
      }
      __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
    }
  }
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
```

</details>

L16  🔴  (score=26)
```python
from typing import IO, TYPE_CHECKING
```
<details><summary>Show generated C (score=26)</summary>

```c
  {
    PyObject* const __pyx_imported_names[] = {__pyx_mstate_global->__pyx_n_u_IO,__pyx_mstate_global->__pyx_n_u_TYPE_CHECKING};
    __pyx_t_1 = __Pyx_Import(__pyx_mstate_global->__pyx_n_u_typing, __pyx_imported_names, 2, NULL, 0); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 16, __pyx_L1_error)
  }
  __pyx_t_2 = __pyx_t_1;
  __Pyx_GOTREF(__pyx_t_2);
  {
    PyObject* const __pyx_imported_names[] = {__pyx_mstate_global->__pyx_n_u_IO,__pyx_mstate_global->__pyx_n_u_TYPE_CHECKING};
    for (__pyx_t_3=0; __pyx_t_3 < 2; __pyx_t_3++) {
      __pyx_t_4 = __Pyx_ImportFrom(__pyx_t_2, __pyx_imported_names[__pyx_t_3]); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 16, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_4);
      switch (__pyx_t_3) {
        case 0: case 1:
        #if CYTHON_COMPILING_IN_CPYTHON && PY_VERSION_HEX >= 0x030A0000 && !CYTHON_COMPILING_IN_LIMITED_API
        extern int _PyDict_SetItem_KnownHash(PyObject*, PyObject*, PyObject*, Py_hash_t);
        {
              Py_hash_t __pyx_hash = PyObject_Hash(__pyx_imported_names[__pyx_t_3]);
              if (unlikely(__pyx_hash == -1)) __PYX_ERR(0, 16, __pyx_L1_error);
          if (_PyDict_SetItem_KnownHash(__pyx_mstate_global->__pyx_d, __pyx_imported_names[__pyx_t_3], __pyx_t_4, __pyx_hash) < (0)) __PYX_ERR(0, 16, __pyx_L1_error)
        }
        #else
        if (PyDict_SetItem(__pyx_mstate_global->__pyx_d, __pyx_imported_names[__pyx_t_3], __pyx_t_4) < (0)) __PYX_ERR(0, 16, __pyx_L1_error)
        #endif
        break;
      }
      __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
    }
  }
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
```

</details>

L17  🔴  (score=26)
```python
from unicodedata import normalize
```
<details><summary>Show generated C (score=26)</summary>

```c
  {
    PyObject* const __pyx_imported_names[] = {__pyx_mstate_global->__pyx_n_u_normalize};
    __pyx_t_1 = __Pyx_Import(__pyx_mstate_global->__pyx_n_u_unicodedata, __pyx_imported_names, 1, NULL, 0); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 17, __pyx_L1_error)
  }
  __pyx_t_2 = __pyx_t_1;
  __Pyx_GOTREF(__pyx_t_2);
  {
    PyObject* const __pyx_imported_names[] = {__pyx_mstate_global->__pyx_n_u_normalize};
    for (__pyx_t_3=0; __pyx_t_3 < 1; __pyx_t_3++) {
      __pyx_t_4 = __Pyx_ImportFrom(__pyx_t_2, __pyx_imported_names[__pyx_t_3]); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 17, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_4);
      switch (__pyx_t_3) {
        case 0:
        #if CYTHON_COMPILING_IN_CPYTHON && PY_VERSION_HEX >= 0x030A0000 && !CYTHON_COMPILING_IN_LIMITED_API
        extern int _PyDict_SetItem_KnownHash(PyObject*, PyObject*, PyObject*, Py_hash_t);
        {
              Py_hash_t __pyx_hash = PyObject_Hash(__pyx_imported_names[__pyx_t_3]);
              if (unlikely(__pyx_hash == -1)) __PYX_ERR(0, 17, __pyx_L1_error);
          if (_PyDict_SetItem_KnownHash(__pyx_mstate_global->__pyx_d, __pyx_imported_names[__pyx_t_3], __pyx_t_4, __pyx_hash) < (0)) __PYX_ERR(0, 17, __pyx_L1_error)
        }
        #else
        if (PyDict_SetItem(__pyx_mstate_global->__pyx_d, __pyx_imported_names[__pyx_t_3], __pyx_t_4) < (0)) __PYX_ERR(0, 17, __pyx_L1_error)
        #endif
        break;
      }
      __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
    }
  }
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
```

</details>

L18  ⚪  (score=0)
```python
```
L19  🔴  (score=26)
```python
from .. import Utils
```
<details><summary>Show generated C (score=26)</summary>

```c
  {
    PyObject* const __pyx_imported_names[] = {__pyx_mstate_global->__pyx_n_u_Utils};
    __pyx_t_1 = __Pyx_Import(__pyx_mstate_global->__pyx_n_u__6, __pyx_imported_names, 1, __pyx_mstate_global->__pyx_kp_u_Cython, 2); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 19, __pyx_L1_error)
  }
  __pyx_t_2 = __pyx_t_1;
  __Pyx_GOTREF(__pyx_t_2);
  {
    PyObject* const __pyx_imported_names[] = {__pyx_mstate_global->__pyx_n_u_Utils};
    for (__pyx_t_3=0; __pyx_t_3 < 1; __pyx_t_3++) {
      __pyx_t_4 = __Pyx_ImportFrom(__pyx_t_2, __pyx_imported_names[__pyx_t_3]); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 19, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_4);
      switch (__pyx_t_3) {
        case 0:
        #if CYTHON_COMPILING_IN_CPYTHON && PY_VERSION_HEX >= 0x030A0000 && !CYTHON_COMPILING_IN_LIMITED_API
        extern int _PyDict_SetItem_KnownHash(PyObject*, PyObject*, PyObject*, Py_hash_t);
        {
              Py_hash_t __pyx_hash = PyObject_Hash(__pyx_imported_names[__pyx_t_3]);
              if (unlikely(__pyx_hash == -1)) __PYX_ERR(0, 19, __pyx_L1_error);
          if (_PyDict_SetItem_KnownHash(__pyx_mstate_global->__pyx_d, __pyx_imported_names[__pyx_t_3], __pyx_t_4, __pyx_hash) < (0)) __PYX_ERR(0, 19, __pyx_L1_error)
        }
        #else
        if (PyDict_SetItem(__pyx_mstate_global->__pyx_d, __pyx_imported_names[__pyx_t_3], __pyx_t_4) < (0)) __PYX_ERR(0, 19, __pyx_L1_error)
        #endif
        break;
      }
      __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
    }
  }
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
```

</details>

L20  🔴  (score=26)
```python
from ..Plex.Errors import UnrecognizedInput
```
<details><summary>Show generated C (score=26)</summary>

```c
  {
    PyObject* const __pyx_imported_names[] = {__pyx_mstate_global->__pyx_n_u_UnrecognizedInput};
    __pyx_t_1 = __Pyx_Import(__pyx_mstate_global->__pyx_n_u_Plex_Errors, __pyx_imported_names, 1, __pyx_mstate_global->__pyx_kp_u_Cython_Plex_Errors, 2); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 20, __pyx_L1_error)
  }
  __pyx_t_2 = __pyx_t_1;
  __Pyx_GOTREF(__pyx_t_2);
  {
    PyObject* const __pyx_imported_names[] = {__pyx_mstate_global->__pyx_n_u_UnrecognizedInput};
    for (__pyx_t_3=0; __pyx_t_3 < 1; __pyx_t_3++) {
      __pyx_t_4 = __Pyx_ImportFrom(__pyx_t_2, __pyx_imported_names[__pyx_t_3]); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 20, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_4);
      switch (__pyx_t_3) {
        case 0:
        #if CYTHON_COMPILING_IN_CPYTHON && PY_VERSION_HEX >= 0x030A0000 && !CYTHON_COMPILING_IN_LIMITED_API
        extern int _PyDict_SetItem_KnownHash(PyObject*, PyObject*, PyObject*, Py_hash_t);
        {
              Py_hash_t __pyx_hash = PyObject_Hash(__pyx_imported_names[__pyx_t_3]);
              if (unlikely(__pyx_hash == -1)) __PYX_ERR(0, 20, __pyx_L1_error);
          if (_PyDict_SetItem_KnownHash(__pyx_mstate_global->__pyx_d, __pyx_imported_names[__pyx_t_3], __pyx_t_4, __pyx_hash) < (0)) __PYX_ERR(0, 20, __pyx_L1_error)
        }
        #else
        if (PyDict_SetItem(__pyx_mstate_global->__pyx_d, __pyx_imported_names[__pyx_t_3], __pyx_t_4) < (0)) __PYX_ERR(0, 20, __pyx_L1_error)
        #endif
        break;
      }
      __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
    }
  }
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
```

</details>

L21  🔴  (score=26)
```python
from ..Plex.Scanners import Scanner
```
<details><summary>Show generated C (score=26)</summary>

```c
  {
    PyObject* const __pyx_imported_names[] = {__pyx_mstate_global->__pyx_n_u_Scanner};
    __pyx_t_1 = __Pyx_Import(__pyx_mstate_global->__pyx_n_u_Plex_Scanners, __pyx_imported_names, 1, __pyx_mstate_global->__pyx_kp_u_Cython_Plex_Scanners, 2); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 21, __pyx_L1_error)
  }
  __pyx_t_2 = __pyx_t_1;
  __Pyx_GOTREF(__pyx_t_2);
  {
    PyObject* const __pyx_imported_names[] = {__pyx_mstate_global->__pyx_n_u_Scanner};
    for (__pyx_t_3=0; __pyx_t_3 < 1; __pyx_t_3++) {
      __pyx_t_4 = __Pyx_ImportFrom(__pyx_t_2, __pyx_imported_names[__pyx_t_3]); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 21, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_4);
      switch (__pyx_t_3) {
        case 0:
        #if CYTHON_COMPILING_IN_CPYTHON && PY_VERSION_HEX >= 0x030A0000 && !CYTHON_COMPILING_IN_LIMITED_API
        extern int _PyDict_SetItem_KnownHash(PyObject*, PyObject*, PyObject*, Py_hash_t);
        {
              Py_hash_t __pyx_hash = PyObject_Hash(__pyx_imported_names[__pyx_t_3]);
              if (unlikely(__pyx_hash == -1)) __PYX_ERR(0, 21, __pyx_L1_error);
          if (_PyDict_SetItem_KnownHash(__pyx_mstate_global->__pyx_d, __pyx_imported_names[__pyx_t_3], __pyx_t_4, __pyx_hash) < (0)) __PYX_ERR(0, 21, __pyx_L1_error)
        }
        #else
        if (PyDict_SetItem(__pyx_mstate_global->__pyx_d, __pyx_imported_names[__pyx_t_3], __pyx_t_4) < (0)) __PYX_ERR(0, 21, __pyx_L1_error)
        #endif
        break;
      }
      __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
    }
  }
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
```

</details>

L22  🔴  (score=30)
```python
from .Errors import CompileError, error, hold_errors, release_errors, warning
```
<details><summary>Show generated C (score=30)</summary>

```c
  {
    PyObject* const __pyx_imported_names[] = {__pyx_mstate_global->__pyx_n_u_CompileError,__pyx_mstate_global->__pyx_n_u_error,__pyx_mstate_global->__pyx_n_u_hold_errors,__pyx_mstate_global->__pyx_n_u_release_errors,__pyx_mstate_global->__pyx_n_u_warning};
    __pyx_t_1 = __Pyx_Import(__pyx_mstate_global->__pyx_n_u_Errors, __pyx_imported_names, 5, __pyx_mstate_global->__pyx_kp_u_Cython_Compiler_Errors, 1); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 22, __pyx_L1_error)
  }
  __pyx_t_2 = __pyx_t_1;
  __Pyx_GOTREF(__pyx_t_2);
  {
    PyObject* const __pyx_imported_names[] = {__pyx_mstate_global->__pyx_n_u_CompileError,__pyx_mstate_global->__pyx_n_u_error,__pyx_mstate_global->__pyx_n_u_hold_errors,__pyx_mstate_global->__pyx_n_u_release_errors,__pyx_mstate_global->__pyx_n_u_warning};
    for (__pyx_t_3=0; __pyx_t_3 < 5; __pyx_t_3++) {
      __pyx_t_4 = __Pyx_ImportFrom(__pyx_t_2, __pyx_imported_names[__pyx_t_3]); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 22, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_4);
      switch (__pyx_t_3) {
        case 0: case 2: case 3:
        #if CYTHON_COMPILING_IN_CPYTHON && PY_VERSION_HEX >= 0x030A0000 && !CYTHON_COMPILING_IN_LIMITED_API
        extern int _PyDict_SetItem_KnownHash(PyObject*, PyObject*, PyObject*, Py_hash_t);
        {
              Py_hash_t __pyx_hash = PyObject_Hash(__pyx_imported_names[__pyx_t_3]);
              if (unlikely(__pyx_hash == -1)) __PYX_ERR(0, 22, __pyx_L1_error);
          if (_PyDict_SetItem_KnownHash(__pyx_mstate_global->__pyx_d, __pyx_imported_names[__pyx_t_3], __pyx_t_4, __pyx_hash) < (0)) __PYX_ERR(0, 22, __pyx_L1_error)
        }
        #else
        if (PyDict_SetItem(__pyx_mstate_global->__pyx_d, __pyx_imported_names[__pyx_t_3], __pyx_t_4) < (0)) __PYX_ERR(0, 22, __pyx_L1_error)
        #endif
        break;
        case 1:
        __Pyx_INCREF(__pyx_t_4);
        __Pyx_XGOTREF(__pyx_v_6Cython_8Compiler_8Scanning_error);
        __Pyx_DECREF_SET(__pyx_v_6Cython_8Compiler_8Scanning_error, __pyx_t_4);
        __Pyx_GIVEREF(__pyx_t_4);
        break;
        case 4:
        __Pyx_INCREF(__pyx_t_4);
        __Pyx_XGOTREF(__pyx_v_6Cython_8Compiler_8Scanning_warning);
        __Pyx_DECREF_SET(__pyx_v_6Cython_8Compiler_8Scanning_warning, __pyx_t_4);
        __Pyx_GIVEREF(__pyx_t_4);
        break;
      }
      __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
    }
  }
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
```

</details>

L23  🟠  (score=8)
```python
from .Future import print_function
```
<details><summary>Show generated C (score=8)</summary>

```c
  {
    PyObject* const __pyx_imported_names[] = {__pyx_mstate_global->__pyx_n_u_print_function};
    __pyx_t_1 = __Pyx_Import(__pyx_mstate_global->__pyx_n_u_Future, __pyx_imported_names, 1, __pyx_mstate_global->__pyx_kp_u_Cython_Compiler_Future, 1); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 23, __pyx_L1_error)
  }
  __pyx_t_2 = __pyx_t_1;
  __Pyx_GOTREF(__pyx_t_2);
  {
    PyObject* const __pyx_imported_names[] = {__pyx_mstate_global->__pyx_n_u_print_function};
    for (__pyx_t_3=0; __pyx_t_3 < 1; __pyx_t_3++) {
      __pyx_t_4 = __Pyx_ImportFrom(__pyx_t_2, __pyx_imported_names[__pyx_t_3]); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 23, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_4);
      switch (__pyx_t_3) {
        case 0:
        __Pyx_INCREF(__pyx_t_4);
        __Pyx_XGOTREF(__pyx_v_6Cython_8Compiler_8Scanning_print_function);
        __Pyx_DECREF_SET(__pyx_v_6Cython_8Compiler_8Scanning_print_function, __pyx_t_4);
        __Pyx_GIVEREF(__pyx_t_4);
        break;
      }
      __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
    }
  }
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
```

</details>

L24  🔴  (score=28)
```python
from .Lexicon import IDENT, any_string_prefix, ft_string_prefixes, make_lexicon
```
<details><summary>Show generated C (score=28)</summary>

```c
  {
    PyObject* const __pyx_imported_names[] = {__pyx_mstate_global->__pyx_n_u_IDENT,__pyx_mstate_global->__pyx_n_u_any_string_prefix,__pyx_mstate_global->__pyx_n_u_ft_string_prefixes,__pyx_mstate_global->__pyx_n_u_make_lexicon};
    __pyx_t_1 = __Pyx_Import(__pyx_mstate_global->__pyx_n_u_Lexicon, __pyx_imported_names, 4, __pyx_mstate_global->__pyx_kp_u_Cython_Compiler_Lexicon, 1); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 24, __pyx_L1_error)
  }
  __pyx_t_2 = __pyx_t_1;
  __Pyx_GOTREF(__pyx_t_2);
  {
    PyObject* const __pyx_imported_names[] = {__pyx_mstate_global->__pyx_n_u_IDENT,__pyx_mstate_global->__pyx_n_u_any_string_prefix,__pyx_mstate_global->__pyx_n_u_ft_string_prefixes,__pyx_mstate_global->__pyx_n_u_make_lexicon};
    for (__pyx_t_3=0; __pyx_t_3 < 4; __pyx_t_3++) {
      __pyx_t_4 = __Pyx_ImportFrom(__pyx_t_2, __pyx_imported_names[__pyx_t_3]); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 24, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_4);
      switch (__pyx_t_3) {
        case 0: case 1: case 2:
        #if CYTHON_COMPILING_IN_CPYTHON && PY_VERSION_HEX >= 0x030A0000 && !CYTHON_COMPILING_IN_LIMITED_API
        extern int _PyDict_SetItem_KnownHash(PyObject*, PyObject*, PyObject*, Py_hash_t);
        {
              Py_hash_t __pyx_hash = PyObject_Hash(__pyx_imported_names[__pyx_t_3]);
              if (unlikely(__pyx_hash == -1)) __PYX_ERR(0, 24, __pyx_L1_error);
          if (_PyDict_SetItem_KnownHash(__pyx_mstate_global->__pyx_d, __pyx_imported_names[__pyx_t_3], __pyx_t_4, __pyx_hash) < (0)) __PYX_ERR(0, 24, __pyx_L1_error)
        }
        #else
        if (PyDict_SetItem(__pyx_mstate_global->__pyx_d, __pyx_imported_names[__pyx_t_3], __pyx_t_4) < (0)) __PYX_ERR(0, 24, __pyx_L1_error)
        #endif
        break;
        case 3:
        __Pyx_INCREF(__pyx_t_4);
        __Pyx_XGOTREF(__pyx_v_6Cython_8Compiler_8Scanning_make_lexicon);
        __Pyx_DECREF_SET(__pyx_v_6Cython_8Compiler_8Scanning_make_lexicon, __pyx_t_4);
        __Pyx_GIVEREF(__pyx_t_4);
        break;
      }
      __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
    }
  }
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
```

</details>

L25  ⚪  (score=0)
```python
```
L26  🟠  (score=5)
```python
if TYPE_CHECKING:
```
<details><summary>Show generated C (score=5)</summary>

```c
  __Pyx_GetModuleGlobalName(__pyx_t_2, __pyx_mstate_global->__pyx_n_u_TYPE_CHECKING); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 26, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __pyx_t_5 = __Pyx_PyObject_IsTrue(__pyx_t_2); if (unlikely((__pyx_t_5 < 0))) __PYX_ERR(0, 26, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  if (__pyx_t_5) {
/* … */
    goto __pyx_L2;
  }
```

</details>

L27  🔴  (score=26)
```python
    from Cython.Build import CompilationContext
```
<details><summary>Show generated C (score=26)</summary>

```c
    {
      PyObject* const __pyx_imported_names[] = {__pyx_mstate_global->__pyx_n_u_CompilationContext};
      __pyx_t_1 = __Pyx_Import(__pyx_mstate_global->__pyx_n_u_Cython_Build, __pyx_imported_names, 1, NULL, 0); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 27, __pyx_L1_error)
    }
    __pyx_t_2 = __pyx_t_1;
    __Pyx_GOTREF(__pyx_t_2);
    {
      PyObject* const __pyx_imported_names[] = {__pyx_mstate_global->__pyx_n_u_CompilationContext};
      for (__pyx_t_3=0; __pyx_t_3 < 1; __pyx_t_3++) {
        __pyx_t_4 = __Pyx_ImportFrom(__pyx_t_2, __pyx_imported_names[__pyx_t_3]); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 27, __pyx_L1_error)
        __Pyx_GOTREF(__pyx_t_4);
        switch (__pyx_t_3) {
          case 0:
          #if CYTHON_COMPILING_IN_CPYTHON && PY_VERSION_HEX >= 0x030A0000 && !CYTHON_COMPILING_IN_LIMITED_API
          extern int _PyDict_SetItem_KnownHash(PyObject*, PyObject*, PyObject*, Py_hash_t);
          {
                Py_hash_t __pyx_hash = PyObject_Hash(__pyx_imported_names[__pyx_t_3]);
                if (unlikely(__pyx_hash == -1)) __PYX_ERR(0, 27, __pyx_L1_error);
            if (_PyDict_SetItem_KnownHash(__pyx_mstate_global->__pyx_d, __pyx_imported_names[__pyx_t_3], __pyx_t_4, __pyx_hash) < (0)) __PYX_ERR(0, 27, __pyx_L1_error)
          }
          #else
          if (PyDict_SetItem(__pyx_mstate_global->__pyx_d, __pyx_imported_names[__pyx_t_3], __pyx_t_4) < (0)) __PYX_ERR(0, 27, __pyx_L1_error)
          #endif
          break;
        }
        __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
      }
    }
    __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
```

</details>

L28  ⚪  (score=0)
```python
```
L29  🔴  (score=26)
```python
    from .Nodes import SourceDescriptor
```
<details><summary>Show generated C (score=26)</summary>

```c
    {
      PyObject* const __pyx_imported_names[] = {__pyx_mstate_global->__pyx_n_u_SourceDescriptor};
      __pyx_t_1 = __Pyx_Import(__pyx_mstate_global->__pyx_n_u_Nodes, __pyx_imported_names, 1, __pyx_mstate_global->__pyx_kp_u_Cython_Compiler_Nodes, 1); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 29, __pyx_L1_error)
    }
    __pyx_t_2 = __pyx_t_1;
    __Pyx_GOTREF(__pyx_t_2);
    {
      PyObject* const __pyx_imported_names[] = {__pyx_mstate_global->__pyx_n_u_SourceDescriptor};
      for (__pyx_t_3=0; __pyx_t_3 < 1; __pyx_t_3++) {
        __pyx_t_4 = __Pyx_ImportFrom(__pyx_t_2, __pyx_imported_names[__pyx_t_3]); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 29, __pyx_L1_error)
        __Pyx_GOTREF(__pyx_t_4);
        switch (__pyx_t_3) {
          case 0:
          #if CYTHON_COMPILING_IN_CPYTHON && PY_VERSION_HEX >= 0x030A0000 && !CYTHON_COMPILING_IN_LIMITED_API
          extern int _PyDict_SetItem_KnownHash(PyObject*, PyObject*, PyObject*, Py_hash_t);
          {
                Py_hash_t __pyx_hash = PyObject_Hash(__pyx_imported_names[__pyx_t_3]);
                if (unlikely(__pyx_hash == -1)) __PYX_ERR(0, 29, __pyx_L1_error);
            if (_PyDict_SetItem_KnownHash(__pyx_mstate_global->__pyx_d, __pyx_imported_names[__pyx_t_3], __pyx_t_4, __pyx_hash) < (0)) __PYX_ERR(0, 29, __pyx_L1_error)
          }
          #else
          if (PyDict_SetItem(__pyx_mstate_global->__pyx_d, __pyx_imported_names[__pyx_t_3], __pyx_t_4) < (0)) __PYX_ERR(0, 29, __pyx_L1_error)
          #endif
          break;
        }
        __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
      }
    }
    __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
```

</details>

L30  🔴  (score=26)
```python
    from .Symtab import Scope
```
<details><summary>Show generated C (score=26)</summary>

```c
    {
      PyObject* const __pyx_imported_names[] = {__pyx_mstate_global->__pyx_n_u_Scope};
      __pyx_t_1 = __Pyx_Import(__pyx_mstate_global->__pyx_n_u_Symtab, __pyx_imported_names, 1, __pyx_mstate_global->__pyx_kp_u_Cython_Compiler_Symtab, 1); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 30, __pyx_L1_error)
    }
    __pyx_t_2 = __pyx_t_1;
    __Pyx_GOTREF(__pyx_t_2);
    {
      PyObject* const __pyx_imported_names[] = {__pyx_mstate_global->__pyx_n_u_Scope};
      for (__pyx_t_3=0; __pyx_t_3 < 1; __pyx_t_3++) {
        __pyx_t_4 = __Pyx_ImportFrom(__pyx_t_2, __pyx_imported_names[__pyx_t_3]); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 30, __pyx_L1_error)
        __Pyx_GOTREF(__pyx_t_4);
        switch (__pyx_t_3) {
          case 0:
          #if CYTHON_COMPILING_IN_CPYTHON && PY_VERSION_HEX >= 0x030A0000 && !CYTHON_COMPILING_IN_LIMITED_API
          extern int _PyDict_SetItem_KnownHash(PyObject*, PyObject*, PyObject*, Py_hash_t);
          {
                Py_hash_t __pyx_hash = PyObject_Hash(__pyx_imported_names[__pyx_t_3]);
                if (unlikely(__pyx_hash == -1)) __PYX_ERR(0, 30, __pyx_L1_error);
            if (_PyDict_SetItem_KnownHash(__pyx_mstate_global->__pyx_d, __pyx_imported_names[__pyx_t_3], __pyx_t_4, __pyx_hash) < (0)) __PYX_ERR(0, 30, __pyx_L1_error)
          }
          #else
          if (PyDict_SetItem(__pyx_mstate_global->__pyx_d, __pyx_imported_names[__pyx_t_3], __pyx_t_4) < (0)) __PYX_ERR(0, 30, __pyx_L1_error)
          #endif
          break;
        }
        __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
      }
    }
    __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
```

</details>

L31  ⚪  (score=0)
```python
else:
```
L32  🟠  (score=5)
```python
    CompilationContext = object
```
<details><summary>Show generated C (score=5)</summary>

```c
  /*else*/ {
    if (PyDict_SetItem(__pyx_mstate_global->__pyx_d, __pyx_mstate_global->__pyx_n_u_CompilationContext, __pyx_builtin_object) < (0)) __PYX_ERR(0, 32, __pyx_L1_error)
```

</details>

L33  🟠  (score=5)
```python
    SourceDescriptor = object
```
<details><summary>Show generated C (score=5)</summary>

```c
    if (PyDict_SetItem(__pyx_mstate_global->__pyx_d, __pyx_mstate_global->__pyx_n_u_SourceDescriptor, __pyx_builtin_object) < (0)) __PYX_ERR(0, 33, __pyx_L1_error)
```

</details>

L34  🟠  (score=5)
```python
    Scope = object
```
<details><summary>Show generated C (score=5)</summary>

```c
    if (PyDict_SetItem(__pyx_mstate_global->__pyx_d, __pyx_mstate_global->__pyx_n_u_Scope, __pyx_builtin_object) < (0)) __PYX_ERR(0, 34, __pyx_L1_error)
```

</details>

L35  🟠  (score=5)
```python
    FileSourceDescriptor = object
```
<details><summary>Show generated C (score=5)</summary>

```c
    if (PyDict_SetItem(__pyx_mstate_global->__pyx_d, __pyx_mstate_global->__pyx_n_u_FileSourceDescriptor, __pyx_builtin_object) < (0)) __PYX_ERR(0, 35, __pyx_L1_error)
```

</details>

L36  🟠  (score=5)
```python
    StringSourceDescriptor = object
```
<details><summary>Show generated C (score=5)</summary>

```c
    if (PyDict_SetItem(__pyx_mstate_global->__pyx_d, __pyx_mstate_global->__pyx_n_u_StringSourceDescriptor, __pyx_builtin_object) < (0)) __PYX_ERR(0, 36, __pyx_L1_error)
  }
  __pyx_L2:;
```

</details>

L37  🟠  (score=5)
```python
debug_scanner = 0
```
<details><summary>Show generated C (score=5)</summary>

```c
  if (PyDict_SetItem(__pyx_mstate_global->__pyx_d, __pyx_mstate_global->__pyx_n_u_debug_scanner, __pyx_mstate_global->__pyx_int_0) < (0)) __PYX_ERR(0, 37, __pyx_L1_error)
```

</details>

L38  🟠  (score=5)
```python
trace_scanner = 0
```
<details><summary>Show generated C (score=5)</summary>

```c
  if (PyDict_SetItem(__pyx_mstate_global->__pyx_d, __pyx_mstate_global->__pyx_n_u_trace_scanner, __pyx_mstate_global->__pyx_int_0) < (0)) __PYX_ERR(0, 38, __pyx_L1_error)
```

</details>

L39  🟠  (score=5)
```python
scanner_debug_flags = 0
```
<details><summary>Show generated C (score=5)</summary>

```c
  if (PyDict_SetItem(__pyx_mstate_global->__pyx_d, __pyx_mstate_global->__pyx_n_u_scanner_debug_flags, __pyx_mstate_global->__pyx_int_0) < (0)) __PYX_ERR(0, 39, __pyx_L1_error)
```

</details>

L40  🟠  (score=5)
```python
scanner_dump_file = None
```
<details><summary>Show generated C (score=5)</summary>

```c
  if (PyDict_SetItem(__pyx_mstate_global->__pyx_d, __pyx_mstate_global->__pyx_n_u_scanner_dump_file, Py_None) < (0)) __PYX_ERR(0, 40, __pyx_L1_error)
```

</details>

L41  ⚪  (score=0)
```python
```
L42  🟡  (score=2)
```python
lexicon = None
```
<details><summary>Show generated C (score=2)</summary>

```c
  __Pyx_INCREF(Py_None);
  __Pyx_XGOTREF(__pyx_v_6Cython_8Compiler_8Scanning_lexicon);
  __Pyx_DECREF_SET(__pyx_v_6Cython_8Compiler_8Scanning_lexicon, Py_None);
  __Pyx_GIVEREF(Py_None);
```

</details>

L43  ⚪  (score=0)
```python
```
L44  ⚪  (score=0)
```python
```
L45  🔴  (score=21)
```python
def get_lexicon():
```
<details><summary>Show generated C (score=21)</summary>

```c
/* Python wrapper */
static PyObject *__pyx_pw_6Cython_8Compiler_8Scanning_1get_lexicon(PyObject *__pyx_self, CYTHON_UNUSED PyObject *unused); /*proto*/
PyDoc_STRVAR(__pyx_doc_6Cython_8Compiler_8Scanning_get_lexicon, "File: Cython/Compiler/Scanning.py (starting at line 45)");
static PyMethodDef __pyx_mdef_6Cython_8Compiler_8Scanning_1get_lexicon = {"get_lexicon", (PyCFunction)__pyx_pw_6Cython_8Compiler_8Scanning_1get_lexicon, METH_NOARGS, __pyx_doc_6Cython_8Compiler_8Scanning_get_lexicon};
static PyObject *__pyx_pw_6Cython_8Compiler_8Scanning_1get_lexicon(PyObject *__pyx_self, CYTHON_UNUSED PyObject *unused) {
  CYTHON_UNUSED PyObject *const *__pyx_kwvalues;
  PyObject *__pyx_r = 0;
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("get_lexicon (wrapper)", 0);
  __pyx_kwvalues = __Pyx_KwValues_VARARGS(__pyx_args, __pyx_nargs);
  __pyx_r = __pyx_pf_6Cython_8Compiler_8Scanning_get_lexicon(__pyx_self);

  /* function exit code */
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}

static PyObject *__pyx_pf_6Cython_8Compiler_8Scanning_get_lexicon(CYTHON_UNUSED PyObject *__pyx_self) {
  PyObject *__pyx_r = NULL;
/* … */
  /* function exit code */
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_t_3);
  __Pyx_XDECREF(__pyx_t_4);
  __Pyx_XDECREF(__pyx_t_5);
  __Pyx_AddTraceback("Cython.Compiler.Scanning.get_lexicon", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_r = NULL;
  __pyx_L0:;
  __Pyx_XGIVEREF(__pyx_r);
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}
/* … */
  __pyx_t_2 = __Pyx_CyFunction_New(&__pyx_mdef_6Cython_8Compiler_8Scanning_1get_lexicon, 0, __pyx_mstate_global->__pyx_n_u_get_lexicon, NULL, __pyx_mstate_global->__pyx_n_u_Cython_Compiler_Scanning, __pyx_mstate_global->__pyx_d, ((PyObject *)__pyx_mstate_global->__pyx_codeobj_tab[1])); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 45, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  #if CYTHON_COMPILING_IN_CPYTHON && PY_VERSION_HEX >= 0x030E0000
  PyUnstable_Object_EnableDeferredRefcount(__pyx_t_2);
  #endif
  if (PyDict_SetItem(__pyx_mstate_global->__pyx_d, __pyx_mstate_global->__pyx_n_u_get_lexicon, __pyx_t_2) < (0)) __PYX_ERR(0, 45, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
```

</details>

L46  ⚪  (score=0)
```python
    global lexicon
```
L47  🟡  (score=2)
```python
    if not lexicon:
```
<details><summary>Show generated C (score=2)</summary>

```c
  __pyx_t_1 = __Pyx_PyObject_IsTrue(__pyx_v_6Cython_8Compiler_8Scanning_lexicon); if (unlikely((__pyx_t_1 < 0))) __PYX_ERR(0, 47, __pyx_L1_error)
  __pyx_t_2 = (!__pyx_t_1);
  if (__pyx_t_2) {
/* … */
  }
```

</details>

L48  🟠  (score=6)
```python
        lexicon = make_lexicon()
```
<details><summary>Show generated C (score=6)</summary>

```c
    __pyx_t_4 = NULL;
    __Pyx_INCREF(__pyx_v_6Cython_8Compiler_8Scanning_make_lexicon);
    __pyx_t_5 = __pyx_v_6Cython_8Compiler_8Scanning_make_lexicon; 
    __pyx_t_6 = 1;
    {
      PyObject *__pyx_callargs[2] = {__pyx_t_4, NULL};
      __pyx_t_3 = __Pyx_PyObject_FastCall((PyObject*)__pyx_t_5, __pyx_callargs+__pyx_t_6, (1-__pyx_t_6) | (__pyx_t_6*__Pyx_PY_VECTORCALL_ARGUMENTS_OFFSET));
      __Pyx_XDECREF(__pyx_t_4); __pyx_t_4 = 0;
      __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
      if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 48, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_3);
    }
    __Pyx_XGOTREF(__pyx_v_6Cython_8Compiler_8Scanning_lexicon);
    __Pyx_DECREF_SET(__pyx_v_6Cython_8Compiler_8Scanning_lexicon, __pyx_t_3);
    __Pyx_GIVEREF(__pyx_t_3);
    __pyx_t_3 = 0;
```

</details>

L49  🟡  (score=2)
```python
    return lexicon
```
<details><summary>Show generated C (score=2)</summary>

```c
  __Pyx_XDECREF(__pyx_r);
  __Pyx_INCREF(__pyx_v_6Cython_8Compiler_8Scanning_lexicon);
  __pyx_r = __pyx_v_6Cython_8Compiler_8Scanning_lexicon;
  goto __pyx_L0;
```

</details>

L50  ⚪  (score=0)
```python
```
L51  ⚪  (score=0)
```python
```
L52  ⚪  (score=0)
```python
#------------------------------------------------------------------
```
L53  ⚪  (score=0)
```python
```
L54  🟠  (score=8)
```python
py_reserved_words = [
```
<details><summary>Show generated C (score=8)</summary>

```c
  __pyx_t_2 = __Pyx_PyList_Pack(31, __pyx_mstate_global->__pyx_n_u_global, __pyx_mstate_global->__pyx_n_u_nonlocal, __pyx_mstate_global->__pyx_n_u_def, __pyx_mstate_global->__pyx_n_u_class, __pyx_mstate_global->__pyx_n_u_print, __pyx_mstate_global->__pyx_n_u_del, __pyx_mstate_global->__pyx_n_u_pass, __pyx_mstate_global->__pyx_n_u_break, __pyx_mstate_global->__pyx_n_u_continue, __pyx_mstate_global->__pyx_n_u_return, __pyx_mstate_global->__pyx_n_u_raise, __pyx_mstate_global->__pyx_n_u_import, __pyx_mstate_global->__pyx_n_u_exec, __pyx_mstate_global->__pyx_n_u_try, __pyx_mstate_global->__pyx_n_u_except, __pyx_mstate_global->__pyx_n_u_finally, __pyx_mstate_global->__pyx_n_u_while, __pyx_mstate_global->__pyx_n_u_if, __pyx_mstate_global->__pyx_n_u_elif, __pyx_mstate_global->__pyx_n_u_else, __pyx_mstate_global->__pyx_n_u_for, __pyx_mstate_global->__pyx_n_u_in, __pyx_mstate_global->__pyx_n_u_assert, __pyx_mstate_global->__pyx_n_u_and, __pyx_mstate_global->__pyx_n_u_or, __pyx_mstate_global->__pyx_n_u_not, __pyx_mstate_global->__pyx_n_u_is, __pyx_mstate_global->__pyx_n_u_lambda, __pyx_mstate_global->__pyx_n_u_from, __pyx_mstate_global->__pyx_n_u_yield, __pyx_mstate_global->__pyx_n_u_with); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 54, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  if (PyDict_SetItem(__pyx_mstate_global->__pyx_d, __pyx_mstate_global->__pyx_n_u_py_reserved_words, __pyx_t_2) < (0)) __PYX_ERR(0, 54, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
```

</details>

L55  ⚪  (score=0)
```python
    "global", "nonlocal", "def", "class", "print", "del", "pass", "break",
```
L56  ⚪  (score=0)
```python
    "continue", "return", "raise", "import", "exec", "try",
```
L57  ⚪  (score=0)
```python
    "except", "finally", "while", "if", "elif", "else", "for",
```
L58  ⚪  (score=0)
```python
    "in", "assert", "and", "or", "not", "is", "lambda",
```
L59  ⚪  (score=0)
```python
    "from", "yield", "with",
```
L60  ⚪  (score=0)
```python
]
```
L61  ⚪  (score=0)
```python
```
L62  🔴  (score=17)
```python
pyx_reserved_words = py_reserved_words + [
```
<details><summary>Show generated C (score=17)</summary>

```c
  __Pyx_GetModuleGlobalName(__pyx_t_2, __pyx_mstate_global->__pyx_n_u_py_reserved_words); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 62, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __pyx_t_4 = __Pyx_PyList_Pack(9, __pyx_mstate_global->__pyx_n_u_include, __pyx_mstate_global->__pyx_n_u_ctypedef, __pyx_mstate_global->__pyx_n_u_cdef, __pyx_mstate_global->__pyx_n_u_cpdef, __pyx_mstate_global->__pyx_n_u_cimport, __pyx_mstate_global->__pyx_n_u_DEF, __pyx_mstate_global->__pyx_n_u_IF, __pyx_mstate_global->__pyx_n_u_ELIF, __pyx_mstate_global->__pyx_n_u_ELSE); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 62, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_4);
  __pyx_t_6 = PyNumber_Add(__pyx_t_2, __pyx_t_4); if (unlikely(!__pyx_t_6)) __PYX_ERR(0, 62, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_6);
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
  if (PyDict_SetItem(__pyx_mstate_global->__pyx_d, __pyx_mstate_global->__pyx_n_u_pyx_reserved_words, __pyx_t_6) < (0)) __PYX_ERR(0, 62, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_6); __pyx_t_6 = 0;
```

</details>

L63  ⚪  (score=0)
```python
    "include", "ctypedef", "cdef", "cpdef",
```
L64  ⚪  (score=0)
```python
    "cimport", "DEF", "IF", "ELIF", "ELSE"
```
L65  ⚪  (score=0)
```python
]
```
L66  ⚪  (score=0)
```python
```
L67  ⚪  (score=0)
```python
```
L68  ⚪  (score=0)
```python
#------------------------------------------------------------------
```
L69  ⚪  (score=0)
```python
```
L70  🔴  (score=12)
```python
class CompileTimeScope:
```
<details><summary>Show generated C (score=12)</summary>

```c
  __pyx_t_6 = __Pyx_Py3MetaclassPrepare((PyObject *) NULL, __pyx_mstate_global->__pyx_empty_tuple, __pyx_mstate_global->__pyx_n_u_CompileTimeScope, __pyx_mstate_global->__pyx_n_u_CompileTimeScope, (PyObject *) NULL, __pyx_mstate_global->__pyx_n_u_Cython_Compiler_Scanning, (PyObject *) NULL); if (unlikely(!__pyx_t_6)) __PYX_ERR(0, 70, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_6);
/* … */
  __pyx_t_4 = __Pyx_Py3ClassCreate(((PyObject*)&PyType_Type), __pyx_mstate_global->__pyx_n_u_CompileTimeScope, __pyx_mstate_global->__pyx_empty_tuple, __pyx_t_6, NULL, 0, 0); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 70, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_4);
  #if CYTHON_COMPILING_IN_CPYTHON && PY_VERSION_HEX >= 0x030E0000
  PyUnstable_Object_EnableDeferredRefcount(__pyx_t_4);
  #endif
  if (PyDict_SetItem(__pyx_mstate_global->__pyx_d, __pyx_mstate_global->__pyx_n_u_CompileTimeScope, __pyx_t_4) < (0)) __PYX_ERR(0, 70, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
  __Pyx_DECREF(__pyx_t_6); __pyx_t_6 = 0;
```

</details>

L71  ⚪  (score=0)
```python
```
L72  🔴  (score=52)
```python
    def __init__(self, outer=None):
```
<details><summary>Show generated C (score=52)</summary>

```c
/* Python wrapper */
static PyObject *__pyx_pw_6Cython_8Compiler_8Scanning_16CompileTimeScope_1__init__(PyObject *__pyx_self, 
#if CYTHON_METH_FASTCALL
PyObject *const *__pyx_args, Py_ssize_t __pyx_nargs, PyObject *__pyx_kwds
#else
PyObject *__pyx_args, PyObject *__pyx_kwds
#endif
); /*proto*/
PyDoc_STRVAR(__pyx_doc_6Cython_8Compiler_8Scanning_16CompileTimeScope___init__, "File: Cython/Compiler/Scanning.py (starting at line 72)");
static PyMethodDef __pyx_mdef_6Cython_8Compiler_8Scanning_16CompileTimeScope_1__init__ = {"__init__", (PyCFunction)(void(*)(void))(__Pyx_PyCFunction_FastCallWithKeywords)__pyx_pw_6Cython_8Compiler_8Scanning_16CompileTimeScope_1__init__, __Pyx_METH_FASTCALL|METH_KEYWORDS, __pyx_doc_6Cython_8Compiler_8Scanning_16CompileTimeScope___init__};
static PyObject *__pyx_pw_6Cython_8Compiler_8Scanning_16CompileTimeScope_1__init__(PyObject *__pyx_self, 
#if CYTHON_METH_FASTCALL
PyObject *const *__pyx_args, Py_ssize_t __pyx_nargs, PyObject *__pyx_kwds
#else
PyObject *__pyx_args, PyObject *__pyx_kwds
#endif
) {
  PyObject *__pyx_v_self = 0;
  PyObject *__pyx_v_outer = 0;
  #if !CYTHON_METH_FASTCALL
  CYTHON_UNUSED Py_ssize_t __pyx_nargs;
  #endif
  CYTHON_UNUSED PyObject *const *__pyx_kwvalues;
  PyObject *__pyx_r = 0;
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("__init__ (wrapper)", 0);
  #if !CYTHON_METH_FASTCALL
  #if CYTHON_ASSUME_SAFE_SIZE
  __pyx_nargs = PyTuple_GET_SIZE(__pyx_args);
  #else
  __pyx_nargs = PyTuple_Size(__pyx_args); if (unlikely(__pyx_nargs < 0)) return NULL;
  #endif
  #endif
  __pyx_kwvalues = __Pyx_KwValues_FASTCALL(__pyx_args, __pyx_nargs);
  {
    PyObject ** const __pyx_pyargnames[] = {&__pyx_mstate_global->__pyx_n_u_self,&__pyx_mstate_global->__pyx_n_u_outer,0};
  PyObject* values[2] = {0,0};
    const Py_ssize_t __pyx_kwds_len = (__pyx_kwds) ? __Pyx_NumKwargs_FASTCALL(__pyx_kwds) : 0;
    if (unlikely(__pyx_kwds_len) < 0) __PYX_ERR(0, 72, __pyx_L3_error)
    if (__pyx_kwds_len > 0) {
      switch (__pyx_nargs) {
        case  2:
        values[1] = __Pyx_ArgRef_FASTCALL(__pyx_args, 1);
        if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[1])) __PYX_ERR(0, 72, __pyx_L3_error)
        CYTHON_FALLTHROUGH;
        case  1:
        values[0] = __Pyx_ArgRef_FASTCALL(__pyx_args, 0);
        if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[0])) __PYX_ERR(0, 72, __pyx_L3_error)
        CYTHON_FALLTHROUGH;
        case  0: break;
        default: goto __pyx_L5_argtuple_error;
      }
      const Py_ssize_t kwd_pos_args = __pyx_nargs;
      if (__Pyx_ParseKeywords(__pyx_kwds, __pyx_kwvalues, __pyx_pyargnames, 0, values, kwd_pos_args, __pyx_kwds_len, "__init__", 0) < (0)) __PYX_ERR(0, 72, __pyx_L3_error)
      if (!values[1]) values[1] = __Pyx_NewRef(((PyObject *)Py_None));
      for (Py_ssize_t i = __pyx_nargs; i < 1; i++) {
        if (unlikely(!values[i])) { __Pyx_RaiseArgtupleInvalid("__init__", 0, 1, 2, i); __PYX_ERR(0, 72, __pyx_L3_error) }
      }
    } else {
      switch (__pyx_nargs) {
        case  2:
        values[1] = __Pyx_ArgRef_FASTCALL(__pyx_args, 1);
        if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[1])) __PYX_ERR(0, 72, __pyx_L3_error)
        CYTHON_FALLTHROUGH;
        case  1:
        values[0] = __Pyx_ArgRef_FASTCALL(__pyx_args, 0);
        if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[0])) __PYX_ERR(0, 72, __pyx_L3_error)
        break;
        default: goto __pyx_L5_argtuple_error;
      }
      if (!values[1]) values[1] = __Pyx_NewRef(((PyObject *)Py_None));
    }
    __pyx_v_self = values[0];
    __pyx_v_outer = values[1];
  }
  goto __pyx_L6_skip;
  __pyx_L5_argtuple_error:;
  __Pyx_RaiseArgtupleInvalid("__init__", 0, 1, 2, __pyx_nargs); __PYX_ERR(0, 72, __pyx_L3_error)
  __pyx_L6_skip:;
  goto __pyx_L4_argument_unpacking_done;
  __pyx_L3_error:;
  for (Py_ssize_t __pyx_temp=0; __pyx_temp < (Py_ssize_t)(sizeof(values)/sizeof(values[0])); ++__pyx_temp) {
    Py_XDECREF(values[__pyx_temp]);
  }
  __Pyx_AddTraceback("Cython.Compiler.Scanning.CompileTimeScope.__init__", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __Pyx_RefNannyFinishContext();
  return NULL;
  __pyx_L4_argument_unpacking_done:;
  __pyx_r = __pyx_pf_6Cython_8Compiler_8Scanning_16CompileTimeScope___init__(__pyx_self, __pyx_v_self, __pyx_v_outer);

  /* function exit code */
  for (Py_ssize_t __pyx_temp=0; __pyx_temp < (Py_ssize_t)(sizeof(values)/sizeof(values[0])); ++__pyx_temp) {
    Py_XDECREF(values[__pyx_temp]);
  }
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}

static PyObject *__pyx_pf_6Cython_8Compiler_8Scanning_16CompileTimeScope___init__(CYTHON_UNUSED PyObject *__pyx_self, PyObject *__pyx_v_self, PyObject *__pyx_v_outer) {
  PyObject *__pyx_r = NULL;
/* … */
  /* function exit code */
  __pyx_r = Py_None; __Pyx_INCREF(Py_None);
  goto __pyx_L0;
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_t_1);
  __Pyx_AddTraceback("Cython.Compiler.Scanning.CompileTimeScope.__init__", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_r = NULL;
  __pyx_L0:;
  __Pyx_XGIVEREF(__pyx_r);
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}
/* … */
  __pyx_t_4 = __Pyx_CyFunction_New(&__pyx_mdef_6Cython_8Compiler_8Scanning_16CompileTimeScope_1__init__, 0, __pyx_mstate_global->__pyx_n_u_CompileTimeScope___init, NULL, __pyx_mstate_global->__pyx_n_u_Cython_Compiler_Scanning, __pyx_mstate_global->__pyx_d, ((PyObject *)__pyx_mstate_global->__pyx_codeobj_tab[2])); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 72, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_4);
  #if CYTHON_COMPILING_IN_CPYTHON && PY_VERSION_HEX >= 0x030E0000
  PyUnstable_Object_EnableDeferredRefcount(__pyx_t_4);
  #endif
  __Pyx_CyFunction_SetDefaultsTuple(__pyx_t_4, __pyx_mstate_global->__pyx_tuple[16]);
  if (__Pyx_SetNameInClass(__pyx_t_6, __pyx_mstate_global->__pyx_n_u_init, __pyx_t_4) < (0)) __PYX_ERR(0, 72, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
/* … */
  __pyx_mstate_global->__pyx_tuple[16] = PyTuple_Pack(1, Py_None); if (unlikely(!__pyx_mstate_global->__pyx_tuple[16])) __PYX_ERR(0, 72, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_mstate_global->__pyx_tuple[16]);
  __Pyx_GIVEREF(__pyx_mstate_global->__pyx_tuple[16]);
```

</details>

L73  🟠  (score=5)
```python
        self.entries = {}
```
<details><summary>Show generated C (score=5)</summary>

```c
  __pyx_t_1 = __Pyx_PyDict_NewPresized(0); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 73, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  if (__Pyx_PyObject_SetAttrStr(__pyx_v_self, __pyx_mstate_global->__pyx_n_u_entries, __pyx_t_1) < (0)) __PYX_ERR(0, 73, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
```

</details>

L74  🟡  (score=2)
```python
        self.outer = outer
```
<details><summary>Show generated C (score=2)</summary>

```c
  if (__Pyx_PyObject_SetAttrStr(__pyx_v_self, __pyx_mstate_global->__pyx_n_u_outer, __pyx_v_outer) < (0)) __PYX_ERR(0, 74, __pyx_L1_error)
```

</details>

L75  ⚪  (score=0)
```python
```
L76  🔴  (score=45)
```python
    def declare(self, name, value):
```
<details><summary>Show generated C (score=45)</summary>

```c
/* Python wrapper */
static PyObject *__pyx_pw_6Cython_8Compiler_8Scanning_16CompileTimeScope_3declare(PyObject *__pyx_self, 
#if CYTHON_METH_FASTCALL
PyObject *const *__pyx_args, Py_ssize_t __pyx_nargs, PyObject *__pyx_kwds
#else
PyObject *__pyx_args, PyObject *__pyx_kwds
#endif
); /*proto*/
PyDoc_STRVAR(__pyx_doc_6Cython_8Compiler_8Scanning_16CompileTimeScope_2declare, "File: Cython/Compiler/Scanning.py (starting at line 76)");
static PyMethodDef __pyx_mdef_6Cython_8Compiler_8Scanning_16CompileTimeScope_3declare = {"declare", (PyCFunction)(void(*)(void))(__Pyx_PyCFunction_FastCallWithKeywords)__pyx_pw_6Cython_8Compiler_8Scanning_16CompileTimeScope_3declare, __Pyx_METH_FASTCALL|METH_KEYWORDS, __pyx_doc_6Cython_8Compiler_8Scanning_16CompileTimeScope_2declare};
static PyObject *__pyx_pw_6Cython_8Compiler_8Scanning_16CompileTimeScope_3declare(PyObject *__pyx_self, 
#if CYTHON_METH_FASTCALL
PyObject *const *__pyx_args, Py_ssize_t __pyx_nargs, PyObject *__pyx_kwds
#else
PyObject *__pyx_args, PyObject *__pyx_kwds
#endif
) {
  PyObject *__pyx_v_self = 0;
  PyObject *__pyx_v_name = 0;
  PyObject *__pyx_v_value = 0;
  #if !CYTHON_METH_FASTCALL
  CYTHON_UNUSED Py_ssize_t __pyx_nargs;
  #endif
  CYTHON_UNUSED PyObject *const *__pyx_kwvalues;
  PyObject *__pyx_r = 0;
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("declare (wrapper)", 0);
  #if !CYTHON_METH_FASTCALL
  #if CYTHON_ASSUME_SAFE_SIZE
  __pyx_nargs = PyTuple_GET_SIZE(__pyx_args);
  #else
  __pyx_nargs = PyTuple_Size(__pyx_args); if (unlikely(__pyx_nargs < 0)) return NULL;
  #endif
  #endif
  __pyx_kwvalues = __Pyx_KwValues_FASTCALL(__pyx_args, __pyx_nargs);
  {
    PyObject ** const __pyx_pyargnames[] = {&__pyx_mstate_global->__pyx_n_u_self,&__pyx_mstate_global->__pyx_n_u_name,&__pyx_mstate_global->__pyx_n_u_value,0};
  PyObject* values[3] = {0,0,0};
    const Py_ssize_t __pyx_kwds_len = (__pyx_kwds) ? __Pyx_NumKwargs_FASTCALL(__pyx_kwds) : 0;
    if (unlikely(__pyx_kwds_len) < 0) __PYX_ERR(0, 76, __pyx_L3_error)
    if (__pyx_kwds_len > 0) {
      switch (__pyx_nargs) {
        case  3:
        values[2] = __Pyx_ArgRef_FASTCALL(__pyx_args, 2);
        if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[2])) __PYX_ERR(0, 76, __pyx_L3_error)
        CYTHON_FALLTHROUGH;
        case  2:
        values[1] = __Pyx_ArgRef_FASTCALL(__pyx_args, 1);
        if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[1])) __PYX_ERR(0, 76, __pyx_L3_error)
        CYTHON_FALLTHROUGH;
        case  1:
        values[0] = __Pyx_ArgRef_FASTCALL(__pyx_args, 0);
        if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[0])) __PYX_ERR(0, 76, __pyx_L3_error)
        CYTHON_FALLTHROUGH;
        case  0: break;
        default: goto __pyx_L5_argtuple_error;
      }
      const Py_ssize_t kwd_pos_args = __pyx_nargs;
      if (__Pyx_ParseKeywords(__pyx_kwds, __pyx_kwvalues, __pyx_pyargnames, 0, values, kwd_pos_args, __pyx_kwds_len, "declare", 0) < (0)) __PYX_ERR(0, 76, __pyx_L3_error)
      for (Py_ssize_t i = __pyx_nargs; i < 3; i++) {
        if (unlikely(!values[i])) { __Pyx_RaiseArgtupleInvalid("declare", 1, 3, 3, i); __PYX_ERR(0, 76, __pyx_L3_error) }
      }
    } else if (unlikely(__pyx_nargs != 3)) {
      goto __pyx_L5_argtuple_error;
    } else {
      values[0] = __Pyx_ArgRef_FASTCALL(__pyx_args, 0);
      if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[0])) __PYX_ERR(0, 76, __pyx_L3_error)
      values[1] = __Pyx_ArgRef_FASTCALL(__pyx_args, 1);
      if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[1])) __PYX_ERR(0, 76, __pyx_L3_error)
      values[2] = __Pyx_ArgRef_FASTCALL(__pyx_args, 2);
      if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[2])) __PYX_ERR(0, 76, __pyx_L3_error)
    }
    __pyx_v_self = values[0];
    __pyx_v_name = values[1];
    __pyx_v_value = values[2];
  }
  goto __pyx_L6_skip;
  __pyx_L5_argtuple_error:;
  __Pyx_RaiseArgtupleInvalid("declare", 1, 3, 3, __pyx_nargs); __PYX_ERR(0, 76, __pyx_L3_error)
  __pyx_L6_skip:;
  goto __pyx_L4_argument_unpacking_done;
  __pyx_L3_error:;
  for (Py_ssize_t __pyx_temp=0; __pyx_temp < (Py_ssize_t)(sizeof(values)/sizeof(values[0])); ++__pyx_temp) {
    Py_XDECREF(values[__pyx_temp]);
  }
  __Pyx_AddTraceback("Cython.Compiler.Scanning.CompileTimeScope.declare", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __Pyx_RefNannyFinishContext();
  return NULL;
  __pyx_L4_argument_unpacking_done:;
  __pyx_r = __pyx_pf_6Cython_8Compiler_8Scanning_16CompileTimeScope_2declare(__pyx_self, __pyx_v_self, __pyx_v_name, __pyx_v_value);
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

static PyObject *__pyx_pf_6Cython_8Compiler_8Scanning_16CompileTimeScope_2declare(CYTHON_UNUSED PyObject *__pyx_self, PyObject *__pyx_v_self, PyObject *__pyx_v_name, PyObject *__pyx_v_value) {
  PyObject *__pyx_r = NULL;
/* … */
  /* function exit code */
  __pyx_r = Py_None; __Pyx_INCREF(Py_None);
  goto __pyx_L0;
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_t_1);
  __Pyx_AddTraceback("Cython.Compiler.Scanning.CompileTimeScope.declare", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_r = NULL;
  __pyx_L0:;
  __Pyx_XGIVEREF(__pyx_r);
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}
/* … */
  __pyx_t_4 = __Pyx_CyFunction_New(&__pyx_mdef_6Cython_8Compiler_8Scanning_16CompileTimeScope_3declare, 0, __pyx_mstate_global->__pyx_n_u_CompileTimeScope_declare, NULL, __pyx_mstate_global->__pyx_n_u_Cython_Compiler_Scanning, __pyx_mstate_global->__pyx_d, ((PyObject *)__pyx_mstate_global->__pyx_codeobj_tab[3])); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 76, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_4);
  #if CYTHON_COMPILING_IN_CPYTHON && PY_VERSION_HEX >= 0x030E0000
  PyUnstable_Object_EnableDeferredRefcount(__pyx_t_4);
  #endif
  if (__Pyx_SetNameInClass(__pyx_t_6, __pyx_mstate_global->__pyx_n_u_declare, __pyx_t_4) < (0)) __PYX_ERR(0, 76, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
```

</details>

L77  🟠  (score=8)
```python
        self.entries[name] = value
```
<details><summary>Show generated C (score=8)</summary>

```c
  __pyx_t_1 = __Pyx_PyObject_GetAttrStr(__pyx_v_self, __pyx_mstate_global->__pyx_n_u_entries); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 77, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  if (unlikely((PyObject_SetItem(__pyx_t_1, __pyx_v_name, __pyx_v_value) < 0))) __PYX_ERR(0, 77, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
```

</details>

L78  ⚪  (score=0)
```python
```
L79  🔴  (score=43)
```python
    def update(self, other):
```
<details><summary>Show generated C (score=43)</summary>

```c
/* Python wrapper */
static PyObject *__pyx_pw_6Cython_8Compiler_8Scanning_16CompileTimeScope_5update(PyObject *__pyx_self, 
#if CYTHON_METH_FASTCALL
PyObject *const *__pyx_args, Py_ssize_t __pyx_nargs, PyObject *__pyx_kwds
#else
PyObject *__pyx_args, PyObject *__pyx_kwds
#endif
); /*proto*/
PyDoc_STRVAR(__pyx_doc_6Cython_8Compiler_8Scanning_16CompileTimeScope_4update, "File: Cython/Compiler/Scanning.py (starting at line 79)");
static PyMethodDef __pyx_mdef_6Cython_8Compiler_8Scanning_16CompileTimeScope_5update = {"update", (PyCFunction)(void(*)(void))(__Pyx_PyCFunction_FastCallWithKeywords)__pyx_pw_6Cython_8Compiler_8Scanning_16CompileTimeScope_5update, __Pyx_METH_FASTCALL|METH_KEYWORDS, __pyx_doc_6Cython_8Compiler_8Scanning_16CompileTimeScope_4update};
static PyObject *__pyx_pw_6Cython_8Compiler_8Scanning_16CompileTimeScope_5update(PyObject *__pyx_self, 
#if CYTHON_METH_FASTCALL
PyObject *const *__pyx_args, Py_ssize_t __pyx_nargs, PyObject *__pyx_kwds
#else
PyObject *__pyx_args, PyObject *__pyx_kwds
#endif
) {
  PyObject *__pyx_v_self = 0;
  PyObject *__pyx_v_other = 0;
  #if !CYTHON_METH_FASTCALL
  CYTHON_UNUSED Py_ssize_t __pyx_nargs;
  #endif
  CYTHON_UNUSED PyObject *const *__pyx_kwvalues;
  PyObject *__pyx_r = 0;
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("update (wrapper)", 0);
  #if !CYTHON_METH_FASTCALL
  #if CYTHON_ASSUME_SAFE_SIZE
  __pyx_nargs = PyTuple_GET_SIZE(__pyx_args);
  #else
  __pyx_nargs = PyTuple_Size(__pyx_args); if (unlikely(__pyx_nargs < 0)) return NULL;
  #endif
  #endif
  __pyx_kwvalues = __Pyx_KwValues_FASTCALL(__pyx_args, __pyx_nargs);
  {
    PyObject ** const __pyx_pyargnames[] = {&__pyx_mstate_global->__pyx_n_u_self,&__pyx_mstate_global->__pyx_n_u_other,0};
  PyObject* values[2] = {0,0};
    const Py_ssize_t __pyx_kwds_len = (__pyx_kwds) ? __Pyx_NumKwargs_FASTCALL(__pyx_kwds) : 0;
    if (unlikely(__pyx_kwds_len) < 0) __PYX_ERR(0, 79, __pyx_L3_error)
    if (__pyx_kwds_len > 0) {
      switch (__pyx_nargs) {
        case  2:
        values[1] = __Pyx_ArgRef_FASTCALL(__pyx_args, 1);
        if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[1])) __PYX_ERR(0, 79, __pyx_L3_error)
        CYTHON_FALLTHROUGH;
        case  1:
        values[0] = __Pyx_ArgRef_FASTCALL(__pyx_args, 0);
        if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[0])) __PYX_ERR(0, 79, __pyx_L3_error)
        CYTHON_FALLTHROUGH;
        case  0: break;
        default: goto __pyx_L5_argtuple_error;
      }
      const Py_ssize_t kwd_pos_args = __pyx_nargs;
      if (__Pyx_ParseKeywords(__pyx_kwds, __pyx_kwvalues, __pyx_pyargnames, 0, values, kwd_pos_args, __pyx_kwds_len, "update", 0) < (0)) __PYX_ERR(0, 79, __pyx_L3_error)
      for (Py_ssize_t i = __pyx_nargs; i < 2; i++) {
        if (unlikely(!values[i])) { __Pyx_RaiseArgtupleInvalid("update", 1, 2, 2, i); __PYX_ERR(0, 79, __pyx_L3_error) }
      }
    } else if (unlikely(__pyx_nargs != 2)) {
      goto __pyx_L5_argtuple_error;
    } else {
      values[0] = __Pyx_ArgRef_FASTCALL(__pyx_args, 0);
      if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[0])) __PYX_ERR(0, 79, __pyx_L3_error)
      values[1] = __Pyx_ArgRef_FASTCALL(__pyx_args, 1);
      if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[1])) __PYX_ERR(0, 79, __pyx_L3_error)
    }
    __pyx_v_self = values[0];
    __pyx_v_other = values[1];
  }
  goto __pyx_L6_skip;
  __pyx_L5_argtuple_error:;
  __Pyx_RaiseArgtupleInvalid("update", 1, 2, 2, __pyx_nargs); __PYX_ERR(0, 79, __pyx_L3_error)
  __pyx_L6_skip:;
  goto __pyx_L4_argument_unpacking_done;
  __pyx_L3_error:;
  for (Py_ssize_t __pyx_temp=0; __pyx_temp < (Py_ssize_t)(sizeof(values)/sizeof(values[0])); ++__pyx_temp) {
    Py_XDECREF(values[__pyx_temp]);
  }
  __Pyx_AddTraceback("Cython.Compiler.Scanning.CompileTimeScope.update", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __Pyx_RefNannyFinishContext();
  return NULL;
  __pyx_L4_argument_unpacking_done:;
  __pyx_r = __pyx_pf_6Cython_8Compiler_8Scanning_16CompileTimeScope_4update(__pyx_self, __pyx_v_self, __pyx_v_other);
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

static PyObject *__pyx_pf_6Cython_8Compiler_8Scanning_16CompileTimeScope_4update(CYTHON_UNUSED PyObject *__pyx_self, PyObject *__pyx_v_self, PyObject *__pyx_v_other) {
  PyObject *__pyx_r = NULL;
/* … */
  /* function exit code */
  __pyx_r = Py_None; __Pyx_INCREF(Py_None);
  goto __pyx_L0;
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_t_1);
  __Pyx_XDECREF(__pyx_t_2);
  __Pyx_XDECREF(__pyx_t_3);
  __Pyx_AddTraceback("Cython.Compiler.Scanning.CompileTimeScope.update", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_r = NULL;
  __pyx_L0:;
  __Pyx_XGIVEREF(__pyx_r);
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}
/* … */
  __pyx_t_4 = __Pyx_CyFunction_New(&__pyx_mdef_6Cython_8Compiler_8Scanning_16CompileTimeScope_5update, 0, __pyx_mstate_global->__pyx_n_u_CompileTimeScope_update, NULL, __pyx_mstate_global->__pyx_n_u_Cython_Compiler_Scanning, __pyx_mstate_global->__pyx_d, ((PyObject *)__pyx_mstate_global->__pyx_codeobj_tab[4])); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 79, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_4);
  #if CYTHON_COMPILING_IN_CPYTHON && PY_VERSION_HEX >= 0x030E0000
  PyUnstable_Object_EnableDeferredRefcount(__pyx_t_4);
  #endif
  if (__Pyx_SetNameInClass(__pyx_t_6, __pyx_mstate_global->__pyx_n_u_update, __pyx_t_4) < (0)) __PYX_ERR(0, 79, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
```

</details>

L80  🟠  (score=8)
```python
        self.entries.update(other)
```
<details><summary>Show generated C (score=8)</summary>

```c
  __pyx_t_3 = __Pyx_PyObject_GetAttrStr(__pyx_v_self, __pyx_mstate_global->__pyx_n_u_entries); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 80, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_3);
  __pyx_t_2 = __pyx_t_3;
  __Pyx_INCREF(__pyx_t_2);
  __pyx_t_4 = 0;
  {
    PyObject *__pyx_callargs[2] = {__pyx_t_2, __pyx_v_other};
    __pyx_t_1 = __Pyx_PyObject_FastCallMethod((PyObject*)__pyx_mstate_global->__pyx_n_u_update, __pyx_callargs+__pyx_t_4, (2-__pyx_t_4) | (1*__Pyx_PY_VECTORCALL_ARGUMENTS_OFFSET));
    __Pyx_XDECREF(__pyx_t_2); __pyx_t_2 = 0;
    __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
    if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 80, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_1);
  }
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
```

</details>

L81  ⚪  (score=0)
```python
```
L82  🔴  (score=41)
```python
    def lookup_here(self, name):
```
<details><summary>Show generated C (score=41)</summary>

```c
/* Python wrapper */
static PyObject *__pyx_pw_6Cython_8Compiler_8Scanning_16CompileTimeScope_7lookup_here(PyObject *__pyx_self, 
#if CYTHON_METH_FASTCALL
PyObject *const *__pyx_args, Py_ssize_t __pyx_nargs, PyObject *__pyx_kwds
#else
PyObject *__pyx_args, PyObject *__pyx_kwds
#endif
); /*proto*/
PyDoc_STRVAR(__pyx_doc_6Cython_8Compiler_8Scanning_16CompileTimeScope_6lookup_here, "File: Cython/Compiler/Scanning.py (starting at line 82)");
static PyMethodDef __pyx_mdef_6Cython_8Compiler_8Scanning_16CompileTimeScope_7lookup_here = {"lookup_here", (PyCFunction)(void(*)(void))(__Pyx_PyCFunction_FastCallWithKeywords)__pyx_pw_6Cython_8Compiler_8Scanning_16CompileTimeScope_7lookup_here, __Pyx_METH_FASTCALL|METH_KEYWORDS, __pyx_doc_6Cython_8Compiler_8Scanning_16CompileTimeScope_6lookup_here};
static PyObject *__pyx_pw_6Cython_8Compiler_8Scanning_16CompileTimeScope_7lookup_here(PyObject *__pyx_self, 
#if CYTHON_METH_FASTCALL
PyObject *const *__pyx_args, Py_ssize_t __pyx_nargs, PyObject *__pyx_kwds
#else
PyObject *__pyx_args, PyObject *__pyx_kwds
#endif
) {
  PyObject *__pyx_v_self = 0;
  PyObject *__pyx_v_name = 0;
  #if !CYTHON_METH_FASTCALL
  CYTHON_UNUSED Py_ssize_t __pyx_nargs;
  #endif
  CYTHON_UNUSED PyObject *const *__pyx_kwvalues;
  PyObject *__pyx_r = 0;
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("lookup_here (wrapper)", 0);
  #if !CYTHON_METH_FASTCALL
  #if CYTHON_ASSUME_SAFE_SIZE
  __pyx_nargs = PyTuple_GET_SIZE(__pyx_args);
  #else
  __pyx_nargs = PyTuple_Size(__pyx_args); if (unlikely(__pyx_nargs < 0)) return NULL;
  #endif
  #endif
  __pyx_kwvalues = __Pyx_KwValues_FASTCALL(__pyx_args, __pyx_nargs);
  {
    PyObject ** const __pyx_pyargnames[] = {&__pyx_mstate_global->__pyx_n_u_self,&__pyx_mstate_global->__pyx_n_u_name,0};
  PyObject* values[2] = {0,0};
    const Py_ssize_t __pyx_kwds_len = (__pyx_kwds) ? __Pyx_NumKwargs_FASTCALL(__pyx_kwds) : 0;
    if (unlikely(__pyx_kwds_len) < 0) __PYX_ERR(0, 82, __pyx_L3_error)
    if (__pyx_kwds_len > 0) {
      switch (__pyx_nargs) {
        case  2:
        values[1] = __Pyx_ArgRef_FASTCALL(__pyx_args, 1);
        if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[1])) __PYX_ERR(0, 82, __pyx_L3_error)
        CYTHON_FALLTHROUGH;
        case  1:
        values[0] = __Pyx_ArgRef_FASTCALL(__pyx_args, 0);
        if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[0])) __PYX_ERR(0, 82, __pyx_L3_error)
        CYTHON_FALLTHROUGH;
        case  0: break;
        default: goto __pyx_L5_argtuple_error;
      }
      const Py_ssize_t kwd_pos_args = __pyx_nargs;
      if (__Pyx_ParseKeywords(__pyx_kwds, __pyx_kwvalues, __pyx_pyargnames, 0, values, kwd_pos_args, __pyx_kwds_len, "lookup_here", 0) < (0)) __PYX_ERR(0, 82, __pyx_L3_error)
      for (Py_ssize_t i = __pyx_nargs; i < 2; i++) {
        if (unlikely(!values[i])) { __Pyx_RaiseArgtupleInvalid("lookup_here", 1, 2, 2, i); __PYX_ERR(0, 82, __pyx_L3_error) }
      }
    } else if (unlikely(__pyx_nargs != 2)) {
      goto __pyx_L5_argtuple_error;
    } else {
      values[0] = __Pyx_ArgRef_FASTCALL(__pyx_args, 0);
      if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[0])) __PYX_ERR(0, 82, __pyx_L3_error)
      values[1] = __Pyx_ArgRef_FASTCALL(__pyx_args, 1);
      if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[1])) __PYX_ERR(0, 82, __pyx_L3_error)
    }
    __pyx_v_self = values[0];
    __pyx_v_name = values[1];
  }
  goto __pyx_L6_skip;
  __pyx_L5_argtuple_error:;
  __Pyx_RaiseArgtupleInvalid("lookup_here", 1, 2, 2, __pyx_nargs); __PYX_ERR(0, 82, __pyx_L3_error)
  __pyx_L6_skip:;
  goto __pyx_L4_argument_unpacking_done;
  __pyx_L3_error:;
  for (Py_ssize_t __pyx_temp=0; __pyx_temp < (Py_ssize_t)(sizeof(values)/sizeof(values[0])); ++__pyx_temp) {
    Py_XDECREF(values[__pyx_temp]);
  }
  __Pyx_AddTraceback("Cython.Compiler.Scanning.CompileTimeScope.lookup_here", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __Pyx_RefNannyFinishContext();
  return NULL;
  __pyx_L4_argument_unpacking_done:;
  __pyx_r = __pyx_pf_6Cython_8Compiler_8Scanning_16CompileTimeScope_6lookup_here(__pyx_self, __pyx_v_self, __pyx_v_name);
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

static PyObject *__pyx_pf_6Cython_8Compiler_8Scanning_16CompileTimeScope_6lookup_here(CYTHON_UNUSED PyObject *__pyx_self, PyObject *__pyx_v_self, PyObject *__pyx_v_name) {
  PyObject *__pyx_r = NULL;
/* … */
  /* function exit code */
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_t_1);
  __Pyx_XDECREF(__pyx_t_2);
  __Pyx_AddTraceback("Cython.Compiler.Scanning.CompileTimeScope.lookup_here", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_r = NULL;
  __pyx_L0:;
  __Pyx_XGIVEREF(__pyx_r);
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}
/* … */
  __pyx_t_4 = __Pyx_CyFunction_New(&__pyx_mdef_6Cython_8Compiler_8Scanning_16CompileTimeScope_7lookup_here, 0, __pyx_mstate_global->__pyx_n_u_CompileTimeScope_lookup_here, NULL, __pyx_mstate_global->__pyx_n_u_Cython_Compiler_Scanning, __pyx_mstate_global->__pyx_d, ((PyObject *)__pyx_mstate_global->__pyx_codeobj_tab[5])); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 82, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_4);
  #if CYTHON_COMPILING_IN_CPYTHON && PY_VERSION_HEX >= 0x030E0000
  PyUnstable_Object_EnableDeferredRefcount(__pyx_t_4);
  #endif
  if (__Pyx_SetNameInClass(__pyx_t_6, __pyx_mstate_global->__pyx_n_u_lookup_here, __pyx_t_4) < (0)) __PYX_ERR(0, 82, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
```

</details>

L83  🟠  (score=6)
```python
        return self.entries[name]
```
<details><summary>Show generated C (score=6)</summary>

```c
  __Pyx_XDECREF(__pyx_r);
  __pyx_t_1 = __Pyx_PyObject_GetAttrStr(__pyx_v_self, __pyx_mstate_global->__pyx_n_u_entries); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 83, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __pyx_t_2 = __Pyx_PyObject_GetItem(__pyx_t_1, __pyx_v_name); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 83, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __pyx_r = __pyx_t_2;
  __pyx_t_2 = 0;
  goto __pyx_L0;
```

</details>

L84  ⚪  (score=0)
```python
```
L85  🔴  (score=40)
```python
    def __contains__(self, name):
```
<details><summary>Show generated C (score=40)</summary>

```c
/* Python wrapper */
static PyObject *__pyx_pw_6Cython_8Compiler_8Scanning_16CompileTimeScope_9__contains__(PyObject *__pyx_self, 
#if CYTHON_METH_FASTCALL
PyObject *const *__pyx_args, Py_ssize_t __pyx_nargs, PyObject *__pyx_kwds
#else
PyObject *__pyx_args, PyObject *__pyx_kwds
#endif
); /*proto*/
PyDoc_STRVAR(__pyx_doc_6Cython_8Compiler_8Scanning_16CompileTimeScope_8__contains__, "File: Cython/Compiler/Scanning.py (starting at line 85)");
static PyMethodDef __pyx_mdef_6Cython_8Compiler_8Scanning_16CompileTimeScope_9__contains__ = {"__contains__", (PyCFunction)(void(*)(void))(__Pyx_PyCFunction_FastCallWithKeywords)__pyx_pw_6Cython_8Compiler_8Scanning_16CompileTimeScope_9__contains__, __Pyx_METH_FASTCALL|METH_KEYWORDS, __pyx_doc_6Cython_8Compiler_8Scanning_16CompileTimeScope_8__contains__};
static PyObject *__pyx_pw_6Cython_8Compiler_8Scanning_16CompileTimeScope_9__contains__(PyObject *__pyx_self, 
#if CYTHON_METH_FASTCALL
PyObject *const *__pyx_args, Py_ssize_t __pyx_nargs, PyObject *__pyx_kwds
#else
PyObject *__pyx_args, PyObject *__pyx_kwds
#endif
) {
  PyObject *__pyx_v_self = 0;
  PyObject *__pyx_v_name = 0;
  #if !CYTHON_METH_FASTCALL
  CYTHON_UNUSED Py_ssize_t __pyx_nargs;
  #endif
  CYTHON_UNUSED PyObject *const *__pyx_kwvalues;
  PyObject *__pyx_r = 0;
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("__contains__ (wrapper)", 0);
  #if !CYTHON_METH_FASTCALL
  #if CYTHON_ASSUME_SAFE_SIZE
  __pyx_nargs = PyTuple_GET_SIZE(__pyx_args);
  #else
  __pyx_nargs = PyTuple_Size(__pyx_args); if (unlikely(__pyx_nargs < 0)) return NULL;
  #endif
  #endif
  __pyx_kwvalues = __Pyx_KwValues_FASTCALL(__pyx_args, __pyx_nargs);
  {
    PyObject ** const __pyx_pyargnames[] = {&__pyx_mstate_global->__pyx_n_u_self,&__pyx_mstate_global->__pyx_n_u_name,0};
  PyObject* values[2] = {0,0};
    const Py_ssize_t __pyx_kwds_len = (__pyx_kwds) ? __Pyx_NumKwargs_FASTCALL(__pyx_kwds) : 0;
    if (unlikely(__pyx_kwds_len) < 0) __PYX_ERR(0, 85, __pyx_L3_error)
    if (__pyx_kwds_len > 0) {
      switch (__pyx_nargs) {
        case  2:
        values[1] = __Pyx_ArgRef_FASTCALL(__pyx_args, 1);
        if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[1])) __PYX_ERR(0, 85, __pyx_L3_error)
        CYTHON_FALLTHROUGH;
        case  1:
        values[0] = __Pyx_ArgRef_FASTCALL(__pyx_args, 0);
        if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[0])) __PYX_ERR(0, 85, __pyx_L3_error)
        CYTHON_FALLTHROUGH;
        case  0: break;
        default: goto __pyx_L5_argtuple_error;
      }
      const Py_ssize_t kwd_pos_args = __pyx_nargs;
      if (__Pyx_ParseKeywords(__pyx_kwds, __pyx_kwvalues, __pyx_pyargnames, 0, values, kwd_pos_args, __pyx_kwds_len, "__contains__", 0) < (0)) __PYX_ERR(0, 85, __pyx_L3_error)
      for (Py_ssize_t i = __pyx_nargs; i < 2; i++) {
        if (unlikely(!values[i])) { __Pyx_RaiseArgtupleInvalid("__contains__", 1, 2, 2, i); __PYX_ERR(0, 85, __pyx_L3_error) }
      }
    } else if (unlikely(__pyx_nargs != 2)) {
      goto __pyx_L5_argtuple_error;
    } else {
      values[0] = __Pyx_ArgRef_FASTCALL(__pyx_args, 0);
      if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[0])) __PYX_ERR(0, 85, __pyx_L3_error)
      values[1] = __Pyx_ArgRef_FASTCALL(__pyx_args, 1);
      if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[1])) __PYX_ERR(0, 85, __pyx_L3_error)
    }
    __pyx_v_self = values[0];
    __pyx_v_name = values[1];
  }
  goto __pyx_L6_skip;
  __pyx_L5_argtuple_error:;
  __Pyx_RaiseArgtupleInvalid("__contains__", 1, 2, 2, __pyx_nargs); __PYX_ERR(0, 85, __pyx_L3_error)
  __pyx_L6_skip:;
  goto __pyx_L4_argument_unpacking_done;
  __pyx_L3_error:;
  for (Py_ssize_t __pyx_temp=0; __pyx_temp < (Py_ssize_t)(sizeof(values)/sizeof(values[0])); ++__pyx_temp) {
    Py_XDECREF(values[__pyx_temp]);
  }
  __Pyx_AddTraceback("Cython.Compiler.Scanning.CompileTimeScope.__contains__", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __Pyx_RefNannyFinishContext();
  return NULL;
  __pyx_L4_argument_unpacking_done:;
  __pyx_r = __pyx_pf_6Cython_8Compiler_8Scanning_16CompileTimeScope_8__contains__(__pyx_self, __pyx_v_self, __pyx_v_name);
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

static PyObject *__pyx_pf_6Cython_8Compiler_8Scanning_16CompileTimeScope_8__contains__(CYTHON_UNUSED PyObject *__pyx_self, PyObject *__pyx_v_self, PyObject *__pyx_v_name) {
  PyObject *__pyx_r = NULL;
/* … */
  /* function exit code */
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_t_1);
  __Pyx_AddTraceback("Cython.Compiler.Scanning.CompileTimeScope.__contains__", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_r = NULL;
  __pyx_L0:;
  __Pyx_XGIVEREF(__pyx_r);
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}
/* … */
  __pyx_t_4 = __Pyx_CyFunction_New(&__pyx_mdef_6Cython_8Compiler_8Scanning_16CompileTimeScope_9__contains__, 0, __pyx_mstate_global->__pyx_n_u_CompileTimeScope___contains, NULL, __pyx_mstate_global->__pyx_n_u_Cython_Compiler_Scanning, __pyx_mstate_global->__pyx_d, ((PyObject *)__pyx_mstate_global->__pyx_codeobj_tab[6])); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 85, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_4);
  #if CYTHON_COMPILING_IN_CPYTHON && PY_VERSION_HEX >= 0x030E0000
  PyUnstable_Object_EnableDeferredRefcount(__pyx_t_4);
  #endif
  if (__Pyx_SetNameInClass(__pyx_t_6, __pyx_mstate_global->__pyx_n_u_contains, __pyx_t_4) < (0)) __PYX_ERR(0, 85, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
```

</details>

L86  🟠  (score=8)
```python
        return name in self.entries
```
<details><summary>Show generated C (score=8)</summary>

```c
  __Pyx_XDECREF(__pyx_r);
  __pyx_t_1 = __Pyx_PyObject_GetAttrStr(__pyx_v_self, __pyx_mstate_global->__pyx_n_u_entries); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 86, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __pyx_t_2 = (__Pyx_PySequence_ContainsTF(__pyx_v_name, __pyx_t_1, Py_EQ)); if (unlikely((__pyx_t_2 < 0))) __PYX_ERR(0, 86, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __pyx_t_1 = __Pyx_PyBool_FromLong(__pyx_t_2); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 86, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __pyx_r = __pyx_t_1;
  __pyx_t_1 = 0;
  goto __pyx_L0;
```

</details>

L87  ⚪  (score=0)
```python
```
L88  🔴  (score=45)
```python
    def lookup(self, name):
```
<details><summary>Show generated C (score=45)</summary>

```c
/* Python wrapper */
static PyObject *__pyx_pw_6Cython_8Compiler_8Scanning_16CompileTimeScope_11lookup(PyObject *__pyx_self, 
#if CYTHON_METH_FASTCALL
PyObject *const *__pyx_args, Py_ssize_t __pyx_nargs, PyObject *__pyx_kwds
#else
PyObject *__pyx_args, PyObject *__pyx_kwds
#endif
); /*proto*/
PyDoc_STRVAR(__pyx_doc_6Cython_8Compiler_8Scanning_16CompileTimeScope_10lookup, "File: Cython/Compiler/Scanning.py (starting at line 88)");
static PyMethodDef __pyx_mdef_6Cython_8Compiler_8Scanning_16CompileTimeScope_11lookup = {"lookup", (PyCFunction)(void(*)(void))(__Pyx_PyCFunction_FastCallWithKeywords)__pyx_pw_6Cython_8Compiler_8Scanning_16CompileTimeScope_11lookup, __Pyx_METH_FASTCALL|METH_KEYWORDS, __pyx_doc_6Cython_8Compiler_8Scanning_16CompileTimeScope_10lookup};
static PyObject *__pyx_pw_6Cython_8Compiler_8Scanning_16CompileTimeScope_11lookup(PyObject *__pyx_self, 
#if CYTHON_METH_FASTCALL
PyObject *const *__pyx_args, Py_ssize_t __pyx_nargs, PyObject *__pyx_kwds
#else
PyObject *__pyx_args, PyObject *__pyx_kwds
#endif
) {
  PyObject *__pyx_v_self = 0;
  PyObject *__pyx_v_name = 0;
  #if !CYTHON_METH_FASTCALL
  CYTHON_UNUSED Py_ssize_t __pyx_nargs;
  #endif
  CYTHON_UNUSED PyObject *const *__pyx_kwvalues;
  PyObject *__pyx_r = 0;
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("lookup (wrapper)", 0);
  #if !CYTHON_METH_FASTCALL
  #if CYTHON_ASSUME_SAFE_SIZE
  __pyx_nargs = PyTuple_GET_SIZE(__pyx_args);
  #else
  __pyx_nargs = PyTuple_Size(__pyx_args); if (unlikely(__pyx_nargs < 0)) return NULL;
  #endif
  #endif
  __pyx_kwvalues = __Pyx_KwValues_FASTCALL(__pyx_args, __pyx_nargs);
  {
    PyObject ** const __pyx_pyargnames[] = {&__pyx_mstate_global->__pyx_n_u_self,&__pyx_mstate_global->__pyx_n_u_name,0};
  PyObject* values[2] = {0,0};
    const Py_ssize_t __pyx_kwds_len = (__pyx_kwds) ? __Pyx_NumKwargs_FASTCALL(__pyx_kwds) : 0;
    if (unlikely(__pyx_kwds_len) < 0) __PYX_ERR(0, 88, __pyx_L3_error)
    if (__pyx_kwds_len > 0) {
      switch (__pyx_nargs) {
        case  2:
        values[1] = __Pyx_ArgRef_FASTCALL(__pyx_args, 1);
        if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[1])) __PYX_ERR(0, 88, __pyx_L3_error)
        CYTHON_FALLTHROUGH;
        case  1:
        values[0] = __Pyx_ArgRef_FASTCALL(__pyx_args, 0);
        if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[0])) __PYX_ERR(0, 88, __pyx_L3_error)
        CYTHON_FALLTHROUGH;
        case  0: break;
        default: goto __pyx_L5_argtuple_error;
      }
      const Py_ssize_t kwd_pos_args = __pyx_nargs;
      if (__Pyx_ParseKeywords(__pyx_kwds, __pyx_kwvalues, __pyx_pyargnames, 0, values, kwd_pos_args, __pyx_kwds_len, "lookup", 0) < (0)) __PYX_ERR(0, 88, __pyx_L3_error)
      for (Py_ssize_t i = __pyx_nargs; i < 2; i++) {
        if (unlikely(!values[i])) { __Pyx_RaiseArgtupleInvalid("lookup", 1, 2, 2, i); __PYX_ERR(0, 88, __pyx_L3_error) }
      }
    } else if (unlikely(__pyx_nargs != 2)) {
      goto __pyx_L5_argtuple_error;
    } else {
      values[0] = __Pyx_ArgRef_FASTCALL(__pyx_args, 0);
      if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[0])) __PYX_ERR(0, 88, __pyx_L3_error)
      values[1] = __Pyx_ArgRef_FASTCALL(__pyx_args, 1);
      if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[1])) __PYX_ERR(0, 88, __pyx_L3_error)
    }
    __pyx_v_self = values[0];
    __pyx_v_name = values[1];
  }
  goto __pyx_L6_skip;
  __pyx_L5_argtuple_error:;
  __Pyx_RaiseArgtupleInvalid("lookup", 1, 2, 2, __pyx_nargs); __PYX_ERR(0, 88, __pyx_L3_error)
  __pyx_L6_skip:;
  goto __pyx_L4_argument_unpacking_done;
  __pyx_L3_error:;
  for (Py_ssize_t __pyx_temp=0; __pyx_temp < (Py_ssize_t)(sizeof(values)/sizeof(values[0])); ++__pyx_temp) {
    Py_XDECREF(values[__pyx_temp]);
  }
  __Pyx_AddTraceback("Cython.Compiler.Scanning.CompileTimeScope.lookup", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __Pyx_RefNannyFinishContext();
  return NULL;
  __pyx_L4_argument_unpacking_done:;
  __pyx_r = __pyx_pf_6Cython_8Compiler_8Scanning_16CompileTimeScope_10lookup(__pyx_self, __pyx_v_self, __pyx_v_name);
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

static PyObject *__pyx_pf_6Cython_8Compiler_8Scanning_16CompileTimeScope_10lookup(CYTHON_UNUSED PyObject *__pyx_self, PyObject *__pyx_v_self, PyObject *__pyx_v_name) {
  PyObject *__pyx_v_outer = NULL;
  PyObject *__pyx_r = NULL;
/* … */
  /* function exit code */
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_t_4);
  __Pyx_XDECREF(__pyx_t_5);
  __Pyx_XDECREF(__pyx_t_8);
  __Pyx_XDECREF(__pyx_t_9);
  __Pyx_XDECREF(__pyx_t_11);
  __Pyx_AddTraceback("Cython.Compiler.Scanning.CompileTimeScope.lookup", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_r = NULL;
  __pyx_L0:;
  __Pyx_XDECREF(__pyx_v_outer);
  __Pyx_XGIVEREF(__pyx_r);
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}
/* … */
  __pyx_t_4 = __Pyx_CyFunction_New(&__pyx_mdef_6Cython_8Compiler_8Scanning_16CompileTimeScope_11lookup, 0, __pyx_mstate_global->__pyx_n_u_CompileTimeScope_lookup, NULL, __pyx_mstate_global->__pyx_n_u_Cython_Compiler_Scanning, __pyx_mstate_global->__pyx_d, ((PyObject *)__pyx_mstate_global->__pyx_codeobj_tab[7])); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 88, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_4);
  #if CYTHON_COMPILING_IN_CPYTHON && PY_VERSION_HEX >= 0x030E0000
  PyUnstable_Object_EnableDeferredRefcount(__pyx_t_4);
  #endif
  if (__Pyx_SetNameInClass(__pyx_t_6, __pyx_mstate_global->__pyx_n_u_lookup, __pyx_t_4) < (0)) __PYX_ERR(0, 88, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
```

</details>

L89  🟠  (score=8)
```python
        try:
```
<details><summary>Show generated C (score=8)</summary>

```c
  {
    /*try:*/ {
/* … */
    }
    __pyx_L3_error:;
    __Pyx_XDECREF(__pyx_t_4); __pyx_t_4 = 0;
    __Pyx_XDECREF(__pyx_t_5); __pyx_t_5 = 0;
/* … */
    __pyx_L5_except_error:;
    __Pyx_XGIVEREF(__pyx_t_1);
    __Pyx_XGIVEREF(__pyx_t_2);
    __Pyx_XGIVEREF(__pyx_t_3);
    __Pyx_ExceptionReset(__pyx_t_1, __pyx_t_2, __pyx_t_3);
    goto __pyx_L1_error;
    __pyx_L7_try_return:;
    __Pyx_XGIVEREF(__pyx_t_1);
    __Pyx_XGIVEREF(__pyx_t_2);
    __Pyx_XGIVEREF(__pyx_t_3);
    __Pyx_ExceptionReset(__pyx_t_1, __pyx_t_2, __pyx_t_3);
    goto __pyx_L0;
    __pyx_L6_except_return:;
    __Pyx_XGIVEREF(__pyx_t_1);
    __Pyx_XGIVEREF(__pyx_t_2);
    __Pyx_XGIVEREF(__pyx_t_3);
    __Pyx_ExceptionReset(__pyx_t_1, __pyx_t_2, __pyx_t_3);
    goto __pyx_L0;
  }
```

</details>

L90  🟠  (score=5)
```python
            return self.lookup_here(name)
```
<details><summary>Show generated C (score=5)</summary>

```c
      __Pyx_XDECREF(__pyx_r);
      __pyx_t_5 = __pyx_v_self;
      __Pyx_INCREF(__pyx_t_5);
      __pyx_t_6 = 0;
      {
        PyObject *__pyx_callargs[2] = {__pyx_t_5, __pyx_v_name};
        __pyx_t_4 = __Pyx_PyObject_FastCallMethod((PyObject*)__pyx_mstate_global->__pyx_n_u_lookup_here, __pyx_callargs+__pyx_t_6, (2-__pyx_t_6) | (1*__Pyx_PY_VECTORCALL_ARGUMENTS_OFFSET));
        __Pyx_XDECREF(__pyx_t_5); __pyx_t_5 = 0;
        if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 90, __pyx_L3_error)
        __Pyx_GOTREF(__pyx_t_4);
      }
      __pyx_r = __pyx_t_4;
      __pyx_t_4 = 0;
      goto __pyx_L7_try_return;
```

</details>

L91  🟠  (score=6)
```python
        except KeyError:
```
<details><summary>Show generated C (score=6)</summary>

```c
    __pyx_t_7 = __Pyx_PyErr_ExceptionMatches(((PyObject *)(((PyTypeObject*)PyExc_KeyError))));
    if (__pyx_t_7) {
      __Pyx_AddTraceback("Cython.Compiler.Scanning.CompileTimeScope.lookup", __pyx_clineno, __pyx_lineno, __pyx_filename);
      if (__Pyx_GetException(&__pyx_t_4, &__pyx_t_5, &__pyx_t_8) < 0) __PYX_ERR(0, 91, __pyx_L5_except_error)
      __Pyx_XGOTREF(__pyx_t_4);
      __Pyx_XGOTREF(__pyx_t_5);
      __Pyx_XGOTREF(__pyx_t_8);
```

</details>

L92  🟡  (score=2)
```python
            outer = self.outer
```
<details><summary>Show generated C (score=2)</summary>

```c
      __pyx_t_9 = __Pyx_PyObject_GetAttrStr(__pyx_v_self, __pyx_mstate_global->__pyx_n_u_outer); if (unlikely(!__pyx_t_9)) __PYX_ERR(0, 92, __pyx_L5_except_error)
      __Pyx_GOTREF(__pyx_t_9);
      __pyx_v_outer = __pyx_t_9;
      __pyx_t_9 = 0;
```

</details>

L93  🟡  (score=2)
```python
            if outer:
```
<details><summary>Show generated C (score=2)</summary>

```c
      __pyx_t_10 = __Pyx_PyObject_IsTrue(__pyx_v_outer); if (unlikely((__pyx_t_10 < 0))) __PYX_ERR(0, 93, __pyx_L5_except_error)
      if (__pyx_t_10) {
/* … */
      }
```

</details>

L94  🟠  (score=8)
```python
                return outer.lookup(name)
```
<details><summary>Show generated C (score=8)</summary>

```c
        __Pyx_XDECREF(__pyx_r);
        __pyx_t_11 = __pyx_v_outer;
        __Pyx_INCREF(__pyx_t_11);
        __pyx_t_6 = 0;
        {
          PyObject *__pyx_callargs[2] = {__pyx_t_11, __pyx_v_name};
          __pyx_t_9 = __Pyx_PyObject_FastCallMethod((PyObject*)__pyx_mstate_global->__pyx_n_u_lookup, __pyx_callargs+__pyx_t_6, (2-__pyx_t_6) | (1*__Pyx_PY_VECTORCALL_ARGUMENTS_OFFSET));
          __Pyx_XDECREF(__pyx_t_11); __pyx_t_11 = 0;
          if (unlikely(!__pyx_t_9)) __PYX_ERR(0, 94, __pyx_L5_except_error)
          __Pyx_GOTREF(__pyx_t_9);
        }
        __pyx_r = __pyx_t_9;
        __pyx_t_9 = 0;
        __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
        __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
        __Pyx_DECREF(__pyx_t_8); __pyx_t_8 = 0;
        goto __pyx_L6_except_return;
```

</details>

L95  🟡  (score=2)
```python
            raise
```
<details><summary>Show generated C (score=2)</summary>

```c
      __Pyx_GIVEREF(__pyx_t_4);
      __Pyx_GIVEREF(__pyx_t_5);
      __Pyx_XGIVEREF(__pyx_t_8);
      __Pyx_ErrRestoreWithState(__pyx_t_4, __pyx_t_5, __pyx_t_8);
      __pyx_t_4 = 0;  __pyx_t_5 = 0;  __pyx_t_8 = 0; 
      __PYX_ERR(0, 95, __pyx_L5_except_error)
    }
    goto __pyx_L5_except_error;
```

</details>

L96  ⚪  (score=0)
```python
```
L97  ⚪  (score=0)
```python
```
L98  🔴  (score=59)
```python
def initial_compile_time_env() -> CompileTimeScope:
```
<details><summary>Show generated C (score=59)</summary>

```c
/* Python wrapper */
static PyObject *__pyx_pw_6Cython_8Compiler_8Scanning_3initial_compile_time_env(PyObject *__pyx_self, CYTHON_UNUSED PyObject *unused); /*proto*/
PyDoc_STRVAR(__pyx_doc_6Cython_8Compiler_8Scanning_2initial_compile_time_env, "File: Cython/Compiler/Scanning.py (starting at line 98)");
static PyMethodDef __pyx_mdef_6Cython_8Compiler_8Scanning_3initial_compile_time_env = {"initial_compile_time_env", (PyCFunction)__pyx_pw_6Cython_8Compiler_8Scanning_3initial_compile_time_env, METH_NOARGS, __pyx_doc_6Cython_8Compiler_8Scanning_2initial_compile_time_env};
static PyObject *__pyx_pw_6Cython_8Compiler_8Scanning_3initial_compile_time_env(PyObject *__pyx_self, CYTHON_UNUSED PyObject *unused) {
  CYTHON_UNUSED PyObject *const *__pyx_kwvalues;
  PyObject *__pyx_r = 0;
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("initial_compile_time_env (wrapper)", 0);
  __pyx_kwvalues = __Pyx_KwValues_VARARGS(__pyx_args, __pyx_nargs);
  __pyx_r = __pyx_pf_6Cython_8Compiler_8Scanning_2initial_compile_time_env(__pyx_self);

  /* function exit code */
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}

static PyObject *__pyx_pf_6Cython_8Compiler_8Scanning_2initial_compile_time_env(CYTHON_UNUSED PyObject *__pyx_self) {
  PyObject *__pyx_v_benv = NULL;
  PyObject *__pyx_v_names = NULL;
  PyObject *__pyx_v_name = NULL;
  PyObject *__pyx_v_value = NULL;
  PyObject *__pyx_v_builtins = NULL;
  PyObject *__pyx_v_reduce = NULL;
  PyObject *__pyx_r = NULL;
/* … */
  /* function exit code */
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_t_1);
  __Pyx_XDECREF(__pyx_t_2);
  __Pyx_XDECREF(__pyx_t_3);
  __Pyx_XDECREF(__pyx_t_5);
  __Pyx_XDECREF(__pyx_t_8);
  __Pyx_AddTraceback("Cython.Compiler.Scanning.initial_compile_time_env", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_r = NULL;
  __pyx_L0:;
  __Pyx_XDECREF(__pyx_v_benv);
  __Pyx_XDECREF(__pyx_v_names);
  __Pyx_XDECREF(__pyx_v_name);
  __Pyx_XDECREF(__pyx_v_value);
  __Pyx_XDECREF(__pyx_v_builtins);
  __Pyx_XDECREF(__pyx_v_reduce);
  __Pyx_XGIVEREF(__pyx_r);
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}
/* … */
  __pyx_t_6 = __Pyx_PyDict_NewPresized(1); if (unlikely(!__pyx_t_6)) __PYX_ERR(0, 98, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_6);
  #if defined(PyDict_SetItem) && (defined(CYTHON_COMPILING_IN_CPYTHON))
  #if PY_VERSION_HEX >= 0x030A0000 /* CPython 3.10+ exposes KnownHash APIs */
  /* Use CPython's KnownHash APIs when available */
  extern int _PyDict_SetItem_KnownHash(PyObject*, PyObject*, PyObject*, Py_hash_t);
  {
    Py_hash_t __pyx_hash = PyObject_Hash(__pyx_mstate_global->__pyx_n_u_return); if (unlikely(__pyx_hash == -1)) __PYX_ERR(0, 98, __pyx_L1_error);
    if (unlikely(_PyDict_SetItem_KnownHash(__pyx_t_6, __pyx_mstate_global->__pyx_n_u_return, __pyx_mstate_global->__pyx_n_u_CompileTimeScope, __pyx_hash) < 0)) __PYX_ERR(0, 98, __pyx_L1_error);
  }
  #else
  if (PyDict_SetItem(__pyx_t_6, __pyx_mstate_global->__pyx_n_u_return, __pyx_mstate_global->__pyx_n_u_CompileTimeScope) < (0)) __PYX_ERR(0, 98, __pyx_L1_error)
  #endif
  #else
  if (PyDict_SetItem(__pyx_t_6, __pyx_mstate_global->__pyx_n_u_return, __pyx_mstate_global->__pyx_n_u_CompileTimeScope) < (0)) __PYX_ERR(0, 98, __pyx_L1_error)
  #endif
  __pyx_t_4 = __Pyx_CyFunction_New(&__pyx_mdef_6Cython_8Compiler_8Scanning_3initial_compile_time_env, 0, __pyx_mstate_global->__pyx_n_u_initial_compile_time_env, NULL, __pyx_mstate_global->__pyx_n_u_Cython_Compiler_Scanning, __pyx_mstate_global->__pyx_d, ((PyObject *)__pyx_mstate_global->__pyx_codeobj_tab[8])); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 98, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_4);
  #if CYTHON_COMPILING_IN_CPYTHON && PY_VERSION_HEX >= 0x030E0000
  PyUnstable_Object_EnableDeferredRefcount(__pyx_t_4);
  #endif
  __Pyx_CyFunction_SetAnnotationsDict(__pyx_t_4, __pyx_t_6);
  __Pyx_DECREF(__pyx_t_6); __pyx_t_6 = 0;
  if (PyDict_SetItem(__pyx_mstate_global->__pyx_d, __pyx_mstate_global->__pyx_n_u_initial_compile_time_env, __pyx_t_4) < (0)) __PYX_ERR(0, 98, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
```

</details>

L99  🟠  (score=6)
```python
    benv = CompileTimeScope()
```
<details><summary>Show generated C (score=6)</summary>

```c
  __pyx_t_2 = NULL;
  __Pyx_GetModuleGlobalName(__pyx_t_3, __pyx_mstate_global->__pyx_n_u_CompileTimeScope); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 99, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_3);
  __pyx_t_4 = 1;
  {
    PyObject *__pyx_callargs[2] = {__pyx_t_2, NULL};
    __pyx_t_1 = __Pyx_PyObject_FastCall((PyObject*)__pyx_t_3, __pyx_callargs+__pyx_t_4, (1-__pyx_t_4) | (__pyx_t_4*__Pyx_PY_VECTORCALL_ARGUMENTS_OFFSET));
    __Pyx_XDECREF(__pyx_t_2); __pyx_t_2 = 0;
    __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
    if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 99, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_1);
  }
  __pyx_v_benv = __pyx_t_1;
  __pyx_t_1 = 0;
```

</details>

L100  🟠  (score=6)
```python
    names = ('UNAME_SYSNAME', 'UNAME_NODENAME', 'UNAME_RELEASE', 'UNAME_VERSION', 'UNAME_MACHINE')
```
<details><summary>Show generated C (score=6)</summary>

```c
  __Pyx_INCREF(__pyx_mstate_global->__pyx_tuple[0]);
  __pyx_v_names = __pyx_mstate_global->__pyx_tuple[0];
/* … */
  __pyx_mstate_global->__pyx_tuple[0] = PyTuple_Pack(5, __pyx_mstate_global->__pyx_n_u_UNAME_SYSNAME, __pyx_mstate_global->__pyx_n_u_UNAME_NODENAME, __pyx_mstate_global->__pyx_n_u_UNAME_RELEASE, __pyx_mstate_global->__pyx_n_u_UNAME_VERSION, __pyx_mstate_global->__pyx_n_u_UNAME_MACHINE); if (unlikely(!__pyx_mstate_global->__pyx_tuple[0])) __PYX_ERR(0, 100, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_mstate_global->__pyx_tuple[0]);
  __Pyx_GIVEREF(__pyx_mstate_global->__pyx_tuple[0]);
```

</details>

L101  🔴  (score=113)
```python
    for name, value in zip(names, platform.uname(), strict=False):
```
<details><summary>Show generated C (score=113)</summary>

```c
  __pyx_t_3 = NULL;
  __pyx_t_5 = __pyx_v_6Cython_8Compiler_8Scanning_platform;
  __Pyx_INCREF(__pyx_t_5);
  __pyx_t_4 = 0;
  {
    PyObject *__pyx_callargs[2] = {__pyx_t_5, NULL};
    __pyx_t_2 = __Pyx_PyObject_FastCallMethod((PyObject*)__pyx_mstate_global->__pyx_n_u_uname, __pyx_callargs+__pyx_t_4, (1-__pyx_t_4) | (1*__Pyx_PY_VECTORCALL_ARGUMENTS_OFFSET));
    __Pyx_XDECREF(__pyx_t_5); __pyx_t_5 = 0;
    if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 101, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_2);
  }
  __pyx_t_4 = 1;
  {
    PyObject *__pyx_callargs[3 + ((CYTHON_VECTORCALL) ? 1 : 0)] = {__pyx_t_3, __pyx_v_names, __pyx_t_2};
    __pyx_t_5 = __Pyx_MakeVectorcallBuilderKwds(1); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 101, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_5);
    if (__Pyx_VectorcallBuilder_AddArg(__pyx_mstate_global->__pyx_n_u_strict, Py_False, __pyx_t_5, __pyx_callargs+3, 0) < (0)) __PYX_ERR(0, 101, __pyx_L1_error)
    __pyx_t_1 = __Pyx_Object_Vectorcall_CallFromBuilder((PyObject*)__pyx_builtin_zip, __pyx_callargs+__pyx_t_4, (3-__pyx_t_4) | (__pyx_t_4*__Pyx_PY_VECTORCALL_ARGUMENTS_OFFSET), __pyx_t_5);
    __Pyx_XDECREF(__pyx_t_3); __pyx_t_3 = 0;
    __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
    __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
    if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 101, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_1);
  }
  if (likely(PyList_CheckExact(__pyx_t_1)) || PyTuple_CheckExact(__pyx_t_1)) {
    __pyx_t_5 = __pyx_t_1; __Pyx_INCREF(__pyx_t_5);
    __pyx_t_6 = 0;
    __pyx_t_7 = NULL;
  } else {
    __pyx_t_6 = -1; __pyx_t_5 = PyObject_GetIter(__pyx_t_1); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 101, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_5);
    __pyx_t_7 = (CYTHON_COMPILING_IN_LIMITED_API) ? PyIter_Next : __Pyx_PyObject_GetIterNextFunc(__pyx_t_5); if (unlikely(!__pyx_t_7)) __PYX_ERR(0, 101, __pyx_L1_error)
  }
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  for (;;) {
    if (likely(!__pyx_t_7)) {
      if (likely(PyList_CheckExact(__pyx_t_5))) {
        {
          Py_ssize_t __pyx_temp = __Pyx_PyList_GET_SIZE(__pyx_t_5);
          #if !CYTHON_ASSUME_SAFE_SIZE
          if (unlikely((__pyx_temp < 0))) __PYX_ERR(0, 101, __pyx_L1_error)
          #endif
          if (__pyx_t_6 >= __pyx_temp) break;
        }
        __pyx_t_1 = __Pyx_PyList_GetItemRefFast(__pyx_t_5, __pyx_t_6, __Pyx_ReferenceSharing_OwnStrongReference);
        ++__pyx_t_6;
      } else {
        {
          Py_ssize_t __pyx_temp = __Pyx_PyTuple_GET_SIZE(__pyx_t_5);
          #if !CYTHON_ASSUME_SAFE_SIZE
          if (unlikely((__pyx_temp < 0))) __PYX_ERR(0, 101, __pyx_L1_error)
          #endif
          if (__pyx_t_6 >= __pyx_temp) break;
        }
        #if CYTHON_ASSUME_SAFE_MACROS && !CYTHON_AVOID_BORROWED_REFS
        __pyx_t_1 = __Pyx_NewRef(PyTuple_GET_ITEM(__pyx_t_5, __pyx_t_6));
        #else
        __pyx_t_1 = __Pyx_PySequence_ITEM(__pyx_t_5, __pyx_t_6);
        #endif
        ++__pyx_t_6;
      }
      if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 101, __pyx_L1_error)
    } else {
      __pyx_t_1 = __pyx_t_7(__pyx_t_5);
      if (unlikely(!__pyx_t_1)) {
        PyObject* exc_type = PyErr_Occurred();
        if (exc_type) {
          if (unlikely(!__Pyx_PyErr_GivenExceptionMatches(exc_type, PyExc_StopIteration))) __PYX_ERR(0, 101, __pyx_L1_error)
          PyErr_Clear();
        }
        break;
      }
    }
    __Pyx_GOTREF(__pyx_t_1);
    if ((likely(PyTuple_CheckExact(__pyx_t_1))) || (PyList_CheckExact(__pyx_t_1))) {
      PyObject* sequence = __pyx_t_1;
      Py_ssize_t size = __Pyx_PySequence_SIZE(sequence);
      if (unlikely(size != 2)) {
        if (size > 2) __Pyx_RaiseTooManyValuesError(2);
        else if (size >= 0) __Pyx_RaiseNeedMoreValuesError(size);
        __PYX_ERR(0, 101, __pyx_L1_error)
      }
      #if CYTHON_ASSUME_SAFE_MACROS && !CYTHON_AVOID_BORROWED_REFS
      if (likely(PyTuple_CheckExact(sequence))) {
        __pyx_t_2 = PyTuple_GET_ITEM(sequence, 0);
        __Pyx_INCREF(__pyx_t_2);
        __pyx_t_3 = PyTuple_GET_ITEM(sequence, 1);
        __Pyx_INCREF(__pyx_t_3);
      } else {
        __pyx_t_2 = __Pyx_PyList_GetItemRefFast(sequence, 0, __Pyx_ReferenceSharing_SharedReference);
        if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 101, __pyx_L1_error)
        __Pyx_XGOTREF(__pyx_t_2);
        __pyx_t_3 = __Pyx_PyList_GetItemRefFast(sequence, 1, __Pyx_ReferenceSharing_SharedReference);
        if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 101, __pyx_L1_error)
        __Pyx_XGOTREF(__pyx_t_3);
      }
      #else
      __pyx_t_2 = __Pyx_PySequence_ITEM(sequence, 0); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 101, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_2);
      __pyx_t_3 = __Pyx_PySequence_ITEM(sequence, 1); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 101, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_3);
      #endif
      __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
    } else {
      Py_ssize_t index = -1;
      __pyx_t_8 = PyObject_GetIter(__pyx_t_1); if (unlikely(!__pyx_t_8)) __PYX_ERR(0, 101, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_8);
      __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
      __pyx_t_9 = (CYTHON_COMPILING_IN_LIMITED_API) ? PyIter_Next : __Pyx_PyObject_GetIterNextFunc(__pyx_t_8);
      index = 0; __pyx_t_2 = __pyx_t_9(__pyx_t_8); if (unlikely(!__pyx_t_2)) goto __pyx_L5_unpacking_failed;
      __Pyx_GOTREF(__pyx_t_2);
      index = 1; __pyx_t_3 = __pyx_t_9(__pyx_t_8); if (unlikely(!__pyx_t_3)) goto __pyx_L5_unpacking_failed;
      __Pyx_GOTREF(__pyx_t_3);
      if (__Pyx_IternextUnpackEndCheck(__pyx_t_9(__pyx_t_8), 2) < (0)) __PYX_ERR(0, 101, __pyx_L1_error)
      __pyx_t_9 = NULL;
      __Pyx_DECREF(__pyx_t_8); __pyx_t_8 = 0;
      goto __pyx_L6_unpacking_done;
      __pyx_L5_unpacking_failed:;
      __Pyx_DECREF(__pyx_t_8); __pyx_t_8 = 0;
      __pyx_t_9 = NULL;
      if (__Pyx_IterFinish() == 0) __Pyx_RaiseNeedMoreValuesError(index);
      __PYX_ERR(0, 101, __pyx_L1_error)
      __pyx_L6_unpacking_done:;
    }
    __Pyx_XDECREF_SET(__pyx_v_name, __pyx_t_2);
    __pyx_t_2 = 0;
    __Pyx_XDECREF_SET(__pyx_v_value, __pyx_t_3);
    __pyx_t_3 = 0;
/* … */
  }
  __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
```

</details>

L102  🟠  (score=5)
```python
        benv.declare(name, value)
```
<details><summary>Show generated C (score=5)</summary>

```c
    __pyx_t_3 = __pyx_v_benv;
    __Pyx_INCREF(__pyx_t_3);
    __pyx_t_4 = 0;
    {
      PyObject *__pyx_callargs[3] = {__pyx_t_3, __pyx_v_name, __pyx_v_value};
      __pyx_t_1 = __Pyx_PyObject_FastCallMethod((PyObject*)__pyx_mstate_global->__pyx_n_u_declare, __pyx_callargs+__pyx_t_4, (3-__pyx_t_4) | (1*__Pyx_PY_VECTORCALL_ARGUMENTS_OFFSET));
      __Pyx_XDECREF(__pyx_t_3); __pyx_t_3 = 0;
      if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 102, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_1);
    }
    __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
```

</details>

L103  🟡  (score=2)
```python
    import builtins
```
<details><summary>Show generated C (score=2)</summary>

```c
  __pyx_t_10 = __Pyx_Import(__pyx_mstate_global->__pyx_n_u_builtins, 0, 0, NULL, 0); if (unlikely(!__pyx_t_10)) __PYX_ERR(0, 103, __pyx_L1_error)
  __pyx_t_5 = __pyx_t_10;
  __Pyx_GOTREF(__pyx_t_5);
  __pyx_v_builtins = __pyx_t_5;
  __pyx_t_5 = 0;
```

</details>

L104  ⚪  (score=0)
```python
```
L105  ⚪  (score=0)
```python
    names = (
```
L106  🟠  (score=7)
```python
        'False', 'True',
```
<details><summary>Show generated C (score=7)</summary>

```c
  __Pyx_INCREF(__pyx_mstate_global->__pyx_tuple[1]);
  __Pyx_DECREF_SET(__pyx_v_names, __pyx_mstate_global->__pyx_tuple[1]);
/* … */
  __pyx_mstate_global->__pyx_tuple[1] = PyTuple_Pack(42, __pyx_mstate_global->__pyx_n_u_False, __pyx_mstate_global->__pyx_n_u_True, __pyx_mstate_global->__pyx_n_u_abs, __pyx_mstate_global->__pyx_n_u_all, __pyx_mstate_global->__pyx_n_u_any, __pyx_mstate_global->__pyx_n_u_ascii, __pyx_mstate_global->__pyx_n_u_bin, __pyx_mstate_global->__pyx_n_u_bool, __pyx_mstate_global->__pyx_n_u_bytearray, __pyx_mstate_global->__pyx_n_u_bytes, __pyx_mstate_global->__pyx_n_u_chr, __pyx_mstate_global->__pyx_n_u_complex, __pyx_mstate_global->__pyx_n_u_dict, __pyx_mstate_global->__pyx_n_u_divmod, __pyx_mstate_global->__pyx_n_u_enumerate, __pyx_mstate_global->__pyx_n_u_filter, __pyx_mstate_global->__pyx_n_u_float, __pyx_mstate_global->__pyx_n_u_format, __pyx_mstate_global->__pyx_n_u_frozenset, __pyx_mstate_global->__pyx_n_u_hash, __pyx_mstate_global->__pyx_n_u_hex, __pyx_mstate_global->__pyx_n_u_int, __pyx_mstate_global->__pyx_n_u_len, __pyx_mstate_global->__pyx_n_u_list, __pyx_mstate_global->__pyx_n_u_map, __pyx_mstate_global->__pyx_n_u_max, __pyx_mstate_global->__pyx_n_u_min, __pyx_mstate_global->__pyx_n_u_next, __pyx_mstate_global->__pyx_n_u_oct, __pyx_mstate_global->__pyx_n_u_ord, __pyx_mstate_global->__pyx_n_u_pow, __pyx_mstate_global->__pyx_n_u_range, __pyx_mstate_global->__pyx_n_u_repr, __pyx_mstate_global->__pyx_n_u_reversed, __pyx_mstate_global->__pyx_n_u_round, __pyx_mstate_global->__pyx_n_u_set, __pyx_mstate_global->__pyx_n_u_slice, __pyx_mstate_global->__pyx_n_u_sorted, __pyx_mstate_global->__pyx_n_u_str, __pyx_mstate_global->__pyx_n_u_sum, __pyx_mstate_global->__pyx_n_u_tuple, __pyx_mstate_global->__pyx_n_u_zip); if (unlikely(!__pyx_mstate_global->__pyx_tuple[1])) __PYX_ERR(0, 106, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_mstate_global->__pyx_tuple[1]);
  __Pyx_GIVEREF(__pyx_mstate_global->__pyx_tuple[1]);
```

</details>

L107  ⚪  (score=0)
```python
        'abs', 'all', 'any', 'ascii', 'bin', 'bool', 'bytearray', 'bytes',
```
L108  ⚪  (score=0)
```python
        'chr', 'complex', 'dict', 'divmod', 'enumerate', 'filter',
```
L109  ⚪  (score=0)
```python
        'float', 'format', 'frozenset', 'hash', 'hex', 'int', 'len',
```
L110  ⚪  (score=0)
```python
        'list', 'map', 'max', 'min', 'next', 'oct', 'ord', 'pow', 'range',
```
L111  ⚪  (score=0)
```python
        'repr', 'reversed', 'round', 'set', 'slice', 'sorted', 'str',
```
L112  ⚪  (score=0)
```python
        'sum', 'tuple', 'zip',
```
L113  ⚪  (score=0)
```python
        ### defined below in a platform independent way
```
L114  ⚪  (score=0)
```python
        # 'long', 'unicode', 'reduce', 'xrange'
```
L115  ⚪  (score=0)
```python
    )
```
L116  ⚪  (score=0)
```python
```
L117  🔴  (score=48)
```python
    for name in names:
```
<details><summary>Show generated C (score=48)</summary>

```c
  if (likely(PyList_CheckExact(__pyx_v_names)) || PyTuple_CheckExact(__pyx_v_names)) {
    __pyx_t_5 = __pyx_v_names; __Pyx_INCREF(__pyx_t_5);
    __pyx_t_6 = 0;
    __pyx_t_7 = NULL;
  } else {
    __pyx_t_6 = -1; __pyx_t_5 = PyObject_GetIter(__pyx_v_names); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 117, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_5);
    __pyx_t_7 = (CYTHON_COMPILING_IN_LIMITED_API) ? PyIter_Next : __Pyx_PyObject_GetIterNextFunc(__pyx_t_5); if (unlikely(!__pyx_t_7)) __PYX_ERR(0, 117, __pyx_L1_error)
  }
  for (;;) {
    if (likely(!__pyx_t_7)) {
      if (likely(PyList_CheckExact(__pyx_t_5))) {
        {
          Py_ssize_t __pyx_temp = __Pyx_PyList_GET_SIZE(__pyx_t_5);
          #if !CYTHON_ASSUME_SAFE_SIZE
          if (unlikely((__pyx_temp < 0))) __PYX_ERR(0, 117, __pyx_L1_error)
          #endif
          if (__pyx_t_6 >= __pyx_temp) break;
        }
        __pyx_t_1 = __Pyx_PyList_GetItemRefFast(__pyx_t_5, __pyx_t_6, __Pyx_ReferenceSharing_OwnStrongReference);
        ++__pyx_t_6;
      } else {
        {
          Py_ssize_t __pyx_temp = __Pyx_PyTuple_GET_SIZE(__pyx_t_5);
          #if !CYTHON_ASSUME_SAFE_SIZE
          if (unlikely((__pyx_temp < 0))) __PYX_ERR(0, 117, __pyx_L1_error)
          #endif
          if (__pyx_t_6 >= __pyx_temp) break;
        }
        #if CYTHON_ASSUME_SAFE_MACROS && !CYTHON_AVOID_BORROWED_REFS
        __pyx_t_1 = __Pyx_NewRef(PyTuple_GET_ITEM(__pyx_t_5, __pyx_t_6));
        #else
        __pyx_t_1 = __Pyx_PySequence_ITEM(__pyx_t_5, __pyx_t_6);
        #endif
        ++__pyx_t_6;
      }
      if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 117, __pyx_L1_error)
    } else {
      __pyx_t_1 = __pyx_t_7(__pyx_t_5);
      if (unlikely(!__pyx_t_1)) {
        PyObject* exc_type = PyErr_Occurred();
        if (exc_type) {
          if (unlikely(!__Pyx_PyErr_GivenExceptionMatches(exc_type, PyExc_StopIteration))) __PYX_ERR(0, 117, __pyx_L1_error)
          PyErr_Clear();
        }
        break;
      }
    }
    __Pyx_GOTREF(__pyx_t_1);
    __Pyx_XDECREF_SET(__pyx_v_name, __pyx_t_1);
    __pyx_t_1 = 0;
/* … */
  }
  __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
```

</details>

L118  🟠  (score=8)
```python
        benv.declare(name, getattr(builtins, name))
```
<details><summary>Show generated C (score=8)</summary>

```c
    __pyx_t_3 = __pyx_v_benv;
    __Pyx_INCREF(__pyx_t_3);
    __pyx_t_2 = __Pyx_GetAttr(__pyx_v_builtins, __pyx_v_name); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 118, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_2);
    __pyx_t_4 = 0;
    {
      PyObject *__pyx_callargs[3] = {__pyx_t_3, __pyx_v_name, __pyx_t_2};
      __pyx_t_1 = __Pyx_PyObject_FastCallMethod((PyObject*)__pyx_mstate_global->__pyx_n_u_declare, __pyx_callargs+__pyx_t_4, (3-__pyx_t_4) | (1*__Pyx_PY_VECTORCALL_ARGUMENTS_OFFSET));
      __Pyx_XDECREF(__pyx_t_3); __pyx_t_3 = 0;
      __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
      if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 118, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_1);
    }
    __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
```

</details>

L119  ⚪  (score=0)
```python
```
L120  ⚪  (score=0)
```python
    # legacy Py2 names
```
L121  🟠  (score=7)
```python
    from functools import reduce
```
<details><summary>Show generated C (score=7)</summary>

```c
  {
    PyObject* const __pyx_imported_names[] = {__pyx_mstate_global->__pyx_n_u_reduce};
    __pyx_t_10 = __Pyx_Import(__pyx_mstate_global->__pyx_n_u_functools, __pyx_imported_names, 1, NULL, 0); if (unlikely(!__pyx_t_10)) __PYX_ERR(0, 121, __pyx_L1_error)
  }
  __pyx_t_5 = __pyx_t_10;
  __Pyx_GOTREF(__pyx_t_5);
  {
    PyObject* const __pyx_imported_names[] = {__pyx_mstate_global->__pyx_n_u_reduce};
    for (__pyx_t_6=0; __pyx_t_6 < 1; __pyx_t_6++) {
      __pyx_t_1 = __Pyx_ImportFrom(__pyx_t_5, __pyx_imported_names[__pyx_t_6]); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 121, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_1);
      switch (__pyx_t_6) {
        case 0:
        __Pyx_INCREF(__pyx_t_1);
        __pyx_v_reduce = __pyx_t_1;
        break;
      }
      __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
    }
  }
  __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
```

</details>

L122  🟠  (score=5)
```python
    benv.declare('reduce', reduce)
```
<details><summary>Show generated C (score=5)</summary>

```c
  __pyx_t_1 = __pyx_v_benv;
  __Pyx_INCREF(__pyx_t_1);
  __pyx_t_4 = 0;
  {
    PyObject *__pyx_callargs[3] = {__pyx_t_1, __pyx_mstate_global->__pyx_n_u_reduce, __pyx_v_reduce};
    __pyx_t_5 = __Pyx_PyObject_FastCallMethod((PyObject*)__pyx_mstate_global->__pyx_n_u_declare, __pyx_callargs+__pyx_t_4, (3-__pyx_t_4) | (1*__Pyx_PY_VECTORCALL_ARGUMENTS_OFFSET));
    __Pyx_XDECREF(__pyx_t_1); __pyx_t_1 = 0;
    if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 122, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_5);
  }
  __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
```

</details>

L123  🟠  (score=5)
```python
    benv.declare('unicode', str)
```
<details><summary>Show generated C (score=5)</summary>

```c
  __pyx_t_1 = __pyx_v_benv;
  __Pyx_INCREF(__pyx_t_1);
  __pyx_t_4 = 0;
  {
    PyObject *__pyx_callargs[3] = {__pyx_t_1, __pyx_mstate_global->__pyx_n_u_unicode, ((PyObject *)(&PyUnicode_Type))};
    __pyx_t_5 = __Pyx_PyObject_FastCallMethod((PyObject*)__pyx_mstate_global->__pyx_n_u_declare, __pyx_callargs+__pyx_t_4, (3-__pyx_t_4) | (1*__Pyx_PY_VECTORCALL_ARGUMENTS_OFFSET));
    __Pyx_XDECREF(__pyx_t_1); __pyx_t_1 = 0;
    if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 123, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_5);
  }
  __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
```

</details>

L124  🟠  (score=5)
```python
    benv.declare('long', int)
```
<details><summary>Show generated C (score=5)</summary>

```c
  __pyx_t_1 = __pyx_v_benv;
  __Pyx_INCREF(__pyx_t_1);
  __pyx_t_4 = 0;
  {
    PyObject *__pyx_callargs[3] = {__pyx_t_1, __pyx_mstate_global->__pyx_n_u_long, ((PyObject *)(&PyLong_Type))};
    __pyx_t_5 = __Pyx_PyObject_FastCallMethod((PyObject*)__pyx_mstate_global->__pyx_n_u_declare, __pyx_callargs+__pyx_t_4, (3-__pyx_t_4) | (1*__Pyx_PY_VECTORCALL_ARGUMENTS_OFFSET));
    __Pyx_XDECREF(__pyx_t_1); __pyx_t_1 = 0;
    if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 124, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_5);
  }
  __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
```

</details>

L125  🟠  (score=5)
```python
    benv.declare('xrange', range)
```
<details><summary>Show generated C (score=5)</summary>

```c
  __pyx_t_1 = __pyx_v_benv;
  __Pyx_INCREF(__pyx_t_1);
  __pyx_t_4 = 0;
  {
    PyObject *__pyx_callargs[3] = {__pyx_t_1, __pyx_mstate_global->__pyx_n_u_xrange, ((PyObject *)(&PyRange_Type))};
    __pyx_t_5 = __Pyx_PyObject_FastCallMethod((PyObject*)__pyx_mstate_global->__pyx_n_u_declare, __pyx_callargs+__pyx_t_4, (3-__pyx_t_4) | (1*__Pyx_PY_VECTORCALL_ARGUMENTS_OFFSET));
    __Pyx_XDECREF(__pyx_t_1); __pyx_t_1 = 0;
    if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 125, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_5);
  }
  __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
```

</details>

L126  ⚪  (score=0)
```python
```
L127  🟠  (score=7)
```python
    return CompileTimeScope(benv)
```
<details><summary>Show generated C (score=7)</summary>

```c
  __Pyx_XDECREF(__pyx_r);
  __pyx_t_1 = NULL;
  __Pyx_GetModuleGlobalName(__pyx_t_2, __pyx_mstate_global->__pyx_n_u_CompileTimeScope); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 127, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __pyx_t_4 = 1;
  {
    PyObject *__pyx_callargs[2] = {__pyx_t_1, __pyx_v_benv};
    __pyx_t_5 = __Pyx_PyObject_FastCall((PyObject*)__pyx_t_2, __pyx_callargs+__pyx_t_4, (2-__pyx_t_4) | (__pyx_t_4*__Pyx_PY_VECTORCALL_ARGUMENTS_OFFSET));
    __Pyx_XDECREF(__pyx_t_1); __pyx_t_1 = 0;
    __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
    if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 127, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_5);
  }
  __pyx_r = __pyx_t_5;
  __pyx_t_5 = 0;
  goto __pyx_L0;
```

</details>

L128  ⚪  (score=0)
```python
```
L129  ⚪  (score=0)
```python
```
L130  ⚪  (score=0)
```python
#------------------------------------------------------------------
```
L131  ⚪  (score=0)
```python
```
L132  🔴  (score=12)
```python
class SourceDescriptor:
```
<details><summary>Show generated C (score=12)</summary>

```c
  __pyx_t_4 = __Pyx_Py3MetaclassPrepare((PyObject *) NULL, __pyx_mstate_global->__pyx_empty_tuple, __pyx_mstate_global->__pyx_n_u_SourceDescriptor, __pyx_mstate_global->__pyx_n_u_SourceDescriptor, (PyObject *) NULL, __pyx_mstate_global->__pyx_n_u_Cython_Compiler_Scanning, __pyx_mstate_global->__pyx_kp_u_File_Cython_Compiler_Scanning_py_2); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 132, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_4);
/* … */
  __pyx_t_6 = __Pyx_Py3ClassCreate(((PyObject*)&PyType_Type), __pyx_mstate_global->__pyx_n_u_SourceDescriptor, __pyx_mstate_global->__pyx_empty_tuple, __pyx_t_4, NULL, 0, 0); if (unlikely(!__pyx_t_6)) __PYX_ERR(0, 132, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_6);
  #if CYTHON_COMPILING_IN_CPYTHON && PY_VERSION_HEX >= 0x030E0000
  PyUnstable_Object_EnableDeferredRefcount(__pyx_t_6);
  #endif
  if (PyDict_SetItem(__pyx_mstate_global->__pyx_d, __pyx_mstate_global->__pyx_n_u_SourceDescriptor, __pyx_t_6) < (0)) __PYX_ERR(0, 132, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_6); __pyx_t_6 = 0;
  __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
```

</details>

L133  ⚪  (score=0)
```python
    """A SourceDescriptor should be considered immutable."""
```
L134  🟡  (score=2)
```python
    filename = None
```
<details><summary>Show generated C (score=2)</summary>

```c
  if (__Pyx_SetNameInClass(__pyx_t_4, __pyx_mstate_global->__pyx_n_u_filename, Py_None) < (0)) __PYX_ERR(0, 134, __pyx_L1_error)
```

</details>

L135  🟡  (score=2)
```python
    in_utility_code = False
```
<details><summary>Show generated C (score=2)</summary>

```c
  if (__Pyx_SetNameInClass(__pyx_t_4, __pyx_mstate_global->__pyx_n_u_in_utility_code, Py_False) < (0)) __PYX_ERR(0, 135, __pyx_L1_error)
```

</details>

L136  ⚪  (score=0)
```python
```
L137  🟡  (score=2)
```python
    _file_type = 'pyx'
```
<details><summary>Show generated C (score=2)</summary>

```c
  if (__Pyx_SetNameInClass(__pyx_t_4, __pyx_mstate_global->__pyx_n_u_file_type, __pyx_mstate_global->__pyx_n_u_pyx_2) < (0)) __PYX_ERR(0, 137, __pyx_L1_error)
```

</details>

L138  ⚪  (score=0)
```python
```
L139  🟡  (score=2)
```python
    _escaped_description = None
```
<details><summary>Show generated C (score=2)</summary>

```c
  if (__Pyx_SetNameInClass(__pyx_t_4, __pyx_mstate_global->__pyx_n_u_escaped_description, Py_None) < (0)) __PYX_ERR(0, 139, __pyx_L1_error)
```

</details>

L140  🟡  (score=2)
```python
    _cmp_name = ''
```
<details><summary>Show generated C (score=2)</summary>

```c
  if (__Pyx_SetNameInClass(__pyx_t_4, __pyx_mstate_global->__pyx_n_u_cmp_name, __pyx_mstate_global->__pyx_kp_u__6) < (0)) __PYX_ERR(0, 140, __pyx_L1_error)
```

</details>

L141  🔴  (score=37)
```python
    def __str__(self):
```
<details><summary>Show generated C (score=37)</summary>

```c
/* Python wrapper */
static PyObject *__pyx_pw_6Cython_8Compiler_8Scanning_16SourceDescriptor_1__str__(PyObject *__pyx_self, 
#if CYTHON_METH_FASTCALL
PyObject *const *__pyx_args, Py_ssize_t __pyx_nargs, PyObject *__pyx_kwds
#else
PyObject *__pyx_args, PyObject *__pyx_kwds
#endif
); /*proto*/
PyDoc_STRVAR(__pyx_doc_6Cython_8Compiler_8Scanning_16SourceDescriptor___str__, "File: Cython/Compiler/Scanning.py (starting at line 141)");
static PyMethodDef __pyx_mdef_6Cython_8Compiler_8Scanning_16SourceDescriptor_1__str__ = {"__str__", (PyCFunction)(void(*)(void))(__Pyx_PyCFunction_FastCallWithKeywords)__pyx_pw_6Cython_8Compiler_8Scanning_16SourceDescriptor_1__str__, __Pyx_METH_FASTCALL|METH_KEYWORDS, __pyx_doc_6Cython_8Compiler_8Scanning_16SourceDescriptor___str__};
static PyObject *__pyx_pw_6Cython_8Compiler_8Scanning_16SourceDescriptor_1__str__(PyObject *__pyx_self, 
#if CYTHON_METH_FASTCALL
PyObject *const *__pyx_args, Py_ssize_t __pyx_nargs, PyObject *__pyx_kwds
#else
PyObject *__pyx_args, PyObject *__pyx_kwds
#endif
) {
  CYTHON_UNUSED PyObject *__pyx_v_self = 0;
  #if !CYTHON_METH_FASTCALL
  CYTHON_UNUSED Py_ssize_t __pyx_nargs;
  #endif
  CYTHON_UNUSED PyObject *const *__pyx_kwvalues;
  PyObject *__pyx_r = 0;
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("__str__ (wrapper)", 0);
  #if !CYTHON_METH_FASTCALL
  #if CYTHON_ASSUME_SAFE_SIZE
  __pyx_nargs = PyTuple_GET_SIZE(__pyx_args);
  #else
  __pyx_nargs = PyTuple_Size(__pyx_args); if (unlikely(__pyx_nargs < 0)) return NULL;
  #endif
  #endif
  __pyx_kwvalues = __Pyx_KwValues_FASTCALL(__pyx_args, __pyx_nargs);
  {
    PyObject ** const __pyx_pyargnames[] = {&__pyx_mstate_global->__pyx_n_u_self,0};
  PyObject* values[1] = {0};
    const Py_ssize_t __pyx_kwds_len = (__pyx_kwds) ? __Pyx_NumKwargs_FASTCALL(__pyx_kwds) : 0;
    if (unlikely(__pyx_kwds_len) < 0) __PYX_ERR(0, 141, __pyx_L3_error)
    if (__pyx_kwds_len > 0) {
      switch (__pyx_nargs) {
        case  1:
        values[0] = __Pyx_ArgRef_FASTCALL(__pyx_args, 0);
        if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[0])) __PYX_ERR(0, 141, __pyx_L3_error)
        CYTHON_FALLTHROUGH;
        case  0: break;
        default: goto __pyx_L5_argtuple_error;
      }
      const Py_ssize_t kwd_pos_args = __pyx_nargs;
      if (__Pyx_ParseKeywords(__pyx_kwds, __pyx_kwvalues, __pyx_pyargnames, 0, values, kwd_pos_args, __pyx_kwds_len, "__str__", 0) < (0)) __PYX_ERR(0, 141, __pyx_L3_error)
      for (Py_ssize_t i = __pyx_nargs; i < 1; i++) {
        if (unlikely(!values[i])) { __Pyx_RaiseArgtupleInvalid("__str__", 1, 1, 1, i); __PYX_ERR(0, 141, __pyx_L3_error) }
      }
    } else if (unlikely(__pyx_nargs != 1)) {
      goto __pyx_L5_argtuple_error;
    } else {
      values[0] = __Pyx_ArgRef_FASTCALL(__pyx_args, 0);
      if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[0])) __PYX_ERR(0, 141, __pyx_L3_error)
    }
    __pyx_v_self = values[0];
  }
  goto __pyx_L6_skip;
  __pyx_L5_argtuple_error:;
  __Pyx_RaiseArgtupleInvalid("__str__", 1, 1, 1, __pyx_nargs); __PYX_ERR(0, 141, __pyx_L3_error)
  __pyx_L6_skip:;
  goto __pyx_L4_argument_unpacking_done;
  __pyx_L3_error:;
  for (Py_ssize_t __pyx_temp=0; __pyx_temp < (Py_ssize_t)(sizeof(values)/sizeof(values[0])); ++__pyx_temp) {
    Py_XDECREF(values[__pyx_temp]);
  }
  __Pyx_AddTraceback("Cython.Compiler.Scanning.SourceDescriptor.__str__", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __Pyx_RefNannyFinishContext();
  return NULL;
  __pyx_L4_argument_unpacking_done:;
  __pyx_r = __pyx_pf_6Cython_8Compiler_8Scanning_16SourceDescriptor___str__(__pyx_self, __pyx_v_self);
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

static PyObject *__pyx_pf_6Cython_8Compiler_8Scanning_16SourceDescriptor___str__(CYTHON_UNUSED PyObject *__pyx_self, CYTHON_UNUSED PyObject *__pyx_v_self) {
  PyObject *__pyx_r = NULL;
/* … */
  /* function exit code */
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_t_1);
  __Pyx_XDECREF(__pyx_t_2);
  __Pyx_AddTraceback("Cython.Compiler.Scanning.SourceDescriptor.__str__", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_r = NULL;
  __Pyx_XGIVEREF(__pyx_r);
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}
/* … */
  __pyx_t_6 = __Pyx_CyFunction_New(&__pyx_mdef_6Cython_8Compiler_8Scanning_16SourceDescriptor_1__str__, 0, __pyx_mstate_global->__pyx_n_u_SourceDescriptor___str, NULL, __pyx_mstate_global->__pyx_n_u_Cython_Compiler_Scanning, __pyx_mstate_global->__pyx_d, ((PyObject *)__pyx_mstate_global->__pyx_codeobj_tab[9])); if (unlikely(!__pyx_t_6)) __PYX_ERR(0, 141, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_6);
  #if CYTHON_COMPILING_IN_CPYTHON && PY_VERSION_HEX >= 0x030E0000
  PyUnstable_Object_EnableDeferredRefcount(__pyx_t_6);
  #endif
  if (__Pyx_SetNameInClass(__pyx_t_4, __pyx_mstate_global->__pyx_n_u_str_2, __pyx_t_6) < (0)) __PYX_ERR(0, 141, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_6); __pyx_t_6 = 0;
```

</details>

L142  🟠  (score=6)
```python
        raise ValueError("SourceDescriptor should not be used directly as a filename")
```
<details><summary>Show generated C (score=6)</summary>

```c
  __pyx_t_2 = NULL;
  __pyx_t_3 = 1;
  {
    PyObject *__pyx_callargs[2] = {__pyx_t_2, __pyx_mstate_global->__pyx_kp_u_SourceDescriptor_should_not_be_u};
    __pyx_t_1 = __Pyx_PyObject_FastCall((PyObject*)(((PyTypeObject*)PyExc_ValueError)), __pyx_callargs+__pyx_t_3, (2-__pyx_t_3) | (__pyx_t_3*__Pyx_PY_VECTORCALL_ARGUMENTS_OFFSET));
    __Pyx_XDECREF(__pyx_t_2); __pyx_t_2 = 0;
    if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 142, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_1);
  }
  __Pyx_Raise(__pyx_t_1, 0, 0, 0);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __PYX_ERR(0, 142, __pyx_L1_error)
```

</details>

L143  ⚪  (score=0)
```python
```
L144  🔴  (score=76)
```python
    def set_file_type_from_name(self, filename:str):
```
<details><summary>Show generated C (score=76)</summary>

```c
/* Python wrapper */
static PyObject *__pyx_pw_6Cython_8Compiler_8Scanning_16SourceDescriptor_3set_file_type_from_name(PyObject *__pyx_self, 
#if CYTHON_METH_FASTCALL
PyObject *const *__pyx_args, Py_ssize_t __pyx_nargs, PyObject *__pyx_kwds
#else
PyObject *__pyx_args, PyObject *__pyx_kwds
#endif
); /*proto*/
PyDoc_STRVAR(__pyx_doc_6Cython_8Compiler_8Scanning_16SourceDescriptor_2set_file_type_from_name, "File: Cython/Compiler/Scanning.py (starting at line 144)");
static PyMethodDef __pyx_mdef_6Cython_8Compiler_8Scanning_16SourceDescriptor_3set_file_type_from_name = {"set_file_type_from_name", (PyCFunction)(void(*)(void))(__Pyx_PyCFunction_FastCallWithKeywords)__pyx_pw_6Cython_8Compiler_8Scanning_16SourceDescriptor_3set_file_type_from_name, __Pyx_METH_FASTCALL|METH_KEYWORDS, __pyx_doc_6Cython_8Compiler_8Scanning_16SourceDescriptor_2set_file_type_from_name};
static PyObject *__pyx_pw_6Cython_8Compiler_8Scanning_16SourceDescriptor_3set_file_type_from_name(PyObject *__pyx_self, 
#if CYTHON_METH_FASTCALL
PyObject *const *__pyx_args, Py_ssize_t __pyx_nargs, PyObject *__pyx_kwds
#else
PyObject *__pyx_args, PyObject *__pyx_kwds
#endif
) {
  PyObject *__pyx_v_self = 0;
  PyObject *__pyx_v_filename = 0;
  #if !CYTHON_METH_FASTCALL
  CYTHON_UNUSED Py_ssize_t __pyx_nargs;
  #endif
  CYTHON_UNUSED PyObject *const *__pyx_kwvalues;
  PyObject *__pyx_r = 0;
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("set_file_type_from_name (wrapper)", 0);
  #if !CYTHON_METH_FASTCALL
  #if CYTHON_ASSUME_SAFE_SIZE
  __pyx_nargs = PyTuple_GET_SIZE(__pyx_args);
  #else
  __pyx_nargs = PyTuple_Size(__pyx_args); if (unlikely(__pyx_nargs < 0)) return NULL;
  #endif
  #endif
  __pyx_kwvalues = __Pyx_KwValues_FASTCALL(__pyx_args, __pyx_nargs);
  {
    PyObject ** const __pyx_pyargnames[] = {&__pyx_mstate_global->__pyx_n_u_self,&__pyx_mstate_global->__pyx_n_u_filename,0};
  PyObject* values[2] = {0,0};
    const Py_ssize_t __pyx_kwds_len = (__pyx_kwds) ? __Pyx_NumKwargs_FASTCALL(__pyx_kwds) : 0;
    if (unlikely(__pyx_kwds_len) < 0) __PYX_ERR(0, 144, __pyx_L3_error)
    if (__pyx_kwds_len > 0) {
      switch (__pyx_nargs) {
        case  2:
        values[1] = __Pyx_ArgRef_FASTCALL(__pyx_args, 1);
        if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[1])) __PYX_ERR(0, 144, __pyx_L3_error)
        CYTHON_FALLTHROUGH;
        case  1:
        values[0] = __Pyx_ArgRef_FASTCALL(__pyx_args, 0);
        if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[0])) __PYX_ERR(0, 144, __pyx_L3_error)
        CYTHON_FALLTHROUGH;
        case  0: break;
        default: goto __pyx_L5_argtuple_error;
      }
      const Py_ssize_t kwd_pos_args = __pyx_nargs;
      if (__Pyx_ParseKeywords(__pyx_kwds, __pyx_kwvalues, __pyx_pyargnames, 0, values, kwd_pos_args, __pyx_kwds_len, "set_file_type_from_name", 0) < (0)) __PYX_ERR(0, 144, __pyx_L3_error)
      for (Py_ssize_t i = __pyx_nargs; i < 2; i++) {
        if (unlikely(!values[i])) { __Pyx_RaiseArgtupleInvalid("set_file_type_from_name", 1, 2, 2, i); __PYX_ERR(0, 144, __pyx_L3_error) }
      }
    } else if (unlikely(__pyx_nargs != 2)) {
      goto __pyx_L5_argtuple_error;
    } else {
      values[0] = __Pyx_ArgRef_FASTCALL(__pyx_args, 0);
      if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[0])) __PYX_ERR(0, 144, __pyx_L3_error)
      values[1] = __Pyx_ArgRef_FASTCALL(__pyx_args, 1);
      if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[1])) __PYX_ERR(0, 144, __pyx_L3_error)
    }
    __pyx_v_self = values[0];
    __pyx_v_filename = ((PyObject*)values[1]);
  }
  goto __pyx_L6_skip;
  __pyx_L5_argtuple_error:;
  __Pyx_RaiseArgtupleInvalid("set_file_type_from_name", 1, 2, 2, __pyx_nargs); __PYX_ERR(0, 144, __pyx_L3_error)
  __pyx_L6_skip:;
  goto __pyx_L4_argument_unpacking_done;
  __pyx_L3_error:;
  for (Py_ssize_t __pyx_temp=0; __pyx_temp < (Py_ssize_t)(sizeof(values)/sizeof(values[0])); ++__pyx_temp) {
    Py_XDECREF(values[__pyx_temp]);
  }
  __Pyx_AddTraceback("Cython.Compiler.Scanning.SourceDescriptor.set_file_type_from_name", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __Pyx_RefNannyFinishContext();
  return NULL;
  __pyx_L4_argument_unpacking_done:;
  if (unlikely(!__Pyx_ArgTypeTest(((PyObject *)__pyx_v_filename), (&PyUnicode_Type), 0, "filename", 2))) __PYX_ERR(0, 144, __pyx_L1_error)
  __pyx_r = __pyx_pf_6Cython_8Compiler_8Scanning_16SourceDescriptor_2set_file_type_from_name(__pyx_self, __pyx_v_self, __pyx_v_filename);
  int __pyx_lineno = 0;
  const char *__pyx_filename = NULL;
  int __pyx_clineno = 0;

  /* function exit code */
  goto __pyx_L0;
  __pyx_L1_error:;
  __pyx_r = NULL;
  for (Py_ssize_t __pyx_temp=0; __pyx_temp < (Py_ssize_t)(sizeof(values)/sizeof(values[0])); ++__pyx_temp) {
    Py_XDECREF(values[__pyx_temp]);
  }
  goto __pyx_L7_cleaned_up;
  __pyx_L0:;
  for (Py_ssize_t __pyx_temp=0; __pyx_temp < (Py_ssize_t)(sizeof(values)/sizeof(values[0])); ++__pyx_temp) {
    Py_XDECREF(values[__pyx_temp]);
  }
  __pyx_L7_cleaned_up:;
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}

static PyObject *__pyx_pf_6Cython_8Compiler_8Scanning_16SourceDescriptor_2set_file_type_from_name(CYTHON_UNUSED PyObject *__pyx_self, PyObject *__pyx_v_self, PyObject *__pyx_v_filename) {
  PyObject *__pyx_v_ext = NULL;
  PyObject *__pyx_r = NULL;
/* … */
  /* function exit code */
  __pyx_r = Py_None; __Pyx_INCREF(Py_None);
  goto __pyx_L0;
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_t_1);
  __Pyx_XDECREF(__pyx_t_2);
  __Pyx_XDECREF(__pyx_t_3);
  __Pyx_AddTraceback("Cython.Compiler.Scanning.SourceDescriptor.set_file_type_from_name", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_r = NULL;
  __pyx_L0:;
  __Pyx_XDECREF(__pyx_v_ext);
  __Pyx_XGIVEREF(__pyx_r);
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}
/* … */
  __pyx_t_6 = __Pyx_PyDict_NewPresized(1); if (unlikely(!__pyx_t_6)) __PYX_ERR(0, 144, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_6);
  #if defined(PyDict_SetItem) && (defined(CYTHON_COMPILING_IN_CPYTHON))
  #if PY_VERSION_HEX >= 0x030A0000 /* CPython 3.10+ exposes KnownHash APIs */
  /* Use CPython's KnownHash APIs when available */
  extern int _PyDict_SetItem_KnownHash(PyObject*, PyObject*, PyObject*, Py_hash_t);
  {
    Py_hash_t __pyx_hash = PyObject_Hash(__pyx_mstate_global->__pyx_n_u_filename); if (unlikely(__pyx_hash == -1)) __PYX_ERR(0, 144, __pyx_L1_error);
    if (unlikely(_PyDict_SetItem_KnownHash(__pyx_t_6, __pyx_mstate_global->__pyx_n_u_filename, __pyx_mstate_global->__pyx_n_u_str, __pyx_hash) < 0)) __PYX_ERR(0, 144, __pyx_L1_error);
  }
  #else
  if (PyDict_SetItem(__pyx_t_6, __pyx_mstate_global->__pyx_n_u_filename, __pyx_mstate_global->__pyx_n_u_str) < (0)) __PYX_ERR(0, 144, __pyx_L1_error)
  #endif
  #else
  if (PyDict_SetItem(__pyx_t_6, __pyx_mstate_global->__pyx_n_u_filename, __pyx_mstate_global->__pyx_n_u_str) < (0)) __PYX_ERR(0, 144, __pyx_L1_error)
  #endif
  __pyx_t_2 = __Pyx_CyFunction_New(&__pyx_mdef_6Cython_8Compiler_8Scanning_16SourceDescriptor_3set_file_type_from_name, 0, __pyx_mstate_global->__pyx_n_u_SourceDescriptor_set_file_type_f, NULL, __pyx_mstate_global->__pyx_n_u_Cython_Compiler_Scanning, __pyx_mstate_global->__pyx_d, ((PyObject *)__pyx_mstate_global->__pyx_codeobj_tab[10])); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 144, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  #if CYTHON_COMPILING_IN_CPYTHON && PY_VERSION_HEX >= 0x030E0000
  PyUnstable_Object_EnableDeferredRefcount(__pyx_t_2);
  #endif
  __Pyx_CyFunction_SetAnnotationsDict(__pyx_t_2, __pyx_t_6);
  __Pyx_DECREF(__pyx_t_6); __pyx_t_6 = 0;
  if (__Pyx_SetNameInClass(__pyx_t_4, __pyx_mstate_global->__pyx_n_u_set_file_type_from_name, __pyx_t_2) < (0)) __PYX_ERR(0, 144, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
```

</details>

L145  🟠  (score=9)
```python
        ext = Path(filename).suffix
```
<details><summary>Show generated C (score=9)</summary>

```c
  __pyx_t_2 = NULL;
  __Pyx_GetModuleGlobalName(__pyx_t_3, __pyx_mstate_global->__pyx_n_u_Path); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 145, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_3);
  __pyx_t_4 = 1;
  {
    PyObject *__pyx_callargs[2] = {__pyx_t_2, __pyx_v_filename};
    __pyx_t_1 = __Pyx_PyObject_FastCall((PyObject*)__pyx_t_3, __pyx_callargs+__pyx_t_4, (2-__pyx_t_4) | (__pyx_t_4*__Pyx_PY_VECTORCALL_ARGUMENTS_OFFSET));
    __Pyx_XDECREF(__pyx_t_2); __pyx_t_2 = 0;
    __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
    if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 145, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_1);
  }
  __pyx_t_3 = __Pyx_PyObject_GetAttrStr(__pyx_t_1, __pyx_mstate_global->__pyx_n_u_suffix); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 145, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_3);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __pyx_v_ext = __pyx_t_3;
  __pyx_t_3 = 0;
```

</details>

L146  🔴  (score=24)
```python
        self._file_type = ext in ('.pyx', '.pxd', '.py') and ext[1:] or 'pyx'
```
<details><summary>Show generated C (score=24)</summary>

```c
  __Pyx_INCREF(__pyx_v_ext);
  __pyx_t_1 = __pyx_v_ext;
  __pyx_t_6 = (__Pyx_PyUnicode_Equals(__pyx_t_1, __pyx_mstate_global->__pyx_kp_u_pyx, Py_EQ)); if (unlikely((__pyx_t_6 < 0))) __PYX_ERR(0, 146, __pyx_L1_error)
  if (!__pyx_t_6) {
  } else {
    __pyx_t_5 = __pyx_t_6;
    goto __pyx_L6_bool_binop_done;
  }
  __pyx_t_6 = (__Pyx_PyUnicode_Equals(__pyx_t_1, __pyx_mstate_global->__pyx_kp_u_pxd, Py_EQ)); if (unlikely((__pyx_t_6 < 0))) __PYX_ERR(0, 146, __pyx_L1_error)
  if (!__pyx_t_6) {
  } else {
    __pyx_t_5 = __pyx_t_6;
    goto __pyx_L6_bool_binop_done;
  }
  __pyx_t_6 = (__Pyx_PyUnicode_Equals(__pyx_t_1, __pyx_mstate_global->__pyx_kp_u_py, Py_EQ)); if (unlikely((__pyx_t_6 < 0))) __PYX_ERR(0, 146, __pyx_L1_error)
  __pyx_t_5 = __pyx_t_6;
  __pyx_L6_bool_binop_done:;
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __pyx_t_6 = __pyx_t_5;
  if (!__pyx_t_6) {
    goto __pyx_L4_next_or;
  } else {
  }
  __pyx_t_1 = __Pyx_PyObject_GetSlice(__pyx_v_ext, 1, 0, NULL, NULL, &__pyx_mstate_global->__pyx_slice[0], 1, 0, 0); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 146, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __pyx_t_6 = __Pyx_PyObject_IsTrue(__pyx_t_1); if (unlikely((__pyx_t_6 < 0))) __PYX_ERR(0, 146, __pyx_L1_error)
  if (!__pyx_t_6) {
    __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  } else {
    __Pyx_INCREF(__pyx_t_1);
    __pyx_t_3 = __pyx_t_1;
    __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
    goto __pyx_L3_bool_binop_done;
  }
  __pyx_L4_next_or:;
  __Pyx_INCREF(__pyx_mstate_global->__pyx_n_u_pyx_2);
  __pyx_t_3 = __pyx_mstate_global->__pyx_n_u_pyx_2;
  __pyx_L3_bool_binop_done:;
  if (__Pyx_PyObject_SetAttrStr(__pyx_v_self, __pyx_mstate_global->__pyx_n_u_file_type, __pyx_t_3) < (0)) __PYX_ERR(0, 146, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
/* … */
  __pyx_mstate_global->__pyx_slice[0] = PySlice_New(__pyx_mstate_global->__pyx_int_1, Py_None, Py_None); if (unlikely(!__pyx_mstate_global->__pyx_slice[0])) __PYX_ERR(0, 146, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_mstate_global->__pyx_slice[0]);
  __Pyx_GIVEREF(__pyx_mstate_global->__pyx_slice[0]);
```

</details>

L147  ⚪  (score=0)
```python
```
L148  🔴  (score=66)
```python
    def is_cython_file(self) -> bool:
```
<details><summary>Show generated C (score=66)</summary>

```c
/* Python wrapper */
static PyObject *__pyx_pw_6Cython_8Compiler_8Scanning_16SourceDescriptor_5is_cython_file(PyObject *__pyx_self, 
#if CYTHON_METH_FASTCALL
PyObject *const *__pyx_args, Py_ssize_t __pyx_nargs, PyObject *__pyx_kwds
#else
PyObject *__pyx_args, PyObject *__pyx_kwds
#endif
); /*proto*/
PyDoc_STRVAR(__pyx_doc_6Cython_8Compiler_8Scanning_16SourceDescriptor_4is_cython_file, "File: Cython/Compiler/Scanning.py (starting at line 148)");
static PyMethodDef __pyx_mdef_6Cython_8Compiler_8Scanning_16SourceDescriptor_5is_cython_file = {"is_cython_file", (PyCFunction)(void(*)(void))(__Pyx_PyCFunction_FastCallWithKeywords)__pyx_pw_6Cython_8Compiler_8Scanning_16SourceDescriptor_5is_cython_file, __Pyx_METH_FASTCALL|METH_KEYWORDS, __pyx_doc_6Cython_8Compiler_8Scanning_16SourceDescriptor_4is_cython_file};
static PyObject *__pyx_pw_6Cython_8Compiler_8Scanning_16SourceDescriptor_5is_cython_file(PyObject *__pyx_self, 
#if CYTHON_METH_FASTCALL
PyObject *const *__pyx_args, Py_ssize_t __pyx_nargs, PyObject *__pyx_kwds
#else
PyObject *__pyx_args, PyObject *__pyx_kwds
#endif
) {
  PyObject *__pyx_v_self = 0;
  #if !CYTHON_METH_FASTCALL
  CYTHON_UNUSED Py_ssize_t __pyx_nargs;
  #endif
  CYTHON_UNUSED PyObject *const *__pyx_kwvalues;
  PyObject *__pyx_r = 0;
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("is_cython_file (wrapper)", 0);
  #if !CYTHON_METH_FASTCALL
  #if CYTHON_ASSUME_SAFE_SIZE
  __pyx_nargs = PyTuple_GET_SIZE(__pyx_args);
  #else
  __pyx_nargs = PyTuple_Size(__pyx_args); if (unlikely(__pyx_nargs < 0)) return NULL;
  #endif
  #endif
  __pyx_kwvalues = __Pyx_KwValues_FASTCALL(__pyx_args, __pyx_nargs);
  {
    PyObject ** const __pyx_pyargnames[] = {&__pyx_mstate_global->__pyx_n_u_self,0};
  PyObject* values[1] = {0};
    const Py_ssize_t __pyx_kwds_len = (__pyx_kwds) ? __Pyx_NumKwargs_FASTCALL(__pyx_kwds) : 0;
    if (unlikely(__pyx_kwds_len) < 0) __PYX_ERR(0, 148, __pyx_L3_error)
    if (__pyx_kwds_len > 0) {
      switch (__pyx_nargs) {
        case  1:
        values[0] = __Pyx_ArgRef_FASTCALL(__pyx_args, 0);
        if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[0])) __PYX_ERR(0, 148, __pyx_L3_error)
        CYTHON_FALLTHROUGH;
        case  0: break;
        default: goto __pyx_L5_argtuple_error;
      }
      const Py_ssize_t kwd_pos_args = __pyx_nargs;
      if (__Pyx_ParseKeywords(__pyx_kwds, __pyx_kwvalues, __pyx_pyargnames, 0, values, kwd_pos_args, __pyx_kwds_len, "is_cython_file", 0) < (0)) __PYX_ERR(0, 148, __pyx_L3_error)
      for (Py_ssize_t i = __pyx_nargs; i < 1; i++) {
        if (unlikely(!values[i])) { __Pyx_RaiseArgtupleInvalid("is_cython_file", 1, 1, 1, i); __PYX_ERR(0, 148, __pyx_L3_error) }
      }
    } else if (unlikely(__pyx_nargs != 1)) {
      goto __pyx_L5_argtuple_error;
    } else {
      values[0] = __Pyx_ArgRef_FASTCALL(__pyx_args, 0);
      if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[0])) __PYX_ERR(0, 148, __pyx_L3_error)
    }
    __pyx_v_self = values[0];
  }
  goto __pyx_L6_skip;
  __pyx_L5_argtuple_error:;
  __Pyx_RaiseArgtupleInvalid("is_cython_file", 1, 1, 1, __pyx_nargs); __PYX_ERR(0, 148, __pyx_L3_error)
  __pyx_L6_skip:;
  goto __pyx_L4_argument_unpacking_done;
  __pyx_L3_error:;
  for (Py_ssize_t __pyx_temp=0; __pyx_temp < (Py_ssize_t)(sizeof(values)/sizeof(values[0])); ++__pyx_temp) {
    Py_XDECREF(values[__pyx_temp]);
  }
  __Pyx_AddTraceback("Cython.Compiler.Scanning.SourceDescriptor.is_cython_file", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __Pyx_RefNannyFinishContext();
  return NULL;
  __pyx_L4_argument_unpacking_done:;
  __pyx_r = __pyx_pf_6Cython_8Compiler_8Scanning_16SourceDescriptor_4is_cython_file(__pyx_self, __pyx_v_self);
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

static PyObject *__pyx_pf_6Cython_8Compiler_8Scanning_16SourceDescriptor_4is_cython_file(CYTHON_UNUSED PyObject *__pyx_self, PyObject *__pyx_v_self) {
  PyObject *__pyx_r = NULL;
/* … */
  /* function exit code */
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_t_1);
  __Pyx_AddTraceback("Cython.Compiler.Scanning.SourceDescriptor.is_cython_file", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_r = NULL;
  __pyx_L0:;
  __Pyx_XGIVEREF(__pyx_r);
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}
/* … */
  __pyx_t_2 = __Pyx_PyDict_NewPresized(1); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 148, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  #if defined(PyDict_SetItem) && (defined(CYTHON_COMPILING_IN_CPYTHON))
  #if PY_VERSION_HEX >= 0x030A0000 /* CPython 3.10+ exposes KnownHash APIs */
  /* Use CPython's KnownHash APIs when available */
  extern int _PyDict_SetItem_KnownHash(PyObject*, PyObject*, PyObject*, Py_hash_t);
  {
    Py_hash_t __pyx_hash = PyObject_Hash(__pyx_mstate_global->__pyx_n_u_return); if (unlikely(__pyx_hash == -1)) __PYX_ERR(0, 148, __pyx_L1_error);
    if (unlikely(_PyDict_SetItem_KnownHash(__pyx_t_2, __pyx_mstate_global->__pyx_n_u_return, __pyx_mstate_global->__pyx_n_u_bool, __pyx_hash) < 0)) __PYX_ERR(0, 148, __pyx_L1_error);
  }
  #else
  if (PyDict_SetItem(__pyx_t_2, __pyx_mstate_global->__pyx_n_u_return, __pyx_mstate_global->__pyx_n_u_bool) < (0)) __PYX_ERR(0, 148, __pyx_L1_error)
  #endif
  #else
  if (PyDict_SetItem(__pyx_t_2, __pyx_mstate_global->__pyx_n_u_return, __pyx_mstate_global->__pyx_n_u_bool) < (0)) __PYX_ERR(0, 148, __pyx_L1_error)
  #endif
  __pyx_t_6 = __Pyx_CyFunction_New(&__pyx_mdef_6Cython_8Compiler_8Scanning_16SourceDescriptor_5is_cython_file, 0, __pyx_mstate_global->__pyx_n_u_SourceDescriptor_is_cython_file, NULL, __pyx_mstate_global->__pyx_n_u_Cython_Compiler_Scanning, __pyx_mstate_global->__pyx_d, ((PyObject *)__pyx_mstate_global->__pyx_codeobj_tab[11])); if (unlikely(!__pyx_t_6)) __PYX_ERR(0, 148, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_6);
  #if CYTHON_COMPILING_IN_CPYTHON && PY_VERSION_HEX >= 0x030E0000
  PyUnstable_Object_EnableDeferredRefcount(__pyx_t_6);
  #endif
  __Pyx_CyFunction_SetAnnotationsDict(__pyx_t_6, __pyx_t_2);
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  if (__Pyx_SetNameInClass(__pyx_t_4, __pyx_mstate_global->__pyx_n_u_is_cython_file, __pyx_t_6) < (0)) __PYX_ERR(0, 148, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_6); __pyx_t_6 = 0;
```

</details>

L149  🔴  (score=10)
```python
        return self._file_type in ('pyx', 'pxd')
```
<details><summary>Show generated C (score=10)</summary>

```c
  __Pyx_XDECREF(__pyx_r);
  __pyx_t_1 = __Pyx_PyObject_GetAttrStr(__pyx_v_self, __pyx_mstate_global->__pyx_n_u_file_type); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 149, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __pyx_t_3 = (__Pyx_PyUnicode_Equals(__pyx_t_1, __pyx_mstate_global->__pyx_n_u_pyx_2, Py_EQ)); if (unlikely((__pyx_t_3 < 0))) __PYX_ERR(0, 149, __pyx_L1_error)
  if (!__pyx_t_3) {
  } else {
    __pyx_t_2 = __pyx_t_3;
    goto __pyx_L3_bool_binop_done;
  }
  __pyx_t_3 = (__Pyx_PyUnicode_Equals(__pyx_t_1, __pyx_mstate_global->__pyx_n_u_pxd_2, Py_EQ)); if (unlikely((__pyx_t_3 < 0))) __PYX_ERR(0, 149, __pyx_L1_error)
  __pyx_t_2 = __pyx_t_3;
  __pyx_L3_bool_binop_done:;
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __pyx_t_1 = __Pyx_PyBool_FromLong(__pyx_t_2); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 149, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __pyx_r = __pyx_t_1;
  __pyx_t_1 = 0;
  goto __pyx_L0;
```

</details>

L150  ⚪  (score=0)
```python
```
L151  🔴  (score=67)
```python
    def is_python_file(self) -> bool:
```
<details><summary>Show generated C (score=67)</summary>

```c
/* Python wrapper */
static PyObject *__pyx_pw_6Cython_8Compiler_8Scanning_16SourceDescriptor_7is_python_file(PyObject *__pyx_self, 
#if CYTHON_METH_FASTCALL
PyObject *const *__pyx_args, Py_ssize_t __pyx_nargs, PyObject *__pyx_kwds
#else
PyObject *__pyx_args, PyObject *__pyx_kwds
#endif
); /*proto*/
PyDoc_STRVAR(__pyx_doc_6Cython_8Compiler_8Scanning_16SourceDescriptor_6is_python_file, "File: Cython/Compiler/Scanning.py (starting at line 151)");
static PyMethodDef __pyx_mdef_6Cython_8Compiler_8Scanning_16SourceDescriptor_7is_python_file = {"is_python_file", (PyCFunction)(void(*)(void))(__Pyx_PyCFunction_FastCallWithKeywords)__pyx_pw_6Cython_8Compiler_8Scanning_16SourceDescriptor_7is_python_file, __Pyx_METH_FASTCALL|METH_KEYWORDS, __pyx_doc_6Cython_8Compiler_8Scanning_16SourceDescriptor_6is_python_file};
static PyObject *__pyx_pw_6Cython_8Compiler_8Scanning_16SourceDescriptor_7is_python_file(PyObject *__pyx_self, 
#if CYTHON_METH_FASTCALL
PyObject *const *__pyx_args, Py_ssize_t __pyx_nargs, PyObject *__pyx_kwds
#else
PyObject *__pyx_args, PyObject *__pyx_kwds
#endif
) {
  PyObject *__pyx_v_self = 0;
  #if !CYTHON_METH_FASTCALL
  CYTHON_UNUSED Py_ssize_t __pyx_nargs;
  #endif
  CYTHON_UNUSED PyObject *const *__pyx_kwvalues;
  PyObject *__pyx_r = 0;
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("is_python_file (wrapper)", 0);
  #if !CYTHON_METH_FASTCALL
  #if CYTHON_ASSUME_SAFE_SIZE
  __pyx_nargs = PyTuple_GET_SIZE(__pyx_args);
  #else
  __pyx_nargs = PyTuple_Size(__pyx_args); if (unlikely(__pyx_nargs < 0)) return NULL;
  #endif
  #endif
  __pyx_kwvalues = __Pyx_KwValues_FASTCALL(__pyx_args, __pyx_nargs);
  {
    PyObject ** const __pyx_pyargnames[] = {&__pyx_mstate_global->__pyx_n_u_self,0};
  PyObject* values[1] = {0};
    const Py_ssize_t __pyx_kwds_len = (__pyx_kwds) ? __Pyx_NumKwargs_FASTCALL(__pyx_kwds) : 0;
    if (unlikely(__pyx_kwds_len) < 0) __PYX_ERR(0, 151, __pyx_L3_error)
    if (__pyx_kwds_len > 0) {
      switch (__pyx_nargs) {
        case  1:
        values[0] = __Pyx_ArgRef_FASTCALL(__pyx_args, 0);
        if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[0])) __PYX_ERR(0, 151, __pyx_L3_error)
        CYTHON_FALLTHROUGH;
        case  0: break;
        default: goto __pyx_L5_argtuple_error;
      }
      const Py_ssize_t kwd_pos_args = __pyx_nargs;
      if (__Pyx_ParseKeywords(__pyx_kwds, __pyx_kwvalues, __pyx_pyargnames, 0, values, kwd_pos_args, __pyx_kwds_len, "is_python_file", 0) < (0)) __PYX_ERR(0, 151, __pyx_L3_error)
      for (Py_ssize_t i = __pyx_nargs; i < 1; i++) {
        if (unlikely(!values[i])) { __Pyx_RaiseArgtupleInvalid("is_python_file", 1, 1, 1, i); __PYX_ERR(0, 151, __pyx_L3_error) }
      }
    } else if (unlikely(__pyx_nargs != 1)) {
      goto __pyx_L5_argtuple_error;
    } else {
      values[0] = __Pyx_ArgRef_FASTCALL(__pyx_args, 0);
      if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[0])) __PYX_ERR(0, 151, __pyx_L3_error)
    }
    __pyx_v_self = values[0];
  }
  goto __pyx_L6_skip;
  __pyx_L5_argtuple_error:;
  __Pyx_RaiseArgtupleInvalid("is_python_file", 1, 1, 1, __pyx_nargs); __PYX_ERR(0, 151, __pyx_L3_error)
  __pyx_L6_skip:;
  goto __pyx_L4_argument_unpacking_done;
  __pyx_L3_error:;
  for (Py_ssize_t __pyx_temp=0; __pyx_temp < (Py_ssize_t)(sizeof(values)/sizeof(values[0])); ++__pyx_temp) {
    Py_XDECREF(values[__pyx_temp]);
  }
  __Pyx_AddTraceback("Cython.Compiler.Scanning.SourceDescriptor.is_python_file", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __Pyx_RefNannyFinishContext();
  return NULL;
  __pyx_L4_argument_unpacking_done:;
  __pyx_r = __pyx_pf_6Cython_8Compiler_8Scanning_16SourceDescriptor_6is_python_file(__pyx_self, __pyx_v_self);
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

static PyObject *__pyx_pf_6Cython_8Compiler_8Scanning_16SourceDescriptor_6is_python_file(CYTHON_UNUSED PyObject *__pyx_self, PyObject *__pyx_v_self) {
  PyObject *__pyx_r = NULL;
/* … */
  /* function exit code */
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_t_1);
  __Pyx_XDECREF(__pyx_t_2);
  __Pyx_AddTraceback("Cython.Compiler.Scanning.SourceDescriptor.is_python_file", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_r = NULL;
  __pyx_L0:;
  __Pyx_XGIVEREF(__pyx_r);
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}
/* … */
  __pyx_t_6 = __Pyx_PyDict_NewPresized(1); if (unlikely(!__pyx_t_6)) __PYX_ERR(0, 151, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_6);
  #if defined(PyDict_SetItem) && (defined(CYTHON_COMPILING_IN_CPYTHON))
  #if PY_VERSION_HEX >= 0x030A0000 /* CPython 3.10+ exposes KnownHash APIs */
  /* Use CPython's KnownHash APIs when available */
  extern int _PyDict_SetItem_KnownHash(PyObject*, PyObject*, PyObject*, Py_hash_t);
  {
    Py_hash_t __pyx_hash = PyObject_Hash(__pyx_mstate_global->__pyx_n_u_return); if (unlikely(__pyx_hash == -1)) __PYX_ERR(0, 151, __pyx_L1_error);
    if (unlikely(_PyDict_SetItem_KnownHash(__pyx_t_6, __pyx_mstate_global->__pyx_n_u_return, __pyx_mstate_global->__pyx_n_u_bool, __pyx_hash) < 0)) __PYX_ERR(0, 151, __pyx_L1_error);
  }
  #else
  if (PyDict_SetItem(__pyx_t_6, __pyx_mstate_global->__pyx_n_u_return, __pyx_mstate_global->__pyx_n_u_bool) < (0)) __PYX_ERR(0, 151, __pyx_L1_error)
  #endif
  #else
  if (PyDict_SetItem(__pyx_t_6, __pyx_mstate_global->__pyx_n_u_return, __pyx_mstate_global->__pyx_n_u_bool) < (0)) __PYX_ERR(0, 151, __pyx_L1_error)
  #endif
  __pyx_t_2 = __Pyx_CyFunction_New(&__pyx_mdef_6Cython_8Compiler_8Scanning_16SourceDescriptor_7is_python_file, 0, __pyx_mstate_global->__pyx_n_u_SourceDescriptor_is_python_file, NULL, __pyx_mstate_global->__pyx_n_u_Cython_Compiler_Scanning, __pyx_mstate_global->__pyx_d, ((PyObject *)__pyx_mstate_global->__pyx_codeobj_tab[12])); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 151, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  #if CYTHON_COMPILING_IN_CPYTHON && PY_VERSION_HEX >= 0x030E0000
  PyUnstable_Object_EnableDeferredRefcount(__pyx_t_2);
  #endif
  __Pyx_CyFunction_SetAnnotationsDict(__pyx_t_2, __pyx_t_6);
  __Pyx_DECREF(__pyx_t_6); __pyx_t_6 = 0;
  if (__Pyx_SetNameInClass(__pyx_t_4, __pyx_mstate_global->__pyx_n_u_is_python_file, __pyx_t_2) < (0)) __PYX_ERR(0, 151, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
```

</details>

L152  🟠  (score=9)
```python
        return self._file_type == 'py'
```
<details><summary>Show generated C (score=9)</summary>

```c
  __Pyx_XDECREF(__pyx_r);
  __pyx_t_1 = __Pyx_PyObject_GetAttrStr(__pyx_v_self, __pyx_mstate_global->__pyx_n_u_file_type); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 152, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __pyx_t_2 = PyObject_RichCompare(__pyx_t_1, __pyx_mstate_global->__pyx_n_u_py_2, Py_EQ); __Pyx_XGOTREF(__pyx_t_2); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 152, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __pyx_r = __pyx_t_2;
  __pyx_t_2 = 0;
  goto __pyx_L0;
```

</details>

L153  ⚪  (score=0)
```python
```
L154  🔴  (score=67)
```python
    def get_escaped_description(self) -> str:
```
<details><summary>Show generated C (score=67)</summary>

```c
/* Python wrapper */
static PyObject *__pyx_pw_6Cython_8Compiler_8Scanning_16SourceDescriptor_9get_escaped_description(PyObject *__pyx_self, 
#if CYTHON_METH_FASTCALL
PyObject *const *__pyx_args, Py_ssize_t __pyx_nargs, PyObject *__pyx_kwds
#else
PyObject *__pyx_args, PyObject *__pyx_kwds
#endif
); /*proto*/
PyDoc_STRVAR(__pyx_doc_6Cython_8Compiler_8Scanning_16SourceDescriptor_8get_escaped_description, "File: Cython/Compiler/Scanning.py (starting at line 154)");
static PyMethodDef __pyx_mdef_6Cython_8Compiler_8Scanning_16SourceDescriptor_9get_escaped_description = {"get_escaped_description", (PyCFunction)(void(*)(void))(__Pyx_PyCFunction_FastCallWithKeywords)__pyx_pw_6Cython_8Compiler_8Scanning_16SourceDescriptor_9get_escaped_description, __Pyx_METH_FASTCALL|METH_KEYWORDS, __pyx_doc_6Cython_8Compiler_8Scanning_16SourceDescriptor_8get_escaped_description};
static PyObject *__pyx_pw_6Cython_8Compiler_8Scanning_16SourceDescriptor_9get_escaped_description(PyObject *__pyx_self, 
#if CYTHON_METH_FASTCALL
PyObject *const *__pyx_args, Py_ssize_t __pyx_nargs, PyObject *__pyx_kwds
#else
PyObject *__pyx_args, PyObject *__pyx_kwds
#endif
) {
  PyObject *__pyx_v_self = 0;
  #if !CYTHON_METH_FASTCALL
  CYTHON_UNUSED Py_ssize_t __pyx_nargs;
  #endif
  CYTHON_UNUSED PyObject *const *__pyx_kwvalues;
  PyObject *__pyx_r = 0;
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("get_escaped_description (wrapper)", 0);
  #if !CYTHON_METH_FASTCALL
  #if CYTHON_ASSUME_SAFE_SIZE
  __pyx_nargs = PyTuple_GET_SIZE(__pyx_args);
  #else
  __pyx_nargs = PyTuple_Size(__pyx_args); if (unlikely(__pyx_nargs < 0)) return NULL;
  #endif
  #endif
  __pyx_kwvalues = __Pyx_KwValues_FASTCALL(__pyx_args, __pyx_nargs);
  {
    PyObject ** const __pyx_pyargnames[] = {&__pyx_mstate_global->__pyx_n_u_self,0};
  PyObject* values[1] = {0};
    const Py_ssize_t __pyx_kwds_len = (__pyx_kwds) ? __Pyx_NumKwargs_FASTCALL(__pyx_kwds) : 0;
    if (unlikely(__pyx_kwds_len) < 0) __PYX_ERR(0, 154, __pyx_L3_error)
    if (__pyx_kwds_len > 0) {
      switch (__pyx_nargs) {
        case  1:
        values[0] = __Pyx_ArgRef_FASTCALL(__pyx_args, 0);
        if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[0])) __PYX_ERR(0, 154, __pyx_L3_error)
        CYTHON_FALLTHROUGH;
        case  0: break;
        default: goto __pyx_L5_argtuple_error;
      }
      const Py_ssize_t kwd_pos_args = __pyx_nargs;
      if (__Pyx_ParseKeywords(__pyx_kwds, __pyx_kwvalues, __pyx_pyargnames, 0, values, kwd_pos_args, __pyx_kwds_len, "get_escaped_description", 0) < (0)) __PYX_ERR(0, 154, __pyx_L3_error)
      for (Py_ssize_t i = __pyx_nargs; i < 1; i++) {
        if (unlikely(!values[i])) { __Pyx_RaiseArgtupleInvalid("get_escaped_description", 1, 1, 1, i); __PYX_ERR(0, 154, __pyx_L3_error) }
      }
    } else if (unlikely(__pyx_nargs != 1)) {
      goto __pyx_L5_argtuple_error;
    } else {
      values[0] = __Pyx_ArgRef_FASTCALL(__pyx_args, 0);
      if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[0])) __PYX_ERR(0, 154, __pyx_L3_error)
    }
    __pyx_v_self = values[0];
  }
  goto __pyx_L6_skip;
  __pyx_L5_argtuple_error:;
  __Pyx_RaiseArgtupleInvalid("get_escaped_description", 1, 1, 1, __pyx_nargs); __PYX_ERR(0, 154, __pyx_L3_error)
  __pyx_L6_skip:;
  goto __pyx_L4_argument_unpacking_done;
  __pyx_L3_error:;
  for (Py_ssize_t __pyx_temp=0; __pyx_temp < (Py_ssize_t)(sizeof(values)/sizeof(values[0])); ++__pyx_temp) {
    Py_XDECREF(values[__pyx_temp]);
  }
  __Pyx_AddTraceback("Cython.Compiler.Scanning.SourceDescriptor.get_escaped_description", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __Pyx_RefNannyFinishContext();
  return NULL;
  __pyx_L4_argument_unpacking_done:;
  __pyx_r = __pyx_pf_6Cython_8Compiler_8Scanning_16SourceDescriptor_8get_escaped_description(__pyx_self, __pyx_v_self);
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

static PyObject *__pyx_pf_6Cython_8Compiler_8Scanning_16SourceDescriptor_8get_escaped_description(CYTHON_UNUSED PyObject *__pyx_self, PyObject *__pyx_v_self) {
  PyObject *__pyx_r = NULL;
/* … */
  /* function exit code */
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_t_1);
  __Pyx_XDECREF(__pyx_t_3);
  __Pyx_AddTraceback("Cython.Compiler.Scanning.SourceDescriptor.get_escaped_description", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_r = NULL;
  __pyx_L0:;
  __Pyx_XGIVEREF(__pyx_r);
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}
/* … */
  __pyx_t_2 = __Pyx_PyDict_NewPresized(1); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 154, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  #if defined(PyDict_SetItem) && (defined(CYTHON_COMPILING_IN_CPYTHON))
  #if PY_VERSION_HEX >= 0x030A0000 /* CPython 3.10+ exposes KnownHash APIs */
  /* Use CPython's KnownHash APIs when available */
  extern int _PyDict_SetItem_KnownHash(PyObject*, PyObject*, PyObject*, Py_hash_t);
  {
    Py_hash_t __pyx_hash = PyObject_Hash(__pyx_mstate_global->__pyx_n_u_return); if (unlikely(__pyx_hash == -1)) __PYX_ERR(0, 154, __pyx_L1_error);
    if (unlikely(_PyDict_SetItem_KnownHash(__pyx_t_2, __pyx_mstate_global->__pyx_n_u_return, __pyx_mstate_global->__pyx_n_u_str, __pyx_hash) < 0)) __PYX_ERR(0, 154, __pyx_L1_error);
  }
  #else
  if (PyDict_SetItem(__pyx_t_2, __pyx_mstate_global->__pyx_n_u_return, __pyx_mstate_global->__pyx_n_u_str) < (0)) __PYX_ERR(0, 154, __pyx_L1_error)
  #endif
  #else
  if (PyDict_SetItem(__pyx_t_2, __pyx_mstate_global->__pyx_n_u_return, __pyx_mstate_global->__pyx_n_u_str) < (0)) __PYX_ERR(0, 154, __pyx_L1_error)
  #endif
  __pyx_t_6 = __Pyx_CyFunction_New(&__pyx_mdef_6Cython_8Compiler_8Scanning_16SourceDescriptor_9get_escaped_description, 0, __pyx_mstate_global->__pyx_n_u_SourceDescriptor_get_escaped_des, NULL, __pyx_mstate_global->__pyx_n_u_Cython_Compiler_Scanning, __pyx_mstate_global->__pyx_d, ((PyObject *)__pyx_mstate_global->__pyx_codeobj_tab[13])); if (unlikely(!__pyx_t_6)) __PYX_ERR(0, 154, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_6);
  #if CYTHON_COMPILING_IN_CPYTHON && PY_VERSION_HEX >= 0x030E0000
  PyUnstable_Object_EnableDeferredRefcount(__pyx_t_6);
  #endif
  __Pyx_CyFunction_SetAnnotationsDict(__pyx_t_6, __pyx_t_2);
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  if (__Pyx_SetNameInClass(__pyx_t_4, __pyx_mstate_global->__pyx_n_u_get_escaped_description, __pyx_t_6) < (0)) __PYX_ERR(0, 154, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_6); __pyx_t_6 = 0;
```

</details>

L155  🟡  (score=3)
```python
        if self._escaped_description is None:
```
<details><summary>Show generated C (score=3)</summary>

```c
  __pyx_t_1 = __Pyx_PyObject_GetAttrStr(__pyx_v_self, __pyx_mstate_global->__pyx_n_u_escaped_description); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 155, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __pyx_t_2 = (__pyx_t_1 == Py_None);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  if (__pyx_t_2) {
/* … */
  }
```

</details>

L156  ⚪  (score=0)
```python
            # Use forward slashes on Windows since these paths
```
L157  ⚪  (score=0)
```python
            # will be used in the #line directives in the C/C++ files.
```
L158  🔴  (score=18)
```python
            self._escaped_description = self.get_description().replace('\\', '/')
```
<details><summary>Show generated C (score=18)</summary>

```c
    __pyx_t_3 = __pyx_v_self;
    __Pyx_INCREF(__pyx_t_3);
    __pyx_t_4 = 0;
    {
      PyObject *__pyx_callargs[2] = {__pyx_t_3, NULL};
      __pyx_t_1 = __Pyx_PyObject_FastCallMethod((PyObject*)__pyx_mstate_global->__pyx_n_u_get_description, __pyx_callargs+__pyx_t_4, (1-__pyx_t_4) | (1*__Pyx_PY_VECTORCALL_ARGUMENTS_OFFSET));
      __Pyx_XDECREF(__pyx_t_3); __pyx_t_3 = 0;
      if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 158, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_1);
    }
    __pyx_t_3 = __Pyx_PyObject_GetAttrStr(__pyx_t_1, __pyx_mstate_global->__pyx_n_u_replace); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 158, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_3);
    __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
    __pyx_t_1 = __Pyx_PyObject_Call(__pyx_t_3, __pyx_mstate_global->__pyx_tuple[2], NULL); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 158, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_1);
    __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
    if (__Pyx_PyObject_SetAttrStr(__pyx_v_self, __pyx_mstate_global->__pyx_n_u_escaped_description, __pyx_t_1) < (0)) __PYX_ERR(0, 158, __pyx_L1_error)
    __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
/* … */
  __pyx_mstate_global->__pyx_tuple[2] = PyTuple_Pack(2, __pyx_mstate_global->__pyx_kp_u__2, __pyx_mstate_global->__pyx_kp_u__3); if (unlikely(!__pyx_mstate_global->__pyx_tuple[2])) __PYX_ERR(0, 158, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_mstate_global->__pyx_tuple[2]);
  __Pyx_GIVEREF(__pyx_mstate_global->__pyx_tuple[2]);
```

</details>

L159  🔴  (score=10)
```python
        return self._escaped_description
```
<details><summary>Show generated C (score=10)</summary>

```c
  __Pyx_XDECREF(__pyx_r);
  __pyx_t_1 = __Pyx_PyObject_GetAttrStr(__pyx_v_self, __pyx_mstate_global->__pyx_n_u_escaped_description); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 159, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  if (!(likely(PyUnicode_CheckExact(__pyx_t_1))||((__pyx_t_1) == Py_None) || __Pyx_RaiseUnexpectedTypeError("str", __pyx_t_1))) __PYX_ERR(0, 159, __pyx_L1_error)
  __pyx_r = ((PyObject*)__pyx_t_1);
  __pyx_t_1 = 0;
  goto __pyx_L0;
```

</details>

L160  ⚪  (score=0)
```python
```
L161  🔴  (score=42)
```python
    def __gt__(self, other):
```
<details><summary>Show generated C (score=42)</summary>

```c
/* Python wrapper */
static PyObject *__pyx_pw_6Cython_8Compiler_8Scanning_16SourceDescriptor_11__gt__(PyObject *__pyx_self, 
#if CYTHON_METH_FASTCALL
PyObject *const *__pyx_args, Py_ssize_t __pyx_nargs, PyObject *__pyx_kwds
#else
PyObject *__pyx_args, PyObject *__pyx_kwds
#endif
); /*proto*/
PyDoc_STRVAR(__pyx_doc_6Cython_8Compiler_8Scanning_16SourceDescriptor_10__gt__, "File: Cython/Compiler/Scanning.py (starting at line 161)");
static PyMethodDef __pyx_mdef_6Cython_8Compiler_8Scanning_16SourceDescriptor_11__gt__ = {"__gt__", (PyCFunction)(void(*)(void))(__Pyx_PyCFunction_FastCallWithKeywords)__pyx_pw_6Cython_8Compiler_8Scanning_16SourceDescriptor_11__gt__, __Pyx_METH_FASTCALL|METH_KEYWORDS, __pyx_doc_6Cython_8Compiler_8Scanning_16SourceDescriptor_10__gt__};
static PyObject *__pyx_pw_6Cython_8Compiler_8Scanning_16SourceDescriptor_11__gt__(PyObject *__pyx_self, 
#if CYTHON_METH_FASTCALL
PyObject *const *__pyx_args, Py_ssize_t __pyx_nargs, PyObject *__pyx_kwds
#else
PyObject *__pyx_args, PyObject *__pyx_kwds
#endif
) {
  PyObject *__pyx_v_self = 0;
  PyObject *__pyx_v_other = 0;
  #if !CYTHON_METH_FASTCALL
  CYTHON_UNUSED Py_ssize_t __pyx_nargs;
  #endif
  CYTHON_UNUSED PyObject *const *__pyx_kwvalues;
  PyObject *__pyx_r = 0;
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("__gt__ (wrapper)", 0);
  #if !CYTHON_METH_FASTCALL
  #if CYTHON_ASSUME_SAFE_SIZE
  __pyx_nargs = PyTuple_GET_SIZE(__pyx_args);
  #else
  __pyx_nargs = PyTuple_Size(__pyx_args); if (unlikely(__pyx_nargs < 0)) return NULL;
  #endif
  #endif
  __pyx_kwvalues = __Pyx_KwValues_FASTCALL(__pyx_args, __pyx_nargs);
  {
    PyObject ** const __pyx_pyargnames[] = {&__pyx_mstate_global->__pyx_n_u_self,&__pyx_mstate_global->__pyx_n_u_other,0};
  PyObject* values[2] = {0,0};
    const Py_ssize_t __pyx_kwds_len = (__pyx_kwds) ? __Pyx_NumKwargs_FASTCALL(__pyx_kwds) : 0;
    if (unlikely(__pyx_kwds_len) < 0) __PYX_ERR(0, 161, __pyx_L3_error)
    if (__pyx_kwds_len > 0) {
      switch (__pyx_nargs) {
        case  2:
        values[1] = __Pyx_ArgRef_FASTCALL(__pyx_args, 1);
        if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[1])) __PYX_ERR(0, 161, __pyx_L3_error)
        CYTHON_FALLTHROUGH;
        case  1:
        values[0] = __Pyx_ArgRef_FASTCALL(__pyx_args, 0);
        if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[0])) __PYX_ERR(0, 161, __pyx_L3_error)
        CYTHON_FALLTHROUGH;
        case  0: break;
        default: goto __pyx_L5_argtuple_error;
      }
      const Py_ssize_t kwd_pos_args = __pyx_nargs;
      if (__Pyx_ParseKeywords(__pyx_kwds, __pyx_kwvalues, __pyx_pyargnames, 0, values, kwd_pos_args, __pyx_kwds_len, "__gt__", 0) < (0)) __PYX_ERR(0, 161, __pyx_L3_error)
      for (Py_ssize_t i = __pyx_nargs; i < 2; i++) {
        if (unlikely(!values[i])) { __Pyx_RaiseArgtupleInvalid("__gt__", 1, 2, 2, i); __PYX_ERR(0, 161, __pyx_L3_error) }
      }
    } else if (unlikely(__pyx_nargs != 2)) {
      goto __pyx_L5_argtuple_error;
    } else {
      values[0] = __Pyx_ArgRef_FASTCALL(__pyx_args, 0);
      if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[0])) __PYX_ERR(0, 161, __pyx_L3_error)
      values[1] = __Pyx_ArgRef_FASTCALL(__pyx_args, 1);
      if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[1])) __PYX_ERR(0, 161, __pyx_L3_error)
    }
    __pyx_v_self = values[0];
    __pyx_v_other = values[1];
  }
  goto __pyx_L6_skip;
  __pyx_L5_argtuple_error:;
  __Pyx_RaiseArgtupleInvalid("__gt__", 1, 2, 2, __pyx_nargs); __PYX_ERR(0, 161, __pyx_L3_error)
  __pyx_L6_skip:;
  goto __pyx_L4_argument_unpacking_done;
  __pyx_L3_error:;
  for (Py_ssize_t __pyx_temp=0; __pyx_temp < (Py_ssize_t)(sizeof(values)/sizeof(values[0])); ++__pyx_temp) {
    Py_XDECREF(values[__pyx_temp]);
  }
  __Pyx_AddTraceback("Cython.Compiler.Scanning.SourceDescriptor.__gt__", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __Pyx_RefNannyFinishContext();
  return NULL;
  __pyx_L4_argument_unpacking_done:;
  __pyx_r = __pyx_pf_6Cython_8Compiler_8Scanning_16SourceDescriptor_10__gt__(__pyx_self, __pyx_v_self, __pyx_v_other);
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

static PyObject *__pyx_pf_6Cython_8Compiler_8Scanning_16SourceDescriptor_10__gt__(CYTHON_UNUSED PyObject *__pyx_self, PyObject *__pyx_v_self, PyObject *__pyx_v_other) {
  PyObject *__pyx_r = NULL;
/* … */
  /* function exit code */
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_t_4);
  __Pyx_XDECREF(__pyx_t_5);
  __Pyx_XDECREF(__pyx_t_6);
  __Pyx_AddTraceback("Cython.Compiler.Scanning.SourceDescriptor.__gt__", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_r = NULL;
  __pyx_L0:;
  __Pyx_XGIVEREF(__pyx_r);
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}
/* … */
  __pyx_t_6 = __Pyx_CyFunction_New(&__pyx_mdef_6Cython_8Compiler_8Scanning_16SourceDescriptor_11__gt__, 0, __pyx_mstate_global->__pyx_n_u_SourceDescriptor___gt, NULL, __pyx_mstate_global->__pyx_n_u_Cython_Compiler_Scanning, __pyx_mstate_global->__pyx_d, ((PyObject *)__pyx_mstate_global->__pyx_codeobj_tab[14])); if (unlikely(!__pyx_t_6)) __PYX_ERR(0, 161, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_6);
  #if CYTHON_COMPILING_IN_CPYTHON && PY_VERSION_HEX >= 0x030E0000
  PyUnstable_Object_EnableDeferredRefcount(__pyx_t_6);
  #endif
  if (__Pyx_SetNameInClass(__pyx_t_4, __pyx_mstate_global->__pyx_n_u_gt, __pyx_t_6) < (0)) __PYX_ERR(0, 161, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_6); __pyx_t_6 = 0;
```

</details>

L162  ⚪  (score=0)
```python
        # this is only used to provide some sort of order
```
L163  🟠  (score=9)
```python
        try:
```
<details><summary>Show generated C (score=9)</summary>

```c
  {
    /*try:*/ {
/* … */
    }
    __pyx_L3_error:;
    __Pyx_XDECREF(__pyx_t_4); __pyx_t_4 = 0;
    __Pyx_XDECREF(__pyx_t_5); __pyx_t_5 = 0;
    __Pyx_XDECREF(__pyx_t_6); __pyx_t_6 = 0;
/* … */
    __pyx_L5_except_error:;
    __Pyx_XGIVEREF(__pyx_t_1);
    __Pyx_XGIVEREF(__pyx_t_2);
    __Pyx_XGIVEREF(__pyx_t_3);
    __Pyx_ExceptionReset(__pyx_t_1, __pyx_t_2, __pyx_t_3);
    goto __pyx_L1_error;
    __pyx_L7_try_return:;
    __Pyx_XGIVEREF(__pyx_t_1);
    __Pyx_XGIVEREF(__pyx_t_2);
    __Pyx_XGIVEREF(__pyx_t_3);
    __Pyx_ExceptionReset(__pyx_t_1, __pyx_t_2, __pyx_t_3);
    goto __pyx_L0;
    __pyx_L6_except_return:;
    __Pyx_XGIVEREF(__pyx_t_1);
    __Pyx_XGIVEREF(__pyx_t_2);
    __Pyx_XGIVEREF(__pyx_t_3);
    __Pyx_ExceptionReset(__pyx_t_1, __pyx_t_2, __pyx_t_3);
    goto __pyx_L0;
  }
```

</details>

L164  🔴  (score=12)
```python
            return self._cmp_name > other._cmp_name
```
<details><summary>Show generated C (score=12)</summary>

```c
      __Pyx_XDECREF(__pyx_r);
      __pyx_t_4 = __Pyx_PyObject_GetAttrStr(__pyx_v_self, __pyx_mstate_global->__pyx_n_u_cmp_name); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 164, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_4);
      __pyx_t_5 = __Pyx_PyObject_GetAttrStr(__pyx_v_other, __pyx_mstate_global->__pyx_n_u_cmp_name); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 164, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_5);
      __pyx_t_6 = PyObject_RichCompare(__pyx_t_4, __pyx_t_5, Py_GT); __Pyx_XGOTREF(__pyx_t_6); if (unlikely(!__pyx_t_6)) __PYX_ERR(0, 164, __pyx_L3_error)
      __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
      __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
      __pyx_r = __pyx_t_6;
      __pyx_t_6 = 0;
      goto __pyx_L7_try_return;
```

</details>

L165  🟡  (score=4)
```python
        except AttributeError:
```
<details><summary>Show generated C (score=4)</summary>

```c
    __pyx_t_7 = __Pyx_PyErr_ExceptionMatches(((PyObject *)(((PyTypeObject*)PyExc_AttributeError))));
    if (__pyx_t_7) {
      __Pyx_ErrRestore(0,0,0);
```

</details>

L166  🟡  (score=2)
```python
            return False
```
<details><summary>Show generated C (score=2)</summary>

```c
      __Pyx_XDECREF(__pyx_r);
      __Pyx_INCREF(Py_False);
      __pyx_r = Py_False;
      goto __pyx_L6_except_return;
    }
    goto __pyx_L5_except_error;
```

</details>

L167  ⚪  (score=0)
```python
```
L168  🔴  (score=42)
```python
    def __lt__(self, other):
```
<details><summary>Show generated C (score=42)</summary>

```c
/* Python wrapper */
static PyObject *__pyx_pw_6Cython_8Compiler_8Scanning_16SourceDescriptor_13__lt__(PyObject *__pyx_self, 
#if CYTHON_METH_FASTCALL
PyObject *const *__pyx_args, Py_ssize_t __pyx_nargs, PyObject *__pyx_kwds
#else
PyObject *__pyx_args, PyObject *__pyx_kwds
#endif
); /*proto*/
PyDoc_STRVAR(__pyx_doc_6Cython_8Compiler_8Scanning_16SourceDescriptor_12__lt__, "File: Cython/Compiler/Scanning.py (starting at line 168)");
static PyMethodDef __pyx_mdef_6Cython_8Compiler_8Scanning_16SourceDescriptor_13__lt__ = {"__lt__", (PyCFunction)(void(*)(void))(__Pyx_PyCFunction_FastCallWithKeywords)__pyx_pw_6Cython_8Compiler_8Scanning_16SourceDescriptor_13__lt__, __Pyx_METH_FASTCALL|METH_KEYWORDS, __pyx_doc_6Cython_8Compiler_8Scanning_16SourceDescriptor_12__lt__};
static PyObject *__pyx_pw_6Cython_8Compiler_8Scanning_16SourceDescriptor_13__lt__(PyObject *__pyx_self, 
#if CYTHON_METH_FASTCALL
PyObject *const *__pyx_args, Py_ssize_t __pyx_nargs, PyObject *__pyx_kwds
#else
PyObject *__pyx_args, PyObject *__pyx_kwds
#endif
) {
  PyObject *__pyx_v_self = 0;
  PyObject *__pyx_v_other = 0;
  #if !CYTHON_METH_FASTCALL
  CYTHON_UNUSED Py_ssize_t __pyx_nargs;
  #endif
  CYTHON_UNUSED PyObject *const *__pyx_kwvalues;
  PyObject *__pyx_r = 0;
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("__lt__ (wrapper)", 0);
  #if !CYTHON_METH_FASTCALL
  #if CYTHON_ASSUME_SAFE_SIZE
  __pyx_nargs = PyTuple_GET_SIZE(__pyx_args);
  #else
  __pyx_nargs = PyTuple_Size(__pyx_args); if (unlikely(__pyx_nargs < 0)) return NULL;
  #endif
  #endif
  __pyx_kwvalues = __Pyx_KwValues_FASTCALL(__pyx_args, __pyx_nargs);
  {
    PyObject ** const __pyx_pyargnames[] = {&__pyx_mstate_global->__pyx_n_u_self,&__pyx_mstate_global->__pyx_n_u_other,0};
  PyObject* values[2] = {0,0};
    const Py_ssize_t __pyx_kwds_len = (__pyx_kwds) ? __Pyx_NumKwargs_FASTCALL(__pyx_kwds) : 0;
    if (unlikely(__pyx_kwds_len) < 0) __PYX_ERR(0, 168, __pyx_L3_error)
    if (__pyx_kwds_len > 0) {
      switch (__pyx_nargs) {
        case  2:
        values[1] = __Pyx_ArgRef_FASTCALL(__pyx_args, 1);
        if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[1])) __PYX_ERR(0, 168, __pyx_L3_error)
        CYTHON_FALLTHROUGH;
        case  1:
        values[0] = __Pyx_ArgRef_FASTCALL(__pyx_args, 0);
        if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[0])) __PYX_ERR(0, 168, __pyx_L3_error)
        CYTHON_FALLTHROUGH;
        case  0: break;
        default: goto __pyx_L5_argtuple_error;
      }
      const Py_ssize_t kwd_pos_args = __pyx_nargs;
      if (__Pyx_ParseKeywords(__pyx_kwds, __pyx_kwvalues, __pyx_pyargnames, 0, values, kwd_pos_args, __pyx_kwds_len, "__lt__", 0) < (0)) __PYX_ERR(0, 168, __pyx_L3_error)
      for (Py_ssize_t i = __pyx_nargs; i < 2; i++) {
        if (unlikely(!values[i])) { __Pyx_RaiseArgtupleInvalid("__lt__", 1, 2, 2, i); __PYX_ERR(0, 168, __pyx_L3_error) }
      }
    } else if (unlikely(__pyx_nargs != 2)) {
      goto __pyx_L5_argtuple_error;
    } else {
      values[0] = __Pyx_ArgRef_FASTCALL(__pyx_args, 0);
      if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[0])) __PYX_ERR(0, 168, __pyx_L3_error)
      values[1] = __Pyx_ArgRef_FASTCALL(__pyx_args, 1);
      if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[1])) __PYX_ERR(0, 168, __pyx_L3_error)
    }
    __pyx_v_self = values[0];
    __pyx_v_other = values[1];
  }
  goto __pyx_L6_skip;
  __pyx_L5_argtuple_error:;
  __Pyx_RaiseArgtupleInvalid("__lt__", 1, 2, 2, __pyx_nargs); __PYX_ERR(0, 168, __pyx_L3_error)
  __pyx_L6_skip:;
  goto __pyx_L4_argument_unpacking_done;
  __pyx_L3_error:;
  for (Py_ssize_t __pyx_temp=0; __pyx_temp < (Py_ssize_t)(sizeof(values)/sizeof(values[0])); ++__pyx_temp) {
    Py_XDECREF(values[__pyx_temp]);
  }
  __Pyx_AddTraceback("Cython.Compiler.Scanning.SourceDescriptor.__lt__", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __Pyx_RefNannyFinishContext();
  return NULL;
  __pyx_L4_argument_unpacking_done:;
  __pyx_r = __pyx_pf_6Cython_8Compiler_8Scanning_16SourceDescriptor_12__lt__(__pyx_self, __pyx_v_self, __pyx_v_other);
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

static PyObject *__pyx_pf_6Cython_8Compiler_8Scanning_16SourceDescriptor_12__lt__(CYTHON_UNUSED PyObject *__pyx_self, PyObject *__pyx_v_self, PyObject *__pyx_v_other) {
  PyObject *__pyx_r = NULL;
/* … */
  /* function exit code */
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_t_4);
  __Pyx_XDECREF(__pyx_t_5);
  __Pyx_XDECREF(__pyx_t_6);
  __Pyx_AddTraceback("Cython.Compiler.Scanning.SourceDescriptor.__lt__", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_r = NULL;
  __pyx_L0:;
  __Pyx_XGIVEREF(__pyx_r);
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}
/* … */
  __pyx_t_6 = __Pyx_CyFunction_New(&__pyx_mdef_6Cython_8Compiler_8Scanning_16SourceDescriptor_13__lt__, 0, __pyx_mstate_global->__pyx_n_u_SourceDescriptor___lt, NULL, __pyx_mstate_global->__pyx_n_u_Cython_Compiler_Scanning, __pyx_mstate_global->__pyx_d, ((PyObject *)__pyx_mstate_global->__pyx_codeobj_tab[15])); if (unlikely(!__pyx_t_6)) __PYX_ERR(0, 168, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_6);
  #if CYTHON_COMPILING_IN_CPYTHON && PY_VERSION_HEX >= 0x030E0000
  PyUnstable_Object_EnableDeferredRefcount(__pyx_t_6);
  #endif
  if (__Pyx_SetNameInClass(__pyx_t_4, __pyx_mstate_global->__pyx_n_u_lt, __pyx_t_6) < (0)) __PYX_ERR(0, 168, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_6); __pyx_t_6 = 0;
```

</details>

L169  ⚪  (score=0)
```python
        # this is only used to provide some sort of order
```
L170  🟠  (score=9)
```python
        try:
```
<details><summary>Show generated C (score=9)</summary>

```c
  {
    /*try:*/ {
/* … */
    }
    __pyx_L3_error:;
    __Pyx_XDECREF(__pyx_t_4); __pyx_t_4 = 0;
    __Pyx_XDECREF(__pyx_t_5); __pyx_t_5 = 0;
    __Pyx_XDECREF(__pyx_t_6); __pyx_t_6 = 0;
/* … */
    __pyx_L5_except_error:;
    __Pyx_XGIVEREF(__pyx_t_1);
    __Pyx_XGIVEREF(__pyx_t_2);
    __Pyx_XGIVEREF(__pyx_t_3);
    __Pyx_ExceptionReset(__pyx_t_1, __pyx_t_2, __pyx_t_3);
    goto __pyx_L1_error;
    __pyx_L7_try_return:;
    __Pyx_XGIVEREF(__pyx_t_1);
    __Pyx_XGIVEREF(__pyx_t_2);
    __Pyx_XGIVEREF(__pyx_t_3);
    __Pyx_ExceptionReset(__pyx_t_1, __pyx_t_2, __pyx_t_3);
    goto __pyx_L0;
    __pyx_L6_except_return:;
    __Pyx_XGIVEREF(__pyx_t_1);
    __Pyx_XGIVEREF(__pyx_t_2);
    __Pyx_XGIVEREF(__pyx_t_3);
    __Pyx_ExceptionReset(__pyx_t_1, __pyx_t_2, __pyx_t_3);
    goto __pyx_L0;
  }
```

</details>

L171  🔴  (score=12)
```python
            return self._cmp_name < other._cmp_name
```
<details><summary>Show generated C (score=12)</summary>

```c
      __Pyx_XDECREF(__pyx_r);
      __pyx_t_4 = __Pyx_PyObject_GetAttrStr(__pyx_v_self, __pyx_mstate_global->__pyx_n_u_cmp_name); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 171, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_4);
      __pyx_t_5 = __Pyx_PyObject_GetAttrStr(__pyx_v_other, __pyx_mstate_global->__pyx_n_u_cmp_name); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 171, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_5);
      __pyx_t_6 = PyObject_RichCompare(__pyx_t_4, __pyx_t_5, Py_LT); __Pyx_XGOTREF(__pyx_t_6); if (unlikely(!__pyx_t_6)) __PYX_ERR(0, 171, __pyx_L3_error)
      __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
      __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
      __pyx_r = __pyx_t_6;
      __pyx_t_6 = 0;
      goto __pyx_L7_try_return;
```

</details>

L172  🟡  (score=4)
```python
        except AttributeError:
```
<details><summary>Show generated C (score=4)</summary>

```c
    __pyx_t_7 = __Pyx_PyErr_ExceptionMatches(((PyObject *)(((PyTypeObject*)PyExc_AttributeError))));
    if (__pyx_t_7) {
      __Pyx_ErrRestore(0,0,0);
```

</details>

L173  🟡  (score=2)
```python
            return False
```
<details><summary>Show generated C (score=2)</summary>

```c
      __Pyx_XDECREF(__pyx_r);
      __Pyx_INCREF(Py_False);
      __pyx_r = Py_False;
      goto __pyx_L6_except_return;
    }
    goto __pyx_L5_except_error;
```

</details>

L174  ⚪  (score=0)
```python
```
L175  🔴  (score=42)
```python
    def __le__(self, other):
```
<details><summary>Show generated C (score=42)</summary>

```c
/* Python wrapper */
static PyObject *__pyx_pw_6Cython_8Compiler_8Scanning_16SourceDescriptor_15__le__(PyObject *__pyx_self, 
#if CYTHON_METH_FASTCALL
PyObject *const *__pyx_args, Py_ssize_t __pyx_nargs, PyObject *__pyx_kwds
#else
PyObject *__pyx_args, PyObject *__pyx_kwds
#endif
); /*proto*/
PyDoc_STRVAR(__pyx_doc_6Cython_8Compiler_8Scanning_16SourceDescriptor_14__le__, "File: Cython/Compiler/Scanning.py (starting at line 175)");
static PyMethodDef __pyx_mdef_6Cython_8Compiler_8Scanning_16SourceDescriptor_15__le__ = {"__le__", (PyCFunction)(void(*)(void))(__Pyx_PyCFunction_FastCallWithKeywords)__pyx_pw_6Cython_8Compiler_8Scanning_16SourceDescriptor_15__le__, __Pyx_METH_FASTCALL|METH_KEYWORDS, __pyx_doc_6Cython_8Compiler_8Scanning_16SourceDescriptor_14__le__};
static PyObject *__pyx_pw_6Cython_8Compiler_8Scanning_16SourceDescriptor_15__le__(PyObject *__pyx_self, 
#if CYTHON_METH_FASTCALL
PyObject *const *__pyx_args, Py_ssize_t __pyx_nargs, PyObject *__pyx_kwds
#else
PyObject *__pyx_args, PyObject *__pyx_kwds
#endif
) {
  PyObject *__pyx_v_self = 0;
  PyObject *__pyx_v_other = 0;
  #if !CYTHON_METH_FASTCALL
  CYTHON_UNUSED Py_ssize_t __pyx_nargs;
  #endif
  CYTHON_UNUSED PyObject *const *__pyx_kwvalues;
  PyObject *__pyx_r = 0;
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("__le__ (wrapper)", 0);
  #if !CYTHON_METH_FASTCALL
  #if CYTHON_ASSUME_SAFE_SIZE
  __pyx_nargs = PyTuple_GET_SIZE(__pyx_args);
  #else
  __pyx_nargs = PyTuple_Size(__pyx_args); if (unlikely(__pyx_nargs < 0)) return NULL;
  #endif
  #endif
  __pyx_kwvalues = __Pyx_KwValues_FASTCALL(__pyx_args, __pyx_nargs);
  {
    PyObject ** const __pyx_pyargnames[] = {&__pyx_mstate_global->__pyx_n_u_self,&__pyx_mstate_global->__pyx_n_u_other,0};
  PyObject* values[2] = {0,0};
    const Py_ssize_t __pyx_kwds_len = (__pyx_kwds) ? __Pyx_NumKwargs_FASTCALL(__pyx_kwds) : 0;
    if (unlikely(__pyx_kwds_len) < 0) __PYX_ERR(0, 175, __pyx_L3_error)
    if (__pyx_kwds_len > 0) {
      switch (__pyx_nargs) {
        case  2:
        values[1] = __Pyx_ArgRef_FASTCALL(__pyx_args, 1);
        if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[1])) __PYX_ERR(0, 175, __pyx_L3_error)
        CYTHON_FALLTHROUGH;
        case  1:
        values[0] = __Pyx_ArgRef_FASTCALL(__pyx_args, 0);
        if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[0])) __PYX_ERR(0, 175, __pyx_L3_error)
        CYTHON_FALLTHROUGH;
        case  0: break;
        default: goto __pyx_L5_argtuple_error;
      }
      const Py_ssize_t kwd_pos_args = __pyx_nargs;
      if (__Pyx_ParseKeywords(__pyx_kwds, __pyx_kwvalues, __pyx_pyargnames, 0, values, kwd_pos_args, __pyx_kwds_len, "__le__", 0) < (0)) __PYX_ERR(0, 175, __pyx_L3_error)
      for (Py_ssize_t i = __pyx_nargs; i < 2; i++) {
        if (unlikely(!values[i])) { __Pyx_RaiseArgtupleInvalid("__le__", 1, 2, 2, i); __PYX_ERR(0, 175, __pyx_L3_error) }
      }
    } else if (unlikely(__pyx_nargs != 2)) {
      goto __pyx_L5_argtuple_error;
    } else {
      values[0] = __Pyx_ArgRef_FASTCALL(__pyx_args, 0);
      if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[0])) __PYX_ERR(0, 175, __pyx_L3_error)
      values[1] = __Pyx_ArgRef_FASTCALL(__pyx_args, 1);
      if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[1])) __PYX_ERR(0, 175, __pyx_L3_error)
    }
    __pyx_v_self = values[0];
    __pyx_v_other = values[1];
  }
  goto __pyx_L6_skip;
  __pyx_L5_argtuple_error:;
  __Pyx_RaiseArgtupleInvalid("__le__", 1, 2, 2, __pyx_nargs); __PYX_ERR(0, 175, __pyx_L3_error)
  __pyx_L6_skip:;
  goto __pyx_L4_argument_unpacking_done;
  __pyx_L3_error:;
  for (Py_ssize_t __pyx_temp=0; __pyx_temp < (Py_ssize_t)(sizeof(values)/sizeof(values[0])); ++__pyx_temp) {
    Py_XDECREF(values[__pyx_temp]);
  }
  __Pyx_AddTraceback("Cython.Compiler.Scanning.SourceDescriptor.__le__", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __Pyx_RefNannyFinishContext();
  return NULL;
  __pyx_L4_argument_unpacking_done:;
  __pyx_r = __pyx_pf_6Cython_8Compiler_8Scanning_16SourceDescriptor_14__le__(__pyx_self, __pyx_v_self, __pyx_v_other);
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

static PyObject *__pyx_pf_6Cython_8Compiler_8Scanning_16SourceDescriptor_14__le__(CYTHON_UNUSED PyObject *__pyx_self, PyObject *__pyx_v_self, PyObject *__pyx_v_other) {
  PyObject *__pyx_r = NULL;
/* … */
  /* function exit code */
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_t_4);
  __Pyx_XDECREF(__pyx_t_5);
  __Pyx_XDECREF(__pyx_t_6);
  __Pyx_AddTraceback("Cython.Compiler.Scanning.SourceDescriptor.__le__", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_r = NULL;
  __pyx_L0:;
  __Pyx_XGIVEREF(__pyx_r);
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}
/* … */
  __pyx_t_6 = __Pyx_CyFunction_New(&__pyx_mdef_6Cython_8Compiler_8Scanning_16SourceDescriptor_15__le__, 0, __pyx_mstate_global->__pyx_n_u_SourceDescriptor___le, NULL, __pyx_mstate_global->__pyx_n_u_Cython_Compiler_Scanning, __pyx_mstate_global->__pyx_d, ((PyObject *)__pyx_mstate_global->__pyx_codeobj_tab[16])); if (unlikely(!__pyx_t_6)) __PYX_ERR(0, 175, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_6);
  #if CYTHON_COMPILING_IN_CPYTHON && PY_VERSION_HEX >= 0x030E0000
  PyUnstable_Object_EnableDeferredRefcount(__pyx_t_6);
  #endif
  if (__Pyx_SetNameInClass(__pyx_t_4, __pyx_mstate_global->__pyx_n_u_le, __pyx_t_6) < (0)) __PYX_ERR(0, 175, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_6); __pyx_t_6 = 0;
```

</details>

L176  ⚪  (score=0)
```python
        # this is only used to provide some sort of order
```
L177  🟠  (score=9)
```python
        try:
```
<details><summary>Show generated C (score=9)</summary>

```c
  {
    /*try:*/ {
/* … */
    }
    __pyx_L3_error:;
    __Pyx_XDECREF(__pyx_t_4); __pyx_t_4 = 0;
    __Pyx_XDECREF(__pyx_t_5); __pyx_t_5 = 0;
    __Pyx_XDECREF(__pyx_t_6); __pyx_t_6 = 0;
/* … */
    __pyx_L5_except_error:;
    __Pyx_XGIVEREF(__pyx_t_1);
    __Pyx_XGIVEREF(__pyx_t_2);
    __Pyx_XGIVEREF(__pyx_t_3);
    __Pyx_ExceptionReset(__pyx_t_1, __pyx_t_2, __pyx_t_3);
    goto __pyx_L1_error;
    __pyx_L7_try_return:;
    __Pyx_XGIVEREF(__pyx_t_1);
    __Pyx_XGIVEREF(__pyx_t_2);
    __Pyx_XGIVEREF(__pyx_t_3);
    __Pyx_ExceptionReset(__pyx_t_1, __pyx_t_2, __pyx_t_3);
    goto __pyx_L0;
    __pyx_L6_except_return:;
    __Pyx_XGIVEREF(__pyx_t_1);
    __Pyx_XGIVEREF(__pyx_t_2);
    __Pyx_XGIVEREF(__pyx_t_3);
    __Pyx_ExceptionReset(__pyx_t_1, __pyx_t_2, __pyx_t_3);
    goto __pyx_L0;
  }
```

</details>

L178  🔴  (score=12)
```python
            return self._cmp_name <= other._cmp_name
```
<details><summary>Show generated C (score=12)</summary>

```c
      __Pyx_XDECREF(__pyx_r);
      __pyx_t_4 = __Pyx_PyObject_GetAttrStr(__pyx_v_self, __pyx_mstate_global->__pyx_n_u_cmp_name); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 178, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_4);
      __pyx_t_5 = __Pyx_PyObject_GetAttrStr(__pyx_v_other, __pyx_mstate_global->__pyx_n_u_cmp_name); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 178, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_5);
      __pyx_t_6 = PyObject_RichCompare(__pyx_t_4, __pyx_t_5, Py_LE); __Pyx_XGOTREF(__pyx_t_6); if (unlikely(!__pyx_t_6)) __PYX_ERR(0, 178, __pyx_L3_error)
      __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
      __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
      __pyx_r = __pyx_t_6;
      __pyx_t_6 = 0;
      goto __pyx_L7_try_return;
```

</details>

L179  🟡  (score=4)
```python
        except AttributeError:
```
<details><summary>Show generated C (score=4)</summary>

```c
    __pyx_t_7 = __Pyx_PyErr_ExceptionMatches(((PyObject *)(((PyTypeObject*)PyExc_AttributeError))));
    if (__pyx_t_7) {
      __Pyx_ErrRestore(0,0,0);
```

</details>

L180  🟡  (score=2)
```python
            return False
```
<details><summary>Show generated C (score=2)</summary>

```c
      __Pyx_XDECREF(__pyx_r);
      __Pyx_INCREF(Py_False);
      __pyx_r = Py_False;
      goto __pyx_L6_except_return;
    }
    goto __pyx_L5_except_error;
```

</details>

L181  ⚪  (score=0)
```python
```
L182  🔴  (score=33)
```python
    def __copy__(self):
```
<details><summary>Show generated C (score=33)</summary>

```c
/* Python wrapper */
static PyObject *__pyx_pw_6Cython_8Compiler_8Scanning_16SourceDescriptor_17__copy__(PyObject *__pyx_self, 
#if CYTHON_METH_FASTCALL
PyObject *const *__pyx_args, Py_ssize_t __pyx_nargs, PyObject *__pyx_kwds
#else
PyObject *__pyx_args, PyObject *__pyx_kwds
#endif
); /*proto*/
PyDoc_STRVAR(__pyx_doc_6Cython_8Compiler_8Scanning_16SourceDescriptor_16__copy__, "File: Cython/Compiler/Scanning.py (starting at line 182)");
static PyMethodDef __pyx_mdef_6Cython_8Compiler_8Scanning_16SourceDescriptor_17__copy__ = {"__copy__", (PyCFunction)(void(*)(void))(__Pyx_PyCFunction_FastCallWithKeywords)__pyx_pw_6Cython_8Compiler_8Scanning_16SourceDescriptor_17__copy__, __Pyx_METH_FASTCALL|METH_KEYWORDS, __pyx_doc_6Cython_8Compiler_8Scanning_16SourceDescriptor_16__copy__};
static PyObject *__pyx_pw_6Cython_8Compiler_8Scanning_16SourceDescriptor_17__copy__(PyObject *__pyx_self, 
#if CYTHON_METH_FASTCALL
PyObject *const *__pyx_args, Py_ssize_t __pyx_nargs, PyObject *__pyx_kwds
#else
PyObject *__pyx_args, PyObject *__pyx_kwds
#endif
) {
  PyObject *__pyx_v_self = 0;
  #if !CYTHON_METH_FASTCALL
  CYTHON_UNUSED Py_ssize_t __pyx_nargs;
  #endif
  CYTHON_UNUSED PyObject *const *__pyx_kwvalues;
  PyObject *__pyx_r = 0;
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("__copy__ (wrapper)", 0);
  #if !CYTHON_METH_FASTCALL
  #if CYTHON_ASSUME_SAFE_SIZE
  __pyx_nargs = PyTuple_GET_SIZE(__pyx_args);
  #else
  __pyx_nargs = PyTuple_Size(__pyx_args); if (unlikely(__pyx_nargs < 0)) return NULL;
  #endif
  #endif
  __pyx_kwvalues = __Pyx_KwValues_FASTCALL(__pyx_args, __pyx_nargs);
  {
    PyObject ** const __pyx_pyargnames[] = {&__pyx_mstate_global->__pyx_n_u_self,0};
  PyObject* values[1] = {0};
    const Py_ssize_t __pyx_kwds_len = (__pyx_kwds) ? __Pyx_NumKwargs_FASTCALL(__pyx_kwds) : 0;
    if (unlikely(__pyx_kwds_len) < 0) __PYX_ERR(0, 182, __pyx_L3_error)
    if (__pyx_kwds_len > 0) {
      switch (__pyx_nargs) {
        case  1:
        values[0] = __Pyx_ArgRef_FASTCALL(__pyx_args, 0);
        if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[0])) __PYX_ERR(0, 182, __pyx_L3_error)
        CYTHON_FALLTHROUGH;
        case  0: break;
        default: goto __pyx_L5_argtuple_error;
      }
      const Py_ssize_t kwd_pos_args = __pyx_nargs;
      if (__Pyx_ParseKeywords(__pyx_kwds, __pyx_kwvalues, __pyx_pyargnames, 0, values, kwd_pos_args, __pyx_kwds_len, "__copy__", 0) < (0)) __PYX_ERR(0, 182, __pyx_L3_error)
      for (Py_ssize_t i = __pyx_nargs; i < 1; i++) {
        if (unlikely(!values[i])) { __Pyx_RaiseArgtupleInvalid("__copy__", 1, 1, 1, i); __PYX_ERR(0, 182, __pyx_L3_error) }
      }
    } else if (unlikely(__pyx_nargs != 1)) {
      goto __pyx_L5_argtuple_error;
    } else {
      values[0] = __Pyx_ArgRef_FASTCALL(__pyx_args, 0);
      if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[0])) __PYX_ERR(0, 182, __pyx_L3_error)
    }
    __pyx_v_self = values[0];
  }
  goto __pyx_L6_skip;
  __pyx_L5_argtuple_error:;
  __Pyx_RaiseArgtupleInvalid("__copy__", 1, 1, 1, __pyx_nargs); __PYX_ERR(0, 182, __pyx_L3_error)
  __pyx_L6_skip:;
  goto __pyx_L4_argument_unpacking_done;
  __pyx_L3_error:;
  for (Py_ssize_t __pyx_temp=0; __pyx_temp < (Py_ssize_t)(sizeof(values)/sizeof(values[0])); ++__pyx_temp) {
    Py_XDECREF(values[__pyx_temp]);
  }
  __Pyx_AddTraceback("Cython.Compiler.Scanning.SourceDescriptor.__copy__", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __Pyx_RefNannyFinishContext();
  return NULL;
  __pyx_L4_argument_unpacking_done:;
  __pyx_r = __pyx_pf_6Cython_8Compiler_8Scanning_16SourceDescriptor_16__copy__(__pyx_self, __pyx_v_self);
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

static PyObject *__pyx_pf_6Cython_8Compiler_8Scanning_16SourceDescriptor_16__copy__(CYTHON_UNUSED PyObject *__pyx_self, PyObject *__pyx_v_self) {
  PyObject *__pyx_r = NULL;
/* … */
  /* function exit code */
  __pyx_L0:;
  __Pyx_XGIVEREF(__pyx_r);
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}
/* … */
  __pyx_t_6 = __Pyx_CyFunction_New(&__pyx_mdef_6Cython_8Compiler_8Scanning_16SourceDescriptor_17__copy__, 0, __pyx_mstate_global->__pyx_n_u_SourceDescriptor___copy, NULL, __pyx_mstate_global->__pyx_n_u_Cython_Compiler_Scanning, __pyx_mstate_global->__pyx_d, ((PyObject *)__pyx_mstate_global->__pyx_codeobj_tab[17])); if (unlikely(!__pyx_t_6)) __PYX_ERR(0, 182, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_6);
  #if CYTHON_COMPILING_IN_CPYTHON && PY_VERSION_HEX >= 0x030E0000
  PyUnstable_Object_EnableDeferredRefcount(__pyx_t_6);
  #endif
  if (__Pyx_SetNameInClass(__pyx_t_4, __pyx_mstate_global->__pyx_n_u_copy, __pyx_t_6) < (0)) __PYX_ERR(0, 182, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_6); __pyx_t_6 = 0;
```

</details>

L183  🟡  (score=2)
```python
        return self  # immutable, no need to copy
```
<details><summary>Show generated C (score=2)</summary>

```c
  __Pyx_XDECREF(__pyx_r);
  __Pyx_INCREF(__pyx_v_self);
  __pyx_r = __pyx_v_self;
  goto __pyx_L0;
```

</details>

L184  ⚪  (score=0)
```python
```
L185  🔴  (score=37)
```python
    def __deepcopy__(self, memo):
```
<details><summary>Show generated C (score=37)</summary>

```c
/* Python wrapper */
static PyObject *__pyx_pw_6Cython_8Compiler_8Scanning_16SourceDescriptor_19__deepcopy__(PyObject *__pyx_self, 
#if CYTHON_METH_FASTCALL
PyObject *const *__pyx_args, Py_ssize_t __pyx_nargs, PyObject *__pyx_kwds
#else
PyObject *__pyx_args, PyObject *__pyx_kwds
#endif
); /*proto*/
PyDoc_STRVAR(__pyx_doc_6Cython_8Compiler_8Scanning_16SourceDescriptor_18__deepcopy__, "File: Cython/Compiler/Scanning.py (starting at line 185)");
static PyMethodDef __pyx_mdef_6Cython_8Compiler_8Scanning_16SourceDescriptor_19__deepcopy__ = {"__deepcopy__", (PyCFunction)(void(*)(void))(__Pyx_PyCFunction_FastCallWithKeywords)__pyx_pw_6Cython_8Compiler_8Scanning_16SourceDescriptor_19__deepcopy__, __Pyx_METH_FASTCALL|METH_KEYWORDS, __pyx_doc_6Cython_8Compiler_8Scanning_16SourceDescriptor_18__deepcopy__};
static PyObject *__pyx_pw_6Cython_8Compiler_8Scanning_16SourceDescriptor_19__deepcopy__(PyObject *__pyx_self, 
#if CYTHON_METH_FASTCALL
PyObject *const *__pyx_args, Py_ssize_t __pyx_nargs, PyObject *__pyx_kwds
#else
PyObject *__pyx_args, PyObject *__pyx_kwds
#endif
) {
  PyObject *__pyx_v_self = 0;
  CYTHON_UNUSED PyObject *__pyx_v_memo = 0;
  #if !CYTHON_METH_FASTCALL
  CYTHON_UNUSED Py_ssize_t __pyx_nargs;
  #endif
  CYTHON_UNUSED PyObject *const *__pyx_kwvalues;
  PyObject *__pyx_r = 0;
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("__deepcopy__ (wrapper)", 0);
  #if !CYTHON_METH_FASTCALL
  #if CYTHON_ASSUME_SAFE_SIZE
  __pyx_nargs = PyTuple_GET_SIZE(__pyx_args);
  #else
  __pyx_nargs = PyTuple_Size(__pyx_args); if (unlikely(__pyx_nargs < 0)) return NULL;
  #endif
  #endif
  __pyx_kwvalues = __Pyx_KwValues_FASTCALL(__pyx_args, __pyx_nargs);
  {
    PyObject ** const __pyx_pyargnames[] = {&__pyx_mstate_global->__pyx_n_u_self,&__pyx_mstate_global->__pyx_n_u_memo,0};
  PyObject* values[2] = {0,0};
    const Py_ssize_t __pyx_kwds_len = (__pyx_kwds) ? __Pyx_NumKwargs_FASTCALL(__pyx_kwds) : 0;
    if (unlikely(__pyx_kwds_len) < 0) __PYX_ERR(0, 185, __pyx_L3_error)
    if (__pyx_kwds_len > 0) {
      switch (__pyx_nargs) {
        case  2:
        values[1] = __Pyx_ArgRef_FASTCALL(__pyx_args, 1);
        if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[1])) __PYX_ERR(0, 185, __pyx_L3_error)
        CYTHON_FALLTHROUGH;
        case  1:
        values[0] = __Pyx_ArgRef_FASTCALL(__pyx_args, 0);
        if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[0])) __PYX_ERR(0, 185, __pyx_L3_error)
        CYTHON_FALLTHROUGH;
        case  0: break;
        default: goto __pyx_L5_argtuple_error;
      }
      const Py_ssize_t kwd_pos_args = __pyx_nargs;
      if (__Pyx_ParseKeywords(__pyx_kwds, __pyx_kwvalues, __pyx_pyargnames, 0, values, kwd_pos_args, __pyx_kwds_len, "__deepcopy__", 0) < (0)) __PYX_ERR(0, 185, __pyx_L3_error)
      for (Py_ssize_t i = __pyx_nargs; i < 2; i++) {
        if (unlikely(!values[i])) { __Pyx_RaiseArgtupleInvalid("__deepcopy__", 1, 2, 2, i); __PYX_ERR(0, 185, __pyx_L3_error) }
      }
    } else if (unlikely(__pyx_nargs != 2)) {
      goto __pyx_L5_argtuple_error;
    } else {
      values[0] = __Pyx_ArgRef_FASTCALL(__pyx_args, 0);
      if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[0])) __PYX_ERR(0, 185, __pyx_L3_error)
      values[1] = __Pyx_ArgRef_FASTCALL(__pyx_args, 1);
      if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[1])) __PYX_ERR(0, 185, __pyx_L3_error)
    }
    __pyx_v_self = values[0];
    __pyx_v_memo = values[1];
  }
  goto __pyx_L6_skip;
  __pyx_L5_argtuple_error:;
  __Pyx_RaiseArgtupleInvalid("__deepcopy__", 1, 2, 2, __pyx_nargs); __PYX_ERR(0, 185, __pyx_L3_error)
  __pyx_L6_skip:;
  goto __pyx_L4_argument_unpacking_done;
  __pyx_L3_error:;
  for (Py_ssize_t __pyx_temp=0; __pyx_temp < (Py_ssize_t)(sizeof(values)/sizeof(values[0])); ++__pyx_temp) {
    Py_XDECREF(values[__pyx_temp]);
  }
  __Pyx_AddTraceback("Cython.Compiler.Scanning.SourceDescriptor.__deepcopy__", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __Pyx_RefNannyFinishContext();
  return NULL;
  __pyx_L4_argument_unpacking_done:;
  __pyx_r = __pyx_pf_6Cython_8Compiler_8Scanning_16SourceDescriptor_18__deepcopy__(__pyx_self, __pyx_v_self, __pyx_v_memo);
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

static PyObject *__pyx_pf_6Cython_8Compiler_8Scanning_16SourceDescriptor_18__deepcopy__(CYTHON_UNUSED PyObject *__pyx_self, PyObject *__pyx_v_self, CYTHON_UNUSED PyObject *__pyx_v_memo) {
  PyObject *__pyx_r = NULL;
/* … */
  /* function exit code */
  __pyx_L0:;
  __Pyx_XGIVEREF(__pyx_r);
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}
/* … */
  __pyx_t_6 = __Pyx_CyFunction_New(&__pyx_mdef_6Cython_8Compiler_8Scanning_16SourceDescriptor_19__deepcopy__, 0, __pyx_mstate_global->__pyx_n_u_SourceDescriptor___deepcopy, NULL, __pyx_mstate_global->__pyx_n_u_Cython_Compiler_Scanning, __pyx_mstate_global->__pyx_d, ((PyObject *)__pyx_mstate_global->__pyx_codeobj_tab[18])); if (unlikely(!__pyx_t_6)) __PYX_ERR(0, 185, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_6);
  #if CYTHON_COMPILING_IN_CPYTHON && PY_VERSION_HEX >= 0x030E0000
  PyUnstable_Object_EnableDeferredRefcount(__pyx_t_6);
  #endif
  if (__Pyx_SetNameInClass(__pyx_t_4, __pyx_mstate_global->__pyx_n_u_deepcopy, __pyx_t_6) < (0)) __PYX_ERR(0, 185, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_6); __pyx_t_6 = 0;
```

</details>

L186  🟡  (score=2)
```python
        return self  # immutable, no need to copy
```
<details><summary>Show generated C (score=2)</summary>

```c
  __Pyx_XDECREF(__pyx_r);
  __Pyx_INCREF(__pyx_v_self);
  __pyx_r = __pyx_v_self;
  goto __pyx_L0;
```

</details>

L187  ⚪  (score=0)
```python
```
L188  ⚪  (score=0)
```python
```
L189  🔴  (score=30)
```python
class FileSourceDescriptor(SourceDescriptor):
```
<details><summary>Show generated C (score=30)</summary>

```c
  __Pyx_GetModuleGlobalName(__pyx_t_4, __pyx_mstate_global->__pyx_n_u_SourceDescriptor); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 189, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_4);
  __pyx_t_6 = PyTuple_Pack(1, __pyx_t_4); if (unlikely(!__pyx_t_6)) __PYX_ERR(0, 189, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_6);
  __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
  __pyx_t_4 = __Pyx_PEP560_update_bases(__pyx_t_6); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 189, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_4);
  __pyx_t_2 = __Pyx_CalculateMetaclass(NULL, __pyx_t_4); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 189, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __pyx_t_7 = __Pyx_Py3MetaclassPrepare(__pyx_t_2, __pyx_t_4, __pyx_mstate_global->__pyx_n_u_FileSourceDescriptor, __pyx_mstate_global->__pyx_n_u_FileSourceDescriptor, (PyObject *) NULL, __pyx_mstate_global->__pyx_n_u_Cython_Compiler_Scanning, __pyx_mstate_global->__pyx_kp_u_File_Cython_Compiler_Scanning_py_3); if (unlikely(!__pyx_t_7)) __PYX_ERR(0, 189, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_7);
  if (__pyx_t_4 != __pyx_t_6) {
    if (unlikely((PyDict_SetItemString(__pyx_t_7, "__orig_bases__", __pyx_t_6) < 0))) __PYX_ERR(0, 189, __pyx_L1_error)
  }
  __Pyx_DECREF(__pyx_t_6); __pyx_t_6 = 0;
/* … */
  __pyx_t_6 = __Pyx_Py3ClassCreate(__pyx_t_2, __pyx_mstate_global->__pyx_n_u_FileSourceDescriptor, __pyx_t_4, __pyx_t_7, NULL, 0, 0); if (unlikely(!__pyx_t_6)) __PYX_ERR(0, 189, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_6);
  #if CYTHON_COMPILING_IN_CPYTHON && PY_VERSION_HEX >= 0x030E0000
  PyUnstable_Object_EnableDeferredRefcount(__pyx_t_6);
  #endif
  if (PyDict_SetItem(__pyx_mstate_global->__pyx_d, __pyx_mstate_global->__pyx_n_u_FileSourceDescriptor, __pyx_t_6) < (0)) __PYX_ERR(0, 189, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_6); __pyx_t_6 = 0;
  __Pyx_DECREF(__pyx_t_7); __pyx_t_7 = 0;
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
```

</details>

L190  ⚪  (score=0)
```python
    """
```
L191  ⚪  (score=0)
```python
    Represents a code source. A code source is a more generic abstraction
```
L192  ⚪  (score=0)
```python
    for a "filename" (as sometimes the code doesn't come from a file).
```
L193  ⚪  (score=0)
```python
    Instances of code sources are passed to Scanner.__init__ as the
```
L194  ⚪  (score=0)
```python
    optional name argument and will be passed back when asking for
```
L195  ⚪  (score=0)
```python
    the position()-tuple.
```
L196  ⚪  (score=0)
```python
    """
```
L197  🔴  (score=57)
```python
    def __init__(self, filename, path_description=None):
```
<details><summary>Show generated C (score=57)</summary>

```c
/* Python wrapper */
static PyObject *__pyx_pw_6Cython_8Compiler_8Scanning_20FileSourceDescriptor_1__init__(PyObject *__pyx_self, 
#if CYTHON_METH_FASTCALL
PyObject *const *__pyx_args, Py_ssize_t __pyx_nargs, PyObject *__pyx_kwds
#else
PyObject *__pyx_args, PyObject *__pyx_kwds
#endif
); /*proto*/
PyDoc_STRVAR(__pyx_doc_6Cython_8Compiler_8Scanning_20FileSourceDescriptor___init__, "File: Cython/Compiler/Scanning.py (starting at line 197)");
static PyMethodDef __pyx_mdef_6Cython_8Compiler_8Scanning_20FileSourceDescriptor_1__init__ = {"__init__", (PyCFunction)(void(*)(void))(__Pyx_PyCFunction_FastCallWithKeywords)__pyx_pw_6Cython_8Compiler_8Scanning_20FileSourceDescriptor_1__init__, __Pyx_METH_FASTCALL|METH_KEYWORDS, __pyx_doc_6Cython_8Compiler_8Scanning_20FileSourceDescriptor___init__};
static PyObject *__pyx_pw_6Cython_8Compiler_8Scanning_20FileSourceDescriptor_1__init__(PyObject *__pyx_self, 
#if CYTHON_METH_FASTCALL
PyObject *const *__pyx_args, Py_ssize_t __pyx_nargs, PyObject *__pyx_kwds
#else
PyObject *__pyx_args, PyObject *__pyx_kwds
#endif
) {
  PyObject *__pyx_v_self = 0;
  PyObject *__pyx_v_filename = 0;
  PyObject *__pyx_v_path_description = 0;
  #if !CYTHON_METH_FASTCALL
  CYTHON_UNUSED Py_ssize_t __pyx_nargs;
  #endif
  CYTHON_UNUSED PyObject *const *__pyx_kwvalues;
  PyObject *__pyx_r = 0;
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("__init__ (wrapper)", 0);
  #if !CYTHON_METH_FASTCALL
  #if CYTHON_ASSUME_SAFE_SIZE
  __pyx_nargs = PyTuple_GET_SIZE(__pyx_args);
  #else
  __pyx_nargs = PyTuple_Size(__pyx_args); if (unlikely(__pyx_nargs < 0)) return NULL;
  #endif
  #endif
  __pyx_kwvalues = __Pyx_KwValues_FASTCALL(__pyx_args, __pyx_nargs);
  {
    PyObject ** const __pyx_pyargnames[] = {&__pyx_mstate_global->__pyx_n_u_self,&__pyx_mstate_global->__pyx_n_u_filename,&__pyx_mstate_global->__pyx_n_u_path_description,0};
  PyObject* values[3] = {0,0,0};
    const Py_ssize_t __pyx_kwds_len = (__pyx_kwds) ? __Pyx_NumKwargs_FASTCALL(__pyx_kwds) : 0;
    if (unlikely(__pyx_kwds_len) < 0) __PYX_ERR(0, 197, __pyx_L3_error)
    if (__pyx_kwds_len > 0) {
      switch (__pyx_nargs) {
        case  3:
        values[2] = __Pyx_ArgRef_FASTCALL(__pyx_args, 2);
        if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[2])) __PYX_ERR(0, 197, __pyx_L3_error)
        CYTHON_FALLTHROUGH;
        case  2:
        values[1] = __Pyx_ArgRef_FASTCALL(__pyx_args, 1);
        if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[1])) __PYX_ERR(0, 197, __pyx_L3_error)
        CYTHON_FALLTHROUGH;
        case  1:
        values[0] = __Pyx_ArgRef_FASTCALL(__pyx_args, 0);
        if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[0])) __PYX_ERR(0, 197, __pyx_L3_error)
        CYTHON_FALLTHROUGH;
        case  0: break;
        default: goto __pyx_L5_argtuple_error;
      }
      const Py_ssize_t kwd_pos_args = __pyx_nargs;
      if (__Pyx_ParseKeywords(__pyx_kwds, __pyx_kwvalues, __pyx_pyargnames, 0, values, kwd_pos_args, __pyx_kwds_len, "__init__", 0) < (0)) __PYX_ERR(0, 197, __pyx_L3_error)
      if (!values[2]) values[2] = __Pyx_NewRef(((PyObject *)Py_None));
      for (Py_ssize_t i = __pyx_nargs; i < 2; i++) {
        if (unlikely(!values[i])) { __Pyx_RaiseArgtupleInvalid("__init__", 0, 2, 3, i); __PYX_ERR(0, 197, __pyx_L3_error) }
      }
    } else {
      switch (__pyx_nargs) {
        case  3:
        values[2] = __Pyx_ArgRef_FASTCALL(__pyx_args, 2);
        if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[2])) __PYX_ERR(0, 197, __pyx_L3_error)
        CYTHON_FALLTHROUGH;
        case  2:
        values[1] = __Pyx_ArgRef_FASTCALL(__pyx_args, 1);
        if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[1])) __PYX_ERR(0, 197, __pyx_L3_error)
        values[0] = __Pyx_ArgRef_FASTCALL(__pyx_args, 0);
        if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[0])) __PYX_ERR(0, 197, __pyx_L3_error)
        break;
        default: goto __pyx_L5_argtuple_error;
      }
      if (!values[2]) values[2] = __Pyx_NewRef(((PyObject *)Py_None));
    }
    __pyx_v_self = values[0];
    __pyx_v_filename = values[1];
    __pyx_v_path_description = values[2];
  }
  goto __pyx_L6_skip;
  __pyx_L5_argtuple_error:;
  __Pyx_RaiseArgtupleInvalid("__init__", 0, 2, 3, __pyx_nargs); __PYX_ERR(0, 197, __pyx_L3_error)
  __pyx_L6_skip:;
  goto __pyx_L4_argument_unpacking_done;
  __pyx_L3_error:;
  for (Py_ssize_t __pyx_temp=0; __pyx_temp < (Py_ssize_t)(sizeof(values)/sizeof(values[0])); ++__pyx_temp) {
    Py_XDECREF(values[__pyx_temp]);
  }
  __Pyx_AddTraceback("Cython.Compiler.Scanning.FileSourceDescriptor.__init__", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __Pyx_RefNannyFinishContext();
  return NULL;
  __pyx_L4_argument_unpacking_done:;
  __pyx_r = __pyx_pf_6Cython_8Compiler_8Scanning_20FileSourceDescriptor___init__(__pyx_self, __pyx_v_self, __pyx_v_filename, __pyx_v_path_description);

  /* function exit code */
  for (Py_ssize_t __pyx_temp=0; __pyx_temp < (Py_ssize_t)(sizeof(values)/sizeof(values[0])); ++__pyx_temp) {
    Py_XDECREF(values[__pyx_temp]);
  }
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}

static PyObject *__pyx_pf_6Cython_8Compiler_8Scanning_20FileSourceDescriptor___init__(CYTHON_UNUSED PyObject *__pyx_self, PyObject *__pyx_v_self, PyObject *__pyx_v_filename, PyObject *__pyx_v_path_description) {
  PyObject *__pyx_v_workdir = NULL;
  PyObject *__pyx_r = NULL;
  __Pyx_INCREF(__pyx_v_filename);
/* … */
  /* function exit code */
  __pyx_r = Py_None; __Pyx_INCREF(Py_None);
  goto __pyx_L0;
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_t_1);
  __Pyx_XDECREF(__pyx_t_2);
  __Pyx_XDECREF(__pyx_t_3);
  __Pyx_XDECREF(__pyx_t_4);
  __Pyx_AddTraceback("Cython.Compiler.Scanning.FileSourceDescriptor.__init__", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_r = NULL;
  __pyx_L0:;
  __Pyx_XDECREF(__pyx_v_workdir);
  __Pyx_XDECREF(__pyx_v_filename);
  __Pyx_XGIVEREF(__pyx_r);
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}
/* … */
  __pyx_t_6 = __Pyx_CyFunction_New(&__pyx_mdef_6Cython_8Compiler_8Scanning_20FileSourceDescriptor_1__init__, 0, __pyx_mstate_global->__pyx_n_u_FileSourceDescriptor___init, NULL, __pyx_mstate_global->__pyx_n_u_Cython_Compiler_Scanning, __pyx_mstate_global->__pyx_d, ((PyObject *)__pyx_mstate_global->__pyx_codeobj_tab[19])); if (unlikely(!__pyx_t_6)) __PYX_ERR(0, 197, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_6);
  #if CYTHON_COMPILING_IN_CPYTHON && PY_VERSION_HEX >= 0x030E0000
  PyUnstable_Object_EnableDeferredRefcount(__pyx_t_6);
  #endif
  __Pyx_CyFunction_SetDefaultsTuple(__pyx_t_6, __pyx_mstate_global->__pyx_tuple[16]);
  if (__Pyx_SetNameInClass(__pyx_t_7, __pyx_mstate_global->__pyx_n_u_init, __pyx_t_6) < (0)) __PYX_ERR(0, 197, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_6); __pyx_t_6 = 0;
```

</details>

L198  🔴  (score=10)
```python
        filename = Utils.decode_filename(filename)
```
<details><summary>Show generated C (score=10)</summary>

```c
  __pyx_t_2 = NULL;
  __Pyx_GetModuleGlobalName(__pyx_t_3, __pyx_mstate_global->__pyx_n_u_Utils); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 198, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_3);
  __pyx_t_4 = __Pyx_PyObject_GetAttrStr(__pyx_t_3, __pyx_mstate_global->__pyx_n_u_decode_filename); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 198, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_4);
  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
  __pyx_t_5 = 1;
  {
    PyObject *__pyx_callargs[2] = {__pyx_t_2, __pyx_v_filename};
    __pyx_t_1 = __Pyx_PyObject_FastCall((PyObject*)__pyx_t_4, __pyx_callargs+__pyx_t_5, (2-__pyx_t_5) | (__pyx_t_5*__Pyx_PY_VECTORCALL_ARGUMENTS_OFFSET));
    __Pyx_XDECREF(__pyx_t_2); __pyx_t_2 = 0;
    __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
    if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 198, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_1);
  }
  __Pyx_DECREF_SET(__pyx_v_filename, __pyx_t_1);
  __pyx_t_1 = 0;
```

</details>

L199  🟡  (score=2)
```python
        self.filename = filename
```
<details><summary>Show generated C (score=2)</summary>

```c
  if (__Pyx_PyObject_SetAttrStr(__pyx_v_self, __pyx_mstate_global->__pyx_n_u_filename, __pyx_v_filename) < (0)) __PYX_ERR(0, 199, __pyx_L1_error)
```

</details>

L200  🟠  (score=7)
```python
        self.path_description = path_description or filename
```
<details><summary>Show generated C (score=7)</summary>

```c
  __pyx_t_6 = __Pyx_PyObject_IsTrue(__pyx_v_path_description); if (unlikely((__pyx_t_6 < 0))) __PYX_ERR(0, 200, __pyx_L1_error)
  if (!__pyx_t_6) {
  } else {
    __Pyx_INCREF(__pyx_v_path_description);
    __pyx_t_1 = __pyx_v_path_description;
    goto __pyx_L3_bool_binop_done;
  }
  __Pyx_INCREF(__pyx_v_filename);
  __pyx_t_1 = __pyx_v_filename;
  __pyx_L3_bool_binop_done:;
  if (__Pyx_PyObject_SetAttrStr(__pyx_v_self, __pyx_mstate_global->__pyx_n_u_path_description, __pyx_t_1) < (0)) __PYX_ERR(0, 200, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
```

</details>

L201  🔴  (score=11)
```python
        try:
```
<details><summary>Show generated C (score=11)</summary>

```c
  {
    /*try:*/ {
/* … */
    }
    __Pyx_XDECREF(__pyx_t_7); __pyx_t_7 = 0;
    __Pyx_XDECREF(__pyx_t_8); __pyx_t_8 = 0;
    __Pyx_XDECREF(__pyx_t_9); __pyx_t_9 = 0;
    goto __pyx_L10_try_end;
    __pyx_L5_error:;
    __Pyx_XDECREF(__pyx_t_1); __pyx_t_1 = 0;
    __Pyx_XDECREF(__pyx_t_2); __pyx_t_2 = 0;
    __Pyx_XDECREF(__pyx_t_3); __pyx_t_3 = 0;
    __Pyx_XDECREF(__pyx_t_4); __pyx_t_4 = 0;
/* … */
    __pyx_L7_except_error:;
    __Pyx_XGIVEREF(__pyx_t_7);
    __Pyx_XGIVEREF(__pyx_t_8);
    __Pyx_XGIVEREF(__pyx_t_9);
    __Pyx_ExceptionReset(__pyx_t_7, __pyx_t_8, __pyx_t_9);
    goto __pyx_L1_error;
    __pyx_L6_exception_handled:;
    __Pyx_XGIVEREF(__pyx_t_7);
    __Pyx_XGIVEREF(__pyx_t_8);
    __Pyx_XGIVEREF(__pyx_t_9);
    __Pyx_ExceptionReset(__pyx_t_7, __pyx_t_8, __pyx_t_9);
    __pyx_L10_try_end:;
  }
```

</details>

L202  🔴  (score=13)
```python
            self._short_path_description = os.path.relpath(self.path_description)
```
<details><summary>Show generated C (score=13)</summary>

```c
      __pyx_t_2 = __Pyx_PyObject_GetAttrStr(__pyx_v_6Cython_8Compiler_8Scanning_os, __pyx_mstate_global->__pyx_n_u_path); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 202, __pyx_L5_error)
      __Pyx_GOTREF(__pyx_t_2);
      __pyx_t_4 = __pyx_t_2;
      __Pyx_INCREF(__pyx_t_4);
      __pyx_t_3 = __Pyx_PyObject_GetAttrStr(__pyx_v_self, __pyx_mstate_global->__pyx_n_u_path_description); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 202, __pyx_L5_error)
      __Pyx_GOTREF(__pyx_t_3);
      __pyx_t_5 = 0;
      {
        PyObject *__pyx_callargs[2] = {__pyx_t_4, __pyx_t_3};
        __pyx_t_1 = __Pyx_PyObject_FastCallMethod((PyObject*)__pyx_mstate_global->__pyx_n_u_relpath, __pyx_callargs+__pyx_t_5, (2-__pyx_t_5) | (1*__Pyx_PY_VECTORCALL_ARGUMENTS_OFFSET));
        __Pyx_XDECREF(__pyx_t_4); __pyx_t_4 = 0;
        __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
        __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
        if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 202, __pyx_L5_error)
        __Pyx_GOTREF(__pyx_t_1);
      }
      if (__Pyx_PyObject_SetAttrStr(__pyx_v_self, __pyx_mstate_global->__pyx_n_u_short_path_description, __pyx_t_1) < (0)) __PYX_ERR(0, 202, __pyx_L5_error)
      __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
```

</details>

L203  🟠  (score=6)
```python
        except ValueError:
```
<details><summary>Show generated C (score=6)</summary>

```c
    __pyx_t_10 = __Pyx_PyErr_ExceptionMatches(((PyObject *)(((PyTypeObject*)PyExc_ValueError))));
    if (__pyx_t_10) {
      __Pyx_AddTraceback("Cython.Compiler.Scanning.FileSourceDescriptor.__init__", __pyx_clineno, __pyx_lineno, __pyx_filename);
      if (__Pyx_GetException(&__pyx_t_1, &__pyx_t_2, &__pyx_t_3) < 0) __PYX_ERR(0, 203, __pyx_L7_except_error)
      __Pyx_XGOTREF(__pyx_t_1);
      __Pyx_XGOTREF(__pyx_t_2);
      __Pyx_XGOTREF(__pyx_t_3);
```

</details>

L204  ⚪  (score=0)
```python
            # path not under current directory => use complete file path
```
L205  🟠  (score=8)
```python
            self._short_path_description = self.path_description
```
<details><summary>Show generated C (score=8)</summary>

```c
      __pyx_t_4 = __Pyx_PyObject_GetAttrStr(__pyx_v_self, __pyx_mstate_global->__pyx_n_u_path_description); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 205, __pyx_L7_except_error)
      __Pyx_GOTREF(__pyx_t_4);
      if (__Pyx_PyObject_SetAttrStr(__pyx_v_self, __pyx_mstate_global->__pyx_n_u_short_path_description, __pyx_t_4) < (0)) __PYX_ERR(0, 205, __pyx_L7_except_error)
      __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
      __Pyx_XDECREF(__pyx_t_1); __pyx_t_1 = 0;
      __Pyx_XDECREF(__pyx_t_2); __pyx_t_2 = 0;
      __Pyx_XDECREF(__pyx_t_3); __pyx_t_3 = 0;
      goto __pyx_L6_exception_handled;
    }
    goto __pyx_L7_except_error;
```

</details>

L206  ⚪  (score=0)
```python
        # Prefer relative paths to current directory (which is most likely the project root) over absolute paths.
```
L207  🔴  (score=16)
```python
        workdir = os.path.abspath('.') + os.sep
```
<details><summary>Show generated C (score=16)</summary>

```c
  __pyx_t_1 = __Pyx_PyObject_GetAttrStr(__pyx_v_6Cython_8Compiler_8Scanning_os, __pyx_mstate_global->__pyx_n_u_path); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 207, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __pyx_t_2 = __pyx_t_1;
  __Pyx_INCREF(__pyx_t_2);
  __pyx_t_5 = 0;
  {
    PyObject *__pyx_callargs[2] = {__pyx_t_2, __pyx_mstate_global->__pyx_kp_u_};
    __pyx_t_3 = __Pyx_PyObject_FastCallMethod((PyObject*)__pyx_mstate_global->__pyx_n_u_abspath, __pyx_callargs+__pyx_t_5, (2-__pyx_t_5) | (1*__Pyx_PY_VECTORCALL_ARGUMENTS_OFFSET));
    __Pyx_XDECREF(__pyx_t_2); __pyx_t_2 = 0;
    __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
    if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 207, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_3);
  }
  __pyx_t_1 = __Pyx_PyObject_GetAttrStr(__pyx_v_6Cython_8Compiler_8Scanning_os, __pyx_mstate_global->__pyx_n_u_sep); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 207, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __pyx_t_2 = PyNumber_Add(__pyx_t_3, __pyx_t_1); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 207, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __pyx_v_workdir = __pyx_t_2;
  __pyx_t_2 = 0;
```

</details>

L208  🔴  (score=18)
```python
        self.file_path = filename[len(workdir):] if filename.startswith(workdir) else filename
```
<details><summary>Show generated C (score=18)</summary>

```c
  __pyx_t_3 = __pyx_v_filename;
  __Pyx_INCREF(__pyx_t_3);
  __pyx_t_5 = 0;
  {
    PyObject *__pyx_callargs[2] = {__pyx_t_3, __pyx_v_workdir};
    __pyx_t_1 = __Pyx_PyObject_FastCallMethod((PyObject*)__pyx_mstate_global->__pyx_n_u_startswith, __pyx_callargs+__pyx_t_5, (2-__pyx_t_5) | (1*__Pyx_PY_VECTORCALL_ARGUMENTS_OFFSET));
    __Pyx_XDECREF(__pyx_t_3); __pyx_t_3 = 0;
    if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 208, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_1);
  }
  __pyx_t_6 = __Pyx_PyObject_IsTrue(__pyx_t_1); if (unlikely((__pyx_t_6 < 0))) __PYX_ERR(0, 208, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  if (__pyx_t_6) {
    __pyx_t_11 = PyObject_Length(__pyx_v_workdir); if (unlikely(__pyx_t_11 == ((Py_ssize_t)-1))) __PYX_ERR(0, 208, __pyx_L1_error)
    __pyx_t_1 = __Pyx_PyObject_GetSlice(__pyx_v_filename, __pyx_t_11, 0, NULL, NULL, NULL, 1, 0, 0); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 208, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_1);
    __pyx_t_2 = __pyx_t_1;
    __pyx_t_1 = 0;
  } else {
    __Pyx_INCREF(__pyx_v_filename);
    __pyx_t_2 = __pyx_v_filename;
  }
  if (__Pyx_PyObject_SetAttrStr(__pyx_v_self, __pyx_mstate_global->__pyx_n_u_file_path, __pyx_t_2) < (0)) __PYX_ERR(0, 208, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
```

</details>

L209  🟠  (score=5)
```python
        self.set_file_type_from_name(filename)
```
<details><summary>Show generated C (score=5)</summary>

```c
  __pyx_t_1 = __pyx_v_self;
  __Pyx_INCREF(__pyx_t_1);
  __pyx_t_5 = 0;
  {
    PyObject *__pyx_callargs[2] = {__pyx_t_1, __pyx_v_filename};
    __pyx_t_2 = __Pyx_PyObject_FastCallMethod((PyObject*)__pyx_mstate_global->__pyx_n_u_set_file_type_from_name, __pyx_callargs+__pyx_t_5, (2-__pyx_t_5) | (1*__Pyx_PY_VECTORCALL_ARGUMENTS_OFFSET));
    __Pyx_XDECREF(__pyx_t_1); __pyx_t_1 = 0;
    if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 209, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_2);
  }
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
```

</details>

L210  🟡  (score=2)
```python
        self._cmp_name = filename
```
<details><summary>Show generated C (score=2)</summary>

```c
  if (__Pyx_PyObject_SetAttrStr(__pyx_v_self, __pyx_mstate_global->__pyx_n_u_cmp_name, __pyx_v_filename) < (0)) __PYX_ERR(0, 210, __pyx_L1_error)
```

</details>

L211  🟠  (score=5)
```python
        self._lines = {}
```
<details><summary>Show generated C (score=5)</summary>

```c
  __pyx_t_2 = __Pyx_PyDict_NewPresized(0); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 211, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  if (__Pyx_PyObject_SetAttrStr(__pyx_v_self, __pyx_mstate_global->__pyx_n_u_lines, __pyx_t_2) < (0)) __PYX_ERR(0, 211, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
```

</details>

L212  ⚪  (score=0)
```python
```
L213  🔴  (score=66)
```python
    def get_lines(self, encoding=None, error_handling=None):
```
<details><summary>Show generated C (score=66)</summary>

```c
/* Python wrapper */
static PyObject *__pyx_pw_6Cython_8Compiler_8Scanning_20FileSourceDescriptor_3get_lines(PyObject *__pyx_self, 
#if CYTHON_METH_FASTCALL
PyObject *const *__pyx_args, Py_ssize_t __pyx_nargs, PyObject *__pyx_kwds
#else
PyObject *__pyx_args, PyObject *__pyx_kwds
#endif
); /*proto*/
PyDoc_STRVAR(__pyx_doc_6Cython_8Compiler_8Scanning_20FileSourceDescriptor_2get_lines, "File: Cython/Compiler/Scanning.py (starting at line 213)");
static PyMethodDef __pyx_mdef_6Cython_8Compiler_8Scanning_20FileSourceDescriptor_3get_lines = {"get_lines", (PyCFunction)(void(*)(void))(__Pyx_PyCFunction_FastCallWithKeywords)__pyx_pw_6Cython_8Compiler_8Scanning_20FileSourceDescriptor_3get_lines, __Pyx_METH_FASTCALL|METH_KEYWORDS, __pyx_doc_6Cython_8Compiler_8Scanning_20FileSourceDescriptor_2get_lines};
static PyObject *__pyx_pw_6Cython_8Compiler_8Scanning_20FileSourceDescriptor_3get_lines(PyObject *__pyx_self, 
#if CYTHON_METH_FASTCALL
PyObject *const *__pyx_args, Py_ssize_t __pyx_nargs, PyObject *__pyx_kwds
#else
PyObject *__pyx_args, PyObject *__pyx_kwds
#endif
) {
  PyObject *__pyx_v_self = 0;
  PyObject *__pyx_v_encoding = 0;
  PyObject *__pyx_v_error_handling = 0;
  #if !CYTHON_METH_FASTCALL
  CYTHON_UNUSED Py_ssize_t __pyx_nargs;
  #endif
  CYTHON_UNUSED PyObject *const *__pyx_kwvalues;
  PyObject *__pyx_r = 0;
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("get_lines (wrapper)", 0);
  #if !CYTHON_METH_FASTCALL
  #if CYTHON_ASSUME_SAFE_SIZE
  __pyx_nargs = PyTuple_GET_SIZE(__pyx_args);
  #else
  __pyx_nargs = PyTuple_Size(__pyx_args); if (unlikely(__pyx_nargs < 0)) return NULL;
  #endif
  #endif
  __pyx_kwvalues = __Pyx_KwValues_FASTCALL(__pyx_args, __pyx_nargs);
  {
    PyObject ** const __pyx_pyargnames[] = {&__pyx_mstate_global->__pyx_n_u_self,&__pyx_mstate_global->__pyx_n_u_encoding,&__pyx_mstate_global->__pyx_n_u_error_handling,0};
  PyObject* values[3] = {0,0,0};
    const Py_ssize_t __pyx_kwds_len = (__pyx_kwds) ? __Pyx_NumKwargs_FASTCALL(__pyx_kwds) : 0;
    if (unlikely(__pyx_kwds_len) < 0) __PYX_ERR(0, 213, __pyx_L3_error)
    if (__pyx_kwds_len > 0) {
      switch (__pyx_nargs) {
        case  3:
        values[2] = __Pyx_ArgRef_FASTCALL(__pyx_args, 2);
        if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[2])) __PYX_ERR(0, 213, __pyx_L3_error)
        CYTHON_FALLTHROUGH;
        case  2:
        values[1] = __Pyx_ArgRef_FASTCALL(__pyx_args, 1);
        if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[1])) __PYX_ERR(0, 213, __pyx_L3_error)
        CYTHON_FALLTHROUGH;
        case  1:
        values[0] = __Pyx_ArgRef_FASTCALL(__pyx_args, 0);
        if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[0])) __PYX_ERR(0, 213, __pyx_L3_error)
        CYTHON_FALLTHROUGH;
        case  0: break;
        default: goto __pyx_L5_argtuple_error;
      }
      const Py_ssize_t kwd_pos_args = __pyx_nargs;
      if (__Pyx_ParseKeywords(__pyx_kwds, __pyx_kwvalues, __pyx_pyargnames, 0, values, kwd_pos_args, __pyx_kwds_len, "get_lines", 0) < (0)) __PYX_ERR(0, 213, __pyx_L3_error)
      if (!values[1]) values[1] = __Pyx_NewRef(((PyObject *)Py_None));
      if (!values[2]) values[2] = __Pyx_NewRef(((PyObject *)Py_None));
      for (Py_ssize_t i = __pyx_nargs; i < 1; i++) {
        if (unlikely(!values[i])) { __Pyx_RaiseArgtupleInvalid("get_lines", 0, 1, 3, i); __PYX_ERR(0, 213, __pyx_L3_error) }
      }
    } else {
      switch (__pyx_nargs) {
        case  3:
        values[2] = __Pyx_ArgRef_FASTCALL(__pyx_args, 2);
        if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[2])) __PYX_ERR(0, 213, __pyx_L3_error)
        CYTHON_FALLTHROUGH;
        case  2:
        values[1] = __Pyx_ArgRef_FASTCALL(__pyx_args, 1);
        if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[1])) __PYX_ERR(0, 213, __pyx_L3_error)
        CYTHON_FALLTHROUGH;
        case  1:
        values[0] = __Pyx_ArgRef_FASTCALL(__pyx_args, 0);
        if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[0])) __PYX_ERR(0, 213, __pyx_L3_error)
        break;
        default: goto __pyx_L5_argtuple_error;
      }
      if (!values[1]) values[1] = __Pyx_NewRef(((PyObject *)Py_None));
      if (!values[2]) values[2] = __Pyx_NewRef(((PyObject *)Py_None));
    }
    __pyx_v_self = values[0];
    __pyx_v_encoding = values[1];
    __pyx_v_error_handling = values[2];
  }
  goto __pyx_L6_skip;
  __pyx_L5_argtuple_error:;
  __Pyx_RaiseArgtupleInvalid("get_lines", 0, 1, 3, __pyx_nargs); __PYX_ERR(0, 213, __pyx_L3_error)
  __pyx_L6_skip:;
  goto __pyx_L4_argument_unpacking_done;
  __pyx_L3_error:;
  for (Py_ssize_t __pyx_temp=0; __pyx_temp < (Py_ssize_t)(sizeof(values)/sizeof(values[0])); ++__pyx_temp) {
    Py_XDECREF(values[__pyx_temp]);
  }
  __Pyx_AddTraceback("Cython.Compiler.Scanning.FileSourceDescriptor.get_lines", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __Pyx_RefNannyFinishContext();
  return NULL;
  __pyx_L4_argument_unpacking_done:;
  __pyx_r = __pyx_pf_6Cython_8Compiler_8Scanning_20FileSourceDescriptor_2get_lines(__pyx_self, __pyx_v_self, __pyx_v_encoding, __pyx_v_error_handling);

  /* function exit code */
  for (Py_ssize_t __pyx_temp=0; __pyx_temp < (Py_ssize_t)(sizeof(values)/sizeof(values[0])); ++__pyx_temp) {
    Py_XDECREF(values[__pyx_temp]);
  }
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}

static PyObject *__pyx_pf_6Cython_8Compiler_8Scanning_20FileSourceDescriptor_2get_lines(CYTHON_UNUSED PyObject *__pyx_self, PyObject *__pyx_v_self, PyObject *__pyx_v_encoding, PyObject *__pyx_v_error_handling) {
  PyObject *__pyx_v_key = NULL;
  PyObject *__pyx_v_lines = NULL;
  PyObject *__pyx_v_f = NULL;
  PyObject *__pyx_7genexpr__pyx_v_line = NULL;
  PyObject *__pyx_r = NULL;
/* … */
  /* function exit code */
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_t_1);
  __Pyx_XDECREF(__pyx_t_2);
  __Pyx_XDECREF(__pyx_t_3);
  __Pyx_XDECREF(__pyx_t_7);
  __Pyx_AddTraceback("Cython.Compiler.Scanning.FileSourceDescriptor.get_lines", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_r = NULL;
  __pyx_L0:;
  __Pyx_XDECREF(__pyx_v_key);
  __Pyx_XDECREF(__pyx_v_lines);
  __Pyx_XDECREF(__pyx_v_f);
  __Pyx_XDECREF(__pyx_7genexpr__pyx_v_line);
  __Pyx_XGIVEREF(__pyx_r);
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}
/* … */
  __pyx_t_6 = __Pyx_CyFunction_New(&__pyx_mdef_6Cython_8Compiler_8Scanning_20FileSourceDescriptor_3get_lines, 0, __pyx_mstate_global->__pyx_n_u_FileSourceDescriptor_get_lines, NULL, __pyx_mstate_global->__pyx_n_u_Cython_Compiler_Scanning, __pyx_mstate_global->__pyx_d, ((PyObject *)__pyx_mstate_global->__pyx_codeobj_tab[20])); if (unlikely(!__pyx_t_6)) __PYX_ERR(0, 213, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_6);
  #if CYTHON_COMPILING_IN_CPYTHON && PY_VERSION_HEX >= 0x030E0000
  PyUnstable_Object_EnableDeferredRefcount(__pyx_t_6);
  #endif
  __Pyx_CyFunction_SetDefaultsTuple(__pyx_t_6, __pyx_mstate_global->__pyx_tuple[17]);
  if (__Pyx_SetNameInClass(__pyx_t_7, __pyx_mstate_global->__pyx_n_u_get_lines, __pyx_t_6) < (0)) __PYX_ERR(0, 213, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_6); __pyx_t_6 = 0;
/* … */
  __pyx_mstate_global->__pyx_tuple[17] = PyTuple_Pack(2, Py_None, Py_None); if (unlikely(!__pyx_mstate_global->__pyx_tuple[17])) __PYX_ERR(0, 213, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_mstate_global->__pyx_tuple[17]);
  __Pyx_GIVEREF(__pyx_mstate_global->__pyx_tuple[17]);
```

</details>

L214  ⚪  (score=0)
```python
        # we cache the lines only the second time this is called, in
```
L215  ⚪  (score=0)
```python
        # order to save memory when they are only used once
```
L216  🔴  (score=11)
```python
        key = (encoding, error_handling)
```
<details><summary>Show generated C (score=11)</summary>

```c
  __pyx_t_1 = PyTuple_New(2); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 216, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_INCREF(__pyx_v_encoding);
  __Pyx_GIVEREF(__pyx_v_encoding);
  if (__Pyx_PyTuple_SET_ITEM(__pyx_t_1, 0, __pyx_v_encoding) != (0)) __PYX_ERR(0, 216, __pyx_L1_error);
  __Pyx_INCREF(__pyx_v_error_handling);
  __Pyx_GIVEREF(__pyx_v_error_handling);
  if (__Pyx_PyTuple_SET_ITEM(__pyx_t_1, 1, __pyx_v_error_handling) != (0)) __PYX_ERR(0, 216, __pyx_L1_error);
  __pyx_v_key = __pyx_t_1;
  __pyx_t_1 = 0;
```

</details>

L217  🟠  (score=7)
```python
        lines = self._lines.get(key)
```
<details><summary>Show generated C (score=7)</summary>

```c
  __pyx_t_3 = __Pyx_PyObject_GetAttrStr(__pyx_v_self, __pyx_mstate_global->__pyx_n_u_lines); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 217, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_3);
  __pyx_t_2 = __pyx_t_3;
  __Pyx_INCREF(__pyx_t_2);
  __pyx_t_4 = 0;
  {
    PyObject *__pyx_callargs[2] = {__pyx_t_2, __pyx_v_key};
    __pyx_t_1 = __Pyx_PyObject_FastCallMethod((PyObject*)__pyx_mstate_global->__pyx_n_u_get, __pyx_callargs+__pyx_t_4, (2-__pyx_t_4) | (1*__Pyx_PY_VECTORCALL_ARGUMENTS_OFFSET));
    __Pyx_XDECREF(__pyx_t_2); __pyx_t_2 = 0;
    __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
    if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 217, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_1);
  }
  __pyx_v_lines = __pyx_t_1;
  __pyx_t_1 = 0;
```

</details>

L218  ⚪  (score=0)
```python
        if lines is not None:
```
<details><summary>Show generated C (score=0)</summary>

```c
  __pyx_t_5 = (__pyx_v_lines != Py_None);
  if (__pyx_t_5) {
/* … */
  }
```

</details>

L219  🟡  (score=2)
```python
            return lines
```
<details><summary>Show generated C (score=2)</summary>

```c
    __Pyx_XDECREF(__pyx_r);
    __Pyx_INCREF(__pyx_v_lines);
    __pyx_r = __pyx_v_lines;
    goto __pyx_L0;
```

</details>

L220  ⚪  (score=0)
```python
```
L221  🔴  (score=62)
```python
        with self.get_file_object(encoding=encoding, error_handling=error_handling) as f:
```
<details><summary>Show generated C (score=62)</summary>

```c
  /*with:*/ {
    __pyx_t_3 = __pyx_v_self;
    __Pyx_INCREF(__pyx_t_3);
    __pyx_t_4 = 0;
    {
      PyObject *__pyx_callargs[2 + ((CYTHON_VECTORCALL) ? 2 : 0)] = {__pyx_t_3, NULL};
      __pyx_t_2 = __Pyx_MakeVectorcallBuilderKwds(2); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 221, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_2);
      if (__Pyx_VectorcallBuilder_AddArg(__pyx_mstate_global->__pyx_n_u_encoding, __pyx_v_encoding, __pyx_t_2, __pyx_callargs+1, 0) < (0)) __PYX_ERR(0, 221, __pyx_L1_error)
      if (__Pyx_VectorcallBuilder_AddArg(__pyx_mstate_global->__pyx_n_u_error_handling, __pyx_v_error_handling, __pyx_t_2, __pyx_callargs+1, 1) < (0)) __PYX_ERR(0, 221, __pyx_L1_error)
      __pyx_t_1 = __Pyx_Object_VectorcallMethod_CallFromBuilder((PyObject*)__pyx_mstate_global->__pyx_n_u_get_file_object, __pyx_callargs+__pyx_t_4, (1-__pyx_t_4) | (1*__Pyx_PY_VECTORCALL_ARGUMENTS_OFFSET), __pyx_t_2);
      __Pyx_XDECREF(__pyx_t_3); __pyx_t_3 = 0;
      __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
      if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 221, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_1);
    }
    __pyx_t_6 = __Pyx_PyObject_LookupSpecial(__pyx_t_1, __pyx_mstate_global->__pyx_n_u_exit); if (unlikely(!__pyx_t_6)) __PYX_ERR(0, 221, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_6);
    __pyx_t_3 = NULL;
    __pyx_t_7 = __Pyx_PyObject_LookupSpecial(__pyx_t_1, __pyx_mstate_global->__pyx_n_u_enter); if (unlikely(!__pyx_t_7)) __PYX_ERR(0, 221, __pyx_L4_error)
    __Pyx_GOTREF(__pyx_t_7);
    __pyx_t_4 = 1;
    {
      PyObject *__pyx_callargs[2] = {__pyx_t_3, NULL};
      __pyx_t_2 = __Pyx_PyObject_FastCall((PyObject*)__pyx_t_7, __pyx_callargs+__pyx_t_4, (1-__pyx_t_4) | (__pyx_t_4*__Pyx_PY_VECTORCALL_ARGUMENTS_OFFSET));
      __Pyx_XDECREF(__pyx_t_3); __pyx_t_3 = 0;
      __Pyx_DECREF(__pyx_t_7); __pyx_t_7 = 0;
      if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 221, __pyx_L4_error)
      __Pyx_GOTREF(__pyx_t_2);
    }
    __pyx_t_7 = __pyx_t_2;
    __pyx_t_2 = 0;
    __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
    /*try:*/ {
      {
        /*try:*/ {
          __pyx_v_f = __pyx_t_7;
          __pyx_t_7 = 0;
/* … */
        }
        __Pyx_XDECREF(__pyx_t_8); __pyx_t_8 = 0;
        __Pyx_XDECREF(__pyx_t_9); __pyx_t_9 = 0;
        __Pyx_XDECREF(__pyx_t_10); __pyx_t_10 = 0;
        goto __pyx_L13_try_end;
        __pyx_L8_error:;
        __Pyx_XDECREF(__pyx_t_1); __pyx_t_1 = 0;
        __Pyx_XDECREF(__pyx_t_2); __pyx_t_2 = 0;
        __Pyx_XDECREF(__pyx_t_3); __pyx_t_3 = 0;
        __Pyx_XDECREF(__pyx_t_7); __pyx_t_7 = 0;
        /*except:*/ {
          __Pyx_AddTraceback("Cython.Compiler.Scanning.FileSourceDescriptor.get_lines", __pyx_clineno, __pyx_lineno, __pyx_filename);
          if (__Pyx_GetException(&__pyx_t_7, &__pyx_t_2, &__pyx_t_1) < 0) __PYX_ERR(0, 221, __pyx_L10_except_error)
          __Pyx_XGOTREF(__pyx_t_7);
          __Pyx_XGOTREF(__pyx_t_2);
          __Pyx_XGOTREF(__pyx_t_1);
          __pyx_t_3 = PyTuple_Pack(3, __pyx_t_7, __pyx_t_2, __pyx_t_1); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 221, __pyx_L10_except_error)
          __Pyx_GOTREF(__pyx_t_3);
          __pyx_t_13 = __Pyx_PyObject_Call(__pyx_t_6, __pyx_t_3, NULL);
          __Pyx_DECREF(__pyx_t_6); __pyx_t_6 = 0;
          __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
          if (unlikely(!__pyx_t_13)) __PYX_ERR(0, 221, __pyx_L10_except_error)
          __Pyx_GOTREF(__pyx_t_13);
          __pyx_t_5 = __Pyx_PyObject_IsTrue(__pyx_t_13);
          __Pyx_DECREF(__pyx_t_13); __pyx_t_13 = 0;
          if (__pyx_t_5 < (0)) __PYX_ERR(0, 221, __pyx_L10_except_error)
          __pyx_t_14 = (!__pyx_t_5);
          if (unlikely(__pyx_t_14)) {
            __Pyx_GIVEREF(__pyx_t_7);
            __Pyx_GIVEREF(__pyx_t_2);
            __Pyx_XGIVEREF(__pyx_t_1);
            __Pyx_ErrRestoreWithState(__pyx_t_7, __pyx_t_2, __pyx_t_1);
            __pyx_t_7 = 0;  __pyx_t_2 = 0;  __pyx_t_1 = 0; 
            __PYX_ERR(0, 221, __pyx_L10_except_error)
          }
          __Pyx_XDECREF(__pyx_t_7); __pyx_t_7 = 0;
          __Pyx_XDECREF(__pyx_t_2); __pyx_t_2 = 0;
          __Pyx_XDECREF(__pyx_t_1); __pyx_t_1 = 0;
          goto __pyx_L9_exception_handled;
        }
        __pyx_L10_except_error:;
        __Pyx_XGIVEREF(__pyx_t_8);
        __Pyx_XGIVEREF(__pyx_t_9);
        __Pyx_XGIVEREF(__pyx_t_10);
        __Pyx_ExceptionReset(__pyx_t_8, __pyx_t_9, __pyx_t_10);
        goto __pyx_L1_error;
        __pyx_L9_exception_handled:;
        __Pyx_XGIVEREF(__pyx_t_8);
        __Pyx_XGIVEREF(__pyx_t_9);
        __Pyx_XGIVEREF(__pyx_t_10);
        __Pyx_ExceptionReset(__pyx_t_8, __pyx_t_9, __pyx_t_10);
        __pyx_L13_try_end:;
      }
    }
    /*finally:*/ {
      /*normal exit:*/{
        if (__pyx_t_6) {
          __pyx_t_10 = __Pyx_PyObject_Call(__pyx_t_6, __pyx_mstate_global->__pyx_tuple[3], NULL);
          __Pyx_DECREF(__pyx_t_6); __pyx_t_6 = 0;
          if (unlikely(!__pyx_t_10)) __PYX_ERR(0, 221, __pyx_L1_error)
          __Pyx_GOTREF(__pyx_t_10);
          __Pyx_DECREF(__pyx_t_10); __pyx_t_10 = 0;
        }
        goto __pyx_L7;
      }
      __pyx_L7:;
    }
    goto __pyx_L24;
    __pyx_L4_error:;
    __Pyx_DECREF(__pyx_t_6); __pyx_t_6 = 0;
    goto __pyx_L1_error;
    __pyx_L24:;
  }
/* … */
  __pyx_mstate_global->__pyx_tuple[3] = PyTuple_Pack(3, Py_None, Py_None, Py_None); if (unlikely(!__pyx_mstate_global->__pyx_tuple[3])) __PYX_ERR(0, 221, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_mstate_global->__pyx_tuple[3]);
  __Pyx_GIVEREF(__pyx_mstate_global->__pyx_tuple[3]);
```

</details>

L222  🔴  (score=68)
```python
            lines = [line.rstrip() for line in f.readlines()]
```
<details><summary>Show generated C (score=68)</summary>

```c
          { /* enter inner scope */
            __pyx_t_7 = PyList_New(0); if (unlikely(!__pyx_t_7)) __PYX_ERR(0, 222, __pyx_L16_error)
            __Pyx_GOTREF(__pyx_t_7);
            __pyx_t_2 = __pyx_v_f;
            __Pyx_INCREF(__pyx_t_2);
            __pyx_t_4 = 0;
            {
              PyObject *__pyx_callargs[2] = {__pyx_t_2, NULL};
              __pyx_t_1 = __Pyx_PyObject_FastCallMethod((PyObject*)__pyx_mstate_global->__pyx_n_u_readlines, __pyx_callargs+__pyx_t_4, (1-__pyx_t_4) | (1*__Pyx_PY_VECTORCALL_ARGUMENTS_OFFSET));
              __Pyx_XDECREF(__pyx_t_2); __pyx_t_2 = 0;
              if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 222, __pyx_L16_error)
              __Pyx_GOTREF(__pyx_t_1);
            }
            if (likely(PyList_CheckExact(__pyx_t_1)) || PyTuple_CheckExact(__pyx_t_1)) {
              __pyx_t_2 = __pyx_t_1; __Pyx_INCREF(__pyx_t_2);
              __pyx_t_11 = 0;
              __pyx_t_12 = NULL;
            } else {
              __pyx_t_11 = -1; __pyx_t_2 = PyObject_GetIter(__pyx_t_1); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 222, __pyx_L16_error)
              __Pyx_GOTREF(__pyx_t_2);
              __pyx_t_12 = (CYTHON_COMPILING_IN_LIMITED_API) ? PyIter_Next : __Pyx_PyObject_GetIterNextFunc(__pyx_t_2); if (unlikely(!__pyx_t_12)) __PYX_ERR(0, 222, __pyx_L16_error)
            }
            __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
            for (;;) {
              if (likely(!__pyx_t_12)) {
                if (likely(PyList_CheckExact(__pyx_t_2))) {
                  {
                    Py_ssize_t __pyx_temp = __Pyx_PyList_GET_SIZE(__pyx_t_2);
                    #if !CYTHON_ASSUME_SAFE_SIZE
                    if (unlikely((__pyx_temp < 0))) __PYX_ERR(0, 222, __pyx_L16_error)
                    #endif
                    if (__pyx_t_11 >= __pyx_temp) break;
                  }
                  __pyx_t_1 = __Pyx_PyList_GetItemRefFast(__pyx_t_2, __pyx_t_11, __Pyx_ReferenceSharing_OwnStrongReference);
                  ++__pyx_t_11;
                } else {
                  {
                    Py_ssize_t __pyx_temp = __Pyx_PyTuple_GET_SIZE(__pyx_t_2);
                    #if !CYTHON_ASSUME_SAFE_SIZE
                    if (unlikely((__pyx_temp < 0))) __PYX_ERR(0, 222, __pyx_L16_error)
                    #endif
                    if (__pyx_t_11 >= __pyx_temp) break;
                  }
                  #if CYTHON_ASSUME_SAFE_MACROS && !CYTHON_AVOID_BORROWED_REFS
                  __pyx_t_1 = __Pyx_NewRef(PyTuple_GET_ITEM(__pyx_t_2, __pyx_t_11));
                  #else
                  __pyx_t_1 = __Pyx_PySequence_ITEM(__pyx_t_2, __pyx_t_11);
                  #endif
                  ++__pyx_t_11;
                }
                if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 222, __pyx_L16_error)
              } else {
                __pyx_t_1 = __pyx_t_12(__pyx_t_2);
                if (unlikely(!__pyx_t_1)) {
                  PyObject* exc_type = PyErr_Occurred();
                  if (exc_type) {
                    if (unlikely(!__Pyx_PyErr_GivenExceptionMatches(exc_type, PyExc_StopIteration))) __PYX_ERR(0, 222, __pyx_L16_error)
                    PyErr_Clear();
                  }
                  break;
                }
              }
              __Pyx_GOTREF(__pyx_t_1);
              __Pyx_XDECREF_SET(__pyx_7genexpr__pyx_v_line, __pyx_t_1);
              __pyx_t_1 = 0;
              __pyx_t_3 = __pyx_7genexpr__pyx_v_line;
              __Pyx_INCREF(__pyx_t_3);
              __pyx_t_4 = 0;
              {
                PyObject *__pyx_callargs[2] = {__pyx_t_3, NULL};
                __pyx_t_1 = __Pyx_PyObject_FastCallMethod((PyObject*)__pyx_mstate_global->__pyx_n_u_rstrip, __pyx_callargs+__pyx_t_4, (1-__pyx_t_4) | (1*__Pyx_PY_VECTORCALL_ARGUMENTS_OFFSET));
                __Pyx_XDECREF(__pyx_t_3); __pyx_t_3 = 0;
                if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 222, __pyx_L16_error)
                __Pyx_GOTREF(__pyx_t_1);
              }
              if (unlikely(__Pyx_ListComp_Append(__pyx_t_7, (PyObject*)__pyx_t_1))) __PYX_ERR(0, 222, __pyx_L16_error)
              __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
            }
            __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
            __Pyx_XDECREF(__pyx_7genexpr__pyx_v_line); __pyx_7genexpr__pyx_v_line = 0;
            goto __pyx_L20_exit_scope;
            __pyx_L16_error:;
            __Pyx_XDECREF(__pyx_7genexpr__pyx_v_line); __pyx_7genexpr__pyx_v_line = 0;
            goto __pyx_L8_error;
            __pyx_L20_exit_scope:;
          } /* exit inner scope */
          __Pyx_DECREF_SET(__pyx_v_lines, __pyx_t_7);
          __pyx_t_7 = 0;
```

</details>

L223  ⚪  (score=0)
```python
```
L224  ⚪  (score=0)
```python
        # Do not cache the first access, but add the key to remember that we already read it once.
```
L225  🔴  (score=16)
```python
        self._lines[key] = lines if key in self._lines else None
```
<details><summary>Show generated C (score=16)</summary>

```c
  __pyx_t_2 = __Pyx_PyObject_GetAttrStr(__pyx_v_self, __pyx_mstate_global->__pyx_n_u_lines); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 225, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __pyx_t_14 = (__Pyx_PySequence_ContainsTF(__pyx_v_key, __pyx_t_2, Py_EQ)); if (unlikely((__pyx_t_14 < 0))) __PYX_ERR(0, 225, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  if (__pyx_t_14) {
    __Pyx_INCREF(__pyx_v_lines);
    __pyx_t_1 = __pyx_v_lines;
  } else {
    __Pyx_INCREF(Py_None);
    __pyx_t_1 = Py_None;
  }
  __pyx_t_2 = __Pyx_PyObject_GetAttrStr(__pyx_v_self, __pyx_mstate_global->__pyx_n_u_lines); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 225, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  if (unlikely((PyObject_SetItem(__pyx_t_2, __pyx_v_key, __pyx_t_1) < 0))) __PYX_ERR(0, 225, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
```

</details>

L226  🟡  (score=2)
```python
        return lines
```
<details><summary>Show generated C (score=2)</summary>

```c
  __Pyx_XDECREF(__pyx_r);
  __Pyx_INCREF(__pyx_v_lines);
  __pyx_r = __pyx_v_lines;
  goto __pyx_L0;
```

</details>

L227  ⚪  (score=0)
```python
```
L228  🔴  (score=57)
```python
    def get_file_object(self, encoding=None, error_handling=None):
```
<details><summary>Show generated C (score=57)</summary>

```c
/* Python wrapper */
static PyObject *__pyx_pw_6Cython_8Compiler_8Scanning_20FileSourceDescriptor_5get_file_object(PyObject *__pyx_self, 
#if CYTHON_METH_FASTCALL
PyObject *const *__pyx_args, Py_ssize_t __pyx_nargs, PyObject *__pyx_kwds
#else
PyObject *__pyx_args, PyObject *__pyx_kwds
#endif
); /*proto*/
PyDoc_STRVAR(__pyx_doc_6Cython_8Compiler_8Scanning_20FileSourceDescriptor_4get_file_object, "File: Cython/Compiler/Scanning.py (starting at line 228)");
static PyMethodDef __pyx_mdef_6Cython_8Compiler_8Scanning_20FileSourceDescriptor_5get_file_object = {"get_file_object", (PyCFunction)(void(*)(void))(__Pyx_PyCFunction_FastCallWithKeywords)__pyx_pw_6Cython_8Compiler_8Scanning_20FileSourceDescriptor_5get_file_object, __Pyx_METH_FASTCALL|METH_KEYWORDS, __pyx_doc_6Cython_8Compiler_8Scanning_20FileSourceDescriptor_4get_file_object};
static PyObject *__pyx_pw_6Cython_8Compiler_8Scanning_20FileSourceDescriptor_5get_file_object(PyObject *__pyx_self, 
#if CYTHON_METH_FASTCALL
PyObject *const *__pyx_args, Py_ssize_t __pyx_nargs, PyObject *__pyx_kwds
#else
PyObject *__pyx_args, PyObject *__pyx_kwds
#endif
) {
  PyObject *__pyx_v_self = 0;
  PyObject *__pyx_v_encoding = 0;
  PyObject *__pyx_v_error_handling = 0;
  #if !CYTHON_METH_FASTCALL
  CYTHON_UNUSED Py_ssize_t __pyx_nargs;
  #endif
  CYTHON_UNUSED PyObject *const *__pyx_kwvalues;
  PyObject *__pyx_r = 0;
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("get_file_object (wrapper)", 0);
  #if !CYTHON_METH_FASTCALL
  #if CYTHON_ASSUME_SAFE_SIZE
  __pyx_nargs = PyTuple_GET_SIZE(__pyx_args);
  #else
  __pyx_nargs = PyTuple_Size(__pyx_args); if (unlikely(__pyx_nargs < 0)) return NULL;
  #endif
  #endif
  __pyx_kwvalues = __Pyx_KwValues_FASTCALL(__pyx_args, __pyx_nargs);
  {
    PyObject ** const __pyx_pyargnames[] = {&__pyx_mstate_global->__pyx_n_u_self,&__pyx_mstate_global->__pyx_n_u_encoding,&__pyx_mstate_global->__pyx_n_u_error_handling,0};
  PyObject* values[3] = {0,0,0};
    const Py_ssize_t __pyx_kwds_len = (__pyx_kwds) ? __Pyx_NumKwargs_FASTCALL(__pyx_kwds) : 0;
    if (unlikely(__pyx_kwds_len) < 0) __PYX_ERR(0, 228, __pyx_L3_error)
    if (__pyx_kwds_len > 0) {
      switch (__pyx_nargs) {
        case  3:
        values[2] = __Pyx_ArgRef_FASTCALL(__pyx_args, 2);
        if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[2])) __PYX_ERR(0, 228, __pyx_L3_error)
        CYTHON_FALLTHROUGH;
        case  2:
        values[1] = __Pyx_ArgRef_FASTCALL(__pyx_args, 1);
        if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[1])) __PYX_ERR(0, 228, __pyx_L3_error)
        CYTHON_FALLTHROUGH;
        case  1:
        values[0] = __Pyx_ArgRef_FASTCALL(__pyx_args, 0);
        if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[0])) __PYX_ERR(0, 228, __pyx_L3_error)
        CYTHON_FALLTHROUGH;
        case  0: break;
        default: goto __pyx_L5_argtuple_error;
      }
      const Py_ssize_t kwd_pos_args = __pyx_nargs;
      if (__Pyx_ParseKeywords(__pyx_kwds, __pyx_kwvalues, __pyx_pyargnames, 0, values, kwd_pos_args, __pyx_kwds_len, "get_file_object", 0) < (0)) __PYX_ERR(0, 228, __pyx_L3_error)
      if (!values[1]) values[1] = __Pyx_NewRef(((PyObject *)Py_None));
      if (!values[2]) values[2] = __Pyx_NewRef(((PyObject *)Py_None));
      for (Py_ssize_t i = __pyx_nargs; i < 1; i++) {
        if (unlikely(!values[i])) { __Pyx_RaiseArgtupleInvalid("get_file_object", 0, 1, 3, i); __PYX_ERR(0, 228, __pyx_L3_error) }
      }
    } else {
      switch (__pyx_nargs) {
        case  3:
        values[2] = __Pyx_ArgRef_FASTCALL(__pyx_args, 2);
        if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[2])) __PYX_ERR(0, 228, __pyx_L3_error)
        CYTHON_FALLTHROUGH;
        case  2:
        values[1] = __Pyx_ArgRef_FASTCALL(__pyx_args, 1);
        if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[1])) __PYX_ERR(0, 228, __pyx_L3_error)
        CYTHON_FALLTHROUGH;
        case  1:
        values[0] = __Pyx_ArgRef_FASTCALL(__pyx_args, 0);
        if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[0])) __PYX_ERR(0, 228, __pyx_L3_error)
        break;
        default: goto __pyx_L5_argtuple_error;
      }
      if (!values[1]) values[1] = __Pyx_NewRef(((PyObject *)Py_None));
      if (!values[2]) values[2] = __Pyx_NewRef(((PyObject *)Py_None));
    }
    __pyx_v_self = values[0];
    __pyx_v_encoding = values[1];
    __pyx_v_error_handling = values[2];
  }
  goto __pyx_L6_skip;
  __pyx_L5_argtuple_error:;
  __Pyx_RaiseArgtupleInvalid("get_file_object", 0, 1, 3, __pyx_nargs); __PYX_ERR(0, 228, __pyx_L3_error)
  __pyx_L6_skip:;
  goto __pyx_L4_argument_unpacking_done;
  __pyx_L3_error:;
  for (Py_ssize_t __pyx_temp=0; __pyx_temp < (Py_ssize_t)(sizeof(values)/sizeof(values[0])); ++__pyx_temp) {
    Py_XDECREF(values[__pyx_temp]);
  }
  __Pyx_AddTraceback("Cython.Compiler.Scanning.FileSourceDescriptor.get_file_object", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __Pyx_RefNannyFinishContext();
  return NULL;
  __pyx_L4_argument_unpacking_done:;
  __pyx_r = __pyx_pf_6Cython_8Compiler_8Scanning_20FileSourceDescriptor_4get_file_object(__pyx_self, __pyx_v_self, __pyx_v_encoding, __pyx_v_error_handling);

  /* function exit code */
  for (Py_ssize_t __pyx_temp=0; __pyx_temp < (Py_ssize_t)(sizeof(values)/sizeof(values[0])); ++__pyx_temp) {
    Py_XDECREF(values[__pyx_temp]);
  }
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}

static PyObject *__pyx_pf_6Cython_8Compiler_8Scanning_20FileSourceDescriptor_4get_file_object(CYTHON_UNUSED PyObject *__pyx_self, PyObject *__pyx_v_self, PyObject *__pyx_v_encoding, PyObject *__pyx_v_error_handling) {
  PyObject *__pyx_r = NULL;
/* … */
  /* function exit code */
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_t_1);
  __Pyx_XDECREF(__pyx_t_2);
  __Pyx_XDECREF(__pyx_t_3);
  __Pyx_XDECREF(__pyx_t_4);
  __Pyx_AddTraceback("Cython.Compiler.Scanning.FileSourceDescriptor.get_file_object", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_r = NULL;
  __pyx_L0:;
  __Pyx_XGIVEREF(__pyx_r);
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}
/* … */
  __pyx_t_6 = __Pyx_CyFunction_New(&__pyx_mdef_6Cython_8Compiler_8Scanning_20FileSourceDescriptor_5get_file_object, 0, __pyx_mstate_global->__pyx_n_u_FileSourceDescriptor_get_file_ob, NULL, __pyx_mstate_global->__pyx_n_u_Cython_Compiler_Scanning, __pyx_mstate_global->__pyx_d, ((PyObject *)__pyx_mstate_global->__pyx_codeobj_tab[21])); if (unlikely(!__pyx_t_6)) __PYX_ERR(0, 228, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_6);
  #if CYTHON_COMPILING_IN_CPYTHON && PY_VERSION_HEX >= 0x030E0000
  PyUnstable_Object_EnableDeferredRefcount(__pyx_t_6);
  #endif
  __Pyx_CyFunction_SetDefaultsTuple(__pyx_t_6, __pyx_mstate_global->__pyx_tuple[17]);
  if (__Pyx_SetNameInClass(__pyx_t_7, __pyx_mstate_global->__pyx_n_u_get_file_object, __pyx_t_6) < (0)) __PYX_ERR(0, 228, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_6); __pyx_t_6 = 0;
```

</details>

L229  🔴  (score=13)
```python
        return Utils.open_source_file(self.filename, encoding, error_handling)
```
<details><summary>Show generated C (score=13)</summary>

```c
  __Pyx_XDECREF(__pyx_r);
  __pyx_t_2 = NULL;
  __Pyx_GetModuleGlobalName(__pyx_t_3, __pyx_mstate_global->__pyx_n_u_Utils); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 229, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_3);
  __pyx_t_4 = __Pyx_PyObject_GetAttrStr(__pyx_t_3, __pyx_mstate_global->__pyx_n_u_open_source_file); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 229, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_4);
  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
  __pyx_t_3 = __Pyx_PyObject_GetAttrStr(__pyx_v_self, __pyx_mstate_global->__pyx_n_u_filename); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 229, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_3);
  __pyx_t_5 = 1;
  {
    PyObject *__pyx_callargs[4] = {__pyx_t_2, __pyx_t_3, __pyx_v_encoding, __pyx_v_error_handling};
    __pyx_t_1 = __Pyx_PyObject_FastCall((PyObject*)__pyx_t_4, __pyx_callargs+__pyx_t_5, (4-__pyx_t_5) | (__pyx_t_5*__Pyx_PY_VECTORCALL_ARGUMENTS_OFFSET));
    __Pyx_XDECREF(__pyx_t_2); __pyx_t_2 = 0;
    __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
    __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
    if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 229, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_1);
  }
  __pyx_r = __pyx_t_1;
  __pyx_t_1 = 0;
  goto __pyx_L0;
```

</details>

L230  ⚪  (score=0)
```python
```
L231  🔴  (score=36)
```python
    def get_description(self):
```
<details><summary>Show generated C (score=36)</summary>

```c
/* Python wrapper */
static PyObject *__pyx_pw_6Cython_8Compiler_8Scanning_20FileSourceDescriptor_7get_description(PyObject *__pyx_self, 
#if CYTHON_METH_FASTCALL
PyObject *const *__pyx_args, Py_ssize_t __pyx_nargs, PyObject *__pyx_kwds
#else
PyObject *__pyx_args, PyObject *__pyx_kwds
#endif
); /*proto*/
PyDoc_STRVAR(__pyx_doc_6Cython_8Compiler_8Scanning_20FileSourceDescriptor_6get_description, "File: Cython/Compiler/Scanning.py (starting at line 231)");
static PyMethodDef __pyx_mdef_6Cython_8Compiler_8Scanning_20FileSourceDescriptor_7get_description = {"get_description", (PyCFunction)(void(*)(void))(__Pyx_PyCFunction_FastCallWithKeywords)__pyx_pw_6Cython_8Compiler_8Scanning_20FileSourceDescriptor_7get_description, __Pyx_METH_FASTCALL|METH_KEYWORDS, __pyx_doc_6Cython_8Compiler_8Scanning_20FileSourceDescriptor_6get_description};
static PyObject *__pyx_pw_6Cython_8Compiler_8Scanning_20FileSourceDescriptor_7get_description(PyObject *__pyx_self, 
#if CYTHON_METH_FASTCALL
PyObject *const *__pyx_args, Py_ssize_t __pyx_nargs, PyObject *__pyx_kwds
#else
PyObject *__pyx_args, PyObject *__pyx_kwds
#endif
) {
  PyObject *__pyx_v_self = 0;
  #if !CYTHON_METH_FASTCALL
  CYTHON_UNUSED Py_ssize_t __pyx_nargs;
  #endif
  CYTHON_UNUSED PyObject *const *__pyx_kwvalues;
  PyObject *__pyx_r = 0;
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("get_description (wrapper)", 0);
  #if !CYTHON_METH_FASTCALL
  #if CYTHON_ASSUME_SAFE_SIZE
  __pyx_nargs = PyTuple_GET_SIZE(__pyx_args);
  #else
  __pyx_nargs = PyTuple_Size(__pyx_args); if (unlikely(__pyx_nargs < 0)) return NULL;
  #endif
  #endif
  __pyx_kwvalues = __Pyx_KwValues_FASTCALL(__pyx_args, __pyx_nargs);
  {
    PyObject ** const __pyx_pyargnames[] = {&__pyx_mstate_global->__pyx_n_u_self,0};
  PyObject* values[1] = {0};
    const Py_ssize_t __pyx_kwds_len = (__pyx_kwds) ? __Pyx_NumKwargs_FASTCALL(__pyx_kwds) : 0;
    if (unlikely(__pyx_kwds_len) < 0) __PYX_ERR(0, 231, __pyx_L3_error)
    if (__pyx_kwds_len > 0) {
      switch (__pyx_nargs) {
        case  1:
        values[0] = __Pyx_ArgRef_FASTCALL(__pyx_args, 0);
        if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[0])) __PYX_ERR(0, 231, __pyx_L3_error)
        CYTHON_FALLTHROUGH;
        case  0: break;
        default: goto __pyx_L5_argtuple_error;
      }
      const Py_ssize_t kwd_pos_args = __pyx_nargs;
      if (__Pyx_ParseKeywords(__pyx_kwds, __pyx_kwvalues, __pyx_pyargnames, 0, values, kwd_pos_args, __pyx_kwds_len, "get_description", 0) < (0)) __PYX_ERR(0, 231, __pyx_L3_error)
      for (Py_ssize_t i = __pyx_nargs; i < 1; i++) {
        if (unlikely(!values[i])) { __Pyx_RaiseArgtupleInvalid("get_description", 1, 1, 1, i); __PYX_ERR(0, 231, __pyx_L3_error) }
      }
    } else if (unlikely(__pyx_nargs != 1)) {
      goto __pyx_L5_argtuple_error;
    } else {
      values[0] = __Pyx_ArgRef_FASTCALL(__pyx_args, 0);
      if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[0])) __PYX_ERR(0, 231, __pyx_L3_error)
    }
    __pyx_v_self = values[0];
  }
  goto __pyx_L6_skip;
  __pyx_L5_argtuple_error:;
  __Pyx_RaiseArgtupleInvalid("get_description", 1, 1, 1, __pyx_nargs); __PYX_ERR(0, 231, __pyx_L3_error)
  __pyx_L6_skip:;
  goto __pyx_L4_argument_unpacking_done;
  __pyx_L3_error:;
  for (Py_ssize_t __pyx_temp=0; __pyx_temp < (Py_ssize_t)(sizeof(values)/sizeof(values[0])); ++__pyx_temp) {
    Py_XDECREF(values[__pyx_temp]);
  }
  __Pyx_AddTraceback("Cython.Compiler.Scanning.FileSourceDescriptor.get_description", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __Pyx_RefNannyFinishContext();
  return NULL;
  __pyx_L4_argument_unpacking_done:;
  __pyx_r = __pyx_pf_6Cython_8Compiler_8Scanning_20FileSourceDescriptor_6get_description(__pyx_self, __pyx_v_self);
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

static PyObject *__pyx_pf_6Cython_8Compiler_8Scanning_20FileSourceDescriptor_6get_description(CYTHON_UNUSED PyObject *__pyx_self, PyObject *__pyx_v_self) {
  PyObject *__pyx_r = NULL;
/* … */
  /* function exit code */
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_t_1);
  __Pyx_AddTraceback("Cython.Compiler.Scanning.FileSourceDescriptor.get_description", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_r = NULL;
  __pyx_L0:;
  __Pyx_XGIVEREF(__pyx_r);
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}
/* … */
  __pyx_t_6 = __Pyx_CyFunction_New(&__pyx_mdef_6Cython_8Compiler_8Scanning_20FileSourceDescriptor_7get_description, 0, __pyx_mstate_global->__pyx_n_u_FileSourceDescriptor_get_descrip, NULL, __pyx_mstate_global->__pyx_n_u_Cython_Compiler_Scanning, __pyx_mstate_global->__pyx_d, ((PyObject *)__pyx_mstate_global->__pyx_codeobj_tab[22])); if (unlikely(!__pyx_t_6)) __PYX_ERR(0, 231, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_6);
  #if CYTHON_COMPILING_IN_CPYTHON && PY_VERSION_HEX >= 0x030E0000
  PyUnstable_Object_EnableDeferredRefcount(__pyx_t_6);
  #endif
  if (__Pyx_SetNameInClass(__pyx_t_7, __pyx_mstate_global->__pyx_n_u_get_description, __pyx_t_6) < (0)) __PYX_ERR(0, 231, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_6); __pyx_t_6 = 0;
```

</details>

L232  🟡  (score=3)
```python
        return self._short_path_description
```
<details><summary>Show generated C (score=3)</summary>

```c
  __Pyx_XDECREF(__pyx_r);
  __pyx_t_1 = __Pyx_PyObject_GetAttrStr(__pyx_v_self, __pyx_mstate_global->__pyx_n_u_short_path_description); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 232, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __pyx_r = __pyx_t_1;
  __pyx_t_1 = 0;
  goto __pyx_L0;
```

</details>

L233  ⚪  (score=0)
```python
```
L234  🔴  (score=43)
```python
    def get_error_description(self):
```
<details><summary>Show generated C (score=43)</summary>

```c
/* Python wrapper */
static PyObject *__pyx_pw_6Cython_8Compiler_8Scanning_20FileSourceDescriptor_9get_error_description(PyObject *__pyx_self, 
#if CYTHON_METH_FASTCALL
PyObject *const *__pyx_args, Py_ssize_t __pyx_nargs, PyObject *__pyx_kwds
#else
PyObject *__pyx_args, PyObject *__pyx_kwds
#endif
); /*proto*/
PyDoc_STRVAR(__pyx_doc_6Cython_8Compiler_8Scanning_20FileSourceDescriptor_8get_error_description, "File: Cython/Compiler/Scanning.py (starting at line 234)");
static PyMethodDef __pyx_mdef_6Cython_8Compiler_8Scanning_20FileSourceDescriptor_9get_error_description = {"get_error_description", (PyCFunction)(void(*)(void))(__Pyx_PyCFunction_FastCallWithKeywords)__pyx_pw_6Cython_8Compiler_8Scanning_20FileSourceDescriptor_9get_error_description, __Pyx_METH_FASTCALL|METH_KEYWORDS, __pyx_doc_6Cython_8Compiler_8Scanning_20FileSourceDescriptor_8get_error_description};
static PyObject *__pyx_pw_6Cython_8Compiler_8Scanning_20FileSourceDescriptor_9get_error_description(PyObject *__pyx_self, 
#if CYTHON_METH_FASTCALL
PyObject *const *__pyx_args, Py_ssize_t __pyx_nargs, PyObject *__pyx_kwds
#else
PyObject *__pyx_args, PyObject *__pyx_kwds
#endif
) {
  PyObject *__pyx_v_self = 0;
  #if !CYTHON_METH_FASTCALL
  CYTHON_UNUSED Py_ssize_t __pyx_nargs;
  #endif
  CYTHON_UNUSED PyObject *const *__pyx_kwvalues;
  PyObject *__pyx_r = 0;
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("get_error_description (wrapper)", 0);
  #if !CYTHON_METH_FASTCALL
  #if CYTHON_ASSUME_SAFE_SIZE
  __pyx_nargs = PyTuple_GET_SIZE(__pyx_args);
  #else
  __pyx_nargs = PyTuple_Size(__pyx_args); if (unlikely(__pyx_nargs < 0)) return NULL;
  #endif
  #endif
  __pyx_kwvalues = __Pyx_KwValues_FASTCALL(__pyx_args, __pyx_nargs);
  {
    PyObject ** const __pyx_pyargnames[] = {&__pyx_mstate_global->__pyx_n_u_self,0};
  PyObject* values[1] = {0};
    const Py_ssize_t __pyx_kwds_len = (__pyx_kwds) ? __Pyx_NumKwargs_FASTCALL(__pyx_kwds) : 0;
    if (unlikely(__pyx_kwds_len) < 0) __PYX_ERR(0, 234, __pyx_L3_error)
    if (__pyx_kwds_len > 0) {
      switch (__pyx_nargs) {
        case  1:
        values[0] = __Pyx_ArgRef_FASTCALL(__pyx_args, 0);
        if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[0])) __PYX_ERR(0, 234, __pyx_L3_error)
        CYTHON_FALLTHROUGH;
        case  0: break;
        default: goto __pyx_L5_argtuple_error;
      }
      const Py_ssize_t kwd_pos_args = __pyx_nargs;
      if (__Pyx_ParseKeywords(__pyx_kwds, __pyx_kwvalues, __pyx_pyargnames, 0, values, kwd_pos_args, __pyx_kwds_len, "get_error_description", 0) < (0)) __PYX_ERR(0, 234, __pyx_L3_error)
      for (Py_ssize_t i = __pyx_nargs; i < 1; i++) {
        if (unlikely(!values[i])) { __Pyx_RaiseArgtupleInvalid("get_error_description", 1, 1, 1, i); __PYX_ERR(0, 234, __pyx_L3_error) }
      }
    } else if (unlikely(__pyx_nargs != 1)) {
      goto __pyx_L5_argtuple_error;
    } else {
      values[0] = __Pyx_ArgRef_FASTCALL(__pyx_args, 0);
      if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[0])) __PYX_ERR(0, 234, __pyx_L3_error)
    }
    __pyx_v_self = values[0];
  }
  goto __pyx_L6_skip;
  __pyx_L5_argtuple_error:;
  __Pyx_RaiseArgtupleInvalid("get_error_description", 1, 1, 1, __pyx_nargs); __PYX_ERR(0, 234, __pyx_L3_error)
  __pyx_L6_skip:;
  goto __pyx_L4_argument_unpacking_done;
  __pyx_L3_error:;
  for (Py_ssize_t __pyx_temp=0; __pyx_temp < (Py_ssize_t)(sizeof(values)/sizeof(values[0])); ++__pyx_temp) {
    Py_XDECREF(values[__pyx_temp]);
  }
  __Pyx_AddTraceback("Cython.Compiler.Scanning.FileSourceDescriptor.get_error_description", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __Pyx_RefNannyFinishContext();
  return NULL;
  __pyx_L4_argument_unpacking_done:;
  __pyx_r = __pyx_pf_6Cython_8Compiler_8Scanning_20FileSourceDescriptor_8get_error_description(__pyx_self, __pyx_v_self);
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

static PyObject *__pyx_pf_6Cython_8Compiler_8Scanning_20FileSourceDescriptor_8get_error_description(CYTHON_UNUSED PyObject *__pyx_self, PyObject *__pyx_v_self) {
  PyObject *__pyx_v_path = NULL;
  PyObject *__pyx_v_cwd = NULL;
  PyObject *__pyx_r = NULL;
/* … */
  /* function exit code */
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_t_1);
  __Pyx_XDECREF(__pyx_t_2);
  __Pyx_XDECREF(__pyx_t_3);
  __Pyx_XDECREF(__pyx_t_4);
  __Pyx_XDECREF(__pyx_t_5);
  __Pyx_XDECREF(__pyx_t_7);
  __Pyx_AddTraceback("Cython.Compiler.Scanning.FileSourceDescriptor.get_error_description", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_r = NULL;
  __pyx_L0:;
  __Pyx_XDECREF(__pyx_v_path);
  __Pyx_XDECREF(__pyx_v_cwd);
  __Pyx_XGIVEREF(__pyx_r);
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}
/* … */
  __pyx_t_6 = __Pyx_CyFunction_New(&__pyx_mdef_6Cython_8Compiler_8Scanning_20FileSourceDescriptor_9get_error_description, 0, __pyx_mstate_global->__pyx_n_u_FileSourceDescriptor_get_error_d, NULL, __pyx_mstate_global->__pyx_n_u_Cython_Compiler_Scanning, __pyx_mstate_global->__pyx_d, ((PyObject *)__pyx_mstate_global->__pyx_codeobj_tab[23])); if (unlikely(!__pyx_t_6)) __PYX_ERR(0, 234, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_6);
  #if CYTHON_COMPILING_IN_CPYTHON && PY_VERSION_HEX >= 0x030E0000
  PyUnstable_Object_EnableDeferredRefcount(__pyx_t_6);
  #endif
  if (__Pyx_SetNameInClass(__pyx_t_7, __pyx_mstate_global->__pyx_n_u_get_error_description, __pyx_t_6) < (0)) __PYX_ERR(0, 234, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_6); __pyx_t_6 = 0;
```

</details>

L235  🟡  (score=2)
```python
        path = self.filename
```
<details><summary>Show generated C (score=2)</summary>

```c
  __pyx_t_1 = __Pyx_PyObject_GetAttrStr(__pyx_v_self, __pyx_mstate_global->__pyx_n_u_filename); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 235, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __pyx_v_path = __pyx_t_1;
  __pyx_t_1 = 0;
```

</details>

L236  🔴  (score=26)
```python
        cwd = Utils.decode_filename(os.getcwd() + os.path.sep)
```
<details><summary>Show generated C (score=26)</summary>

```c
  __pyx_t_2 = NULL;
  __Pyx_GetModuleGlobalName(__pyx_t_3, __pyx_mstate_global->__pyx_n_u_Utils); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 236, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_3);
  __pyx_t_4 = __Pyx_PyObject_GetAttrStr(__pyx_t_3, __pyx_mstate_global->__pyx_n_u_decode_filename); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 236, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_4);
  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
  __pyx_t_5 = __pyx_v_6Cython_8Compiler_8Scanning_os;
  __Pyx_INCREF(__pyx_t_5);
  __pyx_t_6 = 0;
  {
    PyObject *__pyx_callargs[2] = {__pyx_t_5, NULL};
    __pyx_t_3 = __Pyx_PyObject_FastCallMethod((PyObject*)__pyx_mstate_global->__pyx_n_u_getcwd, __pyx_callargs+__pyx_t_6, (1-__pyx_t_6) | (1*__Pyx_PY_VECTORCALL_ARGUMENTS_OFFSET));
    __Pyx_XDECREF(__pyx_t_5); __pyx_t_5 = 0;
    if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 236, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_3);
  }
  __pyx_t_5 = __Pyx_PyObject_GetAttrStr(__pyx_v_6Cython_8Compiler_8Scanning_os, __pyx_mstate_global->__pyx_n_u_path); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 236, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_5);
  __pyx_t_7 = __Pyx_PyObject_GetAttrStr(__pyx_t_5, __pyx_mstate_global->__pyx_n_u_sep); if (unlikely(!__pyx_t_7)) __PYX_ERR(0, 236, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_7);
  __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
  __pyx_t_5 = PyNumber_Add(__pyx_t_3, __pyx_t_7); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 236, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_5);
  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
  __Pyx_DECREF(__pyx_t_7); __pyx_t_7 = 0;
  __pyx_t_6 = 1;
  {
    PyObject *__pyx_callargs[2] = {__pyx_t_2, __pyx_t_5};
    __pyx_t_1 = __Pyx_PyObject_FastCall((PyObject*)__pyx_t_4, __pyx_callargs+__pyx_t_6, (2-__pyx_t_6) | (__pyx_t_6*__Pyx_PY_VECTORCALL_ARGUMENTS_OFFSET));
    __Pyx_XDECREF(__pyx_t_2); __pyx_t_2 = 0;
    __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
    __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
    if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 236, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_1);
  }
  __pyx_v_cwd = __pyx_t_1;
  __pyx_t_1 = 0;
```

</details>

L237  🟠  (score=7)
```python
        if path.startswith(cwd):
```
<details><summary>Show generated C (score=7)</summary>

```c
  __pyx_t_4 = __pyx_v_path;
  __Pyx_INCREF(__pyx_t_4);
  __pyx_t_6 = 0;
  {
    PyObject *__pyx_callargs[2] = {__pyx_t_4, __pyx_v_cwd};
    __pyx_t_1 = __Pyx_PyObject_FastCallMethod((PyObject*)__pyx_mstate_global->__pyx_n_u_startswith, __pyx_callargs+__pyx_t_6, (2-__pyx_t_6) | (1*__Pyx_PY_VECTORCALL_ARGUMENTS_OFFSET));
    __Pyx_XDECREF(__pyx_t_4); __pyx_t_4 = 0;
    if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 237, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_1);
  }
  __pyx_t_8 = __Pyx_PyObject_IsTrue(__pyx_t_1); if (unlikely((__pyx_t_8 < 0))) __PYX_ERR(0, 237, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  if (__pyx_t_8) {
/* … */
  }
```

</details>

L238  🟠  (score=8)
```python
            return path[len(cwd):]
```
<details><summary>Show generated C (score=8)</summary>

```c
    __Pyx_XDECREF(__pyx_r);
    __pyx_t_9 = PyObject_Length(__pyx_v_cwd); if (unlikely(__pyx_t_9 == ((Py_ssize_t)-1))) __PYX_ERR(0, 238, __pyx_L1_error)
    __pyx_t_1 = __Pyx_PyObject_GetSlice(__pyx_v_path, __pyx_t_9, 0, NULL, NULL, NULL, 1, 0, 0); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 238, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_1);
    __pyx_r = __pyx_t_1;
    __pyx_t_1 = 0;
    goto __pyx_L0;
```

</details>

L239  🟡  (score=2)
```python
        return path
```
<details><summary>Show generated C (score=2)</summary>

```c
  __Pyx_XDECREF(__pyx_r);
  __Pyx_INCREF(__pyx_v_path);
  __pyx_r = __pyx_v_path;
  goto __pyx_L0;
```

</details>

L240  ⚪  (score=0)
```python
```
L241  🔴  (score=36)
```python
    def get_filenametable_entry(self):
```
<details><summary>Show generated C (score=36)</summary>

```c
/* Python wrapper */
static PyObject *__pyx_pw_6Cython_8Compiler_8Scanning_20FileSourceDescriptor_11get_filenametable_entry(PyObject *__pyx_self, 
#if CYTHON_METH_FASTCALL
PyObject *const *__pyx_args, Py_ssize_t __pyx_nargs, PyObject *__pyx_kwds
#else
PyObject *__pyx_args, PyObject *__pyx_kwds
#endif
); /*proto*/
PyDoc_STRVAR(__pyx_doc_6Cython_8Compiler_8Scanning_20FileSourceDescriptor_10get_filenametable_entry, "File: Cython/Compiler/Scanning.py (starting at line 241)");
static PyMethodDef __pyx_mdef_6Cython_8Compiler_8Scanning_20FileSourceDescriptor_11get_filenametable_entry = {"get_filenametable_entry", (PyCFunction)(void(*)(void))(__Pyx_PyCFunction_FastCallWithKeywords)__pyx_pw_6Cython_8Compiler_8Scanning_20FileSourceDescriptor_11get_filenametable_entry, __Pyx_METH_FASTCALL|METH_KEYWORDS, __pyx_doc_6Cython_8Compiler_8Scanning_20FileSourceDescriptor_10get_filenametable_entry};
static PyObject *__pyx_pw_6Cython_8Compiler_8Scanning_20FileSourceDescriptor_11get_filenametable_entry(PyObject *__pyx_self, 
#if CYTHON_METH_FASTCALL
PyObject *const *__pyx_args, Py_ssize_t __pyx_nargs, PyObject *__pyx_kwds
#else
PyObject *__pyx_args, PyObject *__pyx_kwds
#endif
) {
  PyObject *__pyx_v_self = 0;
  #if !CYTHON_METH_FASTCALL
  CYTHON_UNUSED Py_ssize_t __pyx_nargs;
  #endif
  CYTHON_UNUSED PyObject *const *__pyx_kwvalues;
  PyObject *__pyx_r = 0;
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("get_filenametable_entry (wrapper)", 0);
  #if !CYTHON_METH_FASTCALL
  #if CYTHON_ASSUME_SAFE_SIZE
  __pyx_nargs = PyTuple_GET_SIZE(__pyx_args);
  #else
  __pyx_nargs = PyTuple_Size(__pyx_args); if (unlikely(__pyx_nargs < 0)) return NULL;
  #endif
  #endif
  __pyx_kwvalues = __Pyx_KwValues_FASTCALL(__pyx_args, __pyx_nargs);
  {
    PyObject ** const __pyx_pyargnames[] = {&__pyx_mstate_global->__pyx_n_u_self,0};
  PyObject* values[1] = {0};
    const Py_ssize_t __pyx_kwds_len = (__pyx_kwds) ? __Pyx_NumKwargs_FASTCALL(__pyx_kwds) : 0;
    if (unlikely(__pyx_kwds_len) < 0) __PYX_ERR(0, 241, __pyx_L3_error)
    if (__pyx_kwds_len > 0) {
      switch (__pyx_nargs) {
        case  1:
        values[0] = __Pyx_ArgRef_FASTCALL(__pyx_args, 0);
        if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[0])) __PYX_ERR(0, 241, __pyx_L3_error)
        CYTHON_FALLTHROUGH;
        case  0: break;
        default: goto __pyx_L5_argtuple_error;
      }
      const Py_ssize_t kwd_pos_args = __pyx_nargs;
      if (__Pyx_ParseKeywords(__pyx_kwds, __pyx_kwvalues, __pyx_pyargnames, 0, values, kwd_pos_args, __pyx_kwds_len, "get_filenametable_entry", 0) < (0)) __PYX_ERR(0, 241, __pyx_L3_error)
      for (Py_ssize_t i = __pyx_nargs; i < 1; i++) {
        if (unlikely(!values[i])) { __Pyx_RaiseArgtupleInvalid("get_filenametable_entry", 1, 1, 1, i); __PYX_ERR(0, 241, __pyx_L3_error) }
      }
    } else if (unlikely(__pyx_nargs != 1)) {
      goto __pyx_L5_argtuple_error;
    } else {
      values[0] = __Pyx_ArgRef_FASTCALL(__pyx_args, 0);
      if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[0])) __PYX_ERR(0, 241, __pyx_L3_error)
    }
    __pyx_v_self = values[0];
  }
  goto __pyx_L6_skip;
  __pyx_L5_argtuple_error:;
  __Pyx_RaiseArgtupleInvalid("get_filenametable_entry", 1, 1, 1, __pyx_nargs); __PYX_ERR(0, 241, __pyx_L3_error)
  __pyx_L6_skip:;
  goto __pyx_L4_argument_unpacking_done;
  __pyx_L3_error:;
  for (Py_ssize_t __pyx_temp=0; __pyx_temp < (Py_ssize_t)(sizeof(values)/sizeof(values[0])); ++__pyx_temp) {
    Py_XDECREF(values[__pyx_temp]);
  }
  __Pyx_AddTraceback("Cython.Compiler.Scanning.FileSourceDescriptor.get_filenametable_entry", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __Pyx_RefNannyFinishContext();
  return NULL;
  __pyx_L4_argument_unpacking_done:;
  __pyx_r = __pyx_pf_6Cython_8Compiler_8Scanning_20FileSourceDescriptor_10get_filenametable_entry(__pyx_self, __pyx_v_self);
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

static PyObject *__pyx_pf_6Cython_8Compiler_8Scanning_20FileSourceDescriptor_10get_filenametable_entry(CYTHON_UNUSED PyObject *__pyx_self, PyObject *__pyx_v_self) {
  PyObject *__pyx_r = NULL;
/* … */
  /* function exit code */
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_t_1);
  __Pyx_AddTraceback("Cython.Compiler.Scanning.FileSourceDescriptor.get_filenametable_entry", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_r = NULL;
  __pyx_L0:;
  __Pyx_XGIVEREF(__pyx_r);
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}
/* … */
  __pyx_t_6 = __Pyx_CyFunction_New(&__pyx_mdef_6Cython_8Compiler_8Scanning_20FileSourceDescriptor_11get_filenametable_entry, 0, __pyx_mstate_global->__pyx_n_u_FileSourceDescriptor_get_filenam, NULL, __pyx_mstate_global->__pyx_n_u_Cython_Compiler_Scanning, __pyx_mstate_global->__pyx_d, ((PyObject *)__pyx_mstate_global->__pyx_codeobj_tab[24])); if (unlikely(!__pyx_t_6)) __PYX_ERR(0, 241, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_6);
  #if CYTHON_COMPILING_IN_CPYTHON && PY_VERSION_HEX >= 0x030E0000
  PyUnstable_Object_EnableDeferredRefcount(__pyx_t_6);
  #endif
  if (__Pyx_SetNameInClass(__pyx_t_7, __pyx_mstate_global->__pyx_n_u_get_filenametable_entry, __pyx_t_6) < (0)) __PYX_ERR(0, 241, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_6); __pyx_t_6 = 0;
```

</details>

L242  🟡  (score=3)
```python
        return self.file_path
```
<details><summary>Show generated C (score=3)</summary>

```c
  __Pyx_XDECREF(__pyx_r);
  __pyx_t_1 = __Pyx_PyObject_GetAttrStr(__pyx_v_self, __pyx_mstate_global->__pyx_n_u_file_path); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 242, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __pyx_r = __pyx_t_1;
  __pyx_t_1 = 0;
  goto __pyx_L0;
```

</details>

L243  ⚪  (score=0)
```python
```
L244  🔴  (score=43)
```python
    def __eq__(self, other):
```
<details><summary>Show generated C (score=43)</summary>

```c
/* Python wrapper */
static PyObject *__pyx_pw_6Cython_8Compiler_8Scanning_20FileSourceDescriptor_13__eq__(PyObject *__pyx_self, 
#if CYTHON_METH_FASTCALL
PyObject *const *__pyx_args, Py_ssize_t __pyx_nargs, PyObject *__pyx_kwds
#else
PyObject *__pyx_args, PyObject *__pyx_kwds
#endif
); /*proto*/
PyDoc_STRVAR(__pyx_doc_6Cython_8Compiler_8Scanning_20FileSourceDescriptor_12__eq__, "File: Cython/Compiler/Scanning.py (starting at line 244)");
static PyMethodDef __pyx_mdef_6Cython_8Compiler_8Scanning_20FileSourceDescriptor_13__eq__ = {"__eq__", (PyCFunction)(void(*)(void))(__Pyx_PyCFunction_FastCallWithKeywords)__pyx_pw_6Cython_8Compiler_8Scanning_20FileSourceDescriptor_13__eq__, __Pyx_METH_FASTCALL|METH_KEYWORDS, __pyx_doc_6Cython_8Compiler_8Scanning_20FileSourceDescriptor_12__eq__};
static PyObject *__pyx_pw_6Cython_8Compiler_8Scanning_20FileSourceDescriptor_13__eq__(PyObject *__pyx_self, 
#if CYTHON_METH_FASTCALL
PyObject *const *__pyx_args, Py_ssize_t __pyx_nargs, PyObject *__pyx_kwds
#else
PyObject *__pyx_args, PyObject *__pyx_kwds
#endif
) {
  PyObject *__pyx_v_self = 0;
  PyObject *__pyx_v_other = 0;
  #if !CYTHON_METH_FASTCALL
  CYTHON_UNUSED Py_ssize_t __pyx_nargs;
  #endif
  CYTHON_UNUSED PyObject *const *__pyx_kwvalues;
  PyObject *__pyx_r = 0;
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("__eq__ (wrapper)", 0);
  #if !CYTHON_METH_FASTCALL
  #if CYTHON_ASSUME_SAFE_SIZE
  __pyx_nargs = PyTuple_GET_SIZE(__pyx_args);
  #else
  __pyx_nargs = PyTuple_Size(__pyx_args); if (unlikely(__pyx_nargs < 0)) return NULL;
  #endif
  #endif
  __pyx_kwvalues = __Pyx_KwValues_FASTCALL(__pyx_args, __pyx_nargs);
  {
    PyObject ** const __pyx_pyargnames[] = {&__pyx_mstate_global->__pyx_n_u_self,&__pyx_mstate_global->__pyx_n_u_other,0};
  PyObject* values[2] = {0,0};
    const Py_ssize_t __pyx_kwds_len = (__pyx_kwds) ? __Pyx_NumKwargs_FASTCALL(__pyx_kwds) : 0;
    if (unlikely(__pyx_kwds_len) < 0) __PYX_ERR(0, 244, __pyx_L3_error)
    if (__pyx_kwds_len > 0) {
      switch (__pyx_nargs) {
        case  2:
        values[1] = __Pyx_ArgRef_FASTCALL(__pyx_args, 1);
        if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[1])) __PYX_ERR(0, 244, __pyx_L3_error)
        CYTHON_FALLTHROUGH;
        case  1:
        values[0] = __Pyx_ArgRef_FASTCALL(__pyx_args, 0);
        if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[0])) __PYX_ERR(0, 244, __pyx_L3_error)
        CYTHON_FALLTHROUGH;
        case  0: break;
        default: goto __pyx_L5_argtuple_error;
      }
      const Py_ssize_t kwd_pos_args = __pyx_nargs;
      if (__Pyx_ParseKeywords(__pyx_kwds, __pyx_kwvalues, __pyx_pyargnames, 0, values, kwd_pos_args, __pyx_kwds_len, "__eq__", 0) < (0)) __PYX_ERR(0, 244, __pyx_L3_error)
      for (Py_ssize_t i = __pyx_nargs; i < 2; i++) {
        if (unlikely(!values[i])) { __Pyx_RaiseArgtupleInvalid("__eq__", 1, 2, 2, i); __PYX_ERR(0, 244, __pyx_L3_error) }
      }
    } else if (unlikely(__pyx_nargs != 2)) {
      goto __pyx_L5_argtuple_error;
    } else {
      values[0] = __Pyx_ArgRef_FASTCALL(__pyx_args, 0);
      if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[0])) __PYX_ERR(0, 244, __pyx_L3_error)
      values[1] = __Pyx_ArgRef_FASTCALL(__pyx_args, 1);
      if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[1])) __PYX_ERR(0, 244, __pyx_L3_error)
    }
    __pyx_v_self = values[0];
    __pyx_v_other = values[1];
  }
  goto __pyx_L6_skip;
  __pyx_L5_argtuple_error:;
  __Pyx_RaiseArgtupleInvalid("__eq__", 1, 2, 2, __pyx_nargs); __PYX_ERR(0, 244, __pyx_L3_error)
  __pyx_L6_skip:;
  goto __pyx_L4_argument_unpacking_done;
  __pyx_L3_error:;
  for (Py_ssize_t __pyx_temp=0; __pyx_temp < (Py_ssize_t)(sizeof(values)/sizeof(values[0])); ++__pyx_temp) {
    Py_XDECREF(values[__pyx_temp]);
  }
  __Pyx_AddTraceback("Cython.Compiler.Scanning.FileSourceDescriptor.__eq__", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __Pyx_RefNannyFinishContext();
  return NULL;
  __pyx_L4_argument_unpacking_done:;
  __pyx_r = __pyx_pf_6Cython_8Compiler_8Scanning_20FileSourceDescriptor_12__eq__(__pyx_self, __pyx_v_self, __pyx_v_other);
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

static PyObject *__pyx_pf_6Cython_8Compiler_8Scanning_20FileSourceDescriptor_12__eq__(CYTHON_UNUSED PyObject *__pyx_self, PyObject *__pyx_v_self, PyObject *__pyx_v_other) {
  PyObject *__pyx_r = NULL;
/* … */
  /* function exit code */
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_t_1);
  __Pyx_XDECREF(__pyx_t_2);
  __Pyx_XDECREF(__pyx_t_4);
  __Pyx_XDECREF(__pyx_t_5);
  __Pyx_AddTraceback("Cython.Compiler.Scanning.FileSourceDescriptor.__eq__", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_r = NULL;
  __pyx_L0:;
  __Pyx_XGIVEREF(__pyx_r);
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}
/* … */
  __pyx_t_6 = __Pyx_CyFunction_New(&__pyx_mdef_6Cython_8Compiler_8Scanning_20FileSourceDescriptor_13__eq__, 0, __pyx_mstate_global->__pyx_n_u_FileSourceDescriptor___eq, NULL, __pyx_mstate_global->__pyx_n_u_Cython_Compiler_Scanning, __pyx_mstate_global->__pyx_d, ((PyObject *)__pyx_mstate_global->__pyx_codeobj_tab[25])); if (unlikely(!__pyx_t_6)) __PYX_ERR(0, 244, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_6);
  #if CYTHON_COMPILING_IN_CPYTHON && PY_VERSION_HEX >= 0x030E0000
  PyUnstable_Object_EnableDeferredRefcount(__pyx_t_6);
  #endif
  if (__Pyx_SetNameInClass(__pyx_t_7, __pyx_mstate_global->__pyx_n_u_eq, __pyx_t_6) < (0)) __PYX_ERR(0, 244, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_6); __pyx_t_6 = 0;
```

</details>

L245  🔴  (score=24)
```python
        return isinstance(other, FileSourceDescriptor) and self.filename == other.filename
```
<details><summary>Show generated C (score=24)</summary>

```c
  __Pyx_XDECREF(__pyx_r);
  __Pyx_GetModuleGlobalName(__pyx_t_2, __pyx_mstate_global->__pyx_n_u_FileSourceDescriptor); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 245, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __pyx_t_3 = PyObject_IsInstance(__pyx_v_other, __pyx_t_2); if (unlikely(__pyx_t_3 == ((int)-1))) __PYX_ERR(0, 245, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  if (__pyx_t_3) {
  } else {
    __pyx_t_2 = __Pyx_PyBool_FromLong(__pyx_t_3); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 245, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_2);
    __pyx_t_1 = __pyx_t_2;
    __pyx_t_2 = 0;
    goto __pyx_L3_bool_binop_done;
  }
  __pyx_t_2 = __Pyx_PyObject_GetAttrStr(__pyx_v_self, __pyx_mstate_global->__pyx_n_u_filename); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 245, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __pyx_t_4 = __Pyx_PyObject_GetAttrStr(__pyx_v_other, __pyx_mstate_global->__pyx_n_u_filename); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 245, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_4);
  __pyx_t_5 = PyObject_RichCompare(__pyx_t_2, __pyx_t_4, Py_EQ); __Pyx_XGOTREF(__pyx_t_5); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 245, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
  __Pyx_INCREF(__pyx_t_5);
  __pyx_t_1 = __pyx_t_5;
  __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
  __pyx_L3_bool_binop_done:;
  __pyx_r = __pyx_t_1;
  __pyx_t_1 = 0;
  goto __pyx_L0;
```

</details>

L246  ⚪  (score=0)
```python
```
L247  🔴  (score=36)
```python
    def __hash__(self):
```
<details><summary>Show generated C (score=36)</summary>

```c
/* Python wrapper */
static PyObject *__pyx_pw_6Cython_8Compiler_8Scanning_20FileSourceDescriptor_15__hash__(PyObject *__pyx_self, 
#if CYTHON_METH_FASTCALL
PyObject *const *__pyx_args, Py_ssize_t __pyx_nargs, PyObject *__pyx_kwds
#else
PyObject *__pyx_args, PyObject *__pyx_kwds
#endif
); /*proto*/
PyDoc_STRVAR(__pyx_doc_6Cython_8Compiler_8Scanning_20FileSourceDescriptor_14__hash__, "File: Cython/Compiler/Scanning.py (starting at line 247)");
static PyMethodDef __pyx_mdef_6Cython_8Compiler_8Scanning_20FileSourceDescriptor_15__hash__ = {"__hash__", (PyCFunction)(void(*)(void))(__Pyx_PyCFunction_FastCallWithKeywords)__pyx_pw_6Cython_8Compiler_8Scanning_20FileSourceDescriptor_15__hash__, __Pyx_METH_FASTCALL|METH_KEYWORDS, __pyx_doc_6Cython_8Compiler_8Scanning_20FileSourceDescriptor_14__hash__};
static PyObject *__pyx_pw_6Cython_8Compiler_8Scanning_20FileSourceDescriptor_15__hash__(PyObject *__pyx_self, 
#if CYTHON_METH_FASTCALL
PyObject *const *__pyx_args, Py_ssize_t __pyx_nargs, PyObject *__pyx_kwds
#else
PyObject *__pyx_args, PyObject *__pyx_kwds
#endif
) {
  PyObject *__pyx_v_self = 0;
  #if !CYTHON_METH_FASTCALL
  CYTHON_UNUSED Py_ssize_t __pyx_nargs;
  #endif
  CYTHON_UNUSED PyObject *const *__pyx_kwvalues;
  PyObject *__pyx_r = 0;
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("__hash__ (wrapper)", 0);
  #if !CYTHON_METH_FASTCALL
  #if CYTHON_ASSUME_SAFE_SIZE
  __pyx_nargs = PyTuple_GET_SIZE(__pyx_args);
  #else
  __pyx_nargs = PyTuple_Size(__pyx_args); if (unlikely(__pyx_nargs < 0)) return NULL;
  #endif
  #endif
  __pyx_kwvalues = __Pyx_KwValues_FASTCALL(__pyx_args, __pyx_nargs);
  {
    PyObject ** const __pyx_pyargnames[] = {&__pyx_mstate_global->__pyx_n_u_self,0};
  PyObject* values[1] = {0};
    const Py_ssize_t __pyx_kwds_len = (__pyx_kwds) ? __Pyx_NumKwargs_FASTCALL(__pyx_kwds) : 0;
    if (unlikely(__pyx_kwds_len) < 0) __PYX_ERR(0, 247, __pyx_L3_error)
    if (__pyx_kwds_len > 0) {
      switch (__pyx_nargs) {
        case  1:
        values[0] = __Pyx_ArgRef_FASTCALL(__pyx_args, 0);
        if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[0])) __PYX_ERR(0, 247, __pyx_L3_error)
        CYTHON_FALLTHROUGH;
        case  0: break;
        default: goto __pyx_L5_argtuple_error;
      }
      const Py_ssize_t kwd_pos_args = __pyx_nargs;
      if (__Pyx_ParseKeywords(__pyx_kwds, __pyx_kwvalues, __pyx_pyargnames, 0, values, kwd_pos_args, __pyx_kwds_len, "__hash__", 0) < (0)) __PYX_ERR(0, 247, __pyx_L3_error)
      for (Py_ssize_t i = __pyx_nargs; i < 1; i++) {
        if (unlikely(!values[i])) { __Pyx_RaiseArgtupleInvalid("__hash__", 1, 1, 1, i); __PYX_ERR(0, 247, __pyx_L3_error) }
      }
    } else if (unlikely(__pyx_nargs != 1)) {
      goto __pyx_L5_argtuple_error;
    } else {
      values[0] = __Pyx_ArgRef_FASTCALL(__pyx_args, 0);
      if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[0])) __PYX_ERR(0, 247, __pyx_L3_error)
    }
    __pyx_v_self = values[0];
  }
  goto __pyx_L6_skip;
  __pyx_L5_argtuple_error:;
  __Pyx_RaiseArgtupleInvalid("__hash__", 1, 1, 1, __pyx_nargs); __PYX_ERR(0, 247, __pyx_L3_error)
  __pyx_L6_skip:;
  goto __pyx_L4_argument_unpacking_done;
  __pyx_L3_error:;
  for (Py_ssize_t __pyx_temp=0; __pyx_temp < (Py_ssize_t)(sizeof(values)/sizeof(values[0])); ++__pyx_temp) {
    Py_XDECREF(values[__pyx_temp]);
  }
  __Pyx_AddTraceback("Cython.Compiler.Scanning.FileSourceDescriptor.__hash__", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __Pyx_RefNannyFinishContext();
  return NULL;
  __pyx_L4_argument_unpacking_done:;
  __pyx_r = __pyx_pf_6Cython_8Compiler_8Scanning_20FileSourceDescriptor_14__hash__(__pyx_self, __pyx_v_self);
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

static PyObject *__pyx_pf_6Cython_8Compiler_8Scanning_20FileSourceDescriptor_14__hash__(CYTHON_UNUSED PyObject *__pyx_self, PyObject *__pyx_v_self) {
  PyObject *__pyx_r = NULL;
/* … */
  /* function exit code */
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_t_1);
  __Pyx_AddTraceback("Cython.Compiler.Scanning.FileSourceDescriptor.__hash__", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_r = NULL;
  __pyx_L0:;
  __Pyx_XGIVEREF(__pyx_r);
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}
/* … */
  __pyx_t_6 = __Pyx_CyFunction_New(&__pyx_mdef_6Cython_8Compiler_8Scanning_20FileSourceDescriptor_15__hash__, 0, __pyx_mstate_global->__pyx_n_u_FileSourceDescriptor___hash, NULL, __pyx_mstate_global->__pyx_n_u_Cython_Compiler_Scanning, __pyx_mstate_global->__pyx_d, ((PyObject *)__pyx_mstate_global->__pyx_codeobj_tab[26])); if (unlikely(!__pyx_t_6)) __PYX_ERR(0, 247, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_6);
  #if CYTHON_COMPILING_IN_CPYTHON && PY_VERSION_HEX >= 0x030E0000
  PyUnstable_Object_EnableDeferredRefcount(__pyx_t_6);
  #endif
  if (__Pyx_SetNameInClass(__pyx_t_7, __pyx_mstate_global->__pyx_n_u_hash_2, __pyx_t_6) < (0)) __PYX_ERR(0, 247, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_6); __pyx_t_6 = 0;
```

</details>

L248  🔴  (score=11)
```python
        return hash(self.filename)
```
<details><summary>Show generated C (score=11)</summary>

```c
  __Pyx_XDECREF(__pyx_r);
  __pyx_t_1 = __Pyx_PyObject_GetAttrStr(__pyx_v_self, __pyx_mstate_global->__pyx_n_u_filename); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 248, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __pyx_t_2 = PyObject_Hash(__pyx_t_1); if (unlikely(__pyx_t_2 == ((Py_hash_t)-1))) __PYX_ERR(0, 248, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __pyx_t_1 = __Pyx_PyLong_FromHash_t(__pyx_t_2); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 248, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __pyx_r = __pyx_t_1;
  __pyx_t_1 = 0;
  goto __pyx_L0;
```

</details>

L249  ⚪  (score=0)
```python
```
L250  🔴  (score=37)
```python
    def __repr__(self):
```
<details><summary>Show generated C (score=37)</summary>

```c
/* Python wrapper */
static PyObject *__pyx_pw_6Cython_8Compiler_8Scanning_20FileSourceDescriptor_17__repr__(PyObject *__pyx_self, 
#if CYTHON_METH_FASTCALL
PyObject *const *__pyx_args, Py_ssize_t __pyx_nargs, PyObject *__pyx_kwds
#else
PyObject *__pyx_args, PyObject *__pyx_kwds
#endif
); /*proto*/
PyDoc_STRVAR(__pyx_doc_6Cython_8Compiler_8Scanning_20FileSourceDescriptor_16__repr__, "File: Cython/Compiler/Scanning.py (starting at line 250)");
static PyMethodDef __pyx_mdef_6Cython_8Compiler_8Scanning_20FileSourceDescriptor_17__repr__ = {"__repr__", (PyCFunction)(void(*)(void))(__Pyx_PyCFunction_FastCallWithKeywords)__pyx_pw_6Cython_8Compiler_8Scanning_20FileSourceDescriptor_17__repr__, __Pyx_METH_FASTCALL|METH_KEYWORDS, __pyx_doc_6Cython_8Compiler_8Scanning_20FileSourceDescriptor_16__repr__};
static PyObject *__pyx_pw_6Cython_8Compiler_8Scanning_20FileSourceDescriptor_17__repr__(PyObject *__pyx_self, 
#if CYTHON_METH_FASTCALL
PyObject *const *__pyx_args, Py_ssize_t __pyx_nargs, PyObject *__pyx_kwds
#else
PyObject *__pyx_args, PyObject *__pyx_kwds
#endif
) {
  PyObject *__pyx_v_self = 0;
  #if !CYTHON_METH_FASTCALL
  CYTHON_UNUSED Py_ssize_t __pyx_nargs;
  #endif
  CYTHON_UNUSED PyObject *const *__pyx_kwvalues;
  PyObject *__pyx_r = 0;
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("__repr__ (wrapper)", 0);
  #if !CYTHON_METH_FASTCALL
  #if CYTHON_ASSUME_SAFE_SIZE
  __pyx_nargs = PyTuple_GET_SIZE(__pyx_args);
  #else
  __pyx_nargs = PyTuple_Size(__pyx_args); if (unlikely(__pyx_nargs < 0)) return NULL;
  #endif
  #endif
  __pyx_kwvalues = __Pyx_KwValues_FASTCALL(__pyx_args, __pyx_nargs);
  {
    PyObject ** const __pyx_pyargnames[] = {&__pyx_mstate_global->__pyx_n_u_self,0};
  PyObject* values[1] = {0};
    const Py_ssize_t __pyx_kwds_len = (__pyx_kwds) ? __Pyx_NumKwargs_FASTCALL(__pyx_kwds) : 0;
    if (unlikely(__pyx_kwds_len) < 0) __PYX_ERR(0, 250, __pyx_L3_error)
    if (__pyx_kwds_len > 0) {
      switch (__pyx_nargs) {
        case  1:
        values[0] = __Pyx_ArgRef_FASTCALL(__pyx_args, 0);
        if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[0])) __PYX_ERR(0, 250, __pyx_L3_error)
        CYTHON_FALLTHROUGH;
        case  0: break;
        default: goto __pyx_L5_argtuple_error;
      }
      const Py_ssize_t kwd_pos_args = __pyx_nargs;
      if (__Pyx_ParseKeywords(__pyx_kwds, __pyx_kwvalues, __pyx_pyargnames, 0, values, kwd_pos_args, __pyx_kwds_len, "__repr__", 0) < (0)) __PYX_ERR(0, 250, __pyx_L3_error)
      for (Py_ssize_t i = __pyx_nargs; i < 1; i++) {
        if (unlikely(!values[i])) { __Pyx_RaiseArgtupleInvalid("__repr__", 1, 1, 1, i); __PYX_ERR(0, 250, __pyx_L3_error) }
      }
    } else if (unlikely(__pyx_nargs != 1)) {
      goto __pyx_L5_argtuple_error;
    } else {
      values[0] = __Pyx_ArgRef_FASTCALL(__pyx_args, 0);
      if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[0])) __PYX_ERR(0, 250, __pyx_L3_error)
    }
    __pyx_v_self = values[0];
  }
  goto __pyx_L6_skip;
  __pyx_L5_argtuple_error:;
  __Pyx_RaiseArgtupleInvalid("__repr__", 1, 1, 1, __pyx_nargs); __PYX_ERR(0, 250, __pyx_L3_error)
  __pyx_L6_skip:;
  goto __pyx_L4_argument_unpacking_done;
  __pyx_L3_error:;
  for (Py_ssize_t __pyx_temp=0; __pyx_temp < (Py_ssize_t)(sizeof(values)/sizeof(values[0])); ++__pyx_temp) {
    Py_XDECREF(values[__pyx_temp]);
  }
  __Pyx_AddTraceback("Cython.Compiler.Scanning.FileSourceDescriptor.__repr__", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __Pyx_RefNannyFinishContext();
  return NULL;
  __pyx_L4_argument_unpacking_done:;
  __pyx_r = __pyx_pf_6Cython_8Compiler_8Scanning_20FileSourceDescriptor_16__repr__(__pyx_self, __pyx_v_self);
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

static PyObject *__pyx_pf_6Cython_8Compiler_8Scanning_20FileSourceDescriptor_16__repr__(CYTHON_UNUSED PyObject *__pyx_self, PyObject *__pyx_v_self) {
  PyObject *__pyx_r = NULL;
/* … */
  /* function exit code */
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_t_1);
  __Pyx_XDECREF(__pyx_t_2);
  __Pyx_AddTraceback("Cython.Compiler.Scanning.FileSourceDescriptor.__repr__", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_r = NULL;
  __pyx_L0:;
  __Pyx_XGIVEREF(__pyx_r);
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}
/* … */
  __pyx_t_6 = __Pyx_CyFunction_New(&__pyx_mdef_6Cython_8Compiler_8Scanning_20FileSourceDescriptor_17__repr__, 0, __pyx_mstate_global->__pyx_n_u_FileSourceDescriptor___repr, NULL, __pyx_mstate_global->__pyx_n_u_Cython_Compiler_Scanning, __pyx_mstate_global->__pyx_d, ((PyObject *)__pyx_mstate_global->__pyx_codeobj_tab[27])); if (unlikely(!__pyx_t_6)) __PYX_ERR(0, 250, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_6);
  #if CYTHON_COMPILING_IN_CPYTHON && PY_VERSION_HEX >= 0x030E0000
  PyUnstable_Object_EnableDeferredRefcount(__pyx_t_6);
  #endif
  if (__Pyx_SetNameInClass(__pyx_t_7, __pyx_mstate_global->__pyx_n_u_repr_2, __pyx_t_6) < (0)) __PYX_ERR(0, 250, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_6); __pyx_t_6 = 0;
```

</details>

L251  🟠  (score=6)
```python
        return "<FileSourceDescriptor:%s>" % self.filename
```
<details><summary>Show generated C (score=6)</summary>

```c
  __Pyx_XDECREF(__pyx_r);
  __pyx_t_1 = __Pyx_PyObject_GetAttrStr(__pyx_v_self, __pyx_mstate_global->__pyx_n_u_filename); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 251, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __pyx_t_2 = __Pyx_PyUnicode_FormatSafe(__pyx_mstate_global->__pyx_kp_u_FileSourceDescriptor_s, __pyx_t_1); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 251, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __pyx_r = __pyx_t_2;
  __pyx_t_2 = 0;
  goto __pyx_L0;
```

</details>

L252  ⚪  (score=0)
```python
```
L253  ⚪  (score=0)
```python
```
L254  🔴  (score=30)
```python
class StringSourceDescriptor(SourceDescriptor):
```
<details><summary>Show generated C (score=30)</summary>

```c
  __Pyx_GetModuleGlobalName(__pyx_t_4, __pyx_mstate_global->__pyx_n_u_SourceDescriptor); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 254, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_4);
  __pyx_t_2 = PyTuple_Pack(1, __pyx_t_4); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 254, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
  __pyx_t_4 = __Pyx_PEP560_update_bases(__pyx_t_2); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 254, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_4);
  __pyx_t_7 = __Pyx_CalculateMetaclass(NULL, __pyx_t_4); if (unlikely(!__pyx_t_7)) __PYX_ERR(0, 254, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_7);
  __pyx_t_6 = __Pyx_Py3MetaclassPrepare(__pyx_t_7, __pyx_t_4, __pyx_mstate_global->__pyx_n_u_StringSourceDescriptor, __pyx_mstate_global->__pyx_n_u_StringSourceDescriptor, (PyObject *) NULL, __pyx_mstate_global->__pyx_n_u_Cython_Compiler_Scanning, __pyx_mstate_global->__pyx_kp_u_File_Cython_Compiler_Scanning_py_4); if (unlikely(!__pyx_t_6)) __PYX_ERR(0, 254, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_6);
  if (__pyx_t_4 != __pyx_t_2) {
    if (unlikely((PyDict_SetItemString(__pyx_t_6, "__orig_bases__", __pyx_t_2) < 0))) __PYX_ERR(0, 254, __pyx_L1_error)
  }
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
/* … */
  __pyx_t_8 = __Pyx_Py3ClassCreate(__pyx_t_7, __pyx_mstate_global->__pyx_n_u_StringSourceDescriptor, __pyx_t_4, __pyx_t_6, NULL, 0, 0); if (unlikely(!__pyx_t_8)) __PYX_ERR(0, 254, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_8);
  #if CYTHON_COMPILING_IN_CPYTHON && PY_VERSION_HEX >= 0x030E0000
  PyUnstable_Object_EnableDeferredRefcount(__pyx_t_8);
  #endif
  if (PyDict_SetItem(__pyx_mstate_global->__pyx_d, __pyx_mstate_global->__pyx_n_u_StringSourceDescriptor, __pyx_t_8) < (0)) __PYX_ERR(0, 254, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_8); __pyx_t_8 = 0;
  __Pyx_DECREF(__pyx_t_6); __pyx_t_6 = 0;
  __Pyx_DECREF(__pyx_t_7); __pyx_t_7 = 0;
  __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
```

</details>

L255  ⚪  (score=0)
```python
    """Instances of this class can be used instead of a filenames if the code originates from a string object."""
```
L256  ⚪  (score=0)
```python
```
L257  🔴  (score=49)
```python
    def __init__(self, name, code):
```
<details><summary>Show generated C (score=49)</summary>

```c
/* Python wrapper */
static PyObject *__pyx_pw_6Cython_8Compiler_8Scanning_22StringSourceDescriptor_1__init__(PyObject *__pyx_self, 
#if CYTHON_METH_FASTCALL
PyObject *const *__pyx_args, Py_ssize_t __pyx_nargs, PyObject *__pyx_kwds
#else
PyObject *__pyx_args, PyObject *__pyx_kwds
#endif
); /*proto*/
PyDoc_STRVAR(__pyx_doc_6Cython_8Compiler_8Scanning_22StringSourceDescriptor___init__, "File: Cython/Compiler/Scanning.py (starting at line 257)");
static PyMethodDef __pyx_mdef_6Cython_8Compiler_8Scanning_22StringSourceDescriptor_1__init__ = {"__init__", (PyCFunction)(void(*)(void))(__Pyx_PyCFunction_FastCallWithKeywords)__pyx_pw_6Cython_8Compiler_8Scanning_22StringSourceDescriptor_1__init__, __Pyx_METH_FASTCALL|METH_KEYWORDS, __pyx_doc_6Cython_8Compiler_8Scanning_22StringSourceDescriptor___init__};
static PyObject *__pyx_pw_6Cython_8Compiler_8Scanning_22StringSourceDescriptor_1__init__(PyObject *__pyx_self, 
#if CYTHON_METH_FASTCALL
PyObject *const *__pyx_args, Py_ssize_t __pyx_nargs, PyObject *__pyx_kwds
#else
PyObject *__pyx_args, PyObject *__pyx_kwds
#endif
) {
  PyObject *__pyx_v_self = 0;
  PyObject *__pyx_v_name = 0;
  PyObject *__pyx_v_code = 0;
  #if !CYTHON_METH_FASTCALL
  CYTHON_UNUSED Py_ssize_t __pyx_nargs;
  #endif
  CYTHON_UNUSED PyObject *const *__pyx_kwvalues;
  PyObject *__pyx_r = 0;
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("__init__ (wrapper)", 0);
  #if !CYTHON_METH_FASTCALL
  #if CYTHON_ASSUME_SAFE_SIZE
  __pyx_nargs = PyTuple_GET_SIZE(__pyx_args);
  #else
  __pyx_nargs = PyTuple_Size(__pyx_args); if (unlikely(__pyx_nargs < 0)) return NULL;
  #endif
  #endif
  __pyx_kwvalues = __Pyx_KwValues_FASTCALL(__pyx_args, __pyx_nargs);
  {
    PyObject ** const __pyx_pyargnames[] = {&__pyx_mstate_global->__pyx_n_u_self,&__pyx_mstate_global->__pyx_n_u_name,&__pyx_mstate_global->__pyx_n_u_code,0};
  PyObject* values[3] = {0,0,0};
    const Py_ssize_t __pyx_kwds_len = (__pyx_kwds) ? __Pyx_NumKwargs_FASTCALL(__pyx_kwds) : 0;
    if (unlikely(__pyx_kwds_len) < 0) __PYX_ERR(0, 257, __pyx_L3_error)
    if (__pyx_kwds_len > 0) {
      switch (__pyx_nargs) {
        case  3:
        values[2] = __Pyx_ArgRef_FASTCALL(__pyx_args, 2);
        if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[2])) __PYX_ERR(0, 257, __pyx_L3_error)
        CYTHON_FALLTHROUGH;
        case  2:
        values[1] = __Pyx_ArgRef_FASTCALL(__pyx_args, 1);
        if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[1])) __PYX_ERR(0, 257, __pyx_L3_error)
        CYTHON_FALLTHROUGH;
        case  1:
        values[0] = __Pyx_ArgRef_FASTCALL(__pyx_args, 0);
        if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[0])) __PYX_ERR(0, 257, __pyx_L3_error)
        CYTHON_FALLTHROUGH;
        case  0: break;
        default: goto __pyx_L5_argtuple_error;
      }
      const Py_ssize_t kwd_pos_args = __pyx_nargs;
      if (__Pyx_ParseKeywords(__pyx_kwds, __pyx_kwvalues, __pyx_pyargnames, 0, values, kwd_pos_args, __pyx_kwds_len, "__init__", 0) < (0)) __PYX_ERR(0, 257, __pyx_L3_error)
      for (Py_ssize_t i = __pyx_nargs; i < 3; i++) {
        if (unlikely(!values[i])) { __Pyx_RaiseArgtupleInvalid("__init__", 1, 3, 3, i); __PYX_ERR(0, 257, __pyx_L3_error) }
      }
    } else if (unlikely(__pyx_nargs != 3)) {
      goto __pyx_L5_argtuple_error;
    } else {
      values[0] = __Pyx_ArgRef_FASTCALL(__pyx_args, 0);
      if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[0])) __PYX_ERR(0, 257, __pyx_L3_error)
      values[1] = __Pyx_ArgRef_FASTCALL(__pyx_args, 1);
      if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[1])) __PYX_ERR(0, 257, __pyx_L3_error)
      values[2] = __Pyx_ArgRef_FASTCALL(__pyx_args, 2);
      if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[2])) __PYX_ERR(0, 257, __pyx_L3_error)
    }
    __pyx_v_self = values[0];
    __pyx_v_name = values[1];
    __pyx_v_code = values[2];
  }
  goto __pyx_L6_skip;
  __pyx_L5_argtuple_error:;
  __Pyx_RaiseArgtupleInvalid("__init__", 1, 3, 3, __pyx_nargs); __PYX_ERR(0, 257, __pyx_L3_error)
  __pyx_L6_skip:;
  goto __pyx_L4_argument_unpacking_done;
  __pyx_L3_error:;
  for (Py_ssize_t __pyx_temp=0; __pyx_temp < (Py_ssize_t)(sizeof(values)/sizeof(values[0])); ++__pyx_temp) {
    Py_XDECREF(values[__pyx_temp]);
  }
  __Pyx_AddTraceback("Cython.Compiler.Scanning.StringSourceDescriptor.__init__", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __Pyx_RefNannyFinishContext();
  return NULL;
  __pyx_L4_argument_unpacking_done:;
  __pyx_r = __pyx_pf_6Cython_8Compiler_8Scanning_22StringSourceDescriptor___init__(__pyx_self, __pyx_v_self, __pyx_v_name, __pyx_v_code);
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

static PyObject *__pyx_pf_6Cython_8Compiler_8Scanning_22StringSourceDescriptor___init__(CYTHON_UNUSED PyObject *__pyx_self, PyObject *__pyx_v_self, PyObject *__pyx_v_name, PyObject *__pyx_v_code) {
  PyObject *__pyx_8genexpr1__pyx_v_line = NULL;
  PyObject *__pyx_r = NULL;
/* … */
  /* function exit code */
  __pyx_r = Py_None; __Pyx_INCREF(Py_None);
  goto __pyx_L0;
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_t_1);
  __Pyx_XDECREF(__pyx_t_2);
  __Pyx_XDECREF(__pyx_t_3);
  __Pyx_XDECREF(__pyx_t_7);
  __Pyx_AddTraceback("Cython.Compiler.Scanning.StringSourceDescriptor.__init__", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_r = NULL;
  __pyx_L0:;
  __Pyx_XDECREF(__pyx_8genexpr1__pyx_v_line);
  __Pyx_XGIVEREF(__pyx_r);
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}
/* … */
  __pyx_t_2 = __Pyx_CyFunction_New(&__pyx_mdef_6Cython_8Compiler_8Scanning_22StringSourceDescriptor_1__init__, 0, __pyx_mstate_global->__pyx_n_u_StringSourceDescriptor___init, NULL, __pyx_mstate_global->__pyx_n_u_Cython_Compiler_Scanning, __pyx_mstate_global->__pyx_d, ((PyObject *)__pyx_mstate_global->__pyx_codeobj_tab[28])); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 257, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  #if CYTHON_COMPILING_IN_CPYTHON && PY_VERSION_HEX >= 0x030E0000
  PyUnstable_Object_EnableDeferredRefcount(__pyx_t_2);
  #endif
  if (__Pyx_SetNameInClass(__pyx_t_6, __pyx_mstate_global->__pyx_n_u_init, __pyx_t_2) < (0)) __PYX_ERR(0, 257, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
```

</details>

L258  🟡  (score=2)
```python
        self.name = name
```
<details><summary>Show generated C (score=2)</summary>

```c
  if (__Pyx_PyObject_SetAttrStr(__pyx_v_self, __pyx_mstate_global->__pyx_n_u_name, __pyx_v_name) < (0)) __PYX_ERR(0, 258, __pyx_L1_error)
```

</details>

L259  🔴  (score=70)
```python
        self.codelines = [line.rstrip() for line in code.splitlines()]
```
<details><summary>Show generated C (score=70)</summary>

```c
  { /* enter inner scope */
    __pyx_t_1 = PyList_New(0); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 259, __pyx_L5_error)
    __Pyx_GOTREF(__pyx_t_1);
    __pyx_t_3 = __pyx_v_code;
    __Pyx_INCREF(__pyx_t_3);
    __pyx_t_4 = 0;
    {
      PyObject *__pyx_callargs[2] = {__pyx_t_3, NULL};
      __pyx_t_2 = __Pyx_PyObject_FastCallMethod((PyObject*)__pyx_mstate_global->__pyx_n_u_splitlines, __pyx_callargs+__pyx_t_4, (1-__pyx_t_4) | (1*__Pyx_PY_VECTORCALL_ARGUMENTS_OFFSET));
      __Pyx_XDECREF(__pyx_t_3); __pyx_t_3 = 0;
      if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 259, __pyx_L5_error)
      __Pyx_GOTREF(__pyx_t_2);
    }
    if (likely(PyList_CheckExact(__pyx_t_2)) || PyTuple_CheckExact(__pyx_t_2)) {
      __pyx_t_3 = __pyx_t_2; __Pyx_INCREF(__pyx_t_3);
      __pyx_t_5 = 0;
      __pyx_t_6 = NULL;
    } else {
      __pyx_t_5 = -1; __pyx_t_3 = PyObject_GetIter(__pyx_t_2); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 259, __pyx_L5_error)
      __Pyx_GOTREF(__pyx_t_3);
      __pyx_t_6 = (CYTHON_COMPILING_IN_LIMITED_API) ? PyIter_Next : __Pyx_PyObject_GetIterNextFunc(__pyx_t_3); if (unlikely(!__pyx_t_6)) __PYX_ERR(0, 259, __pyx_L5_error)
    }
    __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
    for (;;) {
      if (likely(!__pyx_t_6)) {
        if (likely(PyList_CheckExact(__pyx_t_3))) {
          {
            Py_ssize_t __pyx_temp = __Pyx_PyList_GET_SIZE(__pyx_t_3);
            #if !CYTHON_ASSUME_SAFE_SIZE
            if (unlikely((__pyx_temp < 0))) __PYX_ERR(0, 259, __pyx_L5_error)
            #endif
            if (__pyx_t_5 >= __pyx_temp) break;
          }
          __pyx_t_2 = __Pyx_PyList_GetItemRefFast(__pyx_t_3, __pyx_t_5, __Pyx_ReferenceSharing_OwnStrongReference);
          ++__pyx_t_5;
        } else {
          {
            Py_ssize_t __pyx_temp = __Pyx_PyTuple_GET_SIZE(__pyx_t_3);
            #if !CYTHON_ASSUME_SAFE_SIZE
            if (unlikely((__pyx_temp < 0))) __PYX_ERR(0, 259, __pyx_L5_error)
            #endif
            if (__pyx_t_5 >= __pyx_temp) break;
          }
          #if CYTHON_ASSUME_SAFE_MACROS && !CYTHON_AVOID_BORROWED_REFS
          __pyx_t_2 = __Pyx_NewRef(PyTuple_GET_ITEM(__pyx_t_3, __pyx_t_5));
          #else
          __pyx_t_2 = __Pyx_PySequence_ITEM(__pyx_t_3, __pyx_t_5);
          #endif
          ++__pyx_t_5;
        }
        if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 259, __pyx_L5_error)
      } else {
        __pyx_t_2 = __pyx_t_6(__pyx_t_3);
        if (unlikely(!__pyx_t_2)) {
          PyObject* exc_type = PyErr_Occurred();
          if (exc_type) {
            if (unlikely(!__Pyx_PyErr_GivenExceptionMatches(exc_type, PyExc_StopIteration))) __PYX_ERR(0, 259, __pyx_L5_error)
            PyErr_Clear();
          }
          break;
        }
      }
      __Pyx_GOTREF(__pyx_t_2);
      __Pyx_XDECREF_SET(__pyx_8genexpr1__pyx_v_line, __pyx_t_2);
      __pyx_t_2 = 0;
      __pyx_t_7 = __pyx_8genexpr1__pyx_v_line;
      __Pyx_INCREF(__pyx_t_7);
      __pyx_t_4 = 0;
      {
        PyObject *__pyx_callargs[2] = {__pyx_t_7, NULL};
        __pyx_t_2 = __Pyx_PyObject_FastCallMethod((PyObject*)__pyx_mstate_global->__pyx_n_u_rstrip, __pyx_callargs+__pyx_t_4, (1-__pyx_t_4) | (1*__Pyx_PY_VECTORCALL_ARGUMENTS_OFFSET));
        __Pyx_XDECREF(__pyx_t_7); __pyx_t_7 = 0;
        if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 259, __pyx_L5_error)
        __Pyx_GOTREF(__pyx_t_2);
      }
      if (unlikely(__Pyx_ListComp_Append(__pyx_t_1, (PyObject*)__pyx_t_2))) __PYX_ERR(0, 259, __pyx_L5_error)
      __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
    }
    __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
    __Pyx_XDECREF(__pyx_8genexpr1__pyx_v_line); __pyx_8genexpr1__pyx_v_line = 0;
    goto __pyx_L9_exit_scope;
    __pyx_L5_error:;
    __Pyx_XDECREF(__pyx_8genexpr1__pyx_v_line); __pyx_8genexpr1__pyx_v_line = 0;
    goto __pyx_L1_error;
    __pyx_L9_exit_scope:;
  } /* exit inner scope */
  if (__Pyx_PyObject_SetAttrStr(__pyx_v_self, __pyx_mstate_global->__pyx_n_u_codelines, __pyx_t_1) < (0)) __PYX_ERR(0, 259, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
```

</details>

L260  🟡  (score=2)
```python
        self._cmp_name = name
```
<details><summary>Show generated C (score=2)</summary>

```c
  if (__Pyx_PyObject_SetAttrStr(__pyx_v_self, __pyx_mstate_global->__pyx_n_u_cmp_name, __pyx_v_name) < (0)) __PYX_ERR(0, 260, __pyx_L1_error)
```

</details>

L261  ⚪  (score=0)
```python
```
L262  🔴  (score=144)
```python
    def get_lines(self, encoding:str|None=None, error_handling:str|None=None) -> list[str]:
```
<details><summary>Show generated C (score=144)</summary>

```c
/* Python wrapper */
static PyObject *__pyx_pw_6Cython_8Compiler_8Scanning_22StringSourceDescriptor_3get_lines(PyObject *__pyx_self, 
#if CYTHON_METH_FASTCALL
PyObject *const *__pyx_args, Py_ssize_t __pyx_nargs, PyObject *__pyx_kwds
#else
PyObject *__pyx_args, PyObject *__pyx_kwds
#endif
); /*proto*/
PyDoc_STRVAR(__pyx_doc_6Cython_8Compiler_8Scanning_22StringSourceDescriptor_2get_lines, "File: Cython/Compiler/Scanning.py (starting at line 262)");
static PyMethodDef __pyx_mdef_6Cython_8Compiler_8Scanning_22StringSourceDescriptor_3get_lines = {"get_lines", (PyCFunction)(void(*)(void))(__Pyx_PyCFunction_FastCallWithKeywords)__pyx_pw_6Cython_8Compiler_8Scanning_22StringSourceDescriptor_3get_lines, __Pyx_METH_FASTCALL|METH_KEYWORDS, __pyx_doc_6Cython_8Compiler_8Scanning_22StringSourceDescriptor_2get_lines};
static PyObject *__pyx_pw_6Cython_8Compiler_8Scanning_22StringSourceDescriptor_3get_lines(PyObject *__pyx_self, 
#if CYTHON_METH_FASTCALL
PyObject *const *__pyx_args, Py_ssize_t __pyx_nargs, PyObject *__pyx_kwds
#else
PyObject *__pyx_args, PyObject *__pyx_kwds
#endif
) {
  PyObject *__pyx_v_self = 0;
  PyObject *__pyx_v_encoding = 0;
  PyObject *__pyx_v_error_handling = 0;
  #if !CYTHON_METH_FASTCALL
  CYTHON_UNUSED Py_ssize_t __pyx_nargs;
  #endif
  CYTHON_UNUSED PyObject *const *__pyx_kwvalues;
  PyObject *__pyx_r = 0;
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("get_lines (wrapper)", 0);
  #if !CYTHON_METH_FASTCALL
  #if CYTHON_ASSUME_SAFE_SIZE
  __pyx_nargs = PyTuple_GET_SIZE(__pyx_args);
  #else
  __pyx_nargs = PyTuple_Size(__pyx_args); if (unlikely(__pyx_nargs < 0)) return NULL;
  #endif
  #endif
  __pyx_kwvalues = __Pyx_KwValues_FASTCALL(__pyx_args, __pyx_nargs);
  {
    PyObject ** const __pyx_pyargnames[] = {&__pyx_mstate_global->__pyx_n_u_self,&__pyx_mstate_global->__pyx_n_u_encoding,&__pyx_mstate_global->__pyx_n_u_error_handling,0};
  PyObject* values[3] = {0,0,0};
    const Py_ssize_t __pyx_kwds_len = (__pyx_kwds) ? __Pyx_NumKwargs_FASTCALL(__pyx_kwds) : 0;
    if (unlikely(__pyx_kwds_len) < 0) __PYX_ERR(0, 262, __pyx_L3_error)
    if (__pyx_kwds_len > 0) {
      switch (__pyx_nargs) {
        case  3:
        values[2] = __Pyx_ArgRef_FASTCALL(__pyx_args, 2);
        if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[2])) __PYX_ERR(0, 262, __pyx_L3_error)
        CYTHON_FALLTHROUGH;
        case  2:
        values[1] = __Pyx_ArgRef_FASTCALL(__pyx_args, 1);
        if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[1])) __PYX_ERR(0, 262, __pyx_L3_error)
        CYTHON_FALLTHROUGH;
        case  1:
        values[0] = __Pyx_ArgRef_FASTCALL(__pyx_args, 0);
        if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[0])) __PYX_ERR(0, 262, __pyx_L3_error)
        CYTHON_FALLTHROUGH;
        case  0: break;
        default: goto __pyx_L5_argtuple_error;
      }
      const Py_ssize_t kwd_pos_args = __pyx_nargs;
      if (__Pyx_ParseKeywords(__pyx_kwds, __pyx_kwvalues, __pyx_pyargnames, 0, values, kwd_pos_args, __pyx_kwds_len, "get_lines", 0) < (0)) __PYX_ERR(0, 262, __pyx_L3_error)
      if (!values[1]) values[1] = __Pyx_NewRef(((PyObject*)Py_None));
      if (!values[2]) values[2] = __Pyx_NewRef(((PyObject*)Py_None));
      for (Py_ssize_t i = __pyx_nargs; i < 1; i++) {
        if (unlikely(!values[i])) { __Pyx_RaiseArgtupleInvalid("get_lines", 0, 1, 3, i); __PYX_ERR(0, 262, __pyx_L3_error) }
      }
    } else {
      switch (__pyx_nargs) {
        case  3:
        values[2] = __Pyx_ArgRef_FASTCALL(__pyx_args, 2);
        if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[2])) __PYX_ERR(0, 262, __pyx_L3_error)
        CYTHON_FALLTHROUGH;
        case  2:
        values[1] = __Pyx_ArgRef_FASTCALL(__pyx_args, 1);
        if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[1])) __PYX_ERR(0, 262, __pyx_L3_error)
        CYTHON_FALLTHROUGH;
        case  1:
        values[0] = __Pyx_ArgRef_FASTCALL(__pyx_args, 0);
        if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[0])) __PYX_ERR(0, 262, __pyx_L3_error)
        break;
        default: goto __pyx_L5_argtuple_error;
      }
      if (!values[1]) values[1] = __Pyx_NewRef(((PyObject*)Py_None));
      if (!values[2]) values[2] = __Pyx_NewRef(((PyObject*)Py_None));
    }
    __pyx_v_self = values[0];
    __pyx_v_encoding = ((PyObject*)values[1]);
    __pyx_v_error_handling = ((PyObject*)values[2]);
  }
  goto __pyx_L6_skip;
  __pyx_L5_argtuple_error:;
  __Pyx_RaiseArgtupleInvalid("get_lines", 0, 1, 3, __pyx_nargs); __PYX_ERR(0, 262, __pyx_L3_error)
  __pyx_L6_skip:;
  goto __pyx_L4_argument_unpacking_done;
  __pyx_L3_error:;
  for (Py_ssize_t __pyx_temp=0; __pyx_temp < (Py_ssize_t)(sizeof(values)/sizeof(values[0])); ++__pyx_temp) {
    Py_XDECREF(values[__pyx_temp]);
  }
  __Pyx_AddTraceback("Cython.Compiler.Scanning.StringSourceDescriptor.get_lines", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __Pyx_RefNannyFinishContext();
  return NULL;
  __pyx_L4_argument_unpacking_done:;
  if (unlikely(!__Pyx_ArgTypeTest(((PyObject *)__pyx_v_encoding), (&PyUnicode_Type), 1, "encoding", 2))) __PYX_ERR(0, 262, __pyx_L1_error)
  if (unlikely(!__Pyx_ArgTypeTest(((PyObject *)__pyx_v_error_handling), (&PyUnicode_Type), 1, "error_handling", 2))) __PYX_ERR(0, 262, __pyx_L1_error)
  __pyx_r = __pyx_pf_6Cython_8Compiler_8Scanning_22StringSourceDescriptor_2get_lines(__pyx_self, __pyx_v_self, __pyx_v_encoding, __pyx_v_error_handling);

  /* function exit code */
  goto __pyx_L0;
  __pyx_L1_error:;
  __pyx_r = NULL;
  for (Py_ssize_t __pyx_temp=0; __pyx_temp < (Py_ssize_t)(sizeof(values)/sizeof(values[0])); ++__pyx_temp) {
    Py_XDECREF(values[__pyx_temp]);
  }
  goto __pyx_L7_cleaned_up;
  __pyx_L0:;
  for (Py_ssize_t __pyx_temp=0; __pyx_temp < (Py_ssize_t)(sizeof(values)/sizeof(values[0])); ++__pyx_temp) {
    Py_XDECREF(values[__pyx_temp]);
  }
  __pyx_L7_cleaned_up:;
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}

static PyObject *__pyx_pf_6Cython_8Compiler_8Scanning_22StringSourceDescriptor_2get_lines(CYTHON_UNUSED PyObject *__pyx_self, PyObject *__pyx_v_self, PyObject *__pyx_v_encoding, PyObject *__pyx_v_error_handling) {
  PyObject *__pyx_8genexpr2__pyx_v_line = NULL;
  PyObject *__pyx_r = NULL;
/* … */
  /* function exit code */
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_t_3);
  __Pyx_XDECREF(__pyx_t_4);
  __Pyx_XDECREF(__pyx_t_5);
  __Pyx_XDECREF(__pyx_t_8);
  __Pyx_XDECREF(__pyx_t_9);
  __Pyx_XDECREF(__pyx_t_10);
  __Pyx_AddTraceback("Cython.Compiler.Scanning.StringSourceDescriptor.get_lines", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_r = NULL;
  __pyx_L0:;
  __Pyx_XDECREF(__pyx_8genexpr2__pyx_v_line);
  __Pyx_XGIVEREF(__pyx_r);
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}
/* … */
  __pyx_t_2 = __Pyx_PyDict_NewPresized(3); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 262, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  #if defined(PyDict_SetItem) && (defined(CYTHON_COMPILING_IN_CPYTHON))
  #if PY_VERSION_HEX >= 0x030A0000 /* CPython 3.10+ exposes KnownHash APIs */
  /* Use CPython's KnownHash APIs when available */
  extern int _PyDict_SetItem_KnownHash(PyObject*, PyObject*, PyObject*, Py_hash_t);
  {
    Py_hash_t __pyx_hash = PyObject_Hash(__pyx_mstate_global->__pyx_n_u_encoding); if (unlikely(__pyx_hash == -1)) __PYX_ERR(0, 262, __pyx_L1_error);
    if (unlikely(_PyDict_SetItem_KnownHash(__pyx_t_2, __pyx_mstate_global->__pyx_n_u_encoding, __pyx_mstate_global->__pyx_kp_u_str_None, __pyx_hash) < 0)) __PYX_ERR(0, 262, __pyx_L1_error);
  }
  #else
  if (PyDict_SetItem(__pyx_t_2, __pyx_mstate_global->__pyx_n_u_encoding, __pyx_mstate_global->__pyx_kp_u_str_None) < (0)) __PYX_ERR(0, 262, __pyx_L1_error)
  #endif
  #else
  if (PyDict_SetItem(__pyx_t_2, __pyx_mstate_global->__pyx_n_u_encoding, __pyx_mstate_global->__pyx_kp_u_str_None) < (0)) __PYX_ERR(0, 262, __pyx_L1_error)
  #endif
  #if defined(PyDict_SetItem) && (defined(CYTHON_COMPILING_IN_CPYTHON))
  #if PY_VERSION_HEX >= 0x030A0000 /* CPython 3.10+ exposes KnownHash APIs */
  /* Use CPython's KnownHash APIs when available */
  extern int _PyDict_SetItem_KnownHash(PyObject*, PyObject*, PyObject*, Py_hash_t);
  {
    Py_hash_t __pyx_hash = PyObject_Hash(__pyx_mstate_global->__pyx_n_u_error_handling); if (unlikely(__pyx_hash == -1)) __PYX_ERR(0, 262, __pyx_L1_error);
    if (unlikely(_PyDict_SetItem_KnownHash(__pyx_t_2, __pyx_mstate_global->__pyx_n_u_error_handling, __pyx_mstate_global->__pyx_kp_u_str_None, __pyx_hash) < 0)) __PYX_ERR(0, 262, __pyx_L1_error);
  }
  #else
  if (PyDict_SetItem(__pyx_t_2, __pyx_mstate_global->__pyx_n_u_error_handling, __pyx_mstate_global->__pyx_kp_u_str_None) < (0)) __PYX_ERR(0, 262, __pyx_L1_error)
  #endif
  #else
  if (PyDict_SetItem(__pyx_t_2, __pyx_mstate_global->__pyx_n_u_error_handling, __pyx_mstate_global->__pyx_kp_u_str_None) < (0)) __PYX_ERR(0, 262, __pyx_L1_error)
  #endif
  #if defined(PyDict_SetItem) && (defined(CYTHON_COMPILING_IN_CPYTHON))
  #if PY_VERSION_HEX >= 0x030A0000 /* CPython 3.10+ exposes KnownHash APIs */
  /* Use CPython's KnownHash APIs when available */
  extern int _PyDict_SetItem_KnownHash(PyObject*, PyObject*, PyObject*, Py_hash_t);
  {
    Py_hash_t __pyx_hash = PyObject_Hash(__pyx_mstate_global->__pyx_n_u_return); if (unlikely(__pyx_hash == -1)) __PYX_ERR(0, 262, __pyx_L1_error);
    if (unlikely(_PyDict_SetItem_KnownHash(__pyx_t_2, __pyx_mstate_global->__pyx_n_u_return, __pyx_mstate_global->__pyx_kp_u_list_str, __pyx_hash) < 0)) __PYX_ERR(0, 262, __pyx_L1_error);
  }
  #else
  if (PyDict_SetItem(__pyx_t_2, __pyx_mstate_global->__pyx_n_u_return, __pyx_mstate_global->__pyx_kp_u_list_str) < (0)) __PYX_ERR(0, 262, __pyx_L1_error)
  #endif
  #else
  if (PyDict_SetItem(__pyx_t_2, __pyx_mstate_global->__pyx_n_u_return, __pyx_mstate_global->__pyx_kp_u_list_str) < (0)) __PYX_ERR(0, 262, __pyx_L1_error)
  #endif
  __pyx_t_8 = __Pyx_CyFunction_New(&__pyx_mdef_6Cython_8Compiler_8Scanning_22StringSourceDescriptor_3get_lines, 0, __pyx_mstate_global->__pyx_n_u_StringSourceDescriptor_get_lines, NULL, __pyx_mstate_global->__pyx_n_u_Cython_Compiler_Scanning, __pyx_mstate_global->__pyx_d, ((PyObject *)__pyx_mstate_global->__pyx_codeobj_tab[29])); if (unlikely(!__pyx_t_8)) __PYX_ERR(0, 262, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_8);
  #if CYTHON_COMPILING_IN_CPYTHON && PY_VERSION_HEX >= 0x030E0000
  PyUnstable_Object_EnableDeferredRefcount(__pyx_t_8);
  #endif
  __Pyx_CyFunction_SetDefaultsTuple(__pyx_t_8, __pyx_mstate_global->__pyx_tuple[17]);
  __Pyx_CyFunction_SetAnnotationsDict(__pyx_t_8, __pyx_t_2);
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  if (__Pyx_SetNameInClass(__pyx_t_6, __pyx_mstate_global->__pyx_n_u_get_lines, __pyx_t_8) < (0)) __PYX_ERR(0, 262, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_8); __pyx_t_8 = 0;
```

</details>

L263  🟡  (score=2)
```python
        if not encoding:
```
<details><summary>Show generated C (score=2)</summary>

```c
  if (__pyx_v_encoding == Py_None) __pyx_t_1 = 0;
  else
  {
    Py_ssize_t __pyx_temp = __Pyx_PyUnicode_IS_TRUE(__pyx_v_encoding);
    if (unlikely(((!CYTHON_ASSUME_SAFE_SIZE) && __pyx_temp < 0))) __PYX_ERR(0, 263, __pyx_L1_error)
    __pyx_t_1 = (__pyx_temp != 0);
  }

  __pyx_t_2 = (!__pyx_t_1);
  if (__pyx_t_2) {
/* … */
  }
```

</details>

L264  🟠  (score=8)
```python
            return self.codelines
```
<details><summary>Show generated C (score=8)</summary>

```c
    __Pyx_XDECREF(__pyx_r);
    __pyx_t_3 = __Pyx_PyObject_GetAttrStr(__pyx_v_self, __pyx_mstate_global->__pyx_n_u_codelines); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 264, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_3);
    __pyx_t_3 = PySequence_List(__pyx_t_3); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 264, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_3);
    __pyx_r = __pyx_t_3;
    __pyx_t_3 = 0;
    goto __pyx_L0;
```

</details>

L265  ⚪  (score=0)
```python
```
L266  🔴  (score=18)
```python
        return [line.encode(encoding, error_handling).decode(encoding)
```
<details><summary>Show generated C (score=18)</summary>

```c
  __Pyx_XDECREF(__pyx_r);
  { /* enter inner scope */
    __pyx_t_3 = PyList_New(0); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 266, __pyx_L6_error)
    __Pyx_GOTREF(__pyx_t_3);
/* … */
      __pyx_t_10 = __pyx_8genexpr2__pyx_v_line;
      __Pyx_INCREF(__pyx_t_10);
      __pyx_t_11 = 0;
      {
        PyObject *__pyx_callargs[3] = {__pyx_t_10, __pyx_v_encoding, __pyx_v_error_handling};
        __pyx_t_9 = __Pyx_PyObject_FastCallMethod((PyObject*)__pyx_mstate_global->__pyx_n_u_encode, __pyx_callargs+__pyx_t_11, (3-__pyx_t_11) | (1*__Pyx_PY_VECTORCALL_ARGUMENTS_OFFSET));
        __Pyx_XDECREF(__pyx_t_10); __pyx_t_10 = 0;
        if (unlikely(!__pyx_t_9)) __PYX_ERR(0, 266, __pyx_L6_error)
        __Pyx_GOTREF(__pyx_t_9);
      }
      __pyx_t_8 = __pyx_t_9;
      __Pyx_INCREF(__pyx_t_8);
      __pyx_t_11 = 0;
      {
        PyObject *__pyx_callargs[2] = {__pyx_t_8, __pyx_v_encoding};
        __pyx_t_4 = __Pyx_PyObject_FastCallMethod((PyObject*)__pyx_mstate_global->__pyx_n_u_decode, __pyx_callargs+__pyx_t_11, (2-__pyx_t_11) | (1*__Pyx_PY_VECTORCALL_ARGUMENTS_OFFSET));
        __Pyx_XDECREF(__pyx_t_8); __pyx_t_8 = 0;
        __Pyx_DECREF(__pyx_t_9); __pyx_t_9 = 0;
        if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 266, __pyx_L6_error)
        __Pyx_GOTREF(__pyx_t_4);
      }
      if (unlikely(__Pyx_ListComp_Append(__pyx_t_3, (PyObject*)__pyx_t_4))) __PYX_ERR(0, 266, __pyx_L6_error)
      __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
```

</details>

L267  🔴  (score=53)
```python
                    for line in self.codelines]
```
<details><summary>Show generated C (score=53)</summary>

```c
    __pyx_t_4 = __Pyx_PyObject_GetAttrStr(__pyx_v_self, __pyx_mstate_global->__pyx_n_u_codelines); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 267, __pyx_L6_error)
    __Pyx_GOTREF(__pyx_t_4);
    if (likely(PyList_CheckExact(__pyx_t_4)) || PyTuple_CheckExact(__pyx_t_4)) {
      __pyx_t_5 = __pyx_t_4; __Pyx_INCREF(__pyx_t_5);
      __pyx_t_6 = 0;
      __pyx_t_7 = NULL;
    } else {
      __pyx_t_6 = -1; __pyx_t_5 = PyObject_GetIter(__pyx_t_4); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 267, __pyx_L6_error)
      __Pyx_GOTREF(__pyx_t_5);
      __pyx_t_7 = (CYTHON_COMPILING_IN_LIMITED_API) ? PyIter_Next : __Pyx_PyObject_GetIterNextFunc(__pyx_t_5); if (unlikely(!__pyx_t_7)) __PYX_ERR(0, 267, __pyx_L6_error)
    }
    __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
    for (;;) {
      if (likely(!__pyx_t_7)) {
        if (likely(PyList_CheckExact(__pyx_t_5))) {
          {
            Py_ssize_t __pyx_temp = __Pyx_PyList_GET_SIZE(__pyx_t_5);
            #if !CYTHON_ASSUME_SAFE_SIZE
            if (unlikely((__pyx_temp < 0))) __PYX_ERR(0, 267, __pyx_L6_error)
            #endif
            if (__pyx_t_6 >= __pyx_temp) break;
          }
          __pyx_t_4 = __Pyx_PyList_GetItemRefFast(__pyx_t_5, __pyx_t_6, __Pyx_ReferenceSharing_OwnStrongReference);
          ++__pyx_t_6;
        } else {
          {
            Py_ssize_t __pyx_temp = __Pyx_PyTuple_GET_SIZE(__pyx_t_5);
            #if !CYTHON_ASSUME_SAFE_SIZE
            if (unlikely((__pyx_temp < 0))) __PYX_ERR(0, 267, __pyx_L6_error)
            #endif
            if (__pyx_t_6 >= __pyx_temp) break;
          }
          #if CYTHON_ASSUME_SAFE_MACROS && !CYTHON_AVOID_BORROWED_REFS
          __pyx_t_4 = __Pyx_NewRef(PyTuple_GET_ITEM(__pyx_t_5, __pyx_t_6));
          #else
          __pyx_t_4 = __Pyx_PySequence_ITEM(__pyx_t_5, __pyx_t_6);
          #endif
          ++__pyx_t_6;
        }
        if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 267, __pyx_L6_error)
      } else {
        __pyx_t_4 = __pyx_t_7(__pyx_t_5);
        if (unlikely(!__pyx_t_4)) {
          PyObject* exc_type = PyErr_Occurred();
          if (exc_type) {
            if (unlikely(!__Pyx_PyErr_GivenExceptionMatches(exc_type, PyExc_StopIteration))) __PYX_ERR(0, 267, __pyx_L6_error)
            PyErr_Clear();
          }
          break;
        }
      }
      __Pyx_GOTREF(__pyx_t_4);
      __Pyx_XDECREF_SET(__pyx_8genexpr2__pyx_v_line, __pyx_t_4);
      __pyx_t_4 = 0;
/* … */
    }
    __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
    __Pyx_XDECREF(__pyx_8genexpr2__pyx_v_line); __pyx_8genexpr2__pyx_v_line = 0;
    goto __pyx_L10_exit_scope;
    __pyx_L6_error:;
    __Pyx_XDECREF(__pyx_8genexpr2__pyx_v_line); __pyx_8genexpr2__pyx_v_line = 0;
    goto __pyx_L1_error;
    __pyx_L10_exit_scope:;
  } /* exit inner scope */
  __pyx_r = ((PyObject*)__pyx_t_3);
  __pyx_t_3 = 0;
  goto __pyx_L0;
```

</details>

L268  ⚪  (score=0)
```python
```
L269  🔴  (score=66)
```python
    def get_description(self) -> str:
```
<details><summary>Show generated C (score=66)</summary>

```c
/* Python wrapper */
static PyObject *__pyx_pw_6Cython_8Compiler_8Scanning_22StringSourceDescriptor_5get_description(PyObject *__pyx_self, 
#if CYTHON_METH_FASTCALL
PyObject *const *__pyx_args, Py_ssize_t __pyx_nargs, PyObject *__pyx_kwds
#else
PyObject *__pyx_args, PyObject *__pyx_kwds
#endif
); /*proto*/
PyDoc_STRVAR(__pyx_doc_6Cython_8Compiler_8Scanning_22StringSourceDescriptor_4get_description, "File: Cython/Compiler/Scanning.py (starting at line 269)");
static PyMethodDef __pyx_mdef_6Cython_8Compiler_8Scanning_22StringSourceDescriptor_5get_description = {"get_description", (PyCFunction)(void(*)(void))(__Pyx_PyCFunction_FastCallWithKeywords)__pyx_pw_6Cython_8Compiler_8Scanning_22StringSourceDescriptor_5get_description, __Pyx_METH_FASTCALL|METH_KEYWORDS, __pyx_doc_6Cython_8Compiler_8Scanning_22StringSourceDescriptor_4get_description};
static PyObject *__pyx_pw_6Cython_8Compiler_8Scanning_22StringSourceDescriptor_5get_description(PyObject *__pyx_self, 
#if CYTHON_METH_FASTCALL
PyObject *const *__pyx_args, Py_ssize_t __pyx_nargs, PyObject *__pyx_kwds
#else
PyObject *__pyx_args, PyObject *__pyx_kwds
#endif
) {
  PyObject *__pyx_v_self = 0;
  #if !CYTHON_METH_FASTCALL
  CYTHON_UNUSED Py_ssize_t __pyx_nargs;
  #endif
  CYTHON_UNUSED PyObject *const *__pyx_kwvalues;
  PyObject *__pyx_r = 0;
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("get_description (wrapper)", 0);
  #if !CYTHON_METH_FASTCALL
  #if CYTHON_ASSUME_SAFE_SIZE
  __pyx_nargs = PyTuple_GET_SIZE(__pyx_args);
  #else
  __pyx_nargs = PyTuple_Size(__pyx_args); if (unlikely(__pyx_nargs < 0)) return NULL;
  #endif
  #endif
  __pyx_kwvalues = __Pyx_KwValues_FASTCALL(__pyx_args, __pyx_nargs);
  {
    PyObject ** const __pyx_pyargnames[] = {&__pyx_mstate_global->__pyx_n_u_self,0};
  PyObject* values[1] = {0};
    const Py_ssize_t __pyx_kwds_len = (__pyx_kwds) ? __Pyx_NumKwargs_FASTCALL(__pyx_kwds) : 0;
    if (unlikely(__pyx_kwds_len) < 0) __PYX_ERR(0, 269, __pyx_L3_error)
    if (__pyx_kwds_len > 0) {
      switch (__pyx_nargs) {
        case  1:
        values[0] = __Pyx_ArgRef_FASTCALL(__pyx_args, 0);
        if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[0])) __PYX_ERR(0, 269, __pyx_L3_error)
        CYTHON_FALLTHROUGH;
        case  0: break;
        default: goto __pyx_L5_argtuple_error;
      }
      const Py_ssize_t kwd_pos_args = __pyx_nargs;
      if (__Pyx_ParseKeywords(__pyx_kwds, __pyx_kwvalues, __pyx_pyargnames, 0, values, kwd_pos_args, __pyx_kwds_len, "get_description", 0) < (0)) __PYX_ERR(0, 269, __pyx_L3_error)
      for (Py_ssize_t i = __pyx_nargs; i < 1; i++) {
        if (unlikely(!values[i])) { __Pyx_RaiseArgtupleInvalid("get_description", 1, 1, 1, i); __PYX_ERR(0, 269, __pyx_L3_error) }
      }
    } else if (unlikely(__pyx_nargs != 1)) {
      goto __pyx_L5_argtuple_error;
    } else {
      values[0] = __Pyx_ArgRef_FASTCALL(__pyx_args, 0);
      if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[0])) __PYX_ERR(0, 269, __pyx_L3_error)
    }
    __pyx_v_self = values[0];
  }
  goto __pyx_L6_skip;
  __pyx_L5_argtuple_error:;
  __Pyx_RaiseArgtupleInvalid("get_description", 1, 1, 1, __pyx_nargs); __PYX_ERR(0, 269, __pyx_L3_error)
  __pyx_L6_skip:;
  goto __pyx_L4_argument_unpacking_done;
  __pyx_L3_error:;
  for (Py_ssize_t __pyx_temp=0; __pyx_temp < (Py_ssize_t)(sizeof(values)/sizeof(values[0])); ++__pyx_temp) {
    Py_XDECREF(values[__pyx_temp]);
  }
  __Pyx_AddTraceback("Cython.Compiler.Scanning.StringSourceDescriptor.get_description", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __Pyx_RefNannyFinishContext();
  return NULL;
  __pyx_L4_argument_unpacking_done:;
  __pyx_r = __pyx_pf_6Cython_8Compiler_8Scanning_22StringSourceDescriptor_4get_description(__pyx_self, __pyx_v_self);
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

static PyObject *__pyx_pf_6Cython_8Compiler_8Scanning_22StringSourceDescriptor_4get_description(CYTHON_UNUSED PyObject *__pyx_self, PyObject *__pyx_v_self) {
  PyObject *__pyx_r = NULL;
/* … */
  /* function exit code */
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_t_1);
  __Pyx_AddTraceback("Cython.Compiler.Scanning.StringSourceDescriptor.get_description", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_r = NULL;
  __pyx_L0:;
  __Pyx_XGIVEREF(__pyx_r);
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}
/* … */
  __pyx_t_8 = __Pyx_PyDict_NewPresized(1); if (unlikely(!__pyx_t_8)) __PYX_ERR(0, 269, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_8);
  #if defined(PyDict_SetItem) && (defined(CYTHON_COMPILING_IN_CPYTHON))
  #if PY_VERSION_HEX >= 0x030A0000 /* CPython 3.10+ exposes KnownHash APIs */
  /* Use CPython's KnownHash APIs when available */
  extern int _PyDict_SetItem_KnownHash(PyObject*, PyObject*, PyObject*, Py_hash_t);
  {
    Py_hash_t __pyx_hash = PyObject_Hash(__pyx_mstate_global->__pyx_n_u_return); if (unlikely(__pyx_hash == -1)) __PYX_ERR(0, 269, __pyx_L1_error);
    if (unlikely(_PyDict_SetItem_KnownHash(__pyx_t_8, __pyx_mstate_global->__pyx_n_u_return, __pyx_mstate_global->__pyx_n_u_str, __pyx_hash) < 0)) __PYX_ERR(0, 269, __pyx_L1_error);
  }
  #else
  if (PyDict_SetItem(__pyx_t_8, __pyx_mstate_global->__pyx_n_u_return, __pyx_mstate_global->__pyx_n_u_str) < (0)) __PYX_ERR(0, 269, __pyx_L1_error)
  #endif
  #else
  if (PyDict_SetItem(__pyx_t_8, __pyx_mstate_global->__pyx_n_u_return, __pyx_mstate_global->__pyx_n_u_str) < (0)) __PYX_ERR(0, 269, __pyx_L1_error)
  #endif
  __pyx_t_2 = __Pyx_CyFunction_New(&__pyx_mdef_6Cython_8Compiler_8Scanning_22StringSourceDescriptor_5get_description, 0, __pyx_mstate_global->__pyx_n_u_StringSourceDescriptor_get_descr, NULL, __pyx_mstate_global->__pyx_n_u_Cython_Compiler_Scanning, __pyx_mstate_global->__pyx_d, ((PyObject *)__pyx_mstate_global->__pyx_codeobj_tab[30])); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 269, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  #if CYTHON_COMPILING_IN_CPYTHON && PY_VERSION_HEX >= 0x030E0000
  PyUnstable_Object_EnableDeferredRefcount(__pyx_t_2);
  #endif
  __Pyx_CyFunction_SetAnnotationsDict(__pyx_t_2, __pyx_t_8);
  __Pyx_DECREF(__pyx_t_8); __pyx_t_8 = 0;
  if (__Pyx_SetNameInClass(__pyx_t_6, __pyx_mstate_global->__pyx_n_u_get_description, __pyx_t_2) < (0)) __PYX_ERR(0, 269, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
```

</details>

L270  🔴  (score=10)
```python
        return self.name
```
<details><summary>Show generated C (score=10)</summary>

```c
  __Pyx_XDECREF(__pyx_r);
  __pyx_t_1 = __Pyx_PyObject_GetAttrStr(__pyx_v_self, __pyx_mstate_global->__pyx_n_u_name); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 270, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  if (!(likely(PyUnicode_CheckExact(__pyx_t_1))||((__pyx_t_1) == Py_None) || __Pyx_RaiseUnexpectedTypeError("str", __pyx_t_1))) __PYX_ERR(0, 270, __pyx_L1_error)
  __pyx_r = ((PyObject*)__pyx_t_1);
  __pyx_t_1 = 0;
  goto __pyx_L0;
```

</details>

L271  ⚪  (score=0)
```python
```
L272  🔴  (score=15)
```python
    get_error_description = get_description
```
<details><summary>Show generated C (score=15)</summary>

```c
  __pyx_t_2 = PyObject_GetItem(__pyx_t_6, __pyx_mstate_global->__pyx_n_u_get_description);
  if (unlikely(!__pyx_t_2)) {
    PyErr_Clear();
    __Pyx_GetModuleGlobalName(__pyx_t_2, __pyx_mstate_global->__pyx_n_u_get_description);
  }
  if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 272, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  if (__Pyx_SetNameInClass(__pyx_t_6, __pyx_mstate_global->__pyx_n_u_get_error_description, __pyx_t_2) < (0)) __PYX_ERR(0, 272, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
```

</details>

L273  ⚪  (score=0)
```python
```
L274  🔴  (score=63)
```python
    def get_filenametable_entry(self) -> str:
```
<details><summary>Show generated C (score=63)</summary>

```c
/* Python wrapper */
static PyObject *__pyx_pw_6Cython_8Compiler_8Scanning_22StringSourceDescriptor_7get_filenametable_entry(PyObject *__pyx_self, 
#if CYTHON_METH_FASTCALL
PyObject *const *__pyx_args, Py_ssize_t __pyx_nargs, PyObject *__pyx_kwds
#else
PyObject *__pyx_args, PyObject *__pyx_kwds
#endif
); /*proto*/
PyDoc_STRVAR(__pyx_doc_6Cython_8Compiler_8Scanning_22StringSourceDescriptor_6get_filenametable_entry, "File: Cython/Compiler/Scanning.py (starting at line 274)");
static PyMethodDef __pyx_mdef_6Cython_8Compiler_8Scanning_22StringSourceDescriptor_7get_filenametable_entry = {"get_filenametable_entry", (PyCFunction)(void(*)(void))(__Pyx_PyCFunction_FastCallWithKeywords)__pyx_pw_6Cython_8Compiler_8Scanning_22StringSourceDescriptor_7get_filenametable_entry, __Pyx_METH_FASTCALL|METH_KEYWORDS, __pyx_doc_6Cython_8Compiler_8Scanning_22StringSourceDescriptor_6get_filenametable_entry};
static PyObject *__pyx_pw_6Cython_8Compiler_8Scanning_22StringSourceDescriptor_7get_filenametable_entry(PyObject *__pyx_self, 
#if CYTHON_METH_FASTCALL
PyObject *const *__pyx_args, Py_ssize_t __pyx_nargs, PyObject *__pyx_kwds
#else
PyObject *__pyx_args, PyObject *__pyx_kwds
#endif
) {
  CYTHON_UNUSED PyObject *__pyx_v_self = 0;
  #if !CYTHON_METH_FASTCALL
  CYTHON_UNUSED Py_ssize_t __pyx_nargs;
  #endif
  CYTHON_UNUSED PyObject *const *__pyx_kwvalues;
  PyObject *__pyx_r = 0;
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("get_filenametable_entry (wrapper)", 0);
  #if !CYTHON_METH_FASTCALL
  #if CYTHON_ASSUME_SAFE_SIZE
  __pyx_nargs = PyTuple_GET_SIZE(__pyx_args);
  #else
  __pyx_nargs = PyTuple_Size(__pyx_args); if (unlikely(__pyx_nargs < 0)) return NULL;
  #endif
  #endif
  __pyx_kwvalues = __Pyx_KwValues_FASTCALL(__pyx_args, __pyx_nargs);
  {
    PyObject ** const __pyx_pyargnames[] = {&__pyx_mstate_global->__pyx_n_u_self,0};
  PyObject* values[1] = {0};
    const Py_ssize_t __pyx_kwds_len = (__pyx_kwds) ? __Pyx_NumKwargs_FASTCALL(__pyx_kwds) : 0;
    if (unlikely(__pyx_kwds_len) < 0) __PYX_ERR(0, 274, __pyx_L3_error)
    if (__pyx_kwds_len > 0) {
      switch (__pyx_nargs) {
        case  1:
        values[0] = __Pyx_ArgRef_FASTCALL(__pyx_args, 0);
        if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[0])) __PYX_ERR(0, 274, __pyx_L3_error)
        CYTHON_FALLTHROUGH;
        case  0: break;
        default: goto __pyx_L5_argtuple_error;
      }
      const Py_ssize_t kwd_pos_args = __pyx_nargs;
      if (__Pyx_ParseKeywords(__pyx_kwds, __pyx_kwvalues, __pyx_pyargnames, 0, values, kwd_pos_args, __pyx_kwds_len, "get_filenametable_entry", 0) < (0)) __PYX_ERR(0, 274, __pyx_L3_error)
      for (Py_ssize_t i = __pyx_nargs; i < 1; i++) {
        if (unlikely(!values[i])) { __Pyx_RaiseArgtupleInvalid("get_filenametable_entry", 1, 1, 1, i); __PYX_ERR(0, 274, __pyx_L3_error) }
      }
    } else if (unlikely(__pyx_nargs != 1)) {
      goto __pyx_L5_argtuple_error;
    } else {
      values[0] = __Pyx_ArgRef_FASTCALL(__pyx_args, 0);
      if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[0])) __PYX_ERR(0, 274, __pyx_L3_error)
    }
    __pyx_v_self = values[0];
  }
  goto __pyx_L6_skip;
  __pyx_L5_argtuple_error:;
  __Pyx_RaiseArgtupleInvalid("get_filenametable_entry", 1, 1, 1, __pyx_nargs); __PYX_ERR(0, 274, __pyx_L3_error)
  __pyx_L6_skip:;
  goto __pyx_L4_argument_unpacking_done;
  __pyx_L3_error:;
  for (Py_ssize_t __pyx_temp=0; __pyx_temp < (Py_ssize_t)(sizeof(values)/sizeof(values[0])); ++__pyx_temp) {
    Py_XDECREF(values[__pyx_temp]);
  }
  __Pyx_AddTraceback("Cython.Compiler.Scanning.StringSourceDescriptor.get_filenametable_entry", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __Pyx_RefNannyFinishContext();
  return NULL;
  __pyx_L4_argument_unpacking_done:;
  __pyx_r = __pyx_pf_6Cython_8Compiler_8Scanning_22StringSourceDescriptor_6get_filenametable_entry(__pyx_self, __pyx_v_self);
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

static PyObject *__pyx_pf_6Cython_8Compiler_8Scanning_22StringSourceDescriptor_6get_filenametable_entry(CYTHON_UNUSED PyObject *__pyx_self, CYTHON_UNUSED PyObject *__pyx_v_self) {
  PyObject *__pyx_r = NULL;
/* … */
  /* function exit code */
  __pyx_L0:;
  __Pyx_XGIVEREF(__pyx_r);
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}
/* … */
  __pyx_t_2 = __Pyx_PyDict_NewPresized(1); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 274, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  #if defined(PyDict_SetItem) && (defined(CYTHON_COMPILING_IN_CPYTHON))
  #if PY_VERSION_HEX >= 0x030A0000 /* CPython 3.10+ exposes KnownHash APIs */
  /* Use CPython's KnownHash APIs when available */
  extern int _PyDict_SetItem_KnownHash(PyObject*, PyObject*, PyObject*, Py_hash_t);
  {
    Py_hash_t __pyx_hash = PyObject_Hash(__pyx_mstate_global->__pyx_n_u_return); if (unlikely(__pyx_hash == -1)) __PYX_ERR(0, 274, __pyx_L1_error);
    if (unlikely(_PyDict_SetItem_KnownHash(__pyx_t_2, __pyx_mstate_global->__pyx_n_u_return, __pyx_mstate_global->__pyx_n_u_str, __pyx_hash) < 0)) __PYX_ERR(0, 274, __pyx_L1_error);
  }
  #else
  if (PyDict_SetItem(__pyx_t_2, __pyx_mstate_global->__pyx_n_u_return, __pyx_mstate_global->__pyx_n_u_str) < (0)) __PYX_ERR(0, 274, __pyx_L1_error)
  #endif
  #else
  if (PyDict_SetItem(__pyx_t_2, __pyx_mstate_global->__pyx_n_u_return, __pyx_mstate_global->__pyx_n_u_str) < (0)) __PYX_ERR(0, 274, __pyx_L1_error)
  #endif
  __pyx_t_8 = __Pyx_CyFunction_New(&__pyx_mdef_6Cython_8Compiler_8Scanning_22StringSourceDescriptor_7get_filenametable_entry, 0, __pyx_mstate_global->__pyx_n_u_StringSourceDescriptor_get_filen, NULL, __pyx_mstate_global->__pyx_n_u_Cython_Compiler_Scanning, __pyx_mstate_global->__pyx_d, ((PyObject *)__pyx_mstate_global->__pyx_codeobj_tab[31])); if (unlikely(!__pyx_t_8)) __PYX_ERR(0, 274, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_8);
  #if CYTHON_COMPILING_IN_CPYTHON && PY_VERSION_HEX >= 0x030E0000
  PyUnstable_Object_EnableDeferredRefcount(__pyx_t_8);
  #endif
  __Pyx_CyFunction_SetAnnotationsDict(__pyx_t_8, __pyx_t_2);
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  if (__Pyx_SetNameInClass(__pyx_t_6, __pyx_mstate_global->__pyx_n_u_get_filenametable_entry, __pyx_t_8) < (0)) __PYX_ERR(0, 274, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_8); __pyx_t_8 = 0;
```

</details>

L275  🟡  (score=2)
```python
        return "<stringsource>"
```
<details><summary>Show generated C (score=2)</summary>

```c
  __Pyx_XDECREF(__pyx_r);
  __Pyx_INCREF(__pyx_mstate_global->__pyx_kp_u_stringsource);
  __pyx_r = __pyx_mstate_global->__pyx_kp_u_stringsource;
  goto __pyx_L0;
```

</details>

L276  ⚪  (score=0)
```python
```
L277  🔴  (score=37)
```python
    def __hash__(self):
```
<details><summary>Show generated C (score=37)</summary>

```c
/* Python wrapper */
static PyObject *__pyx_pw_6Cython_8Compiler_8Scanning_22StringSourceDescriptor_9__hash__(PyObject *__pyx_self, 
#if CYTHON_METH_FASTCALL
PyObject *const *__pyx_args, Py_ssize_t __pyx_nargs, PyObject *__pyx_kwds
#else
PyObject *__pyx_args, PyObject *__pyx_kwds
#endif
); /*proto*/
PyDoc_STRVAR(__pyx_doc_6Cython_8Compiler_8Scanning_22StringSourceDescriptor_8__hash__, "File: Cython/Compiler/Scanning.py (starting at line 277)");
static PyMethodDef __pyx_mdef_6Cython_8Compiler_8Scanning_22StringSourceDescriptor_9__hash__ = {"__hash__", (PyCFunction)(void(*)(void))(__Pyx_PyCFunction_FastCallWithKeywords)__pyx_pw_6Cython_8Compiler_8Scanning_22StringSourceDescriptor_9__hash__, __Pyx_METH_FASTCALL|METH_KEYWORDS, __pyx_doc_6Cython_8Compiler_8Scanning_22StringSourceDescriptor_8__hash__};
static PyObject *__pyx_pw_6Cython_8Compiler_8Scanning_22StringSourceDescriptor_9__hash__(PyObject *__pyx_self, 
#if CYTHON_METH_FASTCALL
PyObject *const *__pyx_args, Py_ssize_t __pyx_nargs, PyObject *__pyx_kwds
#else
PyObject *__pyx_args, PyObject *__pyx_kwds
#endif
) {
  PyObject *__pyx_v_self = 0;
  #if !CYTHON_METH_FASTCALL
  CYTHON_UNUSED Py_ssize_t __pyx_nargs;
  #endif
  CYTHON_UNUSED PyObject *const *__pyx_kwvalues;
  PyObject *__pyx_r = 0;
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("__hash__ (wrapper)", 0);
  #if !CYTHON_METH_FASTCALL
  #if CYTHON_ASSUME_SAFE_SIZE
  __pyx_nargs = PyTuple_GET_SIZE(__pyx_args);
  #else
  __pyx_nargs = PyTuple_Size(__pyx_args); if (unlikely(__pyx_nargs < 0)) return NULL;
  #endif
  #endif
  __pyx_kwvalues = __Pyx_KwValues_FASTCALL(__pyx_args, __pyx_nargs);
  {
    PyObject ** const __pyx_pyargnames[] = {&__pyx_mstate_global->__pyx_n_u_self,0};
  PyObject* values[1] = {0};
    const Py_ssize_t __pyx_kwds_len = (__pyx_kwds) ? __Pyx_NumKwargs_FASTCALL(__pyx_kwds) : 0;
    if (unlikely(__pyx_kwds_len) < 0) __PYX_ERR(0, 277, __pyx_L3_error)
    if (__pyx_kwds_len > 0) {
      switch (__pyx_nargs) {
        case  1:
        values[0] = __Pyx_ArgRef_FASTCALL(__pyx_args, 0);
        if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[0])) __PYX_ERR(0, 277, __pyx_L3_error)
        CYTHON_FALLTHROUGH;
        case  0: break;
        default: goto __pyx_L5_argtuple_error;
      }
      const Py_ssize_t kwd_pos_args = __pyx_nargs;
      if (__Pyx_ParseKeywords(__pyx_kwds, __pyx_kwvalues, __pyx_pyargnames, 0, values, kwd_pos_args, __pyx_kwds_len, "__hash__", 0) < (0)) __PYX_ERR(0, 277, __pyx_L3_error)
      for (Py_ssize_t i = __pyx_nargs; i < 1; i++) {
        if (unlikely(!values[i])) { __Pyx_RaiseArgtupleInvalid("__hash__", 1, 1, 1, i); __PYX_ERR(0, 277, __pyx_L3_error) }
      }
    } else if (unlikely(__pyx_nargs != 1)) {
      goto __pyx_L5_argtuple_error;
    } else {
      values[0] = __Pyx_ArgRef_FASTCALL(__pyx_args, 0);
      if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[0])) __PYX_ERR(0, 277, __pyx_L3_error)
    }
    __pyx_v_self = values[0];
  }
  goto __pyx_L6_skip;
  __pyx_L5_argtuple_error:;
  __Pyx_RaiseArgtupleInvalid("__hash__", 1, 1, 1, __pyx_nargs); __PYX_ERR(0, 277, __pyx_L3_error)
  __pyx_L6_skip:;
  goto __pyx_L4_argument_unpacking_done;
  __pyx_L3_error:;
  for (Py_ssize_t __pyx_temp=0; __pyx_temp < (Py_ssize_t)(sizeof(values)/sizeof(values[0])); ++__pyx_temp) {
    Py_XDECREF(values[__pyx_temp]);
  }
  __Pyx_AddTraceback("Cython.Compiler.Scanning.StringSourceDescriptor.__hash__", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __Pyx_RefNannyFinishContext();
  return NULL;
  __pyx_L4_argument_unpacking_done:;
  __pyx_r = __pyx_pf_6Cython_8Compiler_8Scanning_22StringSourceDescriptor_8__hash__(__pyx_self, __pyx_v_self);
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

static PyObject *__pyx_pf_6Cython_8Compiler_8Scanning_22StringSourceDescriptor_8__hash__(CYTHON_UNUSED PyObject *__pyx_self, PyObject *__pyx_v_self) {
  PyObject *__pyx_r = NULL;
/* … */
  /* function exit code */
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_t_1);
  __Pyx_XDECREF(__pyx_t_2);
  __Pyx_AddTraceback("Cython.Compiler.Scanning.StringSourceDescriptor.__hash__", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_r = NULL;
  __pyx_L0:;
  __Pyx_XGIVEREF(__pyx_r);
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}
/* … */
  __pyx_t_8 = __Pyx_CyFunction_New(&__pyx_mdef_6Cython_8Compiler_8Scanning_22StringSourceDescriptor_9__hash__, 0, __pyx_mstate_global->__pyx_n_u_StringSourceDescriptor___hash, NULL, __pyx_mstate_global->__pyx_n_u_Cython_Compiler_Scanning, __pyx_mstate_global->__pyx_d, ((PyObject *)__pyx_mstate_global->__pyx_codeobj_tab[32])); if (unlikely(!__pyx_t_8)) __PYX_ERR(0, 277, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_8);
  #if CYTHON_COMPILING_IN_CPYTHON && PY_VERSION_HEX >= 0x030E0000
  PyUnstable_Object_EnableDeferredRefcount(__pyx_t_8);
  #endif
  if (__Pyx_SetNameInClass(__pyx_t_6, __pyx_mstate_global->__pyx_n_u_hash_2, __pyx_t_8) < (0)) __PYX_ERR(0, 277, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_8); __pyx_t_8 = 0;
```

</details>

L278  🟡  (score=4)
```python
        return id(self)
```
<details><summary>Show generated C (score=4)</summary>

```c
  __Pyx_XDECREF(__pyx_r);
  __pyx_t_2 = NULL;
  __pyx_t_3 = 1;
  {
    PyObject *__pyx_callargs[2] = {__pyx_t_2, __pyx_v_self};
    __pyx_t_1 = __Pyx_PyObject_FastCall((PyObject*)__pyx_builtin_id, __pyx_callargs+__pyx_t_3, (2-__pyx_t_3) | (__pyx_t_3*__Pyx_PY_VECTORCALL_ARGUMENTS_OFFSET));
    __Pyx_XDECREF(__pyx_t_2); __pyx_t_2 = 0;
    if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 278, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_1);
  }
  __pyx_r = __pyx_t_1;
  __pyx_t_1 = 0;
  goto __pyx_L0;
```

</details>

L279  ⚪  (score=0)
```python
        # Do not hash on the name, an identical string source should be the
```
L280  ⚪  (score=0)
```python
        # same object (name is often defaulted in other places)
```
L281  ⚪  (score=0)
```python
```
L282  🔴  (score=43)
```python
    def __eq__(self, other):
```
<details><summary>Show generated C (score=43)</summary>

```c
/* Python wrapper */
static PyObject *__pyx_pw_6Cython_8Compiler_8Scanning_22StringSourceDescriptor_11__eq__(PyObject *__pyx_self, 
#if CYTHON_METH_FASTCALL
PyObject *const *__pyx_args, Py_ssize_t __pyx_nargs, PyObject *__pyx_kwds
#else
PyObject *__pyx_args, PyObject *__pyx_kwds
#endif
); /*proto*/
PyDoc_STRVAR(__pyx_doc_6Cython_8Compiler_8Scanning_22StringSourceDescriptor_10__eq__, "File: Cython/Compiler/Scanning.py (starting at line 282)");
static PyMethodDef __pyx_mdef_6Cython_8Compiler_8Scanning_22StringSourceDescriptor_11__eq__ = {"__eq__", (PyCFunction)(void(*)(void))(__Pyx_PyCFunction_FastCallWithKeywords)__pyx_pw_6Cython_8Compiler_8Scanning_22StringSourceDescriptor_11__eq__, __Pyx_METH_FASTCALL|METH_KEYWORDS, __pyx_doc_6Cython_8Compiler_8Scanning_22StringSourceDescriptor_10__eq__};
static PyObject *__pyx_pw_6Cython_8Compiler_8Scanning_22StringSourceDescriptor_11__eq__(PyObject *__pyx_self, 
#if CYTHON_METH_FASTCALL
PyObject *const *__pyx_args, Py_ssize_t __pyx_nargs, PyObject *__pyx_kwds
#else
PyObject *__pyx_args, PyObject *__pyx_kwds
#endif
) {
  PyObject *__pyx_v_self = 0;
  PyObject *__pyx_v_other = 0;
  #if !CYTHON_METH_FASTCALL
  CYTHON_UNUSED Py_ssize_t __pyx_nargs;
  #endif
  CYTHON_UNUSED PyObject *const *__pyx_kwvalues;
  PyObject *__pyx_r = 0;
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("__eq__ (wrapper)", 0);
  #if !CYTHON_METH_FASTCALL
  #if CYTHON_ASSUME_SAFE_SIZE
  __pyx_nargs = PyTuple_GET_SIZE(__pyx_args);
  #else
  __pyx_nargs = PyTuple_Size(__pyx_args); if (unlikely(__pyx_nargs < 0)) return NULL;
  #endif
  #endif
  __pyx_kwvalues = __Pyx_KwValues_FASTCALL(__pyx_args, __pyx_nargs);
  {
    PyObject ** const __pyx_pyargnames[] = {&__pyx_mstate_global->__pyx_n_u_self,&__pyx_mstate_global->__pyx_n_u_other,0};
  PyObject* values[2] = {0,0};
    const Py_ssize_t __pyx_kwds_len = (__pyx_kwds) ? __Pyx_NumKwargs_FASTCALL(__pyx_kwds) : 0;
    if (unlikely(__pyx_kwds_len) < 0) __PYX_ERR(0, 282, __pyx_L3_error)
    if (__pyx_kwds_len > 0) {
      switch (__pyx_nargs) {
        case  2:
        values[1] = __Pyx_ArgRef_FASTCALL(__pyx_args, 1);
        if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[1])) __PYX_ERR(0, 282, __pyx_L3_error)
        CYTHON_FALLTHROUGH;
        case  1:
        values[0] = __Pyx_ArgRef_FASTCALL(__pyx_args, 0);
        if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[0])) __PYX_ERR(0, 282, __pyx_L3_error)
        CYTHON_FALLTHROUGH;
        case  0: break;
        default: goto __pyx_L5_argtuple_error;
      }
      const Py_ssize_t kwd_pos_args = __pyx_nargs;
      if (__Pyx_ParseKeywords(__pyx_kwds, __pyx_kwvalues, __pyx_pyargnames, 0, values, kwd_pos_args, __pyx_kwds_len, "__eq__", 0) < (0)) __PYX_ERR(0, 282, __pyx_L3_error)
      for (Py_ssize_t i = __pyx_nargs; i < 2; i++) {
        if (unlikely(!values[i])) { __Pyx_RaiseArgtupleInvalid("__eq__", 1, 2, 2, i); __PYX_ERR(0, 282, __pyx_L3_error) }
      }
    } else if (unlikely(__pyx_nargs != 2)) {
      goto __pyx_L5_argtuple_error;
    } else {
      values[0] = __Pyx_ArgRef_FASTCALL(__pyx_args, 0);
      if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[0])) __PYX_ERR(0, 282, __pyx_L3_error)
      values[1] = __Pyx_ArgRef_FASTCALL(__pyx_args, 1);
      if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[1])) __PYX_ERR(0, 282, __pyx_L3_error)
    }
    __pyx_v_self = values[0];
    __pyx_v_other = values[1];
  }
  goto __pyx_L6_skip;
  __pyx_L5_argtuple_error:;
  __Pyx_RaiseArgtupleInvalid("__eq__", 1, 2, 2, __pyx_nargs); __PYX_ERR(0, 282, __pyx_L3_error)
  __pyx_L6_skip:;
  goto __pyx_L4_argument_unpacking_done;
  __pyx_L3_error:;
  for (Py_ssize_t __pyx_temp=0; __pyx_temp < (Py_ssize_t)(sizeof(values)/sizeof(values[0])); ++__pyx_temp) {
    Py_XDECREF(values[__pyx_temp]);
  }
  __Pyx_AddTraceback("Cython.Compiler.Scanning.StringSourceDescriptor.__eq__", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __Pyx_RefNannyFinishContext();
  return NULL;
  __pyx_L4_argument_unpacking_done:;
  __pyx_r = __pyx_pf_6Cython_8Compiler_8Scanning_22StringSourceDescriptor_10__eq__(__pyx_self, __pyx_v_self, __pyx_v_other);
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

static PyObject *__pyx_pf_6Cython_8Compiler_8Scanning_22StringSourceDescriptor_10__eq__(CYTHON_UNUSED PyObject *__pyx_self, PyObject *__pyx_v_self, PyObject *__pyx_v_other) {
  PyObject *__pyx_r = NULL;
/* … */
  /* function exit code */
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_t_1);
  __Pyx_XDECREF(__pyx_t_2);
  __Pyx_XDECREF(__pyx_t_4);
  __Pyx_XDECREF(__pyx_t_5);
  __Pyx_AddTraceback("Cython.Compiler.Scanning.StringSourceDescriptor.__eq__", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_r = NULL;
  __pyx_L0:;
  __Pyx_XGIVEREF(__pyx_r);
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}
/* … */
  __pyx_t_8 = __Pyx_CyFunction_New(&__pyx_mdef_6Cython_8Compiler_8Scanning_22StringSourceDescriptor_11__eq__, 0, __pyx_mstate_global->__pyx_n_u_StringSourceDescriptor___eq, NULL, __pyx_mstate_global->__pyx_n_u_Cython_Compiler_Scanning, __pyx_mstate_global->__pyx_d, ((PyObject *)__pyx_mstate_global->__pyx_codeobj_tab[33])); if (unlikely(!__pyx_t_8)) __PYX_ERR(0, 282, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_8);
  #if CYTHON_COMPILING_IN_CPYTHON && PY_VERSION_HEX >= 0x030E0000
  PyUnstable_Object_EnableDeferredRefcount(__pyx_t_8);
  #endif
  if (__Pyx_SetNameInClass(__pyx_t_6, __pyx_mstate_global->__pyx_n_u_eq, __pyx_t_8) < (0)) __PYX_ERR(0, 282, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_8); __pyx_t_8 = 0;
```

</details>

L283  🔴  (score=24)
```python
        return isinstance(other, StringSourceDescriptor) and self.name == other.name
```
<details><summary>Show generated C (score=24)</summary>

```c
  __Pyx_XDECREF(__pyx_r);
  __Pyx_GetModuleGlobalName(__pyx_t_2, __pyx_mstate_global->__pyx_n_u_StringSourceDescriptor); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 283, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __pyx_t_3 = PyObject_IsInstance(__pyx_v_other, __pyx_t_2); if (unlikely(__pyx_t_3 == ((int)-1))) __PYX_ERR(0, 283, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  if (__pyx_t_3) {
  } else {
    __pyx_t_2 = __Pyx_PyBool_FromLong(__pyx_t_3); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 283, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_2);
    __pyx_t_1 = __pyx_t_2;
    __pyx_t_2 = 0;
    goto __pyx_L3_bool_binop_done;
  }
  __pyx_t_2 = __Pyx_PyObject_GetAttrStr(__pyx_v_self, __pyx_mstate_global->__pyx_n_u_name); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 283, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __pyx_t_4 = __Pyx_PyObject_GetAttrStr(__pyx_v_other, __pyx_mstate_global->__pyx_n_u_name); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 283, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_4);
  __pyx_t_5 = PyObject_RichCompare(__pyx_t_2, __pyx_t_4, Py_EQ); __Pyx_XGOTREF(__pyx_t_5); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 283, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
  __Pyx_INCREF(__pyx_t_5);
  __pyx_t_1 = __pyx_t_5;
  __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
  __pyx_L3_bool_binop_done:;
  __pyx_r = __pyx_t_1;
  __pyx_t_1 = 0;
  goto __pyx_L0;
```

</details>

L284  ⚪  (score=0)
```python
```
L285  🔴  (score=37)
```python
    def __repr__(self):
```
<details><summary>Show generated C (score=37)</summary>

```c
/* Python wrapper */
static PyObject *__pyx_pw_6Cython_8Compiler_8Scanning_22StringSourceDescriptor_13__repr__(PyObject *__pyx_self, 
#if CYTHON_METH_FASTCALL
PyObject *const *__pyx_args, Py_ssize_t __pyx_nargs, PyObject *__pyx_kwds
#else
PyObject *__pyx_args, PyObject *__pyx_kwds
#endif
); /*proto*/
PyDoc_STRVAR(__pyx_doc_6Cython_8Compiler_8Scanning_22StringSourceDescriptor_12__repr__, "File: Cython/Compiler/Scanning.py (starting at line 285)");
static PyMethodDef __pyx_mdef_6Cython_8Compiler_8Scanning_22StringSourceDescriptor_13__repr__ = {"__repr__", (PyCFunction)(void(*)(void))(__Pyx_PyCFunction_FastCallWithKeywords)__pyx_pw_6Cython_8Compiler_8Scanning_22StringSourceDescriptor_13__repr__, __Pyx_METH_FASTCALL|METH_KEYWORDS, __pyx_doc_6Cython_8Compiler_8Scanning_22StringSourceDescriptor_12__repr__};
static PyObject *__pyx_pw_6Cython_8Compiler_8Scanning_22StringSourceDescriptor_13__repr__(PyObject *__pyx_self, 
#if CYTHON_METH_FASTCALL
PyObject *const *__pyx_args, Py_ssize_t __pyx_nargs, PyObject *__pyx_kwds
#else
PyObject *__pyx_args, PyObject *__pyx_kwds
#endif
) {
  PyObject *__pyx_v_self = 0;
  #if !CYTHON_METH_FASTCALL
  CYTHON_UNUSED Py_ssize_t __pyx_nargs;
  #endif
  CYTHON_UNUSED PyObject *const *__pyx_kwvalues;
  PyObject *__pyx_r = 0;
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("__repr__ (wrapper)", 0);
  #if !CYTHON_METH_FASTCALL
  #if CYTHON_ASSUME_SAFE_SIZE
  __pyx_nargs = PyTuple_GET_SIZE(__pyx_args);
  #else
  __pyx_nargs = PyTuple_Size(__pyx_args); if (unlikely(__pyx_nargs < 0)) return NULL;
  #endif
  #endif
  __pyx_kwvalues = __Pyx_KwValues_FASTCALL(__pyx_args, __pyx_nargs);
  {
    PyObject ** const __pyx_pyargnames[] = {&__pyx_mstate_global->__pyx_n_u_self,0};
  PyObject* values[1] = {0};
    const Py_ssize_t __pyx_kwds_len = (__pyx_kwds) ? __Pyx_NumKwargs_FASTCALL(__pyx_kwds) : 0;
    if (unlikely(__pyx_kwds_len) < 0) __PYX_ERR(0, 285, __pyx_L3_error)
    if (__pyx_kwds_len > 0) {
      switch (__pyx_nargs) {
        case  1:
        values[0] = __Pyx_ArgRef_FASTCALL(__pyx_args, 0);
        if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[0])) __PYX_ERR(0, 285, __pyx_L3_error)
        CYTHON_FALLTHROUGH;
        case  0: break;
        default: goto __pyx_L5_argtuple_error;
      }
      const Py_ssize_t kwd_pos_args = __pyx_nargs;
      if (__Pyx_ParseKeywords(__pyx_kwds, __pyx_kwvalues, __pyx_pyargnames, 0, values, kwd_pos_args, __pyx_kwds_len, "__repr__", 0) < (0)) __PYX_ERR(0, 285, __pyx_L3_error)
      for (Py_ssize_t i = __pyx_nargs; i < 1; i++) {
        if (unlikely(!values[i])) { __Pyx_RaiseArgtupleInvalid("__repr__", 1, 1, 1, i); __PYX_ERR(0, 285, __pyx_L3_error) }
      }
    } else if (unlikely(__pyx_nargs != 1)) {
      goto __pyx_L5_argtuple_error;
    } else {
      values[0] = __Pyx_ArgRef_FASTCALL(__pyx_args, 0);
      if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[0])) __PYX_ERR(0, 285, __pyx_L3_error)
    }
    __pyx_v_self = values[0];
  }
  goto __pyx_L6_skip;
  __pyx_L5_argtuple_error:;
  __Pyx_RaiseArgtupleInvalid("__repr__", 1, 1, 1, __pyx_nargs); __PYX_ERR(0, 285, __pyx_L3_error)
  __pyx_L6_skip:;
  goto __pyx_L4_argument_unpacking_done;
  __pyx_L3_error:;
  for (Py_ssize_t __pyx_temp=0; __pyx_temp < (Py_ssize_t)(sizeof(values)/sizeof(values[0])); ++__pyx_temp) {
    Py_XDECREF(values[__pyx_temp]);
  }
  __Pyx_AddTraceback("Cython.Compiler.Scanning.StringSourceDescriptor.__repr__", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __Pyx_RefNannyFinishContext();
  return NULL;
  __pyx_L4_argument_unpacking_done:;
  __pyx_r = __pyx_pf_6Cython_8Compiler_8Scanning_22StringSourceDescriptor_12__repr__(__pyx_self, __pyx_v_self);
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

static PyObject *__pyx_pf_6Cython_8Compiler_8Scanning_22StringSourceDescriptor_12__repr__(CYTHON_UNUSED PyObject *__pyx_self, PyObject *__pyx_v_self) {
  PyObject *__pyx_r = NULL;
/* … */
  /* function exit code */
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_t_1);
  __Pyx_XDECREF(__pyx_t_2);
  __Pyx_AddTraceback("Cython.Compiler.Scanning.StringSourceDescriptor.__repr__", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_r = NULL;
  __pyx_L0:;
  __Pyx_XGIVEREF(__pyx_r);
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}
/* … */
  __pyx_t_8 = __Pyx_CyFunction_New(&__pyx_mdef_6Cython_8Compiler_8Scanning_22StringSourceDescriptor_13__repr__, 0, __pyx_mstate_global->__pyx_n_u_StringSourceDescriptor___repr, NULL, __pyx_mstate_global->__pyx_n_u_Cython_Compiler_Scanning, __pyx_mstate_global->__pyx_d, ((PyObject *)__pyx_mstate_global->__pyx_codeobj_tab[34])); if (unlikely(!__pyx_t_8)) __PYX_ERR(0, 285, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_8);
  #if CYTHON_COMPILING_IN_CPYTHON && PY_VERSION_HEX >= 0x030E0000
  PyUnstable_Object_EnableDeferredRefcount(__pyx_t_8);
  #endif
  if (__Pyx_SetNameInClass(__pyx_t_6, __pyx_mstate_global->__pyx_n_u_repr_2, __pyx_t_8) < (0)) __PYX_ERR(0, 285, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_8); __pyx_t_8 = 0;
```

</details>

L286  🔴  (score=13)
```python
        return f"<StringSourceDescriptor:{self.name}>"
```
<details><summary>Show generated C (score=13)</summary>

```c
  __Pyx_XDECREF(__pyx_r);
  __pyx_t_1 = __Pyx_PyObject_GetAttrStr(__pyx_v_self, __pyx_mstate_global->__pyx_n_u_name); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 286, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __pyx_t_2 = __Pyx_PyObject_FormatSimple(__pyx_t_1, __pyx_mstate_global->__pyx_empty_unicode); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 286, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __pyx_t_3[0] = __pyx_mstate_global->__pyx_kp_u_StringSourceDescriptor_2;
  __pyx_t_3[1] = __pyx_t_2;
  __pyx_t_3[2] = __pyx_mstate_global->__pyx_kp_u__4;
  __pyx_t_1 = __Pyx_PyUnicode_Join(__pyx_t_3, 3, 24 + __Pyx_PyUnicode_GET_LENGTH(__pyx_t_2) + 1, 127 | __Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_2));
  if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 286, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __pyx_r = __pyx_t_1;
  __pyx_t_1 = 0;
  goto __pyx_L0;
```

</details>

L287  ⚪  (score=0)
```python
```
L288  ⚪  (score=0)
```python
```
L289  ⚪  (score=0)
```python
#------------------------------------------------------------------
```
L290  ⚪  (score=0)
```python
```
L291  🔴  (score=30)
```python
class PyrexScanner(Scanner):
```
<details><summary>Show generated C (score=30)</summary>

```c
  __Pyx_GetModuleGlobalName(__pyx_t_4, __pyx_mstate_global->__pyx_n_u_Scanner); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 291, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_4);
  __pyx_t_7 = PyTuple_Pack(1, __pyx_t_4); if (unlikely(!__pyx_t_7)) __PYX_ERR(0, 291, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_7);
  __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
  __pyx_t_4 = __Pyx_PEP560_update_bases(__pyx_t_7); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 291, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_4);
  __pyx_t_6 = __Pyx_CalculateMetaclass(NULL, __pyx_t_4); if (unlikely(!__pyx_t_6)) __PYX_ERR(0, 291, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_6);
  __pyx_t_8 = __Pyx_Py3MetaclassPrepare(__pyx_t_6, __pyx_t_4, __pyx_mstate_global->__pyx_n_u_PyrexScanner, __pyx_mstate_global->__pyx_n_u_PyrexScanner, (PyObject *) NULL, __pyx_mstate_global->__pyx_n_u_Cython_Compiler_Scanning, (PyObject *) NULL); if (unlikely(!__pyx_t_8)) __PYX_ERR(0, 291, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_8);
  if (__pyx_t_4 != __pyx_t_7) {
    if (unlikely((PyDict_SetItemString(__pyx_t_8, "__orig_bases__", __pyx_t_7) < 0))) __PYX_ERR(0, 291, __pyx_L1_error)
  }
  __Pyx_DECREF(__pyx_t_7); __pyx_t_7 = 0;
/* … */
  __pyx_t_2 = __Pyx_Py3ClassCreate(__pyx_t_6, __pyx_mstate_global->__pyx_n_u_PyrexScanner, __pyx_t_4, __pyx_t_8, NULL, 0, 0); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 291, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  #if CYTHON_COMPILING_IN_CPYTHON && PY_VERSION_HEX >= 0x030E0000
  PyUnstable_Object_EnableDeferredRefcount(__pyx_t_2);
  #endif
  if (PyDict_SetItem(__pyx_mstate_global->__pyx_d, __pyx_mstate_global->__pyx_n_u_PyrexScanner, __pyx_t_2) < (0)) __PYX_ERR(0, 291, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __Pyx_DECREF(__pyx_t_8); __pyx_t_8 = 0;
  __Pyx_DECREF(__pyx_t_6); __pyx_t_6 = 0;
  __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
```

</details>

L292  ⚪  (score=0)
```python
    #  context            Context  Compilation context
```
L293  ⚪  (score=0)
```python
    #  included_files     [string] Files included with 'include' statement
```
L294  ⚪  (score=0)
```python
    #  compile_time_env   dict     Environment for conditional compilation
```
L295  ⚪  (score=0)
```python
    #  compile_time_eval  boolean  In a true conditional compilation context
```
L296  ⚪  (score=0)
```python
    #  compile_time_expr  boolean  In a compile-time expression context
```
L297  ⚪  (score=0)
```python
    #  put_back_on_failure  list or None  If set, this records states so the tentatively_scan
```
L298  ⚪  (score=0)
```python
    #                                       contextmanager can restore it
```
L299  ⚪  (score=0)
```python
```
L300  🔴  (score=270)
```python
    def __init__(self, file:IO, filename:SourceDescriptor, parent_scanner:"PyrexScanner|None"=None,
```
<details><summary>Show generated C (score=270)</summary>

```c
/* Python wrapper */
static PyObject *__pyx_pw_6Cython_8Compiler_8Scanning_12PyrexScanner_1__init__(PyObject *__pyx_self, 
#if CYTHON_METH_FASTCALL
PyObject *const *__pyx_args, Py_ssize_t __pyx_nargs, PyObject *__pyx_kwds
#else
PyObject *__pyx_args, PyObject *__pyx_kwds
#endif
); /*proto*/
PyDoc_STRVAR(__pyx_doc_6Cython_8Compiler_8Scanning_12PyrexScanner___init__, "File: Cython/Compiler/Scanning.py (starting at line 300)");
static PyMethodDef __pyx_mdef_6Cython_8Compiler_8Scanning_12PyrexScanner_1__init__ = {"__init__", (PyCFunction)(void(*)(void))(__Pyx_PyCFunction_FastCallWithKeywords)__pyx_pw_6Cython_8Compiler_8Scanning_12PyrexScanner_1__init__, __Pyx_METH_FASTCALL|METH_KEYWORDS, __pyx_doc_6Cython_8Compiler_8Scanning_12PyrexScanner___init__};
static PyObject *__pyx_pw_6Cython_8Compiler_8Scanning_12PyrexScanner_1__init__(PyObject *__pyx_self, 
#if CYTHON_METH_FASTCALL
PyObject *const *__pyx_args, Py_ssize_t __pyx_nargs, PyObject *__pyx_kwds
#else
PyObject *__pyx_args, PyObject *__pyx_kwds
#endif
) {
  PyObject *__pyx_v_self = 0;
  PyObject *__pyx_v_file = 0;
  PyObject *__pyx_v_filename = 0;
  PyObject *__pyx_v_parent_scanner = 0;
  PyObject *__pyx_v_scope = 0;
  PyObject *__pyx_v_context = 0;
  PyObject *__pyx_v_source_encoding = 0;
  int __pyx_v_parse_comments;
  PyObject *__pyx_v_initial_pos = 0;
  #if !CYTHON_METH_FASTCALL
  CYTHON_UNUSED Py_ssize_t __pyx_nargs;
  #endif
  CYTHON_UNUSED PyObject *const *__pyx_kwvalues;
  PyObject *__pyx_r = 0;
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("__init__ (wrapper)", 0);
  #if !CYTHON_METH_FASTCALL
  #if CYTHON_ASSUME_SAFE_SIZE
  __pyx_nargs = PyTuple_GET_SIZE(__pyx_args);
  #else
  __pyx_nargs = PyTuple_Size(__pyx_args); if (unlikely(__pyx_nargs < 0)) return NULL;
  #endif
  #endif
  __pyx_kwvalues = __Pyx_KwValues_FASTCALL(__pyx_args, __pyx_nargs);
  {
    PyObject ** const __pyx_pyargnames[] = {&__pyx_mstate_global->__pyx_n_u_self,&__pyx_mstate_global->__pyx_n_u_file,&__pyx_mstate_global->__pyx_n_u_filename,&__pyx_mstate_global->__pyx_n_u_parent_scanner,&__pyx_mstate_global->__pyx_n_u_scope,&__pyx_mstate_global->__pyx_n_u_context,&__pyx_mstate_global->__pyx_n_u_source_encoding,&__pyx_mstate_global->__pyx_n_u_parse_comments,&__pyx_mstate_global->__pyx_n_u_initial_pos,0};
  PyObject* values[9] = {0,0,0,0,0,0,0,0,0};
    const Py_ssize_t __pyx_kwds_len = (__pyx_kwds) ? __Pyx_NumKwargs_FASTCALL(__pyx_kwds) : 0;
    if (unlikely(__pyx_kwds_len) < 0) __PYX_ERR(0, 300, __pyx_L3_error)
    if (__pyx_kwds_len > 0) {
      switch (__pyx_nargs) {
        case  9:
        values[8] = __Pyx_ArgRef_FASTCALL(__pyx_args, 8);
        if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[8])) __PYX_ERR(0, 300, __pyx_L3_error)
        CYTHON_FALLTHROUGH;
        case  8:
        values[7] = __Pyx_ArgRef_FASTCALL(__pyx_args, 7);
        if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[7])) __PYX_ERR(0, 300, __pyx_L3_error)
        CYTHON_FALLTHROUGH;
        case  7:
        values[6] = __Pyx_ArgRef_FASTCALL(__pyx_args, 6);
        if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[6])) __PYX_ERR(0, 300, __pyx_L3_error)
        CYTHON_FALLTHROUGH;
        case  6:
        values[5] = __Pyx_ArgRef_FASTCALL(__pyx_args, 5);
        if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[5])) __PYX_ERR(0, 300, __pyx_L3_error)
        CYTHON_FALLTHROUGH;
        case  5:
        values[4] = __Pyx_ArgRef_FASTCALL(__pyx_args, 4);
        if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[4])) __PYX_ERR(0, 300, __pyx_L3_error)
        CYTHON_FALLTHROUGH;
        case  4:
        values[3] = __Pyx_ArgRef_FASTCALL(__pyx_args, 3);
        if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[3])) __PYX_ERR(0, 300, __pyx_L3_error)
        CYTHON_FALLTHROUGH;
        case  3:
        values[2] = __Pyx_ArgRef_FASTCALL(__pyx_args, 2);
        if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[2])) __PYX_ERR(0, 300, __pyx_L3_error)
        CYTHON_FALLTHROUGH;
        case  2:
        values[1] = __Pyx_ArgRef_FASTCALL(__pyx_args, 1);
        if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[1])) __PYX_ERR(0, 300, __pyx_L3_error)
        CYTHON_FALLTHROUGH;
        case  1:
        values[0] = __Pyx_ArgRef_FASTCALL(__pyx_args, 0);
        if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[0])) __PYX_ERR(0, 300, __pyx_L3_error)
        CYTHON_FALLTHROUGH;
        case  0: break;
        default: goto __pyx_L5_argtuple_error;
      }
      const Py_ssize_t kwd_pos_args = __pyx_nargs;
      if (__Pyx_ParseKeywords(__pyx_kwds, __pyx_kwvalues, __pyx_pyargnames, 0, values, kwd_pos_args, __pyx_kwds_len, "__init__", 0) < (0)) __PYX_ERR(0, 300, __pyx_L3_error)
      if (!values[3]) values[3] = __Pyx_NewRef(((PyObject *)Py_None));
/* … */
      if (!values[3]) values[3] = __Pyx_NewRef(((PyObject *)Py_None));
/* … */
  /* function exit code */
  goto __pyx_L0;
  __pyx_L1_error:;
  __pyx_r = NULL;
  for (Py_ssize_t __pyx_temp=0; __pyx_temp < (Py_ssize_t)(sizeof(values)/sizeof(values[0])); ++__pyx_temp) {
    Py_XDECREF(values[__pyx_temp]);
  }
  goto __pyx_L7_cleaned_up;
  __pyx_L0:;
  for (Py_ssize_t __pyx_temp=0; __pyx_temp < (Py_ssize_t)(sizeof(values)/sizeof(values[0])); ++__pyx_temp) {
    Py_XDECREF(values[__pyx_temp]);
  }
  __pyx_L7_cleaned_up:;
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}

static PyObject *__pyx_pf_6Cython_8Compiler_8Scanning_12PyrexScanner___init__(CYTHON_UNUSED PyObject *__pyx_self, PyObject *__pyx_v_self, PyObject *__pyx_v_file, PyObject *__pyx_v_filename, PyObject *__pyx_v_parent_scanner, PyObject *__pyx_v_scope, PyObject *__pyx_v_context, PyObject *__pyx_v_source_encoding, int __pyx_v_parse_comments, PyObject *__pyx_v_initial_pos) {
  PyObject *__pyx_v_keywords = NULL;
  PyObject *__pyx_8genexpr3__pyx_v_keyword = NULL;
  PyObject *__pyx_r = NULL;
/* … */
  /* function exit code */
  __pyx_r = Py_None; __Pyx_INCREF(Py_None);
  goto __pyx_L0;
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_t_1);
  __Pyx_XDECREF(__pyx_t_2);
  __Pyx_XDECREF(__pyx_t_3);
  __Pyx_XDECREF(__pyx_t_4);
  __Pyx_XDECREF(__pyx_t_5);
  __Pyx_XDECREF(__pyx_t_6);
  __Pyx_AddTraceback("Cython.Compiler.Scanning.PyrexScanner.__init__", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_r = NULL;
  __pyx_L0:;
  __Pyx_XDECREF(__pyx_v_keywords);
  __Pyx_XDECREF(__pyx_8genexpr3__pyx_v_keyword);
  __Pyx_XGIVEREF(__pyx_r);
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}
/* … */
  __pyx_t_2 = PyTuple_Pack(6, Py_None, Py_None, Py_None, Py_None, __pyx_t_7, Py_None); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 300, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_DECREF(__pyx_t_7); __pyx_t_7 = 0;
  __pyx_t_7 = __Pyx_PyDict_NewPresized(8); if (unlikely(!__pyx_t_7)) __PYX_ERR(0, 300, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_7);
  #if defined(PyDict_SetItem) && (defined(CYTHON_COMPILING_IN_CPYTHON))
  #if PY_VERSION_HEX >= 0x030A0000 /* CPython 3.10+ exposes KnownHash APIs */
  /* Use CPython's KnownHash APIs when available */
  extern int _PyDict_SetItem_KnownHash(PyObject*, PyObject*, PyObject*, Py_hash_t);
  {
    Py_hash_t __pyx_hash = PyObject_Hash(__pyx_mstate_global->__pyx_n_u_file); if (unlikely(__pyx_hash == -1)) __PYX_ERR(0, 300, __pyx_L1_error);
    if (unlikely(_PyDict_SetItem_KnownHash(__pyx_t_7, __pyx_mstate_global->__pyx_n_u_file, __pyx_mstate_global->__pyx_n_u_IO, __pyx_hash) < 0)) __PYX_ERR(0, 300, __pyx_L1_error);
  }
  #else
  if (PyDict_SetItem(__pyx_t_7, __pyx_mstate_global->__pyx_n_u_file, __pyx_mstate_global->__pyx_n_u_IO) < (0)) __PYX_ERR(0, 300, __pyx_L1_error)
  #endif
  #else
  if (PyDict_SetItem(__pyx_t_7, __pyx_mstate_global->__pyx_n_u_file, __pyx_mstate_global->__pyx_n_u_IO) < (0)) __PYX_ERR(0, 300, __pyx_L1_error)
  #endif
  #if defined(PyDict_SetItem) && (defined(CYTHON_COMPILING_IN_CPYTHON))
  #if PY_VERSION_HEX >= 0x030A0000 /* CPython 3.10+ exposes KnownHash APIs */
  /* Use CPython's KnownHash APIs when available */
  extern int _PyDict_SetItem_KnownHash(PyObject*, PyObject*, PyObject*, Py_hash_t);
  {
    Py_hash_t __pyx_hash = PyObject_Hash(__pyx_mstate_global->__pyx_n_u_filename); if (unlikely(__pyx_hash == -1)) __PYX_ERR(0, 300, __pyx_L1_error);
    if (unlikely(_PyDict_SetItem_KnownHash(__pyx_t_7, __pyx_mstate_global->__pyx_n_u_filename, __pyx_mstate_global->__pyx_n_u_SourceDescriptor, __pyx_hash) < 0)) __PYX_ERR(0, 300, __pyx_L1_error);
  }
  #else
  if (PyDict_SetItem(__pyx_t_7, __pyx_mstate_global->__pyx_n_u_filename, __pyx_mstate_global->__pyx_n_u_SourceDescriptor) < (0)) __PYX_ERR(0, 300, __pyx_L1_error)
  #endif
  #else
  if (PyDict_SetItem(__pyx_t_7, __pyx_mstate_global->__pyx_n_u_filename, __pyx_mstate_global->__pyx_n_u_SourceDescriptor) < (0)) __PYX_ERR(0, 300, __pyx_L1_error)
  #endif
  #if defined(PyDict_SetItem) && (defined(CYTHON_COMPILING_IN_CPYTHON))
  #if PY_VERSION_HEX >= 0x030A0000 /* CPython 3.10+ exposes KnownHash APIs */
  /* Use CPython's KnownHash APIs when available */
  extern int _PyDict_SetItem_KnownHash(PyObject*, PyObject*, PyObject*, Py_hash_t);
  {
    Py_hash_t __pyx_hash = PyObject_Hash(__pyx_mstate_global->__pyx_n_u_parent_scanner); if (unlikely(__pyx_hash == -1)) __PYX_ERR(0, 300, __pyx_L1_error);
    if (unlikely(_PyDict_SetItem_KnownHash(__pyx_t_7, __pyx_mstate_global->__pyx_n_u_parent_scanner, __pyx_mstate_global->__pyx_kp_u_PyrexScanner_None, __pyx_hash) < 0)) __PYX_ERR(0, 300, __pyx_L1_error);
  }
  #else
  if (PyDict_SetItem(__pyx_t_7, __pyx_mstate_global->__pyx_n_u_parent_scanner, __pyx_mstate_global->__pyx_kp_u_PyrexScanner_None) < (0)) __PYX_ERR(0, 300, __pyx_L1_error)
  #endif
  #else
  if (PyDict_SetItem(__pyx_t_7, __pyx_mstate_global->__pyx_n_u_parent_scanner, __pyx_mstate_global->__pyx_kp_u_PyrexScanner_None) < (0)) __PYX_ERR(0, 300, __pyx_L1_error)
  #endif
  #if defined(PyDict_SetItem) && (defined(CYTHON_COMPILING_IN_CPYTHON))
  #if PY_VERSION_HEX >= 0x030A0000 /* CPython 3.10+ exposes KnownHash APIs */
  /* Use CPython's KnownHash APIs when available */
  extern int _PyDict_SetItem_KnownHash(PyObject*, PyObject*, PyObject*, Py_hash_t);
  {
    Py_hash_t __pyx_hash = PyObject_Hash(__pyx_mstate_global->__pyx_n_u_scope); if (unlikely(__pyx_hash == -1)) __PYX_ERR(0, 300, __pyx_L1_error);
    if (unlikely(_PyDict_SetItem_KnownHash(__pyx_t_7, __pyx_mstate_global->__pyx_n_u_scope, __pyx_mstate_global->__pyx_kp_u_Scope_None, __pyx_hash) < 0)) __PYX_ERR(0, 300, __pyx_L1_error);
  }
  #else
  if (PyDict_SetItem(__pyx_t_7, __pyx_mstate_global->__pyx_n_u_scope, __pyx_mstate_global->__pyx_kp_u_Scope_None) < (0)) __PYX_ERR(0, 300, __pyx_L1_error)
  #endif
  #else
  if (PyDict_SetItem(__pyx_t_7, __pyx_mstate_global->__pyx_n_u_scope, __pyx_mstate_global->__pyx_kp_u_Scope_None) < (0)) __PYX_ERR(0, 300, __pyx_L1_error)
  #endif
  #if defined(PyDict_SetItem) && (defined(CYTHON_COMPILING_IN_CPYTHON))
  #if PY_VERSION_HEX >= 0x030A0000 /* CPython 3.10+ exposes KnownHash APIs */
  /* Use CPython's KnownHash APIs when available */
  extern int _PyDict_SetItem_KnownHash(PyObject*, PyObject*, PyObject*, Py_hash_t);
  {
    Py_hash_t __pyx_hash = PyObject_Hash(__pyx_mstate_global->__pyx_n_u_context); if (unlikely(__pyx_hash == -1)) __PYX_ERR(0, 300, __pyx_L1_error);
    if (unlikely(_PyDict_SetItem_KnownHash(__pyx_t_7, __pyx_mstate_global->__pyx_n_u_context, __pyx_mstate_global->__pyx_kp_u_CompilationContext_None, __pyx_hash) < 0)) __PYX_ERR(0, 300, __pyx_L1_error);
  }
  #else
  if (PyDict_SetItem(__pyx_t_7, __pyx_mstate_global->__pyx_n_u_context, __pyx_mstate_global->__pyx_kp_u_CompilationContext_None) < (0)) __PYX_ERR(0, 300, __pyx_L1_error)
  #endif
  #else
  if (PyDict_SetItem(__pyx_t_7, __pyx_mstate_global->__pyx_n_u_context, __pyx_mstate_global->__pyx_kp_u_CompilationContext_None) < (0)) __PYX_ERR(0, 300, __pyx_L1_error)
  #endif
  #if defined(PyDict_SetItem) && (defined(CYTHON_COMPILING_IN_CPYTHON))
  #if PY_VERSION_HEX >= 0x030A0000 /* CPython 3.10+ exposes KnownHash APIs */
  /* Use CPython's KnownHash APIs when available */
  extern int _PyDict_SetItem_KnownHash(PyObject*, PyObject*, PyObject*, Py_hash_t);
  {
    Py_hash_t __pyx_hash = PyObject_Hash(__pyx_mstate_global->__pyx_n_u_source_encoding); if (unlikely(__pyx_hash == -1)) __PYX_ERR(0, 300, __pyx_L1_error);
    if (unlikely(_PyDict_SetItem_KnownHash(__pyx_t_7, __pyx_mstate_global->__pyx_n_u_source_encoding, __pyx_mstate_global->__pyx_kp_u_str_None, __pyx_hash) < 0)) __PYX_ERR(0, 300, __pyx_L1_error);
  }
  #else
  if (PyDict_SetItem(__pyx_t_7, __pyx_mstate_global->__pyx_n_u_source_encoding, __pyx_mstate_global->__pyx_kp_u_str_None) < (0)) __PYX_ERR(0, 300, __pyx_L1_error)
  #endif
  #else
  if (PyDict_SetItem(__pyx_t_7, __pyx_mstate_global->__pyx_n_u_source_encoding, __pyx_mstate_global->__pyx_kp_u_str_None) < (0)) __PYX_ERR(0, 300, __pyx_L1_error)
  #endif
  #if defined(PyDict_SetItem) && (defined(CYTHON_COMPILING_IN_CPYTHON))
  #if PY_VERSION_HEX >= 0x030A0000 /* CPython 3.10+ exposes KnownHash APIs */
  /* Use CPython's KnownHash APIs when available */
  extern int _PyDict_SetItem_KnownHash(PyObject*, PyObject*, PyObject*, Py_hash_t);
  {
    Py_hash_t __pyx_hash = PyObject_Hash(__pyx_mstate_global->__pyx_n_u_parse_comments); if (unlikely(__pyx_hash == -1)) __PYX_ERR(0, 300, __pyx_L1_error);
    if (unlikely(_PyDict_SetItem_KnownHash(__pyx_t_7, __pyx_mstate_global->__pyx_n_u_parse_comments, __pyx_mstate_global->__pyx_n_u_bool, __pyx_hash) < 0)) __PYX_ERR(0, 300, __pyx_L1_error);
  }
  #else
  if (PyDict_SetItem(__pyx_t_7, __pyx_mstate_global->__pyx_n_u_parse_comments, __pyx_mstate_global->__pyx_n_u_bool) < (0)) __PYX_ERR(0, 300, __pyx_L1_error)
  #endif
  #else
  if (PyDict_SetItem(__pyx_t_7, __pyx_mstate_global->__pyx_n_u_parse_comments, __pyx_mstate_global->__pyx_n_u_bool) < (0)) __PYX_ERR(0, 300, __pyx_L1_error)
  #endif
  #if defined(PyDict_SetItem) && (defined(CYTHON_COMPILING_IN_CPYTHON))
  #if PY_VERSION_HEX >= 0x030A0000 /* CPython 3.10+ exposes KnownHash APIs */
  /* Use CPython's KnownHash APIs when available */
  extern int _PyDict_SetItem_KnownHash(PyObject*, PyObject*, PyObject*, Py_hash_t);
  {
    Py_hash_t __pyx_hash = PyObject_Hash(__pyx_mstate_global->__pyx_n_u_initial_pos); if (unlikely(__pyx_hash == -1)) __PYX_ERR(0, 300, __pyx_L1_error);
    if (unlikely(_PyDict_SetItem_KnownHash(__pyx_t_7, __pyx_mstate_global->__pyx_n_u_initial_pos, __pyx_mstate_global->__pyx_kp_u_tuple_int_int_int, __pyx_hash) < 0)) __PYX_ERR(0, 300, __pyx_L1_error);
  }
  #else
  if (PyDict_SetItem(__pyx_t_7, __pyx_mstate_global->__pyx_n_u_initial_pos, __pyx_mstate_global->__pyx_kp_u_tuple_int_int_int) < (0)) __PYX_ERR(0, 300, __pyx_L1_error)
  #endif
  #else
  if (PyDict_SetItem(__pyx_t_7, __pyx_mstate_global->__pyx_n_u_initial_pos, __pyx_mstate_global->__pyx_kp_u_tuple_int_int_int) < (0)) __PYX_ERR(0, 300, __pyx_L1_error)
  #endif
  __pyx_t_9 = __Pyx_CyFunction_New(&__pyx_mdef_6Cython_8Compiler_8Scanning_12PyrexScanner_1__init__, 0, __pyx_mstate_global->__pyx_n_u_PyrexScanner___init, NULL, __pyx_mstate_global->__pyx_n_u_Cython_Compiler_Scanning, __pyx_mstate_global->__pyx_d, ((PyObject *)__pyx_mstate_global->__pyx_codeobj_tab[35])); if (unlikely(!__pyx_t_9)) __PYX_ERR(0, 300, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_9);
  #if CYTHON_COMPILING_IN_CPYTHON && PY_VERSION_HEX >= 0x030E0000
  PyUnstable_Object_EnableDeferredRefcount(__pyx_t_9);
  #endif
  __Pyx_CyFunction_SetDefaultsTuple(__pyx_t_9, __pyx_t_2);
  __Pyx_CyFunction_SetAnnotationsDict(__pyx_t_9, __pyx_t_7);
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __Pyx_DECREF(__pyx_t_7); __pyx_t_7 = 0;
  if (__Pyx_SetNameInClass(__pyx_t_8, __pyx_mstate_global->__pyx_n_u_init, __pyx_t_9) < (0)) __PYX_ERR(0, 300, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_9); __pyx_t_9 = 0;
```

</details>

L301  🔴  (score=48)
```python
                 scope:Scope|None=None, context:CompilationContext|None=None, source_encoding:str|None=None, parse_comments:bool=True, initial_pos:tuple[int, int, int]=None):
```
<details><summary>Show generated C (score=48)</summary>

```c
      if (!values[4]) values[4] = __Pyx_NewRef(((PyObject *)Py_None));
      if (!values[5]) values[5] = __Pyx_NewRef(((PyObject *)Py_None));
      if (!values[6]) values[6] = __Pyx_NewRef(((PyObject*)Py_None));
      if (!values[8]) values[8] = __Pyx_NewRef(((PyObject*)Py_None));
      for (Py_ssize_t i = __pyx_nargs; i < 3; i++) {
        if (unlikely(!values[i])) { __Pyx_RaiseArgtupleInvalid("__init__", 0, 3, 9, i); __PYX_ERR(0, 300, __pyx_L3_error) }
      }
    } else {
      switch (__pyx_nargs) {
        case  9:
        values[8] = __Pyx_ArgRef_FASTCALL(__pyx_args, 8);
        if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[8])) __PYX_ERR(0, 300, __pyx_L3_error)
        CYTHON_FALLTHROUGH;
        case  8:
        values[7] = __Pyx_ArgRef_FASTCALL(__pyx_args, 7);
        if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[7])) __PYX_ERR(0, 300, __pyx_L3_error)
        CYTHON_FALLTHROUGH;
        case  7:
        values[6] = __Pyx_ArgRef_FASTCALL(__pyx_args, 6);
        if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[6])) __PYX_ERR(0, 300, __pyx_L3_error)
        CYTHON_FALLTHROUGH;
        case  6:
        values[5] = __Pyx_ArgRef_FASTCALL(__pyx_args, 5);
        if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[5])) __PYX_ERR(0, 300, __pyx_L3_error)
        CYTHON_FALLTHROUGH;
        case  5:
        values[4] = __Pyx_ArgRef_FASTCALL(__pyx_args, 4);
        if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[4])) __PYX_ERR(0, 300, __pyx_L3_error)
        CYTHON_FALLTHROUGH;
        case  4:
        values[3] = __Pyx_ArgRef_FASTCALL(__pyx_args, 3);
        if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[3])) __PYX_ERR(0, 300, __pyx_L3_error)
        CYTHON_FALLTHROUGH;
        case  3:
        values[2] = __Pyx_ArgRef_FASTCALL(__pyx_args, 2);
        if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[2])) __PYX_ERR(0, 300, __pyx_L3_error)
        values[1] = __Pyx_ArgRef_FASTCALL(__pyx_args, 1);
        if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[1])) __PYX_ERR(0, 300, __pyx_L3_error)
        values[0] = __Pyx_ArgRef_FASTCALL(__pyx_args, 0);
        if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[0])) __PYX_ERR(0, 300, __pyx_L3_error)
        break;
        default: goto __pyx_L5_argtuple_error;
      }
/* … */
      if (!values[4]) values[4] = __Pyx_NewRef(((PyObject *)Py_None));
      if (!values[5]) values[5] = __Pyx_NewRef(((PyObject *)Py_None));
      if (!values[6]) values[6] = __Pyx_NewRef(((PyObject*)Py_None));
      if (!values[8]) values[8] = __Pyx_NewRef(((PyObject*)Py_None));
    }
    __pyx_v_self = values[0];
    __pyx_v_file = values[1];
    __pyx_v_filename = values[2];
    __pyx_v_parent_scanner = values[3];
    __pyx_v_scope = values[4];
    __pyx_v_context = values[5];
    __pyx_v_source_encoding = ((PyObject*)values[6]);
    if (values[7]) {
      __pyx_v_parse_comments = __Pyx_PyObject_IsTrue(values[7]); if (unlikely((__pyx_v_parse_comments == (int)-1) && PyErr_Occurred())) __PYX_ERR(0, 301, __pyx_L3_error)
    } else {
      __pyx_v_parse_comments = ((int)((int)1));
    }
    __pyx_v_initial_pos = ((PyObject*)values[8]);
  }
  goto __pyx_L6_skip;
  __pyx_L5_argtuple_error:;
  __Pyx_RaiseArgtupleInvalid("__init__", 0, 3, 9, __pyx_nargs); __PYX_ERR(0, 300, __pyx_L3_error)
  __pyx_L6_skip:;
  goto __pyx_L4_argument_unpacking_done;
  __pyx_L3_error:;
  for (Py_ssize_t __pyx_temp=0; __pyx_temp < (Py_ssize_t)(sizeof(values)/sizeof(values[0])); ++__pyx_temp) {
    Py_XDECREF(values[__pyx_temp]);
  }
  __Pyx_AddTraceback("Cython.Compiler.Scanning.PyrexScanner.__init__", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __Pyx_RefNannyFinishContext();
  return NULL;
  __pyx_L4_argument_unpacking_done:;
  if (unlikely(!__Pyx_ArgTypeTest(((PyObject *)__pyx_v_source_encoding), (&PyUnicode_Type), 1, "source_encoding", 2))) __PYX_ERR(0, 301, __pyx_L1_error)
  if (unlikely(!__Pyx_ArgTypeTest(((PyObject *)__pyx_v_initial_pos), (&PyTuple_Type), 1, "initial_pos", 2))) __PYX_ERR(0, 301, __pyx_L1_error)
  __pyx_r = __pyx_pf_6Cython_8Compiler_8Scanning_12PyrexScanner___init__(__pyx_self, __pyx_v_self, __pyx_v_file, __pyx_v_filename, __pyx_v_parent_scanner, __pyx_v_scope, __pyx_v_context, __pyx_v_source_encoding, __pyx_v_parse_comments, __pyx_v_initial_pos);
/* … */
  __pyx_t_7 = __Pyx_PyBool_FromLong(((int)1)); if (unlikely(!__pyx_t_7)) __PYX_ERR(0, 301, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_7);
```

</details>

L302  🔴  (score=17)
```python
        Scanner.__init__(self, get_lexicon(), file, filename, initial_pos)
```
<details><summary>Show generated C (score=17)</summary>

```c
  __pyx_t_2 = NULL;
  __Pyx_GetModuleGlobalName(__pyx_t_3, __pyx_mstate_global->__pyx_n_u_Scanner); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 302, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_3);
  __pyx_t_4 = __Pyx_PyObject_GetAttrStr(__pyx_t_3, __pyx_mstate_global->__pyx_n_u_init); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 302, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_4);
  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
  __pyx_t_5 = NULL;
  __Pyx_GetModuleGlobalName(__pyx_t_6, __pyx_mstate_global->__pyx_n_u_get_lexicon); if (unlikely(!__pyx_t_6)) __PYX_ERR(0, 302, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_6);
  __pyx_t_7 = 1;
  {
    PyObject *__pyx_callargs[2] = {__pyx_t_5, NULL};
    __pyx_t_3 = __Pyx_PyObject_FastCall((PyObject*)__pyx_t_6, __pyx_callargs+__pyx_t_7, (1-__pyx_t_7) | (__pyx_t_7*__Pyx_PY_VECTORCALL_ARGUMENTS_OFFSET));
    __Pyx_XDECREF(__pyx_t_5); __pyx_t_5 = 0;
    __Pyx_DECREF(__pyx_t_6); __pyx_t_6 = 0;
    if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 302, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_3);
  }
  __pyx_t_7 = 1;
  {
    PyObject *__pyx_callargs[6] = {__pyx_t_2, __pyx_v_self, __pyx_t_3, __pyx_v_file, __pyx_v_filename, __pyx_v_initial_pos};
    __pyx_t_1 = __Pyx_PyObject_FastCall((PyObject*)__pyx_t_4, __pyx_callargs+__pyx_t_7, (6-__pyx_t_7) | (__pyx_t_7*__Pyx_PY_VECTORCALL_ARGUMENTS_OFFSET));
    __Pyx_XDECREF(__pyx_t_2); __pyx_t_2 = 0;
    __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
    __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
    if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 302, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_1);
  }
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
```

</details>

L303  ⚪  (score=0)
```python
```
L304  🟠  (score=7)
```python
        if filename.is_python_file():
```
<details><summary>Show generated C (score=7)</summary>

```c
  __pyx_t_4 = __pyx_v_filename;
  __Pyx_INCREF(__pyx_t_4);
  __pyx_t_7 = 0;
  {
    PyObject *__pyx_callargs[2] = {__pyx_t_4, NULL};
    __pyx_t_1 = __Pyx_PyObject_FastCallMethod((PyObject*)__pyx_mstate_global->__pyx_n_u_is_python_file, __pyx_callargs+__pyx_t_7, (1-__pyx_t_7) | (1*__Pyx_PY_VECTORCALL_ARGUMENTS_OFFSET));
    __Pyx_XDECREF(__pyx_t_4); __pyx_t_4 = 0;
    if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 304, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_1);
  }
  __pyx_t_8 = __Pyx_PyObject_IsTrue(__pyx_t_1); if (unlikely((__pyx_t_8 < 0))) __PYX_ERR(0, 304, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  if (__pyx_t_8) {
/* … */
    goto __pyx_L3;
  }
```

</details>

L305  🟡  (score=2)
```python
            self.in_python_file = True
```
<details><summary>Show generated C (score=2)</summary>

```c
    if (__Pyx_PyObject_SetAttrStr(__pyx_v_self, __pyx_mstate_global->__pyx_n_u_in_python_file, Py_True) < (0)) __PYX_ERR(0, 305, __pyx_L1_error)
```

</details>

L306  🟡  (score=2)
```python
            keywords = py_reserved_words
```
<details><summary>Show generated C (score=2)</summary>

```c
    __Pyx_GetModuleGlobalName(__pyx_t_1, __pyx_mstate_global->__pyx_n_u_py_reserved_words); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 306, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_1);
    __pyx_v_keywords = __pyx_t_1;
    __pyx_t_1 = 0;
```

</details>

L307  ⚪  (score=0)
```python
        else:
```
L308  🟡  (score=2)
```python
            self.in_python_file = False
```
<details><summary>Show generated C (score=2)</summary>

```c
  /*else*/ {
    if (__Pyx_PyObject_SetAttrStr(__pyx_v_self, __pyx_mstate_global->__pyx_n_u_in_python_file, Py_False) < (0)) __PYX_ERR(0, 308, __pyx_L1_error)
```

</details>

L309  🟡  (score=2)
```python
            keywords = pyx_reserved_words
```
<details><summary>Show generated C (score=2)</summary>

```c
    __Pyx_GetModuleGlobalName(__pyx_t_1, __pyx_mstate_global->__pyx_n_u_pyx_reserved_words); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 309, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_1);
    __pyx_v_keywords = __pyx_t_1;
    __pyx_t_1 = 0;
  }
  __pyx_L3:;
```

</details>

L310  🔴  (score=63)
```python
        self.keywords = {keyword: keyword for keyword in keywords}
```
<details><summary>Show generated C (score=63)</summary>

```c
  { /* enter inner scope */
    __pyx_t_1 = PyDict_New(); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 310, __pyx_L6_error)
    __Pyx_GOTREF(__pyx_t_1);
    if (likely(PyList_CheckExact(__pyx_v_keywords)) || PyTuple_CheckExact(__pyx_v_keywords)) {
      __pyx_t_4 = __pyx_v_keywords; __Pyx_INCREF(__pyx_t_4);
      __pyx_t_9 = 0;
      __pyx_t_10 = NULL;
    } else {
      __pyx_t_9 = -1; __pyx_t_4 = PyObject_GetIter(__pyx_v_keywords); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 310, __pyx_L6_error)
      __Pyx_GOTREF(__pyx_t_4);
      __pyx_t_10 = (CYTHON_COMPILING_IN_LIMITED_API) ? PyIter_Next : __Pyx_PyObject_GetIterNextFunc(__pyx_t_4); if (unlikely(!__pyx_t_10)) __PYX_ERR(0, 310, __pyx_L6_error)
    }
    for (;;) {
      if (likely(!__pyx_t_10)) {
        if (likely(PyList_CheckExact(__pyx_t_4))) {
          {
            Py_ssize_t __pyx_temp = __Pyx_PyList_GET_SIZE(__pyx_t_4);
            #if !CYTHON_ASSUME_SAFE_SIZE
            if (unlikely((__pyx_temp < 0))) __PYX_ERR(0, 310, __pyx_L6_error)
            #endif
            if (__pyx_t_9 >= __pyx_temp) break;
          }
          __pyx_t_3 = __Pyx_PyList_GetItemRefFast(__pyx_t_4, __pyx_t_9, __Pyx_ReferenceSharing_OwnStrongReference);
          ++__pyx_t_9;
        } else {
          {
            Py_ssize_t __pyx_temp = __Pyx_PyTuple_GET_SIZE(__pyx_t_4);
            #if !CYTHON_ASSUME_SAFE_SIZE
            if (unlikely((__pyx_temp < 0))) __PYX_ERR(0, 310, __pyx_L6_error)
            #endif
            if (__pyx_t_9 >= __pyx_temp) break;
          }
          #if CYTHON_ASSUME_SAFE_MACROS && !CYTHON_AVOID_BORROWED_REFS
          __pyx_t_3 = __Pyx_NewRef(PyTuple_GET_ITEM(__pyx_t_4, __pyx_t_9));
          #else
          __pyx_t_3 = __Pyx_PySequence_ITEM(__pyx_t_4, __pyx_t_9);
          #endif
          ++__pyx_t_9;
        }
        if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 310, __pyx_L6_error)
      } else {
        __pyx_t_3 = __pyx_t_10(__pyx_t_4);
        if (unlikely(!__pyx_t_3)) {
          PyObject* exc_type = PyErr_Occurred();
          if (exc_type) {
            if (unlikely(!__Pyx_PyErr_GivenExceptionMatches(exc_type, PyExc_StopIteration))) __PYX_ERR(0, 310, __pyx_L6_error)
            PyErr_Clear();
          }
          break;
        }
      }
      __Pyx_GOTREF(__pyx_t_3);
      __Pyx_XDECREF_SET(__pyx_8genexpr3__pyx_v_keyword, __pyx_t_3);
      __pyx_t_3 = 0;
      if (unlikely(PyDict_SetItem(__pyx_t_1, (PyObject*)__pyx_8genexpr3__pyx_v_keyword, (PyObject*)__pyx_8genexpr3__pyx_v_keyword))) __PYX_ERR(0, 310, __pyx_L6_error)
    }
    __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
    __Pyx_XDECREF(__pyx_8genexpr3__pyx_v_keyword); __pyx_8genexpr3__pyx_v_keyword = 0;
    goto __pyx_L10_exit_scope;
    __pyx_L6_error:;
    __Pyx_XDECREF(__pyx_8genexpr3__pyx_v_keyword); __pyx_8genexpr3__pyx_v_keyword = 0;
    goto __pyx_L1_error;
    __pyx_L10_exit_scope:;
  } /* exit inner scope */
  if (__Pyx_PyObject_SetAttrStr(__pyx_v_self, __pyx_mstate_global->__pyx_n_u_keywords, __pyx_t_1) < (0)) __PYX_ERR(0, 310, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
```

</details>

L311  ⚪  (score=0)
```python
```
L312  🟡  (score=2)
```python
        self.async_enabled = 0
```
<details><summary>Show generated C (score=2)</summary>

```c
  if (__Pyx_PyObject_SetAttrStr(__pyx_v_self, __pyx_mstate_global->__pyx_n_u_async_enabled, __pyx_mstate_global->__pyx_int_0) < (0)) __PYX_ERR(0, 312, __pyx_L1_error)
```

</details>

L313  ⚪  (score=0)
```python
```
L314  🟡  (score=2)
```python
        if parent_scanner:
```
<details><summary>Show generated C (score=2)</summary>

```c
  __pyx_t_8 = __Pyx_PyObject_IsTrue(__pyx_v_parent_scanner); if (unlikely((__pyx_t_8 < 0))) __PYX_ERR(0, 314, __pyx_L1_error)
  if (__pyx_t_8) {
/* … */
    goto __pyx_L11;
  }
```

</details>

L315  🟠  (score=5)
```python
            self.context = parent_scanner.context
```
<details><summary>Show generated C (score=5)</summary>

```c
    __pyx_t_1 = __Pyx_PyObject_GetAttrStr(__pyx_v_parent_scanner, __pyx_mstate_global->__pyx_n_u_context); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 315, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_1);
    if (__Pyx_PyObject_SetAttrStr(__pyx_v_self, __pyx_mstate_global->__pyx_n_u_context, __pyx_t_1) < (0)) __PYX_ERR(0, 315, __pyx_L1_error)
    __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
```

</details>

L316  🟠  (score=5)
```python
            self.included_files = parent_scanner.included_files
```
<details><summary>Show generated C (score=5)</summary>

```c
    __pyx_t_1 = __Pyx_PyObject_GetAttrStr(__pyx_v_parent_scanner, __pyx_mstate_global->__pyx_n_u_included_files); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 316, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_1);
    if (__Pyx_PyObject_SetAttrStr(__pyx_v_self, __pyx_mstate_global->__pyx_n_u_included_files, __pyx_t_1) < (0)) __PYX_ERR(0, 316, __pyx_L1_error)
    __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
```

</details>

L317  🟠  (score=5)
```python
            self.compile_time_env = parent_scanner.compile_time_env
```
<details><summary>Show generated C (score=5)</summary>

```c
    __pyx_t_1 = __Pyx_PyObject_GetAttrStr(__pyx_v_parent_scanner, __pyx_mstate_global->__pyx_n_u_compile_time_env); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 317, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_1);
    if (__Pyx_PyObject_SetAttrStr(__pyx_v_self, __pyx_mstate_global->__pyx_n_u_compile_time_env, __pyx_t_1) < (0)) __PYX_ERR(0, 317, __pyx_L1_error)
    __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
```

</details>

L318  🟠  (score=5)
```python
            self.compile_time_eval = parent_scanner.compile_time_eval
```
<details><summary>Show generated C (score=5)</summary>

```c
    __pyx_t_1 = __Pyx_PyObject_GetAttrStr(__pyx_v_parent_scanner, __pyx_mstate_global->__pyx_n_u_compile_time_eval); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 318, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_1);
    if (__Pyx_PyObject_SetAttrStr(__pyx_v_self, __pyx_mstate_global->__pyx_n_u_compile_time_eval, __pyx_t_1) < (0)) __PYX_ERR(0, 318, __pyx_L1_error)
    __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
```

</details>

L319  🟠  (score=5)
```python
            self.compile_time_expr = parent_scanner.compile_time_expr
```
<details><summary>Show generated C (score=5)</summary>

```c
    __pyx_t_1 = __Pyx_PyObject_GetAttrStr(__pyx_v_parent_scanner, __pyx_mstate_global->__pyx_n_u_compile_time_expr); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 319, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_1);
    if (__Pyx_PyObject_SetAttrStr(__pyx_v_self, __pyx_mstate_global->__pyx_n_u_compile_time_expr, __pyx_t_1) < (0)) __PYX_ERR(0, 319, __pyx_L1_error)
    __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
```

</details>

L320  ⚪  (score=0)
```python
```
L321  🟠  (score=5)
```python
            if parent_scanner.async_enabled:
```
<details><summary>Show generated C (score=5)</summary>

```c
    __pyx_t_1 = __Pyx_PyObject_GetAttrStr(__pyx_v_parent_scanner, __pyx_mstate_global->__pyx_n_u_async_enabled); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 321, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_1);
    __pyx_t_8 = __Pyx_PyObject_IsTrue(__pyx_t_1); if (unlikely((__pyx_t_8 < 0))) __PYX_ERR(0, 321, __pyx_L1_error)
    __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
    if (__pyx_t_8) {
/* … */
    }
```

</details>

L322  🟠  (score=5)
```python
                self.enter_async()
```
<details><summary>Show generated C (score=5)</summary>

```c
      __pyx_t_4 = __pyx_v_self;
      __Pyx_INCREF(__pyx_t_4);
      __pyx_t_7 = 0;
      {
        PyObject *__pyx_callargs[2] = {__pyx_t_4, NULL};
        __pyx_t_1 = __Pyx_PyObject_FastCallMethod((PyObject*)__pyx_mstate_global->__pyx_n_u_enter_async, __pyx_callargs+__pyx_t_7, (1-__pyx_t_7) | (1*__Pyx_PY_VECTORCALL_ARGUMENTS_OFFSET));
        __Pyx_XDECREF(__pyx_t_4); __pyx_t_4 = 0;
        if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 322, __pyx_L1_error)
        __Pyx_GOTREF(__pyx_t_1);
      }
      __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
```

</details>

L323  ⚪  (score=0)
```python
        else:
```
L324  🟡  (score=2)
```python
            self.context = context
```
<details><summary>Show generated C (score=2)</summary>

```c
  /*else*/ {
    if (__Pyx_PyObject_SetAttrStr(__pyx_v_self, __pyx_mstate_global->__pyx_n_u_context, __pyx_v_context) < (0)) __PYX_ERR(0, 324, __pyx_L1_error)
```

</details>

L325  🟠  (score=5)
```python
            self.included_files = scope.included_files
```
<details><summary>Show generated C (score=5)</summary>

```c
    __pyx_t_1 = __Pyx_PyObject_GetAttrStr(__pyx_v_scope, __pyx_mstate_global->__pyx_n_u_included_files); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 325, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_1);
    if (__Pyx_PyObject_SetAttrStr(__pyx_v_self, __pyx_mstate_global->__pyx_n_u_included_files, __pyx_t_1) < (0)) __PYX_ERR(0, 325, __pyx_L1_error)
    __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
```

</details>

L326  🟠  (score=9)
```python
            self.compile_time_env = initial_compile_time_env()
```
<details><summary>Show generated C (score=9)</summary>

```c
    __pyx_t_4 = NULL;
    __Pyx_GetModuleGlobalName(__pyx_t_3, __pyx_mstate_global->__pyx_n_u_initial_compile_time_env); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 326, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_3);
    __pyx_t_7 = 1;
    {
      PyObject *__pyx_callargs[2] = {__pyx_t_4, NULL};
      __pyx_t_1 = __Pyx_PyObject_FastCall((PyObject*)__pyx_t_3, __pyx_callargs+__pyx_t_7, (1-__pyx_t_7) | (__pyx_t_7*__Pyx_PY_VECTORCALL_ARGUMENTS_OFFSET));
      __Pyx_XDECREF(__pyx_t_4); __pyx_t_4 = 0;
      __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
      if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 326, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_1);
    }
    if (__Pyx_PyObject_SetAttrStr(__pyx_v_self, __pyx_mstate_global->__pyx_n_u_compile_time_env, __pyx_t_1) < (0)) __PYX_ERR(0, 326, __pyx_L1_error)
    __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
```

</details>

L327  🟡  (score=2)
```python
            self.compile_time_eval = 1
```
<details><summary>Show generated C (score=2)</summary>

```c
    if (__Pyx_PyObject_SetAttrStr(__pyx_v_self, __pyx_mstate_global->__pyx_n_u_compile_time_eval, __pyx_mstate_global->__pyx_int_1) < (0)) __PYX_ERR(0, 327, __pyx_L1_error)
```

</details>

L328  🟡  (score=2)
```python
            self.compile_time_expr = 0
```
<details><summary>Show generated C (score=2)</summary>

```c
    if (__Pyx_PyObject_SetAttrStr(__pyx_v_self, __pyx_mstate_global->__pyx_n_u_compile_time_expr, __pyx_mstate_global->__pyx_int_0) < (0)) __PYX_ERR(0, 328, __pyx_L1_error)
```

</details>

L329  🟠  (score=6)
```python
            if getattr(context.options, 'compile_time_env', None):
```
<details><summary>Show generated C (score=6)</summary>

```c
    __pyx_t_1 = __Pyx_PyObject_GetAttrStr(__pyx_v_context, __pyx_mstate_global->__pyx_n_u_options); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 329, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_1);
    __pyx_t_3 = __Pyx_GetAttr3(__pyx_t_1, __pyx_mstate_global->__pyx_n_u_compile_time_env, Py_None); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 329, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_3);
    __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
    __pyx_t_8 = __Pyx_PyObject_IsTrue(__pyx_t_3); if (unlikely((__pyx_t_8 < 0))) __PYX_ERR(0, 329, __pyx_L1_error)
    __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
    if (__pyx_t_8) {
/* … */
    }
  }
  __pyx_L11:;
```

</details>

L330  🔴  (score=14)
```python
                self.compile_time_env.update(context.options.compile_time_env)
```
<details><summary>Show generated C (score=14)</summary>

```c
      __pyx_t_4 = __Pyx_PyObject_GetAttrStr(__pyx_v_self, __pyx_mstate_global->__pyx_n_u_compile_time_env); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 330, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_4);
      __pyx_t_1 = __pyx_t_4;
      __Pyx_INCREF(__pyx_t_1);
      __pyx_t_2 = __Pyx_PyObject_GetAttrStr(__pyx_v_context, __pyx_mstate_global->__pyx_n_u_options); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 330, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_2);
      __pyx_t_6 = __Pyx_PyObject_GetAttrStr(__pyx_t_2, __pyx_mstate_global->__pyx_n_u_compile_time_env); if (unlikely(!__pyx_t_6)) __PYX_ERR(0, 330, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_6);
      __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
      __pyx_t_7 = 0;
      {
        PyObject *__pyx_callargs[2] = {__pyx_t_1, __pyx_t_6};
        __pyx_t_3 = __Pyx_PyObject_FastCallMethod((PyObject*)__pyx_mstate_global->__pyx_n_u_update, __pyx_callargs+__pyx_t_7, (2-__pyx_t_7) | (1*__Pyx_PY_VECTORCALL_ARGUMENTS_OFFSET));
        __Pyx_XDECREF(__pyx_t_1); __pyx_t_1 = 0;
        __Pyx_DECREF(__pyx_t_6); __pyx_t_6 = 0;
        __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
        if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 330, __pyx_L1_error)
        __Pyx_GOTREF(__pyx_t_3);
      }
      __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
```

</details>

L331  🟠  (score=5)
```python
        self.parse_comments = parse_comments
```
<details><summary>Show generated C (score=5)</summary>

```c
  __pyx_t_3 = __Pyx_PyBool_FromLong(__pyx_v_parse_comments); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 331, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_3);
  if (__Pyx_PyObject_SetAttrStr(__pyx_v_self, __pyx_mstate_global->__pyx_n_u_parse_comments, __pyx_t_3) < (0)) __PYX_ERR(0, 331, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
```

</details>

L332  🟡  (score=2)
```python
        self.source_encoding = source_encoding
```
<details><summary>Show generated C (score=2)</summary>

```c
  if (__Pyx_PyObject_SetAttrStr(__pyx_v_self, __pyx_mstate_global->__pyx_n_u_source_encoding, __pyx_v_source_encoding) < (0)) __PYX_ERR(0, 332, __pyx_L1_error)
```

</details>

L333  🟠  (score=5)
```python
        self.trace = trace_scanner
```
<details><summary>Show generated C (score=5)</summary>

```c
  __Pyx_GetModuleGlobalName(__pyx_t_3, __pyx_mstate_global->__pyx_n_u_trace_scanner); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 333, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_3);
  if (__Pyx_PyObject_SetAttrStr(__pyx_v_self, __pyx_mstate_global->__pyx_n_u_trace, __pyx_t_3) < (0)) __PYX_ERR(0, 333, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
```

</details>

L334  🔴  (score=11)
```python
        self.indentation_stack = [0]
```
<details><summary>Show generated C (score=11)</summary>

```c
  __pyx_t_3 = PyList_New(1); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 334, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_3);
  __Pyx_INCREF(__pyx_mstate_global->__pyx_int_0);
  __Pyx_GIVEREF(__pyx_mstate_global->__pyx_int_0);
  if (__Pyx_PyList_SET_ITEM(__pyx_t_3, 0, __pyx_mstate_global->__pyx_int_0) != (0)) __PYX_ERR(0, 334, __pyx_L1_error);
  if (__Pyx_PyObject_SetAttrStr(__pyx_v_self, __pyx_mstate_global->__pyx_n_u_indentation_stack, __pyx_t_3) < (0)) __PYX_ERR(0, 334, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
```

</details>

L335  🟡  (score=2)
```python
        self.indentation_char = '\0'
```
<details><summary>Show generated C (score=2)</summary>

```c
  if (__Pyx_PyObject_SetAttrStr(__pyx_v_self, __pyx_mstate_global->__pyx_n_u_indentation_char, __pyx_mstate_global->__pyx_kp_u__5) < (0)) __PYX_ERR(0, 335, __pyx_L1_error)
```

</details>

L336  🟡  (score=2)
```python
        self.bracket_nesting_level = 0
```
<details><summary>Show generated C (score=2)</summary>

```c
  if (__Pyx_PyObject_SetAttrStr(__pyx_v_self, __pyx_mstate_global->__pyx_n_u_bracket_nesting_level, __pyx_mstate_global->__pyx_int_0) < (0)) __PYX_ERR(0, 336, __pyx_L1_error)
```

</details>

L337  ⚪  (score=0)
```python
        # fstrings/tstrings
```
L338  🟠  (score=8)
```python
        self.ft_string_state_stack = []
```
<details><summary>Show generated C (score=8)</summary>

```c
  __pyx_t_3 = PyList_New(0); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 338, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_3);
  if (__Pyx_PyObject_SetAttrStr(__pyx_v_self, __pyx_mstate_global->__pyx_n_u_ft_string_state_stack, __pyx_t_3) < (0)) __PYX_ERR(0, 338, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
```

</details>

L339  🟡  (score=2)
```python
        self.in_ft_string_expr_prescan = 0
```
<details><summary>Show generated C (score=2)</summary>

```c
  if (__Pyx_PyObject_SetAttrStr(__pyx_v_self, __pyx_mstate_global->__pyx_n_u_in_ft_string_expr_prescan, __pyx_mstate_global->__pyx_int_0) < (0)) __PYX_ERR(0, 339, __pyx_L1_error)
```

</details>

L340  ⚪  (score=0)
```python
```
L341  🟡  (score=2)
```python
        self.put_back_on_failure = None
```
<details><summary>Show generated C (score=2)</summary>

```c
  if (__Pyx_PyObject_SetAttrStr(__pyx_v_self, __pyx_mstate_global->__pyx_n_u_put_back_on_failure, Py_None) < (0)) __PYX_ERR(0, 341, __pyx_L1_error)
```

</details>

L342  ⚪  (score=0)
```python
```
L343  🟠  (score=5)
```python
        self.begin('INDENT')
```
<details><summary>Show generated C (score=5)</summary>

```c
  __pyx_t_4 = __pyx_v_self;
  __Pyx_INCREF(__pyx_t_4);
  __pyx_t_7 = 0;
  {
    PyObject *__pyx_callargs[2] = {__pyx_t_4, __pyx_mstate_global->__pyx_n_u_INDENT};
    __pyx_t_3 = __Pyx_PyObject_FastCallMethod((PyObject*)__pyx_mstate_global->__pyx_n_u_begin, __pyx_callargs+__pyx_t_7, (2-__pyx_t_7) | (1*__Pyx_PY_VECTORCALL_ARGUMENTS_OFFSET));
    __Pyx_XDECREF(__pyx_t_4); __pyx_t_4 = 0;
    if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 343, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_3);
  }
  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
```

</details>

L344  🟡  (score=2)
```python
        self.sy = ''
```
<details><summary>Show generated C (score=2)</summary>

```c
  if (__Pyx_PyObject_SetAttrStr(__pyx_v_self, __pyx_mstate_global->__pyx_n_u_sy, __pyx_mstate_global->__pyx_kp_u__6) < (0)) __PYX_ERR(0, 344, __pyx_L1_error)
```

</details>

L345  🟠  (score=5)
```python
        self.next()
```
<details><summary>Show generated C (score=5)</summary>

```c
  __pyx_t_4 = __pyx_v_self;
  __Pyx_INCREF(__pyx_t_4);
  __pyx_t_7 = 0;
  {
    PyObject *__pyx_callargs[2] = {__pyx_t_4, NULL};
    __pyx_t_3 = __Pyx_PyObject_FastCallMethod((PyObject*)__pyx_mstate_global->__pyx_n_u_next, __pyx_callargs+__pyx_t_7, (1-__pyx_t_7) | (1*__Pyx_PY_VECTORCALL_ARGUMENTS_OFFSET));
    __Pyx_XDECREF(__pyx_t_4); __pyx_t_4 = 0;
    if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 345, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_3);
  }
  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
```

</details>

L346  ⚪  (score=0)
```python
```
L347  🔴  (score=45)
```python
    def normalize_ident(self, text):
```
<details><summary>Show generated C (score=45)</summary>

```c
/* Python wrapper */
static PyObject *__pyx_pw_6Cython_8Compiler_8Scanning_12PyrexScanner_3normalize_ident(PyObject *__pyx_self, 
#if CYTHON_METH_FASTCALL
PyObject *const *__pyx_args, Py_ssize_t __pyx_nargs, PyObject *__pyx_kwds
#else
PyObject *__pyx_args, PyObject *__pyx_kwds
#endif
); /*proto*/
PyDoc_STRVAR(__pyx_doc_6Cython_8Compiler_8Scanning_12PyrexScanner_2normalize_ident, "File: Cython/Compiler/Scanning.py (starting at line 347)");
static PyMethodDef __pyx_mdef_6Cython_8Compiler_8Scanning_12PyrexScanner_3normalize_ident = {"normalize_ident", (PyCFunction)(void(*)(void))(__Pyx_PyCFunction_FastCallWithKeywords)__pyx_pw_6Cython_8Compiler_8Scanning_12PyrexScanner_3normalize_ident, __Pyx_METH_FASTCALL|METH_KEYWORDS, __pyx_doc_6Cython_8Compiler_8Scanning_12PyrexScanner_2normalize_ident};
static PyObject *__pyx_pw_6Cython_8Compiler_8Scanning_12PyrexScanner_3normalize_ident(PyObject *__pyx_self, 
#if CYTHON_METH_FASTCALL
PyObject *const *__pyx_args, Py_ssize_t __pyx_nargs, PyObject *__pyx_kwds
#else
PyObject *__pyx_args, PyObject *__pyx_kwds
#endif
) {
  PyObject *__pyx_v_self = 0;
  PyObject *__pyx_v_text = 0;
  #if !CYTHON_METH_FASTCALL
  CYTHON_UNUSED Py_ssize_t __pyx_nargs;
  #endif
  CYTHON_UNUSED PyObject *const *__pyx_kwvalues;
  PyObject *__pyx_r = 0;
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("normalize_ident (wrapper)", 0);
  #if !CYTHON_METH_FASTCALL
  #if CYTHON_ASSUME_SAFE_SIZE
  __pyx_nargs = PyTuple_GET_SIZE(__pyx_args);
  #else
  __pyx_nargs = PyTuple_Size(__pyx_args); if (unlikely(__pyx_nargs < 0)) return NULL;
  #endif
  #endif
  __pyx_kwvalues = __Pyx_KwValues_FASTCALL(__pyx_args, __pyx_nargs);
  {
    PyObject ** const __pyx_pyargnames[] = {&__pyx_mstate_global->__pyx_n_u_self,&__pyx_mstate_global->__pyx_n_u_text,0};
  PyObject* values[2] = {0,0};
    const Py_ssize_t __pyx_kwds_len = (__pyx_kwds) ? __Pyx_NumKwargs_FASTCALL(__pyx_kwds) : 0;
    if (unlikely(__pyx_kwds_len) < 0) __PYX_ERR(0, 347, __pyx_L3_error)
    if (__pyx_kwds_len > 0) {
      switch (__pyx_nargs) {
        case  2:
        values[1] = __Pyx_ArgRef_FASTCALL(__pyx_args, 1);
        if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[1])) __PYX_ERR(0, 347, __pyx_L3_error)
        CYTHON_FALLTHROUGH;
        case  1:
        values[0] = __Pyx_ArgRef_FASTCALL(__pyx_args, 0);
        if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[0])) __PYX_ERR(0, 347, __pyx_L3_error)
        CYTHON_FALLTHROUGH;
        case  0: break;
        default: goto __pyx_L5_argtuple_error;
      }
      const Py_ssize_t kwd_pos_args = __pyx_nargs;
      if (__Pyx_ParseKeywords(__pyx_kwds, __pyx_kwvalues, __pyx_pyargnames, 0, values, kwd_pos_args, __pyx_kwds_len, "normalize_ident", 0) < (0)) __PYX_ERR(0, 347, __pyx_L3_error)
      for (Py_ssize_t i = __pyx_nargs; i < 2; i++) {
        if (unlikely(!values[i])) { __Pyx_RaiseArgtupleInvalid("normalize_ident", 1, 2, 2, i); __PYX_ERR(0, 347, __pyx_L3_error) }
      }
    } else if (unlikely(__pyx_nargs != 2)) {
      goto __pyx_L5_argtuple_error;
    } else {
      values[0] = __Pyx_ArgRef_FASTCALL(__pyx_args, 0);
      if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[0])) __PYX_ERR(0, 347, __pyx_L3_error)
      values[1] = __Pyx_ArgRef_FASTCALL(__pyx_args, 1);
      if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[1])) __PYX_ERR(0, 347, __pyx_L3_error)
    }
    __pyx_v_self = values[0];
    __pyx_v_text = values[1];
  }
  goto __pyx_L6_skip;
  __pyx_L5_argtuple_error:;
  __Pyx_RaiseArgtupleInvalid("normalize_ident", 1, 2, 2, __pyx_nargs); __PYX_ERR(0, 347, __pyx_L3_error)
  __pyx_L6_skip:;
  goto __pyx_L4_argument_unpacking_done;
  __pyx_L3_error:;
  for (Py_ssize_t __pyx_temp=0; __pyx_temp < (Py_ssize_t)(sizeof(values)/sizeof(values[0])); ++__pyx_temp) {
    Py_XDECREF(values[__pyx_temp]);
  }
  __Pyx_AddTraceback("Cython.Compiler.Scanning.PyrexScanner.normalize_ident", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __Pyx_RefNannyFinishContext();
  return NULL;
  __pyx_L4_argument_unpacking_done:;
  __pyx_r = __pyx_pf_6Cython_8Compiler_8Scanning_12PyrexScanner_2normalize_ident(__pyx_self, __pyx_v_self, __pyx_v_text);
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

static PyObject *__pyx_pf_6Cython_8Compiler_8Scanning_12PyrexScanner_2normalize_ident(CYTHON_UNUSED PyObject *__pyx_self, PyObject *__pyx_v_self, PyObject *__pyx_v_text) {
  PyObject *__pyx_r = NULL;
  __Pyx_INCREF(__pyx_v_text);
/* … */
  /* function exit code */
  __pyx_r = Py_None; __Pyx_INCREF(Py_None);
  goto __pyx_L0;
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_t_1);
  __Pyx_XDECREF(__pyx_t_2);
  __Pyx_XDECREF(__pyx_t_6);
  __Pyx_AddTraceback("Cython.Compiler.Scanning.PyrexScanner.normalize_ident", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_r = NULL;
  __pyx_L0:;
  __Pyx_XDECREF(__pyx_v_text);
  __Pyx_XGIVEREF(__pyx_r);
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}
/* … */
  __pyx_t_9 = __Pyx_CyFunction_New(&__pyx_mdef_6Cython_8Compiler_8Scanning_12PyrexScanner_3normalize_ident, 0, __pyx_mstate_global->__pyx_n_u_PyrexScanner_normalize_ident, NULL, __pyx_mstate_global->__pyx_n_u_Cython_Compiler_Scanning, __pyx_mstate_global->__pyx_d, ((PyObject *)__pyx_mstate_global->__pyx_codeobj_tab[36])); if (unlikely(!__pyx_t_9)) __PYX_ERR(0, 347, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_9);
  #if CYTHON_COMPILING_IN_CPYTHON && PY_VERSION_HEX >= 0x030E0000
  PyUnstable_Object_EnableDeferredRefcount(__pyx_t_9);
  #endif
  if (__Pyx_SetNameInClass(__pyx_t_8, __pyx_mstate_global->__pyx_n_u_normalize_ident, __pyx_t_9) < (0)) __PYX_ERR(0, 347, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_9); __pyx_t_9 = 0;
```

</details>

L348  🟠  (score=7)
```python
        if not text.isascii():
```
<details><summary>Show generated C (score=7)</summary>

```c
  __pyx_t_2 = __pyx_v_text;
  __Pyx_INCREF(__pyx_t_2);
  __pyx_t_3 = 0;
  {
    PyObject *__pyx_callargs[2] = {__pyx_t_2, NULL};
    __pyx_t_1 = __Pyx_PyObject_FastCallMethod((PyObject*)__pyx_mstate_global->__pyx_n_u_isascii, __pyx_callargs+__pyx_t_3, (1-__pyx_t_3) | (1*__Pyx_PY_VECTORCALL_ARGUMENTS_OFFSET));
    __Pyx_XDECREF(__pyx_t_2); __pyx_t_2 = 0;
    if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 348, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_1);
  }
  __pyx_t_4 = __Pyx_PyObject_IsTrue(__pyx_t_1); if (unlikely((__pyx_t_4 < 0))) __PYX_ERR(0, 348, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __pyx_t_5 = (!__pyx_t_4);
  if (__pyx_t_5) {
/* … */
  }
```

</details>

L349  🟠  (score=7)
```python
            text = normalize('NFKC', text)
```
<details><summary>Show generated C (score=7)</summary>

```c
    __pyx_t_2 = NULL;
    __Pyx_GetModuleGlobalName(__pyx_t_6, __pyx_mstate_global->__pyx_n_u_normalize); if (unlikely(!__pyx_t_6)) __PYX_ERR(0, 349, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_6);
    __pyx_t_3 = 1;
    {
      PyObject *__pyx_callargs[3] = {__pyx_t_2, __pyx_mstate_global->__pyx_n_u_NFKC, __pyx_v_text};
      __pyx_t_1 = __Pyx_PyObject_FastCall((PyObject*)__pyx_t_6, __pyx_callargs+__pyx_t_3, (3-__pyx_t_3) | (__pyx_t_3*__Pyx_PY_VECTORCALL_ARGUMENTS_OFFSET));
      __Pyx_XDECREF(__pyx_t_2); __pyx_t_2 = 0;
      __Pyx_DECREF(__pyx_t_6); __pyx_t_6 = 0;
      if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 349, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_1);
    }
    __Pyx_DECREF_SET(__pyx_v_text, __pyx_t_1);
    __pyx_t_1 = 0;
```

</details>

L350  🟠  (score=8)
```python
        self.produce(IDENT, text)
```
<details><summary>Show generated C (score=8)</summary>

```c
  __pyx_t_6 = __pyx_v_self;
  __Pyx_INCREF(__pyx_t_6);
  __Pyx_GetModuleGlobalName(__pyx_t_2, __pyx_mstate_global->__pyx_n_u_IDENT); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 350, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __pyx_t_3 = 0;
  {
    PyObject *__pyx_callargs[3] = {__pyx_t_6, __pyx_t_2, __pyx_v_text};
    __pyx_t_1 = __Pyx_PyObject_FastCallMethod((PyObject*)__pyx_mstate_global->__pyx_n_u_produce, __pyx_callargs+__pyx_t_3, (3-__pyx_t_3) | (1*__Pyx_PY_VECTORCALL_ARGUMENTS_OFFSET));
    __Pyx_XDECREF(__pyx_t_6); __pyx_t_6 = 0;
    __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
    if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 350, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_1);
  }
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
```

</details>

L351  ⚪  (score=0)
```python
```
L352  🔴  (score=42)
```python
    def commentline(self, text):
```
<details><summary>Show generated C (score=42)</summary>

```c
/* Python wrapper */
static PyObject *__pyx_pw_6Cython_8Compiler_8Scanning_12PyrexScanner_5commentline(PyObject *__pyx_self, 
#if CYTHON_METH_FASTCALL
PyObject *const *__pyx_args, Py_ssize_t __pyx_nargs, PyObject *__pyx_kwds
#else
PyObject *__pyx_args, PyObject *__pyx_kwds
#endif
); /*proto*/
PyDoc_STRVAR(__pyx_doc_6Cython_8Compiler_8Scanning_12PyrexScanner_4commentline, "File: Cython/Compiler/Scanning.py (starting at line 352)");
static PyMethodDef __pyx_mdef_6Cython_8Compiler_8Scanning_12PyrexScanner_5commentline = {"commentline", (PyCFunction)(void(*)(void))(__Pyx_PyCFunction_FastCallWithKeywords)__pyx_pw_6Cython_8Compiler_8Scanning_12PyrexScanner_5commentline, __Pyx_METH_FASTCALL|METH_KEYWORDS, __pyx_doc_6Cython_8Compiler_8Scanning_12PyrexScanner_4commentline};
static PyObject *__pyx_pw_6Cython_8Compiler_8Scanning_12PyrexScanner_5commentline(PyObject *__pyx_self, 
#if CYTHON_METH_FASTCALL
PyObject *const *__pyx_args, Py_ssize_t __pyx_nargs, PyObject *__pyx_kwds
#else
PyObject *__pyx_args, PyObject *__pyx_kwds
#endif
) {
  PyObject *__pyx_v_self = 0;
  PyObject *__pyx_v_text = 0;
  #if !CYTHON_METH_FASTCALL
  CYTHON_UNUSED Py_ssize_t __pyx_nargs;
  #endif
  CYTHON_UNUSED PyObject *const *__pyx_kwvalues;
  PyObject *__pyx_r = 0;
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("commentline (wrapper)", 0);
  #if !CYTHON_METH_FASTCALL
  #if CYTHON_ASSUME_SAFE_SIZE
  __pyx_nargs = PyTuple_GET_SIZE(__pyx_args);
  #else
  __pyx_nargs = PyTuple_Size(__pyx_args); if (unlikely(__pyx_nargs < 0)) return NULL;
  #endif
  #endif
  __pyx_kwvalues = __Pyx_KwValues_FASTCALL(__pyx_args, __pyx_nargs);
  {
    PyObject ** const __pyx_pyargnames[] = {&__pyx_mstate_global->__pyx_n_u_self,&__pyx_mstate_global->__pyx_n_u_text,0};
  PyObject* values[2] = {0,0};
    const Py_ssize_t __pyx_kwds_len = (__pyx_kwds) ? __Pyx_NumKwargs_FASTCALL(__pyx_kwds) : 0;
    if (unlikely(__pyx_kwds_len) < 0) __PYX_ERR(0, 352, __pyx_L3_error)
    if (__pyx_kwds_len > 0) {
      switch (__pyx_nargs) {
        case  2:
        values[1] = __Pyx_ArgRef_FASTCALL(__pyx_args, 1);
        if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[1])) __PYX_ERR(0, 352, __pyx_L3_error)
        CYTHON_FALLTHROUGH;
        case  1:
        values[0] = __Pyx_ArgRef_FASTCALL(__pyx_args, 0);
        if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[0])) __PYX_ERR(0, 352, __pyx_L3_error)
        CYTHON_FALLTHROUGH;
        case  0: break;
        default: goto __pyx_L5_argtuple_error;
      }
      const Py_ssize_t kwd_pos_args = __pyx_nargs;
      if (__Pyx_ParseKeywords(__pyx_kwds, __pyx_kwvalues, __pyx_pyargnames, 0, values, kwd_pos_args, __pyx_kwds_len, "commentline", 0) < (0)) __PYX_ERR(0, 352, __pyx_L3_error)
      for (Py_ssize_t i = __pyx_nargs; i < 2; i++) {
        if (unlikely(!values[i])) { __Pyx_RaiseArgtupleInvalid("commentline", 1, 2, 2, i); __PYX_ERR(0, 352, __pyx_L3_error) }
      }
    } else if (unlikely(__pyx_nargs != 2)) {
      goto __pyx_L5_argtuple_error;
    } else {
      values[0] = __Pyx_ArgRef_FASTCALL(__pyx_args, 0);
      if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[0])) __PYX_ERR(0, 352, __pyx_L3_error)
      values[1] = __Pyx_ArgRef_FASTCALL(__pyx_args, 1);
      if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[1])) __PYX_ERR(0, 352, __pyx_L3_error)
    }
    __pyx_v_self = values[0];
    __pyx_v_text = values[1];
  }
  goto __pyx_L6_skip;
  __pyx_L5_argtuple_error:;
  __Pyx_RaiseArgtupleInvalid("commentline", 1, 2, 2, __pyx_nargs); __PYX_ERR(0, 352, __pyx_L3_error)
  __pyx_L6_skip:;
  goto __pyx_L4_argument_unpacking_done;
  __pyx_L3_error:;
  for (Py_ssize_t __pyx_temp=0; __pyx_temp < (Py_ssize_t)(sizeof(values)/sizeof(values[0])); ++__pyx_temp) {
    Py_XDECREF(values[__pyx_temp]);
  }
  __Pyx_AddTraceback("Cython.Compiler.Scanning.PyrexScanner.commentline", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __Pyx_RefNannyFinishContext();
  return NULL;
  __pyx_L4_argument_unpacking_done:;
  __pyx_r = __pyx_pf_6Cython_8Compiler_8Scanning_12PyrexScanner_4commentline(__pyx_self, __pyx_v_self, __pyx_v_text);
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

static PyObject *__pyx_pf_6Cython_8Compiler_8Scanning_12PyrexScanner_4commentline(CYTHON_UNUSED PyObject *__pyx_self, PyObject *__pyx_v_self, PyObject *__pyx_v_text) {
  PyObject *__pyx_r = NULL;
/* … */
  /* function exit code */
  __pyx_r = Py_None; __Pyx_INCREF(Py_None);
  goto __pyx_L0;
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_t_1);
  __Pyx_XDECREF(__pyx_t_3);
  __Pyx_AddTraceback("Cython.Compiler.Scanning.PyrexScanner.commentline", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_r = NULL;
  __pyx_L0:;
  __Pyx_XGIVEREF(__pyx_r);
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}
/* … */
  __pyx_t_9 = __Pyx_CyFunction_New(&__pyx_mdef_6Cython_8Compiler_8Scanning_12PyrexScanner_5commentline, 0, __pyx_mstate_global->__pyx_n_u_PyrexScanner_commentline, NULL, __pyx_mstate_global->__pyx_n_u_Cython_Compiler_Scanning, __pyx_mstate_global->__pyx_d, ((PyObject *)__pyx_mstate_global->__pyx_codeobj_tab[37])); if (unlikely(!__pyx_t_9)) __PYX_ERR(0, 352, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_9);
  #if CYTHON_COMPILING_IN_CPYTHON && PY_VERSION_HEX >= 0x030E0000
  PyUnstable_Object_EnableDeferredRefcount(__pyx_t_9);
  #endif
  if (__Pyx_SetNameInClass(__pyx_t_8, __pyx_mstate_global->__pyx_n_u_commentline, __pyx_t_9) < (0)) __PYX_ERR(0, 352, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_9); __pyx_t_9 = 0;
```

</details>

L353  🟠  (score=5)
```python
        if self.parse_comments:
```
<details><summary>Show generated C (score=5)</summary>

```c
  __pyx_t_1 = __Pyx_PyObject_GetAttrStr(__pyx_v_self, __pyx_mstate_global->__pyx_n_u_parse_comments); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 353, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __pyx_t_2 = __Pyx_PyObject_IsTrue(__pyx_t_1); if (unlikely((__pyx_t_2 < 0))) __PYX_ERR(0, 353, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  if (__pyx_t_2) {
/* … */
  }
```

</details>

L354  🟠  (score=5)
```python
            self.produce('commentline', text)
```
<details><summary>Show generated C (score=5)</summary>

```c
    __pyx_t_3 = __pyx_v_self;
    __Pyx_INCREF(__pyx_t_3);
    __pyx_t_4 = 0;
    {
      PyObject *__pyx_callargs[3] = {__pyx_t_3, __pyx_mstate_global->__pyx_n_u_commentline, __pyx_v_text};
      __pyx_t_1 = __Pyx_PyObject_FastCallMethod((PyObject*)__pyx_mstate_global->__pyx_n_u_produce, __pyx_callargs+__pyx_t_4, (3-__pyx_t_4) | (1*__Pyx_PY_VECTORCALL_ARGUMENTS_OFFSET));
      __Pyx_XDECREF(__pyx_t_3); __pyx_t_3 = 0;
      if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 354, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_1);
    }
    __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
```

</details>

L355  ⚪  (score=0)
```python
```
L356  🔴  (score=48)
```python
    def strip_underscores(self, text, symbol):
```
<details><summary>Show generated C (score=48)</summary>

```c
/* Python wrapper */
static PyObject *__pyx_pw_6Cython_8Compiler_8Scanning_12PyrexScanner_7strip_underscores(PyObject *__pyx_self, 
#if CYTHON_METH_FASTCALL
PyObject *const *__pyx_args, Py_ssize_t __pyx_nargs, PyObject *__pyx_kwds
#else
PyObject *__pyx_args, PyObject *__pyx_kwds
#endif
); /*proto*/
PyDoc_STRVAR(__pyx_doc_6Cython_8Compiler_8Scanning_12PyrexScanner_6strip_underscores, "File: Cython/Compiler/Scanning.py (starting at line 356)");
static PyMethodDef __pyx_mdef_6Cython_8Compiler_8Scanning_12PyrexScanner_7strip_underscores = {"strip_underscores", (PyCFunction)(void(*)(void))(__Pyx_PyCFunction_FastCallWithKeywords)__pyx_pw_6Cython_8Compiler_8Scanning_12PyrexScanner_7strip_underscores, __Pyx_METH_FASTCALL|METH_KEYWORDS, __pyx_doc_6Cython_8Compiler_8Scanning_12PyrexScanner_6strip_underscores};
static PyObject *__pyx_pw_6Cython_8Compiler_8Scanning_12PyrexScanner_7strip_underscores(PyObject *__pyx_self, 
#if CYTHON_METH_FASTCALL
PyObject *const *__pyx_args, Py_ssize_t __pyx_nargs, PyObject *__pyx_kwds
#else
PyObject *__pyx_args, PyObject *__pyx_kwds
#endif
) {
  PyObject *__pyx_v_self = 0;
  PyObject *__pyx_v_text = 0;
  PyObject *__pyx_v_symbol = 0;
  #if !CYTHON_METH_FASTCALL
  CYTHON_UNUSED Py_ssize_t __pyx_nargs;
  #endif
  CYTHON_UNUSED PyObject *const *__pyx_kwvalues;
  PyObject *__pyx_r = 0;
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("strip_underscores (wrapper)", 0);
  #if !CYTHON_METH_FASTCALL
  #if CYTHON_ASSUME_SAFE_SIZE
  __pyx_nargs = PyTuple_GET_SIZE(__pyx_args);
  #else
  __pyx_nargs = PyTuple_Size(__pyx_args); if (unlikely(__pyx_nargs < 0)) return NULL;
  #endif
  #endif
  __pyx_kwvalues = __Pyx_KwValues_FASTCALL(__pyx_args, __pyx_nargs);
  {
    PyObject ** const __pyx_pyargnames[] = {&__pyx_mstate_global->__pyx_n_u_self,&__pyx_mstate_global->__pyx_n_u_text,&__pyx_mstate_global->__pyx_n_u_symbol,0};
  PyObject* values[3] = {0,0,0};
    const Py_ssize_t __pyx_kwds_len = (__pyx_kwds) ? __Pyx_NumKwargs_FASTCALL(__pyx_kwds) : 0;
    if (unlikely(__pyx_kwds_len) < 0) __PYX_ERR(0, 356, __pyx_L3_error)
    if (__pyx_kwds_len > 0) {
      switch (__pyx_nargs) {
        case  3:
        values[2] = __Pyx_ArgRef_FASTCALL(__pyx_args, 2);
        if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[2])) __PYX_ERR(0, 356, __pyx_L3_error)
        CYTHON_FALLTHROUGH;
        case  2:
        values[1] = __Pyx_ArgRef_FASTCALL(__pyx_args, 1);
        if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[1])) __PYX_ERR(0, 356, __pyx_L3_error)
        CYTHON_FALLTHROUGH;
        case  1:
        values[0] = __Pyx_ArgRef_FASTCALL(__pyx_args, 0);
        if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[0])) __PYX_ERR(0, 356, __pyx_L3_error)
        CYTHON_FALLTHROUGH;
        case  0: break;
        default: goto __pyx_L5_argtuple_error;
      }
      const Py_ssize_t kwd_pos_args = __pyx_nargs;
      if (__Pyx_ParseKeywords(__pyx_kwds, __pyx_kwvalues, __pyx_pyargnames, 0, values, kwd_pos_args, __pyx_kwds_len, "strip_underscores", 0) < (0)) __PYX_ERR(0, 356, __pyx_L3_error)
      for (Py_ssize_t i = __pyx_nargs; i < 3; i++) {
        if (unlikely(!values[i])) { __Pyx_RaiseArgtupleInvalid("strip_underscores", 1, 3, 3, i); __PYX_ERR(0, 356, __pyx_L3_error) }
      }
    } else if (unlikely(__pyx_nargs != 3)) {
      goto __pyx_L5_argtuple_error;
    } else {
      values[0] = __Pyx_ArgRef_FASTCALL(__pyx_args, 0);
      if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[0])) __PYX_ERR(0, 356, __pyx_L3_error)
      values[1] = __Pyx_ArgRef_FASTCALL(__pyx_args, 1);
      if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[1])) __PYX_ERR(0, 356, __pyx_L3_error)
      values[2] = __Pyx_ArgRef_FASTCALL(__pyx_args, 2);
      if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[2])) __PYX_ERR(0, 356, __pyx_L3_error)
    }
    __pyx_v_self = values[0];
    __pyx_v_text = values[1];
    __pyx_v_symbol = values[2];
  }
  goto __pyx_L6_skip;
  __pyx_L5_argtuple_error:;
  __Pyx_RaiseArgtupleInvalid("strip_underscores", 1, 3, 3, __pyx_nargs); __PYX_ERR(0, 356, __pyx_L3_error)
  __pyx_L6_skip:;
  goto __pyx_L4_argument_unpacking_done;
  __pyx_L3_error:;
  for (Py_ssize_t __pyx_temp=0; __pyx_temp < (Py_ssize_t)(sizeof(values)/sizeof(values[0])); ++__pyx_temp) {
    Py_XDECREF(values[__pyx_temp]);
  }
  __Pyx_AddTraceback("Cython.Compiler.Scanning.PyrexScanner.strip_underscores", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __Pyx_RefNannyFinishContext();
  return NULL;
  __pyx_L4_argument_unpacking_done:;
  __pyx_r = __pyx_pf_6Cython_8Compiler_8Scanning_12PyrexScanner_6strip_underscores(__pyx_self, __pyx_v_self, __pyx_v_text, __pyx_v_symbol);
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

static PyObject *__pyx_pf_6Cython_8Compiler_8Scanning_12PyrexScanner_6strip_underscores(CYTHON_UNUSED PyObject *__pyx_self, PyObject *__pyx_v_self, PyObject *__pyx_v_text, PyObject *__pyx_v_symbol) {
  PyObject *__pyx_r = NULL;
/* … */
  /* function exit code */
  __pyx_r = Py_None; __Pyx_INCREF(Py_None);
  goto __pyx_L0;
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_t_1);
  __Pyx_XDECREF(__pyx_t_2);
  __Pyx_XDECREF(__pyx_t_3);
  __Pyx_XDECREF(__pyx_t_4);
  __Pyx_AddTraceback("Cython.Compiler.Scanning.PyrexScanner.strip_underscores", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_r = NULL;
  __pyx_L0:;
  __Pyx_XGIVEREF(__pyx_r);
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}
/* … */
  __pyx_t_9 = __Pyx_CyFunction_New(&__pyx_mdef_6Cython_8Compiler_8Scanning_12PyrexScanner_7strip_underscores, 0, __pyx_mstate_global->__pyx_n_u_PyrexScanner_strip_underscores, NULL, __pyx_mstate_global->__pyx_n_u_Cython_Compiler_Scanning, __pyx_mstate_global->__pyx_d, ((PyObject *)__pyx_mstate_global->__pyx_codeobj_tab[38])); if (unlikely(!__pyx_t_9)) __PYX_ERR(0, 356, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_9);
  #if CYTHON_COMPILING_IN_CPYTHON && PY_VERSION_HEX >= 0x030E0000
  PyUnstable_Object_EnableDeferredRefcount(__pyx_t_9);
  #endif
  if (__Pyx_SetNameInClass(__pyx_t_8, __pyx_mstate_global->__pyx_n_u_strip_underscores, __pyx_t_9) < (0)) __PYX_ERR(0, 356, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_9); __pyx_t_9 = 0;
```

</details>

L357  🔴  (score=16)
```python
        self.produce(symbol, text.replace('_', ''))
```
<details><summary>Show generated C (score=16)</summary>

```c
  __pyx_t_2 = __pyx_v_self;
  __Pyx_INCREF(__pyx_t_2);
  __pyx_t_3 = __Pyx_PyObject_GetAttrStr(__pyx_v_text, __pyx_mstate_global->__pyx_n_u_replace); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 357, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_3);
  __pyx_t_4 = __Pyx_PyObject_Call(__pyx_t_3, __pyx_mstate_global->__pyx_tuple[4], NULL); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 357, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_4);
  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
  __pyx_t_5 = 0;
  {
    PyObject *__pyx_callargs[3] = {__pyx_t_2, __pyx_v_symbol, __pyx_t_4};
    __pyx_t_1 = __Pyx_PyObject_FastCallMethod((PyObject*)__pyx_mstate_global->__pyx_n_u_produce, __pyx_callargs+__pyx_t_5, (3-__pyx_t_5) | (1*__Pyx_PY_VECTORCALL_ARGUMENTS_OFFSET));
    __Pyx_XDECREF(__pyx_t_2); __pyx_t_2 = 0;
    __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
    if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 357, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_1);
  }
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
/* … */
  __pyx_mstate_global->__pyx_tuple[4] = PyTuple_Pack(2, __pyx_mstate_global->__pyx_n_u__7, __pyx_mstate_global->__pyx_kp_u__6); if (unlikely(!__pyx_mstate_global->__pyx_tuple[4])) __PYX_ERR(0, 357, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_mstate_global->__pyx_tuple[4]);
  __Pyx_GIVEREF(__pyx_mstate_global->__pyx_tuple[4]);
```

</details>

L358  ⚪  (score=0)
```python
```
L359  🔴  (score=37)
```python
    def current_level(self):
```
<details><summary>Show generated C (score=37)</summary>

```c
/* Python wrapper */
static PyObject *__pyx_pw_6Cython_8Compiler_8Scanning_12PyrexScanner_9current_level(PyObject *__pyx_self, 
#if CYTHON_METH_FASTCALL
PyObject *const *__pyx_args, Py_ssize_t __pyx_nargs, PyObject *__pyx_kwds
#else
PyObject *__pyx_args, PyObject *__pyx_kwds
#endif
); /*proto*/
PyDoc_STRVAR(__pyx_doc_6Cython_8Compiler_8Scanning_12PyrexScanner_8current_level, "File: Cython/Compiler/Scanning.py (starting at line 359)");
static PyMethodDef __pyx_mdef_6Cython_8Compiler_8Scanning_12PyrexScanner_9current_level = {"current_level", (PyCFunction)(void(*)(void))(__Pyx_PyCFunction_FastCallWithKeywords)__pyx_pw_6Cython_8Compiler_8Scanning_12PyrexScanner_9current_level, __Pyx_METH_FASTCALL|METH_KEYWORDS, __pyx_doc_6Cython_8Compiler_8Scanning_12PyrexScanner_8current_level};
static PyObject *__pyx_pw_6Cython_8Compiler_8Scanning_12PyrexScanner_9current_level(PyObject *__pyx_self, 
#if CYTHON_METH_FASTCALL
PyObject *const *__pyx_args, Py_ssize_t __pyx_nargs, PyObject *__pyx_kwds
#else
PyObject *__pyx_args, PyObject *__pyx_kwds
#endif
) {
  PyObject *__pyx_v_self = 0;
  #if !CYTHON_METH_FASTCALL
  CYTHON_UNUSED Py_ssize_t __pyx_nargs;
  #endif
  CYTHON_UNUSED PyObject *const *__pyx_kwvalues;
  PyObject *__pyx_r = 0;
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("current_level (wrapper)", 0);
  #if !CYTHON_METH_FASTCALL
  #if CYTHON_ASSUME_SAFE_SIZE
  __pyx_nargs = PyTuple_GET_SIZE(__pyx_args);
  #else
  __pyx_nargs = PyTuple_Size(__pyx_args); if (unlikely(__pyx_nargs < 0)) return NULL;
  #endif
  #endif
  __pyx_kwvalues = __Pyx_KwValues_FASTCALL(__pyx_args, __pyx_nargs);
  {
    PyObject ** const __pyx_pyargnames[] = {&__pyx_mstate_global->__pyx_n_u_self,0};
  PyObject* values[1] = {0};
    const Py_ssize_t __pyx_kwds_len = (__pyx_kwds) ? __Pyx_NumKwargs_FASTCALL(__pyx_kwds) : 0;
    if (unlikely(__pyx_kwds_len) < 0) __PYX_ERR(0, 359, __pyx_L3_error)
    if (__pyx_kwds_len > 0) {
      switch (__pyx_nargs) {
        case  1:
        values[0] = __Pyx_ArgRef_FASTCALL(__pyx_args, 0);
        if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[0])) __PYX_ERR(0, 359, __pyx_L3_error)
        CYTHON_FALLTHROUGH;
        case  0: break;
        default: goto __pyx_L5_argtuple_error;
      }
      const Py_ssize_t kwd_pos_args = __pyx_nargs;
      if (__Pyx_ParseKeywords(__pyx_kwds, __pyx_kwvalues, __pyx_pyargnames, 0, values, kwd_pos_args, __pyx_kwds_len, "current_level", 0) < (0)) __PYX_ERR(0, 359, __pyx_L3_error)
      for (Py_ssize_t i = __pyx_nargs; i < 1; i++) {
        if (unlikely(!values[i])) { __Pyx_RaiseArgtupleInvalid("current_level", 1, 1, 1, i); __PYX_ERR(0, 359, __pyx_L3_error) }
      }
    } else if (unlikely(__pyx_nargs != 1)) {
      goto __pyx_L5_argtuple_error;
    } else {
      values[0] = __Pyx_ArgRef_FASTCALL(__pyx_args, 0);
      if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[0])) __PYX_ERR(0, 359, __pyx_L3_error)
    }
    __pyx_v_self = values[0];
  }
  goto __pyx_L6_skip;
  __pyx_L5_argtuple_error:;
  __Pyx_RaiseArgtupleInvalid("current_level", 1, 1, 1, __pyx_nargs); __PYX_ERR(0, 359, __pyx_L3_error)
  __pyx_L6_skip:;
  goto __pyx_L4_argument_unpacking_done;
  __pyx_L3_error:;
  for (Py_ssize_t __pyx_temp=0; __pyx_temp < (Py_ssize_t)(sizeof(values)/sizeof(values[0])); ++__pyx_temp) {
    Py_XDECREF(values[__pyx_temp]);
  }
  __Pyx_AddTraceback("Cython.Compiler.Scanning.PyrexScanner.current_level", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __Pyx_RefNannyFinishContext();
  return NULL;
  __pyx_L4_argument_unpacking_done:;
  __pyx_r = __pyx_pf_6Cython_8Compiler_8Scanning_12PyrexScanner_8current_level(__pyx_self, __pyx_v_self);
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

static PyObject *__pyx_pf_6Cython_8Compiler_8Scanning_12PyrexScanner_8current_level(CYTHON_UNUSED PyObject *__pyx_self, PyObject *__pyx_v_self) {
  PyObject *__pyx_r = NULL;
/* … */
  /* function exit code */
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_t_1);
  __Pyx_XDECREF(__pyx_t_2);
  __Pyx_AddTraceback("Cython.Compiler.Scanning.PyrexScanner.current_level", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_r = NULL;
  __pyx_L0:;
  __Pyx_XGIVEREF(__pyx_r);
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}
/* … */
  __pyx_t_9 = __Pyx_CyFunction_New(&__pyx_mdef_6Cython_8Compiler_8Scanning_12PyrexScanner_9current_level, 0, __pyx_mstate_global->__pyx_n_u_PyrexScanner_current_level, NULL, __pyx_mstate_global->__pyx_n_u_Cython_Compiler_Scanning, __pyx_mstate_global->__pyx_d, ((PyObject *)__pyx_mstate_global->__pyx_codeobj_tab[39])); if (unlikely(!__pyx_t_9)) __PYX_ERR(0, 359, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_9);
  #if CYTHON_COMPILING_IN_CPYTHON && PY_VERSION_HEX >= 0x030E0000
  PyUnstable_Object_EnableDeferredRefcount(__pyx_t_9);
  #endif
  if (__Pyx_SetNameInClass(__pyx_t_8, __pyx_mstate_global->__pyx_n_u_current_level, __pyx_t_9) < (0)) __PYX_ERR(0, 359, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_9); __pyx_t_9 = 0;
```

</details>

L360  🟠  (score=6)
```python
        return self.indentation_stack[-1]
```
<details><summary>Show generated C (score=6)</summary>

```c
  __Pyx_XDECREF(__pyx_r);
  __pyx_t_1 = __Pyx_PyObject_GetAttrStr(__pyx_v_self, __pyx_mstate_global->__pyx_n_u_indentation_stack); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 360, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __pyx_t_2 = __Pyx_GetItemInt(__pyx_t_1, -1L, long, 1, __Pyx_PyLong_From_long, 0, 0, 0, 1, __Pyx_ReferenceSharing_OwnStrongReference); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 360, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __pyx_r = __pyx_t_2;
  __pyx_t_2 = 0;
  goto __pyx_L0;
```

</details>

L361  ⚪  (score=0)
```python
```
L362  🔴  (score=41)
```python
    def open_bracket_action(self, text):
```
<details><summary>Show generated C (score=41)</summary>

```c
/* Python wrapper */
static PyObject *__pyx_pw_6Cython_8Compiler_8Scanning_12PyrexScanner_11open_bracket_action(PyObject *__pyx_self, 
#if CYTHON_METH_FASTCALL
PyObject *const *__pyx_args, Py_ssize_t __pyx_nargs, PyObject *__pyx_kwds
#else
PyObject *__pyx_args, PyObject *__pyx_kwds
#endif
); /*proto*/
PyDoc_STRVAR(__pyx_doc_6Cython_8Compiler_8Scanning_12PyrexScanner_10open_bracket_action, "File: Cython/Compiler/Scanning.py (starting at line 362)");
static PyMethodDef __pyx_mdef_6Cython_8Compiler_8Scanning_12PyrexScanner_11open_bracket_action = {"open_bracket_action", (PyCFunction)(void(*)(void))(__Pyx_PyCFunction_FastCallWithKeywords)__pyx_pw_6Cython_8Compiler_8Scanning_12PyrexScanner_11open_bracket_action, __Pyx_METH_FASTCALL|METH_KEYWORDS, __pyx_doc_6Cython_8Compiler_8Scanning_12PyrexScanner_10open_bracket_action};
static PyObject *__pyx_pw_6Cython_8Compiler_8Scanning_12PyrexScanner_11open_bracket_action(PyObject *__pyx_self, 
#if CYTHON_METH_FASTCALL
PyObject *const *__pyx_args, Py_ssize_t __pyx_nargs, PyObject *__pyx_kwds
#else
PyObject *__pyx_args, PyObject *__pyx_kwds
#endif
) {
  PyObject *__pyx_v_self = 0;
  PyObject *__pyx_v_text = 0;
  #if !CYTHON_METH_FASTCALL
  CYTHON_UNUSED Py_ssize_t __pyx_nargs;
  #endif
  CYTHON_UNUSED PyObject *const *__pyx_kwvalues;
  PyObject *__pyx_r = 0;
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("open_bracket_action (wrapper)", 0);
  #if !CYTHON_METH_FASTCALL
  #if CYTHON_ASSUME_SAFE_SIZE
  __pyx_nargs = PyTuple_GET_SIZE(__pyx_args);
  #else
  __pyx_nargs = PyTuple_Size(__pyx_args); if (unlikely(__pyx_nargs < 0)) return NULL;
  #endif
  #endif
  __pyx_kwvalues = __Pyx_KwValues_FASTCALL(__pyx_args, __pyx_nargs);
  {
    PyObject ** const __pyx_pyargnames[] = {&__pyx_mstate_global->__pyx_n_u_self,&__pyx_mstate_global->__pyx_n_u_text,0};
  PyObject* values[2] = {0,0};
    const Py_ssize_t __pyx_kwds_len = (__pyx_kwds) ? __Pyx_NumKwargs_FASTCALL(__pyx_kwds) : 0;
    if (unlikely(__pyx_kwds_len) < 0) __PYX_ERR(0, 362, __pyx_L3_error)
    if (__pyx_kwds_len > 0) {
      switch (__pyx_nargs) {
        case  2:
        values[1] = __Pyx_ArgRef_FASTCALL(__pyx_args, 1);
        if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[1])) __PYX_ERR(0, 362, __pyx_L3_error)
        CYTHON_FALLTHROUGH;
        case  1:
        values[0] = __Pyx_ArgRef_FASTCALL(__pyx_args, 0);
        if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[0])) __PYX_ERR(0, 362, __pyx_L3_error)
        CYTHON_FALLTHROUGH;
        case  0: break;
        default: goto __pyx_L5_argtuple_error;
      }
      const Py_ssize_t kwd_pos_args = __pyx_nargs;
      if (__Pyx_ParseKeywords(__pyx_kwds, __pyx_kwvalues, __pyx_pyargnames, 0, values, kwd_pos_args, __pyx_kwds_len, "open_bracket_action", 0) < (0)) __PYX_ERR(0, 362, __pyx_L3_error)
      for (Py_ssize_t i = __pyx_nargs; i < 2; i++) {
        if (unlikely(!values[i])) { __Pyx_RaiseArgtupleInvalid("open_bracket_action", 1, 2, 2, i); __PYX_ERR(0, 362, __pyx_L3_error) }
      }
    } else if (unlikely(__pyx_nargs != 2)) {
      goto __pyx_L5_argtuple_error;
    } else {
      values[0] = __Pyx_ArgRef_FASTCALL(__pyx_args, 0);
      if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[0])) __PYX_ERR(0, 362, __pyx_L3_error)
      values[1] = __Pyx_ArgRef_FASTCALL(__pyx_args, 1);
      if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[1])) __PYX_ERR(0, 362, __pyx_L3_error)
    }
    __pyx_v_self = values[0];
    __pyx_v_text = values[1];
  }
  goto __pyx_L6_skip;
  __pyx_L5_argtuple_error:;
  __Pyx_RaiseArgtupleInvalid("open_bracket_action", 1, 2, 2, __pyx_nargs); __PYX_ERR(0, 362, __pyx_L3_error)
  __pyx_L6_skip:;
  goto __pyx_L4_argument_unpacking_done;
  __pyx_L3_error:;
  for (Py_ssize_t __pyx_temp=0; __pyx_temp < (Py_ssize_t)(sizeof(values)/sizeof(values[0])); ++__pyx_temp) {
    Py_XDECREF(values[__pyx_temp]);
  }
  __Pyx_AddTraceback("Cython.Compiler.Scanning.PyrexScanner.open_bracket_action", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __Pyx_RefNannyFinishContext();
  return NULL;
  __pyx_L4_argument_unpacking_done:;
  __pyx_r = __pyx_pf_6Cython_8Compiler_8Scanning_12PyrexScanner_10open_bracket_action(__pyx_self, __pyx_v_self, __pyx_v_text);
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

static PyObject *__pyx_pf_6Cython_8Compiler_8Scanning_12PyrexScanner_10open_bracket_action(CYTHON_UNUSED PyObject *__pyx_self, PyObject *__pyx_v_self, PyObject *__pyx_v_text) {
  PyObject *__pyx_r = NULL;
/* … */
  /* function exit code */
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_t_1);
  __Pyx_XDECREF(__pyx_t_2);
  __Pyx_AddTraceback("Cython.Compiler.Scanning.PyrexScanner.open_bracket_action", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_r = NULL;
  __pyx_L0:;
  __Pyx_XGIVEREF(__pyx_r);
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}
/* … */
  __pyx_t_9 = __Pyx_CyFunction_New(&__pyx_mdef_6Cython_8Compiler_8Scanning_12PyrexScanner_11open_bracket_action, 0, __pyx_mstate_global->__pyx_n_u_PyrexScanner_open_bracket_action, NULL, __pyx_mstate_global->__pyx_n_u_Cython_Compiler_Scanning, __pyx_mstate_global->__pyx_d, ((PyObject *)__pyx_mstate_global->__pyx_codeobj_tab[40])); if (unlikely(!__pyx_t_9)) __PYX_ERR(0, 362, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_9);
  #if CYTHON_COMPILING_IN_CPYTHON && PY_VERSION_HEX >= 0x030E0000
  PyUnstable_Object_EnableDeferredRefcount(__pyx_t_9);
  #endif
  if (__Pyx_SetNameInClass(__pyx_t_8, __pyx_mstate_global->__pyx_n_u_open_bracket_action, __pyx_t_9) < (0)) __PYX_ERR(0, 362, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_9); __pyx_t_9 = 0;
```

</details>

L363  🟠  (score=8)
```python
        self.bracket_nesting_level += 1
```
<details><summary>Show generated C (score=8)</summary>

```c
  __pyx_t_1 = __Pyx_PyObject_GetAttrStr(__pyx_v_self, __pyx_mstate_global->__pyx_n_u_bracket_nesting_level); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 363, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __pyx_t_2 = __Pyx_PyLong_AddObjC(__pyx_t_1, __pyx_mstate_global->__pyx_int_1, 1, 1, 0); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 363, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  if (__Pyx_PyObject_SetAttrStr(__pyx_v_self, __pyx_mstate_global->__pyx_n_u_bracket_nesting_level, __pyx_t_2) < (0)) __PYX_ERR(0, 363, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
```

</details>

L364  🟡  (score=2)
```python
        return text
```
<details><summary>Show generated C (score=2)</summary>

```c
  __Pyx_XDECREF(__pyx_r);
  __Pyx_INCREF(__pyx_v_text);
  __pyx_r = __pyx_v_text;
  goto __pyx_L0;
```

</details>

L365  ⚪  (score=0)
```python
```
L366  🔴  (score=41)
```python
    def close_bracket_action(self, text):
```
<details><summary>Show generated C (score=41)</summary>

```c
/* Python wrapper */
static PyObject *__pyx_pw_6Cython_8Compiler_8Scanning_12PyrexScanner_13close_bracket_action(PyObject *__pyx_self, 
#if CYTHON_METH_FASTCALL
PyObject *const *__pyx_args, Py_ssize_t __pyx_nargs, PyObject *__pyx_kwds
#else
PyObject *__pyx_args, PyObject *__pyx_kwds
#endif
); /*proto*/
PyDoc_STRVAR(__pyx_doc_6Cython_8Compiler_8Scanning_12PyrexScanner_12close_bracket_action, "File: Cython/Compiler/Scanning.py (starting at line 366)");
static PyMethodDef __pyx_mdef_6Cython_8Compiler_8Scanning_12PyrexScanner_13close_bracket_action = {"close_bracket_action", (PyCFunction)(void(*)(void))(__Pyx_PyCFunction_FastCallWithKeywords)__pyx_pw_6Cython_8Compiler_8Scanning_12PyrexScanner_13close_bracket_action, __Pyx_METH_FASTCALL|METH_KEYWORDS, __pyx_doc_6Cython_8Compiler_8Scanning_12PyrexScanner_12close_bracket_action};
static PyObject *__pyx_pw_6Cython_8Compiler_8Scanning_12PyrexScanner_13close_bracket_action(PyObject *__pyx_self, 
#if CYTHON_METH_FASTCALL
PyObject *const *__pyx_args, Py_ssize_t __pyx_nargs, PyObject *__pyx_kwds
#else
PyObject *__pyx_args, PyObject *__pyx_kwds
#endif
) {
  PyObject *__pyx_v_self = 0;
  PyObject *__pyx_v_text = 0;
  #if !CYTHON_METH_FASTCALL
  CYTHON_UNUSED Py_ssize_t __pyx_nargs;
  #endif
  CYTHON_UNUSED PyObject *const *__pyx_kwvalues;
  PyObject *__pyx_r = 0;
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("close_bracket_action (wrapper)", 0);
  #if !CYTHON_METH_FASTCALL
  #if CYTHON_ASSUME_SAFE_SIZE
  __pyx_nargs = PyTuple_GET_SIZE(__pyx_args);
  #else
  __pyx_nargs = PyTuple_Size(__pyx_args); if (unlikely(__pyx_nargs < 0)) return NULL;
  #endif
  #endif
  __pyx_kwvalues = __Pyx_KwValues_FASTCALL(__pyx_args, __pyx_nargs);
  {
    PyObject ** const __pyx_pyargnames[] = {&__pyx_mstate_global->__pyx_n_u_self,&__pyx_mstate_global->__pyx_n_u_text,0};
  PyObject* values[2] = {0,0};
    const Py_ssize_t __pyx_kwds_len = (__pyx_kwds) ? __Pyx_NumKwargs_FASTCALL(__pyx_kwds) : 0;
    if (unlikely(__pyx_kwds_len) < 0) __PYX_ERR(0, 366, __pyx_L3_error)
    if (__pyx_kwds_len > 0) {
      switch (__pyx_nargs) {
        case  2:
        values[1] = __Pyx_ArgRef_FASTCALL(__pyx_args, 1);
        if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[1])) __PYX_ERR(0, 366, __pyx_L3_error)
        CYTHON_FALLTHROUGH;
        case  1:
        values[0] = __Pyx_ArgRef_FASTCALL(__pyx_args, 0);
        if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[0])) __PYX_ERR(0, 366, __pyx_L3_error)
        CYTHON_FALLTHROUGH;
        case  0: break;
        default: goto __pyx_L5_argtuple_error;
      }
      const Py_ssize_t kwd_pos_args = __pyx_nargs;
      if (__Pyx_ParseKeywords(__pyx_kwds, __pyx_kwvalues, __pyx_pyargnames, 0, values, kwd_pos_args, __pyx_kwds_len, "close_bracket_action", 0) < (0)) __PYX_ERR(0, 366, __pyx_L3_error)
      for (Py_ssize_t i = __pyx_nargs; i < 2; i++) {
        if (unlikely(!values[i])) { __Pyx_RaiseArgtupleInvalid("close_bracket_action", 1, 2, 2, i); __PYX_ERR(0, 366, __pyx_L3_error) }
      }
    } else if (unlikely(__pyx_nargs != 2)) {
      goto __pyx_L5_argtuple_error;
    } else {
      values[0] = __Pyx_ArgRef_FASTCALL(__pyx_args, 0);
      if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[0])) __PYX_ERR(0, 366, __pyx_L3_error)
      values[1] = __Pyx_ArgRef_FASTCALL(__pyx_args, 1);
      if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[1])) __PYX_ERR(0, 366, __pyx_L3_error)
    }
    __pyx_v_self = values[0];
    __pyx_v_text = values[1];
  }
  goto __pyx_L6_skip;
  __pyx_L5_argtuple_error:;
  __Pyx_RaiseArgtupleInvalid("close_bracket_action", 1, 2, 2, __pyx_nargs); __PYX_ERR(0, 366, __pyx_L3_error)
  __pyx_L6_skip:;
  goto __pyx_L4_argument_unpacking_done;
  __pyx_L3_error:;
  for (Py_ssize_t __pyx_temp=0; __pyx_temp < (Py_ssize_t)(sizeof(values)/sizeof(values[0])); ++__pyx_temp) {
    Py_XDECREF(values[__pyx_temp]);
  }
  __Pyx_AddTraceback("Cython.Compiler.Scanning.PyrexScanner.close_bracket_action", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __Pyx_RefNannyFinishContext();
  return NULL;
  __pyx_L4_argument_unpacking_done:;
  __pyx_r = __pyx_pf_6Cython_8Compiler_8Scanning_12PyrexScanner_12close_bracket_action(__pyx_self, __pyx_v_self, __pyx_v_text);
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

static PyObject *__pyx_pf_6Cython_8Compiler_8Scanning_12PyrexScanner_12close_bracket_action(CYTHON_UNUSED PyObject *__pyx_self, PyObject *__pyx_v_self, PyObject *__pyx_v_text) {
  PyObject *__pyx_r = NULL;
/* … */
  /* function exit code */
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_t_1);
  __Pyx_XDECREF(__pyx_t_2);
  __Pyx_AddTraceback("Cython.Compiler.Scanning.PyrexScanner.close_bracket_action", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_r = NULL;
  __pyx_L0:;
  __Pyx_XGIVEREF(__pyx_r);
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}
/* … */
  __pyx_t_9 = __Pyx_CyFunction_New(&__pyx_mdef_6Cython_8Compiler_8Scanning_12PyrexScanner_13close_bracket_action, 0, __pyx_mstate_global->__pyx_n_u_PyrexScanner_close_bracket_actio, NULL, __pyx_mstate_global->__pyx_n_u_Cython_Compiler_Scanning, __pyx_mstate_global->__pyx_d, ((PyObject *)__pyx_mstate_global->__pyx_codeobj_tab[41])); if (unlikely(!__pyx_t_9)) __PYX_ERR(0, 366, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_9);
  #if CYTHON_COMPILING_IN_CPYTHON && PY_VERSION_HEX >= 0x030E0000
  PyUnstable_Object_EnableDeferredRefcount(__pyx_t_9);
  #endif
  if (__Pyx_SetNameInClass(__pyx_t_8, __pyx_mstate_global->__pyx_n_u_close_bracket_action, __pyx_t_9) < (0)) __PYX_ERR(0, 366, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_9); __pyx_t_9 = 0;
```

</details>

L367  🟠  (score=8)
```python
        self.bracket_nesting_level -= 1
```
<details><summary>Show generated C (score=8)</summary>

```c
  __pyx_t_1 = __Pyx_PyObject_GetAttrStr(__pyx_v_self, __pyx_mstate_global->__pyx_n_u_bracket_nesting_level); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 367, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __pyx_t_2 = __Pyx_PyLong_SubtractObjC(__pyx_t_1, __pyx_mstate_global->__pyx_int_1, 1, 1, 0); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 367, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  if (__Pyx_PyObject_SetAttrStr(__pyx_v_self, __pyx_mstate_global->__pyx_n_u_bracket_nesting_level, __pyx_t_2) < (0)) __PYX_ERR(0, 367, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
```

</details>

L368  🟡  (score=2)
```python
        return text
```
<details><summary>Show generated C (score=2)</summary>

```c
  __Pyx_XDECREF(__pyx_r);
  __Pyx_INCREF(__pyx_v_text);
  __pyx_r = __pyx_v_text;
  goto __pyx_L0;
```

</details>

L369  ⚪  (score=0)
```python
```
L370  🔴  (score=41)
```python
    def open_brace_action(self, text):
```
<details><summary>Show generated C (score=41)</summary>

```c
/* Python wrapper */
static PyObject *__pyx_pw_6Cython_8Compiler_8Scanning_12PyrexScanner_15open_brace_action(PyObject *__pyx_self, 
#if CYTHON_METH_FASTCALL
PyObject *const *__pyx_args, Py_ssize_t __pyx_nargs, PyObject *__pyx_kwds
#else
PyObject *__pyx_args, PyObject *__pyx_kwds
#endif
); /*proto*/
PyDoc_STRVAR(__pyx_doc_6Cython_8Compiler_8Scanning_12PyrexScanner_14open_brace_action, "File: Cython/Compiler/Scanning.py (starting at line 370)");
static PyMethodDef __pyx_mdef_6Cython_8Compiler_8Scanning_12PyrexScanner_15open_brace_action = {"open_brace_action", (PyCFunction)(void(*)(void))(__Pyx_PyCFunction_FastCallWithKeywords)__pyx_pw_6Cython_8Compiler_8Scanning_12PyrexScanner_15open_brace_action, __Pyx_METH_FASTCALL|METH_KEYWORDS, __pyx_doc_6Cython_8Compiler_8Scanning_12PyrexScanner_14open_brace_action};
static PyObject *__pyx_pw_6Cython_8Compiler_8Scanning_12PyrexScanner_15open_brace_action(PyObject *__pyx_self, 
#if CYTHON_METH_FASTCALL
PyObject *const *__pyx_args, Py_ssize_t __pyx_nargs, PyObject *__pyx_kwds
#else
PyObject *__pyx_args, PyObject *__pyx_kwds
#endif
) {
  PyObject *__pyx_v_self = 0;
  PyObject *__pyx_v_text = 0;
  #if !CYTHON_METH_FASTCALL
  CYTHON_UNUSED Py_ssize_t __pyx_nargs;
  #endif
  CYTHON_UNUSED PyObject *const *__pyx_kwvalues;
  PyObject *__pyx_r = 0;
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("open_brace_action (wrapper)", 0);
  #if !CYTHON_METH_FASTCALL
  #if CYTHON_ASSUME_SAFE_SIZE
  __pyx_nargs = PyTuple_GET_SIZE(__pyx_args);
  #else
  __pyx_nargs = PyTuple_Size(__pyx_args); if (unlikely(__pyx_nargs < 0)) return NULL;
  #endif
  #endif
  __pyx_kwvalues = __Pyx_KwValues_FASTCALL(__pyx_args, __pyx_nargs);
  {
    PyObject ** const __pyx_pyargnames[] = {&__pyx_mstate_global->__pyx_n_u_self,&__pyx_mstate_global->__pyx_n_u_text,0};
  PyObject* values[2] = {0,0};
    const Py_ssize_t __pyx_kwds_len = (__pyx_kwds) ? __Pyx_NumKwargs_FASTCALL(__pyx_kwds) : 0;
    if (unlikely(__pyx_kwds_len) < 0) __PYX_ERR(0, 370, __pyx_L3_error)
    if (__pyx_kwds_len > 0) {
      switch (__pyx_nargs) {
        case  2:
        values[1] = __Pyx_ArgRef_FASTCALL(__pyx_args, 1);
        if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[1])) __PYX_ERR(0, 370, __pyx_L3_error)
        CYTHON_FALLTHROUGH;
        case  1:
        values[0] = __Pyx_ArgRef_FASTCALL(__pyx_args, 0);
        if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[0])) __PYX_ERR(0, 370, __pyx_L3_error)
        CYTHON_FALLTHROUGH;
        case  0: break;
        default: goto __pyx_L5_argtuple_error;
      }
      const Py_ssize_t kwd_pos_args = __pyx_nargs;
      if (__Pyx_ParseKeywords(__pyx_kwds, __pyx_kwvalues, __pyx_pyargnames, 0, values, kwd_pos_args, __pyx_kwds_len, "open_brace_action", 0) < (0)) __PYX_ERR(0, 370, __pyx_L3_error)
      for (Py_ssize_t i = __pyx_nargs; i < 2; i++) {
        if (unlikely(!values[i])) { __Pyx_RaiseArgtupleInvalid("open_brace_action", 1, 2, 2, i); __PYX_ERR(0, 370, __pyx_L3_error) }
      }
    } else if (unlikely(__pyx_nargs != 2)) {
      goto __pyx_L5_argtuple_error;
    } else {
      values[0] = __Pyx_ArgRef_FASTCALL(__pyx_args, 0);
      if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[0])) __PYX_ERR(0, 370, __pyx_L3_error)
      values[1] = __Pyx_ArgRef_FASTCALL(__pyx_args, 1);
      if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[1])) __PYX_ERR(0, 370, __pyx_L3_error)
    }
    __pyx_v_self = values[0];
    __pyx_v_text = values[1];
  }
  goto __pyx_L6_skip;
  __pyx_L5_argtuple_error:;
  __Pyx_RaiseArgtupleInvalid("open_brace_action", 1, 2, 2, __pyx_nargs); __PYX_ERR(0, 370, __pyx_L3_error)
  __pyx_L6_skip:;
  goto __pyx_L4_argument_unpacking_done;
  __pyx_L3_error:;
  for (Py_ssize_t __pyx_temp=0; __pyx_temp < (Py_ssize_t)(sizeof(values)/sizeof(values[0])); ++__pyx_temp) {
    Py_XDECREF(values[__pyx_temp]);
  }
  __Pyx_AddTraceback("Cython.Compiler.Scanning.PyrexScanner.open_brace_action", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __Pyx_RefNannyFinishContext();
  return NULL;
  __pyx_L4_argument_unpacking_done:;
  __pyx_r = __pyx_pf_6Cython_8Compiler_8Scanning_12PyrexScanner_14open_brace_action(__pyx_self, __pyx_v_self, __pyx_v_text);
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

static PyObject *__pyx_pf_6Cython_8Compiler_8Scanning_12PyrexScanner_14open_brace_action(CYTHON_UNUSED PyObject *__pyx_self, PyObject *__pyx_v_self, PyObject *__pyx_v_text) {
  PyObject *__pyx_r = NULL;
/* … */
  /* function exit code */
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_t_1);
  __Pyx_XDECREF(__pyx_t_2);
  __Pyx_AddTraceback("Cython.Compiler.Scanning.PyrexScanner.open_brace_action", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_r = NULL;
  __pyx_L0:;
  __Pyx_XGIVEREF(__pyx_r);
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}
/* … */
  __pyx_t_9 = __Pyx_CyFunction_New(&__pyx_mdef_6Cython_8Compiler_8Scanning_12PyrexScanner_15open_brace_action, 0, __pyx_mstate_global->__pyx_n_u_PyrexScanner_open_brace_action, NULL, __pyx_mstate_global->__pyx_n_u_Cython_Compiler_Scanning, __pyx_mstate_global->__pyx_d, ((PyObject *)__pyx_mstate_global->__pyx_codeobj_tab[42])); if (unlikely(!__pyx_t_9)) __PYX_ERR(0, 370, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_9);
  #if CYTHON_COMPILING_IN_CPYTHON && PY_VERSION_HEX >= 0x030E0000
  PyUnstable_Object_EnableDeferredRefcount(__pyx_t_9);
  #endif
  if (__Pyx_SetNameInClass(__pyx_t_8, __pyx_mstate_global->__pyx_n_u_open_brace_action, __pyx_t_9) < (0)) __PYX_ERR(0, 370, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_9); __pyx_t_9 = 0;
```

</details>

L371  🟠  (score=5)
```python
        return self.open_bracket_action(text)
```
<details><summary>Show generated C (score=5)</summary>

```c
  __Pyx_XDECREF(__pyx_r);
  __pyx_t_2 = __pyx_v_self;
  __Pyx_INCREF(__pyx_t_2);
  __pyx_t_3 = 0;
  {
    PyObject *__pyx_callargs[2] = {__pyx_t_2, __pyx_v_text};
    __pyx_t_1 = __Pyx_PyObject_FastCallMethod((PyObject*)__pyx_mstate_global->__pyx_n_u_open_bracket_action, __pyx_callargs+__pyx_t_3, (2-__pyx_t_3) | (1*__Pyx_PY_VECTORCALL_ARGUMENTS_OFFSET));
    __Pyx_XDECREF(__pyx_t_2); __pyx_t_2 = 0;
    if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 371, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_1);
  }
  __pyx_r = __pyx_t_1;
  __pyx_t_1 = 0;
  goto __pyx_L0;
```

</details>

L372  ⚪  (score=0)
```python
```
L373  🔴  (score=43)
```python
    def close_brace_action(self, text):
```
<details><summary>Show generated C (score=43)</summary>

```c
/* Python wrapper */
static PyObject *__pyx_pw_6Cython_8Compiler_8Scanning_12PyrexScanner_17close_brace_action(PyObject *__pyx_self, 
#if CYTHON_METH_FASTCALL
PyObject *const *__pyx_args, Py_ssize_t __pyx_nargs, PyObject *__pyx_kwds
#else
PyObject *__pyx_args, PyObject *__pyx_kwds
#endif
); /*proto*/
PyDoc_STRVAR(__pyx_doc_6Cython_8Compiler_8Scanning_12PyrexScanner_16close_brace_action, "File: Cython/Compiler/Scanning.py (starting at line 373)");
static PyMethodDef __pyx_mdef_6Cython_8Compiler_8Scanning_12PyrexScanner_17close_brace_action = {"close_brace_action", (PyCFunction)(void(*)(void))(__Pyx_PyCFunction_FastCallWithKeywords)__pyx_pw_6Cython_8Compiler_8Scanning_12PyrexScanner_17close_brace_action, __Pyx_METH_FASTCALL|METH_KEYWORDS, __pyx_doc_6Cython_8Compiler_8Scanning_12PyrexScanner_16close_brace_action};
static PyObject *__pyx_pw_6Cython_8Compiler_8Scanning_12PyrexScanner_17close_brace_action(PyObject *__pyx_self, 
#if CYTHON_METH_FASTCALL
PyObject *const *__pyx_args, Py_ssize_t __pyx_nargs, PyObject *__pyx_kwds
#else
PyObject *__pyx_args, PyObject *__pyx_kwds
#endif
) {
  PyObject *__pyx_v_self = 0;
  PyObject *__pyx_v_text = 0;
  #if !CYTHON_METH_FASTCALL
  CYTHON_UNUSED Py_ssize_t __pyx_nargs;
  #endif
  CYTHON_UNUSED PyObject *const *__pyx_kwvalues;
  PyObject *__pyx_r = 0;
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("close_brace_action (wrapper)", 0);
  #if !CYTHON_METH_FASTCALL
  #if CYTHON_ASSUME_SAFE_SIZE
  __pyx_nargs = PyTuple_GET_SIZE(__pyx_args);
  #else
  __pyx_nargs = PyTuple_Size(__pyx_args); if (unlikely(__pyx_nargs < 0)) return NULL;
  #endif
  #endif
  __pyx_kwvalues = __Pyx_KwValues_FASTCALL(__pyx_args, __pyx_nargs);
  {
    PyObject ** const __pyx_pyargnames[] = {&__pyx_mstate_global->__pyx_n_u_self,&__pyx_mstate_global->__pyx_n_u_text,0};
  PyObject* values[2] = {0,0};
    const Py_ssize_t __pyx_kwds_len = (__pyx_kwds) ? __Pyx_NumKwargs_FASTCALL(__pyx_kwds) : 0;
    if (unlikely(__pyx_kwds_len) < 0) __PYX_ERR(0, 373, __pyx_L3_error)
    if (__pyx_kwds_len > 0) {
      switch (__pyx_nargs) {
        case  2:
        values[1] = __Pyx_ArgRef_FASTCALL(__pyx_args, 1);
        if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[1])) __PYX_ERR(0, 373, __pyx_L3_error)
        CYTHON_FALLTHROUGH;
        case  1:
        values[0] = __Pyx_ArgRef_FASTCALL(__pyx_args, 0);
        if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[0])) __PYX_ERR(0, 373, __pyx_L3_error)
        CYTHON_FALLTHROUGH;
        case  0: break;
        default: goto __pyx_L5_argtuple_error;
      }
      const Py_ssize_t kwd_pos_args = __pyx_nargs;
      if (__Pyx_ParseKeywords(__pyx_kwds, __pyx_kwvalues, __pyx_pyargnames, 0, values, kwd_pos_args, __pyx_kwds_len, "close_brace_action", 0) < (0)) __PYX_ERR(0, 373, __pyx_L3_error)
      for (Py_ssize_t i = __pyx_nargs; i < 2; i++) {
        if (unlikely(!values[i])) { __Pyx_RaiseArgtupleInvalid("close_brace_action", 1, 2, 2, i); __PYX_ERR(0, 373, __pyx_L3_error) }
      }
    } else if (unlikely(__pyx_nargs != 2)) {
      goto __pyx_L5_argtuple_error;
    } else {
      values[0] = __Pyx_ArgRef_FASTCALL(__pyx_args, 0);
      if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[0])) __PYX_ERR(0, 373, __pyx_L3_error)
      values[1] = __Pyx_ArgRef_FASTCALL(__pyx_args, 1);
      if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[1])) __PYX_ERR(0, 373, __pyx_L3_error)
    }
    __pyx_v_self = values[0];
    __pyx_v_text = values[1];
  }
  goto __pyx_L6_skip;
  __pyx_L5_argtuple_error:;
  __Pyx_RaiseArgtupleInvalid("close_brace_action", 1, 2, 2, __pyx_nargs); __PYX_ERR(0, 373, __pyx_L3_error)
  __pyx_L6_skip:;
  goto __pyx_L4_argument_unpacking_done;
  __pyx_L3_error:;
  for (Py_ssize_t __pyx_temp=0; __pyx_temp < (Py_ssize_t)(sizeof(values)/sizeof(values[0])); ++__pyx_temp) {
    Py_XDECREF(values[__pyx_temp]);
  }
  __Pyx_AddTraceback("Cython.Compiler.Scanning.PyrexScanner.close_brace_action", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __Pyx_RefNannyFinishContext();
  return NULL;
  __pyx_L4_argument_unpacking_done:;
  __pyx_r = __pyx_pf_6Cython_8Compiler_8Scanning_12PyrexScanner_16close_brace_action(__pyx_self, __pyx_v_self, __pyx_v_text);
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

static PyObject *__pyx_pf_6Cython_8Compiler_8Scanning_12PyrexScanner_16close_brace_action(CYTHON_UNUSED PyObject *__pyx_self, PyObject *__pyx_v_self, PyObject *__pyx_v_text) {
  PyObject *__pyx_r = NULL;
/* … */
  /* function exit code */
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_t_2);
  __Pyx_XDECREF(__pyx_t_4);
  __Pyx_XDECREF(__pyx_t_5);
  __Pyx_XDECREF(__pyx_t_6);
  __Pyx_AddTraceback("Cython.Compiler.Scanning.PyrexScanner.close_brace_action", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_r = NULL;
  __pyx_L0:;
  __Pyx_XGIVEREF(__pyx_r);
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}
/* … */
  __pyx_t_9 = __Pyx_CyFunction_New(&__pyx_mdef_6Cython_8Compiler_8Scanning_12PyrexScanner_17close_brace_action, 0, __pyx_mstate_global->__pyx_n_u_PyrexScanner_close_brace_action, NULL, __pyx_mstate_global->__pyx_n_u_Cython_Compiler_Scanning, __pyx_mstate_global->__pyx_d, ((PyObject *)__pyx_mstate_global->__pyx_codeobj_tab[43])); if (unlikely(!__pyx_t_9)) __PYX_ERR(0, 373, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_9);
  #if CYTHON_COMPILING_IN_CPYTHON && PY_VERSION_HEX >= 0x030E0000
  PyUnstable_Object_EnableDeferredRefcount(__pyx_t_9);
  #endif
  if (__Pyx_SetNameInClass(__pyx_t_8, __pyx_mstate_global->__pyx_n_u_close_brace_action, __pyx_t_9) < (0)) __PYX_ERR(0, 373, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_9); __pyx_t_9 = 0;
```

</details>

L374  🟡  (score=4)
```python
        assert text == '}'
```
<details><summary>Show generated C (score=4)</summary>

```c
  #ifndef CYTHON_WITHOUT_ASSERTIONS
  if (unlikely(__pyx_assertions_enabled())) {
    __pyx_t_1 = (__Pyx_PyUnicode_Equals(__pyx_v_text, __pyx_mstate_global->__pyx_kp_u__8, Py_EQ)); if (unlikely((__pyx_t_1 < 0))) __PYX_ERR(0, 374, __pyx_L1_error)
    if (unlikely(!__pyx_t_1)) {
      __Pyx_Raise(((PyObject *)(((PyTypeObject*)PyExc_AssertionError))), 0, 0, 0);
      __PYX_ERR(0, 374, __pyx_L1_error)
    }
  }
  #else
  if ((1)); else __PYX_ERR(0, 374, __pyx_L1_error)
  #endif
```

</details>

L375  🟠  (score=5)
```python
        if (self.ft_string_state_stack and
```
<details><summary>Show generated C (score=5)</summary>

```c
  __pyx_t_2 = __Pyx_PyObject_GetAttrStr(__pyx_v_self, __pyx_mstate_global->__pyx_n_u_ft_string_state_stack); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 375, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __pyx_t_3 = __Pyx_PyObject_IsTrue(__pyx_t_2); if (unlikely((__pyx_t_3 < 0))) __PYX_ERR(0, 375, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  if (__pyx_t_3) {
  } else {
    __pyx_t_1 = __pyx_t_3;
    goto __pyx_L4_bool_binop_done;
  }
/* … */
  if (__pyx_t_1) {
/* … */
  }
```

</details>

L376  🔴  (score=22)
```python
                self.ft_string_state_stack[-1].bracket_nesting_level() == self.bracket_nesting_level):
```
<details><summary>Show generated C (score=22)</summary>

```c
  __pyx_t_5 = __Pyx_PyObject_GetAttrStr(__pyx_v_self, __pyx_mstate_global->__pyx_n_u_ft_string_state_stack); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 376, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_5);
  __pyx_t_6 = __Pyx_GetItemInt(__pyx_t_5, -1L, long, 1, __Pyx_PyLong_From_long, 0, 0, 0, 1, __Pyx_ReferenceSharing_OwnStrongReference); if (unlikely(!__pyx_t_6)) __PYX_ERR(0, 376, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_6);
  __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
  __pyx_t_4 = __pyx_t_6;
  __Pyx_INCREF(__pyx_t_4);
  __pyx_t_7 = 0;
  {
    PyObject *__pyx_callargs[2] = {__pyx_t_4, NULL};
    __pyx_t_2 = __Pyx_PyObject_FastCallMethod((PyObject*)__pyx_mstate_global->__pyx_n_u_bracket_nesting_level, __pyx_callargs+__pyx_t_7, (1-__pyx_t_7) | (1*__Pyx_PY_VECTORCALL_ARGUMENTS_OFFSET));
    __Pyx_XDECREF(__pyx_t_4); __pyx_t_4 = 0;
    __Pyx_DECREF(__pyx_t_6); __pyx_t_6 = 0;
    if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 376, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_2);
  }
  __pyx_t_6 = __Pyx_PyObject_GetAttrStr(__pyx_v_self, __pyx_mstate_global->__pyx_n_u_bracket_nesting_level); if (unlikely(!__pyx_t_6)) __PYX_ERR(0, 376, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_6);
  __pyx_t_4 = PyObject_RichCompare(__pyx_t_2, __pyx_t_6, Py_EQ); __Pyx_XGOTREF(__pyx_t_4); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 376, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __Pyx_DECREF(__pyx_t_6); __pyx_t_6 = 0;
  __pyx_t_3 = __Pyx_PyObject_IsTrue(__pyx_t_4); if (unlikely((__pyx_t_3 < 0))) __PYX_ERR(0, 376, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
  __pyx_t_1 = __pyx_t_3;
  __pyx_L4_bool_binop_done:;
```

</details>

L377  🔴  (score=13)
```python
            if not self.ft_string_state_stack[-1].in_format_specifier():
```
<details><summary>Show generated C (score=13)</summary>

```c
    __pyx_t_2 = __Pyx_PyObject_GetAttrStr(__pyx_v_self, __pyx_mstate_global->__pyx_n_u_ft_string_state_stack); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 377, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_2);
    __pyx_t_5 = __Pyx_GetItemInt(__pyx_t_2, -1L, long, 1, __Pyx_PyLong_From_long, 0, 0, 0, 1, __Pyx_ReferenceSharing_OwnStrongReference); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 377, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_5);
    __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
    __pyx_t_6 = __pyx_t_5;
    __Pyx_INCREF(__pyx_t_6);
    __pyx_t_7 = 0;
    {
      PyObject *__pyx_callargs[2] = {__pyx_t_6, NULL};
      __pyx_t_4 = __Pyx_PyObject_FastCallMethod((PyObject*)__pyx_mstate_global->__pyx_n_u_in_format_specifier, __pyx_callargs+__pyx_t_7, (1-__pyx_t_7) | (1*__Pyx_PY_VECTORCALL_ARGUMENTS_OFFSET));
      __Pyx_XDECREF(__pyx_t_6); __pyx_t_6 = 0;
      __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
      if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 377, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_4);
    }
    __pyx_t_1 = __Pyx_PyObject_IsTrue(__pyx_t_4); if (unlikely((__pyx_t_1 < 0))) __PYX_ERR(0, 377, __pyx_L1_error)
    __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
    __pyx_t_3 = (!__pyx_t_1);
    if (__pyx_t_3) {
/* … */
    }
```

</details>

L378  🟠  (score=8)
```python
                self.in_ft_string_expr_prescan -= 1
```
<details><summary>Show generated C (score=8)</summary>

```c
      __pyx_t_4 = __Pyx_PyObject_GetAttrStr(__pyx_v_self, __pyx_mstate_global->__pyx_n_u_in_ft_string_expr_prescan); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 378, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_4);
      __pyx_t_5 = __Pyx_PyLong_SubtractObjC(__pyx_t_4, __pyx_mstate_global->__pyx_int_1, 1, 1, 0); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 378, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_5);
      __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
      if (__Pyx_PyObject_SetAttrStr(__pyx_v_self, __pyx_mstate_global->__pyx_n_u_in_ft_string_expr_prescan, __pyx_t_5) < (0)) __PYX_ERR(0, 378, __pyx_L1_error)
      __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
```

</details>

L379  🟠  (score=5)
```python
                if self.in_ft_string_expr_prescan == 0:
```
<details><summary>Show generated C (score=5)</summary>

```c
      __pyx_t_5 = __Pyx_PyObject_GetAttrStr(__pyx_v_self, __pyx_mstate_global->__pyx_n_u_in_ft_string_expr_prescan); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 379, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_5);
      __pyx_t_3 = (__Pyx_PyLong_BoolEqObjC(__pyx_t_5, __pyx_mstate_global->__pyx_int_0, 0, 0)); if (unlikely((__pyx_t_3 < 0))) __PYX_ERR(0, 379, __pyx_L1_error)
      __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
      if (__pyx_t_3) {
/* … */
      }
```

</details>

L380  🟠  (score=5)
```python
                    self.produce("END_FT_STRING_EXPR")
```
<details><summary>Show generated C (score=5)</summary>

```c
        __pyx_t_4 = __pyx_v_self;
        __Pyx_INCREF(__pyx_t_4);
        __pyx_t_7 = 0;
        {
          PyObject *__pyx_callargs[2] = {__pyx_t_4, __pyx_mstate_global->__pyx_n_u_END_FT_STRING_EXPR};
          __pyx_t_5 = __Pyx_PyObject_FastCallMethod((PyObject*)__pyx_mstate_global->__pyx_n_u_produce, __pyx_callargs+__pyx_t_7, (2-__pyx_t_7) | (1*__Pyx_PY_VECTORCALL_ARGUMENTS_OFFSET));
          __Pyx_XDECREF(__pyx_t_4); __pyx_t_4 = 0;
          if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 380, __pyx_L1_error)
          __Pyx_GOTREF(__pyx_t_5);
        }
        __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
```

</details>

L381  🔴  (score=14)
```python
            self.begin(self.ft_string_state_stack[-1].scanner_state)
```
<details><summary>Show generated C (score=14)</summary>

```c
    __pyx_t_4 = __pyx_v_self;
    __Pyx_INCREF(__pyx_t_4);
    __pyx_t_6 = __Pyx_PyObject_GetAttrStr(__pyx_v_self, __pyx_mstate_global->__pyx_n_u_ft_string_state_stack); if (unlikely(!__pyx_t_6)) __PYX_ERR(0, 381, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_6);
    __pyx_t_2 = __Pyx_GetItemInt(__pyx_t_6, -1L, long, 1, __Pyx_PyLong_From_long, 0, 0, 0, 1, __Pyx_ReferenceSharing_OwnStrongReference); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 381, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_2);
    __Pyx_DECREF(__pyx_t_6); __pyx_t_6 = 0;
    __pyx_t_6 = __Pyx_PyObject_GetAttrStr(__pyx_t_2, __pyx_mstate_global->__pyx_n_u_scanner_state); if (unlikely(!__pyx_t_6)) __PYX_ERR(0, 381, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_6);
    __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
    __pyx_t_7 = 0;
    {
      PyObject *__pyx_callargs[2] = {__pyx_t_4, __pyx_t_6};
      __pyx_t_5 = __Pyx_PyObject_FastCallMethod((PyObject*)__pyx_mstate_global->__pyx_n_u_begin, __pyx_callargs+__pyx_t_7, (2-__pyx_t_7) | (1*__Pyx_PY_VECTORCALL_ARGUMENTS_OFFSET));
      __Pyx_XDECREF(__pyx_t_4); __pyx_t_4 = 0;
      __Pyx_DECREF(__pyx_t_6); __pyx_t_6 = 0;
      if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 381, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_5);
    }
    __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
```

</details>

L382  🔴  (score=11)
```python
            self.ft_string_state_stack[-1].pop_bracket_state()
```
<details><summary>Show generated C (score=11)</summary>

```c
    __pyx_t_4 = __Pyx_PyObject_GetAttrStr(__pyx_v_self, __pyx_mstate_global->__pyx_n_u_ft_string_state_stack); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 382, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_4);
    __pyx_t_2 = __Pyx_GetItemInt(__pyx_t_4, -1L, long, 1, __Pyx_PyLong_From_long, 0, 0, 0, 1, __Pyx_ReferenceSharing_OwnStrongReference); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 382, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_2);
    __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
    __pyx_t_6 = __pyx_t_2;
    __Pyx_INCREF(__pyx_t_6);
    __pyx_t_7 = 0;
    {
      PyObject *__pyx_callargs[2] = {__pyx_t_6, NULL};
      __pyx_t_5 = __Pyx_PyObject_FastCallMethod((PyObject*)__pyx_mstate_global->__pyx_n_u_pop_bracket_state, __pyx_callargs+__pyx_t_7, (1-__pyx_t_7) | (1*__Pyx_PY_VECTORCALL_ARGUMENTS_OFFSET));
      __Pyx_XDECREF(__pyx_t_6); __pyx_t_6 = 0;
      __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
      if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 382, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_5);
    }
    __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
```

</details>

L383  🟠  (score=8)
```python
        self.bracket_nesting_level -= 1
```
<details><summary>Show generated C (score=8)</summary>

```c
  __pyx_t_5 = __Pyx_PyObject_GetAttrStr(__pyx_v_self, __pyx_mstate_global->__pyx_n_u_bracket_nesting_level); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 383, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_5);
  __pyx_t_2 = __Pyx_PyLong_SubtractObjC(__pyx_t_5, __pyx_mstate_global->__pyx_int_1, 1, 1, 0); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 383, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
  if (__Pyx_PyObject_SetAttrStr(__pyx_v_self, __pyx_mstate_global->__pyx_n_u_bracket_nesting_level, __pyx_t_2) < (0)) __PYX_ERR(0, 383, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
```

</details>

L384  🟡  (score=2)
```python
        return text
```
<details><summary>Show generated C (score=2)</summary>

```c
  __Pyx_XDECREF(__pyx_r);
  __Pyx_INCREF(__pyx_v_text);
  __pyx_r = __pyx_v_text;
  goto __pyx_L0;
```

</details>

L385  ⚪  (score=0)
```python
```
L386  🔴  (score=43)
```python
    def colon_action(self, text):
```
<details><summary>Show generated C (score=43)</summary>

```c
/* Python wrapper */
static PyObject *__pyx_pw_6Cython_8Compiler_8Scanning_12PyrexScanner_19colon_action(PyObject *__pyx_self, 
#if CYTHON_METH_FASTCALL
PyObject *const *__pyx_args, Py_ssize_t __pyx_nargs, PyObject *__pyx_kwds
#else
PyObject *__pyx_args, PyObject *__pyx_kwds
#endif
); /*proto*/
PyDoc_STRVAR(__pyx_doc_6Cython_8Compiler_8Scanning_12PyrexScanner_18colon_action, "File: Cython/Compiler/Scanning.py (starting at line 386)");
static PyMethodDef __pyx_mdef_6Cython_8Compiler_8Scanning_12PyrexScanner_19colon_action = {"colon_action", (PyCFunction)(void(*)(void))(__Pyx_PyCFunction_FastCallWithKeywords)__pyx_pw_6Cython_8Compiler_8Scanning_12PyrexScanner_19colon_action, __Pyx_METH_FASTCALL|METH_KEYWORDS, __pyx_doc_6Cython_8Compiler_8Scanning_12PyrexScanner_18colon_action};
static PyObject *__pyx_pw_6Cython_8Compiler_8Scanning_12PyrexScanner_19colon_action(PyObject *__pyx_self, 
#if CYTHON_METH_FASTCALL
PyObject *const *__pyx_args, Py_ssize_t __pyx_nargs, PyObject *__pyx_kwds
#else
PyObject *__pyx_args, PyObject *__pyx_kwds
#endif
) {
  PyObject *__pyx_v_self = 0;
  PyObject *__pyx_v_text = 0;
  #if !CYTHON_METH_FASTCALL
  CYTHON_UNUSED Py_ssize_t __pyx_nargs;
  #endif
  CYTHON_UNUSED PyObject *const *__pyx_kwvalues;
  PyObject *__pyx_r = 0;
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("colon_action (wrapper)", 0);
  #if !CYTHON_METH_FASTCALL
  #if CYTHON_ASSUME_SAFE_SIZE
  __pyx_nargs = PyTuple_GET_SIZE(__pyx_args);
  #else
  __pyx_nargs = PyTuple_Size(__pyx_args); if (unlikely(__pyx_nargs < 0)) return NULL;
  #endif
  #endif
  __pyx_kwvalues = __Pyx_KwValues_FASTCALL(__pyx_args, __pyx_nargs);
  {
    PyObject ** const __pyx_pyargnames[] = {&__pyx_mstate_global->__pyx_n_u_self,&__pyx_mstate_global->__pyx_n_u_text,0};
  PyObject* values[2] = {0,0};
    const Py_ssize_t __pyx_kwds_len = (__pyx_kwds) ? __Pyx_NumKwargs_FASTCALL(__pyx_kwds) : 0;
    if (unlikely(__pyx_kwds_len) < 0) __PYX_ERR(0, 386, __pyx_L3_error)
    if (__pyx_kwds_len > 0) {
      switch (__pyx_nargs) {
        case  2:
        values[1] = __Pyx_ArgRef_FASTCALL(__pyx_args, 1);
        if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[1])) __PYX_ERR(0, 386, __pyx_L3_error)
        CYTHON_FALLTHROUGH;
        case  1:
        values[0] = __Pyx_ArgRef_FASTCALL(__pyx_args, 0);
        if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[0])) __PYX_ERR(0, 386, __pyx_L3_error)
        CYTHON_FALLTHROUGH;
        case  0: break;
        default: goto __pyx_L5_argtuple_error;
      }
      const Py_ssize_t kwd_pos_args = __pyx_nargs;
      if (__Pyx_ParseKeywords(__pyx_kwds, __pyx_kwvalues, __pyx_pyargnames, 0, values, kwd_pos_args, __pyx_kwds_len, "colon_action", 0) < (0)) __PYX_ERR(0, 386, __pyx_L3_error)
      for (Py_ssize_t i = __pyx_nargs; i < 2; i++) {
        if (unlikely(!values[i])) { __Pyx_RaiseArgtupleInvalid("colon_action", 1, 2, 2, i); __PYX_ERR(0, 386, __pyx_L3_error) }
      }
    } else if (unlikely(__pyx_nargs != 2)) {
      goto __pyx_L5_argtuple_error;
    } else {
      values[0] = __Pyx_ArgRef_FASTCALL(__pyx_args, 0);
      if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[0])) __PYX_ERR(0, 386, __pyx_L3_error)
      values[1] = __Pyx_ArgRef_FASTCALL(__pyx_args, 1);
      if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[1])) __PYX_ERR(0, 386, __pyx_L3_error)
    }
    __pyx_v_self = values[0];
    __pyx_v_text = values[1];
  }
  goto __pyx_L6_skip;
  __pyx_L5_argtuple_error:;
  __Pyx_RaiseArgtupleInvalid("colon_action", 1, 2, 2, __pyx_nargs); __PYX_ERR(0, 386, __pyx_L3_error)
  __pyx_L6_skip:;
  goto __pyx_L4_argument_unpacking_done;
  __pyx_L3_error:;
  for (Py_ssize_t __pyx_temp=0; __pyx_temp < (Py_ssize_t)(sizeof(values)/sizeof(values[0])); ++__pyx_temp) {
    Py_XDECREF(values[__pyx_temp]);
  }
  __Pyx_AddTraceback("Cython.Compiler.Scanning.PyrexScanner.colon_action", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __Pyx_RefNannyFinishContext();
  return NULL;
  __pyx_L4_argument_unpacking_done:;
  __pyx_r = __pyx_pf_6Cython_8Compiler_8Scanning_12PyrexScanner_18colon_action(__pyx_self, __pyx_v_self, __pyx_v_text);
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

static PyObject *__pyx_pf_6Cython_8Compiler_8Scanning_12PyrexScanner_18colon_action(CYTHON_UNUSED PyObject *__pyx_self, PyObject *__pyx_v_self, PyObject *__pyx_v_text) {
  PyObject *__pyx_r = NULL;
/* … */
  /* function exit code */
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_t_2);
  __Pyx_XDECREF(__pyx_t_4);
  __Pyx_XDECREF(__pyx_t_5);
  __Pyx_XDECREF(__pyx_t_6);
  __Pyx_AddTraceback("Cython.Compiler.Scanning.PyrexScanner.colon_action", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_r = NULL;
  __pyx_L0:;
  __Pyx_XGIVEREF(__pyx_r);
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}
/* … */
  __pyx_t_9 = __Pyx_CyFunction_New(&__pyx_mdef_6Cython_8Compiler_8Scanning_12PyrexScanner_19colon_action, 0, __pyx_mstate_global->__pyx_n_u_PyrexScanner_colon_action, NULL, __pyx_mstate_global->__pyx_n_u_Cython_Compiler_Scanning, __pyx_mstate_global->__pyx_d, ((PyObject *)__pyx_mstate_global->__pyx_codeobj_tab[44])); if (unlikely(!__pyx_t_9)) __PYX_ERR(0, 386, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_9);
  #if CYTHON_COMPILING_IN_CPYTHON && PY_VERSION_HEX >= 0x030E0000
  PyUnstable_Object_EnableDeferredRefcount(__pyx_t_9);
  #endif
  if (__Pyx_SetNameInClass(__pyx_t_8, __pyx_mstate_global->__pyx_n_u_colon_action, __pyx_t_9) < (0)) __PYX_ERR(0, 386, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_9); __pyx_t_9 = 0;
```

</details>

L387  🟠  (score=5)
```python
        if (self.ft_string_state_stack and
```
<details><summary>Show generated C (score=5)</summary>

```c
  __pyx_t_2 = __Pyx_PyObject_GetAttrStr(__pyx_v_self, __pyx_mstate_global->__pyx_n_u_ft_string_state_stack); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 387, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __pyx_t_3 = __Pyx_PyObject_IsTrue(__pyx_t_2); if (unlikely((__pyx_t_3 < 0))) __PYX_ERR(0, 387, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  if (__pyx_t_3) {
  } else {
    __pyx_t_1 = __pyx_t_3;
    goto __pyx_L4_bool_binop_done;
  }
/* … */
  if (__pyx_t_1) {
/* … */
  }
```

</details>

L388  🔴  (score=22)
```python
                self.ft_string_state_stack[-1].bracket_nesting_level() == self.bracket_nesting_level):
```
<details><summary>Show generated C (score=22)</summary>

```c
  __pyx_t_5 = __Pyx_PyObject_GetAttrStr(__pyx_v_self, __pyx_mstate_global->__pyx_n_u_ft_string_state_stack); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 388, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_5);
  __pyx_t_6 = __Pyx_GetItemInt(__pyx_t_5, -1L, long, 1, __Pyx_PyLong_From_long, 0, 0, 0, 1, __Pyx_ReferenceSharing_OwnStrongReference); if (unlikely(!__pyx_t_6)) __PYX_ERR(0, 388, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_6);
  __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
  __pyx_t_4 = __pyx_t_6;
  __Pyx_INCREF(__pyx_t_4);
  __pyx_t_7 = 0;
  {
    PyObject *__pyx_callargs[2] = {__pyx_t_4, NULL};
    __pyx_t_2 = __Pyx_PyObject_FastCallMethod((PyObject*)__pyx_mstate_global->__pyx_n_u_bracket_nesting_level, __pyx_callargs+__pyx_t_7, (1-__pyx_t_7) | (1*__Pyx_PY_VECTORCALL_ARGUMENTS_OFFSET));
    __Pyx_XDECREF(__pyx_t_4); __pyx_t_4 = 0;
    __Pyx_DECREF(__pyx_t_6); __pyx_t_6 = 0;
    if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 388, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_2);
  }
  __pyx_t_6 = __Pyx_PyObject_GetAttrStr(__pyx_v_self, __pyx_mstate_global->__pyx_n_u_bracket_nesting_level); if (unlikely(!__pyx_t_6)) __PYX_ERR(0, 388, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_6);
  __pyx_t_4 = PyObject_RichCompare(__pyx_t_2, __pyx_t_6, Py_EQ); __Pyx_XGOTREF(__pyx_t_4); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 388, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __Pyx_DECREF(__pyx_t_6); __pyx_t_6 = 0;
  __pyx_t_3 = __Pyx_PyObject_IsTrue(__pyx_t_4); if (unlikely((__pyx_t_3 < 0))) __PYX_ERR(0, 388, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
  __pyx_t_1 = __pyx_t_3;
  __pyx_L4_bool_binop_done:;
```

</details>

L389  🟠  (score=8)
```python
            self.in_ft_string_expr_prescan -= 1
```
<details><summary>Show generated C (score=8)</summary>

```c
    __pyx_t_4 = __Pyx_PyObject_GetAttrStr(__pyx_v_self, __pyx_mstate_global->__pyx_n_u_in_ft_string_expr_prescan); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 389, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_4);
    __pyx_t_6 = __Pyx_PyLong_SubtractObjC(__pyx_t_4, __pyx_mstate_global->__pyx_int_1, 1, 1, 0); if (unlikely(!__pyx_t_6)) __PYX_ERR(0, 389, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_6);
    __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
    if (__Pyx_PyObject_SetAttrStr(__pyx_v_self, __pyx_mstate_global->__pyx_n_u_in_ft_string_expr_prescan, __pyx_t_6) < (0)) __PYX_ERR(0, 389, __pyx_L1_error)
    __Pyx_DECREF(__pyx_t_6); __pyx_t_6 = 0;
```

</details>

L390  🟠  (score=5)
```python
            if self.in_ft_string_expr_prescan == 0:
```
<details><summary>Show generated C (score=5)</summary>

```c
    __pyx_t_6 = __Pyx_PyObject_GetAttrStr(__pyx_v_self, __pyx_mstate_global->__pyx_n_u_in_ft_string_expr_prescan); if (unlikely(!__pyx_t_6)) __PYX_ERR(0, 390, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_6);
    __pyx_t_1 = (__Pyx_PyLong_BoolEqObjC(__pyx_t_6, __pyx_mstate_global->__pyx_int_0, 0, 0)); if (unlikely((__pyx_t_1 < 0))) __PYX_ERR(0, 390, __pyx_L1_error)
    __Pyx_DECREF(__pyx_t_6); __pyx_t_6 = 0;
    if (__pyx_t_1) {
/* … */
    }
```

</details>

L391  🟠  (score=5)
```python
                self.produce("END_FT_STRING_EXPR")
```
<details><summary>Show generated C (score=5)</summary>

```c
      __pyx_t_4 = __pyx_v_self;
      __Pyx_INCREF(__pyx_t_4);
      __pyx_t_7 = 0;
      {
        PyObject *__pyx_callargs[2] = {__pyx_t_4, __pyx_mstate_global->__pyx_n_u_END_FT_STRING_EXPR};
        __pyx_t_6 = __Pyx_PyObject_FastCallMethod((PyObject*)__pyx_mstate_global->__pyx_n_u_produce, __pyx_callargs+__pyx_t_7, (2-__pyx_t_7) | (1*__Pyx_PY_VECTORCALL_ARGUMENTS_OFFSET));
        __Pyx_XDECREF(__pyx_t_4); __pyx_t_4 = 0;
        if (unlikely(!__pyx_t_6)) __PYX_ERR(0, 391, __pyx_L1_error)
        __Pyx_GOTREF(__pyx_t_6);
      }
      __Pyx_DECREF(__pyx_t_6); __pyx_t_6 = 0;
```

</details>

L392  🔴  (score=14)
```python
            self.begin(self.ft_string_state_stack[-1].scanner_state)
```
<details><summary>Show generated C (score=14)</summary>

```c
    __pyx_t_4 = __pyx_v_self;
    __Pyx_INCREF(__pyx_t_4);
    __pyx_t_2 = __Pyx_PyObject_GetAttrStr(__pyx_v_self, __pyx_mstate_global->__pyx_n_u_ft_string_state_stack); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 392, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_2);
    __pyx_t_5 = __Pyx_GetItemInt(__pyx_t_2, -1L, long, 1, __Pyx_PyLong_From_long, 0, 0, 0, 1, __Pyx_ReferenceSharing_OwnStrongReference); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 392, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_5);
    __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
    __pyx_t_2 = __Pyx_PyObject_GetAttrStr(__pyx_t_5, __pyx_mstate_global->__pyx_n_u_scanner_state); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 392, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_2);
    __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
    __pyx_t_7 = 0;
    {
      PyObject *__pyx_callargs[2] = {__pyx_t_4, __pyx_t_2};
      __pyx_t_6 = __Pyx_PyObject_FastCallMethod((PyObject*)__pyx_mstate_global->__pyx_n_u_begin, __pyx_callargs+__pyx_t_7, (2-__pyx_t_7) | (1*__Pyx_PY_VECTORCALL_ARGUMENTS_OFFSET));
      __Pyx_XDECREF(__pyx_t_4); __pyx_t_4 = 0;
      __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
      if (unlikely(!__pyx_t_6)) __PYX_ERR(0, 392, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_6);
    }
    __Pyx_DECREF(__pyx_t_6); __pyx_t_6 = 0;
```

</details>

L393  🔴  (score=11)
```python
            self.ft_string_state_stack[-1].set_in_format_specifier()
```
<details><summary>Show generated C (score=11)</summary>

```c
    __pyx_t_4 = __Pyx_PyObject_GetAttrStr(__pyx_v_self, __pyx_mstate_global->__pyx_n_u_ft_string_state_stack); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 393, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_4);
    __pyx_t_5 = __Pyx_GetItemInt(__pyx_t_4, -1L, long, 1, __Pyx_PyLong_From_long, 0, 0, 0, 1, __Pyx_ReferenceSharing_OwnStrongReference); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 393, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_5);
    __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
    __pyx_t_2 = __pyx_t_5;
    __Pyx_INCREF(__pyx_t_2);
    __pyx_t_7 = 0;
    {
      PyObject *__pyx_callargs[2] = {__pyx_t_2, NULL};
      __pyx_t_6 = __Pyx_PyObject_FastCallMethod((PyObject*)__pyx_mstate_global->__pyx_n_u_set_in_format_specifier, __pyx_callargs+__pyx_t_7, (1-__pyx_t_7) | (1*__Pyx_PY_VECTORCALL_ARGUMENTS_OFFSET));
      __Pyx_XDECREF(__pyx_t_2); __pyx_t_2 = 0;
      __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
      if (unlikely(!__pyx_t_6)) __PYX_ERR(0, 393, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_6);
    }
    __Pyx_DECREF(__pyx_t_6); __pyx_t_6 = 0;
```

</details>

L394  🟡  (score=2)
```python
        return text
```
<details><summary>Show generated C (score=2)</summary>

```c
  __Pyx_XDECREF(__pyx_r);
  __Pyx_INCREF(__pyx_v_text);
  __pyx_r = __pyx_v_text;
  goto __pyx_L0;
```

</details>

L395  ⚪  (score=0)
```python
```
L396  🔴  (score=42)
```python
    def newline_action(self, text):
```
<details><summary>Show generated C (score=42)</summary>

```c
/* Python wrapper */
static PyObject *__pyx_pw_6Cython_8Compiler_8Scanning_12PyrexScanner_21newline_action(PyObject *__pyx_self, 
#if CYTHON_METH_FASTCALL
PyObject *const *__pyx_args, Py_ssize_t __pyx_nargs, PyObject *__pyx_kwds
#else
PyObject *__pyx_args, PyObject *__pyx_kwds
#endif
); /*proto*/
PyDoc_STRVAR(__pyx_doc_6Cython_8Compiler_8Scanning_12PyrexScanner_20newline_action, "File: Cython/Compiler/Scanning.py (starting at line 396)");
static PyMethodDef __pyx_mdef_6Cython_8Compiler_8Scanning_12PyrexScanner_21newline_action = {"newline_action", (PyCFunction)(void(*)(void))(__Pyx_PyCFunction_FastCallWithKeywords)__pyx_pw_6Cython_8Compiler_8Scanning_12PyrexScanner_21newline_action, __Pyx_METH_FASTCALL|METH_KEYWORDS, __pyx_doc_6Cython_8Compiler_8Scanning_12PyrexScanner_20newline_action};
static PyObject *__pyx_pw_6Cython_8Compiler_8Scanning_12PyrexScanner_21newline_action(PyObject *__pyx_self, 
#if CYTHON_METH_FASTCALL
PyObject *const *__pyx_args, Py_ssize_t __pyx_nargs, PyObject *__pyx_kwds
#else
PyObject *__pyx_args, PyObject *__pyx_kwds
#endif
) {
  PyObject *__pyx_v_self = 0;
  CYTHON_UNUSED PyObject *__pyx_v_text = 0;
  #if !CYTHON_METH_FASTCALL
  CYTHON_UNUSED Py_ssize_t __pyx_nargs;
  #endif
  CYTHON_UNUSED PyObject *const *__pyx_kwvalues;
  PyObject *__pyx_r = 0;
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("newline_action (wrapper)", 0);
  #if !CYTHON_METH_FASTCALL
  #if CYTHON_ASSUME_SAFE_SIZE
  __pyx_nargs = PyTuple_GET_SIZE(__pyx_args);
  #else
  __pyx_nargs = PyTuple_Size(__pyx_args); if (unlikely(__pyx_nargs < 0)) return NULL;
  #endif
  #endif
  __pyx_kwvalues = __Pyx_KwValues_FASTCALL(__pyx_args, __pyx_nargs);
  {
    PyObject ** const __pyx_pyargnames[] = {&__pyx_mstate_global->__pyx_n_u_self,&__pyx_mstate_global->__pyx_n_u_text,0};
  PyObject* values[2] = {0,0};
    const Py_ssize_t __pyx_kwds_len = (__pyx_kwds) ? __Pyx_NumKwargs_FASTCALL(__pyx_kwds) : 0;
    if (unlikely(__pyx_kwds_len) < 0) __PYX_ERR(0, 396, __pyx_L3_error)
    if (__pyx_kwds_len > 0) {
      switch (__pyx_nargs) {
        case  2:
        values[1] = __Pyx_ArgRef_FASTCALL(__pyx_args, 1);
        if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[1])) __PYX_ERR(0, 396, __pyx_L3_error)
        CYTHON_FALLTHROUGH;
        case  1:
        values[0] = __Pyx_ArgRef_FASTCALL(__pyx_args, 0);
        if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[0])) __PYX_ERR(0, 396, __pyx_L3_error)
        CYTHON_FALLTHROUGH;
        case  0: break;
        default: goto __pyx_L5_argtuple_error;
      }
      const Py_ssize_t kwd_pos_args = __pyx_nargs;
      if (__Pyx_ParseKeywords(__pyx_kwds, __pyx_kwvalues, __pyx_pyargnames, 0, values, kwd_pos_args, __pyx_kwds_len, "newline_action", 0) < (0)) __PYX_ERR(0, 396, __pyx_L3_error)
      for (Py_ssize_t i = __pyx_nargs; i < 2; i++) {
        if (unlikely(!values[i])) { __Pyx_RaiseArgtupleInvalid("newline_action", 1, 2, 2, i); __PYX_ERR(0, 396, __pyx_L3_error) }
      }
    } else if (unlikely(__pyx_nargs != 2)) {
      goto __pyx_L5_argtuple_error;
    } else {
      values[0] = __Pyx_ArgRef_FASTCALL(__pyx_args, 0);
      if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[0])) __PYX_ERR(0, 396, __pyx_L3_error)
      values[1] = __Pyx_ArgRef_FASTCALL(__pyx_args, 1);
      if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[1])) __PYX_ERR(0, 396, __pyx_L3_error)
    }
    __pyx_v_self = values[0];
    __pyx_v_text = values[1];
  }
  goto __pyx_L6_skip;
  __pyx_L5_argtuple_error:;
  __Pyx_RaiseArgtupleInvalid("newline_action", 1, 2, 2, __pyx_nargs); __PYX_ERR(0, 396, __pyx_L3_error)
  __pyx_L6_skip:;
  goto __pyx_L4_argument_unpacking_done;
  __pyx_L3_error:;
  for (Py_ssize_t __pyx_temp=0; __pyx_temp < (Py_ssize_t)(sizeof(values)/sizeof(values[0])); ++__pyx_temp) {
    Py_XDECREF(values[__pyx_temp]);
  }
  __Pyx_AddTraceback("Cython.Compiler.Scanning.PyrexScanner.newline_action", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __Pyx_RefNannyFinishContext();
  return NULL;
  __pyx_L4_argument_unpacking_done:;
  __pyx_r = __pyx_pf_6Cython_8Compiler_8Scanning_12PyrexScanner_20newline_action(__pyx_self, __pyx_v_self, __pyx_v_text);
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

static PyObject *__pyx_pf_6Cython_8Compiler_8Scanning_12PyrexScanner_20newline_action(CYTHON_UNUSED PyObject *__pyx_self, PyObject *__pyx_v_self, CYTHON_UNUSED PyObject *__pyx_v_text) {
  PyObject *__pyx_r = NULL;
/* … */
  /* function exit code */
  __pyx_r = Py_None; __Pyx_INCREF(Py_None);
  goto __pyx_L0;
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_t_1);
  __Pyx_XDECREF(__pyx_t_3);
  __Pyx_AddTraceback("Cython.Compiler.Scanning.PyrexScanner.newline_action", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_r = NULL;
  __pyx_L0:;
  __Pyx_XGIVEREF(__pyx_r);
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}
/* … */
  __pyx_t_9 = __Pyx_CyFunction_New(&__pyx_mdef_6Cython_8Compiler_8Scanning_12PyrexScanner_21newline_action, 0, __pyx_mstate_global->__pyx_n_u_PyrexScanner_newline_action, NULL, __pyx_mstate_global->__pyx_n_u_Cython_Compiler_Scanning, __pyx_mstate_global->__pyx_d, ((PyObject *)__pyx_mstate_global->__pyx_codeobj_tab[45])); if (unlikely(!__pyx_t_9)) __PYX_ERR(0, 396, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_9);
  #if CYTHON_COMPILING_IN_CPYTHON && PY_VERSION_HEX >= 0x030E0000
  PyUnstable_Object_EnableDeferredRefcount(__pyx_t_9);
  #endif
  if (__Pyx_SetNameInClass(__pyx_t_8, __pyx_mstate_global->__pyx_n_u_newline_action, __pyx_t_9) < (0)) __PYX_ERR(0, 396, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_9); __pyx_t_9 = 0;
```

</details>

L397  🟠  (score=5)
```python
        if self.bracket_nesting_level == 0:
```
<details><summary>Show generated C (score=5)</summary>

```c
  __pyx_t_1 = __Pyx_PyObject_GetAttrStr(__pyx_v_self, __pyx_mstate_global->__pyx_n_u_bracket_nesting_level); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 397, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __pyx_t_2 = (__Pyx_PyLong_BoolEqObjC(__pyx_t_1, __pyx_mstate_global->__pyx_int_0, 0, 0)); if (unlikely((__pyx_t_2 < 0))) __PYX_ERR(0, 397, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  if (__pyx_t_2) {
/* … */
  }
```

</details>

L398  🟠  (score=5)
```python
            self.begin('INDENT')
```
<details><summary>Show generated C (score=5)</summary>

```c
    __pyx_t_3 = __pyx_v_self;
    __Pyx_INCREF(__pyx_t_3);
    __pyx_t_4 = 0;
    {
      PyObject *__pyx_callargs[2] = {__pyx_t_3, __pyx_mstate_global->__pyx_n_u_INDENT};
      __pyx_t_1 = __Pyx_PyObject_FastCallMethod((PyObject*)__pyx_mstate_global->__pyx_n_u_begin, __pyx_callargs+__pyx_t_4, (2-__pyx_t_4) | (1*__Pyx_PY_VECTORCALL_ARGUMENTS_OFFSET));
      __Pyx_XDECREF(__pyx_t_3); __pyx_t_3 = 0;
      if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 398, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_1);
    }
    __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
```

</details>

L399  🔴  (score=11)
```python
            self.produce('NEWLINE', '')
```
<details><summary>Show generated C (score=11)</summary>

```c
    __pyx_t_1 = __Pyx_PyObject_GetAttrStr(__pyx_v_self, __pyx_mstate_global->__pyx_n_u_produce); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 399, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_1);
    __pyx_t_3 = __Pyx_PyObject_Call(__pyx_t_1, __pyx_mstate_global->__pyx_tuple[5], NULL); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 399, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_3);
    __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
    __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
/* … */
  __pyx_mstate_global->__pyx_tuple[5] = PyTuple_Pack(2, __pyx_mstate_global->__pyx_n_u_NEWLINE, __pyx_mstate_global->__pyx_kp_u__6); if (unlikely(!__pyx_mstate_global->__pyx_tuple[5])) __PYX_ERR(0, 399, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_mstate_global->__pyx_tuple[5]);
  __Pyx_GIVEREF(__pyx_mstate_global->__pyx_tuple[5]);
```

</details>

L400  ⚪  (score=0)
```python
```
L401  ⚪  (score=0)
```python
    string_states = {
```
L402  🔴  (score=105)
```python
        "'":   'SQ_STRING',
```
<details><summary>Show generated C (score=105)</summary>

```c
  __pyx_t_9 = __Pyx_PyDict_NewPresized(4); if (unlikely(!__pyx_t_9)) __PYX_ERR(0, 402, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_9);
  #if defined(PyDict_SetItem) && (defined(CYTHON_COMPILING_IN_CPYTHON))
  #if PY_VERSION_HEX >= 0x030A0000 /* CPython 3.10+ exposes KnownHash APIs */
  /* Use CPython's KnownHash APIs when available */
  extern int _PyDict_SetItem_KnownHash(PyObject*, PyObject*, PyObject*, Py_hash_t);
  {
    Py_hash_t __pyx_hash = PyObject_Hash(__pyx_mstate_global->__pyx_kp_u__10); if (unlikely(__pyx_hash == -1)) __PYX_ERR(0, 402, __pyx_L1_error);
    if (unlikely(_PyDict_SetItem_KnownHash(__pyx_t_9, __pyx_mstate_global->__pyx_kp_u__10, __pyx_mstate_global->__pyx_n_u_SQ_STRING, __pyx_hash) < 0)) __PYX_ERR(0, 402, __pyx_L1_error);
  }
  #else
  if (PyDict_SetItem(__pyx_t_9, __pyx_mstate_global->__pyx_kp_u__10, __pyx_mstate_global->__pyx_n_u_SQ_STRING) < (0)) __PYX_ERR(0, 402, __pyx_L1_error)
  #endif
  #else
  if (PyDict_SetItem(__pyx_t_9, __pyx_mstate_global->__pyx_kp_u__10, __pyx_mstate_global->__pyx_n_u_SQ_STRING) < (0)) __PYX_ERR(0, 402, __pyx_L1_error)
  #endif
  #if defined(PyDict_SetItem) && (defined(CYTHON_COMPILING_IN_CPYTHON))
  #if PY_VERSION_HEX >= 0x030A0000 /* CPython 3.10+ exposes KnownHash APIs */
  /* Use CPython's KnownHash APIs when available */
  extern int _PyDict_SetItem_KnownHash(PyObject*, PyObject*, PyObject*, Py_hash_t);
  {
    Py_hash_t __pyx_hash = PyObject_Hash(__pyx_mstate_global->__pyx_kp_u__12); if (unlikely(__pyx_hash == -1)) __PYX_ERR(0, 402, __pyx_L1_error);
    if (unlikely(_PyDict_SetItem_KnownHash(__pyx_t_9, __pyx_mstate_global->__pyx_kp_u__12, __pyx_mstate_global->__pyx_n_u_DQ_STRING, __pyx_hash) < 0)) __PYX_ERR(0, 402, __pyx_L1_error);
  }
  #else
  if (PyDict_SetItem(__pyx_t_9, __pyx_mstate_global->__pyx_kp_u__12, __pyx_mstate_global->__pyx_n_u_DQ_STRING) < (0)) __PYX_ERR(0, 402, __pyx_L1_error)
  #endif
  #else
  if (PyDict_SetItem(__pyx_t_9, __pyx_mstate_global->__pyx_kp_u__12, __pyx_mstate_global->__pyx_n_u_DQ_STRING) < (0)) __PYX_ERR(0, 402, __pyx_L1_error)
  #endif
  #if defined(PyDict_SetItem) && (defined(CYTHON_COMPILING_IN_CPYTHON))
  #if PY_VERSION_HEX >= 0x030A0000 /* CPython 3.10+ exposes KnownHash APIs */
  /* Use CPython's KnownHash APIs when available */
  extern int _PyDict_SetItem_KnownHash(PyObject*, PyObject*, PyObject*, Py_hash_t);
  {
    Py_hash_t __pyx_hash = PyObject_Hash(__pyx_mstate_global->__pyx_kp_u__13); if (unlikely(__pyx_hash == -1)) __PYX_ERR(0, 402, __pyx_L1_error);
    if (unlikely(_PyDict_SetItem_KnownHash(__pyx_t_9, __pyx_mstate_global->__pyx_kp_u__13, __pyx_mstate_global->__pyx_n_u_TSQ_STRING, __pyx_hash) < 0)) __PYX_ERR(0, 402, __pyx_L1_error);
  }
  #else
  if (PyDict_SetItem(__pyx_t_9, __pyx_mstate_global->__pyx_kp_u__13, __pyx_mstate_global->__pyx_n_u_TSQ_STRING) < (0)) __PYX_ERR(0, 402, __pyx_L1_error)
  #endif
  #else
  if (PyDict_SetItem(__pyx_t_9, __pyx_mstate_global->__pyx_kp_u__13, __pyx_mstate_global->__pyx_n_u_TSQ_STRING) < (0)) __PYX_ERR(0, 402, __pyx_L1_error)
  #endif
  #if defined(PyDict_SetItem) && (defined(CYTHON_COMPILING_IN_CPYTHON))
  #if PY_VERSION_HEX >= 0x030A0000 /* CPython 3.10+ exposes KnownHash APIs */
  /* Use CPython's KnownHash APIs when available */
  extern int _PyDict_SetItem_KnownHash(PyObject*, PyObject*, PyObject*, Py_hash_t);
  {
    Py_hash_t __pyx_hash = PyObject_Hash(__pyx_mstate_global->__pyx_kp_u__14); if (unlikely(__pyx_hash == -1)) __PYX_ERR(0, 402, __pyx_L1_error);
    if (unlikely(_PyDict_SetItem_KnownHash(__pyx_t_9, __pyx_mstate_global->__pyx_kp_u__14, __pyx_mstate_global->__pyx_n_u_TDQ_STRING, __pyx_hash) < 0)) __PYX_ERR(0, 402, __pyx_L1_error);
  }
  #else
  if (PyDict_SetItem(__pyx_t_9, __pyx_mstate_global->__pyx_kp_u__14, __pyx_mstate_global->__pyx_n_u_TDQ_STRING) < (0)) __PYX_ERR(0, 402, __pyx_L1_error)
  #endif
  #else
  if (PyDict_SetItem(__pyx_t_9, __pyx_mstate_global->__pyx_kp_u__14, __pyx_mstate_global->__pyx_n_u_TDQ_STRING) < (0)) __PYX_ERR(0, 402, __pyx_L1_error)
  #endif
  if (__Pyx_SetNameInClass(__pyx_t_8, __pyx_mstate_global->__pyx_n_u_string_states, __pyx_t_9) < (0)) __PYX_ERR(0, 401, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_9); __pyx_t_9 = 0;
```

</details>

L403  ⚪  (score=0)
```python
        '"':   'DQ_STRING',
```
L404  ⚪  (score=0)
```python
        "'''": 'TSQ_STRING',
```
L405  ⚪  (score=0)
```python
        '"""': 'TDQ_STRING'
```
L406  ⚪  (score=0)
```python
    }
```
L407  ⚪  (score=0)
```python
```
L408  🔴  (score=78)
```python
    def begin_string_action(self, text: str):
```
<details><summary>Show generated C (score=78)</summary>

```c
/* Python wrapper */
static PyObject *__pyx_pw_6Cython_8Compiler_8Scanning_12PyrexScanner_23begin_string_action(PyObject *__pyx_self, 
#if CYTHON_METH_FASTCALL
PyObject *const *__pyx_args, Py_ssize_t __pyx_nargs, PyObject *__pyx_kwds
#else
PyObject *__pyx_args, PyObject *__pyx_kwds
#endif
); /*proto*/
PyDoc_STRVAR(__pyx_doc_6Cython_8Compiler_8Scanning_12PyrexScanner_22begin_string_action, "File: Cython/Compiler/Scanning.py (starting at line 408)");
static PyMethodDef __pyx_mdef_6Cython_8Compiler_8Scanning_12PyrexScanner_23begin_string_action = {"begin_string_action", (PyCFunction)(void(*)(void))(__Pyx_PyCFunction_FastCallWithKeywords)__pyx_pw_6Cython_8Compiler_8Scanning_12PyrexScanner_23begin_string_action, __Pyx_METH_FASTCALL|METH_KEYWORDS, __pyx_doc_6Cython_8Compiler_8Scanning_12PyrexScanner_22begin_string_action};
static PyObject *__pyx_pw_6Cython_8Compiler_8Scanning_12PyrexScanner_23begin_string_action(PyObject *__pyx_self, 
#if CYTHON_METH_FASTCALL
PyObject *const *__pyx_args, Py_ssize_t __pyx_nargs, PyObject *__pyx_kwds
#else
PyObject *__pyx_args, PyObject *__pyx_kwds
#endif
) {
  PyObject *__pyx_v_self = 0;
  PyObject *__pyx_v_text = 0;
  #if !CYTHON_METH_FASTCALL
  CYTHON_UNUSED Py_ssize_t __pyx_nargs;
  #endif
  CYTHON_UNUSED PyObject *const *__pyx_kwvalues;
  PyObject *__pyx_r = 0;
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("begin_string_action (wrapper)", 0);
  #if !CYTHON_METH_FASTCALL
  #if CYTHON_ASSUME_SAFE_SIZE
  __pyx_nargs = PyTuple_GET_SIZE(__pyx_args);
  #else
  __pyx_nargs = PyTuple_Size(__pyx_args); if (unlikely(__pyx_nargs < 0)) return NULL;
  #endif
  #endif
  __pyx_kwvalues = __Pyx_KwValues_FASTCALL(__pyx_args, __pyx_nargs);
  {
    PyObject ** const __pyx_pyargnames[] = {&__pyx_mstate_global->__pyx_n_u_self,&__pyx_mstate_global->__pyx_n_u_text,0};
  PyObject* values[2] = {0,0};
    const Py_ssize_t __pyx_kwds_len = (__pyx_kwds) ? __Pyx_NumKwargs_FASTCALL(__pyx_kwds) : 0;
    if (unlikely(__pyx_kwds_len) < 0) __PYX_ERR(0, 408, __pyx_L3_error)
    if (__pyx_kwds_len > 0) {
      switch (__pyx_nargs) {
        case  2:
        values[1] = __Pyx_ArgRef_FASTCALL(__pyx_args, 1);
        if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[1])) __PYX_ERR(0, 408, __pyx_L3_error)
        CYTHON_FALLTHROUGH;
        case  1:
        values[0] = __Pyx_ArgRef_FASTCALL(__pyx_args, 0);
        if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[0])) __PYX_ERR(0, 408, __pyx_L3_error)
        CYTHON_FALLTHROUGH;
        case  0: break;
        default: goto __pyx_L5_argtuple_error;
      }
      const Py_ssize_t kwd_pos_args = __pyx_nargs;
      if (__Pyx_ParseKeywords(__pyx_kwds, __pyx_kwvalues, __pyx_pyargnames, 0, values, kwd_pos_args, __pyx_kwds_len, "begin_string_action", 0) < (0)) __PYX_ERR(0, 408, __pyx_L3_error)
      for (Py_ssize_t i = __pyx_nargs; i < 2; i++) {
        if (unlikely(!values[i])) { __Pyx_RaiseArgtupleInvalid("begin_string_action", 1, 2, 2, i); __PYX_ERR(0, 408, __pyx_L3_error) }
      }
    } else if (unlikely(__pyx_nargs != 2)) {
      goto __pyx_L5_argtuple_error;
    } else {
      values[0] = __Pyx_ArgRef_FASTCALL(__pyx_args, 0);
      if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[0])) __PYX_ERR(0, 408, __pyx_L3_error)
      values[1] = __Pyx_ArgRef_FASTCALL(__pyx_args, 1);
      if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[1])) __PYX_ERR(0, 408, __pyx_L3_error)
    }
    __pyx_v_self = values[0];
    __pyx_v_text = ((PyObject*)values[1]);
  }
  goto __pyx_L6_skip;
  __pyx_L5_argtuple_error:;
  __Pyx_RaiseArgtupleInvalid("begin_string_action", 1, 2, 2, __pyx_nargs); __PYX_ERR(0, 408, __pyx_L3_error)
  __pyx_L6_skip:;
  goto __pyx_L4_argument_unpacking_done;
  __pyx_L3_error:;
  for (Py_ssize_t __pyx_temp=0; __pyx_temp < (Py_ssize_t)(sizeof(values)/sizeof(values[0])); ++__pyx_temp) {
    Py_XDECREF(values[__pyx_temp]);
  }
  __Pyx_AddTraceback("Cython.Compiler.Scanning.PyrexScanner.begin_string_action", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __Pyx_RefNannyFinishContext();
  return NULL;
  __pyx_L4_argument_unpacking_done:;
  if (unlikely(!__Pyx_ArgTypeTest(((PyObject *)__pyx_v_text), (&PyUnicode_Type), 0, "text", 2))) __PYX_ERR(0, 408, __pyx_L1_error)
  __pyx_r = __pyx_pf_6Cython_8Compiler_8Scanning_12PyrexScanner_22begin_string_action(__pyx_self, __pyx_v_self, __pyx_v_text);
  int __pyx_lineno = 0;
  const char *__pyx_filename = NULL;
  int __pyx_clineno = 0;

  /* function exit code */
  goto __pyx_L0;
  __pyx_L1_error:;
  __pyx_r = NULL;
  for (Py_ssize_t __pyx_temp=0; __pyx_temp < (Py_ssize_t)(sizeof(values)/sizeof(values[0])); ++__pyx_temp) {
    Py_XDECREF(values[__pyx_temp]);
  }
  goto __pyx_L7_cleaned_up;
  __pyx_L0:;
  for (Py_ssize_t __pyx_temp=0; __pyx_temp < (Py_ssize_t)(sizeof(values)/sizeof(values[0])); ++__pyx_temp) {
    Py_XDECREF(values[__pyx_temp]);
  }
  __pyx_L7_cleaned_up:;
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}

static PyObject *__pyx_pf_6Cython_8Compiler_8Scanning_12PyrexScanner_22begin_string_action(CYTHON_UNUSED PyObject *__pyx_self, PyObject *__pyx_v_self, PyObject *__pyx_v_text) {
  PyObject *__pyx_r = NULL;
  __Pyx_INCREF(__pyx_v_text);
/* … */
  /* function exit code */
  __pyx_r = Py_None; __Pyx_INCREF(Py_None);
  goto __pyx_L0;
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_t_4);
  __Pyx_XDECREF(__pyx_t_5);
  __Pyx_XDECREF(__pyx_t_6);
  __Pyx_XDECREF(__pyx_t_7);
  __Pyx_AddTraceback("Cython.Compiler.Scanning.PyrexScanner.begin_string_action", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_r = NULL;
  __pyx_L0:;
  __Pyx_XDECREF(__pyx_v_text);
  __Pyx_XGIVEREF(__pyx_r);
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}
/* … */
  __pyx_t_9 = __Pyx_PyDict_NewPresized(1); if (unlikely(!__pyx_t_9)) __PYX_ERR(0, 408, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_9);
  #if defined(PyDict_SetItem) && (defined(CYTHON_COMPILING_IN_CPYTHON))
  #if PY_VERSION_HEX >= 0x030A0000 /* CPython 3.10+ exposes KnownHash APIs */
  /* Use CPython's KnownHash APIs when available */
  extern int _PyDict_SetItem_KnownHash(PyObject*, PyObject*, PyObject*, Py_hash_t);
  {
    Py_hash_t __pyx_hash = PyObject_Hash(__pyx_mstate_global->__pyx_n_u_text); if (unlikely(__pyx_hash == -1)) __PYX_ERR(0, 408, __pyx_L1_error);
    if (unlikely(_PyDict_SetItem_KnownHash(__pyx_t_9, __pyx_mstate_global->__pyx_n_u_text, __pyx_mstate_global->__pyx_n_u_str, __pyx_hash) < 0)) __PYX_ERR(0, 408, __pyx_L1_error);
  }
  #else
  if (PyDict_SetItem(__pyx_t_9, __pyx_mstate_global->__pyx_n_u_text, __pyx_mstate_global->__pyx_n_u_str) < (0)) __PYX_ERR(0, 408, __pyx_L1_error)
  #endif
  #else
  if (PyDict_SetItem(__pyx_t_9, __pyx_mstate_global->__pyx_n_u_text, __pyx_mstate_global->__pyx_n_u_str) < (0)) __PYX_ERR(0, 408, __pyx_L1_error)
  #endif
  __pyx_t_7 = __Pyx_CyFunction_New(&__pyx_mdef_6Cython_8Compiler_8Scanning_12PyrexScanner_23begin_string_action, 0, __pyx_mstate_global->__pyx_n_u_PyrexScanner_begin_string_action, NULL, __pyx_mstate_global->__pyx_n_u_Cython_Compiler_Scanning, __pyx_mstate_global->__pyx_d, ((PyObject *)__pyx_mstate_global->__pyx_codeobj_tab[46])); if (unlikely(!__pyx_t_7)) __PYX_ERR(0, 408, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_7);
  #if CYTHON_COMPILING_IN_CPYTHON && PY_VERSION_HEX >= 0x030E0000
  PyUnstable_Object_EnableDeferredRefcount(__pyx_t_7);
  #endif
  __Pyx_CyFunction_SetAnnotationsDict(__pyx_t_7, __pyx_t_9);
  __Pyx_DECREF(__pyx_t_9); __pyx_t_9 = 0;
  if (__Pyx_SetNameInClass(__pyx_t_8, __pyx_mstate_global->__pyx_n_u_begin_string_action, __pyx_t_7) < (0)) __PYX_ERR(0, 408, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_7); __pyx_t_7 = 0;
```

</details>

L409  🔴  (score=12)
```python
        while text and text[0] in any_string_prefix:
```
<details><summary>Show generated C (score=12)</summary>

```c
  while (1) {
    {
      Py_ssize_t __pyx_temp = __Pyx_PyUnicode_IS_TRUE(__pyx_v_text);
      if (unlikely(((!CYTHON_ASSUME_SAFE_SIZE) && __pyx_temp < 0))) __PYX_ERR(0, 409, __pyx_L1_error)
      __pyx_t_2 = (__pyx_temp != 0);
    }

    if (__pyx_t_2) {
    } else {
      __pyx_t_1 = __pyx_t_2;
      goto __pyx_L5_bool_binop_done;
    }
    __pyx_t_3 = __Pyx_GetItemInt_Unicode(__pyx_v_text, 0, long, 1, __Pyx_PyLong_From_long, 0, 0, 0, 1, __Pyx_ReferenceSharing_FunctionArgument); if (unlikely(__pyx_t_3 == (Py_UCS4)-1)) __PYX_ERR(0, 409, __pyx_L1_error)
    __pyx_t_4 = __Pyx_PyUnicode_FromOrdinal(__pyx_t_3); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 409, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_4);
    __Pyx_GetModuleGlobalName(__pyx_t_5, __pyx_mstate_global->__pyx_n_u_any_string_prefix); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 409, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_5);
    __pyx_t_2 = (__Pyx_PySequence_ContainsTF(__pyx_t_4, __pyx_t_5, Py_EQ)); if (unlikely((__pyx_t_2 < 0))) __PYX_ERR(0, 409, __pyx_L1_error)
    __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
    __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
    __pyx_t_1 = __pyx_t_2;
    __pyx_L5_bool_binop_done:;
    if (!__pyx_t_1) break;
```

</details>

L410  🟡  (score=3)
```python
            text = text[1:]
```
<details><summary>Show generated C (score=3)</summary>

```c
    __pyx_t_5 = __Pyx_PyUnicode_Substring(__pyx_v_text, 1, PY_SSIZE_T_MAX); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 410, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_5);
    __Pyx_DECREF_SET(__pyx_v_text, ((PyObject*)__pyx_t_5));
    __pyx_t_5 = 0;
  }
```

</details>

L411  🔴  (score=11)
```python
        self.begin(self.string_states[text])
```
<details><summary>Show generated C (score=11)</summary>

```c
  __pyx_t_4 = __pyx_v_self;
  __Pyx_INCREF(__pyx_t_4);
  __pyx_t_6 = __Pyx_PyObject_GetAttrStr(__pyx_v_self, __pyx_mstate_global->__pyx_n_u_string_states); if (unlikely(!__pyx_t_6)) __PYX_ERR(0, 411, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_6);
  __pyx_t_7 = __Pyx_PyObject_Dict_GetItem(__pyx_t_6, __pyx_v_text); if (unlikely(!__pyx_t_7)) __PYX_ERR(0, 411, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_7);
  __Pyx_DECREF(__pyx_t_6); __pyx_t_6 = 0;
  __pyx_t_8 = 0;
  {
    PyObject *__pyx_callargs[2] = {__pyx_t_4, __pyx_t_7};
    __pyx_t_5 = __Pyx_PyObject_FastCallMethod((PyObject*)__pyx_mstate_global->__pyx_n_u_begin, __pyx_callargs+__pyx_t_8, (2-__pyx_t_8) | (1*__Pyx_PY_VECTORCALL_ARGUMENTS_OFFSET));
    __Pyx_XDECREF(__pyx_t_4); __pyx_t_4 = 0;
    __Pyx_DECREF(__pyx_t_7); __pyx_t_7 = 0;
    if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 411, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_5);
  }
  __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
```

</details>

L412  🟠  (score=5)
```python
        self.produce('BEGIN_STRING')
```
<details><summary>Show generated C (score=5)</summary>

```c
  __pyx_t_7 = __pyx_v_self;
  __Pyx_INCREF(__pyx_t_7);
  __pyx_t_8 = 0;
  {
    PyObject *__pyx_callargs[2] = {__pyx_t_7, __pyx_mstate_global->__pyx_n_u_BEGIN_STRING};
    __pyx_t_5 = __Pyx_PyObject_FastCallMethod((PyObject*)__pyx_mstate_global->__pyx_n_u_produce, __pyx_callargs+__pyx_t_8, (2-__pyx_t_8) | (1*__Pyx_PY_VECTORCALL_ARGUMENTS_OFFSET));
    __Pyx_XDECREF(__pyx_t_7); __pyx_t_7 = 0;
    if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 412, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_5);
  }
  __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
```

</details>

L413  ⚪  (score=0)
```python
```
L414  🔴  (score=44)
```python
    def end_string_action(self, text):
```
<details><summary>Show generated C (score=44)</summary>

```c
/* Python wrapper */
static PyObject *__pyx_pw_6Cython_8Compiler_8Scanning_12PyrexScanner_25end_string_action(PyObject *__pyx_self, 
#if CYTHON_METH_FASTCALL
PyObject *const *__pyx_args, Py_ssize_t __pyx_nargs, PyObject *__pyx_kwds
#else
PyObject *__pyx_args, PyObject *__pyx_kwds
#endif
); /*proto*/
PyDoc_STRVAR(__pyx_doc_6Cython_8Compiler_8Scanning_12PyrexScanner_24end_string_action, "File: Cython/Compiler/Scanning.py (starting at line 414)");
static PyMethodDef __pyx_mdef_6Cython_8Compiler_8Scanning_12PyrexScanner_25end_string_action = {"end_string_action", (PyCFunction)(void(*)(void))(__Pyx_PyCFunction_FastCallWithKeywords)__pyx_pw_6Cython_8Compiler_8Scanning_12PyrexScanner_25end_string_action, __Pyx_METH_FASTCALL|METH_KEYWORDS, __pyx_doc_6Cython_8Compiler_8Scanning_12PyrexScanner_24end_string_action};
static PyObject *__pyx_pw_6Cython_8Compiler_8Scanning_12PyrexScanner_25end_string_action(PyObject *__pyx_self, 
#if CYTHON_METH_FASTCALL
PyObject *const *__pyx_args, Py_ssize_t __pyx_nargs, PyObject *__pyx_kwds
#else
PyObject *__pyx_args, PyObject *__pyx_kwds
#endif
) {
  PyObject *__pyx_v_self = 0;
  CYTHON_UNUSED PyObject *__pyx_v_text = 0;
  #if !CYTHON_METH_FASTCALL
  CYTHON_UNUSED Py_ssize_t __pyx_nargs;
  #endif
  CYTHON_UNUSED PyObject *const *__pyx_kwvalues;
  PyObject *__pyx_r = 0;
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("end_string_action (wrapper)", 0);
  #if !CYTHON_METH_FASTCALL
  #if CYTHON_ASSUME_SAFE_SIZE
  __pyx_nargs = PyTuple_GET_SIZE(__pyx_args);
  #else
  __pyx_nargs = PyTuple_Size(__pyx_args); if (unlikely(__pyx_nargs < 0)) return NULL;
  #endif
  #endif
  __pyx_kwvalues = __Pyx_KwValues_FASTCALL(__pyx_args, __pyx_nargs);
  {
    PyObject ** const __pyx_pyargnames[] = {&__pyx_mstate_global->__pyx_n_u_self,&__pyx_mstate_global->__pyx_n_u_text,0};
  PyObject* values[2] = {0,0};
    const Py_ssize_t __pyx_kwds_len = (__pyx_kwds) ? __Pyx_NumKwargs_FASTCALL(__pyx_kwds) : 0;
    if (unlikely(__pyx_kwds_len) < 0) __PYX_ERR(0, 414, __pyx_L3_error)
    if (__pyx_kwds_len > 0) {
      switch (__pyx_nargs) {
        case  2:
        values[1] = __Pyx_ArgRef_FASTCALL(__pyx_args, 1);
        if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[1])) __PYX_ERR(0, 414, __pyx_L3_error)
        CYTHON_FALLTHROUGH;
        case  1:
        values[0] = __Pyx_ArgRef_FASTCALL(__pyx_args, 0);
        if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[0])) __PYX_ERR(0, 414, __pyx_L3_error)
        CYTHON_FALLTHROUGH;
        case  0: break;
        default: goto __pyx_L5_argtuple_error;
      }
      const Py_ssize_t kwd_pos_args = __pyx_nargs;
      if (__Pyx_ParseKeywords(__pyx_kwds, __pyx_kwvalues, __pyx_pyargnames, 0, values, kwd_pos_args, __pyx_kwds_len, "end_string_action", 0) < (0)) __PYX_ERR(0, 414, __pyx_L3_error)
      for (Py_ssize_t i = __pyx_nargs; i < 2; i++) {
        if (unlikely(!values[i])) { __Pyx_RaiseArgtupleInvalid("end_string_action", 1, 2, 2, i); __PYX_ERR(0, 414, __pyx_L3_error) }
      }
    } else if (unlikely(__pyx_nargs != 2)) {
      goto __pyx_L5_argtuple_error;
    } else {
      values[0] = __Pyx_ArgRef_FASTCALL(__pyx_args, 0);
      if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[0])) __PYX_ERR(0, 414, __pyx_L3_error)
      values[1] = __Pyx_ArgRef_FASTCALL(__pyx_args, 1);
      if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[1])) __PYX_ERR(0, 414, __pyx_L3_error)
    }
    __pyx_v_self = values[0];
    __pyx_v_text = values[1];
  }
  goto __pyx_L6_skip;
  __pyx_L5_argtuple_error:;
  __Pyx_RaiseArgtupleInvalid("end_string_action", 1, 2, 2, __pyx_nargs); __PYX_ERR(0, 414, __pyx_L3_error)
  __pyx_L6_skip:;
  goto __pyx_L4_argument_unpacking_done;
  __pyx_L3_error:;
  for (Py_ssize_t __pyx_temp=0; __pyx_temp < (Py_ssize_t)(sizeof(values)/sizeof(values[0])); ++__pyx_temp) {
    Py_XDECREF(values[__pyx_temp]);
  }
  __Pyx_AddTraceback("Cython.Compiler.Scanning.PyrexScanner.end_string_action", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __Pyx_RefNannyFinishContext();
  return NULL;
  __pyx_L4_argument_unpacking_done:;
  __pyx_r = __pyx_pf_6Cython_8Compiler_8Scanning_12PyrexScanner_24end_string_action(__pyx_self, __pyx_v_self, __pyx_v_text);
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

static PyObject *__pyx_pf_6Cython_8Compiler_8Scanning_12PyrexScanner_24end_string_action(CYTHON_UNUSED PyObject *__pyx_self, PyObject *__pyx_v_self, CYTHON_UNUSED PyObject *__pyx_v_text) {
  PyObject *__pyx_r = NULL;
/* … */
  /* function exit code */
  __pyx_r = Py_None; __Pyx_INCREF(Py_None);
  goto __pyx_L0;
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_t_1);
  __Pyx_XDECREF(__pyx_t_2);
  __Pyx_XDECREF(__pyx_t_3);
  __Pyx_XDECREF(__pyx_t_4);
  __Pyx_AddTraceback("Cython.Compiler.Scanning.PyrexScanner.end_string_action", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_r = NULL;
  __pyx_L0:;
  __Pyx_XGIVEREF(__pyx_r);
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}
/* … */
  __pyx_t_7 = __Pyx_CyFunction_New(&__pyx_mdef_6Cython_8Compiler_8Scanning_12PyrexScanner_25end_string_action, 0, __pyx_mstate_global->__pyx_n_u_PyrexScanner_end_string_action, NULL, __pyx_mstate_global->__pyx_n_u_Cython_Compiler_Scanning, __pyx_mstate_global->__pyx_d, ((PyObject *)__pyx_mstate_global->__pyx_codeobj_tab[47])); if (unlikely(!__pyx_t_7)) __PYX_ERR(0, 414, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_7);
  #if CYTHON_COMPILING_IN_CPYTHON && PY_VERSION_HEX >= 0x030E0000
  PyUnstable_Object_EnableDeferredRefcount(__pyx_t_7);
  #endif
  if (__Pyx_SetNameInClass(__pyx_t_8, __pyx_mstate_global->__pyx_n_u_end_string_action, __pyx_t_7) < (0)) __PYX_ERR(0, 414, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_7); __pyx_t_7 = 0;
```

</details>

L415  🔴  (score=13)
```python
        self.begin('FT_STRING_EXPR_PRESCAN' if self.in_ft_string_expr_prescan else '')
```
<details><summary>Show generated C (score=13)</summary>

```c
  __pyx_t_2 = __pyx_v_self;
  __Pyx_INCREF(__pyx_t_2);
  __pyx_t_4 = __Pyx_PyObject_GetAttrStr(__pyx_v_self, __pyx_mstate_global->__pyx_n_u_in_ft_string_expr_prescan); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 415, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_4);
  __pyx_t_5 = __Pyx_PyObject_IsTrue(__pyx_t_4); if (unlikely((__pyx_t_5 < 0))) __PYX_ERR(0, 415, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
  if (__pyx_t_5) {
    __Pyx_INCREF(__pyx_mstate_global->__pyx_n_u_FT_STRING_EXPR_PRESCAN);
    __pyx_t_3 = __pyx_mstate_global->__pyx_n_u_FT_STRING_EXPR_PRESCAN;
  } else {
    __Pyx_INCREF(__pyx_mstate_global->__pyx_kp_u__6);
    __pyx_t_3 = __pyx_mstate_global->__pyx_kp_u__6;
  }
  __pyx_t_6 = 0;
  {
    PyObject *__pyx_callargs[2] = {__pyx_t_2, __pyx_t_3};
    __pyx_t_1 = __Pyx_PyObject_FastCallMethod((PyObject*)__pyx_mstate_global->__pyx_n_u_begin, __pyx_callargs+__pyx_t_6, (2-__pyx_t_6) | (1*__Pyx_PY_VECTORCALL_ARGUMENTS_OFFSET));
    __Pyx_XDECREF(__pyx_t_2); __pyx_t_2 = 0;
    __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
    if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 415, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_1);
  }
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
```

</details>

L416  🟠  (score=5)
```python
        self.produce('END_STRING')
```
<details><summary>Show generated C (score=5)</summary>

```c
  __pyx_t_3 = __pyx_v_self;
  __Pyx_INCREF(__pyx_t_3);
  __pyx_t_6 = 0;
  {
    PyObject *__pyx_callargs[2] = {__pyx_t_3, __pyx_mstate_global->__pyx_n_u_END_STRING};
    __pyx_t_1 = __Pyx_PyObject_FastCallMethod((PyObject*)__pyx_mstate_global->__pyx_n_u_produce, __pyx_callargs+__pyx_t_6, (2-__pyx_t_6) | (1*__Pyx_PY_VECTORCALL_ARGUMENTS_OFFSET));
    __Pyx_XDECREF(__pyx_t_3); __pyx_t_3 = 0;
    if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 416, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_1);
  }
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
```

</details>

L417  ⚪  (score=0)
```python
```
L418  🔴  (score=48)
```python
    def begin_ft_string_action(self, text):
```
<details><summary>Show generated C (score=48)</summary>

```c
/* Python wrapper */
static PyObject *__pyx_pw_6Cython_8Compiler_8Scanning_12PyrexScanner_27begin_ft_string_action(PyObject *__pyx_self, 
#if CYTHON_METH_FASTCALL
PyObject *const *__pyx_args, Py_ssize_t __pyx_nargs, PyObject *__pyx_kwds
#else
PyObject *__pyx_args, PyObject *__pyx_kwds
#endif
); /*proto*/
PyDoc_STRVAR(__pyx_doc_6Cython_8Compiler_8Scanning_12PyrexScanner_26begin_ft_string_action, "File: Cython/Compiler/Scanning.py (starting at line 418)");
static PyMethodDef __pyx_mdef_6Cython_8Compiler_8Scanning_12PyrexScanner_27begin_ft_string_action = {"begin_ft_string_action", (PyCFunction)(void(*)(void))(__Pyx_PyCFunction_FastCallWithKeywords)__pyx_pw_6Cython_8Compiler_8Scanning_12PyrexScanner_27begin_ft_string_action, __Pyx_METH_FASTCALL|METH_KEYWORDS, __pyx_doc_6Cython_8Compiler_8Scanning_12PyrexScanner_26begin_ft_string_action};
static PyObject *__pyx_pw_6Cython_8Compiler_8Scanning_12PyrexScanner_27begin_ft_string_action(PyObject *__pyx_self, 
#if CYTHON_METH_FASTCALL
PyObject *const *__pyx_args, Py_ssize_t __pyx_nargs, PyObject *__pyx_kwds
#else
PyObject *__pyx_args, PyObject *__pyx_kwds
#endif
) {
  PyObject *__pyx_v_self = 0;
  PyObject *__pyx_v_text = 0;
  #if !CYTHON_METH_FASTCALL
  CYTHON_UNUSED Py_ssize_t __pyx_nargs;
  #endif
  CYTHON_UNUSED PyObject *const *__pyx_kwvalues;
  PyObject *__pyx_r = 0;
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("begin_ft_string_action (wrapper)", 0);
  #if !CYTHON_METH_FASTCALL
  #if CYTHON_ASSUME_SAFE_SIZE
  __pyx_nargs = PyTuple_GET_SIZE(__pyx_args);
  #else
  __pyx_nargs = PyTuple_Size(__pyx_args); if (unlikely(__pyx_nargs < 0)) return NULL;
  #endif
  #endif
  __pyx_kwvalues = __Pyx_KwValues_FASTCALL(__pyx_args, __pyx_nargs);
  {
    PyObject ** const __pyx_pyargnames[] = {&__pyx_mstate_global->__pyx_n_u_self,&__pyx_mstate_global->__pyx_n_u_text,0};
  PyObject* values[2] = {0,0};
    const Py_ssize_t __pyx_kwds_len = (__pyx_kwds) ? __Pyx_NumKwargs_FASTCALL(__pyx_kwds) : 0;
    if (unlikely(__pyx_kwds_len) < 0) __PYX_ERR(0, 418, __pyx_L3_error)
    if (__pyx_kwds_len > 0) {
      switch (__pyx_nargs) {
        case  2:
        values[1] = __Pyx_ArgRef_FASTCALL(__pyx_args, 1);
        if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[1])) __PYX_ERR(0, 418, __pyx_L3_error)
        CYTHON_FALLTHROUGH;
        case  1:
        values[0] = __Pyx_ArgRef_FASTCALL(__pyx_args, 0);
        if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[0])) __PYX_ERR(0, 418, __pyx_L3_error)
        CYTHON_FALLTHROUGH;
        case  0: break;
        default: goto __pyx_L5_argtuple_error;
      }
      const Py_ssize_t kwd_pos_args = __pyx_nargs;
      if (__Pyx_ParseKeywords(__pyx_kwds, __pyx_kwvalues, __pyx_pyargnames, 0, values, kwd_pos_args, __pyx_kwds_len, "begin_ft_string_action", 0) < (0)) __PYX_ERR(0, 418, __pyx_L3_error)
      for (Py_ssize_t i = __pyx_nargs; i < 2; i++) {
        if (unlikely(!values[i])) { __Pyx_RaiseArgtupleInvalid("begin_ft_string_action", 1, 2, 2, i); __PYX_ERR(0, 418, __pyx_L3_error) }
      }
    } else if (unlikely(__pyx_nargs != 2)) {
      goto __pyx_L5_argtuple_error;
    } else {
      values[0] = __Pyx_ArgRef_FASTCALL(__pyx_args, 0);
      if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[0])) __PYX_ERR(0, 418, __pyx_L3_error)
      values[1] = __Pyx_ArgRef_FASTCALL(__pyx_args, 1);
      if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[1])) __PYX_ERR(0, 418, __pyx_L3_error)
    }
    __pyx_v_self = values[0];
    __pyx_v_text = values[1];
  }
  goto __pyx_L6_skip;
  __pyx_L5_argtuple_error:;
  __Pyx_RaiseArgtupleInvalid("begin_ft_string_action", 1, 2, 2, __pyx_nargs); __PYX_ERR(0, 418, __pyx_L3_error)
  __pyx_L6_skip:;
  goto __pyx_L4_argument_unpacking_done;
  __pyx_L3_error:;
  for (Py_ssize_t __pyx_temp=0; __pyx_temp < (Py_ssize_t)(sizeof(values)/sizeof(values[0])); ++__pyx_temp) {
    Py_XDECREF(values[__pyx_temp]);
  }
  __Pyx_AddTraceback("Cython.Compiler.Scanning.PyrexScanner.begin_ft_string_action", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __Pyx_RefNannyFinishContext();
  return NULL;
  __pyx_L4_argument_unpacking_done:;
  __pyx_r = __pyx_pf_6Cython_8Compiler_8Scanning_12PyrexScanner_26begin_ft_string_action(__pyx_self, __pyx_v_self, __pyx_v_text);
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

static PyObject *__pyx_pf_6Cython_8Compiler_8Scanning_12PyrexScanner_26begin_ft_string_action(CYTHON_UNUSED PyObject *__pyx_self, PyObject *__pyx_v_self, PyObject *__pyx_v_text) {
  PyObject *__pyx_v_is_raw = NULL;
  PyObject *__pyx_v_ft_string_state = NULL;
  PyObject *__pyx_r = NULL;
  __Pyx_INCREF(__pyx_v_text);
/* … */
  /* function exit code */
  __pyx_r = Py_None; __Pyx_INCREF(Py_None);
  goto __pyx_L0;
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_t_1);
  __Pyx_XDECREF(__pyx_t_3);
  __Pyx_XDECREF(__pyx_t_5);
  __Pyx_XDECREF(__pyx_t_7);
  __Pyx_AddTraceback("Cython.Compiler.Scanning.PyrexScanner.begin_ft_string_action", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_r = NULL;
  __pyx_L0:;
  __Pyx_XDECREF(__pyx_v_is_raw);
  __Pyx_XDECREF(__pyx_v_ft_string_state);
  __Pyx_XDECREF(__pyx_v_text);
  __Pyx_XGIVEREF(__pyx_r);
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}
/* … */
  __pyx_t_7 = __Pyx_CyFunction_New(&__pyx_mdef_6Cython_8Compiler_8Scanning_12PyrexScanner_27begin_ft_string_action, 0, __pyx_mstate_global->__pyx_n_u_PyrexScanner_begin_ft_string_act, NULL, __pyx_mstate_global->__pyx_n_u_Cython_Compiler_Scanning, __pyx_mstate_global->__pyx_d, ((PyObject *)__pyx_mstate_global->__pyx_codeobj_tab[48])); if (unlikely(!__pyx_t_7)) __PYX_ERR(0, 418, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_7);
  #if CYTHON_COMPILING_IN_CPYTHON && PY_VERSION_HEX >= 0x030E0000
  PyUnstable_Object_EnableDeferredRefcount(__pyx_t_7);
  #endif
  if (__Pyx_SetNameInClass(__pyx_t_8, __pyx_mstate_global->__pyx_n_u_begin_ft_string_action, __pyx_t_7) < (0)) __PYX_ERR(0, 418, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_7); __pyx_t_7 = 0;
```

</details>

L419  🟠  (score=8)
```python
        is_raw = 'r' in text or 'R' in text
```
<details><summary>Show generated C (score=8)</summary>

```c
  __pyx_t_2 = (__Pyx_PySequence_ContainsTF(__pyx_mstate_global->__pyx_n_u_r, __pyx_v_text, Py_EQ)); if (unlikely((__pyx_t_2 < 0))) __PYX_ERR(0, 419, __pyx_L1_error)
  if (!__pyx_t_2) {
  } else {
    __pyx_t_3 = __Pyx_PyBool_FromLong(__pyx_t_2); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 419, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_3);
    __pyx_t_1 = __pyx_t_3;
    __pyx_t_3 = 0;
    goto __pyx_L3_bool_binop_done;
  }
  __pyx_t_2 = (__Pyx_PySequence_ContainsTF(__pyx_mstate_global->__pyx_n_u_R, __pyx_v_text, Py_EQ)); if (unlikely((__pyx_t_2 < 0))) __PYX_ERR(0, 419, __pyx_L1_error)
  __pyx_t_3 = __Pyx_PyBool_FromLong(__pyx_t_2); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 419, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_3);
  __pyx_t_1 = __pyx_t_3;
  __pyx_t_3 = 0;
  __pyx_L3_bool_binop_done:;
  __pyx_v_is_raw = __pyx_t_1;
  __pyx_t_1 = 0;
```

</details>

L420  🔴  (score=18)
```python
        while text and (text[0] in any_string_prefix or text[0] in ft_string_prefixes):
```
<details><summary>Show generated C (score=18)</summary>

```c
  while (1) {
    __pyx_t_4 = __Pyx_PyObject_IsTrue(__pyx_v_text); if (unlikely((__pyx_t_4 < 0))) __PYX_ERR(0, 420, __pyx_L1_error)
    if (__pyx_t_4) {
    } else {
      __pyx_t_2 = __pyx_t_4;
      goto __pyx_L7_bool_binop_done;
    }
    __pyx_t_1 = __Pyx_GetItemInt(__pyx_v_text, 0, long, 1, __Pyx_PyLong_From_long, 0, 0, 0, 1, __Pyx_ReferenceSharing_FunctionArgument); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 420, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_1);
    __Pyx_GetModuleGlobalName(__pyx_t_3, __pyx_mstate_global->__pyx_n_u_any_string_prefix); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 420, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_3);
    __pyx_t_4 = (__Pyx_PySequence_ContainsTF(__pyx_t_1, __pyx_t_3, Py_EQ)); if (unlikely((__pyx_t_4 < 0))) __PYX_ERR(0, 420, __pyx_L1_error)
    __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
    __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
    if (!__pyx_t_4) {
    } else {
      __pyx_t_2 = __pyx_t_4;
      goto __pyx_L7_bool_binop_done;
    }
    __pyx_t_3 = __Pyx_GetItemInt(__pyx_v_text, 0, long, 1, __Pyx_PyLong_From_long, 0, 0, 0, 1, __Pyx_ReferenceSharing_FunctionArgument); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 420, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_3);
    __Pyx_GetModuleGlobalName(__pyx_t_1, __pyx_mstate_global->__pyx_n_u_ft_string_prefixes); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 420, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_1);
    __pyx_t_4 = (__Pyx_PySequence_ContainsTF(__pyx_t_3, __pyx_t_1, Py_EQ)); if (unlikely((__pyx_t_4 < 0))) __PYX_ERR(0, 420, __pyx_L1_error)
    __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
    __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
    __pyx_t_2 = __pyx_t_4;
    __pyx_L7_bool_binop_done:;
    if (!__pyx_t_2) break;
```

</details>

L421  🟡  (score=3)
```python
            text = text[1:]
```
<details><summary>Show generated C (score=3)</summary>

```c
    __pyx_t_1 = __Pyx_PyObject_GetSlice(__pyx_v_text, 1, 0, NULL, NULL, &__pyx_mstate_global->__pyx_slice[0], 1, 0, 0); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 421, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_1);
    __Pyx_DECREF_SET(__pyx_v_text, __pyx_t_1);
    __pyx_t_1 = 0;
  }
```

</details>

L422  🔴  (score=27)
```python
        ft_string_state = f'{self.string_states[text]}_FT{"R" if is_raw else ""}'
```
<details><summary>Show generated C (score=27)</summary>

```c
  __pyx_t_1 = __Pyx_PyObject_GetAttrStr(__pyx_v_self, __pyx_mstate_global->__pyx_n_u_string_states); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 422, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __pyx_t_3 = __Pyx_PyObject_GetItem(__pyx_t_1, __pyx_v_text); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 422, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_3);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __pyx_t_1 = __Pyx_PyObject_FormatSimple(__pyx_t_3, __pyx_mstate_global->__pyx_empty_unicode); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 422, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
  __pyx_t_2 = __Pyx_PyObject_IsTrue(__pyx_v_is_raw); if (unlikely((__pyx_t_2 < 0))) __PYX_ERR(0, 422, __pyx_L1_error)
  if (__pyx_t_2) {
    __Pyx_INCREF(__pyx_mstate_global->__pyx_n_u_R);
    __pyx_t_3 = __pyx_mstate_global->__pyx_n_u_R;
  } else {
    __Pyx_INCREF(__pyx_mstate_global->__pyx_kp_u__6);
    __pyx_t_3 = __pyx_mstate_global->__pyx_kp_u__6;
  }
  __pyx_t_5 = __Pyx_PyUnicode_Unicode(__pyx_t_3); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 422, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_5);
  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
  __pyx_t_6[0] = __pyx_t_1;
  __pyx_t_6[1] = __pyx_mstate_global->__pyx_n_u_FT;
  __pyx_t_6[2] = __pyx_t_5;
  __pyx_t_3 = __Pyx_PyUnicode_Join(__pyx_t_6, 3, __Pyx_PyUnicode_GET_LENGTH(__pyx_t_1) + 3 + __Pyx_PyUnicode_GET_LENGTH(__pyx_t_5), 127 | __Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_1) | __Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_5));
  if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 422, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_3);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
  __pyx_v_ft_string_state = __pyx_t_3;
  __pyx_t_3 = 0;
```

</details>

L423  🟠  (score=6)
```python
        self.ft_string_state_stack.append(
```
<details><summary>Show generated C (score=6)</summary>

```c
  __pyx_t_3 = __Pyx_PyObject_GetAttrStr(__pyx_v_self, __pyx_mstate_global->__pyx_n_u_ft_string_state_stack); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 423, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_3);
/* … */
  __pyx_t_9 = __Pyx_PyObject_Append(__pyx_t_3, __pyx_t_5); if (unlikely(__pyx_t_9 == ((int)-1))) __PYX_ERR(0, 423, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
  __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
```

</details>

L424  🟠  (score=6)
```python
            FTStringState(ft_string_state)
```
<details><summary>Show generated C (score=6)</summary>

```c
  __pyx_t_1 = NULL;
  __Pyx_GetModuleGlobalName(__pyx_t_7, __pyx_mstate_global->__pyx_n_u_FTStringState); if (unlikely(!__pyx_t_7)) __PYX_ERR(0, 424, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_7);
  __pyx_t_8 = 1;
  {
    PyObject *__pyx_callargs[2] = {__pyx_t_1, __pyx_v_ft_string_state};
    __pyx_t_5 = __Pyx_PyObject_FastCall((PyObject*)__pyx_t_7, __pyx_callargs+__pyx_t_8, (2-__pyx_t_8) | (__pyx_t_8*__Pyx_PY_VECTORCALL_ARGUMENTS_OFFSET));
    __Pyx_XDECREF(__pyx_t_1); __pyx_t_1 = 0;
    __Pyx_DECREF(__pyx_t_7); __pyx_t_7 = 0;
    if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 424, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_5);
  }
```

</details>

L425  ⚪  (score=0)
```python
        )
```
L426  🟠  (score=5)
```python
        self.begin(ft_string_state)
```
<details><summary>Show generated C (score=5)</summary>

```c
  __pyx_t_3 = __pyx_v_self;
  __Pyx_INCREF(__pyx_t_3);
  __pyx_t_8 = 0;
  {
    PyObject *__pyx_callargs[2] = {__pyx_t_3, __pyx_v_ft_string_state};
    __pyx_t_5 = __Pyx_PyObject_FastCallMethod((PyObject*)__pyx_mstate_global->__pyx_n_u_begin, __pyx_callargs+__pyx_t_8, (2-__pyx_t_8) | (1*__Pyx_PY_VECTORCALL_ARGUMENTS_OFFSET));
    __Pyx_XDECREF(__pyx_t_3); __pyx_t_3 = 0;
    if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 426, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_5);
  }
  __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
```

</details>

L427  🟠  (score=5)
```python
        self.produce('BEGIN_FT_STRING')
```
<details><summary>Show generated C (score=5)</summary>

```c
  __pyx_t_3 = __pyx_v_self;
  __Pyx_INCREF(__pyx_t_3);
  __pyx_t_8 = 0;
  {
    PyObject *__pyx_callargs[2] = {__pyx_t_3, __pyx_mstate_global->__pyx_n_u_BEGIN_FT_STRING};
    __pyx_t_5 = __Pyx_PyObject_FastCallMethod((PyObject*)__pyx_mstate_global->__pyx_n_u_produce, __pyx_callargs+__pyx_t_8, (2-__pyx_t_8) | (1*__Pyx_PY_VECTORCALL_ARGUMENTS_OFFSET));
    __Pyx_XDECREF(__pyx_t_3); __pyx_t_3 = 0;
    if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 427, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_5);
  }
  __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
```

</details>

L428  ⚪  (score=0)
```python
```
L429  🔴  (score=44)
```python
    def end_ft_string_action(self, text):
```
<details><summary>Show generated C (score=44)</summary>

```c
/* Python wrapper */
static PyObject *__pyx_pw_6Cython_8Compiler_8Scanning_12PyrexScanner_29end_ft_string_action(PyObject *__pyx_self, 
#if CYTHON_METH_FASTCALL
PyObject *const *__pyx_args, Py_ssize_t __pyx_nargs, PyObject *__pyx_kwds
#else
PyObject *__pyx_args, PyObject *__pyx_kwds
#endif
); /*proto*/
PyDoc_STRVAR(__pyx_doc_6Cython_8Compiler_8Scanning_12PyrexScanner_28end_ft_string_action, "File: Cython/Compiler/Scanning.py (starting at line 429)");
static PyMethodDef __pyx_mdef_6Cython_8Compiler_8Scanning_12PyrexScanner_29end_ft_string_action = {"end_ft_string_action", (PyCFunction)(void(*)(void))(__Pyx_PyCFunction_FastCallWithKeywords)__pyx_pw_6Cython_8Compiler_8Scanning_12PyrexScanner_29end_ft_string_action, __Pyx_METH_FASTCALL|METH_KEYWORDS, __pyx_doc_6Cython_8Compiler_8Scanning_12PyrexScanner_28end_ft_string_action};
static PyObject *__pyx_pw_6Cython_8Compiler_8Scanning_12PyrexScanner_29end_ft_string_action(PyObject *__pyx_self, 
#if CYTHON_METH_FASTCALL
PyObject *const *__pyx_args, Py_ssize_t __pyx_nargs, PyObject *__pyx_kwds
#else
PyObject *__pyx_args, PyObject *__pyx_kwds
#endif
) {
  PyObject *__pyx_v_self = 0;
  CYTHON_UNUSED PyObject *__pyx_v_text = 0;
  #if !CYTHON_METH_FASTCALL
  CYTHON_UNUSED Py_ssize_t __pyx_nargs;
  #endif
  CYTHON_UNUSED PyObject *const *__pyx_kwvalues;
  PyObject *__pyx_r = 0;
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("end_ft_string_action (wrapper)", 0);
  #if !CYTHON_METH_FASTCALL
  #if CYTHON_ASSUME_SAFE_SIZE
  __pyx_nargs = PyTuple_GET_SIZE(__pyx_args);
  #else
  __pyx_nargs = PyTuple_Size(__pyx_args); if (unlikely(__pyx_nargs < 0)) return NULL;
  #endif
  #endif
  __pyx_kwvalues = __Pyx_KwValues_FASTCALL(__pyx_args, __pyx_nargs);
  {
    PyObject ** const __pyx_pyargnames[] = {&__pyx_mstate_global->__pyx_n_u_self,&__pyx_mstate_global->__pyx_n_u_text,0};
  PyObject* values[2] = {0,0};
    const Py_ssize_t __pyx_kwds_len = (__pyx_kwds) ? __Pyx_NumKwargs_FASTCALL(__pyx_kwds) : 0;
    if (unlikely(__pyx_kwds_len) < 0) __PYX_ERR(0, 429, __pyx_L3_error)
    if (__pyx_kwds_len > 0) {
      switch (__pyx_nargs) {
        case  2:
        values[1] = __Pyx_ArgRef_FASTCALL(__pyx_args, 1);
        if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[1])) __PYX_ERR(0, 429, __pyx_L3_error)
        CYTHON_FALLTHROUGH;
        case  1:
        values[0] = __Pyx_ArgRef_FASTCALL(__pyx_args, 0);
        if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[0])) __PYX_ERR(0, 429, __pyx_L3_error)
        CYTHON_FALLTHROUGH;
        case  0: break;
        default: goto __pyx_L5_argtuple_error;
      }
      const Py_ssize_t kwd_pos_args = __pyx_nargs;
      if (__Pyx_ParseKeywords(__pyx_kwds, __pyx_kwvalues, __pyx_pyargnames, 0, values, kwd_pos_args, __pyx_kwds_len, "end_ft_string_action", 0) < (0)) __PYX_ERR(0, 429, __pyx_L3_error)
      for (Py_ssize_t i = __pyx_nargs; i < 2; i++) {
        if (unlikely(!values[i])) { __Pyx_RaiseArgtupleInvalid("end_ft_string_action", 1, 2, 2, i); __PYX_ERR(0, 429, __pyx_L3_error) }
      }
    } else if (unlikely(__pyx_nargs != 2)) {
      goto __pyx_L5_argtuple_error;
    } else {
      values[0] = __Pyx_ArgRef_FASTCALL(__pyx_args, 0);
      if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[0])) __PYX_ERR(0, 429, __pyx_L3_error)
      values[1] = __Pyx_ArgRef_FASTCALL(__pyx_args, 1);
      if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[1])) __PYX_ERR(0, 429, __pyx_L3_error)
    }
    __pyx_v_self = values[0];
    __pyx_v_text = values[1];
  }
  goto __pyx_L6_skip;
  __pyx_L5_argtuple_error:;
  __Pyx_RaiseArgtupleInvalid("end_ft_string_action", 1, 2, 2, __pyx_nargs); __PYX_ERR(0, 429, __pyx_L3_error)
  __pyx_L6_skip:;
  goto __pyx_L4_argument_unpacking_done;
  __pyx_L3_error:;
  for (Py_ssize_t __pyx_temp=0; __pyx_temp < (Py_ssize_t)(sizeof(values)/sizeof(values[0])); ++__pyx_temp) {
    Py_XDECREF(values[__pyx_temp]);
  }
  __Pyx_AddTraceback("Cython.Compiler.Scanning.PyrexScanner.end_ft_string_action", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __Pyx_RefNannyFinishContext();
  return NULL;
  __pyx_L4_argument_unpacking_done:;
  __pyx_r = __pyx_pf_6Cython_8Compiler_8Scanning_12PyrexScanner_28end_ft_string_action(__pyx_self, __pyx_v_self, __pyx_v_text);
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

static PyObject *__pyx_pf_6Cython_8Compiler_8Scanning_12PyrexScanner_28end_ft_string_action(CYTHON_UNUSED PyObject *__pyx_self, PyObject *__pyx_v_self, CYTHON_UNUSED PyObject *__pyx_v_text) {
  PyObject *__pyx_r = NULL;
/* … */
  /* function exit code */
  __pyx_r = Py_None; __Pyx_INCREF(Py_None);
  goto __pyx_L0;
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_t_1);
  __Pyx_XDECREF(__pyx_t_2);
  __Pyx_XDECREF(__pyx_t_3);
  __Pyx_XDECREF(__pyx_t_4);
  __Pyx_AddTraceback("Cython.Compiler.Scanning.PyrexScanner.end_ft_string_action", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_r = NULL;
  __pyx_L0:;
  __Pyx_XGIVEREF(__pyx_r);
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}
/* … */
  __pyx_t_7 = __Pyx_CyFunction_New(&__pyx_mdef_6Cython_8Compiler_8Scanning_12PyrexScanner_29end_ft_string_action, 0, __pyx_mstate_global->__pyx_n_u_PyrexScanner_end_ft_string_actio, NULL, __pyx_mstate_global->__pyx_n_u_Cython_Compiler_Scanning, __pyx_mstate_global->__pyx_d, ((PyObject *)__pyx_mstate_global->__pyx_codeobj_tab[49])); if (unlikely(!__pyx_t_7)) __PYX_ERR(0, 429, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_7);
  #if CYTHON_COMPILING_IN_CPYTHON && PY_VERSION_HEX >= 0x030E0000
  PyUnstable_Object_EnableDeferredRefcount(__pyx_t_7);
  #endif
  if (__Pyx_SetNameInClass(__pyx_t_8, __pyx_mstate_global->__pyx_n_u_end_ft_string_action, __pyx_t_7) < (0)) __PYX_ERR(0, 429, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_7); __pyx_t_7 = 0;
```

</details>

L430  🟠  (score=6)
```python
        self.ft_string_state_stack.pop()
```
<details><summary>Show generated C (score=6)</summary>

```c
  __pyx_t_1 = __Pyx_PyObject_GetAttrStr(__pyx_v_self, __pyx_mstate_global->__pyx_n_u_ft_string_state_stack); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 430, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __pyx_t_2 = __Pyx_PyObject_Pop(__pyx_t_1); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 430, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
```

</details>

L431  🔴  (score=13)
```python
        self.begin('FT_STRING_EXPR_PRESCAN' if self.in_ft_string_expr_prescan else '')
```
<details><summary>Show generated C (score=13)</summary>

```c
  __pyx_t_1 = __pyx_v_self;
  __Pyx_INCREF(__pyx_t_1);
  __pyx_t_4 = __Pyx_PyObject_GetAttrStr(__pyx_v_self, __pyx_mstate_global->__pyx_n_u_in_ft_string_expr_prescan); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 431, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_4);
  __pyx_t_5 = __Pyx_PyObject_IsTrue(__pyx_t_4); if (unlikely((__pyx_t_5 < 0))) __PYX_ERR(0, 431, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
  if (__pyx_t_5) {
    __Pyx_INCREF(__pyx_mstate_global->__pyx_n_u_FT_STRING_EXPR_PRESCAN);
    __pyx_t_3 = __pyx_mstate_global->__pyx_n_u_FT_STRING_EXPR_PRESCAN;
  } else {
    __Pyx_INCREF(__pyx_mstate_global->__pyx_kp_u__6);
    __pyx_t_3 = __pyx_mstate_global->__pyx_kp_u__6;
  }
  __pyx_t_6 = 0;
  {
    PyObject *__pyx_callargs[2] = {__pyx_t_1, __pyx_t_3};
    __pyx_t_2 = __Pyx_PyObject_FastCallMethod((PyObject*)__pyx_mstate_global->__pyx_n_u_begin, __pyx_callargs+__pyx_t_6, (2-__pyx_t_6) | (1*__Pyx_PY_VECTORCALL_ARGUMENTS_OFFSET));
    __Pyx_XDECREF(__pyx_t_1); __pyx_t_1 = 0;
    __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
    if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 431, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_2);
  }
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
```

</details>

L432  🟠  (score=5)
```python
        self.produce('END_FT_STRING')
```
<details><summary>Show generated C (score=5)</summary>

```c
  __pyx_t_3 = __pyx_v_self;
  __Pyx_INCREF(__pyx_t_3);
  __pyx_t_6 = 0;
  {
    PyObject *__pyx_callargs[2] = {__pyx_t_3, __pyx_mstate_global->__pyx_n_u_END_FT_STRING};
    __pyx_t_2 = __Pyx_PyObject_FastCallMethod((PyObject*)__pyx_mstate_global->__pyx_n_u_produce, __pyx_callargs+__pyx_t_6, (2-__pyx_t_6) | (1*__Pyx_PY_VECTORCALL_ARGUMENTS_OFFSET));
    __Pyx_XDECREF(__pyx_t_3); __pyx_t_3 = 0;
    if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 432, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_2);
  }
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
```

</details>

L433  ⚪  (score=0)
```python
```
L434  🔴  (score=44)
```python
    def _handle_open_single_ft_string_brace(self, started_ft_string_expr):
```
<details><summary>Show generated C (score=44)</summary>

```c
/* Python wrapper */
static PyObject *__pyx_pw_6Cython_8Compiler_8Scanning_12PyrexScanner_31_handle_open_single_ft_string_brace(PyObject *__pyx_self, 
#if CYTHON_METH_FASTCALL
PyObject *const *__pyx_args, Py_ssize_t __pyx_nargs, PyObject *__pyx_kwds
#else
PyObject *__pyx_args, PyObject *__pyx_kwds
#endif
); /*proto*/
PyDoc_STRVAR(__pyx_doc_6Cython_8Compiler_8Scanning_12PyrexScanner_30_handle_open_single_ft_string_brace, "File: Cython/Compiler/Scanning.py (starting at line 434)");
static PyMethodDef __pyx_mdef_6Cython_8Compiler_8Scanning_12PyrexScanner_31_handle_open_single_ft_string_brace = {"_handle_open_single_ft_string_brace", (PyCFunction)(void(*)(void))(__Pyx_PyCFunction_FastCallWithKeywords)__pyx_pw_6Cython_8Compiler_8Scanning_12PyrexScanner_31_handle_open_single_ft_string_brace, __Pyx_METH_FASTCALL|METH_KEYWORDS, __pyx_doc_6Cython_8Compiler_8Scanning_12PyrexScanner_30_handle_open_single_ft_string_brace};
static PyObject *__pyx_pw_6Cython_8Compiler_8Scanning_12PyrexScanner_31_handle_open_single_ft_string_brace(PyObject *__pyx_self, 
#if CYTHON_METH_FASTCALL
PyObject *const *__pyx_args, Py_ssize_t __pyx_nargs, PyObject *__pyx_kwds
#else
PyObject *__pyx_args, PyObject *__pyx_kwds
#endif
) {
  PyObject *__pyx_v_self = 0;
  PyObject *__pyx_v_started_ft_string_expr = 0;
  #if !CYTHON_METH_FASTCALL
  CYTHON_UNUSED Py_ssize_t __pyx_nargs;
  #endif
  CYTHON_UNUSED PyObject *const *__pyx_kwvalues;
  PyObject *__pyx_r = 0;
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("_handle_open_single_ft_string_brace (wrapper)", 0);
  #if !CYTHON_METH_FASTCALL
  #if CYTHON_ASSUME_SAFE_SIZE
  __pyx_nargs = PyTuple_GET_SIZE(__pyx_args);
  #else
  __pyx_nargs = PyTuple_Size(__pyx_args); if (unlikely(__pyx_nargs < 0)) return NULL;
  #endif
  #endif
  __pyx_kwvalues = __Pyx_KwValues_FASTCALL(__pyx_args, __pyx_nargs);
  {
    PyObject ** const __pyx_pyargnames[] = {&__pyx_mstate_global->__pyx_n_u_self,&__pyx_mstate_global->__pyx_n_u_started_ft_string_expr,0};
  PyObject* values[2] = {0,0};
    const Py_ssize_t __pyx_kwds_len = (__pyx_kwds) ? __Pyx_NumKwargs_FASTCALL(__pyx_kwds) : 0;
    if (unlikely(__pyx_kwds_len) < 0) __PYX_ERR(0, 434, __pyx_L3_error)
    if (__pyx_kwds_len > 0) {
      switch (__pyx_nargs) {
        case  2:
        values[1] = __Pyx_ArgRef_FASTCALL(__pyx_args, 1);
        if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[1])) __PYX_ERR(0, 434, __pyx_L3_error)
        CYTHON_FALLTHROUGH;
        case  1:
        values[0] = __Pyx_ArgRef_FASTCALL(__pyx_args, 0);
        if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[0])) __PYX_ERR(0, 434, __pyx_L3_error)
        CYTHON_FALLTHROUGH;
        case  0: break;
        default: goto __pyx_L5_argtuple_error;
      }
      const Py_ssize_t kwd_pos_args = __pyx_nargs;
      if (__Pyx_ParseKeywords(__pyx_kwds, __pyx_kwvalues, __pyx_pyargnames, 0, values, kwd_pos_args, __pyx_kwds_len, "_handle_open_single_ft_string_brace", 0) < (0)) __PYX_ERR(0, 434, __pyx_L3_error)
      for (Py_ssize_t i = __pyx_nargs; i < 2; i++) {
        if (unlikely(!values[i])) { __Pyx_RaiseArgtupleInvalid("_handle_open_single_ft_string_brace", 1, 2, 2, i); __PYX_ERR(0, 434, __pyx_L3_error) }
      }
    } else if (unlikely(__pyx_nargs != 2)) {
      goto __pyx_L5_argtuple_error;
    } else {
      values[0] = __Pyx_ArgRef_FASTCALL(__pyx_args, 0);
      if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[0])) __PYX_ERR(0, 434, __pyx_L3_error)
      values[1] = __Pyx_ArgRef_FASTCALL(__pyx_args, 1);
      if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[1])) __PYX_ERR(0, 434, __pyx_L3_error)
    }
    __pyx_v_self = values[0];
    __pyx_v_started_ft_string_expr = values[1];
  }
  goto __pyx_L6_skip;
  __pyx_L5_argtuple_error:;
  __Pyx_RaiseArgtupleInvalid("_handle_open_single_ft_string_brace", 1, 2, 2, __pyx_nargs); __PYX_ERR(0, 434, __pyx_L3_error)
  __pyx_L6_skip:;
  goto __pyx_L4_argument_unpacking_done;
  __pyx_L3_error:;
  for (Py_ssize_t __pyx_temp=0; __pyx_temp < (Py_ssize_t)(sizeof(values)/sizeof(values[0])); ++__pyx_temp) {
    Py_XDECREF(values[__pyx_temp]);
  }
  __Pyx_AddTraceback("Cython.Compiler.Scanning.PyrexScanner._handle_open_single_ft_string_brace", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __Pyx_RefNannyFinishContext();
  return NULL;
  __pyx_L4_argument_unpacking_done:;
  __pyx_r = __pyx_pf_6Cython_8Compiler_8Scanning_12PyrexScanner_30_handle_open_single_ft_string_brace(__pyx_self, __pyx_v_self, __pyx_v_started_ft_string_expr);
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

static PyObject *__pyx_pf_6Cython_8Compiler_8Scanning_12PyrexScanner_30_handle_open_single_ft_string_brace(CYTHON_UNUSED PyObject *__pyx_self, PyObject *__pyx_v_self, PyObject *__pyx_v_started_ft_string_expr) {
  PyObject *__pyx_r = NULL;
/* … */
  /* function exit code */
  __pyx_r = Py_None; __Pyx_INCREF(Py_None);
  goto __pyx_L0;
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_t_1);
  __Pyx_XDECREF(__pyx_t_2);
  __Pyx_XDECREF(__pyx_t_5);
  __Pyx_XDECREF(__pyx_t_6);
  __Pyx_AddTraceback("Cython.Compiler.Scanning.PyrexScanner._handle_open_single_ft_string_brace", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_r = NULL;
  __pyx_L0:;
  __Pyx_XGIVEREF(__pyx_r);
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}
/* … */
  __pyx_t_7 = __Pyx_CyFunction_New(&__pyx_mdef_6Cython_8Compiler_8Scanning_12PyrexScanner_31_handle_open_single_ft_string_brace, 0, __pyx_mstate_global->__pyx_n_u_PyrexScanner__handle_open_single, NULL, __pyx_mstate_global->__pyx_n_u_Cython_Compiler_Scanning, __pyx_mstate_global->__pyx_d, ((PyObject *)__pyx_mstate_global->__pyx_codeobj_tab[50])); if (unlikely(!__pyx_t_7)) __PYX_ERR(0, 434, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_7);
  #if CYTHON_COMPILING_IN_CPYTHON && PY_VERSION_HEX >= 0x030E0000
  PyUnstable_Object_EnableDeferredRefcount(__pyx_t_7);
  #endif
  if (__Pyx_SetNameInClass(__pyx_t_8, __pyx_mstate_global->__pyx_n_u_handle_open_single_ft_string_br, __pyx_t_7) < (0)) __PYX_ERR(0, 434, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_7); __pyx_t_7 = 0;
```

</details>

L435  🟠  (score=8)
```python
        self.bracket_nesting_level += 1
```
<details><summary>Show generated C (score=8)</summary>

```c
  __pyx_t_1 = __Pyx_PyObject_GetAttrStr(__pyx_v_self, __pyx_mstate_global->__pyx_n_u_bracket_nesting_level); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 435, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __pyx_t_2 = __Pyx_PyLong_AddObjC(__pyx_t_1, __pyx_mstate_global->__pyx_int_1, 1, 1, 0); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 435, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  if (__Pyx_PyObject_SetAttrStr(__pyx_v_self, __pyx_mstate_global->__pyx_n_u_bracket_nesting_level, __pyx_t_2) < (0)) __PYX_ERR(0, 435, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
```

</details>

L436  🟡  (score=2)
```python
        if not started_ft_string_expr:
```
<details><summary>Show generated C (score=2)</summary>

```c
  __pyx_t_3 = __Pyx_PyObject_IsTrue(__pyx_v_started_ft_string_expr); if (unlikely((__pyx_t_3 < 0))) __PYX_ERR(0, 436, __pyx_L1_error)
  __pyx_t_4 = (!__pyx_t_3);
  if (__pyx_t_4) {
/* … */
  }
```

</details>

L437  🔴  (score=14)
```python
            self.ft_string_state_stack[-1].push_bracket_state(self.bracket_nesting_level)
```
<details><summary>Show generated C (score=14)</summary>

```c
    __pyx_t_5 = __Pyx_PyObject_GetAttrStr(__pyx_v_self, __pyx_mstate_global->__pyx_n_u_ft_string_state_stack); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 437, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_5);
    __pyx_t_6 = __Pyx_GetItemInt(__pyx_t_5, -1L, long, 1, __Pyx_PyLong_From_long, 0, 0, 0, 1, __Pyx_ReferenceSharing_OwnStrongReference); if (unlikely(!__pyx_t_6)) __PYX_ERR(0, 437, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_6);
    __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
    __pyx_t_1 = __pyx_t_6;
    __Pyx_INCREF(__pyx_t_1);
    __pyx_t_5 = __Pyx_PyObject_GetAttrStr(__pyx_v_self, __pyx_mstate_global->__pyx_n_u_bracket_nesting_level); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 437, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_5);
    __pyx_t_7 = 0;
    {
      PyObject *__pyx_callargs[2] = {__pyx_t_1, __pyx_t_5};
      __pyx_t_2 = __Pyx_PyObject_FastCallMethod((PyObject*)__pyx_mstate_global->__pyx_n_u_push_bracket_state, __pyx_callargs+__pyx_t_7, (2-__pyx_t_7) | (1*__Pyx_PY_VECTORCALL_ARGUMENTS_OFFSET));
      __Pyx_XDECREF(__pyx_t_1); __pyx_t_1 = 0;
      __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
      __Pyx_DECREF(__pyx_t_6); __pyx_t_6 = 0;
      if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 437, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_2);
    }
    __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
```

</details>

L438  🟠  (score=5)
```python
            self.begin('FT_STRING_EXPR_PRESCAN')
```
<details><summary>Show generated C (score=5)</summary>

```c
    __pyx_t_6 = __pyx_v_self;
    __Pyx_INCREF(__pyx_t_6);
    __pyx_t_7 = 0;
    {
      PyObject *__pyx_callargs[2] = {__pyx_t_6, __pyx_mstate_global->__pyx_n_u_FT_STRING_EXPR_PRESCAN};
      __pyx_t_2 = __Pyx_PyObject_FastCallMethod((PyObject*)__pyx_mstate_global->__pyx_n_u_begin, __pyx_callargs+__pyx_t_7, (2-__pyx_t_7) | (1*__Pyx_PY_VECTORCALL_ARGUMENTS_OFFSET));
      __Pyx_XDECREF(__pyx_t_6); __pyx_t_6 = 0;
      if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 438, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_2);
    }
    __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
```

</details>

L439  🟠  (score=8)
```python
            self.in_ft_string_expr_prescan += 1
```
<details><summary>Show generated C (score=8)</summary>

```c
    __pyx_t_2 = __Pyx_PyObject_GetAttrStr(__pyx_v_self, __pyx_mstate_global->__pyx_n_u_in_ft_string_expr_prescan); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 439, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_2);
    __pyx_t_6 = __Pyx_PyLong_AddObjC(__pyx_t_2, __pyx_mstate_global->__pyx_int_1, 1, 1, 0); if (unlikely(!__pyx_t_6)) __PYX_ERR(0, 439, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_6);
    __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
    if (__Pyx_PyObject_SetAttrStr(__pyx_v_self, __pyx_mstate_global->__pyx_n_u_in_ft_string_expr_prescan, __pyx_t_6) < (0)) __PYX_ERR(0, 439, __pyx_L1_error)
    __Pyx_DECREF(__pyx_t_6); __pyx_t_6 = 0;
```

</details>

L440  🟠  (score=5)
```python
        self.produce('{')
```
<details><summary>Show generated C (score=5)</summary>

```c
  __pyx_t_2 = __pyx_v_self;
  __Pyx_INCREF(__pyx_t_2);
  __pyx_t_7 = 0;
  {
    PyObject *__pyx_callargs[2] = {__pyx_t_2, __pyx_mstate_global->__pyx_kp_u__9};
    __pyx_t_6 = __Pyx_PyObject_FastCallMethod((PyObject*)__pyx_mstate_global->__pyx_n_u_produce, __pyx_callargs+__pyx_t_7, (2-__pyx_t_7) | (1*__Pyx_PY_VECTORCALL_ARGUMENTS_OFFSET));
    __Pyx_XDECREF(__pyx_t_2); __pyx_t_2 = 0;
    if (unlikely(!__pyx_t_6)) __PYX_ERR(0, 440, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_6);
  }
  __Pyx_DECREF(__pyx_t_6); __pyx_t_6 = 0;
```

</details>

L441  ⚪  (score=0)
```python
```
L442  🔴  (score=48)
```python
    def open_ft_string_brace_action(self, text):
```
<details><summary>Show generated C (score=48)</summary>

```c
/* Python wrapper */
static PyObject *__pyx_pw_6Cython_8Compiler_8Scanning_12PyrexScanner_33open_ft_string_brace_action(PyObject *__pyx_self, 
#if CYTHON_METH_FASTCALL
PyObject *const *__pyx_args, Py_ssize_t __pyx_nargs, PyObject *__pyx_kwds
#else
PyObject *__pyx_args, PyObject *__pyx_kwds
#endif
); /*proto*/
PyDoc_STRVAR(__pyx_doc_6Cython_8Compiler_8Scanning_12PyrexScanner_32open_ft_string_brace_action, "File: Cython/Compiler/Scanning.py (starting at line 442)");
static PyMethodDef __pyx_mdef_6Cython_8Compiler_8Scanning_12PyrexScanner_33open_ft_string_brace_action = {"open_ft_string_brace_action", (PyCFunction)(void(*)(void))(__Pyx_PyCFunction_FastCallWithKeywords)__pyx_pw_6Cython_8Compiler_8Scanning_12PyrexScanner_33open_ft_string_brace_action, __Pyx_METH_FASTCALL|METH_KEYWORDS, __pyx_doc_6Cython_8Compiler_8Scanning_12PyrexScanner_32open_ft_string_brace_action};
static PyObject *__pyx_pw_6Cython_8Compiler_8Scanning_12PyrexScanner_33open_ft_string_brace_action(PyObject *__pyx_self, 
#if CYTHON_METH_FASTCALL
PyObject *const *__pyx_args, Py_ssize_t __pyx_nargs, PyObject *__pyx_kwds
#else
PyObject *__pyx_args, PyObject *__pyx_kwds
#endif
) {
  PyObject *__pyx_v_self = 0;
  PyObject *__pyx_v_text = 0;
  #if !CYTHON_METH_FASTCALL
  CYTHON_UNUSED Py_ssize_t __pyx_nargs;
  #endif
  CYTHON_UNUSED PyObject *const *__pyx_kwvalues;
  PyObject *__pyx_r = 0;
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("open_ft_string_brace_action (wrapper)", 0);
  #if !CYTHON_METH_FASTCALL
  #if CYTHON_ASSUME_SAFE_SIZE
  __pyx_nargs = PyTuple_GET_SIZE(__pyx_args);
  #else
  __pyx_nargs = PyTuple_Size(__pyx_args); if (unlikely(__pyx_nargs < 0)) return NULL;
  #endif
  #endif
  __pyx_kwvalues = __Pyx_KwValues_FASTCALL(__pyx_args, __pyx_nargs);
  {
    PyObject ** const __pyx_pyargnames[] = {&__pyx_mstate_global->__pyx_n_u_self,&__pyx_mstate_global->__pyx_n_u_text,0};
  PyObject* values[2] = {0,0};
    const Py_ssize_t __pyx_kwds_len = (__pyx_kwds) ? __Pyx_NumKwargs_FASTCALL(__pyx_kwds) : 0;
    if (unlikely(__pyx_kwds_len) < 0) __PYX_ERR(0, 442, __pyx_L3_error)
    if (__pyx_kwds_len > 0) {
      switch (__pyx_nargs) {
        case  2:
        values[1] = __Pyx_ArgRef_FASTCALL(__pyx_args, 1);
        if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[1])) __PYX_ERR(0, 442, __pyx_L3_error)
        CYTHON_FALLTHROUGH;
        case  1:
        values[0] = __Pyx_ArgRef_FASTCALL(__pyx_args, 0);
        if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[0])) __PYX_ERR(0, 442, __pyx_L3_error)
        CYTHON_FALLTHROUGH;
        case  0: break;
        default: goto __pyx_L5_argtuple_error;
      }
      const Py_ssize_t kwd_pos_args = __pyx_nargs;
      if (__Pyx_ParseKeywords(__pyx_kwds, __pyx_kwvalues, __pyx_pyargnames, 0, values, kwd_pos_args, __pyx_kwds_len, "open_ft_string_brace_action", 0) < (0)) __PYX_ERR(0, 442, __pyx_L3_error)
      for (Py_ssize_t i = __pyx_nargs; i < 2; i++) {
        if (unlikely(!values[i])) { __Pyx_RaiseArgtupleInvalid("open_ft_string_brace_action", 1, 2, 2, i); __PYX_ERR(0, 442, __pyx_L3_error) }
      }
    } else if (unlikely(__pyx_nargs != 2)) {
      goto __pyx_L5_argtuple_error;
    } else {
      values[0] = __Pyx_ArgRef_FASTCALL(__pyx_args, 0);
      if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[0])) __PYX_ERR(0, 442, __pyx_L3_error)
      values[1] = __Pyx_ArgRef_FASTCALL(__pyx_args, 1);
      if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[1])) __PYX_ERR(0, 442, __pyx_L3_error)
    }
    __pyx_v_self = values[0];
    __pyx_v_text = values[1];
  }
  goto __pyx_L6_skip;
  __pyx_L5_argtuple_error:;
  __Pyx_RaiseArgtupleInvalid("open_ft_string_brace_action", 1, 2, 2, __pyx_nargs); __PYX_ERR(0, 442, __pyx_L3_error)
  __pyx_L6_skip:;
  goto __pyx_L4_argument_unpacking_done;
  __pyx_L3_error:;
  for (Py_ssize_t __pyx_temp=0; __pyx_temp < (Py_ssize_t)(sizeof(values)/sizeof(values[0])); ++__pyx_temp) {
    Py_XDECREF(values[__pyx_temp]);
  }
  __Pyx_AddTraceback("Cython.Compiler.Scanning.PyrexScanner.open_ft_string_brace_action", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __Pyx_RefNannyFinishContext();
  return NULL;
  __pyx_L4_argument_unpacking_done:;
  __pyx_r = __pyx_pf_6Cython_8Compiler_8Scanning_12PyrexScanner_32open_ft_string_brace_action(__pyx_self, __pyx_v_self, __pyx_v_text);
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

static PyObject *__pyx_pf_6Cython_8Compiler_8Scanning_12PyrexScanner_32open_ft_string_brace_action(CYTHON_UNUSED PyObject *__pyx_self, PyObject *__pyx_v_self, PyObject *__pyx_v_text) {
  PyObject *__pyx_v_len_text = NULL;
  PyObject *__pyx_v_started_ft_string_expr = NULL;
  PyObject *__pyx_v_double_braces = NULL;
  CYTHON_UNUSED PyObject *__pyx_v__ = NULL;
  PyObject *__pyx_r = NULL;
/* … */
  /* function exit code */
  __pyx_r = Py_None; __Pyx_INCREF(Py_None);
  goto __pyx_L0;
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_t_2);
  __Pyx_XDECREF(__pyx_t_3);
  __Pyx_XDECREF(__pyx_t_4);
  __Pyx_XDECREF(__pyx_t_5);
  __Pyx_AddTraceback("Cython.Compiler.Scanning.PyrexScanner.open_ft_string_brace_action", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_r = NULL;
  __pyx_L0:;
  __Pyx_XDECREF(__pyx_v_len_text);
  __Pyx_XDECREF(__pyx_v_started_ft_string_expr);
  __Pyx_XDECREF(__pyx_v_double_braces);
  __Pyx_XDECREF(__pyx_v__);
  __Pyx_XGIVEREF(__pyx_r);
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}
/* … */
  __pyx_t_7 = __Pyx_CyFunction_New(&__pyx_mdef_6Cython_8Compiler_8Scanning_12PyrexScanner_33open_ft_string_brace_action, 0, __pyx_mstate_global->__pyx_n_u_PyrexScanner_open_ft_string_brac, NULL, __pyx_mstate_global->__pyx_n_u_Cython_Compiler_Scanning, __pyx_mstate_global->__pyx_d, ((PyObject *)__pyx_mstate_global->__pyx_codeobj_tab[51])); if (unlikely(!__pyx_t_7)) __PYX_ERR(0, 442, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_7);
  #if CYTHON_COMPILING_IN_CPYTHON && PY_VERSION_HEX >= 0x030E0000
  PyUnstable_Object_EnableDeferredRefcount(__pyx_t_7);
  #endif
  if (__Pyx_SetNameInClass(__pyx_t_8, __pyx_mstate_global->__pyx_n_u_open_ft_string_brace_action, __pyx_t_7) < (0)) __PYX_ERR(0, 442, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_7); __pyx_t_7 = 0;
```

</details>

L443  🔴  (score=10)
```python
        len_text = len(text)
```
<details><summary>Show generated C (score=10)</summary>

```c
  __pyx_t_1 = PyObject_Length(__pyx_v_text); if (unlikely(__pyx_t_1 == ((Py_ssize_t)-1))) __PYX_ERR(0, 443, __pyx_L1_error)
  __pyx_t_2 = PyLong_FromSsize_t(__pyx_t_1); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 443, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __pyx_v_len_text = __pyx_t_2;
  __pyx_t_2 = 0;
```

</details>

L444  🟡  (score=1)
```python
        started_ft_string_expr = False
```
<details><summary>Show generated C (score=1)</summary>

```c
  __Pyx_INCREF(Py_False);
  __pyx_v_started_ft_string_expr = Py_False;
```

</details>

L445  🔴  (score=13)
```python
        if self.ft_string_state_stack[-1].in_format_specifier():
```
<details><summary>Show generated C (score=13)</summary>

```c
  __pyx_t_4 = __Pyx_PyObject_GetAttrStr(__pyx_v_self, __pyx_mstate_global->__pyx_n_u_ft_string_state_stack); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 445, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_4);
  __pyx_t_5 = __Pyx_GetItemInt(__pyx_t_4, -1L, long, 1, __Pyx_PyLong_From_long, 0, 0, 0, 1, __Pyx_ReferenceSharing_OwnStrongReference); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 445, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_5);
  __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
  __pyx_t_3 = __pyx_t_5;
  __Pyx_INCREF(__pyx_t_3);
  __pyx_t_6 = 0;
  {
    PyObject *__pyx_callargs[2] = {__pyx_t_3, NULL};
    __pyx_t_2 = __Pyx_PyObject_FastCallMethod((PyObject*)__pyx_mstate_global->__pyx_n_u_in_format_specifier, __pyx_callargs+__pyx_t_6, (1-__pyx_t_6) | (1*__Pyx_PY_VECTORCALL_ARGUMENTS_OFFSET));
    __Pyx_XDECREF(__pyx_t_3); __pyx_t_3 = 0;
    __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
    if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 445, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_2);
  }
  __pyx_t_7 = __Pyx_PyObject_IsTrue(__pyx_t_2); if (unlikely((__pyx_t_7 < 0))) __PYX_ERR(0, 445, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  if (__pyx_t_7) {
/* … */
  }
```

</details>

L446  🟠  (score=5)
```python
            self._handle_open_single_ft_string_brace(started_ft_string_expr)
```
<details><summary>Show generated C (score=5)</summary>

```c
    __pyx_t_5 = __pyx_v_self;
    __Pyx_INCREF(__pyx_t_5);
    __pyx_t_6 = 0;
    {
      PyObject *__pyx_callargs[2] = {__pyx_t_5, __pyx_v_started_ft_string_expr};
      __pyx_t_2 = __Pyx_PyObject_FastCallMethod((PyObject*)__pyx_mstate_global->__pyx_n_u_handle_open_single_ft_string_br, __pyx_callargs+__pyx_t_6, (2-__pyx_t_6) | (1*__Pyx_PY_VECTORCALL_ARGUMENTS_OFFSET));
      __Pyx_XDECREF(__pyx_t_5); __pyx_t_5 = 0;
      if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 446, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_2);
    }
    __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
```

</details>

L447  🟡  (score=3)
```python
            len_text -= 1
```
<details><summary>Show generated C (score=3)</summary>

```c
    __pyx_t_2 = __Pyx_PyLong_SubtractObjC(__pyx_v_len_text, __pyx_mstate_global->__pyx_int_1, 1, 1, 0); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 447, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_2);
    __Pyx_DECREF_SET(__pyx_v_len_text, __pyx_t_2);
    __pyx_t_2 = 0;
```

</details>

L448  🟡  (score=2)
```python
            started_ft_string_expr = True
```
<details><summary>Show generated C (score=2)</summary>

```c
    __Pyx_INCREF(Py_True);
    __Pyx_DECREF_SET(__pyx_v_started_ft_string_expr, Py_True);
```

</details>

L449  🔴  (score=15)
```python
        assert not self.ft_string_state_stack[-1].in_format_specifier()
```
<details><summary>Show generated C (score=15)</summary>

```c
  #ifndef CYTHON_WITHOUT_ASSERTIONS
  if (unlikely(__pyx_assertions_enabled())) {
    __pyx_t_3 = __Pyx_PyObject_GetAttrStr(__pyx_v_self, __pyx_mstate_global->__pyx_n_u_ft_string_state_stack); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 449, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_3);
    __pyx_t_4 = __Pyx_GetItemInt(__pyx_t_3, -1L, long, 1, __Pyx_PyLong_From_long, 0, 0, 0, 1, __Pyx_ReferenceSharing_OwnStrongReference); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 449, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_4);
    __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
    __pyx_t_5 = __pyx_t_4;
    __Pyx_INCREF(__pyx_t_5);
    __pyx_t_6 = 0;
    {
      PyObject *__pyx_callargs[2] = {__pyx_t_5, NULL};
      __pyx_t_2 = __Pyx_PyObject_FastCallMethod((PyObject*)__pyx_mstate_global->__pyx_n_u_in_format_specifier, __pyx_callargs+__pyx_t_6, (1-__pyx_t_6) | (1*__Pyx_PY_VECTORCALL_ARGUMENTS_OFFSET));
      __Pyx_XDECREF(__pyx_t_5); __pyx_t_5 = 0;
      __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
      if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 449, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_2);
    }
    __pyx_t_7 = __Pyx_PyObject_IsTrue(__pyx_t_2); if (unlikely((__pyx_t_7 < 0))) __PYX_ERR(0, 449, __pyx_L1_error)
    __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
    __pyx_t_8 = (!__pyx_t_7);
    if (unlikely(!__pyx_t_8)) {
      __Pyx_Raise(((PyObject *)(((PyTypeObject*)PyExc_AssertionError))), 0, 0, 0);
      __PYX_ERR(0, 449, __pyx_L1_error)
    }
  }
  #else
  if ((1)); else __PYX_ERR(0, 449, __pyx_L1_error)
  #endif
```

</details>

L450  ⚪  (score=0)
```python
```
L451  🟡  (score=2)
```python
        double_braces = len_text // 2
```
<details><summary>Show generated C (score=2)</summary>

```c
  __pyx_t_2 = __Pyx_PyLong_FloorDivideObjC(__pyx_v_len_text, __pyx_mstate_global->__pyx_int_2, 2, 0, 0); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 451, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __pyx_v_double_braces = __pyx_t_2;
  __pyx_t_2 = 0;
```

</details>

L452  🔴  (score=25)
```python
        for _ in range(double_braces):
```
<details><summary>Show generated C (score=25)</summary>

```c
  __pyx_t_4 = NULL;
  __pyx_t_6 = 1;
  {
    PyObject *__pyx_callargs[2] = {__pyx_t_4, __pyx_v_double_braces};
    __pyx_t_2 = __Pyx_PyObject_FastCall((PyObject*)(&PyRange_Type), __pyx_callargs+__pyx_t_6, (2-__pyx_t_6) | (__pyx_t_6*__Pyx_PY_VECTORCALL_ARGUMENTS_OFFSET));
    __Pyx_XDECREF(__pyx_t_4); __pyx_t_4 = 0;
    if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 452, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_2);
  }
  __pyx_t_4 = PyObject_GetIter(__pyx_t_2); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 452, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_4);
  __pyx_t_9 = (CYTHON_COMPILING_IN_LIMITED_API) ? PyIter_Next : __Pyx_PyObject_GetIterNextFunc(__pyx_t_4); if (unlikely(!__pyx_t_9)) __PYX_ERR(0, 452, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  for (;;) {
    {
      __pyx_t_2 = __pyx_t_9(__pyx_t_4);
      if (unlikely(!__pyx_t_2)) {
        PyObject* exc_type = PyErr_Occurred();
        if (exc_type) {
          if (unlikely(!__Pyx_PyErr_GivenExceptionMatches(exc_type, PyExc_StopIteration))) __PYX_ERR(0, 452, __pyx_L1_error)
          PyErr_Clear();
        }
        break;
      }
    }
    __Pyx_GOTREF(__pyx_t_2);
    __Pyx_XDECREF_SET(__pyx_v__, __pyx_t_2);
    __pyx_t_2 = 0;
/* … */
  }
  __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
```

</details>

L453  🔴  (score=11)
```python
            self.produce('CHARS', '{')
```
<details><summary>Show generated C (score=11)</summary>

```c
    __pyx_t_2 = __Pyx_PyObject_GetAttrStr(__pyx_v_self, __pyx_mstate_global->__pyx_n_u_produce); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 453, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_2);
    __pyx_t_5 = __Pyx_PyObject_Call(__pyx_t_2, __pyx_mstate_global->__pyx_tuple[6], NULL); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 453, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_5);
    __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
    __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
/* … */
  __pyx_mstate_global->__pyx_tuple[6] = PyTuple_Pack(2, __pyx_mstate_global->__pyx_n_u_CHARS, __pyx_mstate_global->__pyx_kp_u__9); if (unlikely(!__pyx_mstate_global->__pyx_tuple[6])) __PYX_ERR(0, 453, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_mstate_global->__pyx_tuple[6]);
  __Pyx_GIVEREF(__pyx_mstate_global->__pyx_tuple[6]);
```

</details>

L454  🟠  (score=9)
```python
        len_text -= (double_braces*2)
```
<details><summary>Show generated C (score=9)</summary>

```c
  __pyx_t_4 = __Pyx_PyLong_MultiplyObjC(__pyx_v_double_braces, __pyx_mstate_global->__pyx_int_2, 2, 0, 0); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 454, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_4);
  __pyx_t_5 = PyNumber_InPlaceSubtract(__pyx_v_len_text, __pyx_t_4); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 454, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_5);
  __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
  __Pyx_DECREF_SET(__pyx_v_len_text, __pyx_t_5);
  __pyx_t_5 = 0;
```

</details>

L455  ⚪  (score=0)
```python
```
L456  🟡  (score=2)
```python
        if len_text:
```
<details><summary>Show generated C (score=2)</summary>

```c
  __pyx_t_8 = __Pyx_PyObject_IsTrue(__pyx_v_len_text); if (unlikely((__pyx_t_8 < 0))) __PYX_ERR(0, 456, __pyx_L1_error)
  if (__pyx_t_8) {
/* … */
  }
```

</details>

L457  🟡  (score=4)
```python
            assert len_text == 1
```
<details><summary>Show generated C (score=4)</summary>

```c
    #ifndef CYTHON_WITHOUT_ASSERTIONS
    if (unlikely(__pyx_assertions_enabled())) {
      __pyx_t_8 = (__Pyx_PyLong_BoolEqObjC(__pyx_v_len_text, __pyx_mstate_global->__pyx_int_1, 1, 0)); if (unlikely((__pyx_t_8 < 0))) __PYX_ERR(0, 457, __pyx_L1_error)
      if (unlikely(!__pyx_t_8)) {
        __Pyx_Raise(((PyObject *)(((PyTypeObject*)PyExc_AssertionError))), 0, 0, 0);
        __PYX_ERR(0, 457, __pyx_L1_error)
      }
    }
    #else
    if ((1)); else __PYX_ERR(0, 457, __pyx_L1_error)
    #endif
```

</details>

L458  🟠  (score=5)
```python
            self._handle_open_single_ft_string_brace(started_ft_string_expr)
```
<details><summary>Show generated C (score=5)</summary>

```c
    __pyx_t_4 = __pyx_v_self;
    __Pyx_INCREF(__pyx_t_4);
    __pyx_t_6 = 0;
    {
      PyObject *__pyx_callargs[2] = {__pyx_t_4, __pyx_v_started_ft_string_expr};
      __pyx_t_5 = __Pyx_PyObject_FastCallMethod((PyObject*)__pyx_mstate_global->__pyx_n_u_handle_open_single_ft_string_br, __pyx_callargs+__pyx_t_6, (2-__pyx_t_6) | (1*__Pyx_PY_VECTORCALL_ARGUMENTS_OFFSET));
      __Pyx_XDECREF(__pyx_t_4); __pyx_t_4 = 0;
      if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 458, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_5);
    }
    __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
```

</details>

L459  ⚪  (score=0)
```python
```
L460  🔴  (score=41)
```python
    def _handle_close_single_ft_string_brace(self):
```
<details><summary>Show generated C (score=41)</summary>

```c
/* Python wrapper */
static PyObject *__pyx_pw_6Cython_8Compiler_8Scanning_12PyrexScanner_35_handle_close_single_ft_string_brace(PyObject *__pyx_self, 
#if CYTHON_METH_FASTCALL
PyObject *const *__pyx_args, Py_ssize_t __pyx_nargs, PyObject *__pyx_kwds
#else
PyObject *__pyx_args, PyObject *__pyx_kwds
#endif
); /*proto*/
PyDoc_STRVAR(__pyx_doc_6Cython_8Compiler_8Scanning_12PyrexScanner_34_handle_close_single_ft_string_brace, "File: Cython/Compiler/Scanning.py (starting at line 460)");
static PyMethodDef __pyx_mdef_6Cython_8Compiler_8Scanning_12PyrexScanner_35_handle_close_single_ft_string_brace = {"_handle_close_single_ft_string_brace", (PyCFunction)(void(*)(void))(__Pyx_PyCFunction_FastCallWithKeywords)__pyx_pw_6Cython_8Compiler_8Scanning_12PyrexScanner_35_handle_close_single_ft_string_brace, __Pyx_METH_FASTCALL|METH_KEYWORDS, __pyx_doc_6Cython_8Compiler_8Scanning_12PyrexScanner_34_handle_close_single_ft_string_brace};
static PyObject *__pyx_pw_6Cython_8Compiler_8Scanning_12PyrexScanner_35_handle_close_single_ft_string_brace(PyObject *__pyx_self, 
#if CYTHON_METH_FASTCALL
PyObject *const *__pyx_args, Py_ssize_t __pyx_nargs, PyObject *__pyx_kwds
#else
PyObject *__pyx_args, PyObject *__pyx_kwds
#endif
) {
  PyObject *__pyx_v_self = 0;
  #if !CYTHON_METH_FASTCALL
  CYTHON_UNUSED Py_ssize_t __pyx_nargs;
  #endif
  CYTHON_UNUSED PyObject *const *__pyx_kwvalues;
  PyObject *__pyx_r = 0;
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("_handle_close_single_ft_string_brace (wrapper)", 0);
  #if !CYTHON_METH_FASTCALL
  #if CYTHON_ASSUME_SAFE_SIZE
  __pyx_nargs = PyTuple_GET_SIZE(__pyx_args);
  #else
  __pyx_nargs = PyTuple_Size(__pyx_args); if (unlikely(__pyx_nargs < 0)) return NULL;
  #endif
  #endif
  __pyx_kwvalues = __Pyx_KwValues_FASTCALL(__pyx_args, __pyx_nargs);
  {
    PyObject ** const __pyx_pyargnames[] = {&__pyx_mstate_global->__pyx_n_u_self,0};
  PyObject* values[1] = {0};
    const Py_ssize_t __pyx_kwds_len = (__pyx_kwds) ? __Pyx_NumKwargs_FASTCALL(__pyx_kwds) : 0;
    if (unlikely(__pyx_kwds_len) < 0) __PYX_ERR(0, 460, __pyx_L3_error)
    if (__pyx_kwds_len > 0) {
      switch (__pyx_nargs) {
        case  1:
        values[0] = __Pyx_ArgRef_FASTCALL(__pyx_args, 0);
        if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[0])) __PYX_ERR(0, 460, __pyx_L3_error)
        CYTHON_FALLTHROUGH;
        case  0: break;
        default: goto __pyx_L5_argtuple_error;
      }
      const Py_ssize_t kwd_pos_args = __pyx_nargs;
      if (__Pyx_ParseKeywords(__pyx_kwds, __pyx_kwvalues, __pyx_pyargnames, 0, values, kwd_pos_args, __pyx_kwds_len, "_handle_close_single_ft_string_brace", 0) < (0)) __PYX_ERR(0, 460, __pyx_L3_error)
      for (Py_ssize_t i = __pyx_nargs; i < 1; i++) {
        if (unlikely(!values[i])) { __Pyx_RaiseArgtupleInvalid("_handle_close_single_ft_string_brace", 1, 1, 1, i); __PYX_ERR(0, 460, __pyx_L3_error) }
      }
    } else if (unlikely(__pyx_nargs != 1)) {
      goto __pyx_L5_argtuple_error;
    } else {
      values[0] = __Pyx_ArgRef_FASTCALL(__pyx_args, 0);
      if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[0])) __PYX_ERR(0, 460, __pyx_L3_error)
    }
    __pyx_v_self = values[0];
  }
  goto __pyx_L6_skip;
  __pyx_L5_argtuple_error:;
  __Pyx_RaiseArgtupleInvalid("_handle_close_single_ft_string_brace", 1, 1, 1, __pyx_nargs); __PYX_ERR(0, 460, __pyx_L3_error)
  __pyx_L6_skip:;
  goto __pyx_L4_argument_unpacking_done;
  __pyx_L3_error:;
  for (Py_ssize_t __pyx_temp=0; __pyx_temp < (Py_ssize_t)(sizeof(values)/sizeof(values[0])); ++__pyx_temp) {
    Py_XDECREF(values[__pyx_temp]);
  }
  __Pyx_AddTraceback("Cython.Compiler.Scanning.PyrexScanner._handle_close_single_ft_string_brace", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __Pyx_RefNannyFinishContext();
  return NULL;
  __pyx_L4_argument_unpacking_done:;
  __pyx_r = __pyx_pf_6Cython_8Compiler_8Scanning_12PyrexScanner_34_handle_close_single_ft_string_brace(__pyx_self, __pyx_v_self);
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

static PyObject *__pyx_pf_6Cython_8Compiler_8Scanning_12PyrexScanner_34_handle_close_single_ft_string_brace(CYTHON_UNUSED PyObject *__pyx_self, PyObject *__pyx_v_self) {
  PyObject *__pyx_v_ft_string_bracket_level = NULL;
  PyObject *__pyx_r = NULL;
/* … */
  /* function exit code */
  __pyx_r = Py_None; __Pyx_INCREF(Py_None);
  goto __pyx_L0;
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_t_1);
  __Pyx_XDECREF(__pyx_t_2);
  __Pyx_XDECREF(__pyx_t_3);
  __Pyx_XDECREF(__pyx_t_4);
  __Pyx_AddTraceback("Cython.Compiler.Scanning.PyrexScanner._handle_close_single_ft_string_brace", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_r = NULL;
  __pyx_L0:;
  __Pyx_XDECREF(__pyx_v_ft_string_bracket_level);
  __Pyx_XGIVEREF(__pyx_r);
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}
/* … */
  __pyx_t_7 = __Pyx_CyFunction_New(&__pyx_mdef_6Cython_8Compiler_8Scanning_12PyrexScanner_35_handle_close_single_ft_string_brace, 0, __pyx_mstate_global->__pyx_n_u_PyrexScanner__handle_close_singl, NULL, __pyx_mstate_global->__pyx_n_u_Cython_Compiler_Scanning, __pyx_mstate_global->__pyx_d, ((PyObject *)__pyx_mstate_global->__pyx_codeobj_tab[52])); if (unlikely(!__pyx_t_7)) __PYX_ERR(0, 460, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_7);
  #if CYTHON_COMPILING_IN_CPYTHON && PY_VERSION_HEX >= 0x030E0000
  PyUnstable_Object_EnableDeferredRefcount(__pyx_t_7);
  #endif
  if (__Pyx_SetNameInClass(__pyx_t_8, __pyx_mstate_global->__pyx_n_u_handle_close_single_ft_string_b, __pyx_t_7) < (0)) __PYX_ERR(0, 460, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_7); __pyx_t_7 = 0;
```

</details>

L461  🔴  (score=10)
```python
        ft_string_bracket_level = self.ft_string_state_stack[-1].bracket_nesting_level()
```
<details><summary>Show generated C (score=10)</summary>

```c
  __pyx_t_3 = __Pyx_PyObject_GetAttrStr(__pyx_v_self, __pyx_mstate_global->__pyx_n_u_ft_string_state_stack); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 461, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_3);
  __pyx_t_4 = __Pyx_GetItemInt(__pyx_t_3, -1L, long, 1, __Pyx_PyLong_From_long, 0, 0, 0, 1, __Pyx_ReferenceSharing_OwnStrongReference); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 461, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_4);
  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
  __pyx_t_2 = __pyx_t_4;
  __Pyx_INCREF(__pyx_t_2);
  __pyx_t_5 = 0;
  {
    PyObject *__pyx_callargs[2] = {__pyx_t_2, NULL};
    __pyx_t_1 = __Pyx_PyObject_FastCallMethod((PyObject*)__pyx_mstate_global->__pyx_n_u_bracket_nesting_level, __pyx_callargs+__pyx_t_5, (1-__pyx_t_5) | (1*__Pyx_PY_VECTORCALL_ARGUMENTS_OFFSET));
    __Pyx_XDECREF(__pyx_t_2); __pyx_t_2 = 0;
    __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
    if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 461, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_1);
  }
  __pyx_v_ft_string_bracket_level = __pyx_t_1;
  __pyx_t_1 = 0;
```

</details>

L462  🔴  (score=11)
```python
        if ft_string_bracket_level is None or self.bracket_nesting_level < ft_string_bracket_level:
```
<details><summary>Show generated C (score=11)</summary>

```c
  __pyx_t_7 = (__pyx_v_ft_string_bracket_level == Py_None);
  if (!__pyx_t_7) {
  } else {
    __pyx_t_6 = __pyx_t_7;
    goto __pyx_L4_bool_binop_done;
  }
  __pyx_t_1 = __Pyx_PyObject_GetAttrStr(__pyx_v_self, __pyx_mstate_global->__pyx_n_u_bracket_nesting_level); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 462, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __pyx_t_4 = PyObject_RichCompare(__pyx_t_1, __pyx_v_ft_string_bracket_level, Py_LT); __Pyx_XGOTREF(__pyx_t_4); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 462, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __pyx_t_7 = __Pyx_PyObject_IsTrue(__pyx_t_4); if (unlikely((__pyx_t_7 < 0))) __PYX_ERR(0, 462, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
  __pyx_t_6 = __pyx_t_7;
  __pyx_L4_bool_binop_done:;
  if (__pyx_t_6) {
/* … */
    goto __pyx_L3;
  }
```

</details>

L463  ⚪  (score=0)
```python
            # To help try to parse a little further, don't reduce the bracket
```
L464  ⚪  (score=0)
```python
            # nesting level more.
```
L465  🟡  (score=1)
```python
            self.error(
```
<details><summary>Show generated C (score=1)</summary>

```c
    __pyx_t_1 = __pyx_v_self;
    __Pyx_INCREF(__pyx_t_1);
```

</details>

L466  ⚪  (score=0)
```python
                # Unfortunately the scanner doesn't know which
```
L467  ⚪  (score=0)
```python
                "f-string or t-string: single '}' is not allowed",
```
L468  🟡  (score=4)
```python
                pos=self.get_current_scan_pos(),
```
<details><summary>Show generated C (score=4)</summary>

```c
    __pyx_t_3 = __pyx_v_self;
    __Pyx_INCREF(__pyx_t_3);
    __pyx_t_5 = 0;
    {
      PyObject *__pyx_callargs[2] = {__pyx_t_3, NULL};
      __pyx_t_2 = __Pyx_PyObject_FastCallMethod((PyObject*)__pyx_mstate_global->__pyx_n_u_get_current_scan_pos, __pyx_callargs+__pyx_t_5, (1-__pyx_t_5) | (1*__Pyx_PY_VECTORCALL_ARGUMENTS_OFFSET));
      __Pyx_XDECREF(__pyx_t_3); __pyx_t_3 = 0;
      if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 468, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_2);
    }
```

</details>

L469  🔴  (score=12)
```python
                fatal=False)
```
<details><summary>Show generated C (score=12)</summary>

```c
    __pyx_t_5 = 0;
    {
      PyObject *__pyx_callargs[2 + ((CYTHON_VECTORCALL) ? 2 : 0)] = {__pyx_t_1, __pyx_mstate_global->__pyx_kp_u_f_string_or_t_string_single_is_n};
      __pyx_t_3 = __Pyx_MakeVectorcallBuilderKwds(2); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 465, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_3);
      if (__Pyx_VectorcallBuilder_AddArg(__pyx_mstate_global->__pyx_n_u_pos, __pyx_t_2, __pyx_t_3, __pyx_callargs+2, 0) < (0)) __PYX_ERR(0, 465, __pyx_L1_error)
      if (__Pyx_VectorcallBuilder_AddArg(__pyx_mstate_global->__pyx_n_u_fatal, Py_False, __pyx_t_3, __pyx_callargs+2, 1) < (0)) __PYX_ERR(0, 465, __pyx_L1_error)
      __pyx_t_4 = __Pyx_Object_VectorcallMethod_CallFromBuilder((PyObject*)__pyx_mstate_global->__pyx_n_u_error, __pyx_callargs+__pyx_t_5, (2-__pyx_t_5) | (1*__Pyx_PY_VECTORCALL_ARGUMENTS_OFFSET), __pyx_t_3);
      __Pyx_XDECREF(__pyx_t_1); __pyx_t_1 = 0;
      __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
      __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
      if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 465, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_4);
    }
    __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
```

</details>

L470  🔴  (score=11)
```python
            self.produce('}', '}')
```
<details><summary>Show generated C (score=11)</summary>

```c
    __pyx_t_4 = __Pyx_PyObject_GetAttrStr(__pyx_v_self, __pyx_mstate_global->__pyx_n_u_produce); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 470, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_4);
    __pyx_t_3 = __Pyx_PyObject_Call(__pyx_t_4, __pyx_mstate_global->__pyx_tuple[7], NULL); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 470, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_3);
    __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
    __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
/* … */
  __pyx_mstate_global->__pyx_tuple[7] = PyTuple_Pack(2, __pyx_mstate_global->__pyx_kp_u__8, __pyx_mstate_global->__pyx_kp_u__8); if (unlikely(!__pyx_mstate_global->__pyx_tuple[7])) __PYX_ERR(0, 470, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_mstate_global->__pyx_tuple[7]);
  __Pyx_GIVEREF(__pyx_mstate_global->__pyx_tuple[7]);
```

</details>

L471  ⚪  (score=0)
```python
        else:
```
L472  🔴  (score=10)
```python
            self.produce(self.close_brace_action('}'), '}')
```
<details><summary>Show generated C (score=10)</summary>

```c
  /*else*/ {
    __pyx_t_4 = __pyx_v_self;
    __Pyx_INCREF(__pyx_t_4);
    __pyx_t_1 = __pyx_v_self;
    __Pyx_INCREF(__pyx_t_1);
    __pyx_t_5 = 0;
    {
      PyObject *__pyx_callargs[2] = {__pyx_t_1, __pyx_mstate_global->__pyx_kp_u__8};
      __pyx_t_2 = __Pyx_PyObject_FastCallMethod((PyObject*)__pyx_mstate_global->__pyx_n_u_close_brace_action, __pyx_callargs+__pyx_t_5, (2-__pyx_t_5) | (1*__Pyx_PY_VECTORCALL_ARGUMENTS_OFFSET));
      __Pyx_XDECREF(__pyx_t_1); __pyx_t_1 = 0;
      if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 472, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_2);
    }
    __pyx_t_5 = 0;
    {
      PyObject *__pyx_callargs[3] = {__pyx_t_4, __pyx_t_2, __pyx_mstate_global->__pyx_kp_u__8};
      __pyx_t_3 = __Pyx_PyObject_FastCallMethod((PyObject*)__pyx_mstate_global->__pyx_n_u_produce, __pyx_callargs+__pyx_t_5, (3-__pyx_t_5) | (1*__Pyx_PY_VECTORCALL_ARGUMENTS_OFFSET));
      __Pyx_XDECREF(__pyx_t_4); __pyx_t_4 = 0;
      __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
      if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 472, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_3);
    }
    __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
  }
  __pyx_L3:;
```

</details>

L473  ⚪  (score=0)
```python
```
L474  🔴  (score=47)
```python
    def close_ft_string_brace_action(self, text):
```
<details><summary>Show generated C (score=47)</summary>

```c
/* Python wrapper */
static PyObject *__pyx_pw_6Cython_8Compiler_8Scanning_12PyrexScanner_37close_ft_string_brace_action(PyObject *__pyx_self, 
#if CYTHON_METH_FASTCALL
PyObject *const *__pyx_args, Py_ssize_t __pyx_nargs, PyObject *__pyx_kwds
#else
PyObject *__pyx_args, PyObject *__pyx_kwds
#endif
); /*proto*/
PyDoc_STRVAR(__pyx_doc_6Cython_8Compiler_8Scanning_12PyrexScanner_36close_ft_string_brace_action, "File: Cython/Compiler/Scanning.py (starting at line 474)");
static PyMethodDef __pyx_mdef_6Cython_8Compiler_8Scanning_12PyrexScanner_37close_ft_string_brace_action = {"close_ft_string_brace_action", (PyCFunction)(void(*)(void))(__Pyx_PyCFunction_FastCallWithKeywords)__pyx_pw_6Cython_8Compiler_8Scanning_12PyrexScanner_37close_ft_string_brace_action, __Pyx_METH_FASTCALL|METH_KEYWORDS, __pyx_doc_6Cython_8Compiler_8Scanning_12PyrexScanner_36close_ft_string_brace_action};
static PyObject *__pyx_pw_6Cython_8Compiler_8Scanning_12PyrexScanner_37close_ft_string_brace_action(PyObject *__pyx_self, 
#if CYTHON_METH_FASTCALL
PyObject *const *__pyx_args, Py_ssize_t __pyx_nargs, PyObject *__pyx_kwds
#else
PyObject *__pyx_args, PyObject *__pyx_kwds
#endif
) {
  PyObject *__pyx_v_self = 0;
  PyObject *__pyx_v_text = 0;
  #if !CYTHON_METH_FASTCALL
  CYTHON_UNUSED Py_ssize_t __pyx_nargs;
  #endif
  CYTHON_UNUSED PyObject *const *__pyx_kwvalues;
  PyObject *__pyx_r = 0;
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("close_ft_string_brace_action (wrapper)", 0);
  #if !CYTHON_METH_FASTCALL
  #if CYTHON_ASSUME_SAFE_SIZE
  __pyx_nargs = PyTuple_GET_SIZE(__pyx_args);
  #else
  __pyx_nargs = PyTuple_Size(__pyx_args); if (unlikely(__pyx_nargs < 0)) return NULL;
  #endif
  #endif
  __pyx_kwvalues = __Pyx_KwValues_FASTCALL(__pyx_args, __pyx_nargs);
  {
    PyObject ** const __pyx_pyargnames[] = {&__pyx_mstate_global->__pyx_n_u_self,&__pyx_mstate_global->__pyx_n_u_text,0};
  PyObject* values[2] = {0,0};
    const Py_ssize_t __pyx_kwds_len = (__pyx_kwds) ? __Pyx_NumKwargs_FASTCALL(__pyx_kwds) : 0;
    if (unlikely(__pyx_kwds_len) < 0) __PYX_ERR(0, 474, __pyx_L3_error)
    if (__pyx_kwds_len > 0) {
      switch (__pyx_nargs) {
        case  2:
        values[1] = __Pyx_ArgRef_FASTCALL(__pyx_args, 1);
        if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[1])) __PYX_ERR(0, 474, __pyx_L3_error)
        CYTHON_FALLTHROUGH;
        case  1:
        values[0] = __Pyx_ArgRef_FASTCALL(__pyx_args, 0);
        if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[0])) __PYX_ERR(0, 474, __pyx_L3_error)
        CYTHON_FALLTHROUGH;
        case  0: break;
        default: goto __pyx_L5_argtuple_error;
      }
      const Py_ssize_t kwd_pos_args = __pyx_nargs;
      if (__Pyx_ParseKeywords(__pyx_kwds, __pyx_kwvalues, __pyx_pyargnames, 0, values, kwd_pos_args, __pyx_kwds_len, "close_ft_string_brace_action", 0) < (0)) __PYX_ERR(0, 474, __pyx_L3_error)
      for (Py_ssize_t i = __pyx_nargs; i < 2; i++) {
        if (unlikely(!values[i])) { __Pyx_RaiseArgtupleInvalid("close_ft_string_brace_action", 1, 2, 2, i); __PYX_ERR(0, 474, __pyx_L3_error) }
      }
    } else if (unlikely(__pyx_nargs != 2)) {
      goto __pyx_L5_argtuple_error;
    } else {
      values[0] = __Pyx_ArgRef_FASTCALL(__pyx_args, 0);
      if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[0])) __PYX_ERR(0, 474, __pyx_L3_error)
      values[1] = __Pyx_ArgRef_FASTCALL(__pyx_args, 1);
      if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[1])) __PYX_ERR(0, 474, __pyx_L3_error)
    }
    __pyx_v_self = values[0];
    __pyx_v_text = values[1];
  }
  goto __pyx_L6_skip;
  __pyx_L5_argtuple_error:;
  __Pyx_RaiseArgtupleInvalid("close_ft_string_brace_action", 1, 2, 2, __pyx_nargs); __PYX_ERR(0, 474, __pyx_L3_error)
  __pyx_L6_skip:;
  goto __pyx_L4_argument_unpacking_done;
  __pyx_L3_error:;
  for (Py_ssize_t __pyx_temp=0; __pyx_temp < (Py_ssize_t)(sizeof(values)/sizeof(values[0])); ++__pyx_temp) {
    Py_XDECREF(values[__pyx_temp]);
  }
  __Pyx_AddTraceback("Cython.Compiler.Scanning.PyrexScanner.close_ft_string_brace_action", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __Pyx_RefNannyFinishContext();
  return NULL;
  __pyx_L4_argument_unpacking_done:;
  __pyx_r = __pyx_pf_6Cython_8Compiler_8Scanning_12PyrexScanner_36close_ft_string_brace_action(__pyx_self, __pyx_v_self, __pyx_v_text);
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

static PyObject *__pyx_pf_6Cython_8Compiler_8Scanning_12PyrexScanner_36close_ft_string_brace_action(CYTHON_UNUSED PyObject *__pyx_self, PyObject *__pyx_v_self, PyObject *__pyx_v_text) {
  PyObject *__pyx_v_len_text = NULL;
  PyObject *__pyx_v_double_braces = NULL;
  CYTHON_UNUSED PyObject *__pyx_v__ = NULL;
  PyObject *__pyx_r = NULL;
/* … */
  /* function exit code */
  __pyx_r = Py_None; __Pyx_INCREF(Py_None);
  goto __pyx_L0;
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_t_2);
  __Pyx_XDECREF(__pyx_t_5);
  __Pyx_XDECREF(__pyx_t_6);
  __Pyx_XDECREF(__pyx_t_7);
  __Pyx_AddTraceback("Cython.Compiler.Scanning.PyrexScanner.close_ft_string_brace_action", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_r = NULL;
  __pyx_L0:;
  __Pyx_XDECREF(__pyx_v_len_text);
  __Pyx_XDECREF(__pyx_v_double_braces);
  __Pyx_XDECREF(__pyx_v__);
  __Pyx_XGIVEREF(__pyx_r);
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}
/* … */
  __pyx_t_7 = __Pyx_CyFunction_New(&__pyx_mdef_6Cython_8Compiler_8Scanning_12PyrexScanner_37close_ft_string_brace_action, 0, __pyx_mstate_global->__pyx_n_u_PyrexScanner_close_ft_string_bra, NULL, __pyx_mstate_global->__pyx_n_u_Cython_Compiler_Scanning, __pyx_mstate_global->__pyx_d, ((PyObject *)__pyx_mstate_global->__pyx_codeobj_tab[53])); if (unlikely(!__pyx_t_7)) __PYX_ERR(0, 474, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_7);
  #if CYTHON_COMPILING_IN_CPYTHON && PY_VERSION_HEX >= 0x030E0000
  PyUnstable_Object_EnableDeferredRefcount(__pyx_t_7);
  #endif
  if (__Pyx_SetNameInClass(__pyx_t_8, __pyx_mstate_global->__pyx_n_u_close_ft_string_brace_action, __pyx_t_7) < (0)) __PYX_ERR(0, 474, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_7); __pyx_t_7 = 0;
```

</details>

L475  🔴  (score=10)
```python
        len_text = len(text)
```
<details><summary>Show generated C (score=10)</summary>

```c
  __pyx_t_1 = PyObject_Length(__pyx_v_text); if (unlikely(__pyx_t_1 == ((Py_ssize_t)-1))) __PYX_ERR(0, 475, __pyx_L1_error)
  __pyx_t_2 = PyLong_FromSsize_t(__pyx_t_1); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 475, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __pyx_v_len_text = __pyx_t_2;
  __pyx_t_2 = 0;
```

</details>

L476  🔴  (score=15)
```python
        while len_text and self.ft_string_state_stack[-1].in_format_specifier():
```
<details><summary>Show generated C (score=15)</summary>

```c
  while (1) {
    __pyx_t_4 = __Pyx_PyObject_IsTrue(__pyx_v_len_text); if (unlikely((__pyx_t_4 < 0))) __PYX_ERR(0, 476, __pyx_L1_error)
    if (__pyx_t_4) {
    } else {
      __pyx_t_3 = __pyx_t_4;
      goto __pyx_L5_bool_binop_done;
    }
    __pyx_t_6 = __Pyx_PyObject_GetAttrStr(__pyx_v_self, __pyx_mstate_global->__pyx_n_u_ft_string_state_stack); if (unlikely(!__pyx_t_6)) __PYX_ERR(0, 476, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_6);
    __pyx_t_7 = __Pyx_GetItemInt(__pyx_t_6, -1L, long, 1, __Pyx_PyLong_From_long, 0, 0, 0, 1, __Pyx_ReferenceSharing_OwnStrongReference); if (unlikely(!__pyx_t_7)) __PYX_ERR(0, 476, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_7);
    __Pyx_DECREF(__pyx_t_6); __pyx_t_6 = 0;
    __pyx_t_5 = __pyx_t_7;
    __Pyx_INCREF(__pyx_t_5);
    __pyx_t_8 = 0;
    {
      PyObject *__pyx_callargs[2] = {__pyx_t_5, NULL};
      __pyx_t_2 = __Pyx_PyObject_FastCallMethod((PyObject*)__pyx_mstate_global->__pyx_n_u_in_format_specifier, __pyx_callargs+__pyx_t_8, (1-__pyx_t_8) | (1*__Pyx_PY_VECTORCALL_ARGUMENTS_OFFSET));
      __Pyx_XDECREF(__pyx_t_5); __pyx_t_5 = 0;
      __Pyx_DECREF(__pyx_t_7); __pyx_t_7 = 0;
      if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 476, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_2);
    }
    __pyx_t_4 = __Pyx_PyObject_IsTrue(__pyx_t_2); if (unlikely((__pyx_t_4 < 0))) __PYX_ERR(0, 476, __pyx_L1_error)
    __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
    __pyx_t_3 = __pyx_t_4;
    __pyx_L5_bool_binop_done:;
    if (!__pyx_t_3) break;
```

</details>

L477  🟠  (score=5)
```python
            self._handle_close_single_ft_string_brace()
```
<details><summary>Show generated C (score=5)</summary>

```c
    __pyx_t_7 = __pyx_v_self;
    __Pyx_INCREF(__pyx_t_7);
    __pyx_t_8 = 0;
    {
      PyObject *__pyx_callargs[2] = {__pyx_t_7, NULL};
      __pyx_t_2 = __Pyx_PyObject_FastCallMethod((PyObject*)__pyx_mstate_global->__pyx_n_u_handle_close_single_ft_string_b, __pyx_callargs+__pyx_t_8, (1-__pyx_t_8) | (1*__Pyx_PY_VECTORCALL_ARGUMENTS_OFFSET));
      __Pyx_XDECREF(__pyx_t_7); __pyx_t_7 = 0;
      if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 477, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_2);
    }
    __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
```

</details>

L478  🟡  (score=3)
```python
            len_text -= 1
```
<details><summary>Show generated C (score=3)</summary>

```c
    __pyx_t_2 = __Pyx_PyLong_SubtractObjC(__pyx_v_len_text, __pyx_mstate_global->__pyx_int_1, 1, 1, 0); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 478, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_2);
    __Pyx_DECREF_SET(__pyx_v_len_text, __pyx_t_2);
    __pyx_t_2 = 0;
  }
```

</details>

L479  ⚪  (score=0)
```python
```
L480  🟡  (score=2)
```python
        double_braces = len_text // 2
```
<details><summary>Show generated C (score=2)</summary>

```c
  __pyx_t_2 = __Pyx_PyLong_FloorDivideObjC(__pyx_v_len_text, __pyx_mstate_global->__pyx_int_2, 2, 0, 0); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 480, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __pyx_v_double_braces = __pyx_t_2;
  __pyx_t_2 = 0;
```

</details>

L481  🔴  (score=25)
```python
        for _ in range(double_braces):
```
<details><summary>Show generated C (score=25)</summary>

```c
  __pyx_t_7 = NULL;
  __pyx_t_8 = 1;
  {
    PyObject *__pyx_callargs[2] = {__pyx_t_7, __pyx_v_double_braces};
    __pyx_t_2 = __Pyx_PyObject_FastCall((PyObject*)(&PyRange_Type), __pyx_callargs+__pyx_t_8, (2-__pyx_t_8) | (__pyx_t_8*__Pyx_PY_VECTORCALL_ARGUMENTS_OFFSET));
    __Pyx_XDECREF(__pyx_t_7); __pyx_t_7 = 0;
    if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 481, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_2);
  }
  __pyx_t_7 = PyObject_GetIter(__pyx_t_2); if (unlikely(!__pyx_t_7)) __PYX_ERR(0, 481, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_7);
  __pyx_t_9 = (CYTHON_COMPILING_IN_LIMITED_API) ? PyIter_Next : __Pyx_PyObject_GetIterNextFunc(__pyx_t_7); if (unlikely(!__pyx_t_9)) __PYX_ERR(0, 481, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  for (;;) {
    {
      __pyx_t_2 = __pyx_t_9(__pyx_t_7);
      if (unlikely(!__pyx_t_2)) {
        PyObject* exc_type = PyErr_Occurred();
        if (exc_type) {
          if (unlikely(!__Pyx_PyErr_GivenExceptionMatches(exc_type, PyExc_StopIteration))) __PYX_ERR(0, 481, __pyx_L1_error)
          PyErr_Clear();
        }
        break;
      }
    }
    __Pyx_GOTREF(__pyx_t_2);
    __Pyx_XDECREF_SET(__pyx_v__, __pyx_t_2);
    __pyx_t_2 = 0;
/* … */
  }
  __Pyx_DECREF(__pyx_t_7); __pyx_t_7 = 0;
```

</details>

L482  🔴  (score=11)
```python
            self.produce('CHARS', '}')
```
<details><summary>Show generated C (score=11)</summary>

```c
    __pyx_t_2 = __Pyx_PyObject_GetAttrStr(__pyx_v_self, __pyx_mstate_global->__pyx_n_u_produce); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 482, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_2);
    __pyx_t_5 = __Pyx_PyObject_Call(__pyx_t_2, __pyx_mstate_global->__pyx_tuple[8], NULL); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 482, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_5);
    __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
    __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
/* … */
  __pyx_mstate_global->__pyx_tuple[8] = PyTuple_Pack(2, __pyx_mstate_global->__pyx_n_u_CHARS, __pyx_mstate_global->__pyx_kp_u__8); if (unlikely(!__pyx_mstate_global->__pyx_tuple[8])) __PYX_ERR(0, 482, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_mstate_global->__pyx_tuple[8]);
  __Pyx_GIVEREF(__pyx_mstate_global->__pyx_tuple[8]);
```

</details>

L483  🟠  (score=9)
```python
        len_text -= double_braces*2
```
<details><summary>Show generated C (score=9)</summary>

```c
  __pyx_t_7 = __Pyx_PyLong_MultiplyObjC(__pyx_v_double_braces, __pyx_mstate_global->__pyx_int_2, 2, 0, 0); if (unlikely(!__pyx_t_7)) __PYX_ERR(0, 483, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_7);
  __pyx_t_5 = PyNumber_InPlaceSubtract(__pyx_v_len_text, __pyx_t_7); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 483, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_5);
  __Pyx_DECREF(__pyx_t_7); __pyx_t_7 = 0;
  __Pyx_DECREF_SET(__pyx_v_len_text, __pyx_t_5);
  __pyx_t_5 = 0;
```

</details>

L484  ⚪  (score=0)
```python
```
L485  🟡  (score=2)
```python
        if len_text:
```
<details><summary>Show generated C (score=2)</summary>

```c
  __pyx_t_3 = __Pyx_PyObject_IsTrue(__pyx_v_len_text); if (unlikely((__pyx_t_3 < 0))) __PYX_ERR(0, 485, __pyx_L1_error)
  if (__pyx_t_3) {
/* … */
  }
```

</details>

L486  🟠  (score=5)
```python
            self._handle_close_single_ft_string_brace()
```
<details><summary>Show generated C (score=5)</summary>

```c
    __pyx_t_7 = __pyx_v_self;
    __Pyx_INCREF(__pyx_t_7);
    __pyx_t_8 = 0;
    {
      PyObject *__pyx_callargs[2] = {__pyx_t_7, NULL};
      __pyx_t_5 = __Pyx_PyObject_FastCallMethod((PyObject*)__pyx_mstate_global->__pyx_n_u_handle_close_single_ft_string_b, __pyx_callargs+__pyx_t_8, (1-__pyx_t_8) | (1*__Pyx_PY_VECTORCALL_ARGUMENTS_OFFSET));
      __Pyx_XDECREF(__pyx_t_7); __pyx_t_7 = 0;
      if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 486, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_5);
    }
    __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
```

</details>

L487  ⚪  (score=0)
```python
```
L488  🔴  (score=42)
```python
    def unclosed_string_action(self, text):
```
<details><summary>Show generated C (score=42)</summary>

```c
/* Python wrapper */
static PyObject *__pyx_pw_6Cython_8Compiler_8Scanning_12PyrexScanner_39unclosed_string_action(PyObject *__pyx_self, 
#if CYTHON_METH_FASTCALL
PyObject *const *__pyx_args, Py_ssize_t __pyx_nargs, PyObject *__pyx_kwds
#else
PyObject *__pyx_args, PyObject *__pyx_kwds
#endif
); /*proto*/
PyDoc_STRVAR(__pyx_doc_6Cython_8Compiler_8Scanning_12PyrexScanner_38unclosed_string_action, "File: Cython/Compiler/Scanning.py (starting at line 488)");
static PyMethodDef __pyx_mdef_6Cython_8Compiler_8Scanning_12PyrexScanner_39unclosed_string_action = {"unclosed_string_action", (PyCFunction)(void(*)(void))(__Pyx_PyCFunction_FastCallWithKeywords)__pyx_pw_6Cython_8Compiler_8Scanning_12PyrexScanner_39unclosed_string_action, __Pyx_METH_FASTCALL|METH_KEYWORDS, __pyx_doc_6Cython_8Compiler_8Scanning_12PyrexScanner_38unclosed_string_action};
static PyObject *__pyx_pw_6Cython_8Compiler_8Scanning_12PyrexScanner_39unclosed_string_action(PyObject *__pyx_self, 
#if CYTHON_METH_FASTCALL
PyObject *const *__pyx_args, Py_ssize_t __pyx_nargs, PyObject *__pyx_kwds
#else
PyObject *__pyx_args, PyObject *__pyx_kwds
#endif
) {
  PyObject *__pyx_v_self = 0;
  PyObject *__pyx_v_text = 0;
  #if !CYTHON_METH_FASTCALL
  CYTHON_UNUSED Py_ssize_t __pyx_nargs;
  #endif
  CYTHON_UNUSED PyObject *const *__pyx_kwvalues;
  PyObject *__pyx_r = 0;
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("unclosed_string_action (wrapper)", 0);
  #if !CYTHON_METH_FASTCALL
  #if CYTHON_ASSUME_SAFE_SIZE
  __pyx_nargs = PyTuple_GET_SIZE(__pyx_args);
  #else
  __pyx_nargs = PyTuple_Size(__pyx_args); if (unlikely(__pyx_nargs < 0)) return NULL;
  #endif
  #endif
  __pyx_kwvalues = __Pyx_KwValues_FASTCALL(__pyx_args, __pyx_nargs);
  {
    PyObject ** const __pyx_pyargnames[] = {&__pyx_mstate_global->__pyx_n_u_self,&__pyx_mstate_global->__pyx_n_u_text,0};
  PyObject* values[2] = {0,0};
    const Py_ssize_t __pyx_kwds_len = (__pyx_kwds) ? __Pyx_NumKwargs_FASTCALL(__pyx_kwds) : 0;
    if (unlikely(__pyx_kwds_len) < 0) __PYX_ERR(0, 488, __pyx_L3_error)
    if (__pyx_kwds_len > 0) {
      switch (__pyx_nargs) {
        case  2:
        values[1] = __Pyx_ArgRef_FASTCALL(__pyx_args, 1);
        if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[1])) __PYX_ERR(0, 488, __pyx_L3_error)
        CYTHON_FALLTHROUGH;
        case  1:
        values[0] = __Pyx_ArgRef_FASTCALL(__pyx_args, 0);
        if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[0])) __PYX_ERR(0, 488, __pyx_L3_error)
        CYTHON_FALLTHROUGH;
        case  0: break;
        default: goto __pyx_L5_argtuple_error;
      }
      const Py_ssize_t kwd_pos_args = __pyx_nargs;
      if (__Pyx_ParseKeywords(__pyx_kwds, __pyx_kwvalues, __pyx_pyargnames, 0, values, kwd_pos_args, __pyx_kwds_len, "unclosed_string_action", 0) < (0)) __PYX_ERR(0, 488, __pyx_L3_error)
      for (Py_ssize_t i = __pyx_nargs; i < 2; i++) {
        if (unlikely(!values[i])) { __Pyx_RaiseArgtupleInvalid("unclosed_string_action", 1, 2, 2, i); __PYX_ERR(0, 488, __pyx_L3_error) }
      }
    } else if (unlikely(__pyx_nargs != 2)) {
      goto __pyx_L5_argtuple_error;
    } else {
      values[0] = __Pyx_ArgRef_FASTCALL(__pyx_args, 0);
      if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[0])) __PYX_ERR(0, 488, __pyx_L3_error)
      values[1] = __Pyx_ArgRef_FASTCALL(__pyx_args, 1);
      if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[1])) __PYX_ERR(0, 488, __pyx_L3_error)
    }
    __pyx_v_self = values[0];
    __pyx_v_text = values[1];
  }
  goto __pyx_L6_skip;
  __pyx_L5_argtuple_error:;
  __Pyx_RaiseArgtupleInvalid("unclosed_string_action", 1, 2, 2, __pyx_nargs); __PYX_ERR(0, 488, __pyx_L3_error)
  __pyx_L6_skip:;
  goto __pyx_L4_argument_unpacking_done;
  __pyx_L3_error:;
  for (Py_ssize_t __pyx_temp=0; __pyx_temp < (Py_ssize_t)(sizeof(values)/sizeof(values[0])); ++__pyx_temp) {
    Py_XDECREF(values[__pyx_temp]);
  }
  __Pyx_AddTraceback("Cython.Compiler.Scanning.PyrexScanner.unclosed_string_action", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __Pyx_RefNannyFinishContext();
  return NULL;
  __pyx_L4_argument_unpacking_done:;
  __pyx_r = __pyx_pf_6Cython_8Compiler_8Scanning_12PyrexScanner_38unclosed_string_action(__pyx_self, __pyx_v_self, __pyx_v_text);
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

static PyObject *__pyx_pf_6Cython_8Compiler_8Scanning_12PyrexScanner_38unclosed_string_action(CYTHON_UNUSED PyObject *__pyx_self, PyObject *__pyx_v_self, PyObject *__pyx_v_text) {
  PyObject *__pyx_r = NULL;
/* … */
  /* function exit code */
  __pyx_r = Py_None; __Pyx_INCREF(Py_None);
  goto __pyx_L0;
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_t_1);
  __Pyx_XDECREF(__pyx_t_2);
  __Pyx_AddTraceback("Cython.Compiler.Scanning.PyrexScanner.unclosed_string_action", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_r = NULL;
  __pyx_L0:;
  __Pyx_XGIVEREF(__pyx_r);
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}
/* … */
  __pyx_t_7 = __Pyx_CyFunction_New(&__pyx_mdef_6Cython_8Compiler_8Scanning_12PyrexScanner_39unclosed_string_action, 0, __pyx_mstate_global->__pyx_n_u_PyrexScanner_unclosed_string_act, NULL, __pyx_mstate_global->__pyx_n_u_Cython_Compiler_Scanning, __pyx_mstate_global->__pyx_d, ((PyObject *)__pyx_mstate_global->__pyx_codeobj_tab[54])); if (unlikely(!__pyx_t_7)) __PYX_ERR(0, 488, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_7);
  #if CYTHON_COMPILING_IN_CPYTHON && PY_VERSION_HEX >= 0x030E0000
  PyUnstable_Object_EnableDeferredRefcount(__pyx_t_7);
  #endif
  if (__Pyx_SetNameInClass(__pyx_t_8, __pyx_mstate_global->__pyx_n_u_unclosed_string_action, __pyx_t_7) < (0)) __PYX_ERR(0, 488, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_7); __pyx_t_7 = 0;
```

</details>

L489  🟠  (score=5)
```python
        self.end_string_action(text)
```
<details><summary>Show generated C (score=5)</summary>

```c
  __pyx_t_2 = __pyx_v_self;
  __Pyx_INCREF(__pyx_t_2);
  __pyx_t_3 = 0;
  {
    PyObject *__pyx_callargs[2] = {__pyx_t_2, __pyx_v_text};
    __pyx_t_1 = __Pyx_PyObject_FastCallMethod((PyObject*)__pyx_mstate_global->__pyx_n_u_end_string_action, __pyx_callargs+__pyx_t_3, (2-__pyx_t_3) | (1*__Pyx_PY_VECTORCALL_ARGUMENTS_OFFSET));
    __Pyx_XDECREF(__pyx_t_2); __pyx_t_2 = 0;
    if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 489, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_1);
  }
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
```

</details>

L490  🟠  (score=5)
```python
        self.error_at_scanpos("Unclosed string literal")
```
<details><summary>Show generated C (score=5)</summary>

```c
  __pyx_t_2 = __pyx_v_self;
  __Pyx_INCREF(__pyx_t_2);
  __pyx_t_3 = 0;
  {
    PyObject *__pyx_callargs[2] = {__pyx_t_2, __pyx_mstate_global->__pyx_kp_u_Unclosed_string_literal};
    __pyx_t_1 = __Pyx_PyObject_FastCallMethod((PyObject*)__pyx_mstate_global->__pyx_n_u_error_at_scanpos, __pyx_callargs+__pyx_t_3, (2-__pyx_t_3) | (1*__Pyx_PY_VECTORCALL_ARGUMENTS_OFFSET));
    __Pyx_XDECREF(__pyx_t_2); __pyx_t_2 = 0;
    if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 490, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_1);
  }
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
```

</details>

L491  ⚪  (score=0)
```python
```
L492  🔴  (score=76)
```python
    def indentation_action(self, text: str):
```
<details><summary>Show generated C (score=76)</summary>

```c
/* Python wrapper */
static PyObject *__pyx_pw_6Cython_8Compiler_8Scanning_12PyrexScanner_41indentation_action(PyObject *__pyx_self, 
#if CYTHON_METH_FASTCALL
PyObject *const *__pyx_args, Py_ssize_t __pyx_nargs, PyObject *__pyx_kwds
#else
PyObject *__pyx_args, PyObject *__pyx_kwds
#endif
); /*proto*/
PyDoc_STRVAR(__pyx_doc_6Cython_8Compiler_8Scanning_12PyrexScanner_40indentation_action, "File: Cython/Compiler/Scanning.py (starting at line 492)");
static PyMethodDef __pyx_mdef_6Cython_8Compiler_8Scanning_12PyrexScanner_41indentation_action = {"indentation_action", (PyCFunction)(void(*)(void))(__Pyx_PyCFunction_FastCallWithKeywords)__pyx_pw_6Cython_8Compiler_8Scanning_12PyrexScanner_41indentation_action, __Pyx_METH_FASTCALL|METH_KEYWORDS, __pyx_doc_6Cython_8Compiler_8Scanning_12PyrexScanner_40indentation_action};
static PyObject *__pyx_pw_6Cython_8Compiler_8Scanning_12PyrexScanner_41indentation_action(PyObject *__pyx_self, 
#if CYTHON_METH_FASTCALL
PyObject *const *__pyx_args, Py_ssize_t __pyx_nargs, PyObject *__pyx_kwds
#else
PyObject *__pyx_args, PyObject *__pyx_kwds
#endif
) {
  PyObject *__pyx_v_self = 0;
  PyObject *__pyx_v_text = 0;
  #if !CYTHON_METH_FASTCALL
  CYTHON_UNUSED Py_ssize_t __pyx_nargs;
  #endif
  CYTHON_UNUSED PyObject *const *__pyx_kwvalues;
  PyObject *__pyx_r = 0;
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("indentation_action (wrapper)", 0);
  #if !CYTHON_METH_FASTCALL
  #if CYTHON_ASSUME_SAFE_SIZE
  __pyx_nargs = PyTuple_GET_SIZE(__pyx_args);
  #else
  __pyx_nargs = PyTuple_Size(__pyx_args); if (unlikely(__pyx_nargs < 0)) return NULL;
  #endif
  #endif
  __pyx_kwvalues = __Pyx_KwValues_FASTCALL(__pyx_args, __pyx_nargs);
  {
    PyObject ** const __pyx_pyargnames[] = {&__pyx_mstate_global->__pyx_n_u_self,&__pyx_mstate_global->__pyx_n_u_text,0};
  PyObject* values[2] = {0,0};
    const Py_ssize_t __pyx_kwds_len = (__pyx_kwds) ? __Pyx_NumKwargs_FASTCALL(__pyx_kwds) : 0;
    if (unlikely(__pyx_kwds_len) < 0) __PYX_ERR(0, 492, __pyx_L3_error)
    if (__pyx_kwds_len > 0) {
      switch (__pyx_nargs) {
        case  2:
        values[1] = __Pyx_ArgRef_FASTCALL(__pyx_args, 1);
        if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[1])) __PYX_ERR(0, 492, __pyx_L3_error)
        CYTHON_FALLTHROUGH;
        case  1:
        values[0] = __Pyx_ArgRef_FASTCALL(__pyx_args, 0);
        if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[0])) __PYX_ERR(0, 492, __pyx_L3_error)
        CYTHON_FALLTHROUGH;
        case  0: break;
        default: goto __pyx_L5_argtuple_error;
      }
      const Py_ssize_t kwd_pos_args = __pyx_nargs;
      if (__Pyx_ParseKeywords(__pyx_kwds, __pyx_kwvalues, __pyx_pyargnames, 0, values, kwd_pos_args, __pyx_kwds_len, "indentation_action", 0) < (0)) __PYX_ERR(0, 492, __pyx_L3_error)
      for (Py_ssize_t i = __pyx_nargs; i < 2; i++) {
        if (unlikely(!values[i])) { __Pyx_RaiseArgtupleInvalid("indentation_action", 1, 2, 2, i); __PYX_ERR(0, 492, __pyx_L3_error) }
      }
    } else if (unlikely(__pyx_nargs != 2)) {
      goto __pyx_L5_argtuple_error;
    } else {
      values[0] = __Pyx_ArgRef_FASTCALL(__pyx_args, 0);
      if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[0])) __PYX_ERR(0, 492, __pyx_L3_error)
      values[1] = __Pyx_ArgRef_FASTCALL(__pyx_args, 1);
      if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[1])) __PYX_ERR(0, 492, __pyx_L3_error)
    }
    __pyx_v_self = values[0];
    __pyx_v_text = ((PyObject*)values[1]);
  }
  goto __pyx_L6_skip;
  __pyx_L5_argtuple_error:;
  __Pyx_RaiseArgtupleInvalid("indentation_action", 1, 2, 2, __pyx_nargs); __PYX_ERR(0, 492, __pyx_L3_error)
  __pyx_L6_skip:;
  goto __pyx_L4_argument_unpacking_done;
  __pyx_L3_error:;
  for (Py_ssize_t __pyx_temp=0; __pyx_temp < (Py_ssize_t)(sizeof(values)/sizeof(values[0])); ++__pyx_temp) {
    Py_XDECREF(values[__pyx_temp]);
  }
  __Pyx_AddTraceback("Cython.Compiler.Scanning.PyrexScanner.indentation_action", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __Pyx_RefNannyFinishContext();
  return NULL;
  __pyx_L4_argument_unpacking_done:;
  if (unlikely(!__Pyx_ArgTypeTest(((PyObject *)__pyx_v_text), (&PyUnicode_Type), 0, "text", 2))) __PYX_ERR(0, 492, __pyx_L1_error)
  __pyx_r = __pyx_pf_6Cython_8Compiler_8Scanning_12PyrexScanner_40indentation_action(__pyx_self, __pyx_v_self, __pyx_v_text);
  int __pyx_lineno = 0;
  const char *__pyx_filename = NULL;
  int __pyx_clineno = 0;

  /* function exit code */
  goto __pyx_L0;
  __pyx_L1_error:;
  __pyx_r = NULL;
  for (Py_ssize_t __pyx_temp=0; __pyx_temp < (Py_ssize_t)(sizeof(values)/sizeof(values[0])); ++__pyx_temp) {
    Py_XDECREF(values[__pyx_temp]);
  }
  goto __pyx_L7_cleaned_up;
  __pyx_L0:;
  for (Py_ssize_t __pyx_temp=0; __pyx_temp < (Py_ssize_t)(sizeof(values)/sizeof(values[0])); ++__pyx_temp) {
    Py_XDECREF(values[__pyx_temp]);
  }
  __pyx_L7_cleaned_up:;
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}

static PyObject *__pyx_pf_6Cython_8Compiler_8Scanning_12PyrexScanner_40indentation_action(CYTHON_UNUSED PyObject *__pyx_self, PyObject *__pyx_v_self, PyObject *__pyx_v_text) {
  PyObject *__pyx_v_c = NULL;
  Py_ssize_t __pyx_v_current_level;
  Py_ssize_t __pyx_v_new_level;
  PyObject *__pyx_r = NULL;
/* … */
  /* function exit code */
  __pyx_r = Py_None; __Pyx_INCREF(Py_None);
  goto __pyx_L0;
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_t_1);
  __Pyx_XDECREF(__pyx_t_2);
  __Pyx_XDECREF(__pyx_t_8);
  __Pyx_AddTraceback("Cython.Compiler.Scanning.PyrexScanner.indentation_action", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_r = NULL;
  __pyx_L0:;
  __Pyx_XDECREF(__pyx_v_c);
  __Pyx_XGIVEREF(__pyx_r);
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}
/* … */
  __pyx_t_7 = __Pyx_PyDict_NewPresized(1); if (unlikely(!__pyx_t_7)) __PYX_ERR(0, 492, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_7);
  #if defined(PyDict_SetItem) && (defined(CYTHON_COMPILING_IN_CPYTHON))
  #if PY_VERSION_HEX >= 0x030A0000 /* CPython 3.10+ exposes KnownHash APIs */
  /* Use CPython's KnownHash APIs when available */
  extern int _PyDict_SetItem_KnownHash(PyObject*, PyObject*, PyObject*, Py_hash_t);
  {
    Py_hash_t __pyx_hash = PyObject_Hash(__pyx_mstate_global->__pyx_n_u_text); if (unlikely(__pyx_hash == -1)) __PYX_ERR(0, 492, __pyx_L1_error);
    if (unlikely(_PyDict_SetItem_KnownHash(__pyx_t_7, __pyx_mstate_global->__pyx_n_u_text, __pyx_mstate_global->__pyx_n_u_str, __pyx_hash) < 0)) __PYX_ERR(0, 492, __pyx_L1_error);
  }
  #else
  if (PyDict_SetItem(__pyx_t_7, __pyx_mstate_global->__pyx_n_u_text, __pyx_mstate_global->__pyx_n_u_str) < (0)) __PYX_ERR(0, 492, __pyx_L1_error)
  #endif
  #else
  if (PyDict_SetItem(__pyx_t_7, __pyx_mstate_global->__pyx_n_u_text, __pyx_mstate_global->__pyx_n_u_str) < (0)) __PYX_ERR(0, 492, __pyx_L1_error)
  #endif
  __pyx_t_9 = __Pyx_CyFunction_New(&__pyx_mdef_6Cython_8Compiler_8Scanning_12PyrexScanner_41indentation_action, 0, __pyx_mstate_global->__pyx_n_u_PyrexScanner_indentation_action, NULL, __pyx_mstate_global->__pyx_n_u_Cython_Compiler_Scanning, __pyx_mstate_global->__pyx_d, ((PyObject *)__pyx_mstate_global->__pyx_codeobj_tab[55])); if (unlikely(!__pyx_t_9)) __PYX_ERR(0, 492, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_9);
  #if CYTHON_COMPILING_IN_CPYTHON && PY_VERSION_HEX >= 0x030E0000
  PyUnstable_Object_EnableDeferredRefcount(__pyx_t_9);
  #endif
  __Pyx_CyFunction_SetAnnotationsDict(__pyx_t_9, __pyx_t_7);
  __Pyx_DECREF(__pyx_t_7); __pyx_t_7 = 0;
  if (__Pyx_SetNameInClass(__pyx_t_8, __pyx_mstate_global->__pyx_n_u_indentation_action, __pyx_t_9) < (0)) __PYX_ERR(0, 492, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_9); __pyx_t_9 = 0;
```

</details>

L493  🟠  (score=5)
```python
        self.begin('')
```
<details><summary>Show generated C (score=5)</summary>

```c
  __pyx_t_2 = __pyx_v_self;
  __Pyx_INCREF(__pyx_t_2);
  __pyx_t_3 = 0;
  {
    PyObject *__pyx_callargs[2] = {__pyx_t_2, __pyx_mstate_global->__pyx_kp_u__6};
    __pyx_t_1 = __Pyx_PyObject_FastCallMethod((PyObject*)__pyx_mstate_global->__pyx_n_u_begin, __pyx_callargs+__pyx_t_3, (2-__pyx_t_3) | (1*__Pyx_PY_VECTORCALL_ARGUMENTS_OFFSET));
    __Pyx_XDECREF(__pyx_t_2); __pyx_t_2 = 0;
    if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 493, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_1);
  }
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
```

</details>

L494  ⚪  (score=0)
```python
        # Indentation within brackets should be ignored.
```
L495  ⚪  (score=0)
```python
        #if self.bracket_nesting_level > 0:
```
L496  ⚪  (score=0)
```python
        #    return
```
L497  ⚪  (score=0)
```python
        # Check that tabs and spaces are being used consistently.
```
L498  🟡  (score=2)
```python
        if text:
```
<details><summary>Show generated C (score=2)</summary>

```c
  {
    Py_ssize_t __pyx_temp = __Pyx_PyUnicode_IS_TRUE(__pyx_v_text);
    if (unlikely(((!CYTHON_ASSUME_SAFE_SIZE) && __pyx_temp < 0))) __PYX_ERR(0, 498, __pyx_L1_error)
    __pyx_t_4 = (__pyx_temp != 0);
  }

  if (__pyx_t_4) {
/* … */
  }
```

</details>

L499  🟡  (score=4)
```python
            c = text[0]
```
<details><summary>Show generated C (score=4)</summary>

```c
    __pyx_t_5 = __Pyx_GetItemInt_Unicode(__pyx_v_text, 0, long, 1, __Pyx_PyLong_From_long, 0, 0, 0, 1, __Pyx_ReferenceSharing_FunctionArgument); if (unlikely(__pyx_t_5 == (Py_UCS4)-1)) __PYX_ERR(0, 499, __pyx_L1_error)
    __pyx_t_1 = __Pyx_PyUnicode_FromOrdinal(__pyx_t_5); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 499, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_1);
    __pyx_v_c = __pyx_t_1;
    __pyx_t_1 = 0;
```

</details>

L500  ⚪  (score=0)
```python
            #print "Scanner.indentation_action: indent with", repr(c) ###
```
L501  🟠  (score=5)
```python
            if self.indentation_char == '\0':
```
<details><summary>Show generated C (score=5)</summary>

```c
    __pyx_t_1 = __Pyx_PyObject_GetAttrStr(__pyx_v_self, __pyx_mstate_global->__pyx_n_u_indentation_char); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 501, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_1);
    __pyx_t_4 = (__Pyx_PyUnicode_Equals(__pyx_t_1, __pyx_mstate_global->__pyx_kp_u__5, Py_EQ)); if (unlikely((__pyx_t_4 < 0))) __PYX_ERR(0, 501, __pyx_L1_error)
    __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
    if (__pyx_t_4) {
/* … */
      goto __pyx_L4;
    }
```

</details>

L502  🟡  (score=2)
```python
                self.indentation_char = c
```
<details><summary>Show generated C (score=2)</summary>

```c
      if (__Pyx_PyObject_SetAttrStr(__pyx_v_self, __pyx_mstate_global->__pyx_n_u_indentation_char, __pyx_v_c) < (0)) __PYX_ERR(0, 502, __pyx_L1_error)
```

</details>

L503  ⚪  (score=0)
```python
                #print "Scanner.indentation_action: setting indent_char to", repr(c)
```
L504  ⚪  (score=0)
```python
            else:
```
L505  🔴  (score=11)
```python
                if self.indentation_char != c:
```
<details><summary>Show generated C (score=11)</summary>

```c
    /*else*/ {
      __pyx_t_1 = __Pyx_PyObject_GetAttrStr(__pyx_v_self, __pyx_mstate_global->__pyx_n_u_indentation_char); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 505, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_1);
      __pyx_t_2 = PyObject_RichCompare(__pyx_t_1, __pyx_v_c, Py_NE); __Pyx_XGOTREF(__pyx_t_2); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 505, __pyx_L1_error)
      __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
      __pyx_t_4 = __Pyx_PyObject_IsTrue(__pyx_t_2); if (unlikely((__pyx_t_4 < 0))) __PYX_ERR(0, 505, __pyx_L1_error)
      __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
      if (__pyx_t_4) {
/* … */
      }
    }
    __pyx_L4:;
```

</details>

L506  🟠  (score=5)
```python
                    self.error_at_scanpos("Mixed use of tabs and spaces")
```
<details><summary>Show generated C (score=5)</summary>

```c
        __pyx_t_1 = __pyx_v_self;
        __Pyx_INCREF(__pyx_t_1);
        __pyx_t_3 = 0;
        {
          PyObject *__pyx_callargs[2] = {__pyx_t_1, __pyx_mstate_global->__pyx_kp_u_Mixed_use_of_tabs_and_spaces};
          __pyx_t_2 = __Pyx_PyObject_FastCallMethod((PyObject*)__pyx_mstate_global->__pyx_n_u_error_at_scanpos, __pyx_callargs+__pyx_t_3, (2-__pyx_t_3) | (1*__Pyx_PY_VECTORCALL_ARGUMENTS_OFFSET));
          __Pyx_XDECREF(__pyx_t_1); __pyx_t_1 = 0;
          if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 506, __pyx_L1_error)
          __Pyx_GOTREF(__pyx_t_2);
        }
        __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
```

</details>

L507  🟠  (score=8)
```python
            if text.replace(c, "") != "":
```
<details><summary>Show generated C (score=8)</summary>

```c
    __pyx_t_2 = PyUnicode_Replace(__pyx_v_text, __pyx_v_c, __pyx_mstate_global->__pyx_kp_u__6, -1); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 507, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_2);
    __pyx_t_4 = (__Pyx_PyUnicode_Equals(__pyx_t_2, __pyx_mstate_global->__pyx_kp_u__6, Py_NE)); if (unlikely((__pyx_t_4 < 0))) __PYX_ERR(0, 507, __pyx_L1_error)
    __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
    if (__pyx_t_4) {
/* … */
    }
```

</details>

L508  🟠  (score=5)
```python
                self.error_at_scanpos("Mixed use of tabs and spaces")
```
<details><summary>Show generated C (score=5)</summary>

```c
      __pyx_t_1 = __pyx_v_self;
      __Pyx_INCREF(__pyx_t_1);
      __pyx_t_3 = 0;
      {
        PyObject *__pyx_callargs[2] = {__pyx_t_1, __pyx_mstate_global->__pyx_kp_u_Mixed_use_of_tabs_and_spaces};
        __pyx_t_2 = __Pyx_PyObject_FastCallMethod((PyObject*)__pyx_mstate_global->__pyx_n_u_error_at_scanpos, __pyx_callargs+__pyx_t_3, (2-__pyx_t_3) | (1*__Pyx_PY_VECTORCALL_ARGUMENTS_OFFSET));
        __Pyx_XDECREF(__pyx_t_1); __pyx_t_1 = 0;
        if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 508, __pyx_L1_error)
        __Pyx_GOTREF(__pyx_t_2);
      }
      __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
```

</details>

L509  ⚪  (score=0)
```python
        # Figure out how many indents/dedents to do
```
L510  🟠  (score=7)
```python
        current_level: cython.Py_ssize_t = self.current_level()
```
<details><summary>Show generated C (score=7)</summary>

```c
  __pyx_t_1 = __pyx_v_self;
  __Pyx_INCREF(__pyx_t_1);
  __pyx_t_3 = 0;
  {
    PyObject *__pyx_callargs[2] = {__pyx_t_1, NULL};
    __pyx_t_2 = __Pyx_PyObject_FastCallMethod((PyObject*)__pyx_mstate_global->__pyx_n_u_current_level, __pyx_callargs+__pyx_t_3, (1-__pyx_t_3) | (1*__Pyx_PY_VECTORCALL_ARGUMENTS_OFFSET));
    __Pyx_XDECREF(__pyx_t_1); __pyx_t_1 = 0;
    if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 510, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_2);
  }
  __pyx_t_6 = __Pyx_PyIndex_AsSsize_t(__pyx_t_2); if (unlikely((__pyx_t_6 == (Py_ssize_t)-1) && PyErr_Occurred())) __PYX_ERR(0, 510, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __pyx_v_current_level = __pyx_t_6;
```

</details>

L511  🟡  (score=2)
```python
        new_level: cython.Py_ssize_t = len(text)
```
<details><summary>Show generated C (score=2)</summary>

```c
  __pyx_t_6 = __Pyx_PyUnicode_GET_LENGTH(__pyx_v_text); if (unlikely(__pyx_t_6 == ((Py_ssize_t)-1))) __PYX_ERR(0, 511, __pyx_L1_error)
  __pyx_v_new_level = __pyx_t_6;
```

</details>

L512  ⚪  (score=0)
```python
        #print "Changing indent level from", current_level, "to", new_level ###
```
L513  ⚪  (score=0)
```python
        if new_level == current_level:
```
<details><summary>Show generated C (score=0)</summary>

```c
  __pyx_t_4 = (__pyx_v_new_level == __pyx_v_current_level);
  if (__pyx_t_4) {
/* … */
  }
```

</details>

L514  🟡  (score=2)
```python
            return
```
<details><summary>Show generated C (score=2)</summary>

```c
    __Pyx_XDECREF(__pyx_r);
    __pyx_r = Py_None; __Pyx_INCREF(Py_None);
    goto __pyx_L0;
```

</details>

L515  ⚪  (score=0)
```python
        elif new_level > current_level:
```
<details><summary>Show generated C (score=0)</summary>

```c
  __pyx_t_4 = (__pyx_v_new_level > __pyx_v_current_level);
  if (__pyx_t_4) {
/* … */
    goto __pyx_L7;
  }
```

</details>

L516  ⚪  (score=0)
```python
            #print "...pushing level", new_level ###
```
L517  🔴  (score=11)
```python
            self.indentation_stack.append(new_level)
```
<details><summary>Show generated C (score=11)</summary>

```c
    __pyx_t_2 = __Pyx_PyObject_GetAttrStr(__pyx_v_self, __pyx_mstate_global->__pyx_n_u_indentation_stack); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 517, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_2);
    __pyx_t_1 = PyLong_FromSsize_t(__pyx_v_new_level); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 517, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_1);
    __pyx_t_7 = __Pyx_PyObject_Append(__pyx_t_2, __pyx_t_1); if (unlikely(__pyx_t_7 == ((int)-1))) __PYX_ERR(0, 517, __pyx_L1_error)
    __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
    __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
```

</details>

L518  🔴  (score=11)
```python
            self.produce('INDENT', '')
```
<details><summary>Show generated C (score=11)</summary>

```c
    __pyx_t_1 = __Pyx_PyObject_GetAttrStr(__pyx_v_self, __pyx_mstate_global->__pyx_n_u_produce); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 518, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_1);
    __pyx_t_2 = __Pyx_PyObject_Call(__pyx_t_1, __pyx_mstate_global->__pyx_tuple[9], NULL); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 518, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_2);
    __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
    __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
/* … */
  __pyx_mstate_global->__pyx_tuple[9] = PyTuple_Pack(2, __pyx_mstate_global->__pyx_n_u_INDENT, __pyx_mstate_global->__pyx_kp_u__6); if (unlikely(!__pyx_mstate_global->__pyx_tuple[9])) __PYX_ERR(0, 518, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_mstate_global->__pyx_tuple[9]);
  __Pyx_GIVEREF(__pyx_mstate_global->__pyx_tuple[9]);
```

</details>

L519  ⚪  (score=0)
```python
        else:
```
L520  🔴  (score=19)
```python
            while new_level < self.current_level():
```
<details><summary>Show generated C (score=19)</summary>

```c
  /*else*/ {
    while (1) {
      __pyx_t_2 = PyLong_FromSsize_t(__pyx_v_new_level); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 520, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_2);
      __pyx_t_8 = __pyx_v_self;
      __Pyx_INCREF(__pyx_t_8);
      __pyx_t_3 = 0;
      {
        PyObject *__pyx_callargs[2] = {__pyx_t_8, NULL};
        __pyx_t_1 = __Pyx_PyObject_FastCallMethod((PyObject*)__pyx_mstate_global->__pyx_n_u_current_level, __pyx_callargs+__pyx_t_3, (1-__pyx_t_3) | (1*__Pyx_PY_VECTORCALL_ARGUMENTS_OFFSET));
        __Pyx_XDECREF(__pyx_t_8); __pyx_t_8 = 0;
        if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 520, __pyx_L1_error)
        __Pyx_GOTREF(__pyx_t_1);
      }
      __pyx_t_8 = PyObject_RichCompare(__pyx_t_2, __pyx_t_1, Py_LT); __Pyx_XGOTREF(__pyx_t_8); if (unlikely(!__pyx_t_8)) __PYX_ERR(0, 520, __pyx_L1_error)
      __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
      __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
      __pyx_t_4 = __Pyx_PyObject_IsTrue(__pyx_t_8); if (unlikely((__pyx_t_4 < 0))) __PYX_ERR(0, 520, __pyx_L1_error)
      __Pyx_DECREF(__pyx_t_8); __pyx_t_8 = 0;
      if (!__pyx_t_4) break;
```

</details>

L521  ⚪  (score=0)
```python
                #print "...popping level", self.indentation_stack[-1] ###
```
L522  🟠  (score=6)
```python
                self.indentation_stack.pop()
```
<details><summary>Show generated C (score=6)</summary>

```c
      __pyx_t_8 = __Pyx_PyObject_GetAttrStr(__pyx_v_self, __pyx_mstate_global->__pyx_n_u_indentation_stack); if (unlikely(!__pyx_t_8)) __PYX_ERR(0, 522, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_8);
      __pyx_t_1 = __Pyx_PyObject_Pop(__pyx_t_8); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 522, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_1);
      __Pyx_DECREF(__pyx_t_8); __pyx_t_8 = 0;
      __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
```

</details>

L523  🔴  (score=11)
```python
                self.produce('DEDENT', '')
```
<details><summary>Show generated C (score=11)</summary>

```c
      __pyx_t_1 = __Pyx_PyObject_GetAttrStr(__pyx_v_self, __pyx_mstate_global->__pyx_n_u_produce); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 523, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_1);
      __pyx_t_8 = __Pyx_PyObject_Call(__pyx_t_1, __pyx_mstate_global->__pyx_tuple[10], NULL); if (unlikely(!__pyx_t_8)) __PYX_ERR(0, 523, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_8);
      __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
      __Pyx_DECREF(__pyx_t_8); __pyx_t_8 = 0;
    }
/* … */
  __pyx_mstate_global->__pyx_tuple[10] = PyTuple_Pack(2, __pyx_mstate_global->__pyx_n_u_DEDENT, __pyx_mstate_global->__pyx_kp_u__6); if (unlikely(!__pyx_mstate_global->__pyx_tuple[10])) __PYX_ERR(0, 523, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_mstate_global->__pyx_tuple[10]);
  __Pyx_GIVEREF(__pyx_mstate_global->__pyx_tuple[10]);
```

</details>

L524  ⚪  (score=0)
```python
            #print "...current level now", self.current_level() ###
```
L525  🔴  (score=19)
```python
            if new_level != self.current_level():
```
<details><summary>Show generated C (score=19)</summary>

```c
    __pyx_t_8 = PyLong_FromSsize_t(__pyx_v_new_level); if (unlikely(!__pyx_t_8)) __PYX_ERR(0, 525, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_8);
    __pyx_t_2 = __pyx_v_self;
    __Pyx_INCREF(__pyx_t_2);
    __pyx_t_3 = 0;
    {
      PyObject *__pyx_callargs[2] = {__pyx_t_2, NULL};
      __pyx_t_1 = __Pyx_PyObject_FastCallMethod((PyObject*)__pyx_mstate_global->__pyx_n_u_current_level, __pyx_callargs+__pyx_t_3, (1-__pyx_t_3) | (1*__Pyx_PY_VECTORCALL_ARGUMENTS_OFFSET));
      __Pyx_XDECREF(__pyx_t_2); __pyx_t_2 = 0;
      if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 525, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_1);
    }
    __pyx_t_2 = PyObject_RichCompare(__pyx_t_8, __pyx_t_1, Py_NE); __Pyx_XGOTREF(__pyx_t_2); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 525, __pyx_L1_error)
    __Pyx_DECREF(__pyx_t_8); __pyx_t_8 = 0;
    __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
    __pyx_t_4 = __Pyx_PyObject_IsTrue(__pyx_t_2); if (unlikely((__pyx_t_4 < 0))) __PYX_ERR(0, 525, __pyx_L1_error)
    __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
    if (__pyx_t_4) {
/* … */
    }
  }
  __pyx_L7:;
```

</details>

L526  🟠  (score=5)
```python
                self.error_at_scanpos("Inconsistent indentation")
```
<details><summary>Show generated C (score=5)</summary>

```c
      __pyx_t_1 = __pyx_v_self;
      __Pyx_INCREF(__pyx_t_1);
      __pyx_t_3 = 0;
      {
        PyObject *__pyx_callargs[2] = {__pyx_t_1, __pyx_mstate_global->__pyx_kp_u_Inconsistent_indentation};
        __pyx_t_2 = __Pyx_PyObject_FastCallMethod((PyObject*)__pyx_mstate_global->__pyx_n_u_error_at_scanpos, __pyx_callargs+__pyx_t_3, (2-__pyx_t_3) | (1*__Pyx_PY_VECTORCALL_ARGUMENTS_OFFSET));
        __Pyx_XDECREF(__pyx_t_1); __pyx_t_1 = 0;
        if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 526, __pyx_L1_error)
        __Pyx_GOTREF(__pyx_t_2);
      }
      __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
```

</details>

L527  ⚪  (score=0)
```python
```
L528  🔴  (score=42)
```python
    def eof_action(self, text):
```
<details><summary>Show generated C (score=42)</summary>

```c
/* Python wrapper */
static PyObject *__pyx_pw_6Cython_8Compiler_8Scanning_12PyrexScanner_43eof_action(PyObject *__pyx_self, 
#if CYTHON_METH_FASTCALL
PyObject *const *__pyx_args, Py_ssize_t __pyx_nargs, PyObject *__pyx_kwds
#else
PyObject *__pyx_args, PyObject *__pyx_kwds
#endif
); /*proto*/
PyDoc_STRVAR(__pyx_doc_6Cython_8Compiler_8Scanning_12PyrexScanner_42eof_action, "File: Cython/Compiler/Scanning.py (starting at line 528)");
static PyMethodDef __pyx_mdef_6Cython_8Compiler_8Scanning_12PyrexScanner_43eof_action = {"eof_action", (PyCFunction)(void(*)(void))(__Pyx_PyCFunction_FastCallWithKeywords)__pyx_pw_6Cython_8Compiler_8Scanning_12PyrexScanner_43eof_action, __Pyx_METH_FASTCALL|METH_KEYWORDS, __pyx_doc_6Cython_8Compiler_8Scanning_12PyrexScanner_42eof_action};
static PyObject *__pyx_pw_6Cython_8Compiler_8Scanning_12PyrexScanner_43eof_action(PyObject *__pyx_self, 
#if CYTHON_METH_FASTCALL
PyObject *const *__pyx_args, Py_ssize_t __pyx_nargs, PyObject *__pyx_kwds
#else
PyObject *__pyx_args, PyObject *__pyx_kwds
#endif
) {
  PyObject *__pyx_v_self = 0;
  CYTHON_UNUSED PyObject *__pyx_v_text = 0;
  #if !CYTHON_METH_FASTCALL
  CYTHON_UNUSED Py_ssize_t __pyx_nargs;
  #endif
  CYTHON_UNUSED PyObject *const *__pyx_kwvalues;
  PyObject *__pyx_r = 0;
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("eof_action (wrapper)", 0);
  #if !CYTHON_METH_FASTCALL
  #if CYTHON_ASSUME_SAFE_SIZE
  __pyx_nargs = PyTuple_GET_SIZE(__pyx_args);
  #else
  __pyx_nargs = PyTuple_Size(__pyx_args); if (unlikely(__pyx_nargs < 0)) return NULL;
  #endif
  #endif
  __pyx_kwvalues = __Pyx_KwValues_FASTCALL(__pyx_args, __pyx_nargs);
  {
    PyObject ** const __pyx_pyargnames[] = {&__pyx_mstate_global->__pyx_n_u_self,&__pyx_mstate_global->__pyx_n_u_text,0};
  PyObject* values[2] = {0,0};
    const Py_ssize_t __pyx_kwds_len = (__pyx_kwds) ? __Pyx_NumKwargs_FASTCALL(__pyx_kwds) : 0;
    if (unlikely(__pyx_kwds_len) < 0) __PYX_ERR(0, 528, __pyx_L3_error)
    if (__pyx_kwds_len > 0) {
      switch (__pyx_nargs) {
        case  2:
        values[1] = __Pyx_ArgRef_FASTCALL(__pyx_args, 1);
        if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[1])) __PYX_ERR(0, 528, __pyx_L3_error)
        CYTHON_FALLTHROUGH;
        case  1:
        values[0] = __Pyx_ArgRef_FASTCALL(__pyx_args, 0);
        if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[0])) __PYX_ERR(0, 528, __pyx_L3_error)
        CYTHON_FALLTHROUGH;
        case  0: break;
        default: goto __pyx_L5_argtuple_error;
      }
      const Py_ssize_t kwd_pos_args = __pyx_nargs;
      if (__Pyx_ParseKeywords(__pyx_kwds, __pyx_kwvalues, __pyx_pyargnames, 0, values, kwd_pos_args, __pyx_kwds_len, "eof_action", 0) < (0)) __PYX_ERR(0, 528, __pyx_L3_error)
      for (Py_ssize_t i = __pyx_nargs; i < 2; i++) {
        if (unlikely(!values[i])) { __Pyx_RaiseArgtupleInvalid("eof_action", 1, 2, 2, i); __PYX_ERR(0, 528, __pyx_L3_error) }
      }
    } else if (unlikely(__pyx_nargs != 2)) {
      goto __pyx_L5_argtuple_error;
    } else {
      values[0] = __Pyx_ArgRef_FASTCALL(__pyx_args, 0);
      if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[0])) __PYX_ERR(0, 528, __pyx_L3_error)
      values[1] = __Pyx_ArgRef_FASTCALL(__pyx_args, 1);
      if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[1])) __PYX_ERR(0, 528, __pyx_L3_error)
    }
    __pyx_v_self = values[0];
    __pyx_v_text = values[1];
  }
  goto __pyx_L6_skip;
  __pyx_L5_argtuple_error:;
  __Pyx_RaiseArgtupleInvalid("eof_action", 1, 2, 2, __pyx_nargs); __PYX_ERR(0, 528, __pyx_L3_error)
  __pyx_L6_skip:;
  goto __pyx_L4_argument_unpacking_done;
  __pyx_L3_error:;
  for (Py_ssize_t __pyx_temp=0; __pyx_temp < (Py_ssize_t)(sizeof(values)/sizeof(values[0])); ++__pyx_temp) {
    Py_XDECREF(values[__pyx_temp]);
  }
  __Pyx_AddTraceback("Cython.Compiler.Scanning.PyrexScanner.eof_action", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __Pyx_RefNannyFinishContext();
  return NULL;
  __pyx_L4_argument_unpacking_done:;
  __pyx_r = __pyx_pf_6Cython_8Compiler_8Scanning_12PyrexScanner_42eof_action(__pyx_self, __pyx_v_self, __pyx_v_text);
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

static PyObject *__pyx_pf_6Cython_8Compiler_8Scanning_12PyrexScanner_42eof_action(CYTHON_UNUSED PyObject *__pyx_self, PyObject *__pyx_v_self, CYTHON_UNUSED PyObject *__pyx_v_text) {
  PyObject *__pyx_r = NULL;
/* … */
  /* function exit code */
  __pyx_r = Py_None; __Pyx_INCREF(Py_None);
  goto __pyx_L0;
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_t_1);
  __Pyx_XDECREF(__pyx_t_4);
  __Pyx_AddTraceback("Cython.Compiler.Scanning.PyrexScanner.eof_action", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_r = NULL;
  __pyx_L0:;
  __Pyx_XGIVEREF(__pyx_r);
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}
/* … */
  __pyx_t_9 = __Pyx_CyFunction_New(&__pyx_mdef_6Cython_8Compiler_8Scanning_12PyrexScanner_43eof_action, 0, __pyx_mstate_global->__pyx_n_u_PyrexScanner_eof_action, NULL, __pyx_mstate_global->__pyx_n_u_Cython_Compiler_Scanning, __pyx_mstate_global->__pyx_d, ((PyObject *)__pyx_mstate_global->__pyx_codeobj_tab[56])); if (unlikely(!__pyx_t_9)) __PYX_ERR(0, 528, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_9);
  #if CYTHON_COMPILING_IN_CPYTHON && PY_VERSION_HEX >= 0x030E0000
  PyUnstable_Object_EnableDeferredRefcount(__pyx_t_9);
  #endif
  if (__Pyx_SetNameInClass(__pyx_t_8, __pyx_mstate_global->__pyx_n_u_eof_action, __pyx_t_9) < (0)) __PYX_ERR(0, 528, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_9); __pyx_t_9 = 0;
```

</details>

L529  🟠  (score=8)
```python
        while len(self.indentation_stack) > 1:
```
<details><summary>Show generated C (score=8)</summary>

```c
  while (1) {
    __pyx_t_1 = __Pyx_PyObject_GetAttrStr(__pyx_v_self, __pyx_mstate_global->__pyx_n_u_indentation_stack); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 529, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_1);
    __pyx_t_2 = PyObject_Length(__pyx_t_1); if (unlikely(__pyx_t_2 == ((Py_ssize_t)-1))) __PYX_ERR(0, 529, __pyx_L1_error)
    __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
    __pyx_t_3 = (__pyx_t_2 > 1);
    if (!__pyx_t_3) break;
```

</details>

L530  🟠  (score=6)
```python
            self.produce('DEDENT', '')
```
<details><summary>Show generated C (score=6)</summary>

```c
    __pyx_t_1 = __Pyx_PyObject_GetAttrStr(__pyx_v_self, __pyx_mstate_global->__pyx_n_u_produce); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 530, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_1);
    __pyx_t_4 = __Pyx_PyObject_Call(__pyx_t_1, __pyx_mstate_global->__pyx_tuple[10], NULL); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 530, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_4);
    __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
    __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
```

</details>

L531  🟠  (score=6)
```python
            self.indentation_stack.pop()
```
<details><summary>Show generated C (score=6)</summary>

```c
    __pyx_t_4 = __Pyx_PyObject_GetAttrStr(__pyx_v_self, __pyx_mstate_global->__pyx_n_u_indentation_stack); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 531, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_4);
    __pyx_t_1 = __Pyx_PyObject_Pop(__pyx_t_4); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 531, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_1);
    __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
    __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  }
```

</details>

L532  🔴  (score=11)
```python
        self.produce('EOF', '')
```
<details><summary>Show generated C (score=11)</summary>

```c
  __pyx_t_1 = __Pyx_PyObject_GetAttrStr(__pyx_v_self, __pyx_mstate_global->__pyx_n_u_produce); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 532, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __pyx_t_4 = __Pyx_PyObject_Call(__pyx_t_1, __pyx_mstate_global->__pyx_tuple[11], NULL); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 532, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_4);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
/* … */
  __pyx_mstate_global->__pyx_tuple[11] = PyTuple_Pack(2, __pyx_mstate_global->__pyx_n_u_EOF, __pyx_mstate_global->__pyx_kp_u__6); if (unlikely(!__pyx_mstate_global->__pyx_tuple[11])) __PYX_ERR(0, 532, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_mstate_global->__pyx_tuple[11]);
  __Pyx_GIVEREF(__pyx_mstate_global->__pyx_tuple[11]);
```

</details>

L533  ⚪  (score=0)
```python
```
L534  🔴  (score=43)
```python
    def next(self):
```
<details><summary>Show generated C (score=43)</summary>

```c
/* Python wrapper */
static PyObject *__pyx_pw_6Cython_8Compiler_8Scanning_12PyrexScanner_45next(PyObject *__pyx_self, 
#if CYTHON_METH_FASTCALL
PyObject *const *__pyx_args, Py_ssize_t __pyx_nargs, PyObject *__pyx_kwds
#else
PyObject *__pyx_args, PyObject *__pyx_kwds
#endif
); /*proto*/
PyDoc_STRVAR(__pyx_doc_6Cython_8Compiler_8Scanning_12PyrexScanner_44next, "File: Cython/Compiler/Scanning.py (starting at line 534)");
static PyMethodDef __pyx_mdef_6Cython_8Compiler_8Scanning_12PyrexScanner_45next = {"next", (PyCFunction)(void(*)(void))(__Pyx_PyCFunction_FastCallWithKeywords)__pyx_pw_6Cython_8Compiler_8Scanning_12PyrexScanner_45next, __Pyx_METH_FASTCALL|METH_KEYWORDS, __pyx_doc_6Cython_8Compiler_8Scanning_12PyrexScanner_44next};
static PyObject *__pyx_pw_6Cython_8Compiler_8Scanning_12PyrexScanner_45next(PyObject *__pyx_self, 
#if CYTHON_METH_FASTCALL
PyObject *const *__pyx_args, Py_ssize_t __pyx_nargs, PyObject *__pyx_kwds
#else
PyObject *__pyx_args, PyObject *__pyx_kwds
#endif
) {
  PyObject *__pyx_v_self = 0;
  #if !CYTHON_METH_FASTCALL
  CYTHON_UNUSED Py_ssize_t __pyx_nargs;
  #endif
  CYTHON_UNUSED PyObject *const *__pyx_kwvalues;
  PyObject *__pyx_r = 0;
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("next (wrapper)", 0);
  #if !CYTHON_METH_FASTCALL
  #if CYTHON_ASSUME_SAFE_SIZE
  __pyx_nargs = PyTuple_GET_SIZE(__pyx_args);
  #else
  __pyx_nargs = PyTuple_Size(__pyx_args); if (unlikely(__pyx_nargs < 0)) return NULL;
  #endif
  #endif
  __pyx_kwvalues = __Pyx_KwValues_FASTCALL(__pyx_args, __pyx_nargs);
  {
    PyObject ** const __pyx_pyargnames[] = {&__pyx_mstate_global->__pyx_n_u_self,0};
  PyObject* values[1] = {0};
    const Py_ssize_t __pyx_kwds_len = (__pyx_kwds) ? __Pyx_NumKwargs_FASTCALL(__pyx_kwds) : 0;
    if (unlikely(__pyx_kwds_len) < 0) __PYX_ERR(0, 534, __pyx_L3_error)
    if (__pyx_kwds_len > 0) {
      switch (__pyx_nargs) {
        case  1:
        values[0] = __Pyx_ArgRef_FASTCALL(__pyx_args, 0);
        if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[0])) __PYX_ERR(0, 534, __pyx_L3_error)
        CYTHON_FALLTHROUGH;
        case  0: break;
        default: goto __pyx_L5_argtuple_error;
      }
      const Py_ssize_t kwd_pos_args = __pyx_nargs;
      if (__Pyx_ParseKeywords(__pyx_kwds, __pyx_kwvalues, __pyx_pyargnames, 0, values, kwd_pos_args, __pyx_kwds_len, "next", 0) < (0)) __PYX_ERR(0, 534, __pyx_L3_error)
      for (Py_ssize_t i = __pyx_nargs; i < 1; i++) {
        if (unlikely(!values[i])) { __Pyx_RaiseArgtupleInvalid("next", 1, 1, 1, i); __PYX_ERR(0, 534, __pyx_L3_error) }
      }
    } else if (unlikely(__pyx_nargs != 1)) {
      goto __pyx_L5_argtuple_error;
    } else {
      values[0] = __Pyx_ArgRef_FASTCALL(__pyx_args, 0);
      if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[0])) __PYX_ERR(0, 534, __pyx_L3_error)
    }
    __pyx_v_self = values[0];
  }
  goto __pyx_L6_skip;
  __pyx_L5_argtuple_error:;
  __Pyx_RaiseArgtupleInvalid("next", 1, 1, 1, __pyx_nargs); __PYX_ERR(0, 534, __pyx_L3_error)
  __pyx_L6_skip:;
  goto __pyx_L4_argument_unpacking_done;
  __pyx_L3_error:;
  for (Py_ssize_t __pyx_temp=0; __pyx_temp < (Py_ssize_t)(sizeof(values)/sizeof(values[0])); ++__pyx_temp) {
    Py_XDECREF(values[__pyx_temp]);
  }
  __Pyx_AddTraceback("Cython.Compiler.Scanning.PyrexScanner.next", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __Pyx_RefNannyFinishContext();
  return NULL;
  __pyx_L4_argument_unpacking_done:;
  __pyx_r = __pyx_pf_6Cython_8Compiler_8Scanning_12PyrexScanner_44next(__pyx_self, __pyx_v_self);
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

static PyObject *__pyx_pf_6Cython_8Compiler_8Scanning_12PyrexScanner_44next(CYTHON_UNUSED PyObject *__pyx_self, PyObject *__pyx_v_self) {
  PyObject *__pyx_v_sy = NULL;
  PyObject *__pyx_v_systring = NULL;
  PyObject *__pyx_r = NULL;
/* … */
  /* function exit code */
  __pyx_r = Py_None; __Pyx_INCREF(Py_None);
  goto __pyx_L0;
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_t_4);
  __Pyx_XDECREF(__pyx_t_5);
  __Pyx_XDECREF(__pyx_t_7);
  __Pyx_XDECREF(__pyx_t_8);
  __Pyx_XDECREF(__pyx_t_11);
  __Pyx_AddTraceback("Cython.Compiler.Scanning.PyrexScanner.next", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_r = NULL;
  __pyx_L0:;
  __Pyx_XDECREF(__pyx_v_sy);
  __Pyx_XDECREF(__pyx_v_systring);
  __Pyx_XGIVEREF(__pyx_r);
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}
/* … */
  __pyx_t_9 = __Pyx_CyFunction_New(&__pyx_mdef_6Cython_8Compiler_8Scanning_12PyrexScanner_45next, 0, __pyx_mstate_global->__pyx_n_u_PyrexScanner_next, NULL, __pyx_mstate_global->__pyx_n_u_Cython_Compiler_Scanning, __pyx_mstate_global->__pyx_d, ((PyObject *)__pyx_mstate_global->__pyx_codeobj_tab[57])); if (unlikely(!__pyx_t_9)) __PYX_ERR(0, 534, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_9);
  #if CYTHON_COMPILING_IN_CPYTHON && PY_VERSION_HEX >= 0x030E0000
  PyUnstable_Object_EnableDeferredRefcount(__pyx_t_9);
  #endif
  if (__Pyx_SetNameInClass(__pyx_t_8, __pyx_mstate_global->__pyx_n_u_next, __pyx_t_9) < (0)) __PYX_ERR(0, 534, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_9); __pyx_t_9 = 0;
```

</details>

L535  🔴  (score=11)
```python
        try:
```
<details><summary>Show generated C (score=11)</summary>

```c
  {
    /*try:*/ {
/* … */
    }
    __Pyx_XDECREF(__pyx_t_1); __pyx_t_1 = 0;
    __Pyx_XDECREF(__pyx_t_2); __pyx_t_2 = 0;
    __Pyx_XDECREF(__pyx_t_3); __pyx_t_3 = 0;
    goto __pyx_L8_try_end;
    __pyx_L3_error:;
    __Pyx_XDECREF(__pyx_t_4); __pyx_t_4 = 0;
    __Pyx_XDECREF(__pyx_t_5); __pyx_t_5 = 0;
    __Pyx_XDECREF(__pyx_t_7); __pyx_t_7 = 0;
    __Pyx_XDECREF(__pyx_t_8); __pyx_t_8 = 0;
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
    __pyx_L8_try_end:;
  }
```

</details>

L536  🔴  (score=54)
```python
            sy, systring = self.read()
```
<details><summary>Show generated C (score=54)</summary>

```c
      __pyx_t_5 = __pyx_v_self;
      __Pyx_INCREF(__pyx_t_5);
      __pyx_t_6 = 0;
      {
        PyObject *__pyx_callargs[2] = {__pyx_t_5, NULL};
        __pyx_t_4 = __Pyx_PyObject_FastCallMethod((PyObject*)__pyx_mstate_global->__pyx_n_u_read, __pyx_callargs+__pyx_t_6, (1-__pyx_t_6) | (1*__Pyx_PY_VECTORCALL_ARGUMENTS_OFFSET));
        __Pyx_XDECREF(__pyx_t_5); __pyx_t_5 = 0;
        if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 536, __pyx_L3_error)
        __Pyx_GOTREF(__pyx_t_4);
      }
      if ((likely(PyTuple_CheckExact(__pyx_t_4))) || (PyList_CheckExact(__pyx_t_4))) {
        PyObject* sequence = __pyx_t_4;
        Py_ssize_t size = __Pyx_PySequence_SIZE(sequence);
        if (unlikely(size != 2)) {
          if (size > 2) __Pyx_RaiseTooManyValuesError(2);
          else if (size >= 0) __Pyx_RaiseNeedMoreValuesError(size);
          __PYX_ERR(0, 536, __pyx_L3_error)
        }
        #if CYTHON_ASSUME_SAFE_MACROS && !CYTHON_AVOID_BORROWED_REFS
        if (likely(PyTuple_CheckExact(sequence))) {
          __pyx_t_5 = PyTuple_GET_ITEM(sequence, 0);
          __Pyx_INCREF(__pyx_t_5);
          __pyx_t_7 = PyTuple_GET_ITEM(sequence, 1);
          __Pyx_INCREF(__pyx_t_7);
        } else {
          __pyx_t_5 = __Pyx_PyList_GetItemRefFast(sequence, 0, __Pyx_ReferenceSharing_SharedReference);
          if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 536, __pyx_L3_error)
          __Pyx_XGOTREF(__pyx_t_5);
          __pyx_t_7 = __Pyx_PyList_GetItemRefFast(sequence, 1, __Pyx_ReferenceSharing_SharedReference);
          if (unlikely(!__pyx_t_7)) __PYX_ERR(0, 536, __pyx_L3_error)
          __Pyx_XGOTREF(__pyx_t_7);
        }
        #else
        __pyx_t_5 = __Pyx_PySequence_ITEM(sequence, 0); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 536, __pyx_L3_error)
        __Pyx_GOTREF(__pyx_t_5);
        __pyx_t_7 = __Pyx_PySequence_ITEM(sequence, 1); if (unlikely(!__pyx_t_7)) __PYX_ERR(0, 536, __pyx_L3_error)
        __Pyx_GOTREF(__pyx_t_7);
        #endif
        __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
      } else {
        Py_ssize_t index = -1;
        __pyx_t_8 = PyObject_GetIter(__pyx_t_4); if (unlikely(!__pyx_t_8)) __PYX_ERR(0, 536, __pyx_L3_error)
        __Pyx_GOTREF(__pyx_t_8);
        __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
        __pyx_t_9 = (CYTHON_COMPILING_IN_LIMITED_API) ? PyIter_Next : __Pyx_PyObject_GetIterNextFunc(__pyx_t_8);
        index = 0; __pyx_t_5 = __pyx_t_9(__pyx_t_8); if (unlikely(!__pyx_t_5)) goto __pyx_L9_unpacking_failed;
        __Pyx_GOTREF(__pyx_t_5);
        index = 1; __pyx_t_7 = __pyx_t_9(__pyx_t_8); if (unlikely(!__pyx_t_7)) goto __pyx_L9_unpacking_failed;
        __Pyx_GOTREF(__pyx_t_7);
        if (__Pyx_IternextUnpackEndCheck(__pyx_t_9(__pyx_t_8), 2) < (0)) __PYX_ERR(0, 536, __pyx_L3_error)
        __pyx_t_9 = NULL;
        __Pyx_DECREF(__pyx_t_8); __pyx_t_8 = 0;
        goto __pyx_L10_unpacking_done;
        __pyx_L9_unpacking_failed:;
        __Pyx_DECREF(__pyx_t_8); __pyx_t_8 = 0;
        __pyx_t_9 = NULL;
        if (__Pyx_IterFinish() == 0) __Pyx_RaiseNeedMoreValuesError(index);
        __PYX_ERR(0, 536, __pyx_L3_error)
        __pyx_L10_unpacking_done:;
      }
      __pyx_v_sy = __pyx_t_5;
      __pyx_t_5 = 0;
      __pyx_v_systring = __pyx_t_7;
      __pyx_t_7 = 0;
```

</details>

L537  🔴  (score=13)
```python
        except UnrecognizedInput:
```
<details><summary>Show generated C (score=13)</summary>

```c
    __Pyx_ErrFetch(&__pyx_t_4, &__pyx_t_7, &__pyx_t_5);
    __Pyx_GetModuleGlobalName(__pyx_t_8, __pyx_mstate_global->__pyx_n_u_UnrecognizedInput); if (unlikely(!__pyx_t_8)) __PYX_ERR(0, 537, __pyx_L5_except_error)
    __Pyx_GOTREF(__pyx_t_8);
    __pyx_t_10 = __Pyx_PyErr_GivenExceptionMatches(__pyx_t_4, __pyx_t_8);
    __Pyx_DECREF(__pyx_t_8); __pyx_t_8 = 0;
    __Pyx_ErrRestore(__pyx_t_4, __pyx_t_7, __pyx_t_5);
    __pyx_t_4 = 0; __pyx_t_7 = 0; __pyx_t_5 = 0;
    if (__pyx_t_10) {
      __Pyx_AddTraceback("Cython.Compiler.Scanning.PyrexScanner.next", __pyx_clineno, __pyx_lineno, __pyx_filename);
      if (__Pyx_GetException(&__pyx_t_5, &__pyx_t_7, &__pyx_t_4) < 0) __PYX_ERR(0, 537, __pyx_L5_except_error)
      __Pyx_XGOTREF(__pyx_t_5);
      __Pyx_XGOTREF(__pyx_t_7);
      __Pyx_XGOTREF(__pyx_t_4);
```

</details>

L538  🟠  (score=5)
```python
            self.error_at_scanpos("Unrecognized character")
```
<details><summary>Show generated C (score=5)</summary>

```c
      __pyx_t_11 = __pyx_v_self;
      __Pyx_INCREF(__pyx_t_11);
      __pyx_t_6 = 0;
      {
        PyObject *__pyx_callargs[2] = {__pyx_t_11, __pyx_mstate_global->__pyx_kp_u_Unrecognized_character};
        __pyx_t_8 = __Pyx_PyObject_FastCallMethod((PyObject*)__pyx_mstate_global->__pyx_n_u_error_at_scanpos, __pyx_callargs+__pyx_t_6, (2-__pyx_t_6) | (1*__Pyx_PY_VECTORCALL_ARGUMENTS_OFFSET));
        __Pyx_XDECREF(__pyx_t_11); __pyx_t_11 = 0;
        if (unlikely(!__pyx_t_8)) __PYX_ERR(0, 538, __pyx_L5_except_error)
        __Pyx_GOTREF(__pyx_t_8);
      }
      __Pyx_DECREF(__pyx_t_8); __pyx_t_8 = 0;
```

</details>

L539  🟠  (score=5)
```python
            return  # just a marker, error() always raises
```
<details><summary>Show generated C (score=5)</summary>

```c
      __Pyx_XDECREF(__pyx_r);
      __pyx_r = Py_None; __Pyx_INCREF(Py_None);
      __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
      __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
      __Pyx_DECREF(__pyx_t_7); __pyx_t_7 = 0;
      goto __pyx_L6_except_return;
    }
    goto __pyx_L5_except_error;
```

</details>

L540  🔴  (score=11)
```python
        if sy == IDENT:
```
<details><summary>Show generated C (score=11)</summary>

```c
  __Pyx_GetModuleGlobalName(__pyx_t_4, __pyx_mstate_global->__pyx_n_u_IDENT); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 540, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_4);
  __pyx_t_7 = PyObject_RichCompare(__pyx_v_sy, __pyx_t_4, Py_EQ); __Pyx_XGOTREF(__pyx_t_7); if (unlikely(!__pyx_t_7)) __PYX_ERR(0, 540, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
  __pyx_t_12 = __Pyx_PyObject_IsTrue(__pyx_t_7); if (unlikely((__pyx_t_12 < 0))) __PYX_ERR(0, 540, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_7); __pyx_t_7 = 0;
  if (__pyx_t_12) {
/* … */
  }
```

</details>

L541  🟠  (score=5)
```python
            if systring in self.keywords:
```
<details><summary>Show generated C (score=5)</summary>

```c
    __pyx_t_7 = __Pyx_PyObject_GetAttrStr(__pyx_v_self, __pyx_mstate_global->__pyx_n_u_keywords); if (unlikely(!__pyx_t_7)) __PYX_ERR(0, 541, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_7);
    __pyx_t_12 = (__Pyx_PySequence_ContainsTF(__pyx_v_systring, __pyx_t_7, Py_EQ)); if (unlikely((__pyx_t_12 < 0))) __PYX_ERR(0, 541, __pyx_L1_error)
    __Pyx_DECREF(__pyx_t_7); __pyx_t_7 = 0;
    if (__pyx_t_12) {
/* … */
    }
```

</details>

L542  🔴  (score=10)
```python
                if systring == 'print' and print_function in self.context.future_directives:
```
<details><summary>Show generated C (score=10)</summary>

```c
      __pyx_t_13 = (__Pyx_PyUnicode_Equals(__pyx_v_systring, __pyx_mstate_global->__pyx_n_u_print, Py_EQ)); if (unlikely((__pyx_t_13 < 0))) __PYX_ERR(0, 542, __pyx_L1_error)
      if (__pyx_t_13) {
      } else {
        __pyx_t_12 = __pyx_t_13;
        goto __pyx_L16_bool_binop_done;
      }
      __pyx_t_7 = __Pyx_PyObject_GetAttrStr(__pyx_v_self, __pyx_mstate_global->__pyx_n_u_context); if (unlikely(!__pyx_t_7)) __PYX_ERR(0, 542, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_7);
      __pyx_t_4 = __Pyx_PyObject_GetAttrStr(__pyx_t_7, __pyx_mstate_global->__pyx_n_u_future_directives); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 542, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_4);
      __Pyx_DECREF(__pyx_t_7); __pyx_t_7 = 0;
      __pyx_t_13 = (__Pyx_PySequence_ContainsTF(__pyx_v_6Cython_8Compiler_8Scanning_print_function, __pyx_t_4, Py_EQ)); if (unlikely((__pyx_t_13 < 0))) __PYX_ERR(0, 542, __pyx_L1_error)
      __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
      __pyx_t_12 = __pyx_t_13;
      __pyx_L16_bool_binop_done:;
      if (__pyx_t_12) {
/* … */
        goto __pyx_L15;
      }
```

</details>

L543  🔴  (score=14)
```python
                    self.keywords.pop('print', None)
```
<details><summary>Show generated C (score=14)</summary>

```c
        __pyx_t_4 = __Pyx_PyObject_GetAttrStr(__pyx_v_self, __pyx_mstate_global->__pyx_n_u_keywords); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 543, __pyx_L1_error)
        __Pyx_GOTREF(__pyx_t_4);
        __pyx_t_7 = __Pyx_PyObject_GetAttrStr(__pyx_t_4, __pyx_mstate_global->__pyx_n_u_pop); if (unlikely(!__pyx_t_7)) __PYX_ERR(0, 543, __pyx_L1_error)
        __Pyx_GOTREF(__pyx_t_7);
        __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
        __pyx_t_4 = __Pyx_PyObject_Call(__pyx_t_7, __pyx_mstate_global->__pyx_tuple[12], NULL); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 543, __pyx_L1_error)
        __Pyx_GOTREF(__pyx_t_4);
        __Pyx_DECREF(__pyx_t_7); __pyx_t_7 = 0;
        __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
/* … */
  __pyx_mstate_global->__pyx_tuple[12] = PyTuple_Pack(2, __pyx_mstate_global->__pyx_n_u_print, Py_None); if (unlikely(!__pyx_mstate_global->__pyx_tuple[12])) __PYX_ERR(0, 543, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_mstate_global->__pyx_tuple[12]);
  __Pyx_GIVEREF(__pyx_mstate_global->__pyx_tuple[12]);
```

</details>

L544  🔴  (score=16)
```python
                elif systring == 'exec' and self.context.language_level >= 3:
```
<details><summary>Show generated C (score=16)</summary>

```c
      __pyx_t_13 = (__Pyx_PyUnicode_Equals(__pyx_v_systring, __pyx_mstate_global->__pyx_n_u_exec, Py_EQ)); if (unlikely((__pyx_t_13 < 0))) __PYX_ERR(0, 544, __pyx_L1_error)
      if (__pyx_t_13) {
      } else {
        __pyx_t_12 = __pyx_t_13;
        goto __pyx_L18_bool_binop_done;
      }
      __pyx_t_4 = __Pyx_PyObject_GetAttrStr(__pyx_v_self, __pyx_mstate_global->__pyx_n_u_context); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 544, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_4);
      __pyx_t_7 = __Pyx_PyObject_GetAttrStr(__pyx_t_4, __pyx_mstate_global->__pyx_n_u_language_level); if (unlikely(!__pyx_t_7)) __PYX_ERR(0, 544, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_7);
      __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
      __pyx_t_4 = PyObject_RichCompare(__pyx_t_7, __pyx_mstate_global->__pyx_int_3, Py_GE); __Pyx_XGOTREF(__pyx_t_4); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 544, __pyx_L1_error)
      __Pyx_DECREF(__pyx_t_7); __pyx_t_7 = 0;
      __pyx_t_13 = __Pyx_PyObject_IsTrue(__pyx_t_4); if (unlikely((__pyx_t_13 < 0))) __PYX_ERR(0, 544, __pyx_L1_error)
      __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
      __pyx_t_12 = __pyx_t_13;
      __pyx_L18_bool_binop_done:;
      if (__pyx_t_12) {
/* … */
        goto __pyx_L15;
      }
```

</details>

L545  🔴  (score=14)
```python
                    self.keywords.pop('exec', None)
```
<details><summary>Show generated C (score=14)</summary>

```c
        __pyx_t_4 = __Pyx_PyObject_GetAttrStr(__pyx_v_self, __pyx_mstate_global->__pyx_n_u_keywords); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 545, __pyx_L1_error)
        __Pyx_GOTREF(__pyx_t_4);
        __pyx_t_7 = __Pyx_PyObject_GetAttrStr(__pyx_t_4, __pyx_mstate_global->__pyx_n_u_pop); if (unlikely(!__pyx_t_7)) __PYX_ERR(0, 545, __pyx_L1_error)
        __Pyx_GOTREF(__pyx_t_7);
        __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
        __pyx_t_4 = __Pyx_PyObject_Call(__pyx_t_7, __pyx_mstate_global->__pyx_tuple[13], NULL); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 545, __pyx_L1_error)
        __Pyx_GOTREF(__pyx_t_4);
        __Pyx_DECREF(__pyx_t_7); __pyx_t_7 = 0;
        __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
/* … */
  __pyx_mstate_global->__pyx_tuple[13] = PyTuple_Pack(2, __pyx_mstate_global->__pyx_n_u_exec, Py_None); if (unlikely(!__pyx_mstate_global->__pyx_tuple[13])) __PYX_ERR(0, 545, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_mstate_global->__pyx_tuple[13]);
  __Pyx_GIVEREF(__pyx_mstate_global->__pyx_tuple[13]);
```

</details>

L546  ⚪  (score=0)
```python
                else:
```
L547  🟠  (score=6)
```python
                    sy = self.keywords[systring]  # intern
```
<details><summary>Show generated C (score=6)</summary>

```c
      /*else*/ {
        __pyx_t_4 = __Pyx_PyObject_GetAttrStr(__pyx_v_self, __pyx_mstate_global->__pyx_n_u_keywords); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 547, __pyx_L1_error)
        __Pyx_GOTREF(__pyx_t_4);
        __pyx_t_7 = __Pyx_PyObject_GetItem(__pyx_t_4, __pyx_v_systring); if (unlikely(!__pyx_t_7)) __PYX_ERR(0, 547, __pyx_L1_error)
        __Pyx_GOTREF(__pyx_t_7);
        __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
        __Pyx_DECREF_SET(__pyx_v_sy, __pyx_t_7);
        __pyx_t_7 = 0;
      }
      __pyx_L15:;
```

</details>

L548  🟠  (score=8)
```python
            systring = self.context.intern_ustring(systring)
```
<details><summary>Show generated C (score=8)</summary>

```c
    __pyx_t_5 = __Pyx_PyObject_GetAttrStr(__pyx_v_self, __pyx_mstate_global->__pyx_n_u_context); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 548, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_5);
    __pyx_t_4 = __pyx_t_5;
    __Pyx_INCREF(__pyx_t_4);
    __pyx_t_6 = 0;
    {
      PyObject *__pyx_callargs[2] = {__pyx_t_4, __pyx_v_systring};
      __pyx_t_7 = __Pyx_PyObject_FastCallMethod((PyObject*)__pyx_mstate_global->__pyx_n_u_intern_ustring, __pyx_callargs+__pyx_t_6, (2-__pyx_t_6) | (1*__Pyx_PY_VECTORCALL_ARGUMENTS_OFFSET));
      __Pyx_XDECREF(__pyx_t_4); __pyx_t_4 = 0;
      __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
      if (unlikely(!__pyx_t_7)) __PYX_ERR(0, 548, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_7);
    }
    __Pyx_DECREF_SET(__pyx_v_systring, __pyx_t_7);
    __pyx_t_7 = 0;
```

</details>

L549  🟡  (score=3)
```python
        if self.put_back_on_failure is not None:
```
<details><summary>Show generated C (score=3)</summary>

```c
  __pyx_t_7 = __Pyx_PyObject_GetAttrStr(__pyx_v_self, __pyx_mstate_global->__pyx_n_u_put_back_on_failure); if (unlikely(!__pyx_t_7)) __PYX_ERR(0, 549, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_7);
  __pyx_t_12 = (__pyx_t_7 != Py_None);
  __Pyx_DECREF(__pyx_t_7); __pyx_t_7 = 0;
  if (__pyx_t_12) {
/* … */
  }
```

</details>

L550  🔴  (score=23)
```python
            self.put_back_on_failure.append((sy, systring, self.position()))
```
<details><summary>Show generated C (score=23)</summary>

```c
    __pyx_t_7 = __Pyx_PyObject_GetAttrStr(__pyx_v_self, __pyx_mstate_global->__pyx_n_u_put_back_on_failure); if (unlikely(!__pyx_t_7)) __PYX_ERR(0, 550, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_7);
    __pyx_t_4 = __pyx_v_self;
    __Pyx_INCREF(__pyx_t_4);
    __pyx_t_6 = 0;
    {
      PyObject *__pyx_callargs[2] = {__pyx_t_4, NULL};
      __pyx_t_5 = __Pyx_PyObject_FastCallMethod((PyObject*)__pyx_mstate_global->__pyx_n_u_position, __pyx_callargs+__pyx_t_6, (1-__pyx_t_6) | (1*__Pyx_PY_VECTORCALL_ARGUMENTS_OFFSET));
      __Pyx_XDECREF(__pyx_t_4); __pyx_t_4 = 0;
      if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 550, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_5);
    }
    __pyx_t_4 = PyTuple_New(3); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 550, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_4);
    __Pyx_INCREF(__pyx_v_sy);
    __Pyx_GIVEREF(__pyx_v_sy);
    if (__Pyx_PyTuple_SET_ITEM(__pyx_t_4, 0, __pyx_v_sy) != (0)) __PYX_ERR(0, 550, __pyx_L1_error);
    __Pyx_INCREF(__pyx_v_systring);
    __Pyx_GIVEREF(__pyx_v_systring);
    if (__Pyx_PyTuple_SET_ITEM(__pyx_t_4, 1, __pyx_v_systring) != (0)) __PYX_ERR(0, 550, __pyx_L1_error);
    __Pyx_GIVEREF(__pyx_t_5);
    if (__Pyx_PyTuple_SET_ITEM(__pyx_t_4, 2, __pyx_t_5) != (0)) __PYX_ERR(0, 550, __pyx_L1_error);
    __pyx_t_5 = 0;
    __pyx_t_14 = __Pyx_PyObject_Append(__pyx_t_7, __pyx_t_4); if (unlikely(__pyx_t_14 == ((int)-1))) __PYX_ERR(0, 550, __pyx_L1_error)
    __Pyx_DECREF(__pyx_t_7); __pyx_t_7 = 0;
    __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
```

</details>

L551  🟡  (score=2)
```python
        self.sy = sy
```
<details><summary>Show generated C (score=2)</summary>

```c
  if (__Pyx_PyObject_SetAttrStr(__pyx_v_self, __pyx_mstate_global->__pyx_n_u_sy, __pyx_v_sy) < (0)) __PYX_ERR(0, 551, __pyx_L1_error)
```

</details>

L552  🟡  (score=2)
```python
        self.systring = systring
```
<details><summary>Show generated C (score=2)</summary>

```c
  if (__Pyx_PyObject_SetAttrStr(__pyx_v_self, __pyx_mstate_global->__pyx_n_u_systring, __pyx_v_systring) < (0)) __PYX_ERR(0, 552, __pyx_L1_error)
```

</details>

L553  ⚪  (score=0)
```python
        if False:  # debug_scanner:
```
L554  ⚪  (score=0)
```python
            _, line, col = self.position()
```
L555  ⚪  (score=0)
```python
            if not self.systring or self.sy == self.systring:
```
L556  ⚪  (score=0)
```python
                t = self.sy
```
L557  ⚪  (score=0)
```python
            else:
```
L558  ⚪  (score=0)
```python
                t = "%s %s" % (self.sy, self.systring)
```
L559  ⚪  (score=0)
```python
            print("--- %3d %2d %s" % (line, col, t))
```
L560  ⚪  (score=0)
```python
```
L561  🔴  (score=44)
```python
    def peek(self):
```
<details><summary>Show generated C (score=44)</summary>

```c
/* Python wrapper */
static PyObject *__pyx_pw_6Cython_8Compiler_8Scanning_12PyrexScanner_47peek(PyObject *__pyx_self, 
#if CYTHON_METH_FASTCALL
PyObject *const *__pyx_args, Py_ssize_t __pyx_nargs, PyObject *__pyx_kwds
#else
PyObject *__pyx_args, PyObject *__pyx_kwds
#endif
); /*proto*/
PyDoc_STRVAR(__pyx_doc_6Cython_8Compiler_8Scanning_12PyrexScanner_46peek, "File: Cython/Compiler/Scanning.py (starting at line 561)");
static PyMethodDef __pyx_mdef_6Cython_8Compiler_8Scanning_12PyrexScanner_47peek = {"peek", (PyCFunction)(void(*)(void))(__Pyx_PyCFunction_FastCallWithKeywords)__pyx_pw_6Cython_8Compiler_8Scanning_12PyrexScanner_47peek, __Pyx_METH_FASTCALL|METH_KEYWORDS, __pyx_doc_6Cython_8Compiler_8Scanning_12PyrexScanner_46peek};
static PyObject *__pyx_pw_6Cython_8Compiler_8Scanning_12PyrexScanner_47peek(PyObject *__pyx_self, 
#if CYTHON_METH_FASTCALL
PyObject *const *__pyx_args, Py_ssize_t __pyx_nargs, PyObject *__pyx_kwds
#else
PyObject *__pyx_args, PyObject *__pyx_kwds
#endif
) {
  PyObject *__pyx_v_self = 0;
  #if !CYTHON_METH_FASTCALL
  CYTHON_UNUSED Py_ssize_t __pyx_nargs;
  #endif
  CYTHON_UNUSED PyObject *const *__pyx_kwvalues;
  PyObject *__pyx_r = 0;
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("peek (wrapper)", 0);
  #if !CYTHON_METH_FASTCALL
  #if CYTHON_ASSUME_SAFE_SIZE
  __pyx_nargs = PyTuple_GET_SIZE(__pyx_args);
  #else
  __pyx_nargs = PyTuple_Size(__pyx_args); if (unlikely(__pyx_nargs < 0)) return NULL;
  #endif
  #endif
  __pyx_kwvalues = __Pyx_KwValues_FASTCALL(__pyx_args, __pyx_nargs);
  {
    PyObject ** const __pyx_pyargnames[] = {&__pyx_mstate_global->__pyx_n_u_self,0};
  PyObject* values[1] = {0};
    const Py_ssize_t __pyx_kwds_len = (__pyx_kwds) ? __Pyx_NumKwargs_FASTCALL(__pyx_kwds) : 0;
    if (unlikely(__pyx_kwds_len) < 0) __PYX_ERR(0, 561, __pyx_L3_error)
    if (__pyx_kwds_len > 0) {
      switch (__pyx_nargs) {
        case  1:
        values[0] = __Pyx_ArgRef_FASTCALL(__pyx_args, 0);
        if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[0])) __PYX_ERR(0, 561, __pyx_L3_error)
        CYTHON_FALLTHROUGH;
        case  0: break;
        default: goto __pyx_L5_argtuple_error;
      }
      const Py_ssize_t kwd_pos_args = __pyx_nargs;
      if (__Pyx_ParseKeywords(__pyx_kwds, __pyx_kwvalues, __pyx_pyargnames, 0, values, kwd_pos_args, __pyx_kwds_len, "peek", 0) < (0)) __PYX_ERR(0, 561, __pyx_L3_error)
      for (Py_ssize_t i = __pyx_nargs; i < 1; i++) {
        if (unlikely(!values[i])) { __Pyx_RaiseArgtupleInvalid("peek", 1, 1, 1, i); __PYX_ERR(0, 561, __pyx_L3_error) }
      }
    } else if (unlikely(__pyx_nargs != 1)) {
      goto __pyx_L5_argtuple_error;
    } else {
      values[0] = __Pyx_ArgRef_FASTCALL(__pyx_args, 0);
      if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[0])) __PYX_ERR(0, 561, __pyx_L3_error)
    }
    __pyx_v_self = values[0];
  }
  goto __pyx_L6_skip;
  __pyx_L5_argtuple_error:;
  __Pyx_RaiseArgtupleInvalid("peek", 1, 1, 1, __pyx_nargs); __PYX_ERR(0, 561, __pyx_L3_error)
  __pyx_L6_skip:;
  goto __pyx_L4_argument_unpacking_done;
  __pyx_L3_error:;
  for (Py_ssize_t __pyx_temp=0; __pyx_temp < (Py_ssize_t)(sizeof(values)/sizeof(values[0])); ++__pyx_temp) {
    Py_XDECREF(values[__pyx_temp]);
  }
  __Pyx_AddTraceback("Cython.Compiler.Scanning.PyrexScanner.peek", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __Pyx_RefNannyFinishContext();
  return NULL;
  __pyx_L4_argument_unpacking_done:;
  __pyx_r = __pyx_pf_6Cython_8Compiler_8Scanning_12PyrexScanner_46peek(__pyx_self, __pyx_v_self);
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

static PyObject *__pyx_pf_6Cython_8Compiler_8Scanning_12PyrexScanner_46peek(CYTHON_UNUSED PyObject *__pyx_self, PyObject *__pyx_v_self) {
  PyObject *__pyx_v_saved = NULL;
  PyObject *__pyx_v_saved_pos = NULL;
  PyObject *__pyx_v_next = NULL;
  PyObject *__pyx_r = NULL;
/* … */
  /* function exit code */
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_t_1);
  __Pyx_XDECREF(__pyx_t_2);
  __Pyx_XDECREF(__pyx_t_3);
  __Pyx_XDECREF(__pyx_t_5);
  __Pyx_XDECREF(__pyx_t_6);
  __Pyx_XDECREF(__pyx_t_7);
  __Pyx_AddTraceback("Cython.Compiler.Scanning.PyrexScanner.peek", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_r = NULL;
  __pyx_L0:;
  __Pyx_XDECREF(__pyx_v_saved);
  __Pyx_XDECREF(__pyx_v_saved_pos);
  __Pyx_XDECREF(__pyx_v_next);
  __Pyx_XGIVEREF(__pyx_r);
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}
/* … */
  __pyx_t_9 = __Pyx_CyFunction_New(&__pyx_mdef_6Cython_8Compiler_8Scanning_12PyrexScanner_47peek, 0, __pyx_mstate_global->__pyx_n_u_PyrexScanner_peek, NULL, __pyx_mstate_global->__pyx_n_u_Cython_Compiler_Scanning, __pyx_mstate_global->__pyx_d, ((PyObject *)__pyx_mstate_global->__pyx_codeobj_tab[58])); if (unlikely(!__pyx_t_9)) __PYX_ERR(0, 561, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_9);
  #if CYTHON_COMPILING_IN_CPYTHON && PY_VERSION_HEX >= 0x030E0000
  PyUnstable_Object_EnableDeferredRefcount(__pyx_t_9);
  #endif
  if (__Pyx_SetNameInClass(__pyx_t_8, __pyx_mstate_global->__pyx_n_u_peek, __pyx_t_9) < (0)) __PYX_ERR(0, 561, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_9); __pyx_t_9 = 0;
```

</details>

L562  🔴  (score=13)
```python
        saved = self.sy, self.systring
```
<details><summary>Show generated C (score=13)</summary>

```c
  __pyx_t_1 = __Pyx_PyObject_GetAttrStr(__pyx_v_self, __pyx_mstate_global->__pyx_n_u_sy); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 562, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __pyx_t_2 = __Pyx_PyObject_GetAttrStr(__pyx_v_self, __pyx_mstate_global->__pyx_n_u_systring); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 562, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __pyx_t_3 = PyTuple_New(2); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 562, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_3);
  __Pyx_GIVEREF(__pyx_t_1);
  if (__Pyx_PyTuple_SET_ITEM(__pyx_t_3, 0, __pyx_t_1) != (0)) __PYX_ERR(0, 562, __pyx_L1_error);
  __Pyx_GIVEREF(__pyx_t_2);
  if (__Pyx_PyTuple_SET_ITEM(__pyx_t_3, 1, __pyx_t_2) != (0)) __PYX_ERR(0, 562, __pyx_L1_error);
  __pyx_t_1 = 0;
  __pyx_t_2 = 0;
  __pyx_v_saved = __pyx_t_3;
  __pyx_t_3 = 0;
```

</details>

L563  🟡  (score=4)
```python
        saved_pos = self.position()
```
<details><summary>Show generated C (score=4)</summary>

```c
  __pyx_t_2 = __pyx_v_self;
  __Pyx_INCREF(__pyx_t_2);
  __pyx_t_4 = 0;
  {
    PyObject *__pyx_callargs[2] = {__pyx_t_2, NULL};
    __pyx_t_3 = __Pyx_PyObject_FastCallMethod((PyObject*)__pyx_mstate_global->__pyx_n_u_position, __pyx_callargs+__pyx_t_4, (1-__pyx_t_4) | (1*__Pyx_PY_VECTORCALL_ARGUMENTS_OFFSET));
    __Pyx_XDECREF(__pyx_t_2); __pyx_t_2 = 0;
    if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 563, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_3);
  }
  __pyx_v_saved_pos = __pyx_t_3;
  __pyx_t_3 = 0;
```

</details>

L564  🟠  (score=5)
```python
        self.next()
```
<details><summary>Show generated C (score=5)</summary>

```c
  __pyx_t_2 = __pyx_v_self;
  __Pyx_INCREF(__pyx_t_2);
  __pyx_t_4 = 0;
  {
    PyObject *__pyx_callargs[2] = {__pyx_t_2, NULL};
    __pyx_t_3 = __Pyx_PyObject_FastCallMethod((PyObject*)__pyx_mstate_global->__pyx_n_u_next, __pyx_callargs+__pyx_t_4, (1-__pyx_t_4) | (1*__Pyx_PY_VECTORCALL_ARGUMENTS_OFFSET));
    __Pyx_XDECREF(__pyx_t_2); __pyx_t_2 = 0;
    if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 564, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_3);
  }
  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
```

</details>

L565  🔴  (score=13)
```python
        next = self.sy, self.systring
```
<details><summary>Show generated C (score=13)</summary>

```c
  __pyx_t_3 = __Pyx_PyObject_GetAttrStr(__pyx_v_self, __pyx_mstate_global->__pyx_n_u_sy); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 565, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_3);
  __pyx_t_2 = __Pyx_PyObject_GetAttrStr(__pyx_v_self, __pyx_mstate_global->__pyx_n_u_systring); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 565, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __pyx_t_1 = PyTuple_New(2); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 565, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_GIVEREF(__pyx_t_3);
  if (__Pyx_PyTuple_SET_ITEM(__pyx_t_1, 0, __pyx_t_3) != (0)) __PYX_ERR(0, 565, __pyx_L1_error);
  __Pyx_GIVEREF(__pyx_t_2);
  if (__Pyx_PyTuple_SET_ITEM(__pyx_t_1, 1, __pyx_t_2) != (0)) __PYX_ERR(0, 565, __pyx_L1_error);
  __pyx_t_3 = 0;
  __pyx_t_2 = 0;
  __pyx_v_next = __pyx_t_1;
  __pyx_t_1 = 0;
```

</details>

L566  🔴  (score=16)
```python
        self.unread(self.sy, self.systring, self.position())
```
<details><summary>Show generated C (score=16)</summary>

```c
  __pyx_t_2 = __pyx_v_self;
  __Pyx_INCREF(__pyx_t_2);
  __pyx_t_3 = __Pyx_PyObject_GetAttrStr(__pyx_v_self, __pyx_mstate_global->__pyx_n_u_sy); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 566, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_3);
  __pyx_t_5 = __Pyx_PyObject_GetAttrStr(__pyx_v_self, __pyx_mstate_global->__pyx_n_u_systring); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 566, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_5);
  __pyx_t_7 = __pyx_v_self;
  __Pyx_INCREF(__pyx_t_7);
  __pyx_t_4 = 0;
  {
    PyObject *__pyx_callargs[2] = {__pyx_t_7, NULL};
    __pyx_t_6 = __Pyx_PyObject_FastCallMethod((PyObject*)__pyx_mstate_global->__pyx_n_u_position, __pyx_callargs+__pyx_t_4, (1-__pyx_t_4) | (1*__Pyx_PY_VECTORCALL_ARGUMENTS_OFFSET));
    __Pyx_XDECREF(__pyx_t_7); __pyx_t_7 = 0;
    if (unlikely(!__pyx_t_6)) __PYX_ERR(0, 566, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_6);
  }
  __pyx_t_4 = 0;
  {
    PyObject *__pyx_callargs[4] = {__pyx_t_2, __pyx_t_3, __pyx_t_5, __pyx_t_6};
    __pyx_t_1 = __Pyx_PyObject_FastCallMethod((PyObject*)__pyx_mstate_global->__pyx_n_u_unread, __pyx_callargs+__pyx_t_4, (4-__pyx_t_4) | (1*__Pyx_PY_VECTORCALL_ARGUMENTS_OFFSET));
    __Pyx_XDECREF(__pyx_t_2); __pyx_t_2 = 0;
    __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
    __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
    __Pyx_DECREF(__pyx_t_6); __pyx_t_6 = 0;
    if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 566, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_1);
  }
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
```

</details>

L567  🔴  (score=54)
```python
        self.sy, self.systring = saved
```
<details><summary>Show generated C (score=54)</summary>

```c
  if ((likely(PyTuple_CheckExact(__pyx_v_saved))) || (PyList_CheckExact(__pyx_v_saved))) {
    PyObject* sequence = __pyx_v_saved;
    Py_ssize_t size = __Pyx_PySequence_SIZE(sequence);
    if (unlikely(size != 2)) {
      if (size > 2) __Pyx_RaiseTooManyValuesError(2);
      else if (size >= 0) __Pyx_RaiseNeedMoreValuesError(size);
      __PYX_ERR(0, 567, __pyx_L1_error)
    }
    #if CYTHON_ASSUME_SAFE_MACROS && !CYTHON_AVOID_BORROWED_REFS
    if (likely(PyTuple_CheckExact(sequence))) {
      __pyx_t_1 = PyTuple_GET_ITEM(sequence, 0);
      __Pyx_INCREF(__pyx_t_1);
      __pyx_t_6 = PyTuple_GET_ITEM(sequence, 1);
      __Pyx_INCREF(__pyx_t_6);
    } else {
      __pyx_t_1 = __Pyx_PyList_GetItemRefFast(sequence, 0, __Pyx_ReferenceSharing_SharedReference);
      if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 567, __pyx_L1_error)
      __Pyx_XGOTREF(__pyx_t_1);
      __pyx_t_6 = __Pyx_PyList_GetItemRefFast(sequence, 1, __Pyx_ReferenceSharing_SharedReference);
      if (unlikely(!__pyx_t_6)) __PYX_ERR(0, 567, __pyx_L1_error)
      __Pyx_XGOTREF(__pyx_t_6);
    }
    #else
    __pyx_t_1 = __Pyx_PySequence_ITEM(sequence, 0); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 567, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_1);
    __pyx_t_6 = __Pyx_PySequence_ITEM(sequence, 1); if (unlikely(!__pyx_t_6)) __PYX_ERR(0, 567, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_6);
    #endif
  } else {
    Py_ssize_t index = -1;
    __pyx_t_5 = PyObject_GetIter(__pyx_v_saved); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 567, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_5);
    __pyx_t_8 = (CYTHON_COMPILING_IN_LIMITED_API) ? PyIter_Next : __Pyx_PyObject_GetIterNextFunc(__pyx_t_5);
    index = 0; __pyx_t_1 = __pyx_t_8(__pyx_t_5); if (unlikely(!__pyx_t_1)) goto __pyx_L3_unpacking_failed;
    __Pyx_GOTREF(__pyx_t_1);
    index = 1; __pyx_t_6 = __pyx_t_8(__pyx_t_5); if (unlikely(!__pyx_t_6)) goto __pyx_L3_unpacking_failed;
    __Pyx_GOTREF(__pyx_t_6);
    if (__Pyx_IternextUnpackEndCheck(__pyx_t_8(__pyx_t_5), 2) < (0)) __PYX_ERR(0, 567, __pyx_L1_error)
    __pyx_t_8 = NULL;
    __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
    goto __pyx_L4_unpacking_done;
    __pyx_L3_unpacking_failed:;
    __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
    __pyx_t_8 = NULL;
    if (__Pyx_IterFinish() == 0) __Pyx_RaiseNeedMoreValuesError(index);
    __PYX_ERR(0, 567, __pyx_L1_error)
    __pyx_L4_unpacking_done:;
  }
  if (__Pyx_PyObject_SetAttrStr(__pyx_v_self, __pyx_mstate_global->__pyx_n_u_sy, __pyx_t_1) < (0)) __PYX_ERR(0, 567, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  if (__Pyx_PyObject_SetAttrStr(__pyx_v_self, __pyx_mstate_global->__pyx_n_u_systring, __pyx_t_6) < (0)) __PYX_ERR(0, 567, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_6); __pyx_t_6 = 0;
```

</details>

L568  🟡  (score=2)
```python
        self.last_token_position_tuple = saved_pos
```
<details><summary>Show generated C (score=2)</summary>

```c
  if (__Pyx_PyObject_SetAttrStr(__pyx_v_self, __pyx_mstate_global->__pyx_n_u_last_token_position_tuple, __pyx_v_saved_pos) < (0)) __PYX_ERR(0, 568, __pyx_L1_error)
```

</details>

L569  🟡  (score=2)
```python
        return next
```
<details><summary>Show generated C (score=2)</summary>

```c
  __Pyx_XDECREF(__pyx_r);
  __Pyx_INCREF(__pyx_v_next);
  __pyx_r = __pyx_v_next;
  goto __pyx_L0;
```

</details>

L570  ⚪  (score=0)
```python
```
L571  🔴  (score=53)
```python
    def put_back(self, sy, systring, pos):
```
<details><summary>Show generated C (score=53)</summary>

```c
/* Python wrapper */
static PyObject *__pyx_pw_6Cython_8Compiler_8Scanning_12PyrexScanner_49put_back(PyObject *__pyx_self, 
#if CYTHON_METH_FASTCALL
PyObject *const *__pyx_args, Py_ssize_t __pyx_nargs, PyObject *__pyx_kwds
#else
PyObject *__pyx_args, PyObject *__pyx_kwds
#endif
); /*proto*/
PyDoc_STRVAR(__pyx_doc_6Cython_8Compiler_8Scanning_12PyrexScanner_48put_back, "File: Cython/Compiler/Scanning.py (starting at line 571)");
static PyMethodDef __pyx_mdef_6Cython_8Compiler_8Scanning_12PyrexScanner_49put_back = {"put_back", (PyCFunction)(void(*)(void))(__Pyx_PyCFunction_FastCallWithKeywords)__pyx_pw_6Cython_8Compiler_8Scanning_12PyrexScanner_49put_back, __Pyx_METH_FASTCALL|METH_KEYWORDS, __pyx_doc_6Cython_8Compiler_8Scanning_12PyrexScanner_48put_back};
static PyObject *__pyx_pw_6Cython_8Compiler_8Scanning_12PyrexScanner_49put_back(PyObject *__pyx_self, 
#if CYTHON_METH_FASTCALL
PyObject *const *__pyx_args, Py_ssize_t __pyx_nargs, PyObject *__pyx_kwds
#else
PyObject *__pyx_args, PyObject *__pyx_kwds
#endif
) {
  PyObject *__pyx_v_self = 0;
  PyObject *__pyx_v_sy = 0;
  PyObject *__pyx_v_systring = 0;
  PyObject *__pyx_v_pos = 0;
  #if !CYTHON_METH_FASTCALL
  CYTHON_UNUSED Py_ssize_t __pyx_nargs;
  #endif
  CYTHON_UNUSED PyObject *const *__pyx_kwvalues;
  PyObject *__pyx_r = 0;
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("put_back (wrapper)", 0);
  #if !CYTHON_METH_FASTCALL
  #if CYTHON_ASSUME_SAFE_SIZE
  __pyx_nargs = PyTuple_GET_SIZE(__pyx_args);
  #else
  __pyx_nargs = PyTuple_Size(__pyx_args); if (unlikely(__pyx_nargs < 0)) return NULL;
  #endif
  #endif
  __pyx_kwvalues = __Pyx_KwValues_FASTCALL(__pyx_args, __pyx_nargs);
  {
    PyObject ** const __pyx_pyargnames[] = {&__pyx_mstate_global->__pyx_n_u_self,&__pyx_mstate_global->__pyx_n_u_sy,&__pyx_mstate_global->__pyx_n_u_systring,&__pyx_mstate_global->__pyx_n_u_pos,0};
  PyObject* values[4] = {0,0,0,0};
    const Py_ssize_t __pyx_kwds_len = (__pyx_kwds) ? __Pyx_NumKwargs_FASTCALL(__pyx_kwds) : 0;
    if (unlikely(__pyx_kwds_len) < 0) __PYX_ERR(0, 571, __pyx_L3_error)
    if (__pyx_kwds_len > 0) {
      switch (__pyx_nargs) {
        case  4:
        values[3] = __Pyx_ArgRef_FASTCALL(__pyx_args, 3);
        if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[3])) __PYX_ERR(0, 571, __pyx_L3_error)
        CYTHON_FALLTHROUGH;
        case  3:
        values[2] = __Pyx_ArgRef_FASTCALL(__pyx_args, 2);
        if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[2])) __PYX_ERR(0, 571, __pyx_L3_error)
        CYTHON_FALLTHROUGH;
        case  2:
        values[1] = __Pyx_ArgRef_FASTCALL(__pyx_args, 1);
        if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[1])) __PYX_ERR(0, 571, __pyx_L3_error)
        CYTHON_FALLTHROUGH;
        case  1:
        values[0] = __Pyx_ArgRef_FASTCALL(__pyx_args, 0);
        if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[0])) __PYX_ERR(0, 571, __pyx_L3_error)
        CYTHON_FALLTHROUGH;
        case  0: break;
        default: goto __pyx_L5_argtuple_error;
      }
      const Py_ssize_t kwd_pos_args = __pyx_nargs;
      if (__Pyx_ParseKeywords(__pyx_kwds, __pyx_kwvalues, __pyx_pyargnames, 0, values, kwd_pos_args, __pyx_kwds_len, "put_back", 0) < (0)) __PYX_ERR(0, 571, __pyx_L3_error)
      for (Py_ssize_t i = __pyx_nargs; i < 4; i++) {
        if (unlikely(!values[i])) { __Pyx_RaiseArgtupleInvalid("put_back", 1, 4, 4, i); __PYX_ERR(0, 571, __pyx_L3_error) }
      }
    } else if (unlikely(__pyx_nargs != 4)) {
      goto __pyx_L5_argtuple_error;
    } else {
      values[0] = __Pyx_ArgRef_FASTCALL(__pyx_args, 0);
      if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[0])) __PYX_ERR(0, 571, __pyx_L3_error)
      values[1] = __Pyx_ArgRef_FASTCALL(__pyx_args, 1);
      if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[1])) __PYX_ERR(0, 571, __pyx_L3_error)
      values[2] = __Pyx_ArgRef_FASTCALL(__pyx_args, 2);
      if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[2])) __PYX_ERR(0, 571, __pyx_L3_error)
      values[3] = __Pyx_ArgRef_FASTCALL(__pyx_args, 3);
      if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[3])) __PYX_ERR(0, 571, __pyx_L3_error)
    }
    __pyx_v_self = values[0];
    __pyx_v_sy = values[1];
    __pyx_v_systring = values[2];
    __pyx_v_pos = values[3];
  }
  goto __pyx_L6_skip;
  __pyx_L5_argtuple_error:;
  __Pyx_RaiseArgtupleInvalid("put_back", 1, 4, 4, __pyx_nargs); __PYX_ERR(0, 571, __pyx_L3_error)
  __pyx_L6_skip:;
  goto __pyx_L4_argument_unpacking_done;
  __pyx_L3_error:;
  for (Py_ssize_t __pyx_temp=0; __pyx_temp < (Py_ssize_t)(sizeof(values)/sizeof(values[0])); ++__pyx_temp) {
    Py_XDECREF(values[__pyx_temp]);
  }
  __Pyx_AddTraceback("Cython.Compiler.Scanning.PyrexScanner.put_back", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __Pyx_RefNannyFinishContext();
  return NULL;
  __pyx_L4_argument_unpacking_done:;
  __pyx_r = __pyx_pf_6Cython_8Compiler_8Scanning_12PyrexScanner_48put_back(__pyx_self, __pyx_v_self, __pyx_v_sy, __pyx_v_systring, __pyx_v_pos);
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

static PyObject *__pyx_pf_6Cython_8Compiler_8Scanning_12PyrexScanner_48put_back(CYTHON_UNUSED PyObject *__pyx_self, PyObject *__pyx_v_self, PyObject *__pyx_v_sy, PyObject *__pyx_v_systring, PyObject *__pyx_v_pos) {
  PyObject *__pyx_r = NULL;
/* … */
  /* function exit code */
  __pyx_r = Py_None; __Pyx_INCREF(Py_None);
  goto __pyx_L0;
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_t_1);
  __Pyx_XDECREF(__pyx_t_2);
  __Pyx_XDECREF(__pyx_t_3);
  __Pyx_XDECREF(__pyx_t_4);
  __Pyx_XDECREF(__pyx_t_5);
  __Pyx_AddTraceback("Cython.Compiler.Scanning.PyrexScanner.put_back", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_r = NULL;
  __pyx_L0:;
  __Pyx_XGIVEREF(__pyx_r);
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}
/* … */
  __pyx_t_9 = __Pyx_CyFunction_New(&__pyx_mdef_6Cython_8Compiler_8Scanning_12PyrexScanner_49put_back, 0, __pyx_mstate_global->__pyx_n_u_PyrexScanner_put_back, NULL, __pyx_mstate_global->__pyx_n_u_Cython_Compiler_Scanning, __pyx_mstate_global->__pyx_d, ((PyObject *)__pyx_mstate_global->__pyx_codeobj_tab[59])); if (unlikely(!__pyx_t_9)) __PYX_ERR(0, 571, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_9);
  #if CYTHON_COMPILING_IN_CPYTHON && PY_VERSION_HEX >= 0x030E0000
  PyUnstable_Object_EnableDeferredRefcount(__pyx_t_9);
  #endif
  if (__Pyx_SetNameInClass(__pyx_t_8, __pyx_mstate_global->__pyx_n_u_put_back, __pyx_t_9) < (0)) __PYX_ERR(0, 571, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_9); __pyx_t_9 = 0;
```

</details>

L572  🔴  (score=14)
```python
        self.unread(self.sy, self.systring, self.last_token_position_tuple)
```
<details><summary>Show generated C (score=14)</summary>

```c
  __pyx_t_2 = __pyx_v_self;
  __Pyx_INCREF(__pyx_t_2);
  __pyx_t_3 = __Pyx_PyObject_GetAttrStr(__pyx_v_self, __pyx_mstate_global->__pyx_n_u_sy); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 572, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_3);
  __pyx_t_4 = __Pyx_PyObject_GetAttrStr(__pyx_v_self, __pyx_mstate_global->__pyx_n_u_systring); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 572, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_4);
  __pyx_t_5 = __Pyx_PyObject_GetAttrStr(__pyx_v_self, __pyx_mstate_global->__pyx_n_u_last_token_position_tuple); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 572, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_5);
  __pyx_t_6 = 0;
  {
    PyObject *__pyx_callargs[4] = {__pyx_t_2, __pyx_t_3, __pyx_t_4, __pyx_t_5};
    __pyx_t_1 = __Pyx_PyObject_FastCallMethod((PyObject*)__pyx_mstate_global->__pyx_n_u_unread, __pyx_callargs+__pyx_t_6, (4-__pyx_t_6) | (1*__Pyx_PY_VECTORCALL_ARGUMENTS_OFFSET));
    __Pyx_XDECREF(__pyx_t_2); __pyx_t_2 = 0;
    __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
    __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
    __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
    if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 572, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_1);
  }
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
```

</details>

L573  🟡  (score=2)
```python
        self.sy = sy
```
<details><summary>Show generated C (score=2)</summary>

```c
  if (__Pyx_PyObject_SetAttrStr(__pyx_v_self, __pyx_mstate_global->__pyx_n_u_sy, __pyx_v_sy) < (0)) __PYX_ERR(0, 573, __pyx_L1_error)
```

</details>

L574  🟡  (score=2)
```python
        self.systring = systring
```
<details><summary>Show generated C (score=2)</summary>

```c
  if (__Pyx_PyObject_SetAttrStr(__pyx_v_self, __pyx_mstate_global->__pyx_n_u_systring, __pyx_v_systring) < (0)) __PYX_ERR(0, 574, __pyx_L1_error)
```

</details>

L575  🟡  (score=2)
```python
        self.last_token_position_tuple = pos
```
<details><summary>Show generated C (score=2)</summary>

```c
  if (__Pyx_PyObject_SetAttrStr(__pyx_v_self, __pyx_mstate_global->__pyx_n_u_last_token_position_tuple, __pyx_v_pos) < (0)) __PYX_ERR(0, 575, __pyx_L1_error)
```

</details>

L576  ⚪  (score=0)
```python
```
L577  ⚪  (score=0)
```python
```
L578  🔴  (score=69)
```python
    def error(self, message, pos=None, fatal=True):
```
<details><summary>Show generated C (score=69)</summary>

```c
/* Python wrapper */
static PyObject *__pyx_pw_6Cython_8Compiler_8Scanning_12PyrexScanner_51error(PyObject *__pyx_self, 
#if CYTHON_METH_FASTCALL
PyObject *const *__pyx_args, Py_ssize_t __pyx_nargs, PyObject *__pyx_kwds
#else
PyObject *__pyx_args, PyObject *__pyx_kwds
#endif
); /*proto*/
PyDoc_STRVAR(__pyx_doc_6Cython_8Compiler_8Scanning_12PyrexScanner_50error, "File: Cython/Compiler/Scanning.py (starting at line 578)");
static PyMethodDef __pyx_mdef_6Cython_8Compiler_8Scanning_12PyrexScanner_51error = {"error", (PyCFunction)(void(*)(void))(__Pyx_PyCFunction_FastCallWithKeywords)__pyx_pw_6Cython_8Compiler_8Scanning_12PyrexScanner_51error, __Pyx_METH_FASTCALL|METH_KEYWORDS, __pyx_doc_6Cython_8Compiler_8Scanning_12PyrexScanner_50error};
static PyObject *__pyx_pw_6Cython_8Compiler_8Scanning_12PyrexScanner_51error(PyObject *__pyx_self, 
#if CYTHON_METH_FASTCALL
PyObject *const *__pyx_args, Py_ssize_t __pyx_nargs, PyObject *__pyx_kwds
#else
PyObject *__pyx_args, PyObject *__pyx_kwds
#endif
) {
  PyObject *__pyx_v_self = 0;
  PyObject *__pyx_v_message = 0;
  PyObject *__pyx_v_pos = 0;
  PyObject *__pyx_v_fatal = 0;
  #if !CYTHON_METH_FASTCALL
  CYTHON_UNUSED Py_ssize_t __pyx_nargs;
  #endif
  CYTHON_UNUSED PyObject *const *__pyx_kwvalues;
  PyObject *__pyx_r = 0;
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("error (wrapper)", 0);
  #if !CYTHON_METH_FASTCALL
  #if CYTHON_ASSUME_SAFE_SIZE
  __pyx_nargs = PyTuple_GET_SIZE(__pyx_args);
  #else
  __pyx_nargs = PyTuple_Size(__pyx_args); if (unlikely(__pyx_nargs < 0)) return NULL;
  #endif
  #endif
  __pyx_kwvalues = __Pyx_KwValues_FASTCALL(__pyx_args, __pyx_nargs);
  {
    PyObject ** const __pyx_pyargnames[] = {&__pyx_mstate_global->__pyx_n_u_self,&__pyx_mstate_global->__pyx_n_u_message,&__pyx_mstate_global->__pyx_n_u_pos,&__pyx_mstate_global->__pyx_n_u_fatal,0};
  PyObject* values[4] = {0,0,0,0};
    const Py_ssize_t __pyx_kwds_len = (__pyx_kwds) ? __Pyx_NumKwargs_FASTCALL(__pyx_kwds) : 0;
    if (unlikely(__pyx_kwds_len) < 0) __PYX_ERR(0, 578, __pyx_L3_error)
    if (__pyx_kwds_len > 0) {
      switch (__pyx_nargs) {
        case  4:
        values[3] = __Pyx_ArgRef_FASTCALL(__pyx_args, 3);
        if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[3])) __PYX_ERR(0, 578, __pyx_L3_error)
        CYTHON_FALLTHROUGH;
        case  3:
        values[2] = __Pyx_ArgRef_FASTCALL(__pyx_args, 2);
        if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[2])) __PYX_ERR(0, 578, __pyx_L3_error)
        CYTHON_FALLTHROUGH;
        case  2:
        values[1] = __Pyx_ArgRef_FASTCALL(__pyx_args, 1);
        if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[1])) __PYX_ERR(0, 578, __pyx_L3_error)
        CYTHON_FALLTHROUGH;
        case  1:
        values[0] = __Pyx_ArgRef_FASTCALL(__pyx_args, 0);
        if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[0])) __PYX_ERR(0, 578, __pyx_L3_error)
        CYTHON_FALLTHROUGH;
        case  0: break;
        default: goto __pyx_L5_argtuple_error;
      }
      const Py_ssize_t kwd_pos_args = __pyx_nargs;
      if (__Pyx_ParseKeywords(__pyx_kwds, __pyx_kwvalues, __pyx_pyargnames, 0, values, kwd_pos_args, __pyx_kwds_len, "error", 0) < (0)) __PYX_ERR(0, 578, __pyx_L3_error)
      if (!values[2]) values[2] = __Pyx_NewRef(((PyObject *)Py_None));
      if (!values[3]) values[3] = __Pyx_NewRef(((PyObject *)((PyObject*)Py_True)));
      for (Py_ssize_t i = __pyx_nargs; i < 2; i++) {
        if (unlikely(!values[i])) { __Pyx_RaiseArgtupleInvalid("error", 0, 2, 4, i); __PYX_ERR(0, 578, __pyx_L3_error) }
      }
    } else {
      switch (__pyx_nargs) {
        case  4:
        values[3] = __Pyx_ArgRef_FASTCALL(__pyx_args, 3);
        if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[3])) __PYX_ERR(0, 578, __pyx_L3_error)
        CYTHON_FALLTHROUGH;
        case  3:
        values[2] = __Pyx_ArgRef_FASTCALL(__pyx_args, 2);
        if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[2])) __PYX_ERR(0, 578, __pyx_L3_error)
        CYTHON_FALLTHROUGH;
        case  2:
        values[1] = __Pyx_ArgRef_FASTCALL(__pyx_args, 1);
        if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[1])) __PYX_ERR(0, 578, __pyx_L3_error)
        values[0] = __Pyx_ArgRef_FASTCALL(__pyx_args, 0);
        if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[0])) __PYX_ERR(0, 578, __pyx_L3_error)
        break;
        default: goto __pyx_L5_argtuple_error;
      }
      if (!values[2]) values[2] = __Pyx_NewRef(((PyObject *)Py_None));
      if (!values[3]) values[3] = __Pyx_NewRef(((PyObject *)((PyObject*)Py_True)));
    }
    __pyx_v_self = values[0];
    __pyx_v_message = values[1];
    __pyx_v_pos = values[2];
    __pyx_v_fatal = values[3];
  }
  goto __pyx_L6_skip;
  __pyx_L5_argtuple_error:;
  __Pyx_RaiseArgtupleInvalid("error", 0, 2, 4, __pyx_nargs); __PYX_ERR(0, 578, __pyx_L3_error)
  __pyx_L6_skip:;
  goto __pyx_L4_argument_unpacking_done;
  __pyx_L3_error:;
  for (Py_ssize_t __pyx_temp=0; __pyx_temp < (Py_ssize_t)(sizeof(values)/sizeof(values[0])); ++__pyx_temp) {
    Py_XDECREF(values[__pyx_temp]);
  }
  __Pyx_AddTraceback("Cython.Compiler.Scanning.PyrexScanner.error", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __Pyx_RefNannyFinishContext();
  return NULL;
  __pyx_L4_argument_unpacking_done:;
  __pyx_r = __pyx_pf_6Cython_8Compiler_8Scanning_12PyrexScanner_50error(__pyx_self, __pyx_v_self, __pyx_v_message, __pyx_v_pos, __pyx_v_fatal);

  /* function exit code */
  for (Py_ssize_t __pyx_temp=0; __pyx_temp < (Py_ssize_t)(sizeof(values)/sizeof(values[0])); ++__pyx_temp) {
    Py_XDECREF(values[__pyx_temp]);
  }
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}

static PyObject *__pyx_pf_6Cython_8Compiler_8Scanning_12PyrexScanner_50error(CYTHON_UNUSED PyObject *__pyx_self, PyObject *__pyx_v_self, PyObject *__pyx_v_message, PyObject *__pyx_v_pos, PyObject *__pyx_v_fatal) {
  PyObject *__pyx_v_err = NULL;
  PyObject *__pyx_r = NULL;
  __Pyx_INCREF(__pyx_v_pos);
/* … */
  /* function exit code */
  __pyx_r = Py_None; __Pyx_INCREF(Py_None);
  goto __pyx_L0;
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_t_2);
  __Pyx_XDECREF(__pyx_t_3);
  __Pyx_XDECREF(__pyx_t_5);
  __Pyx_AddTraceback("Cython.Compiler.Scanning.PyrexScanner.error", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_r = NULL;
  __pyx_L0:;
  __Pyx_XDECREF(__pyx_v_err);
  __Pyx_XDECREF(__pyx_v_pos);
  __Pyx_XGIVEREF(__pyx_r);
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}
/* … */
  __pyx_t_9 = __Pyx_CyFunction_New(&__pyx_mdef_6Cython_8Compiler_8Scanning_12PyrexScanner_51error, 0, __pyx_mstate_global->__pyx_n_u_PyrexScanner_error, NULL, __pyx_mstate_global->__pyx_n_u_Cython_Compiler_Scanning, __pyx_mstate_global->__pyx_d, ((PyObject *)__pyx_mstate_global->__pyx_codeobj_tab[60])); if (unlikely(!__pyx_t_9)) __PYX_ERR(0, 578, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_9);
  #if CYTHON_COMPILING_IN_CPYTHON && PY_VERSION_HEX >= 0x030E0000
  PyUnstable_Object_EnableDeferredRefcount(__pyx_t_9);
  #endif
  __Pyx_CyFunction_SetDefaultsTuple(__pyx_t_9, __pyx_mstate_global->__pyx_tuple[18]);
  if (__Pyx_SetNameInClass(__pyx_t_8, __pyx_mstate_global->__pyx_n_u_error, __pyx_t_9) < (0)) __PYX_ERR(0, 578, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_9); __pyx_t_9 = 0;
/* … */
  __pyx_mstate_global->__pyx_tuple[18] = PyTuple_Pack(2, Py_None, ((PyObject*)Py_True)); if (unlikely(!__pyx_mstate_global->__pyx_tuple[18])) __PYX_ERR(0, 578, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_mstate_global->__pyx_tuple[18]);
  __Pyx_GIVEREF(__pyx_mstate_global->__pyx_tuple[18]);
```

</details>

L579  ⚪  (score=0)
```python
        if pos is None:
```
<details><summary>Show generated C (score=0)</summary>

```c
  __pyx_t_1 = (__pyx_v_pos == Py_None);
  if (__pyx_t_1) {
/* … */
  }
```

</details>

L580  🟠  (score=5)
```python
            pos = self.position()
```
<details><summary>Show generated C (score=5)</summary>

```c
    __pyx_t_3 = __pyx_v_self;
    __Pyx_INCREF(__pyx_t_3);
    __pyx_t_4 = 0;
    {
      PyObject *__pyx_callargs[2] = {__pyx_t_3, NULL};
      __pyx_t_2 = __Pyx_PyObject_FastCallMethod((PyObject*)__pyx_mstate_global->__pyx_n_u_position, __pyx_callargs+__pyx_t_4, (1-__pyx_t_4) | (1*__Pyx_PY_VECTORCALL_ARGUMENTS_OFFSET));
      __Pyx_XDECREF(__pyx_t_3); __pyx_t_3 = 0;
      if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 580, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_2);
    }
    __Pyx_DECREF_SET(__pyx_v_pos, __pyx_t_2);
    __pyx_t_2 = 0;
```

</details>

L581  🟠  (score=5)
```python
        if self.sy == 'INDENT':
```
<details><summary>Show generated C (score=5)</summary>

```c
  __pyx_t_2 = __Pyx_PyObject_GetAttrStr(__pyx_v_self, __pyx_mstate_global->__pyx_n_u_sy); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 581, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __pyx_t_1 = (__Pyx_PyUnicode_Equals(__pyx_t_2, __pyx_mstate_global->__pyx_n_u_INDENT, Py_EQ)); if (unlikely((__pyx_t_1 < 0))) __PYX_ERR(0, 581, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  if (__pyx_t_1) {
/* … */
  }
```

</details>

L582  🟠  (score=6)
```python
            error(pos, "Possible inconsistent indentation")
```
<details><summary>Show generated C (score=6)</summary>

```c
    __pyx_t_3 = NULL;
    __Pyx_INCREF(__pyx_v_6Cython_8Compiler_8Scanning_error);
    __pyx_t_5 = __pyx_v_6Cython_8Compiler_8Scanning_error; 
    __pyx_t_4 = 1;
    {
      PyObject *__pyx_callargs[3] = {__pyx_t_3, __pyx_v_pos, __pyx_mstate_global->__pyx_kp_u_Possible_inconsistent_indentatio};
      __pyx_t_2 = __Pyx_PyObject_FastCall((PyObject*)__pyx_t_5, __pyx_callargs+__pyx_t_4, (3-__pyx_t_4) | (__pyx_t_4*__Pyx_PY_VECTORCALL_ARGUMENTS_OFFSET));
      __Pyx_XDECREF(__pyx_t_3); __pyx_t_3 = 0;
      __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
      if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 582, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_2);
    }
    __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
```

</details>

L583  🟠  (score=5)
```python
        err = error(pos, message)
```
<details><summary>Show generated C (score=5)</summary>

```c
  __pyx_t_5 = NULL;
  __Pyx_INCREF(__pyx_v_6Cython_8Compiler_8Scanning_error);
  __pyx_t_3 = __pyx_v_6Cython_8Compiler_8Scanning_error; 
  __pyx_t_4 = 1;
  {
    PyObject *__pyx_callargs[3] = {__pyx_t_5, __pyx_v_pos, __pyx_v_message};
    __pyx_t_2 = __Pyx_PyObject_FastCall((PyObject*)__pyx_t_3, __pyx_callargs+__pyx_t_4, (3-__pyx_t_4) | (__pyx_t_4*__Pyx_PY_VECTORCALL_ARGUMENTS_OFFSET));
    __Pyx_XDECREF(__pyx_t_5); __pyx_t_5 = 0;
    __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
    if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 583, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_2);
  }
  __pyx_v_err = __pyx_t_2;
  __pyx_t_2 = 0;
```

</details>

L584  🟡  (score=4)
```python
        if fatal: raise err
```
<details><summary>Show generated C (score=4)</summary>

```c
  __pyx_t_1 = __Pyx_PyObject_IsTrue(__pyx_v_fatal); if (unlikely((__pyx_t_1 < 0))) __PYX_ERR(0, 584, __pyx_L1_error)
  if (unlikely(__pyx_t_1)) {
    __Pyx_Raise(__pyx_v_err, 0, 0, 0);
    __PYX_ERR(0, 584, __pyx_L1_error)
  }
```

</details>

L585  ⚪  (score=0)
```python
```
L586  🔴  (score=43)
```python
    def error_at_scanpos(self, message):
```
<details><summary>Show generated C (score=43)</summary>

```c
/* Python wrapper */
static PyObject *__pyx_pw_6Cython_8Compiler_8Scanning_12PyrexScanner_53error_at_scanpos(PyObject *__pyx_self, 
#if CYTHON_METH_FASTCALL
PyObject *const *__pyx_args, Py_ssize_t __pyx_nargs, PyObject *__pyx_kwds
#else
PyObject *__pyx_args, PyObject *__pyx_kwds
#endif
); /*proto*/
PyDoc_STRVAR(__pyx_doc_6Cython_8Compiler_8Scanning_12PyrexScanner_52error_at_scanpos, "File: Cython/Compiler/Scanning.py (starting at line 586)");
static PyMethodDef __pyx_mdef_6Cython_8Compiler_8Scanning_12PyrexScanner_53error_at_scanpos = {"error_at_scanpos", (PyCFunction)(void(*)(void))(__Pyx_PyCFunction_FastCallWithKeywords)__pyx_pw_6Cython_8Compiler_8Scanning_12PyrexScanner_53error_at_scanpos, __Pyx_METH_FASTCALL|METH_KEYWORDS, __pyx_doc_6Cython_8Compiler_8Scanning_12PyrexScanner_52error_at_scanpos};
static PyObject *__pyx_pw_6Cython_8Compiler_8Scanning_12PyrexScanner_53error_at_scanpos(PyObject *__pyx_self, 
#if CYTHON_METH_FASTCALL
PyObject *const *__pyx_args, Py_ssize_t __pyx_nargs, PyObject *__pyx_kwds
#else
PyObject *__pyx_args, PyObject *__pyx_kwds
#endif
) {
  PyObject *__pyx_v_self = 0;
  PyObject *__pyx_v_message = 0;
  #if !CYTHON_METH_FASTCALL
  CYTHON_UNUSED Py_ssize_t __pyx_nargs;
  #endif
  CYTHON_UNUSED PyObject *const *__pyx_kwvalues;
  PyObject *__pyx_r = 0;
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("error_at_scanpos (wrapper)", 0);
  #if !CYTHON_METH_FASTCALL
  #if CYTHON_ASSUME_SAFE_SIZE
  __pyx_nargs = PyTuple_GET_SIZE(__pyx_args);
  #else
  __pyx_nargs = PyTuple_Size(__pyx_args); if (unlikely(__pyx_nargs < 0)) return NULL;
  #endif
  #endif
  __pyx_kwvalues = __Pyx_KwValues_FASTCALL(__pyx_args, __pyx_nargs);
  {
    PyObject ** const __pyx_pyargnames[] = {&__pyx_mstate_global->__pyx_n_u_self,&__pyx_mstate_global->__pyx_n_u_message,0};
  PyObject* values[2] = {0,0};
    const Py_ssize_t __pyx_kwds_len = (__pyx_kwds) ? __Pyx_NumKwargs_FASTCALL(__pyx_kwds) : 0;
    if (unlikely(__pyx_kwds_len) < 0) __PYX_ERR(0, 586, __pyx_L3_error)
    if (__pyx_kwds_len > 0) {
      switch (__pyx_nargs) {
        case  2:
        values[1] = __Pyx_ArgRef_FASTCALL(__pyx_args, 1);
        if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[1])) __PYX_ERR(0, 586, __pyx_L3_error)
        CYTHON_FALLTHROUGH;
        case  1:
        values[0] = __Pyx_ArgRef_FASTCALL(__pyx_args, 0);
        if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[0])) __PYX_ERR(0, 586, __pyx_L3_error)
        CYTHON_FALLTHROUGH;
        case  0: break;
        default: goto __pyx_L5_argtuple_error;
      }
      const Py_ssize_t kwd_pos_args = __pyx_nargs;
      if (__Pyx_ParseKeywords(__pyx_kwds, __pyx_kwvalues, __pyx_pyargnames, 0, values, kwd_pos_args, __pyx_kwds_len, "error_at_scanpos", 0) < (0)) __PYX_ERR(0, 586, __pyx_L3_error)
      for (Py_ssize_t i = __pyx_nargs; i < 2; i++) {
        if (unlikely(!values[i])) { __Pyx_RaiseArgtupleInvalid("error_at_scanpos", 1, 2, 2, i); __PYX_ERR(0, 586, __pyx_L3_error) }
      }
    } else if (unlikely(__pyx_nargs != 2)) {
      goto __pyx_L5_argtuple_error;
    } else {
      values[0] = __Pyx_ArgRef_FASTCALL(__pyx_args, 0);
      if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[0])) __PYX_ERR(0, 586, __pyx_L3_error)
      values[1] = __Pyx_ArgRef_FASTCALL(__pyx_args, 1);
      if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[1])) __PYX_ERR(0, 586, __pyx_L3_error)
    }
    __pyx_v_self = values[0];
    __pyx_v_message = values[1];
  }
  goto __pyx_L6_skip;
  __pyx_L5_argtuple_error:;
  __Pyx_RaiseArgtupleInvalid("error_at_scanpos", 1, 2, 2, __pyx_nargs); __PYX_ERR(0, 586, __pyx_L3_error)
  __pyx_L6_skip:;
  goto __pyx_L4_argument_unpacking_done;
  __pyx_L3_error:;
  for (Py_ssize_t __pyx_temp=0; __pyx_temp < (Py_ssize_t)(sizeof(values)/sizeof(values[0])); ++__pyx_temp) {
    Py_XDECREF(values[__pyx_temp]);
  }
  __Pyx_AddTraceback("Cython.Compiler.Scanning.PyrexScanner.error_at_scanpos", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __Pyx_RefNannyFinishContext();
  return NULL;
  __pyx_L4_argument_unpacking_done:;
  __pyx_r = __pyx_pf_6Cython_8Compiler_8Scanning_12PyrexScanner_52error_at_scanpos(__pyx_self, __pyx_v_self, __pyx_v_message);
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

static PyObject *__pyx_pf_6Cython_8Compiler_8Scanning_12PyrexScanner_52error_at_scanpos(CYTHON_UNUSED PyObject *__pyx_self, PyObject *__pyx_v_self, PyObject *__pyx_v_message) {
  PyObject *__pyx_v_pos = NULL;
  PyObject *__pyx_r = NULL;
/* … */
  /* function exit code */
  __pyx_r = Py_None; __Pyx_INCREF(Py_None);
  goto __pyx_L0;
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_t_1);
  __Pyx_XDECREF(__pyx_t_2);
  __Pyx_AddTraceback("Cython.Compiler.Scanning.PyrexScanner.error_at_scanpos", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_r = NULL;
  __pyx_L0:;
  __Pyx_XDECREF(__pyx_v_pos);
  __Pyx_XGIVEREF(__pyx_r);
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}
/* … */
  __pyx_t_9 = __Pyx_CyFunction_New(&__pyx_mdef_6Cython_8Compiler_8Scanning_12PyrexScanner_53error_at_scanpos, 0, __pyx_mstate_global->__pyx_n_u_PyrexScanner_error_at_scanpos, NULL, __pyx_mstate_global->__pyx_n_u_Cython_Compiler_Scanning, __pyx_mstate_global->__pyx_d, ((PyObject *)__pyx_mstate_global->__pyx_codeobj_tab[61])); if (unlikely(!__pyx_t_9)) __PYX_ERR(0, 586, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_9);
  #if CYTHON_COMPILING_IN_CPYTHON && PY_VERSION_HEX >= 0x030E0000
  PyUnstable_Object_EnableDeferredRefcount(__pyx_t_9);
  #endif
  if (__Pyx_SetNameInClass(__pyx_t_8, __pyx_mstate_global->__pyx_n_u_error_at_scanpos, __pyx_t_9) < (0)) __PYX_ERR(0, 586, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_9); __pyx_t_9 = 0;
```

</details>

L587  ⚪  (score=0)
```python
        # Like error(fatal=True), but gets the current scanning position rather than
```
L588  ⚪  (score=0)
```python
        # the position of the last token read.
```
L589  🟡  (score=4)
```python
        pos = self.get_current_scan_pos()
```
<details><summary>Show generated C (score=4)</summary>

```c
  __pyx_t_2 = __pyx_v_self;
  __Pyx_INCREF(__pyx_t_2);
  __pyx_t_3 = 0;
  {
    PyObject *__pyx_callargs[2] = {__pyx_t_2, NULL};
    __pyx_t_1 = __Pyx_PyObject_FastCallMethod((PyObject*)__pyx_mstate_global->__pyx_n_u_get_current_scan_pos, __pyx_callargs+__pyx_t_3, (1-__pyx_t_3) | (1*__Pyx_PY_VECTORCALL_ARGUMENTS_OFFSET));
    __Pyx_XDECREF(__pyx_t_2); __pyx_t_2 = 0;
    if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 589, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_1);
  }
  __pyx_v_pos = __pyx_t_1;
  __pyx_t_1 = 0;
```

</details>

L590  🟠  (score=5)
```python
        self.error(message, pos, True)
```
<details><summary>Show generated C (score=5)</summary>

```c
  __pyx_t_2 = __pyx_v_self;
  __Pyx_INCREF(__pyx_t_2);
  __pyx_t_3 = 0;
  {
    PyObject *__pyx_callargs[4] = {__pyx_t_2, __pyx_v_message, __pyx_v_pos, Py_True};
    __pyx_t_1 = __Pyx_PyObject_FastCallMethod((PyObject*)__pyx_mstate_global->__pyx_n_u_error, __pyx_callargs+__pyx_t_3, (4-__pyx_t_3) | (1*__Pyx_PY_VECTORCALL_ARGUMENTS_OFFSET));
    __Pyx_XDECREF(__pyx_t_2); __pyx_t_2 = 0;
    if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 590, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_1);
  }
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
```

</details>

L591  ⚪  (score=0)
```python
```
L592  🔴  (score=52)
```python
    def expect(self, what, message=None):
```
<details><summary>Show generated C (score=52)</summary>

```c
/* Python wrapper */
static PyObject *__pyx_pw_6Cython_8Compiler_8Scanning_12PyrexScanner_55expect(PyObject *__pyx_self, 
#if CYTHON_METH_FASTCALL
PyObject *const *__pyx_args, Py_ssize_t __pyx_nargs, PyObject *__pyx_kwds
#else
PyObject *__pyx_args, PyObject *__pyx_kwds
#endif
); /*proto*/
PyDoc_STRVAR(__pyx_doc_6Cython_8Compiler_8Scanning_12PyrexScanner_54expect, "File: Cython/Compiler/Scanning.py (starting at line 592)");
static PyMethodDef __pyx_mdef_6Cython_8Compiler_8Scanning_12PyrexScanner_55expect = {"expect", (PyCFunction)(void(*)(void))(__Pyx_PyCFunction_FastCallWithKeywords)__pyx_pw_6Cython_8Compiler_8Scanning_12PyrexScanner_55expect, __Pyx_METH_FASTCALL|METH_KEYWORDS, __pyx_doc_6Cython_8Compiler_8Scanning_12PyrexScanner_54expect};
static PyObject *__pyx_pw_6Cython_8Compiler_8Scanning_12PyrexScanner_55expect(PyObject *__pyx_self, 
#if CYTHON_METH_FASTCALL
PyObject *const *__pyx_args, Py_ssize_t __pyx_nargs, PyObject *__pyx_kwds
#else
PyObject *__pyx_args, PyObject *__pyx_kwds
#endif
) {
  PyObject *__pyx_v_self = 0;
  PyObject *__pyx_v_what = 0;
  PyObject *__pyx_v_message = 0;
  #if !CYTHON_METH_FASTCALL
  CYTHON_UNUSED Py_ssize_t __pyx_nargs;
  #endif
  CYTHON_UNUSED PyObject *const *__pyx_kwvalues;
  PyObject *__pyx_r = 0;
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("expect (wrapper)", 0);
  #if !CYTHON_METH_FASTCALL
  #if CYTHON_ASSUME_SAFE_SIZE
  __pyx_nargs = PyTuple_GET_SIZE(__pyx_args);
  #else
  __pyx_nargs = PyTuple_Size(__pyx_args); if (unlikely(__pyx_nargs < 0)) return NULL;
  #endif
  #endif
  __pyx_kwvalues = __Pyx_KwValues_FASTCALL(__pyx_args, __pyx_nargs);
  {
    PyObject ** const __pyx_pyargnames[] = {&__pyx_mstate_global->__pyx_n_u_self,&__pyx_mstate_global->__pyx_n_u_what,&__pyx_mstate_global->__pyx_n_u_message,0};
  PyObject* values[3] = {0,0,0};
    const Py_ssize_t __pyx_kwds_len = (__pyx_kwds) ? __Pyx_NumKwargs_FASTCALL(__pyx_kwds) : 0;
    if (unlikely(__pyx_kwds_len) < 0) __PYX_ERR(0, 592, __pyx_L3_error)
    if (__pyx_kwds_len > 0) {
      switch (__pyx_nargs) {
        case  3:
        values[2] = __Pyx_ArgRef_FASTCALL(__pyx_args, 2);
        if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[2])) __PYX_ERR(0, 592, __pyx_L3_error)
        CYTHON_FALLTHROUGH;
        case  2:
        values[1] = __Pyx_ArgRef_FASTCALL(__pyx_args, 1);
        if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[1])) __PYX_ERR(0, 592, __pyx_L3_error)
        CYTHON_FALLTHROUGH;
        case  1:
        values[0] = __Pyx_ArgRef_FASTCALL(__pyx_args, 0);
        if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[0])) __PYX_ERR(0, 592, __pyx_L3_error)
        CYTHON_FALLTHROUGH;
        case  0: break;
        default: goto __pyx_L5_argtuple_error;
      }
      const Py_ssize_t kwd_pos_args = __pyx_nargs;
      if (__Pyx_ParseKeywords(__pyx_kwds, __pyx_kwvalues, __pyx_pyargnames, 0, values, kwd_pos_args, __pyx_kwds_len, "expect", 0) < (0)) __PYX_ERR(0, 592, __pyx_L3_error)
      if (!values[2]) values[2] = __Pyx_NewRef(((PyObject *)Py_None));
      for (Py_ssize_t i = __pyx_nargs; i < 2; i++) {
        if (unlikely(!values[i])) { __Pyx_RaiseArgtupleInvalid("expect", 0, 2, 3, i); __PYX_ERR(0, 592, __pyx_L3_error) }
      }
    } else {
      switch (__pyx_nargs) {
        case  3:
        values[2] = __Pyx_ArgRef_FASTCALL(__pyx_args, 2);
        if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[2])) __PYX_ERR(0, 592, __pyx_L3_error)
        CYTHON_FALLTHROUGH;
        case  2:
        values[1] = __Pyx_ArgRef_FASTCALL(__pyx_args, 1);
        if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[1])) __PYX_ERR(0, 592, __pyx_L3_error)
        values[0] = __Pyx_ArgRef_FASTCALL(__pyx_args, 0);
        if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[0])) __PYX_ERR(0, 592, __pyx_L3_error)
        break;
        default: goto __pyx_L5_argtuple_error;
      }
      if (!values[2]) values[2] = __Pyx_NewRef(((PyObject *)Py_None));
    }
    __pyx_v_self = values[0];
    __pyx_v_what = values[1];
    __pyx_v_message = values[2];
  }
  goto __pyx_L6_skip;
  __pyx_L5_argtuple_error:;
  __Pyx_RaiseArgtupleInvalid("expect", 0, 2, 3, __pyx_nargs); __PYX_ERR(0, 592, __pyx_L3_error)
  __pyx_L6_skip:;
  goto __pyx_L4_argument_unpacking_done;
  __pyx_L3_error:;
  for (Py_ssize_t __pyx_temp=0; __pyx_temp < (Py_ssize_t)(sizeof(values)/sizeof(values[0])); ++__pyx_temp) {
    Py_XDECREF(values[__pyx_temp]);
  }
  __Pyx_AddTraceback("Cython.Compiler.Scanning.PyrexScanner.expect", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __Pyx_RefNannyFinishContext();
  return NULL;
  __pyx_L4_argument_unpacking_done:;
  __pyx_r = __pyx_pf_6Cython_8Compiler_8Scanning_12PyrexScanner_54expect(__pyx_self, __pyx_v_self, __pyx_v_what, __pyx_v_message);

  /* function exit code */
  for (Py_ssize_t __pyx_temp=0; __pyx_temp < (Py_ssize_t)(sizeof(values)/sizeof(values[0])); ++__pyx_temp) {
    Py_XDECREF(values[__pyx_temp]);
  }
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}

static PyObject *__pyx_pf_6Cython_8Compiler_8Scanning_12PyrexScanner_54expect(CYTHON_UNUSED PyObject *__pyx_self, PyObject *__pyx_v_self, PyObject *__pyx_v_what, PyObject *__pyx_v_message) {
  PyObject *__pyx_r = NULL;
/* … */
  /* function exit code */
  __pyx_r = Py_None; __Pyx_INCREF(Py_None);
  goto __pyx_L0;
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_t_1);
  __Pyx_XDECREF(__pyx_t_2);
  __Pyx_AddTraceback("Cython.Compiler.Scanning.PyrexScanner.expect", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_r = NULL;
  __pyx_L0:;
  __Pyx_XGIVEREF(__pyx_r);
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}
/* … */
  __pyx_t_9 = __Pyx_CyFunction_New(&__pyx_mdef_6Cython_8Compiler_8Scanning_12PyrexScanner_55expect, 0, __pyx_mstate_global->__pyx_n_u_PyrexScanner_expect, NULL, __pyx_mstate_global->__pyx_n_u_Cython_Compiler_Scanning, __pyx_mstate_global->__pyx_d, ((PyObject *)__pyx_mstate_global->__pyx_codeobj_tab[62])); if (unlikely(!__pyx_t_9)) __PYX_ERR(0, 592, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_9);
  #if CYTHON_COMPILING_IN_CPYTHON && PY_VERSION_HEX >= 0x030E0000
  PyUnstable_Object_EnableDeferredRefcount(__pyx_t_9);
  #endif
  __Pyx_CyFunction_SetDefaultsTuple(__pyx_t_9, __pyx_mstate_global->__pyx_tuple[16]);
  if (__Pyx_SetNameInClass(__pyx_t_8, __pyx_mstate_global->__pyx_n_u_expect, __pyx_t_9) < (0)) __PYX_ERR(0, 592, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_9); __pyx_t_9 = 0;
```

</details>

L593  🔴  (score=11)
```python
        if self.sy == what:
```
<details><summary>Show generated C (score=11)</summary>

```c
  __pyx_t_1 = __Pyx_PyObject_GetAttrStr(__pyx_v_self, __pyx_mstate_global->__pyx_n_u_sy); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 593, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __pyx_t_2 = PyObject_RichCompare(__pyx_t_1, __pyx_v_what, Py_EQ); __Pyx_XGOTREF(__pyx_t_2); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 593, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __pyx_t_3 = __Pyx_PyObject_IsTrue(__pyx_t_2); if (unlikely((__pyx_t_3 < 0))) __PYX_ERR(0, 593, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  if (__pyx_t_3) {
/* … */
    goto __pyx_L3;
  }
```

</details>

L594  🟠  (score=5)
```python
            self.next()
```
<details><summary>Show generated C (score=5)</summary>

```c
    __pyx_t_1 = __pyx_v_self;
    __Pyx_INCREF(__pyx_t_1);
    __pyx_t_4 = 0;
    {
      PyObject *__pyx_callargs[2] = {__pyx_t_1, NULL};
      __pyx_t_2 = __Pyx_PyObject_FastCallMethod((PyObject*)__pyx_mstate_global->__pyx_n_u_next, __pyx_callargs+__pyx_t_4, (1-__pyx_t_4) | (1*__Pyx_PY_VECTORCALL_ARGUMENTS_OFFSET));
      __Pyx_XDECREF(__pyx_t_1); __pyx_t_1 = 0;
      if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 594, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_2);
    }
    __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
```

</details>

L595  ⚪  (score=0)
```python
        else:
```
L596  🟠  (score=5)
```python
            self.expected(what, message)
```
<details><summary>Show generated C (score=5)</summary>

```c
  /*else*/ {
    __pyx_t_1 = __pyx_v_self;
    __Pyx_INCREF(__pyx_t_1);
    __pyx_t_4 = 0;
    {
      PyObject *__pyx_callargs[3] = {__pyx_t_1, __pyx_v_what, __pyx_v_message};
      __pyx_t_2 = __Pyx_PyObject_FastCallMethod((PyObject*)__pyx_mstate_global->__pyx_n_u_expected, __pyx_callargs+__pyx_t_4, (3-__pyx_t_4) | (1*__Pyx_PY_VECTORCALL_ARGUMENTS_OFFSET));
      __Pyx_XDECREF(__pyx_t_1); __pyx_t_1 = 0;
      if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 596, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_2);
    }
    __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  }
  __pyx_L3:;
```

</details>

L597  ⚪  (score=0)
```python
```
L598  🔴  (score=53)
```python
    def expect_keyword(self, what, message=None):
```
<details><summary>Show generated C (score=53)</summary>

```c
/* Python wrapper */
static PyObject *__pyx_pw_6Cython_8Compiler_8Scanning_12PyrexScanner_57expect_keyword(PyObject *__pyx_self, 
#if CYTHON_METH_FASTCALL
PyObject *const *__pyx_args, Py_ssize_t __pyx_nargs, PyObject *__pyx_kwds
#else
PyObject *__pyx_args, PyObject *__pyx_kwds
#endif
); /*proto*/
PyDoc_STRVAR(__pyx_doc_6Cython_8Compiler_8Scanning_12PyrexScanner_56expect_keyword, "File: Cython/Compiler/Scanning.py (starting at line 598)");
static PyMethodDef __pyx_mdef_6Cython_8Compiler_8Scanning_12PyrexScanner_57expect_keyword = {"expect_keyword", (PyCFunction)(void(*)(void))(__Pyx_PyCFunction_FastCallWithKeywords)__pyx_pw_6Cython_8Compiler_8Scanning_12PyrexScanner_57expect_keyword, __Pyx_METH_FASTCALL|METH_KEYWORDS, __pyx_doc_6Cython_8Compiler_8Scanning_12PyrexScanner_56expect_keyword};
static PyObject *__pyx_pw_6Cython_8Compiler_8Scanning_12PyrexScanner_57expect_keyword(PyObject *__pyx_self, 
#if CYTHON_METH_FASTCALL
PyObject *const *__pyx_args, Py_ssize_t __pyx_nargs, PyObject *__pyx_kwds
#else
PyObject *__pyx_args, PyObject *__pyx_kwds
#endif
) {
  PyObject *__pyx_v_self = 0;
  PyObject *__pyx_v_what = 0;
  PyObject *__pyx_v_message = 0;
  #if !CYTHON_METH_FASTCALL
  CYTHON_UNUSED Py_ssize_t __pyx_nargs;
  #endif
  CYTHON_UNUSED PyObject *const *__pyx_kwvalues;
  PyObject *__pyx_r = 0;
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("expect_keyword (wrapper)", 0);
  #if !CYTHON_METH_FASTCALL
  #if CYTHON_ASSUME_SAFE_SIZE
  __pyx_nargs = PyTuple_GET_SIZE(__pyx_args);
  #else
  __pyx_nargs = PyTuple_Size(__pyx_args); if (unlikely(__pyx_nargs < 0)) return NULL;
  #endif
  #endif
  __pyx_kwvalues = __Pyx_KwValues_FASTCALL(__pyx_args, __pyx_nargs);
  {
    PyObject ** const __pyx_pyargnames[] = {&__pyx_mstate_global->__pyx_n_u_self,&__pyx_mstate_global->__pyx_n_u_what,&__pyx_mstate_global->__pyx_n_u_message,0};
  PyObject* values[3] = {0,0,0};
    const Py_ssize_t __pyx_kwds_len = (__pyx_kwds) ? __Pyx_NumKwargs_FASTCALL(__pyx_kwds) : 0;
    if (unlikely(__pyx_kwds_len) < 0) __PYX_ERR(0, 598, __pyx_L3_error)
    if (__pyx_kwds_len > 0) {
      switch (__pyx_nargs) {
        case  3:
        values[2] = __Pyx_ArgRef_FASTCALL(__pyx_args, 2);
        if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[2])) __PYX_ERR(0, 598, __pyx_L3_error)
        CYTHON_FALLTHROUGH;
        case  2:
        values[1] = __Pyx_ArgRef_FASTCALL(__pyx_args, 1);
        if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[1])) __PYX_ERR(0, 598, __pyx_L3_error)
        CYTHON_FALLTHROUGH;
        case  1:
        values[0] = __Pyx_ArgRef_FASTCALL(__pyx_args, 0);
        if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[0])) __PYX_ERR(0, 598, __pyx_L3_error)
        CYTHON_FALLTHROUGH;
        case  0: break;
        default: goto __pyx_L5_argtuple_error;
      }
      const Py_ssize_t kwd_pos_args = __pyx_nargs;
      if (__Pyx_ParseKeywords(__pyx_kwds, __pyx_kwvalues, __pyx_pyargnames, 0, values, kwd_pos_args, __pyx_kwds_len, "expect_keyword", 0) < (0)) __PYX_ERR(0, 598, __pyx_L3_error)
      if (!values[2]) values[2] = __Pyx_NewRef(((PyObject *)Py_None));
      for (Py_ssize_t i = __pyx_nargs; i < 2; i++) {
        if (unlikely(!values[i])) { __Pyx_RaiseArgtupleInvalid("expect_keyword", 0, 2, 3, i); __PYX_ERR(0, 598, __pyx_L3_error) }
      }
    } else {
      switch (__pyx_nargs) {
        case  3:
        values[2] = __Pyx_ArgRef_FASTCALL(__pyx_args, 2);
        if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[2])) __PYX_ERR(0, 598, __pyx_L3_error)
        CYTHON_FALLTHROUGH;
        case  2:
        values[1] = __Pyx_ArgRef_FASTCALL(__pyx_args, 1);
        if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[1])) __PYX_ERR(0, 598, __pyx_L3_error)
        values[0] = __Pyx_ArgRef_FASTCALL(__pyx_args, 0);
        if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[0])) __PYX_ERR(0, 598, __pyx_L3_error)
        break;
        default: goto __pyx_L5_argtuple_error;
      }
      if (!values[2]) values[2] = __Pyx_NewRef(((PyObject *)Py_None));
    }
    __pyx_v_self = values[0];
    __pyx_v_what = values[1];
    __pyx_v_message = values[2];
  }
  goto __pyx_L6_skip;
  __pyx_L5_argtuple_error:;
  __Pyx_RaiseArgtupleInvalid("expect_keyword", 0, 2, 3, __pyx_nargs); __PYX_ERR(0, 598, __pyx_L3_error)
  __pyx_L6_skip:;
  goto __pyx_L4_argument_unpacking_done;
  __pyx_L3_error:;
  for (Py_ssize_t __pyx_temp=0; __pyx_temp < (Py_ssize_t)(sizeof(values)/sizeof(values[0])); ++__pyx_temp) {
    Py_XDECREF(values[__pyx_temp]);
  }
  __Pyx_AddTraceback("Cython.Compiler.Scanning.PyrexScanner.expect_keyword", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __Pyx_RefNannyFinishContext();
  return NULL;
  __pyx_L4_argument_unpacking_done:;
  __pyx_r = __pyx_pf_6Cython_8Compiler_8Scanning_12PyrexScanner_56expect_keyword(__pyx_self, __pyx_v_self, __pyx_v_what, __pyx_v_message);

  /* function exit code */
  for (Py_ssize_t __pyx_temp=0; __pyx_temp < (Py_ssize_t)(sizeof(values)/sizeof(values[0])); ++__pyx_temp) {
    Py_XDECREF(values[__pyx_temp]);
  }
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}

static PyObject *__pyx_pf_6Cython_8Compiler_8Scanning_12PyrexScanner_56expect_keyword(CYTHON_UNUSED PyObject *__pyx_self, PyObject *__pyx_v_self, PyObject *__pyx_v_what, PyObject *__pyx_v_message) {
  PyObject *__pyx_r = NULL;
/* … */
  /* function exit code */
  __pyx_r = Py_None; __Pyx_INCREF(Py_None);
  goto __pyx_L0;
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_t_2);
  __Pyx_XDECREF(__pyx_t_3);
  __Pyx_XDECREF(__pyx_t_4);
  __Pyx_AddTraceback("Cython.Compiler.Scanning.PyrexScanner.expect_keyword", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_r = NULL;
  __pyx_L0:;
  __Pyx_XGIVEREF(__pyx_r);
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}
/* … */
  __pyx_t_9 = __Pyx_CyFunction_New(&__pyx_mdef_6Cython_8Compiler_8Scanning_12PyrexScanner_57expect_keyword, 0, __pyx_mstate_global->__pyx_n_u_PyrexScanner_expect_keyword, NULL, __pyx_mstate_global->__pyx_n_u_Cython_Compiler_Scanning, __pyx_mstate_global->__pyx_d, ((PyObject *)__pyx_mstate_global->__pyx_codeobj_tab[63])); if (unlikely(!__pyx_t_9)) __PYX_ERR(0, 598, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_9);
  #if CYTHON_COMPILING_IN_CPYTHON && PY_VERSION_HEX >= 0x030E0000
  PyUnstable_Object_EnableDeferredRefcount(__pyx_t_9);
  #endif
  __Pyx_CyFunction_SetDefaultsTuple(__pyx_t_9, __pyx_mstate_global->__pyx_tuple[16]);
  if (__Pyx_SetNameInClass(__pyx_t_8, __pyx_mstate_global->__pyx_n_u_expect_keyword, __pyx_t_9) < (0)) __PYX_ERR(0, 598, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_9); __pyx_t_9 = 0;
```

</details>

L599  🔴  (score=25)
```python
        if self.sy == IDENT and self.systring == what:
```
<details><summary>Show generated C (score=25)</summary>

```c
  __pyx_t_2 = __Pyx_PyObject_GetAttrStr(__pyx_v_self, __pyx_mstate_global->__pyx_n_u_sy); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 599, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_GetModuleGlobalName(__pyx_t_3, __pyx_mstate_global->__pyx_n_u_IDENT); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 599, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_3);
  __pyx_t_4 = PyObject_RichCompare(__pyx_t_2, __pyx_t_3, Py_EQ); __Pyx_XGOTREF(__pyx_t_4); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 599, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
  __pyx_t_5 = __Pyx_PyObject_IsTrue(__pyx_t_4); if (unlikely((__pyx_t_5 < 0))) __PYX_ERR(0, 599, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
  if (__pyx_t_5) {
  } else {
    __pyx_t_1 = __pyx_t_5;
    goto __pyx_L4_bool_binop_done;
  }
  __pyx_t_4 = __Pyx_PyObject_GetAttrStr(__pyx_v_self, __pyx_mstate_global->__pyx_n_u_systring); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 599, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_4);
  __pyx_t_3 = PyObject_RichCompare(__pyx_t_4, __pyx_v_what, Py_EQ); __Pyx_XGOTREF(__pyx_t_3); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 599, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
  __pyx_t_5 = __Pyx_PyObject_IsTrue(__pyx_t_3); if (unlikely((__pyx_t_5 < 0))) __PYX_ERR(0, 599, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
  __pyx_t_1 = __pyx_t_5;
  __pyx_L4_bool_binop_done:;
  if (__pyx_t_1) {
/* … */
    goto __pyx_L3;
  }
```

</details>

L600  🟠  (score=5)
```python
            self.next()
```
<details><summary>Show generated C (score=5)</summary>

```c
    __pyx_t_4 = __pyx_v_self;
    __Pyx_INCREF(__pyx_t_4);
    __pyx_t_6 = 0;
    {
      PyObject *__pyx_callargs[2] = {__pyx_t_4, NULL};
      __pyx_t_3 = __Pyx_PyObject_FastCallMethod((PyObject*)__pyx_mstate_global->__pyx_n_u_next, __pyx_callargs+__pyx_t_6, (1-__pyx_t_6) | (1*__Pyx_PY_VECTORCALL_ARGUMENTS_OFFSET));
      __Pyx_XDECREF(__pyx_t_4); __pyx_t_4 = 0;
      if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 600, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_3);
    }
    __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
```

</details>

L601  ⚪  (score=0)
```python
        else:
```
L602  🟠  (score=5)
```python
            self.expected(what, message)
```
<details><summary>Show generated C (score=5)</summary>

```c
  /*else*/ {
    __pyx_t_4 = __pyx_v_self;
    __Pyx_INCREF(__pyx_t_4);
    __pyx_t_6 = 0;
    {
      PyObject *__pyx_callargs[3] = {__pyx_t_4, __pyx_v_what, __pyx_v_message};
      __pyx_t_3 = __Pyx_PyObject_FastCallMethod((PyObject*)__pyx_mstate_global->__pyx_n_u_expected, __pyx_callargs+__pyx_t_6, (3-__pyx_t_6) | (1*__Pyx_PY_VECTORCALL_ARGUMENTS_OFFSET));
      __Pyx_XDECREF(__pyx_t_4); __pyx_t_4 = 0;
      if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 602, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_3);
    }
    __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
  }
  __pyx_L3:;
```

</details>

L603  ⚪  (score=0)
```python
```
L604  🔴  (score=56)
```python
    def expected(self, what, message=None):
```
<details><summary>Show generated C (score=56)</summary>

```c
/* Python wrapper */
static PyObject *__pyx_pw_6Cython_8Compiler_8Scanning_12PyrexScanner_59expected(PyObject *__pyx_self, 
#if CYTHON_METH_FASTCALL
PyObject *const *__pyx_args, Py_ssize_t __pyx_nargs, PyObject *__pyx_kwds
#else
PyObject *__pyx_args, PyObject *__pyx_kwds
#endif
); /*proto*/
PyDoc_STRVAR(__pyx_doc_6Cython_8Compiler_8Scanning_12PyrexScanner_58expected, "File: Cython/Compiler/Scanning.py (starting at line 604)");
static PyMethodDef __pyx_mdef_6Cython_8Compiler_8Scanning_12PyrexScanner_59expected = {"expected", (PyCFunction)(void(*)(void))(__Pyx_PyCFunction_FastCallWithKeywords)__pyx_pw_6Cython_8Compiler_8Scanning_12PyrexScanner_59expected, __Pyx_METH_FASTCALL|METH_KEYWORDS, __pyx_doc_6Cython_8Compiler_8Scanning_12PyrexScanner_58expected};
static PyObject *__pyx_pw_6Cython_8Compiler_8Scanning_12PyrexScanner_59expected(PyObject *__pyx_self, 
#if CYTHON_METH_FASTCALL
PyObject *const *__pyx_args, Py_ssize_t __pyx_nargs, PyObject *__pyx_kwds
#else
PyObject *__pyx_args, PyObject *__pyx_kwds
#endif
) {
  PyObject *__pyx_v_self = 0;
  PyObject *__pyx_v_what = 0;
  PyObject *__pyx_v_message = 0;
  #if !CYTHON_METH_FASTCALL
  CYTHON_UNUSED Py_ssize_t __pyx_nargs;
  #endif
  CYTHON_UNUSED PyObject *const *__pyx_kwvalues;
  PyObject *__pyx_r = 0;
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("expected (wrapper)", 0);
  #if !CYTHON_METH_FASTCALL
  #if CYTHON_ASSUME_SAFE_SIZE
  __pyx_nargs = PyTuple_GET_SIZE(__pyx_args);
  #else
  __pyx_nargs = PyTuple_Size(__pyx_args); if (unlikely(__pyx_nargs < 0)) return NULL;
  #endif
  #endif
  __pyx_kwvalues = __Pyx_KwValues_FASTCALL(__pyx_args, __pyx_nargs);
  {
    PyObject ** const __pyx_pyargnames[] = {&__pyx_mstate_global->__pyx_n_u_self,&__pyx_mstate_global->__pyx_n_u_what,&__pyx_mstate_global->__pyx_n_u_message,0};
  PyObject* values[3] = {0,0,0};
    const Py_ssize_t __pyx_kwds_len = (__pyx_kwds) ? __Pyx_NumKwargs_FASTCALL(__pyx_kwds) : 0;
    if (unlikely(__pyx_kwds_len) < 0) __PYX_ERR(0, 604, __pyx_L3_error)
    if (__pyx_kwds_len > 0) {
      switch (__pyx_nargs) {
        case  3:
        values[2] = __Pyx_ArgRef_FASTCALL(__pyx_args, 2);
        if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[2])) __PYX_ERR(0, 604, __pyx_L3_error)
        CYTHON_FALLTHROUGH;
        case  2:
        values[1] = __Pyx_ArgRef_FASTCALL(__pyx_args, 1);
        if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[1])) __PYX_ERR(0, 604, __pyx_L3_error)
        CYTHON_FALLTHROUGH;
        case  1:
        values[0] = __Pyx_ArgRef_FASTCALL(__pyx_args, 0);
        if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[0])) __PYX_ERR(0, 604, __pyx_L3_error)
        CYTHON_FALLTHROUGH;
        case  0: break;
        default: goto __pyx_L5_argtuple_error;
      }
      const Py_ssize_t kwd_pos_args = __pyx_nargs;
      if (__Pyx_ParseKeywords(__pyx_kwds, __pyx_kwvalues, __pyx_pyargnames, 0, values, kwd_pos_args, __pyx_kwds_len, "expected", 0) < (0)) __PYX_ERR(0, 604, __pyx_L3_error)
      if (!values[2]) values[2] = __Pyx_NewRef(((PyObject *)Py_None));
      for (Py_ssize_t i = __pyx_nargs; i < 2; i++) {
        if (unlikely(!values[i])) { __Pyx_RaiseArgtupleInvalid("expected", 0, 2, 3, i); __PYX_ERR(0, 604, __pyx_L3_error) }
      }
    } else {
      switch (__pyx_nargs) {
        case  3:
        values[2] = __Pyx_ArgRef_FASTCALL(__pyx_args, 2);
        if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[2])) __PYX_ERR(0, 604, __pyx_L3_error)
        CYTHON_FALLTHROUGH;
        case  2:
        values[1] = __Pyx_ArgRef_FASTCALL(__pyx_args, 1);
        if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[1])) __PYX_ERR(0, 604, __pyx_L3_error)
        values[0] = __Pyx_ArgRef_FASTCALL(__pyx_args, 0);
        if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[0])) __PYX_ERR(0, 604, __pyx_L3_error)
        break;
        default: goto __pyx_L5_argtuple_error;
      }
      if (!values[2]) values[2] = __Pyx_NewRef(((PyObject *)Py_None));
    }
    __pyx_v_self = values[0];
    __pyx_v_what = values[1];
    __pyx_v_message = values[2];
  }
  goto __pyx_L6_skip;
  __pyx_L5_argtuple_error:;
  __Pyx_RaiseArgtupleInvalid("expected", 0, 2, 3, __pyx_nargs); __PYX_ERR(0, 604, __pyx_L3_error)
  __pyx_L6_skip:;
  goto __pyx_L4_argument_unpacking_done;
  __pyx_L3_error:;
  for (Py_ssize_t __pyx_temp=0; __pyx_temp < (Py_ssize_t)(sizeof(values)/sizeof(values[0])); ++__pyx_temp) {
    Py_XDECREF(values[__pyx_temp]);
  }
  __Pyx_AddTraceback("Cython.Compiler.Scanning.PyrexScanner.expected", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __Pyx_RefNannyFinishContext();
  return NULL;
  __pyx_L4_argument_unpacking_done:;
  __pyx_r = __pyx_pf_6Cython_8Compiler_8Scanning_12PyrexScanner_58expected(__pyx_self, __pyx_v_self, __pyx_v_what, __pyx_v_message);

  /* function exit code */
  for (Py_ssize_t __pyx_temp=0; __pyx_temp < (Py_ssize_t)(sizeof(values)/sizeof(values[0])); ++__pyx_temp) {
    Py_XDECREF(values[__pyx_temp]);
  }
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}

static PyObject *__pyx_pf_6Cython_8Compiler_8Scanning_12PyrexScanner_58expected(CYTHON_UNUSED PyObject *__pyx_self, PyObject *__pyx_v_self, PyObject *__pyx_v_what, PyObject *__pyx_v_message) {
  PyObject *__pyx_v_found = NULL;
  PyObject *__pyx_r = NULL;
/* … */
  /* function exit code */
  __pyx_r = Py_None; __Pyx_INCREF(Py_None);
  goto __pyx_L0;
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_t_2);
  __Pyx_XDECREF(__pyx_t_3);
  __Pyx_XDECREF(__pyx_t_5);
  __Pyx_XDECREF(__pyx_t_6);
  __Pyx_XDECREF(__pyx_t_8);
  __Pyx_AddTraceback("Cython.Compiler.Scanning.PyrexScanner.expected", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_r = NULL;
  __pyx_L0:;
  __Pyx_XDECREF(__pyx_v_found);
  __Pyx_XGIVEREF(__pyx_r);
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}
/* … */
  __pyx_t_9 = __Pyx_CyFunction_New(&__pyx_mdef_6Cython_8Compiler_8Scanning_12PyrexScanner_59expected, 0, __pyx_mstate_global->__pyx_n_u_PyrexScanner_expected, NULL, __pyx_mstate_global->__pyx_n_u_Cython_Compiler_Scanning, __pyx_mstate_global->__pyx_d, ((PyObject *)__pyx_mstate_global->__pyx_codeobj_tab[64])); if (unlikely(!__pyx_t_9)) __PYX_ERR(0, 604, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_9);
  #if CYTHON_COMPILING_IN_CPYTHON && PY_VERSION_HEX >= 0x030E0000
  PyUnstable_Object_EnableDeferredRefcount(__pyx_t_9);
  #endif
  __Pyx_CyFunction_SetDefaultsTuple(__pyx_t_9, __pyx_mstate_global->__pyx_tuple[16]);
  if (__Pyx_SetNameInClass(__pyx_t_8, __pyx_mstate_global->__pyx_n_u_expected, __pyx_t_9) < (0)) __PYX_ERR(0, 604, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_9); __pyx_t_9 = 0;
```

</details>

L605  🟡  (score=2)
```python
        if message:
```
<details><summary>Show generated C (score=2)</summary>

```c
  __pyx_t_1 = __Pyx_PyObject_IsTrue(__pyx_v_message); if (unlikely((__pyx_t_1 < 0))) __PYX_ERR(0, 605, __pyx_L1_error)
  if (__pyx_t_1) {
/* … */
    goto __pyx_L3;
  }
```

</details>

L606  🟠  (score=5)
```python
            self.error(message)
```
<details><summary>Show generated C (score=5)</summary>

```c
    __pyx_t_3 = __pyx_v_self;
    __Pyx_INCREF(__pyx_t_3);
    __pyx_t_4 = 0;
    {
      PyObject *__pyx_callargs[2] = {__pyx_t_3, __pyx_v_message};
      __pyx_t_2 = __Pyx_PyObject_FastCallMethod((PyObject*)__pyx_mstate_global->__pyx_n_u_error, __pyx_callargs+__pyx_t_4, (2-__pyx_t_4) | (1*__Pyx_PY_VECTORCALL_ARGUMENTS_OFFSET));
      __Pyx_XDECREF(__pyx_t_3); __pyx_t_3 = 0;
      if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 606, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_2);
    }
    __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
```

</details>

L607  ⚪  (score=0)
```python
        else:
```
L608  🔴  (score=14)
```python
            if self.sy == IDENT:
```
<details><summary>Show generated C (score=14)</summary>

```c
  /*else*/ {
    __pyx_t_2 = __Pyx_PyObject_GetAttrStr(__pyx_v_self, __pyx_mstate_global->__pyx_n_u_sy); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 608, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_2);
    __Pyx_GetModuleGlobalName(__pyx_t_3, __pyx_mstate_global->__pyx_n_u_IDENT); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 608, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_3);
    __pyx_t_5 = PyObject_RichCompare(__pyx_t_2, __pyx_t_3, Py_EQ); __Pyx_XGOTREF(__pyx_t_5); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 608, __pyx_L1_error)
    __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
    __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
    __pyx_t_1 = __Pyx_PyObject_IsTrue(__pyx_t_5); if (unlikely((__pyx_t_1 < 0))) __PYX_ERR(0, 608, __pyx_L1_error)
    __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
    if (__pyx_t_1) {
/* … */
      goto __pyx_L4;
    }
```

</details>

L609  🟡  (score=2)
```python
                found = self.systring
```
<details><summary>Show generated C (score=2)</summary>

```c
      __pyx_t_5 = __Pyx_PyObject_GetAttrStr(__pyx_v_self, __pyx_mstate_global->__pyx_n_u_systring); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 609, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_5);
      __pyx_v_found = __pyx_t_5;
      __pyx_t_5 = 0;
```

</details>

L610  ⚪  (score=0)
```python
            else:
```
L611  🟡  (score=2)
```python
                found = self.sy
```
<details><summary>Show generated C (score=2)</summary>

```c
    /*else*/ {
      __pyx_t_5 = __Pyx_PyObject_GetAttrStr(__pyx_v_self, __pyx_mstate_global->__pyx_n_u_sy); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 611, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_5);
      __pyx_v_found = __pyx_t_5;
      __pyx_t_5 = 0;
    }
    __pyx_L4:;
```

</details>

L612  🔴  (score=32)
```python
            self.error("Expected '%s', found '%s'" % (what, found))
```
<details><summary>Show generated C (score=32)</summary>

```c
    __pyx_t_3 = __pyx_v_self;
    __Pyx_INCREF(__pyx_t_3);
    __pyx_t_2 = __Pyx_PyObject_FormatSimpleAndDecref(PyObject_Str(__pyx_v_what), __pyx_mstate_global->__pyx_empty_unicode); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 612, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_2);
    __pyx_t_6 = __Pyx_PyObject_FormatSimpleAndDecref(PyObject_Str(__pyx_v_found), __pyx_mstate_global->__pyx_empty_unicode); if (unlikely(!__pyx_t_6)) __PYX_ERR(0, 612, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_6);
    __pyx_t_7[0] = __pyx_mstate_global->__pyx_kp_u_Expected;
    __pyx_t_7[1] = __pyx_t_2;
    __pyx_t_7[2] = __pyx_mstate_global->__pyx_kp_u_found;
    __pyx_t_7[3] = __pyx_t_6;
    __pyx_t_7[4] = __pyx_mstate_global->__pyx_kp_u__10;
    __pyx_t_8 = __Pyx_PyUnicode_Join(__pyx_t_7, 5, 10 * 2 + __Pyx_PyUnicode_GET_LENGTH(__pyx_t_2) + __Pyx_PyUnicode_GET_LENGTH(__pyx_t_6) + 1, 127 | __Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_2) | __Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_6));
    if (unlikely(!__pyx_t_8)) __PYX_ERR(0, 612, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_8);
    __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
    __Pyx_DECREF(__pyx_t_6); __pyx_t_6 = 0;
    __pyx_t_4 = 0;
    {
      PyObject *__pyx_callargs[2] = {__pyx_t_3, __pyx_t_8};
      __pyx_t_5 = __Pyx_PyObject_FastCallMethod((PyObject*)__pyx_mstate_global->__pyx_n_u_error, __pyx_callargs+__pyx_t_4, (2-__pyx_t_4) | (1*__Pyx_PY_VECTORCALL_ARGUMENTS_OFFSET));
      __Pyx_XDECREF(__pyx_t_3); __pyx_t_3 = 0;
      __Pyx_DECREF(__pyx_t_8); __pyx_t_8 = 0;
      if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 612, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_5);
    }
    __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
  }
  __pyx_L3:;
```

</details>

L613  ⚪  (score=0)
```python
```
L614  🔴  (score=38)
```python
    def expect_indent(self):
```
<details><summary>Show generated C (score=38)</summary>

```c
/* Python wrapper */
static PyObject *__pyx_pw_6Cython_8Compiler_8Scanning_12PyrexScanner_61expect_indent(PyObject *__pyx_self, 
#if CYTHON_METH_FASTCALL
PyObject *const *__pyx_args, Py_ssize_t __pyx_nargs, PyObject *__pyx_kwds
#else
PyObject *__pyx_args, PyObject *__pyx_kwds
#endif
); /*proto*/
PyDoc_STRVAR(__pyx_doc_6Cython_8Compiler_8Scanning_12PyrexScanner_60expect_indent, "File: Cython/Compiler/Scanning.py (starting at line 614)");
static PyMethodDef __pyx_mdef_6Cython_8Compiler_8Scanning_12PyrexScanner_61expect_indent = {"expect_indent", (PyCFunction)(void(*)(void))(__Pyx_PyCFunction_FastCallWithKeywords)__pyx_pw_6Cython_8Compiler_8Scanning_12PyrexScanner_61expect_indent, __Pyx_METH_FASTCALL|METH_KEYWORDS, __pyx_doc_6Cython_8Compiler_8Scanning_12PyrexScanner_60expect_indent};
static PyObject *__pyx_pw_6Cython_8Compiler_8Scanning_12PyrexScanner_61expect_indent(PyObject *__pyx_self, 
#if CYTHON_METH_FASTCALL
PyObject *const *__pyx_args, Py_ssize_t __pyx_nargs, PyObject *__pyx_kwds
#else
PyObject *__pyx_args, PyObject *__pyx_kwds
#endif
) {
  PyObject *__pyx_v_self = 0;
  #if !CYTHON_METH_FASTCALL
  CYTHON_UNUSED Py_ssize_t __pyx_nargs;
  #endif
  CYTHON_UNUSED PyObject *const *__pyx_kwvalues;
  PyObject *__pyx_r = 0;
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("expect_indent (wrapper)", 0);
  #if !CYTHON_METH_FASTCALL
  #if CYTHON_ASSUME_SAFE_SIZE
  __pyx_nargs = PyTuple_GET_SIZE(__pyx_args);
  #else
  __pyx_nargs = PyTuple_Size(__pyx_args); if (unlikely(__pyx_nargs < 0)) return NULL;
  #endif
  #endif
  __pyx_kwvalues = __Pyx_KwValues_FASTCALL(__pyx_args, __pyx_nargs);
  {
    PyObject ** const __pyx_pyargnames[] = {&__pyx_mstate_global->__pyx_n_u_self,0};
  PyObject* values[1] = {0};
    const Py_ssize_t __pyx_kwds_len = (__pyx_kwds) ? __Pyx_NumKwargs_FASTCALL(__pyx_kwds) : 0;
    if (unlikely(__pyx_kwds_len) < 0) __PYX_ERR(0, 614, __pyx_L3_error)
    if (__pyx_kwds_len > 0) {
      switch (__pyx_nargs) {
        case  1:
        values[0] = __Pyx_ArgRef_FASTCALL(__pyx_args, 0);
        if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[0])) __PYX_ERR(0, 614, __pyx_L3_error)
        CYTHON_FALLTHROUGH;
        case  0: break;
        default: goto __pyx_L5_argtuple_error;
      }
      const Py_ssize_t kwd_pos_args = __pyx_nargs;
      if (__Pyx_ParseKeywords(__pyx_kwds, __pyx_kwvalues, __pyx_pyargnames, 0, values, kwd_pos_args, __pyx_kwds_len, "expect_indent", 0) < (0)) __PYX_ERR(0, 614, __pyx_L3_error)
      for (Py_ssize_t i = __pyx_nargs; i < 1; i++) {
        if (unlikely(!values[i])) { __Pyx_RaiseArgtupleInvalid("expect_indent", 1, 1, 1, i); __PYX_ERR(0, 614, __pyx_L3_error) }
      }
    } else if (unlikely(__pyx_nargs != 1)) {
      goto __pyx_L5_argtuple_error;
    } else {
      values[0] = __Pyx_ArgRef_FASTCALL(__pyx_args, 0);
      if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[0])) __PYX_ERR(0, 614, __pyx_L3_error)
    }
    __pyx_v_self = values[0];
  }
  goto __pyx_L6_skip;
  __pyx_L5_argtuple_error:;
  __Pyx_RaiseArgtupleInvalid("expect_indent", 1, 1, 1, __pyx_nargs); __PYX_ERR(0, 614, __pyx_L3_error)
  __pyx_L6_skip:;
  goto __pyx_L4_argument_unpacking_done;
  __pyx_L3_error:;
  for (Py_ssize_t __pyx_temp=0; __pyx_temp < (Py_ssize_t)(sizeof(values)/sizeof(values[0])); ++__pyx_temp) {
    Py_XDECREF(values[__pyx_temp]);
  }
  __Pyx_AddTraceback("Cython.Compiler.Scanning.PyrexScanner.expect_indent", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __Pyx_RefNannyFinishContext();
  return NULL;
  __pyx_L4_argument_unpacking_done:;
  __pyx_r = __pyx_pf_6Cython_8Compiler_8Scanning_12PyrexScanner_60expect_indent(__pyx_self, __pyx_v_self);
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

static PyObject *__pyx_pf_6Cython_8Compiler_8Scanning_12PyrexScanner_60expect_indent(CYTHON_UNUSED PyObject *__pyx_self, PyObject *__pyx_v_self) {
  PyObject *__pyx_r = NULL;
/* … */
  /* function exit code */
  __pyx_r = Py_None; __Pyx_INCREF(Py_None);
  goto __pyx_L0;
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_t_1);
  __Pyx_XDECREF(__pyx_t_2);
  __Pyx_AddTraceback("Cython.Compiler.Scanning.PyrexScanner.expect_indent", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_r = NULL;
  __pyx_L0:;
  __Pyx_XGIVEREF(__pyx_r);
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}
/* … */
  __pyx_t_9 = __Pyx_CyFunction_New(&__pyx_mdef_6Cython_8Compiler_8Scanning_12PyrexScanner_61expect_indent, 0, __pyx_mstate_global->__pyx_n_u_PyrexScanner_expect_indent, NULL, __pyx_mstate_global->__pyx_n_u_Cython_Compiler_Scanning, __pyx_mstate_global->__pyx_d, ((PyObject *)__pyx_mstate_global->__pyx_codeobj_tab[65])); if (unlikely(!__pyx_t_9)) __PYX_ERR(0, 614, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_9);
  #if CYTHON_COMPILING_IN_CPYTHON && PY_VERSION_HEX >= 0x030E0000
  PyUnstable_Object_EnableDeferredRefcount(__pyx_t_9);
  #endif
  if (__Pyx_SetNameInClass(__pyx_t_8, __pyx_mstate_global->__pyx_n_u_expect_indent, __pyx_t_9) < (0)) __PYX_ERR(0, 614, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_9); __pyx_t_9 = 0;
```

</details>

L615  🔴  (score=11)
```python
        self.expect('INDENT', "Expected an increase in indentation level")
```
<details><summary>Show generated C (score=11)</summary>

```c
  __pyx_t_1 = __Pyx_PyObject_GetAttrStr(__pyx_v_self, __pyx_mstate_global->__pyx_n_u_expect); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 615, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __pyx_t_2 = __Pyx_PyObject_Call(__pyx_t_1, __pyx_mstate_global->__pyx_tuple[14], NULL); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 615, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
/* … */
  __pyx_mstate_global->__pyx_tuple[14] = PyTuple_Pack(2, __pyx_mstate_global->__pyx_n_u_INDENT, __pyx_mstate_global->__pyx_kp_u_Expected_an_increase_in_indentat); if (unlikely(!__pyx_mstate_global->__pyx_tuple[14])) __PYX_ERR(0, 615, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_mstate_global->__pyx_tuple[14]);
  __Pyx_GIVEREF(__pyx_mstate_global->__pyx_tuple[14]);
```

</details>

L616  ⚪  (score=0)
```python
```
L617  🔴  (score=38)
```python
    def expect_dedent(self):
```
<details><summary>Show generated C (score=38)</summary>

```c
/* Python wrapper */
static PyObject *__pyx_pw_6Cython_8Compiler_8Scanning_12PyrexScanner_63expect_dedent(PyObject *__pyx_self, 
#if CYTHON_METH_FASTCALL
PyObject *const *__pyx_args, Py_ssize_t __pyx_nargs, PyObject *__pyx_kwds
#else
PyObject *__pyx_args, PyObject *__pyx_kwds
#endif
); /*proto*/
PyDoc_STRVAR(__pyx_doc_6Cython_8Compiler_8Scanning_12PyrexScanner_62expect_dedent, "File: Cython/Compiler/Scanning.py (starting at line 617)");
static PyMethodDef __pyx_mdef_6Cython_8Compiler_8Scanning_12PyrexScanner_63expect_dedent = {"expect_dedent", (PyCFunction)(void(*)(void))(__Pyx_PyCFunction_FastCallWithKeywords)__pyx_pw_6Cython_8Compiler_8Scanning_12PyrexScanner_63expect_dedent, __Pyx_METH_FASTCALL|METH_KEYWORDS, __pyx_doc_6Cython_8Compiler_8Scanning_12PyrexScanner_62expect_dedent};
static PyObject *__pyx_pw_6Cython_8Compiler_8Scanning_12PyrexScanner_63expect_dedent(PyObject *__pyx_self, 
#if CYTHON_METH_FASTCALL
PyObject *const *__pyx_args, Py_ssize_t __pyx_nargs, PyObject *__pyx_kwds
#else
PyObject *__pyx_args, PyObject *__pyx_kwds
#endif
) {
  PyObject *__pyx_v_self = 0;
  #if !CYTHON_METH_FASTCALL
  CYTHON_UNUSED Py_ssize_t __pyx_nargs;
  #endif
  CYTHON_UNUSED PyObject *const *__pyx_kwvalues;
  PyObject *__pyx_r = 0;
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("expect_dedent (wrapper)", 0);
  #if !CYTHON_METH_FASTCALL
  #if CYTHON_ASSUME_SAFE_SIZE
  __pyx_nargs = PyTuple_GET_SIZE(__pyx_args);
  #else
  __pyx_nargs = PyTuple_Size(__pyx_args); if (unlikely(__pyx_nargs < 0)) return NULL;
  #endif
  #endif
  __pyx_kwvalues = __Pyx_KwValues_FASTCALL(__pyx_args, __pyx_nargs);
  {
    PyObject ** const __pyx_pyargnames[] = {&__pyx_mstate_global->__pyx_n_u_self,0};
  PyObject* values[1] = {0};
    const Py_ssize_t __pyx_kwds_len = (__pyx_kwds) ? __Pyx_NumKwargs_FASTCALL(__pyx_kwds) : 0;
    if (unlikely(__pyx_kwds_len) < 0) __PYX_ERR(0, 617, __pyx_L3_error)
    if (__pyx_kwds_len > 0) {
      switch (__pyx_nargs) {
        case  1:
        values[0] = __Pyx_ArgRef_FASTCALL(__pyx_args, 0);
        if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[0])) __PYX_ERR(0, 617, __pyx_L3_error)
        CYTHON_FALLTHROUGH;
        case  0: break;
        default: goto __pyx_L5_argtuple_error;
      }
      const Py_ssize_t kwd_pos_args = __pyx_nargs;
      if (__Pyx_ParseKeywords(__pyx_kwds, __pyx_kwvalues, __pyx_pyargnames, 0, values, kwd_pos_args, __pyx_kwds_len, "expect_dedent", 0) < (0)) __PYX_ERR(0, 617, __pyx_L3_error)
      for (Py_ssize_t i = __pyx_nargs; i < 1; i++) {
        if (unlikely(!values[i])) { __Pyx_RaiseArgtupleInvalid("expect_dedent", 1, 1, 1, i); __PYX_ERR(0, 617, __pyx_L3_error) }
      }
    } else if (unlikely(__pyx_nargs != 1)) {
      goto __pyx_L5_argtuple_error;
    } else {
      values[0] = __Pyx_ArgRef_FASTCALL(__pyx_args, 0);
      if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[0])) __PYX_ERR(0, 617, __pyx_L3_error)
    }
    __pyx_v_self = values[0];
  }
  goto __pyx_L6_skip;
  __pyx_L5_argtuple_error:;
  __Pyx_RaiseArgtupleInvalid("expect_dedent", 1, 1, 1, __pyx_nargs); __PYX_ERR(0, 617, __pyx_L3_error)
  __pyx_L6_skip:;
  goto __pyx_L4_argument_unpacking_done;
  __pyx_L3_error:;
  for (Py_ssize_t __pyx_temp=0; __pyx_temp < (Py_ssize_t)(sizeof(values)/sizeof(values[0])); ++__pyx_temp) {
    Py_XDECREF(values[__pyx_temp]);
  }
  __Pyx_AddTraceback("Cython.Compiler.Scanning.PyrexScanner.expect_dedent", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __Pyx_RefNannyFinishContext();
  return NULL;
  __pyx_L4_argument_unpacking_done:;
  __pyx_r = __pyx_pf_6Cython_8Compiler_8Scanning_12PyrexScanner_62expect_dedent(__pyx_self, __pyx_v_self);
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

static PyObject *__pyx_pf_6Cython_8Compiler_8Scanning_12PyrexScanner_62expect_dedent(CYTHON_UNUSED PyObject *__pyx_self, PyObject *__pyx_v_self) {
  PyObject *__pyx_r = NULL;
/* … */
  /* function exit code */
  __pyx_r = Py_None; __Pyx_INCREF(Py_None);
  goto __pyx_L0;
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_t_1);
  __Pyx_XDECREF(__pyx_t_2);
  __Pyx_AddTraceback("Cython.Compiler.Scanning.PyrexScanner.expect_dedent", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_r = NULL;
  __pyx_L0:;
  __Pyx_XGIVEREF(__pyx_r);
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}
/* … */
  __pyx_t_9 = __Pyx_CyFunction_New(&__pyx_mdef_6Cython_8Compiler_8Scanning_12PyrexScanner_63expect_dedent, 0, __pyx_mstate_global->__pyx_n_u_PyrexScanner_expect_dedent, NULL, __pyx_mstate_global->__pyx_n_u_Cython_Compiler_Scanning, __pyx_mstate_global->__pyx_d, ((PyObject *)__pyx_mstate_global->__pyx_codeobj_tab[66])); if (unlikely(!__pyx_t_9)) __PYX_ERR(0, 617, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_9);
  #if CYTHON_COMPILING_IN_CPYTHON && PY_VERSION_HEX >= 0x030E0000
  PyUnstable_Object_EnableDeferredRefcount(__pyx_t_9);
  #endif
  if (__Pyx_SetNameInClass(__pyx_t_8, __pyx_mstate_global->__pyx_n_u_expect_dedent, __pyx_t_9) < (0)) __PYX_ERR(0, 617, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_9); __pyx_t_9 = 0;
```

</details>

L618  🔴  (score=11)
```python
        self.expect('DEDENT', "Expected a decrease in indentation level")
```
<details><summary>Show generated C (score=11)</summary>

```c
  __pyx_t_1 = __Pyx_PyObject_GetAttrStr(__pyx_v_self, __pyx_mstate_global->__pyx_n_u_expect); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 618, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __pyx_t_2 = __Pyx_PyObject_Call(__pyx_t_1, __pyx_mstate_global->__pyx_tuple[15], NULL); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 618, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
/* … */
  __pyx_mstate_global->__pyx_tuple[15] = PyTuple_Pack(2, __pyx_mstate_global->__pyx_n_u_DEDENT, __pyx_mstate_global->__pyx_kp_u_Expected_a_decrease_in_indentati); if (unlikely(!__pyx_mstate_global->__pyx_tuple[15])) __PYX_ERR(0, 618, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_mstate_global->__pyx_tuple[15]);
  __Pyx_GIVEREF(__pyx_mstate_global->__pyx_tuple[15]);
```

</details>

L619  ⚪  (score=0)
```python
```
L620  🔴  (score=95)
```python
    def expect_newline(self, message="Expected a newline", ignore_semicolon: cython.bint = False):
```
<details><summary>Show generated C (score=95)</summary>

```c
/* Python wrapper */
static PyObject *__pyx_pw_6Cython_8Compiler_8Scanning_12PyrexScanner_65expect_newline(PyObject *__pyx_self, 
#if CYTHON_METH_FASTCALL
PyObject *const *__pyx_args, Py_ssize_t __pyx_nargs, PyObject *__pyx_kwds
#else
PyObject *__pyx_args, PyObject *__pyx_kwds
#endif
); /*proto*/
PyDoc_STRVAR(__pyx_doc_6Cython_8Compiler_8Scanning_12PyrexScanner_64expect_newline, "File: Cython/Compiler/Scanning.py (starting at line 620)");
static PyMethodDef __pyx_mdef_6Cython_8Compiler_8Scanning_12PyrexScanner_65expect_newline = {"expect_newline", (PyCFunction)(void(*)(void))(__Pyx_PyCFunction_FastCallWithKeywords)__pyx_pw_6Cython_8Compiler_8Scanning_12PyrexScanner_65expect_newline, __Pyx_METH_FASTCALL|METH_KEYWORDS, __pyx_doc_6Cython_8Compiler_8Scanning_12PyrexScanner_64expect_newline};
static PyObject *__pyx_pw_6Cython_8Compiler_8Scanning_12PyrexScanner_65expect_newline(PyObject *__pyx_self, 
#if CYTHON_METH_FASTCALL
PyObject *const *__pyx_args, Py_ssize_t __pyx_nargs, PyObject *__pyx_kwds
#else
PyObject *__pyx_args, PyObject *__pyx_kwds
#endif
) {
  PyObject *__pyx_v_self = 0;
  PyObject *__pyx_v_message = 0;
  int __pyx_v_ignore_semicolon;
  #if !CYTHON_METH_FASTCALL
  CYTHON_UNUSED Py_ssize_t __pyx_nargs;
  #endif
  CYTHON_UNUSED PyObject *const *__pyx_kwvalues;
  PyObject *__pyx_r = 0;
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("expect_newline (wrapper)", 0);
  #if !CYTHON_METH_FASTCALL
  #if CYTHON_ASSUME_SAFE_SIZE
  __pyx_nargs = PyTuple_GET_SIZE(__pyx_args);
  #else
  __pyx_nargs = PyTuple_Size(__pyx_args); if (unlikely(__pyx_nargs < 0)) return NULL;
  #endif
  #endif
  __pyx_kwvalues = __Pyx_KwValues_FASTCALL(__pyx_args, __pyx_nargs);
  {
    PyObject ** const __pyx_pyargnames[] = {&__pyx_mstate_global->__pyx_n_u_self,&__pyx_mstate_global->__pyx_n_u_message,&__pyx_mstate_global->__pyx_n_u_ignore_semicolon,0};
  PyObject* values[3] = {0,0,0};
    const Py_ssize_t __pyx_kwds_len = (__pyx_kwds) ? __Pyx_NumKwargs_FASTCALL(__pyx_kwds) : 0;
    if (unlikely(__pyx_kwds_len) < 0) __PYX_ERR(0, 620, __pyx_L3_error)
    if (__pyx_kwds_len > 0) {
      switch (__pyx_nargs) {
        case  3:
        values[2] = __Pyx_ArgRef_FASTCALL(__pyx_args, 2);
        if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[2])) __PYX_ERR(0, 620, __pyx_L3_error)
        CYTHON_FALLTHROUGH;
        case  2:
        values[1] = __Pyx_ArgRef_FASTCALL(__pyx_args, 1);
        if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[1])) __PYX_ERR(0, 620, __pyx_L3_error)
        CYTHON_FALLTHROUGH;
        case  1:
        values[0] = __Pyx_ArgRef_FASTCALL(__pyx_args, 0);
        if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[0])) __PYX_ERR(0, 620, __pyx_L3_error)
        CYTHON_FALLTHROUGH;
        case  0: break;
        default: goto __pyx_L5_argtuple_error;
      }
      const Py_ssize_t kwd_pos_args = __pyx_nargs;
      if (__Pyx_ParseKeywords(__pyx_kwds, __pyx_kwvalues, __pyx_pyargnames, 0, values, kwd_pos_args, __pyx_kwds_len, "expect_newline", 0) < (0)) __PYX_ERR(0, 620, __pyx_L3_error)
      if (!values[1]) values[1] = __Pyx_NewRef(((PyObject *)((PyObject*)__pyx_mstate_global->__pyx_kp_u_Expected_a_newline)));
      for (Py_ssize_t i = __pyx_nargs; i < 1; i++) {
        if (unlikely(!values[i])) { __Pyx_RaiseArgtupleInvalid("expect_newline", 0, 1, 3, i); __PYX_ERR(0, 620, __pyx_L3_error) }
      }
    } else {
      switch (__pyx_nargs) {
        case  3:
        values[2] = __Pyx_ArgRef_FASTCALL(__pyx_args, 2);
        if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[2])) __PYX_ERR(0, 620, __pyx_L3_error)
        CYTHON_FALLTHROUGH;
        case  2:
        values[1] = __Pyx_ArgRef_FASTCALL(__pyx_args, 1);
        if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[1])) __PYX_ERR(0, 620, __pyx_L3_error)
        CYTHON_FALLTHROUGH;
        case  1:
        values[0] = __Pyx_ArgRef_FASTCALL(__pyx_args, 0);
        if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[0])) __PYX_ERR(0, 620, __pyx_L3_error)
        break;
        default: goto __pyx_L5_argtuple_error;
      }
      if (!values[1]) values[1] = __Pyx_NewRef(((PyObject *)((PyObject*)__pyx_mstate_global->__pyx_kp_u_Expected_a_newline)));
    }
    __pyx_v_self = values[0];
    __pyx_v_message = values[1];
    if (values[2]) {
      __pyx_v_ignore_semicolon = __Pyx_PyObject_IsTrue(values[2]); if (unlikely((__pyx_v_ignore_semicolon == (int)-1) && PyErr_Occurred())) __PYX_ERR(0, 620, __pyx_L3_error)
    } else {
      __pyx_v_ignore_semicolon = ((int)((int)0));
    }
  }
  goto __pyx_L6_skip;
  __pyx_L5_argtuple_error:;
  __Pyx_RaiseArgtupleInvalid("expect_newline", 0, 1, 3, __pyx_nargs); __PYX_ERR(0, 620, __pyx_L3_error)
  __pyx_L6_skip:;
  goto __pyx_L4_argument_unpacking_done;
  __pyx_L3_error:;
  for (Py_ssize_t __pyx_temp=0; __pyx_temp < (Py_ssize_t)(sizeof(values)/sizeof(values[0])); ++__pyx_temp) {
    Py_XDECREF(values[__pyx_temp]);
  }
  __Pyx_AddTraceback("Cython.Compiler.Scanning.PyrexScanner.expect_newline", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __Pyx_RefNannyFinishContext();
  return NULL;
  __pyx_L4_argument_unpacking_done:;
  __pyx_r = __pyx_pf_6Cython_8Compiler_8Scanning_12PyrexScanner_64expect_newline(__pyx_self, __pyx_v_self, __pyx_v_message, __pyx_v_ignore_semicolon);

  /* function exit code */
  for (Py_ssize_t __pyx_temp=0; __pyx_temp < (Py_ssize_t)(sizeof(values)/sizeof(values[0])); ++__pyx_temp) {
    Py_XDECREF(values[__pyx_temp]);
  }
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}

static PyObject *__pyx_pf_6Cython_8Compiler_8Scanning_12PyrexScanner_64expect_newline(CYTHON_UNUSED PyObject *__pyx_self, PyObject *__pyx_v_self, PyObject *__pyx_v_message, int __pyx_v_ignore_semicolon) {
  PyObject *__pyx_v_useless_trailing_semicolon = NULL;
  PyObject *__pyx_r = NULL;
/* … */
  /* function exit code */
  __pyx_r = Py_None; __Pyx_INCREF(Py_None);
  goto __pyx_L0;
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_t_2);
  __Pyx_XDECREF(__pyx_t_4);
  __Pyx_XDECREF(__pyx_t_6);
  __Pyx_AddTraceback("Cython.Compiler.Scanning.PyrexScanner.expect_newline", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_r = NULL;
  __pyx_L0:;
  __Pyx_XDECREF(__pyx_v_useless_trailing_semicolon);
  __Pyx_XGIVEREF(__pyx_r);
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}
/* … */
  __pyx_t_9 = __Pyx_PyBool_FromLong(((int)0)); if (unlikely(!__pyx_t_9)) __PYX_ERR(0, 620, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_9);
  __pyx_t_7 = PyTuple_Pack(2, ((PyObject*)__pyx_mstate_global->__pyx_kp_u_Expected_a_newline), __pyx_t_9); if (unlikely(!__pyx_t_7)) __PYX_ERR(0, 620, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_7);
  __Pyx_DECREF(__pyx_t_9); __pyx_t_9 = 0;
  __pyx_t_9 = __Pyx_PyDict_NewPresized(1); if (unlikely(!__pyx_t_9)) __PYX_ERR(0, 620, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_9);
  #if defined(PyDict_SetItem) && (defined(CYTHON_COMPILING_IN_CPYTHON))
  #if PY_VERSION_HEX >= 0x030A0000 /* CPython 3.10+ exposes KnownHash APIs */
  /* Use CPython's KnownHash APIs when available */
  extern int _PyDict_SetItem_KnownHash(PyObject*, PyObject*, PyObject*, Py_hash_t);
  {
    Py_hash_t __pyx_hash = PyObject_Hash(__pyx_mstate_global->__pyx_n_u_ignore_semicolon); if (unlikely(__pyx_hash == -1)) __PYX_ERR(0, 620, __pyx_L1_error);
    if (unlikely(_PyDict_SetItem_KnownHash(__pyx_t_9, __pyx_mstate_global->__pyx_n_u_ignore_semicolon, __pyx_mstate_global->__pyx_kp_u_cython_bint, __pyx_hash) < 0)) __PYX_ERR(0, 620, __pyx_L1_error);
  }
  #else
  if (PyDict_SetItem(__pyx_t_9, __pyx_mstate_global->__pyx_n_u_ignore_semicolon, __pyx_mstate_global->__pyx_kp_u_cython_bint) < (0)) __PYX_ERR(0, 620, __pyx_L1_error)
  #endif
  #else
  if (PyDict_SetItem(__pyx_t_9, __pyx_mstate_global->__pyx_n_u_ignore_semicolon, __pyx_mstate_global->__pyx_kp_u_cython_bint) < (0)) __PYX_ERR(0, 620, __pyx_L1_error)
  #endif
  __pyx_t_2 = __Pyx_CyFunction_New(&__pyx_mdef_6Cython_8Compiler_8Scanning_12PyrexScanner_65expect_newline, 0, __pyx_mstate_global->__pyx_n_u_PyrexScanner_expect_newline, NULL, __pyx_mstate_global->__pyx_n_u_Cython_Compiler_Scanning, __pyx_mstate_global->__pyx_d, ((PyObject *)__pyx_mstate_global->__pyx_codeobj_tab[67])); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 620, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  #if CYTHON_COMPILING_IN_CPYTHON && PY_VERSION_HEX >= 0x030E0000
  PyUnstable_Object_EnableDeferredRefcount(__pyx_t_2);
  #endif
  __Pyx_CyFunction_SetDefaultsTuple(__pyx_t_2, __pyx_t_7);
  __Pyx_CyFunction_SetAnnotationsDict(__pyx_t_2, __pyx_t_9);
  __Pyx_DECREF(__pyx_t_7); __pyx_t_7 = 0;
  __Pyx_DECREF(__pyx_t_9); __pyx_t_9 = 0;
  if (__Pyx_SetNameInClass(__pyx_t_8, __pyx_mstate_global->__pyx_n_u_expect_newline, __pyx_t_2) < (0)) __PYX_ERR(0, 620, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
```

</details>

L621  ⚪  (score=0)
```python
        # Expect either a newline or end of file
```
L622  🟡  (score=1)
```python
        useless_trailing_semicolon = None
```
<details><summary>Show generated C (score=1)</summary>

```c
  __Pyx_INCREF(Py_None);
  __pyx_v_useless_trailing_semicolon = Py_None;
```

</details>

L623  🟠  (score=5)
```python
        if ignore_semicolon and self.sy == ';':
```
<details><summary>Show generated C (score=5)</summary>

```c
  if (__pyx_v_ignore_semicolon) {
  } else {
    __pyx_t_1 = __pyx_v_ignore_semicolon;
    goto __pyx_L4_bool_binop_done;
  }
  __pyx_t_2 = __Pyx_PyObject_GetAttrStr(__pyx_v_self, __pyx_mstate_global->__pyx_n_u_sy); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 623, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __pyx_t_3 = (__Pyx_PyUnicode_Equals(__pyx_t_2, __pyx_mstate_global->__pyx_kp_u__11, Py_EQ)); if (unlikely((__pyx_t_3 < 0))) __PYX_ERR(0, 623, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __pyx_t_1 = __pyx_t_3;
  __pyx_L4_bool_binop_done:;
  if (__pyx_t_1) {
/* … */
  }
```

</details>

L624  🟠  (score=5)
```python
            useless_trailing_semicolon = self.position()
```
<details><summary>Show generated C (score=5)</summary>

```c
    __pyx_t_4 = __pyx_v_self;
    __Pyx_INCREF(__pyx_t_4);
    __pyx_t_5 = 0;
    {
      PyObject *__pyx_callargs[2] = {__pyx_t_4, NULL};
      __pyx_t_2 = __Pyx_PyObject_FastCallMethod((PyObject*)__pyx_mstate_global->__pyx_n_u_position, __pyx_callargs+__pyx_t_5, (1-__pyx_t_5) | (1*__Pyx_PY_VECTORCALL_ARGUMENTS_OFFSET));
      __Pyx_XDECREF(__pyx_t_4); __pyx_t_4 = 0;
      if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 624, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_2);
    }
    __Pyx_DECREF_SET(__pyx_v_useless_trailing_semicolon, __pyx_t_2);
    __pyx_t_2 = 0;
```

</details>

L625  🟠  (score=5)
```python
            self.next()
```
<details><summary>Show generated C (score=5)</summary>

```c
    __pyx_t_4 = __pyx_v_self;
    __Pyx_INCREF(__pyx_t_4);
    __pyx_t_5 = 0;
    {
      PyObject *__pyx_callargs[2] = {__pyx_t_4, NULL};
      __pyx_t_2 = __Pyx_PyObject_FastCallMethod((PyObject*)__pyx_mstate_global->__pyx_n_u_next, __pyx_callargs+__pyx_t_5, (1-__pyx_t_5) | (1*__Pyx_PY_VECTORCALL_ARGUMENTS_OFFSET));
      __Pyx_XDECREF(__pyx_t_4); __pyx_t_4 = 0;
      if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 625, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_2);
    }
    __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
```

</details>

L626  🟠  (score=5)
```python
        if self.sy != 'EOF':
```
<details><summary>Show generated C (score=5)</summary>

```c
  __pyx_t_2 = __Pyx_PyObject_GetAttrStr(__pyx_v_self, __pyx_mstate_global->__pyx_n_u_sy); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 626, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __pyx_t_1 = (__Pyx_PyUnicode_Equals(__pyx_t_2, __pyx_mstate_global->__pyx_n_u_EOF, Py_NE)); if (unlikely((__pyx_t_1 < 0))) __PYX_ERR(0, 626, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  if (__pyx_t_1) {
/* … */
  }
```

</details>

L627  🟠  (score=5)
```python
            self.expect('NEWLINE', message)
```
<details><summary>Show generated C (score=5)</summary>

```c
    __pyx_t_4 = __pyx_v_self;
    __Pyx_INCREF(__pyx_t_4);
    __pyx_t_5 = 0;
    {
      PyObject *__pyx_callargs[3] = {__pyx_t_4, __pyx_mstate_global->__pyx_n_u_NEWLINE, __pyx_v_message};
      __pyx_t_2 = __Pyx_PyObject_FastCallMethod((PyObject*)__pyx_mstate_global->__pyx_n_u_expect, __pyx_callargs+__pyx_t_5, (3-__pyx_t_5) | (1*__Pyx_PY_VECTORCALL_ARGUMENTS_OFFSET));
      __Pyx_XDECREF(__pyx_t_4); __pyx_t_4 = 0;
      if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 627, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_2);
    }
    __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
```

</details>

L628  ⚪  (score=0)
```python
        if useless_trailing_semicolon is not None:
```
<details><summary>Show generated C (score=0)</summary>

```c
  __pyx_t_1 = (__pyx_v_useless_trailing_semicolon != Py_None);
  if (__pyx_t_1) {
/* … */
  }
```

</details>

L629  🟠  (score=6)
```python
            warning(useless_trailing_semicolon, "useless trailing semicolon")
```
<details><summary>Show generated C (score=6)</summary>

```c
    __pyx_t_4 = NULL;
    __Pyx_INCREF(__pyx_v_6Cython_8Compiler_8Scanning_warning);
    __pyx_t_6 = __pyx_v_6Cython_8Compiler_8Scanning_warning; 
    __pyx_t_5 = 1;
    {
      PyObject *__pyx_callargs[3] = {__pyx_t_4, __pyx_v_useless_trailing_semicolon, __pyx_mstate_global->__pyx_kp_u_useless_trailing_semicolon};
      __pyx_t_2 = __Pyx_PyObject_FastCall((PyObject*)__pyx_t_6, __pyx_callargs+__pyx_t_5, (3-__pyx_t_5) | (__pyx_t_5*__Pyx_PY_VECTORCALL_ARGUMENTS_OFFSET));
      __Pyx_XDECREF(__pyx_t_4); __pyx_t_4 = 0;
      __Pyx_DECREF(__pyx_t_6); __pyx_t_6 = 0;
      if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 629, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_2);
    }
    __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
```

</details>

L630  ⚪  (score=0)
```python
```
L631  🔴  (score=38)
```python
    def enter_async(self):
```
<details><summary>Show generated C (score=38)</summary>

```c
/* Python wrapper */
static PyObject *__pyx_pw_6Cython_8Compiler_8Scanning_12PyrexScanner_67enter_async(PyObject *__pyx_self, 
#if CYTHON_METH_FASTCALL
PyObject *const *__pyx_args, Py_ssize_t __pyx_nargs, PyObject *__pyx_kwds
#else
PyObject *__pyx_args, PyObject *__pyx_kwds
#endif
); /*proto*/
PyDoc_STRVAR(__pyx_doc_6Cython_8Compiler_8Scanning_12PyrexScanner_66enter_async, "File: Cython/Compiler/Scanning.py (starting at line 631)");
static PyMethodDef __pyx_mdef_6Cython_8Compiler_8Scanning_12PyrexScanner_67enter_async = {"enter_async", (PyCFunction)(void(*)(void))(__Pyx_PyCFunction_FastCallWithKeywords)__pyx_pw_6Cython_8Compiler_8Scanning_12PyrexScanner_67enter_async, __Pyx_METH_FASTCALL|METH_KEYWORDS, __pyx_doc_6Cython_8Compiler_8Scanning_12PyrexScanner_66enter_async};
static PyObject *__pyx_pw_6Cython_8Compiler_8Scanning_12PyrexScanner_67enter_async(PyObject *__pyx_self, 
#if CYTHON_METH_FASTCALL
PyObject *const *__pyx_args, Py_ssize_t __pyx_nargs, PyObject *__pyx_kwds
#else
PyObject *__pyx_args, PyObject *__pyx_kwds
#endif
) {
  PyObject *__pyx_v_self = 0;
  #if !CYTHON_METH_FASTCALL
  CYTHON_UNUSED Py_ssize_t __pyx_nargs;
  #endif
  CYTHON_UNUSED PyObject *const *__pyx_kwvalues;
  PyObject *__pyx_r = 0;
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("enter_async (wrapper)", 0);
  #if !CYTHON_METH_FASTCALL
  #if CYTHON_ASSUME_SAFE_SIZE
  __pyx_nargs = PyTuple_GET_SIZE(__pyx_args);
  #else
  __pyx_nargs = PyTuple_Size(__pyx_args); if (unlikely(__pyx_nargs < 0)) return NULL;
  #endif
  #endif
  __pyx_kwvalues = __Pyx_KwValues_FASTCALL(__pyx_args, __pyx_nargs);
  {
    PyObject ** const __pyx_pyargnames[] = {&__pyx_mstate_global->__pyx_n_u_self,0};
  PyObject* values[1] = {0};
    const Py_ssize_t __pyx_kwds_len = (__pyx_kwds) ? __Pyx_NumKwargs_FASTCALL(__pyx_kwds) : 0;
    if (unlikely(__pyx_kwds_len) < 0) __PYX_ERR(0, 631, __pyx_L3_error)
    if (__pyx_kwds_len > 0) {
      switch (__pyx_nargs) {
        case  1:
        values[0] = __Pyx_ArgRef_FASTCALL(__pyx_args, 0);
        if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[0])) __PYX_ERR(0, 631, __pyx_L3_error)
        CYTHON_FALLTHROUGH;
        case  0: break;
        default: goto __pyx_L5_argtuple_error;
      }
      const Py_ssize_t kwd_pos_args = __pyx_nargs;
      if (__Pyx_ParseKeywords(__pyx_kwds, __pyx_kwvalues, __pyx_pyargnames, 0, values, kwd_pos_args, __pyx_kwds_len, "enter_async", 0) < (0)) __PYX_ERR(0, 631, __pyx_L3_error)
      for (Py_ssize_t i = __pyx_nargs; i < 1; i++) {
        if (unlikely(!values[i])) { __Pyx_RaiseArgtupleInvalid("enter_async", 1, 1, 1, i); __PYX_ERR(0, 631, __pyx_L3_error) }
      }
    } else if (unlikely(__pyx_nargs != 1)) {
      goto __pyx_L5_argtuple_error;
    } else {
      values[0] = __Pyx_ArgRef_FASTCALL(__pyx_args, 0);
      if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[0])) __PYX_ERR(0, 631, __pyx_L3_error)
    }
    __pyx_v_self = values[0];
  }
  goto __pyx_L6_skip;
  __pyx_L5_argtuple_error:;
  __Pyx_RaiseArgtupleInvalid("enter_async", 1, 1, 1, __pyx_nargs); __PYX_ERR(0, 631, __pyx_L3_error)
  __pyx_L6_skip:;
  goto __pyx_L4_argument_unpacking_done;
  __pyx_L3_error:;
  for (Py_ssize_t __pyx_temp=0; __pyx_temp < (Py_ssize_t)(sizeof(values)/sizeof(values[0])); ++__pyx_temp) {
    Py_XDECREF(values[__pyx_temp]);
  }
  __Pyx_AddTraceback("Cython.Compiler.Scanning.PyrexScanner.enter_async", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __Pyx_RefNannyFinishContext();
  return NULL;
  __pyx_L4_argument_unpacking_done:;
  __pyx_r = __pyx_pf_6Cython_8Compiler_8Scanning_12PyrexScanner_66enter_async(__pyx_self, __pyx_v_self);
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

static PyObject *__pyx_pf_6Cython_8Compiler_8Scanning_12PyrexScanner_66enter_async(CYTHON_UNUSED PyObject *__pyx_self, PyObject *__pyx_v_self) {
  PyObject *__pyx_r = NULL;
/* … */
  /* function exit code */
  __pyx_r = Py_None; __Pyx_INCREF(Py_None);
  goto __pyx_L0;
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_t_1);
  __Pyx_XDECREF(__pyx_t_2);
  __Pyx_AddTraceback("Cython.Compiler.Scanning.PyrexScanner.enter_async", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_r = NULL;
  __pyx_L0:;
  __Pyx_XGIVEREF(__pyx_r);
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}
/* … */
  __pyx_t_2 = __Pyx_CyFunction_New(&__pyx_mdef_6Cython_8Compiler_8Scanning_12PyrexScanner_67enter_async, 0, __pyx_mstate_global->__pyx_n_u_PyrexScanner_enter_async, NULL, __pyx_mstate_global->__pyx_n_u_Cython_Compiler_Scanning, __pyx_mstate_global->__pyx_d, ((PyObject *)__pyx_mstate_global->__pyx_codeobj_tab[68])); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 631, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  #if CYTHON_COMPILING_IN_CPYTHON && PY_VERSION_HEX >= 0x030E0000
  PyUnstable_Object_EnableDeferredRefcount(__pyx_t_2);
  #endif
  if (__Pyx_SetNameInClass(__pyx_t_8, __pyx_mstate_global->__pyx_n_u_enter_async, __pyx_t_2) < (0)) __PYX_ERR(0, 631, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
```

</details>

L632  🟠  (score=8)
```python
        self.async_enabled += 1
```
<details><summary>Show generated C (score=8)</summary>

```c
  __pyx_t_1 = __Pyx_PyObject_GetAttrStr(__pyx_v_self, __pyx_mstate_global->__pyx_n_u_async_enabled); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 632, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __pyx_t_2 = __Pyx_PyLong_AddObjC(__pyx_t_1, __pyx_mstate_global->__pyx_int_1, 1, 1, 0); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 632, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  if (__Pyx_PyObject_SetAttrStr(__pyx_v_self, __pyx_mstate_global->__pyx_n_u_async_enabled, __pyx_t_2) < (0)) __PYX_ERR(0, 632, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
```

</details>

L633  🟠  (score=5)
```python
        if self.async_enabled == 1:
```
<details><summary>Show generated C (score=5)</summary>

```c
  __pyx_t_2 = __Pyx_PyObject_GetAttrStr(__pyx_v_self, __pyx_mstate_global->__pyx_n_u_async_enabled); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 633, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __pyx_t_3 = (__Pyx_PyLong_BoolEqObjC(__pyx_t_2, __pyx_mstate_global->__pyx_int_1, 1, 0)); if (unlikely((__pyx_t_3 < 0))) __PYX_ERR(0, 633, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  if (__pyx_t_3) {
/* … */
  }
```

</details>

L634  🟠  (score=8)
```python
            self.keywords['async'] = 'async'
```
<details><summary>Show generated C (score=8)</summary>

```c
    __pyx_t_2 = __Pyx_PyObject_GetAttrStr(__pyx_v_self, __pyx_mstate_global->__pyx_n_u_keywords); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 634, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_2);
    if (unlikely((PyObject_SetItem(__pyx_t_2, __pyx_mstate_global->__pyx_n_u_async, __pyx_mstate_global->__pyx_n_u_async) < 0))) __PYX_ERR(0, 634, __pyx_L1_error)
    __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
```

</details>

L635  🟠  (score=8)
```python
            self.keywords['await'] = 'await'
```
<details><summary>Show generated C (score=8)</summary>

```c
    __pyx_t_2 = __Pyx_PyObject_GetAttrStr(__pyx_v_self, __pyx_mstate_global->__pyx_n_u_keywords); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 635, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_2);
    if (unlikely((PyObject_SetItem(__pyx_t_2, __pyx_mstate_global->__pyx_n_u_await, __pyx_mstate_global->__pyx_n_u_await) < 0))) __PYX_ERR(0, 635, __pyx_L1_error)
    __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
```

</details>

L636  ⚪  (score=0)
```python
```
L637  🔴  (score=41)
```python
    def exit_async(self):
```
<details><summary>Show generated C (score=41)</summary>

```c
/* Python wrapper */
static PyObject *__pyx_pw_6Cython_8Compiler_8Scanning_12PyrexScanner_69exit_async(PyObject *__pyx_self, 
#if CYTHON_METH_FASTCALL
PyObject *const *__pyx_args, Py_ssize_t __pyx_nargs, PyObject *__pyx_kwds
#else
PyObject *__pyx_args, PyObject *__pyx_kwds
#endif
); /*proto*/
PyDoc_STRVAR(__pyx_doc_6Cython_8Compiler_8Scanning_12PyrexScanner_68exit_async, "File: Cython/Compiler/Scanning.py (starting at line 637)");
static PyMethodDef __pyx_mdef_6Cython_8Compiler_8Scanning_12PyrexScanner_69exit_async = {"exit_async", (PyCFunction)(void(*)(void))(__Pyx_PyCFunction_FastCallWithKeywords)__pyx_pw_6Cython_8Compiler_8Scanning_12PyrexScanner_69exit_async, __Pyx_METH_FASTCALL|METH_KEYWORDS, __pyx_doc_6Cython_8Compiler_8Scanning_12PyrexScanner_68exit_async};
static PyObject *__pyx_pw_6Cython_8Compiler_8Scanning_12PyrexScanner_69exit_async(PyObject *__pyx_self, 
#if CYTHON_METH_FASTCALL
PyObject *const *__pyx_args, Py_ssize_t __pyx_nargs, PyObject *__pyx_kwds
#else
PyObject *__pyx_args, PyObject *__pyx_kwds
#endif
) {
  PyObject *__pyx_v_self = 0;
  #if !CYTHON_METH_FASTCALL
  CYTHON_UNUSED Py_ssize_t __pyx_nargs;
  #endif
  CYTHON_UNUSED PyObject *const *__pyx_kwvalues;
  PyObject *__pyx_r = 0;
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("exit_async (wrapper)", 0);
  #if !CYTHON_METH_FASTCALL
  #if CYTHON_ASSUME_SAFE_SIZE
  __pyx_nargs = PyTuple_GET_SIZE(__pyx_args);
  #else
  __pyx_nargs = PyTuple_Size(__pyx_args); if (unlikely(__pyx_nargs < 0)) return NULL;
  #endif
  #endif
  __pyx_kwvalues = __Pyx_KwValues_FASTCALL(__pyx_args, __pyx_nargs);
  {
    PyObject ** const __pyx_pyargnames[] = {&__pyx_mstate_global->__pyx_n_u_self,0};
  PyObject* values[1] = {0};
    const Py_ssize_t __pyx_kwds_len = (__pyx_kwds) ? __Pyx_NumKwargs_FASTCALL(__pyx_kwds) : 0;
    if (unlikely(__pyx_kwds_len) < 0) __PYX_ERR(0, 637, __pyx_L3_error)
    if (__pyx_kwds_len > 0) {
      switch (__pyx_nargs) {
        case  1:
        values[0] = __Pyx_ArgRef_FASTCALL(__pyx_args, 0);
        if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[0])) __PYX_ERR(0, 637, __pyx_L3_error)
        CYTHON_FALLTHROUGH;
        case  0: break;
        default: goto __pyx_L5_argtuple_error;
      }
      const Py_ssize_t kwd_pos_args = __pyx_nargs;
      if (__Pyx_ParseKeywords(__pyx_kwds, __pyx_kwvalues, __pyx_pyargnames, 0, values, kwd_pos_args, __pyx_kwds_len, "exit_async", 0) < (0)) __PYX_ERR(0, 637, __pyx_L3_error)
      for (Py_ssize_t i = __pyx_nargs; i < 1; i++) {
        if (unlikely(!values[i])) { __Pyx_RaiseArgtupleInvalid("exit_async", 1, 1, 1, i); __PYX_ERR(0, 637, __pyx_L3_error) }
      }
    } else if (unlikely(__pyx_nargs != 1)) {
      goto __pyx_L5_argtuple_error;
    } else {
      values[0] = __Pyx_ArgRef_FASTCALL(__pyx_args, 0);
      if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[0])) __PYX_ERR(0, 637, __pyx_L3_error)
    }
    __pyx_v_self = values[0];
  }
  goto __pyx_L6_skip;
  __pyx_L5_argtuple_error:;
  __Pyx_RaiseArgtupleInvalid("exit_async", 1, 1, 1, __pyx_nargs); __PYX_ERR(0, 637, __pyx_L3_error)
  __pyx_L6_skip:;
  goto __pyx_L4_argument_unpacking_done;
  __pyx_L3_error:;
  for (Py_ssize_t __pyx_temp=0; __pyx_temp < (Py_ssize_t)(sizeof(values)/sizeof(values[0])); ++__pyx_temp) {
    Py_XDECREF(values[__pyx_temp]);
  }
  __Pyx_AddTraceback("Cython.Compiler.Scanning.PyrexScanner.exit_async", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __Pyx_RefNannyFinishContext();
  return NULL;
  __pyx_L4_argument_unpacking_done:;
  __pyx_r = __pyx_pf_6Cython_8Compiler_8Scanning_12PyrexScanner_68exit_async(__pyx_self, __pyx_v_self);
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

static PyObject *__pyx_pf_6Cython_8Compiler_8Scanning_12PyrexScanner_68exit_async(CYTHON_UNUSED PyObject *__pyx_self, PyObject *__pyx_v_self) {
  PyObject *__pyx_r = NULL;
/* … */
  /* function exit code */
  __pyx_r = Py_None; __Pyx_INCREF(Py_None);
  goto __pyx_L0;
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_t_1);
  __Pyx_XDECREF(__pyx_t_2);
  __Pyx_XDECREF(__pyx_t_5);
  __Pyx_XDECREF(__pyx_t_6);
  __Pyx_XDECREF(__pyx_t_7);
  __Pyx_AddTraceback("Cython.Compiler.Scanning.PyrexScanner.exit_async", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_r = NULL;
  __pyx_L0:;
  __Pyx_XGIVEREF(__pyx_r);
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}
static PyObject *__pyx_gb_6Cython_8Compiler_8Scanning_6generator(__pyx_CoroutineObject *__pyx_generator, CYTHON_UNUSED PyThreadState *__pyx_tstate, PyObject *__pyx_sent_value); /* proto */
/* … */
  __pyx_t_2 = __Pyx_CyFunction_New(&__pyx_mdef_6Cython_8Compiler_8Scanning_12PyrexScanner_69exit_async, 0, __pyx_mstate_global->__pyx_n_u_PyrexScanner_exit_async, NULL, __pyx_mstate_global->__pyx_n_u_Cython_Compiler_Scanning, __pyx_mstate_global->__pyx_d, ((PyObject *)__pyx_mstate_global->__pyx_codeobj_tab[69])); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 637, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  #if CYTHON_COMPILING_IN_CPYTHON && PY_VERSION_HEX >= 0x030E0000
  PyUnstable_Object_EnableDeferredRefcount(__pyx_t_2);
  #endif
  if (__Pyx_SetNameInClass(__pyx_t_8, __pyx_mstate_global->__pyx_n_u_exit_async, __pyx_t_2) < (0)) __PYX_ERR(0, 637, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
```

</details>

L638  🔴  (score=13)
```python
        assert self.async_enabled > 0
```
<details><summary>Show generated C (score=13)</summary>

```c
  #ifndef CYTHON_WITHOUT_ASSERTIONS
  if (unlikely(__pyx_assertions_enabled())) {
    __pyx_t_1 = __Pyx_PyObject_GetAttrStr(__pyx_v_self, __pyx_mstate_global->__pyx_n_u_async_enabled); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 638, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_1);
    __pyx_t_2 = PyObject_RichCompare(__pyx_t_1, __pyx_mstate_global->__pyx_int_0, Py_GT); __Pyx_XGOTREF(__pyx_t_2); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 638, __pyx_L1_error)
    __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
    __pyx_t_3 = __Pyx_PyObject_IsTrue(__pyx_t_2); if (unlikely((__pyx_t_3 < 0))) __PYX_ERR(0, 638, __pyx_L1_error)
    __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
    if (unlikely(!__pyx_t_3)) {
      __Pyx_Raise(((PyObject *)(((PyTypeObject*)PyExc_AssertionError))), 0, 0, 0);
      __PYX_ERR(0, 638, __pyx_L1_error)
    }
  }
  #else
  if ((1)); else __PYX_ERR(0, 638, __pyx_L1_error)
  #endif
```

</details>

L639  🟠  (score=8)
```python
        self.async_enabled -= 1
```
<details><summary>Show generated C (score=8)</summary>

```c
  __pyx_t_2 = __Pyx_PyObject_GetAttrStr(__pyx_v_self, __pyx_mstate_global->__pyx_n_u_async_enabled); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 639, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __pyx_t_1 = __Pyx_PyLong_SubtractObjC(__pyx_t_2, __pyx_mstate_global->__pyx_int_1, 1, 1, 0); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 639, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  if (__Pyx_PyObject_SetAttrStr(__pyx_v_self, __pyx_mstate_global->__pyx_n_u_async_enabled, __pyx_t_1) < (0)) __PYX_ERR(0, 639, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
```

</details>

L640  🟠  (score=5)
```python
        if not self.async_enabled:
```
<details><summary>Show generated C (score=5)</summary>

```c
  __pyx_t_1 = __Pyx_PyObject_GetAttrStr(__pyx_v_self, __pyx_mstate_global->__pyx_n_u_async_enabled); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 640, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __pyx_t_3 = __Pyx_PyObject_IsTrue(__pyx_t_1); if (unlikely((__pyx_t_3 < 0))) __PYX_ERR(0, 640, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __pyx_t_4 = (!__pyx_t_3);
  if (__pyx_t_4) {
/* … */
  }
```

</details>

L641  🟠  (score=8)
```python
            del self.keywords['await']
```
<details><summary>Show generated C (score=8)</summary>

```c
    __pyx_t_1 = __Pyx_PyObject_GetAttrStr(__pyx_v_self, __pyx_mstate_global->__pyx_n_u_keywords); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 641, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_1);
    if (unlikely((PyObject_DelItem(__pyx_t_1, __pyx_mstate_global->__pyx_n_u_await) < 0))) __PYX_ERR(0, 641, __pyx_L1_error)
    __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
```

</details>

L642  🟠  (score=8)
```python
            del self.keywords['async']
```
<details><summary>Show generated C (score=8)</summary>

```c
    __pyx_t_1 = __Pyx_PyObject_GetAttrStr(__pyx_v_self, __pyx_mstate_global->__pyx_n_u_keywords); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 642, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_1);
    if (unlikely((PyObject_DelItem(__pyx_t_1, __pyx_mstate_global->__pyx_n_u_async) < 0))) __PYX_ERR(0, 642, __pyx_L1_error)
    __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
```

</details>

L643  🟠  (score=7)
```python
            if self.sy in ('async', 'await'):
```
<details><summary>Show generated C (score=7)</summary>

```c
    __pyx_t_1 = __Pyx_PyObject_GetAttrStr(__pyx_v_self, __pyx_mstate_global->__pyx_n_u_sy); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 643, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_1);
    __pyx_t_3 = (__Pyx_PyUnicode_Equals(__pyx_t_1, __pyx_mstate_global->__pyx_n_u_async, Py_EQ)); if (unlikely((__pyx_t_3 < 0))) __PYX_ERR(0, 643, __pyx_L1_error)
    if (!__pyx_t_3) {
    } else {
      __pyx_t_4 = __pyx_t_3;
      goto __pyx_L5_bool_binop_done;
    }
    __pyx_t_3 = (__Pyx_PyUnicode_Equals(__pyx_t_1, __pyx_mstate_global->__pyx_n_u_await, Py_EQ)); if (unlikely((__pyx_t_3 < 0))) __PYX_ERR(0, 643, __pyx_L1_error)
    __pyx_t_4 = __pyx_t_3;
    __pyx_L5_bool_binop_done:;
    __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
    __pyx_t_3 = __pyx_t_4;
    if (__pyx_t_3) {
/* … */
    }
```

</details>

L644  🔴  (score=18)
```python
                self.sy, self.systring = IDENT, self.context.intern_ustring(self.sy)
```
<details><summary>Show generated C (score=18)</summary>

```c
      __Pyx_GetModuleGlobalName(__pyx_t_1, __pyx_mstate_global->__pyx_n_u_IDENT); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 644, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_1);
      __pyx_t_6 = __Pyx_PyObject_GetAttrStr(__pyx_v_self, __pyx_mstate_global->__pyx_n_u_context); if (unlikely(!__pyx_t_6)) __PYX_ERR(0, 644, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_6);
      __pyx_t_5 = __pyx_t_6;
      __Pyx_INCREF(__pyx_t_5);
      __pyx_t_7 = __Pyx_PyObject_GetAttrStr(__pyx_v_self, __pyx_mstate_global->__pyx_n_u_sy); if (unlikely(!__pyx_t_7)) __PYX_ERR(0, 644, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_7);
      __pyx_t_8 = 0;
      {
        PyObject *__pyx_callargs[2] = {__pyx_t_5, __pyx_t_7};
        __pyx_t_2 = __Pyx_PyObject_FastCallMethod((PyObject*)__pyx_mstate_global->__pyx_n_u_intern_ustring, __pyx_callargs+__pyx_t_8, (2-__pyx_t_8) | (1*__Pyx_PY_VECTORCALL_ARGUMENTS_OFFSET));
        __Pyx_XDECREF(__pyx_t_5); __pyx_t_5 = 0;
        __Pyx_DECREF(__pyx_t_7); __pyx_t_7 = 0;
        __Pyx_DECREF(__pyx_t_6); __pyx_t_6 = 0;
        if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 644, __pyx_L1_error)
        __Pyx_GOTREF(__pyx_t_2);
      }
      if (__Pyx_PyObject_SetAttrStr(__pyx_v_self, __pyx_mstate_global->__pyx_n_u_sy, __pyx_t_1) < (0)) __PYX_ERR(0, 644, __pyx_L1_error)
      __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
      if (__Pyx_PyObject_SetAttrStr(__pyx_v_self, __pyx_mstate_global->__pyx_n_u_systring, __pyx_t_2) < (0)) __PYX_ERR(0, 644, __pyx_L1_error)
      __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
```

</details>

L645  ⚪  (score=0)
```python
```
L646  🔴  (score=101)
```python
@contextmanager
```
<details><summary>Show generated C (score=101)</summary>

```c
/* Python wrapper */
static PyObject *__pyx_pw_6Cython_8Compiler_8Scanning_5tentatively_scan(PyObject *__pyx_self, 
#if CYTHON_METH_FASTCALL
PyObject *const *__pyx_args, Py_ssize_t __pyx_nargs, PyObject *__pyx_kwds
#else
PyObject *__pyx_args, PyObject *__pyx_kwds
#endif
); /*proto*/
PyDoc_STRVAR(__pyx_doc_6Cython_8Compiler_8Scanning_4tentatively_scan, "File: Cython/Compiler/Scanning.py (starting at line 646)");
static PyMethodDef __pyx_mdef_6Cython_8Compiler_8Scanning_5tentatively_scan = {"tentatively_scan", (PyCFunction)(void(*)(void))(__Pyx_PyCFunction_FastCallWithKeywords)__pyx_pw_6Cython_8Compiler_8Scanning_5tentatively_scan, __Pyx_METH_FASTCALL|METH_KEYWORDS, __pyx_doc_6Cython_8Compiler_8Scanning_4tentatively_scan};
static PyObject *__pyx_pw_6Cython_8Compiler_8Scanning_5tentatively_scan(PyObject *__pyx_self, 
#if CYTHON_METH_FASTCALL
PyObject *const *__pyx_args, Py_ssize_t __pyx_nargs, PyObject *__pyx_kwds
#else
PyObject *__pyx_args, PyObject *__pyx_kwds
#endif
) {
  PyObject *__pyx_v_scanner = 0;
  #if !CYTHON_METH_FASTCALL
  CYTHON_UNUSED Py_ssize_t __pyx_nargs;
  #endif
  CYTHON_UNUSED PyObject *const *__pyx_kwvalues;
  PyObject *__pyx_r = 0;
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("tentatively_scan (wrapper)", 0);
  #if !CYTHON_METH_FASTCALL
  #if CYTHON_ASSUME_SAFE_SIZE
  __pyx_nargs = PyTuple_GET_SIZE(__pyx_args);
  #else
  __pyx_nargs = PyTuple_Size(__pyx_args); if (unlikely(__pyx_nargs < 0)) return NULL;
  #endif
  #endif
  __pyx_kwvalues = __Pyx_KwValues_FASTCALL(__pyx_args, __pyx_nargs);
  {
    PyObject ** const __pyx_pyargnames[] = {&__pyx_mstate_global->__pyx_n_u_scanner,0};
  PyObject* values[1] = {0};
    const Py_ssize_t __pyx_kwds_len = (__pyx_kwds) ? __Pyx_NumKwargs_FASTCALL(__pyx_kwds) : 0;
    if (unlikely(__pyx_kwds_len) < 0) __PYX_ERR(0, 646, __pyx_L3_error)
    if (__pyx_kwds_len > 0) {
      switch (__pyx_nargs) {
        case  1:
        values[0] = __Pyx_ArgRef_FASTCALL(__pyx_args, 0);
        if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[0])) __PYX_ERR(0, 646, __pyx_L3_error)
        CYTHON_FALLTHROUGH;
        case  0: break;
        default: goto __pyx_L5_argtuple_error;
      }
      const Py_ssize_t kwd_pos_args = __pyx_nargs;
      if (__Pyx_ParseKeywords(__pyx_kwds, __pyx_kwvalues, __pyx_pyargnames, 0, values, kwd_pos_args, __pyx_kwds_len, "tentatively_scan", 0) < (0)) __PYX_ERR(0, 646, __pyx_L3_error)
      for (Py_ssize_t i = __pyx_nargs; i < 1; i++) {
        if (unlikely(!values[i])) { __Pyx_RaiseArgtupleInvalid("tentatively_scan", 1, 1, 1, i); __PYX_ERR(0, 646, __pyx_L3_error) }
      }
    } else if (unlikely(__pyx_nargs != 1)) {
      goto __pyx_L5_argtuple_error;
    } else {
      values[0] = __Pyx_ArgRef_FASTCALL(__pyx_args, 0);
      if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[0])) __PYX_ERR(0, 646, __pyx_L3_error)
    }
    __pyx_v_scanner = values[0];
  }
  goto __pyx_L6_skip;
  __pyx_L5_argtuple_error:;
  __Pyx_RaiseArgtupleInvalid("tentatively_scan", 1, 1, 1, __pyx_nargs); __PYX_ERR(0, 646, __pyx_L3_error)
  __pyx_L6_skip:;
  goto __pyx_L4_argument_unpacking_done;
  __pyx_L3_error:;
  for (Py_ssize_t __pyx_temp=0; __pyx_temp < (Py_ssize_t)(sizeof(values)/sizeof(values[0])); ++__pyx_temp) {
    Py_XDECREF(values[__pyx_temp]);
  }
  __Pyx_AddTraceback("Cython.Compiler.Scanning.tentatively_scan", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __Pyx_RefNannyFinishContext();
  return NULL;
  __pyx_L4_argument_unpacking_done:;
  __pyx_r = __pyx_pf_6Cython_8Compiler_8Scanning_4tentatively_scan(__pyx_self, __pyx_v_scanner);
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

static PyObject *__pyx_pf_6Cython_8Compiler_8Scanning_4tentatively_scan(CYTHON_UNUSED PyObject *__pyx_self, PyObject *__pyx_v_scanner) {
  struct __pyx_obj_6Cython_8Compiler_8Scanning___pyx_scope_struct__tentatively_scan *__pyx_cur_scope;
  PyObject *__pyx_r = NULL;
  __pyx_cur_scope = (struct __pyx_obj_6Cython_8Compiler_8Scanning___pyx_scope_struct__tentatively_scan *)__pyx_tp_new_6Cython_8Compiler_8Scanning___pyx_scope_struct__tentatively_scan(__pyx_mstate_global->__pyx_ptype_6Cython_8Compiler_8Scanning___pyx_scope_struct__tentatively_scan, __pyx_mstate_global->__pyx_empty_tuple, NULL);
  if (unlikely(!__pyx_cur_scope)) {
    __pyx_cur_scope = ((struct __pyx_obj_6Cython_8Compiler_8Scanning___pyx_scope_struct__tentatively_scan *)Py_None);
    __Pyx_INCREF(Py_None);
    __PYX_ERR(0, 646, __pyx_L1_error)
  } else {
    __Pyx_GOTREF((PyObject *)__pyx_cur_scope);
  }
  __pyx_cur_scope->__pyx_v_scanner = __pyx_v_scanner;
  __Pyx_INCREF(__pyx_cur_scope->__pyx_v_scanner);
  __Pyx_GIVEREF(__pyx_cur_scope->__pyx_v_scanner);
  {
    __pyx_CoroutineObject *gen = __Pyx_Generator_New((__pyx_coroutine_body_t) __pyx_gb_6Cython_8Compiler_8Scanning_6generator, ((PyObject *)__pyx_mstate_global->__pyx_codeobj_tab[0]), (PyObject *) __pyx_cur_scope, __pyx_mstate_global->__pyx_n_u_tentatively_scan, __pyx_mstate_global->__pyx_n_u_tentatively_scan, __pyx_mstate_global->__pyx_n_u_Cython_Compiler_Scanning); if (unlikely(!gen)) __PYX_ERR(0, 646, __pyx_L1_error)
    __Pyx_DECREF(__pyx_cur_scope);
    __Pyx_RefNannyFinishContext();
    return (PyObject *) gen;
  }

  /* function exit code */
  __pyx_L1_error:;
  __Pyx_AddTraceback("Cython.Compiler.Scanning.tentatively_scan", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_r = NULL;
  __Pyx_DECREF((PyObject *)__pyx_cur_scope);
  __Pyx_XGIVEREF(__pyx_r);
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}

static PyObject *__pyx_gb_6Cython_8Compiler_8Scanning_6generator(__pyx_CoroutineObject *__pyx_generator, CYTHON_UNUSED PyThreadState *__pyx_tstate, PyObject *__pyx_sent_value) /* generator body */
{
  PyObject *__pyx_r = NULL;
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("tentatively_scan", 0);
  __pyx_L3_first_run:;
  if (unlikely(__pyx_sent_value != Py_None)) {
    if (unlikely(__pyx_sent_value)) PyErr_SetString(PyExc_TypeError, "can't send non-None value to a just-started generator");
    __PYX_ERR(0, 646, __pyx_L1_error)
  }
/* … */
  /* function exit code */
  __pyx_r = Py_None; __Pyx_INCREF(Py_None);
  goto __pyx_L0;
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_t_1);
  __Pyx_XDECREF(__pyx_t_2);
  __Pyx_XDECREF(__pyx_t_3);
  __Pyx_XDECREF(__pyx_t_5);
  if (__Pyx_PyErr_Occurred()) {
    __Pyx_Generator_Replace_StopIteration(0);
    __Pyx_AddTraceback("tentatively_scan", __pyx_clineno, __pyx_lineno, __pyx_filename);
  }
  __pyx_L0:;
  __Pyx_XGIVEREF(__pyx_r);
  #if !CYTHON_USE_EXC_INFO_STACK
  __Pyx_Coroutine_ResetAndClearException(__pyx_generator);
  #endif
  __pyx_generator->resume_label = -1;
  __Pyx_Coroutine_clear((PyObject*)__pyx_generator);
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}
/* … */
  __pyx_t_6 = NULL;
  __Pyx_GetModuleGlobalName(__pyx_t_8, __pyx_mstate_global->__pyx_n_u_contextmanager); if (unlikely(!__pyx_t_8)) __PYX_ERR(0, 646, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_8);
  __pyx_t_2 = __Pyx_PyDict_NewPresized(1); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 646, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  #if defined(PyDict_SetItem) && (defined(CYTHON_COMPILING_IN_CPYTHON))
  #if PY_VERSION_HEX >= 0x030A0000 /* CPython 3.10+ exposes KnownHash APIs */
  /* Use CPython's KnownHash APIs when available */
  extern int _PyDict_SetItem_KnownHash(PyObject*, PyObject*, PyObject*, Py_hash_t);
  {
    Py_hash_t __pyx_hash = PyObject_Hash(__pyx_mstate_global->__pyx_n_u_scanner); if (unlikely(__pyx_hash == -1)) __PYX_ERR(0, 646, __pyx_L1_error);
    if (unlikely(_PyDict_SetItem_KnownHash(__pyx_t_2, __pyx_mstate_global->__pyx_n_u_scanner, __pyx_mstate_global->__pyx_n_u_PyrexScanner, __pyx_hash) < 0)) __PYX_ERR(0, 646, __pyx_L1_error);
  }
  #else
  if (PyDict_SetItem(__pyx_t_2, __pyx_mstate_global->__pyx_n_u_scanner, __pyx_mstate_global->__pyx_n_u_PyrexScanner) < (0)) __PYX_ERR(0, 646, __pyx_L1_error)
  #endif
  #else
  if (PyDict_SetItem(__pyx_t_2, __pyx_mstate_global->__pyx_n_u_scanner, __pyx_mstate_global->__pyx_n_u_PyrexScanner) < (0)) __PYX_ERR(0, 646, __pyx_L1_error)
  #endif
  __pyx_t_9 = __Pyx_CyFunction_New(&__pyx_mdef_6Cython_8Compiler_8Scanning_5tentatively_scan, 0, __pyx_mstate_global->__pyx_n_u_tentatively_scan, NULL, __pyx_mstate_global->__pyx_n_u_Cython_Compiler_Scanning, __pyx_mstate_global->__pyx_d, ((PyObject *)__pyx_mstate_global->__pyx_codeobj_tab[0])); if (unlikely(!__pyx_t_9)) __PYX_ERR(0, 646, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_9);
  #if CYTHON_COMPILING_IN_CPYTHON && PY_VERSION_HEX >= 0x030E0000
  PyUnstable_Object_EnableDeferredRefcount(__pyx_t_9);
  #endif
  __Pyx_CyFunction_SetAnnotationsDict(__pyx_t_9, __pyx_t_2);
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __pyx_t_10 = 1;
  {
    PyObject *__pyx_callargs[2] = {__pyx_t_6, __pyx_t_9};
    __pyx_t_4 = __Pyx_PyObject_FastCall((PyObject*)__pyx_t_8, __pyx_callargs+__pyx_t_10, (2-__pyx_t_10) | (__pyx_t_10*__Pyx_PY_VECTORCALL_ARGUMENTS_OFFSET));
    __Pyx_XDECREF(__pyx_t_6); __pyx_t_6 = 0;
    __Pyx_DECREF(__pyx_t_9); __pyx_t_9 = 0;
    __Pyx_DECREF(__pyx_t_8); __pyx_t_8 = 0;
    if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 646, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_4);
  }
  if (PyDict_SetItem(__pyx_mstate_global->__pyx_d, __pyx_mstate_global->__pyx_n_u_tentatively_scan, __pyx_t_4) < (0)) __PYX_ERR(0, 646, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
```

</details>

L647  ⚪  (score=0)
```python
def tentatively_scan(scanner: PyrexScanner):
```
L648  🟠  (score=6)
```python
    errors = hold_errors()
```
<details><summary>Show generated C (score=6)</summary>

```c
  __pyx_t_2 = NULL;
  __Pyx_GetModuleGlobalName(__pyx_t_3, __pyx_mstate_global->__pyx_n_u_hold_errors); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 648, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_3);
  __pyx_t_4 = 1;
  {
    PyObject *__pyx_callargs[2] = {__pyx_t_2, NULL};
    __pyx_t_1 = __Pyx_PyObject_FastCall((PyObject*)__pyx_t_3, __pyx_callargs+__pyx_t_4, (1-__pyx_t_4) | (__pyx_t_4*__Pyx_PY_VECTORCALL_ARGUMENTS_OFFSET));
    __Pyx_XDECREF(__pyx_t_2); __pyx_t_2 = 0;
    __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
    if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 648, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_1);
  }
  __Pyx_GIVEREF(__pyx_t_1);
  __pyx_cur_scope->__pyx_v_errors = __pyx_t_1;
  __pyx_t_1 = 0;
```

</details>

L649  ⚪  (score=0)
```python
    try:
```
<details><summary>Show generated C (score=0)</summary>

```c
  /*try:*/ {
```

</details>

L650  🟡  (score=2)
```python
        put_back_on_failure = scanner.put_back_on_failure
```
<details><summary>Show generated C (score=2)</summary>

```c
    __pyx_t_1 = __Pyx_PyObject_GetAttrStr(__pyx_cur_scope->__pyx_v_scanner, __pyx_mstate_global->__pyx_n_u_put_back_on_failure); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 650, __pyx_L5_error)
    __Pyx_GOTREF(__pyx_t_1);
    __Pyx_GIVEREF(__pyx_t_1);
    __pyx_cur_scope->__pyx_v_put_back_on_failure = __pyx_t_1;
    __pyx_t_1 = 0;
```

</details>

L651  🟠  (score=8)
```python
        scanner.put_back_on_failure = []
```
<details><summary>Show generated C (score=8)</summary>

```c
    __pyx_t_1 = PyList_New(0); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 651, __pyx_L5_error)
    __Pyx_GOTREF(__pyx_t_1);
    if (__Pyx_PyObject_SetAttrStr(__pyx_cur_scope->__pyx_v_scanner, __pyx_mstate_global->__pyx_n_u_put_back_on_failure, __pyx_t_1) < (0)) __PYX_ERR(0, 651, __pyx_L5_error)
    __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
```

</details>

L652  🔴  (score=19)
```python
        initial_state = (scanner.sy, scanner.systring, scanner.position())
```
<details><summary>Show generated C (score=19)</summary>

```c
    __pyx_t_1 = __Pyx_PyObject_GetAttrStr(__pyx_cur_scope->__pyx_v_scanner, __pyx_mstate_global->__pyx_n_u_sy); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 652, __pyx_L5_error)
    __Pyx_GOTREF(__pyx_t_1);
    __pyx_t_3 = __Pyx_PyObject_GetAttrStr(__pyx_cur_scope->__pyx_v_scanner, __pyx_mstate_global->__pyx_n_u_systring); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 652, __pyx_L5_error)
    __Pyx_GOTREF(__pyx_t_3);
    __pyx_t_5 = __pyx_cur_scope->__pyx_v_scanner;
    __Pyx_INCREF(__pyx_t_5);
    __pyx_t_4 = 0;
    {
      PyObject *__pyx_callargs[2] = {__pyx_t_5, NULL};
      __pyx_t_2 = __Pyx_PyObject_FastCallMethod((PyObject*)__pyx_mstate_global->__pyx_n_u_position, __pyx_callargs+__pyx_t_4, (1-__pyx_t_4) | (1*__Pyx_PY_VECTORCALL_ARGUMENTS_OFFSET));
      __Pyx_XDECREF(__pyx_t_5); __pyx_t_5 = 0;
      if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 652, __pyx_L5_error)
      __Pyx_GOTREF(__pyx_t_2);
    }
    __pyx_t_5 = PyTuple_New(3); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 652, __pyx_L5_error)
    __Pyx_GOTREF(__pyx_t_5);
    __Pyx_GIVEREF(__pyx_t_1);
    if (__Pyx_PyTuple_SET_ITEM(__pyx_t_5, 0, __pyx_t_1) != (0)) __PYX_ERR(0, 652, __pyx_L5_error);
    __Pyx_GIVEREF(__pyx_t_3);
    if (__Pyx_PyTuple_SET_ITEM(__pyx_t_5, 1, __pyx_t_3) != (0)) __PYX_ERR(0, 652, __pyx_L5_error);
    __Pyx_GIVEREF(__pyx_t_2);
    if (__Pyx_PyTuple_SET_ITEM(__pyx_t_5, 2, __pyx_t_2) != (0)) __PYX_ERR(0, 652, __pyx_L5_error);
    __pyx_t_1 = 0;
    __pyx_t_3 = 0;
    __pyx_t_2 = 0;
    __Pyx_GIVEREF(__pyx_t_5);
    __pyx_cur_scope->__pyx_v_initial_state = __pyx_t_5;
    __pyx_t_5 = 0;
```

</details>

L653  🔴  (score=11)
```python
        try:
```
<details><summary>Show generated C (score=11)</summary>

```c
    /*try:*/ {
      {
        /*try:*/ {
/* … */
        }
        __Pyx_XDECREF(__pyx_t_6); __pyx_t_6 = 0;
        __Pyx_XDECREF(__pyx_t_7); __pyx_t_7 = 0;
        __Pyx_XDECREF(__pyx_t_8); __pyx_t_8 = 0;
        goto __pyx_L15_try_end;
        __pyx_L10_error:;
        __Pyx_XDECREF(__pyx_t_1); __pyx_t_1 = 0;
        __Pyx_XDECREF(__pyx_t_2); __pyx_t_2 = 0;
        __Pyx_XDECREF(__pyx_t_3); __pyx_t_3 = 0;
        __Pyx_XDECREF(__pyx_t_5); __pyx_t_5 = 0;
/* … */
        __pyx_L12_except_error:;
        __Pyx_XGIVEREF(__pyx_t_6);
        __Pyx_XGIVEREF(__pyx_t_7);
        __Pyx_XGIVEREF(__pyx_t_8);
        __Pyx_ExceptionReset(__pyx_t_6, __pyx_t_7, __pyx_t_8);
        goto __pyx_L8_error;
        __pyx_L11_exception_handled:;
        __Pyx_XGIVEREF(__pyx_t_6);
        __Pyx_XGIVEREF(__pyx_t_7);
        __Pyx_XGIVEREF(__pyx_t_8);
        __Pyx_ExceptionReset(__pyx_t_6, __pyx_t_7, __pyx_t_8);
        __pyx_L15_try_end:;
      }
    }
```

</details>

L654  🟡  (score=3)
```python
            yield errors
```
<details><summary>Show generated C (score=3)</summary>

```c
          __Pyx_INCREF(__pyx_cur_scope->__pyx_v_errors);
          __pyx_r = __pyx_cur_scope->__pyx_v_errors;
          __Pyx_XGIVEREF(__pyx_t_6);
          __pyx_cur_scope->__pyx_t_0 = __pyx_t_6;
          __Pyx_XGIVEREF(__pyx_t_7);
          __pyx_cur_scope->__pyx_t_1 = __pyx_t_7;
          __Pyx_XGIVEREF(__pyx_t_8);
          __pyx_cur_scope->__pyx_t_2 = __pyx_t_8;
          __Pyx_XGIVEREF(__pyx_r);
          __Pyx_RefNannyFinishContext();
          __Pyx_Coroutine_ResetAndClearException(__pyx_generator);
          /* return from generator, yielding value */
          __pyx_generator->resume_label = 1;
          return __pyx_r;
          __pyx_L16_resume_from_yield:;
          __pyx_t_6 = __pyx_cur_scope->__pyx_t_0;
          __pyx_cur_scope->__pyx_t_0 = 0;
          __Pyx_XGOTREF(__pyx_t_6);
          __pyx_t_7 = __pyx_cur_scope->__pyx_t_1;
          __pyx_cur_scope->__pyx_t_1 = 0;
          __Pyx_XGOTREF(__pyx_t_7);
          __pyx_t_8 = __pyx_cur_scope->__pyx_t_2;
          __pyx_cur_scope->__pyx_t_2 = 0;
          __Pyx_XGOTREF(__pyx_t_8);
          if (unlikely(!__pyx_sent_value)) __PYX_ERR(0, 654, __pyx_L10_error)
```

</details>

L655  🔴  (score=18)
```python
        except CompileError as e:
```
<details><summary>Show generated C (score=18)</summary>

```c
        __Pyx_ErrFetch(&__pyx_t_5, &__pyx_t_2, &__pyx_t_3);
        __Pyx_GetModuleGlobalName(__pyx_t_1, __pyx_mstate_global->__pyx_n_u_CompileError); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 655, __pyx_L12_except_error)
        __Pyx_GOTREF(__pyx_t_1);
        __pyx_t_9 = __Pyx_PyErr_GivenExceptionMatches(__pyx_t_5, __pyx_t_1);
        __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
        __Pyx_ErrRestore(__pyx_t_5, __pyx_t_2, __pyx_t_3);
        __pyx_t_5 = 0; __pyx_t_2 = 0; __pyx_t_3 = 0;
        if (__pyx_t_9) {
          __Pyx_AddTraceback("Cython.Compiler.Scanning.tentatively_scan", __pyx_clineno, __pyx_lineno, __pyx_filename);
          if (__Pyx_GetException(&__pyx_t_3, &__pyx_t_2, &__pyx_t_5) < 0) __PYX_ERR(0, 655, __pyx_L12_except_error)
          __Pyx_XGOTREF(__pyx_t_3);
          __Pyx_XGOTREF(__pyx_t_2);
          __Pyx_XGOTREF(__pyx_t_5);
          __Pyx_INCREF(__pyx_t_2);
          __Pyx_GIVEREF(__pyx_t_2);
          __pyx_cur_scope->__pyx_v_e = __pyx_t_2;
          /*try:*/ {
          }
          /*finally:*/ {
            /*normal exit:*/{
              __Pyx_GOTREF(__pyx_cur_scope->__pyx_v_e);
              __Pyx_DECREF(__pyx_cur_scope->__pyx_v_e); __pyx_cur_scope->__pyx_v_e = 0;
              goto __pyx_L23;
            }
            __pyx_L23:;
          }
          __Pyx_XDECREF(__pyx_t_3); __pyx_t_3 = 0;
          __Pyx_XDECREF(__pyx_t_2); __pyx_t_2 = 0;
          __Pyx_XDECREF(__pyx_t_5); __pyx_t_5 = 0;
          goto __pyx_L11_exception_handled;
        }
        goto __pyx_L12_except_error;
```

</details>

L656  ⚪  (score=0)
```python
            pass
```
L657  ⚪  (score=0)
```python
        finally:
```
L658  🟡  (score=4)
```python
            if errors:
```
<details><summary>Show generated C (score=4)</summary>

```c
    /*finally:*/ {
      /*normal exit:*/{
        __pyx_t_10 = __Pyx_PyObject_IsTrue(__pyx_cur_scope->__pyx_v_errors); if (unlikely((__pyx_t_10 < 0))) __PYX_ERR(0, 658, __pyx_L5_error)
        if (__pyx_t_10) {
/* … */
          goto __pyx_L24;
        }
/* … */
          __pyx_t_10 = __Pyx_PyObject_IsTrue(__pyx_cur_scope->__pyx_v_errors); if (unlikely((__pyx_t_10 < 0))) __PYX_ERR(0, 658, __pyx_L30_error)
          if (__pyx_t_10) {
/* … */
            goto __pyx_L31;
          }
```

</details>

L659  🔴  (score=10)
```python
                if scanner.put_back_on_failure:
```
<details><summary>Show generated C (score=10)</summary>

```c
          __pyx_t_5 = __Pyx_PyObject_GetAttrStr(__pyx_cur_scope->__pyx_v_scanner, __pyx_mstate_global->__pyx_n_u_put_back_on_failure); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 659, __pyx_L5_error)
          __Pyx_GOTREF(__pyx_t_5);
          __pyx_t_10 = __Pyx_PyObject_IsTrue(__pyx_t_5); if (unlikely((__pyx_t_10 < 0))) __PYX_ERR(0, 659, __pyx_L5_error)
          __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
          if (__pyx_t_10) {
/* … */
          }
/* … */
            __pyx_t_2 = __Pyx_PyObject_GetAttrStr(__pyx_cur_scope->__pyx_v_scanner, __pyx_mstate_global->__pyx_n_u_put_back_on_failure); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 659, __pyx_L30_error)
            __Pyx_GOTREF(__pyx_t_2);
            __pyx_t_10 = __Pyx_PyObject_IsTrue(__pyx_t_2); if (unlikely((__pyx_t_10 < 0))) __PYX_ERR(0, 659, __pyx_L30_error)
            __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
            if (__pyx_t_10) {
/* … */
            }
```

</details>

L660  🔴  (score=121)
```python
                    for put_back in reversed(scanner.put_back_on_failure[:-1]):
```
<details><summary>Show generated C (score=121)</summary>

```c
            __pyx_t_2 = NULL;
            __pyx_t_3 = __Pyx_PyObject_GetAttrStr(__pyx_cur_scope->__pyx_v_scanner, __pyx_mstate_global->__pyx_n_u_put_back_on_failure); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 660, __pyx_L5_error)
            __Pyx_GOTREF(__pyx_t_3);
            __pyx_t_1 = __Pyx_PyObject_GetSlice(__pyx_t_3, 0, -1L, NULL, NULL, &__pyx_mstate_global->__pyx_slice[1], 0, 1, 0); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 660, __pyx_L5_error)
            __Pyx_GOTREF(__pyx_t_1);
            __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
            __pyx_t_4 = 1;
            {
              PyObject *__pyx_callargs[2] = {__pyx_t_2, __pyx_t_1};
              __pyx_t_5 = __Pyx_PyObject_FastCall((PyObject*)__pyx_builtin_reversed, __pyx_callargs+__pyx_t_4, (2-__pyx_t_4) | (__pyx_t_4*__Pyx_PY_VECTORCALL_ARGUMENTS_OFFSET));
              __Pyx_XDECREF(__pyx_t_2); __pyx_t_2 = 0;
              __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
              if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 660, __pyx_L5_error)
              __Pyx_GOTREF(__pyx_t_5);
            }
            if (likely(PyList_CheckExact(__pyx_t_5)) || PyTuple_CheckExact(__pyx_t_5)) {
              __pyx_t_1 = __pyx_t_5; __Pyx_INCREF(__pyx_t_1);
              __pyx_t_11 = 0;
              __pyx_t_12 = NULL;
            } else {
              __pyx_t_11 = -1; __pyx_t_1 = PyObject_GetIter(__pyx_t_5); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 660, __pyx_L5_error)
              __Pyx_GOTREF(__pyx_t_1);
              __pyx_t_12 = (CYTHON_COMPILING_IN_LIMITED_API) ? PyIter_Next : __Pyx_PyObject_GetIterNextFunc(__pyx_t_1); if (unlikely(!__pyx_t_12)) __PYX_ERR(0, 660, __pyx_L5_error)
            }
            __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
            for (;;) {
              if (likely(!__pyx_t_12)) {
                if (likely(PyList_CheckExact(__pyx_t_1))) {
                  {
                    Py_ssize_t __pyx_temp = __Pyx_PyList_GET_SIZE(__pyx_t_1);
                    #if !CYTHON_ASSUME_SAFE_SIZE
                    if (unlikely((__pyx_temp < 0))) __PYX_ERR(0, 660, __pyx_L5_error)
                    #endif
                    if (__pyx_t_11 >= __pyx_temp) break;
                  }
                  __pyx_t_5 = __Pyx_PyList_GetItemRefFast(__pyx_t_1, __pyx_t_11, __Pyx_ReferenceSharing_OwnStrongReference);
                  ++__pyx_t_11;
                } else {
                  {
                    Py_ssize_t __pyx_temp = __Pyx_PyTuple_GET_SIZE(__pyx_t_1);
                    #if !CYTHON_ASSUME_SAFE_SIZE
                    if (unlikely((__pyx_temp < 0))) __PYX_ERR(0, 660, __pyx_L5_error)
                    #endif
                    if (__pyx_t_11 >= __pyx_temp) break;
                  }
                  #if CYTHON_ASSUME_SAFE_MACROS && !CYTHON_AVOID_BORROWED_REFS
                  __pyx_t_5 = __Pyx_NewRef(PyTuple_GET_ITEM(__pyx_t_1, __pyx_t_11));
                  #else
                  __pyx_t_5 = __Pyx_PySequence_ITEM(__pyx_t_1, __pyx_t_11);
                  #endif
                  ++__pyx_t_11;
                }
                if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 660, __pyx_L5_error)
              } else {
                __pyx_t_5 = __pyx_t_12(__pyx_t_1);
                if (unlikely(!__pyx_t_5)) {
                  PyObject* exc_type = PyErr_Occurred();
                  if (exc_type) {
                    if (unlikely(!__Pyx_PyErr_GivenExceptionMatches(exc_type, PyExc_StopIteration))) __PYX_ERR(0, 660, __pyx_L5_error)
                    PyErr_Clear();
                  }
                  break;
                }
              }
              __Pyx_GOTREF(__pyx_t_5);
              __Pyx_XGOTREF(__pyx_cur_scope->__pyx_v_put_back);
              __Pyx_XDECREF_SET(__pyx_cur_scope->__pyx_v_put_back, __pyx_t_5);
              __Pyx_GIVEREF(__pyx_t_5);
              __pyx_t_5 = 0;
/* … */
            }
            __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
/* … */
              __pyx_t_1 = NULL;
              __pyx_t_3 = __Pyx_PyObject_GetAttrStr(__pyx_cur_scope->__pyx_v_scanner, __pyx_mstate_global->__pyx_n_u_put_back_on_failure); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 660, __pyx_L30_error)
              __Pyx_GOTREF(__pyx_t_3);
              __pyx_t_5 = __Pyx_PyObject_GetSlice(__pyx_t_3, 0, -1L, NULL, NULL, &__pyx_mstate_global->__pyx_slice[1], 0, 1, 0); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 660, __pyx_L30_error)
              __Pyx_GOTREF(__pyx_t_5);
              __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
              __pyx_t_4 = 1;
              {
                PyObject *__pyx_callargs[2] = {__pyx_t_1, __pyx_t_5};
                __pyx_t_2 = __Pyx_PyObject_FastCall((PyObject*)__pyx_builtin_reversed, __pyx_callargs+__pyx_t_4, (2-__pyx_t_4) | (__pyx_t_4*__Pyx_PY_VECTORCALL_ARGUMENTS_OFFSET));
                __Pyx_XDECREF(__pyx_t_1); __pyx_t_1 = 0;
                __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
                if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 660, __pyx_L30_error)
                __Pyx_GOTREF(__pyx_t_2);
              }
              if (likely(PyList_CheckExact(__pyx_t_2)) || PyTuple_CheckExact(__pyx_t_2)) {
                __pyx_t_5 = __pyx_t_2; __Pyx_INCREF(__pyx_t_5);
                __pyx_t_11 = 0;
                __pyx_t_12 = NULL;
              } else {
                __pyx_t_11 = -1; __pyx_t_5 = PyObject_GetIter(__pyx_t_2); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 660, __pyx_L30_error)
                __Pyx_GOTREF(__pyx_t_5);
                __pyx_t_12 = (CYTHON_COMPILING_IN_LIMITED_API) ? PyIter_Next : __Pyx_PyObject_GetIterNextFunc(__pyx_t_5); if (unlikely(!__pyx_t_12)) __PYX_ERR(0, 660, __pyx_L30_error)
              }
              __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
              for (;;) {
                if (likely(!__pyx_t_12)) {
                  if (likely(PyList_CheckExact(__pyx_t_5))) {
                    {
                      Py_ssize_t __pyx_temp = __Pyx_PyList_GET_SIZE(__pyx_t_5);
                      #if !CYTHON_ASSUME_SAFE_SIZE
                      if (unlikely((__pyx_temp < 0))) __PYX_ERR(0, 660, __pyx_L30_error)
                      #endif
                      if (__pyx_t_11 >= __pyx_temp) break;
                    }
                    __pyx_t_2 = __Pyx_PyList_GetItemRefFast(__pyx_t_5, __pyx_t_11, __Pyx_ReferenceSharing_OwnStrongReference);
                    ++__pyx_t_11;
                  } else {
                    {
                      Py_ssize_t __pyx_temp = __Pyx_PyTuple_GET_SIZE(__pyx_t_5);
                      #if !CYTHON_ASSUME_SAFE_SIZE
                      if (unlikely((__pyx_temp < 0))) __PYX_ERR(0, 660, __pyx_L30_error)
                      #endif
                      if (__pyx_t_11 >= __pyx_temp) break;
                    }
                    #if CYTHON_ASSUME_SAFE_MACROS && !CYTHON_AVOID_BORROWED_REFS
                    __pyx_t_2 = __Pyx_NewRef(PyTuple_GET_ITEM(__pyx_t_5, __pyx_t_11));
                    #else
                    __pyx_t_2 = __Pyx_PySequence_ITEM(__pyx_t_5, __pyx_t_11);
                    #endif
                    ++__pyx_t_11;
                  }
                  if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 660, __pyx_L30_error)
                } else {
                  __pyx_t_2 = __pyx_t_12(__pyx_t_5);
                  if (unlikely(!__pyx_t_2)) {
                    PyObject* exc_type = PyErr_Occurred();
                    if (exc_type) {
                      if (unlikely(!__Pyx_PyErr_GivenExceptionMatches(exc_type, PyExc_StopIteration))) __PYX_ERR(0, 660, __pyx_L30_error)
                      PyErr_Clear();
                    }
                    break;
                  }
                }
                __Pyx_GOTREF(__pyx_t_2);
                __Pyx_XGOTREF(__pyx_cur_scope->__pyx_v_put_back);
                __Pyx_XDECREF_SET(__pyx_cur_scope->__pyx_v_put_back, __pyx_t_2);
                __Pyx_GIVEREF(__pyx_t_2);
                __pyx_t_2 = 0;
/* … */
              }
              __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
/* … */
  __pyx_mstate_global->__pyx_slice[1] = PySlice_New(Py_None, __pyx_mstate_global->__pyx_int_neg_1, Py_None); if (unlikely(!__pyx_mstate_global->__pyx_slice[1])) __PYX_ERR(0, 660, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_mstate_global->__pyx_slice[1]);
  __Pyx_GIVEREF(__pyx_mstate_global->__pyx_slice[1]);
```

</details>

L661  🔴  (score=18)
```python
                        scanner.put_back(*put_back)
```
<details><summary>Show generated C (score=18)</summary>

```c
              __pyx_t_5 = __Pyx_PyObject_GetAttrStr(__pyx_cur_scope->__pyx_v_scanner, __pyx_mstate_global->__pyx_n_u_put_back); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 661, __pyx_L5_error)
              __Pyx_GOTREF(__pyx_t_5);
              __pyx_t_2 = __Pyx_PySequence_Tuple(__pyx_cur_scope->__pyx_v_put_back); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 661, __pyx_L5_error)
              __Pyx_GOTREF(__pyx_t_2);
              __pyx_t_3 = __Pyx_PyObject_Call(__pyx_t_5, __pyx_t_2, NULL); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 661, __pyx_L5_error)
              __Pyx_GOTREF(__pyx_t_3);
              __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
              __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
              __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
/* … */
                __pyx_t_2 = __Pyx_PyObject_GetAttrStr(__pyx_cur_scope->__pyx_v_scanner, __pyx_mstate_global->__pyx_n_u_put_back); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 661, __pyx_L30_error)
                __Pyx_GOTREF(__pyx_t_2);
                __pyx_t_1 = __Pyx_PySequence_Tuple(__pyx_cur_scope->__pyx_v_put_back); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 661, __pyx_L30_error)
                __Pyx_GOTREF(__pyx_t_1);
                __pyx_t_3 = __Pyx_PyObject_Call(__pyx_t_2, __pyx_t_1, NULL); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 661, __pyx_L30_error)
                __Pyx_GOTREF(__pyx_t_3);
                __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
                __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
                __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
```

</details>

L662  ⚪  (score=0)
```python
                    # we need to restore the initial state too
```
L663  🔴  (score=18)
```python
                    scanner.put_back(*initial_state)
```
<details><summary>Show generated C (score=18)</summary>

```c
            __pyx_t_1 = __Pyx_PyObject_GetAttrStr(__pyx_cur_scope->__pyx_v_scanner, __pyx_mstate_global->__pyx_n_u_put_back); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 663, __pyx_L5_error)
            __Pyx_GOTREF(__pyx_t_1);
            __pyx_t_3 = __Pyx_PySequence_Tuple(__pyx_cur_scope->__pyx_v_initial_state); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 663, __pyx_L5_error)
            __Pyx_GOTREF(__pyx_t_3);
            __pyx_t_2 = __Pyx_PyObject_Call(__pyx_t_1, __pyx_t_3, NULL); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 663, __pyx_L5_error)
            __Pyx_GOTREF(__pyx_t_2);
            __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
            __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
            __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
/* … */
              __pyx_t_5 = __Pyx_PyObject_GetAttrStr(__pyx_cur_scope->__pyx_v_scanner, __pyx_mstate_global->__pyx_n_u_put_back); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 663, __pyx_L30_error)
              __Pyx_GOTREF(__pyx_t_5);
              __pyx_t_3 = __Pyx_PySequence_Tuple(__pyx_cur_scope->__pyx_v_initial_state); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 663, __pyx_L30_error)
              __Pyx_GOTREF(__pyx_t_3);
              __pyx_t_1 = __Pyx_PyObject_Call(__pyx_t_5, __pyx_t_3, NULL); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 663, __pyx_L30_error)
              __Pyx_GOTREF(__pyx_t_1);
              __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
              __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
              __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
```

</details>

L664  ⚪  (score=0)
```python
            elif put_back_on_failure is not None:
```
<details><summary>Show generated C (score=0)</summary>

```c
        __pyx_t_10 = (__pyx_cur_scope->__pyx_v_put_back_on_failure != Py_None);
        if (__pyx_t_10) {
/* … */
        }
        __pyx_L24:;
/* … */
          __pyx_t_10 = (__pyx_cur_scope->__pyx_v_put_back_on_failure != Py_None);
          if (__pyx_t_10) {
/* … */
          }
          __pyx_L31:;
```

</details>

L665  ⚪  (score=0)
```python
                # the outer "tentatively_scan" block that we're in might still
```
L666  ⚪  (score=0)
```python
                # want to undo this block
```
L667  🔴  (score=16)
```python
                put_back_on_failure.extend(scanner.put_back_on_failure)
```
<details><summary>Show generated C (score=16)</summary>

```c
          __pyx_t_3 = __pyx_cur_scope->__pyx_v_put_back_on_failure;
          __Pyx_INCREF(__pyx_t_3);
          __pyx_t_1 = __Pyx_PyObject_GetAttrStr(__pyx_cur_scope->__pyx_v_scanner, __pyx_mstate_global->__pyx_n_u_put_back_on_failure); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 667, __pyx_L5_error)
          __Pyx_GOTREF(__pyx_t_1);
          __pyx_t_4 = 0;
          {
            PyObject *__pyx_callargs[2] = {__pyx_t_3, __pyx_t_1};
            __pyx_t_2 = __Pyx_PyObject_FastCallMethod((PyObject*)__pyx_mstate_global->__pyx_n_u_extend, __pyx_callargs+__pyx_t_4, (2-__pyx_t_4) | (1*__Pyx_PY_VECTORCALL_ARGUMENTS_OFFSET));
            __Pyx_XDECREF(__pyx_t_3); __pyx_t_3 = 0;
            __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
            if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 667, __pyx_L5_error)
            __Pyx_GOTREF(__pyx_t_2);
          }
          __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
/* … */
            __pyx_t_3 = __pyx_cur_scope->__pyx_v_put_back_on_failure;
            __Pyx_INCREF(__pyx_t_3);
            __pyx_t_5 = __Pyx_PyObject_GetAttrStr(__pyx_cur_scope->__pyx_v_scanner, __pyx_mstate_global->__pyx_n_u_put_back_on_failure); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 667, __pyx_L30_error)
            __Pyx_GOTREF(__pyx_t_5);
            __pyx_t_4 = 0;
            {
              PyObject *__pyx_callargs[2] = {__pyx_t_3, __pyx_t_5};
              __pyx_t_1 = __Pyx_PyObject_FastCallMethod((PyObject*)__pyx_mstate_global->__pyx_n_u_extend, __pyx_callargs+__pyx_t_4, (2-__pyx_t_4) | (1*__Pyx_PY_VECTORCALL_ARGUMENTS_OFFSET));
              __Pyx_XDECREF(__pyx_t_3); __pyx_t_3 = 0;
              __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
              if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 667, __pyx_L30_error)
              __Pyx_GOTREF(__pyx_t_1);
            }
            __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
```

</details>

L668  🔴  (score=23)
```python
            scanner.put_back_on_failure = put_back_on_failure
```
<details><summary>Show generated C (score=23)</summary>

```c
        if (__Pyx_PyObject_SetAttrStr(__pyx_cur_scope->__pyx_v_scanner, __pyx_mstate_global->__pyx_n_u_put_back_on_failure, __pyx_cur_scope->__pyx_v_put_back_on_failure) < (0)) __PYX_ERR(0, 668, __pyx_L5_error)
        goto __pyx_L9;
      }
      __pyx_L8_error:;
      /*exception exit:*/{
        __Pyx_PyThreadState_assign
        __pyx_t_8 = 0; __pyx_t_7 = 0; __pyx_t_6 = 0; __pyx_t_15 = 0; __pyx_t_16 = 0; __pyx_t_17 = 0;
        __Pyx_XDECREF(__pyx_t_1); __pyx_t_1 = 0;
        __Pyx_XDECREF(__pyx_t_2); __pyx_t_2 = 0;
        __Pyx_XDECREF(__pyx_t_3); __pyx_t_3 = 0;
        __Pyx_XDECREF(__pyx_t_5); __pyx_t_5 = 0;
         __Pyx_ExceptionSwap(&__pyx_t_15, &__pyx_t_16, &__pyx_t_17);
        if ( unlikely(__Pyx_GetException(&__pyx_t_8, &__pyx_t_7, &__pyx_t_6) < 0)) __Pyx_ErrFetch(&__pyx_t_8, &__pyx_t_7, &__pyx_t_6);
        __Pyx_XGOTREF(__pyx_t_8);
        __Pyx_XGOTREF(__pyx_t_7);
        __Pyx_XGOTREF(__pyx_t_6);
        __Pyx_XGOTREF(__pyx_t_15);
        __Pyx_XGOTREF(__pyx_t_16);
        __Pyx_XGOTREF(__pyx_t_17);
        __pyx_t_9 = __pyx_lineno; __pyx_t_13 = __pyx_clineno; __pyx_t_14 = __pyx_filename;
        {
/* … */
          if (__Pyx_PyObject_SetAttrStr(__pyx_cur_scope->__pyx_v_scanner, __pyx_mstate_global->__pyx_n_u_put_back_on_failure, __pyx_cur_scope->__pyx_v_put_back_on_failure) < (0)) __PYX_ERR(0, 668, __pyx_L30_error)
        }
        __Pyx_XGIVEREF(__pyx_t_15);
        __Pyx_XGIVEREF(__pyx_t_16);
        __Pyx_XGIVEREF(__pyx_t_17);
        __Pyx_ExceptionReset(__pyx_t_15, __pyx_t_16, __pyx_t_17);
        __Pyx_XGIVEREF(__pyx_t_8);
        __Pyx_XGIVEREF(__pyx_t_7);
        __Pyx_XGIVEREF(__pyx_t_6);
        __Pyx_ErrRestore(__pyx_t_8, __pyx_t_7, __pyx_t_6);
        __pyx_t_8 = 0; __pyx_t_7 = 0; __pyx_t_6 = 0; __pyx_t_15 = 0; __pyx_t_16 = 0; __pyx_t_17 = 0;
        __pyx_lineno = __pyx_t_9; __pyx_clineno = __pyx_t_13; __pyx_filename = __pyx_t_14;
        goto __pyx_L5_error;
        __pyx_L30_error:;
        __Pyx_XGIVEREF(__pyx_t_15);
        __Pyx_XGIVEREF(__pyx_t_16);
        __Pyx_XGIVEREF(__pyx_t_17);
        __Pyx_ExceptionReset(__pyx_t_15, __pyx_t_16, __pyx_t_17);
        __Pyx_XDECREF(__pyx_t_8); __pyx_t_8 = 0;
        __Pyx_XDECREF(__pyx_t_7); __pyx_t_7 = 0;
        __Pyx_XDECREF(__pyx_t_6); __pyx_t_6 = 0;
        __pyx_t_15 = 0; __pyx_t_16 = 0; __pyx_t_17 = 0;
        goto __pyx_L5_error;
      }
      __pyx_L9:;
    }
  }
```

</details>

L669  ⚪  (score=0)
```python
    finally:
```
L670  🔴  (score=43)
```python
        release_errors(ignore=True)
```
<details><summary>Show generated C (score=43)</summary>

```c
  /*finally:*/ {
    /*normal exit:*/{
      __pyx_t_5 = NULL;
      __Pyx_GetModuleGlobalName(__pyx_t_3, __pyx_mstate_global->__pyx_n_u_release_errors); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 670, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_3);
      __pyx_t_4 = 1;
      {
        PyObject *__pyx_callargs[2 + ((CYTHON_VECTORCALL) ? 1 : 0)] = {__pyx_t_5, NULL};
        __pyx_t_2 = __Pyx_MakeVectorcallBuilderKwds(1); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 670, __pyx_L1_error)
        __Pyx_GOTREF(__pyx_t_2);
        if (__Pyx_VectorcallBuilder_AddArg(__pyx_mstate_global->__pyx_n_u_ignore, Py_True, __pyx_t_2, __pyx_callargs+1, 0) < (0)) __PYX_ERR(0, 670, __pyx_L1_error)
        __pyx_t_1 = __Pyx_Object_Vectorcall_CallFromBuilder((PyObject*)__pyx_t_3, __pyx_callargs+__pyx_t_4, (1-__pyx_t_4) | (__pyx_t_4*__Pyx_PY_VECTORCALL_ARGUMENTS_OFFSET), __pyx_t_2);
        __Pyx_XDECREF(__pyx_t_5); __pyx_t_5 = 0;
        __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
        __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
        if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 670, __pyx_L1_error)
        __Pyx_GOTREF(__pyx_t_1);
      }
      __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
      goto __pyx_L6;
    }
    __pyx_L5_error:;
    /*exception exit:*/{
      __Pyx_PyThreadState_assign
      __pyx_t_17 = 0; __pyx_t_16 = 0; __pyx_t_15 = 0; __pyx_t_6 = 0; __pyx_t_7 = 0; __pyx_t_8 = 0;
      __Pyx_XDECREF(__pyx_t_1); __pyx_t_1 = 0;
      __Pyx_XDECREF(__pyx_t_2); __pyx_t_2 = 0;
      __Pyx_XDECREF(__pyx_t_3); __pyx_t_3 = 0;
      __Pyx_XDECREF(__pyx_t_5); __pyx_t_5 = 0;
       __Pyx_ExceptionSwap(&__pyx_t_6, &__pyx_t_7, &__pyx_t_8);
      if ( unlikely(__Pyx_GetException(&__pyx_t_17, &__pyx_t_16, &__pyx_t_15) < 0)) __Pyx_ErrFetch(&__pyx_t_17, &__pyx_t_16, &__pyx_t_15);
      __Pyx_XGOTREF(__pyx_t_17);
      __Pyx_XGOTREF(__pyx_t_16);
      __Pyx_XGOTREF(__pyx_t_15);
      __Pyx_XGOTREF(__pyx_t_6);
      __Pyx_XGOTREF(__pyx_t_7);
      __Pyx_XGOTREF(__pyx_t_8);
      __pyx_t_13 = __pyx_lineno; __pyx_t_9 = __pyx_clineno; __pyx_t_18 = __pyx_filename;
      {
        __pyx_t_3 = NULL;
        __Pyx_GetModuleGlobalName(__pyx_t_2, __pyx_mstate_global->__pyx_n_u_release_errors); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 670, __pyx_L37_error)
        __Pyx_GOTREF(__pyx_t_2);
        __pyx_t_4 = 1;
        {
          PyObject *__pyx_callargs[2 + ((CYTHON_VECTORCALL) ? 1 : 0)] = {__pyx_t_3, NULL};
          __pyx_t_5 = __Pyx_MakeVectorcallBuilderKwds(1); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 670, __pyx_L37_error)
          __Pyx_GOTREF(__pyx_t_5);
          if (__Pyx_VectorcallBuilder_AddArg(__pyx_mstate_global->__pyx_n_u_ignore, Py_True, __pyx_t_5, __pyx_callargs+1, 0) < (0)) __PYX_ERR(0, 670, __pyx_L37_error)
          __pyx_t_1 = __Pyx_Object_Vectorcall_CallFromBuilder((PyObject*)__pyx_t_2, __pyx_callargs+__pyx_t_4, (1-__pyx_t_4) | (__pyx_t_4*__Pyx_PY_VECTORCALL_ARGUMENTS_OFFSET), __pyx_t_5);
          __Pyx_XDECREF(__pyx_t_3); __pyx_t_3 = 0;
          __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
          __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
          if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 670, __pyx_L37_error)
          __Pyx_GOTREF(__pyx_t_1);
        }
        __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
      }
      __Pyx_XGIVEREF(__pyx_t_6);
      __Pyx_XGIVEREF(__pyx_t_7);
      __Pyx_XGIVEREF(__pyx_t_8);
      __Pyx_ExceptionReset(__pyx_t_6, __pyx_t_7, __pyx_t_8);
      __Pyx_XGIVEREF(__pyx_t_17);
      __Pyx_XGIVEREF(__pyx_t_16);
      __Pyx_XGIVEREF(__pyx_t_15);
      __Pyx_ErrRestore(__pyx_t_17, __pyx_t_16, __pyx_t_15);
      __pyx_t_17 = 0; __pyx_t_16 = 0; __pyx_t_15 = 0; __pyx_t_6 = 0; __pyx_t_7 = 0; __pyx_t_8 = 0;
      __pyx_lineno = __pyx_t_13; __pyx_clineno = __pyx_t_9; __pyx_filename = __pyx_t_18;
      goto __pyx_L1_error;
      __pyx_L37_error:;
      __Pyx_XGIVEREF(__pyx_t_6);
      __Pyx_XGIVEREF(__pyx_t_7);
      __Pyx_XGIVEREF(__pyx_t_8);
      __Pyx_ExceptionReset(__pyx_t_6, __pyx_t_7, __pyx_t_8);
      __Pyx_XDECREF(__pyx_t_17); __pyx_t_17 = 0;
      __Pyx_XDECREF(__pyx_t_16); __pyx_t_16 = 0;
      __Pyx_XDECREF(__pyx_t_15); __pyx_t_15 = 0;
      __pyx_t_6 = 0; __pyx_t_7 = 0; __pyx_t_8 = 0;
      goto __pyx_L1_error;
    }
    __pyx_L6:;
  }
  CYTHON_MAYBE_UNUSED_VAR(__pyx_cur_scope);
```

</details>

L671  ⚪  (score=0)
```python
```
L672  ⚪  (score=0)
```python
```
L673  🔴  (score=12)
```python
class FTStringState:
```
<details><summary>Show generated C (score=12)</summary>

```c
  __pyx_t_4 = __Pyx_Py3MetaclassPrepare((PyObject *) NULL, __pyx_mstate_global->__pyx_empty_tuple, __pyx_mstate_global->__pyx_n_u_FTStringState, __pyx_mstate_global->__pyx_n_u_FTStringState, (PyObject *) NULL, __pyx_mstate_global->__pyx_n_u_Cython_Compiler_Scanning, (PyObject *) NULL); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 673, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_4);
/* … */
  __pyx_t_9 = __Pyx_Py3ClassCreate(((PyObject*)&PyType_Type), __pyx_mstate_global->__pyx_n_u_FTStringState, __pyx_mstate_global->__pyx_empty_tuple, __pyx_t_4, NULL, 0, 0); if (unlikely(!__pyx_t_9)) __PYX_ERR(0, 673, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_9);
  #if CYTHON_COMPILING_IN_CPYTHON && PY_VERSION_HEX >= 0x030E0000
  PyUnstable_Object_EnableDeferredRefcount(__pyx_t_9);
  #endif
  if (PyDict_SetItem(__pyx_mstate_global->__pyx_d, __pyx_mstate_global->__pyx_n_u_FTStringState, __pyx_t_9) < (0)) __PYX_ERR(0, 673, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_9); __pyx_t_9 = 0;
  __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
```

</details>

L674  🔴  (score=41)
```python
    def __init__(self, scanner_state):
```
<details><summary>Show generated C (score=41)</summary>

```c
/* Python wrapper */
static PyObject *__pyx_pw_6Cython_8Compiler_8Scanning_13FTStringState_1__init__(PyObject *__pyx_self, 
#if CYTHON_METH_FASTCALL
PyObject *const *__pyx_args, Py_ssize_t __pyx_nargs, PyObject *__pyx_kwds
#else
PyObject *__pyx_args, PyObject *__pyx_kwds
#endif
); /*proto*/
PyDoc_STRVAR(__pyx_doc_6Cython_8Compiler_8Scanning_13FTStringState___init__, "File: Cython/Compiler/Scanning.py (starting at line 674)");
static PyMethodDef __pyx_mdef_6Cython_8Compiler_8Scanning_13FTStringState_1__init__ = {"__init__", (PyCFunction)(void(*)(void))(__Pyx_PyCFunction_FastCallWithKeywords)__pyx_pw_6Cython_8Compiler_8Scanning_13FTStringState_1__init__, __Pyx_METH_FASTCALL|METH_KEYWORDS, __pyx_doc_6Cython_8Compiler_8Scanning_13FTStringState___init__};
static PyObject *__pyx_pw_6Cython_8Compiler_8Scanning_13FTStringState_1__init__(PyObject *__pyx_self, 
#if CYTHON_METH_FASTCALL
PyObject *const *__pyx_args, Py_ssize_t __pyx_nargs, PyObject *__pyx_kwds
#else
PyObject *__pyx_args, PyObject *__pyx_kwds
#endif
) {
  PyObject *__pyx_v_self = 0;
  PyObject *__pyx_v_scanner_state = 0;
  #if !CYTHON_METH_FASTCALL
  CYTHON_UNUSED Py_ssize_t __pyx_nargs;
  #endif
  CYTHON_UNUSED PyObject *const *__pyx_kwvalues;
  PyObject *__pyx_r = 0;
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("__init__ (wrapper)", 0);
  #if !CYTHON_METH_FASTCALL
  #if CYTHON_ASSUME_SAFE_SIZE
  __pyx_nargs = PyTuple_GET_SIZE(__pyx_args);
  #else
  __pyx_nargs = PyTuple_Size(__pyx_args); if (unlikely(__pyx_nargs < 0)) return NULL;
  #endif
  #endif
  __pyx_kwvalues = __Pyx_KwValues_FASTCALL(__pyx_args, __pyx_nargs);
  {
    PyObject ** const __pyx_pyargnames[] = {&__pyx_mstate_global->__pyx_n_u_self,&__pyx_mstate_global->__pyx_n_u_scanner_state,0};
  PyObject* values[2] = {0,0};
    const Py_ssize_t __pyx_kwds_len = (__pyx_kwds) ? __Pyx_NumKwargs_FASTCALL(__pyx_kwds) : 0;
    if (unlikely(__pyx_kwds_len) < 0) __PYX_ERR(0, 674, __pyx_L3_error)
    if (__pyx_kwds_len > 0) {
      switch (__pyx_nargs) {
        case  2:
        values[1] = __Pyx_ArgRef_FASTCALL(__pyx_args, 1);
        if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[1])) __PYX_ERR(0, 674, __pyx_L3_error)
        CYTHON_FALLTHROUGH;
        case  1:
        values[0] = __Pyx_ArgRef_FASTCALL(__pyx_args, 0);
        if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[0])) __PYX_ERR(0, 674, __pyx_L3_error)
        CYTHON_FALLTHROUGH;
        case  0: break;
        default: goto __pyx_L5_argtuple_error;
      }
      const Py_ssize_t kwd_pos_args = __pyx_nargs;
      if (__Pyx_ParseKeywords(__pyx_kwds, __pyx_kwvalues, __pyx_pyargnames, 0, values, kwd_pos_args, __pyx_kwds_len, "__init__", 0) < (0)) __PYX_ERR(0, 674, __pyx_L3_error)
      for (Py_ssize_t i = __pyx_nargs; i < 2; i++) {
        if (unlikely(!values[i])) { __Pyx_RaiseArgtupleInvalid("__init__", 1, 2, 2, i); __PYX_ERR(0, 674, __pyx_L3_error) }
      }
    } else if (unlikely(__pyx_nargs != 2)) {
      goto __pyx_L5_argtuple_error;
    } else {
      values[0] = __Pyx_ArgRef_FASTCALL(__pyx_args, 0);
      if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[0])) __PYX_ERR(0, 674, __pyx_L3_error)
      values[1] = __Pyx_ArgRef_FASTCALL(__pyx_args, 1);
      if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[1])) __PYX_ERR(0, 674, __pyx_L3_error)
    }
    __pyx_v_self = values[0];
    __pyx_v_scanner_state = values[1];
  }
  goto __pyx_L6_skip;
  __pyx_L5_argtuple_error:;
  __Pyx_RaiseArgtupleInvalid("__init__", 1, 2, 2, __pyx_nargs); __PYX_ERR(0, 674, __pyx_L3_error)
  __pyx_L6_skip:;
  goto __pyx_L4_argument_unpacking_done;
  __pyx_L3_error:;
  for (Py_ssize_t __pyx_temp=0; __pyx_temp < (Py_ssize_t)(sizeof(values)/sizeof(values[0])); ++__pyx_temp) {
    Py_XDECREF(values[__pyx_temp]);
  }
  __Pyx_AddTraceback("Cython.Compiler.Scanning.FTStringState.__init__", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __Pyx_RefNannyFinishContext();
  return NULL;
  __pyx_L4_argument_unpacking_done:;
  __pyx_r = __pyx_pf_6Cython_8Compiler_8Scanning_13FTStringState___init__(__pyx_self, __pyx_v_self, __pyx_v_scanner_state);
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

static PyObject *__pyx_pf_6Cython_8Compiler_8Scanning_13FTStringState___init__(CYTHON_UNUSED PyObject *__pyx_self, PyObject *__pyx_v_self, PyObject *__pyx_v_scanner_state) {
  PyObject *__pyx_r = NULL;
/* … */
  /* function exit code */
  __pyx_r = Py_None; __Pyx_INCREF(Py_None);
  goto __pyx_L0;
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_t_1);
  __Pyx_AddTraceback("Cython.Compiler.Scanning.FTStringState.__init__", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_r = NULL;
  __pyx_L0:;
  __Pyx_XGIVEREF(__pyx_r);
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}
/* … */
  __pyx_t_8 = __Pyx_CyFunction_New(&__pyx_mdef_6Cython_8Compiler_8Scanning_13FTStringState_1__init__, 0, __pyx_mstate_global->__pyx_n_u_FTStringState___init, NULL, __pyx_mstate_global->__pyx_n_u_Cython_Compiler_Scanning, __pyx_mstate_global->__pyx_d, ((PyObject *)__pyx_mstate_global->__pyx_codeobj_tab[70])); if (unlikely(!__pyx_t_8)) __PYX_ERR(0, 674, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_8);
  #if CYTHON_COMPILING_IN_CPYTHON && PY_VERSION_HEX >= 0x030E0000
  PyUnstable_Object_EnableDeferredRefcount(__pyx_t_8);
  #endif
  if (__Pyx_SetNameInClass(__pyx_t_4, __pyx_mstate_global->__pyx_n_u_init, __pyx_t_8) < (0)) __PYX_ERR(0, 674, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_8); __pyx_t_8 = 0;
```

</details>

L675  🟡  (score=2)
```python
        self.scanner_state = scanner_state
```
<details><summary>Show generated C (score=2)</summary>

```c
  if (__Pyx_PyObject_SetAttrStr(__pyx_v_self, __pyx_mstate_global->__pyx_n_u_scanner_state, __pyx_v_scanner_state) < (0)) __PYX_ERR(0, 675, __pyx_L1_error)
```

</details>

L676  🟠  (score=8)
```python
        self.bracket_states = []
```
<details><summary>Show generated C (score=8)</summary>

```c
  __pyx_t_1 = PyList_New(0); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 676, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  if (__Pyx_PyObject_SetAttrStr(__pyx_v_self, __pyx_mstate_global->__pyx_n_u_bracket_states, __pyx_t_1) < (0)) __PYX_ERR(0, 676, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
```

</details>

L677  ⚪  (score=0)
```python
```
L678  🔴  (score=37)
```python
    def bracket_nesting_level(self):
```
<details><summary>Show generated C (score=37)</summary>

```c
/* Python wrapper */
static PyObject *__pyx_pw_6Cython_8Compiler_8Scanning_13FTStringState_3bracket_nesting_level(PyObject *__pyx_self, 
#if CYTHON_METH_FASTCALL
PyObject *const *__pyx_args, Py_ssize_t __pyx_nargs, PyObject *__pyx_kwds
#else
PyObject *__pyx_args, PyObject *__pyx_kwds
#endif
); /*proto*/
PyDoc_STRVAR(__pyx_doc_6Cython_8Compiler_8Scanning_13FTStringState_2bracket_nesting_level, "File: Cython/Compiler/Scanning.py (starting at line 678)");
static PyMethodDef __pyx_mdef_6Cython_8Compiler_8Scanning_13FTStringState_3bracket_nesting_level = {"bracket_nesting_level", (PyCFunction)(void(*)(void))(__Pyx_PyCFunction_FastCallWithKeywords)__pyx_pw_6Cython_8Compiler_8Scanning_13FTStringState_3bracket_nesting_level, __Pyx_METH_FASTCALL|METH_KEYWORDS, __pyx_doc_6Cython_8Compiler_8Scanning_13FTStringState_2bracket_nesting_level};
static PyObject *__pyx_pw_6Cython_8Compiler_8Scanning_13FTStringState_3bracket_nesting_level(PyObject *__pyx_self, 
#if CYTHON_METH_FASTCALL
PyObject *const *__pyx_args, Py_ssize_t __pyx_nargs, PyObject *__pyx_kwds
#else
PyObject *__pyx_args, PyObject *__pyx_kwds
#endif
) {
  PyObject *__pyx_v_self = 0;
  #if !CYTHON_METH_FASTCALL
  CYTHON_UNUSED Py_ssize_t __pyx_nargs;
  #endif
  CYTHON_UNUSED PyObject *const *__pyx_kwvalues;
  PyObject *__pyx_r = 0;
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("bracket_nesting_level (wrapper)", 0);
  #if !CYTHON_METH_FASTCALL
  #if CYTHON_ASSUME_SAFE_SIZE
  __pyx_nargs = PyTuple_GET_SIZE(__pyx_args);
  #else
  __pyx_nargs = PyTuple_Size(__pyx_args); if (unlikely(__pyx_nargs < 0)) return NULL;
  #endif
  #endif
  __pyx_kwvalues = __Pyx_KwValues_FASTCALL(__pyx_args, __pyx_nargs);
  {
    PyObject ** const __pyx_pyargnames[] = {&__pyx_mstate_global->__pyx_n_u_self,0};
  PyObject* values[1] = {0};
    const Py_ssize_t __pyx_kwds_len = (__pyx_kwds) ? __Pyx_NumKwargs_FASTCALL(__pyx_kwds) : 0;
    if (unlikely(__pyx_kwds_len) < 0) __PYX_ERR(0, 678, __pyx_L3_error)
    if (__pyx_kwds_len > 0) {
      switch (__pyx_nargs) {
        case  1:
        values[0] = __Pyx_ArgRef_FASTCALL(__pyx_args, 0);
        if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[0])) __PYX_ERR(0, 678, __pyx_L3_error)
        CYTHON_FALLTHROUGH;
        case  0: break;
        default: goto __pyx_L5_argtuple_error;
      }
      const Py_ssize_t kwd_pos_args = __pyx_nargs;
      if (__Pyx_ParseKeywords(__pyx_kwds, __pyx_kwvalues, __pyx_pyargnames, 0, values, kwd_pos_args, __pyx_kwds_len, "bracket_nesting_level", 0) < (0)) __PYX_ERR(0, 678, __pyx_L3_error)
      for (Py_ssize_t i = __pyx_nargs; i < 1; i++) {
        if (unlikely(!values[i])) { __Pyx_RaiseArgtupleInvalid("bracket_nesting_level", 1, 1, 1, i); __PYX_ERR(0, 678, __pyx_L3_error) }
      }
    } else if (unlikely(__pyx_nargs != 1)) {
      goto __pyx_L5_argtuple_error;
    } else {
      values[0] = __Pyx_ArgRef_FASTCALL(__pyx_args, 0);
      if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[0])) __PYX_ERR(0, 678, __pyx_L3_error)
    }
    __pyx_v_self = values[0];
  }
  goto __pyx_L6_skip;
  __pyx_L5_argtuple_error:;
  __Pyx_RaiseArgtupleInvalid("bracket_nesting_level", 1, 1, 1, __pyx_nargs); __PYX_ERR(0, 678, __pyx_L3_error)
  __pyx_L6_skip:;
  goto __pyx_L4_argument_unpacking_done;
  __pyx_L3_error:;
  for (Py_ssize_t __pyx_temp=0; __pyx_temp < (Py_ssize_t)(sizeof(values)/sizeof(values[0])); ++__pyx_temp) {
    Py_XDECREF(values[__pyx_temp]);
  }
  __Pyx_AddTraceback("Cython.Compiler.Scanning.FTStringState.bracket_nesting_level", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __Pyx_RefNannyFinishContext();
  return NULL;
  __pyx_L4_argument_unpacking_done:;
  __pyx_r = __pyx_pf_6Cython_8Compiler_8Scanning_13FTStringState_2bracket_nesting_level(__pyx_self, __pyx_v_self);
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

static PyObject *__pyx_pf_6Cython_8Compiler_8Scanning_13FTStringState_2bracket_nesting_level(CYTHON_UNUSED PyObject *__pyx_self, PyObject *__pyx_v_self) {
  PyObject *__pyx_r = NULL;
/* … */
  /* function exit code */
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_t_1);
  __Pyx_XDECREF(__pyx_t_4);
  __Pyx_AddTraceback("Cython.Compiler.Scanning.FTStringState.bracket_nesting_level", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_r = NULL;
  __pyx_L0:;
  __Pyx_XGIVEREF(__pyx_r);
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}
/* … */
  __pyx_t_8 = __Pyx_CyFunction_New(&__pyx_mdef_6Cython_8Compiler_8Scanning_13FTStringState_3bracket_nesting_level, 0, __pyx_mstate_global->__pyx_n_u_FTStringState_bracket_nesting_le, NULL, __pyx_mstate_global->__pyx_n_u_Cython_Compiler_Scanning, __pyx_mstate_global->__pyx_d, ((PyObject *)__pyx_mstate_global->__pyx_codeobj_tab[71])); if (unlikely(!__pyx_t_8)) __PYX_ERR(0, 678, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_8);
  #if CYTHON_COMPILING_IN_CPYTHON && PY_VERSION_HEX >= 0x030E0000
  PyUnstable_Object_EnableDeferredRefcount(__pyx_t_8);
  #endif
  if (__Pyx_SetNameInClass(__pyx_t_4, __pyx_mstate_global->__pyx_n_u_bracket_nesting_level, __pyx_t_8) < (0)) __PYX_ERR(0, 678, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_8); __pyx_t_8 = 0;
```

</details>

L679  🟠  (score=5)
```python
        if not self.bracket_states:
```
<details><summary>Show generated C (score=5)</summary>

```c
  __pyx_t_1 = __Pyx_PyObject_GetAttrStr(__pyx_v_self, __pyx_mstate_global->__pyx_n_u_bracket_states); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 679, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __pyx_t_2 = __Pyx_PyObject_IsTrue(__pyx_t_1); if (unlikely((__pyx_t_2 < 0))) __PYX_ERR(0, 679, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __pyx_t_3 = (!__pyx_t_2);
  if (__pyx_t_3) {
/* … */
  }
```

</details>

L680  🟡  (score=2)
```python
            return None
```
<details><summary>Show generated C (score=2)</summary>

```c
    __Pyx_XDECREF(__pyx_r);
    __pyx_r = Py_None; __Pyx_INCREF(Py_None);
    goto __pyx_L0;
```

</details>

L681  🟠  (score=9)
```python
        return self.bracket_states[-1].bracket_nesting_level
```
<details><summary>Show generated C (score=9)</summary>

```c
  __Pyx_XDECREF(__pyx_r);
  __pyx_t_1 = __Pyx_PyObject_GetAttrStr(__pyx_v_self, __pyx_mstate_global->__pyx_n_u_bracket_states); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 681, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __pyx_t_4 = __Pyx_GetItemInt(__pyx_t_1, -1L, long, 1, __Pyx_PyLong_From_long, 0, 0, 0, 1, __Pyx_ReferenceSharing_OwnStrongReference); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 681, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_4);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __pyx_t_1 = __Pyx_PyObject_GetAttrStr(__pyx_t_4, __pyx_mstate_global->__pyx_n_u_bracket_nesting_level); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 681, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
  __pyx_r = __pyx_t_1;
  __pyx_t_1 = 0;
  goto __pyx_L0;
```

</details>

L682  ⚪  (score=0)
```python
```
L683  🔴  (score=37)
```python
    def in_format_specifier(self):
```
<details><summary>Show generated C (score=37)</summary>

```c
/* Python wrapper */
static PyObject *__pyx_pw_6Cython_8Compiler_8Scanning_13FTStringState_5in_format_specifier(PyObject *__pyx_self, 
#if CYTHON_METH_FASTCALL
PyObject *const *__pyx_args, Py_ssize_t __pyx_nargs, PyObject *__pyx_kwds
#else
PyObject *__pyx_args, PyObject *__pyx_kwds
#endif
); /*proto*/
PyDoc_STRVAR(__pyx_doc_6Cython_8Compiler_8Scanning_13FTStringState_4in_format_specifier, "File: Cython/Compiler/Scanning.py (starting at line 683)");
static PyMethodDef __pyx_mdef_6Cython_8Compiler_8Scanning_13FTStringState_5in_format_specifier = {"in_format_specifier", (PyCFunction)(void(*)(void))(__Pyx_PyCFunction_FastCallWithKeywords)__pyx_pw_6Cython_8Compiler_8Scanning_13FTStringState_5in_format_specifier, __Pyx_METH_FASTCALL|METH_KEYWORDS, __pyx_doc_6Cython_8Compiler_8Scanning_13FTStringState_4in_format_specifier};
static PyObject *__pyx_pw_6Cython_8Compiler_8Scanning_13FTStringState_5in_format_specifier(PyObject *__pyx_self, 
#if CYTHON_METH_FASTCALL
PyObject *const *__pyx_args, Py_ssize_t __pyx_nargs, PyObject *__pyx_kwds
#else
PyObject *__pyx_args, PyObject *__pyx_kwds
#endif
) {
  PyObject *__pyx_v_self = 0;
  #if !CYTHON_METH_FASTCALL
  CYTHON_UNUSED Py_ssize_t __pyx_nargs;
  #endif
  CYTHON_UNUSED PyObject *const *__pyx_kwvalues;
  PyObject *__pyx_r = 0;
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("in_format_specifier (wrapper)", 0);
  #if !CYTHON_METH_FASTCALL
  #if CYTHON_ASSUME_SAFE_SIZE
  __pyx_nargs = PyTuple_GET_SIZE(__pyx_args);
  #else
  __pyx_nargs = PyTuple_Size(__pyx_args); if (unlikely(__pyx_nargs < 0)) return NULL;
  #endif
  #endif
  __pyx_kwvalues = __Pyx_KwValues_FASTCALL(__pyx_args, __pyx_nargs);
  {
    PyObject ** const __pyx_pyargnames[] = {&__pyx_mstate_global->__pyx_n_u_self,0};
  PyObject* values[1] = {0};
    const Py_ssize_t __pyx_kwds_len = (__pyx_kwds) ? __Pyx_NumKwargs_FASTCALL(__pyx_kwds) : 0;
    if (unlikely(__pyx_kwds_len) < 0) __PYX_ERR(0, 683, __pyx_L3_error)
    if (__pyx_kwds_len > 0) {
      switch (__pyx_nargs) {
        case  1:
        values[0] = __Pyx_ArgRef_FASTCALL(__pyx_args, 0);
        if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[0])) __PYX_ERR(0, 683, __pyx_L3_error)
        CYTHON_FALLTHROUGH;
        case  0: break;
        default: goto __pyx_L5_argtuple_error;
      }
      const Py_ssize_t kwd_pos_args = __pyx_nargs;
      if (__Pyx_ParseKeywords(__pyx_kwds, __pyx_kwvalues, __pyx_pyargnames, 0, values, kwd_pos_args, __pyx_kwds_len, "in_format_specifier", 0) < (0)) __PYX_ERR(0, 683, __pyx_L3_error)
      for (Py_ssize_t i = __pyx_nargs; i < 1; i++) {
        if (unlikely(!values[i])) { __Pyx_RaiseArgtupleInvalid("in_format_specifier", 1, 1, 1, i); __PYX_ERR(0, 683, __pyx_L3_error) }
      }
    } else if (unlikely(__pyx_nargs != 1)) {
      goto __pyx_L5_argtuple_error;
    } else {
      values[0] = __Pyx_ArgRef_FASTCALL(__pyx_args, 0);
      if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[0])) __PYX_ERR(0, 683, __pyx_L3_error)
    }
    __pyx_v_self = values[0];
  }
  goto __pyx_L6_skip;
  __pyx_L5_argtuple_error:;
  __Pyx_RaiseArgtupleInvalid("in_format_specifier", 1, 1, 1, __pyx_nargs); __PYX_ERR(0, 683, __pyx_L3_error)
  __pyx_L6_skip:;
  goto __pyx_L4_argument_unpacking_done;
  __pyx_L3_error:;
  for (Py_ssize_t __pyx_temp=0; __pyx_temp < (Py_ssize_t)(sizeof(values)/sizeof(values[0])); ++__pyx_temp) {
    Py_XDECREF(values[__pyx_temp]);
  }
  __Pyx_AddTraceback("Cython.Compiler.Scanning.FTStringState.in_format_specifier", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __Pyx_RefNannyFinishContext();
  return NULL;
  __pyx_L4_argument_unpacking_done:;
  __pyx_r = __pyx_pf_6Cython_8Compiler_8Scanning_13FTStringState_4in_format_specifier(__pyx_self, __pyx_v_self);
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

static PyObject *__pyx_pf_6Cython_8Compiler_8Scanning_13FTStringState_4in_format_specifier(CYTHON_UNUSED PyObject *__pyx_self, PyObject *__pyx_v_self) {
  PyObject *__pyx_r = NULL;
/* … */
  /* function exit code */
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_t_1);
  __Pyx_XDECREF(__pyx_t_4);
  __Pyx_AddTraceback("Cython.Compiler.Scanning.FTStringState.in_format_specifier", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_r = NULL;
  __pyx_L0:;
  __Pyx_XGIVEREF(__pyx_r);
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}
/* … */
  __pyx_t_8 = __Pyx_CyFunction_New(&__pyx_mdef_6Cython_8Compiler_8Scanning_13FTStringState_5in_format_specifier, 0, __pyx_mstate_global->__pyx_n_u_FTStringState_in_format_specifie, NULL, __pyx_mstate_global->__pyx_n_u_Cython_Compiler_Scanning, __pyx_mstate_global->__pyx_d, ((PyObject *)__pyx_mstate_global->__pyx_codeobj_tab[72])); if (unlikely(!__pyx_t_8)) __PYX_ERR(0, 683, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_8);
  #if CYTHON_COMPILING_IN_CPYTHON && PY_VERSION_HEX >= 0x030E0000
  PyUnstable_Object_EnableDeferredRefcount(__pyx_t_8);
  #endif
  if (__Pyx_SetNameInClass(__pyx_t_4, __pyx_mstate_global->__pyx_n_u_in_format_specifier, __pyx_t_8) < (0)) __PYX_ERR(0, 683, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_8); __pyx_t_8 = 0;
```

</details>

L684  🟠  (score=5)
```python
        if not self.bracket_states:
```
<details><summary>Show generated C (score=5)</summary>

```c
  __pyx_t_1 = __Pyx_PyObject_GetAttrStr(__pyx_v_self, __pyx_mstate_global->__pyx_n_u_bracket_states); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 684, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __pyx_t_2 = __Pyx_PyObject_IsTrue(__pyx_t_1); if (unlikely((__pyx_t_2 < 0))) __PYX_ERR(0, 684, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __pyx_t_3 = (!__pyx_t_2);
  if (__pyx_t_3) {
/* … */
  }
```

</details>

L685  🟡  (score=2)
```python
            return False
```
<details><summary>Show generated C (score=2)</summary>

```c
    __Pyx_XDECREF(__pyx_r);
    __Pyx_INCREF(Py_False);
    __pyx_r = Py_False;
    goto __pyx_L0;
```

</details>

L686  🟠  (score=9)
```python
        return self.bracket_states[-1].in_format_specifier
```
<details><summary>Show generated C (score=9)</summary>

```c
  __Pyx_XDECREF(__pyx_r);
  __pyx_t_1 = __Pyx_PyObject_GetAttrStr(__pyx_v_self, __pyx_mstate_global->__pyx_n_u_bracket_states); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 686, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __pyx_t_4 = __Pyx_GetItemInt(__pyx_t_1, -1L, long, 1, __Pyx_PyLong_From_long, 0, 0, 0, 1, __Pyx_ReferenceSharing_OwnStrongReference); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 686, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_4);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __pyx_t_1 = __Pyx_PyObject_GetAttrStr(__pyx_t_4, __pyx_mstate_global->__pyx_n_u_in_format_specifier); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 686, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
  __pyx_r = __pyx_t_1;
  __pyx_t_1 = 0;
  goto __pyx_L0;
```

</details>

L687  ⚪  (score=0)
```python
```
L688  🔴  (score=38)
```python
    def set_in_format_specifier(self):
```
<details><summary>Show generated C (score=38)</summary>

```c
/* Python wrapper */
static PyObject *__pyx_pw_6Cython_8Compiler_8Scanning_13FTStringState_7set_in_format_specifier(PyObject *__pyx_self, 
#if CYTHON_METH_FASTCALL
PyObject *const *__pyx_args, Py_ssize_t __pyx_nargs, PyObject *__pyx_kwds
#else
PyObject *__pyx_args, PyObject *__pyx_kwds
#endif
); /*proto*/
PyDoc_STRVAR(__pyx_doc_6Cython_8Compiler_8Scanning_13FTStringState_6set_in_format_specifier, "File: Cython/Compiler/Scanning.py (starting at line 688)");
static PyMethodDef __pyx_mdef_6Cython_8Compiler_8Scanning_13FTStringState_7set_in_format_specifier = {"set_in_format_specifier", (PyCFunction)(void(*)(void))(__Pyx_PyCFunction_FastCallWithKeywords)__pyx_pw_6Cython_8Compiler_8Scanning_13FTStringState_7set_in_format_specifier, __Pyx_METH_FASTCALL|METH_KEYWORDS, __pyx_doc_6Cython_8Compiler_8Scanning_13FTStringState_6set_in_format_specifier};
static PyObject *__pyx_pw_6Cython_8Compiler_8Scanning_13FTStringState_7set_in_format_specifier(PyObject *__pyx_self, 
#if CYTHON_METH_FASTCALL
PyObject *const *__pyx_args, Py_ssize_t __pyx_nargs, PyObject *__pyx_kwds
#else
PyObject *__pyx_args, PyObject *__pyx_kwds
#endif
) {
  PyObject *__pyx_v_self = 0;
  #if !CYTHON_METH_FASTCALL
  CYTHON_UNUSED Py_ssize_t __pyx_nargs;
  #endif
  CYTHON_UNUSED PyObject *const *__pyx_kwvalues;
  PyObject *__pyx_r = 0;
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("set_in_format_specifier (wrapper)", 0);
  #if !CYTHON_METH_FASTCALL
  #if CYTHON_ASSUME_SAFE_SIZE
  __pyx_nargs = PyTuple_GET_SIZE(__pyx_args);
  #else
  __pyx_nargs = PyTuple_Size(__pyx_args); if (unlikely(__pyx_nargs < 0)) return NULL;
  #endif
  #endif
  __pyx_kwvalues = __Pyx_KwValues_FASTCALL(__pyx_args, __pyx_nargs);
  {
    PyObject ** const __pyx_pyargnames[] = {&__pyx_mstate_global->__pyx_n_u_self,0};
  PyObject* values[1] = {0};
    const Py_ssize_t __pyx_kwds_len = (__pyx_kwds) ? __Pyx_NumKwargs_FASTCALL(__pyx_kwds) : 0;
    if (unlikely(__pyx_kwds_len) < 0) __PYX_ERR(0, 688, __pyx_L3_error)
    if (__pyx_kwds_len > 0) {
      switch (__pyx_nargs) {
        case  1:
        values[0] = __Pyx_ArgRef_FASTCALL(__pyx_args, 0);
        if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[0])) __PYX_ERR(0, 688, __pyx_L3_error)
        CYTHON_FALLTHROUGH;
        case  0: break;
        default: goto __pyx_L5_argtuple_error;
      }
      const Py_ssize_t kwd_pos_args = __pyx_nargs;
      if (__Pyx_ParseKeywords(__pyx_kwds, __pyx_kwvalues, __pyx_pyargnames, 0, values, kwd_pos_args, __pyx_kwds_len, "set_in_format_specifier", 0) < (0)) __PYX_ERR(0, 688, __pyx_L3_error)
      for (Py_ssize_t i = __pyx_nargs; i < 1; i++) {
        if (unlikely(!values[i])) { __Pyx_RaiseArgtupleInvalid("set_in_format_specifier", 1, 1, 1, i); __PYX_ERR(0, 688, __pyx_L3_error) }
      }
    } else if (unlikely(__pyx_nargs != 1)) {
      goto __pyx_L5_argtuple_error;
    } else {
      values[0] = __Pyx_ArgRef_FASTCALL(__pyx_args, 0);
      if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[0])) __PYX_ERR(0, 688, __pyx_L3_error)
    }
    __pyx_v_self = values[0];
  }
  goto __pyx_L6_skip;
  __pyx_L5_argtuple_error:;
  __Pyx_RaiseArgtupleInvalid("set_in_format_specifier", 1, 1, 1, __pyx_nargs); __PYX_ERR(0, 688, __pyx_L3_error)
  __pyx_L6_skip:;
  goto __pyx_L4_argument_unpacking_done;
  __pyx_L3_error:;
  for (Py_ssize_t __pyx_temp=0; __pyx_temp < (Py_ssize_t)(sizeof(values)/sizeof(values[0])); ++__pyx_temp) {
    Py_XDECREF(values[__pyx_temp]);
  }
  __Pyx_AddTraceback("Cython.Compiler.Scanning.FTStringState.set_in_format_specifier", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __Pyx_RefNannyFinishContext();
  return NULL;
  __pyx_L4_argument_unpacking_done:;
  __pyx_r = __pyx_pf_6Cython_8Compiler_8Scanning_13FTStringState_6set_in_format_specifier(__pyx_self, __pyx_v_self);
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

static PyObject *__pyx_pf_6Cython_8Compiler_8Scanning_13FTStringState_6set_in_format_specifier(CYTHON_UNUSED PyObject *__pyx_self, PyObject *__pyx_v_self) {
  PyObject *__pyx_r = NULL;
/* … */
  /* function exit code */
  __pyx_r = Py_None; __Pyx_INCREF(Py_None);
  goto __pyx_L0;
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_t_1);
  __Pyx_XDECREF(__pyx_t_2);
  __Pyx_AddTraceback("Cython.Compiler.Scanning.FTStringState.set_in_format_specifier", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_r = NULL;
  __pyx_L0:;
  __Pyx_XGIVEREF(__pyx_r);
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}
/* … */
  __pyx_t_8 = __Pyx_CyFunction_New(&__pyx_mdef_6Cython_8Compiler_8Scanning_13FTStringState_7set_in_format_specifier, 0, __pyx_mstate_global->__pyx_n_u_FTStringState_set_in_format_spec, NULL, __pyx_mstate_global->__pyx_n_u_Cython_Compiler_Scanning, __pyx_mstate_global->__pyx_d, ((PyObject *)__pyx_mstate_global->__pyx_codeobj_tab[73])); if (unlikely(!__pyx_t_8)) __PYX_ERR(0, 688, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_8);
  #if CYTHON_COMPILING_IN_CPYTHON && PY_VERSION_HEX >= 0x030E0000
  PyUnstable_Object_EnableDeferredRefcount(__pyx_t_8);
  #endif
  if (__Pyx_SetNameInClass(__pyx_t_4, __pyx_mstate_global->__pyx_n_u_set_in_format_specifier, __pyx_t_8) < (0)) __PYX_ERR(0, 688, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_8); __pyx_t_8 = 0;
```

</details>

L689  🟠  (score=8)
```python
        self.bracket_states[-1].in_format_specifier = True
```
<details><summary>Show generated C (score=8)</summary>

```c
  __pyx_t_1 = __Pyx_PyObject_GetAttrStr(__pyx_v_self, __pyx_mstate_global->__pyx_n_u_bracket_states); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 689, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __pyx_t_2 = __Pyx_GetItemInt(__pyx_t_1, -1L, long, 1, __Pyx_PyLong_From_long, 0, 0, 0, 1, __Pyx_ReferenceSharing_OwnStrongReference); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 689, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  if (__Pyx_PyObject_SetAttrStr(__pyx_t_2, __pyx_mstate_global->__pyx_n_u_in_format_specifier, Py_True) < (0)) __PYX_ERR(0, 689, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
```

</details>

L690  ⚪  (score=0)
```python
```
L691  🔴  (score=78)
```python
    def push_bracket_state(self, bracket_nesting_level: int):
```
<details><summary>Show generated C (score=78)</summary>

```c
/* Python wrapper */
static PyObject *__pyx_pw_6Cython_8Compiler_8Scanning_13FTStringState_9push_bracket_state(PyObject *__pyx_self, 
#if CYTHON_METH_FASTCALL
PyObject *const *__pyx_args, Py_ssize_t __pyx_nargs, PyObject *__pyx_kwds
#else
PyObject *__pyx_args, PyObject *__pyx_kwds
#endif
); /*proto*/
PyDoc_STRVAR(__pyx_doc_6Cython_8Compiler_8Scanning_13FTStringState_8push_bracket_state, "File: Cython/Compiler/Scanning.py (starting at line 691)");
static PyMethodDef __pyx_mdef_6Cython_8Compiler_8Scanning_13FTStringState_9push_bracket_state = {"push_bracket_state", (PyCFunction)(void(*)(void))(__Pyx_PyCFunction_FastCallWithKeywords)__pyx_pw_6Cython_8Compiler_8Scanning_13FTStringState_9push_bracket_state, __Pyx_METH_FASTCALL|METH_KEYWORDS, __pyx_doc_6Cython_8Compiler_8Scanning_13FTStringState_8push_bracket_state};
static PyObject *__pyx_pw_6Cython_8Compiler_8Scanning_13FTStringState_9push_bracket_state(PyObject *__pyx_self, 
#if CYTHON_METH_FASTCALL
PyObject *const *__pyx_args, Py_ssize_t __pyx_nargs, PyObject *__pyx_kwds
#else
PyObject *__pyx_args, PyObject *__pyx_kwds
#endif
) {
  PyObject *__pyx_v_self = 0;
  PyObject *__pyx_v_bracket_nesting_level = 0;
  #if !CYTHON_METH_FASTCALL
  CYTHON_UNUSED Py_ssize_t __pyx_nargs;
  #endif
  CYTHON_UNUSED PyObject *const *__pyx_kwvalues;
  PyObject *__pyx_r = 0;
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("push_bracket_state (wrapper)", 0);
  #if !CYTHON_METH_FASTCALL
  #if CYTHON_ASSUME_SAFE_SIZE
  __pyx_nargs = PyTuple_GET_SIZE(__pyx_args);
  #else
  __pyx_nargs = PyTuple_Size(__pyx_args); if (unlikely(__pyx_nargs < 0)) return NULL;
  #endif
  #endif
  __pyx_kwvalues = __Pyx_KwValues_FASTCALL(__pyx_args, __pyx_nargs);
  {
    PyObject ** const __pyx_pyargnames[] = {&__pyx_mstate_global->__pyx_n_u_self,&__pyx_mstate_global->__pyx_n_u_bracket_nesting_level,0};
  PyObject* values[2] = {0,0};
    const Py_ssize_t __pyx_kwds_len = (__pyx_kwds) ? __Pyx_NumKwargs_FASTCALL(__pyx_kwds) : 0;
    if (unlikely(__pyx_kwds_len) < 0) __PYX_ERR(0, 691, __pyx_L3_error)
    if (__pyx_kwds_len > 0) {
      switch (__pyx_nargs) {
        case  2:
        values[1] = __Pyx_ArgRef_FASTCALL(__pyx_args, 1);
        if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[1])) __PYX_ERR(0, 691, __pyx_L3_error)
        CYTHON_FALLTHROUGH;
        case  1:
        values[0] = __Pyx_ArgRef_FASTCALL(__pyx_args, 0);
        if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[0])) __PYX_ERR(0, 691, __pyx_L3_error)
        CYTHON_FALLTHROUGH;
        case  0: break;
        default: goto __pyx_L5_argtuple_error;
      }
      const Py_ssize_t kwd_pos_args = __pyx_nargs;
      if (__Pyx_ParseKeywords(__pyx_kwds, __pyx_kwvalues, __pyx_pyargnames, 0, values, kwd_pos_args, __pyx_kwds_len, "push_bracket_state", 0) < (0)) __PYX_ERR(0, 691, __pyx_L3_error)
      for (Py_ssize_t i = __pyx_nargs; i < 2; i++) {
        if (unlikely(!values[i])) { __Pyx_RaiseArgtupleInvalid("push_bracket_state", 1, 2, 2, i); __PYX_ERR(0, 691, __pyx_L3_error) }
      }
    } else if (unlikely(__pyx_nargs != 2)) {
      goto __pyx_L5_argtuple_error;
    } else {
      values[0] = __Pyx_ArgRef_FASTCALL(__pyx_args, 0);
      if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[0])) __PYX_ERR(0, 691, __pyx_L3_error)
      values[1] = __Pyx_ArgRef_FASTCALL(__pyx_args, 1);
      if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[1])) __PYX_ERR(0, 691, __pyx_L3_error)
    }
    __pyx_v_self = values[0];
    if (__Pyx_PyInt_FromNumber(&values[1], "bracket_nesting_level", 0) < (0)) __PYX_ERR(0, 691, __pyx_L3_error)
    __pyx_v_bracket_nesting_level = ((PyObject*)values[1]);
  }
  goto __pyx_L6_skip;
  __pyx_L5_argtuple_error:;
  __Pyx_RaiseArgtupleInvalid("push_bracket_state", 1, 2, 2, __pyx_nargs); __PYX_ERR(0, 691, __pyx_L3_error)
  __pyx_L6_skip:;
  goto __pyx_L4_argument_unpacking_done;
  __pyx_L3_error:;
  for (Py_ssize_t __pyx_temp=0; __pyx_temp < (Py_ssize_t)(sizeof(values)/sizeof(values[0])); ++__pyx_temp) {
    Py_XDECREF(values[__pyx_temp]);
  }
  __Pyx_AddTraceback("Cython.Compiler.Scanning.FTStringState.push_bracket_state", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __Pyx_RefNannyFinishContext();
  return NULL;
  __pyx_L4_argument_unpacking_done:;
  if (unlikely(!__Pyx_ArgTypeTest(((PyObject *)__pyx_v_bracket_nesting_level), (&PyLong_Type), 0, "bracket_nesting_level", 2))) __PYX_ERR(0, 691, __pyx_L1_error)
  __pyx_r = __pyx_pf_6Cython_8Compiler_8Scanning_13FTStringState_8push_bracket_state(__pyx_self, __pyx_v_self, __pyx_v_bracket_nesting_level);
  int __pyx_lineno = 0;
  const char *__pyx_filename = NULL;
  int __pyx_clineno = 0;

  /* function exit code */
  goto __pyx_L0;
  __pyx_L1_error:;
  __pyx_r = NULL;
  for (Py_ssize_t __pyx_temp=0; __pyx_temp < (Py_ssize_t)(sizeof(values)/sizeof(values[0])); ++__pyx_temp) {
    Py_XDECREF(values[__pyx_temp]);
  }
  goto __pyx_L7_cleaned_up;
  __pyx_L0:;
  for (Py_ssize_t __pyx_temp=0; __pyx_temp < (Py_ssize_t)(sizeof(values)/sizeof(values[0])); ++__pyx_temp) {
    Py_XDECREF(values[__pyx_temp]);
  }
  __pyx_L7_cleaned_up:;
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}

static PyObject *__pyx_pf_6Cython_8Compiler_8Scanning_13FTStringState_8push_bracket_state(CYTHON_UNUSED PyObject *__pyx_self, PyObject *__pyx_v_self, PyObject *__pyx_v_bracket_nesting_level) {
  PyObject *__pyx_r = NULL;
/* … */
  /* function exit code */
  __pyx_r = Py_None; __Pyx_INCREF(Py_None);
  goto __pyx_L0;
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_t_1);
  __Pyx_XDECREF(__pyx_t_2);
  __Pyx_XDECREF(__pyx_t_3);
  __Pyx_XDECREF(__pyx_t_4);
  __Pyx_AddTraceback("Cython.Compiler.Scanning.FTStringState.push_bracket_state", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_r = NULL;
  __pyx_L0:;
  __Pyx_XGIVEREF(__pyx_r);
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}
/* … */
  __pyx_t_8 = __Pyx_PyDict_NewPresized(1); if (unlikely(!__pyx_t_8)) __PYX_ERR(0, 691, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_8);
  #if defined(PyDict_SetItem) && (defined(CYTHON_COMPILING_IN_CPYTHON))
  #if PY_VERSION_HEX >= 0x030A0000 /* CPython 3.10+ exposes KnownHash APIs */
  /* Use CPython's KnownHash APIs when available */
  extern int _PyDict_SetItem_KnownHash(PyObject*, PyObject*, PyObject*, Py_hash_t);
  {
    Py_hash_t __pyx_hash = PyObject_Hash(__pyx_mstate_global->__pyx_n_u_bracket_nesting_level); if (unlikely(__pyx_hash == -1)) __PYX_ERR(0, 691, __pyx_L1_error);
    if (unlikely(_PyDict_SetItem_KnownHash(__pyx_t_8, __pyx_mstate_global->__pyx_n_u_bracket_nesting_level, __pyx_mstate_global->__pyx_n_u_int, __pyx_hash) < 0)) __PYX_ERR(0, 691, __pyx_L1_error);
  }
  #else
  if (PyDict_SetItem(__pyx_t_8, __pyx_mstate_global->__pyx_n_u_bracket_nesting_level, __pyx_mstate_global->__pyx_n_u_int) < (0)) __PYX_ERR(0, 691, __pyx_L1_error)
  #endif
  #else
  if (PyDict_SetItem(__pyx_t_8, __pyx_mstate_global->__pyx_n_u_bracket_nesting_level, __pyx_mstate_global->__pyx_n_u_int) < (0)) __PYX_ERR(0, 691, __pyx_L1_error)
  #endif
  __pyx_t_9 = __Pyx_CyFunction_New(&__pyx_mdef_6Cython_8Compiler_8Scanning_13FTStringState_9push_bracket_state, 0, __pyx_mstate_global->__pyx_n_u_FTStringState_push_bracket_state, NULL, __pyx_mstate_global->__pyx_n_u_Cython_Compiler_Scanning, __pyx_mstate_global->__pyx_d, ((PyObject *)__pyx_mstate_global->__pyx_codeobj_tab[74])); if (unlikely(!__pyx_t_9)) __PYX_ERR(0, 691, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_9);
  #if CYTHON_COMPILING_IN_CPYTHON && PY_VERSION_HEX >= 0x030E0000
  PyUnstable_Object_EnableDeferredRefcount(__pyx_t_9);
  #endif
  __Pyx_CyFunction_SetAnnotationsDict(__pyx_t_9, __pyx_t_8);
  __Pyx_DECREF(__pyx_t_8); __pyx_t_8 = 0;
  if (__Pyx_SetNameInClass(__pyx_t_4, __pyx_mstate_global->__pyx_n_u_push_bracket_state, __pyx_t_9) < (0)) __PYX_ERR(0, 691, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_9); __pyx_t_9 = 0;
```

</details>

L692  🔴  (score=12)
```python
        self.bracket_states.append(FTStringBracketState(bracket_nesting_level))
```
<details><summary>Show generated C (score=12)</summary>

```c
  __pyx_t_1 = __Pyx_PyObject_GetAttrStr(__pyx_v_self, __pyx_mstate_global->__pyx_n_u_bracket_states); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 692, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __pyx_t_3 = NULL;
  __Pyx_GetModuleGlobalName(__pyx_t_4, __pyx_mstate_global->__pyx_n_u_FTStringBracketState); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 692, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_4);
  __pyx_t_5 = 1;
  {
    PyObject *__pyx_callargs[2] = {__pyx_t_3, __pyx_v_bracket_nesting_level};
    __pyx_t_2 = __Pyx_PyObject_FastCall((PyObject*)__pyx_t_4, __pyx_callargs+__pyx_t_5, (2-__pyx_t_5) | (__pyx_t_5*__Pyx_PY_VECTORCALL_ARGUMENTS_OFFSET));
    __Pyx_XDECREF(__pyx_t_3); __pyx_t_3 = 0;
    __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
    if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 692, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_2);
  }
  __pyx_t_6 = __Pyx_PyObject_Append(__pyx_t_1, __pyx_t_2); if (unlikely(__pyx_t_6 == ((int)-1))) __PYX_ERR(0, 692, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
```

</details>

L693  ⚪  (score=0)
```python
```
L694  🔴  (score=38)
```python
    def pop_bracket_state(self):
```
<details><summary>Show generated C (score=38)</summary>

```c
/* Python wrapper */
static PyObject *__pyx_pw_6Cython_8Compiler_8Scanning_13FTStringState_11pop_bracket_state(PyObject *__pyx_self, 
#if CYTHON_METH_FASTCALL
PyObject *const *__pyx_args, Py_ssize_t __pyx_nargs, PyObject *__pyx_kwds
#else
PyObject *__pyx_args, PyObject *__pyx_kwds
#endif
); /*proto*/
PyDoc_STRVAR(__pyx_doc_6Cython_8Compiler_8Scanning_13FTStringState_10pop_bracket_state, "File: Cython/Compiler/Scanning.py (starting at line 694)");
static PyMethodDef __pyx_mdef_6Cython_8Compiler_8Scanning_13FTStringState_11pop_bracket_state = {"pop_bracket_state", (PyCFunction)(void(*)(void))(__Pyx_PyCFunction_FastCallWithKeywords)__pyx_pw_6Cython_8Compiler_8Scanning_13FTStringState_11pop_bracket_state, __Pyx_METH_FASTCALL|METH_KEYWORDS, __pyx_doc_6Cython_8Compiler_8Scanning_13FTStringState_10pop_bracket_state};
static PyObject *__pyx_pw_6Cython_8Compiler_8Scanning_13FTStringState_11pop_bracket_state(PyObject *__pyx_self, 
#if CYTHON_METH_FASTCALL
PyObject *const *__pyx_args, Py_ssize_t __pyx_nargs, PyObject *__pyx_kwds
#else
PyObject *__pyx_args, PyObject *__pyx_kwds
#endif
) {
  PyObject *__pyx_v_self = 0;
  #if !CYTHON_METH_FASTCALL
  CYTHON_UNUSED Py_ssize_t __pyx_nargs;
  #endif
  CYTHON_UNUSED PyObject *const *__pyx_kwvalues;
  PyObject *__pyx_r = 0;
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("pop_bracket_state (wrapper)", 0);
  #if !CYTHON_METH_FASTCALL
  #if CYTHON_ASSUME_SAFE_SIZE
  __pyx_nargs = PyTuple_GET_SIZE(__pyx_args);
  #else
  __pyx_nargs = PyTuple_Size(__pyx_args); if (unlikely(__pyx_nargs < 0)) return NULL;
  #endif
  #endif
  __pyx_kwvalues = __Pyx_KwValues_FASTCALL(__pyx_args, __pyx_nargs);
  {
    PyObject ** const __pyx_pyargnames[] = {&__pyx_mstate_global->__pyx_n_u_self,0};
  PyObject* values[1] = {0};
    const Py_ssize_t __pyx_kwds_len = (__pyx_kwds) ? __Pyx_NumKwargs_FASTCALL(__pyx_kwds) : 0;
    if (unlikely(__pyx_kwds_len) < 0) __PYX_ERR(0, 694, __pyx_L3_error)
    if (__pyx_kwds_len > 0) {
      switch (__pyx_nargs) {
        case  1:
        values[0] = __Pyx_ArgRef_FASTCALL(__pyx_args, 0);
        if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[0])) __PYX_ERR(0, 694, __pyx_L3_error)
        CYTHON_FALLTHROUGH;
        case  0: break;
        default: goto __pyx_L5_argtuple_error;
      }
      const Py_ssize_t kwd_pos_args = __pyx_nargs;
      if (__Pyx_ParseKeywords(__pyx_kwds, __pyx_kwvalues, __pyx_pyargnames, 0, values, kwd_pos_args, __pyx_kwds_len, "pop_bracket_state", 0) < (0)) __PYX_ERR(0, 694, __pyx_L3_error)
      for (Py_ssize_t i = __pyx_nargs; i < 1; i++) {
        if (unlikely(!values[i])) { __Pyx_RaiseArgtupleInvalid("pop_bracket_state", 1, 1, 1, i); __PYX_ERR(0, 694, __pyx_L3_error) }
      }
    } else if (unlikely(__pyx_nargs != 1)) {
      goto __pyx_L5_argtuple_error;
    } else {
      values[0] = __Pyx_ArgRef_FASTCALL(__pyx_args, 0);
      if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[0])) __PYX_ERR(0, 694, __pyx_L3_error)
    }
    __pyx_v_self = values[0];
  }
  goto __pyx_L6_skip;
  __pyx_L5_argtuple_error:;
  __Pyx_RaiseArgtupleInvalid("pop_bracket_state", 1, 1, 1, __pyx_nargs); __PYX_ERR(0, 694, __pyx_L3_error)
  __pyx_L6_skip:;
  goto __pyx_L4_argument_unpacking_done;
  __pyx_L3_error:;
  for (Py_ssize_t __pyx_temp=0; __pyx_temp < (Py_ssize_t)(sizeof(values)/sizeof(values[0])); ++__pyx_temp) {
    Py_XDECREF(values[__pyx_temp]);
  }
  __Pyx_AddTraceback("Cython.Compiler.Scanning.FTStringState.pop_bracket_state", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __Pyx_RefNannyFinishContext();
  return NULL;
  __pyx_L4_argument_unpacking_done:;
  __pyx_r = __pyx_pf_6Cython_8Compiler_8Scanning_13FTStringState_10pop_bracket_state(__pyx_self, __pyx_v_self);
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

static PyObject *__pyx_pf_6Cython_8Compiler_8Scanning_13FTStringState_10pop_bracket_state(CYTHON_UNUSED PyObject *__pyx_self, PyObject *__pyx_v_self) {
  PyObject *__pyx_r = NULL;
/* … */
  /* function exit code */
  __pyx_r = Py_None; __Pyx_INCREF(Py_None);
  goto __pyx_L0;
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_t_1);
  __Pyx_XDECREF(__pyx_t_2);
  __Pyx_AddTraceback("Cython.Compiler.Scanning.FTStringState.pop_bracket_state", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_r = NULL;
  __pyx_L0:;
  __Pyx_XGIVEREF(__pyx_r);
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}
/* … */
  __pyx_t_9 = __Pyx_CyFunction_New(&__pyx_mdef_6Cython_8Compiler_8Scanning_13FTStringState_11pop_bracket_state, 0, __pyx_mstate_global->__pyx_n_u_FTStringState_pop_bracket_state, NULL, __pyx_mstate_global->__pyx_n_u_Cython_Compiler_Scanning, __pyx_mstate_global->__pyx_d, ((PyObject *)__pyx_mstate_global->__pyx_codeobj_tab[75])); if (unlikely(!__pyx_t_9)) __PYX_ERR(0, 694, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_9);
  #if CYTHON_COMPILING_IN_CPYTHON && PY_VERSION_HEX >= 0x030E0000
  PyUnstable_Object_EnableDeferredRefcount(__pyx_t_9);
  #endif
  if (__Pyx_SetNameInClass(__pyx_t_4, __pyx_mstate_global->__pyx_n_u_pop_bracket_state, __pyx_t_9) < (0)) __PYX_ERR(0, 694, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_9); __pyx_t_9 = 0;
```

</details>

L695  🟠  (score=6)
```python
        self.bracket_states.pop()
```
<details><summary>Show generated C (score=6)</summary>

```c
  __pyx_t_1 = __Pyx_PyObject_GetAttrStr(__pyx_v_self, __pyx_mstate_global->__pyx_n_u_bracket_states); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 695, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __pyx_t_2 = __Pyx_PyObject_Pop(__pyx_t_1); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 695, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
```

</details>

L696  ⚪  (score=0)
```python
```
L697  ⚪  (score=0)
```python
```
L698  🔴  (score=67)
```python
class FTStringBracketState:
```
<details><summary>Show generated C (score=67)</summary>

```c
  __pyx_t_4 = __Pyx_Py3MetaclassPrepare((PyObject *) NULL, __pyx_mstate_global->__pyx_empty_tuple, __pyx_mstate_global->__pyx_n_u_FTStringBracketState, __pyx_mstate_global->__pyx_n_u_FTStringBracketState, (PyObject *) NULL, __pyx_mstate_global->__pyx_n_u_Cython_Compiler_Scanning, (PyObject *) NULL); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 698, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_4);
  __pyx_t_9 = __Pyx_PyDict_NewPresized(2); if (unlikely(!__pyx_t_9)) __PYX_ERR(0, 698, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_9);
  #if defined(PyDict_SetItem) && (defined(CYTHON_COMPILING_IN_CPYTHON))
  #if PY_VERSION_HEX >= 0x030A0000 /* CPython 3.10+ exposes KnownHash APIs */
  /* Use CPython's KnownHash APIs when available */
  extern int _PyDict_SetItem_KnownHash(PyObject*, PyObject*, PyObject*, Py_hash_t);
  {
    Py_hash_t __pyx_hash = PyObject_Hash(__pyx_mstate_global->__pyx_n_u_bracket_nesting_level); if (unlikely(__pyx_hash == -1)) __PYX_ERR(0, 698, __pyx_L1_error);
    if (unlikely(_PyDict_SetItem_KnownHash(__pyx_t_9, __pyx_mstate_global->__pyx_n_u_bracket_nesting_level, __pyx_mstate_global->__pyx_n_u_int, __pyx_hash) < 0)) __PYX_ERR(0, 698, __pyx_L1_error);
  }
  #else
  if (PyDict_SetItem(__pyx_t_9, __pyx_mstate_global->__pyx_n_u_bracket_nesting_level, __pyx_mstate_global->__pyx_n_u_int) < (0)) __PYX_ERR(0, 698, __pyx_L1_error)
  #endif
  #else
  if (PyDict_SetItem(__pyx_t_9, __pyx_mstate_global->__pyx_n_u_bracket_nesting_level, __pyx_mstate_global->__pyx_n_u_int) < (0)) __PYX_ERR(0, 698, __pyx_L1_error)
  #endif
  #if defined(PyDict_SetItem) && (defined(CYTHON_COMPILING_IN_CPYTHON))
  #if PY_VERSION_HEX >= 0x030A0000 /* CPython 3.10+ exposes KnownHash APIs */
  /* Use CPython's KnownHash APIs when available */
  extern int _PyDict_SetItem_KnownHash(PyObject*, PyObject*, PyObject*, Py_hash_t);
  {
    Py_hash_t __pyx_hash = PyObject_Hash(__pyx_mstate_global->__pyx_n_u_in_format_specifier); if (unlikely(__pyx_hash == -1)) __PYX_ERR(0, 698, __pyx_L1_error);
    if (unlikely(_PyDict_SetItem_KnownHash(__pyx_t_9, __pyx_mstate_global->__pyx_n_u_in_format_specifier, __pyx_mstate_global->__pyx_n_u_bool, __pyx_hash) < 0)) __PYX_ERR(0, 698, __pyx_L1_error);
  }
  #else
  if (PyDict_SetItem(__pyx_t_9, __pyx_mstate_global->__pyx_n_u_in_format_specifier, __pyx_mstate_global->__pyx_n_u_bool) < (0)) __PYX_ERR(0, 698, __pyx_L1_error)
  #endif
  #else
  if (PyDict_SetItem(__pyx_t_9, __pyx_mstate_global->__pyx_n_u_in_format_specifier, __pyx_mstate_global->__pyx_n_u_bool) < (0)) __PYX_ERR(0, 698, __pyx_L1_error)
  #endif
  if (__Pyx_SetNameInClass(__pyx_t_4, __pyx_mstate_global->__pyx_n_u_annotations, __pyx_t_9) < (0)) __PYX_ERR(0, 698, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_9); __pyx_t_9 = 0;
/* … */
  __pyx_t_8 = __Pyx_Py3ClassCreate(((PyObject*)&PyType_Type), __pyx_mstate_global->__pyx_n_u_FTStringBracketState, __pyx_mstate_global->__pyx_empty_tuple, __pyx_t_4, NULL, 0, 0); if (unlikely(!__pyx_t_8)) __PYX_ERR(0, 698, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_8);
  #if CYTHON_COMPILING_IN_CPYTHON && PY_VERSION_HEX >= 0x030E0000
  PyUnstable_Object_EnableDeferredRefcount(__pyx_t_8);
  #endif
  if (PyDict_SetItem(__pyx_mstate_global->__pyx_d, __pyx_mstate_global->__pyx_n_u_FTStringBracketState, __pyx_t_8) < (0)) __PYX_ERR(0, 698, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_8); __pyx_t_8 = 0;
  __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
```

</details>

L699  ⚪  (score=0)
```python
    # Because of the way this is accessed, it probably doesn't make sense as a cdef class
```
L700  ⚪  (score=0)
```python
    # so just use __slots__ to keep it compact.
```
L701  🟡  (score=2)
```python
    __slots__ = ('bracket_nesting_level', 'in_format_specifier')
```
<details><summary>Show generated C (score=2)</summary>

```c
  if (__Pyx_SetNameInClass(__pyx_t_4, __pyx_mstate_global->__pyx_n_u_slots, __pyx_mstate_global->__pyx_tuple[19]) < (0)) __PYX_ERR(0, 701, __pyx_L1_error)
```

</details>

L702  ⚪  (score=0)
```python
    bracket_nesting_level: int
```
L703  ⚪  (score=0)
```python
    in_format_specifier: bool
```
L704  🔴  (score=71)
```python
    def __init__(self, bracket_nesting_level: int):
```
<details><summary>Show generated C (score=71)</summary>

```c
/* Python wrapper */
static PyObject *__pyx_pw_6Cython_8Compiler_8Scanning_20FTStringBracketState_1__init__(PyObject *__pyx_self, 
#if CYTHON_METH_FASTCALL
PyObject *const *__pyx_args, Py_ssize_t __pyx_nargs, PyObject *__pyx_kwds
#else
PyObject *__pyx_args, PyObject *__pyx_kwds
#endif
); /*proto*/
PyDoc_STRVAR(__pyx_doc_6Cython_8Compiler_8Scanning_20FTStringBracketState___init__, "File: Cython/Compiler/Scanning.py (starting at line 704)");
static PyMethodDef __pyx_mdef_6Cython_8Compiler_8Scanning_20FTStringBracketState_1__init__ = {"__init__", (PyCFunction)(void(*)(void))(__Pyx_PyCFunction_FastCallWithKeywords)__pyx_pw_6Cython_8Compiler_8Scanning_20FTStringBracketState_1__init__, __Pyx_METH_FASTCALL|METH_KEYWORDS, __pyx_doc_6Cython_8Compiler_8Scanning_20FTStringBracketState___init__};
static PyObject *__pyx_pw_6Cython_8Compiler_8Scanning_20FTStringBracketState_1__init__(PyObject *__pyx_self, 
#if CYTHON_METH_FASTCALL
PyObject *const *__pyx_args, Py_ssize_t __pyx_nargs, PyObject *__pyx_kwds
#else
PyObject *__pyx_args, PyObject *__pyx_kwds
#endif
) {
  PyObject *__pyx_v_self = 0;
  PyObject *__pyx_v_bracket_nesting_level = 0;
  #if !CYTHON_METH_FASTCALL
  CYTHON_UNUSED Py_ssize_t __pyx_nargs;
  #endif
  CYTHON_UNUSED PyObject *const *__pyx_kwvalues;
  PyObject *__pyx_r = 0;
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("__init__ (wrapper)", 0);
  #if !CYTHON_METH_FASTCALL
  #if CYTHON_ASSUME_SAFE_SIZE
  __pyx_nargs = PyTuple_GET_SIZE(__pyx_args);
  #else
  __pyx_nargs = PyTuple_Size(__pyx_args); if (unlikely(__pyx_nargs < 0)) return NULL;
  #endif
  #endif
  __pyx_kwvalues = __Pyx_KwValues_FASTCALL(__pyx_args, __pyx_nargs);
  {
    PyObject ** const __pyx_pyargnames[] = {&__pyx_mstate_global->__pyx_n_u_self,&__pyx_mstate_global->__pyx_n_u_bracket_nesting_level,0};
  PyObject* values[2] = {0,0};
    const Py_ssize_t __pyx_kwds_len = (__pyx_kwds) ? __Pyx_NumKwargs_FASTCALL(__pyx_kwds) : 0;
    if (unlikely(__pyx_kwds_len) < 0) __PYX_ERR(0, 704, __pyx_L3_error)
    if (__pyx_kwds_len > 0) {
      switch (__pyx_nargs) {
        case  2:
        values[1] = __Pyx_ArgRef_FASTCALL(__pyx_args, 1);
        if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[1])) __PYX_ERR(0, 704, __pyx_L3_error)
        CYTHON_FALLTHROUGH;
        case  1:
        values[0] = __Pyx_ArgRef_FASTCALL(__pyx_args, 0);
        if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[0])) __PYX_ERR(0, 704, __pyx_L3_error)
        CYTHON_FALLTHROUGH;
        case  0: break;
        default: goto __pyx_L5_argtuple_error;
      }
      const Py_ssize_t kwd_pos_args = __pyx_nargs;
      if (__Pyx_ParseKeywords(__pyx_kwds, __pyx_kwvalues, __pyx_pyargnames, 0, values, kwd_pos_args, __pyx_kwds_len, "__init__", 0) < (0)) __PYX_ERR(0, 704, __pyx_L3_error)
      for (Py_ssize_t i = __pyx_nargs; i < 2; i++) {
        if (unlikely(!values[i])) { __Pyx_RaiseArgtupleInvalid("__init__", 1, 2, 2, i); __PYX_ERR(0, 704, __pyx_L3_error) }
      }
    } else if (unlikely(__pyx_nargs != 2)) {
      goto __pyx_L5_argtuple_error;
    } else {
      values[0] = __Pyx_ArgRef_FASTCALL(__pyx_args, 0);
      if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[0])) __PYX_ERR(0, 704, __pyx_L3_error)
      values[1] = __Pyx_ArgRef_FASTCALL(__pyx_args, 1);
      if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[1])) __PYX_ERR(0, 704, __pyx_L3_error)
    }
    __pyx_v_self = values[0];
    if (__Pyx_PyInt_FromNumber(&values[1], "bracket_nesting_level", 0) < (0)) __PYX_ERR(0, 704, __pyx_L3_error)
    __pyx_v_bracket_nesting_level = ((PyObject*)values[1]);
  }
  goto __pyx_L6_skip;
  __pyx_L5_argtuple_error:;
  __Pyx_RaiseArgtupleInvalid("__init__", 1, 2, 2, __pyx_nargs); __PYX_ERR(0, 704, __pyx_L3_error)
  __pyx_L6_skip:;
  goto __pyx_L4_argument_unpacking_done;
  __pyx_L3_error:;
  for (Py_ssize_t __pyx_temp=0; __pyx_temp < (Py_ssize_t)(sizeof(values)/sizeof(values[0])); ++__pyx_temp) {
    Py_XDECREF(values[__pyx_temp]);
  }
  __Pyx_AddTraceback("Cython.Compiler.Scanning.FTStringBracketState.__init__", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __Pyx_RefNannyFinishContext();
  return NULL;
  __pyx_L4_argument_unpacking_done:;
  if (unlikely(!__Pyx_ArgTypeTest(((PyObject *)__pyx_v_bracket_nesting_level), (&PyLong_Type), 0, "bracket_nesting_level", 2))) __PYX_ERR(0, 704, __pyx_L1_error)
  __pyx_r = __pyx_pf_6Cython_8Compiler_8Scanning_20FTStringBracketState___init__(__pyx_self, __pyx_v_self, __pyx_v_bracket_nesting_level);
  int __pyx_lineno = 0;
  const char *__pyx_filename = NULL;
  int __pyx_clineno = 0;

  /* function exit code */
  goto __pyx_L0;
  __pyx_L1_error:;
  __pyx_r = NULL;
  for (Py_ssize_t __pyx_temp=0; __pyx_temp < (Py_ssize_t)(sizeof(values)/sizeof(values[0])); ++__pyx_temp) {
    Py_XDECREF(values[__pyx_temp]);
  }
  goto __pyx_L7_cleaned_up;
  __pyx_L0:;
  for (Py_ssize_t __pyx_temp=0; __pyx_temp < (Py_ssize_t)(sizeof(values)/sizeof(values[0])); ++__pyx_temp) {
    Py_XDECREF(values[__pyx_temp]);
  }
  __pyx_L7_cleaned_up:;
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}

static PyObject *__pyx_pf_6Cython_8Compiler_8Scanning_20FTStringBracketState___init__(CYTHON_UNUSED PyObject *__pyx_self, PyObject *__pyx_v_self, PyObject *__pyx_v_bracket_nesting_level) {
  PyObject *__pyx_r = NULL;
/* … */
  __pyx_t_9 = __Pyx_PyDict_NewPresized(1); if (unlikely(!__pyx_t_9)) __PYX_ERR(0, 704, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_9);
  #if defined(PyDict_SetItem) && (defined(CYTHON_COMPILING_IN_CPYTHON))
  #if PY_VERSION_HEX >= 0x030A0000 /* CPython 3.10+ exposes KnownHash APIs */
  /* Use CPython's KnownHash APIs when available */
  extern int _PyDict_SetItem_KnownHash(PyObject*, PyObject*, PyObject*, Py_hash_t);
  {
    Py_hash_t __pyx_hash = PyObject_Hash(__pyx_mstate_global->__pyx_n_u_bracket_nesting_level); if (unlikely(__pyx_hash == -1)) __PYX_ERR(0, 704, __pyx_L1_error);
    if (unlikely(_PyDict_SetItem_KnownHash(__pyx_t_9, __pyx_mstate_global->__pyx_n_u_bracket_nesting_level, __pyx_mstate_global->__pyx_n_u_int, __pyx_hash) < 0)) __PYX_ERR(0, 704, __pyx_L1_error);
  }
  #else
  if (PyDict_SetItem(__pyx_t_9, __pyx_mstate_global->__pyx_n_u_bracket_nesting_level, __pyx_mstate_global->__pyx_n_u_int) < (0)) __PYX_ERR(0, 704, __pyx_L1_error)
  #endif
  #else
  if (PyDict_SetItem(__pyx_t_9, __pyx_mstate_global->__pyx_n_u_bracket_nesting_level, __pyx_mstate_global->__pyx_n_u_int) < (0)) __PYX_ERR(0, 704, __pyx_L1_error)
  #endif
  __pyx_t_8 = __Pyx_CyFunction_New(&__pyx_mdef_6Cython_8Compiler_8Scanning_20FTStringBracketState_1__init__, 0, __pyx_mstate_global->__pyx_n_u_FTStringBracketState___init, NULL, __pyx_mstate_global->__pyx_n_u_Cython_Compiler_Scanning, __pyx_mstate_global->__pyx_d, ((PyObject *)__pyx_mstate_global->__pyx_codeobj_tab[76])); if (unlikely(!__pyx_t_8)) __PYX_ERR(0, 704, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_8);
  #if CYTHON_COMPILING_IN_CPYTHON && PY_VERSION_HEX >= 0x030E0000
  PyUnstable_Object_EnableDeferredRefcount(__pyx_t_8);
  #endif
  __Pyx_CyFunction_SetAnnotationsDict(__pyx_t_8, __pyx_t_9);
  __Pyx_DECREF(__pyx_t_9); __pyx_t_9 = 0;
  if (__Pyx_SetNameInClass(__pyx_t_4, __pyx_mstate_global->__pyx_n_u_init, __pyx_t_8) < (0)) __PYX_ERR(0, 704, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_8); __pyx_t_8 = 0;
```

</details>

L705  🟡  (score=2)
```python
        self.bracket_nesting_level = bracket_nesting_level
```
<details><summary>Show generated C (score=2)</summary>

```c
  if (__Pyx_PyObject_SetAttrStr(__pyx_v_self, __pyx_mstate_global->__pyx_n_u_bracket_nesting_level, __pyx_v_bracket_nesting_level) < (0)) __PYX_ERR(0, 705, __pyx_L1_error)
```

</details>

L706  🟡  (score=2)
```python
        self.in_format_specifier = False
```
<details><summary>Show generated C (score=2)</summary>

```c
  if (__Pyx_PyObject_SetAttrStr(__pyx_v_self, __pyx_mstate_global->__pyx_n_u_in_format_specifier, Py_False) < (0)) __PYX_ERR(0, 706, __pyx_L1_error)
```

</details>

