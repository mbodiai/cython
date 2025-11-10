# Cython annotation for Visitor.py

Raw output: Visitor.c

L1  🟠  (score=8)
```python
# cython: infer_types=True
```
<details><summary>Show generated C (score=8)</summary>

```c
  __pyx_t_5 = __Pyx_PyDict_NewPresized(0); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 1, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_5);
  if (PyDict_SetItem(__pyx_mstate_global->__pyx_d, __pyx_mstate_global->__pyx_n_u_test, __pyx_t_5) < (0)) __PYX_ERR(0, 1, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
```

</details>

L2  ⚪  (score=0)
```python
```
L3  ⚪  (score=0)
```python
#
```
L4  ⚪  (score=0)
```python
#   Tree visitor and transform framework
```
L5  ⚪  (score=0)
```python
#
```
L6  ⚪  (score=0)
```python
```
L7  ⚪  (score=0)
```python
```
L8  🔴  (score=11)
```python
from collections.abc import Callable
```
<details><summary>Show generated C (score=11)</summary>

```c
  {
    PyObject* const __pyx_imported_names[] = {__pyx_mstate_global->__pyx_n_u_Callable};
    __pyx_t_1 = __Pyx_Import(__pyx_mstate_global->__pyx_n_u_collections_abc, __pyx_imported_names, 1, NULL, 0); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 8, __pyx_L1_error)
  }
  __pyx_t_2 = __pyx_t_1;
  __Pyx_GOTREF(__pyx_t_2);
  {
    PyObject* const __pyx_imported_names[] = {__pyx_mstate_global->__pyx_n_u_Callable};
    for (__pyx_t_3=0; __pyx_t_3 < 1; __pyx_t_3++) {
      __pyx_t_4 = __Pyx_ImportFrom(__pyx_t_2, __pyx_imported_names[__pyx_t_3]); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 8, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_4);
      switch (__pyx_t_3) {
        case 0:
        if (PyDict_SetItem(__pyx_mstate_global->__pyx_d, __pyx_imported_names[__pyx_t_3], __pyx_t_4) < (0)) __PYX_ERR(0, 8, __pyx_L1_error)
        break;
      }
      __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
    }
  }
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
```

</details>

L9  🟠  (score=8)
```python
import sys
```
<details><summary>Show generated C (score=8)</summary>

```c
  __pyx_t_1 = __Pyx_Import(__pyx_mstate_global->__pyx_n_u_sys, 0, 0, NULL, 0); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 9, __pyx_L1_error)
  __pyx_t_2 = __pyx_t_1;
  __Pyx_GOTREF(__pyx_t_2);
  if (PyDict_SetItem(__pyx_mstate_global->__pyx_d, __pyx_mstate_global->__pyx_n_u_sys, __pyx_t_2) < (0)) __PYX_ERR(0, 9, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
```

</details>

L10  🟠  (score=8)
```python
import inspect
```
<details><summary>Show generated C (score=8)</summary>

```c
  __pyx_t_1 = __Pyx_Import(__pyx_mstate_global->__pyx_n_u_inspect, 0, 0, NULL, 0); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 10, __pyx_L1_error)
  __pyx_t_2 = __pyx_t_1;
  __Pyx_GOTREF(__pyx_t_2);
  if (PyDict_SetItem(__pyx_mstate_global->__pyx_d, __pyx_mstate_global->__pyx_n_u_inspect, __pyx_t_2) < (0)) __PYX_ERR(0, 10, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
```

</details>

L11  🔴  (score=11)
```python
from typing import Any
```
<details><summary>Show generated C (score=11)</summary>

```c
  {
    PyObject* const __pyx_imported_names[] = {__pyx_mstate_global->__pyx_n_u_Any};
    __pyx_t_1 = __Pyx_Import(__pyx_mstate_global->__pyx_n_u_typing, __pyx_imported_names, 1, NULL, 0); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 11, __pyx_L1_error)
  }
  __pyx_t_2 = __pyx_t_1;
  __Pyx_GOTREF(__pyx_t_2);
  {
    PyObject* const __pyx_imported_names[] = {__pyx_mstate_global->__pyx_n_u_Any};
    for (__pyx_t_3=0; __pyx_t_3 < 1; __pyx_t_3++) {
      __pyx_t_4 = __Pyx_ImportFrom(__pyx_t_2, __pyx_imported_names[__pyx_t_3]); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 11, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_4);
      switch (__pyx_t_3) {
        case 0:
        if (PyDict_SetItem(__pyx_mstate_global->__pyx_d, __pyx_imported_names[__pyx_t_3], __pyx_t_4) < (0)) __PYX_ERR(0, 11, __pyx_L1_error)
        break;
      }
      __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
    }
  }
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
```

</details>

L12  ⚪  (score=0)
```python
```
L13  🔴  (score=11)
```python
from . import TypeSlots
```
<details><summary>Show generated C (score=11)</summary>

```c
  {
    PyObject* const __pyx_imported_names[] = {__pyx_mstate_global->__pyx_n_u_TypeSlots};
    __pyx_t_1 = __Pyx_Import(__pyx_mstate_global->__pyx_n_u__7, __pyx_imported_names, 1, __pyx_mstate_global->__pyx_kp_u_Cython_Compiler, 1); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 13, __pyx_L1_error)
  }
  __pyx_t_2 = __pyx_t_1;
  __Pyx_GOTREF(__pyx_t_2);
  {
    PyObject* const __pyx_imported_names[] = {__pyx_mstate_global->__pyx_n_u_TypeSlots};
    for (__pyx_t_3=0; __pyx_t_3 < 1; __pyx_t_3++) {
      __pyx_t_4 = __Pyx_ImportFrom(__pyx_t_2, __pyx_imported_names[__pyx_t_3]); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 13, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_4);
      switch (__pyx_t_3) {
        case 0:
        if (PyDict_SetItem(__pyx_mstate_global->__pyx_d, __pyx_imported_names[__pyx_t_3], __pyx_t_4) < (0)) __PYX_ERR(0, 13, __pyx_L1_error)
        break;
      }
      __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
    }
  }
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
```

</details>

L14  🔴  (score=11)
```python
from . import Builtin
```
<details><summary>Show generated C (score=11)</summary>

```c
  {
    PyObject* const __pyx_imported_names[] = {__pyx_mstate_global->__pyx_n_u_Builtin};
    __pyx_t_1 = __Pyx_Import(__pyx_mstate_global->__pyx_n_u__7, __pyx_imported_names, 1, __pyx_mstate_global->__pyx_kp_u_Cython_Compiler, 1); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 14, __pyx_L1_error)
  }
  __pyx_t_2 = __pyx_t_1;
  __Pyx_GOTREF(__pyx_t_2);
  {
    PyObject* const __pyx_imported_names[] = {__pyx_mstate_global->__pyx_n_u_Builtin};
    for (__pyx_t_3=0; __pyx_t_3 < 1; __pyx_t_3++) {
      __pyx_t_4 = __Pyx_ImportFrom(__pyx_t_2, __pyx_imported_names[__pyx_t_3]); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 14, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_4);
      switch (__pyx_t_3) {
        case 0:
        if (PyDict_SetItem(__pyx_mstate_global->__pyx_d, __pyx_imported_names[__pyx_t_3], __pyx_t_4) < (0)) __PYX_ERR(0, 14, __pyx_L1_error)
        break;
      }
      __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
    }
  }
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
```

</details>

L15  🔴  (score=11)
```python
from . import Nodes
```
<details><summary>Show generated C (score=11)</summary>

```c
  {
    PyObject* const __pyx_imported_names[] = {__pyx_mstate_global->__pyx_n_u_Nodes};
    __pyx_t_1 = __Pyx_Import(__pyx_mstate_global->__pyx_n_u__7, __pyx_imported_names, 1, __pyx_mstate_global->__pyx_kp_u_Cython_Compiler, 1); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 15, __pyx_L1_error)
  }
  __pyx_t_2 = __pyx_t_1;
  __Pyx_GOTREF(__pyx_t_2);
  {
    PyObject* const __pyx_imported_names[] = {__pyx_mstate_global->__pyx_n_u_Nodes};
    for (__pyx_t_3=0; __pyx_t_3 < 1; __pyx_t_3++) {
      __pyx_t_4 = __Pyx_ImportFrom(__pyx_t_2, __pyx_imported_names[__pyx_t_3]); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 15, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_4);
      switch (__pyx_t_3) {
        case 0:
        if (PyDict_SetItem(__pyx_mstate_global->__pyx_d, __pyx_imported_names[__pyx_t_3], __pyx_t_4) < (0)) __PYX_ERR(0, 15, __pyx_L1_error)
        break;
      }
      __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
    }
  }
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
```

</details>

L16  🔴  (score=11)
```python
from . import ExprNodes
```
<details><summary>Show generated C (score=11)</summary>

```c
  {
    PyObject* const __pyx_imported_names[] = {__pyx_mstate_global->__pyx_n_u_ExprNodes};
    __pyx_t_1 = __Pyx_Import(__pyx_mstate_global->__pyx_n_u__7, __pyx_imported_names, 1, __pyx_mstate_global->__pyx_kp_u_Cython_Compiler, 1); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 16, __pyx_L1_error)
  }
  __pyx_t_2 = __pyx_t_1;
  __Pyx_GOTREF(__pyx_t_2);
  {
    PyObject* const __pyx_imported_names[] = {__pyx_mstate_global->__pyx_n_u_ExprNodes};
    for (__pyx_t_3=0; __pyx_t_3 < 1; __pyx_t_3++) {
      __pyx_t_4 = __Pyx_ImportFrom(__pyx_t_2, __pyx_imported_names[__pyx_t_3]); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 16, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_4);
      switch (__pyx_t_3) {
        case 0:
        if (PyDict_SetItem(__pyx_mstate_global->__pyx_d, __pyx_imported_names[__pyx_t_3], __pyx_t_4) < (0)) __PYX_ERR(0, 16, __pyx_L1_error)
        break;
      }
      __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
    }
  }
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
```

</details>

L17  🔴  (score=11)
```python
from . import Errors
```
<details><summary>Show generated C (score=11)</summary>

```c
  {
    PyObject* const __pyx_imported_names[] = {__pyx_mstate_global->__pyx_n_u_Errors};
    __pyx_t_1 = __Pyx_Import(__pyx_mstate_global->__pyx_n_u__7, __pyx_imported_names, 1, __pyx_mstate_global->__pyx_kp_u_Cython_Compiler, 1); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 17, __pyx_L1_error)
  }
  __pyx_t_2 = __pyx_t_1;
  __Pyx_GOTREF(__pyx_t_2);
  {
    PyObject* const __pyx_imported_names[] = {__pyx_mstate_global->__pyx_n_u_Errors};
    for (__pyx_t_3=0; __pyx_t_3 < 1; __pyx_t_3++) {
      __pyx_t_4 = __Pyx_ImportFrom(__pyx_t_2, __pyx_imported_names[__pyx_t_3]); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 17, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_4);
      switch (__pyx_t_3) {
        case 0:
        if (PyDict_SetItem(__pyx_mstate_global->__pyx_d, __pyx_imported_names[__pyx_t_3], __pyx_t_4) < (0)) __PYX_ERR(0, 17, __pyx_L1_error)
        break;
      }
      __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
    }
  }
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
```

</details>

L18  🔴  (score=11)
```python
from . import DebugFlags
```
<details><summary>Show generated C (score=11)</summary>

```c
  {
    PyObject* const __pyx_imported_names[] = {__pyx_mstate_global->__pyx_n_u_DebugFlags};
    __pyx_t_1 = __Pyx_Import(__pyx_mstate_global->__pyx_n_u__7, __pyx_imported_names, 1, __pyx_mstate_global->__pyx_kp_u_Cython_Compiler, 1); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 18, __pyx_L1_error)
  }
  __pyx_t_2 = __pyx_t_1;
  __Pyx_GOTREF(__pyx_t_2);
  {
    PyObject* const __pyx_imported_names[] = {__pyx_mstate_global->__pyx_n_u_DebugFlags};
    for (__pyx_t_3=0; __pyx_t_3 < 1; __pyx_t_3++) {
      __pyx_t_4 = __Pyx_ImportFrom(__pyx_t_2, __pyx_imported_names[__pyx_t_3]); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 18, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_4);
      switch (__pyx_t_3) {
        case 0:
        if (PyDict_SetItem(__pyx_mstate_global->__pyx_d, __pyx_imported_names[__pyx_t_3], __pyx_t_4) < (0)) __PYX_ERR(0, 18, __pyx_L1_error)
        break;
      }
      __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
    }
  }
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
```

</details>

L19  🔴  (score=11)
```python
from . import Future
```
<details><summary>Show generated C (score=11)</summary>

```c
  {
    PyObject* const __pyx_imported_names[] = {__pyx_mstate_global->__pyx_n_u_Future};
    __pyx_t_1 = __Pyx_Import(__pyx_mstate_global->__pyx_n_u__7, __pyx_imported_names, 1, __pyx_mstate_global->__pyx_kp_u_Cython_Compiler, 1); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 19, __pyx_L1_error)
  }
  __pyx_t_2 = __pyx_t_1;
  __Pyx_GOTREF(__pyx_t_2);
  {
    PyObject* const __pyx_imported_names[] = {__pyx_mstate_global->__pyx_n_u_Future};
    for (__pyx_t_3=0; __pyx_t_3 < 1; __pyx_t_3++) {
      __pyx_t_4 = __Pyx_ImportFrom(__pyx_t_2, __pyx_imported_names[__pyx_t_3]); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 19, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_4);
      switch (__pyx_t_3) {
        case 0:
        if (PyDict_SetItem(__pyx_mstate_global->__pyx_d, __pyx_imported_names[__pyx_t_3], __pyx_t_4) < (0)) __PYX_ERR(0, 19, __pyx_L1_error)
        break;
      }
      __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
    }
  }
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
```

</details>

L20  ⚪  (score=0)
```python
```
L21  ⚪  (score=0)
```python
import cython
```
L22  ⚪  (score=0)
```python
```
L23  ⚪  (score=0)
```python
```
L24  🟠  (score=6)
```python
_PRINTABLE:tuple[type, ...] = cython.declare(tuple, (bytes, str, int, float, complex))
```
<details><summary>Show generated C (score=6)</summary>

```c
  __pyx_t_2 = PyTuple_Pack(5, ((PyObject *)(&PyBytes_Type)), ((PyObject *)(&PyUnicode_Type)), ((PyObject *)(&PyLong_Type)), ((PyObject *)(&PyFloat_Type)), ((PyObject *)(&PyComplex_Type))); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 24, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_XGOTREF(__pyx_v_6Cython_8Compiler_7Visitor__PRINTABLE);
  __Pyx_DECREF_SET(__pyx_v_6Cython_8Compiler_7Visitor__PRINTABLE, ((PyObject*)__pyx_t_2));
  __Pyx_GIVEREF(__pyx_t_2);
  __pyx_t_2 = 0;
```

</details>

L25  ⚪  (score=0)
```python
```
L26  ⚪  (score=0)
```python
```
L27  ⚪  (score=0)
```python
class TreeVisitor:
```
<details><summary>Show generated C (score=0)</summary>

```c
struct __pyx_vtabstruct_6Cython_8Compiler_7Visitor_TreeVisitor {
  PyObject *(*visit)(struct __pyx_obj_6Cython_8Compiler_7Visitor_TreeVisitor *, PyObject *, int __pyx_skip_dispatch);
  PyObject *(*_visit)(struct __pyx_obj_6Cython_8Compiler_7Visitor_TreeVisitor *, PyObject *);
  PyObject *(*find_handler)(struct __pyx_obj_6Cython_8Compiler_7Visitor_TreeVisitor *, PyObject *);
  PyObject *(*_visitchild)(struct __pyx_obj_6Cython_8Compiler_7Visitor_TreeVisitor *, PyObject *, PyObject *, PyObject *, PyObject *);
  PyObject *(*_visitchildren)(struct __pyx_obj_6Cython_8Compiler_7Visitor_TreeVisitor *, PyObject *, PyObject *, PyObject *);
  PyObject *(*visitchildren)(struct __pyx_obj_6Cython_8Compiler_7Visitor_TreeVisitor *, PyObject *, int __pyx_skip_dispatch, struct __pyx_opt_args_6Cython_8Compiler_7Visitor_11TreeVisitor_visitchildren *__pyx_optional_args);
  PyObject *(*_raise_compiler_error)(struct __pyx_obj_6Cython_8Compiler_7Visitor_TreeVisitor *, PyObject *, PyObject *);
};
static struct __pyx_vtabstruct_6Cython_8Compiler_7Visitor_TreeVisitor *__pyx_vtabptr_6Cython_8Compiler_7Visitor_TreeVisitor;
static PyObject *__pyx_f_6Cython_8Compiler_7Visitor_11TreeVisitor__visit(struct __pyx_obj_6Cython_8Compiler_7Visitor_TreeVisitor *, PyObject *);
static PyObject *__pyx_f_6Cython_8Compiler_7Visitor_11TreeVisitor_find_handler(struct __pyx_obj_6Cython_8Compiler_7Visitor_TreeVisitor *, PyObject *);
static PyObject *__pyx_f_6Cython_8Compiler_7Visitor_11TreeVisitor__visitchild(struct __pyx_obj_6Cython_8Compiler_7Visitor_TreeVisitor *, PyObject *, PyObject *, PyObject *, PyObject *);
static PyObject *__pyx_f_6Cython_8Compiler_7Visitor_11TreeVisitor__visitchildren(struct __pyx_obj_6Cython_8Compiler_7Visitor_TreeVisitor *, PyObject *, PyObject *, PyObject *);

```

</details>

L28  ⚪  (score=0)
```python
    """
```
L29  ⚪  (score=0)
```python
    Base class for writing visitors for a Cython tree, contains utilities for
```
L30  ⚪  (score=0)
```python
    recursing such trees using visitors. Each node is
```
L31  ⚪  (score=0)
```python
    expected to have a child_attrs iterable containing the names of attributes
```
L32  ⚪  (score=0)
```python
    containing child nodes or lists of child nodes. Lists are not considered
```
L33  ⚪  (score=0)
```python
    part of the tree structure (i.e. contained nodes are considered direct
```
L34  ⚪  (score=0)
```python
    children of the parent node).
```
L35  ⚪  (score=0)
```python
```
L36  ⚪  (score=0)
```python
    visit_children visits each of the children of a given node (see the visit_children
```
L37  ⚪  (score=0)
```python
    documentation). When recursing the tree using visit_children, an attribute
```
L38  ⚪  (score=0)
```python
    access_path is maintained which gives information about the current location
```
L39  ⚪  (score=0)
```python
    in the tree as a stack of tuples: (parent_node, attrname, index), representing
```
L40  ⚪  (score=0)
```python
    the node, attribute and optional list index that was taken in each step in the path to
```
L41  ⚪  (score=0)
```python
    the current node.
```
L42  ⚪  (score=0)
```python
```
L43  ⚪  (score=0)
```python
    Example:
```
L44  ⚪  (score=0)
```python
```
L45  ⚪  (score=0)
```python
    >>> class SampleNode(object):
```
L46  ⚪  (score=0)
```python
    ...     child_attrs = ["head", "body"]
```
L47  ⚪  (score=0)
```python
    ...     def __init__(self, value, head=None, body=None):
```
L48  ⚪  (score=0)
```python
    ...         self.value = value
```
L49  ⚪  (score=0)
```python
    ...         self.head = head
```
L50  ⚪  (score=0)
```python
    ...         self.body = body
```
L51  ⚪  (score=0)
```python
    ...     def __repr__(self): return "SampleNode(%s)" % self.value
```
L52  ⚪  (score=0)
```python
    ...
```
L53  ⚪  (score=0)
```python
    >>> tree = SampleNode(0, SampleNode(1), [SampleNode(2), SampleNode(3)])
```
L54  ⚪  (score=0)
```python
    >>> class MyVisitor(TreeVisitor):
```
L55  ⚪  (score=0)
```python
    ...     def visit_SampleNode(self, node):
```
L56  ⚪  (score=0)
```python
    ...         print("in %s %s" % (node.value, self.access_path))
```
L57  ⚪  (score=0)
```python
    ...         self.visitchildren(node)
```
L58  ⚪  (score=0)
```python
    ...         print("out %s" % node.value)
```
L59  ⚪  (score=0)
```python
    ...
```
L60  ⚪  (score=0)
```python
    >>> MyVisitor().visit(tree)
```
L61  ⚪  (score=0)
```python
    in 0 []
```
L62  ⚪  (score=0)
```python
    in 1 [(SampleNode(0), 'head', None)]
```
L63  ⚪  (score=0)
```python
    out 1
```
L64  ⚪  (score=0)
```python
    in 2 [(SampleNode(0), 'body', 0)]
```
L65  ⚪  (score=0)
```python
    out 2
```
L66  ⚪  (score=0)
```python
    in 3 [(SampleNode(0), 'body', 1)]
```
L67  ⚪  (score=0)
```python
    out 3
```
L68  ⚪  (score=0)
```python
    out 0
```
L69  ⚪  (score=0)
```python
    """
```
L70  ⚪  (score=0)
```python
    dispatch_table: dict[type, Callable[[Any], Any]]
```
L71  ⚪  (score=0)
```python
    access_path: list[tuple[Any, str, Any]]
```
L72  🔴  (score=21)
```python
    def __init__(self):
```
<details><summary>Show generated C (score=21)</summary>

```c
/* Python wrapper */
static int __pyx_pw_6Cython_8Compiler_7Visitor_11TreeVisitor_1__init__(PyObject *__pyx_v_self, PyObject *__pyx_args, PyObject *__pyx_kwds); /*proto*/
PyDoc_STRVAR(__pyx_doc_6Cython_8Compiler_7Visitor_11TreeVisitor___init__, "File: Cython/Compiler/Visitor.py (starting at line 72)");
#if CYTHON_UPDATE_DESCRIPTOR_DOC
struct wrapperbase __pyx_wrapperbase_6Cython_8Compiler_7Visitor_11TreeVisitor___init__;
#endif
static int __pyx_pw_6Cython_8Compiler_7Visitor_11TreeVisitor_1__init__(PyObject *__pyx_v_self, PyObject *__pyx_args, PyObject *__pyx_kwds) {
  CYTHON_UNUSED Py_ssize_t __pyx_nargs;
  CYTHON_UNUSED PyObject *const *__pyx_kwvalues;
  int __pyx_r;
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("__init__ (wrapper)", 0);
  #if CYTHON_ASSUME_SAFE_SIZE
  __pyx_nargs = PyTuple_GET_SIZE(__pyx_args);
  #else
  __pyx_nargs = PyTuple_Size(__pyx_args); if (unlikely(__pyx_nargs < 0)) return -1;
  #endif
  __pyx_kwvalues = __Pyx_KwValues_VARARGS(__pyx_args, __pyx_nargs);
  if (unlikely(__pyx_nargs > 0)) { __Pyx_RaiseArgtupleInvalid("__init__", 1, 0, 0, __pyx_nargs); return -1; }
  const Py_ssize_t __pyx_kwds_len = unlikely(__pyx_kwds) ? __Pyx_NumKwargs_VARARGS(__pyx_kwds) : 0;
  if (unlikely(__pyx_kwds_len < 0)) return -1;
  if (unlikely(__pyx_kwds_len > 0)) {__Pyx_RejectKeywords("__init__", __pyx_kwds); return -1;}
  __pyx_r = __pyx_pf_6Cython_8Compiler_7Visitor_11TreeVisitor___init__(((struct __pyx_obj_6Cython_8Compiler_7Visitor_TreeVisitor *)__pyx_v_self));

  /* function exit code */
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}

static int __pyx_pf_6Cython_8Compiler_7Visitor_11TreeVisitor___init__(struct __pyx_obj_6Cython_8Compiler_7Visitor_TreeVisitor *__pyx_v_self) {
  int __pyx_r;
/* … */
  /* function exit code */
  __pyx_r = 0;
  goto __pyx_L0;
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_t_1);
  __Pyx_XDECREF(__pyx_t_2);
  __Pyx_XDECREF(__pyx_t_3);
  __Pyx_XDECREF(__pyx_t_4);
  __Pyx_AddTraceback("Cython.Compiler.Visitor.TreeVisitor.__init__", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_r = -1;
  __pyx_L0:;
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}
```

</details>

L73  🟠  (score=9)
```python
        super().__init__()
```
<details><summary>Show generated C (score=9)</summary>

```c
  __pyx_t_4 = NULL;
  __pyx_t_5 = 1;
  {
    PyObject *__pyx_callargs[3] = {__pyx_t_4, ((PyObject *)__pyx_mstate_global->__pyx_ptype_6Cython_8Compiler_7Visitor_TreeVisitor), ((PyObject *)__pyx_v_self)};
    __pyx_t_3 = __Pyx_PyObject_FastCall((PyObject*)__pyx_builtin_super, __pyx_callargs+__pyx_t_5, (3-__pyx_t_5) | (__pyx_t_5*__Pyx_PY_VECTORCALL_ARGUMENTS_OFFSET));
    __Pyx_XDECREF(__pyx_t_4); __pyx_t_4 = 0;
    if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 73, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_3);
  }
  __pyx_t_2 = __pyx_t_3;
  __Pyx_INCREF(__pyx_t_2);
  __pyx_t_5 = 0;
  {
    PyObject *__pyx_callargs[2] = {__pyx_t_2, NULL};
    __pyx_t_1 = __Pyx_PyObject_FastCallMethod((PyObject*)__pyx_mstate_global->__pyx_n_u_init, __pyx_callargs+__pyx_t_5, (1-__pyx_t_5) | (1*__Pyx_PY_VECTORCALL_ARGUMENTS_OFFSET));
    __Pyx_XDECREF(__pyx_t_2); __pyx_t_2 = 0;
    __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
    if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 73, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_1);
  }
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
```

</details>

L74  🟡  (score=3)
```python
        self.dispatch_table = {}
```
<details><summary>Show generated C (score=3)</summary>

```c
  __pyx_t_1 = __Pyx_PyDict_NewPresized(0); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 74, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_GIVEREF(__pyx_t_1);
  __Pyx_GOTREF(__pyx_v_self->dispatch_table);
  __Pyx_DECREF(__pyx_v_self->dispatch_table);
  __pyx_v_self->dispatch_table = ((PyObject*)__pyx_t_1);
  __pyx_t_1 = 0;
```

</details>

L75  🟠  (score=6)
```python
        self.access_path = []
```
<details><summary>Show generated C (score=6)</summary>

```c
  __pyx_t_1 = PyList_New(0); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 75, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_GIVEREF(__pyx_t_1);
  __Pyx_GOTREF(__pyx_v_self->access_path);
  __Pyx_DECREF(__pyx_v_self->access_path);
  __pyx_v_self->access_path = ((PyObject*)__pyx_t_1);
  __pyx_t_1 = 0;
```

</details>

L76  ⚪  (score=0)
```python
```
L77  🔴  (score=48)
```python
    def dump_node(self, node):
```
<details><summary>Show generated C (score=48)</summary>

```c
/* Python wrapper */
static PyObject *__pyx_pw_6Cython_8Compiler_7Visitor_11TreeVisitor_3dump_node(PyObject *__pyx_v_self, 
#if CYTHON_METH_FASTCALL
PyObject *const *__pyx_args, Py_ssize_t __pyx_nargs, PyObject *__pyx_kwds
#else
PyObject *__pyx_args, PyObject *__pyx_kwds
#endif
); /*proto*/
PyDoc_STRVAR(__pyx_doc_6Cython_8Compiler_7Visitor_11TreeVisitor_2dump_node, "File: Cython/Compiler/Visitor.py (starting at line 77)");
static PyMethodDef __pyx_mdef_6Cython_8Compiler_7Visitor_11TreeVisitor_3dump_node = {"dump_node", (PyCFunction)(void(*)(void))(__Pyx_PyCFunction_FastCallWithKeywords)__pyx_pw_6Cython_8Compiler_7Visitor_11TreeVisitor_3dump_node, __Pyx_METH_FASTCALL|METH_KEYWORDS, __pyx_doc_6Cython_8Compiler_7Visitor_11TreeVisitor_2dump_node};
static PyObject *__pyx_pw_6Cython_8Compiler_7Visitor_11TreeVisitor_3dump_node(PyObject *__pyx_v_self, 
#if CYTHON_METH_FASTCALL
PyObject *const *__pyx_args, Py_ssize_t __pyx_nargs, PyObject *__pyx_kwds
#else
PyObject *__pyx_args, PyObject *__pyx_kwds
#endif
) {
  PyObject *__pyx_v_node = 0;
  #if !CYTHON_METH_FASTCALL
  CYTHON_UNUSED Py_ssize_t __pyx_nargs;
  #endif
  CYTHON_UNUSED PyObject *const *__pyx_kwvalues;
  PyObject *__pyx_r = 0;
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("dump_node (wrapper)", 0);
  #if !CYTHON_METH_FASTCALL
  #if CYTHON_ASSUME_SAFE_SIZE
  __pyx_nargs = PyTuple_GET_SIZE(__pyx_args);
  #else
  __pyx_nargs = PyTuple_Size(__pyx_args); if (unlikely(__pyx_nargs < 0)) return NULL;
  #endif
  #endif
  __pyx_kwvalues = __Pyx_KwValues_FASTCALL(__pyx_args, __pyx_nargs);
  {
    PyObject ** const __pyx_pyargnames[] = {&__pyx_mstate_global->__pyx_n_u_node,0};
  PyObject* values[1] = {0};
    const Py_ssize_t __pyx_kwds_len = (__pyx_kwds) ? __Pyx_NumKwargs_FASTCALL(__pyx_kwds) : 0;
    if (unlikely(__pyx_kwds_len) < 0) __PYX_ERR(0, 77, __pyx_L3_error)
    if (__pyx_kwds_len > 0) {
      switch (__pyx_nargs) {
        case  1:
        values[0] = __Pyx_ArgRef_FASTCALL(__pyx_args, 0);
        if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[0])) __PYX_ERR(0, 77, __pyx_L3_error)
        CYTHON_FALLTHROUGH;
        case  0: break;
        default: goto __pyx_L5_argtuple_error;
      }
      const Py_ssize_t kwd_pos_args = __pyx_nargs;
      if (__Pyx_ParseKeywords(__pyx_kwds, __pyx_kwvalues, __pyx_pyargnames, 0, values, kwd_pos_args, __pyx_kwds_len, "dump_node", 0) < (0)) __PYX_ERR(0, 77, __pyx_L3_error)
      for (Py_ssize_t i = __pyx_nargs; i < 1; i++) {
        if (unlikely(!values[i])) { __Pyx_RaiseArgtupleInvalid("dump_node", 1, 1, 1, i); __PYX_ERR(0, 77, __pyx_L3_error) }
      }
    } else if (unlikely(__pyx_nargs != 1)) {
      goto __pyx_L5_argtuple_error;
    } else {
      values[0] = __Pyx_ArgRef_FASTCALL(__pyx_args, 0);
      if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[0])) __PYX_ERR(0, 77, __pyx_L3_error)
    }
    __pyx_v_node = values[0];
  }
  goto __pyx_L6_skip;
  __pyx_L5_argtuple_error:;
  __Pyx_RaiseArgtupleInvalid("dump_node", 1, 1, 1, __pyx_nargs); __PYX_ERR(0, 77, __pyx_L3_error)
  __pyx_L6_skip:;
  goto __pyx_L4_argument_unpacking_done;
  __pyx_L3_error:;
  for (Py_ssize_t __pyx_temp=0; __pyx_temp < (Py_ssize_t)(sizeof(values)/sizeof(values[0])); ++__pyx_temp) {
    Py_XDECREF(values[__pyx_temp]);
  }
  __Pyx_AddTraceback("Cython.Compiler.Visitor.TreeVisitor.dump_node", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __Pyx_RefNannyFinishContext();
  return NULL;
  __pyx_L4_argument_unpacking_done:;
  __pyx_r = __pyx_pf_6Cython_8Compiler_7Visitor_11TreeVisitor_2dump_node(((struct __pyx_obj_6Cython_8Compiler_7Visitor_TreeVisitor *)__pyx_v_self), __pyx_v_node);
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

static PyObject *__pyx_pf_6Cython_8Compiler_7Visitor_11TreeVisitor_2dump_node(CYTHON_UNUSED struct __pyx_obj_6Cython_8Compiler_7Visitor_TreeVisitor *__pyx_v_self, PyObject *__pyx_v_node) {
  PyObject *__pyx_v_ignored = NULL;
  PyObject *__pyx_v_values = NULL;
  PyObject *__pyx_v_pos = NULL;
  PyObject *__pyx_v_source = NULL;
  PyObject *__pyx_v_os = NULL;
  PyObject *__pyx_v_attribute_names = NULL;
  PyObject *__pyx_v_attr = NULL;
  PyObject *__pyx_v_value = NULL;
  PyObject *__pyx_r = NULL;
/* … */
  /* function exit code */
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_t_1);
  __Pyx_XDECREF(__pyx_t_2);
  __Pyx_XDECREF(__pyx_t_4);
  __Pyx_XDECREF(__pyx_t_6);
  __Pyx_XDECREF(__pyx_t_7);
  __Pyx_AddTraceback("Cython.Compiler.Visitor.TreeVisitor.dump_node", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_r = NULL;
  __pyx_L0:;
  __Pyx_XDECREF(__pyx_v_ignored);
  __Pyx_XDECREF(__pyx_v_values);
  __Pyx_XDECREF(__pyx_v_pos);
  __Pyx_XDECREF(__pyx_v_source);
  __Pyx_XDECREF(__pyx_v_os);
  __Pyx_XDECREF(__pyx_v_attribute_names);
  __Pyx_XDECREF(__pyx_v_attr);
  __Pyx_XDECREF(__pyx_v_value);
  __Pyx_XGIVEREF(__pyx_r);
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}
/* … */
  __pyx_t_2 = __Pyx_CyFunction_New(&__pyx_mdef_6Cython_8Compiler_7Visitor_11TreeVisitor_3dump_node, __Pyx_CYFUNCTION_CCLASS, __pyx_mstate_global->__pyx_n_u_TreeVisitor_dump_node, NULL, __pyx_mstate_global->__pyx_n_u_Cython_Compiler_Visitor, __pyx_mstate_global->__pyx_d, ((PyObject *)__pyx_mstate_global->__pyx_codeobj_tab[0])); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 77, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  #if CYTHON_COMPILING_IN_CPYTHON && PY_VERSION_HEX >= 0x030E0000
  PyUnstable_Object_EnableDeferredRefcount(__pyx_t_2);
  #endif
  if (__Pyx_SetItemOnTypeDict(__pyx_mstate_global->__pyx_ptype_6Cython_8Compiler_7Visitor_TreeVisitor, __pyx_mstate_global->__pyx_n_u_dump_node, __pyx_t_2) < (0)) __PYX_ERR(0, 77, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
```

</details>

L78  🔴  (score=44)
```python
        ignored = list(node.child_attrs or []) + [
```
<details><summary>Show generated C (score=44)</summary>

```c
  __pyx_t_2 = __Pyx_PyObject_GetAttrStr(__pyx_v_node, __pyx_mstate_global->__pyx_n_u_child_attrs); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 78, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __pyx_t_3 = __Pyx_PyObject_IsTrue(__pyx_t_2); if (unlikely((__pyx_t_3 < 0))) __PYX_ERR(0, 78, __pyx_L1_error)
  if (!__pyx_t_3) {
    __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  } else {
    __Pyx_INCREF(__pyx_t_2);
    __pyx_t_1 = __pyx_t_2;
    __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
    goto __pyx_L3_bool_binop_done;
  }
  __pyx_t_2 = PyList_New(0); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 78, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_INCREF(__pyx_t_2);
  __pyx_t_1 = __pyx_t_2;
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __pyx_L3_bool_binop_done:;
  __pyx_t_2 = __Pyx_PySequence_ListKeepNew(__pyx_t_1); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 78, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __pyx_t_1 = PyList_New(5); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 78, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_INCREF(__pyx_mstate_global->__pyx_n_u_child_attrs);
  __Pyx_GIVEREF(__pyx_mstate_global->__pyx_n_u_child_attrs);
  if (__Pyx_PyList_SET_ITEM(__pyx_t_1, 0, __pyx_mstate_global->__pyx_n_u_child_attrs) != (0)) __PYX_ERR(0, 78, __pyx_L1_error);
  __Pyx_INCREF(__pyx_mstate_global->__pyx_n_u_pos);
  __Pyx_GIVEREF(__pyx_mstate_global->__pyx_n_u_pos);
  if (__Pyx_PyList_SET_ITEM(__pyx_t_1, 1, __pyx_mstate_global->__pyx_n_u_pos) != (0)) __PYX_ERR(0, 78, __pyx_L1_error);
  __Pyx_INCREF(__pyx_mstate_global->__pyx_n_u_gil_message);
  __Pyx_GIVEREF(__pyx_mstate_global->__pyx_n_u_gil_message);
  if (__Pyx_PyList_SET_ITEM(__pyx_t_1, 2, __pyx_mstate_global->__pyx_n_u_gil_message) != (0)) __PYX_ERR(0, 78, __pyx_L1_error);
  __Pyx_INCREF(__pyx_mstate_global->__pyx_n_u_cpp_message);
  __Pyx_GIVEREF(__pyx_mstate_global->__pyx_n_u_cpp_message);
  if (__Pyx_PyList_SET_ITEM(__pyx_t_1, 3, __pyx_mstate_global->__pyx_n_u_cpp_message) != (0)) __PYX_ERR(0, 78, __pyx_L1_error);
  __Pyx_INCREF(__pyx_mstate_global->__pyx_n_u_subexprs);
  __Pyx_GIVEREF(__pyx_mstate_global->__pyx_n_u_subexprs);
  if (__Pyx_PyList_SET_ITEM(__pyx_t_1, 4, __pyx_mstate_global->__pyx_n_u_subexprs) != (0)) __PYX_ERR(0, 78, __pyx_L1_error);
  __pyx_t_4 = PyNumber_Add(__pyx_t_2, __pyx_t_1); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 78, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_4);
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __pyx_v_ignored = ((PyObject*)__pyx_t_4);
  __pyx_t_4 = 0;
```

</details>

L79  ⚪  (score=0)
```python
            'child_attrs', 'pos', 'gil_message', 'cpp_message', 'subexprs']
```
L80  🟠  (score=5)
```python
        values = []
```
<details><summary>Show generated C (score=5)</summary>

```c
  __pyx_t_4 = PyList_New(0); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 80, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_4);
  __pyx_v_values = ((PyObject*)__pyx_t_4);
  __pyx_t_4 = 0;
```

</details>

L81  ⚪  (score=0)
```python
        pos = getattr(node, 'pos', None)
```
<details><summary>Show generated C (score=0)</summary>

```c
  __pyx_t_4 = __Pyx_GetAttr3(__pyx_v_node, __pyx_mstate_global->__pyx_n_u_pos, Py_None); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 81, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_4);
  __pyx_v_pos = __pyx_t_4;
  __pyx_t_4 = 0;
```

</details>

L82  🟡  (score=2)
```python
        if pos:
```
<details><summary>Show generated C (score=2)</summary>

```c
  __pyx_t_3 = __Pyx_PyObject_IsTrue(__pyx_v_pos); if (unlikely((__pyx_t_3 < 0))) __PYX_ERR(0, 82, __pyx_L1_error)
  if (__pyx_t_3) {
/* … */
  }
```

</details>

L83  🟡  (score=2)
```python
            source = pos[0]
```
<details><summary>Show generated C (score=2)</summary>

```c
    __pyx_t_4 = __Pyx_GetItemInt(__pyx_v_pos, 0, long, 1, __Pyx_PyLong_From_long, 0, 0, 1, 1, __Pyx_ReferenceSharing_OwnStrongReference); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 83, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_4);
    __pyx_v_source = __pyx_t_4;
    __pyx_t_4 = 0;
```

</details>

L84  🟡  (score=2)
```python
            if source:
```
<details><summary>Show generated C (score=2)</summary>

```c
    __pyx_t_3 = __Pyx_PyObject_IsTrue(__pyx_v_source); if (unlikely((__pyx_t_3 < 0))) __PYX_ERR(0, 84, __pyx_L1_error)
    if (__pyx_t_3) {
/* … */
    }
```

</details>

L85  🟡  (score=2)
```python
                import os.path
```
<details><summary>Show generated C (score=2)</summary>

```c
      __pyx_t_5 = __Pyx_Import(__pyx_mstate_global->__pyx_n_u_os_path, 0, 0, NULL, 0); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 85, __pyx_L1_error)
      __pyx_t_4 = __pyx_t_5;
      __Pyx_GOTREF(__pyx_t_4);
      __pyx_v_os = __pyx_t_4;
      __pyx_t_4 = 0;
```

</details>

L86  🔴  (score=13)
```python
                source = os.path.basename(source.get_description())
```
<details><summary>Show generated C (score=13)</summary>

```c
      __pyx_t_2 = __Pyx_PyObject_GetAttrStr(__pyx_v_os, __pyx_mstate_global->__pyx_n_u_path); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 86, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_2);
      __pyx_t_1 = __pyx_t_2;
      __Pyx_INCREF(__pyx_t_1);
      __pyx_t_7 = __pyx_v_source;
      __Pyx_INCREF(__pyx_t_7);
      __pyx_t_8 = 0;
      {
        PyObject *__pyx_callargs[2] = {__pyx_t_7, NULL};
        __pyx_t_6 = __Pyx_PyObject_FastCallMethod((PyObject*)__pyx_mstate_global->__pyx_n_u_get_description, __pyx_callargs+__pyx_t_8, (1-__pyx_t_8) | (1*__Pyx_PY_VECTORCALL_ARGUMENTS_OFFSET));
        __Pyx_XDECREF(__pyx_t_7); __pyx_t_7 = 0;
        if (unlikely(!__pyx_t_6)) __PYX_ERR(0, 86, __pyx_L1_error)
        __Pyx_GOTREF(__pyx_t_6);
      }
      __pyx_t_8 = 0;
      {
        PyObject *__pyx_callargs[2] = {__pyx_t_1, __pyx_t_6};
        __pyx_t_4 = __Pyx_PyObject_FastCallMethod((PyObject*)__pyx_mstate_global->__pyx_n_u_basename, __pyx_callargs+__pyx_t_8, (2-__pyx_t_8) | (1*__Pyx_PY_VECTORCALL_ARGUMENTS_OFFSET));
        __Pyx_XDECREF(__pyx_t_1); __pyx_t_1 = 0;
        __Pyx_DECREF(__pyx_t_6); __pyx_t_6 = 0;
        __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
        if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 86, __pyx_L1_error)
        __Pyx_GOTREF(__pyx_t_4);
      }
      __Pyx_DECREF_SET(__pyx_v_source, __pyx_t_4);
      __pyx_t_4 = 0;
```

</details>

L87  🔴  (score=47)
```python
            values.append('%s:%s:%s' % (source, pos[1], pos[2]))
```
<details><summary>Show generated C (score=47)</summary>

```c
    __pyx_t_4 = __Pyx_PyObject_FormatSimpleAndDecref(PyObject_Str(__pyx_v_source), __pyx_mstate_global->__pyx_empty_unicode); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 87, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_4);
    __pyx_t_2 = __Pyx_GetItemInt(__pyx_v_pos, 1, long, 1, __Pyx_PyLong_From_long, 0, 0, 1, 1, __Pyx_ReferenceSharing_OwnStrongReference); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 87, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_2);
    __pyx_t_6 = __Pyx_PyObject_FormatSimpleAndDecref(PyObject_Str(__pyx_t_2), __pyx_mstate_global->__pyx_empty_unicode); if (unlikely(!__pyx_t_6)) __PYX_ERR(0, 87, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_6);
    __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
    __pyx_t_2 = __Pyx_GetItemInt(__pyx_v_pos, 2, long, 1, __Pyx_PyLong_From_long, 0, 0, 1, 1, __Pyx_ReferenceSharing_OwnStrongReference); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 87, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_2);
    __pyx_t_1 = __Pyx_PyObject_FormatSimpleAndDecref(PyObject_Str(__pyx_t_2), __pyx_mstate_global->__pyx_empty_unicode); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 87, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_1);
    __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
    __pyx_t_9[0] = __pyx_t_4;
    __pyx_t_9[1] = __pyx_mstate_global->__pyx_kp_u_;
    __pyx_t_9[2] = __pyx_t_6;
    __pyx_t_9[3] = __pyx_mstate_global->__pyx_kp_u_;
    __pyx_t_9[4] = __pyx_t_1;
    __pyx_t_2 = __Pyx_PyUnicode_Join(__pyx_t_9, 5, __Pyx_PyUnicode_GET_LENGTH(__pyx_t_4) + 1 * 2 + __Pyx_PyUnicode_GET_LENGTH(__pyx_t_6) + __Pyx_PyUnicode_GET_LENGTH(__pyx_t_1), 127 | __Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_4) | __Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_6) | __Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_1));
    if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 87, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_2);
    __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
    __Pyx_DECREF(__pyx_t_6); __pyx_t_6 = 0;
    __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
    __pyx_t_10 = __Pyx_PyList_Append(__pyx_v_values, __pyx_t_2); if (unlikely(__pyx_t_10 == ((int)-1))) __PYX_ERR(0, 87, __pyx_L1_error)
    __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
```

</details>

L88  🟠  (score=5)
```python
        attribute_names = dir(node)
```
<details><summary>Show generated C (score=5)</summary>

```c
  __pyx_t_2 = PyObject_Dir(__pyx_v_node); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 88, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __pyx_v_attribute_names = __pyx_t_2;
  __pyx_t_2 = 0;
```

</details>

L89  🔴  (score=48)
```python
        for attr in attribute_names:
```
<details><summary>Show generated C (score=48)</summary>

```c
  if (likely(PyList_CheckExact(__pyx_v_attribute_names)) || PyTuple_CheckExact(__pyx_v_attribute_names)) {
    __pyx_t_2 = __pyx_v_attribute_names; __Pyx_INCREF(__pyx_t_2);
    __pyx_t_11 = 0;
    __pyx_t_12 = NULL;
  } else {
    __pyx_t_11 = -1; __pyx_t_2 = PyObject_GetIter(__pyx_v_attribute_names); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 89, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_2);
    __pyx_t_12 = (CYTHON_COMPILING_IN_LIMITED_API) ? PyIter_Next : __Pyx_PyObject_GetIterNextFunc(__pyx_t_2); if (unlikely(!__pyx_t_12)) __PYX_ERR(0, 89, __pyx_L1_error)
  }
  for (;;) {
    if (likely(!__pyx_t_12)) {
      if (likely(PyList_CheckExact(__pyx_t_2))) {
        {
          Py_ssize_t __pyx_temp = __Pyx_PyList_GET_SIZE(__pyx_t_2);
          #if !CYTHON_ASSUME_SAFE_SIZE
          if (unlikely((__pyx_temp < 0))) __PYX_ERR(0, 89, __pyx_L1_error)
          #endif
          if (__pyx_t_11 >= __pyx_temp) break;
        }
        __pyx_t_1 = __Pyx_PyList_GetItemRefFast(__pyx_t_2, __pyx_t_11, __Pyx_ReferenceSharing_OwnStrongReference);
        ++__pyx_t_11;
      } else {
        {
          Py_ssize_t __pyx_temp = __Pyx_PyTuple_GET_SIZE(__pyx_t_2);
          #if !CYTHON_ASSUME_SAFE_SIZE
          if (unlikely((__pyx_temp < 0))) __PYX_ERR(0, 89, __pyx_L1_error)
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
      if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 89, __pyx_L1_error)
    } else {
      __pyx_t_1 = __pyx_t_12(__pyx_t_2);
      if (unlikely(!__pyx_t_1)) {
        PyObject* exc_type = PyErr_Occurred();
        if (exc_type) {
          if (unlikely(!__Pyx_PyErr_GivenExceptionMatches(exc_type, PyExc_StopIteration))) __PYX_ERR(0, 89, __pyx_L1_error)
          PyErr_Clear();
        }
        break;
      }
    }
    __Pyx_GOTREF(__pyx_t_1);
    __Pyx_XDECREF_SET(__pyx_v_attr, __pyx_t_1);
    __pyx_t_1 = 0;
/* … */
    __pyx_L7_continue:;
  }
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
```

</details>

L90  🟡  (score=2)
```python
            if attr in ignored:
```
<details><summary>Show generated C (score=2)</summary>

```c
    __pyx_t_3 = (__Pyx_PySequence_ContainsTF(__pyx_v_attr, __pyx_v_ignored, Py_EQ)); if (unlikely((__pyx_t_3 < 0))) __PYX_ERR(0, 90, __pyx_L1_error)
    if (__pyx_t_3) {
/* … */
    }
```

</details>

L91  ⚪  (score=0)
```python
                continue
```
<details><summary>Show generated C (score=0)</summary>

```c
      goto __pyx_L7_continue;
```

</details>

L92  🔴  (score=14)
```python
            if attr.startswith('_') or attr.endswith('_'):
```
<details><summary>Show generated C (score=14)</summary>

```c
    __pyx_t_6 = __pyx_v_attr;
    __Pyx_INCREF(__pyx_t_6);
    __pyx_t_8 = 0;
    {
      PyObject *__pyx_callargs[2] = {__pyx_t_6, __pyx_mstate_global->__pyx_n_u__2};
      __pyx_t_1 = __Pyx_PyObject_FastCallMethod((PyObject*)__pyx_mstate_global->__pyx_n_u_startswith, __pyx_callargs+__pyx_t_8, (2-__pyx_t_8) | (1*__Pyx_PY_VECTORCALL_ARGUMENTS_OFFSET));
      __Pyx_XDECREF(__pyx_t_6); __pyx_t_6 = 0;
      if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 92, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_1);
    }
    __pyx_t_13 = __Pyx_PyObject_IsTrue(__pyx_t_1); if (unlikely((__pyx_t_13 < 0))) __PYX_ERR(0, 92, __pyx_L1_error)
    __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
    if (!__pyx_t_13) {
    } else {
      __pyx_t_3 = __pyx_t_13;
      goto __pyx_L11_bool_binop_done;
    }
    __pyx_t_6 = __pyx_v_attr;
    __Pyx_INCREF(__pyx_t_6);
    __pyx_t_8 = 0;
    {
      PyObject *__pyx_callargs[2] = {__pyx_t_6, __pyx_mstate_global->__pyx_n_u__2};
      __pyx_t_1 = __Pyx_PyObject_FastCallMethod((PyObject*)__pyx_mstate_global->__pyx_n_u_endswith, __pyx_callargs+__pyx_t_8, (2-__pyx_t_8) | (1*__Pyx_PY_VECTORCALL_ARGUMENTS_OFFSET));
      __Pyx_XDECREF(__pyx_t_6); __pyx_t_6 = 0;
      if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 92, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_1);
    }
    __pyx_t_13 = __Pyx_PyObject_IsTrue(__pyx_t_1); if (unlikely((__pyx_t_13 < 0))) __PYX_ERR(0, 92, __pyx_L1_error)
    __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
    __pyx_t_3 = __pyx_t_13;
    __pyx_L11_bool_binop_done:;
    if (__pyx_t_3) {
/* … */
    }
```

</details>

L93  ⚪  (score=0)
```python
                continue
```
<details><summary>Show generated C (score=0)</summary>

```c
      goto __pyx_L7_continue;
```

</details>

L94  🔴  (score=11)
```python
            try:
```
<details><summary>Show generated C (score=11)</summary>

```c
    {
      /*try:*/ {
/* … */
      }
      __Pyx_XDECREF(__pyx_t_5); __pyx_t_5 = 0;
      __Pyx_XDECREF(__pyx_t_14); __pyx_t_14 = 0;
      __Pyx_XDECREF(__pyx_t_15); __pyx_t_15 = 0;
      goto __pyx_L20_try_end;
      __pyx_L13_error:;
      __Pyx_XDECREF(__pyx_t_1); __pyx_t_1 = 0;
      __Pyx_XDECREF(__pyx_t_4); __pyx_t_4 = 0;
      __Pyx_XDECREF(__pyx_t_6); __pyx_t_6 = 0;
      __Pyx_XDECREF(__pyx_t_7); __pyx_t_7 = 0;
/* … */
      __pyx_L15_except_error:;
      __Pyx_XGIVEREF(__pyx_t_5);
      __Pyx_XGIVEREF(__pyx_t_14);
      __Pyx_XGIVEREF(__pyx_t_15);
      __Pyx_ExceptionReset(__pyx_t_5, __pyx_t_14, __pyx_t_15);
      goto __pyx_L1_error;
      __pyx_L19_try_continue:;
      __Pyx_XGIVEREF(__pyx_t_5);
      __Pyx_XGIVEREF(__pyx_t_14);
      __Pyx_XGIVEREF(__pyx_t_15);
      __Pyx_ExceptionReset(__pyx_t_5, __pyx_t_14, __pyx_t_15);
      goto __pyx_L7_continue;
      __pyx_L20_try_end:;
    }
```

</details>

L95  🟡  (score=3)
```python
                value = getattr(node, attr)
```
<details><summary>Show generated C (score=3)</summary>

```c
        __pyx_t_1 = __Pyx_GetAttr(__pyx_v_node, __pyx_v_attr); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 95, __pyx_L13_error)
        __Pyx_GOTREF(__pyx_t_1);
        __Pyx_XDECREF_SET(__pyx_v_value, __pyx_t_1);
        __pyx_t_1 = 0;
```

</details>

L96  🟠  (score=6)
```python
            except AttributeError:
```
<details><summary>Show generated C (score=6)</summary>

```c
      __pyx_t_16 = __Pyx_PyErr_ExceptionMatches(((PyObject *)(((PyTypeObject*)PyExc_AttributeError))));
      if (__pyx_t_16) {
        __Pyx_AddTraceback("Cython.Compiler.Visitor.TreeVisitor.dump_node", __pyx_clineno, __pyx_lineno, __pyx_filename);
        if (__Pyx_GetException(&__pyx_t_1, &__pyx_t_6, &__pyx_t_4) < 0) __PYX_ERR(0, 96, __pyx_L15_except_error)
        __Pyx_XGOTREF(__pyx_t_1);
        __Pyx_XGOTREF(__pyx_t_6);
        __Pyx_XGOTREF(__pyx_t_4);
```

</details>

L97  🟡  (score=3)
```python
                continue
```
<details><summary>Show generated C (score=3)</summary>

```c
        goto __pyx_L21_except_continue;
        __pyx_L21_except_continue:;
        __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
        __Pyx_DECREF(__pyx_t_6); __pyx_t_6 = 0;
        __Pyx_XDECREF(__pyx_t_4); __pyx_t_4 = 0;
        goto __pyx_L19_try_continue;
      }
      goto __pyx_L15_except_error;
```

</details>

L98  🟡  (score=2)
```python
            if value is None or value == 0:
```
<details><summary>Show generated C (score=2)</summary>

```c
    __pyx_t_13 = (__pyx_v_value == Py_None);
    if (!__pyx_t_13) {
    } else {
      __pyx_t_3 = __pyx_t_13;
      goto __pyx_L24_bool_binop_done;
    }
    __pyx_t_13 = (__Pyx_PyLong_BoolEqObjC(__pyx_v_value, __pyx_mstate_global->__pyx_int_0, 0, 0)); if (unlikely((__pyx_t_13 < 0))) __PYX_ERR(0, 98, __pyx_L1_error)
    __pyx_t_3 = __pyx_t_13;
    __pyx_L24_bool_binop_done:;
    if (__pyx_t_3) {
/* … */
    }
```

</details>

L99  ⚪  (score=0)
```python
                continue
```
<details><summary>Show generated C (score=0)</summary>

```c
      goto __pyx_L7_continue;
```

</details>

L100  🟠  (score=5)
```python
            elif isinstance(value, list):
```
<details><summary>Show generated C (score=5)</summary>

```c
    __pyx_t_3 = PyList_Check(__pyx_v_value); 
    if (__pyx_t_3) {
/* … */
      goto __pyx_L23;
    }
```

</details>

L101  🔴  (score=17)
```python
                value = '[...]/%d' % len(value)
```
<details><summary>Show generated C (score=17)</summary>

```c
      __pyx_t_17 = PyObject_Length(__pyx_v_value); if (unlikely(__pyx_t_17 == ((Py_ssize_t)-1))) __PYX_ERR(0, 101, __pyx_L1_error)
      __pyx_t_4 = PyLong_FromSsize_t(__pyx_t_17); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 101, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_4);
      __pyx_t_6 = PyUnicode_Format(__pyx_mstate_global->__pyx_kp_u_d, __pyx_t_4); if (unlikely(!__pyx_t_6)) __PYX_ERR(0, 101, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_6);
      __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
      __Pyx_DECREF_SET(__pyx_v_value, __pyx_t_6);
      __pyx_t_6 = 0;
```

</details>

L102  🟠  (score=7)
```python
            elif not isinstance(value, _PRINTABLE):
```
<details><summary>Show generated C (score=7)</summary>

```c
    __pyx_t_6 = __pyx_v_6Cython_8Compiler_7Visitor__PRINTABLE;
    __Pyx_INCREF(__pyx_t_6);
    __pyx_t_3 = PyObject_IsInstance(__pyx_v_value, __pyx_t_6); if (unlikely(__pyx_t_3 == ((int)-1))) __PYX_ERR(0, 102, __pyx_L1_error)
    __Pyx_DECREF(__pyx_t_6); __pyx_t_6 = 0;
    __pyx_t_13 = (!__pyx_t_3);
    if (__pyx_t_13) {
/* … */
    }
```

</details>

L103  ⚪  (score=0)
```python
                continue
```
<details><summary>Show generated C (score=0)</summary>

```c
      goto __pyx_L7_continue;
```

</details>

L104  ⚪  (score=0)
```python
            else:
```
L105  🟠  (score=6)
```python
                value = repr(value)
```
<details><summary>Show generated C (score=6)</summary>

```c
    /*else*/ {
      __pyx_t_6 = PyObject_Repr(__pyx_v_value); if (unlikely(!__pyx_t_6)) __PYX_ERR(0, 105, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_6);
      __Pyx_DECREF_SET(__pyx_v_value, __pyx_t_6);
      __pyx_t_6 = 0;
    }
    __pyx_L23:;
```

</details>

L106  🔴  (score=29)
```python
            values.append('%s = %s' % (attr, value))
```
<details><summary>Show generated C (score=29)</summary>

```c
    __pyx_t_6 = __Pyx_PyObject_FormatSimpleAndDecref(PyObject_Str(__pyx_v_attr), __pyx_mstate_global->__pyx_empty_unicode); if (unlikely(!__pyx_t_6)) __PYX_ERR(0, 106, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_6);
    __pyx_t_4 = __Pyx_PyObject_FormatSimpleAndDecref(PyObject_Str(__pyx_v_value), __pyx_mstate_global->__pyx_empty_unicode); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 106, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_4);
    __pyx_t_18[0] = __pyx_t_6;
    __pyx_t_18[1] = __pyx_mstate_global->__pyx_kp_u__3;
    __pyx_t_18[2] = __pyx_t_4;
    __pyx_t_1 = __Pyx_PyUnicode_Join(__pyx_t_18, 3, __Pyx_PyUnicode_GET_LENGTH(__pyx_t_6) + 3 + __Pyx_PyUnicode_GET_LENGTH(__pyx_t_4), 127 | __Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_6) | __Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_4));
    if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 106, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_1);
    __Pyx_DECREF(__pyx_t_6); __pyx_t_6 = 0;
    __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
    __pyx_t_10 = __Pyx_PyList_Append(__pyx_v_values, __pyx_t_1); if (unlikely(__pyx_t_10 == ((int)-1))) __PYX_ERR(0, 106, __pyx_L1_error)
    __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
```

</details>

L107  🔴  (score=31)
```python
        return '%s(%s)' % (node.__class__.__name__, ',\n    '.join(values))
```
<details><summary>Show generated C (score=31)</summary>

```c
  __Pyx_XDECREF(__pyx_r);
  __pyx_t_2 = __Pyx_PyObject_GetAttrStr(__pyx_v_node, __pyx_mstate_global->__pyx_n_u_class); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 107, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __pyx_t_1 = __Pyx_PyObject_GetAttrStr(__pyx_t_2, __pyx_mstate_global->__pyx_n_u_name); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 107, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __pyx_t_2 = __Pyx_PyObject_FormatSimpleAndDecref(PyObject_Str(__pyx_t_1), __pyx_mstate_global->__pyx_empty_unicode); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 107, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __pyx_t_1 = PyUnicode_Join(__pyx_mstate_global->__pyx_kp_u__5, __pyx_v_values); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 107, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __pyx_t_19[0] = __pyx_t_2;
  __pyx_t_19[1] = __pyx_mstate_global->__pyx_kp_u__4;
  __pyx_t_19[2] = __pyx_t_1;
  __pyx_t_19[3] = __pyx_mstate_global->__pyx_kp_u__6;
  __pyx_t_4 = __Pyx_PyUnicode_Join(__pyx_t_19, 4, __Pyx_PyUnicode_GET_LENGTH(__pyx_t_2) + 1 * 2 + __Pyx_PyUnicode_GET_LENGTH(__pyx_t_1), 127 | __Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_2) | __Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_1));
  if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 107, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_4);
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __pyx_r = __pyx_t_4;
  __pyx_t_4 = 0;
  goto __pyx_L0;
```

</details>

L108  ⚪  (score=0)
```python
```
L109  🔴  (score=49)
```python
    def _find_node_path(self, stacktrace):
```
<details><summary>Show generated C (score=49)</summary>

```c
/* Python wrapper */
static PyObject *__pyx_pw_6Cython_8Compiler_7Visitor_11TreeVisitor_5_find_node_path(PyObject *__pyx_v_self, 
#if CYTHON_METH_FASTCALL
PyObject *const *__pyx_args, Py_ssize_t __pyx_nargs, PyObject *__pyx_kwds
#else
PyObject *__pyx_args, PyObject *__pyx_kwds
#endif
); /*proto*/
PyDoc_STRVAR(__pyx_doc_6Cython_8Compiler_7Visitor_11TreeVisitor_4_find_node_path, "File: Cython/Compiler/Visitor.py (starting at line 109)");
static PyMethodDef __pyx_mdef_6Cython_8Compiler_7Visitor_11TreeVisitor_5_find_node_path = {"_find_node_path", (PyCFunction)(void(*)(void))(__Pyx_PyCFunction_FastCallWithKeywords)__pyx_pw_6Cython_8Compiler_7Visitor_11TreeVisitor_5_find_node_path, __Pyx_METH_FASTCALL|METH_KEYWORDS, __pyx_doc_6Cython_8Compiler_7Visitor_11TreeVisitor_4_find_node_path};
static PyObject *__pyx_pw_6Cython_8Compiler_7Visitor_11TreeVisitor_5_find_node_path(PyObject *__pyx_v_self, 
#if CYTHON_METH_FASTCALL
PyObject *const *__pyx_args, Py_ssize_t __pyx_nargs, PyObject *__pyx_kwds
#else
PyObject *__pyx_args, PyObject *__pyx_kwds
#endif
) {
  PyObject *__pyx_v_stacktrace = 0;
  #if !CYTHON_METH_FASTCALL
  CYTHON_UNUSED Py_ssize_t __pyx_nargs;
  #endif
  CYTHON_UNUSED PyObject *const *__pyx_kwvalues;
  PyObject *__pyx_r = 0;
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("_find_node_path (wrapper)", 0);
  #if !CYTHON_METH_FASTCALL
  #if CYTHON_ASSUME_SAFE_SIZE
  __pyx_nargs = PyTuple_GET_SIZE(__pyx_args);
  #else
  __pyx_nargs = PyTuple_Size(__pyx_args); if (unlikely(__pyx_nargs < 0)) return NULL;
  #endif
  #endif
  __pyx_kwvalues = __Pyx_KwValues_FASTCALL(__pyx_args, __pyx_nargs);
  {
    PyObject ** const __pyx_pyargnames[] = {&__pyx_mstate_global->__pyx_n_u_stacktrace,0};
  PyObject* values[1] = {0};
    const Py_ssize_t __pyx_kwds_len = (__pyx_kwds) ? __Pyx_NumKwargs_FASTCALL(__pyx_kwds) : 0;
    if (unlikely(__pyx_kwds_len) < 0) __PYX_ERR(0, 109, __pyx_L3_error)
    if (__pyx_kwds_len > 0) {
      switch (__pyx_nargs) {
        case  1:
        values[0] = __Pyx_ArgRef_FASTCALL(__pyx_args, 0);
        if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[0])) __PYX_ERR(0, 109, __pyx_L3_error)
        CYTHON_FALLTHROUGH;
        case  0: break;
        default: goto __pyx_L5_argtuple_error;
      }
      const Py_ssize_t kwd_pos_args = __pyx_nargs;
      if (__Pyx_ParseKeywords(__pyx_kwds, __pyx_kwvalues, __pyx_pyargnames, 0, values, kwd_pos_args, __pyx_kwds_len, "_find_node_path", 0) < (0)) __PYX_ERR(0, 109, __pyx_L3_error)
      for (Py_ssize_t i = __pyx_nargs; i < 1; i++) {
        if (unlikely(!values[i])) { __Pyx_RaiseArgtupleInvalid("_find_node_path", 1, 1, 1, i); __PYX_ERR(0, 109, __pyx_L3_error) }
      }
    } else if (unlikely(__pyx_nargs != 1)) {
      goto __pyx_L5_argtuple_error;
    } else {
      values[0] = __Pyx_ArgRef_FASTCALL(__pyx_args, 0);
      if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[0])) __PYX_ERR(0, 109, __pyx_L3_error)
    }
    __pyx_v_stacktrace = values[0];
  }
  goto __pyx_L6_skip;
  __pyx_L5_argtuple_error:;
  __Pyx_RaiseArgtupleInvalid("_find_node_path", 1, 1, 1, __pyx_nargs); __PYX_ERR(0, 109, __pyx_L3_error)
  __pyx_L6_skip:;
  goto __pyx_L4_argument_unpacking_done;
  __pyx_L3_error:;
  for (Py_ssize_t __pyx_temp=0; __pyx_temp < (Py_ssize_t)(sizeof(values)/sizeof(values[0])); ++__pyx_temp) {
    Py_XDECREF(values[__pyx_temp]);
  }
  __Pyx_AddTraceback("Cython.Compiler.Visitor.TreeVisitor._find_node_path", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __Pyx_RefNannyFinishContext();
  return NULL;
  __pyx_L4_argument_unpacking_done:;
  __pyx_r = __pyx_pf_6Cython_8Compiler_7Visitor_11TreeVisitor_4_find_node_path(((struct __pyx_obj_6Cython_8Compiler_7Visitor_TreeVisitor *)__pyx_v_self), __pyx_v_stacktrace);
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

static PyObject *__pyx_pf_6Cython_8Compiler_7Visitor_11TreeVisitor_4_find_node_path(CYTHON_UNUSED struct __pyx_obj_6Cython_8Compiler_7Visitor_TreeVisitor *__pyx_v_self, PyObject *__pyx_v_stacktrace) {
  PyObject *__pyx_v_os = NULL;
  PyObject *__pyx_v_last_traceback = NULL;
  PyObject *__pyx_v_nodes = NULL;
  PyObject *__pyx_v_frame = NULL;
  PyObject *__pyx_v_node = NULL;
  PyObject *__pyx_v_code = NULL;
  PyObject *__pyx_v_method_name = NULL;
  PyObject *__pyx_v_pos = NULL;
  PyObject *__pyx_r = NULL;
  __Pyx_INCREF(__pyx_v_stacktrace);
/* … */
  /* function exit code */
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_t_1);
  __Pyx_XDECREF(__pyx_t_4);
  __Pyx_XDECREF(__pyx_t_5);
  __Pyx_XDECREF(__pyx_t_7);
  __Pyx_AddTraceback("Cython.Compiler.Visitor.TreeVisitor._find_node_path", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_r = NULL;
  __pyx_L0:;
  __Pyx_XDECREF(__pyx_v_os);
  __Pyx_XDECREF(__pyx_v_last_traceback);
  __Pyx_XDECREF(__pyx_v_nodes);
  __Pyx_XDECREF(__pyx_v_frame);
  __Pyx_XDECREF(__pyx_v_node);
  __Pyx_XDECREF(__pyx_v_code);
  __Pyx_XDECREF(__pyx_v_method_name);
  __Pyx_XDECREF(__pyx_v_pos);
  __Pyx_XDECREF(__pyx_v_stacktrace);
  __Pyx_XGIVEREF(__pyx_r);
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}
/* … */
  __pyx_t_2 = __Pyx_CyFunction_New(&__pyx_mdef_6Cython_8Compiler_7Visitor_11TreeVisitor_5_find_node_path, __Pyx_CYFUNCTION_CCLASS, __pyx_mstate_global->__pyx_n_u_TreeVisitor__find_node_path, NULL, __pyx_mstate_global->__pyx_n_u_Cython_Compiler_Visitor, __pyx_mstate_global->__pyx_d, ((PyObject *)__pyx_mstate_global->__pyx_codeobj_tab[1])); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 109, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  #if CYTHON_COMPILING_IN_CPYTHON && PY_VERSION_HEX >= 0x030E0000
  PyUnstable_Object_EnableDeferredRefcount(__pyx_t_2);
  #endif
  if (__Pyx_SetItemOnTypeDict(__pyx_mstate_global->__pyx_ptype_6Cython_8Compiler_7Visitor_TreeVisitor, __pyx_mstate_global->__pyx_n_u_find_node_path, __pyx_t_2) < (0)) __PYX_ERR(0, 109, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
```

</details>

L110  🟡  (score=2)
```python
        import os.path
```
<details><summary>Show generated C (score=2)</summary>

```c
  __pyx_t_2 = __Pyx_Import(__pyx_mstate_global->__pyx_n_u_os_path, 0, 0, NULL, 0); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 110, __pyx_L1_error)
  __pyx_t_1 = __pyx_t_2;
  __Pyx_GOTREF(__pyx_t_1);
  __pyx_v_os = __pyx_t_1;
  __pyx_t_1 = 0;
```

</details>

L111  🟡  (score=1)
```python
        last_traceback = stacktrace
```
<details><summary>Show generated C (score=1)</summary>

```c
  __Pyx_INCREF(__pyx_v_stacktrace);
  __pyx_v_last_traceback = __pyx_v_stacktrace;
```

</details>

L112  🟠  (score=5)
```python
        nodes = []
```
<details><summary>Show generated C (score=5)</summary>

```c
  __pyx_t_1 = PyList_New(0); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 112, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __pyx_v_nodes = ((PyObject*)__pyx_t_1);
  __pyx_t_1 = 0;
```

</details>

L113  🟡  (score=2)
```python
        while hasattr(stacktrace, 'tb_frame'):
```
<details><summary>Show generated C (score=2)</summary>

```c
  while (1) {
    __pyx_t_3 = __Pyx_HasAttr(__pyx_v_stacktrace, __pyx_mstate_global->__pyx_n_u_tb_frame); if (unlikely(__pyx_t_3 == ((int)-1))) __PYX_ERR(0, 113, __pyx_L1_error)
    if (!__pyx_t_3) break;
```

</details>

L114  🟡  (score=3)
```python
            frame = stacktrace.tb_frame
```
<details><summary>Show generated C (score=3)</summary>

```c
    __pyx_t_1 = __Pyx_PyObject_GetAttrStr(__pyx_v_stacktrace, __pyx_mstate_global->__pyx_n_u_tb_frame); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 114, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_1);
    __Pyx_XDECREF_SET(__pyx_v_frame, __pyx_t_1);
    __pyx_t_1 = 0;
```

</details>

L115  🟠  (score=8)
```python
            node = frame.f_locals.get('self')
```
<details><summary>Show generated C (score=8)</summary>

```c
    __pyx_t_5 = __Pyx_PyObject_GetAttrStr(__pyx_v_frame, __pyx_mstate_global->__pyx_n_u_f_locals); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 115, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_5);
    __pyx_t_4 = __pyx_t_5;
    __Pyx_INCREF(__pyx_t_4);
    __pyx_t_6 = 0;
    {
      PyObject *__pyx_callargs[2] = {__pyx_t_4, __pyx_mstate_global->__pyx_n_u_self};
      __pyx_t_1 = __Pyx_PyObject_FastCallMethod((PyObject*)__pyx_mstate_global->__pyx_n_u_get, __pyx_callargs+__pyx_t_6, (2-__pyx_t_6) | (1*__Pyx_PY_VECTORCALL_ARGUMENTS_OFFSET));
      __Pyx_XDECREF(__pyx_t_4); __pyx_t_4 = 0;
      __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
      if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 115, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_1);
    }
    __Pyx_XDECREF_SET(__pyx_v_node, __pyx_t_1);
    __pyx_t_1 = 0;
```

</details>

L116  🔴  (score=11)
```python
            if isinstance(node, Nodes.Node):
```
<details><summary>Show generated C (score=11)</summary>

```c
    __Pyx_GetModuleGlobalName(__pyx_t_1, __pyx_mstate_global->__pyx_n_u_Nodes); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 116, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_1);
    __pyx_t_5 = __Pyx_PyObject_GetAttrStr(__pyx_t_1, __pyx_mstate_global->__pyx_n_u_Node); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 116, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_5);
    __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
    __pyx_t_3 = PyObject_IsInstance(__pyx_v_node, __pyx_t_5); if (unlikely(__pyx_t_3 == ((int)-1))) __PYX_ERR(0, 116, __pyx_L1_error)
    __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
    if (__pyx_t_3) {
/* … */
    }
```

</details>

L117  🟡  (score=3)
```python
                code = frame.f_code
```
<details><summary>Show generated C (score=3)</summary>

```c
      __pyx_t_5 = __Pyx_PyObject_GetAttrStr(__pyx_v_frame, __pyx_mstate_global->__pyx_n_u_f_code); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 117, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_5);
      __Pyx_XDECREF_SET(__pyx_v_code, __pyx_t_5);
      __pyx_t_5 = 0;
```

</details>

L118  🟡  (score=3)
```python
                method_name = code.co_name
```
<details><summary>Show generated C (score=3)</summary>

```c
      __pyx_t_5 = __Pyx_PyObject_GetAttrStr(__pyx_v_code, __pyx_mstate_global->__pyx_n_u_co_name); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 118, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_5);
      __Pyx_XDECREF_SET(__pyx_v_method_name, __pyx_t_5);
      __pyx_t_5 = 0;
```

</details>

L119  🔴  (score=20)
```python
                pos = (os.path.basename(code.co_filename),
```
<details><summary>Show generated C (score=20)</summary>

```c
      __pyx_t_4 = __Pyx_PyObject_GetAttrStr(__pyx_v_os, __pyx_mstate_global->__pyx_n_u_path); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 119, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_4);
      __pyx_t_1 = __pyx_t_4;
      __Pyx_INCREF(__pyx_t_1);
      __pyx_t_7 = __Pyx_PyObject_GetAttrStr(__pyx_v_code, __pyx_mstate_global->__pyx_n_u_co_filename); if (unlikely(!__pyx_t_7)) __PYX_ERR(0, 119, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_7);
      __pyx_t_6 = 0;
      {
        PyObject *__pyx_callargs[2] = {__pyx_t_1, __pyx_t_7};
        __pyx_t_5 = __Pyx_PyObject_FastCallMethod((PyObject*)__pyx_mstate_global->__pyx_n_u_basename, __pyx_callargs+__pyx_t_6, (2-__pyx_t_6) | (1*__Pyx_PY_VECTORCALL_ARGUMENTS_OFFSET));
        __Pyx_XDECREF(__pyx_t_1); __pyx_t_1 = 0;
        __Pyx_DECREF(__pyx_t_7); __pyx_t_7 = 0;
        __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
        if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 119, __pyx_L1_error)
        __Pyx_GOTREF(__pyx_t_5);
      }
/* … */
      __pyx_t_7 = PyTuple_New(2); if (unlikely(!__pyx_t_7)) __PYX_ERR(0, 119, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_7);
      __Pyx_GIVEREF(__pyx_t_5);
      if (__Pyx_PyTuple_SET_ITEM(__pyx_t_7, 0, __pyx_t_5) != (0)) __PYX_ERR(0, 119, __pyx_L1_error);
      __Pyx_GIVEREF(__pyx_t_4);
      if (__Pyx_PyTuple_SET_ITEM(__pyx_t_7, 1, __pyx_t_4) != (0)) __PYX_ERR(0, 119, __pyx_L1_error);
      __pyx_t_5 = 0;
      __pyx_t_4 = 0;
      __Pyx_XDECREF_SET(__pyx_v_pos, ((PyObject*)__pyx_t_7));
      __pyx_t_7 = 0;
```

</details>

L120  🟡  (score=2)
```python
                       frame.f_lineno)
```
<details><summary>Show generated C (score=2)</summary>

```c
      __pyx_t_4 = __Pyx_PyObject_GetAttrStr(__pyx_v_frame, __pyx_mstate_global->__pyx_n_u_f_lineno); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 120, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_4);
```

</details>

L121  🔴  (score=17)
```python
                nodes.append((node, method_name, pos))
```
<details><summary>Show generated C (score=17)</summary>

```c
      __pyx_t_7 = PyTuple_New(3); if (unlikely(!__pyx_t_7)) __PYX_ERR(0, 121, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_7);
      __Pyx_INCREF(__pyx_v_node);
      __Pyx_GIVEREF(__pyx_v_node);
      if (__Pyx_PyTuple_SET_ITEM(__pyx_t_7, 0, __pyx_v_node) != (0)) __PYX_ERR(0, 121, __pyx_L1_error);
      __Pyx_INCREF(__pyx_v_method_name);
      __Pyx_GIVEREF(__pyx_v_method_name);
      if (__Pyx_PyTuple_SET_ITEM(__pyx_t_7, 1, __pyx_v_method_name) != (0)) __PYX_ERR(0, 121, __pyx_L1_error);
      __Pyx_INCREF(__pyx_v_pos);
      __Pyx_GIVEREF(__pyx_v_pos);
      if (__Pyx_PyTuple_SET_ITEM(__pyx_t_7, 2, __pyx_v_pos) != (0)) __PYX_ERR(0, 121, __pyx_L1_error);
      __pyx_t_8 = __Pyx_PyList_Append(__pyx_v_nodes, __pyx_t_7); if (unlikely(__pyx_t_8 == ((int)-1))) __PYX_ERR(0, 121, __pyx_L1_error)
      __Pyx_DECREF(__pyx_t_7); __pyx_t_7 = 0;
```

</details>

L122  🟡  (score=2)
```python
                last_traceback = stacktrace
```
<details><summary>Show generated C (score=2)</summary>

```c
      __Pyx_INCREF(__pyx_v_stacktrace);
      __Pyx_DECREF_SET(__pyx_v_last_traceback, __pyx_v_stacktrace);
```

</details>

L123  🟡  (score=3)
```python
            stacktrace = stacktrace.tb_next
```
<details><summary>Show generated C (score=3)</summary>

```c
    __pyx_t_7 = __Pyx_PyObject_GetAttrStr(__pyx_v_stacktrace, __pyx_mstate_global->__pyx_n_u_tb_next); if (unlikely(!__pyx_t_7)) __PYX_ERR(0, 123, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_7);
    __Pyx_DECREF_SET(__pyx_v_stacktrace, __pyx_t_7);
    __pyx_t_7 = 0;
  }
```

</details>

L124  🔴  (score=12)
```python
        return (last_traceback, nodes)
```
<details><summary>Show generated C (score=12)</summary>

```c
  __Pyx_XDECREF(__pyx_r);
  __pyx_t_7 = PyTuple_New(2); if (unlikely(!__pyx_t_7)) __PYX_ERR(0, 124, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_7);
  __Pyx_INCREF(__pyx_v_last_traceback);
  __Pyx_GIVEREF(__pyx_v_last_traceback);
  if (__Pyx_PyTuple_SET_ITEM(__pyx_t_7, 0, __pyx_v_last_traceback) != (0)) __PYX_ERR(0, 124, __pyx_L1_error);
  __Pyx_INCREF(__pyx_v_nodes);
  __Pyx_GIVEREF(__pyx_v_nodes);
  if (__Pyx_PyTuple_SET_ITEM(__pyx_t_7, 1, __pyx_v_nodes) != (0)) __PYX_ERR(0, 124, __pyx_L1_error);
  __pyx_r = __pyx_t_7;
  __pyx_t_7 = 0;
  goto __pyx_L0;
```

</details>

L125  ⚪  (score=0)
```python
```
L126  🔴  (score=18)
```python
    def _raise_compiler_error(self, child, e):
```
<details><summary>Show generated C (score=18)</summary>

```c
static PyObject *__pyx_f_6Cython_8Compiler_7Visitor_11TreeVisitor__raise_compiler_error(struct __pyx_obj_6Cython_8Compiler_7Visitor_TreeVisitor *__pyx_v_self, PyObject *__pyx_v_child, PyObject *__pyx_v_e) {
  PyObject *__pyx_v_trace = NULL;
  PyObject *__pyx_v_parent = NULL;
  PyObject *__pyx_v_attribute = NULL;
  PyObject *__pyx_v_index = NULL;
  PyObject *__pyx_v_node = NULL;
  PyObject *__pyx_v_stacktrace = NULL;
  PyObject *__pyx_v_called_nodes = NULL;
  PyObject *__pyx_v_last_node = NULL;
  PyObject *__pyx_v_method_name = NULL;
  PyObject *__pyx_v_pos = NULL;
  PyObject *__pyx_r = NULL;
/* … */
  /* function exit code */
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_t_1);
  __Pyx_XDECREF(__pyx_t_3);
  __Pyx_XDECREF(__pyx_t_4);
  __Pyx_XDECREF(__pyx_t_5);
  __Pyx_XDECREF(__pyx_t_6);
  __Pyx_XDECREF(__pyx_t_7);
  __Pyx_AddTraceback("Cython.Compiler.Visitor.TreeVisitor._raise_compiler_error", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_r = 0;
  __Pyx_XDECREF(__pyx_v_trace);
  __Pyx_XDECREF(__pyx_v_parent);
  __Pyx_XDECREF(__pyx_v_attribute);
  __Pyx_XDECREF(__pyx_v_index);
  __Pyx_XDECREF(__pyx_v_node);
  __Pyx_XDECREF(__pyx_v_stacktrace);
  __Pyx_XDECREF(__pyx_v_called_nodes);
  __Pyx_XDECREF(__pyx_v_last_node);
  __Pyx_XDECREF(__pyx_v_method_name);
  __Pyx_XDECREF(__pyx_v_pos);
  __Pyx_XGIVEREF(__pyx_r);
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}
```

</details>

L127  🟠  (score=8)
```python
        trace = ['']
```
<details><summary>Show generated C (score=8)</summary>

```c
  __pyx_t_1 = PyList_New(1); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 127, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_INCREF(__pyx_mstate_global->__pyx_kp_u__7);
  __Pyx_GIVEREF(__pyx_mstate_global->__pyx_kp_u__7);
  if (__Pyx_PyList_SET_ITEM(__pyx_t_1, 0, __pyx_mstate_global->__pyx_kp_u__7) != (0)) __PYX_ERR(0, 127, __pyx_L1_error);
  __pyx_v_trace = ((PyObject*)__pyx_t_1);
  __pyx_t_1 = 0;
```

</details>

L128  🔴  (score=70)
```python
        for parent, attribute, index in self.access_path:
```
<details><summary>Show generated C (score=70)</summary>

```c
  if (unlikely(__pyx_v_self->access_path == Py_None)) {
    PyErr_SetString(PyExc_TypeError, "'NoneType' object is not iterable");
    __PYX_ERR(0, 128, __pyx_L1_error)
  }
  __pyx_t_1 = __pyx_v_self->access_path; __Pyx_INCREF(__pyx_t_1);
  __pyx_t_2 = 0;
  for (;;) {
    {
      Py_ssize_t __pyx_temp = __Pyx_PyList_GET_SIZE(__pyx_t_1);
      #if !CYTHON_ASSUME_SAFE_SIZE
      if (unlikely((__pyx_temp < 0))) __PYX_ERR(0, 128, __pyx_L1_error)
      #endif
      if (__pyx_t_2 >= __pyx_temp) break;
    }
    __pyx_t_3 = __Pyx_PyList_GetItemRefFast(__pyx_t_1, __pyx_t_2, __Pyx_ReferenceSharing_OwnStrongReference);
    ++__pyx_t_2;
    if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 128, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_3);
    if ((likely(PyTuple_CheckExact(__pyx_t_3))) || (PyList_CheckExact(__pyx_t_3))) {
      PyObject* sequence = __pyx_t_3;
      Py_ssize_t size = __Pyx_PySequence_SIZE(sequence);
      if (unlikely(size != 3)) {
        if (size > 3) __Pyx_RaiseTooManyValuesError(3);
        else if (size >= 0) __Pyx_RaiseNeedMoreValuesError(size);
        __PYX_ERR(0, 128, __pyx_L1_error)
      }
      #if CYTHON_ASSUME_SAFE_MACROS && !CYTHON_AVOID_BORROWED_REFS
      if (likely(PyTuple_CheckExact(sequence))) {
        __pyx_t_4 = PyTuple_GET_ITEM(sequence, 0);
        __Pyx_INCREF(__pyx_t_4);
        __pyx_t_5 = PyTuple_GET_ITEM(sequence, 1);
        __Pyx_INCREF(__pyx_t_5);
        __pyx_t_6 = PyTuple_GET_ITEM(sequence, 2);
        __Pyx_INCREF(__pyx_t_6);
      } else {
        __pyx_t_4 = __Pyx_PyList_GetItemRefFast(sequence, 0, __Pyx_ReferenceSharing_SharedReference);
        if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 128, __pyx_L1_error)
        __Pyx_XGOTREF(__pyx_t_4);
        __pyx_t_5 = __Pyx_PyList_GetItemRefFast(sequence, 1, __Pyx_ReferenceSharing_SharedReference);
        if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 128, __pyx_L1_error)
        __Pyx_XGOTREF(__pyx_t_5);
        __pyx_t_6 = __Pyx_PyList_GetItemRefFast(sequence, 2, __Pyx_ReferenceSharing_SharedReference);
        if (unlikely(!__pyx_t_6)) __PYX_ERR(0, 128, __pyx_L1_error)
        __Pyx_XGOTREF(__pyx_t_6);
      }
      #else
      __pyx_t_4 = __Pyx_PySequence_ITEM(sequence, 0); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 128, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_4);
      __pyx_t_5 = __Pyx_PySequence_ITEM(sequence, 1); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 128, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_5);
      __pyx_t_6 = __Pyx_PySequence_ITEM(sequence, 2); if (unlikely(!__pyx_t_6)) __PYX_ERR(0, 128, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_6);
      #endif
      __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
    } else {
      Py_ssize_t index = -1;
      __pyx_t_7 = PyObject_GetIter(__pyx_t_3); if (unlikely(!__pyx_t_7)) __PYX_ERR(0, 128, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_7);
      __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
      __pyx_t_8 = (CYTHON_COMPILING_IN_LIMITED_API) ? PyIter_Next : __Pyx_PyObject_GetIterNextFunc(__pyx_t_7);
      index = 0; __pyx_t_4 = __pyx_t_8(__pyx_t_7); if (unlikely(!__pyx_t_4)) goto __pyx_L5_unpacking_failed;
      __Pyx_GOTREF(__pyx_t_4);
      index = 1; __pyx_t_5 = __pyx_t_8(__pyx_t_7); if (unlikely(!__pyx_t_5)) goto __pyx_L5_unpacking_failed;
      __Pyx_GOTREF(__pyx_t_5);
      index = 2; __pyx_t_6 = __pyx_t_8(__pyx_t_7); if (unlikely(!__pyx_t_6)) goto __pyx_L5_unpacking_failed;
      __Pyx_GOTREF(__pyx_t_6);
      if (__Pyx_IternextUnpackEndCheck(__pyx_t_8(__pyx_t_7), 3) < (0)) __PYX_ERR(0, 128, __pyx_L1_error)
      __pyx_t_8 = NULL;
      __Pyx_DECREF(__pyx_t_7); __pyx_t_7 = 0;
      goto __pyx_L6_unpacking_done;
      __pyx_L5_unpacking_failed:;
      __Pyx_DECREF(__pyx_t_7); __pyx_t_7 = 0;
      __pyx_t_8 = NULL;
      if (__Pyx_IterFinish() == 0) __Pyx_RaiseNeedMoreValuesError(index);
      __PYX_ERR(0, 128, __pyx_L1_error)
      __pyx_L6_unpacking_done:;
    }
    __Pyx_XDECREF_SET(__pyx_v_parent, __pyx_t_4);
    __pyx_t_4 = 0;
    __Pyx_XDECREF_SET(__pyx_v_attribute, __pyx_t_5);
    __pyx_t_5 = 0;
    __Pyx_XDECREF_SET(__pyx_v_index, __pyx_t_6);
    __pyx_t_6 = 0;
/* … */
  }
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
```

</details>

L129  🟡  (score=3)
```python
            node = getattr(parent, attribute)
```
<details><summary>Show generated C (score=3)</summary>

```c
    __pyx_t_3 = __Pyx_GetAttr(__pyx_v_parent, __pyx_v_attribute); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 129, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_3);
    __Pyx_XDECREF_SET(__pyx_v_node, __pyx_t_3);
    __pyx_t_3 = 0;
```

</details>

L130  ⚪  (score=0)
```python
            if index is None:
```
<details><summary>Show generated C (score=0)</summary>

```c
    __pyx_t_9 = (__pyx_v_index == Py_None);
    if (__pyx_t_9) {
/* … */
      goto __pyx_L7;
    }
```

</details>

L131  🟡  (score=2)
```python
                index = ''
```
<details><summary>Show generated C (score=2)</summary>

```c
      __Pyx_INCREF(__pyx_mstate_global->__pyx_kp_u__7);
      __Pyx_DECREF_SET(__pyx_v_index, __pyx_mstate_global->__pyx_kp_u__7);
```

</details>

L132  ⚪  (score=0)
```python
            else:
```
L133  🟡  (score=3)
```python
                node = node[index]
```
<details><summary>Show generated C (score=3)</summary>

```c
    /*else*/ {
      __pyx_t_3 = __Pyx_PyObject_GetItem(__pyx_v_node, __pyx_v_index); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 133, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_3);
      __Pyx_DECREF_SET(__pyx_v_node, __pyx_t_3);
      __pyx_t_3 = 0;
```

</details>

L134  🟡  (score=3)
```python
                index = '[%d]' % index
```
<details><summary>Show generated C (score=3)</summary>

```c
      __pyx_t_3 = __Pyx_PyUnicode_FormatSafe(__pyx_mstate_global->__pyx_kp_u_d_2, __pyx_v_index); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 134, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_3);
      __Pyx_DECREF_SET(__pyx_v_index, __pyx_t_3);
      __pyx_t_3 = 0;
    }
    __pyx_L7:;
```

</details>

L135  🔴  (score=25)
```python
            trace.append('%s.%s%s = %s' % (
```
<details><summary>Show generated C (score=25)</summary>

```c
    __pyx_t_7 = __Pyx_PyUnicode_Join(__pyx_t_10, 6, __Pyx_PyUnicode_GET_LENGTH(__pyx_t_3) + 1 + __Pyx_PyUnicode_GET_LENGTH(__pyx_t_6) + __Pyx_PyUnicode_GET_LENGTH(__pyx_t_5) + 3 + __Pyx_PyUnicode_GET_LENGTH(__pyx_t_4), 127 | __Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_3) | __Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_6) | __Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_5) | __Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_4));
    if (unlikely(!__pyx_t_7)) __PYX_ERR(0, 135, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_7);
    __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
    __Pyx_DECREF(__pyx_t_6); __pyx_t_6 = 0;
    __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
    __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
    __pyx_t_11 = __Pyx_PyList_Append(__pyx_v_trace, __pyx_t_7); if (unlikely(__pyx_t_11 == ((int)-1))) __PYX_ERR(0, 135, __pyx_L1_error)
    __Pyx_DECREF(__pyx_t_7); __pyx_t_7 = 0;
```

</details>

L136  🔴  (score=27)
```python
                parent.__class__.__name__, attribute, index,
```
<details><summary>Show generated C (score=27)</summary>

```c
    __pyx_t_3 = __Pyx_PyObject_GetAttrStr(__pyx_v_parent, __pyx_mstate_global->__pyx_n_u_class); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 136, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_3);
    __pyx_t_6 = __Pyx_PyObject_GetAttrStr(__pyx_t_3, __pyx_mstate_global->__pyx_n_u_name); if (unlikely(!__pyx_t_6)) __PYX_ERR(0, 136, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_6);
    __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
    __pyx_t_3 = __Pyx_PyObject_FormatSimpleAndDecref(PyObject_Str(__pyx_t_6), __pyx_mstate_global->__pyx_empty_unicode); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 136, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_3);
    __Pyx_DECREF(__pyx_t_6); __pyx_t_6 = 0;
    __pyx_t_6 = __Pyx_PyObject_FormatSimpleAndDecref(PyObject_Str(__pyx_v_attribute), __pyx_mstate_global->__pyx_empty_unicode); if (unlikely(!__pyx_t_6)) __PYX_ERR(0, 136, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_6);
    __pyx_t_5 = __Pyx_PyObject_FormatSimpleAndDecref(PyObject_Str(__pyx_v_index), __pyx_mstate_global->__pyx_empty_unicode); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 136, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_5);
```

</details>

L137  🔴  (score=13)
```python
                self.dump_node(node)))
```
<details><summary>Show generated C (score=13)</summary>

```c
    __pyx_t_4 = __Pyx_PyObject_GetAttrStr(((PyObject *)__pyx_v_self), __pyx_mstate_global->__pyx_n_u_dump_node); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 137, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_4);
    __pyx_t_7 = __Pyx_PyObject_CallOneArg(__pyx_t_4, __pyx_v_node); if (unlikely(!__pyx_t_7)) __PYX_ERR(0, 137, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_7);
    __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
    __pyx_t_4 = __Pyx_PyObject_FormatSimpleAndDecref(PyObject_Str(__pyx_t_7), __pyx_mstate_global->__pyx_empty_unicode); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 137, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_4);
    __Pyx_DECREF(__pyx_t_7); __pyx_t_7 = 0;
    __pyx_t_10[0] = __pyx_t_3;
    __pyx_t_10[1] = __pyx_mstate_global->__pyx_kp_u__8;
    __pyx_t_10[2] = __pyx_t_6;
    __pyx_t_10[3] = __pyx_t_5;
    __pyx_t_10[4] = __pyx_mstate_global->__pyx_kp_u__3;
    __pyx_t_10[5] = __pyx_t_4;
```

</details>

L138  🔴  (score=77)
```python
        stacktrace, called_nodes = self._find_node_path(sys.exc_info()[2])
```
<details><summary>Show generated C (score=77)</summary>

```c
  __pyx_t_7 = ((PyObject *)__pyx_v_self);
  __Pyx_INCREF(__pyx_t_7);
  __pyx_t_5 = NULL;
  __Pyx_GetModuleGlobalName(__pyx_t_6, __pyx_mstate_global->__pyx_n_u_sys); if (unlikely(!__pyx_t_6)) __PYX_ERR(0, 138, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_6);
  __pyx_t_3 = __Pyx_PyObject_GetAttrStr(__pyx_t_6, __pyx_mstate_global->__pyx_n_u_exc_info); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 138, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_3);
  __Pyx_DECREF(__pyx_t_6); __pyx_t_6 = 0;
  __pyx_t_12 = 1;
  #if CYTHON_UNPACK_METHODS
  if (unlikely(PyMethod_Check(__pyx_t_3))) {
    __pyx_t_5 = PyMethod_GET_SELF(__pyx_t_3);
    assert(__pyx_t_5);
    PyObject* __pyx__function = PyMethod_GET_FUNCTION(__pyx_t_3);
    __Pyx_INCREF(__pyx_t_5);
    __Pyx_INCREF(__pyx__function);
    __Pyx_DECREF_SET(__pyx_t_3, __pyx__function);
    __pyx_t_12 = 0;
  }
  #endif
  {
    PyObject *__pyx_callargs[2] = {__pyx_t_5, NULL};
    __pyx_t_4 = __Pyx_PyObject_FastCall((PyObject*)__pyx_t_3, __pyx_callargs+__pyx_t_12, (1-__pyx_t_12) | (__pyx_t_12*__Pyx_PY_VECTORCALL_ARGUMENTS_OFFSET));
    __Pyx_XDECREF(__pyx_t_5); __pyx_t_5 = 0;
    __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
    if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 138, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_4);
  }
  __pyx_t_3 = __Pyx_GetItemInt(__pyx_t_4, 2, long, 1, __Pyx_PyLong_From_long, 0, 0, 1, 1, __Pyx_ReferenceSharing_OwnStrongReference); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 138, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_3);
  __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
  __pyx_t_12 = 0;
  {
    PyObject *__pyx_callargs[2] = {__pyx_t_7, __pyx_t_3};
    __pyx_t_1 = __Pyx_PyObject_FastCallMethod((PyObject*)__pyx_mstate_global->__pyx_n_u_find_node_path, __pyx_callargs+__pyx_t_12, (2-__pyx_t_12) | (1*__Pyx_PY_VECTORCALL_ARGUMENTS_OFFSET));
    __Pyx_XDECREF(__pyx_t_7); __pyx_t_7 = 0;
    __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
    if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 138, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_1);
  }
  if ((likely(PyTuple_CheckExact(__pyx_t_1))) || (PyList_CheckExact(__pyx_t_1))) {
    PyObject* sequence = __pyx_t_1;
    Py_ssize_t size = __Pyx_PySequence_SIZE(sequence);
    if (unlikely(size != 2)) {
      if (size > 2) __Pyx_RaiseTooManyValuesError(2);
      else if (size >= 0) __Pyx_RaiseNeedMoreValuesError(size);
      __PYX_ERR(0, 138, __pyx_L1_error)
    }
    #if CYTHON_ASSUME_SAFE_MACROS && !CYTHON_AVOID_BORROWED_REFS
    if (likely(PyTuple_CheckExact(sequence))) {
      __pyx_t_3 = PyTuple_GET_ITEM(sequence, 0);
      __Pyx_INCREF(__pyx_t_3);
      __pyx_t_7 = PyTuple_GET_ITEM(sequence, 1);
      __Pyx_INCREF(__pyx_t_7);
    } else {
      __pyx_t_3 = __Pyx_PyList_GetItemRefFast(sequence, 0, __Pyx_ReferenceSharing_SharedReference);
      if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 138, __pyx_L1_error)
      __Pyx_XGOTREF(__pyx_t_3);
      __pyx_t_7 = __Pyx_PyList_GetItemRefFast(sequence, 1, __Pyx_ReferenceSharing_SharedReference);
      if (unlikely(!__pyx_t_7)) __PYX_ERR(0, 138, __pyx_L1_error)
      __Pyx_XGOTREF(__pyx_t_7);
    }
    #else
    __pyx_t_3 = __Pyx_PySequence_ITEM(sequence, 0); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 138, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_3);
    __pyx_t_7 = __Pyx_PySequence_ITEM(sequence, 1); if (unlikely(!__pyx_t_7)) __PYX_ERR(0, 138, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_7);
    #endif
    __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  } else {
    Py_ssize_t index = -1;
    __pyx_t_4 = PyObject_GetIter(__pyx_t_1); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 138, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_4);
    __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
    __pyx_t_8 = (CYTHON_COMPILING_IN_LIMITED_API) ? PyIter_Next : __Pyx_PyObject_GetIterNextFunc(__pyx_t_4);
    index = 0; __pyx_t_3 = __pyx_t_8(__pyx_t_4); if (unlikely(!__pyx_t_3)) goto __pyx_L9_unpacking_failed;
    __Pyx_GOTREF(__pyx_t_3);
    index = 1; __pyx_t_7 = __pyx_t_8(__pyx_t_4); if (unlikely(!__pyx_t_7)) goto __pyx_L9_unpacking_failed;
    __Pyx_GOTREF(__pyx_t_7);
    if (__Pyx_IternextUnpackEndCheck(__pyx_t_8(__pyx_t_4), 2) < (0)) __PYX_ERR(0, 138, __pyx_L1_error)
    __pyx_t_8 = NULL;
    __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
    goto __pyx_L10_unpacking_done;
    __pyx_L9_unpacking_failed:;
    __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
    __pyx_t_8 = NULL;
    if (__Pyx_IterFinish() == 0) __Pyx_RaiseNeedMoreValuesError(index);
    __PYX_ERR(0, 138, __pyx_L1_error)
    __pyx_L10_unpacking_done:;
  }
  __pyx_v_stacktrace = __pyx_t_3;
  __pyx_t_3 = 0;
  __pyx_v_called_nodes = __pyx_t_7;
  __pyx_t_7 = 0;
```

</details>

L139  🟡  (score=1)
```python
        last_node = child
```
<details><summary>Show generated C (score=1)</summary>

```c
  __Pyx_INCREF(__pyx_v_child);
  __pyx_v_last_node = __pyx_v_child;
```

</details>

L140  🔴  (score=106)
```python
        for node, method_name, pos in called_nodes:
```
<details><summary>Show generated C (score=106)</summary>

```c
  if (likely(PyList_CheckExact(__pyx_v_called_nodes)) || PyTuple_CheckExact(__pyx_v_called_nodes)) {
    __pyx_t_1 = __pyx_v_called_nodes; __Pyx_INCREF(__pyx_t_1);
    __pyx_t_2 = 0;
    __pyx_t_13 = NULL;
  } else {
    __pyx_t_2 = -1; __pyx_t_1 = PyObject_GetIter(__pyx_v_called_nodes); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 140, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_1);
    __pyx_t_13 = (CYTHON_COMPILING_IN_LIMITED_API) ? PyIter_Next : __Pyx_PyObject_GetIterNextFunc(__pyx_t_1); if (unlikely(!__pyx_t_13)) __PYX_ERR(0, 140, __pyx_L1_error)
  }
  for (;;) {
    if (likely(!__pyx_t_13)) {
      if (likely(PyList_CheckExact(__pyx_t_1))) {
        {
          Py_ssize_t __pyx_temp = __Pyx_PyList_GET_SIZE(__pyx_t_1);
          #if !CYTHON_ASSUME_SAFE_SIZE
          if (unlikely((__pyx_temp < 0))) __PYX_ERR(0, 140, __pyx_L1_error)
          #endif
          if (__pyx_t_2 >= __pyx_temp) break;
        }
        __pyx_t_7 = __Pyx_PyList_GetItemRefFast(__pyx_t_1, __pyx_t_2, __Pyx_ReferenceSharing_OwnStrongReference);
        ++__pyx_t_2;
      } else {
        {
          Py_ssize_t __pyx_temp = __Pyx_PyTuple_GET_SIZE(__pyx_t_1);
          #if !CYTHON_ASSUME_SAFE_SIZE
          if (unlikely((__pyx_temp < 0))) __PYX_ERR(0, 140, __pyx_L1_error)
          #endif
          if (__pyx_t_2 >= __pyx_temp) break;
        }
        #if CYTHON_ASSUME_SAFE_MACROS && !CYTHON_AVOID_BORROWED_REFS
        __pyx_t_7 = __Pyx_NewRef(PyTuple_GET_ITEM(__pyx_t_1, __pyx_t_2));
        #else
        __pyx_t_7 = __Pyx_PySequence_ITEM(__pyx_t_1, __pyx_t_2);
        #endif
        ++__pyx_t_2;
      }
      if (unlikely(!__pyx_t_7)) __PYX_ERR(0, 140, __pyx_L1_error)
    } else {
      __pyx_t_7 = __pyx_t_13(__pyx_t_1);
      if (unlikely(!__pyx_t_7)) {
        PyObject* exc_type = PyErr_Occurred();
        if (exc_type) {
          if (unlikely(!__Pyx_PyErr_GivenExceptionMatches(exc_type, PyExc_StopIteration))) __PYX_ERR(0, 140, __pyx_L1_error)
          PyErr_Clear();
        }
        break;
      }
    }
    __Pyx_GOTREF(__pyx_t_7);
    if ((likely(PyTuple_CheckExact(__pyx_t_7))) || (PyList_CheckExact(__pyx_t_7))) {
      PyObject* sequence = __pyx_t_7;
      Py_ssize_t size = __Pyx_PySequence_SIZE(sequence);
      if (unlikely(size != 3)) {
        if (size > 3) __Pyx_RaiseTooManyValuesError(3);
        else if (size >= 0) __Pyx_RaiseNeedMoreValuesError(size);
        __PYX_ERR(0, 140, __pyx_L1_error)
      }
      #if CYTHON_ASSUME_SAFE_MACROS && !CYTHON_AVOID_BORROWED_REFS
      if (likely(PyTuple_CheckExact(sequence))) {
        __pyx_t_3 = PyTuple_GET_ITEM(sequence, 0);
        __Pyx_INCREF(__pyx_t_3);
        __pyx_t_4 = PyTuple_GET_ITEM(sequence, 1);
        __Pyx_INCREF(__pyx_t_4);
        __pyx_t_5 = PyTuple_GET_ITEM(sequence, 2);
        __Pyx_INCREF(__pyx_t_5);
      } else {
        __pyx_t_3 = __Pyx_PyList_GetItemRefFast(sequence, 0, __Pyx_ReferenceSharing_SharedReference);
        if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 140, __pyx_L1_error)
        __Pyx_XGOTREF(__pyx_t_3);
        __pyx_t_4 = __Pyx_PyList_GetItemRefFast(sequence, 1, __Pyx_ReferenceSharing_SharedReference);
        if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 140, __pyx_L1_error)
        __Pyx_XGOTREF(__pyx_t_4);
        __pyx_t_5 = __Pyx_PyList_GetItemRefFast(sequence, 2, __Pyx_ReferenceSharing_SharedReference);
        if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 140, __pyx_L1_error)
        __Pyx_XGOTREF(__pyx_t_5);
      }
      #else
      __pyx_t_3 = __Pyx_PySequence_ITEM(sequence, 0); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 140, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_3);
      __pyx_t_4 = __Pyx_PySequence_ITEM(sequence, 1); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 140, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_4);
      __pyx_t_5 = __Pyx_PySequence_ITEM(sequence, 2); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 140, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_5);
      #endif
      __Pyx_DECREF(__pyx_t_7); __pyx_t_7 = 0;
    } else {
      Py_ssize_t index = -1;
      __pyx_t_6 = PyObject_GetIter(__pyx_t_7); if (unlikely(!__pyx_t_6)) __PYX_ERR(0, 140, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_6);
      __Pyx_DECREF(__pyx_t_7); __pyx_t_7 = 0;
      __pyx_t_8 = (CYTHON_COMPILING_IN_LIMITED_API) ? PyIter_Next : __Pyx_PyObject_GetIterNextFunc(__pyx_t_6);
      index = 0; __pyx_t_3 = __pyx_t_8(__pyx_t_6); if (unlikely(!__pyx_t_3)) goto __pyx_L13_unpacking_failed;
      __Pyx_GOTREF(__pyx_t_3);
      index = 1; __pyx_t_4 = __pyx_t_8(__pyx_t_6); if (unlikely(!__pyx_t_4)) goto __pyx_L13_unpacking_failed;
      __Pyx_GOTREF(__pyx_t_4);
      index = 2; __pyx_t_5 = __pyx_t_8(__pyx_t_6); if (unlikely(!__pyx_t_5)) goto __pyx_L13_unpacking_failed;
      __Pyx_GOTREF(__pyx_t_5);
      if (__Pyx_IternextUnpackEndCheck(__pyx_t_8(__pyx_t_6), 3) < (0)) __PYX_ERR(0, 140, __pyx_L1_error)
      __pyx_t_8 = NULL;
      __Pyx_DECREF(__pyx_t_6); __pyx_t_6 = 0;
      goto __pyx_L14_unpacking_done;
      __pyx_L13_unpacking_failed:;
      __Pyx_DECREF(__pyx_t_6); __pyx_t_6 = 0;
      __pyx_t_8 = NULL;
      if (__Pyx_IterFinish() == 0) __Pyx_RaiseNeedMoreValuesError(index);
      __PYX_ERR(0, 140, __pyx_L1_error)
      __pyx_L14_unpacking_done:;
    }
    __Pyx_XDECREF_SET(__pyx_v_node, __pyx_t_3);
    __pyx_t_3 = 0;
    __Pyx_XDECREF_SET(__pyx_v_method_name, __pyx_t_4);
    __pyx_t_4 = 0;
    __Pyx_XDECREF_SET(__pyx_v_pos, __pyx_t_5);
    __pyx_t_5 = 0;
/* … */
  }
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
```

</details>

L141  🟡  (score=2)
```python
            last_node = node
```
<details><summary>Show generated C (score=2)</summary>

```c
    __Pyx_INCREF(__pyx_v_node);
    __Pyx_DECREF_SET(__pyx_v_last_node, __pyx_v_node);
```

</details>

L142  🔴  (score=25)
```python
            trace.append("File '%s', line %d, in %s: %s" % (
```
<details><summary>Show generated C (score=25)</summary>

```c
    __pyx_t_6 = __Pyx_PyUnicode_Join(__pyx_t_14, 8, 6 + __Pyx_PyUnicode_GET_LENGTH(__pyx_t_5) + 8 + __Pyx_PyUnicode_GET_LENGTH(__pyx_t_4) + 5 + __Pyx_PyUnicode_GET_LENGTH(__pyx_t_7) + 2 + __Pyx_PyUnicode_GET_LENGTH(__pyx_t_3), 127 | __Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_5) | __Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_4) | __Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_7) | __Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_3));
    if (unlikely(!__pyx_t_6)) __PYX_ERR(0, 142, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_6);
    __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
    __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
    __Pyx_DECREF(__pyx_t_7); __pyx_t_7 = 0;
    __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
    __pyx_t_11 = __Pyx_PyList_Append(__pyx_v_trace, __pyx_t_6); if (unlikely(__pyx_t_11 == ((int)-1))) __PYX_ERR(0, 142, __pyx_L1_error)
    __Pyx_DECREF(__pyx_t_6); __pyx_t_6 = 0;
```

</details>

L143  🔴  (score=37)
```python
                pos[0], pos[1], method_name, self.dump_node(node)))
```
<details><summary>Show generated C (score=37)</summary>

```c
    __pyx_t_7 = __Pyx_GetItemInt(__pyx_v_pos, 0, long, 1, __Pyx_PyLong_From_long, 0, 0, 1, 1, __Pyx_ReferenceSharing_OwnStrongReference); if (unlikely(!__pyx_t_7)) __PYX_ERR(0, 143, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_7);
    __pyx_t_5 = __Pyx_PyObject_FormatSimpleAndDecref(PyObject_Str(__pyx_t_7), __pyx_mstate_global->__pyx_empty_unicode); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 143, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_5);
    __Pyx_DECREF(__pyx_t_7); __pyx_t_7 = 0;
    __pyx_t_7 = __Pyx_GetItemInt(__pyx_v_pos, 1, long, 1, __Pyx_PyLong_From_long, 0, 0, 1, 1, __Pyx_ReferenceSharing_OwnStrongReference); if (unlikely(!__pyx_t_7)) __PYX_ERR(0, 143, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_7);
    __pyx_t_4 = __Pyx_PyObject_FormatAndDecref(__Pyx_PyNumber_Long(__pyx_t_7), __pyx_mstate_global->__pyx_n_u_d_3); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 143, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_4);
    __Pyx_DECREF(__pyx_t_7); __pyx_t_7 = 0;
    __pyx_t_7 = __Pyx_PyObject_FormatSimpleAndDecref(PyObject_Str(__pyx_v_method_name), __pyx_mstate_global->__pyx_empty_unicode); if (unlikely(!__pyx_t_7)) __PYX_ERR(0, 143, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_7);
    __pyx_t_3 = __Pyx_PyObject_GetAttrStr(((PyObject *)__pyx_v_self), __pyx_mstate_global->__pyx_n_u_dump_node); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 143, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_3);
    __pyx_t_6 = __Pyx_PyObject_CallOneArg(__pyx_t_3, __pyx_v_node); if (unlikely(!__pyx_t_6)) __PYX_ERR(0, 143, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_6);
    __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
    __pyx_t_3 = __Pyx_PyObject_FormatSimpleAndDecref(PyObject_Str(__pyx_t_6), __pyx_mstate_global->__pyx_empty_unicode); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 143, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_3);
    __Pyx_DECREF(__pyx_t_6); __pyx_t_6 = 0;
    __pyx_t_14[0] = __pyx_mstate_global->__pyx_kp_u_File;
    __pyx_t_14[1] = __pyx_t_5;
    __pyx_t_14[2] = __pyx_mstate_global->__pyx_kp_u_line;
    __pyx_t_14[3] = __pyx_t_4;
    __pyx_t_14[4] = __pyx_mstate_global->__pyx_kp_u_in;
    __pyx_t_14[5] = __pyx_t_7;
    __pyx_t_14[6] = __pyx_mstate_global->__pyx_kp_u__9;
    __pyx_t_14[7] = __pyx_t_3;
```

</details>

L144  🟠  (score=5)
```python
        raise Errors.CompilerCrash(
```
<details><summary>Show generated C (score=5)</summary>

```c
  __pyx_t_6 = NULL;
  __Pyx_GetModuleGlobalName(__pyx_t_3, __pyx_mstate_global->__pyx_n_u_Errors); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 144, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_3);
  __pyx_t_7 = __Pyx_PyObject_GetAttrStr(__pyx_t_3, __pyx_mstate_global->__pyx_n_u_CompilerCrash); if (unlikely(!__pyx_t_7)) __PYX_ERR(0, 144, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_7);
  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
```

</details>

L145  🟠  (score=5)
```python
            getattr(last_node, 'pos', None), self.__class__.__name__,
```
<details><summary>Show generated C (score=5)</summary>

```c
  __pyx_t_3 = __Pyx_GetAttr3(__pyx_v_last_node, __pyx_mstate_global->__pyx_n_u_pos, Py_None); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 145, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_3);
  __pyx_t_4 = __Pyx_PyObject_GetAttrStr(((PyObject *)__pyx_v_self), __pyx_mstate_global->__pyx_n_u_class); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 145, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_4);
  __pyx_t_5 = __Pyx_PyObject_GetAttrStr(__pyx_t_4, __pyx_mstate_global->__pyx_n_u_name); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 145, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_5);
  __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
```

</details>

L146  🔴  (score=25)
```python
            '\n'.join(trace), e, stacktrace)
```
<details><summary>Show generated C (score=25)</summary>

```c
  __pyx_t_4 = PyUnicode_Join(__pyx_mstate_global->__pyx_kp_u__10, __pyx_v_trace); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 146, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_4);
  __pyx_t_12 = 1;
  #if CYTHON_UNPACK_METHODS
  if (unlikely(PyMethod_Check(__pyx_t_7))) {
    __pyx_t_6 = PyMethod_GET_SELF(__pyx_t_7);
    assert(__pyx_t_6);
    PyObject* __pyx__function = PyMethod_GET_FUNCTION(__pyx_t_7);
    __Pyx_INCREF(__pyx_t_6);
    __Pyx_INCREF(__pyx__function);
    __Pyx_DECREF_SET(__pyx_t_7, __pyx__function);
    __pyx_t_12 = 0;
  }
  #endif
  {
    PyObject *__pyx_callargs[6] = {__pyx_t_6, __pyx_t_3, __pyx_t_5, __pyx_t_4, __pyx_v_e, __pyx_v_stacktrace};
    __pyx_t_1 = __Pyx_PyObject_FastCall((PyObject*)__pyx_t_7, __pyx_callargs+__pyx_t_12, (6-__pyx_t_12) | (__pyx_t_12*__Pyx_PY_VECTORCALL_ARGUMENTS_OFFSET));
    __Pyx_XDECREF(__pyx_t_6); __pyx_t_6 = 0;
    __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
    __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
    __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
    __Pyx_DECREF(__pyx_t_7); __pyx_t_7 = 0;
    if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 144, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_1);
  }
  __Pyx_Raise(__pyx_t_1, 0, 0, 0);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __PYX_ERR(0, 144, __pyx_L1_error)
```

</details>

L147  ⚪  (score=0)
```python
```
L148  🔴  (score=11)
```python
    @cython.final
```
<details><summary>Show generated C (score=11)</summary>

```c
static PyObject *__pyx_f_6Cython_8Compiler_7Visitor_11TreeVisitor_find_handler(struct __pyx_obj_6Cython_8Compiler_7Visitor_TreeVisitor *__pyx_v_self, PyObject *__pyx_v_obj) {
  PyTypeObject *__pyx_v_cls = NULL;
  PyObject *__pyx_v_mro = NULL;
  PyObject *__pyx_v_mro_cls = NULL;
  PyObject *__pyx_v_handler_method = NULL;
  PyObject *__pyx_r = NULL;
/* … */
  /* function exit code */
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_t_1);
  __Pyx_XDECREF(__pyx_t_2);
  __Pyx_XDECREF(__pyx_t_3);
  __Pyx_XDECREF(__pyx_t_4);
  __Pyx_XDECREF(__pyx_t_10);
  __Pyx_AddTraceback("Cython.Compiler.Visitor.TreeVisitor.find_handler", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_r = 0;
  __pyx_L0:;
  __Pyx_XDECREF((PyObject *)__pyx_v_cls);
  __Pyx_XDECREF(__pyx_v_mro);
  __Pyx_XDECREF(__pyx_v_mro_cls);
  __Pyx_XDECREF(__pyx_v_handler_method);
  __Pyx_XGIVEREF(__pyx_r);
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}
```

</details>

L149  ⚪  (score=0)
```python
    def find_handler(self, obj):
```
L150  ⚪  (score=0)
```python
        # to resolve, try entire hierarchy
```
L151  🟡  (score=1)
```python
        cls = type(obj)
```
<details><summary>Show generated C (score=1)</summary>

```c
  __Pyx_INCREF(((PyObject *)Py_TYPE(__pyx_v_obj)));
  __pyx_v_cls = ((PyTypeObject*)((PyObject *)Py_TYPE(__pyx_v_obj)));
```

</details>

L152  🔴  (score=19)
```python
        mro = inspect.getmro(cls)
```
<details><summary>Show generated C (score=19)</summary>

```c
  __pyx_t_2 = NULL;
  __Pyx_GetModuleGlobalName(__pyx_t_3, __pyx_mstate_global->__pyx_n_u_inspect); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 152, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_3);
  __pyx_t_4 = __Pyx_PyObject_GetAttrStr(__pyx_t_3, __pyx_mstate_global->__pyx_n_u_getmro); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 152, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_4);
  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
  __pyx_t_5 = 1;
  #if CYTHON_UNPACK_METHODS
  if (unlikely(PyMethod_Check(__pyx_t_4))) {
    __pyx_t_2 = PyMethod_GET_SELF(__pyx_t_4);
    assert(__pyx_t_2);
    PyObject* __pyx__function = PyMethod_GET_FUNCTION(__pyx_t_4);
    __Pyx_INCREF(__pyx_t_2);
    __Pyx_INCREF(__pyx__function);
    __Pyx_DECREF_SET(__pyx_t_4, __pyx__function);
    __pyx_t_5 = 0;
  }
  #endif
  {
    PyObject *__pyx_callargs[2] = {__pyx_t_2, ((PyObject *)__pyx_v_cls)};
    __pyx_t_1 = __Pyx_PyObject_FastCall((PyObject*)__pyx_t_4, __pyx_callargs+__pyx_t_5, (2-__pyx_t_5) | (__pyx_t_5*__Pyx_PY_VECTORCALL_ARGUMENTS_OFFSET));
    __Pyx_XDECREF(__pyx_t_2); __pyx_t_2 = 0;
    __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
    if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 152, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_1);
  }
  __pyx_v_mro = __pyx_t_1;
  __pyx_t_1 = 0;
```

</details>

L153  🔴  (score=48)
```python
        for mro_cls in mro:
```
<details><summary>Show generated C (score=48)</summary>

```c
  if (likely(PyList_CheckExact(__pyx_v_mro)) || PyTuple_CheckExact(__pyx_v_mro)) {
    __pyx_t_1 = __pyx_v_mro; __Pyx_INCREF(__pyx_t_1);
    __pyx_t_6 = 0;
    __pyx_t_7 = NULL;
  } else {
    __pyx_t_6 = -1; __pyx_t_1 = PyObject_GetIter(__pyx_v_mro); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 153, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_1);
    __pyx_t_7 = (CYTHON_COMPILING_IN_LIMITED_API) ? PyIter_Next : __Pyx_PyObject_GetIterNextFunc(__pyx_t_1); if (unlikely(!__pyx_t_7)) __PYX_ERR(0, 153, __pyx_L1_error)
  }
  for (;;) {
    if (likely(!__pyx_t_7)) {
      if (likely(PyList_CheckExact(__pyx_t_1))) {
        {
          Py_ssize_t __pyx_temp = __Pyx_PyList_GET_SIZE(__pyx_t_1);
          #if !CYTHON_ASSUME_SAFE_SIZE
          if (unlikely((__pyx_temp < 0))) __PYX_ERR(0, 153, __pyx_L1_error)
          #endif
          if (__pyx_t_6 >= __pyx_temp) break;
        }
        __pyx_t_4 = __Pyx_PyList_GetItemRefFast(__pyx_t_1, __pyx_t_6, __Pyx_ReferenceSharing_OwnStrongReference);
        ++__pyx_t_6;
      } else {
        {
          Py_ssize_t __pyx_temp = __Pyx_PyTuple_GET_SIZE(__pyx_t_1);
          #if !CYTHON_ASSUME_SAFE_SIZE
          if (unlikely((__pyx_temp < 0))) __PYX_ERR(0, 153, __pyx_L1_error)
          #endif
          if (__pyx_t_6 >= __pyx_temp) break;
        }
        #if CYTHON_ASSUME_SAFE_MACROS && !CYTHON_AVOID_BORROWED_REFS
        __pyx_t_4 = __Pyx_NewRef(PyTuple_GET_ITEM(__pyx_t_1, __pyx_t_6));
        #else
        __pyx_t_4 = __Pyx_PySequence_ITEM(__pyx_t_1, __pyx_t_6);
        #endif
        ++__pyx_t_6;
      }
      if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 153, __pyx_L1_error)
    } else {
      __pyx_t_4 = __pyx_t_7(__pyx_t_1);
      if (unlikely(!__pyx_t_4)) {
        PyObject* exc_type = PyErr_Occurred();
        if (exc_type) {
          if (unlikely(!__Pyx_PyErr_GivenExceptionMatches(exc_type, PyExc_StopIteration))) __PYX_ERR(0, 153, __pyx_L1_error)
          PyErr_Clear();
        }
        break;
      }
    }
    __Pyx_GOTREF(__pyx_t_4);
    __Pyx_XDECREF_SET(__pyx_v_mro_cls, __pyx_t_4);
    __pyx_t_4 = 0;
/* … */
  }
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
```

</details>

L154  🔴  (score=10)
```python
            handler_method = getattr(self, "visit_" + mro_cls.__name__, None)
```
<details><summary>Show generated C (score=10)</summary>

```c
    __pyx_t_4 = __Pyx_PyObject_GetAttrStr(__pyx_v_mro_cls, __pyx_mstate_global->__pyx_n_u_name); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 154, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_4);
    __pyx_t_2 = PyNumber_Add(__pyx_mstate_global->__pyx_n_u_visit, __pyx_t_4); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 154, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_2);
    __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
    __pyx_t_4 = __Pyx_GetAttr3(((PyObject *)__pyx_v_self), __pyx_t_2, Py_None); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 154, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_4);
    __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
    __Pyx_XDECREF_SET(__pyx_v_handler_method, __pyx_t_4);
    __pyx_t_4 = 0;
```

</details>

L155  ⚪  (score=0)
```python
            if handler_method is not None:
```
<details><summary>Show generated C (score=0)</summary>

```c
    __pyx_t_8 = (__pyx_v_handler_method != Py_None);
    if (__pyx_t_8) {
/* … */
    }
```

</details>

L156  🟡  (score=3)
```python
                return handler_method
```
<details><summary>Show generated C (score=3)</summary>

```c
      __Pyx_XDECREF(__pyx_r);
      __Pyx_INCREF(__pyx_v_handler_method);
      __pyx_r = __pyx_v_handler_method;
      __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
      goto __pyx_L0;
```

</details>

L157  ⚪  (score=0)
```python
```
L158  🟡  (score=4)
```python
        print(type(self), cls)
```
<details><summary>Show generated C (score=4)</summary>

```c
  __pyx_t_4 = NULL;
  __pyx_t_5 = 1;
  {
    PyObject *__pyx_callargs[3] = {__pyx_t_4, ((PyObject *)Py_TYPE(((PyObject *)__pyx_v_self))), ((PyObject *)__pyx_v_cls)};
    __pyx_t_1 = __Pyx_PyObject_FastCall((PyObject*)__pyx_builtin_print, __pyx_callargs+__pyx_t_5, (3-__pyx_t_5) | (__pyx_t_5*__Pyx_PY_VECTORCALL_ARGUMENTS_OFFSET));
    __Pyx_XDECREF(__pyx_t_4); __pyx_t_4 = 0;
    if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 158, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_1);
  }
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
```

</details>

L159  🟡  (score=2)
```python
        if self.access_path:
```
<details><summary>Show generated C (score=2)</summary>

```c
  if (__pyx_v_self->access_path == Py_None) __pyx_t_8 = 0;
  else
  {
    Py_ssize_t __pyx_temp = __Pyx_PyList_GET_SIZE(__pyx_v_self->access_path);
    if (unlikely(((!CYTHON_ASSUME_SAFE_SIZE) && __pyx_temp < 0))) __PYX_ERR(0, 159, __pyx_L1_error)
    __pyx_t_8 = (__pyx_temp != 0);
  }

  if (__pyx_t_8) {
/* … */
  }
```

</details>

L160  🟡  (score=4)
```python
            print(self.access_path)
```
<details><summary>Show generated C (score=4)</summary>

```c
    __pyx_t_4 = NULL;
    __pyx_t_5 = 1;
    {
      PyObject *__pyx_callargs[2] = {__pyx_t_4, __pyx_v_self->access_path};
      __pyx_t_1 = __Pyx_PyObject_FastCall((PyObject*)__pyx_builtin_print, __pyx_callargs+__pyx_t_5, (2-__pyx_t_5) | (__pyx_t_5*__Pyx_PY_VECTORCALL_ARGUMENTS_OFFSET));
      __Pyx_XDECREF(__pyx_t_4); __pyx_t_4 = 0;
      if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 160, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_1);
    }
    __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
```

</details>

L161  🔴  (score=18)
```python
            print(self.access_path[-1][0].pos)
```
<details><summary>Show generated C (score=18)</summary>

```c
    __pyx_t_4 = NULL;
    if (unlikely(__pyx_v_self->access_path == Py_None)) {
      PyErr_SetString(PyExc_TypeError, "'NoneType' object is not subscriptable");
      __PYX_ERR(0, 161, __pyx_L1_error)
    }
    __pyx_t_2 = __Pyx_GetItemInt_List(__pyx_v_self->access_path, -1L, long, 1, __Pyx_PyLong_From_long, 1, 1, 1, 1, __Pyx_ReferenceSharing_SharedReference); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 161, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_2);
    __pyx_t_3 = __Pyx_GetItemInt(__pyx_t_2, 0, long, 1, __Pyx_PyLong_From_long, 0, 0, 1, 1, __Pyx_ReferenceSharing_OwnStrongReference); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 161, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_3);
    __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
    __pyx_t_2 = __Pyx_PyObject_GetAttrStr(__pyx_t_3, __pyx_mstate_global->__pyx_n_u_pos); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 161, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_2);
    __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
    __pyx_t_5 = 1;
    {
      PyObject *__pyx_callargs[2] = {__pyx_t_4, __pyx_t_2};
      __pyx_t_1 = __Pyx_PyObject_FastCall((PyObject*)__pyx_builtin_print, __pyx_callargs+__pyx_t_5, (2-__pyx_t_5) | (__pyx_t_5*__Pyx_PY_VECTORCALL_ARGUMENTS_OFFSET));
      __Pyx_XDECREF(__pyx_t_4); __pyx_t_4 = 0;
      __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
      if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 161, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_1);
    }
    __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
```

</details>

L162  🔴  (score=18)
```python
            print(self.access_path[-1][0].__dict__)
```
<details><summary>Show generated C (score=18)</summary>

```c
    __pyx_t_2 = NULL;
    if (unlikely(__pyx_v_self->access_path == Py_None)) {
      PyErr_SetString(PyExc_TypeError, "'NoneType' object is not subscriptable");
      __PYX_ERR(0, 162, __pyx_L1_error)
    }
    __pyx_t_4 = __Pyx_GetItemInt_List(__pyx_v_self->access_path, -1L, long, 1, __Pyx_PyLong_From_long, 1, 1, 1, 1, __Pyx_ReferenceSharing_SharedReference); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 162, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_4);
    __pyx_t_3 = __Pyx_GetItemInt(__pyx_t_4, 0, long, 1, __Pyx_PyLong_From_long, 0, 0, 1, 1, __Pyx_ReferenceSharing_OwnStrongReference); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 162, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_3);
    __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
    __pyx_t_4 = __Pyx_PyObject_GetAttrStr(__pyx_t_3, __pyx_mstate_global->__pyx_n_u_dict); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 162, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_4);
    __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
    __pyx_t_5 = 1;
    {
      PyObject *__pyx_callargs[2] = {__pyx_t_2, __pyx_t_4};
      __pyx_t_1 = __Pyx_PyObject_FastCall((PyObject*)__pyx_builtin_print, __pyx_callargs+__pyx_t_5, (2-__pyx_t_5) | (__pyx_t_5*__Pyx_PY_VECTORCALL_ARGUMENTS_OFFSET));
      __Pyx_XDECREF(__pyx_t_2); __pyx_t_2 = 0;
      __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
      if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 162, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_1);
    }
    __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
```

</details>

L163  🔴  (score=33)
```python
        raise RuntimeError("Visitor %r does not accept object: %s" % (self, obj))
```
<details><summary>Show generated C (score=33)</summary>

```c
  __pyx_t_4 = NULL;
  __pyx_t_2 = __Pyx_PyObject_FormatSimpleAndDecref(PyObject_Repr(((PyObject *)__pyx_v_self)), __pyx_mstate_global->__pyx_empty_unicode); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 163, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __pyx_t_3 = __Pyx_PyObject_FormatSimpleAndDecref(PyObject_Str(__pyx_v_obj), __pyx_mstate_global->__pyx_empty_unicode); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 163, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_3);
  __pyx_t_9[0] = __pyx_mstate_global->__pyx_kp_u_Visitor;
  __pyx_t_9[1] = __pyx_t_2;
  __pyx_t_9[2] = __pyx_mstate_global->__pyx_kp_u_does_not_accept_object;
  __pyx_t_9[3] = __pyx_t_3;
  __pyx_t_10 = __Pyx_PyUnicode_Join(__pyx_t_9, 4, 8 + __Pyx_PyUnicode_GET_LENGTH(__pyx_t_2) + 25 + __Pyx_PyUnicode_GET_LENGTH(__pyx_t_3), 127 | __Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_2) | __Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_3));
  if (unlikely(!__pyx_t_10)) __PYX_ERR(0, 163, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_10);
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
  __pyx_t_5 = 1;
  {
    PyObject *__pyx_callargs[2] = {__pyx_t_4, __pyx_t_10};
    __pyx_t_1 = __Pyx_PyObject_FastCall((PyObject*)(((PyTypeObject*)PyExc_RuntimeError)), __pyx_callargs+__pyx_t_5, (2-__pyx_t_5) | (__pyx_t_5*__Pyx_PY_VECTORCALL_ARGUMENTS_OFFSET));
    __Pyx_XDECREF(__pyx_t_4); __pyx_t_4 = 0;
    __Pyx_DECREF(__pyx_t_10); __pyx_t_10 = 0;
    if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 163, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_1);
  }
  __Pyx_Raise(__pyx_t_1, 0, 0, 0);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __PYX_ERR(0, 163, __pyx_L1_error)
```

</details>

L164  ⚪  (score=0)
```python
```
L165  🔴  (score=69)
```python
    def visit(self, obj):
```
<details><summary>Show generated C (score=69)</summary>

```c
static PyObject *__pyx_pw_6Cython_8Compiler_7Visitor_11TreeVisitor_7visit(PyObject *__pyx_v_self, 
#if CYTHON_METH_FASTCALL
PyObject *const *__pyx_args, Py_ssize_t __pyx_nargs, PyObject *__pyx_kwds
#else
PyObject *__pyx_args, PyObject *__pyx_kwds
#endif
); /*proto*/
static PyObject *__pyx_f_6Cython_8Compiler_7Visitor_11TreeVisitor_visit(struct __pyx_obj_6Cython_8Compiler_7Visitor_TreeVisitor *__pyx_v_self, PyObject *__pyx_v_obj, int __pyx_skip_dispatch) {
  PyObject *__pyx_r = NULL;
  /* Check if called by wrapper */
  if (unlikely(__pyx_skip_dispatch)) ;
  /* Check if overridden in Python */
  else if (
  #if !CYTHON_USE_TYPE_SLOTS
  unlikely(Py_TYPE(((PyObject *)__pyx_v_self)) != __pyx_mstate_global->__pyx_ptype_6Cython_8Compiler_7Visitor_TreeVisitor &&
  __Pyx_PyType_HasFeature(Py_TYPE(((PyObject *)__pyx_v_self)), Py_TPFLAGS_HAVE_GC))
  #else
  unlikely(Py_TYPE(((PyObject *)__pyx_v_self))->tp_dictoffset != 0 || __Pyx_PyType_HasFeature(Py_TYPE(((PyObject *)__pyx_v_self)), (Py_TPFLAGS_IS_ABSTRACT | Py_TPFLAGS_HEAPTYPE)))
  #endif
  ) {
    #if CYTHON_USE_DICT_VERSIONS && CYTHON_USE_PYTYPE_LOOKUP && CYTHON_USE_TYPE_SLOTS
    static PY_UINT64_T __pyx_tp_dict_version = __PYX_DICT_VERSION_INIT, __pyx_obj_dict_version = __PYX_DICT_VERSION_INIT;
    if (unlikely(!__Pyx_object_dict_version_matches(((PyObject *)__pyx_v_self), __pyx_tp_dict_version, __pyx_obj_dict_version))) {
      PY_UINT64_T __pyx_typedict_guard = __Pyx_get_tp_dict_version(((PyObject *)__pyx_v_self));
      #endif
      __pyx_t_1 = __Pyx_PyObject_GetAttrStr(((PyObject *)__pyx_v_self), __pyx_mstate_global->__pyx_n_u_visit_2); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 165, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_1);
      if (!__Pyx_IsSameCFunction(__pyx_t_1, (void(*)(void)) __pyx_pw_6Cython_8Compiler_7Visitor_11TreeVisitor_7visit)) {
        __Pyx_XDECREF(__pyx_r);
        __pyx_t_3 = NULL;
        __Pyx_INCREF(__pyx_t_1);
        __pyx_t_4 = __pyx_t_1; 
        __pyx_t_5 = 1;
        #if CYTHON_UNPACK_METHODS
        if (unlikely(PyMethod_Check(__pyx_t_4))) {
          __pyx_t_3 = PyMethod_GET_SELF(__pyx_t_4);
          assert(__pyx_t_3);
          PyObject* __pyx__function = PyMethod_GET_FUNCTION(__pyx_t_4);
          __Pyx_INCREF(__pyx_t_3);
          __Pyx_INCREF(__pyx__function);
          __Pyx_DECREF_SET(__pyx_t_4, __pyx__function);
          __pyx_t_5 = 0;
        }
        #endif
        {
          PyObject *__pyx_callargs[2] = {__pyx_t_3, __pyx_v_obj};
          __pyx_t_2 = __Pyx_PyObject_FastCall((PyObject*)__pyx_t_4, __pyx_callargs+__pyx_t_5, (2-__pyx_t_5) | (__pyx_t_5*__Pyx_PY_VECTORCALL_ARGUMENTS_OFFSET));
          __Pyx_XDECREF(__pyx_t_3); __pyx_t_3 = 0;
          __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
          if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 165, __pyx_L1_error)
          __Pyx_GOTREF(__pyx_t_2);
        }
        __pyx_r = __pyx_t_2;
        __pyx_t_2 = 0;
        __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
        goto __pyx_L0;
      }
      #if CYTHON_USE_DICT_VERSIONS && CYTHON_USE_PYTYPE_LOOKUP && CYTHON_USE_TYPE_SLOTS
      __pyx_tp_dict_version = __Pyx_get_tp_dict_version(((PyObject *)__pyx_v_self));
      __pyx_obj_dict_version = __Pyx_get_object_dict_version(((PyObject *)__pyx_v_self));
      if (unlikely(__pyx_typedict_guard != __pyx_tp_dict_version)) {
        __pyx_tp_dict_version = __pyx_obj_dict_version = __PYX_DICT_VERSION_INIT;
      }
      #endif
      __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
      #if CYTHON_USE_DICT_VERSIONS && CYTHON_USE_PYTYPE_LOOKUP && CYTHON_USE_TYPE_SLOTS
    }
    #endif
  }
/* … */
  /* function exit code */
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_t_1);
  __Pyx_XDECREF(__pyx_t_2);
  __Pyx_XDECREF(__pyx_t_3);
  __Pyx_XDECREF(__pyx_t_4);
  __Pyx_AddTraceback("Cython.Compiler.Visitor.TreeVisitor.visit", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_r = 0;
  __pyx_L0:;
  __Pyx_XGIVEREF(__pyx_r);
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}

/* Python wrapper */
static PyObject *__pyx_pw_6Cython_8Compiler_7Visitor_11TreeVisitor_7visit(PyObject *__pyx_v_self, 
#if CYTHON_METH_FASTCALL
PyObject *const *__pyx_args, Py_ssize_t __pyx_nargs, PyObject *__pyx_kwds
#else
PyObject *__pyx_args, PyObject *__pyx_kwds
#endif
); /*proto*/
PyDoc_STRVAR(__pyx_doc_6Cython_8Compiler_7Visitor_11TreeVisitor_6visit, "File: Cython/Compiler/Visitor.py (starting at line 165)");
static PyMethodDef __pyx_mdef_6Cython_8Compiler_7Visitor_11TreeVisitor_7visit = {"visit", (PyCFunction)(void(*)(void))(__Pyx_PyCFunction_FastCallWithKeywords)__pyx_pw_6Cython_8Compiler_7Visitor_11TreeVisitor_7visit, __Pyx_METH_FASTCALL|METH_KEYWORDS, __pyx_doc_6Cython_8Compiler_7Visitor_11TreeVisitor_6visit};
static PyObject *__pyx_pw_6Cython_8Compiler_7Visitor_11TreeVisitor_7visit(PyObject *__pyx_v_self, 
#if CYTHON_METH_FASTCALL
PyObject *const *__pyx_args, Py_ssize_t __pyx_nargs, PyObject *__pyx_kwds
#else
PyObject *__pyx_args, PyObject *__pyx_kwds
#endif
) {
  PyObject *__pyx_v_obj = 0;
  #if !CYTHON_METH_FASTCALL
  CYTHON_UNUSED Py_ssize_t __pyx_nargs;
  #endif
  CYTHON_UNUSED PyObject *const *__pyx_kwvalues;
  PyObject *__pyx_r = 0;
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("visit (wrapper)", 0);
  #if !CYTHON_METH_FASTCALL
  #if CYTHON_ASSUME_SAFE_SIZE
  __pyx_nargs = PyTuple_GET_SIZE(__pyx_args);
  #else
  __pyx_nargs = PyTuple_Size(__pyx_args); if (unlikely(__pyx_nargs < 0)) return NULL;
  #endif
  #endif
  __pyx_kwvalues = __Pyx_KwValues_FASTCALL(__pyx_args, __pyx_nargs);
  {
    PyObject ** const __pyx_pyargnames[] = {&__pyx_mstate_global->__pyx_n_u_obj,0};
  PyObject* values[1] = {0};
    const Py_ssize_t __pyx_kwds_len = (__pyx_kwds) ? __Pyx_NumKwargs_FASTCALL(__pyx_kwds) : 0;
    if (unlikely(__pyx_kwds_len) < 0) __PYX_ERR(0, 165, __pyx_L3_error)
    if (__pyx_kwds_len > 0) {
      switch (__pyx_nargs) {
        case  1:
        values[0] = __Pyx_ArgRef_FASTCALL(__pyx_args, 0);
        if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[0])) __PYX_ERR(0, 165, __pyx_L3_error)
        CYTHON_FALLTHROUGH;
        case  0: break;
        default: goto __pyx_L5_argtuple_error;
      }
      const Py_ssize_t kwd_pos_args = __pyx_nargs;
      if (__Pyx_ParseKeywords(__pyx_kwds, __pyx_kwvalues, __pyx_pyargnames, 0, values, kwd_pos_args, __pyx_kwds_len, "visit", 0) < (0)) __PYX_ERR(0, 165, __pyx_L3_error)
      for (Py_ssize_t i = __pyx_nargs; i < 1; i++) {
        if (unlikely(!values[i])) { __Pyx_RaiseArgtupleInvalid("visit", 1, 1, 1, i); __PYX_ERR(0, 165, __pyx_L3_error) }
      }
    } else if (unlikely(__pyx_nargs != 1)) {
      goto __pyx_L5_argtuple_error;
    } else {
      values[0] = __Pyx_ArgRef_FASTCALL(__pyx_args, 0);
      if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[0])) __PYX_ERR(0, 165, __pyx_L3_error)
    }
    __pyx_v_obj = values[0];
  }
  goto __pyx_L6_skip;
  __pyx_L5_argtuple_error:;
  __Pyx_RaiseArgtupleInvalid("visit", 1, 1, 1, __pyx_nargs); __PYX_ERR(0, 165, __pyx_L3_error)
  __pyx_L6_skip:;
  goto __pyx_L4_argument_unpacking_done;
  __pyx_L3_error:;
  for (Py_ssize_t __pyx_temp=0; __pyx_temp < (Py_ssize_t)(sizeof(values)/sizeof(values[0])); ++__pyx_temp) {
    Py_XDECREF(values[__pyx_temp]);
  }
  __Pyx_AddTraceback("Cython.Compiler.Visitor.TreeVisitor.visit", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __Pyx_RefNannyFinishContext();
  return NULL;
  __pyx_L4_argument_unpacking_done:;
  __pyx_r = __pyx_pf_6Cython_8Compiler_7Visitor_11TreeVisitor_6visit(((struct __pyx_obj_6Cython_8Compiler_7Visitor_TreeVisitor *)__pyx_v_self), __pyx_v_obj);
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

static PyObject *__pyx_pf_6Cython_8Compiler_7Visitor_11TreeVisitor_6visit(struct __pyx_obj_6Cython_8Compiler_7Visitor_TreeVisitor *__pyx_v_self, PyObject *__pyx_v_obj) {
  PyObject *__pyx_r = NULL;
  __Pyx_XDECREF(__pyx_r);
  __pyx_t_1 = __pyx_f_6Cython_8Compiler_7Visitor_11TreeVisitor_visit(__pyx_v_self, __pyx_v_obj, 1); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 165, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __pyx_r = __pyx_t_1;
  __pyx_t_1 = 0;
  goto __pyx_L0;

  /* function exit code */
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_t_1);
  __Pyx_AddTraceback("Cython.Compiler.Visitor.TreeVisitor.visit", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_r = NULL;
  __pyx_L0:;
  __Pyx_XGIVEREF(__pyx_r);
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}
/* … */
  __pyx_t_2 = __Pyx_CyFunction_New(&__pyx_mdef_6Cython_8Compiler_7Visitor_11TreeVisitor_7visit, __Pyx_CYFUNCTION_CCLASS, __pyx_mstate_global->__pyx_n_u_TreeVisitor_visit, NULL, __pyx_mstate_global->__pyx_n_u_Cython_Compiler_Visitor, __pyx_mstate_global->__pyx_d, ((PyObject *)__pyx_mstate_global->__pyx_codeobj_tab[2])); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 165, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  #if CYTHON_COMPILING_IN_CPYTHON && PY_VERSION_HEX >= 0x030E0000
  PyUnstable_Object_EnableDeferredRefcount(__pyx_t_2);
  #endif
  if (__Pyx_SetItemOnTypeDict(__pyx_mstate_global->__pyx_ptype_6Cython_8Compiler_7Visitor_TreeVisitor, __pyx_mstate_global->__pyx_n_u_visit_2, __pyx_t_2) < (0)) __PYX_ERR(0, 165, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
```

</details>

L166  ⚪  (score=0)
```python
        # generic def entry point for calls from Python subclasses
```
L167  🟡  (score=1)
```python
        return self._visit(obj)
```
<details><summary>Show generated C (score=1)</summary>

```c
  __Pyx_XDECREF(__pyx_r);
  __pyx_t_1 = __pyx_f_6Cython_8Compiler_7Visitor_11TreeVisitor__visit(__pyx_v_self, __pyx_v_obj); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 167, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __pyx_r = __pyx_t_1;
  __pyx_t_1 = 0;
  goto __pyx_L0;
```

</details>

L168  ⚪  (score=0)
```python
```
L169  🔴  (score=10)
```python
    @cython.final
```
<details><summary>Show generated C (score=10)</summary>

```c
static PyObject *__pyx_f_6Cython_8Compiler_7Visitor_11TreeVisitor__visit(struct __pyx_obj_6Cython_8Compiler_7Visitor_TreeVisitor *__pyx_v_self, PyObject *__pyx_v_obj) {
  PyObject *__pyx_v_handler_method = NULL;
  PyObject *__pyx_v_e = NULL;
  PyObject *__pyx_r = NULL;
/* … */
  /* function exit code */
  __pyx_r = Py_None; __Pyx_INCREF(Py_None);
  goto __pyx_L0;
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_t_7);
  __Pyx_XDECREF(__pyx_t_9);
  __Pyx_XDECREF(__pyx_t_10);
  __Pyx_XDECREF(__pyx_t_11);
  __Pyx_XDECREF(__pyx_t_13);
  __Pyx_AddTraceback("Cython.Compiler.Visitor.TreeVisitor._visit", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_r = 0;
  __pyx_L0:;
  __Pyx_XDECREF(__pyx_v_handler_method);
  __Pyx_XDECREF(__pyx_v_e);
  __Pyx_XGIVEREF(__pyx_r);
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}
```

</details>

L170  ⚪  (score=0)
```python
    def _visit(self, obj):
```
L171  ⚪  (score=0)
```python
        # fast cdef entry point for calls from Cython subclasses
```
L172  🔴  (score=10)
```python
        try:
```
<details><summary>Show generated C (score=10)</summary>

```c
  {
    /*try:*/ {
/* … */
    }
    __pyx_L3_error:;
    __Pyx_XDECREF(__pyx_t_10); __pyx_t_10 = 0;
    __Pyx_XDECREF(__pyx_t_11); __pyx_t_11 = 0;
    __Pyx_XDECREF(__pyx_t_7); __pyx_t_7 = 0;
    __Pyx_XDECREF(__pyx_t_9); __pyx_t_9 = 0;
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
    __pyx_L4_exception_handled:;
    __Pyx_XGIVEREF(__pyx_t_1);
    __Pyx_XGIVEREF(__pyx_t_2);
    __Pyx_XGIVEREF(__pyx_t_3);
    __Pyx_ExceptionReset(__pyx_t_1, __pyx_t_2, __pyx_t_3);
  }
```

</details>

L173  🟠  (score=8)
```python
            try:
```
<details><summary>Show generated C (score=8)</summary>

```c
      {
        /*try:*/ {
/* … */
        }
        __Pyx_XDECREF(__pyx_t_4); __pyx_t_4 = 0;
        __Pyx_XDECREF(__pyx_t_5); __pyx_t_5 = 0;
        __Pyx_XDECREF(__pyx_t_6); __pyx_t_6 = 0;
        goto __pyx_L14_try_end;
        __pyx_L9_error:;
        __Pyx_XDECREF(__pyx_t_7); __pyx_t_7 = 0;
/* … */
        __pyx_L11_except_error:;
        __Pyx_XGIVEREF(__pyx_t_4);
        __Pyx_XGIVEREF(__pyx_t_5);
        __Pyx_XGIVEREF(__pyx_t_6);
        __Pyx_ExceptionReset(__pyx_t_4, __pyx_t_5, __pyx_t_6);
        goto __pyx_L3_error;
        __pyx_L10_exception_handled:;
        __Pyx_XGIVEREF(__pyx_t_4);
        __Pyx_XGIVEREF(__pyx_t_5);
        __Pyx_XGIVEREF(__pyx_t_6);
        __Pyx_ExceptionReset(__pyx_t_4, __pyx_t_5, __pyx_t_6);
        __pyx_L14_try_end:;
      }
```

</details>

L174  🟠  (score=7)
```python
                handler_method = self.dispatch_table[type(obj)]
```
<details><summary>Show generated C (score=7)</summary>

```c
          if (unlikely(__pyx_v_self->dispatch_table == Py_None)) {
            PyErr_SetString(PyExc_TypeError, "'NoneType' object is not subscriptable");
            __PYX_ERR(0, 174, __pyx_L9_error)
          }
          __pyx_t_7 = __Pyx_PyDict_GetItem(__pyx_v_self->dispatch_table, ((PyObject *)Py_TYPE(__pyx_v_obj))); if (unlikely(!__pyx_t_7)) __PYX_ERR(0, 174, __pyx_L9_error)
          __Pyx_GOTREF(__pyx_t_7);
          __pyx_v_handler_method = __pyx_t_7;
          __pyx_t_7 = 0;
```

</details>

L175  🟠  (score=6)
```python
            except KeyError:
```
<details><summary>Show generated C (score=6)</summary>

```c
        __pyx_t_8 = __Pyx_PyErr_ExceptionMatches(((PyObject *)(((PyTypeObject*)PyExc_KeyError))));
        if (__pyx_t_8) {
          __Pyx_AddTraceback("Cython.Compiler.Visitor.TreeVisitor._visit", __pyx_clineno, __pyx_lineno, __pyx_filename);
          if (__Pyx_GetException(&__pyx_t_7, &__pyx_t_9, &__pyx_t_10) < 0) __PYX_ERR(0, 175, __pyx_L11_except_error)
          __Pyx_XGOTREF(__pyx_t_7);
          __Pyx_XGOTREF(__pyx_t_9);
          __Pyx_XGOTREF(__pyx_t_10);
```

</details>

L176  🟡  (score=1)
```python
                handler_method = self.find_handler(obj)
```
<details><summary>Show generated C (score=1)</summary>

```c
          __pyx_t_11 = __pyx_f_6Cython_8Compiler_7Visitor_11TreeVisitor_find_handler(__pyx_v_self, __pyx_v_obj); if (unlikely(!__pyx_t_11)) __PYX_ERR(0, 176, __pyx_L11_except_error)
          __Pyx_GOTREF(__pyx_t_11);
          __Pyx_XDECREF_SET(__pyx_v_handler_method, __pyx_t_11);
          __pyx_t_11 = 0;
```

</details>

L177  🔴  (score=13)
```python
                self.dispatch_table[type(obj)] = handler_method
```
<details><summary>Show generated C (score=13)</summary>

```c
          if (unlikely(__pyx_v_self->dispatch_table == Py_None)) {
            PyErr_SetString(PyExc_TypeError, "'NoneType' object is not subscriptable");
            __PYX_ERR(0, 177, __pyx_L11_except_error)
          }
          if (unlikely((PyDict_SetItem(__pyx_v_self->dispatch_table, ((PyObject *)Py_TYPE(__pyx_v_obj)), __pyx_v_handler_method) < 0))) __PYX_ERR(0, 177, __pyx_L11_except_error)
          __Pyx_XDECREF(__pyx_t_7); __pyx_t_7 = 0;
          __Pyx_XDECREF(__pyx_t_9); __pyx_t_9 = 0;
          __Pyx_XDECREF(__pyx_t_10); __pyx_t_10 = 0;
          goto __pyx_L10_exception_handled;
        }
        goto __pyx_L11_except_error;
```

</details>

L178  🔴  (score=16)
```python
            return handler_method(obj)
```
<details><summary>Show generated C (score=16)</summary>

```c
      __Pyx_XDECREF(__pyx_r);
      __pyx_t_9 = NULL;
      __Pyx_INCREF(__pyx_v_handler_method);
      __pyx_t_7 = __pyx_v_handler_method; 
      __pyx_t_12 = 1;
      #if CYTHON_UNPACK_METHODS
      if (unlikely(PyMethod_Check(__pyx_t_7))) {
        __pyx_t_9 = PyMethod_GET_SELF(__pyx_t_7);
        assert(__pyx_t_9);
        PyObject* __pyx__function = PyMethod_GET_FUNCTION(__pyx_t_7);
        __Pyx_INCREF(__pyx_t_9);
        __Pyx_INCREF(__pyx__function);
        __Pyx_DECREF_SET(__pyx_t_7, __pyx__function);
        __pyx_t_12 = 0;
      }
      #endif
      {
        PyObject *__pyx_callargs[2] = {__pyx_t_9, __pyx_v_obj};
        __pyx_t_10 = __Pyx_PyObject_FastCall((PyObject*)__pyx_t_7, __pyx_callargs+__pyx_t_12, (2-__pyx_t_12) | (__pyx_t_12*__Pyx_PY_VECTORCALL_ARGUMENTS_OFFSET));
        __Pyx_XDECREF(__pyx_t_9); __pyx_t_9 = 0;
        __Pyx_DECREF(__pyx_t_7); __pyx_t_7 = 0;
        if (unlikely(!__pyx_t_10)) __PYX_ERR(0, 178, __pyx_L3_error)
        __Pyx_GOTREF(__pyx_t_10);
      }
      __pyx_r = __pyx_t_10;
      __pyx_t_10 = 0;
      goto __pyx_L7_try_return;
```

</details>

L179  🔴  (score=16)
```python
        except Errors.CompileError:
```
<details><summary>Show generated C (score=16)</summary>

```c
    __Pyx_ErrFetch(&__pyx_t_10, &__pyx_t_7, &__pyx_t_9);
    __Pyx_GetModuleGlobalName(__pyx_t_11, __pyx_mstate_global->__pyx_n_u_Errors); if (unlikely(!__pyx_t_11)) __PYX_ERR(0, 179, __pyx_L5_except_error)
    __Pyx_GOTREF(__pyx_t_11);
    __pyx_t_13 = __Pyx_PyObject_GetAttrStr(__pyx_t_11, __pyx_mstate_global->__pyx_n_u_CompileError); if (unlikely(!__pyx_t_13)) __PYX_ERR(0, 179, __pyx_L5_except_error)
    __Pyx_GOTREF(__pyx_t_13);
    __Pyx_DECREF(__pyx_t_11); __pyx_t_11 = 0;
    __pyx_t_8 = __Pyx_PyErr_GivenExceptionMatches(__pyx_t_10, __pyx_t_13);
    __Pyx_DECREF(__pyx_t_13); __pyx_t_13 = 0;
    __Pyx_ErrRestore(__pyx_t_10, __pyx_t_7, __pyx_t_9);
    __pyx_t_10 = 0; __pyx_t_7 = 0; __pyx_t_9 = 0;
    if (__pyx_t_8) {
      __Pyx_AddTraceback("Cython.Compiler.Visitor.TreeVisitor._visit", __pyx_clineno, __pyx_lineno, __pyx_filename);
      if (__Pyx_GetException(&__pyx_t_9, &__pyx_t_7, &__pyx_t_10) < 0) __PYX_ERR(0, 179, __pyx_L5_except_error)
      __Pyx_XGOTREF(__pyx_t_9);
      __Pyx_XGOTREF(__pyx_t_7);
      __Pyx_XGOTREF(__pyx_t_10);
```

</details>

L180  🟡  (score=2)
```python
            raise
```
<details><summary>Show generated C (score=2)</summary>

```c
      __Pyx_GIVEREF(__pyx_t_9);
      __Pyx_GIVEREF(__pyx_t_7);
      __Pyx_XGIVEREF(__pyx_t_10);
      __Pyx_ErrRestoreWithState(__pyx_t_9, __pyx_t_7, __pyx_t_10);
      __pyx_t_9 = 0;  __pyx_t_7 = 0;  __pyx_t_10 = 0; 
      __PYX_ERR(0, 180, __pyx_L5_except_error)
    }
```

</details>

L181  🔴  (score=16)
```python
        except Errors.AbortError:
```
<details><summary>Show generated C (score=16)</summary>

```c
    __Pyx_ErrFetch(&__pyx_t_10, &__pyx_t_7, &__pyx_t_9);
    __Pyx_GetModuleGlobalName(__pyx_t_13, __pyx_mstate_global->__pyx_n_u_Errors); if (unlikely(!__pyx_t_13)) __PYX_ERR(0, 181, __pyx_L5_except_error)
    __Pyx_GOTREF(__pyx_t_13);
    __pyx_t_11 = __Pyx_PyObject_GetAttrStr(__pyx_t_13, __pyx_mstate_global->__pyx_n_u_AbortError); if (unlikely(!__pyx_t_11)) __PYX_ERR(0, 181, __pyx_L5_except_error)
    __Pyx_GOTREF(__pyx_t_11);
    __Pyx_DECREF(__pyx_t_13); __pyx_t_13 = 0;
    __pyx_t_8 = __Pyx_PyErr_GivenExceptionMatches(__pyx_t_10, __pyx_t_11);
    __Pyx_DECREF(__pyx_t_11); __pyx_t_11 = 0;
    __Pyx_ErrRestore(__pyx_t_10, __pyx_t_7, __pyx_t_9);
    __pyx_t_10 = 0; __pyx_t_7 = 0; __pyx_t_9 = 0;
    if (__pyx_t_8) {
      __Pyx_AddTraceback("Cython.Compiler.Visitor.TreeVisitor._visit", __pyx_clineno, __pyx_lineno, __pyx_filename);
      if (__Pyx_GetException(&__pyx_t_9, &__pyx_t_7, &__pyx_t_10) < 0) __PYX_ERR(0, 181, __pyx_L5_except_error)
      __Pyx_XGOTREF(__pyx_t_9);
      __Pyx_XGOTREF(__pyx_t_7);
      __Pyx_XGOTREF(__pyx_t_10);
```

</details>

L182  🟡  (score=2)
```python
            raise
```
<details><summary>Show generated C (score=2)</summary>

```c
      __Pyx_GIVEREF(__pyx_t_9);
      __Pyx_GIVEREF(__pyx_t_7);
      __Pyx_XGIVEREF(__pyx_t_10);
      __Pyx_ErrRestoreWithState(__pyx_t_9, __pyx_t_7, __pyx_t_10);
      __pyx_t_9 = 0;  __pyx_t_7 = 0;  __pyx_t_10 = 0; 
      __PYX_ERR(0, 182, __pyx_L5_except_error)
    }
```

</details>

L183  🔴  (score=24)
```python
        except Exception as e:
```
<details><summary>Show generated C (score=24)</summary>

```c
    __pyx_t_8 = __Pyx_PyErr_ExceptionMatches(((PyObject *)(((PyTypeObject*)PyExc_Exception))));
    if (__pyx_t_8) {
      __Pyx_AddTraceback("Cython.Compiler.Visitor.TreeVisitor._visit", __pyx_clineno, __pyx_lineno, __pyx_filename);
      if (__Pyx_GetException(&__pyx_t_10, &__pyx_t_7, &__pyx_t_9) < 0) __PYX_ERR(0, 183, __pyx_L5_except_error)
      __Pyx_XGOTREF(__pyx_t_10);
      __Pyx_XGOTREF(__pyx_t_7);
      __Pyx_XGOTREF(__pyx_t_9);
      __Pyx_INCREF(__pyx_t_7);
      __pyx_v_e = __pyx_t_7;
      /*try:*/ {
/* … */
      /*finally:*/ {
        /*normal exit:*/{
          __Pyx_DECREF(__pyx_v_e); __pyx_v_e = 0;
          goto __pyx_L27;
        }
        __pyx_L26_error:;
        /*exception exit:*/{
          __Pyx_PyThreadState_declare
          __Pyx_PyThreadState_assign
          __pyx_t_6 = 0; __pyx_t_5 = 0; __pyx_t_4 = 0; __pyx_t_17 = 0; __pyx_t_18 = 0; __pyx_t_19 = 0;
          __Pyx_XDECREF(__pyx_t_11); __pyx_t_11 = 0;
          __Pyx_XDECREF(__pyx_t_13); __pyx_t_13 = 0;
           __Pyx_ExceptionSwap(&__pyx_t_17, &__pyx_t_18, &__pyx_t_19);
          if ( unlikely(__Pyx_GetException(&__pyx_t_6, &__pyx_t_5, &__pyx_t_4) < 0)) __Pyx_ErrFetch(&__pyx_t_6, &__pyx_t_5, &__pyx_t_4);
          __Pyx_XGOTREF(__pyx_t_6);
          __Pyx_XGOTREF(__pyx_t_5);
          __Pyx_XGOTREF(__pyx_t_4);
          __Pyx_XGOTREF(__pyx_t_17);
          __Pyx_XGOTREF(__pyx_t_18);
          __Pyx_XGOTREF(__pyx_t_19);
          __pyx_t_8 = __pyx_lineno; __pyx_t_15 = __pyx_clineno; __pyx_t_16 = __pyx_filename;
          {
            __Pyx_DECREF(__pyx_v_e); __pyx_v_e = 0;
          }
          __Pyx_XGIVEREF(__pyx_t_17);
          __Pyx_XGIVEREF(__pyx_t_18);
          __Pyx_XGIVEREF(__pyx_t_19);
          __Pyx_ExceptionReset(__pyx_t_17, __pyx_t_18, __pyx_t_19);
          __Pyx_XGIVEREF(__pyx_t_6);
          __Pyx_XGIVEREF(__pyx_t_5);
          __Pyx_XGIVEREF(__pyx_t_4);
          __Pyx_ErrRestore(__pyx_t_6, __pyx_t_5, __pyx_t_4);
          __pyx_t_6 = 0; __pyx_t_5 = 0; __pyx_t_4 = 0; __pyx_t_17 = 0; __pyx_t_18 = 0; __pyx_t_19 = 0;
          __pyx_lineno = __pyx_t_8; __pyx_clineno = __pyx_t_15; __pyx_filename = __pyx_t_16;
          goto __pyx_L5_except_error;
        }
        __pyx_L27:;
      }
      __Pyx_XDECREF(__pyx_t_10); __pyx_t_10 = 0;
      __Pyx_XDECREF(__pyx_t_7); __pyx_t_7 = 0;
      __Pyx_XDECREF(__pyx_t_9); __pyx_t_9 = 0;
      goto __pyx_L4_exception_handled;
    }
    goto __pyx_L5_except_error;
```

</details>

L184  🟠  (score=8)
```python
            if DebugFlags.debug_no_exception_intercept:
```
<details><summary>Show generated C (score=8)</summary>

```c
        __Pyx_GetModuleGlobalName(__pyx_t_11, __pyx_mstate_global->__pyx_n_u_DebugFlags); if (unlikely(!__pyx_t_11)) __PYX_ERR(0, 184, __pyx_L26_error)
        __Pyx_GOTREF(__pyx_t_11);
        __pyx_t_13 = __Pyx_PyObject_GetAttrStr(__pyx_t_11, __pyx_mstate_global->__pyx_n_u_debug_no_exception_intercept); if (unlikely(!__pyx_t_13)) __PYX_ERR(0, 184, __pyx_L26_error)
        __Pyx_GOTREF(__pyx_t_13);
        __Pyx_DECREF(__pyx_t_11); __pyx_t_11 = 0;
        __pyx_t_14 = __Pyx_PyObject_IsTrue(__pyx_t_13); if (unlikely((__pyx_t_14 < 0))) __PYX_ERR(0, 184, __pyx_L26_error)
        __Pyx_DECREF(__pyx_t_13); __pyx_t_13 = 0;
        if (unlikely(__pyx_t_14)) {
/* … */
        }
```

</details>

L185  🟡  (score=2)
```python
                raise
```
<details><summary>Show generated C (score=2)</summary>

```c
          __Pyx_GIVEREF(__pyx_t_10);
          __Pyx_GIVEREF(__pyx_t_7);
          __Pyx_XGIVEREF(__pyx_t_9);
          __Pyx_ErrRestoreWithState(__pyx_t_10, __pyx_t_7, __pyx_t_9);
          __pyx_t_10 = 0;  __pyx_t_7 = 0;  __pyx_t_9 = 0; 
          __PYX_ERR(0, 185, __pyx_L26_error)
```

</details>

L186  🟡  (score=1)
```python
            self._raise_compiler_error(obj, e)
```
<details><summary>Show generated C (score=1)</summary>

```c
        __pyx_t_13 = ((struct __pyx_vtabstruct_6Cython_8Compiler_7Visitor_TreeVisitor *)__pyx_v_self->__pyx_vtab)->_raise_compiler_error(__pyx_v_self, __pyx_v_obj, __pyx_v_e); if (unlikely(!__pyx_t_13)) __PYX_ERR(0, 186, __pyx_L26_error)
        __Pyx_GOTREF(__pyx_t_13);
        __Pyx_DECREF(__pyx_t_13); __pyx_t_13 = 0;
      }
```

</details>

L187  ⚪  (score=0)
```python
```
L188  🟡  (score=4)
```python
    @cython.final
```
<details><summary>Show generated C (score=4)</summary>

```c
static PyObject *__pyx_f_6Cython_8Compiler_7Visitor_11TreeVisitor__visitchild(struct __pyx_obj_6Cython_8Compiler_7Visitor_TreeVisitor *__pyx_v_self, PyObject *__pyx_v_child, PyObject *__pyx_v_parent, PyObject *__pyx_v_attrname, PyObject *__pyx_v_idx) {
  PyObject *__pyx_v_result = NULL;
  PyObject *__pyx_r = NULL;
/* … */
  /* function exit code */
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_t_1);
  __Pyx_AddTraceback("Cython.Compiler.Visitor.TreeVisitor._visitchild", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_r = 0;
  __pyx_L0:;
  __Pyx_XDECREF(__pyx_v_result);
  __Pyx_XGIVEREF(__pyx_r);
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}
```

</details>

L189  ⚪  (score=0)
```python
    def _visitchild(self, child, parent, attrname, idx):
```
L190  ⚪  (score=0)
```python
        # fast cdef entry point for calls from Cython subclasses
```
L191  🔴  (score=22)
```python
        self.access_path.append((parent, attrname, idx))
```
<details><summary>Show generated C (score=22)</summary>

```c
  if (unlikely(__pyx_v_self->access_path == Py_None)) {
    PyErr_Format(PyExc_AttributeError, "'NoneType' object has no attribute '%.30s'", "append");
    __PYX_ERR(0, 191, __pyx_L1_error)
  }
  __pyx_t_1 = PyTuple_New(3); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 191, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_INCREF(__pyx_v_parent);
  __Pyx_GIVEREF(__pyx_v_parent);
  if (__Pyx_PyTuple_SET_ITEM(__pyx_t_1, 0, __pyx_v_parent) != (0)) __PYX_ERR(0, 191, __pyx_L1_error);
  __Pyx_INCREF(__pyx_v_attrname);
  __Pyx_GIVEREF(__pyx_v_attrname);
  if (__Pyx_PyTuple_SET_ITEM(__pyx_t_1, 1, __pyx_v_attrname) != (0)) __PYX_ERR(0, 191, __pyx_L1_error);
  __Pyx_INCREF(__pyx_v_idx);
  __Pyx_GIVEREF(__pyx_v_idx);
  if (__Pyx_PyTuple_SET_ITEM(__pyx_t_1, 2, __pyx_v_idx) != (0)) __PYX_ERR(0, 191, __pyx_L1_error);
  __pyx_t_2 = __Pyx_PyList_Append(__pyx_v_self->access_path, __pyx_t_1); if (unlikely(__pyx_t_2 == ((int)-1))) __PYX_ERR(0, 191, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
```

</details>

L192  ⚪  (score=0)
```python
        result = self._visit(child)
```
<details><summary>Show generated C (score=0)</summary>

```c
  __pyx_t_1 = __pyx_f_6Cython_8Compiler_7Visitor_11TreeVisitor__visit(__pyx_v_self, __pyx_v_child); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 192, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __pyx_v_result = __pyx_t_1;
  __pyx_t_1 = 0;
```

</details>

L193  🟠  (score=8)
```python
        self.access_path.pop()
```
<details><summary>Show generated C (score=8)</summary>

```c
  if (unlikely(__pyx_v_self->access_path == Py_None)) {
    PyErr_Format(PyExc_AttributeError, "'NoneType' object has no attribute '%.30s'", "pop");
    __PYX_ERR(0, 193, __pyx_L1_error)
  }
  __pyx_t_1 = __Pyx_PyList_Pop(__pyx_v_self->access_path); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 193, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
```

</details>

L194  🟡  (score=2)
```python
        return result
```
<details><summary>Show generated C (score=2)</summary>

```c
  __Pyx_XDECREF(__pyx_r);
  __Pyx_INCREF(__pyx_v_result);
  __pyx_r = __pyx_v_result;
  goto __pyx_L0;
```

</details>

L195  ⚪  (score=0)
```python
```
L196  🔴  (score=92)
```python
    def visitchildren(self, parent, attrs=None, exclude=None):
```
<details><summary>Show generated C (score=92)</summary>

```c
static PyObject *__pyx_pw_6Cython_8Compiler_7Visitor_11TreeVisitor_9visitchildren(PyObject *__pyx_v_self, 
#if CYTHON_METH_FASTCALL
PyObject *const *__pyx_args, Py_ssize_t __pyx_nargs, PyObject *__pyx_kwds
#else
PyObject *__pyx_args, PyObject *__pyx_kwds
#endif
); /*proto*/
static PyObject *__pyx_f_6Cython_8Compiler_7Visitor_11TreeVisitor_visitchildren(struct __pyx_obj_6Cython_8Compiler_7Visitor_TreeVisitor *__pyx_v_self, PyObject *__pyx_v_parent, int __pyx_skip_dispatch, struct __pyx_opt_args_6Cython_8Compiler_7Visitor_11TreeVisitor_visitchildren *__pyx_optional_args) {
  PyObject *__pyx_v_attrs = ((PyObject *)Py_None);
  PyObject *__pyx_v_exclude = ((PyObject *)Py_None);
  PyObject *__pyx_r = NULL;
  if (__pyx_optional_args) {
    if (__pyx_optional_args->__pyx_n > 0) {
      __pyx_v_attrs = __pyx_optional_args->attrs;
      if (__pyx_optional_args->__pyx_n > 1) {
        __pyx_v_exclude = __pyx_optional_args->exclude;
      }
    }
  }
  /* Check if called by wrapper */
  if (unlikely(__pyx_skip_dispatch)) ;
  /* Check if overridden in Python */
  else if (
  #if !CYTHON_USE_TYPE_SLOTS
  unlikely(Py_TYPE(((PyObject *)__pyx_v_self)) != __pyx_mstate_global->__pyx_ptype_6Cython_8Compiler_7Visitor_TreeVisitor &&
  __Pyx_PyType_HasFeature(Py_TYPE(((PyObject *)__pyx_v_self)), Py_TPFLAGS_HAVE_GC))
  #else
  unlikely(Py_TYPE(((PyObject *)__pyx_v_self))->tp_dictoffset != 0 || __Pyx_PyType_HasFeature(Py_TYPE(((PyObject *)__pyx_v_self)), (Py_TPFLAGS_IS_ABSTRACT | Py_TPFLAGS_HEAPTYPE)))
  #endif
  ) {
    #if CYTHON_USE_DICT_VERSIONS && CYTHON_USE_PYTYPE_LOOKUP && CYTHON_USE_TYPE_SLOTS
    static PY_UINT64_T __pyx_tp_dict_version = __PYX_DICT_VERSION_INIT, __pyx_obj_dict_version = __PYX_DICT_VERSION_INIT;
    if (unlikely(!__Pyx_object_dict_version_matches(((PyObject *)__pyx_v_self), __pyx_tp_dict_version, __pyx_obj_dict_version))) {
      PY_UINT64_T __pyx_typedict_guard = __Pyx_get_tp_dict_version(((PyObject *)__pyx_v_self));
      #endif
      __pyx_t_1 = __Pyx_PyObject_GetAttrStr(((PyObject *)__pyx_v_self), __pyx_mstate_global->__pyx_n_u_visitchildren); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 196, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_1);
      if (!__Pyx_IsSameCFunction(__pyx_t_1, (void(*)(void)) __pyx_pw_6Cython_8Compiler_7Visitor_11TreeVisitor_9visitchildren)) {
        __Pyx_XDECREF(__pyx_r);
        __pyx_t_3 = NULL;
        __Pyx_INCREF(__pyx_t_1);
        __pyx_t_4 = __pyx_t_1; 
        __pyx_t_5 = 1;
        #if CYTHON_UNPACK_METHODS
        if (unlikely(PyMethod_Check(__pyx_t_4))) {
          __pyx_t_3 = PyMethod_GET_SELF(__pyx_t_4);
          assert(__pyx_t_3);
          PyObject* __pyx__function = PyMethod_GET_FUNCTION(__pyx_t_4);
          __Pyx_INCREF(__pyx_t_3);
          __Pyx_INCREF(__pyx__function);
          __Pyx_DECREF_SET(__pyx_t_4, __pyx__function);
          __pyx_t_5 = 0;
        }
        #endif
        {
          PyObject *__pyx_callargs[4] = {__pyx_t_3, __pyx_v_parent, __pyx_v_attrs, __pyx_v_exclude};
          __pyx_t_2 = __Pyx_PyObject_FastCall((PyObject*)__pyx_t_4, __pyx_callargs+__pyx_t_5, (4-__pyx_t_5) | (__pyx_t_5*__Pyx_PY_VECTORCALL_ARGUMENTS_OFFSET));
          __Pyx_XDECREF(__pyx_t_3); __pyx_t_3 = 0;
          __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
          if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 196, __pyx_L1_error)
          __Pyx_GOTREF(__pyx_t_2);
        }
        __pyx_r = __pyx_t_2;
        __pyx_t_2 = 0;
        __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
        goto __pyx_L0;
      }
      #if CYTHON_USE_DICT_VERSIONS && CYTHON_USE_PYTYPE_LOOKUP && CYTHON_USE_TYPE_SLOTS
      __pyx_tp_dict_version = __Pyx_get_tp_dict_version(((PyObject *)__pyx_v_self));
      __pyx_obj_dict_version = __Pyx_get_object_dict_version(((PyObject *)__pyx_v_self));
      if (unlikely(__pyx_typedict_guard != __pyx_tp_dict_version)) {
        __pyx_tp_dict_version = __pyx_obj_dict_version = __PYX_DICT_VERSION_INIT;
      }
      #endif
      __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
      #if CYTHON_USE_DICT_VERSIONS && CYTHON_USE_PYTYPE_LOOKUP && CYTHON_USE_TYPE_SLOTS
    }
    #endif
  }
/* … */
  /* function exit code */
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_t_1);
  __Pyx_XDECREF(__pyx_t_2);
  __Pyx_XDECREF(__pyx_t_3);
  __Pyx_XDECREF(__pyx_t_4);
  __Pyx_AddTraceback("Cython.Compiler.Visitor.TreeVisitor.visitchildren", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_r = 0;
  __pyx_L0:;
  __Pyx_XGIVEREF(__pyx_r);
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}

/* Python wrapper */
static PyObject *__pyx_pw_6Cython_8Compiler_7Visitor_11TreeVisitor_9visitchildren(PyObject *__pyx_v_self, 
#if CYTHON_METH_FASTCALL
PyObject *const *__pyx_args, Py_ssize_t __pyx_nargs, PyObject *__pyx_kwds
#else
PyObject *__pyx_args, PyObject *__pyx_kwds
#endif
); /*proto*/
PyDoc_STRVAR(__pyx_doc_6Cython_8Compiler_7Visitor_11TreeVisitor_8visitchildren, "File: Cython/Compiler/Visitor.py (starting at line 196)");
static PyMethodDef __pyx_mdef_6Cython_8Compiler_7Visitor_11TreeVisitor_9visitchildren = {"visitchildren", (PyCFunction)(void(*)(void))(__Pyx_PyCFunction_FastCallWithKeywords)__pyx_pw_6Cython_8Compiler_7Visitor_11TreeVisitor_9visitchildren, __Pyx_METH_FASTCALL|METH_KEYWORDS, __pyx_doc_6Cython_8Compiler_7Visitor_11TreeVisitor_8visitchildren};
static PyObject *__pyx_pw_6Cython_8Compiler_7Visitor_11TreeVisitor_9visitchildren(PyObject *__pyx_v_self, 
#if CYTHON_METH_FASTCALL
PyObject *const *__pyx_args, Py_ssize_t __pyx_nargs, PyObject *__pyx_kwds
#else
PyObject *__pyx_args, PyObject *__pyx_kwds
#endif
) {
  PyObject *__pyx_v_parent = 0;
  PyObject *__pyx_v_attrs = 0;
  PyObject *__pyx_v_exclude = 0;
  #if !CYTHON_METH_FASTCALL
  CYTHON_UNUSED Py_ssize_t __pyx_nargs;
  #endif
  CYTHON_UNUSED PyObject *const *__pyx_kwvalues;
  PyObject *__pyx_r = 0;
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("visitchildren (wrapper)", 0);
  #if !CYTHON_METH_FASTCALL
  #if CYTHON_ASSUME_SAFE_SIZE
  __pyx_nargs = PyTuple_GET_SIZE(__pyx_args);
  #else
  __pyx_nargs = PyTuple_Size(__pyx_args); if (unlikely(__pyx_nargs < 0)) return NULL;
  #endif
  #endif
  __pyx_kwvalues = __Pyx_KwValues_FASTCALL(__pyx_args, __pyx_nargs);
  {
    PyObject ** const __pyx_pyargnames[] = {&__pyx_mstate_global->__pyx_n_u_parent,&__pyx_mstate_global->__pyx_n_u_attrs,&__pyx_mstate_global->__pyx_n_u_exclude,0};
  PyObject* values[3] = {0,0,0};
    const Py_ssize_t __pyx_kwds_len = (__pyx_kwds) ? __Pyx_NumKwargs_FASTCALL(__pyx_kwds) : 0;
    if (unlikely(__pyx_kwds_len) < 0) __PYX_ERR(0, 196, __pyx_L3_error)
    if (__pyx_kwds_len > 0) {
      switch (__pyx_nargs) {
        case  3:
        values[2] = __Pyx_ArgRef_FASTCALL(__pyx_args, 2);
        if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[2])) __PYX_ERR(0, 196, __pyx_L3_error)
        CYTHON_FALLTHROUGH;
        case  2:
        values[1] = __Pyx_ArgRef_FASTCALL(__pyx_args, 1);
        if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[1])) __PYX_ERR(0, 196, __pyx_L3_error)
        CYTHON_FALLTHROUGH;
        case  1:
        values[0] = __Pyx_ArgRef_FASTCALL(__pyx_args, 0);
        if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[0])) __PYX_ERR(0, 196, __pyx_L3_error)
        CYTHON_FALLTHROUGH;
        case  0: break;
        default: goto __pyx_L5_argtuple_error;
      }
      const Py_ssize_t kwd_pos_args = __pyx_nargs;
      if (__Pyx_ParseKeywords(__pyx_kwds, __pyx_kwvalues, __pyx_pyargnames, 0, values, kwd_pos_args, __pyx_kwds_len, "visitchildren", 0) < (0)) __PYX_ERR(0, 196, __pyx_L3_error)
      if (!values[1]) values[1] = __Pyx_NewRef(((PyObject *)Py_None));
      if (!values[2]) values[2] = __Pyx_NewRef(((PyObject *)Py_None));
      for (Py_ssize_t i = __pyx_nargs; i < 1; i++) {
        if (unlikely(!values[i])) { __Pyx_RaiseArgtupleInvalid("visitchildren", 0, 1, 3, i); __PYX_ERR(0, 196, __pyx_L3_error) }
      }
    } else {
      switch (__pyx_nargs) {
        case  3:
        values[2] = __Pyx_ArgRef_FASTCALL(__pyx_args, 2);
        if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[2])) __PYX_ERR(0, 196, __pyx_L3_error)
        CYTHON_FALLTHROUGH;
        case  2:
        values[1] = __Pyx_ArgRef_FASTCALL(__pyx_args, 1);
        if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[1])) __PYX_ERR(0, 196, __pyx_L3_error)
        CYTHON_FALLTHROUGH;
        case  1:
        values[0] = __Pyx_ArgRef_FASTCALL(__pyx_args, 0);
        if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[0])) __PYX_ERR(0, 196, __pyx_L3_error)
        break;
        default: goto __pyx_L5_argtuple_error;
      }
      if (!values[1]) values[1] = __Pyx_NewRef(((PyObject *)Py_None));
      if (!values[2]) values[2] = __Pyx_NewRef(((PyObject *)Py_None));
    }
    __pyx_v_parent = values[0];
    __pyx_v_attrs = values[1];
    __pyx_v_exclude = values[2];
  }
  goto __pyx_L6_skip;
  __pyx_L5_argtuple_error:;
  __Pyx_RaiseArgtupleInvalid("visitchildren", 0, 1, 3, __pyx_nargs); __PYX_ERR(0, 196, __pyx_L3_error)
  __pyx_L6_skip:;
  goto __pyx_L4_argument_unpacking_done;
  __pyx_L3_error:;
  for (Py_ssize_t __pyx_temp=0; __pyx_temp < (Py_ssize_t)(sizeof(values)/sizeof(values[0])); ++__pyx_temp) {
    Py_XDECREF(values[__pyx_temp]);
  }
  __Pyx_AddTraceback("Cython.Compiler.Visitor.TreeVisitor.visitchildren", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __Pyx_RefNannyFinishContext();
  return NULL;
  __pyx_L4_argument_unpacking_done:;
  __pyx_r = __pyx_pf_6Cython_8Compiler_7Visitor_11TreeVisitor_8visitchildren(((struct __pyx_obj_6Cython_8Compiler_7Visitor_TreeVisitor *)__pyx_v_self), __pyx_v_parent, __pyx_v_attrs, __pyx_v_exclude);

  /* function exit code */
  for (Py_ssize_t __pyx_temp=0; __pyx_temp < (Py_ssize_t)(sizeof(values)/sizeof(values[0])); ++__pyx_temp) {
    Py_XDECREF(values[__pyx_temp]);
  }
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}

static PyObject *__pyx_pf_6Cython_8Compiler_7Visitor_11TreeVisitor_8visitchildren(struct __pyx_obj_6Cython_8Compiler_7Visitor_TreeVisitor *__pyx_v_self, PyObject *__pyx_v_parent, PyObject *__pyx_v_attrs, PyObject *__pyx_v_exclude) {
  PyObject *__pyx_r = NULL;
  __Pyx_XDECREF(__pyx_r);
  __pyx_t_2.__pyx_n = 2;
  __pyx_t_2.attrs = __pyx_v_attrs;
  __pyx_t_2.exclude = __pyx_v_exclude;
  __pyx_t_1 = __pyx_vtabptr_6Cython_8Compiler_7Visitor_TreeVisitor->visitchildren(__pyx_v_self, __pyx_v_parent, 1, &__pyx_t_2); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 196, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __pyx_r = __pyx_t_1;
  __pyx_t_1 = 0;
  goto __pyx_L0;

  /* function exit code */
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_t_1);
  __Pyx_AddTraceback("Cython.Compiler.Visitor.TreeVisitor.visitchildren", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_r = NULL;
  __pyx_L0:;
  __Pyx_XGIVEREF(__pyx_r);
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}
/* … */
  __pyx_t_2 = __Pyx_CyFunction_New(&__pyx_mdef_6Cython_8Compiler_7Visitor_11TreeVisitor_9visitchildren, __Pyx_CYFUNCTION_CCLASS, __pyx_mstate_global->__pyx_n_u_TreeVisitor_visitchildren, NULL, __pyx_mstate_global->__pyx_n_u_Cython_Compiler_Visitor, __pyx_mstate_global->__pyx_d, ((PyObject *)__pyx_mstate_global->__pyx_codeobj_tab[3])); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 196, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  #if CYTHON_COMPILING_IN_CPYTHON && PY_VERSION_HEX >= 0x030E0000
  PyUnstable_Object_EnableDeferredRefcount(__pyx_t_2);
  #endif
  __Pyx_CyFunction_SetDefaultsTuple(__pyx_t_2, __pyx_mstate_global->__pyx_tuple[7]);
  if (__Pyx_SetItemOnTypeDict(__pyx_mstate_global->__pyx_ptype_6Cython_8Compiler_7Visitor_TreeVisitor, __pyx_mstate_global->__pyx_n_u_visitchildren, __pyx_t_2) < (0)) __PYX_ERR(0, 196, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
/* … */
  __pyx_mstate_global->__pyx_tuple[7] = PyTuple_Pack(2, Py_None, Py_None); if (unlikely(!__pyx_mstate_global->__pyx_tuple[7])) __PYX_ERR(0, 196, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_mstate_global->__pyx_tuple[7]);
  __Pyx_GIVEREF(__pyx_mstate_global->__pyx_tuple[7]);
```

</details>

L197  ⚪  (score=0)
```python
        # generic def entry point for calls from Python subclasses
```
L198  🟡  (score=1)
```python
        return self._visitchildren(parent, attrs, exclude)
```
<details><summary>Show generated C (score=1)</summary>

```c
  __Pyx_XDECREF(__pyx_r);
  __pyx_t_1 = __pyx_f_6Cython_8Compiler_7Visitor_11TreeVisitor__visitchildren(__pyx_v_self, __pyx_v_parent, __pyx_v_attrs, __pyx_v_exclude); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 198, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __pyx_r = __pyx_t_1;
  __pyx_t_1 = 0;
  goto __pyx_L0;
```

</details>

L199  ⚪  (score=0)
```python
```
L200  🔴  (score=12)
```python
    @cython.final
```
<details><summary>Show generated C (score=12)</summary>

```c
static PyObject *__pyx_f_6Cython_8Compiler_7Visitor_11TreeVisitor__visitchildren(struct __pyx_obj_6Cython_8Compiler_7Visitor_TreeVisitor *__pyx_v_self, PyObject *__pyx_v_parent, PyObject *__pyx_v_attrs, PyObject *__pyx_v_exclude) {
  PyObject *__pyx_v_result = NULL;
  PyObject *__pyx_v_attr = NULL;
  PyObject *__pyx_v_child = NULL;
  PyObject *__pyx_v_childretval = NULL;
  Py_ssize_t __pyx_7genexpr__pyx_v_idx;
  PyObject *__pyx_7genexpr__pyx_v_x = NULL;
  PyObject *__pyx_r = NULL;
/* … */
  /* function exit code */
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_t_2);
  __Pyx_XDECREF(__pyx_t_3);
  __Pyx_XDECREF(__pyx_t_8);
  __Pyx_XDECREF(__pyx_t_11);
  __Pyx_XDECREF(__pyx_t_12);
  __Pyx_AddTraceback("Cython.Compiler.Visitor.TreeVisitor._visitchildren", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_r = 0;
  __pyx_L0:;
  __Pyx_XDECREF(__pyx_v_result);
  __Pyx_XDECREF(__pyx_v_attr);
  __Pyx_XDECREF(__pyx_v_child);
  __Pyx_XDECREF(__pyx_v_childretval);
  __Pyx_XDECREF(__pyx_7genexpr__pyx_v_x);
  __Pyx_XGIVEREF(__pyx_r);
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}
```

</details>

L201  ⚪  (score=0)
```python
    def _visitchildren(self, parent, attrs, exclude):
```
L202  ⚪  (score=0)
```python
        # fast cdef entry point for calls from Cython subclasses
```
L203  ⚪  (score=0)
```python
        """
```
L204  ⚪  (score=0)
```python
        Visits the children of the given parent. If parent is None, returns
```
L205  ⚪  (score=0)
```python
        immediately (returning None).
```
L206  ⚪  (score=0)
```python
```
L207  ⚪  (score=0)
```python
        The return value is a dictionary giving the results for each
```
L208  ⚪  (score=0)
```python
        child (mapping the attribute name to either the return value
```
L209  ⚪  (score=0)
```python
        or a list of return values (in the case of multiple children
```
L210  ⚪  (score=0)
```python
        in an attribute)).
```
L211  ⚪  (score=0)
```python
        """
```
L212  ⚪  (score=0)
```python
        idx: cython.Py_ssize_t
```
L213  ⚪  (score=0)
```python
```
L214  ⚪  (score=0)
```python
        if parent is None: 
```
<details><summary>Show generated C (score=0)</summary>

```c
  __pyx_t_1 = (__pyx_v_parent == Py_None);
  if (__pyx_t_1) {
/* … */
  }
```

</details>

L215  🟡  (score=2)
```python
            return None
```
<details><summary>Show generated C (score=2)</summary>

```c
    __Pyx_XDECREF(__pyx_r);
    __pyx_r = ((PyObject*)Py_None); __Pyx_INCREF(Py_None);
    goto __pyx_L0;
```

</details>

L216  🟡  (score=2)
```python
        result = {}
```
<details><summary>Show generated C (score=2)</summary>

```c
  __pyx_t_2 = __Pyx_PyDict_NewPresized(0); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 216, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __pyx_v_result = ((PyObject*)__pyx_t_2);
  __pyx_t_2 = 0;
```

</details>

L217  🔴  (score=51)
```python
        for attr in parent.child_attrs:
```
<details><summary>Show generated C (score=51)</summary>

```c
  __pyx_t_2 = __Pyx_PyObject_GetAttrStr(__pyx_v_parent, __pyx_mstate_global->__pyx_n_u_child_attrs); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 217, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  if (likely(PyList_CheckExact(__pyx_t_2)) || PyTuple_CheckExact(__pyx_t_2)) {
    __pyx_t_3 = __pyx_t_2; __Pyx_INCREF(__pyx_t_3);
    __pyx_t_4 = 0;
    __pyx_t_5 = NULL;
  } else {
    __pyx_t_4 = -1; __pyx_t_3 = PyObject_GetIter(__pyx_t_2); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 217, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_3);
    __pyx_t_5 = (CYTHON_COMPILING_IN_LIMITED_API) ? PyIter_Next : __Pyx_PyObject_GetIterNextFunc(__pyx_t_3); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 217, __pyx_L1_error)
  }
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  for (;;) {
    if (likely(!__pyx_t_5)) {
      if (likely(PyList_CheckExact(__pyx_t_3))) {
        {
          Py_ssize_t __pyx_temp = __Pyx_PyList_GET_SIZE(__pyx_t_3);
          #if !CYTHON_ASSUME_SAFE_SIZE
          if (unlikely((__pyx_temp < 0))) __PYX_ERR(0, 217, __pyx_L1_error)
          #endif
          if (__pyx_t_4 >= __pyx_temp) break;
        }
        __pyx_t_2 = __Pyx_PyList_GetItemRefFast(__pyx_t_3, __pyx_t_4, __Pyx_ReferenceSharing_OwnStrongReference);
        ++__pyx_t_4;
      } else {
        {
          Py_ssize_t __pyx_temp = __Pyx_PyTuple_GET_SIZE(__pyx_t_3);
          #if !CYTHON_ASSUME_SAFE_SIZE
          if (unlikely((__pyx_temp < 0))) __PYX_ERR(0, 217, __pyx_L1_error)
          #endif
          if (__pyx_t_4 >= __pyx_temp) break;
        }
        #if CYTHON_ASSUME_SAFE_MACROS && !CYTHON_AVOID_BORROWED_REFS
        __pyx_t_2 = __Pyx_NewRef(PyTuple_GET_ITEM(__pyx_t_3, __pyx_t_4));
        #else
        __pyx_t_2 = __Pyx_PySequence_ITEM(__pyx_t_3, __pyx_t_4);
        #endif
        ++__pyx_t_4;
      }
      if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 217, __pyx_L1_error)
    } else {
      __pyx_t_2 = __pyx_t_5(__pyx_t_3);
      if (unlikely(!__pyx_t_2)) {
        PyObject* exc_type = PyErr_Occurred();
        if (exc_type) {
          if (unlikely(!__Pyx_PyErr_GivenExceptionMatches(exc_type, PyExc_StopIteration))) __PYX_ERR(0, 217, __pyx_L1_error)
          PyErr_Clear();
        }
        break;
      }
    }
    __Pyx_GOTREF(__pyx_t_2);
    __Pyx_XDECREF_SET(__pyx_v_attr, __pyx_t_2);
    __pyx_t_2 = 0;
/* … */
    __pyx_L4_continue:;
  }
  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
```

</details>

L218  🟡  (score=2)
```python
            if attrs is not None and attr not in attrs: continue
```
<details><summary>Show generated C (score=2)</summary>

```c
    __pyx_t_6 = (__pyx_v_attrs != Py_None);
    if (__pyx_t_6) {
    } else {
      __pyx_t_1 = __pyx_t_6;
      goto __pyx_L7_bool_binop_done;
    }
    __pyx_t_6 = (__Pyx_PySequence_ContainsTF(__pyx_v_attr, __pyx_v_attrs, Py_NE)); if (unlikely((__pyx_t_6 < 0))) __PYX_ERR(0, 218, __pyx_L1_error)
    __pyx_t_1 = __pyx_t_6;
    __pyx_L7_bool_binop_done:;
    if (__pyx_t_1) {
      goto __pyx_L4_continue;
    }
```

</details>

L219  🟡  (score=2)
```python
            if exclude is not None and attr in exclude: continue
```
<details><summary>Show generated C (score=2)</summary>

```c
    __pyx_t_6 = (__pyx_v_exclude != Py_None);
    if (__pyx_t_6) {
    } else {
      __pyx_t_1 = __pyx_t_6;
      goto __pyx_L10_bool_binop_done;
    }
    __pyx_t_6 = (__Pyx_PySequence_ContainsTF(__pyx_v_attr, __pyx_v_exclude, Py_EQ)); if (unlikely((__pyx_t_6 < 0))) __PYX_ERR(0, 219, __pyx_L1_error)
    __pyx_t_1 = __pyx_t_6;
    __pyx_L10_bool_binop_done:;
    if (__pyx_t_1) {
      goto __pyx_L4_continue;
    }
```

</details>

L220  🟡  (score=3)
```python
            child = getattr(parent, attr)
```
<details><summary>Show generated C (score=3)</summary>

```c
    __pyx_t_2 = __Pyx_GetAttr(__pyx_v_parent, __pyx_v_attr); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 220, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_2);
    __Pyx_XDECREF_SET(__pyx_v_child, __pyx_t_2);
    __pyx_t_2 = 0;
```

</details>

L221  ⚪  (score=0)
```python
            if child is not None:
```
<details><summary>Show generated C (score=0)</summary>

```c
    __pyx_t_1 = (__pyx_v_child != Py_None);
    if (__pyx_t_1) {
/* … */
    }
```

</details>

L222  ⚪  (score=0)
```python
                if type(child) is list:
```
<details><summary>Show generated C (score=0)</summary>

```c
      __pyx_t_1 = (((PyObject *)Py_TYPE(__pyx_v_child)) == ((PyObject *)(&PyList_Type)));
      if (__pyx_t_1) {
/* … */
        goto __pyx_L13;
      }
```

</details>

L223  🔴  (score=65)
```python
                    childretval = [self._visitchild(x, parent, attr, idx) for idx, x in enumerate(child)]
```
<details><summary>Show generated C (score=65)</summary>

```c
        { /* enter inner scope */
          __pyx_t_2 = PyList_New(0); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 223, __pyx_L16_error)
          __Pyx_GOTREF(__pyx_t_2);
          __pyx_t_7 = 0;
          if (likely(PyList_CheckExact(__pyx_v_child)) || PyTuple_CheckExact(__pyx_v_child)) {
            __pyx_t_8 = __pyx_v_child; __Pyx_INCREF(__pyx_t_8);
            __pyx_t_9 = 0;
            __pyx_t_10 = NULL;
          } else {
            __pyx_t_9 = -1; __pyx_t_8 = PyObject_GetIter(__pyx_v_child); if (unlikely(!__pyx_t_8)) __PYX_ERR(0, 223, __pyx_L16_error)
            __Pyx_GOTREF(__pyx_t_8);
            __pyx_t_10 = (CYTHON_COMPILING_IN_LIMITED_API) ? PyIter_Next : __Pyx_PyObject_GetIterNextFunc(__pyx_t_8); if (unlikely(!__pyx_t_10)) __PYX_ERR(0, 223, __pyx_L16_error)
          }
          for (;;) {
            if (likely(!__pyx_t_10)) {
              if (likely(PyList_CheckExact(__pyx_t_8))) {
                {
                  Py_ssize_t __pyx_temp = __Pyx_PyList_GET_SIZE(__pyx_t_8);
                  #if !CYTHON_ASSUME_SAFE_SIZE
                  if (unlikely((__pyx_temp < 0))) __PYX_ERR(0, 223, __pyx_L16_error)
                  #endif
                  if (__pyx_t_9 >= __pyx_temp) break;
                }
                __pyx_t_11 = __Pyx_PyList_GetItemRefFast(__pyx_t_8, __pyx_t_9, __Pyx_ReferenceSharing_OwnStrongReference);
                ++__pyx_t_9;
              } else {
                {
                  Py_ssize_t __pyx_temp = __Pyx_PyTuple_GET_SIZE(__pyx_t_8);
                  #if !CYTHON_ASSUME_SAFE_SIZE
                  if (unlikely((__pyx_temp < 0))) __PYX_ERR(0, 223, __pyx_L16_error)
                  #endif
                  if (__pyx_t_9 >= __pyx_temp) break;
                }
                #if CYTHON_ASSUME_SAFE_MACROS && !CYTHON_AVOID_BORROWED_REFS
                __pyx_t_11 = __Pyx_NewRef(PyTuple_GET_ITEM(__pyx_t_8, __pyx_t_9));
                #else
                __pyx_t_11 = __Pyx_PySequence_ITEM(__pyx_t_8, __pyx_t_9);
                #endif
                ++__pyx_t_9;
              }
              if (unlikely(!__pyx_t_11)) __PYX_ERR(0, 223, __pyx_L16_error)
            } else {
              __pyx_t_11 = __pyx_t_10(__pyx_t_8);
              if (unlikely(!__pyx_t_11)) {
                PyObject* exc_type = PyErr_Occurred();
                if (exc_type) {
                  if (unlikely(!__Pyx_PyErr_GivenExceptionMatches(exc_type, PyExc_StopIteration))) __PYX_ERR(0, 223, __pyx_L16_error)
                  PyErr_Clear();
                }
                break;
              }
            }
            __Pyx_GOTREF(__pyx_t_11);
            __Pyx_XDECREF_SET(__pyx_7genexpr__pyx_v_x, __pyx_t_11);
            __pyx_t_11 = 0;
            __pyx_7genexpr__pyx_v_idx = __pyx_t_7;
            __pyx_t_7 = (__pyx_t_7 + 1);
            __pyx_t_11 = PyLong_FromSsize_t(__pyx_7genexpr__pyx_v_idx); if (unlikely(!__pyx_t_11)) __PYX_ERR(0, 223, __pyx_L16_error)
            __Pyx_GOTREF(__pyx_t_11);
            __pyx_t_12 = __pyx_f_6Cython_8Compiler_7Visitor_11TreeVisitor__visitchild(__pyx_v_self, __pyx_7genexpr__pyx_v_x, __pyx_v_parent, __pyx_v_attr, __pyx_t_11); if (unlikely(!__pyx_t_12)) __PYX_ERR(0, 223, __pyx_L16_error)
            __Pyx_GOTREF(__pyx_t_12);
            __Pyx_DECREF(__pyx_t_11); __pyx_t_11 = 0;
            if (unlikely(__Pyx_ListComp_Append(__pyx_t_2, (PyObject*)__pyx_t_12))) __PYX_ERR(0, 223, __pyx_L16_error)
            __Pyx_DECREF(__pyx_t_12); __pyx_t_12 = 0;
          }
          __Pyx_DECREF(__pyx_t_8); __pyx_t_8 = 0;
          __Pyx_XDECREF(__pyx_7genexpr__pyx_v_x); __pyx_7genexpr__pyx_v_x = 0;
          goto __pyx_L20_exit_scope;
          __pyx_L16_error:;
          __Pyx_XDECREF(__pyx_7genexpr__pyx_v_x); __pyx_7genexpr__pyx_v_x = 0;
          goto __pyx_L1_error;
          __pyx_L20_exit_scope:;
        } /* exit inner scope */
        __Pyx_XDECREF_SET(__pyx_v_childretval, __pyx_t_2);
        __pyx_t_2 = 0;
```

</details>

L224  ⚪  (score=0)
```python
                else:
```
L225  🟡  (score=1)
```python
                    childretval = self._visitchild(child, parent, attr, None)
```
<details><summary>Show generated C (score=1)</summary>

```c
      /*else*/ {
        __pyx_t_2 = __pyx_f_6Cython_8Compiler_7Visitor_11TreeVisitor__visitchild(__pyx_v_self, __pyx_v_child, __pyx_v_parent, __pyx_v_attr, Py_None); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 225, __pyx_L1_error)
        __Pyx_GOTREF(__pyx_t_2);
        __Pyx_XDECREF_SET(__pyx_v_childretval, __pyx_t_2);
        __pyx_t_2 = 0;
```

</details>

L226  🔴  (score=34)
```python
                    assert not isinstance(childretval, list), 'Cannot insert list here: %s in %r' % (attr, parent)
```
<details><summary>Show generated C (score=34)</summary>

```c
        #ifndef CYTHON_WITHOUT_ASSERTIONS
        if (unlikely(__pyx_assertions_enabled())) {
          __pyx_t_1 = PyList_Check(__pyx_v_childretval); 
          __pyx_t_6 = (!__pyx_t_1);
          if (unlikely(!__pyx_t_6)) {
            __pyx_t_2 = __Pyx_PyObject_FormatSimpleAndDecref(PyObject_Str(__pyx_v_attr), __pyx_mstate_global->__pyx_empty_unicode); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 226, __pyx_L1_error)
            __Pyx_GOTREF(__pyx_t_2);
            __pyx_t_8 = __Pyx_PyObject_FormatSimpleAndDecref(PyObject_Repr(__pyx_v_parent), __pyx_mstate_global->__pyx_empty_unicode); if (unlikely(!__pyx_t_8)) __PYX_ERR(0, 226, __pyx_L1_error)
            __Pyx_GOTREF(__pyx_t_8);
            __pyx_t_13[0] = __pyx_mstate_global->__pyx_kp_u_Cannot_insert_list_here;
            __pyx_t_13[1] = __pyx_t_2;
            __pyx_t_13[2] = __pyx_mstate_global->__pyx_kp_u_in_2;
            __pyx_t_13[3] = __pyx_t_8;
            __pyx_t_12 = __Pyx_PyUnicode_Join(__pyx_t_13, 4, 25 + __Pyx_PyUnicode_GET_LENGTH(__pyx_t_2) + 4 + __Pyx_PyUnicode_GET_LENGTH(__pyx_t_8), 127 | __Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_2) | __Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_8));
            if (unlikely(!__pyx_t_12)) __PYX_ERR(0, 226, __pyx_L1_error)
            __Pyx_GOTREF(__pyx_t_12);
            __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
            __Pyx_DECREF(__pyx_t_8); __pyx_t_8 = 0;
            __Pyx_Raise(((PyObject *)(((PyTypeObject*)PyExc_AssertionError))), __pyx_t_12, 0, 0);
            __Pyx_DECREF(__pyx_t_12); __pyx_t_12 = 0;
            __PYX_ERR(0, 226, __pyx_L1_error)
          }
        }
        #else
        if ((1)); else __PYX_ERR(0, 226, __pyx_L1_error)
        #endif
      }
      __pyx_L13:;
```

</details>

L227  🟠  (score=5)
```python
                result[attr] = childretval
```
<details><summary>Show generated C (score=5)</summary>

```c
      if (unlikely((PyDict_SetItem(__pyx_v_result, __pyx_v_attr, __pyx_v_childretval) < 0))) __PYX_ERR(0, 227, __pyx_L1_error)
```

</details>

L228  🟡  (score=2)
```python
        return result
```
<details><summary>Show generated C (score=2)</summary>

```c
  __Pyx_XDECREF(__pyx_r);
  __Pyx_INCREF(__pyx_v_result);
  __pyx_r = __pyx_v_result;
  goto __pyx_L0;
```

</details>

L229  ⚪  (score=0)
```python
```
L230  ⚪  (score=0)
```python
```
L231  ⚪  (score=0)
```python
class VisitorTransform(TreeVisitor):
```
<details><summary>Show generated C (score=0)</summary>

```c
struct __pyx_vtabstruct_6Cython_8Compiler_7Visitor_VisitorTransform {
  struct __pyx_vtabstruct_6Cython_8Compiler_7Visitor_TreeVisitor __pyx_base;
  PyObject *(*_process_children)(struct __pyx_obj_6Cython_8Compiler_7Visitor_VisitorTransform *, PyObject *, struct __pyx_opt_args_6Cython_8Compiler_7Visitor_16VisitorTransform__process_children *__pyx_optional_args);
  PyObject *(*_flatten_list)(struct __pyx_obj_6Cython_8Compiler_7Visitor_VisitorTransform *, PyObject *);
  PyObject *(*visitchild)(struct __pyx_obj_6Cython_8Compiler_7Visitor_VisitorTransform *, PyObject *, PyObject *, int __pyx_skip_dispatch, struct __pyx_opt_args_6Cython_8Compiler_7Visitor_16VisitorTransform_visitchild *__pyx_optional_args);
};
static struct __pyx_vtabstruct_6Cython_8Compiler_7Visitor_VisitorTransform *__pyx_vtabptr_6Cython_8Compiler_7Visitor_VisitorTransform;
static PyObject *__pyx_f_6Cython_8Compiler_7Visitor_16VisitorTransform__process_children(struct __pyx_obj_6Cython_8Compiler_7Visitor_VisitorTransform *, PyObject *, struct __pyx_opt_args_6Cython_8Compiler_7Visitor_16VisitorTransform__process_children *__pyx_optional_args);
static PyObject *__pyx_f_6Cython_8Compiler_7Visitor_16VisitorTransform__flatten_list(struct __pyx_obj_6Cython_8Compiler_7Visitor_VisitorTransform *, PyObject *);

```

</details>

L232  ⚪  (score=0)
```python
    """
```
L233  ⚪  (score=0)
```python
    A tree transform is a base class for visitors that wants to do stream
```
L234  ⚪  (score=0)
```python
    processing of the structure (rather than attributes etc.) of a tree.
```
L235  ⚪  (score=0)
```python
```
L236  ⚪  (score=0)
```python
    It implements __call__ to simply visit the argument node.
```
L237  ⚪  (score=0)
```python
```
L238  ⚪  (score=0)
```python
    It requires the visitor methods to return the nodes which should take
```
L239  ⚪  (score=0)
```python
    the place of the visited node in the result tree (which can be the same
```
L240  ⚪  (score=0)
```python
    or one or more replacement). Specifically, if the return value from
```
L241  ⚪  (score=0)
```python
    a visitor method is:
```
L242  ⚪  (score=0)
```python
```
L243  ⚪  (score=0)
```python
    - [] or None; the visited node will be removed (set to None if an attribute and
```
L244  ⚪  (score=0)
```python
    removed if in a list)
```
L245  ⚪  (score=0)
```python
    - A single node; the visited node will be replaced by the returned node.
```
L246  ⚪  (score=0)
```python
    - A list of nodes; the visited nodes will be replaced by all the nodes in the
```
L247  ⚪  (score=0)
```python
    list. This will only work if the node was already a member of a list; if it
```
L248  ⚪  (score=0)
```python
    was not, an exception will be raised. (Typically you want to ensure that you
```
L249  ⚪  (score=0)
```python
    are within a StatListNode or similar before doing this.)
```
L250  ⚪  (score=0)
```python
    """
```
L251  🔴  (score=87)
```python
    def visitchildren(self, parent, attrs=None, exclude=None):
```
<details><summary>Show generated C (score=87)</summary>

```c
static PyObject *__pyx_pw_6Cython_8Compiler_7Visitor_16VisitorTransform_1visitchildren(PyObject *__pyx_v_self, 
#if CYTHON_METH_FASTCALL
PyObject *const *__pyx_args, Py_ssize_t __pyx_nargs, PyObject *__pyx_kwds
#else
PyObject *__pyx_args, PyObject *__pyx_kwds
#endif
); /*proto*/
static PyObject *__pyx_f_6Cython_8Compiler_7Visitor_16VisitorTransform_visitchildren(struct __pyx_obj_6Cython_8Compiler_7Visitor_VisitorTransform *__pyx_v_self, PyObject *__pyx_v_parent, int __pyx_skip_dispatch, struct __pyx_opt_args_6Cython_8Compiler_7Visitor_16VisitorTransform_visitchildren *__pyx_optional_args) {
  PyObject *__pyx_v_attrs = ((PyObject *)Py_None);
  PyObject *__pyx_v_exclude = ((PyObject *)Py_None);
  PyObject *__pyx_r = NULL;
  if (__pyx_optional_args) {
    if (__pyx_optional_args->__pyx_n > 0) {
      __pyx_v_attrs = __pyx_optional_args->attrs;
      if (__pyx_optional_args->__pyx_n > 1) {
        __pyx_v_exclude = __pyx_optional_args->exclude;
      }
    }
  }
  /* Check if called by wrapper */
  if (unlikely(__pyx_skip_dispatch)) ;
  /* Check if overridden in Python */
  else if (
  #if !CYTHON_USE_TYPE_SLOTS
  unlikely(Py_TYPE(((PyObject *)__pyx_v_self)) != __pyx_mstate_global->__pyx_ptype_6Cython_8Compiler_7Visitor_VisitorTransform &&
  __Pyx_PyType_HasFeature(Py_TYPE(((PyObject *)__pyx_v_self)), Py_TPFLAGS_HAVE_GC))
  #else
  unlikely(Py_TYPE(((PyObject *)__pyx_v_self))->tp_dictoffset != 0 || __Pyx_PyType_HasFeature(Py_TYPE(((PyObject *)__pyx_v_self)), (Py_TPFLAGS_IS_ABSTRACT | Py_TPFLAGS_HEAPTYPE)))
  #endif
  ) {
    #if CYTHON_USE_DICT_VERSIONS && CYTHON_USE_PYTYPE_LOOKUP && CYTHON_USE_TYPE_SLOTS
    static PY_UINT64_T __pyx_tp_dict_version = __PYX_DICT_VERSION_INIT, __pyx_obj_dict_version = __PYX_DICT_VERSION_INIT;
    if (unlikely(!__Pyx_object_dict_version_matches(((PyObject *)__pyx_v_self), __pyx_tp_dict_version, __pyx_obj_dict_version))) {
      PY_UINT64_T __pyx_typedict_guard = __Pyx_get_tp_dict_version(((PyObject *)__pyx_v_self));
      #endif
      __pyx_t_1 = __Pyx_PyObject_GetAttrStr(((PyObject *)__pyx_v_self), __pyx_mstate_global->__pyx_n_u_visitchildren); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 251, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_1);
      if (!__Pyx_IsSameCFunction(__pyx_t_1, (void(*)(void)) __pyx_pw_6Cython_8Compiler_7Visitor_16VisitorTransform_1visitchildren)) {
        __Pyx_XDECREF(__pyx_r);
        __pyx_t_3 = NULL;
        __Pyx_INCREF(__pyx_t_1);
        __pyx_t_4 = __pyx_t_1; 
        __pyx_t_5 = 1;
        #if CYTHON_UNPACK_METHODS
        if (unlikely(PyMethod_Check(__pyx_t_4))) {
          __pyx_t_3 = PyMethod_GET_SELF(__pyx_t_4);
          assert(__pyx_t_3);
          PyObject* __pyx__function = PyMethod_GET_FUNCTION(__pyx_t_4);
          __Pyx_INCREF(__pyx_t_3);
          __Pyx_INCREF(__pyx__function);
          __Pyx_DECREF_SET(__pyx_t_4, __pyx__function);
          __pyx_t_5 = 0;
        }
        #endif
        {
          PyObject *__pyx_callargs[4] = {__pyx_t_3, __pyx_v_parent, __pyx_v_attrs, __pyx_v_exclude};
          __pyx_t_2 = __Pyx_PyObject_FastCall((PyObject*)__pyx_t_4, __pyx_callargs+__pyx_t_5, (4-__pyx_t_5) | (__pyx_t_5*__Pyx_PY_VECTORCALL_ARGUMENTS_OFFSET));
          __Pyx_XDECREF(__pyx_t_3); __pyx_t_3 = 0;
          __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
          if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 251, __pyx_L1_error)
          __Pyx_GOTREF(__pyx_t_2);
        }
        __pyx_r = __pyx_t_2;
        __pyx_t_2 = 0;
        __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
        goto __pyx_L0;
      }
      #if CYTHON_USE_DICT_VERSIONS && CYTHON_USE_PYTYPE_LOOKUP && CYTHON_USE_TYPE_SLOTS
      __pyx_tp_dict_version = __Pyx_get_tp_dict_version(((PyObject *)__pyx_v_self));
      __pyx_obj_dict_version = __Pyx_get_object_dict_version(((PyObject *)__pyx_v_self));
      if (unlikely(__pyx_typedict_guard != __pyx_tp_dict_version)) {
        __pyx_tp_dict_version = __pyx_obj_dict_version = __PYX_DICT_VERSION_INIT;
      }
      #endif
      __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
      #if CYTHON_USE_DICT_VERSIONS && CYTHON_USE_PYTYPE_LOOKUP && CYTHON_USE_TYPE_SLOTS
    }
    #endif
  }
/* … */
  /* function exit code */
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_t_1);
  __Pyx_XDECREF(__pyx_t_2);
  __Pyx_XDECREF(__pyx_t_3);
  __Pyx_XDECREF(__pyx_t_4);
  __Pyx_AddTraceback("Cython.Compiler.Visitor.VisitorTransform.visitchildren", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_r = 0;
  __pyx_L0:;
  __Pyx_XGIVEREF(__pyx_r);
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}

/* Python wrapper */
static PyObject *__pyx_pw_6Cython_8Compiler_7Visitor_16VisitorTransform_1visitchildren(PyObject *__pyx_v_self, 
#if CYTHON_METH_FASTCALL
PyObject *const *__pyx_args, Py_ssize_t __pyx_nargs, PyObject *__pyx_kwds
#else
PyObject *__pyx_args, PyObject *__pyx_kwds
#endif
); /*proto*/
PyDoc_STRVAR(__pyx_doc_6Cython_8Compiler_7Visitor_16VisitorTransform_visitchildren, "File: Cython/Compiler/Visitor.py (starting at line 251)");
static PyMethodDef __pyx_mdef_6Cython_8Compiler_7Visitor_16VisitorTransform_1visitchildren = {"visitchildren", (PyCFunction)(void(*)(void))(__Pyx_PyCFunction_FastCallWithKeywords)__pyx_pw_6Cython_8Compiler_7Visitor_16VisitorTransform_1visitchildren, __Pyx_METH_FASTCALL|METH_KEYWORDS, __pyx_doc_6Cython_8Compiler_7Visitor_16VisitorTransform_visitchildren};
static PyObject *__pyx_pw_6Cython_8Compiler_7Visitor_16VisitorTransform_1visitchildren(PyObject *__pyx_v_self, 
#if CYTHON_METH_FASTCALL
PyObject *const *__pyx_args, Py_ssize_t __pyx_nargs, PyObject *__pyx_kwds
#else
PyObject *__pyx_args, PyObject *__pyx_kwds
#endif
) {
  PyObject *__pyx_v_parent = 0;
  PyObject *__pyx_v_attrs = 0;
  PyObject *__pyx_v_exclude = 0;
  #if !CYTHON_METH_FASTCALL
  CYTHON_UNUSED Py_ssize_t __pyx_nargs;
  #endif
  CYTHON_UNUSED PyObject *const *__pyx_kwvalues;
  PyObject *__pyx_r = 0;
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("visitchildren (wrapper)", 0);
  #if !CYTHON_METH_FASTCALL
  #if CYTHON_ASSUME_SAFE_SIZE
  __pyx_nargs = PyTuple_GET_SIZE(__pyx_args);
  #else
  __pyx_nargs = PyTuple_Size(__pyx_args); if (unlikely(__pyx_nargs < 0)) return NULL;
  #endif
  #endif
  __pyx_kwvalues = __Pyx_KwValues_FASTCALL(__pyx_args, __pyx_nargs);
  {
    PyObject ** const __pyx_pyargnames[] = {&__pyx_mstate_global->__pyx_n_u_parent,&__pyx_mstate_global->__pyx_n_u_attrs,&__pyx_mstate_global->__pyx_n_u_exclude,0};
  PyObject* values[3] = {0,0,0};
    const Py_ssize_t __pyx_kwds_len = (__pyx_kwds) ? __Pyx_NumKwargs_FASTCALL(__pyx_kwds) : 0;
    if (unlikely(__pyx_kwds_len) < 0) __PYX_ERR(0, 251, __pyx_L3_error)
    if (__pyx_kwds_len > 0) {
      switch (__pyx_nargs) {
        case  3:
        values[2] = __Pyx_ArgRef_FASTCALL(__pyx_args, 2);
        if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[2])) __PYX_ERR(0, 251, __pyx_L3_error)
        CYTHON_FALLTHROUGH;
        case  2:
        values[1] = __Pyx_ArgRef_FASTCALL(__pyx_args, 1);
        if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[1])) __PYX_ERR(0, 251, __pyx_L3_error)
        CYTHON_FALLTHROUGH;
        case  1:
        values[0] = __Pyx_ArgRef_FASTCALL(__pyx_args, 0);
        if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[0])) __PYX_ERR(0, 251, __pyx_L3_error)
        CYTHON_FALLTHROUGH;
        case  0: break;
        default: goto __pyx_L5_argtuple_error;
      }
      const Py_ssize_t kwd_pos_args = __pyx_nargs;
      if (__Pyx_ParseKeywords(__pyx_kwds, __pyx_kwvalues, __pyx_pyargnames, 0, values, kwd_pos_args, __pyx_kwds_len, "visitchildren", 0) < (0)) __PYX_ERR(0, 251, __pyx_L3_error)
      if (!values[1]) values[1] = __Pyx_NewRef(((PyObject *)Py_None));
      if (!values[2]) values[2] = __Pyx_NewRef(((PyObject *)Py_None));
      for (Py_ssize_t i = __pyx_nargs; i < 1; i++) {
        if (unlikely(!values[i])) { __Pyx_RaiseArgtupleInvalid("visitchildren", 0, 1, 3, i); __PYX_ERR(0, 251, __pyx_L3_error) }
      }
    } else {
      switch (__pyx_nargs) {
        case  3:
        values[2] = __Pyx_ArgRef_FASTCALL(__pyx_args, 2);
        if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[2])) __PYX_ERR(0, 251, __pyx_L3_error)
        CYTHON_FALLTHROUGH;
        case  2:
        values[1] = __Pyx_ArgRef_FASTCALL(__pyx_args, 1);
        if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[1])) __PYX_ERR(0, 251, __pyx_L3_error)
        CYTHON_FALLTHROUGH;
        case  1:
        values[0] = __Pyx_ArgRef_FASTCALL(__pyx_args, 0);
        if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[0])) __PYX_ERR(0, 251, __pyx_L3_error)
        break;
        default: goto __pyx_L5_argtuple_error;
      }
      if (!values[1]) values[1] = __Pyx_NewRef(((PyObject *)Py_None));
      if (!values[2]) values[2] = __Pyx_NewRef(((PyObject *)Py_None));
    }
    __pyx_v_parent = values[0];
    __pyx_v_attrs = values[1];
    __pyx_v_exclude = values[2];
  }
  goto __pyx_L6_skip;
  __pyx_L5_argtuple_error:;
  __Pyx_RaiseArgtupleInvalid("visitchildren", 0, 1, 3, __pyx_nargs); __PYX_ERR(0, 251, __pyx_L3_error)
  __pyx_L6_skip:;
  goto __pyx_L4_argument_unpacking_done;
  __pyx_L3_error:;
  for (Py_ssize_t __pyx_temp=0; __pyx_temp < (Py_ssize_t)(sizeof(values)/sizeof(values[0])); ++__pyx_temp) {
    Py_XDECREF(values[__pyx_temp]);
  }
  __Pyx_AddTraceback("Cython.Compiler.Visitor.VisitorTransform.visitchildren", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __Pyx_RefNannyFinishContext();
  return NULL;
  __pyx_L4_argument_unpacking_done:;
  __pyx_r = __pyx_pf_6Cython_8Compiler_7Visitor_16VisitorTransform_visitchildren(((struct __pyx_obj_6Cython_8Compiler_7Visitor_VisitorTransform *)__pyx_v_self), __pyx_v_parent, __pyx_v_attrs, __pyx_v_exclude);

  /* function exit code */
  for (Py_ssize_t __pyx_temp=0; __pyx_temp < (Py_ssize_t)(sizeof(values)/sizeof(values[0])); ++__pyx_temp) {
    Py_XDECREF(values[__pyx_temp]);
  }
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}

static PyObject *__pyx_pf_6Cython_8Compiler_7Visitor_16VisitorTransform_visitchildren(struct __pyx_obj_6Cython_8Compiler_7Visitor_VisitorTransform *__pyx_v_self, PyObject *__pyx_v_parent, PyObject *__pyx_v_attrs, PyObject *__pyx_v_exclude) {
  PyObject *__pyx_r = NULL;
  __Pyx_XDECREF(__pyx_r);
  __pyx_t_2.__pyx_n = 2;
  __pyx_t_2.attrs = __pyx_v_attrs;
  __pyx_t_2.exclude = __pyx_v_exclude;
  __pyx_t_1 = __pyx_vtabptr_6Cython_8Compiler_7Visitor_VisitorTransform->__pyx_base.visitchildren(((struct __pyx_obj_6Cython_8Compiler_7Visitor_TreeVisitor *)__pyx_v_self), __pyx_v_parent, 1, &__pyx_t_2); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 251, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __pyx_r = __pyx_t_1;
  __pyx_t_1 = 0;
  goto __pyx_L0;

  /* function exit code */
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_t_1);
  __Pyx_AddTraceback("Cython.Compiler.Visitor.VisitorTransform.visitchildren", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_r = NULL;
  __pyx_L0:;
  __Pyx_XGIVEREF(__pyx_r);
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}
/* … */
  __pyx_t_2 = __Pyx_CyFunction_New(&__pyx_mdef_6Cython_8Compiler_7Visitor_16VisitorTransform_1visitchildren, __Pyx_CYFUNCTION_CCLASS, __pyx_mstate_global->__pyx_n_u_VisitorTransform_visitchildren, NULL, __pyx_mstate_global->__pyx_n_u_Cython_Compiler_Visitor, __pyx_mstate_global->__pyx_d, ((PyObject *)__pyx_mstate_global->__pyx_codeobj_tab[6])); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 251, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  #if CYTHON_COMPILING_IN_CPYTHON && PY_VERSION_HEX >= 0x030E0000
  PyUnstable_Object_EnableDeferredRefcount(__pyx_t_2);
  #endif
  __Pyx_CyFunction_SetDefaultsTuple(__pyx_t_2, __pyx_mstate_global->__pyx_tuple[7]);
  if (__Pyx_SetItemOnTypeDict(__pyx_mstate_global->__pyx_ptype_6Cython_8Compiler_7Visitor_VisitorTransform, __pyx_mstate_global->__pyx_n_u_visitchildren, __pyx_t_2) < (0)) __PYX_ERR(0, 251, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
```

</details>

L252  ⚪  (score=0)
```python
        # generic def entry point for calls from Python subclasses
```
L253  🟡  (score=1)
```python
        return self._process_children(parent, attrs, exclude)
```
<details><summary>Show generated C (score=1)</summary>

```c
  __Pyx_XDECREF(__pyx_r);
  __pyx_t_6.__pyx_n = 2;
  __pyx_t_6.attrs = __pyx_v_attrs;
  __pyx_t_6.exclude = __pyx_v_exclude;
  __pyx_t_1 = __pyx_f_6Cython_8Compiler_7Visitor_16VisitorTransform__process_children(__pyx_v_self, __pyx_v_parent, &__pyx_t_6); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 253, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __pyx_r = __pyx_t_1;
  __pyx_t_1 = 0;
  goto __pyx_L0;
```

</details>

L254  ⚪  (score=0)
```python
```
L255  🟠  (score=8)
```python
    @cython.final
```
<details><summary>Show generated C (score=8)</summary>

```c
static PyObject *__pyx_f_6Cython_8Compiler_7Visitor_16VisitorTransform__process_children(struct __pyx_obj_6Cython_8Compiler_7Visitor_VisitorTransform *__pyx_v_self, PyObject *__pyx_v_parent, struct __pyx_opt_args_6Cython_8Compiler_7Visitor_16VisitorTransform__process_children *__pyx_optional_args) {
/* … */
  /* function exit code */
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_t_1);
  __Pyx_XDECREF(__pyx_t_5);
  __Pyx_XDECREF(__pyx_t_6);
  __Pyx_AddTraceback("Cython.Compiler.Visitor.VisitorTransform._process_children", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_r = 0;
  __pyx_L0:;
  __Pyx_XDECREF(__pyx_v_result);
  __Pyx_XDECREF(__pyx_v_attr);
  __Pyx_XDECREF(__pyx_v_newnode);
  __Pyx_XGIVEREF(__pyx_r);
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}
```

</details>

L256  ⚪  (score=0)
```python
    def _process_children(self, parent, attrs=None, exclude=None):
```
<details><summary>Show generated C (score=0)</summary>

```c
  PyObject *__pyx_v_attrs = ((PyObject *)Py_None);
  PyObject *__pyx_v_exclude = ((PyObject *)Py_None);
  PyObject *__pyx_v_result = NULL;
  PyObject *__pyx_v_attr = NULL;
  PyObject *__pyx_v_newnode = NULL;
  PyObject *__pyx_r = NULL;
  if (__pyx_optional_args) {
    if (__pyx_optional_args->__pyx_n > 0) {
      __pyx_v_attrs = __pyx_optional_args->attrs;
      if (__pyx_optional_args->__pyx_n > 1) {
        __pyx_v_exclude = __pyx_optional_args->exclude;
      }
    }
  }
```

</details>

L257  ⚪  (score=0)
```python
        # fast cdef entry point for calls from Cython subclasses
```
L258  ⚪  (score=0)
```python
        result = self._visitchildren(parent, attrs, exclude)
```
<details><summary>Show generated C (score=0)</summary>

```c
  __pyx_t_1 = ((struct __pyx_vtabstruct_6Cython_8Compiler_7Visitor_VisitorTransform *)__pyx_v_self->__pyx_base.__pyx_vtab)->__pyx_base._visitchildren(((struct __pyx_obj_6Cython_8Compiler_7Visitor_TreeVisitor *)__pyx_v_self), __pyx_v_parent, __pyx_v_attrs, __pyx_v_exclude); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 258, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __pyx_v_result = ((PyObject*)__pyx_t_1);
  __pyx_t_1 = 0;
```

</details>

L259  🟠  (score=8)
```python
        for attr, newnode in result.items():
```
<details><summary>Show generated C (score=8)</summary>

```c
  __pyx_t_2 = 0;
  if (unlikely(__pyx_v_result == Py_None)) {
    PyErr_Format(PyExc_AttributeError, "'NoneType' object has no attribute '%.30s'", "items");
    __PYX_ERR(0, 259, __pyx_L1_error)
  }
  __pyx_t_5 = __Pyx_dict_iterator(__pyx_v_result, 1, __pyx_mstate_global->__pyx_n_u_items, (&__pyx_t_3), (&__pyx_t_4)); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 259, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_5);
  __Pyx_XDECREF(__pyx_t_1);
  __pyx_t_1 = __pyx_t_5;
  __pyx_t_5 = 0;
  while (1) {
    __pyx_t_7 = __Pyx_dict_iter_next(__pyx_t_1, __pyx_t_3, &__pyx_t_2, &__pyx_t_5, &__pyx_t_6, NULL, __pyx_t_4);
    if (unlikely(__pyx_t_7 == 0)) break;
    if (unlikely(__pyx_t_7 == -1)) __PYX_ERR(0, 259, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_5);
    __Pyx_GOTREF(__pyx_t_6);
    __Pyx_XDECREF_SET(__pyx_v_attr, __pyx_t_5);
    __pyx_t_5 = 0;
    __Pyx_XDECREF_SET(__pyx_v_newnode, __pyx_t_6);
    __pyx_t_6 = 0;
```

</details>

L260  ⚪  (score=0)
```python
            if type(newnode) is list:
```
<details><summary>Show generated C (score=0)</summary>

```c
    __pyx_t_8 = (((PyObject *)Py_TYPE(__pyx_v_newnode)) == ((PyObject *)(&PyList_Type)));
    if (__pyx_t_8) {
/* … */
    }
```

</details>

L261  🟠  (score=6)
```python
                newnode = self._flatten_list(newnode)
```
<details><summary>Show generated C (score=6)</summary>

```c
      __pyx_v_newnode = PySequence_List(__pyx_v_newnode); if (unlikely(!__pyx_v_newnode)) __PYX_ERR(0, 261, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_v_newnode);
      __pyx_t_6 = __pyx_f_6Cython_8Compiler_7Visitor_16VisitorTransform__flatten_list(__pyx_v_self, __pyx_v_newnode); if (unlikely(!__pyx_t_6)) __PYX_ERR(0, 261, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_6);
      __Pyx_DECREF_SET(__pyx_v_newnode, __pyx_t_6);
      __pyx_t_6 = 0;
```

</details>

L262  🟠  (score=6)
```python
            setattr(parent, attr, newnode)
```
<details><summary>Show generated C (score=6)</summary>

```c
    __pyx_t_9 = PyObject_SetAttr(__pyx_v_parent, __pyx_v_attr, __pyx_v_newnode); if (unlikely(__pyx_t_9 == ((int)-1))) __PYX_ERR(0, 262, __pyx_L1_error)
  }
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
```

</details>

L263  🟡  (score=2)
```python
        return result
```
<details><summary>Show generated C (score=2)</summary>

```c
  __Pyx_XDECREF(__pyx_r);
  __Pyx_INCREF(__pyx_v_result);
  __pyx_r = __pyx_v_result;
  goto __pyx_L0;
```

</details>

L264  ⚪  (score=0)
```python
```
L265  🟠  (score=6)
```python
    @cython.final
```
<details><summary>Show generated C (score=6)</summary>

```c
static PyObject *__pyx_f_6Cython_8Compiler_7Visitor_16VisitorTransform__flatten_list(CYTHON_UNUSED struct __pyx_obj_6Cython_8Compiler_7Visitor_VisitorTransform *__pyx_v_self, PyObject *__pyx_v_orig_list) {
  PyObject *__pyx_v_newlist = NULL;
  PyObject *__pyx_v_x = NULL;
  PyObject *__pyx_r = NULL;
/* … */
  /* function exit code */
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_t_1);
  __Pyx_XDECREF(__pyx_t_3);
  __Pyx_AddTraceback("Cython.Compiler.Visitor.VisitorTransform._flatten_list", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_r = 0;
  __pyx_L0:;
  __Pyx_XDECREF(__pyx_v_newlist);
  __Pyx_XDECREF(__pyx_v_x);
  __Pyx_XGIVEREF(__pyx_r);
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}
```

</details>

L266  ⚪  (score=0)
```python
    def _flatten_list(self, orig_list):
```
L267  ⚪  (score=0)
```python
        # Flatten the list one level and remove any None
```
L268  🟠  (score=5)
```python
        newlist = []
```
<details><summary>Show generated C (score=5)</summary>

```c
  __pyx_t_1 = PyList_New(0); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 268, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __pyx_v_newlist = ((PyObject*)__pyx_t_1);
  __pyx_t_1 = 0;
```

</details>

L269  🔴  (score=12)
```python
        for x in orig_list:
```
<details><summary>Show generated C (score=12)</summary>

```c
  if (unlikely(__pyx_v_orig_list == Py_None)) {
    PyErr_SetString(PyExc_TypeError, "'NoneType' object is not iterable");
    __PYX_ERR(0, 269, __pyx_L1_error)
  }
  __pyx_t_1 = __pyx_v_orig_list; __Pyx_INCREF(__pyx_t_1);
  __pyx_t_2 = 0;
  for (;;) {
    {
      Py_ssize_t __pyx_temp = __Pyx_PyList_GET_SIZE(__pyx_t_1);
      #if !CYTHON_ASSUME_SAFE_SIZE
      if (unlikely((__pyx_temp < 0))) __PYX_ERR(0, 269, __pyx_L1_error)
      #endif
      if (__pyx_t_2 >= __pyx_temp) break;
    }
    __pyx_t_3 = __Pyx_PyList_GetItemRefFast(__pyx_t_1, __pyx_t_2, __Pyx_ReferenceSharing_OwnStrongReference);
    ++__pyx_t_2;
    if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 269, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_3);
    __Pyx_XDECREF_SET(__pyx_v_x, __pyx_t_3);
    __pyx_t_3 = 0;
/* … */
  }
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
```

</details>

L270  ⚪  (score=0)
```python
            if x is not None:
```
<details><summary>Show generated C (score=0)</summary>

```c
    __pyx_t_4 = (__pyx_v_x != Py_None);
    if (__pyx_t_4) {
/* … */
    }
```

</details>

L271  ⚪  (score=0)
```python
                if type(x) is list:
```
<details><summary>Show generated C (score=0)</summary>

```c
      __pyx_t_4 = (((PyObject *)Py_TYPE(__pyx_v_x)) == ((PyObject *)(&PyList_Type)));
      if (__pyx_t_4) {
/* … */
        goto __pyx_L6;
      }
```

</details>

L272  🟡  (score=2)
```python
                    newlist.extend(x)
```
<details><summary>Show generated C (score=2)</summary>

```c
        __pyx_t_5 = __Pyx_PyList_Extend(__pyx_v_newlist, __pyx_v_x); if (unlikely(__pyx_t_5 == ((int)-1))) __PYX_ERR(0, 272, __pyx_L1_error)
```

</details>

L273  ⚪  (score=0)
```python
                else:
```
L274  🟡  (score=2)
```python
                    newlist.append(x)
```
<details><summary>Show generated C (score=2)</summary>

```c
      /*else*/ {
        __pyx_t_5 = __Pyx_PyList_Append(__pyx_v_newlist, __pyx_v_x); if (unlikely(__pyx_t_5 == ((int)-1))) __PYX_ERR(0, 274, __pyx_L1_error)
      }
      __pyx_L6:;
```

</details>

L275  🟡  (score=2)
```python
        return newlist
```
<details><summary>Show generated C (score=2)</summary>

```c
  __Pyx_XDECREF(__pyx_r);
  __Pyx_INCREF(__pyx_v_newlist);
  __pyx_r = __pyx_v_newlist;
  goto __pyx_L0;
```

</details>

L276  ⚪  (score=0)
```python
```
L277  🔴  (score=92)
```python
    def visitchild(self, parent, attr, idx=0):
```
<details><summary>Show generated C (score=92)</summary>

```c
static PyObject *__pyx_pw_6Cython_8Compiler_7Visitor_16VisitorTransform_3visitchild(PyObject *__pyx_v_self, 
#if CYTHON_METH_FASTCALL
PyObject *const *__pyx_args, Py_ssize_t __pyx_nargs, PyObject *__pyx_kwds
#else
PyObject *__pyx_args, PyObject *__pyx_kwds
#endif
); /*proto*/
static PyObject *__pyx_f_6Cython_8Compiler_7Visitor_16VisitorTransform_visitchild(struct __pyx_obj_6Cython_8Compiler_7Visitor_VisitorTransform *__pyx_v_self, PyObject *__pyx_v_parent, PyObject *__pyx_v_attr, int __pyx_skip_dispatch, struct __pyx_opt_args_6Cython_8Compiler_7Visitor_16VisitorTransform_visitchild *__pyx_optional_args) {
  PyObject *__pyx_v_idx = ((PyObject *)__pyx_mstate_global->__pyx_int_0);
  PyObject *__pyx_v_child = NULL;
  PyObject *__pyx_v_node = NULL;
  PyObject *__pyx_r = NULL;
  if (__pyx_optional_args) {
    if (__pyx_optional_args->__pyx_n > 0) {
      __pyx_v_idx = __pyx_optional_args->idx;
    }
  }
  /* Check if called by wrapper */
  if (unlikely(__pyx_skip_dispatch)) ;
  /* Check if overridden in Python */
  else if (
  #if !CYTHON_USE_TYPE_SLOTS
  unlikely(Py_TYPE(((PyObject *)__pyx_v_self)) != __pyx_mstate_global->__pyx_ptype_6Cython_8Compiler_7Visitor_VisitorTransform &&
  __Pyx_PyType_HasFeature(Py_TYPE(((PyObject *)__pyx_v_self)), Py_TPFLAGS_HAVE_GC))
  #else
  unlikely(Py_TYPE(((PyObject *)__pyx_v_self))->tp_dictoffset != 0 || __Pyx_PyType_HasFeature(Py_TYPE(((PyObject *)__pyx_v_self)), (Py_TPFLAGS_IS_ABSTRACT | Py_TPFLAGS_HEAPTYPE)))
  #endif
  ) {
    #if CYTHON_USE_DICT_VERSIONS && CYTHON_USE_PYTYPE_LOOKUP && CYTHON_USE_TYPE_SLOTS
    static PY_UINT64_T __pyx_tp_dict_version = __PYX_DICT_VERSION_INIT, __pyx_obj_dict_version = __PYX_DICT_VERSION_INIT;
    if (unlikely(!__Pyx_object_dict_version_matches(((PyObject *)__pyx_v_self), __pyx_tp_dict_version, __pyx_obj_dict_version))) {
      PY_UINT64_T __pyx_typedict_guard = __Pyx_get_tp_dict_version(((PyObject *)__pyx_v_self));
      #endif
      __pyx_t_1 = __Pyx_PyObject_GetAttrStr(((PyObject *)__pyx_v_self), __pyx_mstate_global->__pyx_n_u_visitchild); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 277, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_1);
      if (!__Pyx_IsSameCFunction(__pyx_t_1, (void(*)(void)) __pyx_pw_6Cython_8Compiler_7Visitor_16VisitorTransform_3visitchild)) {
        __Pyx_XDECREF(__pyx_r);
        __pyx_t_3 = NULL;
        __Pyx_INCREF(__pyx_t_1);
        __pyx_t_4 = __pyx_t_1; 
        __pyx_t_5 = 1;
        #if CYTHON_UNPACK_METHODS
        if (unlikely(PyMethod_Check(__pyx_t_4))) {
          __pyx_t_3 = PyMethod_GET_SELF(__pyx_t_4);
          assert(__pyx_t_3);
          PyObject* __pyx__function = PyMethod_GET_FUNCTION(__pyx_t_4);
          __Pyx_INCREF(__pyx_t_3);
          __Pyx_INCREF(__pyx__function);
          __Pyx_DECREF_SET(__pyx_t_4, __pyx__function);
          __pyx_t_5 = 0;
        }
        #endif
        {
          PyObject *__pyx_callargs[4] = {__pyx_t_3, __pyx_v_parent, __pyx_v_attr, __pyx_v_idx};
          __pyx_t_2 = __Pyx_PyObject_FastCall((PyObject*)__pyx_t_4, __pyx_callargs+__pyx_t_5, (4-__pyx_t_5) | (__pyx_t_5*__Pyx_PY_VECTORCALL_ARGUMENTS_OFFSET));
          __Pyx_XDECREF(__pyx_t_3); __pyx_t_3 = 0;
          __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
          if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 277, __pyx_L1_error)
          __Pyx_GOTREF(__pyx_t_2);
        }
        __pyx_r = __pyx_t_2;
        __pyx_t_2 = 0;
        __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
        goto __pyx_L0;
      }
      #if CYTHON_USE_DICT_VERSIONS && CYTHON_USE_PYTYPE_LOOKUP && CYTHON_USE_TYPE_SLOTS
      __pyx_tp_dict_version = __Pyx_get_tp_dict_version(((PyObject *)__pyx_v_self));
      __pyx_obj_dict_version = __Pyx_get_object_dict_version(((PyObject *)__pyx_v_self));
      if (unlikely(__pyx_typedict_guard != __pyx_tp_dict_version)) {
        __pyx_tp_dict_version = __pyx_obj_dict_version = __PYX_DICT_VERSION_INIT;
      }
      #endif
      __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
      #if CYTHON_USE_DICT_VERSIONS && CYTHON_USE_PYTYPE_LOOKUP && CYTHON_USE_TYPE_SLOTS
    }
    #endif
  }
/* … */
  /* function exit code */
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_t_1);
  __Pyx_XDECREF(__pyx_t_2);
  __Pyx_XDECREF(__pyx_t_3);
  __Pyx_XDECREF(__pyx_t_4);
  __Pyx_AddTraceback("Cython.Compiler.Visitor.VisitorTransform.visitchild", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_r = 0;
  __pyx_L0:;
  __Pyx_XDECREF(__pyx_v_child);
  __Pyx_XDECREF(__pyx_v_node);
  __Pyx_XGIVEREF(__pyx_r);
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}

/* Python wrapper */
static PyObject *__pyx_pw_6Cython_8Compiler_7Visitor_16VisitorTransform_3visitchild(PyObject *__pyx_v_self, 
#if CYTHON_METH_FASTCALL
PyObject *const *__pyx_args, Py_ssize_t __pyx_nargs, PyObject *__pyx_kwds
#else
PyObject *__pyx_args, PyObject *__pyx_kwds
#endif
); /*proto*/
PyDoc_STRVAR(__pyx_doc_6Cython_8Compiler_7Visitor_16VisitorTransform_2visitchild, "File: Cython/Compiler/Visitor.py (starting at line 277)");
static PyMethodDef __pyx_mdef_6Cython_8Compiler_7Visitor_16VisitorTransform_3visitchild = {"visitchild", (PyCFunction)(void(*)(void))(__Pyx_PyCFunction_FastCallWithKeywords)__pyx_pw_6Cython_8Compiler_7Visitor_16VisitorTransform_3visitchild, __Pyx_METH_FASTCALL|METH_KEYWORDS, __pyx_doc_6Cython_8Compiler_7Visitor_16VisitorTransform_2visitchild};
static PyObject *__pyx_pw_6Cython_8Compiler_7Visitor_16VisitorTransform_3visitchild(PyObject *__pyx_v_self, 
#if CYTHON_METH_FASTCALL
PyObject *const *__pyx_args, Py_ssize_t __pyx_nargs, PyObject *__pyx_kwds
#else
PyObject *__pyx_args, PyObject *__pyx_kwds
#endif
) {
  PyObject *__pyx_v_parent = 0;
  PyObject *__pyx_v_attr = 0;
  PyObject *__pyx_v_idx = 0;
  #if !CYTHON_METH_FASTCALL
  CYTHON_UNUSED Py_ssize_t __pyx_nargs;
  #endif
  CYTHON_UNUSED PyObject *const *__pyx_kwvalues;
  PyObject *__pyx_r = 0;
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("visitchild (wrapper)", 0);
  #if !CYTHON_METH_FASTCALL
  #if CYTHON_ASSUME_SAFE_SIZE
  __pyx_nargs = PyTuple_GET_SIZE(__pyx_args);
  #else
  __pyx_nargs = PyTuple_Size(__pyx_args); if (unlikely(__pyx_nargs < 0)) return NULL;
  #endif
  #endif
  __pyx_kwvalues = __Pyx_KwValues_FASTCALL(__pyx_args, __pyx_nargs);
  {
    PyObject ** const __pyx_pyargnames[] = {&__pyx_mstate_global->__pyx_n_u_parent,&__pyx_mstate_global->__pyx_n_u_attr,&__pyx_mstate_global->__pyx_n_u_idx,0};
  PyObject* values[3] = {0,0,0};
    const Py_ssize_t __pyx_kwds_len = (__pyx_kwds) ? __Pyx_NumKwargs_FASTCALL(__pyx_kwds) : 0;
    if (unlikely(__pyx_kwds_len) < 0) __PYX_ERR(0, 277, __pyx_L3_error)
    if (__pyx_kwds_len > 0) {
      switch (__pyx_nargs) {
        case  3:
        values[2] = __Pyx_ArgRef_FASTCALL(__pyx_args, 2);
        if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[2])) __PYX_ERR(0, 277, __pyx_L3_error)
        CYTHON_FALLTHROUGH;
        case  2:
        values[1] = __Pyx_ArgRef_FASTCALL(__pyx_args, 1);
        if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[1])) __PYX_ERR(0, 277, __pyx_L3_error)
        CYTHON_FALLTHROUGH;
        case  1:
        values[0] = __Pyx_ArgRef_FASTCALL(__pyx_args, 0);
        if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[0])) __PYX_ERR(0, 277, __pyx_L3_error)
        CYTHON_FALLTHROUGH;
        case  0: break;
        default: goto __pyx_L5_argtuple_error;
      }
      const Py_ssize_t kwd_pos_args = __pyx_nargs;
      if (__Pyx_ParseKeywords(__pyx_kwds, __pyx_kwvalues, __pyx_pyargnames, 0, values, kwd_pos_args, __pyx_kwds_len, "visitchild", 0) < (0)) __PYX_ERR(0, 277, __pyx_L3_error)
      if (!values[2]) values[2] = __Pyx_NewRef(((PyObject *)__pyx_mstate_global->__pyx_int_0));
      for (Py_ssize_t i = __pyx_nargs; i < 2; i++) {
        if (unlikely(!values[i])) { __Pyx_RaiseArgtupleInvalid("visitchild", 0, 2, 3, i); __PYX_ERR(0, 277, __pyx_L3_error) }
      }
    } else {
      switch (__pyx_nargs) {
        case  3:
        values[2] = __Pyx_ArgRef_FASTCALL(__pyx_args, 2);
        if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[2])) __PYX_ERR(0, 277, __pyx_L3_error)
        CYTHON_FALLTHROUGH;
        case  2:
        values[1] = __Pyx_ArgRef_FASTCALL(__pyx_args, 1);
        if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[1])) __PYX_ERR(0, 277, __pyx_L3_error)
        values[0] = __Pyx_ArgRef_FASTCALL(__pyx_args, 0);
        if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[0])) __PYX_ERR(0, 277, __pyx_L3_error)
        break;
        default: goto __pyx_L5_argtuple_error;
      }
      if (!values[2]) values[2] = __Pyx_NewRef(((PyObject *)__pyx_mstate_global->__pyx_int_0));
    }
    __pyx_v_parent = values[0];
    __pyx_v_attr = ((PyObject*)values[1]);
    __pyx_v_idx = values[2];
  }
  goto __pyx_L6_skip;
  __pyx_L5_argtuple_error:;
  __Pyx_RaiseArgtupleInvalid("visitchild", 0, 2, 3, __pyx_nargs); __PYX_ERR(0, 277, __pyx_L3_error)
  __pyx_L6_skip:;
  goto __pyx_L4_argument_unpacking_done;
  __pyx_L3_error:;
  for (Py_ssize_t __pyx_temp=0; __pyx_temp < (Py_ssize_t)(sizeof(values)/sizeof(values[0])); ++__pyx_temp) {
    Py_XDECREF(values[__pyx_temp]);
  }
  __Pyx_AddTraceback("Cython.Compiler.Visitor.VisitorTransform.visitchild", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __Pyx_RefNannyFinishContext();
  return NULL;
  __pyx_L4_argument_unpacking_done:;
  if (unlikely(!__Pyx_ArgTypeTest(((PyObject *)__pyx_v_attr), (&PyUnicode_Type), 1, "attr", 1))) __PYX_ERR(0, 277, __pyx_L1_error)
  __pyx_r = __pyx_pf_6Cython_8Compiler_7Visitor_16VisitorTransform_2visitchild(((struct __pyx_obj_6Cython_8Compiler_7Visitor_VisitorTransform *)__pyx_v_self), __pyx_v_parent, __pyx_v_attr, __pyx_v_idx);
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

static PyObject *__pyx_pf_6Cython_8Compiler_7Visitor_16VisitorTransform_2visitchild(struct __pyx_obj_6Cython_8Compiler_7Visitor_VisitorTransform *__pyx_v_self, PyObject *__pyx_v_parent, PyObject *__pyx_v_attr, PyObject *__pyx_v_idx) {
  PyObject *__pyx_r = NULL;
  __Pyx_XDECREF(__pyx_r);
  __pyx_t_2.__pyx_n = 1;
  __pyx_t_2.idx = __pyx_v_idx;
  __pyx_t_1 = __pyx_vtabptr_6Cython_8Compiler_7Visitor_VisitorTransform->visitchild(__pyx_v_self, __pyx_v_parent, __pyx_v_attr, 1, &__pyx_t_2); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 277, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __pyx_r = __pyx_t_1;
  __pyx_t_1 = 0;
  goto __pyx_L0;

  /* function exit code */
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_t_1);
  __Pyx_AddTraceback("Cython.Compiler.Visitor.VisitorTransform.visitchild", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_r = NULL;
  __pyx_L0:;
  __Pyx_XGIVEREF(__pyx_r);
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}
/* … */
  __pyx_t_2 = __Pyx_CyFunction_New(&__pyx_mdef_6Cython_8Compiler_7Visitor_16VisitorTransform_3visitchild, __Pyx_CYFUNCTION_CCLASS, __pyx_mstate_global->__pyx_n_u_VisitorTransform_visitchild, NULL, __pyx_mstate_global->__pyx_n_u_Cython_Compiler_Visitor, __pyx_mstate_global->__pyx_d, ((PyObject *)__pyx_mstate_global->__pyx_codeobj_tab[7])); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 277, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  #if CYTHON_COMPILING_IN_CPYTHON && PY_VERSION_HEX >= 0x030E0000
  PyUnstable_Object_EnableDeferredRefcount(__pyx_t_2);
  #endif
  __Pyx_CyFunction_SetDefaultsTuple(__pyx_t_2, __pyx_mstate_global->__pyx_tuple[8]);
  if (__Pyx_SetItemOnTypeDict(__pyx_mstate_global->__pyx_ptype_6Cython_8Compiler_7Visitor_VisitorTransform, __pyx_mstate_global->__pyx_n_u_visitchild, __pyx_t_2) < (0)) __PYX_ERR(0, 277, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
/* … */
  __pyx_mstate_global->__pyx_tuple[8] = PyTuple_Pack(1, __pyx_mstate_global->__pyx_int_0); if (unlikely(!__pyx_mstate_global->__pyx_tuple[8])) __PYX_ERR(0, 277, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_mstate_global->__pyx_tuple[8]);
  __Pyx_GIVEREF(__pyx_mstate_global->__pyx_tuple[8]);
```

</details>

L278  ⚪  (score=0)
```python
        # Helper to visit specific children from Python subclasses
```
L279  🟡  (score=2)
```python
        child = getattr(parent, attr)
```
<details><summary>Show generated C (score=2)</summary>

```c
  __pyx_t_1 = __Pyx_GetAttr(__pyx_v_parent, __pyx_v_attr); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 279, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __pyx_v_child = __pyx_t_1;
  __pyx_t_1 = 0;
```

</details>

L280  ⚪  (score=0)
```python
        if child is not None:
```
<details><summary>Show generated C (score=0)</summary>

```c
  __pyx_t_6 = (__pyx_v_child != Py_None);
  if (__pyx_t_6) {
/* … */
  }
```

</details>

L281  ⚪  (score=0)
```python
            node = self._visitchild(child, parent, attr, idx)
```
<details><summary>Show generated C (score=0)</summary>

```c
    __pyx_t_1 = ((struct __pyx_vtabstruct_6Cython_8Compiler_7Visitor_VisitorTransform *)__pyx_v_self->__pyx_base.__pyx_vtab)->__pyx_base._visitchild(((struct __pyx_obj_6Cython_8Compiler_7Visitor_TreeVisitor *)__pyx_v_self), __pyx_v_child, __pyx_v_parent, __pyx_v_attr, __pyx_v_idx); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 281, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_1);
    __pyx_v_node = __pyx_t_1;
    __pyx_t_1 = 0;
```

</details>

L282  ⚪  (score=0)
```python
            if node is not child:
```
<details><summary>Show generated C (score=0)</summary>

```c
    __pyx_t_6 = (__pyx_v_node != __pyx_v_child);
    if (__pyx_t_6) {
/* … */
    }
```

</details>

L283  🟠  (score=5)
```python
                setattr(parent, attr, node)
```
<details><summary>Show generated C (score=5)</summary>

```c
      __pyx_t_7 = PyObject_SetAttr(__pyx_v_parent, __pyx_v_attr, __pyx_v_node); if (unlikely(__pyx_t_7 == ((int)-1))) __PYX_ERR(0, 283, __pyx_L1_error)
```

</details>

L284  🟡  (score=2)
```python
            child = node
```
<details><summary>Show generated C (score=2)</summary>

```c
    __Pyx_INCREF(__pyx_v_node);
    __Pyx_DECREF_SET(__pyx_v_child, __pyx_v_node);
```

</details>

L285  🟡  (score=2)
```python
        return child
```
<details><summary>Show generated C (score=2)</summary>

```c
  __Pyx_XDECREF(__pyx_r);
  __Pyx_INCREF(__pyx_v_child);
  __pyx_r = __pyx_v_child;
  goto __pyx_L0;
```

</details>

L286  ⚪  (score=0)
```python
```
L287  🔴  (score=36)
```python
    def recurse_to_children(self, node):
```
<details><summary>Show generated C (score=36)</summary>

```c
/* Python wrapper */
static PyObject *__pyx_pw_6Cython_8Compiler_7Visitor_16VisitorTransform_5recurse_to_children(PyObject *__pyx_v_self, 
#if CYTHON_METH_FASTCALL
PyObject *const *__pyx_args, Py_ssize_t __pyx_nargs, PyObject *__pyx_kwds
#else
PyObject *__pyx_args, PyObject *__pyx_kwds
#endif
); /*proto*/
PyDoc_STRVAR(__pyx_doc_6Cython_8Compiler_7Visitor_16VisitorTransform_4recurse_to_children, "File: Cython/Compiler/Visitor.py (starting at line 287)");
static PyMethodDef __pyx_mdef_6Cython_8Compiler_7Visitor_16VisitorTransform_5recurse_to_children = {"recurse_to_children", (PyCFunction)(void(*)(void))(__Pyx_PyCFunction_FastCallWithKeywords)__pyx_pw_6Cython_8Compiler_7Visitor_16VisitorTransform_5recurse_to_children, __Pyx_METH_FASTCALL|METH_KEYWORDS, __pyx_doc_6Cython_8Compiler_7Visitor_16VisitorTransform_4recurse_to_children};
static PyObject *__pyx_pw_6Cython_8Compiler_7Visitor_16VisitorTransform_5recurse_to_children(PyObject *__pyx_v_self, 
#if CYTHON_METH_FASTCALL
PyObject *const *__pyx_args, Py_ssize_t __pyx_nargs, PyObject *__pyx_kwds
#else
PyObject *__pyx_args, PyObject *__pyx_kwds
#endif
) {
  PyObject *__pyx_v_node = 0;
  #if !CYTHON_METH_FASTCALL
  CYTHON_UNUSED Py_ssize_t __pyx_nargs;
  #endif
  CYTHON_UNUSED PyObject *const *__pyx_kwvalues;
  PyObject *__pyx_r = 0;
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("recurse_to_children (wrapper)", 0);
  #if !CYTHON_METH_FASTCALL
  #if CYTHON_ASSUME_SAFE_SIZE
  __pyx_nargs = PyTuple_GET_SIZE(__pyx_args);
  #else
  __pyx_nargs = PyTuple_Size(__pyx_args); if (unlikely(__pyx_nargs < 0)) return NULL;
  #endif
  #endif
  __pyx_kwvalues = __Pyx_KwValues_FASTCALL(__pyx_args, __pyx_nargs);
  {
    PyObject ** const __pyx_pyargnames[] = {&__pyx_mstate_global->__pyx_n_u_node,0};
  PyObject* values[1] = {0};
    const Py_ssize_t __pyx_kwds_len = (__pyx_kwds) ? __Pyx_NumKwargs_FASTCALL(__pyx_kwds) : 0;
    if (unlikely(__pyx_kwds_len) < 0) __PYX_ERR(0, 287, __pyx_L3_error)
    if (__pyx_kwds_len > 0) {
      switch (__pyx_nargs) {
        case  1:
        values[0] = __Pyx_ArgRef_FASTCALL(__pyx_args, 0);
        if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[0])) __PYX_ERR(0, 287, __pyx_L3_error)
        CYTHON_FALLTHROUGH;
        case  0: break;
        default: goto __pyx_L5_argtuple_error;
      }
      const Py_ssize_t kwd_pos_args = __pyx_nargs;
      if (__Pyx_ParseKeywords(__pyx_kwds, __pyx_kwvalues, __pyx_pyargnames, 0, values, kwd_pos_args, __pyx_kwds_len, "recurse_to_children", 0) < (0)) __PYX_ERR(0, 287, __pyx_L3_error)
      for (Py_ssize_t i = __pyx_nargs; i < 1; i++) {
        if (unlikely(!values[i])) { __Pyx_RaiseArgtupleInvalid("recurse_to_children", 1, 1, 1, i); __PYX_ERR(0, 287, __pyx_L3_error) }
      }
    } else if (unlikely(__pyx_nargs != 1)) {
      goto __pyx_L5_argtuple_error;
    } else {
      values[0] = __Pyx_ArgRef_FASTCALL(__pyx_args, 0);
      if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[0])) __PYX_ERR(0, 287, __pyx_L3_error)
    }
    __pyx_v_node = values[0];
  }
  goto __pyx_L6_skip;
  __pyx_L5_argtuple_error:;
  __Pyx_RaiseArgtupleInvalid("recurse_to_children", 1, 1, 1, __pyx_nargs); __PYX_ERR(0, 287, __pyx_L3_error)
  __pyx_L6_skip:;
  goto __pyx_L4_argument_unpacking_done;
  __pyx_L3_error:;
  for (Py_ssize_t __pyx_temp=0; __pyx_temp < (Py_ssize_t)(sizeof(values)/sizeof(values[0])); ++__pyx_temp) {
    Py_XDECREF(values[__pyx_temp]);
  }
  __Pyx_AddTraceback("Cython.Compiler.Visitor.VisitorTransform.recurse_to_children", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __Pyx_RefNannyFinishContext();
  return NULL;
  __pyx_L4_argument_unpacking_done:;
  __pyx_r = __pyx_pf_6Cython_8Compiler_7Visitor_16VisitorTransform_4recurse_to_children(((struct __pyx_obj_6Cython_8Compiler_7Visitor_VisitorTransform *)__pyx_v_self), __pyx_v_node);
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

static PyObject *__pyx_pf_6Cython_8Compiler_7Visitor_16VisitorTransform_4recurse_to_children(struct __pyx_obj_6Cython_8Compiler_7Visitor_VisitorTransform *__pyx_v_self, PyObject *__pyx_v_node) {
  PyObject *__pyx_r = NULL;
/* … */
  /* function exit code */
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_t_1);
  __Pyx_AddTraceback("Cython.Compiler.Visitor.VisitorTransform.recurse_to_children", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_r = NULL;
  __pyx_L0:;
  __Pyx_XGIVEREF(__pyx_r);
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}
/* … */
  __pyx_t_2 = __Pyx_CyFunction_New(&__pyx_mdef_6Cython_8Compiler_7Visitor_16VisitorTransform_5recurse_to_children, __Pyx_CYFUNCTION_CCLASS, __pyx_mstate_global->__pyx_n_u_VisitorTransform_recurse_to_chil, NULL, __pyx_mstate_global->__pyx_n_u_Cython_Compiler_Visitor, __pyx_mstate_global->__pyx_d, ((PyObject *)__pyx_mstate_global->__pyx_codeobj_tab[8])); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 287, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  #if CYTHON_COMPILING_IN_CPYTHON && PY_VERSION_HEX >= 0x030E0000
  PyUnstable_Object_EnableDeferredRefcount(__pyx_t_2);
  #endif
  if (__Pyx_SetItemOnTypeDict(__pyx_mstate_global->__pyx_ptype_6Cython_8Compiler_7Visitor_VisitorTransform, __pyx_mstate_global->__pyx_n_u_recurse_to_children, __pyx_t_2) < (0)) __PYX_ERR(0, 287, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
```

</details>

L288  🟡  (score=1)
```python
        self._process_children(node)
```
<details><summary>Show generated C (score=1)</summary>

```c
  __pyx_t_1 = __pyx_f_6Cython_8Compiler_7Visitor_16VisitorTransform__process_children(__pyx_v_self, __pyx_v_node, NULL); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 288, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
```

</details>

L289  🟡  (score=2)
```python
        return node
```
<details><summary>Show generated C (score=2)</summary>

```c
  __Pyx_XDECREF(__pyx_r);
  __Pyx_INCREF(__pyx_v_node);
  __pyx_r = __pyx_v_node;
  goto __pyx_L0;
```

</details>

L290  ⚪  (score=0)
```python
```
L291  🔴  (score=26)
```python
    def __call__(self, root):
```
<details><summary>Show generated C (score=26)</summary>

```c
/* Python wrapper */
static PyObject *__pyx_pw_6Cython_8Compiler_7Visitor_16VisitorTransform_7__call__(PyObject *__pyx_v_self, PyObject *__pyx_args, PyObject *__pyx_kwds); /*proto*/
PyDoc_STRVAR(__pyx_doc_6Cython_8Compiler_7Visitor_16VisitorTransform_6__call__, "File: Cython/Compiler/Visitor.py (starting at line 291)");
#if CYTHON_UPDATE_DESCRIPTOR_DOC
struct wrapperbase __pyx_wrapperbase_6Cython_8Compiler_7Visitor_16VisitorTransform_6__call__;
#endif
static PyObject *__pyx_pw_6Cython_8Compiler_7Visitor_16VisitorTransform_7__call__(PyObject *__pyx_v_self, PyObject *__pyx_args, PyObject *__pyx_kwds) {
  PyObject *__pyx_v_root = 0;
  CYTHON_UNUSED Py_ssize_t __pyx_nargs;
  CYTHON_UNUSED PyObject *const *__pyx_kwvalues;
  PyObject *__pyx_r = 0;
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("__call__ (wrapper)", 0);
  #if CYTHON_ASSUME_SAFE_SIZE
  __pyx_nargs = PyTuple_GET_SIZE(__pyx_args);
  #else
  __pyx_nargs = PyTuple_Size(__pyx_args); if (unlikely(__pyx_nargs < 0)) return NULL;
  #endif
  __pyx_kwvalues = __Pyx_KwValues_VARARGS(__pyx_args, __pyx_nargs);
  {
    PyObject ** const __pyx_pyargnames[] = {&__pyx_mstate_global->__pyx_n_u_root,0};
  PyObject* values[1] = {0};
    const Py_ssize_t __pyx_kwds_len = (__pyx_kwds) ? __Pyx_NumKwargs_VARARGS(__pyx_kwds) : 0;
    if (unlikely(__pyx_kwds_len) < 0) __PYX_ERR(0, 291, __pyx_L3_error)
    if (__pyx_kwds_len > 0) {
      switch (__pyx_nargs) {
        case  1:
        values[0] = __Pyx_ArgRef_VARARGS(__pyx_args, 0);
        if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[0])) __PYX_ERR(0, 291, __pyx_L3_error)
        CYTHON_FALLTHROUGH;
        case  0: break;
        default: goto __pyx_L5_argtuple_error;
      }
      const Py_ssize_t kwd_pos_args = __pyx_nargs;
      if (__Pyx_ParseKeywords(__pyx_kwds, __pyx_kwvalues, __pyx_pyargnames, 0, values, kwd_pos_args, __pyx_kwds_len, "__call__", 0) < (0)) __PYX_ERR(0, 291, __pyx_L3_error)
      for (Py_ssize_t i = __pyx_nargs; i < 1; i++) {
        if (unlikely(!values[i])) { __Pyx_RaiseArgtupleInvalid("__call__", 1, 1, 1, i); __PYX_ERR(0, 291, __pyx_L3_error) }
      }
    } else if (unlikely(__pyx_nargs != 1)) {
      goto __pyx_L5_argtuple_error;
    } else {
      values[0] = __Pyx_ArgRef_VARARGS(__pyx_args, 0);
      if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[0])) __PYX_ERR(0, 291, __pyx_L3_error)
    }
    __pyx_v_root = values[0];
  }
  goto __pyx_L6_skip;
  __pyx_L5_argtuple_error:;
  __Pyx_RaiseArgtupleInvalid("__call__", 1, 1, 1, __pyx_nargs); __PYX_ERR(0, 291, __pyx_L3_error)
  __pyx_L6_skip:;
  goto __pyx_L4_argument_unpacking_done;
  __pyx_L3_error:;
  for (Py_ssize_t __pyx_temp=0; __pyx_temp < (Py_ssize_t)(sizeof(values)/sizeof(values[0])); ++__pyx_temp) {
    Py_XDECREF(values[__pyx_temp]);
  }
  __Pyx_AddTraceback("Cython.Compiler.Visitor.VisitorTransform.__call__", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __Pyx_RefNannyFinishContext();
  return NULL;
  __pyx_L4_argument_unpacking_done:;
  __pyx_r = __pyx_pf_6Cython_8Compiler_7Visitor_16VisitorTransform_6__call__(((struct __pyx_obj_6Cython_8Compiler_7Visitor_VisitorTransform *)__pyx_v_self), __pyx_v_root);
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

static PyObject *__pyx_pf_6Cython_8Compiler_7Visitor_16VisitorTransform_6__call__(struct __pyx_obj_6Cython_8Compiler_7Visitor_VisitorTransform *__pyx_v_self, PyObject *__pyx_v_root) {
  PyObject *__pyx_r = NULL;
/* … */
  /* function exit code */
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_t_1);
  __Pyx_AddTraceback("Cython.Compiler.Visitor.VisitorTransform.__call__", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_r = NULL;
  __pyx_L0:;
  __Pyx_XGIVEREF(__pyx_r);
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}
```

</details>

L292  🟡  (score=1)
```python
        return self._visit(root)
```
<details><summary>Show generated C (score=1)</summary>

```c
  __Pyx_XDECREF(__pyx_r);
  __pyx_t_1 = ((struct __pyx_vtabstruct_6Cython_8Compiler_7Visitor_VisitorTransform *)__pyx_v_self->__pyx_base.__pyx_vtab)->__pyx_base._visit(((struct __pyx_obj_6Cython_8Compiler_7Visitor_TreeVisitor *)__pyx_v_self), __pyx_v_root); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 292, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __pyx_r = __pyx_t_1;
  __pyx_t_1 = 0;
  goto __pyx_L0;
```

</details>

L293  ⚪  (score=0)
```python
```
L294  ⚪  (score=0)
```python
```
L295  ⚪  (score=0)
```python
class CythonTransform(VisitorTransform):
```
<details><summary>Show generated C (score=0)</summary>

```c
struct __pyx_vtabstruct_6Cython_8Compiler_7Visitor_CythonTransform {
  struct __pyx_vtabstruct_6Cython_8Compiler_7Visitor_VisitorTransform __pyx_base;
};
static struct __pyx_vtabstruct_6Cython_8Compiler_7Visitor_CythonTransform *__pyx_vtabptr_6Cython_8Compiler_7Visitor_CythonTransform;

```

</details>

L296  ⚪  (score=0)
```python
    """
```
L297  ⚪  (score=0)
```python
    Certain common conventions and utilities for Cython transforms.
```
L298  ⚪  (score=0)
```python
```
L299  ⚪  (score=0)
```python
     - Sets up the context of the pipeline in self.context
```
L300  ⚪  (score=0)
```python
     - Tracks directives in effect in self.current_directives
```
L301  ⚪  (score=0)
```python
    """
```
L302  🔴  (score=29)
```python
    def __init__(self, context):
```
<details><summary>Show generated C (score=29)</summary>

```c
/* Python wrapper */
static int __pyx_pw_6Cython_8Compiler_7Visitor_15CythonTransform_1__init__(PyObject *__pyx_v_self, PyObject *__pyx_args, PyObject *__pyx_kwds); /*proto*/
PyDoc_STRVAR(__pyx_doc_6Cython_8Compiler_7Visitor_15CythonTransform___init__, "File: Cython/Compiler/Visitor.py (starting at line 302)");
#if CYTHON_UPDATE_DESCRIPTOR_DOC
struct wrapperbase __pyx_wrapperbase_6Cython_8Compiler_7Visitor_15CythonTransform___init__;
#endif
static int __pyx_pw_6Cython_8Compiler_7Visitor_15CythonTransform_1__init__(PyObject *__pyx_v_self, PyObject *__pyx_args, PyObject *__pyx_kwds) {
  PyObject *__pyx_v_context = 0;
  CYTHON_UNUSED Py_ssize_t __pyx_nargs;
  CYTHON_UNUSED PyObject *const *__pyx_kwvalues;
  int __pyx_r;
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("__init__ (wrapper)", 0);
  #if CYTHON_ASSUME_SAFE_SIZE
  __pyx_nargs = PyTuple_GET_SIZE(__pyx_args);
  #else
  __pyx_nargs = PyTuple_Size(__pyx_args); if (unlikely(__pyx_nargs < 0)) return -1;
  #endif
  __pyx_kwvalues = __Pyx_KwValues_VARARGS(__pyx_args, __pyx_nargs);
  {
    PyObject ** const __pyx_pyargnames[] = {&__pyx_mstate_global->__pyx_n_u_context,0};
  PyObject* values[1] = {0};
    const Py_ssize_t __pyx_kwds_len = (__pyx_kwds) ? __Pyx_NumKwargs_VARARGS(__pyx_kwds) : 0;
    if (unlikely(__pyx_kwds_len) < 0) __PYX_ERR(0, 302, __pyx_L3_error)
    if (__pyx_kwds_len > 0) {
      switch (__pyx_nargs) {
        case  1:
        values[0] = __Pyx_ArgRef_VARARGS(__pyx_args, 0);
        if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[0])) __PYX_ERR(0, 302, __pyx_L3_error)
        CYTHON_FALLTHROUGH;
        case  0: break;
        default: goto __pyx_L5_argtuple_error;
      }
      const Py_ssize_t kwd_pos_args = __pyx_nargs;
      if (__Pyx_ParseKeywords(__pyx_kwds, __pyx_kwvalues, __pyx_pyargnames, 0, values, kwd_pos_args, __pyx_kwds_len, "__init__", 0) < (0)) __PYX_ERR(0, 302, __pyx_L3_error)
      for (Py_ssize_t i = __pyx_nargs; i < 1; i++) {
        if (unlikely(!values[i])) { __Pyx_RaiseArgtupleInvalid("__init__", 1, 1, 1, i); __PYX_ERR(0, 302, __pyx_L3_error) }
      }
    } else if (unlikely(__pyx_nargs != 1)) {
      goto __pyx_L5_argtuple_error;
    } else {
      values[0] = __Pyx_ArgRef_VARARGS(__pyx_args, 0);
      if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[0])) __PYX_ERR(0, 302, __pyx_L3_error)
    }
    __pyx_v_context = values[0];
  }
  goto __pyx_L6_skip;
  __pyx_L5_argtuple_error:;
  __Pyx_RaiseArgtupleInvalid("__init__", 1, 1, 1, __pyx_nargs); __PYX_ERR(0, 302, __pyx_L3_error)
  __pyx_L6_skip:;
  goto __pyx_L4_argument_unpacking_done;
  __pyx_L3_error:;
  for (Py_ssize_t __pyx_temp=0; __pyx_temp < (Py_ssize_t)(sizeof(values)/sizeof(values[0])); ++__pyx_temp) {
    Py_XDECREF(values[__pyx_temp]);
  }
  __Pyx_AddTraceback("Cython.Compiler.Visitor.CythonTransform.__init__", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __Pyx_RefNannyFinishContext();
  return -1;
  __pyx_L4_argument_unpacking_done:;
  __pyx_r = __pyx_pf_6Cython_8Compiler_7Visitor_15CythonTransform___init__(((struct __pyx_obj_6Cython_8Compiler_7Visitor_CythonTransform *)__pyx_v_self), __pyx_v_context);
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

static int __pyx_pf_6Cython_8Compiler_7Visitor_15CythonTransform___init__(struct __pyx_obj_6Cython_8Compiler_7Visitor_CythonTransform *__pyx_v_self, PyObject *__pyx_v_context) {
  int __pyx_r;
/* … */
  /* function exit code */
  __pyx_r = 0;
  goto __pyx_L0;
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_t_1);
  __Pyx_XDECREF(__pyx_t_2);
  __Pyx_XDECREF(__pyx_t_3);
  __Pyx_XDECREF(__pyx_t_4);
  __Pyx_AddTraceback("Cython.Compiler.Visitor.CythonTransform.__init__", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_r = -1;
  __pyx_L0:;
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}
```

</details>

L303  🟠  (score=9)
```python
        super().__init__()
```
<details><summary>Show generated C (score=9)</summary>

```c
  __pyx_t_4 = NULL;
  __pyx_t_5 = 1;
  {
    PyObject *__pyx_callargs[3] = {__pyx_t_4, ((PyObject *)__pyx_mstate_global->__pyx_ptype_6Cython_8Compiler_7Visitor_CythonTransform), ((PyObject *)__pyx_v_self)};
    __pyx_t_3 = __Pyx_PyObject_FastCall((PyObject*)__pyx_builtin_super, __pyx_callargs+__pyx_t_5, (3-__pyx_t_5) | (__pyx_t_5*__Pyx_PY_VECTORCALL_ARGUMENTS_OFFSET));
    __Pyx_XDECREF(__pyx_t_4); __pyx_t_4 = 0;
    if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 303, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_3);
  }
  __pyx_t_2 = __pyx_t_3;
  __Pyx_INCREF(__pyx_t_2);
  __pyx_t_5 = 0;
  {
    PyObject *__pyx_callargs[2] = {__pyx_t_2, NULL};
    __pyx_t_1 = __Pyx_PyObject_FastCallMethod((PyObject*)__pyx_mstate_global->__pyx_n_u_init, __pyx_callargs+__pyx_t_5, (1-__pyx_t_5) | (1*__Pyx_PY_VECTORCALL_ARGUMENTS_OFFSET));
    __Pyx_XDECREF(__pyx_t_2); __pyx_t_2 = 0;
    __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
    if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 303, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_1);
  }
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
```

</details>

L304  🟡  (score=2)
```python
        self.context = context
```
<details><summary>Show generated C (score=2)</summary>

```c
  __Pyx_INCREF(__pyx_v_context);
  __Pyx_GIVEREF(__pyx_v_context);
  __Pyx_GOTREF(__pyx_v_self->context);
  __Pyx_DECREF(__pyx_v_self->context);
  __pyx_v_self->context = __pyx_v_context;
```

</details>

L305  ⚪  (score=0)
```python
```
L306  🔴  (score=30)
```python
    def __call__(self, node):
```
<details><summary>Show generated C (score=30)</summary>

```c
/* Python wrapper */
static PyObject *__pyx_pw_6Cython_8Compiler_7Visitor_15CythonTransform_3__call__(PyObject *__pyx_v_self, PyObject *__pyx_args, PyObject *__pyx_kwds); /*proto*/
PyDoc_STRVAR(__pyx_doc_6Cython_8Compiler_7Visitor_15CythonTransform_2__call__, "File: Cython/Compiler/Visitor.py (starting at line 306)");
#if CYTHON_UPDATE_DESCRIPTOR_DOC
struct wrapperbase __pyx_wrapperbase_6Cython_8Compiler_7Visitor_15CythonTransform_2__call__;
#endif
static PyObject *__pyx_pw_6Cython_8Compiler_7Visitor_15CythonTransform_3__call__(PyObject *__pyx_v_self, PyObject *__pyx_args, PyObject *__pyx_kwds) {
  PyObject *__pyx_v_node = 0;
  CYTHON_UNUSED Py_ssize_t __pyx_nargs;
  CYTHON_UNUSED PyObject *const *__pyx_kwvalues;
  PyObject *__pyx_r = 0;
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("__call__ (wrapper)", 0);
  #if CYTHON_ASSUME_SAFE_SIZE
  __pyx_nargs = PyTuple_GET_SIZE(__pyx_args);
  #else
  __pyx_nargs = PyTuple_Size(__pyx_args); if (unlikely(__pyx_nargs < 0)) return NULL;
  #endif
  __pyx_kwvalues = __Pyx_KwValues_VARARGS(__pyx_args, __pyx_nargs);
  {
    PyObject ** const __pyx_pyargnames[] = {&__pyx_mstate_global->__pyx_n_u_node,0};
  PyObject* values[1] = {0};
    const Py_ssize_t __pyx_kwds_len = (__pyx_kwds) ? __Pyx_NumKwargs_VARARGS(__pyx_kwds) : 0;
    if (unlikely(__pyx_kwds_len) < 0) __PYX_ERR(0, 306, __pyx_L3_error)
    if (__pyx_kwds_len > 0) {
      switch (__pyx_nargs) {
        case  1:
        values[0] = __Pyx_ArgRef_VARARGS(__pyx_args, 0);
        if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[0])) __PYX_ERR(0, 306, __pyx_L3_error)
        CYTHON_FALLTHROUGH;
        case  0: break;
        default: goto __pyx_L5_argtuple_error;
      }
      const Py_ssize_t kwd_pos_args = __pyx_nargs;
      if (__Pyx_ParseKeywords(__pyx_kwds, __pyx_kwvalues, __pyx_pyargnames, 0, values, kwd_pos_args, __pyx_kwds_len, "__call__", 0) < (0)) __PYX_ERR(0, 306, __pyx_L3_error)
      for (Py_ssize_t i = __pyx_nargs; i < 1; i++) {
        if (unlikely(!values[i])) { __Pyx_RaiseArgtupleInvalid("__call__", 1, 1, 1, i); __PYX_ERR(0, 306, __pyx_L3_error) }
      }
    } else if (unlikely(__pyx_nargs != 1)) {
      goto __pyx_L5_argtuple_error;
    } else {
      values[0] = __Pyx_ArgRef_VARARGS(__pyx_args, 0);
      if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[0])) __PYX_ERR(0, 306, __pyx_L3_error)
    }
    __pyx_v_node = values[0];
  }
  goto __pyx_L6_skip;
  __pyx_L5_argtuple_error:;
  __Pyx_RaiseArgtupleInvalid("__call__", 1, 1, 1, __pyx_nargs); __PYX_ERR(0, 306, __pyx_L3_error)
  __pyx_L6_skip:;
  goto __pyx_L4_argument_unpacking_done;
  __pyx_L3_error:;
  for (Py_ssize_t __pyx_temp=0; __pyx_temp < (Py_ssize_t)(sizeof(values)/sizeof(values[0])); ++__pyx_temp) {
    Py_XDECREF(values[__pyx_temp]);
  }
  __Pyx_AddTraceback("Cython.Compiler.Visitor.CythonTransform.__call__", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __Pyx_RefNannyFinishContext();
  return NULL;
  __pyx_L4_argument_unpacking_done:;
  __pyx_r = __pyx_pf_6Cython_8Compiler_7Visitor_15CythonTransform_2__call__(((struct __pyx_obj_6Cython_8Compiler_7Visitor_CythonTransform *)__pyx_v_self), __pyx_v_node);
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

static PyObject *__pyx_pf_6Cython_8Compiler_7Visitor_15CythonTransform_2__call__(struct __pyx_obj_6Cython_8Compiler_7Visitor_CythonTransform *__pyx_v_self, PyObject *__pyx_v_node) {
  PyObject *__pyx_v_ModuleNode = NULL;
  PyObject *__pyx_r = NULL;
/* … */
  /* function exit code */
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_t_1);
  __Pyx_XDECREF(__pyx_t_4);
  __Pyx_XDECREF(__pyx_t_6);
  __Pyx_XDECREF(__pyx_t_7);
  __Pyx_AddTraceback("Cython.Compiler.Visitor.CythonTransform.__call__", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_r = NULL;
  __pyx_L0:;
  __Pyx_XDECREF(__pyx_v_ModuleNode);
  __Pyx_XGIVEREF(__pyx_r);
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}
```

</details>

L307  🟠  (score=7)
```python
        from .ModuleNode import ModuleNode
```
<details><summary>Show generated C (score=7)</summary>

```c
  {
    PyObject* const __pyx_imported_names[] = {__pyx_mstate_global->__pyx_n_u_ModuleNode};
    __pyx_t_2 = __Pyx_Import(__pyx_mstate_global->__pyx_n_u_ModuleNode, __pyx_imported_names, 1, __pyx_mstate_global->__pyx_kp_u_Cython_Compiler_ModuleNode, 1); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 307, __pyx_L1_error)
  }
  __pyx_t_1 = __pyx_t_2;
  __Pyx_GOTREF(__pyx_t_1);
  {
    PyObject* const __pyx_imported_names[] = {__pyx_mstate_global->__pyx_n_u_ModuleNode};
    for (__pyx_t_3=0; __pyx_t_3 < 1; __pyx_t_3++) {
      __pyx_t_4 = __Pyx_ImportFrom(__pyx_t_1, __pyx_imported_names[__pyx_t_3]); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 307, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_4);
      switch (__pyx_t_3) {
        case 0:
        __Pyx_INCREF(__pyx_t_4);
        __pyx_v_ModuleNode = __pyx_t_4;
        break;
      }
      __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
    }
  }
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
```

</details>

L308  🟠  (score=5)
```python
        if isinstance(node, ModuleNode):
```
<details><summary>Show generated C (score=5)</summary>

```c
  __pyx_t_5 = PyObject_IsInstance(__pyx_v_node, __pyx_v_ModuleNode); if (unlikely(__pyx_t_5 == ((int)-1))) __PYX_ERR(0, 308, __pyx_L1_error)
  if (__pyx_t_5) {
/* … */
  }
```

</details>

L309  🟡  (score=3)
```python
            self.current_directives = node.directives
```
<details><summary>Show generated C (score=3)</summary>

```c
    __pyx_t_1 = __Pyx_PyObject_GetAttrStr(__pyx_v_node, __pyx_mstate_global->__pyx_n_u_directives); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 309, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_1);
    __Pyx_GIVEREF(__pyx_t_1);
    __Pyx_GOTREF(__pyx_v_self->current_directives);
    __Pyx_DECREF(__pyx_v_self->current_directives);
    __pyx_v_self->current_directives = __pyx_t_1;
    __pyx_t_1 = 0;
```

</details>

L310  🟠  (score=9)
```python
        return super().__call__(node)
```
<details><summary>Show generated C (score=9)</summary>

```c
  __Pyx_XDECREF(__pyx_r);
  __pyx_t_7 = NULL;
  __pyx_t_8 = 1;
  {
    PyObject *__pyx_callargs[3] = {__pyx_t_7, ((PyObject *)__pyx_mstate_global->__pyx_ptype_6Cython_8Compiler_7Visitor_CythonTransform), ((PyObject *)__pyx_v_self)};
    __pyx_t_6 = __Pyx_PyObject_FastCall((PyObject*)__pyx_builtin_super, __pyx_callargs+__pyx_t_8, (3-__pyx_t_8) | (__pyx_t_8*__Pyx_PY_VECTORCALL_ARGUMENTS_OFFSET));
    __Pyx_XDECREF(__pyx_t_7); __pyx_t_7 = 0;
    if (unlikely(!__pyx_t_6)) __PYX_ERR(0, 310, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_6);
  }
  __pyx_t_4 = __pyx_t_6;
  __Pyx_INCREF(__pyx_t_4);
  __pyx_t_8 = 0;
  {
    PyObject *__pyx_callargs[2] = {__pyx_t_4, __pyx_v_node};
    __pyx_t_1 = __Pyx_PyObject_FastCallMethod((PyObject*)__pyx_mstate_global->__pyx_n_u_call, __pyx_callargs+__pyx_t_8, (2-__pyx_t_8) | (1*__Pyx_PY_VECTORCALL_ARGUMENTS_OFFSET));
    __Pyx_XDECREF(__pyx_t_4); __pyx_t_4 = 0;
    __Pyx_DECREF(__pyx_t_6); __pyx_t_6 = 0;
    if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 310, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_1);
  }
  __pyx_r = __pyx_t_1;
  __pyx_t_1 = 0;
  goto __pyx_L0;
```

</details>

L311  ⚪  (score=0)
```python
```
L312  🔴  (score=37)
```python
    def visit_CompilerDirectivesNode(self, node):
```
<details><summary>Show generated C (score=37)</summary>

```c
/* Python wrapper */
static PyObject *__pyx_pw_6Cython_8Compiler_7Visitor_15CythonTransform_5visit_CompilerDirectivesNode(PyObject *__pyx_v_self, 
#if CYTHON_METH_FASTCALL
PyObject *const *__pyx_args, Py_ssize_t __pyx_nargs, PyObject *__pyx_kwds
#else
PyObject *__pyx_args, PyObject *__pyx_kwds
#endif
); /*proto*/
PyDoc_STRVAR(__pyx_doc_6Cython_8Compiler_7Visitor_15CythonTransform_4visit_CompilerDirectivesNode, "File: Cython/Compiler/Visitor.py (starting at line 312)");
static PyMethodDef __pyx_mdef_6Cython_8Compiler_7Visitor_15CythonTransform_5visit_CompilerDirectivesNode = {"visit_CompilerDirectivesNode", (PyCFunction)(void(*)(void))(__Pyx_PyCFunction_FastCallWithKeywords)__pyx_pw_6Cython_8Compiler_7Visitor_15CythonTransform_5visit_CompilerDirectivesNode, __Pyx_METH_FASTCALL|METH_KEYWORDS, __pyx_doc_6Cython_8Compiler_7Visitor_15CythonTransform_4visit_CompilerDirectivesNode};
static PyObject *__pyx_pw_6Cython_8Compiler_7Visitor_15CythonTransform_5visit_CompilerDirectivesNode(PyObject *__pyx_v_self, 
#if CYTHON_METH_FASTCALL
PyObject *const *__pyx_args, Py_ssize_t __pyx_nargs, PyObject *__pyx_kwds
#else
PyObject *__pyx_args, PyObject *__pyx_kwds
#endif
) {
  PyObject *__pyx_v_node = 0;
  #if !CYTHON_METH_FASTCALL
  CYTHON_UNUSED Py_ssize_t __pyx_nargs;
  #endif
  CYTHON_UNUSED PyObject *const *__pyx_kwvalues;
  PyObject *__pyx_r = 0;
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("visit_CompilerDirectivesNode (wrapper)", 0);
  #if !CYTHON_METH_FASTCALL
  #if CYTHON_ASSUME_SAFE_SIZE
  __pyx_nargs = PyTuple_GET_SIZE(__pyx_args);
  #else
  __pyx_nargs = PyTuple_Size(__pyx_args); if (unlikely(__pyx_nargs < 0)) return NULL;
  #endif
  #endif
  __pyx_kwvalues = __Pyx_KwValues_FASTCALL(__pyx_args, __pyx_nargs);
  {
    PyObject ** const __pyx_pyargnames[] = {&__pyx_mstate_global->__pyx_n_u_node,0};
  PyObject* values[1] = {0};
    const Py_ssize_t __pyx_kwds_len = (__pyx_kwds) ? __Pyx_NumKwargs_FASTCALL(__pyx_kwds) : 0;
    if (unlikely(__pyx_kwds_len) < 0) __PYX_ERR(0, 312, __pyx_L3_error)
    if (__pyx_kwds_len > 0) {
      switch (__pyx_nargs) {
        case  1:
        values[0] = __Pyx_ArgRef_FASTCALL(__pyx_args, 0);
        if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[0])) __PYX_ERR(0, 312, __pyx_L3_error)
        CYTHON_FALLTHROUGH;
        case  0: break;
        default: goto __pyx_L5_argtuple_error;
      }
      const Py_ssize_t kwd_pos_args = __pyx_nargs;
      if (__Pyx_ParseKeywords(__pyx_kwds, __pyx_kwvalues, __pyx_pyargnames, 0, values, kwd_pos_args, __pyx_kwds_len, "visit_CompilerDirectivesNode", 0) < (0)) __PYX_ERR(0, 312, __pyx_L3_error)
      for (Py_ssize_t i = __pyx_nargs; i < 1; i++) {
        if (unlikely(!values[i])) { __Pyx_RaiseArgtupleInvalid("visit_CompilerDirectivesNode", 1, 1, 1, i); __PYX_ERR(0, 312, __pyx_L3_error) }
      }
    } else if (unlikely(__pyx_nargs != 1)) {
      goto __pyx_L5_argtuple_error;
    } else {
      values[0] = __Pyx_ArgRef_FASTCALL(__pyx_args, 0);
      if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[0])) __PYX_ERR(0, 312, __pyx_L3_error)
    }
    __pyx_v_node = values[0];
  }
  goto __pyx_L6_skip;
  __pyx_L5_argtuple_error:;
  __Pyx_RaiseArgtupleInvalid("visit_CompilerDirectivesNode", 1, 1, 1, __pyx_nargs); __PYX_ERR(0, 312, __pyx_L3_error)
  __pyx_L6_skip:;
  goto __pyx_L4_argument_unpacking_done;
  __pyx_L3_error:;
  for (Py_ssize_t __pyx_temp=0; __pyx_temp < (Py_ssize_t)(sizeof(values)/sizeof(values[0])); ++__pyx_temp) {
    Py_XDECREF(values[__pyx_temp]);
  }
  __Pyx_AddTraceback("Cython.Compiler.Visitor.CythonTransform.visit_CompilerDirectivesNode", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __Pyx_RefNannyFinishContext();
  return NULL;
  __pyx_L4_argument_unpacking_done:;
  __pyx_r = __pyx_pf_6Cython_8Compiler_7Visitor_15CythonTransform_4visit_CompilerDirectivesNode(((struct __pyx_obj_6Cython_8Compiler_7Visitor_CythonTransform *)__pyx_v_self), __pyx_v_node);
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

static PyObject *__pyx_pf_6Cython_8Compiler_7Visitor_15CythonTransform_4visit_CompilerDirectivesNode(struct __pyx_obj_6Cython_8Compiler_7Visitor_CythonTransform *__pyx_v_self, PyObject *__pyx_v_node) {
  PyObject *__pyx_v_old = NULL;
  PyObject *__pyx_r = NULL;
/* … */
  /* function exit code */
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_t_1);
  __Pyx_AddTraceback("Cython.Compiler.Visitor.CythonTransform.visit_CompilerDirectivesNode", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_r = NULL;
  __pyx_L0:;
  __Pyx_XDECREF(__pyx_v_old);
  __Pyx_XGIVEREF(__pyx_r);
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}
/* … */
  __pyx_t_2 = __Pyx_CyFunction_New(&__pyx_mdef_6Cython_8Compiler_7Visitor_15CythonTransform_5visit_CompilerDirectivesNode, __Pyx_CYFUNCTION_CCLASS, __pyx_mstate_global->__pyx_n_u_CythonTransform_visit_CompilerDi, NULL, __pyx_mstate_global->__pyx_n_u_Cython_Compiler_Visitor, __pyx_mstate_global->__pyx_d, ((PyObject *)__pyx_mstate_global->__pyx_codeobj_tab[11])); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 312, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  #if CYTHON_COMPILING_IN_CPYTHON && PY_VERSION_HEX >= 0x030E0000
  PyUnstable_Object_EnableDeferredRefcount(__pyx_t_2);
  #endif
  if (__Pyx_SetItemOnTypeDict(__pyx_mstate_global->__pyx_ptype_6Cython_8Compiler_7Visitor_CythonTransform, __pyx_mstate_global->__pyx_n_u_visit_CompilerDirectivesNode, __pyx_t_2) < (0)) __PYX_ERR(0, 312, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
```

</details>

L313  🟡  (score=1)
```python
        old = self.current_directives
```
<details><summary>Show generated C (score=1)</summary>

```c
  __pyx_t_1 = __pyx_v_self->current_directives;
  __Pyx_INCREF(__pyx_t_1);
  __pyx_v_old = __pyx_t_1;
  __pyx_t_1 = 0;
```

</details>

L314  🟡  (score=3)
```python
        self.current_directives = node.directives
```
<details><summary>Show generated C (score=3)</summary>

```c
  __pyx_t_1 = __Pyx_PyObject_GetAttrStr(__pyx_v_node, __pyx_mstate_global->__pyx_n_u_directives); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 314, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_GIVEREF(__pyx_t_1);
  __Pyx_GOTREF(__pyx_v_self->current_directives);
  __Pyx_DECREF(__pyx_v_self->current_directives);
  __pyx_v_self->current_directives = __pyx_t_1;
  __pyx_t_1 = 0;
```

</details>

L315  🟡  (score=1)
```python
        self._process_children(node)
```
<details><summary>Show generated C (score=1)</summary>

```c
  __pyx_t_1 = ((struct __pyx_vtabstruct_6Cython_8Compiler_7Visitor_CythonTransform *)__pyx_v_self->__pyx_base.__pyx_base.__pyx_vtab)->__pyx_base._process_children(((struct __pyx_obj_6Cython_8Compiler_7Visitor_VisitorTransform *)__pyx_v_self), __pyx_v_node, NULL); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 315, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
```

</details>

L316  🟡  (score=2)
```python
        self.current_directives = old
```
<details><summary>Show generated C (score=2)</summary>

```c
  __Pyx_INCREF(__pyx_v_old);
  __Pyx_GIVEREF(__pyx_v_old);
  __Pyx_GOTREF(__pyx_v_self->current_directives);
  __Pyx_DECREF(__pyx_v_self->current_directives);
  __pyx_v_self->current_directives = __pyx_v_old;
```

</details>

L317  🟡  (score=2)
```python
        return node
```
<details><summary>Show generated C (score=2)</summary>

```c
  __Pyx_XDECREF(__pyx_r);
  __Pyx_INCREF(__pyx_v_node);
  __pyx_r = __pyx_v_node;
  goto __pyx_L0;
```

</details>

L318  ⚪  (score=0)
```python
```
L319  🔴  (score=36)
```python
    def visit_Node(self, node):
```
<details><summary>Show generated C (score=36)</summary>

```c
/* Python wrapper */
static PyObject *__pyx_pw_6Cython_8Compiler_7Visitor_15CythonTransform_7visit_Node(PyObject *__pyx_v_self, 
#if CYTHON_METH_FASTCALL
PyObject *const *__pyx_args, Py_ssize_t __pyx_nargs, PyObject *__pyx_kwds
#else
PyObject *__pyx_args, PyObject *__pyx_kwds
#endif
); /*proto*/
PyDoc_STRVAR(__pyx_doc_6Cython_8Compiler_7Visitor_15CythonTransform_6visit_Node, "File: Cython/Compiler/Visitor.py (starting at line 319)");
static PyMethodDef __pyx_mdef_6Cython_8Compiler_7Visitor_15CythonTransform_7visit_Node = {"visit_Node", (PyCFunction)(void(*)(void))(__Pyx_PyCFunction_FastCallWithKeywords)__pyx_pw_6Cython_8Compiler_7Visitor_15CythonTransform_7visit_Node, __Pyx_METH_FASTCALL|METH_KEYWORDS, __pyx_doc_6Cython_8Compiler_7Visitor_15CythonTransform_6visit_Node};
static PyObject *__pyx_pw_6Cython_8Compiler_7Visitor_15CythonTransform_7visit_Node(PyObject *__pyx_v_self, 
#if CYTHON_METH_FASTCALL
PyObject *const *__pyx_args, Py_ssize_t __pyx_nargs, PyObject *__pyx_kwds
#else
PyObject *__pyx_args, PyObject *__pyx_kwds
#endif
) {
  PyObject *__pyx_v_node = 0;
  #if !CYTHON_METH_FASTCALL
  CYTHON_UNUSED Py_ssize_t __pyx_nargs;
  #endif
  CYTHON_UNUSED PyObject *const *__pyx_kwvalues;
  PyObject *__pyx_r = 0;
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("visit_Node (wrapper)", 0);
  #if !CYTHON_METH_FASTCALL
  #if CYTHON_ASSUME_SAFE_SIZE
  __pyx_nargs = PyTuple_GET_SIZE(__pyx_args);
  #else
  __pyx_nargs = PyTuple_Size(__pyx_args); if (unlikely(__pyx_nargs < 0)) return NULL;
  #endif
  #endif
  __pyx_kwvalues = __Pyx_KwValues_FASTCALL(__pyx_args, __pyx_nargs);
  {
    PyObject ** const __pyx_pyargnames[] = {&__pyx_mstate_global->__pyx_n_u_node,0};
  PyObject* values[1] = {0};
    const Py_ssize_t __pyx_kwds_len = (__pyx_kwds) ? __Pyx_NumKwargs_FASTCALL(__pyx_kwds) : 0;
    if (unlikely(__pyx_kwds_len) < 0) __PYX_ERR(0, 319, __pyx_L3_error)
    if (__pyx_kwds_len > 0) {
      switch (__pyx_nargs) {
        case  1:
        values[0] = __Pyx_ArgRef_FASTCALL(__pyx_args, 0);
        if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[0])) __PYX_ERR(0, 319, __pyx_L3_error)
        CYTHON_FALLTHROUGH;
        case  0: break;
        default: goto __pyx_L5_argtuple_error;
      }
      const Py_ssize_t kwd_pos_args = __pyx_nargs;
      if (__Pyx_ParseKeywords(__pyx_kwds, __pyx_kwvalues, __pyx_pyargnames, 0, values, kwd_pos_args, __pyx_kwds_len, "visit_Node", 0) < (0)) __PYX_ERR(0, 319, __pyx_L3_error)
      for (Py_ssize_t i = __pyx_nargs; i < 1; i++) {
        if (unlikely(!values[i])) { __Pyx_RaiseArgtupleInvalid("visit_Node", 1, 1, 1, i); __PYX_ERR(0, 319, __pyx_L3_error) }
      }
    } else if (unlikely(__pyx_nargs != 1)) {
      goto __pyx_L5_argtuple_error;
    } else {
      values[0] = __Pyx_ArgRef_FASTCALL(__pyx_args, 0);
      if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[0])) __PYX_ERR(0, 319, __pyx_L3_error)
    }
    __pyx_v_node = values[0];
  }
  goto __pyx_L6_skip;
  __pyx_L5_argtuple_error:;
  __Pyx_RaiseArgtupleInvalid("visit_Node", 1, 1, 1, __pyx_nargs); __PYX_ERR(0, 319, __pyx_L3_error)
  __pyx_L6_skip:;
  goto __pyx_L4_argument_unpacking_done;
  __pyx_L3_error:;
  for (Py_ssize_t __pyx_temp=0; __pyx_temp < (Py_ssize_t)(sizeof(values)/sizeof(values[0])); ++__pyx_temp) {
    Py_XDECREF(values[__pyx_temp]);
  }
  __Pyx_AddTraceback("Cython.Compiler.Visitor.CythonTransform.visit_Node", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __Pyx_RefNannyFinishContext();
  return NULL;
  __pyx_L4_argument_unpacking_done:;
  __pyx_r = __pyx_pf_6Cython_8Compiler_7Visitor_15CythonTransform_6visit_Node(((struct __pyx_obj_6Cython_8Compiler_7Visitor_CythonTransform *)__pyx_v_self), __pyx_v_node);
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

static PyObject *__pyx_pf_6Cython_8Compiler_7Visitor_15CythonTransform_6visit_Node(struct __pyx_obj_6Cython_8Compiler_7Visitor_CythonTransform *__pyx_v_self, PyObject *__pyx_v_node) {
  PyObject *__pyx_r = NULL;
/* … */
  /* function exit code */
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_t_1);
  __Pyx_AddTraceback("Cython.Compiler.Visitor.CythonTransform.visit_Node", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_r = NULL;
  __pyx_L0:;
  __Pyx_XGIVEREF(__pyx_r);
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}
/* … */
  __pyx_t_2 = __Pyx_CyFunction_New(&__pyx_mdef_6Cython_8Compiler_7Visitor_15CythonTransform_7visit_Node, __Pyx_CYFUNCTION_CCLASS, __pyx_mstate_global->__pyx_n_u_CythonTransform_visit_Node, NULL, __pyx_mstate_global->__pyx_n_u_Cython_Compiler_Visitor, __pyx_mstate_global->__pyx_d, ((PyObject *)__pyx_mstate_global->__pyx_codeobj_tab[12])); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 319, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  #if CYTHON_COMPILING_IN_CPYTHON && PY_VERSION_HEX >= 0x030E0000
  PyUnstable_Object_EnableDeferredRefcount(__pyx_t_2);
  #endif
  if (__Pyx_SetItemOnTypeDict(__pyx_mstate_global->__pyx_ptype_6Cython_8Compiler_7Visitor_CythonTransform, __pyx_mstate_global->__pyx_n_u_visit_Node, __pyx_t_2) < (0)) __PYX_ERR(0, 319, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
```

</details>

L320  🟡  (score=1)
```python
        self._process_children(node)
```
<details><summary>Show generated C (score=1)</summary>

```c
  __pyx_t_1 = ((struct __pyx_vtabstruct_6Cython_8Compiler_7Visitor_CythonTransform *)__pyx_v_self->__pyx_base.__pyx_base.__pyx_vtab)->__pyx_base._process_children(((struct __pyx_obj_6Cython_8Compiler_7Visitor_VisitorTransform *)__pyx_v_self), __pyx_v_node, NULL); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 320, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
```

</details>

L321  🟡  (score=2)
```python
        return node
```
<details><summary>Show generated C (score=2)</summary>

```c
  __Pyx_XDECREF(__pyx_r);
  __Pyx_INCREF(__pyx_v_node);
  __pyx_r = __pyx_v_node;
  goto __pyx_L0;
```

</details>

L322  ⚪  (score=0)
```python
```
L323  ⚪  (score=0)
```python
```
L324  ⚪  (score=0)
```python
class ScopeTrackingTransform(CythonTransform):
```
<details><summary>Show generated C (score=0)</summary>

```c
struct __pyx_vtabstruct_6Cython_8Compiler_7Visitor_ScopeTrackingTransform {
  struct __pyx_vtabstruct_6Cython_8Compiler_7Visitor_CythonTransform __pyx_base;
  PyObject *(*visit_scope)(struct __pyx_obj_6Cython_8Compiler_7Visitor_ScopeTrackingTransform *, PyObject *, PyObject *);
};
static struct __pyx_vtabstruct_6Cython_8Compiler_7Visitor_ScopeTrackingTransform *__pyx_vtabptr_6Cython_8Compiler_7Visitor_ScopeTrackingTransform;

```

</details>

L325  ⚪  (score=0)
```python
    # Keeps track of type of scopes
```
L326  ⚪  (score=0)
```python
    #scope_type: can be either of 'module', 'function', 'cclass', 'pyclass', 'struct'
```
L327  ⚪  (score=0)
```python
    #scope_node: the node that owns the current scope
```
L328  ⚪  (score=0)
```python
```
L329  🔴  (score=36)
```python
    def visit_ModuleNode(self, node):
```
<details><summary>Show generated C (score=36)</summary>

```c
/* Python wrapper */
static PyObject *__pyx_pw_6Cython_8Compiler_7Visitor_22ScopeTrackingTransform_1visit_ModuleNode(PyObject *__pyx_v_self, 
#if CYTHON_METH_FASTCALL
PyObject *const *__pyx_args, Py_ssize_t __pyx_nargs, PyObject *__pyx_kwds
#else
PyObject *__pyx_args, PyObject *__pyx_kwds
#endif
); /*proto*/
PyDoc_STRVAR(__pyx_doc_6Cython_8Compiler_7Visitor_22ScopeTrackingTransform_visit_ModuleNode, "File: Cython/Compiler/Visitor.py (starting at line 329)");
static PyMethodDef __pyx_mdef_6Cython_8Compiler_7Visitor_22ScopeTrackingTransform_1visit_ModuleNode = {"visit_ModuleNode", (PyCFunction)(void(*)(void))(__Pyx_PyCFunction_FastCallWithKeywords)__pyx_pw_6Cython_8Compiler_7Visitor_22ScopeTrackingTransform_1visit_ModuleNode, __Pyx_METH_FASTCALL|METH_KEYWORDS, __pyx_doc_6Cython_8Compiler_7Visitor_22ScopeTrackingTransform_visit_ModuleNode};
static PyObject *__pyx_pw_6Cython_8Compiler_7Visitor_22ScopeTrackingTransform_1visit_ModuleNode(PyObject *__pyx_v_self, 
#if CYTHON_METH_FASTCALL
PyObject *const *__pyx_args, Py_ssize_t __pyx_nargs, PyObject *__pyx_kwds
#else
PyObject *__pyx_args, PyObject *__pyx_kwds
#endif
) {
  PyObject *__pyx_v_node = 0;
  #if !CYTHON_METH_FASTCALL
  CYTHON_UNUSED Py_ssize_t __pyx_nargs;
  #endif
  CYTHON_UNUSED PyObject *const *__pyx_kwvalues;
  PyObject *__pyx_r = 0;
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("visit_ModuleNode (wrapper)", 0);
  #if !CYTHON_METH_FASTCALL
  #if CYTHON_ASSUME_SAFE_SIZE
  __pyx_nargs = PyTuple_GET_SIZE(__pyx_args);
  #else
  __pyx_nargs = PyTuple_Size(__pyx_args); if (unlikely(__pyx_nargs < 0)) return NULL;
  #endif
  #endif
  __pyx_kwvalues = __Pyx_KwValues_FASTCALL(__pyx_args, __pyx_nargs);
  {
    PyObject ** const __pyx_pyargnames[] = {&__pyx_mstate_global->__pyx_n_u_node,0};
  PyObject* values[1] = {0};
    const Py_ssize_t __pyx_kwds_len = (__pyx_kwds) ? __Pyx_NumKwargs_FASTCALL(__pyx_kwds) : 0;
    if (unlikely(__pyx_kwds_len) < 0) __PYX_ERR(0, 329, __pyx_L3_error)
    if (__pyx_kwds_len > 0) {
      switch (__pyx_nargs) {
        case  1:
        values[0] = __Pyx_ArgRef_FASTCALL(__pyx_args, 0);
        if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[0])) __PYX_ERR(0, 329, __pyx_L3_error)
        CYTHON_FALLTHROUGH;
        case  0: break;
        default: goto __pyx_L5_argtuple_error;
      }
      const Py_ssize_t kwd_pos_args = __pyx_nargs;
      if (__Pyx_ParseKeywords(__pyx_kwds, __pyx_kwvalues, __pyx_pyargnames, 0, values, kwd_pos_args, __pyx_kwds_len, "visit_ModuleNode", 0) < (0)) __PYX_ERR(0, 329, __pyx_L3_error)
      for (Py_ssize_t i = __pyx_nargs; i < 1; i++) {
        if (unlikely(!values[i])) { __Pyx_RaiseArgtupleInvalid("visit_ModuleNode", 1, 1, 1, i); __PYX_ERR(0, 329, __pyx_L3_error) }
      }
    } else if (unlikely(__pyx_nargs != 1)) {
      goto __pyx_L5_argtuple_error;
    } else {
      values[0] = __Pyx_ArgRef_FASTCALL(__pyx_args, 0);
      if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[0])) __PYX_ERR(0, 329, __pyx_L3_error)
    }
    __pyx_v_node = values[0];
  }
  goto __pyx_L6_skip;
  __pyx_L5_argtuple_error:;
  __Pyx_RaiseArgtupleInvalid("visit_ModuleNode", 1, 1, 1, __pyx_nargs); __PYX_ERR(0, 329, __pyx_L3_error)
  __pyx_L6_skip:;
  goto __pyx_L4_argument_unpacking_done;
  __pyx_L3_error:;
  for (Py_ssize_t __pyx_temp=0; __pyx_temp < (Py_ssize_t)(sizeof(values)/sizeof(values[0])); ++__pyx_temp) {
    Py_XDECREF(values[__pyx_temp]);
  }
  __Pyx_AddTraceback("Cython.Compiler.Visitor.ScopeTrackingTransform.visit_ModuleNode", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __Pyx_RefNannyFinishContext();
  return NULL;
  __pyx_L4_argument_unpacking_done:;
  __pyx_r = __pyx_pf_6Cython_8Compiler_7Visitor_22ScopeTrackingTransform_visit_ModuleNode(((struct __pyx_obj_6Cython_8Compiler_7Visitor_ScopeTrackingTransform *)__pyx_v_self), __pyx_v_node);
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

static PyObject *__pyx_pf_6Cython_8Compiler_7Visitor_22ScopeTrackingTransform_visit_ModuleNode(struct __pyx_obj_6Cython_8Compiler_7Visitor_ScopeTrackingTransform *__pyx_v_self, PyObject *__pyx_v_node) {
  PyObject *__pyx_r = NULL;
/* … */
  /* function exit code */
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_t_1);
  __Pyx_AddTraceback("Cython.Compiler.Visitor.ScopeTrackingTransform.visit_ModuleNode", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_r = NULL;
  __pyx_L0:;
  __Pyx_XGIVEREF(__pyx_r);
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}
/* … */
  __pyx_t_2 = __Pyx_CyFunction_New(&__pyx_mdef_6Cython_8Compiler_7Visitor_22ScopeTrackingTransform_1visit_ModuleNode, __Pyx_CYFUNCTION_CCLASS, __pyx_mstate_global->__pyx_n_u_ScopeTrackingTransform_visit_Mod, NULL, __pyx_mstate_global->__pyx_n_u_Cython_Compiler_Visitor, __pyx_mstate_global->__pyx_d, ((PyObject *)__pyx_mstate_global->__pyx_codeobj_tab[15])); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 329, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  #if CYTHON_COMPILING_IN_CPYTHON && PY_VERSION_HEX >= 0x030E0000
  PyUnstable_Object_EnableDeferredRefcount(__pyx_t_2);
  #endif
  if (__Pyx_SetItemOnTypeDict(__pyx_mstate_global->__pyx_ptype_6Cython_8Compiler_7Visitor_ScopeTrackingTransform, __pyx_mstate_global->__pyx_n_u_visit_ModuleNode, __pyx_t_2) < (0)) __PYX_ERR(0, 329, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
```

</details>

L330  🟡  (score=2)
```python
        self.scope_type = 'module'
```
<details><summary>Show generated C (score=2)</summary>

```c
  __Pyx_INCREF(__pyx_mstate_global->__pyx_n_u_module);
  __Pyx_GIVEREF(__pyx_mstate_global->__pyx_n_u_module);
  __Pyx_GOTREF(__pyx_v_self->scope_type);
  __Pyx_DECREF(__pyx_v_self->scope_type);
  __pyx_v_self->scope_type = __pyx_mstate_global->__pyx_n_u_module;
```

</details>

L331  🟡  (score=2)
```python
        self.scope_node = node
```
<details><summary>Show generated C (score=2)</summary>

```c
  __Pyx_INCREF(__pyx_v_node);
  __Pyx_GIVEREF(__pyx_v_node);
  __Pyx_GOTREF(__pyx_v_self->scope_node);
  __Pyx_DECREF(__pyx_v_self->scope_node);
  __pyx_v_self->scope_node = __pyx_v_node;
```

</details>

L332  🟡  (score=1)
```python
        self._process_children(node)
```
<details><summary>Show generated C (score=1)</summary>

```c
  __pyx_t_1 = ((struct __pyx_vtabstruct_6Cython_8Compiler_7Visitor_ScopeTrackingTransform *)__pyx_v_self->__pyx_base.__pyx_base.__pyx_base.__pyx_vtab)->__pyx_base.__pyx_base._process_children(((struct __pyx_obj_6Cython_8Compiler_7Visitor_VisitorTransform *)__pyx_v_self), __pyx_v_node, NULL); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 332, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
```

</details>

L333  🟡  (score=2)
```python
        return node
```
<details><summary>Show generated C (score=2)</summary>

```c
  __Pyx_XDECREF(__pyx_r);
  __Pyx_INCREF(__pyx_v_node);
  __pyx_r = __pyx_v_node;
  goto __pyx_L0;
```

</details>

L334  ⚪  (score=0)
```python
```
L335  🟠  (score=5)
```python
    def visit_scope(self, node, scope_type):
```
<details><summary>Show generated C (score=5)</summary>

```c
static PyObject *__pyx_f_6Cython_8Compiler_7Visitor_22ScopeTrackingTransform_visit_scope(struct __pyx_obj_6Cython_8Compiler_7Visitor_ScopeTrackingTransform *__pyx_v_self, PyObject *__pyx_v_node, PyObject *__pyx_v_scope_type) {
  PyObject *__pyx_v_prev = NULL;
  PyObject *__pyx_r = NULL;
/* … */
  /* function exit code */
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_t_1);
  __Pyx_XDECREF(__pyx_t_2);
  __Pyx_AddTraceback("Cython.Compiler.Visitor.ScopeTrackingTransform.visit_scope", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_r = 0;
  __pyx_L0:;
  __Pyx_XDECREF(__pyx_v_prev);
  __Pyx_XGIVEREF(__pyx_r);
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}
```

</details>

L336  🔴  (score=11)
```python
        prev = self.scope_type, self.scope_node
```
<details><summary>Show generated C (score=11)</summary>

```c
  __pyx_t_1 = PyTuple_New(2); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 336, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_INCREF(__pyx_v_self->scope_type);
  __Pyx_GIVEREF(__pyx_v_self->scope_type);
  if (__Pyx_PyTuple_SET_ITEM(__pyx_t_1, 0, __pyx_v_self->scope_type) != (0)) __PYX_ERR(0, 336, __pyx_L1_error);
  __Pyx_INCREF(__pyx_v_self->scope_node);
  __Pyx_GIVEREF(__pyx_v_self->scope_node);
  if (__Pyx_PyTuple_SET_ITEM(__pyx_t_1, 1, __pyx_v_self->scope_node) != (0)) __PYX_ERR(0, 336, __pyx_L1_error);
  __pyx_v_prev = ((PyObject*)__pyx_t_1);
  __pyx_t_1 = 0;
```

</details>

L337  🟡  (score=2)
```python
        self.scope_type = scope_type
```
<details><summary>Show generated C (score=2)</summary>

```c
  __Pyx_INCREF(__pyx_v_scope_type);
  __Pyx_GIVEREF(__pyx_v_scope_type);
  __Pyx_GOTREF(__pyx_v_self->scope_type);
  __Pyx_DECREF(__pyx_v_self->scope_type);
  __pyx_v_self->scope_type = __pyx_v_scope_type;
```

</details>

L338  🟡  (score=2)
```python
        self.scope_node = node
```
<details><summary>Show generated C (score=2)</summary>

```c
  __Pyx_INCREF(__pyx_v_node);
  __Pyx_GIVEREF(__pyx_v_node);
  __Pyx_GOTREF(__pyx_v_self->scope_node);
  __Pyx_DECREF(__pyx_v_self->scope_node);
  __pyx_v_self->scope_node = __pyx_v_node;
```

</details>

L339  🟡  (score=1)
```python
        self._process_children(node)
```
<details><summary>Show generated C (score=1)</summary>

```c
  __pyx_t_1 = ((struct __pyx_vtabstruct_6Cython_8Compiler_7Visitor_ScopeTrackingTransform *)__pyx_v_self->__pyx_base.__pyx_base.__pyx_base.__pyx_vtab)->__pyx_base.__pyx_base._process_children(((struct __pyx_obj_6Cython_8Compiler_7Visitor_VisitorTransform *)__pyx_v_self), __pyx_v_node, NULL); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 339, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
```

</details>

L340  🔴  (score=16)
```python
        self.scope_type, self.scope_node = prev
```
<details><summary>Show generated C (score=16)</summary>

```c
  if (1) {
    PyObject* sequence = __pyx_v_prev;
    Py_ssize_t size = __Pyx_PyTuple_GET_SIZE(sequence);
    if (unlikely(size != 2)) {
      if (size > 2) __Pyx_RaiseTooManyValuesError(2);
      else if (size >= 0) __Pyx_RaiseNeedMoreValuesError(size);
      __PYX_ERR(0, 340, __pyx_L1_error)
    }
    #if CYTHON_ASSUME_SAFE_MACROS && !CYTHON_AVOID_BORROWED_REFS
    __pyx_t_1 = PyTuple_GET_ITEM(sequence, 0);
    __Pyx_INCREF(__pyx_t_1);
    __pyx_t_2 = PyTuple_GET_ITEM(sequence, 1);
    __Pyx_INCREF(__pyx_t_2);
    #else
    __pyx_t_1 = __Pyx_PySequence_ITEM(sequence, 0); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 340, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_1);
    __pyx_t_2 = __Pyx_PySequence_ITEM(sequence, 1); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 340, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_2);
    #endif
  }
  __Pyx_GIVEREF(__pyx_t_1);
  __Pyx_GOTREF(__pyx_v_self->scope_type);
  __Pyx_DECREF(__pyx_v_self->scope_type);
  __pyx_v_self->scope_type = __pyx_t_1;
  __pyx_t_1 = 0;
  __Pyx_GIVEREF(__pyx_t_2);
  __Pyx_GOTREF(__pyx_v_self->scope_node);
  __Pyx_DECREF(__pyx_v_self->scope_node);
  __pyx_v_self->scope_node = __pyx_t_2;
  __pyx_t_2 = 0;
```

</details>

L341  🟡  (score=2)
```python
        return node
```
<details><summary>Show generated C (score=2)</summary>

```c
  __Pyx_XDECREF(__pyx_r);
  __Pyx_INCREF(__pyx_v_node);
  __pyx_r = __pyx_v_node;
  goto __pyx_L0;
```

</details>

L342  ⚪  (score=0)
```python
```
L343  🔴  (score=36)
```python
    def visit_CClassDefNode(self, node):
```
<details><summary>Show generated C (score=36)</summary>

```c
/* Python wrapper */
static PyObject *__pyx_pw_6Cython_8Compiler_7Visitor_22ScopeTrackingTransform_3visit_CClassDefNode(PyObject *__pyx_v_self, 
#if CYTHON_METH_FASTCALL
PyObject *const *__pyx_args, Py_ssize_t __pyx_nargs, PyObject *__pyx_kwds
#else
PyObject *__pyx_args, PyObject *__pyx_kwds
#endif
); /*proto*/
PyDoc_STRVAR(__pyx_doc_6Cython_8Compiler_7Visitor_22ScopeTrackingTransform_2visit_CClassDefNode, "File: Cython/Compiler/Visitor.py (starting at line 343)");
static PyMethodDef __pyx_mdef_6Cython_8Compiler_7Visitor_22ScopeTrackingTransform_3visit_CClassDefNode = {"visit_CClassDefNode", (PyCFunction)(void(*)(void))(__Pyx_PyCFunction_FastCallWithKeywords)__pyx_pw_6Cython_8Compiler_7Visitor_22ScopeTrackingTransform_3visit_CClassDefNode, __Pyx_METH_FASTCALL|METH_KEYWORDS, __pyx_doc_6Cython_8Compiler_7Visitor_22ScopeTrackingTransform_2visit_CClassDefNode};
static PyObject *__pyx_pw_6Cython_8Compiler_7Visitor_22ScopeTrackingTransform_3visit_CClassDefNode(PyObject *__pyx_v_self, 
#if CYTHON_METH_FASTCALL
PyObject *const *__pyx_args, Py_ssize_t __pyx_nargs, PyObject *__pyx_kwds
#else
PyObject *__pyx_args, PyObject *__pyx_kwds
#endif
) {
  PyObject *__pyx_v_node = 0;
  #if !CYTHON_METH_FASTCALL
  CYTHON_UNUSED Py_ssize_t __pyx_nargs;
  #endif
  CYTHON_UNUSED PyObject *const *__pyx_kwvalues;
  PyObject *__pyx_r = 0;
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("visit_CClassDefNode (wrapper)", 0);
  #if !CYTHON_METH_FASTCALL
  #if CYTHON_ASSUME_SAFE_SIZE
  __pyx_nargs = PyTuple_GET_SIZE(__pyx_args);
  #else
  __pyx_nargs = PyTuple_Size(__pyx_args); if (unlikely(__pyx_nargs < 0)) return NULL;
  #endif
  #endif
  __pyx_kwvalues = __Pyx_KwValues_FASTCALL(__pyx_args, __pyx_nargs);
  {
    PyObject ** const __pyx_pyargnames[] = {&__pyx_mstate_global->__pyx_n_u_node,0};
  PyObject* values[1] = {0};
    const Py_ssize_t __pyx_kwds_len = (__pyx_kwds) ? __Pyx_NumKwargs_FASTCALL(__pyx_kwds) : 0;
    if (unlikely(__pyx_kwds_len) < 0) __PYX_ERR(0, 343, __pyx_L3_error)
    if (__pyx_kwds_len > 0) {
      switch (__pyx_nargs) {
        case  1:
        values[0] = __Pyx_ArgRef_FASTCALL(__pyx_args, 0);
        if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[0])) __PYX_ERR(0, 343, __pyx_L3_error)
        CYTHON_FALLTHROUGH;
        case  0: break;
        default: goto __pyx_L5_argtuple_error;
      }
      const Py_ssize_t kwd_pos_args = __pyx_nargs;
      if (__Pyx_ParseKeywords(__pyx_kwds, __pyx_kwvalues, __pyx_pyargnames, 0, values, kwd_pos_args, __pyx_kwds_len, "visit_CClassDefNode", 0) < (0)) __PYX_ERR(0, 343, __pyx_L3_error)
      for (Py_ssize_t i = __pyx_nargs; i < 1; i++) {
        if (unlikely(!values[i])) { __Pyx_RaiseArgtupleInvalid("visit_CClassDefNode", 1, 1, 1, i); __PYX_ERR(0, 343, __pyx_L3_error) }
      }
    } else if (unlikely(__pyx_nargs != 1)) {
      goto __pyx_L5_argtuple_error;
    } else {
      values[0] = __Pyx_ArgRef_FASTCALL(__pyx_args, 0);
      if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[0])) __PYX_ERR(0, 343, __pyx_L3_error)
    }
    __pyx_v_node = values[0];
  }
  goto __pyx_L6_skip;
  __pyx_L5_argtuple_error:;
  __Pyx_RaiseArgtupleInvalid("visit_CClassDefNode", 1, 1, 1, __pyx_nargs); __PYX_ERR(0, 343, __pyx_L3_error)
  __pyx_L6_skip:;
  goto __pyx_L4_argument_unpacking_done;
  __pyx_L3_error:;
  for (Py_ssize_t __pyx_temp=0; __pyx_temp < (Py_ssize_t)(sizeof(values)/sizeof(values[0])); ++__pyx_temp) {
    Py_XDECREF(values[__pyx_temp]);
  }
  __Pyx_AddTraceback("Cython.Compiler.Visitor.ScopeTrackingTransform.visit_CClassDefNode", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __Pyx_RefNannyFinishContext();
  return NULL;
  __pyx_L4_argument_unpacking_done:;
  __pyx_r = __pyx_pf_6Cython_8Compiler_7Visitor_22ScopeTrackingTransform_2visit_CClassDefNode(((struct __pyx_obj_6Cython_8Compiler_7Visitor_ScopeTrackingTransform *)__pyx_v_self), __pyx_v_node);
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

static PyObject *__pyx_pf_6Cython_8Compiler_7Visitor_22ScopeTrackingTransform_2visit_CClassDefNode(struct __pyx_obj_6Cython_8Compiler_7Visitor_ScopeTrackingTransform *__pyx_v_self, PyObject *__pyx_v_node) {
  PyObject *__pyx_r = NULL;
/* … */
  /* function exit code */
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_t_1);
  __Pyx_AddTraceback("Cython.Compiler.Visitor.ScopeTrackingTransform.visit_CClassDefNode", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_r = NULL;
  __pyx_L0:;
  __Pyx_XGIVEREF(__pyx_r);
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}
/* … */
  __pyx_t_2 = __Pyx_CyFunction_New(&__pyx_mdef_6Cython_8Compiler_7Visitor_22ScopeTrackingTransform_3visit_CClassDefNode, __Pyx_CYFUNCTION_CCLASS, __pyx_mstate_global->__pyx_n_u_ScopeTrackingTransform_visit_CCl, NULL, __pyx_mstate_global->__pyx_n_u_Cython_Compiler_Visitor, __pyx_mstate_global->__pyx_d, ((PyObject *)__pyx_mstate_global->__pyx_codeobj_tab[16])); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 343, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  #if CYTHON_COMPILING_IN_CPYTHON && PY_VERSION_HEX >= 0x030E0000
  PyUnstable_Object_EnableDeferredRefcount(__pyx_t_2);
  #endif
  if (__Pyx_SetItemOnTypeDict(__pyx_mstate_global->__pyx_ptype_6Cython_8Compiler_7Visitor_ScopeTrackingTransform, __pyx_mstate_global->__pyx_n_u_visit_CClassDefNode, __pyx_t_2) < (0)) __PYX_ERR(0, 343, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
```

</details>

L344  🟡  (score=1)
```python
        return self.visit_scope(node, 'cclass')
```
<details><summary>Show generated C (score=1)</summary>

```c
  __Pyx_XDECREF(__pyx_r);
  __pyx_t_1 = ((struct __pyx_vtabstruct_6Cython_8Compiler_7Visitor_ScopeTrackingTransform *)__pyx_v_self->__pyx_base.__pyx_base.__pyx_base.__pyx_vtab)->visit_scope(__pyx_v_self, __pyx_v_node, __pyx_mstate_global->__pyx_n_u_cclass); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 344, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __pyx_r = __pyx_t_1;
  __pyx_t_1 = 0;
  goto __pyx_L0;
```

</details>

L345  ⚪  (score=0)
```python
```
L346  🔴  (score=36)
```python
    def visit_PyClassDefNode(self, node):
```
<details><summary>Show generated C (score=36)</summary>

```c
/* Python wrapper */
static PyObject *__pyx_pw_6Cython_8Compiler_7Visitor_22ScopeTrackingTransform_5visit_PyClassDefNode(PyObject *__pyx_v_self, 
#if CYTHON_METH_FASTCALL
PyObject *const *__pyx_args, Py_ssize_t __pyx_nargs, PyObject *__pyx_kwds
#else
PyObject *__pyx_args, PyObject *__pyx_kwds
#endif
); /*proto*/
PyDoc_STRVAR(__pyx_doc_6Cython_8Compiler_7Visitor_22ScopeTrackingTransform_4visit_PyClassDefNode, "File: Cython/Compiler/Visitor.py (starting at line 346)");
static PyMethodDef __pyx_mdef_6Cython_8Compiler_7Visitor_22ScopeTrackingTransform_5visit_PyClassDefNode = {"visit_PyClassDefNode", (PyCFunction)(void(*)(void))(__Pyx_PyCFunction_FastCallWithKeywords)__pyx_pw_6Cython_8Compiler_7Visitor_22ScopeTrackingTransform_5visit_PyClassDefNode, __Pyx_METH_FASTCALL|METH_KEYWORDS, __pyx_doc_6Cython_8Compiler_7Visitor_22ScopeTrackingTransform_4visit_PyClassDefNode};
static PyObject *__pyx_pw_6Cython_8Compiler_7Visitor_22ScopeTrackingTransform_5visit_PyClassDefNode(PyObject *__pyx_v_self, 
#if CYTHON_METH_FASTCALL
PyObject *const *__pyx_args, Py_ssize_t __pyx_nargs, PyObject *__pyx_kwds
#else
PyObject *__pyx_args, PyObject *__pyx_kwds
#endif
) {
  PyObject *__pyx_v_node = 0;
  #if !CYTHON_METH_FASTCALL
  CYTHON_UNUSED Py_ssize_t __pyx_nargs;
  #endif
  CYTHON_UNUSED PyObject *const *__pyx_kwvalues;
  PyObject *__pyx_r = 0;
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("visit_PyClassDefNode (wrapper)", 0);
  #if !CYTHON_METH_FASTCALL
  #if CYTHON_ASSUME_SAFE_SIZE
  __pyx_nargs = PyTuple_GET_SIZE(__pyx_args);
  #else
  __pyx_nargs = PyTuple_Size(__pyx_args); if (unlikely(__pyx_nargs < 0)) return NULL;
  #endif
  #endif
  __pyx_kwvalues = __Pyx_KwValues_FASTCALL(__pyx_args, __pyx_nargs);
  {
    PyObject ** const __pyx_pyargnames[] = {&__pyx_mstate_global->__pyx_n_u_node,0};
  PyObject* values[1] = {0};
    const Py_ssize_t __pyx_kwds_len = (__pyx_kwds) ? __Pyx_NumKwargs_FASTCALL(__pyx_kwds) : 0;
    if (unlikely(__pyx_kwds_len) < 0) __PYX_ERR(0, 346, __pyx_L3_error)
    if (__pyx_kwds_len > 0) {
      switch (__pyx_nargs) {
        case  1:
        values[0] = __Pyx_ArgRef_FASTCALL(__pyx_args, 0);
        if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[0])) __PYX_ERR(0, 346, __pyx_L3_error)
        CYTHON_FALLTHROUGH;
        case  0: break;
        default: goto __pyx_L5_argtuple_error;
      }
      const Py_ssize_t kwd_pos_args = __pyx_nargs;
      if (__Pyx_ParseKeywords(__pyx_kwds, __pyx_kwvalues, __pyx_pyargnames, 0, values, kwd_pos_args, __pyx_kwds_len, "visit_PyClassDefNode", 0) < (0)) __PYX_ERR(0, 346, __pyx_L3_error)
      for (Py_ssize_t i = __pyx_nargs; i < 1; i++) {
        if (unlikely(!values[i])) { __Pyx_RaiseArgtupleInvalid("visit_PyClassDefNode", 1, 1, 1, i); __PYX_ERR(0, 346, __pyx_L3_error) }
      }
    } else if (unlikely(__pyx_nargs != 1)) {
      goto __pyx_L5_argtuple_error;
    } else {
      values[0] = __Pyx_ArgRef_FASTCALL(__pyx_args, 0);
      if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[0])) __PYX_ERR(0, 346, __pyx_L3_error)
    }
    __pyx_v_node = values[0];
  }
  goto __pyx_L6_skip;
  __pyx_L5_argtuple_error:;
  __Pyx_RaiseArgtupleInvalid("visit_PyClassDefNode", 1, 1, 1, __pyx_nargs); __PYX_ERR(0, 346, __pyx_L3_error)
  __pyx_L6_skip:;
  goto __pyx_L4_argument_unpacking_done;
  __pyx_L3_error:;
  for (Py_ssize_t __pyx_temp=0; __pyx_temp < (Py_ssize_t)(sizeof(values)/sizeof(values[0])); ++__pyx_temp) {
    Py_XDECREF(values[__pyx_temp]);
  }
  __Pyx_AddTraceback("Cython.Compiler.Visitor.ScopeTrackingTransform.visit_PyClassDefNode", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __Pyx_RefNannyFinishContext();
  return NULL;
  __pyx_L4_argument_unpacking_done:;
  __pyx_r = __pyx_pf_6Cython_8Compiler_7Visitor_22ScopeTrackingTransform_4visit_PyClassDefNode(((struct __pyx_obj_6Cython_8Compiler_7Visitor_ScopeTrackingTransform *)__pyx_v_self), __pyx_v_node);
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

static PyObject *__pyx_pf_6Cython_8Compiler_7Visitor_22ScopeTrackingTransform_4visit_PyClassDefNode(struct __pyx_obj_6Cython_8Compiler_7Visitor_ScopeTrackingTransform *__pyx_v_self, PyObject *__pyx_v_node) {
  PyObject *__pyx_r = NULL;
/* … */
  /* function exit code */
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_t_1);
  __Pyx_AddTraceback("Cython.Compiler.Visitor.ScopeTrackingTransform.visit_PyClassDefNode", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_r = NULL;
  __pyx_L0:;
  __Pyx_XGIVEREF(__pyx_r);
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}
/* … */
  __pyx_t_2 = __Pyx_CyFunction_New(&__pyx_mdef_6Cython_8Compiler_7Visitor_22ScopeTrackingTransform_5visit_PyClassDefNode, __Pyx_CYFUNCTION_CCLASS, __pyx_mstate_global->__pyx_n_u_ScopeTrackingTransform_visit_PyC, NULL, __pyx_mstate_global->__pyx_n_u_Cython_Compiler_Visitor, __pyx_mstate_global->__pyx_d, ((PyObject *)__pyx_mstate_global->__pyx_codeobj_tab[17])); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 346, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  #if CYTHON_COMPILING_IN_CPYTHON && PY_VERSION_HEX >= 0x030E0000
  PyUnstable_Object_EnableDeferredRefcount(__pyx_t_2);
  #endif
  if (__Pyx_SetItemOnTypeDict(__pyx_mstate_global->__pyx_ptype_6Cython_8Compiler_7Visitor_ScopeTrackingTransform, __pyx_mstate_global->__pyx_n_u_visit_PyClassDefNode, __pyx_t_2) < (0)) __PYX_ERR(0, 346, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
```

</details>

L347  🟡  (score=1)
```python
        return self.visit_scope(node, 'pyclass')
```
<details><summary>Show generated C (score=1)</summary>

```c
  __Pyx_XDECREF(__pyx_r);
  __pyx_t_1 = ((struct __pyx_vtabstruct_6Cython_8Compiler_7Visitor_ScopeTrackingTransform *)__pyx_v_self->__pyx_base.__pyx_base.__pyx_base.__pyx_vtab)->visit_scope(__pyx_v_self, __pyx_v_node, __pyx_mstate_global->__pyx_n_u_pyclass); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 347, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __pyx_r = __pyx_t_1;
  __pyx_t_1 = 0;
  goto __pyx_L0;
```

</details>

L348  ⚪  (score=0)
```python
```
L349  🔴  (score=36)
```python
    def visit_FuncDefNode(self, node):
```
<details><summary>Show generated C (score=36)</summary>

```c
/* Python wrapper */
static PyObject *__pyx_pw_6Cython_8Compiler_7Visitor_22ScopeTrackingTransform_7visit_FuncDefNode(PyObject *__pyx_v_self, 
#if CYTHON_METH_FASTCALL
PyObject *const *__pyx_args, Py_ssize_t __pyx_nargs, PyObject *__pyx_kwds
#else
PyObject *__pyx_args, PyObject *__pyx_kwds
#endif
); /*proto*/
PyDoc_STRVAR(__pyx_doc_6Cython_8Compiler_7Visitor_22ScopeTrackingTransform_6visit_FuncDefNode, "File: Cython/Compiler/Visitor.py (starting at line 349)");
static PyMethodDef __pyx_mdef_6Cython_8Compiler_7Visitor_22ScopeTrackingTransform_7visit_FuncDefNode = {"visit_FuncDefNode", (PyCFunction)(void(*)(void))(__Pyx_PyCFunction_FastCallWithKeywords)__pyx_pw_6Cython_8Compiler_7Visitor_22ScopeTrackingTransform_7visit_FuncDefNode, __Pyx_METH_FASTCALL|METH_KEYWORDS, __pyx_doc_6Cython_8Compiler_7Visitor_22ScopeTrackingTransform_6visit_FuncDefNode};
static PyObject *__pyx_pw_6Cython_8Compiler_7Visitor_22ScopeTrackingTransform_7visit_FuncDefNode(PyObject *__pyx_v_self, 
#if CYTHON_METH_FASTCALL
PyObject *const *__pyx_args, Py_ssize_t __pyx_nargs, PyObject *__pyx_kwds
#else
PyObject *__pyx_args, PyObject *__pyx_kwds
#endif
) {
  PyObject *__pyx_v_node = 0;
  #if !CYTHON_METH_FASTCALL
  CYTHON_UNUSED Py_ssize_t __pyx_nargs;
  #endif
  CYTHON_UNUSED PyObject *const *__pyx_kwvalues;
  PyObject *__pyx_r = 0;
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("visit_FuncDefNode (wrapper)", 0);
  #if !CYTHON_METH_FASTCALL
  #if CYTHON_ASSUME_SAFE_SIZE
  __pyx_nargs = PyTuple_GET_SIZE(__pyx_args);
  #else
  __pyx_nargs = PyTuple_Size(__pyx_args); if (unlikely(__pyx_nargs < 0)) return NULL;
  #endif
  #endif
  __pyx_kwvalues = __Pyx_KwValues_FASTCALL(__pyx_args, __pyx_nargs);
  {
    PyObject ** const __pyx_pyargnames[] = {&__pyx_mstate_global->__pyx_n_u_node,0};
  PyObject* values[1] = {0};
    const Py_ssize_t __pyx_kwds_len = (__pyx_kwds) ? __Pyx_NumKwargs_FASTCALL(__pyx_kwds) : 0;
    if (unlikely(__pyx_kwds_len) < 0) __PYX_ERR(0, 349, __pyx_L3_error)
    if (__pyx_kwds_len > 0) {
      switch (__pyx_nargs) {
        case  1:
        values[0] = __Pyx_ArgRef_FASTCALL(__pyx_args, 0);
        if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[0])) __PYX_ERR(0, 349, __pyx_L3_error)
        CYTHON_FALLTHROUGH;
        case  0: break;
        default: goto __pyx_L5_argtuple_error;
      }
      const Py_ssize_t kwd_pos_args = __pyx_nargs;
      if (__Pyx_ParseKeywords(__pyx_kwds, __pyx_kwvalues, __pyx_pyargnames, 0, values, kwd_pos_args, __pyx_kwds_len, "visit_FuncDefNode", 0) < (0)) __PYX_ERR(0, 349, __pyx_L3_error)
      for (Py_ssize_t i = __pyx_nargs; i < 1; i++) {
        if (unlikely(!values[i])) { __Pyx_RaiseArgtupleInvalid("visit_FuncDefNode", 1, 1, 1, i); __PYX_ERR(0, 349, __pyx_L3_error) }
      }
    } else if (unlikely(__pyx_nargs != 1)) {
      goto __pyx_L5_argtuple_error;
    } else {
      values[0] = __Pyx_ArgRef_FASTCALL(__pyx_args, 0);
      if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[0])) __PYX_ERR(0, 349, __pyx_L3_error)
    }
    __pyx_v_node = values[0];
  }
  goto __pyx_L6_skip;
  __pyx_L5_argtuple_error:;
  __Pyx_RaiseArgtupleInvalid("visit_FuncDefNode", 1, 1, 1, __pyx_nargs); __PYX_ERR(0, 349, __pyx_L3_error)
  __pyx_L6_skip:;
  goto __pyx_L4_argument_unpacking_done;
  __pyx_L3_error:;
  for (Py_ssize_t __pyx_temp=0; __pyx_temp < (Py_ssize_t)(sizeof(values)/sizeof(values[0])); ++__pyx_temp) {
    Py_XDECREF(values[__pyx_temp]);
  }
  __Pyx_AddTraceback("Cython.Compiler.Visitor.ScopeTrackingTransform.visit_FuncDefNode", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __Pyx_RefNannyFinishContext();
  return NULL;
  __pyx_L4_argument_unpacking_done:;
  __pyx_r = __pyx_pf_6Cython_8Compiler_7Visitor_22ScopeTrackingTransform_6visit_FuncDefNode(((struct __pyx_obj_6Cython_8Compiler_7Visitor_ScopeTrackingTransform *)__pyx_v_self), __pyx_v_node);
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

static PyObject *__pyx_pf_6Cython_8Compiler_7Visitor_22ScopeTrackingTransform_6visit_FuncDefNode(struct __pyx_obj_6Cython_8Compiler_7Visitor_ScopeTrackingTransform *__pyx_v_self, PyObject *__pyx_v_node) {
  PyObject *__pyx_r = NULL;
/* … */
  /* function exit code */
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_t_1);
  __Pyx_AddTraceback("Cython.Compiler.Visitor.ScopeTrackingTransform.visit_FuncDefNode", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_r = NULL;
  __pyx_L0:;
  __Pyx_XGIVEREF(__pyx_r);
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}
/* … */
  __pyx_t_2 = __Pyx_CyFunction_New(&__pyx_mdef_6Cython_8Compiler_7Visitor_22ScopeTrackingTransform_7visit_FuncDefNode, __Pyx_CYFUNCTION_CCLASS, __pyx_mstate_global->__pyx_n_u_ScopeTrackingTransform_visit_Fun, NULL, __pyx_mstate_global->__pyx_n_u_Cython_Compiler_Visitor, __pyx_mstate_global->__pyx_d, ((PyObject *)__pyx_mstate_global->__pyx_codeobj_tab[18])); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 349, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  #if CYTHON_COMPILING_IN_CPYTHON && PY_VERSION_HEX >= 0x030E0000
  PyUnstable_Object_EnableDeferredRefcount(__pyx_t_2);
  #endif
  if (__Pyx_SetItemOnTypeDict(__pyx_mstate_global->__pyx_ptype_6Cython_8Compiler_7Visitor_ScopeTrackingTransform, __pyx_mstate_global->__pyx_n_u_visit_FuncDefNode, __pyx_t_2) < (0)) __PYX_ERR(0, 349, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
```

</details>

L350  🟡  (score=1)
```python
        return self.visit_scope(node, 'function')
```
<details><summary>Show generated C (score=1)</summary>

```c
  __Pyx_XDECREF(__pyx_r);
  __pyx_t_1 = ((struct __pyx_vtabstruct_6Cython_8Compiler_7Visitor_ScopeTrackingTransform *)__pyx_v_self->__pyx_base.__pyx_base.__pyx_base.__pyx_vtab)->visit_scope(__pyx_v_self, __pyx_v_node, __pyx_mstate_global->__pyx_n_u_function); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 350, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __pyx_r = __pyx_t_1;
  __pyx_t_1 = 0;
  goto __pyx_L0;
```

</details>

L351  ⚪  (score=0)
```python
```
L352  🔴  (score=36)
```python
    def visit_CStructOrUnionDefNode(self, node):
```
<details><summary>Show generated C (score=36)</summary>

```c
/* Python wrapper */
static PyObject *__pyx_pw_6Cython_8Compiler_7Visitor_22ScopeTrackingTransform_9visit_CStructOrUnionDefNode(PyObject *__pyx_v_self, 
#if CYTHON_METH_FASTCALL
PyObject *const *__pyx_args, Py_ssize_t __pyx_nargs, PyObject *__pyx_kwds
#else
PyObject *__pyx_args, PyObject *__pyx_kwds
#endif
); /*proto*/
PyDoc_STRVAR(__pyx_doc_6Cython_8Compiler_7Visitor_22ScopeTrackingTransform_8visit_CStructOrUnionDefNode, "File: Cython/Compiler/Visitor.py (starting at line 352)");
static PyMethodDef __pyx_mdef_6Cython_8Compiler_7Visitor_22ScopeTrackingTransform_9visit_CStructOrUnionDefNode = {"visit_CStructOrUnionDefNode", (PyCFunction)(void(*)(void))(__Pyx_PyCFunction_FastCallWithKeywords)__pyx_pw_6Cython_8Compiler_7Visitor_22ScopeTrackingTransform_9visit_CStructOrUnionDefNode, __Pyx_METH_FASTCALL|METH_KEYWORDS, __pyx_doc_6Cython_8Compiler_7Visitor_22ScopeTrackingTransform_8visit_CStructOrUnionDefNode};
static PyObject *__pyx_pw_6Cython_8Compiler_7Visitor_22ScopeTrackingTransform_9visit_CStructOrUnionDefNode(PyObject *__pyx_v_self, 
#if CYTHON_METH_FASTCALL
PyObject *const *__pyx_args, Py_ssize_t __pyx_nargs, PyObject *__pyx_kwds
#else
PyObject *__pyx_args, PyObject *__pyx_kwds
#endif
) {
  PyObject *__pyx_v_node = 0;
  #if !CYTHON_METH_FASTCALL
  CYTHON_UNUSED Py_ssize_t __pyx_nargs;
  #endif
  CYTHON_UNUSED PyObject *const *__pyx_kwvalues;
  PyObject *__pyx_r = 0;
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("visit_CStructOrUnionDefNode (wrapper)", 0);
  #if !CYTHON_METH_FASTCALL
  #if CYTHON_ASSUME_SAFE_SIZE
  __pyx_nargs = PyTuple_GET_SIZE(__pyx_args);
  #else
  __pyx_nargs = PyTuple_Size(__pyx_args); if (unlikely(__pyx_nargs < 0)) return NULL;
  #endif
  #endif
  __pyx_kwvalues = __Pyx_KwValues_FASTCALL(__pyx_args, __pyx_nargs);
  {
    PyObject ** const __pyx_pyargnames[] = {&__pyx_mstate_global->__pyx_n_u_node,0};
  PyObject* values[1] = {0};
    const Py_ssize_t __pyx_kwds_len = (__pyx_kwds) ? __Pyx_NumKwargs_FASTCALL(__pyx_kwds) : 0;
    if (unlikely(__pyx_kwds_len) < 0) __PYX_ERR(0, 352, __pyx_L3_error)
    if (__pyx_kwds_len > 0) {
      switch (__pyx_nargs) {
        case  1:
        values[0] = __Pyx_ArgRef_FASTCALL(__pyx_args, 0);
        if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[0])) __PYX_ERR(0, 352, __pyx_L3_error)
        CYTHON_FALLTHROUGH;
        case  0: break;
        default: goto __pyx_L5_argtuple_error;
      }
      const Py_ssize_t kwd_pos_args = __pyx_nargs;
      if (__Pyx_ParseKeywords(__pyx_kwds, __pyx_kwvalues, __pyx_pyargnames, 0, values, kwd_pos_args, __pyx_kwds_len, "visit_CStructOrUnionDefNode", 0) < (0)) __PYX_ERR(0, 352, __pyx_L3_error)
      for (Py_ssize_t i = __pyx_nargs; i < 1; i++) {
        if (unlikely(!values[i])) { __Pyx_RaiseArgtupleInvalid("visit_CStructOrUnionDefNode", 1, 1, 1, i); __PYX_ERR(0, 352, __pyx_L3_error) }
      }
    } else if (unlikely(__pyx_nargs != 1)) {
      goto __pyx_L5_argtuple_error;
    } else {
      values[0] = __Pyx_ArgRef_FASTCALL(__pyx_args, 0);
      if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[0])) __PYX_ERR(0, 352, __pyx_L3_error)
    }
    __pyx_v_node = values[0];
  }
  goto __pyx_L6_skip;
  __pyx_L5_argtuple_error:;
  __Pyx_RaiseArgtupleInvalid("visit_CStructOrUnionDefNode", 1, 1, 1, __pyx_nargs); __PYX_ERR(0, 352, __pyx_L3_error)
  __pyx_L6_skip:;
  goto __pyx_L4_argument_unpacking_done;
  __pyx_L3_error:;
  for (Py_ssize_t __pyx_temp=0; __pyx_temp < (Py_ssize_t)(sizeof(values)/sizeof(values[0])); ++__pyx_temp) {
    Py_XDECREF(values[__pyx_temp]);
  }
  __Pyx_AddTraceback("Cython.Compiler.Visitor.ScopeTrackingTransform.visit_CStructOrUnionDefNode", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __Pyx_RefNannyFinishContext();
  return NULL;
  __pyx_L4_argument_unpacking_done:;
  __pyx_r = __pyx_pf_6Cython_8Compiler_7Visitor_22ScopeTrackingTransform_8visit_CStructOrUnionDefNode(((struct __pyx_obj_6Cython_8Compiler_7Visitor_ScopeTrackingTransform *)__pyx_v_self), __pyx_v_node);
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

static PyObject *__pyx_pf_6Cython_8Compiler_7Visitor_22ScopeTrackingTransform_8visit_CStructOrUnionDefNode(struct __pyx_obj_6Cython_8Compiler_7Visitor_ScopeTrackingTransform *__pyx_v_self, PyObject *__pyx_v_node) {
  PyObject *__pyx_r = NULL;
/* … */
  /* function exit code */
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_t_1);
  __Pyx_AddTraceback("Cython.Compiler.Visitor.ScopeTrackingTransform.visit_CStructOrUnionDefNode", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_r = NULL;
  __pyx_L0:;
  __Pyx_XGIVEREF(__pyx_r);
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}
/* … */
  __pyx_t_2 = __Pyx_CyFunction_New(&__pyx_mdef_6Cython_8Compiler_7Visitor_22ScopeTrackingTransform_9visit_CStructOrUnionDefNode, __Pyx_CYFUNCTION_CCLASS, __pyx_mstate_global->__pyx_n_u_ScopeTrackingTransform_visit_CSt, NULL, __pyx_mstate_global->__pyx_n_u_Cython_Compiler_Visitor, __pyx_mstate_global->__pyx_d, ((PyObject *)__pyx_mstate_global->__pyx_codeobj_tab[19])); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 352, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  #if CYTHON_COMPILING_IN_CPYTHON && PY_VERSION_HEX >= 0x030E0000
  PyUnstable_Object_EnableDeferredRefcount(__pyx_t_2);
  #endif
  if (__Pyx_SetItemOnTypeDict(__pyx_mstate_global->__pyx_ptype_6Cython_8Compiler_7Visitor_ScopeTrackingTransform, __pyx_mstate_global->__pyx_n_u_visit_CStructOrUnionDefNode, __pyx_t_2) < (0)) __PYX_ERR(0, 352, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
```

</details>

L353  🟡  (score=1)
```python
        return self.visit_scope(node, 'struct')
```
<details><summary>Show generated C (score=1)</summary>

```c
  __Pyx_XDECREF(__pyx_r);
  __pyx_t_1 = ((struct __pyx_vtabstruct_6Cython_8Compiler_7Visitor_ScopeTrackingTransform *)__pyx_v_self->__pyx_base.__pyx_base.__pyx_base.__pyx_vtab)->visit_scope(__pyx_v_self, __pyx_v_node, __pyx_mstate_global->__pyx_n_u_struct); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 353, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __pyx_r = __pyx_t_1;
  __pyx_t_1 = 0;
  goto __pyx_L0;
```

</details>

L354  ⚪  (score=0)
```python
```
L355  ⚪  (score=0)
```python
```
L356  ⚪  (score=0)
```python
class EnvTransform(CythonTransform):
```
<details><summary>Show generated C (score=0)</summary>

```c
struct __pyx_vtabstruct_6Cython_8Compiler_7Visitor_EnvTransform {
  struct __pyx_vtabstruct_6Cython_8Compiler_7Visitor_CythonTransform __pyx_base;
};
static struct __pyx_vtabstruct_6Cython_8Compiler_7Visitor_EnvTransform *__pyx_vtabptr_6Cython_8Compiler_7Visitor_EnvTransform;

```

</details>

L357  ⚪  (score=0)
```python
    """
```
L358  ⚪  (score=0)
```python
    This transformation keeps a stack of the environments.
```
L359  ⚪  (score=0)
```python
    """
```
L360  🔴  (score=29)
```python
    def __call__(self, root):
```
<details><summary>Show generated C (score=29)</summary>

```c
/* Python wrapper */
static PyObject *__pyx_pw_6Cython_8Compiler_7Visitor_12EnvTransform_1__call__(PyObject *__pyx_v_self, PyObject *__pyx_args, PyObject *__pyx_kwds); /*proto*/
PyDoc_STRVAR(__pyx_doc_6Cython_8Compiler_7Visitor_12EnvTransform___call__, "File: Cython/Compiler/Visitor.py (starting at line 360)");
#if CYTHON_UPDATE_DESCRIPTOR_DOC
struct wrapperbase __pyx_wrapperbase_6Cython_8Compiler_7Visitor_12EnvTransform___call__;
#endif
static PyObject *__pyx_pw_6Cython_8Compiler_7Visitor_12EnvTransform_1__call__(PyObject *__pyx_v_self, PyObject *__pyx_args, PyObject *__pyx_kwds) {
  PyObject *__pyx_v_root = 0;
  CYTHON_UNUSED Py_ssize_t __pyx_nargs;
  CYTHON_UNUSED PyObject *const *__pyx_kwvalues;
  PyObject *__pyx_r = 0;
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("__call__ (wrapper)", 0);
  #if CYTHON_ASSUME_SAFE_SIZE
  __pyx_nargs = PyTuple_GET_SIZE(__pyx_args);
  #else
  __pyx_nargs = PyTuple_Size(__pyx_args); if (unlikely(__pyx_nargs < 0)) return NULL;
  #endif
  __pyx_kwvalues = __Pyx_KwValues_VARARGS(__pyx_args, __pyx_nargs);
  {
    PyObject ** const __pyx_pyargnames[] = {&__pyx_mstate_global->__pyx_n_u_root,0};
  PyObject* values[1] = {0};
    const Py_ssize_t __pyx_kwds_len = (__pyx_kwds) ? __Pyx_NumKwargs_VARARGS(__pyx_kwds) : 0;
    if (unlikely(__pyx_kwds_len) < 0) __PYX_ERR(0, 360, __pyx_L3_error)
    if (__pyx_kwds_len > 0) {
      switch (__pyx_nargs) {
        case  1:
        values[0] = __Pyx_ArgRef_VARARGS(__pyx_args, 0);
        if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[0])) __PYX_ERR(0, 360, __pyx_L3_error)
        CYTHON_FALLTHROUGH;
        case  0: break;
        default: goto __pyx_L5_argtuple_error;
      }
      const Py_ssize_t kwd_pos_args = __pyx_nargs;
      if (__Pyx_ParseKeywords(__pyx_kwds, __pyx_kwvalues, __pyx_pyargnames, 0, values, kwd_pos_args, __pyx_kwds_len, "__call__", 0) < (0)) __PYX_ERR(0, 360, __pyx_L3_error)
      for (Py_ssize_t i = __pyx_nargs; i < 1; i++) {
        if (unlikely(!values[i])) { __Pyx_RaiseArgtupleInvalid("__call__", 1, 1, 1, i); __PYX_ERR(0, 360, __pyx_L3_error) }
      }
    } else if (unlikely(__pyx_nargs != 1)) {
      goto __pyx_L5_argtuple_error;
    } else {
      values[0] = __Pyx_ArgRef_VARARGS(__pyx_args, 0);
      if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[0])) __PYX_ERR(0, 360, __pyx_L3_error)
    }
    __pyx_v_root = values[0];
  }
  goto __pyx_L6_skip;
  __pyx_L5_argtuple_error:;
  __Pyx_RaiseArgtupleInvalid("__call__", 1, 1, 1, __pyx_nargs); __PYX_ERR(0, 360, __pyx_L3_error)
  __pyx_L6_skip:;
  goto __pyx_L4_argument_unpacking_done;
  __pyx_L3_error:;
  for (Py_ssize_t __pyx_temp=0; __pyx_temp < (Py_ssize_t)(sizeof(values)/sizeof(values[0])); ++__pyx_temp) {
    Py_XDECREF(values[__pyx_temp]);
  }
  __Pyx_AddTraceback("Cython.Compiler.Visitor.EnvTransform.__call__", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __Pyx_RefNannyFinishContext();
  return NULL;
  __pyx_L4_argument_unpacking_done:;
  __pyx_r = __pyx_pf_6Cython_8Compiler_7Visitor_12EnvTransform___call__(((struct __pyx_obj_6Cython_8Compiler_7Visitor_EnvTransform *)__pyx_v_self), __pyx_v_root);
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

static PyObject *__pyx_pf_6Cython_8Compiler_7Visitor_12EnvTransform___call__(struct __pyx_obj_6Cython_8Compiler_7Visitor_EnvTransform *__pyx_v_self, PyObject *__pyx_v_root) {
  PyObject *__pyx_r = NULL;
/* … */
  /* function exit code */
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_t_1);
  __Pyx_XDECREF(__pyx_t_2);
  __Pyx_XDECREF(__pyx_t_3);
  __Pyx_XDECREF(__pyx_t_5);
  __Pyx_AddTraceback("Cython.Compiler.Visitor.EnvTransform.__call__", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_r = NULL;
  __pyx_L0:;
  __Pyx_XGIVEREF(__pyx_r);
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}
```

</details>

L361  🟠  (score=6)
```python
        self.env_stack = []
```
<details><summary>Show generated C (score=6)</summary>

```c
  __pyx_t_1 = PyList_New(0); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 361, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_GIVEREF(__pyx_t_1);
  __Pyx_GOTREF(__pyx_v_self->env_stack);
  __Pyx_DECREF(__pyx_v_self->env_stack);
  __pyx_v_self->env_stack = ((PyObject*)__pyx_t_1);
  __pyx_t_1 = 0;
```

</details>

L362  🟠  (score=8)
```python
        self.enter_scope(root, root.scope)
```
<details><summary>Show generated C (score=8)</summary>

```c
  __pyx_t_2 = ((PyObject *)__pyx_v_self);
  __Pyx_INCREF(__pyx_t_2);
  __pyx_t_3 = __Pyx_PyObject_GetAttrStr(__pyx_v_root, __pyx_mstate_global->__pyx_n_u_scope); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 362, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_3);
  __pyx_t_4 = 0;
  {
    PyObject *__pyx_callargs[3] = {__pyx_t_2, __pyx_v_root, __pyx_t_3};
    __pyx_t_1 = __Pyx_PyObject_FastCallMethod((PyObject*)__pyx_mstate_global->__pyx_n_u_enter_scope, __pyx_callargs+__pyx_t_4, (3-__pyx_t_4) | (1*__Pyx_PY_VECTORCALL_ARGUMENTS_OFFSET));
    __Pyx_XDECREF(__pyx_t_2); __pyx_t_2 = 0;
    __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
    if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 362, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_1);
  }
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
```

</details>

L363  🟠  (score=9)
```python
        return super().__call__(root)
```
<details><summary>Show generated C (score=9)</summary>

```c
  __Pyx_XDECREF(__pyx_r);
  __pyx_t_5 = NULL;
  __pyx_t_4 = 1;
  {
    PyObject *__pyx_callargs[3] = {__pyx_t_5, ((PyObject *)__pyx_mstate_global->__pyx_ptype_6Cython_8Compiler_7Visitor_EnvTransform), ((PyObject *)__pyx_v_self)};
    __pyx_t_2 = __Pyx_PyObject_FastCall((PyObject*)__pyx_builtin_super, __pyx_callargs+__pyx_t_4, (3-__pyx_t_4) | (__pyx_t_4*__Pyx_PY_VECTORCALL_ARGUMENTS_OFFSET));
    __Pyx_XDECREF(__pyx_t_5); __pyx_t_5 = 0;
    if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 363, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_2);
  }
  __pyx_t_3 = __pyx_t_2;
  __Pyx_INCREF(__pyx_t_3);
  __pyx_t_4 = 0;
  {
    PyObject *__pyx_callargs[2] = {__pyx_t_3, __pyx_v_root};
    __pyx_t_1 = __Pyx_PyObject_FastCallMethod((PyObject*)__pyx_mstate_global->__pyx_n_u_call, __pyx_callargs+__pyx_t_4, (2-__pyx_t_4) | (1*__Pyx_PY_VECTORCALL_ARGUMENTS_OFFSET));
    __Pyx_XDECREF(__pyx_t_3); __pyx_t_3 = 0;
    __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
    if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 363, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_1);
  }
  __pyx_r = __pyx_t_1;
  __pyx_t_1 = 0;
  goto __pyx_L0;
```

</details>

L364  ⚪  (score=0)
```python
```
L365  🔴  (score=29)
```python
    def current_env(self):
```
<details><summary>Show generated C (score=29)</summary>

```c
/* Python wrapper */
static PyObject *__pyx_pw_6Cython_8Compiler_7Visitor_12EnvTransform_3current_env(PyObject *__pyx_v_self, 
#if CYTHON_METH_FASTCALL
PyObject *const *__pyx_args, Py_ssize_t __pyx_nargs, PyObject *__pyx_kwds
#else
PyObject *__pyx_args, PyObject *__pyx_kwds
#endif
); /*proto*/
PyDoc_STRVAR(__pyx_doc_6Cython_8Compiler_7Visitor_12EnvTransform_2current_env, "File: Cython/Compiler/Visitor.py (starting at line 365)");
static PyMethodDef __pyx_mdef_6Cython_8Compiler_7Visitor_12EnvTransform_3current_env = {"current_env", (PyCFunction)(void(*)(void))(__Pyx_PyCFunction_FastCallWithKeywords)__pyx_pw_6Cython_8Compiler_7Visitor_12EnvTransform_3current_env, __Pyx_METH_FASTCALL|METH_KEYWORDS, __pyx_doc_6Cython_8Compiler_7Visitor_12EnvTransform_2current_env};
static PyObject *__pyx_pw_6Cython_8Compiler_7Visitor_12EnvTransform_3current_env(PyObject *__pyx_v_self, 
#if CYTHON_METH_FASTCALL
PyObject *const *__pyx_args, Py_ssize_t __pyx_nargs, PyObject *__pyx_kwds
#else
PyObject *__pyx_args, PyObject *__pyx_kwds
#endif
) {
  #if !CYTHON_METH_FASTCALL
  CYTHON_UNUSED Py_ssize_t __pyx_nargs;
  #endif
  CYTHON_UNUSED PyObject *const *__pyx_kwvalues;
  PyObject *__pyx_r = 0;
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("current_env (wrapper)", 0);
  #if !CYTHON_METH_FASTCALL
  #if CYTHON_ASSUME_SAFE_SIZE
  __pyx_nargs = PyTuple_GET_SIZE(__pyx_args);
  #else
  __pyx_nargs = PyTuple_Size(__pyx_args); if (unlikely(__pyx_nargs < 0)) return NULL;
  #endif
  #endif
  __pyx_kwvalues = __Pyx_KwValues_FASTCALL(__pyx_args, __pyx_nargs);
  if (unlikely(__pyx_nargs > 0)) { __Pyx_RaiseArgtupleInvalid("current_env", 1, 0, 0, __pyx_nargs); return NULL; }
  const Py_ssize_t __pyx_kwds_len = unlikely(__pyx_kwds) ? __Pyx_NumKwargs_FASTCALL(__pyx_kwds) : 0;
  if (unlikely(__pyx_kwds_len < 0)) return NULL;
  if (unlikely(__pyx_kwds_len > 0)) {__Pyx_RejectKeywords("current_env", __pyx_kwds); return NULL;}
  __pyx_r = __pyx_pf_6Cython_8Compiler_7Visitor_12EnvTransform_2current_env(((struct __pyx_obj_6Cython_8Compiler_7Visitor_EnvTransform *)__pyx_v_self));

  /* function exit code */
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}

static PyObject *__pyx_pf_6Cython_8Compiler_7Visitor_12EnvTransform_2current_env(struct __pyx_obj_6Cython_8Compiler_7Visitor_EnvTransform *__pyx_v_self) {
  PyObject *__pyx_r = NULL;
/* … */
  /* function exit code */
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_t_1);
  __Pyx_XDECREF(__pyx_t_2);
  __Pyx_AddTraceback("Cython.Compiler.Visitor.EnvTransform.current_env", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_r = NULL;
  __pyx_L0:;
  __Pyx_XGIVEREF(__pyx_r);
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}
/* … */
  __pyx_t_2 = __Pyx_CyFunction_New(&__pyx_mdef_6Cython_8Compiler_7Visitor_12EnvTransform_3current_env, __Pyx_CYFUNCTION_CCLASS, __pyx_mstate_global->__pyx_n_u_EnvTransform_current_env, NULL, __pyx_mstate_global->__pyx_n_u_Cython_Compiler_Visitor, __pyx_mstate_global->__pyx_d, ((PyObject *)__pyx_mstate_global->__pyx_codeobj_tab[22])); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 365, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  #if CYTHON_COMPILING_IN_CPYTHON && PY_VERSION_HEX >= 0x030E0000
  PyUnstable_Object_EnableDeferredRefcount(__pyx_t_2);
  #endif
  if (__Pyx_SetItemOnTypeDict(__pyx_mstate_global->__pyx_ptype_6Cython_8Compiler_7Visitor_EnvTransform, __pyx_mstate_global->__pyx_n_u_current_env, __pyx_t_2) < (0)) __PYX_ERR(0, 365, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
```

</details>

L366  🔴  (score=11)
```python
        return self.env_stack[-1][1]
```
<details><summary>Show generated C (score=11)</summary>

```c
  __Pyx_XDECREF(__pyx_r);
  if (unlikely(__pyx_v_self->env_stack == Py_None)) {
    PyErr_SetString(PyExc_TypeError, "'NoneType' object is not subscriptable");
    __PYX_ERR(0, 366, __pyx_L1_error)
  }
  __pyx_t_1 = __Pyx_GetItemInt_List(__pyx_v_self->env_stack, -1L, long, 1, __Pyx_PyLong_From_long, 1, 1, 1, 1, __Pyx_ReferenceSharing_SharedReference); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 366, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __pyx_t_2 = __Pyx_GetItemInt(__pyx_t_1, 1, long, 1, __Pyx_PyLong_From_long, 0, 0, 1, 1, __Pyx_ReferenceSharing_OwnStrongReference); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 366, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __pyx_r = __pyx_t_2;
  __pyx_t_2 = 0;
  goto __pyx_L0;
```

</details>

L367  ⚪  (score=0)
```python
```
L368  🔴  (score=29)
```python
    def current_scope_node(self):
```
<details><summary>Show generated C (score=29)</summary>

```c
/* Python wrapper */
static PyObject *__pyx_pw_6Cython_8Compiler_7Visitor_12EnvTransform_5current_scope_node(PyObject *__pyx_v_self, 
#if CYTHON_METH_FASTCALL
PyObject *const *__pyx_args, Py_ssize_t __pyx_nargs, PyObject *__pyx_kwds
#else
PyObject *__pyx_args, PyObject *__pyx_kwds
#endif
); /*proto*/
PyDoc_STRVAR(__pyx_doc_6Cython_8Compiler_7Visitor_12EnvTransform_4current_scope_node, "File: Cython/Compiler/Visitor.py (starting at line 368)");
static PyMethodDef __pyx_mdef_6Cython_8Compiler_7Visitor_12EnvTransform_5current_scope_node = {"current_scope_node", (PyCFunction)(void(*)(void))(__Pyx_PyCFunction_FastCallWithKeywords)__pyx_pw_6Cython_8Compiler_7Visitor_12EnvTransform_5current_scope_node, __Pyx_METH_FASTCALL|METH_KEYWORDS, __pyx_doc_6Cython_8Compiler_7Visitor_12EnvTransform_4current_scope_node};
static PyObject *__pyx_pw_6Cython_8Compiler_7Visitor_12EnvTransform_5current_scope_node(PyObject *__pyx_v_self, 
#if CYTHON_METH_FASTCALL
PyObject *const *__pyx_args, Py_ssize_t __pyx_nargs, PyObject *__pyx_kwds
#else
PyObject *__pyx_args, PyObject *__pyx_kwds
#endif
) {
  #if !CYTHON_METH_FASTCALL
  CYTHON_UNUSED Py_ssize_t __pyx_nargs;
  #endif
  CYTHON_UNUSED PyObject *const *__pyx_kwvalues;
  PyObject *__pyx_r = 0;
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("current_scope_node (wrapper)", 0);
  #if !CYTHON_METH_FASTCALL
  #if CYTHON_ASSUME_SAFE_SIZE
  __pyx_nargs = PyTuple_GET_SIZE(__pyx_args);
  #else
  __pyx_nargs = PyTuple_Size(__pyx_args); if (unlikely(__pyx_nargs < 0)) return NULL;
  #endif
  #endif
  __pyx_kwvalues = __Pyx_KwValues_FASTCALL(__pyx_args, __pyx_nargs);
  if (unlikely(__pyx_nargs > 0)) { __Pyx_RaiseArgtupleInvalid("current_scope_node", 1, 0, 0, __pyx_nargs); return NULL; }
  const Py_ssize_t __pyx_kwds_len = unlikely(__pyx_kwds) ? __Pyx_NumKwargs_FASTCALL(__pyx_kwds) : 0;
  if (unlikely(__pyx_kwds_len < 0)) return NULL;
  if (unlikely(__pyx_kwds_len > 0)) {__Pyx_RejectKeywords("current_scope_node", __pyx_kwds); return NULL;}
  __pyx_r = __pyx_pf_6Cython_8Compiler_7Visitor_12EnvTransform_4current_scope_node(((struct __pyx_obj_6Cython_8Compiler_7Visitor_EnvTransform *)__pyx_v_self));

  /* function exit code */
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}

static PyObject *__pyx_pf_6Cython_8Compiler_7Visitor_12EnvTransform_4current_scope_node(struct __pyx_obj_6Cython_8Compiler_7Visitor_EnvTransform *__pyx_v_self) {
  PyObject *__pyx_r = NULL;
/* … */
  /* function exit code */
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_t_1);
  __Pyx_XDECREF(__pyx_t_2);
  __Pyx_AddTraceback("Cython.Compiler.Visitor.EnvTransform.current_scope_node", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_r = NULL;
  __pyx_L0:;
  __Pyx_XGIVEREF(__pyx_r);
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}
/* … */
  __pyx_t_2 = __Pyx_CyFunction_New(&__pyx_mdef_6Cython_8Compiler_7Visitor_12EnvTransform_5current_scope_node, __Pyx_CYFUNCTION_CCLASS, __pyx_mstate_global->__pyx_n_u_EnvTransform_current_scope_node, NULL, __pyx_mstate_global->__pyx_n_u_Cython_Compiler_Visitor, __pyx_mstate_global->__pyx_d, ((PyObject *)__pyx_mstate_global->__pyx_codeobj_tab[23])); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 368, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  #if CYTHON_COMPILING_IN_CPYTHON && PY_VERSION_HEX >= 0x030E0000
  PyUnstable_Object_EnableDeferredRefcount(__pyx_t_2);
  #endif
  if (__Pyx_SetItemOnTypeDict(__pyx_mstate_global->__pyx_ptype_6Cython_8Compiler_7Visitor_EnvTransform, __pyx_mstate_global->__pyx_n_u_current_scope_node, __pyx_t_2) < (0)) __PYX_ERR(0, 368, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
```

</details>

L369  🔴  (score=11)
```python
        return self.env_stack[-1][0]
```
<details><summary>Show generated C (score=11)</summary>

```c
  __Pyx_XDECREF(__pyx_r);
  if (unlikely(__pyx_v_self->env_stack == Py_None)) {
    PyErr_SetString(PyExc_TypeError, "'NoneType' object is not subscriptable");
    __PYX_ERR(0, 369, __pyx_L1_error)
  }
  __pyx_t_1 = __Pyx_GetItemInt_List(__pyx_v_self->env_stack, -1L, long, 1, __Pyx_PyLong_From_long, 1, 1, 1, 1, __Pyx_ReferenceSharing_SharedReference); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 369, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __pyx_t_2 = __Pyx_GetItemInt(__pyx_t_1, 0, long, 1, __Pyx_PyLong_From_long, 0, 0, 1, 1, __Pyx_ReferenceSharing_OwnStrongReference); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 369, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __pyx_r = __pyx_t_2;
  __pyx_t_2 = 0;
  goto __pyx_L0;
```

</details>

L370  ⚪  (score=0)
```python
```
L371  🔴  (score=31)
```python
    def global_scope(self):
```
<details><summary>Show generated C (score=31)</summary>

```c
/* Python wrapper */
static PyObject *__pyx_pw_6Cython_8Compiler_7Visitor_12EnvTransform_7global_scope(PyObject *__pyx_v_self, 
#if CYTHON_METH_FASTCALL
PyObject *const *__pyx_args, Py_ssize_t __pyx_nargs, PyObject *__pyx_kwds
#else
PyObject *__pyx_args, PyObject *__pyx_kwds
#endif
); /*proto*/
PyDoc_STRVAR(__pyx_doc_6Cython_8Compiler_7Visitor_12EnvTransform_6global_scope, "File: Cython/Compiler/Visitor.py (starting at line 371)");
static PyMethodDef __pyx_mdef_6Cython_8Compiler_7Visitor_12EnvTransform_7global_scope = {"global_scope", (PyCFunction)(void(*)(void))(__Pyx_PyCFunction_FastCallWithKeywords)__pyx_pw_6Cython_8Compiler_7Visitor_12EnvTransform_7global_scope, __Pyx_METH_FASTCALL|METH_KEYWORDS, __pyx_doc_6Cython_8Compiler_7Visitor_12EnvTransform_6global_scope};
static PyObject *__pyx_pw_6Cython_8Compiler_7Visitor_12EnvTransform_7global_scope(PyObject *__pyx_v_self, 
#if CYTHON_METH_FASTCALL
PyObject *const *__pyx_args, Py_ssize_t __pyx_nargs, PyObject *__pyx_kwds
#else
PyObject *__pyx_args, PyObject *__pyx_kwds
#endif
) {
  #if !CYTHON_METH_FASTCALL
  CYTHON_UNUSED Py_ssize_t __pyx_nargs;
  #endif
  CYTHON_UNUSED PyObject *const *__pyx_kwvalues;
  PyObject *__pyx_r = 0;
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("global_scope (wrapper)", 0);
  #if !CYTHON_METH_FASTCALL
  #if CYTHON_ASSUME_SAFE_SIZE
  __pyx_nargs = PyTuple_GET_SIZE(__pyx_args);
  #else
  __pyx_nargs = PyTuple_Size(__pyx_args); if (unlikely(__pyx_nargs < 0)) return NULL;
  #endif
  #endif
  __pyx_kwvalues = __Pyx_KwValues_FASTCALL(__pyx_args, __pyx_nargs);
  if (unlikely(__pyx_nargs > 0)) { __Pyx_RaiseArgtupleInvalid("global_scope", 1, 0, 0, __pyx_nargs); return NULL; }
  const Py_ssize_t __pyx_kwds_len = unlikely(__pyx_kwds) ? __Pyx_NumKwargs_FASTCALL(__pyx_kwds) : 0;
  if (unlikely(__pyx_kwds_len < 0)) return NULL;
  if (unlikely(__pyx_kwds_len > 0)) {__Pyx_RejectKeywords("global_scope", __pyx_kwds); return NULL;}
  __pyx_r = __pyx_pf_6Cython_8Compiler_7Visitor_12EnvTransform_6global_scope(((struct __pyx_obj_6Cython_8Compiler_7Visitor_EnvTransform *)__pyx_v_self));

  /* function exit code */
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}

static PyObject *__pyx_pf_6Cython_8Compiler_7Visitor_12EnvTransform_6global_scope(struct __pyx_obj_6Cython_8Compiler_7Visitor_EnvTransform *__pyx_v_self) {
  PyObject *__pyx_r = NULL;
/* … */
  /* function exit code */
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_t_1);
  __Pyx_XDECREF(__pyx_t_2);
  __Pyx_XDECREF(__pyx_t_3);
  __Pyx_XDECREF(__pyx_t_4);
  __Pyx_AddTraceback("Cython.Compiler.Visitor.EnvTransform.global_scope", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_r = NULL;
  __pyx_L0:;
  __Pyx_XGIVEREF(__pyx_r);
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}
/* … */
  __pyx_t_2 = __Pyx_CyFunction_New(&__pyx_mdef_6Cython_8Compiler_7Visitor_12EnvTransform_7global_scope, __Pyx_CYFUNCTION_CCLASS, __pyx_mstate_global->__pyx_n_u_EnvTransform_global_scope, NULL, __pyx_mstate_global->__pyx_n_u_Cython_Compiler_Visitor, __pyx_mstate_global->__pyx_d, ((PyObject *)__pyx_mstate_global->__pyx_codeobj_tab[24])); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 371, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  #if CYTHON_COMPILING_IN_CPYTHON && PY_VERSION_HEX >= 0x030E0000
  PyUnstable_Object_EnableDeferredRefcount(__pyx_t_2);
  #endif
  if (__Pyx_SetItemOnTypeDict(__pyx_mstate_global->__pyx_ptype_6Cython_8Compiler_7Visitor_EnvTransform, __pyx_mstate_global->__pyx_n_u_global_scope, __pyx_t_2) < (0)) __PYX_ERR(0, 371, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
```

</details>

L372  🔴  (score=10)
```python
        return self.current_env().global_scope()
```
<details><summary>Show generated C (score=10)</summary>

```c
  __Pyx_XDECREF(__pyx_r);
  __pyx_t_4 = ((PyObject *)__pyx_v_self);
  __Pyx_INCREF(__pyx_t_4);
  __pyx_t_5 = 0;
  {
    PyObject *__pyx_callargs[2] = {__pyx_t_4, NULL};
    __pyx_t_3 = __Pyx_PyObject_FastCallMethod((PyObject*)__pyx_mstate_global->__pyx_n_u_current_env, __pyx_callargs+__pyx_t_5, (1-__pyx_t_5) | (1*__Pyx_PY_VECTORCALL_ARGUMENTS_OFFSET));
    __Pyx_XDECREF(__pyx_t_4); __pyx_t_4 = 0;
    if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 372, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_3);
  }
  __pyx_t_2 = __pyx_t_3;
  __Pyx_INCREF(__pyx_t_2);
  __pyx_t_5 = 0;
  {
    PyObject *__pyx_callargs[2] = {__pyx_t_2, NULL};
    __pyx_t_1 = __Pyx_PyObject_FastCallMethod((PyObject*)__pyx_mstate_global->__pyx_n_u_global_scope, __pyx_callargs+__pyx_t_5, (1-__pyx_t_5) | (1*__Pyx_PY_VECTORCALL_ARGUMENTS_OFFSET));
    __Pyx_XDECREF(__pyx_t_2); __pyx_t_2 = 0;
    __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
    if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 372, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_1);
  }
  __pyx_r = __pyx_t_1;
  __pyx_t_1 = 0;
  goto __pyx_L0;
```

</details>

L373  ⚪  (score=0)
```python
```
L374  🔴  (score=41)
```python
    def enter_scope(self, node, scope):
```
<details><summary>Show generated C (score=41)</summary>

```c
/* Python wrapper */
static PyObject *__pyx_pw_6Cython_8Compiler_7Visitor_12EnvTransform_9enter_scope(PyObject *__pyx_v_self, 
#if CYTHON_METH_FASTCALL
PyObject *const *__pyx_args, Py_ssize_t __pyx_nargs, PyObject *__pyx_kwds
#else
PyObject *__pyx_args, PyObject *__pyx_kwds
#endif
); /*proto*/
PyDoc_STRVAR(__pyx_doc_6Cython_8Compiler_7Visitor_12EnvTransform_8enter_scope, "File: Cython/Compiler/Visitor.py (starting at line 374)");
static PyMethodDef __pyx_mdef_6Cython_8Compiler_7Visitor_12EnvTransform_9enter_scope = {"enter_scope", (PyCFunction)(void(*)(void))(__Pyx_PyCFunction_FastCallWithKeywords)__pyx_pw_6Cython_8Compiler_7Visitor_12EnvTransform_9enter_scope, __Pyx_METH_FASTCALL|METH_KEYWORDS, __pyx_doc_6Cython_8Compiler_7Visitor_12EnvTransform_8enter_scope};
static PyObject *__pyx_pw_6Cython_8Compiler_7Visitor_12EnvTransform_9enter_scope(PyObject *__pyx_v_self, 
#if CYTHON_METH_FASTCALL
PyObject *const *__pyx_args, Py_ssize_t __pyx_nargs, PyObject *__pyx_kwds
#else
PyObject *__pyx_args, PyObject *__pyx_kwds
#endif
) {
  PyObject *__pyx_v_node = 0;
  PyObject *__pyx_v_scope = 0;
  #if !CYTHON_METH_FASTCALL
  CYTHON_UNUSED Py_ssize_t __pyx_nargs;
  #endif
  CYTHON_UNUSED PyObject *const *__pyx_kwvalues;
  PyObject *__pyx_r = 0;
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("enter_scope (wrapper)", 0);
  #if !CYTHON_METH_FASTCALL
  #if CYTHON_ASSUME_SAFE_SIZE
  __pyx_nargs = PyTuple_GET_SIZE(__pyx_args);
  #else
  __pyx_nargs = PyTuple_Size(__pyx_args); if (unlikely(__pyx_nargs < 0)) return NULL;
  #endif
  #endif
  __pyx_kwvalues = __Pyx_KwValues_FASTCALL(__pyx_args, __pyx_nargs);
  {
    PyObject ** const __pyx_pyargnames[] = {&__pyx_mstate_global->__pyx_n_u_node,&__pyx_mstate_global->__pyx_n_u_scope,0};
  PyObject* values[2] = {0,0};
    const Py_ssize_t __pyx_kwds_len = (__pyx_kwds) ? __Pyx_NumKwargs_FASTCALL(__pyx_kwds) : 0;
    if (unlikely(__pyx_kwds_len) < 0) __PYX_ERR(0, 374, __pyx_L3_error)
    if (__pyx_kwds_len > 0) {
      switch (__pyx_nargs) {
        case  2:
        values[1] = __Pyx_ArgRef_FASTCALL(__pyx_args, 1);
        if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[1])) __PYX_ERR(0, 374, __pyx_L3_error)
        CYTHON_FALLTHROUGH;
        case  1:
        values[0] = __Pyx_ArgRef_FASTCALL(__pyx_args, 0);
        if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[0])) __PYX_ERR(0, 374, __pyx_L3_error)
        CYTHON_FALLTHROUGH;
        case  0: break;
        default: goto __pyx_L5_argtuple_error;
      }
      const Py_ssize_t kwd_pos_args = __pyx_nargs;
      if (__Pyx_ParseKeywords(__pyx_kwds, __pyx_kwvalues, __pyx_pyargnames, 0, values, kwd_pos_args, __pyx_kwds_len, "enter_scope", 0) < (0)) __PYX_ERR(0, 374, __pyx_L3_error)
      for (Py_ssize_t i = __pyx_nargs; i < 2; i++) {
        if (unlikely(!values[i])) { __Pyx_RaiseArgtupleInvalid("enter_scope", 1, 2, 2, i); __PYX_ERR(0, 374, __pyx_L3_error) }
      }
    } else if (unlikely(__pyx_nargs != 2)) {
      goto __pyx_L5_argtuple_error;
    } else {
      values[0] = __Pyx_ArgRef_FASTCALL(__pyx_args, 0);
      if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[0])) __PYX_ERR(0, 374, __pyx_L3_error)
      values[1] = __Pyx_ArgRef_FASTCALL(__pyx_args, 1);
      if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[1])) __PYX_ERR(0, 374, __pyx_L3_error)
    }
    __pyx_v_node = values[0];
    __pyx_v_scope = values[1];
  }
  goto __pyx_L6_skip;
  __pyx_L5_argtuple_error:;
  __Pyx_RaiseArgtupleInvalid("enter_scope", 1, 2, 2, __pyx_nargs); __PYX_ERR(0, 374, __pyx_L3_error)
  __pyx_L6_skip:;
  goto __pyx_L4_argument_unpacking_done;
  __pyx_L3_error:;
  for (Py_ssize_t __pyx_temp=0; __pyx_temp < (Py_ssize_t)(sizeof(values)/sizeof(values[0])); ++__pyx_temp) {
    Py_XDECREF(values[__pyx_temp]);
  }
  __Pyx_AddTraceback("Cython.Compiler.Visitor.EnvTransform.enter_scope", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __Pyx_RefNannyFinishContext();
  return NULL;
  __pyx_L4_argument_unpacking_done:;
  __pyx_r = __pyx_pf_6Cython_8Compiler_7Visitor_12EnvTransform_8enter_scope(((struct __pyx_obj_6Cython_8Compiler_7Visitor_EnvTransform *)__pyx_v_self), __pyx_v_node, __pyx_v_scope);
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

static PyObject *__pyx_pf_6Cython_8Compiler_7Visitor_12EnvTransform_8enter_scope(struct __pyx_obj_6Cython_8Compiler_7Visitor_EnvTransform *__pyx_v_self, PyObject *__pyx_v_node, PyObject *__pyx_v_scope) {
  PyObject *__pyx_r = NULL;
/* … */
  /* function exit code */
  __pyx_r = Py_None; __Pyx_INCREF(Py_None);
  goto __pyx_L0;
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_t_1);
  __Pyx_AddTraceback("Cython.Compiler.Visitor.EnvTransform.enter_scope", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_r = NULL;
  __pyx_L0:;
  __Pyx_XGIVEREF(__pyx_r);
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}
/* … */
  __pyx_t_2 = __Pyx_CyFunction_New(&__pyx_mdef_6Cython_8Compiler_7Visitor_12EnvTransform_9enter_scope, __Pyx_CYFUNCTION_CCLASS, __pyx_mstate_global->__pyx_n_u_EnvTransform_enter_scope, NULL, __pyx_mstate_global->__pyx_n_u_Cython_Compiler_Visitor, __pyx_mstate_global->__pyx_d, ((PyObject *)__pyx_mstate_global->__pyx_codeobj_tab[25])); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 374, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  #if CYTHON_COMPILING_IN_CPYTHON && PY_VERSION_HEX >= 0x030E0000
  PyUnstable_Object_EnableDeferredRefcount(__pyx_t_2);
  #endif
  if (__Pyx_SetItemOnTypeDict(__pyx_mstate_global->__pyx_ptype_6Cython_8Compiler_7Visitor_EnvTransform, __pyx_mstate_global->__pyx_n_u_enter_scope, __pyx_t_2) < (0)) __PYX_ERR(0, 374, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
```

</details>

L375  🔴  (score=19)
```python
        self.env_stack.append((node, scope))
```
<details><summary>Show generated C (score=19)</summary>

```c
  if (unlikely(__pyx_v_self->env_stack == Py_None)) {
    PyErr_Format(PyExc_AttributeError, "'NoneType' object has no attribute '%.30s'", "append");
    __PYX_ERR(0, 375, __pyx_L1_error)
  }
  __pyx_t_1 = PyTuple_New(2); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 375, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_INCREF(__pyx_v_node);
  __Pyx_GIVEREF(__pyx_v_node);
  if (__Pyx_PyTuple_SET_ITEM(__pyx_t_1, 0, __pyx_v_node) != (0)) __PYX_ERR(0, 375, __pyx_L1_error);
  __Pyx_INCREF(__pyx_v_scope);
  __Pyx_GIVEREF(__pyx_v_scope);
  if (__Pyx_PyTuple_SET_ITEM(__pyx_t_1, 1, __pyx_v_scope) != (0)) __PYX_ERR(0, 375, __pyx_L1_error);
  __pyx_t_2 = __Pyx_PyList_Append(__pyx_v_self->env_stack, __pyx_t_1); if (unlikely(__pyx_t_2 == ((int)-1))) __PYX_ERR(0, 375, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
```

</details>

L376  ⚪  (score=0)
```python
```
L377  🔴  (score=29)
```python
    def exit_scope(self):
```
<details><summary>Show generated C (score=29)</summary>

```c
/* Python wrapper */
static PyObject *__pyx_pw_6Cython_8Compiler_7Visitor_12EnvTransform_11exit_scope(PyObject *__pyx_v_self, 
#if CYTHON_METH_FASTCALL
PyObject *const *__pyx_args, Py_ssize_t __pyx_nargs, PyObject *__pyx_kwds
#else
PyObject *__pyx_args, PyObject *__pyx_kwds
#endif
); /*proto*/
PyDoc_STRVAR(__pyx_doc_6Cython_8Compiler_7Visitor_12EnvTransform_10exit_scope, "File: Cython/Compiler/Visitor.py (starting at line 377)");
static PyMethodDef __pyx_mdef_6Cython_8Compiler_7Visitor_12EnvTransform_11exit_scope = {"exit_scope", (PyCFunction)(void(*)(void))(__Pyx_PyCFunction_FastCallWithKeywords)__pyx_pw_6Cython_8Compiler_7Visitor_12EnvTransform_11exit_scope, __Pyx_METH_FASTCALL|METH_KEYWORDS, __pyx_doc_6Cython_8Compiler_7Visitor_12EnvTransform_10exit_scope};
static PyObject *__pyx_pw_6Cython_8Compiler_7Visitor_12EnvTransform_11exit_scope(PyObject *__pyx_v_self, 
#if CYTHON_METH_FASTCALL
PyObject *const *__pyx_args, Py_ssize_t __pyx_nargs, PyObject *__pyx_kwds
#else
PyObject *__pyx_args, PyObject *__pyx_kwds
#endif
) {
  #if !CYTHON_METH_FASTCALL
  CYTHON_UNUSED Py_ssize_t __pyx_nargs;
  #endif
  CYTHON_UNUSED PyObject *const *__pyx_kwvalues;
  PyObject *__pyx_r = 0;
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("exit_scope (wrapper)", 0);
  #if !CYTHON_METH_FASTCALL
  #if CYTHON_ASSUME_SAFE_SIZE
  __pyx_nargs = PyTuple_GET_SIZE(__pyx_args);
  #else
  __pyx_nargs = PyTuple_Size(__pyx_args); if (unlikely(__pyx_nargs < 0)) return NULL;
  #endif
  #endif
  __pyx_kwvalues = __Pyx_KwValues_FASTCALL(__pyx_args, __pyx_nargs);
  if (unlikely(__pyx_nargs > 0)) { __Pyx_RaiseArgtupleInvalid("exit_scope", 1, 0, 0, __pyx_nargs); return NULL; }
  const Py_ssize_t __pyx_kwds_len = unlikely(__pyx_kwds) ? __Pyx_NumKwargs_FASTCALL(__pyx_kwds) : 0;
  if (unlikely(__pyx_kwds_len < 0)) return NULL;
  if (unlikely(__pyx_kwds_len > 0)) {__Pyx_RejectKeywords("exit_scope", __pyx_kwds); return NULL;}
  __pyx_r = __pyx_pf_6Cython_8Compiler_7Visitor_12EnvTransform_10exit_scope(((struct __pyx_obj_6Cython_8Compiler_7Visitor_EnvTransform *)__pyx_v_self));

  /* function exit code */
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}

static PyObject *__pyx_pf_6Cython_8Compiler_7Visitor_12EnvTransform_10exit_scope(struct __pyx_obj_6Cython_8Compiler_7Visitor_EnvTransform *__pyx_v_self) {
  PyObject *__pyx_r = NULL;
/* … */
  /* function exit code */
  __pyx_r = Py_None; __Pyx_INCREF(Py_None);
  goto __pyx_L0;
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_t_1);
  __Pyx_AddTraceback("Cython.Compiler.Visitor.EnvTransform.exit_scope", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_r = NULL;
  __pyx_L0:;
  __Pyx_XGIVEREF(__pyx_r);
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}
/* … */
  __pyx_t_2 = __Pyx_CyFunction_New(&__pyx_mdef_6Cython_8Compiler_7Visitor_12EnvTransform_11exit_scope, __Pyx_CYFUNCTION_CCLASS, __pyx_mstate_global->__pyx_n_u_EnvTransform_exit_scope, NULL, __pyx_mstate_global->__pyx_n_u_Cython_Compiler_Visitor, __pyx_mstate_global->__pyx_d, ((PyObject *)__pyx_mstate_global->__pyx_codeobj_tab[26])); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 377, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  #if CYTHON_COMPILING_IN_CPYTHON && PY_VERSION_HEX >= 0x030E0000
  PyUnstable_Object_EnableDeferredRefcount(__pyx_t_2);
  #endif
  if (__Pyx_SetItemOnTypeDict(__pyx_mstate_global->__pyx_ptype_6Cython_8Compiler_7Visitor_EnvTransform, __pyx_mstate_global->__pyx_n_u_exit_scope, __pyx_t_2) < (0)) __PYX_ERR(0, 377, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
```

</details>

L378  🟠  (score=8)
```python
        self.env_stack.pop()
```
<details><summary>Show generated C (score=8)</summary>

```c
  if (unlikely(__pyx_v_self->env_stack == Py_None)) {
    PyErr_Format(PyExc_AttributeError, "'NoneType' object has no attribute '%.30s'", "pop");
    __PYX_ERR(0, 378, __pyx_L1_error)
  }
  __pyx_t_1 = __Pyx_PyList_Pop(__pyx_v_self->env_stack); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 378, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
```

</details>

L379  ⚪  (score=0)
```python
```
L380  🔴  (score=38)
```python
    def visit_FuncDefNode(self, node):
```
<details><summary>Show generated C (score=38)</summary>

```c
/* Python wrapper */
static PyObject *__pyx_pw_6Cython_8Compiler_7Visitor_12EnvTransform_13visit_FuncDefNode(PyObject *__pyx_v_self, 
#if CYTHON_METH_FASTCALL
PyObject *const *__pyx_args, Py_ssize_t __pyx_nargs, PyObject *__pyx_kwds
#else
PyObject *__pyx_args, PyObject *__pyx_kwds
#endif
); /*proto*/
PyDoc_STRVAR(__pyx_doc_6Cython_8Compiler_7Visitor_12EnvTransform_12visit_FuncDefNode, "File: Cython/Compiler/Visitor.py (starting at line 380)");
static PyMethodDef __pyx_mdef_6Cython_8Compiler_7Visitor_12EnvTransform_13visit_FuncDefNode = {"visit_FuncDefNode", (PyCFunction)(void(*)(void))(__Pyx_PyCFunction_FastCallWithKeywords)__pyx_pw_6Cython_8Compiler_7Visitor_12EnvTransform_13visit_FuncDefNode, __Pyx_METH_FASTCALL|METH_KEYWORDS, __pyx_doc_6Cython_8Compiler_7Visitor_12EnvTransform_12visit_FuncDefNode};
static PyObject *__pyx_pw_6Cython_8Compiler_7Visitor_12EnvTransform_13visit_FuncDefNode(PyObject *__pyx_v_self, 
#if CYTHON_METH_FASTCALL
PyObject *const *__pyx_args, Py_ssize_t __pyx_nargs, PyObject *__pyx_kwds
#else
PyObject *__pyx_args, PyObject *__pyx_kwds
#endif
) {
  PyObject *__pyx_v_node = 0;
  #if !CYTHON_METH_FASTCALL
  CYTHON_UNUSED Py_ssize_t __pyx_nargs;
  #endif
  CYTHON_UNUSED PyObject *const *__pyx_kwvalues;
  PyObject *__pyx_r = 0;
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("visit_FuncDefNode (wrapper)", 0);
  #if !CYTHON_METH_FASTCALL
  #if CYTHON_ASSUME_SAFE_SIZE
  __pyx_nargs = PyTuple_GET_SIZE(__pyx_args);
  #else
  __pyx_nargs = PyTuple_Size(__pyx_args); if (unlikely(__pyx_nargs < 0)) return NULL;
  #endif
  #endif
  __pyx_kwvalues = __Pyx_KwValues_FASTCALL(__pyx_args, __pyx_nargs);
  {
    PyObject ** const __pyx_pyargnames[] = {&__pyx_mstate_global->__pyx_n_u_node,0};
  PyObject* values[1] = {0};
    const Py_ssize_t __pyx_kwds_len = (__pyx_kwds) ? __Pyx_NumKwargs_FASTCALL(__pyx_kwds) : 0;
    if (unlikely(__pyx_kwds_len) < 0) __PYX_ERR(0, 380, __pyx_L3_error)
    if (__pyx_kwds_len > 0) {
      switch (__pyx_nargs) {
        case  1:
        values[0] = __Pyx_ArgRef_FASTCALL(__pyx_args, 0);
        if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[0])) __PYX_ERR(0, 380, __pyx_L3_error)
        CYTHON_FALLTHROUGH;
        case  0: break;
        default: goto __pyx_L5_argtuple_error;
      }
      const Py_ssize_t kwd_pos_args = __pyx_nargs;
      if (__Pyx_ParseKeywords(__pyx_kwds, __pyx_kwvalues, __pyx_pyargnames, 0, values, kwd_pos_args, __pyx_kwds_len, "visit_FuncDefNode", 0) < (0)) __PYX_ERR(0, 380, __pyx_L3_error)
      for (Py_ssize_t i = __pyx_nargs; i < 1; i++) {
        if (unlikely(!values[i])) { __Pyx_RaiseArgtupleInvalid("visit_FuncDefNode", 1, 1, 1, i); __PYX_ERR(0, 380, __pyx_L3_error) }
      }
    } else if (unlikely(__pyx_nargs != 1)) {
      goto __pyx_L5_argtuple_error;
    } else {
      values[0] = __Pyx_ArgRef_FASTCALL(__pyx_args, 0);
      if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[0])) __PYX_ERR(0, 380, __pyx_L3_error)
    }
    __pyx_v_node = values[0];
  }
  goto __pyx_L6_skip;
  __pyx_L5_argtuple_error:;
  __Pyx_RaiseArgtupleInvalid("visit_FuncDefNode", 1, 1, 1, __pyx_nargs); __PYX_ERR(0, 380, __pyx_L3_error)
  __pyx_L6_skip:;
  goto __pyx_L4_argument_unpacking_done;
  __pyx_L3_error:;
  for (Py_ssize_t __pyx_temp=0; __pyx_temp < (Py_ssize_t)(sizeof(values)/sizeof(values[0])); ++__pyx_temp) {
    Py_XDECREF(values[__pyx_temp]);
  }
  __Pyx_AddTraceback("Cython.Compiler.Visitor.EnvTransform.visit_FuncDefNode", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __Pyx_RefNannyFinishContext();
  return NULL;
  __pyx_L4_argument_unpacking_done:;
  __pyx_r = __pyx_pf_6Cython_8Compiler_7Visitor_12EnvTransform_12visit_FuncDefNode(((struct __pyx_obj_6Cython_8Compiler_7Visitor_EnvTransform *)__pyx_v_self), __pyx_v_node);
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

static PyObject *__pyx_pf_6Cython_8Compiler_7Visitor_12EnvTransform_12visit_FuncDefNode(struct __pyx_obj_6Cython_8Compiler_7Visitor_EnvTransform *__pyx_v_self, PyObject *__pyx_v_node) {
  PyObject *__pyx_r = NULL;
/* … */
  /* function exit code */
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_t_1);
  __Pyx_XDECREF(__pyx_t_2);
  __Pyx_XDECREF(__pyx_t_4);
  __Pyx_AddTraceback("Cython.Compiler.Visitor.EnvTransform.visit_FuncDefNode", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_r = NULL;
  __pyx_L0:;
  __Pyx_XGIVEREF(__pyx_r);
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}
/* … */
  __pyx_t_2 = __Pyx_CyFunction_New(&__pyx_mdef_6Cython_8Compiler_7Visitor_12EnvTransform_13visit_FuncDefNode, __Pyx_CYFUNCTION_CCLASS, __pyx_mstate_global->__pyx_n_u_EnvTransform_visit_FuncDefNode, NULL, __pyx_mstate_global->__pyx_n_u_Cython_Compiler_Visitor, __pyx_mstate_global->__pyx_d, ((PyObject *)__pyx_mstate_global->__pyx_codeobj_tab[27])); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 380, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  #if CYTHON_COMPILING_IN_CPYTHON && PY_VERSION_HEX >= 0x030E0000
  PyUnstable_Object_EnableDeferredRefcount(__pyx_t_2);
  #endif
  if (__Pyx_SetItemOnTypeDict(__pyx_mstate_global->__pyx_ptype_6Cython_8Compiler_7Visitor_EnvTransform, __pyx_mstate_global->__pyx_n_u_visit_FuncDefNode, __pyx_t_2) < (0)) __PYX_ERR(0, 380, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
```

</details>

L381  🟠  (score=5)
```python
        self.visit_func_outer_attrs(node)
```
<details><summary>Show generated C (score=5)</summary>

```c
  __pyx_t_2 = ((PyObject *)__pyx_v_self);
  __Pyx_INCREF(__pyx_t_2);
  __pyx_t_3 = 0;
  {
    PyObject *__pyx_callargs[2] = {__pyx_t_2, __pyx_v_node};
    __pyx_t_1 = __Pyx_PyObject_FastCallMethod((PyObject*)__pyx_mstate_global->__pyx_n_u_visit_func_outer_attrs, __pyx_callargs+__pyx_t_3, (2-__pyx_t_3) | (1*__Pyx_PY_VECTORCALL_ARGUMENTS_OFFSET));
    __Pyx_XDECREF(__pyx_t_2); __pyx_t_2 = 0;
    if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 381, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_1);
  }
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
```

</details>

L382  🟠  (score=8)
```python
        self.enter_scope(node, node.local_scope)
```
<details><summary>Show generated C (score=8)</summary>

```c
  __pyx_t_2 = ((PyObject *)__pyx_v_self);
  __Pyx_INCREF(__pyx_t_2);
  __pyx_t_4 = __Pyx_PyObject_GetAttrStr(__pyx_v_node, __pyx_mstate_global->__pyx_n_u_local_scope); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 382, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_4);
  __pyx_t_3 = 0;
  {
    PyObject *__pyx_callargs[3] = {__pyx_t_2, __pyx_v_node, __pyx_t_4};
    __pyx_t_1 = __Pyx_PyObject_FastCallMethod((PyObject*)__pyx_mstate_global->__pyx_n_u_enter_scope, __pyx_callargs+__pyx_t_3, (3-__pyx_t_3) | (1*__Pyx_PY_VECTORCALL_ARGUMENTS_OFFSET));
    __Pyx_XDECREF(__pyx_t_2); __pyx_t_2 = 0;
    __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
    if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 382, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_1);
  }
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
```

</details>

L383  🟡  (score=4)
```python
        self.visitchildren(node, attrs=None, exclude=node.outer_attrs)
```
<details><summary>Show generated C (score=4)</summary>

```c
  __pyx_t_1 = __Pyx_PyObject_GetAttrStr(__pyx_v_node, __pyx_mstate_global->__pyx_n_u_outer_attrs); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 383, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __pyx_t_5.__pyx_n = 2;
  __pyx_t_5.attrs = Py_None;
  __pyx_t_5.exclude = __pyx_t_1;
  __pyx_t_4 = ((struct __pyx_vtabstruct_6Cython_8Compiler_7Visitor_EnvTransform *)__pyx_v_self->__pyx_base.__pyx_base.__pyx_base.__pyx_vtab)->__pyx_base.__pyx_base.__pyx_base.visitchildren(((struct __pyx_obj_6Cython_8Compiler_7Visitor_TreeVisitor *)__pyx_v_self), __pyx_v_node, 0, &__pyx_t_5); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 383, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_4);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
```

</details>

L384  🟠  (score=5)
```python
        self.exit_scope()
```
<details><summary>Show generated C (score=5)</summary>

```c
  __pyx_t_1 = ((PyObject *)__pyx_v_self);
  __Pyx_INCREF(__pyx_t_1);
  __pyx_t_3 = 0;
  {
    PyObject *__pyx_callargs[2] = {__pyx_t_1, NULL};
    __pyx_t_4 = __Pyx_PyObject_FastCallMethod((PyObject*)__pyx_mstate_global->__pyx_n_u_exit_scope, __pyx_callargs+__pyx_t_3, (1-__pyx_t_3) | (1*__Pyx_PY_VECTORCALL_ARGUMENTS_OFFSET));
    __Pyx_XDECREF(__pyx_t_1); __pyx_t_1 = 0;
    if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 384, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_4);
  }
  __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
```

</details>

L385  🟡  (score=2)
```python
        return node
```
<details><summary>Show generated C (score=2)</summary>

```c
  __Pyx_XDECREF(__pyx_r);
  __Pyx_INCREF(__pyx_v_node);
  __pyx_r = __pyx_v_node;
  goto __pyx_L0;
```

</details>

L386  ⚪  (score=0)
```python
```
L387  🔴  (score=38)
```python
    def visit_func_outer_attrs(self, node):
```
<details><summary>Show generated C (score=38)</summary>

```c
/* Python wrapper */
static PyObject *__pyx_pw_6Cython_8Compiler_7Visitor_12EnvTransform_15visit_func_outer_attrs(PyObject *__pyx_v_self, 
#if CYTHON_METH_FASTCALL
PyObject *const *__pyx_args, Py_ssize_t __pyx_nargs, PyObject *__pyx_kwds
#else
PyObject *__pyx_args, PyObject *__pyx_kwds
#endif
); /*proto*/
PyDoc_STRVAR(__pyx_doc_6Cython_8Compiler_7Visitor_12EnvTransform_14visit_func_outer_attrs, "File: Cython/Compiler/Visitor.py (starting at line 387)");
static PyMethodDef __pyx_mdef_6Cython_8Compiler_7Visitor_12EnvTransform_15visit_func_outer_attrs = {"visit_func_outer_attrs", (PyCFunction)(void(*)(void))(__Pyx_PyCFunction_FastCallWithKeywords)__pyx_pw_6Cython_8Compiler_7Visitor_12EnvTransform_15visit_func_outer_attrs, __Pyx_METH_FASTCALL|METH_KEYWORDS, __pyx_doc_6Cython_8Compiler_7Visitor_12EnvTransform_14visit_func_outer_attrs};
static PyObject *__pyx_pw_6Cython_8Compiler_7Visitor_12EnvTransform_15visit_func_outer_attrs(PyObject *__pyx_v_self, 
#if CYTHON_METH_FASTCALL
PyObject *const *__pyx_args, Py_ssize_t __pyx_nargs, PyObject *__pyx_kwds
#else
PyObject *__pyx_args, PyObject *__pyx_kwds
#endif
) {
  PyObject *__pyx_v_node = 0;
  #if !CYTHON_METH_FASTCALL
  CYTHON_UNUSED Py_ssize_t __pyx_nargs;
  #endif
  CYTHON_UNUSED PyObject *const *__pyx_kwvalues;
  PyObject *__pyx_r = 0;
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("visit_func_outer_attrs (wrapper)", 0);
  #if !CYTHON_METH_FASTCALL
  #if CYTHON_ASSUME_SAFE_SIZE
  __pyx_nargs = PyTuple_GET_SIZE(__pyx_args);
  #else
  __pyx_nargs = PyTuple_Size(__pyx_args); if (unlikely(__pyx_nargs < 0)) return NULL;
  #endif
  #endif
  __pyx_kwvalues = __Pyx_KwValues_FASTCALL(__pyx_args, __pyx_nargs);
  {
    PyObject ** const __pyx_pyargnames[] = {&__pyx_mstate_global->__pyx_n_u_node,0};
  PyObject* values[1] = {0};
    const Py_ssize_t __pyx_kwds_len = (__pyx_kwds) ? __Pyx_NumKwargs_FASTCALL(__pyx_kwds) : 0;
    if (unlikely(__pyx_kwds_len) < 0) __PYX_ERR(0, 387, __pyx_L3_error)
    if (__pyx_kwds_len > 0) {
      switch (__pyx_nargs) {
        case  1:
        values[0] = __Pyx_ArgRef_FASTCALL(__pyx_args, 0);
        if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[0])) __PYX_ERR(0, 387, __pyx_L3_error)
        CYTHON_FALLTHROUGH;
        case  0: break;
        default: goto __pyx_L5_argtuple_error;
      }
      const Py_ssize_t kwd_pos_args = __pyx_nargs;
      if (__Pyx_ParseKeywords(__pyx_kwds, __pyx_kwvalues, __pyx_pyargnames, 0, values, kwd_pos_args, __pyx_kwds_len, "visit_func_outer_attrs", 0) < (0)) __PYX_ERR(0, 387, __pyx_L3_error)
      for (Py_ssize_t i = __pyx_nargs; i < 1; i++) {
        if (unlikely(!values[i])) { __Pyx_RaiseArgtupleInvalid("visit_func_outer_attrs", 1, 1, 1, i); __PYX_ERR(0, 387, __pyx_L3_error) }
      }
    } else if (unlikely(__pyx_nargs != 1)) {
      goto __pyx_L5_argtuple_error;
    } else {
      values[0] = __Pyx_ArgRef_FASTCALL(__pyx_args, 0);
      if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[0])) __PYX_ERR(0, 387, __pyx_L3_error)
    }
    __pyx_v_node = values[0];
  }
  goto __pyx_L6_skip;
  __pyx_L5_argtuple_error:;
  __Pyx_RaiseArgtupleInvalid("visit_func_outer_attrs", 1, 1, 1, __pyx_nargs); __PYX_ERR(0, 387, __pyx_L3_error)
  __pyx_L6_skip:;
  goto __pyx_L4_argument_unpacking_done;
  __pyx_L3_error:;
  for (Py_ssize_t __pyx_temp=0; __pyx_temp < (Py_ssize_t)(sizeof(values)/sizeof(values[0])); ++__pyx_temp) {
    Py_XDECREF(values[__pyx_temp]);
  }
  __Pyx_AddTraceback("Cython.Compiler.Visitor.EnvTransform.visit_func_outer_attrs", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __Pyx_RefNannyFinishContext();
  return NULL;
  __pyx_L4_argument_unpacking_done:;
  __pyx_r = __pyx_pf_6Cython_8Compiler_7Visitor_12EnvTransform_14visit_func_outer_attrs(((struct __pyx_obj_6Cython_8Compiler_7Visitor_EnvTransform *)__pyx_v_self), __pyx_v_node);
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

static PyObject *__pyx_pf_6Cython_8Compiler_7Visitor_12EnvTransform_14visit_func_outer_attrs(struct __pyx_obj_6Cython_8Compiler_7Visitor_EnvTransform *__pyx_v_self, PyObject *__pyx_v_node) {
  PyObject *__pyx_r = NULL;
/* … */
  /* function exit code */
  __pyx_r = Py_None; __Pyx_INCREF(Py_None);
  goto __pyx_L0;
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_t_1);
  __Pyx_XDECREF(__pyx_t_2);
  __Pyx_AddTraceback("Cython.Compiler.Visitor.EnvTransform.visit_func_outer_attrs", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_r = NULL;
  __pyx_L0:;
  __Pyx_XGIVEREF(__pyx_r);
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}
/* … */
  __pyx_t_2 = __Pyx_CyFunction_New(&__pyx_mdef_6Cython_8Compiler_7Visitor_12EnvTransform_15visit_func_outer_attrs, __Pyx_CYFUNCTION_CCLASS, __pyx_mstate_global->__pyx_n_u_EnvTransform_visit_func_outer_at, NULL, __pyx_mstate_global->__pyx_n_u_Cython_Compiler_Visitor, __pyx_mstate_global->__pyx_d, ((PyObject *)__pyx_mstate_global->__pyx_codeobj_tab[28])); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 387, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  #if CYTHON_COMPILING_IN_CPYTHON && PY_VERSION_HEX >= 0x030E0000
  PyUnstable_Object_EnableDeferredRefcount(__pyx_t_2);
  #endif
  if (__Pyx_SetItemOnTypeDict(__pyx_mstate_global->__pyx_ptype_6Cython_8Compiler_7Visitor_EnvTransform, __pyx_mstate_global->__pyx_n_u_visit_func_outer_attrs, __pyx_t_2) < (0)) __PYX_ERR(0, 387, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
```

</details>

L388  🟡  (score=4)
```python
        self.visitchildren(node, attrs=node.outer_attrs)
```
<details><summary>Show generated C (score=4)</summary>

```c
  __pyx_t_1 = __Pyx_PyObject_GetAttrStr(__pyx_v_node, __pyx_mstate_global->__pyx_n_u_outer_attrs); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 388, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __pyx_t_3.__pyx_n = 1;
  __pyx_t_3.attrs = __pyx_t_1;
  __pyx_t_2 = ((struct __pyx_vtabstruct_6Cython_8Compiler_7Visitor_EnvTransform *)__pyx_v_self->__pyx_base.__pyx_base.__pyx_base.__pyx_vtab)->__pyx_base.__pyx_base.__pyx_base.visitchildren(((struct __pyx_obj_6Cython_8Compiler_7Visitor_TreeVisitor *)__pyx_v_self), __pyx_v_node, 0, &__pyx_t_3); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 388, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
```

</details>

L389  ⚪  (score=0)
```python
```
L390  🔴  (score=36)
```python
    def visit_GeneratorBodyDefNode(self, node):
```
<details><summary>Show generated C (score=36)</summary>

```c
/* Python wrapper */
static PyObject *__pyx_pw_6Cython_8Compiler_7Visitor_12EnvTransform_17visit_GeneratorBodyDefNode(PyObject *__pyx_v_self, 
#if CYTHON_METH_FASTCALL
PyObject *const *__pyx_args, Py_ssize_t __pyx_nargs, PyObject *__pyx_kwds
#else
PyObject *__pyx_args, PyObject *__pyx_kwds
#endif
); /*proto*/
PyDoc_STRVAR(__pyx_doc_6Cython_8Compiler_7Visitor_12EnvTransform_16visit_GeneratorBodyDefNode, "File: Cython/Compiler/Visitor.py (starting at line 390)");
static PyMethodDef __pyx_mdef_6Cython_8Compiler_7Visitor_12EnvTransform_17visit_GeneratorBodyDefNode = {"visit_GeneratorBodyDefNode", (PyCFunction)(void(*)(void))(__Pyx_PyCFunction_FastCallWithKeywords)__pyx_pw_6Cython_8Compiler_7Visitor_12EnvTransform_17visit_GeneratorBodyDefNode, __Pyx_METH_FASTCALL|METH_KEYWORDS, __pyx_doc_6Cython_8Compiler_7Visitor_12EnvTransform_16visit_GeneratorBodyDefNode};
static PyObject *__pyx_pw_6Cython_8Compiler_7Visitor_12EnvTransform_17visit_GeneratorBodyDefNode(PyObject *__pyx_v_self, 
#if CYTHON_METH_FASTCALL
PyObject *const *__pyx_args, Py_ssize_t __pyx_nargs, PyObject *__pyx_kwds
#else
PyObject *__pyx_args, PyObject *__pyx_kwds
#endif
) {
  PyObject *__pyx_v_node = 0;
  #if !CYTHON_METH_FASTCALL
  CYTHON_UNUSED Py_ssize_t __pyx_nargs;
  #endif
  CYTHON_UNUSED PyObject *const *__pyx_kwvalues;
  PyObject *__pyx_r = 0;
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("visit_GeneratorBodyDefNode (wrapper)", 0);
  #if !CYTHON_METH_FASTCALL
  #if CYTHON_ASSUME_SAFE_SIZE
  __pyx_nargs = PyTuple_GET_SIZE(__pyx_args);
  #else
  __pyx_nargs = PyTuple_Size(__pyx_args); if (unlikely(__pyx_nargs < 0)) return NULL;
  #endif
  #endif
  __pyx_kwvalues = __Pyx_KwValues_FASTCALL(__pyx_args, __pyx_nargs);
  {
    PyObject ** const __pyx_pyargnames[] = {&__pyx_mstate_global->__pyx_n_u_node,0};
  PyObject* values[1] = {0};
    const Py_ssize_t __pyx_kwds_len = (__pyx_kwds) ? __Pyx_NumKwargs_FASTCALL(__pyx_kwds) : 0;
    if (unlikely(__pyx_kwds_len) < 0) __PYX_ERR(0, 390, __pyx_L3_error)
    if (__pyx_kwds_len > 0) {
      switch (__pyx_nargs) {
        case  1:
        values[0] = __Pyx_ArgRef_FASTCALL(__pyx_args, 0);
        if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[0])) __PYX_ERR(0, 390, __pyx_L3_error)
        CYTHON_FALLTHROUGH;
        case  0: break;
        default: goto __pyx_L5_argtuple_error;
      }
      const Py_ssize_t kwd_pos_args = __pyx_nargs;
      if (__Pyx_ParseKeywords(__pyx_kwds, __pyx_kwvalues, __pyx_pyargnames, 0, values, kwd_pos_args, __pyx_kwds_len, "visit_GeneratorBodyDefNode", 0) < (0)) __PYX_ERR(0, 390, __pyx_L3_error)
      for (Py_ssize_t i = __pyx_nargs; i < 1; i++) {
        if (unlikely(!values[i])) { __Pyx_RaiseArgtupleInvalid("visit_GeneratorBodyDefNode", 1, 1, 1, i); __PYX_ERR(0, 390, __pyx_L3_error) }
      }
    } else if (unlikely(__pyx_nargs != 1)) {
      goto __pyx_L5_argtuple_error;
    } else {
      values[0] = __Pyx_ArgRef_FASTCALL(__pyx_args, 0);
      if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[0])) __PYX_ERR(0, 390, __pyx_L3_error)
    }
    __pyx_v_node = values[0];
  }
  goto __pyx_L6_skip;
  __pyx_L5_argtuple_error:;
  __Pyx_RaiseArgtupleInvalid("visit_GeneratorBodyDefNode", 1, 1, 1, __pyx_nargs); __PYX_ERR(0, 390, __pyx_L3_error)
  __pyx_L6_skip:;
  goto __pyx_L4_argument_unpacking_done;
  __pyx_L3_error:;
  for (Py_ssize_t __pyx_temp=0; __pyx_temp < (Py_ssize_t)(sizeof(values)/sizeof(values[0])); ++__pyx_temp) {
    Py_XDECREF(values[__pyx_temp]);
  }
  __Pyx_AddTraceback("Cython.Compiler.Visitor.EnvTransform.visit_GeneratorBodyDefNode", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __Pyx_RefNannyFinishContext();
  return NULL;
  __pyx_L4_argument_unpacking_done:;
  __pyx_r = __pyx_pf_6Cython_8Compiler_7Visitor_12EnvTransform_16visit_GeneratorBodyDefNode(((struct __pyx_obj_6Cython_8Compiler_7Visitor_EnvTransform *)__pyx_v_self), __pyx_v_node);
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

static PyObject *__pyx_pf_6Cython_8Compiler_7Visitor_12EnvTransform_16visit_GeneratorBodyDefNode(struct __pyx_obj_6Cython_8Compiler_7Visitor_EnvTransform *__pyx_v_self, PyObject *__pyx_v_node) {
  PyObject *__pyx_r = NULL;
/* … */
  /* function exit code */
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_t_1);
  __Pyx_AddTraceback("Cython.Compiler.Visitor.EnvTransform.visit_GeneratorBodyDefNode", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_r = NULL;
  __pyx_L0:;
  __Pyx_XGIVEREF(__pyx_r);
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}
/* … */
  __pyx_t_2 = __Pyx_CyFunction_New(&__pyx_mdef_6Cython_8Compiler_7Visitor_12EnvTransform_17visit_GeneratorBodyDefNode, __Pyx_CYFUNCTION_CCLASS, __pyx_mstate_global->__pyx_n_u_EnvTransform_visit_GeneratorBody, NULL, __pyx_mstate_global->__pyx_n_u_Cython_Compiler_Visitor, __pyx_mstate_global->__pyx_d, ((PyObject *)__pyx_mstate_global->__pyx_codeobj_tab[29])); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 390, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  #if CYTHON_COMPILING_IN_CPYTHON && PY_VERSION_HEX >= 0x030E0000
  PyUnstable_Object_EnableDeferredRefcount(__pyx_t_2);
  #endif
  if (__Pyx_SetItemOnTypeDict(__pyx_mstate_global->__pyx_ptype_6Cython_8Compiler_7Visitor_EnvTransform, __pyx_mstate_global->__pyx_n_u_visit_GeneratorBodyDefNode, __pyx_t_2) < (0)) __PYX_ERR(0, 390, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
```

</details>

L391  🟡  (score=1)
```python
        self._process_children(node)
```
<details><summary>Show generated C (score=1)</summary>

```c
  __pyx_t_1 = ((struct __pyx_vtabstruct_6Cython_8Compiler_7Visitor_EnvTransform *)__pyx_v_self->__pyx_base.__pyx_base.__pyx_base.__pyx_vtab)->__pyx_base.__pyx_base._process_children(((struct __pyx_obj_6Cython_8Compiler_7Visitor_VisitorTransform *)__pyx_v_self), __pyx_v_node, NULL); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 391, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
```

</details>

L392  🟡  (score=2)
```python
        return node
```
<details><summary>Show generated C (score=2)</summary>

```c
  __Pyx_XDECREF(__pyx_r);
  __Pyx_INCREF(__pyx_v_node);
  __pyx_r = __pyx_v_node;
  goto __pyx_L0;
```

</details>

L393  ⚪  (score=0)
```python
```
L394  🔴  (score=38)
```python
    def visit_ClassDefNode(self, node):
```
<details><summary>Show generated C (score=38)</summary>

```c
/* Python wrapper */
static PyObject *__pyx_pw_6Cython_8Compiler_7Visitor_12EnvTransform_19visit_ClassDefNode(PyObject *__pyx_v_self, 
#if CYTHON_METH_FASTCALL
PyObject *const *__pyx_args, Py_ssize_t __pyx_nargs, PyObject *__pyx_kwds
#else
PyObject *__pyx_args, PyObject *__pyx_kwds
#endif
); /*proto*/
PyDoc_STRVAR(__pyx_doc_6Cython_8Compiler_7Visitor_12EnvTransform_18visit_ClassDefNode, "File: Cython/Compiler/Visitor.py (starting at line 394)");
static PyMethodDef __pyx_mdef_6Cython_8Compiler_7Visitor_12EnvTransform_19visit_ClassDefNode = {"visit_ClassDefNode", (PyCFunction)(void(*)(void))(__Pyx_PyCFunction_FastCallWithKeywords)__pyx_pw_6Cython_8Compiler_7Visitor_12EnvTransform_19visit_ClassDefNode, __Pyx_METH_FASTCALL|METH_KEYWORDS, __pyx_doc_6Cython_8Compiler_7Visitor_12EnvTransform_18visit_ClassDefNode};
static PyObject *__pyx_pw_6Cython_8Compiler_7Visitor_12EnvTransform_19visit_ClassDefNode(PyObject *__pyx_v_self, 
#if CYTHON_METH_FASTCALL
PyObject *const *__pyx_args, Py_ssize_t __pyx_nargs, PyObject *__pyx_kwds
#else
PyObject *__pyx_args, PyObject *__pyx_kwds
#endif
) {
  PyObject *__pyx_v_node = 0;
  #if !CYTHON_METH_FASTCALL
  CYTHON_UNUSED Py_ssize_t __pyx_nargs;
  #endif
  CYTHON_UNUSED PyObject *const *__pyx_kwvalues;
  PyObject *__pyx_r = 0;
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("visit_ClassDefNode (wrapper)", 0);
  #if !CYTHON_METH_FASTCALL
  #if CYTHON_ASSUME_SAFE_SIZE
  __pyx_nargs = PyTuple_GET_SIZE(__pyx_args);
  #else
  __pyx_nargs = PyTuple_Size(__pyx_args); if (unlikely(__pyx_nargs < 0)) return NULL;
  #endif
  #endif
  __pyx_kwvalues = __Pyx_KwValues_FASTCALL(__pyx_args, __pyx_nargs);
  {
    PyObject ** const __pyx_pyargnames[] = {&__pyx_mstate_global->__pyx_n_u_node,0};
  PyObject* values[1] = {0};
    const Py_ssize_t __pyx_kwds_len = (__pyx_kwds) ? __Pyx_NumKwargs_FASTCALL(__pyx_kwds) : 0;
    if (unlikely(__pyx_kwds_len) < 0) __PYX_ERR(0, 394, __pyx_L3_error)
    if (__pyx_kwds_len > 0) {
      switch (__pyx_nargs) {
        case  1:
        values[0] = __Pyx_ArgRef_FASTCALL(__pyx_args, 0);
        if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[0])) __PYX_ERR(0, 394, __pyx_L3_error)
        CYTHON_FALLTHROUGH;
        case  0: break;
        default: goto __pyx_L5_argtuple_error;
      }
      const Py_ssize_t kwd_pos_args = __pyx_nargs;
      if (__Pyx_ParseKeywords(__pyx_kwds, __pyx_kwvalues, __pyx_pyargnames, 0, values, kwd_pos_args, __pyx_kwds_len, "visit_ClassDefNode", 0) < (0)) __PYX_ERR(0, 394, __pyx_L3_error)
      for (Py_ssize_t i = __pyx_nargs; i < 1; i++) {
        if (unlikely(!values[i])) { __Pyx_RaiseArgtupleInvalid("visit_ClassDefNode", 1, 1, 1, i); __PYX_ERR(0, 394, __pyx_L3_error) }
      }
    } else if (unlikely(__pyx_nargs != 1)) {
      goto __pyx_L5_argtuple_error;
    } else {
      values[0] = __Pyx_ArgRef_FASTCALL(__pyx_args, 0);
      if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[0])) __PYX_ERR(0, 394, __pyx_L3_error)
    }
    __pyx_v_node = values[0];
  }
  goto __pyx_L6_skip;
  __pyx_L5_argtuple_error:;
  __Pyx_RaiseArgtupleInvalid("visit_ClassDefNode", 1, 1, 1, __pyx_nargs); __PYX_ERR(0, 394, __pyx_L3_error)
  __pyx_L6_skip:;
  goto __pyx_L4_argument_unpacking_done;
  __pyx_L3_error:;
  for (Py_ssize_t __pyx_temp=0; __pyx_temp < (Py_ssize_t)(sizeof(values)/sizeof(values[0])); ++__pyx_temp) {
    Py_XDECREF(values[__pyx_temp]);
  }
  __Pyx_AddTraceback("Cython.Compiler.Visitor.EnvTransform.visit_ClassDefNode", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __Pyx_RefNannyFinishContext();
  return NULL;
  __pyx_L4_argument_unpacking_done:;
  __pyx_r = __pyx_pf_6Cython_8Compiler_7Visitor_12EnvTransform_18visit_ClassDefNode(((struct __pyx_obj_6Cython_8Compiler_7Visitor_EnvTransform *)__pyx_v_self), __pyx_v_node);
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

static PyObject *__pyx_pf_6Cython_8Compiler_7Visitor_12EnvTransform_18visit_ClassDefNode(struct __pyx_obj_6Cython_8Compiler_7Visitor_EnvTransform *__pyx_v_self, PyObject *__pyx_v_node) {
  PyObject *__pyx_r = NULL;
/* … */
  /* function exit code */
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_t_1);
  __Pyx_XDECREF(__pyx_t_2);
  __Pyx_XDECREF(__pyx_t_3);
  __Pyx_AddTraceback("Cython.Compiler.Visitor.EnvTransform.visit_ClassDefNode", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_r = NULL;
  __pyx_L0:;
  __Pyx_XGIVEREF(__pyx_r);
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}
/* … */
  __pyx_t_2 = __Pyx_CyFunction_New(&__pyx_mdef_6Cython_8Compiler_7Visitor_12EnvTransform_19visit_ClassDefNode, __Pyx_CYFUNCTION_CCLASS, __pyx_mstate_global->__pyx_n_u_EnvTransform_visit_ClassDefNode, NULL, __pyx_mstate_global->__pyx_n_u_Cython_Compiler_Visitor, __pyx_mstate_global->__pyx_d, ((PyObject *)__pyx_mstate_global->__pyx_codeobj_tab[30])); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 394, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  #if CYTHON_COMPILING_IN_CPYTHON && PY_VERSION_HEX >= 0x030E0000
  PyUnstable_Object_EnableDeferredRefcount(__pyx_t_2);
  #endif
  if (__Pyx_SetItemOnTypeDict(__pyx_mstate_global->__pyx_ptype_6Cython_8Compiler_7Visitor_EnvTransform, __pyx_mstate_global->__pyx_n_u_visit_ClassDefNode, __pyx_t_2) < (0)) __PYX_ERR(0, 394, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
```

</details>

L395  🟠  (score=8)
```python
        self.enter_scope(node, node.scope)
```
<details><summary>Show generated C (score=8)</summary>

```c
  __pyx_t_2 = ((PyObject *)__pyx_v_self);
  __Pyx_INCREF(__pyx_t_2);
  __pyx_t_3 = __Pyx_PyObject_GetAttrStr(__pyx_v_node, __pyx_mstate_global->__pyx_n_u_scope); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 395, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_3);
  __pyx_t_4 = 0;
  {
    PyObject *__pyx_callargs[3] = {__pyx_t_2, __pyx_v_node, __pyx_t_3};
    __pyx_t_1 = __Pyx_PyObject_FastCallMethod((PyObject*)__pyx_mstate_global->__pyx_n_u_enter_scope, __pyx_callargs+__pyx_t_4, (3-__pyx_t_4) | (1*__Pyx_PY_VECTORCALL_ARGUMENTS_OFFSET));
    __Pyx_XDECREF(__pyx_t_2); __pyx_t_2 = 0;
    __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
    if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 395, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_1);
  }
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
```

</details>

L396  🟡  (score=1)
```python
        self._process_children(node)
```
<details><summary>Show generated C (score=1)</summary>

```c
  __pyx_t_1 = ((struct __pyx_vtabstruct_6Cython_8Compiler_7Visitor_EnvTransform *)__pyx_v_self->__pyx_base.__pyx_base.__pyx_base.__pyx_vtab)->__pyx_base.__pyx_base._process_children(((struct __pyx_obj_6Cython_8Compiler_7Visitor_VisitorTransform *)__pyx_v_self), __pyx_v_node, NULL); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 396, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
```

</details>

L397  🟠  (score=5)
```python
        self.exit_scope()
```
<details><summary>Show generated C (score=5)</summary>

```c
  __pyx_t_3 = ((PyObject *)__pyx_v_self);
  __Pyx_INCREF(__pyx_t_3);
  __pyx_t_4 = 0;
  {
    PyObject *__pyx_callargs[2] = {__pyx_t_3, NULL};
    __pyx_t_1 = __Pyx_PyObject_FastCallMethod((PyObject*)__pyx_mstate_global->__pyx_n_u_exit_scope, __pyx_callargs+__pyx_t_4, (1-__pyx_t_4) | (1*__Pyx_PY_VECTORCALL_ARGUMENTS_OFFSET));
    __Pyx_XDECREF(__pyx_t_3); __pyx_t_3 = 0;
    if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 397, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_1);
  }
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
```

</details>

L398  🟡  (score=2)
```python
        return node
```
<details><summary>Show generated C (score=2)</summary>

```c
  __Pyx_XDECREF(__pyx_r);
  __Pyx_INCREF(__pyx_v_node);
  __pyx_r = __pyx_v_node;
  goto __pyx_L0;
```

</details>

L399  ⚪  (score=0)
```python
```
L400  🔴  (score=38)
```python
    def visit_CStructOrUnionDefNode(self, node):
```
<details><summary>Show generated C (score=38)</summary>

```c
/* Python wrapper */
static PyObject *__pyx_pw_6Cython_8Compiler_7Visitor_12EnvTransform_21visit_CStructOrUnionDefNode(PyObject *__pyx_v_self, 
#if CYTHON_METH_FASTCALL
PyObject *const *__pyx_args, Py_ssize_t __pyx_nargs, PyObject *__pyx_kwds
#else
PyObject *__pyx_args, PyObject *__pyx_kwds
#endif
); /*proto*/
PyDoc_STRVAR(__pyx_doc_6Cython_8Compiler_7Visitor_12EnvTransform_20visit_CStructOrUnionDefNode, "File: Cython/Compiler/Visitor.py (starting at line 400)");
static PyMethodDef __pyx_mdef_6Cython_8Compiler_7Visitor_12EnvTransform_21visit_CStructOrUnionDefNode = {"visit_CStructOrUnionDefNode", (PyCFunction)(void(*)(void))(__Pyx_PyCFunction_FastCallWithKeywords)__pyx_pw_6Cython_8Compiler_7Visitor_12EnvTransform_21visit_CStructOrUnionDefNode, __Pyx_METH_FASTCALL|METH_KEYWORDS, __pyx_doc_6Cython_8Compiler_7Visitor_12EnvTransform_20visit_CStructOrUnionDefNode};
static PyObject *__pyx_pw_6Cython_8Compiler_7Visitor_12EnvTransform_21visit_CStructOrUnionDefNode(PyObject *__pyx_v_self, 
#if CYTHON_METH_FASTCALL
PyObject *const *__pyx_args, Py_ssize_t __pyx_nargs, PyObject *__pyx_kwds
#else
PyObject *__pyx_args, PyObject *__pyx_kwds
#endif
) {
  PyObject *__pyx_v_node = 0;
  #if !CYTHON_METH_FASTCALL
  CYTHON_UNUSED Py_ssize_t __pyx_nargs;
  #endif
  CYTHON_UNUSED PyObject *const *__pyx_kwvalues;
  PyObject *__pyx_r = 0;
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("visit_CStructOrUnionDefNode (wrapper)", 0);
  #if !CYTHON_METH_FASTCALL
  #if CYTHON_ASSUME_SAFE_SIZE
  __pyx_nargs = PyTuple_GET_SIZE(__pyx_args);
  #else
  __pyx_nargs = PyTuple_Size(__pyx_args); if (unlikely(__pyx_nargs < 0)) return NULL;
  #endif
  #endif
  __pyx_kwvalues = __Pyx_KwValues_FASTCALL(__pyx_args, __pyx_nargs);
  {
    PyObject ** const __pyx_pyargnames[] = {&__pyx_mstate_global->__pyx_n_u_node,0};
  PyObject* values[1] = {0};
    const Py_ssize_t __pyx_kwds_len = (__pyx_kwds) ? __Pyx_NumKwargs_FASTCALL(__pyx_kwds) : 0;
    if (unlikely(__pyx_kwds_len) < 0) __PYX_ERR(0, 400, __pyx_L3_error)
    if (__pyx_kwds_len > 0) {
      switch (__pyx_nargs) {
        case  1:
        values[0] = __Pyx_ArgRef_FASTCALL(__pyx_args, 0);
        if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[0])) __PYX_ERR(0, 400, __pyx_L3_error)
        CYTHON_FALLTHROUGH;
        case  0: break;
        default: goto __pyx_L5_argtuple_error;
      }
      const Py_ssize_t kwd_pos_args = __pyx_nargs;
      if (__Pyx_ParseKeywords(__pyx_kwds, __pyx_kwvalues, __pyx_pyargnames, 0, values, kwd_pos_args, __pyx_kwds_len, "visit_CStructOrUnionDefNode", 0) < (0)) __PYX_ERR(0, 400, __pyx_L3_error)
      for (Py_ssize_t i = __pyx_nargs; i < 1; i++) {
        if (unlikely(!values[i])) { __Pyx_RaiseArgtupleInvalid("visit_CStructOrUnionDefNode", 1, 1, 1, i); __PYX_ERR(0, 400, __pyx_L3_error) }
      }
    } else if (unlikely(__pyx_nargs != 1)) {
      goto __pyx_L5_argtuple_error;
    } else {
      values[0] = __Pyx_ArgRef_FASTCALL(__pyx_args, 0);
      if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[0])) __PYX_ERR(0, 400, __pyx_L3_error)
    }
    __pyx_v_node = values[0];
  }
  goto __pyx_L6_skip;
  __pyx_L5_argtuple_error:;
  __Pyx_RaiseArgtupleInvalid("visit_CStructOrUnionDefNode", 1, 1, 1, __pyx_nargs); __PYX_ERR(0, 400, __pyx_L3_error)
  __pyx_L6_skip:;
  goto __pyx_L4_argument_unpacking_done;
  __pyx_L3_error:;
  for (Py_ssize_t __pyx_temp=0; __pyx_temp < (Py_ssize_t)(sizeof(values)/sizeof(values[0])); ++__pyx_temp) {
    Py_XDECREF(values[__pyx_temp]);
  }
  __Pyx_AddTraceback("Cython.Compiler.Visitor.EnvTransform.visit_CStructOrUnionDefNode", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __Pyx_RefNannyFinishContext();
  return NULL;
  __pyx_L4_argument_unpacking_done:;
  __pyx_r = __pyx_pf_6Cython_8Compiler_7Visitor_12EnvTransform_20visit_CStructOrUnionDefNode(((struct __pyx_obj_6Cython_8Compiler_7Visitor_EnvTransform *)__pyx_v_self), __pyx_v_node);
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

static PyObject *__pyx_pf_6Cython_8Compiler_7Visitor_12EnvTransform_20visit_CStructOrUnionDefNode(struct __pyx_obj_6Cython_8Compiler_7Visitor_EnvTransform *__pyx_v_self, PyObject *__pyx_v_node) {
  PyObject *__pyx_r = NULL;
/* … */
  /* function exit code */
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_t_1);
  __Pyx_XDECREF(__pyx_t_2);
  __Pyx_XDECREF(__pyx_t_3);
  __Pyx_AddTraceback("Cython.Compiler.Visitor.EnvTransform.visit_CStructOrUnionDefNode", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_r = NULL;
  __pyx_L0:;
  __Pyx_XGIVEREF(__pyx_r);
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}
/* … */
  __pyx_t_2 = __Pyx_CyFunction_New(&__pyx_mdef_6Cython_8Compiler_7Visitor_12EnvTransform_21visit_CStructOrUnionDefNode, __Pyx_CYFUNCTION_CCLASS, __pyx_mstate_global->__pyx_n_u_EnvTransform_visit_CStructOrUnio, NULL, __pyx_mstate_global->__pyx_n_u_Cython_Compiler_Visitor, __pyx_mstate_global->__pyx_d, ((PyObject *)__pyx_mstate_global->__pyx_codeobj_tab[31])); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 400, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  #if CYTHON_COMPILING_IN_CPYTHON && PY_VERSION_HEX >= 0x030E0000
  PyUnstable_Object_EnableDeferredRefcount(__pyx_t_2);
  #endif
  if (__Pyx_SetItemOnTypeDict(__pyx_mstate_global->__pyx_ptype_6Cython_8Compiler_7Visitor_EnvTransform, __pyx_mstate_global->__pyx_n_u_visit_CStructOrUnionDefNode, __pyx_t_2) < (0)) __PYX_ERR(0, 400, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
```

</details>

L401  🟠  (score=8)
```python
        self.enter_scope(node, node.scope)
```
<details><summary>Show generated C (score=8)</summary>

```c
  __pyx_t_2 = ((PyObject *)__pyx_v_self);
  __Pyx_INCREF(__pyx_t_2);
  __pyx_t_3 = __Pyx_PyObject_GetAttrStr(__pyx_v_node, __pyx_mstate_global->__pyx_n_u_scope); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 401, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_3);
  __pyx_t_4 = 0;
  {
    PyObject *__pyx_callargs[3] = {__pyx_t_2, __pyx_v_node, __pyx_t_3};
    __pyx_t_1 = __Pyx_PyObject_FastCallMethod((PyObject*)__pyx_mstate_global->__pyx_n_u_enter_scope, __pyx_callargs+__pyx_t_4, (3-__pyx_t_4) | (1*__Pyx_PY_VECTORCALL_ARGUMENTS_OFFSET));
    __Pyx_XDECREF(__pyx_t_2); __pyx_t_2 = 0;
    __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
    if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 401, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_1);
  }
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
```

</details>

L402  🟡  (score=1)
```python
        self._process_children(node)
```
<details><summary>Show generated C (score=1)</summary>

```c
  __pyx_t_1 = ((struct __pyx_vtabstruct_6Cython_8Compiler_7Visitor_EnvTransform *)__pyx_v_self->__pyx_base.__pyx_base.__pyx_base.__pyx_vtab)->__pyx_base.__pyx_base._process_children(((struct __pyx_obj_6Cython_8Compiler_7Visitor_VisitorTransform *)__pyx_v_self), __pyx_v_node, NULL); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 402, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
```

</details>

L403  🟠  (score=5)
```python
        self.exit_scope()
```
<details><summary>Show generated C (score=5)</summary>

```c
  __pyx_t_3 = ((PyObject *)__pyx_v_self);
  __Pyx_INCREF(__pyx_t_3);
  __pyx_t_4 = 0;
  {
    PyObject *__pyx_callargs[2] = {__pyx_t_3, NULL};
    __pyx_t_1 = __Pyx_PyObject_FastCallMethod((PyObject*)__pyx_mstate_global->__pyx_n_u_exit_scope, __pyx_callargs+__pyx_t_4, (1-__pyx_t_4) | (1*__Pyx_PY_VECTORCALL_ARGUMENTS_OFFSET));
    __Pyx_XDECREF(__pyx_t_3); __pyx_t_3 = 0;
    if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 403, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_1);
  }
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
```

</details>

L404  🟡  (score=2)
```python
        return node
```
<details><summary>Show generated C (score=2)</summary>

```c
  __Pyx_XDECREF(__pyx_r);
  __Pyx_INCREF(__pyx_v_node);
  __pyx_r = __pyx_v_node;
  goto __pyx_L0;
```

</details>

L405  ⚪  (score=0)
```python
```
L406  🔴  (score=38)
```python
    def visit_ScopedExprNode(self, node):
```
<details><summary>Show generated C (score=38)</summary>

```c
/* Python wrapper */
static PyObject *__pyx_pw_6Cython_8Compiler_7Visitor_12EnvTransform_23visit_ScopedExprNode(PyObject *__pyx_v_self, 
#if CYTHON_METH_FASTCALL
PyObject *const *__pyx_args, Py_ssize_t __pyx_nargs, PyObject *__pyx_kwds
#else
PyObject *__pyx_args, PyObject *__pyx_kwds
#endif
); /*proto*/
PyDoc_STRVAR(__pyx_doc_6Cython_8Compiler_7Visitor_12EnvTransform_22visit_ScopedExprNode, "File: Cython/Compiler/Visitor.py (starting at line 406)");
static PyMethodDef __pyx_mdef_6Cython_8Compiler_7Visitor_12EnvTransform_23visit_ScopedExprNode = {"visit_ScopedExprNode", (PyCFunction)(void(*)(void))(__Pyx_PyCFunction_FastCallWithKeywords)__pyx_pw_6Cython_8Compiler_7Visitor_12EnvTransform_23visit_ScopedExprNode, __Pyx_METH_FASTCALL|METH_KEYWORDS, __pyx_doc_6Cython_8Compiler_7Visitor_12EnvTransform_22visit_ScopedExprNode};
static PyObject *__pyx_pw_6Cython_8Compiler_7Visitor_12EnvTransform_23visit_ScopedExprNode(PyObject *__pyx_v_self, 
#if CYTHON_METH_FASTCALL
PyObject *const *__pyx_args, Py_ssize_t __pyx_nargs, PyObject *__pyx_kwds
#else
PyObject *__pyx_args, PyObject *__pyx_kwds
#endif
) {
  PyObject *__pyx_v_node = 0;
  #if !CYTHON_METH_FASTCALL
  CYTHON_UNUSED Py_ssize_t __pyx_nargs;
  #endif
  CYTHON_UNUSED PyObject *const *__pyx_kwvalues;
  PyObject *__pyx_r = 0;
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("visit_ScopedExprNode (wrapper)", 0);
  #if !CYTHON_METH_FASTCALL
  #if CYTHON_ASSUME_SAFE_SIZE
  __pyx_nargs = PyTuple_GET_SIZE(__pyx_args);
  #else
  __pyx_nargs = PyTuple_Size(__pyx_args); if (unlikely(__pyx_nargs < 0)) return NULL;
  #endif
  #endif
  __pyx_kwvalues = __Pyx_KwValues_FASTCALL(__pyx_args, __pyx_nargs);
  {
    PyObject ** const __pyx_pyargnames[] = {&__pyx_mstate_global->__pyx_n_u_node,0};
  PyObject* values[1] = {0};
    const Py_ssize_t __pyx_kwds_len = (__pyx_kwds) ? __Pyx_NumKwargs_FASTCALL(__pyx_kwds) : 0;
    if (unlikely(__pyx_kwds_len) < 0) __PYX_ERR(0, 406, __pyx_L3_error)
    if (__pyx_kwds_len > 0) {
      switch (__pyx_nargs) {
        case  1:
        values[0] = __Pyx_ArgRef_FASTCALL(__pyx_args, 0);
        if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[0])) __PYX_ERR(0, 406, __pyx_L3_error)
        CYTHON_FALLTHROUGH;
        case  0: break;
        default: goto __pyx_L5_argtuple_error;
      }
      const Py_ssize_t kwd_pos_args = __pyx_nargs;
      if (__Pyx_ParseKeywords(__pyx_kwds, __pyx_kwvalues, __pyx_pyargnames, 0, values, kwd_pos_args, __pyx_kwds_len, "visit_ScopedExprNode", 0) < (0)) __PYX_ERR(0, 406, __pyx_L3_error)
      for (Py_ssize_t i = __pyx_nargs; i < 1; i++) {
        if (unlikely(!values[i])) { __Pyx_RaiseArgtupleInvalid("visit_ScopedExprNode", 1, 1, 1, i); __PYX_ERR(0, 406, __pyx_L3_error) }
      }
    } else if (unlikely(__pyx_nargs != 1)) {
      goto __pyx_L5_argtuple_error;
    } else {
      values[0] = __Pyx_ArgRef_FASTCALL(__pyx_args, 0);
      if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[0])) __PYX_ERR(0, 406, __pyx_L3_error)
    }
    __pyx_v_node = values[0];
  }
  goto __pyx_L6_skip;
  __pyx_L5_argtuple_error:;
  __Pyx_RaiseArgtupleInvalid("visit_ScopedExprNode", 1, 1, 1, __pyx_nargs); __PYX_ERR(0, 406, __pyx_L3_error)
  __pyx_L6_skip:;
  goto __pyx_L4_argument_unpacking_done;
  __pyx_L3_error:;
  for (Py_ssize_t __pyx_temp=0; __pyx_temp < (Py_ssize_t)(sizeof(values)/sizeof(values[0])); ++__pyx_temp) {
    Py_XDECREF(values[__pyx_temp]);
  }
  __Pyx_AddTraceback("Cython.Compiler.Visitor.EnvTransform.visit_ScopedExprNode", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __Pyx_RefNannyFinishContext();
  return NULL;
  __pyx_L4_argument_unpacking_done:;
  __pyx_r = __pyx_pf_6Cython_8Compiler_7Visitor_12EnvTransform_22visit_ScopedExprNode(((struct __pyx_obj_6Cython_8Compiler_7Visitor_EnvTransform *)__pyx_v_self), __pyx_v_node);
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

static PyObject *__pyx_pf_6Cython_8Compiler_7Visitor_12EnvTransform_22visit_ScopedExprNode(struct __pyx_obj_6Cython_8Compiler_7Visitor_EnvTransform *__pyx_v_self, PyObject *__pyx_v_node) {
  PyObject *__pyx_r = NULL;
/* … */
  /* function exit code */
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_t_1);
  __Pyx_XDECREF(__pyx_t_3);
  __Pyx_XDECREF(__pyx_t_4);
  __Pyx_AddTraceback("Cython.Compiler.Visitor.EnvTransform.visit_ScopedExprNode", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_r = NULL;
  __pyx_L0:;
  __Pyx_XGIVEREF(__pyx_r);
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}
/* … */
  __pyx_t_2 = __Pyx_CyFunction_New(&__pyx_mdef_6Cython_8Compiler_7Visitor_12EnvTransform_23visit_ScopedExprNode, __Pyx_CYFUNCTION_CCLASS, __pyx_mstate_global->__pyx_n_u_EnvTransform_visit_ScopedExprNod, NULL, __pyx_mstate_global->__pyx_n_u_Cython_Compiler_Visitor, __pyx_mstate_global->__pyx_d, ((PyObject *)__pyx_mstate_global->__pyx_codeobj_tab[32])); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 406, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  #if CYTHON_COMPILING_IN_CPYTHON && PY_VERSION_HEX >= 0x030E0000
  PyUnstable_Object_EnableDeferredRefcount(__pyx_t_2);
  #endif
  if (__Pyx_SetItemOnTypeDict(__pyx_mstate_global->__pyx_ptype_6Cython_8Compiler_7Visitor_EnvTransform, __pyx_mstate_global->__pyx_n_u_visit_ScopedExprNode, __pyx_t_2) < (0)) __PYX_ERR(0, 406, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
```

</details>

L407  🟠  (score=5)
```python
        if node.expr_scope:
```
<details><summary>Show generated C (score=5)</summary>

```c
  __pyx_t_1 = __Pyx_PyObject_GetAttrStr(__pyx_v_node, __pyx_mstate_global->__pyx_n_u_expr_scope); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 407, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __pyx_t_2 = __Pyx_PyObject_IsTrue(__pyx_t_1); if (unlikely((__pyx_t_2 < 0))) __PYX_ERR(0, 407, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  if (__pyx_t_2) {
/* … */
    goto __pyx_L3;
  }
```

</details>

L408  🟠  (score=8)
```python
            self.enter_scope(node, node.expr_scope)
```
<details><summary>Show generated C (score=8)</summary>

```c
    __pyx_t_3 = ((PyObject *)__pyx_v_self);
    __Pyx_INCREF(__pyx_t_3);
    __pyx_t_4 = __Pyx_PyObject_GetAttrStr(__pyx_v_node, __pyx_mstate_global->__pyx_n_u_expr_scope); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 408, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_4);
    __pyx_t_5 = 0;
    {
      PyObject *__pyx_callargs[3] = {__pyx_t_3, __pyx_v_node, __pyx_t_4};
      __pyx_t_1 = __Pyx_PyObject_FastCallMethod((PyObject*)__pyx_mstate_global->__pyx_n_u_enter_scope, __pyx_callargs+__pyx_t_5, (3-__pyx_t_5) | (1*__Pyx_PY_VECTORCALL_ARGUMENTS_OFFSET));
      __Pyx_XDECREF(__pyx_t_3); __pyx_t_3 = 0;
      __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
      if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 408, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_1);
    }
    __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
```

</details>

L409  🟡  (score=1)
```python
            self._process_children(node)
```
<details><summary>Show generated C (score=1)</summary>

```c
    __pyx_t_1 = ((struct __pyx_vtabstruct_6Cython_8Compiler_7Visitor_EnvTransform *)__pyx_v_self->__pyx_base.__pyx_base.__pyx_base.__pyx_vtab)->__pyx_base.__pyx_base._process_children(((struct __pyx_obj_6Cython_8Compiler_7Visitor_VisitorTransform *)__pyx_v_self), __pyx_v_node, NULL); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 409, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_1);
    __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
```

</details>

L410  🟠  (score=5)
```python
            self.exit_scope()
```
<details><summary>Show generated C (score=5)</summary>

```c
    __pyx_t_4 = ((PyObject *)__pyx_v_self);
    __Pyx_INCREF(__pyx_t_4);
    __pyx_t_5 = 0;
    {
      PyObject *__pyx_callargs[2] = {__pyx_t_4, NULL};
      __pyx_t_1 = __Pyx_PyObject_FastCallMethod((PyObject*)__pyx_mstate_global->__pyx_n_u_exit_scope, __pyx_callargs+__pyx_t_5, (1-__pyx_t_5) | (1*__Pyx_PY_VECTORCALL_ARGUMENTS_OFFSET));
      __Pyx_XDECREF(__pyx_t_4); __pyx_t_4 = 0;
      if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 410, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_1);
    }
    __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
```

</details>

L411  ⚪  (score=0)
```python
        else:
```
L412  🟡  (score=1)
```python
            self._process_children(node)
```
<details><summary>Show generated C (score=1)</summary>

```c
  /*else*/ {
    __pyx_t_1 = ((struct __pyx_vtabstruct_6Cython_8Compiler_7Visitor_EnvTransform *)__pyx_v_self->__pyx_base.__pyx_base.__pyx_base.__pyx_vtab)->__pyx_base.__pyx_base._process_children(((struct __pyx_obj_6Cython_8Compiler_7Visitor_VisitorTransform *)__pyx_v_self), __pyx_v_node, NULL); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 412, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_1);
    __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  }
  __pyx_L3:;
```

</details>

L413  🟡  (score=2)
```python
        return node
```
<details><summary>Show generated C (score=2)</summary>

```c
  __Pyx_XDECREF(__pyx_r);
  __Pyx_INCREF(__pyx_v_node);
  __pyx_r = __pyx_v_node;
  goto __pyx_L0;
```

</details>

L414  ⚪  (score=0)
```python
```
L415  🔴  (score=41)
```python
    def visit_CArgDeclNode(self, node):
```
<details><summary>Show generated C (score=41)</summary>

```c
/* Python wrapper */
static PyObject *__pyx_pw_6Cython_8Compiler_7Visitor_12EnvTransform_25visit_CArgDeclNode(PyObject *__pyx_v_self, 
#if CYTHON_METH_FASTCALL
PyObject *const *__pyx_args, Py_ssize_t __pyx_nargs, PyObject *__pyx_kwds
#else
PyObject *__pyx_args, PyObject *__pyx_kwds
#endif
); /*proto*/
PyDoc_STRVAR(__pyx_doc_6Cython_8Compiler_7Visitor_12EnvTransform_24visit_CArgDeclNode, "File: Cython/Compiler/Visitor.py (starting at line 415)");
static PyMethodDef __pyx_mdef_6Cython_8Compiler_7Visitor_12EnvTransform_25visit_CArgDeclNode = {"visit_CArgDeclNode", (PyCFunction)(void(*)(void))(__Pyx_PyCFunction_FastCallWithKeywords)__pyx_pw_6Cython_8Compiler_7Visitor_12EnvTransform_25visit_CArgDeclNode, __Pyx_METH_FASTCALL|METH_KEYWORDS, __pyx_doc_6Cython_8Compiler_7Visitor_12EnvTransform_24visit_CArgDeclNode};
static PyObject *__pyx_pw_6Cython_8Compiler_7Visitor_12EnvTransform_25visit_CArgDeclNode(PyObject *__pyx_v_self, 
#if CYTHON_METH_FASTCALL
PyObject *const *__pyx_args, Py_ssize_t __pyx_nargs, PyObject *__pyx_kwds
#else
PyObject *__pyx_args, PyObject *__pyx_kwds
#endif
) {
  PyObject *__pyx_v_node = 0;
  #if !CYTHON_METH_FASTCALL
  CYTHON_UNUSED Py_ssize_t __pyx_nargs;
  #endif
  CYTHON_UNUSED PyObject *const *__pyx_kwvalues;
  PyObject *__pyx_r = 0;
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("visit_CArgDeclNode (wrapper)", 0);
  #if !CYTHON_METH_FASTCALL
  #if CYTHON_ASSUME_SAFE_SIZE
  __pyx_nargs = PyTuple_GET_SIZE(__pyx_args);
  #else
  __pyx_nargs = PyTuple_Size(__pyx_args); if (unlikely(__pyx_nargs < 0)) return NULL;
  #endif
  #endif
  __pyx_kwvalues = __Pyx_KwValues_FASTCALL(__pyx_args, __pyx_nargs);
  {
    PyObject ** const __pyx_pyargnames[] = {&__pyx_mstate_global->__pyx_n_u_node,0};
  PyObject* values[1] = {0};
    const Py_ssize_t __pyx_kwds_len = (__pyx_kwds) ? __Pyx_NumKwargs_FASTCALL(__pyx_kwds) : 0;
    if (unlikely(__pyx_kwds_len) < 0) __PYX_ERR(0, 415, __pyx_L3_error)
    if (__pyx_kwds_len > 0) {
      switch (__pyx_nargs) {
        case  1:
        values[0] = __Pyx_ArgRef_FASTCALL(__pyx_args, 0);
        if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[0])) __PYX_ERR(0, 415, __pyx_L3_error)
        CYTHON_FALLTHROUGH;
        case  0: break;
        default: goto __pyx_L5_argtuple_error;
      }
      const Py_ssize_t kwd_pos_args = __pyx_nargs;
      if (__Pyx_ParseKeywords(__pyx_kwds, __pyx_kwvalues, __pyx_pyargnames, 0, values, kwd_pos_args, __pyx_kwds_len, "visit_CArgDeclNode", 0) < (0)) __PYX_ERR(0, 415, __pyx_L3_error)
      for (Py_ssize_t i = __pyx_nargs; i < 1; i++) {
        if (unlikely(!values[i])) { __Pyx_RaiseArgtupleInvalid("visit_CArgDeclNode", 1, 1, 1, i); __PYX_ERR(0, 415, __pyx_L3_error) }
      }
    } else if (unlikely(__pyx_nargs != 1)) {
      goto __pyx_L5_argtuple_error;
    } else {
      values[0] = __Pyx_ArgRef_FASTCALL(__pyx_args, 0);
      if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[0])) __PYX_ERR(0, 415, __pyx_L3_error)
    }
    __pyx_v_node = values[0];
  }
  goto __pyx_L6_skip;
  __pyx_L5_argtuple_error:;
  __Pyx_RaiseArgtupleInvalid("visit_CArgDeclNode", 1, 1, 1, __pyx_nargs); __PYX_ERR(0, 415, __pyx_L3_error)
  __pyx_L6_skip:;
  goto __pyx_L4_argument_unpacking_done;
  __pyx_L3_error:;
  for (Py_ssize_t __pyx_temp=0; __pyx_temp < (Py_ssize_t)(sizeof(values)/sizeof(values[0])); ++__pyx_temp) {
    Py_XDECREF(values[__pyx_temp]);
  }
  __Pyx_AddTraceback("Cython.Compiler.Visitor.EnvTransform.visit_CArgDeclNode", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __Pyx_RefNannyFinishContext();
  return NULL;
  __pyx_L4_argument_unpacking_done:;
  __pyx_r = __pyx_pf_6Cython_8Compiler_7Visitor_12EnvTransform_24visit_CArgDeclNode(((struct __pyx_obj_6Cython_8Compiler_7Visitor_EnvTransform *)__pyx_v_self), __pyx_v_node);
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

static PyObject *__pyx_pf_6Cython_8Compiler_7Visitor_12EnvTransform_24visit_CArgDeclNode(struct __pyx_obj_6Cython_8Compiler_7Visitor_EnvTransform *__pyx_v_self, PyObject *__pyx_v_node) {
  PyObject *__pyx_v_attrs = NULL;
  PyObject *__pyx_8genexpr1__pyx_v_attr = NULL;
  PyObject *__pyx_r = NULL;
/* … */
  /* function exit code */
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_t_1);
  __Pyx_XDECREF(__pyx_t_3);
  __Pyx_XDECREF(__pyx_t_4);
  __Pyx_XDECREF(__pyx_t_8);
  __Pyx_AddTraceback("Cython.Compiler.Visitor.EnvTransform.visit_CArgDeclNode", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_r = NULL;
  __pyx_L0:;
  __Pyx_XDECREF(__pyx_v_attrs);
  __Pyx_XDECREF(__pyx_8genexpr1__pyx_v_attr);
  __Pyx_XGIVEREF(__pyx_r);
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}
/* … */
  __pyx_t_2 = __Pyx_CyFunction_New(&__pyx_mdef_6Cython_8Compiler_7Visitor_12EnvTransform_25visit_CArgDeclNode, __Pyx_CYFUNCTION_CCLASS, __pyx_mstate_global->__pyx_n_u_EnvTransform_visit_CArgDeclNode, NULL, __pyx_mstate_global->__pyx_n_u_Cython_Compiler_Visitor, __pyx_mstate_global->__pyx_d, ((PyObject *)__pyx_mstate_global->__pyx_codeobj_tab[33])); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 415, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  #if CYTHON_COMPILING_IN_CPYTHON && PY_VERSION_HEX >= 0x030E0000
  PyUnstable_Object_EnableDeferredRefcount(__pyx_t_2);
  #endif
  if (__Pyx_SetItemOnTypeDict(__pyx_mstate_global->__pyx_ptype_6Cython_8Compiler_7Visitor_EnvTransform, __pyx_mstate_global->__pyx_n_u_visit_CArgDeclNode, __pyx_t_2) < (0)) __PYX_ERR(0, 415, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
```

</details>

L416  ⚪  (score=0)
```python
        # default arguments are evaluated in the outer scope
```
L417  🟠  (score=5)
```python
        if node.default:
```
<details><summary>Show generated C (score=5)</summary>

```c
  __pyx_t_1 = __Pyx_PyObject_GetAttrStr(__pyx_v_node, __pyx_mstate_global->__pyx_n_u_default); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 417, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __pyx_t_2 = __Pyx_PyObject_IsTrue(__pyx_t_1); if (unlikely((__pyx_t_2 < 0))) __PYX_ERR(0, 417, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  if (__pyx_t_2) {
/* … */
    goto __pyx_L3;
  }
```

</details>

L418  🔴  (score=60)
```python
            attrs = [attr for attr in node.child_attrs if attr != 'default']
```
<details><summary>Show generated C (score=60)</summary>

```c
    { /* enter inner scope */
      __pyx_t_1 = PyList_New(0); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 418, __pyx_L6_error)
      __Pyx_GOTREF(__pyx_t_1);
      __pyx_t_3 = __Pyx_PyObject_GetAttrStr(__pyx_v_node, __pyx_mstate_global->__pyx_n_u_child_attrs); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 418, __pyx_L6_error)
      __Pyx_GOTREF(__pyx_t_3);
      if (likely(PyList_CheckExact(__pyx_t_3)) || PyTuple_CheckExact(__pyx_t_3)) {
        __pyx_t_4 = __pyx_t_3; __Pyx_INCREF(__pyx_t_4);
        __pyx_t_5 = 0;
        __pyx_t_6 = NULL;
      } else {
        __pyx_t_5 = -1; __pyx_t_4 = PyObject_GetIter(__pyx_t_3); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 418, __pyx_L6_error)
        __Pyx_GOTREF(__pyx_t_4);
        __pyx_t_6 = (CYTHON_COMPILING_IN_LIMITED_API) ? PyIter_Next : __Pyx_PyObject_GetIterNextFunc(__pyx_t_4); if (unlikely(!__pyx_t_6)) __PYX_ERR(0, 418, __pyx_L6_error)
      }
      __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
      for (;;) {
        if (likely(!__pyx_t_6)) {
          if (likely(PyList_CheckExact(__pyx_t_4))) {
            {
              Py_ssize_t __pyx_temp = __Pyx_PyList_GET_SIZE(__pyx_t_4);
              #if !CYTHON_ASSUME_SAFE_SIZE
              if (unlikely((__pyx_temp < 0))) __PYX_ERR(0, 418, __pyx_L6_error)
              #endif
              if (__pyx_t_5 >= __pyx_temp) break;
            }
            __pyx_t_3 = __Pyx_PyList_GetItemRefFast(__pyx_t_4, __pyx_t_5, __Pyx_ReferenceSharing_OwnStrongReference);
            ++__pyx_t_5;
          } else {
            {
              Py_ssize_t __pyx_temp = __Pyx_PyTuple_GET_SIZE(__pyx_t_4);
              #if !CYTHON_ASSUME_SAFE_SIZE
              if (unlikely((__pyx_temp < 0))) __PYX_ERR(0, 418, __pyx_L6_error)
              #endif
              if (__pyx_t_5 >= __pyx_temp) break;
            }
            #if CYTHON_ASSUME_SAFE_MACROS && !CYTHON_AVOID_BORROWED_REFS
            __pyx_t_3 = __Pyx_NewRef(PyTuple_GET_ITEM(__pyx_t_4, __pyx_t_5));
            #else
            __pyx_t_3 = __Pyx_PySequence_ITEM(__pyx_t_4, __pyx_t_5);
            #endif
            ++__pyx_t_5;
          }
          if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 418, __pyx_L6_error)
        } else {
          __pyx_t_3 = __pyx_t_6(__pyx_t_4);
          if (unlikely(!__pyx_t_3)) {
            PyObject* exc_type = PyErr_Occurred();
            if (exc_type) {
              if (unlikely(!__Pyx_PyErr_GivenExceptionMatches(exc_type, PyExc_StopIteration))) __PYX_ERR(0, 418, __pyx_L6_error)
              PyErr_Clear();
            }
            break;
          }
        }
        __Pyx_GOTREF(__pyx_t_3);
        __Pyx_XDECREF_SET(__pyx_8genexpr1__pyx_v_attr, __pyx_t_3);
        __pyx_t_3 = 0;
        __pyx_t_2 = (__Pyx_PyUnicode_Equals(__pyx_8genexpr1__pyx_v_attr, __pyx_mstate_global->__pyx_n_u_default, Py_NE)); if (unlikely((__pyx_t_2 < 0))) __PYX_ERR(0, 418, __pyx_L6_error)
        if (__pyx_t_2) {
          if (unlikely(__Pyx_ListComp_Append(__pyx_t_1, (PyObject*)__pyx_8genexpr1__pyx_v_attr))) __PYX_ERR(0, 418, __pyx_L6_error)
        }
      }
      __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
      __Pyx_XDECREF(__pyx_8genexpr1__pyx_v_attr); __pyx_8genexpr1__pyx_v_attr = 0;
      goto __pyx_L11_exit_scope;
      __pyx_L6_error:;
      __Pyx_XDECREF(__pyx_8genexpr1__pyx_v_attr); __pyx_8genexpr1__pyx_v_attr = 0;
      goto __pyx_L1_error;
      __pyx_L11_exit_scope:;
    } /* exit inner scope */
    __pyx_v_attrs = ((PyObject*)__pyx_t_1);
    __pyx_t_1 = 0;
```

</details>

L419  🟡  (score=1)
```python
            self._process_children(node, attrs)
```
<details><summary>Show generated C (score=1)</summary>

```c
    __pyx_t_7.__pyx_n = 1;
    __pyx_t_7.attrs = __pyx_v_attrs;
    __pyx_t_1 = ((struct __pyx_vtabstruct_6Cython_8Compiler_7Visitor_EnvTransform *)__pyx_v_self->__pyx_base.__pyx_base.__pyx_base.__pyx_vtab)->__pyx_base.__pyx_base._process_children(((struct __pyx_obj_6Cython_8Compiler_7Visitor_VisitorTransform *)__pyx_v_self), __pyx_v_node, &__pyx_t_7); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 419, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_1);
    __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
```

</details>

L420  🔴  (score=13)
```python
            self.enter_scope(node, self.current_env().outer_scope)
```
<details><summary>Show generated C (score=13)</summary>

```c
    __pyx_t_4 = ((PyObject *)__pyx_v_self);
    __Pyx_INCREF(__pyx_t_4);
    __pyx_t_8 = ((PyObject *)__pyx_v_self);
    __Pyx_INCREF(__pyx_t_8);
    __pyx_t_9 = 0;
    {
      PyObject *__pyx_callargs[2] = {__pyx_t_8, NULL};
      __pyx_t_3 = __Pyx_PyObject_FastCallMethod((PyObject*)__pyx_mstate_global->__pyx_n_u_current_env, __pyx_callargs+__pyx_t_9, (1-__pyx_t_9) | (1*__Pyx_PY_VECTORCALL_ARGUMENTS_OFFSET));
      __Pyx_XDECREF(__pyx_t_8); __pyx_t_8 = 0;
      if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 420, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_3);
    }
    __pyx_t_8 = __Pyx_PyObject_GetAttrStr(__pyx_t_3, __pyx_mstate_global->__pyx_n_u_outer_scope); if (unlikely(!__pyx_t_8)) __PYX_ERR(0, 420, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_8);
    __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
    __pyx_t_9 = 0;
    {
      PyObject *__pyx_callargs[3] = {__pyx_t_4, __pyx_v_node, __pyx_t_8};
      __pyx_t_1 = __Pyx_PyObject_FastCallMethod((PyObject*)__pyx_mstate_global->__pyx_n_u_enter_scope, __pyx_callargs+__pyx_t_9, (3-__pyx_t_9) | (1*__Pyx_PY_VECTORCALL_ARGUMENTS_OFFSET));
      __Pyx_XDECREF(__pyx_t_4); __pyx_t_4 = 0;
      __Pyx_DECREF(__pyx_t_8); __pyx_t_8 = 0;
      if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 420, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_1);
    }
    __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
```

</details>

L421  🟠  (score=6)
```python
            self.visitchildren(node, ('default',))
```
<details><summary>Show generated C (score=6)</summary>

```c
    __pyx_t_10.__pyx_n = 1;
    __pyx_t_10.attrs = __pyx_mstate_global->__pyx_tuple[3];
    __pyx_t_1 = ((struct __pyx_vtabstruct_6Cython_8Compiler_7Visitor_EnvTransform *)__pyx_v_self->__pyx_base.__pyx_base.__pyx_base.__pyx_vtab)->__pyx_base.__pyx_base.__pyx_base.visitchildren(((struct __pyx_obj_6Cython_8Compiler_7Visitor_TreeVisitor *)__pyx_v_self), __pyx_v_node, 0, &__pyx_t_10); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 421, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_1);
    __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
/* … */
  __pyx_mstate_global->__pyx_tuple[3] = PyTuple_Pack(1, __pyx_mstate_global->__pyx_n_u_default); if (unlikely(!__pyx_mstate_global->__pyx_tuple[3])) __PYX_ERR(0, 421, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_mstate_global->__pyx_tuple[3]);
  __Pyx_GIVEREF(__pyx_mstate_global->__pyx_tuple[3]);
```

</details>

L422  🟠  (score=5)
```python
            self.exit_scope()
```
<details><summary>Show generated C (score=5)</summary>

```c
    __pyx_t_8 = ((PyObject *)__pyx_v_self);
    __Pyx_INCREF(__pyx_t_8);
    __pyx_t_9 = 0;
    {
      PyObject *__pyx_callargs[2] = {__pyx_t_8, NULL};
      __pyx_t_1 = __Pyx_PyObject_FastCallMethod((PyObject*)__pyx_mstate_global->__pyx_n_u_exit_scope, __pyx_callargs+__pyx_t_9, (1-__pyx_t_9) | (1*__Pyx_PY_VECTORCALL_ARGUMENTS_OFFSET));
      __Pyx_XDECREF(__pyx_t_8); __pyx_t_8 = 0;
      if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 422, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_1);
    }
    __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
```

</details>

L423  ⚪  (score=0)
```python
        else:
```
L424  🟡  (score=1)
```python
            self._process_children(node)
```
<details><summary>Show generated C (score=1)</summary>

```c
  /*else*/ {
    __pyx_t_1 = ((struct __pyx_vtabstruct_6Cython_8Compiler_7Visitor_EnvTransform *)__pyx_v_self->__pyx_base.__pyx_base.__pyx_base.__pyx_vtab)->__pyx_base.__pyx_base._process_children(((struct __pyx_obj_6Cython_8Compiler_7Visitor_VisitorTransform *)__pyx_v_self), __pyx_v_node, NULL); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 424, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_1);
    __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  }
  __pyx_L3:;
```

</details>

L425  🟡  (score=2)
```python
        return node
```
<details><summary>Show generated C (score=2)</summary>

```c
  __Pyx_XDECREF(__pyx_r);
  __Pyx_INCREF(__pyx_v_node);
  __pyx_r = __pyx_v_node;
  goto __pyx_L0;
```

</details>

L426  ⚪  (score=0)
```python
```
L427  ⚪  (score=0)
```python
```
L428  🔴  (score=20)
```python
class NodeRefCleanupMixin:
```
<details><summary>Show generated C (score=20)</summary>

```c
  __pyx_t_2 = __Pyx_Py3MetaclassPrepare((PyObject *) NULL, __pyx_mstate_global->__pyx_empty_tuple, __pyx_mstate_global->__pyx_n_u_NodeRefCleanupMixin, __pyx_mstate_global->__pyx_n_u_NodeRefCleanupMixin, (PyObject *) NULL, __pyx_mstate_global->__pyx_n_u_Cython_Compiler_Visitor, __pyx_mstate_global->__pyx_kp_u_File_Cython_Compiler_Visitor_py_2); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 428, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __pyx_t_4 = PyList_New(0); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 428, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_4);
/* … */
  __pyx_t_5 = __Pyx_Py3ClassCreate(((PyObject*)&PyType_Type), __pyx_mstate_global->__pyx_n_u_NodeRefCleanupMixin, __pyx_mstate_global->__pyx_empty_tuple, __pyx_t_2, NULL, 0, 0); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 428, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_5);
  #if CYTHON_COMPILING_IN_CPYTHON && PY_VERSION_HEX >= 0x030E0000
  PyUnstable_Object_EnableDeferredRefcount(__pyx_t_5);
  #endif
  if (__Pyx_CyFunction_InitClassCell(__pyx_t_4, __pyx_t_5) < (0)) __PYX_ERR(0, 428, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
  if (PyDict_SetItem(__pyx_mstate_global->__pyx_d, __pyx_mstate_global->__pyx_n_u_NodeRefCleanupMixin, __pyx_t_5) < (0)) __PYX_ERR(0, 428, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
```

</details>

L429  ⚪  (score=0)
```python
    """
```
L430  ⚪  (score=0)
```python
    Clean up references to nodes that were replaced.
```
L431  ⚪  (score=0)
```python
```
L432  ⚪  (score=0)
```python
    NOTE: this implementation assumes that the replacement is
```
L433  ⚪  (score=0)
```python
    done first, before hitting any further references during
```
L434  ⚪  (score=0)
```python
    normal tree traversal.  This needs to be arranged by calling
```
L435  ⚪  (score=0)
```python
    "self.visitchildren()" at a proper place in the transform
```
L436  ⚪  (score=0)
```python
    and by ordering the "child_attrs" of nodes appropriately.
```
L437  ⚪  (score=0)
```python
    """
```
L438  🔴  (score=48)
```python
    def __init__(self, *args):
```
<details><summary>Show generated C (score=48)</summary>

```c
/* Python wrapper */
static PyObject *__pyx_pw_6Cython_8Compiler_7Visitor_19NodeRefCleanupMixin_1__init__(PyObject *__pyx_self, 
#if CYTHON_METH_FASTCALL
PyObject *const *__pyx_args, Py_ssize_t __pyx_nargs, PyObject *__pyx_kwds
#else
PyObject *__pyx_args, PyObject *__pyx_kwds
#endif
); /*proto*/
PyDoc_STRVAR(__pyx_doc_6Cython_8Compiler_7Visitor_19NodeRefCleanupMixin___init__, "File: Cython/Compiler/Visitor.py (starting at line 438)");
static PyMethodDef __pyx_mdef_6Cython_8Compiler_7Visitor_19NodeRefCleanupMixin_1__init__ = {"__init__", (PyCFunction)(void(*)(void))(__Pyx_PyCFunction_FastCallWithKeywords)__pyx_pw_6Cython_8Compiler_7Visitor_19NodeRefCleanupMixin_1__init__, __Pyx_METH_FASTCALL|METH_KEYWORDS, __pyx_doc_6Cython_8Compiler_7Visitor_19NodeRefCleanupMixin___init__};
static PyObject *__pyx_pw_6Cython_8Compiler_7Visitor_19NodeRefCleanupMixin_1__init__(PyObject *__pyx_self, 
#if CYTHON_METH_FASTCALL
PyObject *const *__pyx_args, Py_ssize_t __pyx_nargs, PyObject *__pyx_kwds
#else
PyObject *__pyx_args, PyObject *__pyx_kwds
#endif
) {
  PyObject *__pyx_v_self = 0;
  PyObject *__pyx_v_args = 0;
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
  __pyx_v_args = __Pyx_ArgsSlice_FASTCALL(__pyx_args, 1, __pyx_nargs);
  if (unlikely(!__pyx_v_args)) {
    __Pyx_RefNannyFinishContext();
    return NULL;
  }
  __Pyx_GOTREF(__pyx_v_args);
  {
    PyObject ** const __pyx_pyargnames[] = {&__pyx_mstate_global->__pyx_n_u_self,0};
  PyObject* values[1] = {0};
    const Py_ssize_t __pyx_kwds_len = (__pyx_kwds) ? __Pyx_NumKwargs_FASTCALL(__pyx_kwds) : 0;
    if (unlikely(__pyx_kwds_len) < 0) __PYX_ERR(0, 438, __pyx_L3_error)
    if (__pyx_kwds_len > 0) {
      switch (__pyx_nargs) {
        default:
        case  1:
        values[0] = __Pyx_ArgRef_FASTCALL(__pyx_args, 0);
        if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[0])) __PYX_ERR(0, 438, __pyx_L3_error)
        CYTHON_FALLTHROUGH;
        case  0: break;
      }
      const Py_ssize_t kwd_pos_args = __pyx_nargs;
      const Py_ssize_t used_pos_args = (kwd_pos_args < 1) ? kwd_pos_args : 1;
      if (__Pyx_ParseKeywords(__pyx_kwds, __pyx_kwvalues, __pyx_pyargnames, 0, values, used_pos_args, __pyx_kwds_len, "__init__", 0) < (0)) __PYX_ERR(0, 438, __pyx_L3_error)
      for (Py_ssize_t i = __pyx_nargs; i < 1; i++) {
        if (unlikely(!values[i])) { __Pyx_RaiseArgtupleInvalid("__init__", 0, 1, 1, i); __PYX_ERR(0, 438, __pyx_L3_error) }
      }
    } else if (unlikely(__pyx_nargs < 1)) {
      goto __pyx_L5_argtuple_error;
    } else {
      values[0] = __Pyx_ArgRef_FASTCALL(__pyx_args, 0);
      if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[0])) __PYX_ERR(0, 438, __pyx_L3_error)
    }
    __pyx_v_self = values[0];
  }
  goto __pyx_L6_skip;
  __pyx_L5_argtuple_error:;
  __Pyx_RaiseArgtupleInvalid("__init__", 0, 1, 1, __pyx_nargs); __PYX_ERR(0, 438, __pyx_L3_error)
  __pyx_L6_skip:;
  goto __pyx_L4_argument_unpacking_done;
  __pyx_L3_error:;
  for (Py_ssize_t __pyx_temp=0; __pyx_temp < (Py_ssize_t)(sizeof(values)/sizeof(values[0])); ++__pyx_temp) {
    Py_XDECREF(values[__pyx_temp]);
  }
  __Pyx_DECREF(__pyx_v_args); __pyx_v_args = 0;
  __Pyx_AddTraceback("Cython.Compiler.Visitor.NodeRefCleanupMixin.__init__", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __Pyx_RefNannyFinishContext();
  return NULL;
  __pyx_L4_argument_unpacking_done:;
  __pyx_r = __pyx_pf_6Cython_8Compiler_7Visitor_19NodeRefCleanupMixin___init__(__pyx_self, __pyx_v_self, __pyx_v_args);
  int __pyx_lineno = 0;
  const char *__pyx_filename = NULL;
  int __pyx_clineno = 0;

  /* function exit code */
  for (Py_ssize_t __pyx_temp=0; __pyx_temp < (Py_ssize_t)(sizeof(values)/sizeof(values[0])); ++__pyx_temp) {
    Py_XDECREF(values[__pyx_temp]);
  }
  __Pyx_DECREF(__pyx_v_args);
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}

static PyObject *__pyx_pf_6Cython_8Compiler_7Visitor_19NodeRefCleanupMixin___init__(CYTHON_UNUSED PyObject *__pyx_self, PyObject *__pyx_v_self, PyObject *__pyx_v_args) {
  PyObject *__pyx_r = NULL;
/* … */
  /* function exit code */
  __pyx_r = Py_None; __Pyx_INCREF(Py_None);
  goto __pyx_L0;
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_t_1);
  __Pyx_XDECREF(__pyx_t_2);
  __Pyx_XDECREF(__pyx_t_3);
  __Pyx_AddTraceback("Cython.Compiler.Visitor.NodeRefCleanupMixin.__init__", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_r = NULL;
  __pyx_L0:;
  __Pyx_XGIVEREF(__pyx_r);
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}
/* … */
  __pyx_t_5 = __Pyx_CyFunction_New(&__pyx_mdef_6Cython_8Compiler_7Visitor_19NodeRefCleanupMixin_1__init__, 0, __pyx_mstate_global->__pyx_n_u_NodeRefCleanupMixin___init, NULL, __pyx_mstate_global->__pyx_n_u_Cython_Compiler_Visitor, __pyx_mstate_global->__pyx_d, ((PyObject *)__pyx_mstate_global->__pyx_codeobj_tab[36])); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 438, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_5);
  #if CYTHON_COMPILING_IN_CPYTHON && PY_VERSION_HEX >= 0x030E0000
  PyUnstable_Object_EnableDeferredRefcount(__pyx_t_5);
  #endif
  PyList_Append(__pyx_t_4, __pyx_t_5);
  if (__Pyx_SetNameInClass(__pyx_t_2, __pyx_mstate_global->__pyx_n_u_init, __pyx_t_5) < (0)) __PYX_ERR(0, 438, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
```

</details>

L439  🔴  (score=19)
```python
        super().__init__(*args)
```
<details><summary>Show generated C (score=19)</summary>

```c
  __pyx_t_2 = NULL;
  __pyx_t_3 = __Pyx_CyFunction_GetClassObj(__pyx_self);
  if (!__pyx_t_3) { PyErr_SetString(PyExc_RuntimeError, "super(): empty __class__ cell"); __PYX_ERR(0, 439, __pyx_L1_error) }
  __Pyx_INCREF(__pyx_t_3);
  __pyx_t_4 = 1;
  {
    PyObject *__pyx_callargs[3] = {__pyx_t_2, __pyx_t_3, __pyx_v_self};
    __pyx_t_1 = __Pyx_PyObject_FastCall((PyObject*)__pyx_builtin_super, __pyx_callargs+__pyx_t_4, (3-__pyx_t_4) | (__pyx_t_4*__Pyx_PY_VECTORCALL_ARGUMENTS_OFFSET));
    __Pyx_XDECREF(__pyx_t_2); __pyx_t_2 = 0;
    __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
    if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 439, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_1);
  }
  __pyx_t_3 = __Pyx_PyObject_GetAttrStr(__pyx_t_1, __pyx_mstate_global->__pyx_n_u_init); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 439, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_3);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __pyx_t_1 = __Pyx_PyObject_Call(__pyx_t_3, __pyx_v_args, NULL); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 439, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
```

</details>

L440  🟠  (score=5)
```python
        self._replacements = {}
```
<details><summary>Show generated C (score=5)</summary>

```c
  __pyx_t_1 = __Pyx_PyDict_NewPresized(0); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 440, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  if (__Pyx_PyObject_SetAttrStr(__pyx_v_self, __pyx_mstate_global->__pyx_n_u_replacements, __pyx_t_1) < (0)) __PYX_ERR(0, 440, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
```

</details>

L441  ⚪  (score=0)
```python
```
L442  🔴  (score=43)
```python
    def visit_CloneNode(self, node):
```
<details><summary>Show generated C (score=43)</summary>

```c
/* Python wrapper */
static PyObject *__pyx_pw_6Cython_8Compiler_7Visitor_19NodeRefCleanupMixin_3visit_CloneNode(PyObject *__pyx_self, 
#if CYTHON_METH_FASTCALL
PyObject *const *__pyx_args, Py_ssize_t __pyx_nargs, PyObject *__pyx_kwds
#else
PyObject *__pyx_args, PyObject *__pyx_kwds
#endif
); /*proto*/
PyDoc_STRVAR(__pyx_doc_6Cython_8Compiler_7Visitor_19NodeRefCleanupMixin_2visit_CloneNode, "File: Cython/Compiler/Visitor.py (starting at line 442)");
static PyMethodDef __pyx_mdef_6Cython_8Compiler_7Visitor_19NodeRefCleanupMixin_3visit_CloneNode = {"visit_CloneNode", (PyCFunction)(void(*)(void))(__Pyx_PyCFunction_FastCallWithKeywords)__pyx_pw_6Cython_8Compiler_7Visitor_19NodeRefCleanupMixin_3visit_CloneNode, __Pyx_METH_FASTCALL|METH_KEYWORDS, __pyx_doc_6Cython_8Compiler_7Visitor_19NodeRefCleanupMixin_2visit_CloneNode};
static PyObject *__pyx_pw_6Cython_8Compiler_7Visitor_19NodeRefCleanupMixin_3visit_CloneNode(PyObject *__pyx_self, 
#if CYTHON_METH_FASTCALL
PyObject *const *__pyx_args, Py_ssize_t __pyx_nargs, PyObject *__pyx_kwds
#else
PyObject *__pyx_args, PyObject *__pyx_kwds
#endif
) {
  PyObject *__pyx_v_self = 0;
  PyObject *__pyx_v_node = 0;
  #if !CYTHON_METH_FASTCALL
  CYTHON_UNUSED Py_ssize_t __pyx_nargs;
  #endif
  CYTHON_UNUSED PyObject *const *__pyx_kwvalues;
  PyObject *__pyx_r = 0;
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("visit_CloneNode (wrapper)", 0);
  #if !CYTHON_METH_FASTCALL
  #if CYTHON_ASSUME_SAFE_SIZE
  __pyx_nargs = PyTuple_GET_SIZE(__pyx_args);
  #else
  __pyx_nargs = PyTuple_Size(__pyx_args); if (unlikely(__pyx_nargs < 0)) return NULL;
  #endif
  #endif
  __pyx_kwvalues = __Pyx_KwValues_FASTCALL(__pyx_args, __pyx_nargs);
  {
    PyObject ** const __pyx_pyargnames[] = {&__pyx_mstate_global->__pyx_n_u_self,&__pyx_mstate_global->__pyx_n_u_node,0};
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
      if (__Pyx_ParseKeywords(__pyx_kwds, __pyx_kwvalues, __pyx_pyargnames, 0, values, kwd_pos_args, __pyx_kwds_len, "visit_CloneNode", 0) < (0)) __PYX_ERR(0, 442, __pyx_L3_error)
      for (Py_ssize_t i = __pyx_nargs; i < 2; i++) {
        if (unlikely(!values[i])) { __Pyx_RaiseArgtupleInvalid("visit_CloneNode", 1, 2, 2, i); __PYX_ERR(0, 442, __pyx_L3_error) }
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
    __pyx_v_node = values[1];
  }
  goto __pyx_L6_skip;
  __pyx_L5_argtuple_error:;
  __Pyx_RaiseArgtupleInvalid("visit_CloneNode", 1, 2, 2, __pyx_nargs); __PYX_ERR(0, 442, __pyx_L3_error)
  __pyx_L6_skip:;
  goto __pyx_L4_argument_unpacking_done;
  __pyx_L3_error:;
  for (Py_ssize_t __pyx_temp=0; __pyx_temp < (Py_ssize_t)(sizeof(values)/sizeof(values[0])); ++__pyx_temp) {
    Py_XDECREF(values[__pyx_temp]);
  }
  __Pyx_AddTraceback("Cython.Compiler.Visitor.NodeRefCleanupMixin.visit_CloneNode", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __Pyx_RefNannyFinishContext();
  return NULL;
  __pyx_L4_argument_unpacking_done:;
  __pyx_r = __pyx_pf_6Cython_8Compiler_7Visitor_19NodeRefCleanupMixin_2visit_CloneNode(__pyx_self, __pyx_v_self, __pyx_v_node);
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

static PyObject *__pyx_pf_6Cython_8Compiler_7Visitor_19NodeRefCleanupMixin_2visit_CloneNode(CYTHON_UNUSED PyObject *__pyx_self, PyObject *__pyx_v_self, PyObject *__pyx_v_node) {
  PyObject *__pyx_v_arg = NULL;
  PyObject *__pyx_r = NULL;
/* … */
  /* function exit code */
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_t_1);
  __Pyx_XDECREF(__pyx_t_3);
  __Pyx_XDECREF(__pyx_t_5);
  __Pyx_AddTraceback("Cython.Compiler.Visitor.NodeRefCleanupMixin.visit_CloneNode", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_r = NULL;
  __pyx_L0:;
  __Pyx_XDECREF(__pyx_v_arg);
  __Pyx_XGIVEREF(__pyx_r);
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}
/* … */
  __pyx_t_5 = __Pyx_CyFunction_New(&__pyx_mdef_6Cython_8Compiler_7Visitor_19NodeRefCleanupMixin_3visit_CloneNode, 0, __pyx_mstate_global->__pyx_n_u_NodeRefCleanupMixin_visit_CloneN, NULL, __pyx_mstate_global->__pyx_n_u_Cython_Compiler_Visitor, __pyx_mstate_global->__pyx_d, ((PyObject *)__pyx_mstate_global->__pyx_codeobj_tab[37])); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 442, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_5);
  #if CYTHON_COMPILING_IN_CPYTHON && PY_VERSION_HEX >= 0x030E0000
  PyUnstable_Object_EnableDeferredRefcount(__pyx_t_5);
  #endif
  if (__Pyx_SetNameInClass(__pyx_t_2, __pyx_mstate_global->__pyx_n_u_visit_CloneNode, __pyx_t_5) < (0)) __PYX_ERR(0, 442, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
```

</details>

L443  🟡  (score=2)
```python
        arg = node.arg
```
<details><summary>Show generated C (score=2)</summary>

```c
  __pyx_t_1 = __Pyx_PyObject_GetAttrStr(__pyx_v_node, __pyx_mstate_global->__pyx_n_u_arg); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 443, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __pyx_v_arg = __pyx_t_1;
  __pyx_t_1 = 0;
```

</details>

L444  🟠  (score=5)
```python
        if arg not in self._replacements:
```
<details><summary>Show generated C (score=5)</summary>

```c
  __pyx_t_1 = __Pyx_PyObject_GetAttrStr(__pyx_v_self, __pyx_mstate_global->__pyx_n_u_replacements); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 444, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __pyx_t_2 = (__Pyx_PySequence_ContainsTF(__pyx_v_arg, __pyx_t_1, Py_NE)); if (unlikely((__pyx_t_2 < 0))) __PYX_ERR(0, 444, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  if (__pyx_t_2) {
/* … */
  }
```

</details>

L445  🟠  (score=5)
```python
            self.visitchildren(arg)
```
<details><summary>Show generated C (score=5)</summary>

```c
    __pyx_t_3 = __pyx_v_self;
    __Pyx_INCREF(__pyx_t_3);
    __pyx_t_4 = 0;
    {
      PyObject *__pyx_callargs[2] = {__pyx_t_3, __pyx_v_arg};
      __pyx_t_1 = __Pyx_PyObject_FastCallMethod((PyObject*)__pyx_mstate_global->__pyx_n_u_visitchildren, __pyx_callargs+__pyx_t_4, (2-__pyx_t_4) | (1*__Pyx_PY_VECTORCALL_ARGUMENTS_OFFSET));
      __Pyx_XDECREF(__pyx_t_3); __pyx_t_3 = 0;
      if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 445, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_1);
    }
    __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
```

</details>

L446  🔴  (score=10)
```python
        node.arg = self._replacements.get(arg, arg)
```
<details><summary>Show generated C (score=10)</summary>

```c
  __pyx_t_5 = __Pyx_PyObject_GetAttrStr(__pyx_v_self, __pyx_mstate_global->__pyx_n_u_replacements); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 446, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_5);
  __pyx_t_3 = __pyx_t_5;
  __Pyx_INCREF(__pyx_t_3);
  __pyx_t_4 = 0;
  {
    PyObject *__pyx_callargs[3] = {__pyx_t_3, __pyx_v_arg, __pyx_v_arg};
    __pyx_t_1 = __Pyx_PyObject_FastCallMethod((PyObject*)__pyx_mstate_global->__pyx_n_u_get, __pyx_callargs+__pyx_t_4, (3-__pyx_t_4) | (1*__Pyx_PY_VECTORCALL_ARGUMENTS_OFFSET));
    __Pyx_XDECREF(__pyx_t_3); __pyx_t_3 = 0;
    __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
    if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 446, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_1);
  }
  if (__Pyx_PyObject_SetAttrStr(__pyx_v_node, __pyx_mstate_global->__pyx_n_u_arg, __pyx_t_1) < (0)) __PYX_ERR(0, 446, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
```

</details>

L447  🟡  (score=2)
```python
        return node
```
<details><summary>Show generated C (score=2)</summary>

```c
  __Pyx_XDECREF(__pyx_r);
  __Pyx_INCREF(__pyx_v_node);
  __pyx_r = __pyx_v_node;
  goto __pyx_L0;
```

</details>

L448  ⚪  (score=0)
```python
```
L449  🔴  (score=43)
```python
    def visit_ResultRefNode(self, node):
```
<details><summary>Show generated C (score=43)</summary>

```c
/* Python wrapper */
static PyObject *__pyx_pw_6Cython_8Compiler_7Visitor_19NodeRefCleanupMixin_5visit_ResultRefNode(PyObject *__pyx_self, 
#if CYTHON_METH_FASTCALL
PyObject *const *__pyx_args, Py_ssize_t __pyx_nargs, PyObject *__pyx_kwds
#else
PyObject *__pyx_args, PyObject *__pyx_kwds
#endif
); /*proto*/
PyDoc_STRVAR(__pyx_doc_6Cython_8Compiler_7Visitor_19NodeRefCleanupMixin_4visit_ResultRefNode, "File: Cython/Compiler/Visitor.py (starting at line 449)");
static PyMethodDef __pyx_mdef_6Cython_8Compiler_7Visitor_19NodeRefCleanupMixin_5visit_ResultRefNode = {"visit_ResultRefNode", (PyCFunction)(void(*)(void))(__Pyx_PyCFunction_FastCallWithKeywords)__pyx_pw_6Cython_8Compiler_7Visitor_19NodeRefCleanupMixin_5visit_ResultRefNode, __Pyx_METH_FASTCALL|METH_KEYWORDS, __pyx_doc_6Cython_8Compiler_7Visitor_19NodeRefCleanupMixin_4visit_ResultRefNode};
static PyObject *__pyx_pw_6Cython_8Compiler_7Visitor_19NodeRefCleanupMixin_5visit_ResultRefNode(PyObject *__pyx_self, 
#if CYTHON_METH_FASTCALL
PyObject *const *__pyx_args, Py_ssize_t __pyx_nargs, PyObject *__pyx_kwds
#else
PyObject *__pyx_args, PyObject *__pyx_kwds
#endif
) {
  PyObject *__pyx_v_self = 0;
  PyObject *__pyx_v_node = 0;
  #if !CYTHON_METH_FASTCALL
  CYTHON_UNUSED Py_ssize_t __pyx_nargs;
  #endif
  CYTHON_UNUSED PyObject *const *__pyx_kwvalues;
  PyObject *__pyx_r = 0;
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("visit_ResultRefNode (wrapper)", 0);
  #if !CYTHON_METH_FASTCALL
  #if CYTHON_ASSUME_SAFE_SIZE
  __pyx_nargs = PyTuple_GET_SIZE(__pyx_args);
  #else
  __pyx_nargs = PyTuple_Size(__pyx_args); if (unlikely(__pyx_nargs < 0)) return NULL;
  #endif
  #endif
  __pyx_kwvalues = __Pyx_KwValues_FASTCALL(__pyx_args, __pyx_nargs);
  {
    PyObject ** const __pyx_pyargnames[] = {&__pyx_mstate_global->__pyx_n_u_self,&__pyx_mstate_global->__pyx_n_u_node,0};
  PyObject* values[2] = {0,0};
    const Py_ssize_t __pyx_kwds_len = (__pyx_kwds) ? __Pyx_NumKwargs_FASTCALL(__pyx_kwds) : 0;
    if (unlikely(__pyx_kwds_len) < 0) __PYX_ERR(0, 449, __pyx_L3_error)
    if (__pyx_kwds_len > 0) {
      switch (__pyx_nargs) {
        case  2:
        values[1] = __Pyx_ArgRef_FASTCALL(__pyx_args, 1);
        if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[1])) __PYX_ERR(0, 449, __pyx_L3_error)
        CYTHON_FALLTHROUGH;
        case  1:
        values[0] = __Pyx_ArgRef_FASTCALL(__pyx_args, 0);
        if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[0])) __PYX_ERR(0, 449, __pyx_L3_error)
        CYTHON_FALLTHROUGH;
        case  0: break;
        default: goto __pyx_L5_argtuple_error;
      }
      const Py_ssize_t kwd_pos_args = __pyx_nargs;
      if (__Pyx_ParseKeywords(__pyx_kwds, __pyx_kwvalues, __pyx_pyargnames, 0, values, kwd_pos_args, __pyx_kwds_len, "visit_ResultRefNode", 0) < (0)) __PYX_ERR(0, 449, __pyx_L3_error)
      for (Py_ssize_t i = __pyx_nargs; i < 2; i++) {
        if (unlikely(!values[i])) { __Pyx_RaiseArgtupleInvalid("visit_ResultRefNode", 1, 2, 2, i); __PYX_ERR(0, 449, __pyx_L3_error) }
      }
    } else if (unlikely(__pyx_nargs != 2)) {
      goto __pyx_L5_argtuple_error;
    } else {
      values[0] = __Pyx_ArgRef_FASTCALL(__pyx_args, 0);
      if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[0])) __PYX_ERR(0, 449, __pyx_L3_error)
      values[1] = __Pyx_ArgRef_FASTCALL(__pyx_args, 1);
      if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[1])) __PYX_ERR(0, 449, __pyx_L3_error)
    }
    __pyx_v_self = values[0];
    __pyx_v_node = values[1];
  }
  goto __pyx_L6_skip;
  __pyx_L5_argtuple_error:;
  __Pyx_RaiseArgtupleInvalid("visit_ResultRefNode", 1, 2, 2, __pyx_nargs); __PYX_ERR(0, 449, __pyx_L3_error)
  __pyx_L6_skip:;
  goto __pyx_L4_argument_unpacking_done;
  __pyx_L3_error:;
  for (Py_ssize_t __pyx_temp=0; __pyx_temp < (Py_ssize_t)(sizeof(values)/sizeof(values[0])); ++__pyx_temp) {
    Py_XDECREF(values[__pyx_temp]);
  }
  __Pyx_AddTraceback("Cython.Compiler.Visitor.NodeRefCleanupMixin.visit_ResultRefNode", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __Pyx_RefNannyFinishContext();
  return NULL;
  __pyx_L4_argument_unpacking_done:;
  __pyx_r = __pyx_pf_6Cython_8Compiler_7Visitor_19NodeRefCleanupMixin_4visit_ResultRefNode(__pyx_self, __pyx_v_self, __pyx_v_node);
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

static PyObject *__pyx_pf_6Cython_8Compiler_7Visitor_19NodeRefCleanupMixin_4visit_ResultRefNode(CYTHON_UNUSED PyObject *__pyx_self, PyObject *__pyx_v_self, PyObject *__pyx_v_node) {
  PyObject *__pyx_v_expr = NULL;
  PyObject *__pyx_r = NULL;
/* … */
  /* function exit code */
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_t_1);
  __Pyx_XDECREF(__pyx_t_4);
  __Pyx_XDECREF(__pyx_t_6);
  __Pyx_AddTraceback("Cython.Compiler.Visitor.NodeRefCleanupMixin.visit_ResultRefNode", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_r = NULL;
  __pyx_L0:;
  __Pyx_XDECREF(__pyx_v_expr);
  __Pyx_XGIVEREF(__pyx_r);
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}
/* … */
  __pyx_t_5 = __Pyx_CyFunction_New(&__pyx_mdef_6Cython_8Compiler_7Visitor_19NodeRefCleanupMixin_5visit_ResultRefNode, 0, __pyx_mstate_global->__pyx_n_u_NodeRefCleanupMixin_visit_Result, NULL, __pyx_mstate_global->__pyx_n_u_Cython_Compiler_Visitor, __pyx_mstate_global->__pyx_d, ((PyObject *)__pyx_mstate_global->__pyx_codeobj_tab[38])); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 449, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_5);
  #if CYTHON_COMPILING_IN_CPYTHON && PY_VERSION_HEX >= 0x030E0000
  PyUnstable_Object_EnableDeferredRefcount(__pyx_t_5);
  #endif
  if (__Pyx_SetNameInClass(__pyx_t_2, __pyx_mstate_global->__pyx_n_u_visit_ResultRefNode, __pyx_t_5) < (0)) __PYX_ERR(0, 449, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
```

</details>

L450  🟡  (score=2)
```python
        expr = node.expression
```
<details><summary>Show generated C (score=2)</summary>

```c
  __pyx_t_1 = __Pyx_PyObject_GetAttrStr(__pyx_v_node, __pyx_mstate_global->__pyx_n_u_expression); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 450, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __pyx_v_expr = __pyx_t_1;
  __pyx_t_1 = 0;
```

</details>

L451  🟠  (score=5)
```python
        if expr is None or expr not in self._replacements:
```
<details><summary>Show generated C (score=5)</summary>

```c
  __pyx_t_3 = (__pyx_v_expr == Py_None);
  if (!__pyx_t_3) {
  } else {
    __pyx_t_2 = __pyx_t_3;
    goto __pyx_L4_bool_binop_done;
  }
  __pyx_t_1 = __Pyx_PyObject_GetAttrStr(__pyx_v_self, __pyx_mstate_global->__pyx_n_u_replacements); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 451, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __pyx_t_3 = (__Pyx_PySequence_ContainsTF(__pyx_v_expr, __pyx_t_1, Py_NE)); if (unlikely((__pyx_t_3 < 0))) __PYX_ERR(0, 451, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __pyx_t_2 = __pyx_t_3;
  __pyx_L4_bool_binop_done:;
  if (__pyx_t_2) {
/* … */
  }
```

</details>

L452  🟠  (score=5)
```python
            self.visitchildren(node)
```
<details><summary>Show generated C (score=5)</summary>

```c
    __pyx_t_4 = __pyx_v_self;
    __Pyx_INCREF(__pyx_t_4);
    __pyx_t_5 = 0;
    {
      PyObject *__pyx_callargs[2] = {__pyx_t_4, __pyx_v_node};
      __pyx_t_1 = __Pyx_PyObject_FastCallMethod((PyObject*)__pyx_mstate_global->__pyx_n_u_visitchildren, __pyx_callargs+__pyx_t_5, (2-__pyx_t_5) | (1*__Pyx_PY_VECTORCALL_ARGUMENTS_OFFSET));
      __Pyx_XDECREF(__pyx_t_4); __pyx_t_4 = 0;
      if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 452, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_1);
    }
    __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
```

</details>

L453  🟡  (score=3)
```python
            expr = node.expression
```
<details><summary>Show generated C (score=3)</summary>

```c
    __pyx_t_1 = __Pyx_PyObject_GetAttrStr(__pyx_v_node, __pyx_mstate_global->__pyx_n_u_expression); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 453, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_1);
    __Pyx_DECREF_SET(__pyx_v_expr, __pyx_t_1);
    __pyx_t_1 = 0;
```

</details>

L454  ⚪  (score=0)
```python
        if expr is not None:
```
<details><summary>Show generated C (score=0)</summary>

```c
  __pyx_t_2 = (__pyx_v_expr != Py_None);
  if (__pyx_t_2) {
/* … */
  }
```

</details>

L455  🔴  (score=10)
```python
            node.expression = self._replacements.get(expr, expr)
```
<details><summary>Show generated C (score=10)</summary>

```c
    __pyx_t_6 = __Pyx_PyObject_GetAttrStr(__pyx_v_self, __pyx_mstate_global->__pyx_n_u_replacements); if (unlikely(!__pyx_t_6)) __PYX_ERR(0, 455, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_6);
    __pyx_t_4 = __pyx_t_6;
    __Pyx_INCREF(__pyx_t_4);
    __pyx_t_5 = 0;
    {
      PyObject *__pyx_callargs[3] = {__pyx_t_4, __pyx_v_expr, __pyx_v_expr};
      __pyx_t_1 = __Pyx_PyObject_FastCallMethod((PyObject*)__pyx_mstate_global->__pyx_n_u_get, __pyx_callargs+__pyx_t_5, (3-__pyx_t_5) | (1*__Pyx_PY_VECTORCALL_ARGUMENTS_OFFSET));
      __Pyx_XDECREF(__pyx_t_4); __pyx_t_4 = 0;
      __Pyx_DECREF(__pyx_t_6); __pyx_t_6 = 0;
      if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 455, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_1);
    }
    if (__Pyx_PyObject_SetAttrStr(__pyx_v_node, __pyx_mstate_global->__pyx_n_u_expression, __pyx_t_1) < (0)) __PYX_ERR(0, 455, __pyx_L1_error)
    __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
```

</details>

L456  🟡  (score=2)
```python
        return node
```
<details><summary>Show generated C (score=2)</summary>

```c
  __Pyx_XDECREF(__pyx_r);
  __Pyx_INCREF(__pyx_v_node);
  __pyx_r = __pyx_v_node;
  goto __pyx_L0;
```

</details>

L457  ⚪  (score=0)
```python
```
L458  🔴  (score=44)
```python
    def replace(self, node, replacement):
```
<details><summary>Show generated C (score=44)</summary>

```c
/* Python wrapper */
static PyObject *__pyx_pw_6Cython_8Compiler_7Visitor_19NodeRefCleanupMixin_7replace(PyObject *__pyx_self, 
#if CYTHON_METH_FASTCALL
PyObject *const *__pyx_args, Py_ssize_t __pyx_nargs, PyObject *__pyx_kwds
#else
PyObject *__pyx_args, PyObject *__pyx_kwds
#endif
); /*proto*/
PyDoc_STRVAR(__pyx_doc_6Cython_8Compiler_7Visitor_19NodeRefCleanupMixin_6replace, "File: Cython/Compiler/Visitor.py (starting at line 458)");
static PyMethodDef __pyx_mdef_6Cython_8Compiler_7Visitor_19NodeRefCleanupMixin_7replace = {"replace", (PyCFunction)(void(*)(void))(__Pyx_PyCFunction_FastCallWithKeywords)__pyx_pw_6Cython_8Compiler_7Visitor_19NodeRefCleanupMixin_7replace, __Pyx_METH_FASTCALL|METH_KEYWORDS, __pyx_doc_6Cython_8Compiler_7Visitor_19NodeRefCleanupMixin_6replace};
static PyObject *__pyx_pw_6Cython_8Compiler_7Visitor_19NodeRefCleanupMixin_7replace(PyObject *__pyx_self, 
#if CYTHON_METH_FASTCALL
PyObject *const *__pyx_args, Py_ssize_t __pyx_nargs, PyObject *__pyx_kwds
#else
PyObject *__pyx_args, PyObject *__pyx_kwds
#endif
) {
  PyObject *__pyx_v_self = 0;
  PyObject *__pyx_v_node = 0;
  PyObject *__pyx_v_replacement = 0;
  #if !CYTHON_METH_FASTCALL
  CYTHON_UNUSED Py_ssize_t __pyx_nargs;
  #endif
  CYTHON_UNUSED PyObject *const *__pyx_kwvalues;
  PyObject *__pyx_r = 0;
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("replace (wrapper)", 0);
  #if !CYTHON_METH_FASTCALL
  #if CYTHON_ASSUME_SAFE_SIZE
  __pyx_nargs = PyTuple_GET_SIZE(__pyx_args);
  #else
  __pyx_nargs = PyTuple_Size(__pyx_args); if (unlikely(__pyx_nargs < 0)) return NULL;
  #endif
  #endif
  __pyx_kwvalues = __Pyx_KwValues_FASTCALL(__pyx_args, __pyx_nargs);
  {
    PyObject ** const __pyx_pyargnames[] = {&__pyx_mstate_global->__pyx_n_u_self,&__pyx_mstate_global->__pyx_n_u_node,&__pyx_mstate_global->__pyx_n_u_replacement,0};
  PyObject* values[3] = {0,0,0};
    const Py_ssize_t __pyx_kwds_len = (__pyx_kwds) ? __Pyx_NumKwargs_FASTCALL(__pyx_kwds) : 0;
    if (unlikely(__pyx_kwds_len) < 0) __PYX_ERR(0, 458, __pyx_L3_error)
    if (__pyx_kwds_len > 0) {
      switch (__pyx_nargs) {
        case  3:
        values[2] = __Pyx_ArgRef_FASTCALL(__pyx_args, 2);
        if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[2])) __PYX_ERR(0, 458, __pyx_L3_error)
        CYTHON_FALLTHROUGH;
        case  2:
        values[1] = __Pyx_ArgRef_FASTCALL(__pyx_args, 1);
        if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[1])) __PYX_ERR(0, 458, __pyx_L3_error)
        CYTHON_FALLTHROUGH;
        case  1:
        values[0] = __Pyx_ArgRef_FASTCALL(__pyx_args, 0);
        if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[0])) __PYX_ERR(0, 458, __pyx_L3_error)
        CYTHON_FALLTHROUGH;
        case  0: break;
        default: goto __pyx_L5_argtuple_error;
      }
      const Py_ssize_t kwd_pos_args = __pyx_nargs;
      if (__Pyx_ParseKeywords(__pyx_kwds, __pyx_kwvalues, __pyx_pyargnames, 0, values, kwd_pos_args, __pyx_kwds_len, "replace", 0) < (0)) __PYX_ERR(0, 458, __pyx_L3_error)
      for (Py_ssize_t i = __pyx_nargs; i < 3; i++) {
        if (unlikely(!values[i])) { __Pyx_RaiseArgtupleInvalid("replace", 1, 3, 3, i); __PYX_ERR(0, 458, __pyx_L3_error) }
      }
    } else if (unlikely(__pyx_nargs != 3)) {
      goto __pyx_L5_argtuple_error;
    } else {
      values[0] = __Pyx_ArgRef_FASTCALL(__pyx_args, 0);
      if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[0])) __PYX_ERR(0, 458, __pyx_L3_error)
      values[1] = __Pyx_ArgRef_FASTCALL(__pyx_args, 1);
      if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[1])) __PYX_ERR(0, 458, __pyx_L3_error)
      values[2] = __Pyx_ArgRef_FASTCALL(__pyx_args, 2);
      if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[2])) __PYX_ERR(0, 458, __pyx_L3_error)
    }
    __pyx_v_self = values[0];
    __pyx_v_node = values[1];
    __pyx_v_replacement = values[2];
  }
  goto __pyx_L6_skip;
  __pyx_L5_argtuple_error:;
  __Pyx_RaiseArgtupleInvalid("replace", 1, 3, 3, __pyx_nargs); __PYX_ERR(0, 458, __pyx_L3_error)
  __pyx_L6_skip:;
  goto __pyx_L4_argument_unpacking_done;
  __pyx_L3_error:;
  for (Py_ssize_t __pyx_temp=0; __pyx_temp < (Py_ssize_t)(sizeof(values)/sizeof(values[0])); ++__pyx_temp) {
    Py_XDECREF(values[__pyx_temp]);
  }
  __Pyx_AddTraceback("Cython.Compiler.Visitor.NodeRefCleanupMixin.replace", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __Pyx_RefNannyFinishContext();
  return NULL;
  __pyx_L4_argument_unpacking_done:;
  __pyx_r = __pyx_pf_6Cython_8Compiler_7Visitor_19NodeRefCleanupMixin_6replace(__pyx_self, __pyx_v_self, __pyx_v_node, __pyx_v_replacement);
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

static PyObject *__pyx_pf_6Cython_8Compiler_7Visitor_19NodeRefCleanupMixin_6replace(CYTHON_UNUSED PyObject *__pyx_self, PyObject *__pyx_v_self, PyObject *__pyx_v_node, PyObject *__pyx_v_replacement) {
  PyObject *__pyx_r = NULL;
/* … */
  /* function exit code */
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_t_1);
  __Pyx_AddTraceback("Cython.Compiler.Visitor.NodeRefCleanupMixin.replace", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_r = NULL;
  __pyx_L0:;
  __Pyx_XGIVEREF(__pyx_r);
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}
/* … */
  __pyx_t_5 = __Pyx_CyFunction_New(&__pyx_mdef_6Cython_8Compiler_7Visitor_19NodeRefCleanupMixin_7replace, 0, __pyx_mstate_global->__pyx_n_u_NodeRefCleanupMixin_replace, NULL, __pyx_mstate_global->__pyx_n_u_Cython_Compiler_Visitor, __pyx_mstate_global->__pyx_d, ((PyObject *)__pyx_mstate_global->__pyx_codeobj_tab[39])); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 458, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_5);
  #if CYTHON_COMPILING_IN_CPYTHON && PY_VERSION_HEX >= 0x030E0000
  PyUnstable_Object_EnableDeferredRefcount(__pyx_t_5);
  #endif
  if (__Pyx_SetNameInClass(__pyx_t_2, __pyx_mstate_global->__pyx_n_u_replace, __pyx_t_5) < (0)) __PYX_ERR(0, 458, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
```

</details>

L459  🟠  (score=8)
```python
        self._replacements[node] = replacement
```
<details><summary>Show generated C (score=8)</summary>

```c
  __pyx_t_1 = __Pyx_PyObject_GetAttrStr(__pyx_v_self, __pyx_mstate_global->__pyx_n_u_replacements); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 459, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  if (unlikely((PyObject_SetItem(__pyx_t_1, __pyx_v_node, __pyx_v_replacement) < 0))) __PYX_ERR(0, 459, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
```

</details>

L460  🟡  (score=2)
```python
        return replacement
```
<details><summary>Show generated C (score=2)</summary>

```c
  __Pyx_XDECREF(__pyx_r);
  __Pyx_INCREF(__pyx_v_replacement);
  __pyx_r = __pyx_v_replacement;
  goto __pyx_L0;
```

</details>

L461  ⚪  (score=0)
```python
```
L462  ⚪  (score=0)
```python
```
L463  ⚪  (score=0)
```python
find_special_method_for_binary_operator = {
```
L464  🔴  (score=97)
```python
    '<':  '__lt__',
```
<details><summary>Show generated C (score=97)</summary>

```c
  __pyx_t_2 = __Pyx_PyDict_NewPresized(19); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 464, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  if (PyDict_SetItem(__pyx_t_2, __pyx_mstate_global->__pyx_kp_u__19, __pyx_mstate_global->__pyx_n_u_lt) < (0)) __PYX_ERR(0, 464, __pyx_L1_error)
  if (PyDict_SetItem(__pyx_t_2, __pyx_mstate_global->__pyx_kp_u__20, __pyx_mstate_global->__pyx_n_u_le) < (0)) __PYX_ERR(0, 464, __pyx_L1_error)
  if (PyDict_SetItem(__pyx_t_2, __pyx_mstate_global->__pyx_kp_u__21, __pyx_mstate_global->__pyx_n_u_eq) < (0)) __PYX_ERR(0, 464, __pyx_L1_error)
  if (PyDict_SetItem(__pyx_t_2, __pyx_mstate_global->__pyx_kp_u__22, __pyx_mstate_global->__pyx_n_u_ne) < (0)) __PYX_ERR(0, 464, __pyx_L1_error)
  if (PyDict_SetItem(__pyx_t_2, __pyx_mstate_global->__pyx_kp_u__23, __pyx_mstate_global->__pyx_n_u_ge) < (0)) __PYX_ERR(0, 464, __pyx_L1_error)
  if (PyDict_SetItem(__pyx_t_2, __pyx_mstate_global->__pyx_kp_u__24, __pyx_mstate_global->__pyx_n_u_gt) < (0)) __PYX_ERR(0, 464, __pyx_L1_error)
  if (PyDict_SetItem(__pyx_t_2, __pyx_mstate_global->__pyx_kp_u__25, __pyx_mstate_global->__pyx_n_u_add) < (0)) __PYX_ERR(0, 464, __pyx_L1_error)
  if (PyDict_SetItem(__pyx_t_2, __pyx_mstate_global->__pyx_kp_u__26, __pyx_mstate_global->__pyx_n_u_and) < (0)) __PYX_ERR(0, 464, __pyx_L1_error)
  if (PyDict_SetItem(__pyx_t_2, __pyx_mstate_global->__pyx_kp_u__16, __pyx_mstate_global->__pyx_n_u_div) < (0)) __PYX_ERR(0, 464, __pyx_L1_error)
  if (PyDict_SetItem(__pyx_t_2, __pyx_mstate_global->__pyx_kp_u__27, __pyx_mstate_global->__pyx_n_u_floordiv) < (0)) __PYX_ERR(0, 464, __pyx_L1_error)
  if (PyDict_SetItem(__pyx_t_2, __pyx_mstate_global->__pyx_kp_u__28, __pyx_mstate_global->__pyx_n_u_lshift) < (0)) __PYX_ERR(0, 464, __pyx_L1_error)
  if (PyDict_SetItem(__pyx_t_2, __pyx_mstate_global->__pyx_kp_u__29, __pyx_mstate_global->__pyx_n_u_mod) < (0)) __PYX_ERR(0, 464, __pyx_L1_error)
  if (PyDict_SetItem(__pyx_t_2, __pyx_mstate_global->__pyx_kp_u__30, __pyx_mstate_global->__pyx_n_u_mul) < (0)) __PYX_ERR(0, 464, __pyx_L1_error)
  if (PyDict_SetItem(__pyx_t_2, __pyx_mstate_global->__pyx_kp_u__31, __pyx_mstate_global->__pyx_n_u_or) < (0)) __PYX_ERR(0, 464, __pyx_L1_error)
  if (PyDict_SetItem(__pyx_t_2, __pyx_mstate_global->__pyx_kp_u__32, __pyx_mstate_global->__pyx_n_u_pow) < (0)) __PYX_ERR(0, 464, __pyx_L1_error)
  if (PyDict_SetItem(__pyx_t_2, __pyx_mstate_global->__pyx_kp_u__33, __pyx_mstate_global->__pyx_n_u_rshift) < (0)) __PYX_ERR(0, 464, __pyx_L1_error)
  if (PyDict_SetItem(__pyx_t_2, __pyx_mstate_global->__pyx_kp_u__34, __pyx_mstate_global->__pyx_n_u_sub) < (0)) __PYX_ERR(0, 464, __pyx_L1_error)
  if (PyDict_SetItem(__pyx_t_2, __pyx_mstate_global->__pyx_kp_u__35, __pyx_mstate_global->__pyx_n_u_xor) < (0)) __PYX_ERR(0, 464, __pyx_L1_error)
  if (PyDict_SetItem(__pyx_t_2, __pyx_mstate_global->__pyx_n_u_in_3, __pyx_mstate_global->__pyx_n_u_contains) < (0)) __PYX_ERR(0, 464, __pyx_L1_error)
```

</details>

L465  ⚪  (score=0)
```python
    '<=': '__le__',
```
L466  ⚪  (score=0)
```python
    '==': '__eq__',
```
L467  ⚪  (score=0)
```python
    '!=': '__ne__',
```
L468  ⚪  (score=0)
```python
    '>=': '__ge__',
```
L469  ⚪  (score=0)
```python
    '>':  '__gt__',
```
L470  ⚪  (score=0)
```python
    '+':  '__add__',
```
L471  ⚪  (score=0)
```python
    '&':  '__and__',
```
L472  ⚪  (score=0)
```python
    '/':  '__div__',
```
L473  ⚪  (score=0)
```python
    '//': '__floordiv__',
```
L474  ⚪  (score=0)
```python
    '<<': '__lshift__',
```
L475  ⚪  (score=0)
```python
    '%':  '__mod__',
```
L476  ⚪  (score=0)
```python
    '*':  '__mul__',
```
L477  ⚪  (score=0)
```python
    '|':  '__or__',
```
L478  ⚪  (score=0)
```python
    '**': '__pow__',
```
L479  ⚪  (score=0)
```python
    '>>': '__rshift__',
```
L480  ⚪  (score=0)
```python
    '-':  '__sub__',
```
L481  ⚪  (score=0)
```python
    '^':  '__xor__',
```
L482  ⚪  (score=0)
```python
    'in': '__contains__',
```
L483  🟠  (score=9)
```python
}.get
```
<details><summary>Show generated C (score=9)</summary>

```c
  __pyx_t_5 = __Pyx_PyObject_GetAttrStr(__pyx_t_2, __pyx_mstate_global->__pyx_n_u_get); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 483, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_5);
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  if (PyDict_SetItem(__pyx_mstate_global->__pyx_d, __pyx_mstate_global->__pyx_n_u_find_special_method_for_binary_o, __pyx_t_5) < (0)) __PYX_ERR(0, 463, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
```

</details>

L484  ⚪  (score=0)
```python
```
L485  ⚪  (score=0)
```python
```
L486  ⚪  (score=0)
```python
find_special_method_for_unary_operator = {
```
L487  🔴  (score=22)
```python
    'not': '__not__',
```
<details><summary>Show generated C (score=22)</summary>

```c
  __pyx_t_5 = __Pyx_PyDict_NewPresized(4); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 487, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_5);
  if (PyDict_SetItem(__pyx_t_5, __pyx_mstate_global->__pyx_n_u_not, __pyx_mstate_global->__pyx_n_u_not_2) < (0)) __PYX_ERR(0, 487, __pyx_L1_error)
  if (PyDict_SetItem(__pyx_t_5, __pyx_mstate_global->__pyx_kp_u__36, __pyx_mstate_global->__pyx_n_u_inv) < (0)) __PYX_ERR(0, 487, __pyx_L1_error)
  if (PyDict_SetItem(__pyx_t_5, __pyx_mstate_global->__pyx_kp_u__34, __pyx_mstate_global->__pyx_n_u_neg) < (0)) __PYX_ERR(0, 487, __pyx_L1_error)
  if (PyDict_SetItem(__pyx_t_5, __pyx_mstate_global->__pyx_kp_u__25, __pyx_mstate_global->__pyx_n_u_pos_3) < (0)) __PYX_ERR(0, 487, __pyx_L1_error)
```

</details>

L488  ⚪  (score=0)
```python
    '~':   '__inv__',
```
L489  ⚪  (score=0)
```python
    '-':   '__neg__',
```
L490  ⚪  (score=0)
```python
    '+':   '__pos__',
```
L491  🟠  (score=9)
```python
}.get
```
<details><summary>Show generated C (score=9)</summary>

```c
  __pyx_t_2 = __Pyx_PyObject_GetAttrStr(__pyx_t_5, __pyx_mstate_global->__pyx_n_u_get); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 491, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
  if (PyDict_SetItem(__pyx_mstate_global->__pyx_d, __pyx_mstate_global->__pyx_n_u_find_special_method_for_unary_op, __pyx_t_2) < (0)) __PYX_ERR(0, 486, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
```

</details>

L492  ⚪  (score=0)
```python
```
L493  ⚪  (score=0)
```python
```
L494  ⚪  (score=0)
```python
class MethodDispatcherTransform(EnvTransform):
```
<details><summary>Show generated C (score=0)</summary>

```c
struct __pyx_vtabstruct_6Cython_8Compiler_7Visitor_MethodDispatcherTransform {
  struct __pyx_vtabstruct_6Cython_8Compiler_7Visitor_EnvTransform __pyx_base;
  PyObject *(*_visit_binop_node)(struct __pyx_obj_6Cython_8Compiler_7Visitor_MethodDispatcherTransform *, PyObject *);
  PyObject *(*_find_handler)(struct __pyx_obj_6Cython_8Compiler_7Visitor_MethodDispatcherTransform *, PyObject *, int);
  PyObject *(*_delegate_to_assigned_value)(struct __pyx_obj_6Cython_8Compiler_7Visitor_MethodDispatcherTransform *, PyObject *, PyObject *, PyObject *, PyObject *);
  PyObject *(*_dispatch_to_handler)(struct __pyx_obj_6Cython_8Compiler_7Visitor_MethodDispatcherTransform *, PyObject *, PyObject *, PyObject *, PyObject *);
  PyObject *(*_dispatch_to_method_handler)(struct __pyx_obj_6Cython_8Compiler_7Visitor_MethodDispatcherTransform *, PyObject *, PyObject *, PyObject *, PyObject *, PyObject *, PyObject *, PyObject *, PyObject *);
};
static struct __pyx_vtabstruct_6Cython_8Compiler_7Visitor_MethodDispatcherTransform *__pyx_vtabptr_6Cython_8Compiler_7Visitor_MethodDispatcherTransform;

```

</details>

L495  ⚪  (score=0)
```python
    """
```
L496  ⚪  (score=0)
```python
    Base class for transformations that want to intercept on specific
```
L497  ⚪  (score=0)
```python
    builtin functions or methods of builtin types, including special
```
L498  ⚪  (score=0)
```python
    methods triggered by Python operators.  Must run after declaration
```
L499  ⚪  (score=0)
```python
    analysis when entries were assigned.
```
L500  ⚪  (score=0)
```python
```
L501  ⚪  (score=0)
```python
    Naming pattern for handler methods is as follows:
```
L502  ⚪  (score=0)
```python
```
L503  ⚪  (score=0)
```python
    * builtin functions: _handle_(general|simple|any)_function_NAME
```
L504  ⚪  (score=0)
```python
```
L505  ⚪  (score=0)
```python
    * builtin methods: _handle_(general|simple|any)_method_TYPENAME_METHODNAME
```
L506  ⚪  (score=0)
```python
    """
```
L507  ⚪  (score=0)
```python
    # only visit call nodes and Python operations
```
L508  🔴  (score=41)
```python
    def visit_GeneralCallNode(self, node):
```
<details><summary>Show generated C (score=41)</summary>

```c
/* Python wrapper */
static PyObject *__pyx_pw_6Cython_8Compiler_7Visitor_25MethodDispatcherTransform_1visit_GeneralCallNode(PyObject *__pyx_v_self, 
#if CYTHON_METH_FASTCALL
PyObject *const *__pyx_args, Py_ssize_t __pyx_nargs, PyObject *__pyx_kwds
#else
PyObject *__pyx_args, PyObject *__pyx_kwds
#endif
); /*proto*/
PyDoc_STRVAR(__pyx_doc_6Cython_8Compiler_7Visitor_25MethodDispatcherTransform_visit_GeneralCallNode, "File: Cython/Compiler/Visitor.py (starting at line 508)");
static PyMethodDef __pyx_mdef_6Cython_8Compiler_7Visitor_25MethodDispatcherTransform_1visit_GeneralCallNode = {"visit_GeneralCallNode", (PyCFunction)(void(*)(void))(__Pyx_PyCFunction_FastCallWithKeywords)__pyx_pw_6Cython_8Compiler_7Visitor_25MethodDispatcherTransform_1visit_GeneralCallNode, __Pyx_METH_FASTCALL|METH_KEYWORDS, __pyx_doc_6Cython_8Compiler_7Visitor_25MethodDispatcherTransform_visit_GeneralCallNode};
static PyObject *__pyx_pw_6Cython_8Compiler_7Visitor_25MethodDispatcherTransform_1visit_GeneralCallNode(PyObject *__pyx_v_self, 
#if CYTHON_METH_FASTCALL
PyObject *const *__pyx_args, Py_ssize_t __pyx_nargs, PyObject *__pyx_kwds
#else
PyObject *__pyx_args, PyObject *__pyx_kwds
#endif
) {
  PyObject *__pyx_v_node = 0;
  #if !CYTHON_METH_FASTCALL
  CYTHON_UNUSED Py_ssize_t __pyx_nargs;
  #endif
  CYTHON_UNUSED PyObject *const *__pyx_kwvalues;
  PyObject *__pyx_r = 0;
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("visit_GeneralCallNode (wrapper)", 0);
  #if !CYTHON_METH_FASTCALL
  #if CYTHON_ASSUME_SAFE_SIZE
  __pyx_nargs = PyTuple_GET_SIZE(__pyx_args);
  #else
  __pyx_nargs = PyTuple_Size(__pyx_args); if (unlikely(__pyx_nargs < 0)) return NULL;
  #endif
  #endif
  __pyx_kwvalues = __Pyx_KwValues_FASTCALL(__pyx_args, __pyx_nargs);
  {
    PyObject ** const __pyx_pyargnames[] = {&__pyx_mstate_global->__pyx_n_u_node,0};
  PyObject* values[1] = {0};
    const Py_ssize_t __pyx_kwds_len = (__pyx_kwds) ? __Pyx_NumKwargs_FASTCALL(__pyx_kwds) : 0;
    if (unlikely(__pyx_kwds_len) < 0) __PYX_ERR(0, 508, __pyx_L3_error)
    if (__pyx_kwds_len > 0) {
      switch (__pyx_nargs) {
        case  1:
        values[0] = __Pyx_ArgRef_FASTCALL(__pyx_args, 0);
        if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[0])) __PYX_ERR(0, 508, __pyx_L3_error)
        CYTHON_FALLTHROUGH;
        case  0: break;
        default: goto __pyx_L5_argtuple_error;
      }
      const Py_ssize_t kwd_pos_args = __pyx_nargs;
      if (__Pyx_ParseKeywords(__pyx_kwds, __pyx_kwvalues, __pyx_pyargnames, 0, values, kwd_pos_args, __pyx_kwds_len, "visit_GeneralCallNode", 0) < (0)) __PYX_ERR(0, 508, __pyx_L3_error)
      for (Py_ssize_t i = __pyx_nargs; i < 1; i++) {
        if (unlikely(!values[i])) { __Pyx_RaiseArgtupleInvalid("visit_GeneralCallNode", 1, 1, 1, i); __PYX_ERR(0, 508, __pyx_L3_error) }
      }
    } else if (unlikely(__pyx_nargs != 1)) {
      goto __pyx_L5_argtuple_error;
    } else {
      values[0] = __Pyx_ArgRef_FASTCALL(__pyx_args, 0);
      if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[0])) __PYX_ERR(0, 508, __pyx_L3_error)
    }
    __pyx_v_node = values[0];
  }
  goto __pyx_L6_skip;
  __pyx_L5_argtuple_error:;
  __Pyx_RaiseArgtupleInvalid("visit_GeneralCallNode", 1, 1, 1, __pyx_nargs); __PYX_ERR(0, 508, __pyx_L3_error)
  __pyx_L6_skip:;
  goto __pyx_L4_argument_unpacking_done;
  __pyx_L3_error:;
  for (Py_ssize_t __pyx_temp=0; __pyx_temp < (Py_ssize_t)(sizeof(values)/sizeof(values[0])); ++__pyx_temp) {
    Py_XDECREF(values[__pyx_temp]);
  }
  __Pyx_AddTraceback("Cython.Compiler.Visitor.MethodDispatcherTransform.visit_GeneralCallNode", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __Pyx_RefNannyFinishContext();
  return NULL;
  __pyx_L4_argument_unpacking_done:;
  __pyx_r = __pyx_pf_6Cython_8Compiler_7Visitor_25MethodDispatcherTransform_visit_GeneralCallNode(((struct __pyx_obj_6Cython_8Compiler_7Visitor_MethodDispatcherTransform *)__pyx_v_self), __pyx_v_node);
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

static PyObject *__pyx_pf_6Cython_8Compiler_7Visitor_25MethodDispatcherTransform_visit_GeneralCallNode(struct __pyx_obj_6Cython_8Compiler_7Visitor_MethodDispatcherTransform *__pyx_v_self, PyObject *__pyx_v_node) {
  PyObject *__pyx_v_function = NULL;
  PyObject *__pyx_v_arg_tuple = NULL;
  PyObject *__pyx_v_keyword_args = NULL;
  PyObject *__pyx_v_args = NULL;
  PyObject *__pyx_r = NULL;
/* … */
  /* function exit code */
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_t_1);
  __Pyx_XDECREF(__pyx_t_2);
  __Pyx_AddTraceback("Cython.Compiler.Visitor.MethodDispatcherTransform.visit_GeneralCallNode", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_r = NULL;
  __pyx_L0:;
  __Pyx_XDECREF(__pyx_v_function);
  __Pyx_XDECREF(__pyx_v_arg_tuple);
  __Pyx_XDECREF(__pyx_v_keyword_args);
  __Pyx_XDECREF(__pyx_v_args);
  __Pyx_XGIVEREF(__pyx_r);
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}
/* … */
  __pyx_t_2 = __Pyx_CyFunction_New(&__pyx_mdef_6Cython_8Compiler_7Visitor_25MethodDispatcherTransform_1visit_GeneralCallNode, __Pyx_CYFUNCTION_CCLASS, __pyx_mstate_global->__pyx_n_u_MethodDispatcherTransform_visit, NULL, __pyx_mstate_global->__pyx_n_u_Cython_Compiler_Visitor, __pyx_mstate_global->__pyx_d, ((PyObject *)__pyx_mstate_global->__pyx_codeobj_tab[40])); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 508, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  #if CYTHON_COMPILING_IN_CPYTHON && PY_VERSION_HEX >= 0x030E0000
  PyUnstable_Object_EnableDeferredRefcount(__pyx_t_2);
  #endif
  if (__Pyx_SetItemOnTypeDict(__pyx_mstate_global->__pyx_ptype_6Cython_8Compiler_7Visitor_MethodDispatcherTransform, __pyx_mstate_global->__pyx_n_u_visit_GeneralCallNode, __pyx_t_2) < (0)) __PYX_ERR(0, 508, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
```

</details>

L509  🟡  (score=1)
```python
        self._process_children(node)
```
<details><summary>Show generated C (score=1)</summary>

```c
  __pyx_t_1 = ((struct __pyx_vtabstruct_6Cython_8Compiler_7Visitor_MethodDispatcherTransform *)__pyx_v_self->__pyx_base.__pyx_base.__pyx_base.__pyx_base.__pyx_vtab)->__pyx_base.__pyx_base.__pyx_base._process_children(((struct __pyx_obj_6Cython_8Compiler_7Visitor_VisitorTransform *)__pyx_v_self), __pyx_v_node, NULL); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 509, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
```

</details>

L510  🟡  (score=2)
```python
        function = node.function
```
<details><summary>Show generated C (score=2)</summary>

```c
  __pyx_t_1 = __Pyx_PyObject_GetAttrStr(__pyx_v_node, __pyx_mstate_global->__pyx_n_u_function); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 510, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __pyx_v_function = __pyx_t_1;
  __pyx_t_1 = 0;
```

</details>

L511  🟠  (score=8)
```python
        if not function.type.is_pyobject:
```
<details><summary>Show generated C (score=8)</summary>

```c
  __pyx_t_1 = __Pyx_PyObject_GetAttrStr(__pyx_v_function, __pyx_mstate_global->__pyx_n_u_type); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 511, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __pyx_t_2 = __Pyx_PyObject_GetAttrStr(__pyx_t_1, __pyx_mstate_global->__pyx_n_u_is_pyobject); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 511, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __pyx_t_3 = __Pyx_PyObject_IsTrue(__pyx_t_2); if (unlikely((__pyx_t_3 < 0))) __PYX_ERR(0, 511, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __pyx_t_4 = (!__pyx_t_3);
  if (__pyx_t_4) {
/* … */
  }
```

</details>

L512  🟡  (score=2)
```python
            return node
```
<details><summary>Show generated C (score=2)</summary>

```c
    __Pyx_XDECREF(__pyx_r);
    __Pyx_INCREF(__pyx_v_node);
    __pyx_r = __pyx_v_node;
    goto __pyx_L0;
```

</details>

L513  🟡  (score=2)
```python
        arg_tuple = node.positional_args
```
<details><summary>Show generated C (score=2)</summary>

```c
  __pyx_t_2 = __Pyx_PyObject_GetAttrStr(__pyx_v_node, __pyx_mstate_global->__pyx_n_u_positional_args); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 513, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __pyx_v_arg_tuple = __pyx_t_2;
  __pyx_t_2 = 0;
```

</details>

L514  🔴  (score=11)
```python
        if not isinstance(arg_tuple, ExprNodes.TupleNode):
```
<details><summary>Show generated C (score=11)</summary>

```c
  __Pyx_GetModuleGlobalName(__pyx_t_2, __pyx_mstate_global->__pyx_n_u_ExprNodes); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 514, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __pyx_t_1 = __Pyx_PyObject_GetAttrStr(__pyx_t_2, __pyx_mstate_global->__pyx_n_u_TupleNode); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 514, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __pyx_t_4 = PyObject_IsInstance(__pyx_v_arg_tuple, __pyx_t_1); if (unlikely(__pyx_t_4 == ((int)-1))) __PYX_ERR(0, 514, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __pyx_t_3 = (!__pyx_t_4);
  if (__pyx_t_3) {
/* … */
  }
```

</details>

L515  🟡  (score=2)
```python
            return node
```
<details><summary>Show generated C (score=2)</summary>

```c
    __Pyx_XDECREF(__pyx_r);
    __Pyx_INCREF(__pyx_v_node);
    __pyx_r = __pyx_v_node;
    goto __pyx_L0;
```

</details>

L516  🟡  (score=2)
```python
        keyword_args = node.keyword_args
```
<details><summary>Show generated C (score=2)</summary>

```c
  __pyx_t_1 = __Pyx_PyObject_GetAttrStr(__pyx_v_node, __pyx_mstate_global->__pyx_n_u_keyword_args); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 516, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __pyx_v_keyword_args = __pyx_t_1;
  __pyx_t_1 = 0;
```

</details>

L517  🔴  (score=13)
```python
        if keyword_args and not isinstance(keyword_args, ExprNodes.DictNode):
```
<details><summary>Show generated C (score=13)</summary>

```c
  __pyx_t_4 = __Pyx_PyObject_IsTrue(__pyx_v_keyword_args); if (unlikely((__pyx_t_4 < 0))) __PYX_ERR(0, 517, __pyx_L1_error)
  if (__pyx_t_4) {
  } else {
    __pyx_t_3 = __pyx_t_4;
    goto __pyx_L6_bool_binop_done;
  }
  __Pyx_GetModuleGlobalName(__pyx_t_1, __pyx_mstate_global->__pyx_n_u_ExprNodes); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 517, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __pyx_t_2 = __Pyx_PyObject_GetAttrStr(__pyx_t_1, __pyx_mstate_global->__pyx_n_u_DictNode); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 517, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __pyx_t_4 = PyObject_IsInstance(__pyx_v_keyword_args, __pyx_t_2); if (unlikely(__pyx_t_4 == ((int)-1))) __PYX_ERR(0, 517, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __pyx_t_5 = (!__pyx_t_4);
  __pyx_t_3 = __pyx_t_5;
  __pyx_L6_bool_binop_done:;
  if (__pyx_t_3) {
/* … */
  }
```

</details>

L518  ⚪  (score=0)
```python
            # can't handle **kwargs
```
L519  🟡  (score=2)
```python
            return node
```
<details><summary>Show generated C (score=2)</summary>

```c
    __Pyx_XDECREF(__pyx_r);
    __Pyx_INCREF(__pyx_v_node);
    __pyx_r = __pyx_v_node;
    goto __pyx_L0;
```

</details>

L520  🟡  (score=2)
```python
        args = arg_tuple.args
```
<details><summary>Show generated C (score=2)</summary>

```c
  __pyx_t_2 = __Pyx_PyObject_GetAttrStr(__pyx_v_arg_tuple, __pyx_mstate_global->__pyx_n_u_args); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 520, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __pyx_v_args = __pyx_t_2;
  __pyx_t_2 = 0;
```

</details>

L521  🟡  (score=1)
```python
        return self._dispatch_to_handler(node, function, args, keyword_args)
```
<details><summary>Show generated C (score=1)</summary>

```c
  __Pyx_XDECREF(__pyx_r);
  __pyx_t_2 = ((struct __pyx_vtabstruct_6Cython_8Compiler_7Visitor_MethodDispatcherTransform *)__pyx_v_self->__pyx_base.__pyx_base.__pyx_base.__pyx_base.__pyx_vtab)->_dispatch_to_handler(__pyx_v_self, __pyx_v_node, __pyx_v_function, __pyx_v_args, __pyx_v_keyword_args); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 521, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __pyx_r = __pyx_t_2;
  __pyx_t_2 = 0;
  goto __pyx_L0;
```

</details>

L522  ⚪  (score=0)
```python
```
L523  🔴  (score=40)
```python
    def visit_SimpleCallNode(self, node):
```
<details><summary>Show generated C (score=40)</summary>

```c
/* Python wrapper */
static PyObject *__pyx_pw_6Cython_8Compiler_7Visitor_25MethodDispatcherTransform_3visit_SimpleCallNode(PyObject *__pyx_v_self, 
#if CYTHON_METH_FASTCALL
PyObject *const *__pyx_args, Py_ssize_t __pyx_nargs, PyObject *__pyx_kwds
#else
PyObject *__pyx_args, PyObject *__pyx_kwds
#endif
); /*proto*/
PyDoc_STRVAR(__pyx_doc_6Cython_8Compiler_7Visitor_25MethodDispatcherTransform_2visit_SimpleCallNode, "File: Cython/Compiler/Visitor.py (starting at line 523)");
static PyMethodDef __pyx_mdef_6Cython_8Compiler_7Visitor_25MethodDispatcherTransform_3visit_SimpleCallNode = {"visit_SimpleCallNode", (PyCFunction)(void(*)(void))(__Pyx_PyCFunction_FastCallWithKeywords)__pyx_pw_6Cython_8Compiler_7Visitor_25MethodDispatcherTransform_3visit_SimpleCallNode, __Pyx_METH_FASTCALL|METH_KEYWORDS, __pyx_doc_6Cython_8Compiler_7Visitor_25MethodDispatcherTransform_2visit_SimpleCallNode};
static PyObject *__pyx_pw_6Cython_8Compiler_7Visitor_25MethodDispatcherTransform_3visit_SimpleCallNode(PyObject *__pyx_v_self, 
#if CYTHON_METH_FASTCALL
PyObject *const *__pyx_args, Py_ssize_t __pyx_nargs, PyObject *__pyx_kwds
#else
PyObject *__pyx_args, PyObject *__pyx_kwds
#endif
) {
  PyObject *__pyx_v_node = 0;
  #if !CYTHON_METH_FASTCALL
  CYTHON_UNUSED Py_ssize_t __pyx_nargs;
  #endif
  CYTHON_UNUSED PyObject *const *__pyx_kwvalues;
  PyObject *__pyx_r = 0;
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("visit_SimpleCallNode (wrapper)", 0);
  #if !CYTHON_METH_FASTCALL
  #if CYTHON_ASSUME_SAFE_SIZE
  __pyx_nargs = PyTuple_GET_SIZE(__pyx_args);
  #else
  __pyx_nargs = PyTuple_Size(__pyx_args); if (unlikely(__pyx_nargs < 0)) return NULL;
  #endif
  #endif
  __pyx_kwvalues = __Pyx_KwValues_FASTCALL(__pyx_args, __pyx_nargs);
  {
    PyObject ** const __pyx_pyargnames[] = {&__pyx_mstate_global->__pyx_n_u_node,0};
  PyObject* values[1] = {0};
    const Py_ssize_t __pyx_kwds_len = (__pyx_kwds) ? __Pyx_NumKwargs_FASTCALL(__pyx_kwds) : 0;
    if (unlikely(__pyx_kwds_len) < 0) __PYX_ERR(0, 523, __pyx_L3_error)
    if (__pyx_kwds_len > 0) {
      switch (__pyx_nargs) {
        case  1:
        values[0] = __Pyx_ArgRef_FASTCALL(__pyx_args, 0);
        if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[0])) __PYX_ERR(0, 523, __pyx_L3_error)
        CYTHON_FALLTHROUGH;
        case  0: break;
        default: goto __pyx_L5_argtuple_error;
      }
      const Py_ssize_t kwd_pos_args = __pyx_nargs;
      if (__Pyx_ParseKeywords(__pyx_kwds, __pyx_kwvalues, __pyx_pyargnames, 0, values, kwd_pos_args, __pyx_kwds_len, "visit_SimpleCallNode", 0) < (0)) __PYX_ERR(0, 523, __pyx_L3_error)
      for (Py_ssize_t i = __pyx_nargs; i < 1; i++) {
        if (unlikely(!values[i])) { __Pyx_RaiseArgtupleInvalid("visit_SimpleCallNode", 1, 1, 1, i); __PYX_ERR(0, 523, __pyx_L3_error) }
      }
    } else if (unlikely(__pyx_nargs != 1)) {
      goto __pyx_L5_argtuple_error;
    } else {
      values[0] = __Pyx_ArgRef_FASTCALL(__pyx_args, 0);
      if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[0])) __PYX_ERR(0, 523, __pyx_L3_error)
    }
    __pyx_v_node = values[0];
  }
  goto __pyx_L6_skip;
  __pyx_L5_argtuple_error:;
  __Pyx_RaiseArgtupleInvalid("visit_SimpleCallNode", 1, 1, 1, __pyx_nargs); __PYX_ERR(0, 523, __pyx_L3_error)
  __pyx_L6_skip:;
  goto __pyx_L4_argument_unpacking_done;
  __pyx_L3_error:;
  for (Py_ssize_t __pyx_temp=0; __pyx_temp < (Py_ssize_t)(sizeof(values)/sizeof(values[0])); ++__pyx_temp) {
    Py_XDECREF(values[__pyx_temp]);
  }
  __Pyx_AddTraceback("Cython.Compiler.Visitor.MethodDispatcherTransform.visit_SimpleCallNode", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __Pyx_RefNannyFinishContext();
  return NULL;
  __pyx_L4_argument_unpacking_done:;
  __pyx_r = __pyx_pf_6Cython_8Compiler_7Visitor_25MethodDispatcherTransform_2visit_SimpleCallNode(((struct __pyx_obj_6Cython_8Compiler_7Visitor_MethodDispatcherTransform *)__pyx_v_self), __pyx_v_node);
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

static PyObject *__pyx_pf_6Cython_8Compiler_7Visitor_25MethodDispatcherTransform_2visit_SimpleCallNode(struct __pyx_obj_6Cython_8Compiler_7Visitor_MethodDispatcherTransform *__pyx_v_self, PyObject *__pyx_v_node) {
  PyObject *__pyx_v_function = NULL;
  PyObject *__pyx_v_arg_tuple = NULL;
  PyObject *__pyx_v_args = NULL;
  PyObject *__pyx_r = NULL;
/* … */
  /* function exit code */
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_t_1);
  __Pyx_XDECREF(__pyx_t_2);
  __Pyx_AddTraceback("Cython.Compiler.Visitor.MethodDispatcherTransform.visit_SimpleCallNode", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_r = NULL;
  __pyx_L0:;
  __Pyx_XDECREF(__pyx_v_function);
  __Pyx_XDECREF(__pyx_v_arg_tuple);
  __Pyx_XDECREF(__pyx_v_args);
  __Pyx_XGIVEREF(__pyx_r);
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}
/* … */
  __pyx_t_2 = __Pyx_CyFunction_New(&__pyx_mdef_6Cython_8Compiler_7Visitor_25MethodDispatcherTransform_3visit_SimpleCallNode, __Pyx_CYFUNCTION_CCLASS, __pyx_mstate_global->__pyx_n_u_MethodDispatcherTransform_visit_2, NULL, __pyx_mstate_global->__pyx_n_u_Cython_Compiler_Visitor, __pyx_mstate_global->__pyx_d, ((PyObject *)__pyx_mstate_global->__pyx_codeobj_tab[41])); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 523, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  #if CYTHON_COMPILING_IN_CPYTHON && PY_VERSION_HEX >= 0x030E0000
  PyUnstable_Object_EnableDeferredRefcount(__pyx_t_2);
  #endif
  if (__Pyx_SetItemOnTypeDict(__pyx_mstate_global->__pyx_ptype_6Cython_8Compiler_7Visitor_MethodDispatcherTransform, __pyx_mstate_global->__pyx_n_u_visit_SimpleCallNode, __pyx_t_2) < (0)) __PYX_ERR(0, 523, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
```

</details>

L524  🟡  (score=1)
```python
        self._process_children(node)
```
<details><summary>Show generated C (score=1)</summary>

```c
  __pyx_t_1 = ((struct __pyx_vtabstruct_6Cython_8Compiler_7Visitor_MethodDispatcherTransform *)__pyx_v_self->__pyx_base.__pyx_base.__pyx_base.__pyx_base.__pyx_vtab)->__pyx_base.__pyx_base.__pyx_base._process_children(((struct __pyx_obj_6Cython_8Compiler_7Visitor_VisitorTransform *)__pyx_v_self), __pyx_v_node, NULL); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 524, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
```

</details>

L525  🟡  (score=2)
```python
        function = node.function
```
<details><summary>Show generated C (score=2)</summary>

```c
  __pyx_t_1 = __Pyx_PyObject_GetAttrStr(__pyx_v_node, __pyx_mstate_global->__pyx_n_u_function); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 525, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __pyx_v_function = __pyx_t_1;
  __pyx_t_1 = 0;
```

</details>

L526  🟠  (score=8)
```python
        if function.type.is_pyobject:
```
<details><summary>Show generated C (score=8)</summary>

```c
  __pyx_t_1 = __Pyx_PyObject_GetAttrStr(__pyx_v_function, __pyx_mstate_global->__pyx_n_u_type); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 526, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __pyx_t_2 = __Pyx_PyObject_GetAttrStr(__pyx_t_1, __pyx_mstate_global->__pyx_n_u_is_pyobject); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 526, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __pyx_t_3 = __Pyx_PyObject_IsTrue(__pyx_t_2); if (unlikely((__pyx_t_3 < 0))) __PYX_ERR(0, 526, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  if (__pyx_t_3) {
/* … */
    goto __pyx_L3;
  }
```

</details>

L527  🟡  (score=2)
```python
            arg_tuple = node.arg_tuple
```
<details><summary>Show generated C (score=2)</summary>

```c
    __pyx_t_2 = __Pyx_PyObject_GetAttrStr(__pyx_v_node, __pyx_mstate_global->__pyx_n_u_arg_tuple); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 527, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_2);
    __pyx_v_arg_tuple = __pyx_t_2;
    __pyx_t_2 = 0;
```

</details>

L528  🔴  (score=11)
```python
            if not isinstance(arg_tuple, ExprNodes.TupleNode):
```
<details><summary>Show generated C (score=11)</summary>

```c
    __Pyx_GetModuleGlobalName(__pyx_t_2, __pyx_mstate_global->__pyx_n_u_ExprNodes); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 528, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_2);
    __pyx_t_1 = __Pyx_PyObject_GetAttrStr(__pyx_t_2, __pyx_mstate_global->__pyx_n_u_TupleNode); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 528, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_1);
    __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
    __pyx_t_3 = PyObject_IsInstance(__pyx_v_arg_tuple, __pyx_t_1); if (unlikely(__pyx_t_3 == ((int)-1))) __PYX_ERR(0, 528, __pyx_L1_error)
    __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
    __pyx_t_4 = (!__pyx_t_3);
    if (__pyx_t_4) {
/* … */
    }
```

</details>

L529  🟡  (score=2)
```python
                return node
```
<details><summary>Show generated C (score=2)</summary>

```c
      __Pyx_XDECREF(__pyx_r);
      __Pyx_INCREF(__pyx_v_node);
      __pyx_r = __pyx_v_node;
      goto __pyx_L0;
```

</details>

L530  🟡  (score=2)
```python
            args = arg_tuple.args
```
<details><summary>Show generated C (score=2)</summary>

```c
    __pyx_t_1 = __Pyx_PyObject_GetAttrStr(__pyx_v_arg_tuple, __pyx_mstate_global->__pyx_n_u_args); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 530, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_1);
    __pyx_v_args = __pyx_t_1;
    __pyx_t_1 = 0;
```

</details>

L531  ⚪  (score=0)
```python
        else:
```
L532  🟡  (score=2)
```python
            args = node.args
```
<details><summary>Show generated C (score=2)</summary>

```c
  /*else*/ {
    __pyx_t_1 = __Pyx_PyObject_GetAttrStr(__pyx_v_node, __pyx_mstate_global->__pyx_n_u_args); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 532, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_1);
    __pyx_v_args = __pyx_t_1;
    __pyx_t_1 = 0;
  }
  __pyx_L3:;
```

</details>

L533  🟡  (score=1)
```python
        return self._dispatch_to_handler(node, function, args, None)
```
<details><summary>Show generated C (score=1)</summary>

```c
  __Pyx_XDECREF(__pyx_r);
  __pyx_t_1 = ((struct __pyx_vtabstruct_6Cython_8Compiler_7Visitor_MethodDispatcherTransform *)__pyx_v_self->__pyx_base.__pyx_base.__pyx_base.__pyx_base.__pyx_vtab)->_dispatch_to_handler(__pyx_v_self, __pyx_v_node, __pyx_v_function, __pyx_v_args, Py_None); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 533, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __pyx_r = __pyx_t_1;
  __pyx_t_1 = 0;
  goto __pyx_L0;
```

</details>

L534  ⚪  (score=0)
```python
```
L535  🔴  (score=36)
```python
    def visit_PrimaryCmpNode(self, node):
```
<details><summary>Show generated C (score=36)</summary>

```c
/* Python wrapper */
static PyObject *__pyx_pw_6Cython_8Compiler_7Visitor_25MethodDispatcherTransform_5visit_PrimaryCmpNode(PyObject *__pyx_v_self, 
#if CYTHON_METH_FASTCALL
PyObject *const *__pyx_args, Py_ssize_t __pyx_nargs, PyObject *__pyx_kwds
#else
PyObject *__pyx_args, PyObject *__pyx_kwds
#endif
); /*proto*/
PyDoc_STRVAR(__pyx_doc_6Cython_8Compiler_7Visitor_25MethodDispatcherTransform_4visit_PrimaryCmpNode, "File: Cython/Compiler/Visitor.py (starting at line 535)");
static PyMethodDef __pyx_mdef_6Cython_8Compiler_7Visitor_25MethodDispatcherTransform_5visit_PrimaryCmpNode = {"visit_PrimaryCmpNode", (PyCFunction)(void(*)(void))(__Pyx_PyCFunction_FastCallWithKeywords)__pyx_pw_6Cython_8Compiler_7Visitor_25MethodDispatcherTransform_5visit_PrimaryCmpNode, __Pyx_METH_FASTCALL|METH_KEYWORDS, __pyx_doc_6Cython_8Compiler_7Visitor_25MethodDispatcherTransform_4visit_PrimaryCmpNode};
static PyObject *__pyx_pw_6Cython_8Compiler_7Visitor_25MethodDispatcherTransform_5visit_PrimaryCmpNode(PyObject *__pyx_v_self, 
#if CYTHON_METH_FASTCALL
PyObject *const *__pyx_args, Py_ssize_t __pyx_nargs, PyObject *__pyx_kwds
#else
PyObject *__pyx_args, PyObject *__pyx_kwds
#endif
) {
  PyObject *__pyx_v_node = 0;
  #if !CYTHON_METH_FASTCALL
  CYTHON_UNUSED Py_ssize_t __pyx_nargs;
  #endif
  CYTHON_UNUSED PyObject *const *__pyx_kwvalues;
  PyObject *__pyx_r = 0;
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("visit_PrimaryCmpNode (wrapper)", 0);
  #if !CYTHON_METH_FASTCALL
  #if CYTHON_ASSUME_SAFE_SIZE
  __pyx_nargs = PyTuple_GET_SIZE(__pyx_args);
  #else
  __pyx_nargs = PyTuple_Size(__pyx_args); if (unlikely(__pyx_nargs < 0)) return NULL;
  #endif
  #endif
  __pyx_kwvalues = __Pyx_KwValues_FASTCALL(__pyx_args, __pyx_nargs);
  {
    PyObject ** const __pyx_pyargnames[] = {&__pyx_mstate_global->__pyx_n_u_node,0};
  PyObject* values[1] = {0};
    const Py_ssize_t __pyx_kwds_len = (__pyx_kwds) ? __Pyx_NumKwargs_FASTCALL(__pyx_kwds) : 0;
    if (unlikely(__pyx_kwds_len) < 0) __PYX_ERR(0, 535, __pyx_L3_error)
    if (__pyx_kwds_len > 0) {
      switch (__pyx_nargs) {
        case  1:
        values[0] = __Pyx_ArgRef_FASTCALL(__pyx_args, 0);
        if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[0])) __PYX_ERR(0, 535, __pyx_L3_error)
        CYTHON_FALLTHROUGH;
        case  0: break;
        default: goto __pyx_L5_argtuple_error;
      }
      const Py_ssize_t kwd_pos_args = __pyx_nargs;
      if (__Pyx_ParseKeywords(__pyx_kwds, __pyx_kwvalues, __pyx_pyargnames, 0, values, kwd_pos_args, __pyx_kwds_len, "visit_PrimaryCmpNode", 0) < (0)) __PYX_ERR(0, 535, __pyx_L3_error)
      for (Py_ssize_t i = __pyx_nargs; i < 1; i++) {
        if (unlikely(!values[i])) { __Pyx_RaiseArgtupleInvalid("visit_PrimaryCmpNode", 1, 1, 1, i); __PYX_ERR(0, 535, __pyx_L3_error) }
      }
    } else if (unlikely(__pyx_nargs != 1)) {
      goto __pyx_L5_argtuple_error;
    } else {
      values[0] = __Pyx_ArgRef_FASTCALL(__pyx_args, 0);
      if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[0])) __PYX_ERR(0, 535, __pyx_L3_error)
    }
    __pyx_v_node = values[0];
  }
  goto __pyx_L6_skip;
  __pyx_L5_argtuple_error:;
  __Pyx_RaiseArgtupleInvalid("visit_PrimaryCmpNode", 1, 1, 1, __pyx_nargs); __PYX_ERR(0, 535, __pyx_L3_error)
  __pyx_L6_skip:;
  goto __pyx_L4_argument_unpacking_done;
  __pyx_L3_error:;
  for (Py_ssize_t __pyx_temp=0; __pyx_temp < (Py_ssize_t)(sizeof(values)/sizeof(values[0])); ++__pyx_temp) {
    Py_XDECREF(values[__pyx_temp]);
  }
  __Pyx_AddTraceback("Cython.Compiler.Visitor.MethodDispatcherTransform.visit_PrimaryCmpNode", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __Pyx_RefNannyFinishContext();
  return NULL;
  __pyx_L4_argument_unpacking_done:;
  __pyx_r = __pyx_pf_6Cython_8Compiler_7Visitor_25MethodDispatcherTransform_4visit_PrimaryCmpNode(((struct __pyx_obj_6Cython_8Compiler_7Visitor_MethodDispatcherTransform *)__pyx_v_self), __pyx_v_node);
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

static PyObject *__pyx_pf_6Cython_8Compiler_7Visitor_25MethodDispatcherTransform_4visit_PrimaryCmpNode(struct __pyx_obj_6Cython_8Compiler_7Visitor_MethodDispatcherTransform *__pyx_v_self, PyObject *__pyx_v_node) {
  PyObject *__pyx_r = NULL;
/* … */
  /* function exit code */
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_t_1);
  __Pyx_AddTraceback("Cython.Compiler.Visitor.MethodDispatcherTransform.visit_PrimaryCmpNode", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_r = NULL;
  __pyx_L0:;
  __Pyx_XGIVEREF(__pyx_r);
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}
/* … */
  __pyx_t_2 = __Pyx_CyFunction_New(&__pyx_mdef_6Cython_8Compiler_7Visitor_25MethodDispatcherTransform_5visit_PrimaryCmpNode, __Pyx_CYFUNCTION_CCLASS, __pyx_mstate_global->__pyx_n_u_MethodDispatcherTransform_visit_3, NULL, __pyx_mstate_global->__pyx_n_u_Cython_Compiler_Visitor, __pyx_mstate_global->__pyx_d, ((PyObject *)__pyx_mstate_global->__pyx_codeobj_tab[42])); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 535, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  #if CYTHON_COMPILING_IN_CPYTHON && PY_VERSION_HEX >= 0x030E0000
  PyUnstable_Object_EnableDeferredRefcount(__pyx_t_2);
  #endif
  if (__Pyx_SetItemOnTypeDict(__pyx_mstate_global->__pyx_ptype_6Cython_8Compiler_7Visitor_MethodDispatcherTransform, __pyx_mstate_global->__pyx_n_u_visit_PrimaryCmpNode, __pyx_t_2) < (0)) __PYX_ERR(0, 535, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
```

</details>

L536  🟠  (score=5)
```python
        if node.cascade:
```
<details><summary>Show generated C (score=5)</summary>

```c
  __pyx_t_1 = __Pyx_PyObject_GetAttrStr(__pyx_v_node, __pyx_mstate_global->__pyx_n_u_cascade); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 536, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __pyx_t_2 = __Pyx_PyObject_IsTrue(__pyx_t_1); if (unlikely((__pyx_t_2 < 0))) __PYX_ERR(0, 536, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  if (__pyx_t_2) {
/* … */
  }
```

</details>

L537  ⚪  (score=0)
```python
            # not currently handled below
```
L538  🟡  (score=1)
```python
            self._process_children(node)
```
<details><summary>Show generated C (score=1)</summary>

```c
    __pyx_t_1 = ((struct __pyx_vtabstruct_6Cython_8Compiler_7Visitor_MethodDispatcherTransform *)__pyx_v_self->__pyx_base.__pyx_base.__pyx_base.__pyx_base.__pyx_vtab)->__pyx_base.__pyx_base.__pyx_base._process_children(((struct __pyx_obj_6Cython_8Compiler_7Visitor_VisitorTransform *)__pyx_v_self), __pyx_v_node, NULL); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 538, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_1);
    __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
```

</details>

L539  🟡  (score=2)
```python
            return node
```
<details><summary>Show generated C (score=2)</summary>

```c
    __Pyx_XDECREF(__pyx_r);
    __Pyx_INCREF(__pyx_v_node);
    __pyx_r = __pyx_v_node;
    goto __pyx_L0;
```

</details>

L540  🟡  (score=1)
```python
        return self._visit_binop_node(node)
```
<details><summary>Show generated C (score=1)</summary>

```c
  __Pyx_XDECREF(__pyx_r);
  __pyx_t_1 = ((struct __pyx_vtabstruct_6Cython_8Compiler_7Visitor_MethodDispatcherTransform *)__pyx_v_self->__pyx_base.__pyx_base.__pyx_base.__pyx_base.__pyx_vtab)->_visit_binop_node(__pyx_v_self, __pyx_v_node); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 540, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __pyx_r = __pyx_t_1;
  __pyx_t_1 = 0;
  goto __pyx_L0;
```

</details>

L541  ⚪  (score=0)
```python
```
L542  🔴  (score=36)
```python
    def visit_BinopNode(self, node):
```
<details><summary>Show generated C (score=36)</summary>

```c
/* Python wrapper */
static PyObject *__pyx_pw_6Cython_8Compiler_7Visitor_25MethodDispatcherTransform_7visit_BinopNode(PyObject *__pyx_v_self, 
#if CYTHON_METH_FASTCALL
PyObject *const *__pyx_args, Py_ssize_t __pyx_nargs, PyObject *__pyx_kwds
#else
PyObject *__pyx_args, PyObject *__pyx_kwds
#endif
); /*proto*/
PyDoc_STRVAR(__pyx_doc_6Cython_8Compiler_7Visitor_25MethodDispatcherTransform_6visit_BinopNode, "File: Cython/Compiler/Visitor.py (starting at line 542)");
static PyMethodDef __pyx_mdef_6Cython_8Compiler_7Visitor_25MethodDispatcherTransform_7visit_BinopNode = {"visit_BinopNode", (PyCFunction)(void(*)(void))(__Pyx_PyCFunction_FastCallWithKeywords)__pyx_pw_6Cython_8Compiler_7Visitor_25MethodDispatcherTransform_7visit_BinopNode, __Pyx_METH_FASTCALL|METH_KEYWORDS, __pyx_doc_6Cython_8Compiler_7Visitor_25MethodDispatcherTransform_6visit_BinopNode};
static PyObject *__pyx_pw_6Cython_8Compiler_7Visitor_25MethodDispatcherTransform_7visit_BinopNode(PyObject *__pyx_v_self, 
#if CYTHON_METH_FASTCALL
PyObject *const *__pyx_args, Py_ssize_t __pyx_nargs, PyObject *__pyx_kwds
#else
PyObject *__pyx_args, PyObject *__pyx_kwds
#endif
) {
  PyObject *__pyx_v_node = 0;
  #if !CYTHON_METH_FASTCALL
  CYTHON_UNUSED Py_ssize_t __pyx_nargs;
  #endif
  CYTHON_UNUSED PyObject *const *__pyx_kwvalues;
  PyObject *__pyx_r = 0;
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("visit_BinopNode (wrapper)", 0);
  #if !CYTHON_METH_FASTCALL
  #if CYTHON_ASSUME_SAFE_SIZE
  __pyx_nargs = PyTuple_GET_SIZE(__pyx_args);
  #else
  __pyx_nargs = PyTuple_Size(__pyx_args); if (unlikely(__pyx_nargs < 0)) return NULL;
  #endif
  #endif
  __pyx_kwvalues = __Pyx_KwValues_FASTCALL(__pyx_args, __pyx_nargs);
  {
    PyObject ** const __pyx_pyargnames[] = {&__pyx_mstate_global->__pyx_n_u_node,0};
  PyObject* values[1] = {0};
    const Py_ssize_t __pyx_kwds_len = (__pyx_kwds) ? __Pyx_NumKwargs_FASTCALL(__pyx_kwds) : 0;
    if (unlikely(__pyx_kwds_len) < 0) __PYX_ERR(0, 542, __pyx_L3_error)
    if (__pyx_kwds_len > 0) {
      switch (__pyx_nargs) {
        case  1:
        values[0] = __Pyx_ArgRef_FASTCALL(__pyx_args, 0);
        if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[0])) __PYX_ERR(0, 542, __pyx_L3_error)
        CYTHON_FALLTHROUGH;
        case  0: break;
        default: goto __pyx_L5_argtuple_error;
      }
      const Py_ssize_t kwd_pos_args = __pyx_nargs;
      if (__Pyx_ParseKeywords(__pyx_kwds, __pyx_kwvalues, __pyx_pyargnames, 0, values, kwd_pos_args, __pyx_kwds_len, "visit_BinopNode", 0) < (0)) __PYX_ERR(0, 542, __pyx_L3_error)
      for (Py_ssize_t i = __pyx_nargs; i < 1; i++) {
        if (unlikely(!values[i])) { __Pyx_RaiseArgtupleInvalid("visit_BinopNode", 1, 1, 1, i); __PYX_ERR(0, 542, __pyx_L3_error) }
      }
    } else if (unlikely(__pyx_nargs != 1)) {
      goto __pyx_L5_argtuple_error;
    } else {
      values[0] = __Pyx_ArgRef_FASTCALL(__pyx_args, 0);
      if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[0])) __PYX_ERR(0, 542, __pyx_L3_error)
    }
    __pyx_v_node = values[0];
  }
  goto __pyx_L6_skip;
  __pyx_L5_argtuple_error:;
  __Pyx_RaiseArgtupleInvalid("visit_BinopNode", 1, 1, 1, __pyx_nargs); __PYX_ERR(0, 542, __pyx_L3_error)
  __pyx_L6_skip:;
  goto __pyx_L4_argument_unpacking_done;
  __pyx_L3_error:;
  for (Py_ssize_t __pyx_temp=0; __pyx_temp < (Py_ssize_t)(sizeof(values)/sizeof(values[0])); ++__pyx_temp) {
    Py_XDECREF(values[__pyx_temp]);
  }
  __Pyx_AddTraceback("Cython.Compiler.Visitor.MethodDispatcherTransform.visit_BinopNode", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __Pyx_RefNannyFinishContext();
  return NULL;
  __pyx_L4_argument_unpacking_done:;
  __pyx_r = __pyx_pf_6Cython_8Compiler_7Visitor_25MethodDispatcherTransform_6visit_BinopNode(((struct __pyx_obj_6Cython_8Compiler_7Visitor_MethodDispatcherTransform *)__pyx_v_self), __pyx_v_node);
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

static PyObject *__pyx_pf_6Cython_8Compiler_7Visitor_25MethodDispatcherTransform_6visit_BinopNode(struct __pyx_obj_6Cython_8Compiler_7Visitor_MethodDispatcherTransform *__pyx_v_self, PyObject *__pyx_v_node) {
  PyObject *__pyx_r = NULL;
/* … */
  /* function exit code */
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_t_1);
  __Pyx_AddTraceback("Cython.Compiler.Visitor.MethodDispatcherTransform.visit_BinopNode", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_r = NULL;
  __pyx_L0:;
  __Pyx_XGIVEREF(__pyx_r);
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}
/* … */
  __pyx_t_2 = __Pyx_CyFunction_New(&__pyx_mdef_6Cython_8Compiler_7Visitor_25MethodDispatcherTransform_7visit_BinopNode, __Pyx_CYFUNCTION_CCLASS, __pyx_mstate_global->__pyx_n_u_MethodDispatcherTransform_visit_4, NULL, __pyx_mstate_global->__pyx_n_u_Cython_Compiler_Visitor, __pyx_mstate_global->__pyx_d, ((PyObject *)__pyx_mstate_global->__pyx_codeobj_tab[43])); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 542, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  #if CYTHON_COMPILING_IN_CPYTHON && PY_VERSION_HEX >= 0x030E0000
  PyUnstable_Object_EnableDeferredRefcount(__pyx_t_2);
  #endif
  if (__Pyx_SetItemOnTypeDict(__pyx_mstate_global->__pyx_ptype_6Cython_8Compiler_7Visitor_MethodDispatcherTransform, __pyx_mstate_global->__pyx_n_u_visit_BinopNode, __pyx_t_2) < (0)) __PYX_ERR(0, 542, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
```

</details>

L543  🟡  (score=1)
```python
        return self._visit_binop_node(node)
```
<details><summary>Show generated C (score=1)</summary>

```c
  __Pyx_XDECREF(__pyx_r);
  __pyx_t_1 = ((struct __pyx_vtabstruct_6Cython_8Compiler_7Visitor_MethodDispatcherTransform *)__pyx_v_self->__pyx_base.__pyx_base.__pyx_base.__pyx_base.__pyx_vtab)->_visit_binop_node(__pyx_v_self, __pyx_v_node); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 543, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __pyx_r = __pyx_t_1;
  __pyx_t_1 = 0;
  goto __pyx_L0;
```

</details>

L544  ⚪  (score=0)
```python
```
L545  🔴  (score=13)
```python
    def _visit_binop_node(self, node):
```
<details><summary>Show generated C (score=13)</summary>

```c
static PyObject *__pyx_f_6Cython_8Compiler_7Visitor_25MethodDispatcherTransform__visit_binop_node(struct __pyx_obj_6Cython_8Compiler_7Visitor_MethodDispatcherTransform *__pyx_v_self, PyObject *__pyx_v_node) {
  PyObject *__pyx_v_special_method_name = NULL;
  PyObject *__pyx_v_operand1 = NULL;
  PyObject *__pyx_v_operand2 = NULL;
  PyObject *__pyx_v_obj_type = NULL;
  PyObject *__pyx_v_type_name = NULL;
  PyObject *__pyx_r = NULL;
  __Pyx_INCREF(__pyx_v_node);
/* … */
  /* function exit code */
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_t_1);
  __Pyx_XDECREF(__pyx_t_2);
  __Pyx_XDECREF(__pyx_t_3);
  __Pyx_XDECREF(__pyx_t_4);
  __Pyx_AddTraceback("Cython.Compiler.Visitor.MethodDispatcherTransform._visit_binop_node", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_r = 0;
  __pyx_L0:;
  __Pyx_XDECREF(__pyx_v_special_method_name);
  __Pyx_XDECREF(__pyx_v_operand1);
  __Pyx_XDECREF(__pyx_v_operand2);
  __Pyx_XDECREF(__pyx_v_obj_type);
  __Pyx_XDECREF(__pyx_v_type_name);
  __Pyx_XDECREF(__pyx_v_node);
  __Pyx_XGIVEREF(__pyx_r);
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}
```

</details>

L546  🟡  (score=1)
```python
        self._process_children(node)
```
<details><summary>Show generated C (score=1)</summary>

```c
  __pyx_t_1 = ((struct __pyx_vtabstruct_6Cython_8Compiler_7Visitor_MethodDispatcherTransform *)__pyx_v_self->__pyx_base.__pyx_base.__pyx_base.__pyx_base.__pyx_vtab)->__pyx_base.__pyx_base.__pyx_base._process_children(((struct __pyx_obj_6Cython_8Compiler_7Visitor_VisitorTransform *)__pyx_v_self), __pyx_v_node, NULL); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 546, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
```

</details>

L547  ⚪  (score=0)
```python
        # FIXME: could special case 'not_in'
```
L548  🔴  (score=19)
```python
        special_method_name = find_special_method_for_binary_operator(node.operator)
```
<details><summary>Show generated C (score=19)</summary>

```c
  __pyx_t_2 = NULL;
  __Pyx_GetModuleGlobalName(__pyx_t_3, __pyx_mstate_global->__pyx_n_u_find_special_method_for_binary_o); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 548, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_3);
  __pyx_t_4 = __Pyx_PyObject_GetAttrStr(__pyx_v_node, __pyx_mstate_global->__pyx_n_u_operator); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 548, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_4);
  __pyx_t_5 = 1;
  #if CYTHON_UNPACK_METHODS
  if (unlikely(PyMethod_Check(__pyx_t_3))) {
    __pyx_t_2 = PyMethod_GET_SELF(__pyx_t_3);
    assert(__pyx_t_2);
    PyObject* __pyx__function = PyMethod_GET_FUNCTION(__pyx_t_3);
    __Pyx_INCREF(__pyx_t_2);
    __Pyx_INCREF(__pyx__function);
    __Pyx_DECREF_SET(__pyx_t_3, __pyx__function);
    __pyx_t_5 = 0;
  }
  #endif
  {
    PyObject *__pyx_callargs[2] = {__pyx_t_2, __pyx_t_4};
    __pyx_t_1 = __Pyx_PyObject_FastCall((PyObject*)__pyx_t_3, __pyx_callargs+__pyx_t_5, (2-__pyx_t_5) | (__pyx_t_5*__Pyx_PY_VECTORCALL_ARGUMENTS_OFFSET));
    __Pyx_XDECREF(__pyx_t_2); __pyx_t_2 = 0;
    __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
    __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
    if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 548, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_1);
  }
  __pyx_v_special_method_name = __pyx_t_1;
  __pyx_t_1 = 0;
```

</details>

L549  🟡  (score=2)
```python
        if special_method_name:
```
<details><summary>Show generated C (score=2)</summary>

```c
  __pyx_t_6 = __Pyx_PyObject_IsTrue(__pyx_v_special_method_name); if (unlikely((__pyx_t_6 < 0))) __PYX_ERR(0, 549, __pyx_L1_error)
  if (__pyx_t_6) {
/* … */
  }
```

</details>

L550  🟡  (score=4)
```python
            operand1, operand2 = node.operand1, node.operand2
```
<details><summary>Show generated C (score=4)</summary>

```c
    __pyx_t_1 = __Pyx_PyObject_GetAttrStr(__pyx_v_node, __pyx_mstate_global->__pyx_n_u_operand1); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 550, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_1);
    __pyx_t_3 = __Pyx_PyObject_GetAttrStr(__pyx_v_node, __pyx_mstate_global->__pyx_n_u_operand2); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 550, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_3);
    __pyx_v_operand1 = __pyx_t_1;
    __pyx_t_1 = 0;
    __pyx_v_operand2 = __pyx_t_3;
    __pyx_t_3 = 0;
```

</details>

L551  🟡  (score=2)
```python
            if special_method_name == '__contains__':
```
<details><summary>Show generated C (score=2)</summary>

```c
    __pyx_t_6 = (__Pyx_PyUnicode_Equals(__pyx_v_special_method_name, __pyx_mstate_global->__pyx_n_u_contains, Py_EQ)); if (unlikely((__pyx_t_6 < 0))) __PYX_ERR(0, 551, __pyx_L1_error)
    if (__pyx_t_6) {
/* … */
      goto __pyx_L4;
    }
```

</details>

L552  ⚪  (score=0)
```python
                operand1, operand2 = operand2, operand1
```
<details><summary>Show generated C (score=0)</summary>

```c
      __pyx_t_7 = __pyx_v_operand2;
      __pyx_t_8 = __pyx_v_operand1;
      __pyx_v_operand1 = __pyx_t_7;
      __pyx_t_7 = 0;
      __pyx_v_operand2 = __pyx_t_8;
      __pyx_t_8 = 0;
```

</details>

L553  🟡  (score=2)
```python
            elif special_method_name == '__div__':
```
<details><summary>Show generated C (score=2)</summary>

```c
    __pyx_t_6 = (__Pyx_PyUnicode_Equals(__pyx_v_special_method_name, __pyx_mstate_global->__pyx_n_u_div, Py_EQ)); if (unlikely((__pyx_t_6 < 0))) __PYX_ERR(0, 553, __pyx_L1_error)
    if (__pyx_t_6) {
/* … */
    }
    __pyx_L4:;
```

</details>

L554  🔴  (score=19)
```python
                if Future.division in self.current_env().context.future_directives:
```
<details><summary>Show generated C (score=19)</summary>

```c
      __Pyx_GetModuleGlobalName(__pyx_t_3, __pyx_mstate_global->__pyx_n_u_Future); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 554, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_3);
      __pyx_t_1 = __Pyx_PyObject_GetAttrStr(__pyx_t_3, __pyx_mstate_global->__pyx_n_u_division); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 554, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_1);
      __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
      __pyx_t_4 = ((PyObject *)__pyx_v_self);
      __Pyx_INCREF(__pyx_t_4);
      __pyx_t_5 = 0;
      {
        PyObject *__pyx_callargs[2] = {__pyx_t_4, NULL};
        __pyx_t_3 = __Pyx_PyObject_FastCallMethod((PyObject*)__pyx_mstate_global->__pyx_n_u_current_env, __pyx_callargs+__pyx_t_5, (1-__pyx_t_5) | (1*__Pyx_PY_VECTORCALL_ARGUMENTS_OFFSET));
        __Pyx_XDECREF(__pyx_t_4); __pyx_t_4 = 0;
        if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 554, __pyx_L1_error)
        __Pyx_GOTREF(__pyx_t_3);
      }
      __pyx_t_4 = __Pyx_PyObject_GetAttrStr(__pyx_t_3, __pyx_mstate_global->__pyx_n_u_context); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 554, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_4);
      __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
      __pyx_t_3 = __Pyx_PyObject_GetAttrStr(__pyx_t_4, __pyx_mstate_global->__pyx_n_u_future_directives); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 554, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_3);
      __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
      __pyx_t_6 = (__Pyx_PySequence_ContainsTF(__pyx_t_1, __pyx_t_3, Py_EQ)); if (unlikely((__pyx_t_6 < 0))) __PYX_ERR(0, 554, __pyx_L1_error)
      __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
      __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
      if (__pyx_t_6) {
/* … */
      }
```

</details>

L555  🟡  (score=2)
```python
                    special_method_name = '__truediv__'
```
<details><summary>Show generated C (score=2)</summary>

```c
        __Pyx_INCREF(__pyx_mstate_global->__pyx_n_u_truediv);
        __Pyx_DECREF_SET(__pyx_v_special_method_name, __pyx_mstate_global->__pyx_n_u_truediv);
```

</details>

L556  🟡  (score=2)
```python
            obj_type = operand1.type
```
<details><summary>Show generated C (score=2)</summary>

```c
    __pyx_t_3 = __Pyx_PyObject_GetAttrStr(__pyx_v_operand1, __pyx_mstate_global->__pyx_n_u_type); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 556, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_3);
    __pyx_v_obj_type = __pyx_t_3;
    __pyx_t_3 = 0;
```

</details>

L557  🟠  (score=5)
```python
            if obj_type.is_builtin_type:
```
<details><summary>Show generated C (score=5)</summary>

```c
    __pyx_t_3 = __Pyx_PyObject_GetAttrStr(__pyx_v_obj_type, __pyx_mstate_global->__pyx_n_u_is_builtin_type); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 557, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_3);
    __pyx_t_6 = __Pyx_PyObject_IsTrue(__pyx_t_3); if (unlikely((__pyx_t_6 < 0))) __PYX_ERR(0, 557, __pyx_L1_error)
    __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
    if (__pyx_t_6) {
/* … */
      goto __pyx_L6;
    }
```

</details>

L558  🟡  (score=2)
```python
                type_name = obj_type.name
```
<details><summary>Show generated C (score=2)</summary>

```c
      __pyx_t_3 = __Pyx_PyObject_GetAttrStr(__pyx_v_obj_type, __pyx_mstate_global->__pyx_n_u_name_2); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 558, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_3);
      __pyx_v_type_name = __pyx_t_3;
      __pyx_t_3 = 0;
```

</details>

L559  ⚪  (score=0)
```python
            else:
```
L560  🟡  (score=1)
```python
                type_name = "object"  # safety measure
```
<details><summary>Show generated C (score=1)</summary>

```c
    /*else*/ {
      __Pyx_INCREF(__pyx_mstate_global->__pyx_n_u_object);
      __pyx_v_type_name = __pyx_mstate_global->__pyx_n_u_object;
    }
    __pyx_L6:;
```

</details>

L561  🟡  (score=2)
```python
            node = self._dispatch_to_method_handler(
```
<details><summary>Show generated C (score=2)</summary>

```c
    __pyx_t_1 = ((struct __pyx_vtabstruct_6Cython_8Compiler_7Visitor_MethodDispatcherTransform *)__pyx_v_self->__pyx_base.__pyx_base.__pyx_base.__pyx_base.__pyx_vtab)->_dispatch_to_method_handler(__pyx_v_self, __pyx_v_special_method_name, Py_None, Py_False, __pyx_v_type_name, __pyx_v_node, Py_None, __pyx_t_3, Py_None); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 561, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_1);
    __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
    __Pyx_DECREF_SET(__pyx_v_node, __pyx_t_1);
    __pyx_t_1 = 0;
```

</details>

L562  ⚪  (score=0)
```python
                special_method_name, None, False, type_name,
```
L563  🔴  (score=11)
```python
                node, None, [operand1, operand2], None)
```
<details><summary>Show generated C (score=11)</summary>

```c
    __pyx_t_3 = PyList_New(2); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 563, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_3);
    __Pyx_INCREF(__pyx_v_operand1);
    __Pyx_GIVEREF(__pyx_v_operand1);
    if (__Pyx_PyList_SET_ITEM(__pyx_t_3, 0, __pyx_v_operand1) != (0)) __PYX_ERR(0, 563, __pyx_L1_error);
    __Pyx_INCREF(__pyx_v_operand2);
    __Pyx_GIVEREF(__pyx_v_operand2);
    if (__Pyx_PyList_SET_ITEM(__pyx_t_3, 1, __pyx_v_operand2) != (0)) __PYX_ERR(0, 563, __pyx_L1_error);
```

</details>

L564  🟡  (score=2)
```python
        return node
```
<details><summary>Show generated C (score=2)</summary>

```c
  __Pyx_XDECREF(__pyx_r);
  __Pyx_INCREF(__pyx_v_node);
  __pyx_r = __pyx_v_node;
  goto __pyx_L0;
```

</details>

L565  ⚪  (score=0)
```python
```
L566  🔴  (score=45)
```python
    def visit_UnopNode(self, node):
```
<details><summary>Show generated C (score=45)</summary>

```c
/* Python wrapper */
static PyObject *__pyx_pw_6Cython_8Compiler_7Visitor_25MethodDispatcherTransform_9visit_UnopNode(PyObject *__pyx_v_self, 
#if CYTHON_METH_FASTCALL
PyObject *const *__pyx_args, Py_ssize_t __pyx_nargs, PyObject *__pyx_kwds
#else
PyObject *__pyx_args, PyObject *__pyx_kwds
#endif
); /*proto*/
PyDoc_STRVAR(__pyx_doc_6Cython_8Compiler_7Visitor_25MethodDispatcherTransform_8visit_UnopNode, "File: Cython/Compiler/Visitor.py (starting at line 566)");
static PyMethodDef __pyx_mdef_6Cython_8Compiler_7Visitor_25MethodDispatcherTransform_9visit_UnopNode = {"visit_UnopNode", (PyCFunction)(void(*)(void))(__Pyx_PyCFunction_FastCallWithKeywords)__pyx_pw_6Cython_8Compiler_7Visitor_25MethodDispatcherTransform_9visit_UnopNode, __Pyx_METH_FASTCALL|METH_KEYWORDS, __pyx_doc_6Cython_8Compiler_7Visitor_25MethodDispatcherTransform_8visit_UnopNode};
static PyObject *__pyx_pw_6Cython_8Compiler_7Visitor_25MethodDispatcherTransform_9visit_UnopNode(PyObject *__pyx_v_self, 
#if CYTHON_METH_FASTCALL
PyObject *const *__pyx_args, Py_ssize_t __pyx_nargs, PyObject *__pyx_kwds
#else
PyObject *__pyx_args, PyObject *__pyx_kwds
#endif
) {
  PyObject *__pyx_v_node = 0;
  #if !CYTHON_METH_FASTCALL
  CYTHON_UNUSED Py_ssize_t __pyx_nargs;
  #endif
  CYTHON_UNUSED PyObject *const *__pyx_kwvalues;
  PyObject *__pyx_r = 0;
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("visit_UnopNode (wrapper)", 0);
  #if !CYTHON_METH_FASTCALL
  #if CYTHON_ASSUME_SAFE_SIZE
  __pyx_nargs = PyTuple_GET_SIZE(__pyx_args);
  #else
  __pyx_nargs = PyTuple_Size(__pyx_args); if (unlikely(__pyx_nargs < 0)) return NULL;
  #endif
  #endif
  __pyx_kwvalues = __Pyx_KwValues_FASTCALL(__pyx_args, __pyx_nargs);
  {
    PyObject ** const __pyx_pyargnames[] = {&__pyx_mstate_global->__pyx_n_u_node,0};
  PyObject* values[1] = {0};
    const Py_ssize_t __pyx_kwds_len = (__pyx_kwds) ? __Pyx_NumKwargs_FASTCALL(__pyx_kwds) : 0;
    if (unlikely(__pyx_kwds_len) < 0) __PYX_ERR(0, 566, __pyx_L3_error)
    if (__pyx_kwds_len > 0) {
      switch (__pyx_nargs) {
        case  1:
        values[0] = __Pyx_ArgRef_FASTCALL(__pyx_args, 0);
        if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[0])) __PYX_ERR(0, 566, __pyx_L3_error)
        CYTHON_FALLTHROUGH;
        case  0: break;
        default: goto __pyx_L5_argtuple_error;
      }
      const Py_ssize_t kwd_pos_args = __pyx_nargs;
      if (__Pyx_ParseKeywords(__pyx_kwds, __pyx_kwvalues, __pyx_pyargnames, 0, values, kwd_pos_args, __pyx_kwds_len, "visit_UnopNode", 0) < (0)) __PYX_ERR(0, 566, __pyx_L3_error)
      for (Py_ssize_t i = __pyx_nargs; i < 1; i++) {
        if (unlikely(!values[i])) { __Pyx_RaiseArgtupleInvalid("visit_UnopNode", 1, 1, 1, i); __PYX_ERR(0, 566, __pyx_L3_error) }
      }
    } else if (unlikely(__pyx_nargs != 1)) {
      goto __pyx_L5_argtuple_error;
    } else {
      values[0] = __Pyx_ArgRef_FASTCALL(__pyx_args, 0);
      if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[0])) __PYX_ERR(0, 566, __pyx_L3_error)
    }
    __pyx_v_node = values[0];
  }
  goto __pyx_L6_skip;
  __pyx_L5_argtuple_error:;
  __Pyx_RaiseArgtupleInvalid("visit_UnopNode", 1, 1, 1, __pyx_nargs); __PYX_ERR(0, 566, __pyx_L3_error)
  __pyx_L6_skip:;
  goto __pyx_L4_argument_unpacking_done;
  __pyx_L3_error:;
  for (Py_ssize_t __pyx_temp=0; __pyx_temp < (Py_ssize_t)(sizeof(values)/sizeof(values[0])); ++__pyx_temp) {
    Py_XDECREF(values[__pyx_temp]);
  }
  __Pyx_AddTraceback("Cython.Compiler.Visitor.MethodDispatcherTransform.visit_UnopNode", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __Pyx_RefNannyFinishContext();
  return NULL;
  __pyx_L4_argument_unpacking_done:;
  __pyx_r = __pyx_pf_6Cython_8Compiler_7Visitor_25MethodDispatcherTransform_8visit_UnopNode(((struct __pyx_obj_6Cython_8Compiler_7Visitor_MethodDispatcherTransform *)__pyx_v_self), __pyx_v_node);
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

static PyObject *__pyx_pf_6Cython_8Compiler_7Visitor_25MethodDispatcherTransform_8visit_UnopNode(struct __pyx_obj_6Cython_8Compiler_7Visitor_MethodDispatcherTransform *__pyx_v_self, PyObject *__pyx_v_node) {
  PyObject *__pyx_v_special_method_name = NULL;
  PyObject *__pyx_v_operand = NULL;
  PyObject *__pyx_v_obj_type = NULL;
  PyObject *__pyx_v_type_name = NULL;
  PyObject *__pyx_r = NULL;
  __Pyx_INCREF(__pyx_v_node);
/* … */
  /* function exit code */
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_t_1);
  __Pyx_XDECREF(__pyx_t_2);
  __Pyx_XDECREF(__pyx_t_3);
  __Pyx_XDECREF(__pyx_t_4);
  __Pyx_AddTraceback("Cython.Compiler.Visitor.MethodDispatcherTransform.visit_UnopNode", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_r = NULL;
  __pyx_L0:;
  __Pyx_XDECREF(__pyx_v_special_method_name);
  __Pyx_XDECREF(__pyx_v_operand);
  __Pyx_XDECREF(__pyx_v_obj_type);
  __Pyx_XDECREF(__pyx_v_type_name);
  __Pyx_XDECREF(__pyx_v_node);
  __Pyx_XGIVEREF(__pyx_r);
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}
/* … */
  __pyx_t_2 = __Pyx_CyFunction_New(&__pyx_mdef_6Cython_8Compiler_7Visitor_25MethodDispatcherTransform_9visit_UnopNode, __Pyx_CYFUNCTION_CCLASS, __pyx_mstate_global->__pyx_n_u_MethodDispatcherTransform_visit_5, NULL, __pyx_mstate_global->__pyx_n_u_Cython_Compiler_Visitor, __pyx_mstate_global->__pyx_d, ((PyObject *)__pyx_mstate_global->__pyx_codeobj_tab[44])); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 566, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  #if CYTHON_COMPILING_IN_CPYTHON && PY_VERSION_HEX >= 0x030E0000
  PyUnstable_Object_EnableDeferredRefcount(__pyx_t_2);
  #endif
  if (__Pyx_SetItemOnTypeDict(__pyx_mstate_global->__pyx_ptype_6Cython_8Compiler_7Visitor_MethodDispatcherTransform, __pyx_mstate_global->__pyx_n_u_visit_UnopNode, __pyx_t_2) < (0)) __PYX_ERR(0, 566, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
```

</details>

L567  🟡  (score=1)
```python
        self._process_children(node)
```
<details><summary>Show generated C (score=1)</summary>

```c
  __pyx_t_1 = ((struct __pyx_vtabstruct_6Cython_8Compiler_7Visitor_MethodDispatcherTransform *)__pyx_v_self->__pyx_base.__pyx_base.__pyx_base.__pyx_base.__pyx_vtab)->__pyx_base.__pyx_base.__pyx_base._process_children(((struct __pyx_obj_6Cython_8Compiler_7Visitor_VisitorTransform *)__pyx_v_self), __pyx_v_node, NULL); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 567, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
```

</details>

L568  🔴  (score=19)
```python
        special_method_name = find_special_method_for_unary_operator(node.operator)
```
<details><summary>Show generated C (score=19)</summary>

```c
  __pyx_t_2 = NULL;
  __Pyx_GetModuleGlobalName(__pyx_t_3, __pyx_mstate_global->__pyx_n_u_find_special_method_for_unary_op); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 568, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_3);
  __pyx_t_4 = __Pyx_PyObject_GetAttrStr(__pyx_v_node, __pyx_mstate_global->__pyx_n_u_operator); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 568, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_4);
  __pyx_t_5 = 1;
  #if CYTHON_UNPACK_METHODS
  if (unlikely(PyMethod_Check(__pyx_t_3))) {
    __pyx_t_2 = PyMethod_GET_SELF(__pyx_t_3);
    assert(__pyx_t_2);
    PyObject* __pyx__function = PyMethod_GET_FUNCTION(__pyx_t_3);
    __Pyx_INCREF(__pyx_t_2);
    __Pyx_INCREF(__pyx__function);
    __Pyx_DECREF_SET(__pyx_t_3, __pyx__function);
    __pyx_t_5 = 0;
  }
  #endif
  {
    PyObject *__pyx_callargs[2] = {__pyx_t_2, __pyx_t_4};
    __pyx_t_1 = __Pyx_PyObject_FastCall((PyObject*)__pyx_t_3, __pyx_callargs+__pyx_t_5, (2-__pyx_t_5) | (__pyx_t_5*__Pyx_PY_VECTORCALL_ARGUMENTS_OFFSET));
    __Pyx_XDECREF(__pyx_t_2); __pyx_t_2 = 0;
    __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
    __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
    if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 568, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_1);
  }
  __pyx_v_special_method_name = __pyx_t_1;
  __pyx_t_1 = 0;
```

</details>

L569  🟡  (score=2)
```python
        if special_method_name:
```
<details><summary>Show generated C (score=2)</summary>

```c
  __pyx_t_6 = __Pyx_PyObject_IsTrue(__pyx_v_special_method_name); if (unlikely((__pyx_t_6 < 0))) __PYX_ERR(0, 569, __pyx_L1_error)
  if (__pyx_t_6) {
/* … */
  }
```

</details>

L570  🟡  (score=2)
```python
            operand = node.operand
```
<details><summary>Show generated C (score=2)</summary>

```c
    __pyx_t_1 = __Pyx_PyObject_GetAttrStr(__pyx_v_node, __pyx_mstate_global->__pyx_n_u_operand); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 570, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_1);
    __pyx_v_operand = __pyx_t_1;
    __pyx_t_1 = 0;
```

</details>

L571  🟡  (score=2)
```python
            obj_type = operand.type
```
<details><summary>Show generated C (score=2)</summary>

```c
    __pyx_t_1 = __Pyx_PyObject_GetAttrStr(__pyx_v_operand, __pyx_mstate_global->__pyx_n_u_type); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 571, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_1);
    __pyx_v_obj_type = __pyx_t_1;
    __pyx_t_1 = 0;
```

</details>

L572  🟠  (score=5)
```python
            if obj_type.is_builtin_type:
```
<details><summary>Show generated C (score=5)</summary>

```c
    __pyx_t_1 = __Pyx_PyObject_GetAttrStr(__pyx_v_obj_type, __pyx_mstate_global->__pyx_n_u_is_builtin_type); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 572, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_1);
    __pyx_t_6 = __Pyx_PyObject_IsTrue(__pyx_t_1); if (unlikely((__pyx_t_6 < 0))) __PYX_ERR(0, 572, __pyx_L1_error)
    __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
    if (__pyx_t_6) {
/* … */
      goto __pyx_L4;
    }
```

</details>

L573  🟡  (score=2)
```python
                type_name = obj_type.name
```
<details><summary>Show generated C (score=2)</summary>

```c
      __pyx_t_1 = __Pyx_PyObject_GetAttrStr(__pyx_v_obj_type, __pyx_mstate_global->__pyx_n_u_name_2); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 573, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_1);
      __pyx_v_type_name = __pyx_t_1;
      __pyx_t_1 = 0;
```

</details>

L574  ⚪  (score=0)
```python
            else:
```
L575  🟡  (score=1)
```python
                type_name = "object"  # safety measure
```
<details><summary>Show generated C (score=1)</summary>

```c
    /*else*/ {
      __Pyx_INCREF(__pyx_mstate_global->__pyx_n_u_object);
      __pyx_v_type_name = __pyx_mstate_global->__pyx_n_u_object;
    }
    __pyx_L4:;
```

</details>

L576  🟡  (score=2)
```python
            node = self._dispatch_to_method_handler(
```
<details><summary>Show generated C (score=2)</summary>

```c
    __pyx_t_3 = ((struct __pyx_vtabstruct_6Cython_8Compiler_7Visitor_MethodDispatcherTransform *)__pyx_v_self->__pyx_base.__pyx_base.__pyx_base.__pyx_base.__pyx_vtab)->_dispatch_to_method_handler(__pyx_v_self, __pyx_v_special_method_name, Py_None, Py_False, __pyx_v_type_name, __pyx_v_node, Py_None, __pyx_t_1, Py_None); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 576, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_3);
    __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
    __Pyx_DECREF_SET(__pyx_v_node, __pyx_t_3);
    __pyx_t_3 = 0;
```

</details>

L577  ⚪  (score=0)
```python
                special_method_name, None, False, type_name,
```
L578  🟠  (score=8)
```python
                node, None, [operand], None)
```
<details><summary>Show generated C (score=8)</summary>

```c
    __pyx_t_1 = PyList_New(1); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 578, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_1);
    __Pyx_INCREF(__pyx_v_operand);
    __Pyx_GIVEREF(__pyx_v_operand);
    if (__Pyx_PyList_SET_ITEM(__pyx_t_1, 0, __pyx_v_operand) != (0)) __PYX_ERR(0, 578, __pyx_L1_error);
```

</details>

L579  🟡  (score=2)
```python
        return node
```
<details><summary>Show generated C (score=2)</summary>

```c
  __Pyx_XDECREF(__pyx_r);
  __Pyx_INCREF(__pyx_v_node);
  __pyx_r = __pyx_v_node;
  goto __pyx_L0;
```

</details>

L580  ⚪  (score=0)
```python
```
L581  ⚪  (score=0)
```python
    ### dispatch to specific handlers
```
L582  ⚪  (score=0)
```python
```
L583  🟠  (score=7)
```python
    def _find_handler(self, match_name, has_kwargs):
```
<details><summary>Show generated C (score=7)</summary>

```c
static PyObject *__pyx_f_6Cython_8Compiler_7Visitor_25MethodDispatcherTransform__find_handler(struct __pyx_obj_6Cython_8Compiler_7Visitor_MethodDispatcherTransform *__pyx_v_self, PyObject *__pyx_v_match_name, int __pyx_v_has_kwargs) {
  PyObject *__pyx_v_call_type = NULL;
  PyObject *__pyx_v_handler = NULL;
  PyObject *__pyx_r = NULL;
/* … */
  /* function exit code */
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_t_1);
  __Pyx_XDECREF(__pyx_t_2);
  __Pyx_XDECREF(__pyx_t_7);
  __Pyx_AddTraceback("Cython.Compiler.Visitor.MethodDispatcherTransform._find_handler", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_r = 0;
  __pyx_L0:;
  __Pyx_XDECREF(__pyx_v_call_type);
  __Pyx_XDECREF(__pyx_v_handler);
  __Pyx_XGIVEREF(__pyx_r);
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}
```

</details>

L584  🟠  (score=7)
```python
        if not match_name.isascii():
```
<details><summary>Show generated C (score=7)</summary>

```c
  __pyx_t_2 = __pyx_v_match_name;
  __Pyx_INCREF(__pyx_t_2);
  __pyx_t_3 = 0;
  {
    PyObject *__pyx_callargs[2] = {__pyx_t_2, NULL};
    __pyx_t_1 = __Pyx_PyObject_FastCallMethod((PyObject*)__pyx_mstate_global->__pyx_n_u_isascii, __pyx_callargs+__pyx_t_3, (1-__pyx_t_3) | (1*__Pyx_PY_VECTORCALL_ARGUMENTS_OFFSET));
    __Pyx_XDECREF(__pyx_t_2); __pyx_t_2 = 0;
    if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 584, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_1);
  }
  __pyx_t_4 = __Pyx_PyObject_IsTrue(__pyx_t_1); if (unlikely((__pyx_t_4 < 0))) __PYX_ERR(0, 584, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __pyx_t_5 = (!__pyx_t_4);
  if (__pyx_t_5) {
/* … */
  }
```

</details>

L585  ⚪  (score=0)
```python
            # Classes with unicode names won't have specific handlers.
```
L586  🟡  (score=2)
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

L587  ⚪  (score=0)
```python
```
L588  🟡  (score=2)
```python
        call_type = 'general' if has_kwargs else 'simple'
```
<details><summary>Show generated C (score=2)</summary>

```c
  if (__pyx_v_has_kwargs) {
    __Pyx_INCREF(__pyx_mstate_global->__pyx_n_u_general);
    __pyx_t_1 = __pyx_mstate_global->__pyx_n_u_general;
  } else {
    __Pyx_INCREF(__pyx_mstate_global->__pyx_n_u_simple);
    __pyx_t_1 = __pyx_mstate_global->__pyx_n_u_simple;
  }
  __pyx_v_call_type = ((PyObject*)__pyx_t_1);
  __pyx_t_1 = 0;
```

</details>

L589  🔴  (score=17)
```python
        handler = getattr(self, f'_handle_{call_type}_{match_name}', None)
```
<details><summary>Show generated C (score=17)</summary>

```c
  __pyx_t_1 = __Pyx_PyUnicode_Unicode(__pyx_v_call_type); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 589, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __pyx_t_2 = __Pyx_PyObject_FormatSimple(__pyx_v_match_name, __pyx_mstate_global->__pyx_empty_unicode); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 589, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __pyx_t_6[0] = __pyx_mstate_global->__pyx_n_u_handle;
  __pyx_t_6[1] = __pyx_t_1;
  __pyx_t_6[2] = __pyx_mstate_global->__pyx_n_u__2;
  __pyx_t_6[3] = __pyx_t_2;
  __pyx_t_7 = __Pyx_PyUnicode_Join(__pyx_t_6, 4, 8 + __Pyx_PyUnicode_GET_LENGTH(__pyx_t_1) + 1 + __Pyx_PyUnicode_GET_LENGTH(__pyx_t_2), 127 | __Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_1) | __Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_2));
  if (unlikely(!__pyx_t_7)) __PYX_ERR(0, 589, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_7);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __pyx_t_2 = __Pyx_GetAttr3(((PyObject *)__pyx_v_self), __pyx_t_7, Py_None); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 589, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_DECREF(__pyx_t_7); __pyx_t_7 = 0;
  __pyx_v_handler = __pyx_t_2;
  __pyx_t_2 = 0;
```

</details>

L590  ⚪  (score=0)
```python
        if handler is None:
```
<details><summary>Show generated C (score=0)</summary>

```c
  __pyx_t_5 = (__pyx_v_handler == Py_None);
  if (__pyx_t_5) {
/* … */
  }
```

</details>

L591  🟠  (score=7)
```python
            handler = getattr(self, f'_handle_any_{match_name}', None)
```
<details><summary>Show generated C (score=7)</summary>

```c
    __pyx_t_2 = __Pyx_PyObject_FormatSimple(__pyx_v_match_name, __pyx_mstate_global->__pyx_empty_unicode); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 591, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_2);
    __pyx_t_7 = __Pyx_PyUnicode_Concat(__pyx_mstate_global->__pyx_n_u_handle_any, __pyx_t_2); if (unlikely(!__pyx_t_7)) __PYX_ERR(0, 591, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_7);
    __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
    __pyx_t_2 = __Pyx_GetAttr3(((PyObject *)__pyx_v_self), __pyx_t_7, Py_None); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 591, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_2);
    __Pyx_DECREF(__pyx_t_7); __pyx_t_7 = 0;
    __Pyx_DECREF_SET(__pyx_v_handler, __pyx_t_2);
    __pyx_t_2 = 0;
```

</details>

L592  🟡  (score=2)
```python
        return handler
```
<details><summary>Show generated C (score=2)</summary>

```c
  __Pyx_XDECREF(__pyx_r);
  __Pyx_INCREF(__pyx_v_handler);
  __pyx_r = __pyx_v_handler;
  goto __pyx_L0;
```

</details>

L593  ⚪  (score=0)
```python
```
L594  🟠  (score=6)
```python
    def _delegate_to_assigned_value(self, node, function, arg_list, kwargs):
```
<details><summary>Show generated C (score=6)</summary>

```c
static PyObject *__pyx_f_6Cython_8Compiler_7Visitor_25MethodDispatcherTransform__delegate_to_assigned_value(struct __pyx_obj_6Cython_8Compiler_7Visitor_MethodDispatcherTransform *__pyx_v_self, PyObject *__pyx_v_node, PyObject *__pyx_v_function, PyObject *__pyx_v_arg_list, PyObject *__pyx_v_kwargs) {
  PyObject *__pyx_v_assignment = NULL;
  PyObject *__pyx_v_value = NULL;
  PyObject *__pyx_r = NULL;
/* … */
  /* function exit code */
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_t_1);
  __Pyx_XDECREF(__pyx_t_2);
  __Pyx_AddTraceback("Cython.Compiler.Visitor.MethodDispatcherTransform._delegate_to_assigned_value", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_r = 0;
  __pyx_L0:;
  __Pyx_XDECREF(__pyx_v_assignment);
  __Pyx_XDECREF(__pyx_v_value);
  __Pyx_XGIVEREF(__pyx_r);
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}
```

</details>

L595  🟠  (score=5)
```python
        assignment = function.cf_state[0]
```
<details><summary>Show generated C (score=5)</summary>

```c
  __pyx_t_1 = __Pyx_PyObject_GetAttrStr(__pyx_v_function, __pyx_mstate_global->__pyx_n_u_cf_state); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 595, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __pyx_t_2 = __Pyx_GetItemInt(__pyx_t_1, 0, long, 1, __Pyx_PyLong_From_long, 0, 0, 1, 1, __Pyx_ReferenceSharing_OwnStrongReference); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 595, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __pyx_v_assignment = __pyx_t_2;
  __pyx_t_2 = 0;
```

</details>

L596  🟡  (score=2)
```python
        value = assignment.rhs
```
<details><summary>Show generated C (score=2)</summary>

```c
  __pyx_t_2 = __Pyx_PyObject_GetAttrStr(__pyx_v_assignment, __pyx_mstate_global->__pyx_n_u_rhs); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 596, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __pyx_v_value = __pyx_t_2;
  __pyx_t_2 = 0;
```

</details>

L597  🟠  (score=5)
```python
        if value.is_name:
```
<details><summary>Show generated C (score=5)</summary>

```c
  __pyx_t_2 = __Pyx_PyObject_GetAttrStr(__pyx_v_value, __pyx_mstate_global->__pyx_n_u_is_name); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 597, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __pyx_t_3 = __Pyx_PyObject_IsTrue(__pyx_t_2); if (unlikely((__pyx_t_3 < 0))) __PYX_ERR(0, 597, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  if (__pyx_t_3) {
/* … */
    goto __pyx_L3;
  }
```

</details>

L598  🔴  (score=16)
```python
            if not value.entry or len(value.entry.cf_assignments) > 1:
```
<details><summary>Show generated C (score=16)</summary>

```c
    __pyx_t_2 = __Pyx_PyObject_GetAttrStr(__pyx_v_value, __pyx_mstate_global->__pyx_n_u_entry); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 598, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_2);
    __pyx_t_4 = __Pyx_PyObject_IsTrue(__pyx_t_2); if (unlikely((__pyx_t_4 < 0))) __PYX_ERR(0, 598, __pyx_L1_error)
    __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
    __pyx_t_5 = (!__pyx_t_4);
    if (!__pyx_t_5) {
    } else {
      __pyx_t_3 = __pyx_t_5;
      goto __pyx_L5_bool_binop_done;
    }
    __pyx_t_2 = __Pyx_PyObject_GetAttrStr(__pyx_v_value, __pyx_mstate_global->__pyx_n_u_entry); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 598, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_2);
    __pyx_t_1 = __Pyx_PyObject_GetAttrStr(__pyx_t_2, __pyx_mstate_global->__pyx_n_u_cf_assignments); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 598, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_1);
    __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
    __pyx_t_6 = PyObject_Length(__pyx_t_1); if (unlikely(__pyx_t_6 == ((Py_ssize_t)-1))) __PYX_ERR(0, 598, __pyx_L1_error)
    __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
    __pyx_t_5 = (__pyx_t_6 > 1);
    __pyx_t_3 = __pyx_t_5;
    __pyx_L5_bool_binop_done:;
    if (__pyx_t_3) {
/* … */
    }
```

</details>

L599  ⚪  (score=0)
```python
                # the variable might have been reassigned => play safe
```
L600  🟡  (score=2)
```python
                return node
```
<details><summary>Show generated C (score=2)</summary>

```c
      __Pyx_XDECREF(__pyx_r);
      __Pyx_INCREF(__pyx_v_node);
      __pyx_r = __pyx_v_node;
      goto __pyx_L0;
```

</details>

L601  🔴  (score=13)
```python
        elif value.is_attribute and value.obj.is_name:
```
<details><summary>Show generated C (score=13)</summary>

```c
  __pyx_t_1 = __Pyx_PyObject_GetAttrStr(__pyx_v_value, __pyx_mstate_global->__pyx_n_u_is_attribute); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 601, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __pyx_t_5 = __Pyx_PyObject_IsTrue(__pyx_t_1); if (unlikely((__pyx_t_5 < 0))) __PYX_ERR(0, 601, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  if (__pyx_t_5) {
  } else {
    __pyx_t_3 = __pyx_t_5;
    goto __pyx_L7_bool_binop_done;
  }
  __pyx_t_1 = __Pyx_PyObject_GetAttrStr(__pyx_v_value, __pyx_mstate_global->__pyx_n_u_obj); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 601, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __pyx_t_2 = __Pyx_PyObject_GetAttrStr(__pyx_t_1, __pyx_mstate_global->__pyx_n_u_is_name); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 601, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __pyx_t_5 = __Pyx_PyObject_IsTrue(__pyx_t_2); if (unlikely((__pyx_t_5 < 0))) __PYX_ERR(0, 601, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __pyx_t_3 = __pyx_t_5;
  __pyx_L7_bool_binop_done:;
  if (__pyx_t_3) {
/* … */
    goto __pyx_L3;
  }
```

</details>

L602  🔴  (score=22)
```python
            if not value.obj.entry or len(value.obj.entry.cf_assignments) > 1:
```
<details><summary>Show generated C (score=22)</summary>

```c
    __pyx_t_2 = __Pyx_PyObject_GetAttrStr(__pyx_v_value, __pyx_mstate_global->__pyx_n_u_obj); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 602, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_2);
    __pyx_t_1 = __Pyx_PyObject_GetAttrStr(__pyx_t_2, __pyx_mstate_global->__pyx_n_u_entry); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 602, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_1);
    __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
    __pyx_t_5 = __Pyx_PyObject_IsTrue(__pyx_t_1); if (unlikely((__pyx_t_5 < 0))) __PYX_ERR(0, 602, __pyx_L1_error)
    __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
    __pyx_t_4 = (!__pyx_t_5);
    if (!__pyx_t_4) {
    } else {
      __pyx_t_3 = __pyx_t_4;
      goto __pyx_L10_bool_binop_done;
    }
    __pyx_t_1 = __Pyx_PyObject_GetAttrStr(__pyx_v_value, __pyx_mstate_global->__pyx_n_u_obj); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 602, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_1);
    __pyx_t_2 = __Pyx_PyObject_GetAttrStr(__pyx_t_1, __pyx_mstate_global->__pyx_n_u_entry); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 602, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_2);
    __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
    __pyx_t_1 = __Pyx_PyObject_GetAttrStr(__pyx_t_2, __pyx_mstate_global->__pyx_n_u_cf_assignments); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 602, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_1);
    __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
    __pyx_t_6 = PyObject_Length(__pyx_t_1); if (unlikely(__pyx_t_6 == ((Py_ssize_t)-1))) __PYX_ERR(0, 602, __pyx_L1_error)
    __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
    __pyx_t_4 = (__pyx_t_6 > 1);
    __pyx_t_3 = __pyx_t_4;
    __pyx_L10_bool_binop_done:;
    if (__pyx_t_3) {
/* … */
    }
```

</details>

L603  ⚪  (score=0)
```python
                # the underlying variable might have been reassigned => play safe
```
L604  🟡  (score=2)
```python
                return node
```
<details><summary>Show generated C (score=2)</summary>

```c
      __Pyx_XDECREF(__pyx_r);
      __Pyx_INCREF(__pyx_v_node);
      __pyx_r = __pyx_v_node;
      goto __pyx_L0;
```

</details>

L605  ⚪  (score=0)
```python
        else:
```
L606  🟡  (score=2)
```python
            return node
```
<details><summary>Show generated C (score=2)</summary>

```c
  /*else*/ {
    __Pyx_XDECREF(__pyx_r);
    __Pyx_INCREF(__pyx_v_node);
    __pyx_r = __pyx_v_node;
    goto __pyx_L0;
  }
  __pyx_L3:;
```

</details>

L607  🟡  (score=1)
```python
        return self._dispatch_to_handler(
```
<details><summary>Show generated C (score=1)</summary>

```c
  __Pyx_XDECREF(__pyx_r);
/* … */
  __pyx_t_1 = ((struct __pyx_vtabstruct_6Cython_8Compiler_7Visitor_MethodDispatcherTransform *)__pyx_v_self->__pyx_base.__pyx_base.__pyx_base.__pyx_base.__pyx_vtab)->_dispatch_to_handler(__pyx_v_self, __pyx_v_node, __pyx_v_value, __pyx_v_arg_list, __pyx_v_kwargs); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 607, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __pyx_r = __pyx_t_1;
  __pyx_t_1 = 0;
  goto __pyx_L0;
```

</details>

L608  ⚪  (score=0)
```python
            node, value, arg_list, kwargs)
```
L609  ⚪  (score=0)
```python
```
L610  🔴  (score=18)
```python
    def _dispatch_to_handler(self, node, function, arg_list, kwargs):
```
<details><summary>Show generated C (score=18)</summary>

```c
static PyObject *__pyx_f_6Cython_8Compiler_7Visitor_25MethodDispatcherTransform__dispatch_to_handler(struct __pyx_obj_6Cython_8Compiler_7Visitor_MethodDispatcherTransform *__pyx_v_self, PyObject *__pyx_v_node, PyObject *__pyx_v_function, PyObject *__pyx_v_arg_list, PyObject *__pyx_v_kwargs) {
  PyObject *__pyx_v_entry = NULL;
  PyObject *__pyx_v_is_builtin = NULL;
  PyObject *__pyx_v_function_handler = NULL;
  PyObject *__pyx_v_attr_name = NULL;
  PyObject *__pyx_v_self_arg = NULL;
  PyObject *__pyx_v_obj_type = NULL;
  int __pyx_v_is_unbound_method;
  PyObject *__pyx_v_type_name = NULL;
  PyObject *__pyx_r = NULL;
  __Pyx_INCREF(__pyx_v_arg_list);
/* … */
  /* function exit code */
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_t_1);
  __Pyx_XDECREF(__pyx_t_4);
  __Pyx_XDECREF(__pyx_t_5);
  __Pyx_XDECREF(__pyx_t_6);
  __Pyx_XDECREF(__pyx_t_7);
  __Pyx_XDECREF(__pyx_t_8);
  __Pyx_XDECREF(__pyx_t_9);
  __Pyx_AddTraceback("Cython.Compiler.Visitor.MethodDispatcherTransform._dispatch_to_handler", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_r = 0;
  __pyx_L0:;
  __Pyx_XDECREF(__pyx_v_entry);
  __Pyx_XDECREF(__pyx_v_is_builtin);
  __Pyx_XDECREF(__pyx_v_function_handler);
  __Pyx_XDECREF(__pyx_v_attr_name);
  __Pyx_XDECREF(__pyx_v_self_arg);
  __Pyx_XDECREF(__pyx_v_obj_type);
  __Pyx_XDECREF(__pyx_v_type_name);
  __Pyx_XDECREF(__pyx_v_arg_list);
  __Pyx_XGIVEREF(__pyx_r);
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}
```

</details>

L611  🟠  (score=5)
```python
        if function.is_name:
```
<details><summary>Show generated C (score=5)</summary>

```c
  __pyx_t_1 = __Pyx_PyObject_GetAttrStr(__pyx_v_function, __pyx_mstate_global->__pyx_n_u_is_name); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 611, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __pyx_t_2 = __Pyx_PyObject_IsTrue(__pyx_t_1); if (unlikely((__pyx_t_2 < 0))) __PYX_ERR(0, 611, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  if (__pyx_t_2) {
/* … */
  }
```

</details>

L612  ⚪  (score=0)
```python
            # we only consider functions that are either builtin
```
L613  ⚪  (score=0)
```python
            # Python functions or builtins that were already replaced
```
L614  ⚪  (score=0)
```python
            # into a C function call (defined in the builtin scope)
```
L615  🟠  (score=5)
```python
            if not function.entry:
```
<details><summary>Show generated C (score=5)</summary>

```c
    __pyx_t_1 = __Pyx_PyObject_GetAttrStr(__pyx_v_function, __pyx_mstate_global->__pyx_n_u_entry); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 615, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_1);
    __pyx_t_2 = __Pyx_PyObject_IsTrue(__pyx_t_1); if (unlikely((__pyx_t_2 < 0))) __PYX_ERR(0, 615, __pyx_L1_error)
    __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
    __pyx_t_3 = (!__pyx_t_2);
    if (__pyx_t_3) {
/* … */
    }
```

</details>

L616  🟡  (score=2)
```python
                return node
```
<details><summary>Show generated C (score=2)</summary>

```c
      __Pyx_XDECREF(__pyx_r);
      __Pyx_INCREF(__pyx_v_node);
      __pyx_r = __pyx_v_node;
      goto __pyx_L0;
```

</details>

L617  🟡  (score=2)
```python
            entry = function.entry
```
<details><summary>Show generated C (score=2)</summary>

```c
    __pyx_t_1 = __Pyx_PyObject_GetAttrStr(__pyx_v_function, __pyx_mstate_global->__pyx_n_u_entry); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 617, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_1);
    __pyx_v_entry = __pyx_t_1;
    __pyx_t_1 = 0;
```

</details>

L618  ⚪  (score=0)
```python
            is_builtin = (
```
L619  🟠  (score=7)
```python
                entry.is_builtin or
```
<details><summary>Show generated C (score=7)</summary>

```c
    __pyx_t_4 = __Pyx_PyObject_GetAttrStr(__pyx_v_entry, __pyx_mstate_global->__pyx_n_u_is_builtin); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 619, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_4);
    __pyx_t_3 = __Pyx_PyObject_IsTrue(__pyx_t_4); if (unlikely((__pyx_t_3 < 0))) __PYX_ERR(0, 619, __pyx_L1_error)
    if (!__pyx_t_3) {
      __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
    } else {
      __Pyx_INCREF(__pyx_t_4);
      __pyx_t_1 = __pyx_t_4;
      __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
      goto __pyx_L5_bool_binop_done;
    }
```

</details>

L620  🔴  (score=20)
```python
                entry is self.current_env().builtin_scope().lookup_here(function.name))
```
<details><summary>Show generated C (score=20)</summary>

```c
    __pyx_t_9 = ((PyObject *)__pyx_v_self);
    __Pyx_INCREF(__pyx_t_9);
    __pyx_t_10 = 0;
    {
      PyObject *__pyx_callargs[2] = {__pyx_t_9, NULL};
      __pyx_t_8 = __Pyx_PyObject_FastCallMethod((PyObject*)__pyx_mstate_global->__pyx_n_u_current_env, __pyx_callargs+__pyx_t_10, (1-__pyx_t_10) | (1*__Pyx_PY_VECTORCALL_ARGUMENTS_OFFSET));
      __Pyx_XDECREF(__pyx_t_9); __pyx_t_9 = 0;
      if (unlikely(!__pyx_t_8)) __PYX_ERR(0, 620, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_8);
    }
    __pyx_t_7 = __pyx_t_8;
    __Pyx_INCREF(__pyx_t_7);
    __pyx_t_10 = 0;
    {
      PyObject *__pyx_callargs[2] = {__pyx_t_7, NULL};
      __pyx_t_6 = __Pyx_PyObject_FastCallMethod((PyObject*)__pyx_mstate_global->__pyx_n_u_builtin_scope, __pyx_callargs+__pyx_t_10, (1-__pyx_t_10) | (1*__Pyx_PY_VECTORCALL_ARGUMENTS_OFFSET));
      __Pyx_XDECREF(__pyx_t_7); __pyx_t_7 = 0;
      __Pyx_DECREF(__pyx_t_8); __pyx_t_8 = 0;
      if (unlikely(!__pyx_t_6)) __PYX_ERR(0, 620, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_6);
    }
    __pyx_t_5 = __pyx_t_6;
    __Pyx_INCREF(__pyx_t_5);
    __pyx_t_8 = __Pyx_PyObject_GetAttrStr(__pyx_v_function, __pyx_mstate_global->__pyx_n_u_name_2); if (unlikely(!__pyx_t_8)) __PYX_ERR(0, 620, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_8);
    __pyx_t_10 = 0;
    {
      PyObject *__pyx_callargs[2] = {__pyx_t_5, __pyx_t_8};
      __pyx_t_4 = __Pyx_PyObject_FastCallMethod((PyObject*)__pyx_mstate_global->__pyx_n_u_lookup_here, __pyx_callargs+__pyx_t_10, (2-__pyx_t_10) | (1*__Pyx_PY_VECTORCALL_ARGUMENTS_OFFSET));
      __Pyx_XDECREF(__pyx_t_5); __pyx_t_5 = 0;
      __Pyx_DECREF(__pyx_t_8); __pyx_t_8 = 0;
      __Pyx_DECREF(__pyx_t_6); __pyx_t_6 = 0;
      if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 620, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_4);
    }
    __pyx_t_3 = (__pyx_v_entry == __pyx_t_4);
    __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
    __pyx_t_4 = __Pyx_PyBool_FromLong(__pyx_t_3); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 620, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_4);
    __pyx_t_1 = __pyx_t_4;
    __pyx_t_4 = 0;
    __pyx_L5_bool_binop_done:;
    __pyx_v_is_builtin = __pyx_t_1;
    __pyx_t_1 = 0;
```

</details>

L621  🟡  (score=2)
```python
            if not is_builtin:
```
<details><summary>Show generated C (score=2)</summary>

```c
    __pyx_t_3 = __Pyx_PyObject_IsTrue(__pyx_v_is_builtin); if (unlikely((__pyx_t_3 < 0))) __PYX_ERR(0, 621, __pyx_L1_error)
    __pyx_t_2 = (!__pyx_t_3);
    if (__pyx_t_2) {
/* … */
    }
```

</details>

L622  🔴  (score=13)
```python
                if function.cf_state and function.cf_state.is_single:
```
<details><summary>Show generated C (score=13)</summary>

```c
      __pyx_t_1 = __Pyx_PyObject_GetAttrStr(__pyx_v_function, __pyx_mstate_global->__pyx_n_u_cf_state); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 622, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_1);
      __pyx_t_3 = __Pyx_PyObject_IsTrue(__pyx_t_1); if (unlikely((__pyx_t_3 < 0))) __PYX_ERR(0, 622, __pyx_L1_error)
      __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
      if (__pyx_t_3) {
      } else {
        __pyx_t_2 = __pyx_t_3;
        goto __pyx_L9_bool_binop_done;
      }
      __pyx_t_1 = __Pyx_PyObject_GetAttrStr(__pyx_v_function, __pyx_mstate_global->__pyx_n_u_cf_state); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 622, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_1);
      __pyx_t_4 = __Pyx_PyObject_GetAttrStr(__pyx_t_1, __pyx_mstate_global->__pyx_n_u_is_single); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 622, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_4);
      __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
      __pyx_t_3 = __Pyx_PyObject_IsTrue(__pyx_t_4); if (unlikely((__pyx_t_3 < 0))) __PYX_ERR(0, 622, __pyx_L1_error)
      __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
      __pyx_t_2 = __pyx_t_3;
      __pyx_L9_bool_binop_done:;
      if (__pyx_t_2) {
/* … */
      }
```

</details>

L623  ⚪  (score=0)
```python
                    # we know the value of the variable
```
L624  ⚪  (score=0)
```python
                    # => see if it's usable instead
```
L625  🟡  (score=1)
```python
                    return self._delegate_to_assigned_value(
```
<details><summary>Show generated C (score=1)</summary>

```c
        __Pyx_XDECREF(__pyx_r);
/* … */
        __pyx_t_4 = ((struct __pyx_vtabstruct_6Cython_8Compiler_7Visitor_MethodDispatcherTransform *)__pyx_v_self->__pyx_base.__pyx_base.__pyx_base.__pyx_base.__pyx_vtab)->_delegate_to_assigned_value(__pyx_v_self, __pyx_v_node, __pyx_v_function, __pyx_v_arg_list, __pyx_v_kwargs); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 625, __pyx_L1_error)
        __Pyx_GOTREF(__pyx_t_4);
        __pyx_r = __pyx_t_4;
        __pyx_t_4 = 0;
        goto __pyx_L0;
```

</details>

L626  ⚪  (score=0)
```python
                        node, function, arg_list, kwargs)
```
L627  🔴  (score=23)
```python
                if arg_list and entry.is_cmethod and entry.scope and entry.scope.parent_type.is_builtin_type:
```
<details><summary>Show generated C (score=23)</summary>

```c
      __pyx_t_3 = __Pyx_PyObject_IsTrue(__pyx_v_arg_list); if (unlikely((__pyx_t_3 < 0))) __PYX_ERR(0, 627, __pyx_L1_error)
      if (__pyx_t_3) {
      } else {
        __pyx_t_2 = __pyx_t_3;
        goto __pyx_L12_bool_binop_done;
      }
      __pyx_t_4 = __Pyx_PyObject_GetAttrStr(__pyx_v_entry, __pyx_mstate_global->__pyx_n_u_is_cmethod); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 627, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_4);
      __pyx_t_3 = __Pyx_PyObject_IsTrue(__pyx_t_4); if (unlikely((__pyx_t_3 < 0))) __PYX_ERR(0, 627, __pyx_L1_error)
      __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
      if (__pyx_t_3) {
      } else {
        __pyx_t_2 = __pyx_t_3;
        goto __pyx_L12_bool_binop_done;
      }
      __pyx_t_4 = __Pyx_PyObject_GetAttrStr(__pyx_v_entry, __pyx_mstate_global->__pyx_n_u_scope); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 627, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_4);
      __pyx_t_3 = __Pyx_PyObject_IsTrue(__pyx_t_4); if (unlikely((__pyx_t_3 < 0))) __PYX_ERR(0, 627, __pyx_L1_error)
      __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
      if (__pyx_t_3) {
      } else {
        __pyx_t_2 = __pyx_t_3;
        goto __pyx_L12_bool_binop_done;
      }
      __pyx_t_4 = __Pyx_PyObject_GetAttrStr(__pyx_v_entry, __pyx_mstate_global->__pyx_n_u_scope); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 627, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_4);
      __pyx_t_1 = __Pyx_PyObject_GetAttrStr(__pyx_t_4, __pyx_mstate_global->__pyx_n_u_parent_type); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 627, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_1);
      __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
      __pyx_t_4 = __Pyx_PyObject_GetAttrStr(__pyx_t_1, __pyx_mstate_global->__pyx_n_u_is_builtin_type); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 627, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_4);
      __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
      __pyx_t_3 = __Pyx_PyObject_IsTrue(__pyx_t_4); if (unlikely((__pyx_t_3 < 0))) __PYX_ERR(0, 627, __pyx_L1_error)
      __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
      __pyx_t_2 = __pyx_t_3;
      __pyx_L12_bool_binop_done:;
      if (__pyx_t_2) {
/* … */
      }
```

</details>

L628  🔴  (score=12)
```python
                    if entry.scope.parent_type is arg_list[0].type:
```
<details><summary>Show generated C (score=12)</summary>

```c
        __pyx_t_4 = __Pyx_PyObject_GetAttrStr(__pyx_v_entry, __pyx_mstate_global->__pyx_n_u_scope); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 628, __pyx_L1_error)
        __Pyx_GOTREF(__pyx_t_4);
        __pyx_t_1 = __Pyx_PyObject_GetAttrStr(__pyx_t_4, __pyx_mstate_global->__pyx_n_u_parent_type); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 628, __pyx_L1_error)
        __Pyx_GOTREF(__pyx_t_1);
        __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
        __pyx_t_4 = __Pyx_GetItemInt(__pyx_v_arg_list, 0, long, 1, __Pyx_PyLong_From_long, 0, 0, 1, 1, __Pyx_ReferenceSharing_FunctionArgument); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 628, __pyx_L1_error)
        __Pyx_GOTREF(__pyx_t_4);
        __pyx_t_6 = __Pyx_PyObject_GetAttrStr(__pyx_t_4, __pyx_mstate_global->__pyx_n_u_type); if (unlikely(!__pyx_t_6)) __PYX_ERR(0, 628, __pyx_L1_error)
        __Pyx_GOTREF(__pyx_t_6);
        __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
        __pyx_t_2 = (__pyx_t_1 == __pyx_t_6);
        __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
        __Pyx_DECREF(__pyx_t_6); __pyx_t_6 = 0;
        if (__pyx_t_2) {
/* … */
        }
```

</details>

L629  ⚪  (score=0)
```python
                        # Optimised (unbound) method of a builtin type => try to "de-optimise".
```
L630  🟡  (score=3)
```python
                        return self._dispatch_to_method_handler(
```
<details><summary>Show generated C (score=3)</summary>

```c
          __Pyx_XDECREF(__pyx_r);
/* … */
          __pyx_t_4 = ((struct __pyx_vtabstruct_6Cython_8Compiler_7Visitor_MethodDispatcherTransform *)__pyx_v_self->__pyx_base.__pyx_base.__pyx_base.__pyx_base.__pyx_vtab)->_dispatch_to_method_handler(__pyx_v_self, __pyx_t_6, Py_None, Py_True, __pyx_t_1, __pyx_v_node, __pyx_v_function, __pyx_v_arg_list, __pyx_v_kwargs); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 630, __pyx_L1_error)
          __Pyx_GOTREF(__pyx_t_4);
          __Pyx_DECREF(__pyx_t_6); __pyx_t_6 = 0;
          __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
          __pyx_r = __pyx_t_4;
          __pyx_t_4 = 0;
          goto __pyx_L0;
```

</details>

L631  🟡  (score=2)
```python
                            entry.name, self_arg=None, is_unbound_method=True,
```
<details><summary>Show generated C (score=2)</summary>

```c
          __pyx_t_6 = __Pyx_PyObject_GetAttrStr(__pyx_v_entry, __pyx_mstate_global->__pyx_n_u_name_2); if (unlikely(!__pyx_t_6)) __PYX_ERR(0, 631, __pyx_L1_error)
          __Pyx_GOTREF(__pyx_t_6);
```

</details>

L632  🟠  (score=8)
```python
                            type_name=entry.scope.parent_type.name,
```
<details><summary>Show generated C (score=8)</summary>

```c
          __pyx_t_1 = __Pyx_PyObject_GetAttrStr(__pyx_v_entry, __pyx_mstate_global->__pyx_n_u_scope); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 632, __pyx_L1_error)
          __Pyx_GOTREF(__pyx_t_1);
          __pyx_t_4 = __Pyx_PyObject_GetAttrStr(__pyx_t_1, __pyx_mstate_global->__pyx_n_u_parent_type); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 632, __pyx_L1_error)
          __Pyx_GOTREF(__pyx_t_4);
          __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
          __pyx_t_1 = __Pyx_PyObject_GetAttrStr(__pyx_t_4, __pyx_mstate_global->__pyx_n_u_name_2); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 632, __pyx_L1_error)
          __Pyx_GOTREF(__pyx_t_1);
          __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
```

</details>

L633  ⚪  (score=0)
```python
                            node=node, function=function, arg_list=arg_list, kwargs=kwargs)
```
L634  🟡  (score=2)
```python
                return node
```
<details><summary>Show generated C (score=2)</summary>

```c
      __Pyx_XDECREF(__pyx_r);
      __Pyx_INCREF(__pyx_v_node);
      __pyx_r = __pyx_v_node;
      goto __pyx_L0;
```

</details>

L635  🟡  (score=1)
```python
            function_handler = self._find_handler(
```
<details><summary>Show generated C (score=1)</summary>

```c
    __pyx_t_1 = ((struct __pyx_vtabstruct_6Cython_8Compiler_7Visitor_MethodDispatcherTransform *)__pyx_v_self->__pyx_base.__pyx_base.__pyx_base.__pyx_base.__pyx_vtab)->_find_handler(__pyx_v_self, __pyx_t_4, __pyx_t_2); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 635, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_1);
    __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
    __pyx_v_function_handler = __pyx_t_1;
    __pyx_t_1 = 0;
```

</details>

L636  🔴  (score=10)
```python
                f"function_{function.name}", kwargs)
```
<details><summary>Show generated C (score=10)</summary>

```c
    __pyx_t_4 = __Pyx_PyObject_GetAttrStr(__pyx_v_function, __pyx_mstate_global->__pyx_n_u_name_2); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 636, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_4);
    __pyx_t_1 = __Pyx_PyObject_FormatSimple(__pyx_t_4, __pyx_mstate_global->__pyx_empty_unicode); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 636, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_1);
    __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
    __pyx_t_4 = __Pyx_PyUnicode_Concat(__pyx_mstate_global->__pyx_n_u_function_2, __pyx_t_1); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 636, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_4);
    __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
    __pyx_t_2 = __Pyx_PyObject_IsTrue(__pyx_v_kwargs); if (unlikely((__pyx_t_2 == (int)-1) && PyErr_Occurred())) __PYX_ERR(0, 636, __pyx_L1_error)
```

</details>

L637  ⚪  (score=0)
```python
            if function_handler is None:
```
<details><summary>Show generated C (score=0)</summary>

```c
    __pyx_t_2 = (__pyx_v_function_handler == Py_None);
    if (__pyx_t_2) {
/* … */
    }
```

</details>

L638  🟠  (score=8)
```python
                return self._handle_function(node, function.name, function, arg_list, kwargs)
```
<details><summary>Show generated C (score=8)</summary>

```c
      __Pyx_XDECREF(__pyx_r);
      __pyx_t_4 = ((PyObject *)__pyx_v_self);
      __Pyx_INCREF(__pyx_t_4);
      __pyx_t_6 = __Pyx_PyObject_GetAttrStr(__pyx_v_function, __pyx_mstate_global->__pyx_n_u_name_2); if (unlikely(!__pyx_t_6)) __PYX_ERR(0, 638, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_6);
      __pyx_t_10 = 0;
      {
        PyObject *__pyx_callargs[6] = {__pyx_t_4, __pyx_v_node, __pyx_t_6, __pyx_v_function, __pyx_v_arg_list, __pyx_v_kwargs};
        __pyx_t_1 = __Pyx_PyObject_FastCallMethod((PyObject*)__pyx_mstate_global->__pyx_n_u_handle_function, __pyx_callargs+__pyx_t_10, (6-__pyx_t_10) | (1*__Pyx_PY_VECTORCALL_ARGUMENTS_OFFSET));
        __Pyx_XDECREF(__pyx_t_4); __pyx_t_4 = 0;
        __Pyx_DECREF(__pyx_t_6); __pyx_t_6 = 0;
        if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 638, __pyx_L1_error)
        __Pyx_GOTREF(__pyx_t_1);
      }
      __pyx_r = __pyx_t_1;
      __pyx_t_1 = 0;
      goto __pyx_L0;
```

</details>

L639  🟡  (score=2)
```python
            if kwargs:
```
<details><summary>Show generated C (score=2)</summary>

```c
    __pyx_t_2 = __Pyx_PyObject_IsTrue(__pyx_v_kwargs); if (unlikely((__pyx_t_2 < 0))) __PYX_ERR(0, 639, __pyx_L1_error)
    if (__pyx_t_2) {
/* … */
    }
```

</details>

L640  🔴  (score=16)
```python
                return function_handler(node, function, arg_list, kwargs)
```
<details><summary>Show generated C (score=16)</summary>

```c
      __Pyx_XDECREF(__pyx_r);
      __pyx_t_6 = NULL;
      __Pyx_INCREF(__pyx_v_function_handler);
      __pyx_t_4 = __pyx_v_function_handler; 
      __pyx_t_10 = 1;
      #if CYTHON_UNPACK_METHODS
      if (unlikely(PyMethod_Check(__pyx_t_4))) {
        __pyx_t_6 = PyMethod_GET_SELF(__pyx_t_4);
        assert(__pyx_t_6);
        PyObject* __pyx__function = PyMethod_GET_FUNCTION(__pyx_t_4);
        __Pyx_INCREF(__pyx_t_6);
        __Pyx_INCREF(__pyx__function);
        __Pyx_DECREF_SET(__pyx_t_4, __pyx__function);
        __pyx_t_10 = 0;
      }
      #endif
      {
        PyObject *__pyx_callargs[5] = {__pyx_t_6, __pyx_v_node, __pyx_v_function, __pyx_v_arg_list, __pyx_v_kwargs};
        __pyx_t_1 = __Pyx_PyObject_FastCall((PyObject*)__pyx_t_4, __pyx_callargs+__pyx_t_10, (5-__pyx_t_10) | (__pyx_t_10*__Pyx_PY_VECTORCALL_ARGUMENTS_OFFSET));
        __Pyx_XDECREF(__pyx_t_6); __pyx_t_6 = 0;
        __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
        if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 640, __pyx_L1_error)
        __Pyx_GOTREF(__pyx_t_1);
      }
      __pyx_r = __pyx_t_1;
      __pyx_t_1 = 0;
      goto __pyx_L0;
```

</details>

L641  ⚪  (score=0)
```python
            else:
```
L642  🔴  (score=16)
```python
                return function_handler(node, function, arg_list)
```
<details><summary>Show generated C (score=16)</summary>

```c
    /*else*/ {
      __Pyx_XDECREF(__pyx_r);
      __pyx_t_4 = NULL;
      __Pyx_INCREF(__pyx_v_function_handler);
      __pyx_t_6 = __pyx_v_function_handler; 
      __pyx_t_10 = 1;
      #if CYTHON_UNPACK_METHODS
      if (unlikely(PyMethod_Check(__pyx_t_6))) {
        __pyx_t_4 = PyMethod_GET_SELF(__pyx_t_6);
        assert(__pyx_t_4);
        PyObject* __pyx__function = PyMethod_GET_FUNCTION(__pyx_t_6);
        __Pyx_INCREF(__pyx_t_4);
        __Pyx_INCREF(__pyx__function);
        __Pyx_DECREF_SET(__pyx_t_6, __pyx__function);
        __pyx_t_10 = 0;
      }
      #endif
      {
        PyObject *__pyx_callargs[4] = {__pyx_t_4, __pyx_v_node, __pyx_v_function, __pyx_v_arg_list};
        __pyx_t_1 = __Pyx_PyObject_FastCall((PyObject*)__pyx_t_6, __pyx_callargs+__pyx_t_10, (4-__pyx_t_10) | (__pyx_t_10*__Pyx_PY_VECTORCALL_ARGUMENTS_OFFSET));
        __Pyx_XDECREF(__pyx_t_4); __pyx_t_4 = 0;
        __Pyx_DECREF(__pyx_t_6); __pyx_t_6 = 0;
        if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 642, __pyx_L1_error)
        __Pyx_GOTREF(__pyx_t_1);
      }
      __pyx_r = __pyx_t_1;
      __pyx_t_1 = 0;
      goto __pyx_L0;
    }
```

</details>

L643  🟠  (score=5)
```python
        elif function.is_attribute:
```
<details><summary>Show generated C (score=5)</summary>

```c
  __pyx_t_1 = __Pyx_PyObject_GetAttrStr(__pyx_v_function, __pyx_mstate_global->__pyx_n_u_is_attribute); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 643, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __pyx_t_2 = __Pyx_PyObject_IsTrue(__pyx_t_1); if (unlikely((__pyx_t_2 < 0))) __PYX_ERR(0, 643, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  if (__pyx_t_2) {
/* … */
  }
```

</details>

L644  🟡  (score=2)
```python
            attr_name = function.attribute
```
<details><summary>Show generated C (score=2)</summary>

```c
    __pyx_t_1 = __Pyx_PyObject_GetAttrStr(__pyx_v_function, __pyx_mstate_global->__pyx_n_u_attribute); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 644, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_1);
    __pyx_v_attr_name = __pyx_t_1;
    __pyx_t_1 = 0;
```

</details>

L645  🟠  (score=8)
```python
            if function.type.is_pyobject:
```
<details><summary>Show generated C (score=8)</summary>

```c
    __pyx_t_1 = __Pyx_PyObject_GetAttrStr(__pyx_v_function, __pyx_mstate_global->__pyx_n_u_type); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 645, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_1);
    __pyx_t_6 = __Pyx_PyObject_GetAttrStr(__pyx_t_1, __pyx_mstate_global->__pyx_n_u_is_pyobject); if (unlikely(!__pyx_t_6)) __PYX_ERR(0, 645, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_6);
    __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
    __pyx_t_2 = __Pyx_PyObject_IsTrue(__pyx_t_6); if (unlikely((__pyx_t_2 < 0))) __PYX_ERR(0, 645, __pyx_L1_error)
    __Pyx_DECREF(__pyx_t_6); __pyx_t_6 = 0;
    if (__pyx_t_2) {
/* … */
      goto __pyx_L19;
    }
```

</details>

L646  🟡  (score=2)
```python
                self_arg = function.obj
```
<details><summary>Show generated C (score=2)</summary>

```c
      __pyx_t_6 = __Pyx_PyObject_GetAttrStr(__pyx_v_function, __pyx_mstate_global->__pyx_n_u_obj); if (unlikely(!__pyx_t_6)) __PYX_ERR(0, 646, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_6);
      __pyx_v_self_arg = __pyx_t_6;
      __pyx_t_6 = 0;
```

</details>

L647  🔴  (score=10)
```python
            elif node.self and function.entry:
```
<details><summary>Show generated C (score=10)</summary>

```c
    __pyx_t_6 = __Pyx_PyObject_GetAttrStr(__pyx_v_node, __pyx_mstate_global->__pyx_n_u_self); if (unlikely(!__pyx_t_6)) __PYX_ERR(0, 647, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_6);
    __pyx_t_3 = __Pyx_PyObject_IsTrue(__pyx_t_6); if (unlikely((__pyx_t_3 < 0))) __PYX_ERR(0, 647, __pyx_L1_error)
    __Pyx_DECREF(__pyx_t_6); __pyx_t_6 = 0;
    if (__pyx_t_3) {
    } else {
      __pyx_t_2 = __pyx_t_3;
      goto __pyx_L20_bool_binop_done;
    }
    __pyx_t_6 = __Pyx_PyObject_GetAttrStr(__pyx_v_function, __pyx_mstate_global->__pyx_n_u_entry); if (unlikely(!__pyx_t_6)) __PYX_ERR(0, 647, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_6);
    __pyx_t_3 = __Pyx_PyObject_IsTrue(__pyx_t_6); if (unlikely((__pyx_t_3 < 0))) __PYX_ERR(0, 647, __pyx_L1_error)
    __Pyx_DECREF(__pyx_t_6); __pyx_t_6 = 0;
    __pyx_t_2 = __pyx_t_3;
    __pyx_L20_bool_binop_done:;
    if (__pyx_t_2) {
/* … */
      goto __pyx_L19;
    }
```

</details>

L648  🟠  (score=5)
```python
                entry = function.entry.as_variable
```
<details><summary>Show generated C (score=5)</summary>

```c
      __pyx_t_6 = __Pyx_PyObject_GetAttrStr(__pyx_v_function, __pyx_mstate_global->__pyx_n_u_entry); if (unlikely(!__pyx_t_6)) __PYX_ERR(0, 648, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_6);
      __pyx_t_1 = __Pyx_PyObject_GetAttrStr(__pyx_t_6, __pyx_mstate_global->__pyx_n_u_as_variable); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 648, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_1);
      __Pyx_DECREF(__pyx_t_6); __pyx_t_6 = 0;
      __pyx_v_entry = __pyx_t_1;
      __pyx_t_1 = 0;
```

</details>

L649  🟠  (score=7)
```python
                if not entry or not entry.is_builtin:
```
<details><summary>Show generated C (score=7)</summary>

```c
      __pyx_t_3 = __Pyx_PyObject_IsTrue(__pyx_v_entry); if (unlikely((__pyx_t_3 < 0))) __PYX_ERR(0, 649, __pyx_L1_error)
      __pyx_t_11 = (!__pyx_t_3);
      if (!__pyx_t_11) {
      } else {
        __pyx_t_2 = __pyx_t_11;
        goto __pyx_L23_bool_binop_done;
      }
      __pyx_t_1 = __Pyx_PyObject_GetAttrStr(__pyx_v_entry, __pyx_mstate_global->__pyx_n_u_is_builtin); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 649, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_1);
      __pyx_t_11 = __Pyx_PyObject_IsTrue(__pyx_t_1); if (unlikely((__pyx_t_11 < 0))) __PYX_ERR(0, 649, __pyx_L1_error)
      __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
      __pyx_t_3 = (!__pyx_t_11);
      __pyx_t_2 = __pyx_t_3;
      __pyx_L23_bool_binop_done:;
      if (__pyx_t_2) {
/* … */
      }
```

</details>

L650  🟡  (score=2)
```python
                    return node
```
<details><summary>Show generated C (score=2)</summary>

```c
        __Pyx_XDECREF(__pyx_r);
        __Pyx_INCREF(__pyx_v_node);
        __pyx_r = __pyx_v_node;
        goto __pyx_L0;
```

</details>

L651  ⚪  (score=0)
```python
                # C implementation of a Python builtin method - see if we find further matches
```
L652  🟡  (score=2)
```python
                self_arg = node.self
```
<details><summary>Show generated C (score=2)</summary>

```c
      __pyx_t_1 = __Pyx_PyObject_GetAttrStr(__pyx_v_node, __pyx_mstate_global->__pyx_n_u_self); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 652, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_1);
      __pyx_v_self_arg = __pyx_t_1;
      __pyx_t_1 = 0;
```

</details>

L653  🟠  (score=8)
```python
                arg_list = arg_list[1:]  # drop CloneNode of self argument
```
<details><summary>Show generated C (score=8)</summary>

```c
      __pyx_t_1 = __Pyx_PyObject_GetSlice(__pyx_v_arg_list, 1, 0, NULL, NULL, &__pyx_mstate_global->__pyx_slice[0], 1, 0, 1); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 653, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_1);
      __Pyx_DECREF_SET(__pyx_v_arg_list, __pyx_t_1);
      __pyx_t_1 = 0;
/* … */
  __pyx_mstate_global->__pyx_slice[0] = PySlice_New(__pyx_mstate_global->__pyx_int_1, Py_None, Py_None); if (unlikely(!__pyx_mstate_global->__pyx_slice[0])) __PYX_ERR(0, 653, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_mstate_global->__pyx_slice[0]);
  __Pyx_GIVEREF(__pyx_mstate_global->__pyx_slice[0]);
```

</details>

L654  ⚪  (score=0)
```python
            else:
```
L655  🟡  (score=2)
```python
                return node
```
<details><summary>Show generated C (score=2)</summary>

```c
    /*else*/ {
      __Pyx_XDECREF(__pyx_r);
      __Pyx_INCREF(__pyx_v_node);
      __pyx_r = __pyx_v_node;
      goto __pyx_L0;
    }
    __pyx_L19:;
```

</details>

L656  🟡  (score=2)
```python
            obj_type = self_arg.type
```
<details><summary>Show generated C (score=2)</summary>

```c
    __pyx_t_1 = __Pyx_PyObject_GetAttrStr(__pyx_v_self_arg, __pyx_mstate_global->__pyx_n_u_type); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 656, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_1);
    __pyx_v_obj_type = __pyx_t_1;
    __pyx_t_1 = 0;
```

</details>

L657  ⚪  (score=0)
```python
            is_unbound_method = False
```
<details><summary>Show generated C (score=0)</summary>

```c
    __pyx_v_is_unbound_method = 0;
```

</details>

L658  🟠  (score=5)
```python
            if obj_type.is_builtin_type:
```
<details><summary>Show generated C (score=5)</summary>

```c
    __pyx_t_1 = __Pyx_PyObject_GetAttrStr(__pyx_v_obj_type, __pyx_mstate_global->__pyx_n_u_is_builtin_type); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 658, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_1);
    __pyx_t_2 = __Pyx_PyObject_IsTrue(__pyx_t_1); if (unlikely((__pyx_t_2 < 0))) __PYX_ERR(0, 658, __pyx_L1_error)
    __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
    if (__pyx_t_2) {
/* … */
      goto __pyx_L25;
    }
```

</details>

L659  🔴  (score=24)
```python
                if obj_type is Builtin.type_type and self_arg.is_name and arg_list and arg_list[0].type.is_pyobject:
```
<details><summary>Show generated C (score=24)</summary>

```c
      __Pyx_GetModuleGlobalName(__pyx_t_1, __pyx_mstate_global->__pyx_n_u_Builtin); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 659, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_1);
      __pyx_t_6 = __Pyx_PyObject_GetAttrStr(__pyx_t_1, __pyx_mstate_global->__pyx_n_u_type_type); if (unlikely(!__pyx_t_6)) __PYX_ERR(0, 659, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_6);
      __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
      __pyx_t_3 = (__pyx_v_obj_type == __pyx_t_6);
      __Pyx_DECREF(__pyx_t_6); __pyx_t_6 = 0;
      if (__pyx_t_3) {
      } else {
        __pyx_t_2 = __pyx_t_3;
        goto __pyx_L27_bool_binop_done;
      }
      __pyx_t_6 = __Pyx_PyObject_GetAttrStr(__pyx_v_self_arg, __pyx_mstate_global->__pyx_n_u_is_name); if (unlikely(!__pyx_t_6)) __PYX_ERR(0, 659, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_6);
      __pyx_t_3 = __Pyx_PyObject_IsTrue(__pyx_t_6); if (unlikely((__pyx_t_3 < 0))) __PYX_ERR(0, 659, __pyx_L1_error)
      __Pyx_DECREF(__pyx_t_6); __pyx_t_6 = 0;
      if (__pyx_t_3) {
      } else {
        __pyx_t_2 = __pyx_t_3;
        goto __pyx_L27_bool_binop_done;
      }
      __pyx_t_3 = __Pyx_PyObject_IsTrue(__pyx_v_arg_list); if (unlikely((__pyx_t_3 < 0))) __PYX_ERR(0, 659, __pyx_L1_error)
      if (__pyx_t_3) {
      } else {
        __pyx_t_2 = __pyx_t_3;
        goto __pyx_L27_bool_binop_done;
      }
      __pyx_t_6 = __Pyx_GetItemInt(__pyx_v_arg_list, 0, long, 1, __Pyx_PyLong_From_long, 0, 0, 1, 1, __Pyx_ReferenceSharing_FunctionArgument); if (unlikely(!__pyx_t_6)) __PYX_ERR(0, 659, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_6);
      __pyx_t_1 = __Pyx_PyObject_GetAttrStr(__pyx_t_6, __pyx_mstate_global->__pyx_n_u_type); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 659, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_1);
      __Pyx_DECREF(__pyx_t_6); __pyx_t_6 = 0;
      __pyx_t_6 = __Pyx_PyObject_GetAttrStr(__pyx_t_1, __pyx_mstate_global->__pyx_n_u_is_pyobject); if (unlikely(!__pyx_t_6)) __PYX_ERR(0, 659, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_6);
      __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
      __pyx_t_3 = __Pyx_PyObject_IsTrue(__pyx_t_6); if (unlikely((__pyx_t_3 < 0))) __PYX_ERR(0, 659, __pyx_L1_error)
      __Pyx_DECREF(__pyx_t_6); __pyx_t_6 = 0;
      __pyx_t_2 = __pyx_t_3;
      __pyx_L27_bool_binop_done:;
      if (__pyx_t_2) {
/* … */
        goto __pyx_L26;
      }
```

</details>

L660  ⚪  (score=0)
```python
                    # calling an unbound method like 'list.append(L,x)'
```
L661  ⚪  (score=0)
```python
                    # (ignoring 'type.mro()' here ...)
```
L662  🟡  (score=2)
```python
                    type_name = self_arg.name
```
<details><summary>Show generated C (score=2)</summary>

```c
        __pyx_t_6 = __Pyx_PyObject_GetAttrStr(__pyx_v_self_arg, __pyx_mstate_global->__pyx_n_u_name_2); if (unlikely(!__pyx_t_6)) __PYX_ERR(0, 662, __pyx_L1_error)
        __Pyx_GOTREF(__pyx_t_6);
        __pyx_v_type_name = __pyx_t_6;
        __pyx_t_6 = 0;
```

</details>

L663  🟡  (score=2)
```python
                    self_arg = None
```
<details><summary>Show generated C (score=2)</summary>

```c
        __Pyx_INCREF(Py_None);
        __Pyx_DECREF_SET(__pyx_v_self_arg, Py_None);
```

</details>

L664  ⚪  (score=0)
```python
                    is_unbound_method = True
```
<details><summary>Show generated C (score=0)</summary>

```c
        __pyx_v_is_unbound_method = 1;
```

</details>

L665  ⚪  (score=0)
```python
                else:
```
L666  🟡  (score=2)
```python
                    type_name = obj_type.name
```
<details><summary>Show generated C (score=2)</summary>

```c
      /*else*/ {
        __pyx_t_6 = __Pyx_PyObject_GetAttrStr(__pyx_v_obj_type, __pyx_mstate_global->__pyx_n_u_name_2); if (unlikely(!__pyx_t_6)) __PYX_ERR(0, 666, __pyx_L1_error)
        __Pyx_GOTREF(__pyx_t_6);
        __pyx_v_type_name = __pyx_t_6;
        __pyx_t_6 = 0;
      }
      __pyx_L26:;
```

</details>

L667  🟡  (score=2)
```python
                if type_name == 'str':
```
<details><summary>Show generated C (score=2)</summary>

```c
      __pyx_t_2 = (__Pyx_PyUnicode_Equals(__pyx_v_type_name, __pyx_mstate_global->__pyx_n_u_str, Py_EQ)); if (unlikely((__pyx_t_2 < 0))) __PYX_ERR(0, 667, __pyx_L1_error)
      if (__pyx_t_2) {
/* … */
      }
```

</details>

L668  ⚪  (score=0)
```python
                    # We traditionally used the type name 'unicode' for 'str' dispatch methods.
```
L669  🟡  (score=2)
```python
                    type_name = 'unicode'
```
<details><summary>Show generated C (score=2)</summary>

```c
        __Pyx_INCREF(__pyx_mstate_global->__pyx_n_u_unicode);
        __Pyx_DECREF_SET(__pyx_v_type_name, __pyx_mstate_global->__pyx_n_u_unicode);
```

</details>

L670  ⚪  (score=0)
```python
            else:
```
L671  🟡  (score=1)
```python
                type_name = "object"  # safety measure
```
<details><summary>Show generated C (score=1)</summary>

```c
    /*else*/ {
      __Pyx_INCREF(__pyx_mstate_global->__pyx_n_u_object);
      __pyx_v_type_name = __pyx_mstate_global->__pyx_n_u_object;
    }
    __pyx_L25:;
```

</details>

L672  🟡  (score=2)
```python
            return self._dispatch_to_method_handler(
```
<details><summary>Show generated C (score=2)</summary>

```c
    __Pyx_XDECREF(__pyx_r);
/* … */
    __pyx_t_1 = ((struct __pyx_vtabstruct_6Cython_8Compiler_7Visitor_MethodDispatcherTransform *)__pyx_v_self->__pyx_base.__pyx_base.__pyx_base.__pyx_base.__pyx_vtab)->_dispatch_to_method_handler(__pyx_v_self, __pyx_v_attr_name, __pyx_v_self_arg, __pyx_t_6, __pyx_v_type_name, __pyx_v_node, __pyx_v_function, __pyx_v_arg_list, __pyx_v_kwargs); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 672, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_1);
    __Pyx_DECREF(__pyx_t_6); __pyx_t_6 = 0;
    __pyx_r = __pyx_t_1;
    __pyx_t_1 = 0;
    goto __pyx_L0;
```

</details>

L673  🟡  (score=2)
```python
                attr_name, self_arg, is_unbound_method, type_name,
```
<details><summary>Show generated C (score=2)</summary>

```c
    __pyx_t_6 = __Pyx_PyBool_FromLong(__pyx_v_is_unbound_method); if (unlikely(!__pyx_t_6)) __PYX_ERR(0, 673, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_6);
```

</details>

L674  ⚪  (score=0)
```python
                node, function, arg_list, kwargs)
```
L675  ⚪  (score=0)
```python
        else:
```
L676  🟡  (score=2)
```python
            return node
```
<details><summary>Show generated C (score=2)</summary>

```c
  /*else*/ {
    __Pyx_XDECREF(__pyx_r);
    __Pyx_INCREF(__pyx_v_node);
    __pyx_r = __pyx_v_node;
    goto __pyx_L0;
  }
```

</details>

L677  ⚪  (score=0)
```python
```
L678  🟠  (score=9)
```python
    def _dispatch_to_method_handler(self, attr_name, self_arg,
```
<details><summary>Show generated C (score=9)</summary>

```c
static PyObject *__pyx_f_6Cython_8Compiler_7Visitor_25MethodDispatcherTransform__dispatch_to_method_handler(struct __pyx_obj_6Cython_8Compiler_7Visitor_MethodDispatcherTransform *__pyx_v_self, PyObject *__pyx_v_attr_name, PyObject *__pyx_v_self_arg, PyObject *__pyx_v_is_unbound_method, PyObject *__pyx_v_type_name, PyObject *__pyx_v_node, PyObject *__pyx_v_function, PyObject *__pyx_v_arg_list, PyObject *__pyx_v_kwargs) {
  PyObject *__pyx_v_method_handler = NULL;
  PyObject *__pyx_v_result = NULL;
  PyObject *__pyx_r = NULL;
  __Pyx_INCREF(__pyx_v_arg_list);
/* … */
  /* function exit code */
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_t_1);
  __Pyx_XDECREF(__pyx_t_2);
  __Pyx_XDECREF(__pyx_t_4);
  __Pyx_AddTraceback("Cython.Compiler.Visitor.MethodDispatcherTransform._dispatch_to_method_handler", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_r = 0;
  __pyx_L0:;
  __Pyx_XDECREF(__pyx_v_method_handler);
  __Pyx_XDECREF(__pyx_v_result);
  __Pyx_XDECREF(__pyx_v_arg_list);
  __Pyx_XGIVEREF(__pyx_r);
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}
```

</details>

L679  ⚪  (score=0)
```python
                                    is_unbound_method, type_name,
```
L680  ⚪  (score=0)
```python
                                    node, function, arg_list, kwargs):
```
L681  🟡  (score=1)
```python
        method_handler = self._find_handler(
```
<details><summary>Show generated C (score=1)</summary>

```c
  __pyx_t_2 = ((struct __pyx_vtabstruct_6Cython_8Compiler_7Visitor_MethodDispatcherTransform *)__pyx_v_self->__pyx_base.__pyx_base.__pyx_base.__pyx_base.__pyx_vtab)->_find_handler(__pyx_v_self, __pyx_t_4, __pyx_t_5); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 681, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
  __pyx_v_method_handler = __pyx_t_2;
  __pyx_t_2 = 0;
```

</details>

L682  🔴  (score=18)
```python
            f"method_{type_name}_{attr_name}", kwargs)
```
<details><summary>Show generated C (score=18)</summary>

```c
  __pyx_t_1 = __Pyx_PyObject_FormatSimple(__pyx_v_type_name, __pyx_mstate_global->__pyx_empty_unicode); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 682, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __pyx_t_2 = __Pyx_PyObject_FormatSimple(__pyx_v_attr_name, __pyx_mstate_global->__pyx_empty_unicode); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 682, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __pyx_t_3[0] = __pyx_mstate_global->__pyx_n_u_method;
  __pyx_t_3[1] = __pyx_t_1;
  __pyx_t_3[2] = __pyx_mstate_global->__pyx_n_u__2;
  __pyx_t_3[3] = __pyx_t_2;
  __pyx_t_4 = __Pyx_PyUnicode_Join(__pyx_t_3, 4, 7 + __Pyx_PyUnicode_GET_LENGTH(__pyx_t_1) + 1 + __Pyx_PyUnicode_GET_LENGTH(__pyx_t_2), 127 | __Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_1) | __Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_2));
  if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 682, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_4);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __pyx_t_5 = __Pyx_PyObject_IsTrue(__pyx_v_kwargs); if (unlikely((__pyx_t_5 == (int)-1) && PyErr_Occurred())) __PYX_ERR(0, 682, __pyx_L1_error)
```

</details>

L683  ⚪  (score=0)
```python
        if method_handler is None:
```
<details><summary>Show generated C (score=0)</summary>

```c
  __pyx_t_5 = (__pyx_v_method_handler == Py_None);
  if (__pyx_t_5) {
/* … */
  }
```

</details>

L684  🟠  (score=8)
```python
            if (attr_name in TypeSlots.special_method_names
```
<details><summary>Show generated C (score=8)</summary>

```c
    __Pyx_GetModuleGlobalName(__pyx_t_2, __pyx_mstate_global->__pyx_n_u_TypeSlots); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 684, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_2);
    __pyx_t_4 = __Pyx_PyObject_GetAttrStr(__pyx_t_2, __pyx_mstate_global->__pyx_n_u_special_method_names); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 684, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_4);
    __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
    __pyx_t_6 = (__Pyx_PySequence_ContainsTF(__pyx_v_attr_name, __pyx_t_4, Py_EQ)); if (unlikely((__pyx_t_6 < 0))) __PYX_ERR(0, 684, __pyx_L1_error)
    __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
    if (!__pyx_t_6) {
    } else {
      __pyx_t_5 = __pyx_t_6;
      goto __pyx_L5_bool_binop_done;
    }
/* … */
    if (__pyx_t_5) {
/* … */
    }
```

</details>

L685  🟠  (score=6)
```python
                    or attr_name in ['__new__', '__class__']):
```
<details><summary>Show generated C (score=6)</summary>

```c
    __Pyx_INCREF(__pyx_v_attr_name);
    __pyx_t_4 = __pyx_v_attr_name;
    __pyx_t_7 = (__Pyx_PyUnicode_Equals(__pyx_t_4, __pyx_mstate_global->__pyx_n_u_new, Py_EQ)); if (unlikely((__pyx_t_7 < 0))) __PYX_ERR(0, 685, __pyx_L1_error)
    if (!__pyx_t_7) {
    } else {
      __pyx_t_6 = __pyx_t_7;
      goto __pyx_L7_bool_binop_done;
    }
    __pyx_t_7 = (__Pyx_PyUnicode_Equals(__pyx_t_4, __pyx_mstate_global->__pyx_n_u_class, Py_EQ)); if (unlikely((__pyx_t_7 < 0))) __PYX_ERR(0, 685, __pyx_L1_error)
    __pyx_t_6 = __pyx_t_7;
    __pyx_L7_bool_binop_done:;
    __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
    __pyx_t_7 = __pyx_t_6;
    __pyx_t_5 = __pyx_t_7;
    __pyx_L5_bool_binop_done:;
```

</details>

L686  🟡  (score=2)
```python
                method_handler = self._find_handler(
```
<details><summary>Show generated C (score=2)</summary>

```c
      __pyx_t_4 = ((struct __pyx_vtabstruct_6Cython_8Compiler_7Visitor_MethodDispatcherTransform *)__pyx_v_self->__pyx_base.__pyx_base.__pyx_base.__pyx_base.__pyx_vtab)->_find_handler(__pyx_v_self, __pyx_t_2, __pyx_t_5); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 686, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_4);
      __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
      __Pyx_DECREF_SET(__pyx_v_method_handler, __pyx_t_4);
      __pyx_t_4 = 0;
```

</details>

L687  🟠  (score=7)
```python
                    f"slot{attr_name}", kwargs)
```
<details><summary>Show generated C (score=7)</summary>

```c
      __pyx_t_4 = __Pyx_PyObject_FormatSimple(__pyx_v_attr_name, __pyx_mstate_global->__pyx_empty_unicode); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 687, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_4);
      __pyx_t_2 = __Pyx_PyUnicode_Concat(__pyx_mstate_global->__pyx_n_u_slot, __pyx_t_4); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 687, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_2);
      __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
      __pyx_t_5 = __Pyx_PyObject_IsTrue(__pyx_v_kwargs); if (unlikely((__pyx_t_5 == (int)-1) && PyErr_Occurred())) __PYX_ERR(0, 687, __pyx_L1_error)
```

</details>

L688  ⚪  (score=0)
```python
            if method_handler is None:
```
<details><summary>Show generated C (score=0)</summary>

```c
    __pyx_t_5 = (__pyx_v_method_handler == Py_None);
    if (__pyx_t_5) {
/* … */
    }
```

</details>

L689  🟡  (score=2)
```python
                return self._handle_method(
```
<details><summary>Show generated C (score=2)</summary>

```c
      __Pyx_XDECREF(__pyx_r);
      __pyx_t_2 = ((PyObject *)__pyx_v_self);
      __Pyx_INCREF(__pyx_t_2);
```

</details>

L690  ⚪  (score=0)
```python
                    node, type_name, attr_name, function,
```
L691  🟡  (score=3)
```python
                    arg_list, is_unbound_method, kwargs)
```
<details><summary>Show generated C (score=3)</summary>

```c
      __pyx_t_8 = 0;
      {
        PyObject *__pyx_callargs[8] = {__pyx_t_2, __pyx_v_node, __pyx_v_type_name, __pyx_v_attr_name, __pyx_v_function, __pyx_v_arg_list, __pyx_v_is_unbound_method, __pyx_v_kwargs};
        __pyx_t_4 = __Pyx_PyObject_FastCallMethod((PyObject*)__pyx_mstate_global->__pyx_n_u_handle_method, __pyx_callargs+__pyx_t_8, (8-__pyx_t_8) | (1*__Pyx_PY_VECTORCALL_ARGUMENTS_OFFSET));
        __Pyx_XDECREF(__pyx_t_2); __pyx_t_2 = 0;
        if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 689, __pyx_L1_error)
        __Pyx_GOTREF(__pyx_t_4);
      }
      __pyx_r = __pyx_t_4;
      __pyx_t_4 = 0;
      goto __pyx_L0;
```

</details>

L692  ⚪  (score=0)
```python
        if self_arg is not None:
```
<details><summary>Show generated C (score=0)</summary>

```c
  __pyx_t_5 = (__pyx_v_self_arg != Py_None);
  if (__pyx_t_5) {
/* … */
  }
```

</details>

L693  🔴  (score=21)
```python
            arg_list = [self_arg] + list(arg_list)
```
<details><summary>Show generated C (score=21)</summary>

```c
    __pyx_t_4 = PyList_New(1); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 693, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_4);
    __Pyx_INCREF(__pyx_v_self_arg);
    __Pyx_GIVEREF(__pyx_v_self_arg);
    if (__Pyx_PyList_SET_ITEM(__pyx_t_4, 0, __pyx_v_self_arg) != (0)) __PYX_ERR(0, 693, __pyx_L1_error);
    __pyx_t_2 = PySequence_List(__pyx_v_arg_list); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 693, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_2);
    __pyx_t_1 = PyNumber_Add(__pyx_t_4, __pyx_t_2); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 693, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_1);
    __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
    __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
    __Pyx_DECREF_SET(__pyx_v_arg_list, __pyx_t_1);
    __pyx_t_1 = 0;
```

</details>

L694  🟡  (score=2)
```python
        if kwargs:
```
<details><summary>Show generated C (score=2)</summary>

```c
  __pyx_t_5 = __Pyx_PyObject_IsTrue(__pyx_v_kwargs); if (unlikely((__pyx_t_5 < 0))) __PYX_ERR(0, 694, __pyx_L1_error)
  if (__pyx_t_5) {
/* … */
    goto __pyx_L11;
  }
```

</details>

L695  🟡  (score=1)
```python
            result = method_handler(
```
<details><summary>Show generated C (score=1)</summary>

```c
    __pyx_t_2 = NULL;
    __Pyx_INCREF(__pyx_v_method_handler);
    __pyx_t_4 = __pyx_v_method_handler; 
```

</details>

L696  🔴  (score=14)
```python
                node, function, arg_list, is_unbound_method, kwargs)
```
<details><summary>Show generated C (score=14)</summary>

```c
    __pyx_t_8 = 1;
    #if CYTHON_UNPACK_METHODS
    if (unlikely(PyMethod_Check(__pyx_t_4))) {
      __pyx_t_2 = PyMethod_GET_SELF(__pyx_t_4);
      assert(__pyx_t_2);
      PyObject* __pyx__function = PyMethod_GET_FUNCTION(__pyx_t_4);
      __Pyx_INCREF(__pyx_t_2);
      __Pyx_INCREF(__pyx__function);
      __Pyx_DECREF_SET(__pyx_t_4, __pyx__function);
      __pyx_t_8 = 0;
    }
    #endif
    {
      PyObject *__pyx_callargs[6] = {__pyx_t_2, __pyx_v_node, __pyx_v_function, __pyx_v_arg_list, __pyx_v_is_unbound_method, __pyx_v_kwargs};
      __pyx_t_1 = __Pyx_PyObject_FastCall((PyObject*)__pyx_t_4, __pyx_callargs+__pyx_t_8, (6-__pyx_t_8) | (__pyx_t_8*__Pyx_PY_VECTORCALL_ARGUMENTS_OFFSET));
      __Pyx_XDECREF(__pyx_t_2); __pyx_t_2 = 0;
      __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
      if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 695, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_1);
    }
    __pyx_v_result = __pyx_t_1;
    __pyx_t_1 = 0;
```

</details>

L697  ⚪  (score=0)
```python
        else:
```
L698  🟡  (score=1)
```python
            result = method_handler(
```
<details><summary>Show generated C (score=1)</summary>

```c
  /*else*/ {
    __pyx_t_4 = NULL;
    __Pyx_INCREF(__pyx_v_method_handler);
    __pyx_t_2 = __pyx_v_method_handler; 
```

</details>

L699  🔴  (score=14)
```python
                node, function, arg_list, is_unbound_method)
```
<details><summary>Show generated C (score=14)</summary>

```c
    __pyx_t_8 = 1;
    #if CYTHON_UNPACK_METHODS
    if (unlikely(PyMethod_Check(__pyx_t_2))) {
      __pyx_t_4 = PyMethod_GET_SELF(__pyx_t_2);
      assert(__pyx_t_4);
      PyObject* __pyx__function = PyMethod_GET_FUNCTION(__pyx_t_2);
      __Pyx_INCREF(__pyx_t_4);
      __Pyx_INCREF(__pyx__function);
      __Pyx_DECREF_SET(__pyx_t_2, __pyx__function);
      __pyx_t_8 = 0;
    }
    #endif
    {
      PyObject *__pyx_callargs[5] = {__pyx_t_4, __pyx_v_node, __pyx_v_function, __pyx_v_arg_list, __pyx_v_is_unbound_method};
      __pyx_t_1 = __Pyx_PyObject_FastCall((PyObject*)__pyx_t_2, __pyx_callargs+__pyx_t_8, (5-__pyx_t_8) | (__pyx_t_8*__Pyx_PY_VECTORCALL_ARGUMENTS_OFFSET));
      __Pyx_XDECREF(__pyx_t_4); __pyx_t_4 = 0;
      __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
      if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 698, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_1);
    }
    __pyx_v_result = __pyx_t_1;
    __pyx_t_1 = 0;
  }
  __pyx_L11:;
```

</details>

L700  🟡  (score=2)
```python
        return result
```
<details><summary>Show generated C (score=2)</summary>

```c
  __Pyx_XDECREF(__pyx_r);
  __Pyx_INCREF(__pyx_v_result);
  __pyx_r = __pyx_v_result;
  goto __pyx_L0;
```

</details>

L701  ⚪  (score=0)
```python
```
L702  🔴  (score=49)
```python
    def _handle_function(self, node, function_name, function, arg_list, kwargs):
```
<details><summary>Show generated C (score=49)</summary>

```c
/* Python wrapper */
static PyObject *__pyx_pw_6Cython_8Compiler_7Visitor_25MethodDispatcherTransform_11_handle_function(PyObject *__pyx_v_self, 
#if CYTHON_METH_FASTCALL
PyObject *const *__pyx_args, Py_ssize_t __pyx_nargs, PyObject *__pyx_kwds
#else
PyObject *__pyx_args, PyObject *__pyx_kwds
#endif
); /*proto*/
PyDoc_STRVAR(__pyx_doc_6Cython_8Compiler_7Visitor_25MethodDispatcherTransform_10_handle_function, "File: Cython/Compiler/Visitor.py (starting at line 702)\nFallback handler");
static PyMethodDef __pyx_mdef_6Cython_8Compiler_7Visitor_25MethodDispatcherTransform_11_handle_function = {"_handle_function", (PyCFunction)(void(*)(void))(__Pyx_PyCFunction_FastCallWithKeywords)__pyx_pw_6Cython_8Compiler_7Visitor_25MethodDispatcherTransform_11_handle_function, __Pyx_METH_FASTCALL|METH_KEYWORDS, __pyx_doc_6Cython_8Compiler_7Visitor_25MethodDispatcherTransform_10_handle_function};
static PyObject *__pyx_pw_6Cython_8Compiler_7Visitor_25MethodDispatcherTransform_11_handle_function(PyObject *__pyx_v_self, 
#if CYTHON_METH_FASTCALL
PyObject *const *__pyx_args, Py_ssize_t __pyx_nargs, PyObject *__pyx_kwds
#else
PyObject *__pyx_args, PyObject *__pyx_kwds
#endif
) {
  PyObject *__pyx_v_node = 0;
  CYTHON_UNUSED PyObject *__pyx_v_function_name = 0;
  CYTHON_UNUSED PyObject *__pyx_v_function = 0;
  CYTHON_UNUSED PyObject *__pyx_v_arg_list = 0;
  CYTHON_UNUSED PyObject *__pyx_v_kwargs = 0;
  #if !CYTHON_METH_FASTCALL
  CYTHON_UNUSED Py_ssize_t __pyx_nargs;
  #endif
  CYTHON_UNUSED PyObject *const *__pyx_kwvalues;
  PyObject *__pyx_r = 0;
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("_handle_function (wrapper)", 0);
  #if !CYTHON_METH_FASTCALL
  #if CYTHON_ASSUME_SAFE_SIZE
  __pyx_nargs = PyTuple_GET_SIZE(__pyx_args);
  #else
  __pyx_nargs = PyTuple_Size(__pyx_args); if (unlikely(__pyx_nargs < 0)) return NULL;
  #endif
  #endif
  __pyx_kwvalues = __Pyx_KwValues_FASTCALL(__pyx_args, __pyx_nargs);
  {
    PyObject ** const __pyx_pyargnames[] = {&__pyx_mstate_global->__pyx_n_u_node,&__pyx_mstate_global->__pyx_n_u_function_name,&__pyx_mstate_global->__pyx_n_u_function,&__pyx_mstate_global->__pyx_n_u_arg_list,&__pyx_mstate_global->__pyx_n_u_kwargs,0};
  PyObject* values[5] = {0,0,0,0,0};
    const Py_ssize_t __pyx_kwds_len = (__pyx_kwds) ? __Pyx_NumKwargs_FASTCALL(__pyx_kwds) : 0;
    if (unlikely(__pyx_kwds_len) < 0) __PYX_ERR(0, 702, __pyx_L3_error)
    if (__pyx_kwds_len > 0) {
      switch (__pyx_nargs) {
        case  5:
        values[4] = __Pyx_ArgRef_FASTCALL(__pyx_args, 4);
        if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[4])) __PYX_ERR(0, 702, __pyx_L3_error)
        CYTHON_FALLTHROUGH;
        case  4:
        values[3] = __Pyx_ArgRef_FASTCALL(__pyx_args, 3);
        if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[3])) __PYX_ERR(0, 702, __pyx_L3_error)
        CYTHON_FALLTHROUGH;
        case  3:
        values[2] = __Pyx_ArgRef_FASTCALL(__pyx_args, 2);
        if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[2])) __PYX_ERR(0, 702, __pyx_L3_error)
        CYTHON_FALLTHROUGH;
        case  2:
        values[1] = __Pyx_ArgRef_FASTCALL(__pyx_args, 1);
        if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[1])) __PYX_ERR(0, 702, __pyx_L3_error)
        CYTHON_FALLTHROUGH;
        case  1:
        values[0] = __Pyx_ArgRef_FASTCALL(__pyx_args, 0);
        if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[0])) __PYX_ERR(0, 702, __pyx_L3_error)
        CYTHON_FALLTHROUGH;
        case  0: break;
        default: goto __pyx_L5_argtuple_error;
      }
      const Py_ssize_t kwd_pos_args = __pyx_nargs;
      if (__Pyx_ParseKeywords(__pyx_kwds, __pyx_kwvalues, __pyx_pyargnames, 0, values, kwd_pos_args, __pyx_kwds_len, "_handle_function", 0) < (0)) __PYX_ERR(0, 702, __pyx_L3_error)
      for (Py_ssize_t i = __pyx_nargs; i < 5; i++) {
        if (unlikely(!values[i])) { __Pyx_RaiseArgtupleInvalid("_handle_function", 1, 5, 5, i); __PYX_ERR(0, 702, __pyx_L3_error) }
      }
    } else if (unlikely(__pyx_nargs != 5)) {
      goto __pyx_L5_argtuple_error;
    } else {
      values[0] = __Pyx_ArgRef_FASTCALL(__pyx_args, 0);
      if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[0])) __PYX_ERR(0, 702, __pyx_L3_error)
      values[1] = __Pyx_ArgRef_FASTCALL(__pyx_args, 1);
      if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[1])) __PYX_ERR(0, 702, __pyx_L3_error)
      values[2] = __Pyx_ArgRef_FASTCALL(__pyx_args, 2);
      if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[2])) __PYX_ERR(0, 702, __pyx_L3_error)
      values[3] = __Pyx_ArgRef_FASTCALL(__pyx_args, 3);
      if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[3])) __PYX_ERR(0, 702, __pyx_L3_error)
      values[4] = __Pyx_ArgRef_FASTCALL(__pyx_args, 4);
      if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[4])) __PYX_ERR(0, 702, __pyx_L3_error)
    }
    __pyx_v_node = values[0];
    __pyx_v_function_name = values[1];
    __pyx_v_function = values[2];
    __pyx_v_arg_list = values[3];
    __pyx_v_kwargs = values[4];
  }
  goto __pyx_L6_skip;
  __pyx_L5_argtuple_error:;
  __Pyx_RaiseArgtupleInvalid("_handle_function", 1, 5, 5, __pyx_nargs); __PYX_ERR(0, 702, __pyx_L3_error)
  __pyx_L6_skip:;
  goto __pyx_L4_argument_unpacking_done;
  __pyx_L3_error:;
  for (Py_ssize_t __pyx_temp=0; __pyx_temp < (Py_ssize_t)(sizeof(values)/sizeof(values[0])); ++__pyx_temp) {
    Py_XDECREF(values[__pyx_temp]);
  }
  __Pyx_AddTraceback("Cython.Compiler.Visitor.MethodDispatcherTransform._handle_function", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __Pyx_RefNannyFinishContext();
  return NULL;
  __pyx_L4_argument_unpacking_done:;
  __pyx_r = __pyx_pf_6Cython_8Compiler_7Visitor_25MethodDispatcherTransform_10_handle_function(((struct __pyx_obj_6Cython_8Compiler_7Visitor_MethodDispatcherTransform *)__pyx_v_self), __pyx_v_node, __pyx_v_function_name, __pyx_v_function, __pyx_v_arg_list, __pyx_v_kwargs);
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

static PyObject *__pyx_pf_6Cython_8Compiler_7Visitor_25MethodDispatcherTransform_10_handle_function(CYTHON_UNUSED struct __pyx_obj_6Cython_8Compiler_7Visitor_MethodDispatcherTransform *__pyx_v_self, PyObject *__pyx_v_node, CYTHON_UNUSED PyObject *__pyx_v_function_name, CYTHON_UNUSED PyObject *__pyx_v_function, CYTHON_UNUSED PyObject *__pyx_v_arg_list, CYTHON_UNUSED PyObject *__pyx_v_kwargs) {
  PyObject *__pyx_r = NULL;
/* … */
  /* function exit code */
  __pyx_L0:;
  __Pyx_XGIVEREF(__pyx_r);
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}
/* … */
  __pyx_t_2 = __Pyx_CyFunction_New(&__pyx_mdef_6Cython_8Compiler_7Visitor_25MethodDispatcherTransform_11_handle_function, __Pyx_CYFUNCTION_CCLASS, __pyx_mstate_global->__pyx_n_u_MethodDispatcherTransform__handl, NULL, __pyx_mstate_global->__pyx_n_u_Cython_Compiler_Visitor, __pyx_mstate_global->__pyx_d, ((PyObject *)__pyx_mstate_global->__pyx_codeobj_tab[45])); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 702, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  #if CYTHON_COMPILING_IN_CPYTHON && PY_VERSION_HEX >= 0x030E0000
  PyUnstable_Object_EnableDeferredRefcount(__pyx_t_2);
  #endif
  if (__Pyx_SetItemOnTypeDict(__pyx_mstate_global->__pyx_ptype_6Cython_8Compiler_7Visitor_MethodDispatcherTransform, __pyx_mstate_global->__pyx_n_u_handle_function, __pyx_t_2) < (0)) __PYX_ERR(0, 702, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
```

</details>

L703  ⚪  (score=0)
```python
        """Fallback handler"""
```
L704  🟡  (score=2)
```python
        return node
```
<details><summary>Show generated C (score=2)</summary>

```c
  __Pyx_XDECREF(__pyx_r);
  __Pyx_INCREF(__pyx_v_node);
  __pyx_r = __pyx_v_node;
  goto __pyx_L0;
```

</details>

L705  ⚪  (score=0)
```python
```
L706  🔴  (score=57)
```python
    def _handle_method(self, node, type_name, attr_name, function,
```
<details><summary>Show generated C (score=57)</summary>

```c
/* Python wrapper */
static PyObject *__pyx_pw_6Cython_8Compiler_7Visitor_25MethodDispatcherTransform_13_handle_method(PyObject *__pyx_v_self, 
#if CYTHON_METH_FASTCALL
PyObject *const *__pyx_args, Py_ssize_t __pyx_nargs, PyObject *__pyx_kwds
#else
PyObject *__pyx_args, PyObject *__pyx_kwds
#endif
); /*proto*/
PyDoc_STRVAR(__pyx_doc_6Cython_8Compiler_7Visitor_25MethodDispatcherTransform_12_handle_method, "File: Cython/Compiler/Visitor.py (starting at line 706)\nFallback handler");
static PyMethodDef __pyx_mdef_6Cython_8Compiler_7Visitor_25MethodDispatcherTransform_13_handle_method = {"_handle_method", (PyCFunction)(void(*)(void))(__Pyx_PyCFunction_FastCallWithKeywords)__pyx_pw_6Cython_8Compiler_7Visitor_25MethodDispatcherTransform_13_handle_method, __Pyx_METH_FASTCALL|METH_KEYWORDS, __pyx_doc_6Cython_8Compiler_7Visitor_25MethodDispatcherTransform_12_handle_method};
static PyObject *__pyx_pw_6Cython_8Compiler_7Visitor_25MethodDispatcherTransform_13_handle_method(PyObject *__pyx_v_self, 
#if CYTHON_METH_FASTCALL
PyObject *const *__pyx_args, Py_ssize_t __pyx_nargs, PyObject *__pyx_kwds
#else
PyObject *__pyx_args, PyObject *__pyx_kwds
#endif
) {
  PyObject *__pyx_v_node = 0;
  CYTHON_UNUSED PyObject *__pyx_v_type_name = 0;
  CYTHON_UNUSED PyObject *__pyx_v_attr_name = 0;
  CYTHON_UNUSED PyObject *__pyx_v_function = 0;
  CYTHON_UNUSED PyObject *__pyx_v_arg_list = 0;
  CYTHON_UNUSED PyObject *__pyx_v_is_unbound_method = 0;
  CYTHON_UNUSED PyObject *__pyx_v_kwargs = 0;
  #if !CYTHON_METH_FASTCALL
  CYTHON_UNUSED Py_ssize_t __pyx_nargs;
  #endif
  CYTHON_UNUSED PyObject *const *__pyx_kwvalues;
  PyObject *__pyx_r = 0;
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("_handle_method (wrapper)", 0);
  #if !CYTHON_METH_FASTCALL
  #if CYTHON_ASSUME_SAFE_SIZE
  __pyx_nargs = PyTuple_GET_SIZE(__pyx_args);
  #else
  __pyx_nargs = PyTuple_Size(__pyx_args); if (unlikely(__pyx_nargs < 0)) return NULL;
  #endif
  #endif
  __pyx_kwvalues = __Pyx_KwValues_FASTCALL(__pyx_args, __pyx_nargs);
  {
    PyObject ** const __pyx_pyargnames[] = {&__pyx_mstate_global->__pyx_n_u_node,&__pyx_mstate_global->__pyx_n_u_type_name,&__pyx_mstate_global->__pyx_n_u_attr_name,&__pyx_mstate_global->__pyx_n_u_function,&__pyx_mstate_global->__pyx_n_u_arg_list,&__pyx_mstate_global->__pyx_n_u_is_unbound_method,&__pyx_mstate_global->__pyx_n_u_kwargs,0};
  PyObject* values[7] = {0,0,0,0,0,0,0};
    const Py_ssize_t __pyx_kwds_len = (__pyx_kwds) ? __Pyx_NumKwargs_FASTCALL(__pyx_kwds) : 0;
    if (unlikely(__pyx_kwds_len) < 0) __PYX_ERR(0, 706, __pyx_L3_error)
    if (__pyx_kwds_len > 0) {
      switch (__pyx_nargs) {
        case  7:
        values[6] = __Pyx_ArgRef_FASTCALL(__pyx_args, 6);
        if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[6])) __PYX_ERR(0, 706, __pyx_L3_error)
        CYTHON_FALLTHROUGH;
        case  6:
        values[5] = __Pyx_ArgRef_FASTCALL(__pyx_args, 5);
        if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[5])) __PYX_ERR(0, 706, __pyx_L3_error)
        CYTHON_FALLTHROUGH;
        case  5:
        values[4] = __Pyx_ArgRef_FASTCALL(__pyx_args, 4);
        if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[4])) __PYX_ERR(0, 706, __pyx_L3_error)
        CYTHON_FALLTHROUGH;
        case  4:
        values[3] = __Pyx_ArgRef_FASTCALL(__pyx_args, 3);
        if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[3])) __PYX_ERR(0, 706, __pyx_L3_error)
        CYTHON_FALLTHROUGH;
        case  3:
        values[2] = __Pyx_ArgRef_FASTCALL(__pyx_args, 2);
        if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[2])) __PYX_ERR(0, 706, __pyx_L3_error)
        CYTHON_FALLTHROUGH;
        case  2:
        values[1] = __Pyx_ArgRef_FASTCALL(__pyx_args, 1);
        if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[1])) __PYX_ERR(0, 706, __pyx_L3_error)
        CYTHON_FALLTHROUGH;
        case  1:
        values[0] = __Pyx_ArgRef_FASTCALL(__pyx_args, 0);
        if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[0])) __PYX_ERR(0, 706, __pyx_L3_error)
        CYTHON_FALLTHROUGH;
        case  0: break;
        default: goto __pyx_L5_argtuple_error;
      }
      const Py_ssize_t kwd_pos_args = __pyx_nargs;
      if (__Pyx_ParseKeywords(__pyx_kwds, __pyx_kwvalues, __pyx_pyargnames, 0, values, kwd_pos_args, __pyx_kwds_len, "_handle_method", 0) < (0)) __PYX_ERR(0, 706, __pyx_L3_error)
      for (Py_ssize_t i = __pyx_nargs; i < 7; i++) {
        if (unlikely(!values[i])) { __Pyx_RaiseArgtupleInvalid("_handle_method", 1, 7, 7, i); __PYX_ERR(0, 706, __pyx_L3_error) }
      }
    } else if (unlikely(__pyx_nargs != 7)) {
      goto __pyx_L5_argtuple_error;
    } else {
      values[0] = __Pyx_ArgRef_FASTCALL(__pyx_args, 0);
      if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[0])) __PYX_ERR(0, 706, __pyx_L3_error)
      values[1] = __Pyx_ArgRef_FASTCALL(__pyx_args, 1);
      if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[1])) __PYX_ERR(0, 706, __pyx_L3_error)
      values[2] = __Pyx_ArgRef_FASTCALL(__pyx_args, 2);
      if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[2])) __PYX_ERR(0, 706, __pyx_L3_error)
      values[3] = __Pyx_ArgRef_FASTCALL(__pyx_args, 3);
      if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[3])) __PYX_ERR(0, 706, __pyx_L3_error)
      values[4] = __Pyx_ArgRef_FASTCALL(__pyx_args, 4);
      if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[4])) __PYX_ERR(0, 706, __pyx_L3_error)
      values[5] = __Pyx_ArgRef_FASTCALL(__pyx_args, 5);
      if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[5])) __PYX_ERR(0, 706, __pyx_L3_error)
      values[6] = __Pyx_ArgRef_FASTCALL(__pyx_args, 6);
      if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[6])) __PYX_ERR(0, 706, __pyx_L3_error)
    }
    __pyx_v_node = values[0];
    __pyx_v_type_name = values[1];
    __pyx_v_attr_name = values[2];
    __pyx_v_function = values[3];
    __pyx_v_arg_list = values[4];
    __pyx_v_is_unbound_method = values[5];
    __pyx_v_kwargs = values[6];
  }
  goto __pyx_L6_skip;
  __pyx_L5_argtuple_error:;
  __Pyx_RaiseArgtupleInvalid("_handle_method", 1, 7, 7, __pyx_nargs); __PYX_ERR(0, 706, __pyx_L3_error)
  __pyx_L6_skip:;
  goto __pyx_L4_argument_unpacking_done;
  __pyx_L3_error:;
  for (Py_ssize_t __pyx_temp=0; __pyx_temp < (Py_ssize_t)(sizeof(values)/sizeof(values[0])); ++__pyx_temp) {
    Py_XDECREF(values[__pyx_temp]);
  }
  __Pyx_AddTraceback("Cython.Compiler.Visitor.MethodDispatcherTransform._handle_method", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __Pyx_RefNannyFinishContext();
  return NULL;
  __pyx_L4_argument_unpacking_done:;
  __pyx_r = __pyx_pf_6Cython_8Compiler_7Visitor_25MethodDispatcherTransform_12_handle_method(((struct __pyx_obj_6Cython_8Compiler_7Visitor_MethodDispatcherTransform *)__pyx_v_self), __pyx_v_node, __pyx_v_type_name, __pyx_v_attr_name, __pyx_v_function, __pyx_v_arg_list, __pyx_v_is_unbound_method, __pyx_v_kwargs);
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

static PyObject *__pyx_pf_6Cython_8Compiler_7Visitor_25MethodDispatcherTransform_12_handle_method(CYTHON_UNUSED struct __pyx_obj_6Cython_8Compiler_7Visitor_MethodDispatcherTransform *__pyx_v_self, PyObject *__pyx_v_node, CYTHON_UNUSED PyObject *__pyx_v_type_name, CYTHON_UNUSED PyObject *__pyx_v_attr_name, CYTHON_UNUSED PyObject *__pyx_v_function, CYTHON_UNUSED PyObject *__pyx_v_arg_list, CYTHON_UNUSED PyObject *__pyx_v_is_unbound_method, CYTHON_UNUSED PyObject *__pyx_v_kwargs) {
  PyObject *__pyx_r = NULL;
/* … */
  /* function exit code */
  __pyx_L0:;
  __Pyx_XGIVEREF(__pyx_r);
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}
/* … */
  __pyx_t_2 = __Pyx_CyFunction_New(&__pyx_mdef_6Cython_8Compiler_7Visitor_25MethodDispatcherTransform_13_handle_method, __Pyx_CYFUNCTION_CCLASS, __pyx_mstate_global->__pyx_n_u_MethodDispatcherTransform__handl_2, NULL, __pyx_mstate_global->__pyx_n_u_Cython_Compiler_Visitor, __pyx_mstate_global->__pyx_d, ((PyObject *)__pyx_mstate_global->__pyx_codeobj_tab[46])); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 706, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  #if CYTHON_COMPILING_IN_CPYTHON && PY_VERSION_HEX >= 0x030E0000
  PyUnstable_Object_EnableDeferredRefcount(__pyx_t_2);
  #endif
  if (__Pyx_SetItemOnTypeDict(__pyx_mstate_global->__pyx_ptype_6Cython_8Compiler_7Visitor_MethodDispatcherTransform, __pyx_mstate_global->__pyx_n_u_handle_method, __pyx_t_2) < (0)) __PYX_ERR(0, 706, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
```

</details>

L707  ⚪  (score=0)
```python
                       arg_list, is_unbound_method, kwargs):
```
L708  ⚪  (score=0)
```python
        """Fallback handler"""
```
L709  🟡  (score=2)
```python
        return node
```
<details><summary>Show generated C (score=2)</summary>

```c
  __Pyx_XDECREF(__pyx_r);
  __Pyx_INCREF(__pyx_v_node);
  __pyx_r = __pyx_v_node;
  goto __pyx_L0;
```

</details>

L710  ⚪  (score=0)
```python
```
L711  ⚪  (score=0)
```python
```
L712  ⚪  (score=0)
```python
class RecursiveNodeReplacer(VisitorTransform):
```
<details><summary>Show generated C (score=0)</summary>

```c
struct __pyx_vtabstruct_6Cython_8Compiler_7Visitor_RecursiveNodeReplacer {
  struct __pyx_vtabstruct_6Cython_8Compiler_7Visitor_VisitorTransform __pyx_base;
};
static struct __pyx_vtabstruct_6Cython_8Compiler_7Visitor_RecursiveNodeReplacer *__pyx_vtabptr_6Cython_8Compiler_7Visitor_RecursiveNodeReplacer;

```

</details>

L713  ⚪  (score=0)
```python
    """
```
L714  ⚪  (score=0)
```python
    Recursively replace all occurrences of a node in a subtree by
```
L715  ⚪  (score=0)
```python
    another node.
```
L716  ⚪  (score=0)
```python
    """
```
L717  🔴  (score=33)
```python
    def __init__(self, orig_node, new_node):
```
<details><summary>Show generated C (score=33)</summary>

```c
/* Python wrapper */
static int __pyx_pw_6Cython_8Compiler_7Visitor_21RecursiveNodeReplacer_1__init__(PyObject *__pyx_v_self, PyObject *__pyx_args, PyObject *__pyx_kwds); /*proto*/
PyDoc_STRVAR(__pyx_doc_6Cython_8Compiler_7Visitor_21RecursiveNodeReplacer___init__, "File: Cython/Compiler/Visitor.py (starting at line 717)");
#if CYTHON_UPDATE_DESCRIPTOR_DOC
struct wrapperbase __pyx_wrapperbase_6Cython_8Compiler_7Visitor_21RecursiveNodeReplacer___init__;
#endif
static int __pyx_pw_6Cython_8Compiler_7Visitor_21RecursiveNodeReplacer_1__init__(PyObject *__pyx_v_self, PyObject *__pyx_args, PyObject *__pyx_kwds) {
  PyObject *__pyx_v_orig_node = 0;
  PyObject *__pyx_v_new_node = 0;
  CYTHON_UNUSED Py_ssize_t __pyx_nargs;
  CYTHON_UNUSED PyObject *const *__pyx_kwvalues;
  int __pyx_r;
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("__init__ (wrapper)", 0);
  #if CYTHON_ASSUME_SAFE_SIZE
  __pyx_nargs = PyTuple_GET_SIZE(__pyx_args);
  #else
  __pyx_nargs = PyTuple_Size(__pyx_args); if (unlikely(__pyx_nargs < 0)) return -1;
  #endif
  __pyx_kwvalues = __Pyx_KwValues_VARARGS(__pyx_args, __pyx_nargs);
  {
    PyObject ** const __pyx_pyargnames[] = {&__pyx_mstate_global->__pyx_n_u_orig_node,&__pyx_mstate_global->__pyx_n_u_new_node,0};
  PyObject* values[2] = {0,0};
    const Py_ssize_t __pyx_kwds_len = (__pyx_kwds) ? __Pyx_NumKwargs_VARARGS(__pyx_kwds) : 0;
    if (unlikely(__pyx_kwds_len) < 0) __PYX_ERR(0, 717, __pyx_L3_error)
    if (__pyx_kwds_len > 0) {
      switch (__pyx_nargs) {
        case  2:
        values[1] = __Pyx_ArgRef_VARARGS(__pyx_args, 1);
        if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[1])) __PYX_ERR(0, 717, __pyx_L3_error)
        CYTHON_FALLTHROUGH;
        case  1:
        values[0] = __Pyx_ArgRef_VARARGS(__pyx_args, 0);
        if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[0])) __PYX_ERR(0, 717, __pyx_L3_error)
        CYTHON_FALLTHROUGH;
        case  0: break;
        default: goto __pyx_L5_argtuple_error;
      }
      const Py_ssize_t kwd_pos_args = __pyx_nargs;
      if (__Pyx_ParseKeywords(__pyx_kwds, __pyx_kwvalues, __pyx_pyargnames, 0, values, kwd_pos_args, __pyx_kwds_len, "__init__", 0) < (0)) __PYX_ERR(0, 717, __pyx_L3_error)
      for (Py_ssize_t i = __pyx_nargs; i < 2; i++) {
        if (unlikely(!values[i])) { __Pyx_RaiseArgtupleInvalid("__init__", 1, 2, 2, i); __PYX_ERR(0, 717, __pyx_L3_error) }
      }
    } else if (unlikely(__pyx_nargs != 2)) {
      goto __pyx_L5_argtuple_error;
    } else {
      values[0] = __Pyx_ArgRef_VARARGS(__pyx_args, 0);
      if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[0])) __PYX_ERR(0, 717, __pyx_L3_error)
      values[1] = __Pyx_ArgRef_VARARGS(__pyx_args, 1);
      if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[1])) __PYX_ERR(0, 717, __pyx_L3_error)
    }
    __pyx_v_orig_node = values[0];
    __pyx_v_new_node = values[1];
  }
  goto __pyx_L6_skip;
  __pyx_L5_argtuple_error:;
  __Pyx_RaiseArgtupleInvalid("__init__", 1, 2, 2, __pyx_nargs); __PYX_ERR(0, 717, __pyx_L3_error)
  __pyx_L6_skip:;
  goto __pyx_L4_argument_unpacking_done;
  __pyx_L3_error:;
  for (Py_ssize_t __pyx_temp=0; __pyx_temp < (Py_ssize_t)(sizeof(values)/sizeof(values[0])); ++__pyx_temp) {
    Py_XDECREF(values[__pyx_temp]);
  }
  __Pyx_AddTraceback("Cython.Compiler.Visitor.RecursiveNodeReplacer.__init__", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __Pyx_RefNannyFinishContext();
  return -1;
  __pyx_L4_argument_unpacking_done:;
  __pyx_r = __pyx_pf_6Cython_8Compiler_7Visitor_21RecursiveNodeReplacer___init__(((struct __pyx_obj_6Cython_8Compiler_7Visitor_RecursiveNodeReplacer *)__pyx_v_self), __pyx_v_orig_node, __pyx_v_new_node);
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

static int __pyx_pf_6Cython_8Compiler_7Visitor_21RecursiveNodeReplacer___init__(struct __pyx_obj_6Cython_8Compiler_7Visitor_RecursiveNodeReplacer *__pyx_v_self, PyObject *__pyx_v_orig_node, PyObject *__pyx_v_new_node) {
  int __pyx_r;
/* … */
  /* function exit code */
  __pyx_r = 0;
  goto __pyx_L0;
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_t_1);
  __Pyx_XDECREF(__pyx_t_2);
  __Pyx_XDECREF(__pyx_t_3);
  __Pyx_XDECREF(__pyx_t_4);
  __Pyx_AddTraceback("Cython.Compiler.Visitor.RecursiveNodeReplacer.__init__", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_r = -1;
  __pyx_L0:;
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}
```

</details>

L718  🟠  (score=9)
```python
        super().__init__()
```
<details><summary>Show generated C (score=9)</summary>

```c
  __pyx_t_4 = NULL;
  __pyx_t_5 = 1;
  {
    PyObject *__pyx_callargs[3] = {__pyx_t_4, ((PyObject *)__pyx_mstate_global->__pyx_ptype_6Cython_8Compiler_7Visitor_RecursiveNodeReplacer), ((PyObject *)__pyx_v_self)};
    __pyx_t_3 = __Pyx_PyObject_FastCall((PyObject*)__pyx_builtin_super, __pyx_callargs+__pyx_t_5, (3-__pyx_t_5) | (__pyx_t_5*__Pyx_PY_VECTORCALL_ARGUMENTS_OFFSET));
    __Pyx_XDECREF(__pyx_t_4); __pyx_t_4 = 0;
    if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 718, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_3);
  }
  __pyx_t_2 = __pyx_t_3;
  __Pyx_INCREF(__pyx_t_2);
  __pyx_t_5 = 0;
  {
    PyObject *__pyx_callargs[2] = {__pyx_t_2, NULL};
    __pyx_t_1 = __Pyx_PyObject_FastCallMethod((PyObject*)__pyx_mstate_global->__pyx_n_u_init, __pyx_callargs+__pyx_t_5, (1-__pyx_t_5) | (1*__Pyx_PY_VECTORCALL_ARGUMENTS_OFFSET));
    __Pyx_XDECREF(__pyx_t_2); __pyx_t_2 = 0;
    __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
    if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 718, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_1);
  }
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
```

</details>

L719  🟡  (score=4)
```python
        self.orig_node, self.new_node = orig_node, new_node
```
<details><summary>Show generated C (score=4)</summary>

```c
  __pyx_t_1 = __pyx_v_orig_node;
  __Pyx_INCREF(__pyx_t_1);
  __pyx_t_3 = __pyx_v_new_node;
  __Pyx_INCREF(__pyx_t_3);
  __Pyx_GIVEREF(__pyx_t_1);
  __Pyx_GOTREF(__pyx_v_self->orig_node);
  __Pyx_DECREF(__pyx_v_self->orig_node);
  __pyx_v_self->orig_node = __pyx_t_1;
  __pyx_t_1 = 0;
  __Pyx_GIVEREF(__pyx_t_3);
  __Pyx_GOTREF(__pyx_v_self->new_node);
  __Pyx_DECREF(__pyx_v_self->new_node);
  __pyx_v_self->new_node = __pyx_t_3;
  __pyx_t_3 = 0;
```

</details>

L720  ⚪  (score=0)
```python
```
L721  🔴  (score=36)
```python
    def visit_CloneNode(self, node):
```
<details><summary>Show generated C (score=36)</summary>

```c
/* Python wrapper */
static PyObject *__pyx_pw_6Cython_8Compiler_7Visitor_21RecursiveNodeReplacer_3visit_CloneNode(PyObject *__pyx_v_self, 
#if CYTHON_METH_FASTCALL
PyObject *const *__pyx_args, Py_ssize_t __pyx_nargs, PyObject *__pyx_kwds
#else
PyObject *__pyx_args, PyObject *__pyx_kwds
#endif
); /*proto*/
PyDoc_STRVAR(__pyx_doc_6Cython_8Compiler_7Visitor_21RecursiveNodeReplacer_2visit_CloneNode, "File: Cython/Compiler/Visitor.py (starting at line 721)");
static PyMethodDef __pyx_mdef_6Cython_8Compiler_7Visitor_21RecursiveNodeReplacer_3visit_CloneNode = {"visit_CloneNode", (PyCFunction)(void(*)(void))(__Pyx_PyCFunction_FastCallWithKeywords)__pyx_pw_6Cython_8Compiler_7Visitor_21RecursiveNodeReplacer_3visit_CloneNode, __Pyx_METH_FASTCALL|METH_KEYWORDS, __pyx_doc_6Cython_8Compiler_7Visitor_21RecursiveNodeReplacer_2visit_CloneNode};
static PyObject *__pyx_pw_6Cython_8Compiler_7Visitor_21RecursiveNodeReplacer_3visit_CloneNode(PyObject *__pyx_v_self, 
#if CYTHON_METH_FASTCALL
PyObject *const *__pyx_args, Py_ssize_t __pyx_nargs, PyObject *__pyx_kwds
#else
PyObject *__pyx_args, PyObject *__pyx_kwds
#endif
) {
  PyObject *__pyx_v_node = 0;
  #if !CYTHON_METH_FASTCALL
  CYTHON_UNUSED Py_ssize_t __pyx_nargs;
  #endif
  CYTHON_UNUSED PyObject *const *__pyx_kwvalues;
  PyObject *__pyx_r = 0;
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("visit_CloneNode (wrapper)", 0);
  #if !CYTHON_METH_FASTCALL
  #if CYTHON_ASSUME_SAFE_SIZE
  __pyx_nargs = PyTuple_GET_SIZE(__pyx_args);
  #else
  __pyx_nargs = PyTuple_Size(__pyx_args); if (unlikely(__pyx_nargs < 0)) return NULL;
  #endif
  #endif
  __pyx_kwvalues = __Pyx_KwValues_FASTCALL(__pyx_args, __pyx_nargs);
  {
    PyObject ** const __pyx_pyargnames[] = {&__pyx_mstate_global->__pyx_n_u_node,0};
  PyObject* values[1] = {0};
    const Py_ssize_t __pyx_kwds_len = (__pyx_kwds) ? __Pyx_NumKwargs_FASTCALL(__pyx_kwds) : 0;
    if (unlikely(__pyx_kwds_len) < 0) __PYX_ERR(0, 721, __pyx_L3_error)
    if (__pyx_kwds_len > 0) {
      switch (__pyx_nargs) {
        case  1:
        values[0] = __Pyx_ArgRef_FASTCALL(__pyx_args, 0);
        if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[0])) __PYX_ERR(0, 721, __pyx_L3_error)
        CYTHON_FALLTHROUGH;
        case  0: break;
        default: goto __pyx_L5_argtuple_error;
      }
      const Py_ssize_t kwd_pos_args = __pyx_nargs;
      if (__Pyx_ParseKeywords(__pyx_kwds, __pyx_kwvalues, __pyx_pyargnames, 0, values, kwd_pos_args, __pyx_kwds_len, "visit_CloneNode", 0) < (0)) __PYX_ERR(0, 721, __pyx_L3_error)
      for (Py_ssize_t i = __pyx_nargs; i < 1; i++) {
        if (unlikely(!values[i])) { __Pyx_RaiseArgtupleInvalid("visit_CloneNode", 1, 1, 1, i); __PYX_ERR(0, 721, __pyx_L3_error) }
      }
    } else if (unlikely(__pyx_nargs != 1)) {
      goto __pyx_L5_argtuple_error;
    } else {
      values[0] = __Pyx_ArgRef_FASTCALL(__pyx_args, 0);
      if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[0])) __PYX_ERR(0, 721, __pyx_L3_error)
    }
    __pyx_v_node = values[0];
  }
  goto __pyx_L6_skip;
  __pyx_L5_argtuple_error:;
  __Pyx_RaiseArgtupleInvalid("visit_CloneNode", 1, 1, 1, __pyx_nargs); __PYX_ERR(0, 721, __pyx_L3_error)
  __pyx_L6_skip:;
  goto __pyx_L4_argument_unpacking_done;
  __pyx_L3_error:;
  for (Py_ssize_t __pyx_temp=0; __pyx_temp < (Py_ssize_t)(sizeof(values)/sizeof(values[0])); ++__pyx_temp) {
    Py_XDECREF(values[__pyx_temp]);
  }
  __Pyx_AddTraceback("Cython.Compiler.Visitor.RecursiveNodeReplacer.visit_CloneNode", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __Pyx_RefNannyFinishContext();
  return NULL;
  __pyx_L4_argument_unpacking_done:;
  __pyx_r = __pyx_pf_6Cython_8Compiler_7Visitor_21RecursiveNodeReplacer_2visit_CloneNode(((struct __pyx_obj_6Cython_8Compiler_7Visitor_RecursiveNodeReplacer *)__pyx_v_self), __pyx_v_node);
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

static PyObject *__pyx_pf_6Cython_8Compiler_7Visitor_21RecursiveNodeReplacer_2visit_CloneNode(struct __pyx_obj_6Cython_8Compiler_7Visitor_RecursiveNodeReplacer *__pyx_v_self, PyObject *__pyx_v_node) {
  PyObject *__pyx_r = NULL;
/* … */
  /* function exit code */
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_t_2);
  __Pyx_AddTraceback("Cython.Compiler.Visitor.RecursiveNodeReplacer.visit_CloneNode", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_r = NULL;
  __pyx_L0:;
  __Pyx_XGIVEREF(__pyx_r);
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}
/* … */
  __pyx_t_2 = __Pyx_CyFunction_New(&__pyx_mdef_6Cython_8Compiler_7Visitor_21RecursiveNodeReplacer_3visit_CloneNode, __Pyx_CYFUNCTION_CCLASS, __pyx_mstate_global->__pyx_n_u_RecursiveNodeReplacer_visit_Clon, NULL, __pyx_mstate_global->__pyx_n_u_Cython_Compiler_Visitor, __pyx_mstate_global->__pyx_d, ((PyObject *)__pyx_mstate_global->__pyx_codeobj_tab[49])); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 721, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  #if CYTHON_COMPILING_IN_CPYTHON && PY_VERSION_HEX >= 0x030E0000
  PyUnstable_Object_EnableDeferredRefcount(__pyx_t_2);
  #endif
  if (__Pyx_SetItemOnTypeDict(__pyx_mstate_global->__pyx_ptype_6Cython_8Compiler_7Visitor_RecursiveNodeReplacer, __pyx_mstate_global->__pyx_n_u_visit_CloneNode, __pyx_t_2) < (0)) __PYX_ERR(0, 721, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
```

</details>

L722  ⚪  (score=0)
```python
        if node is self.orig_node:
```
<details><summary>Show generated C (score=0)</summary>

```c
  __pyx_t_1 = (__pyx_v_node == __pyx_v_self->orig_node);
  if (__pyx_t_1) {
/* … */
  }
```

</details>

L723  🟡  (score=2)
```python
            return self.new_node
```
<details><summary>Show generated C (score=2)</summary>

```c
    __Pyx_XDECREF(__pyx_r);
    __Pyx_INCREF(__pyx_v_self->new_node);
    __pyx_r = __pyx_v_self->new_node;
    goto __pyx_L0;
```

</details>

L724  🟡  (score=3)
```python
        if node.arg is self.orig_node:
```
<details><summary>Show generated C (score=3)</summary>

```c
  __pyx_t_2 = __Pyx_PyObject_GetAttrStr(__pyx_v_node, __pyx_mstate_global->__pyx_n_u_arg); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 724, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __pyx_t_1 = (__pyx_t_2 == __pyx_v_self->orig_node);
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  if (__pyx_t_1) {
/* … */
  }
```

</details>

L725  🟡  (score=4)
```python
            node.arg = self.new_node
```
<details><summary>Show generated C (score=4)</summary>

```c
    __pyx_t_2 = __pyx_v_self->new_node;
    __Pyx_INCREF(__pyx_t_2);
    if (__Pyx_PyObject_SetAttrStr(__pyx_v_node, __pyx_mstate_global->__pyx_n_u_arg, __pyx_t_2) < (0)) __PYX_ERR(0, 725, __pyx_L1_error)
    __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
```

</details>

L726  🟡  (score=2)
```python
        return node
```
<details><summary>Show generated C (score=2)</summary>

```c
  __Pyx_XDECREF(__pyx_r);
  __Pyx_INCREF(__pyx_v_node);
  __pyx_r = __pyx_v_node;
  goto __pyx_L0;
```

</details>

L727  ⚪  (score=0)
```python
```
L728  🔴  (score=36)
```python
    def visit_Node(self, node):
```
<details><summary>Show generated C (score=36)</summary>

```c
/* Python wrapper */
static PyObject *__pyx_pw_6Cython_8Compiler_7Visitor_21RecursiveNodeReplacer_5visit_Node(PyObject *__pyx_v_self, 
#if CYTHON_METH_FASTCALL
PyObject *const *__pyx_args, Py_ssize_t __pyx_nargs, PyObject *__pyx_kwds
#else
PyObject *__pyx_args, PyObject *__pyx_kwds
#endif
); /*proto*/
PyDoc_STRVAR(__pyx_doc_6Cython_8Compiler_7Visitor_21RecursiveNodeReplacer_4visit_Node, "File: Cython/Compiler/Visitor.py (starting at line 728)");
static PyMethodDef __pyx_mdef_6Cython_8Compiler_7Visitor_21RecursiveNodeReplacer_5visit_Node = {"visit_Node", (PyCFunction)(void(*)(void))(__Pyx_PyCFunction_FastCallWithKeywords)__pyx_pw_6Cython_8Compiler_7Visitor_21RecursiveNodeReplacer_5visit_Node, __Pyx_METH_FASTCALL|METH_KEYWORDS, __pyx_doc_6Cython_8Compiler_7Visitor_21RecursiveNodeReplacer_4visit_Node};
static PyObject *__pyx_pw_6Cython_8Compiler_7Visitor_21RecursiveNodeReplacer_5visit_Node(PyObject *__pyx_v_self, 
#if CYTHON_METH_FASTCALL
PyObject *const *__pyx_args, Py_ssize_t __pyx_nargs, PyObject *__pyx_kwds
#else
PyObject *__pyx_args, PyObject *__pyx_kwds
#endif
) {
  PyObject *__pyx_v_node = 0;
  #if !CYTHON_METH_FASTCALL
  CYTHON_UNUSED Py_ssize_t __pyx_nargs;
  #endif
  CYTHON_UNUSED PyObject *const *__pyx_kwvalues;
  PyObject *__pyx_r = 0;
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("visit_Node (wrapper)", 0);
  #if !CYTHON_METH_FASTCALL
  #if CYTHON_ASSUME_SAFE_SIZE
  __pyx_nargs = PyTuple_GET_SIZE(__pyx_args);
  #else
  __pyx_nargs = PyTuple_Size(__pyx_args); if (unlikely(__pyx_nargs < 0)) return NULL;
  #endif
  #endif
  __pyx_kwvalues = __Pyx_KwValues_FASTCALL(__pyx_args, __pyx_nargs);
  {
    PyObject ** const __pyx_pyargnames[] = {&__pyx_mstate_global->__pyx_n_u_node,0};
  PyObject* values[1] = {0};
    const Py_ssize_t __pyx_kwds_len = (__pyx_kwds) ? __Pyx_NumKwargs_FASTCALL(__pyx_kwds) : 0;
    if (unlikely(__pyx_kwds_len) < 0) __PYX_ERR(0, 728, __pyx_L3_error)
    if (__pyx_kwds_len > 0) {
      switch (__pyx_nargs) {
        case  1:
        values[0] = __Pyx_ArgRef_FASTCALL(__pyx_args, 0);
        if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[0])) __PYX_ERR(0, 728, __pyx_L3_error)
        CYTHON_FALLTHROUGH;
        case  0: break;
        default: goto __pyx_L5_argtuple_error;
      }
      const Py_ssize_t kwd_pos_args = __pyx_nargs;
      if (__Pyx_ParseKeywords(__pyx_kwds, __pyx_kwvalues, __pyx_pyargnames, 0, values, kwd_pos_args, __pyx_kwds_len, "visit_Node", 0) < (0)) __PYX_ERR(0, 728, __pyx_L3_error)
      for (Py_ssize_t i = __pyx_nargs; i < 1; i++) {
        if (unlikely(!values[i])) { __Pyx_RaiseArgtupleInvalid("visit_Node", 1, 1, 1, i); __PYX_ERR(0, 728, __pyx_L3_error) }
      }
    } else if (unlikely(__pyx_nargs != 1)) {
      goto __pyx_L5_argtuple_error;
    } else {
      values[0] = __Pyx_ArgRef_FASTCALL(__pyx_args, 0);
      if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[0])) __PYX_ERR(0, 728, __pyx_L3_error)
    }
    __pyx_v_node = values[0];
  }
  goto __pyx_L6_skip;
  __pyx_L5_argtuple_error:;
  __Pyx_RaiseArgtupleInvalid("visit_Node", 1, 1, 1, __pyx_nargs); __PYX_ERR(0, 728, __pyx_L3_error)
  __pyx_L6_skip:;
  goto __pyx_L4_argument_unpacking_done;
  __pyx_L3_error:;
  for (Py_ssize_t __pyx_temp=0; __pyx_temp < (Py_ssize_t)(sizeof(values)/sizeof(values[0])); ++__pyx_temp) {
    Py_XDECREF(values[__pyx_temp]);
  }
  __Pyx_AddTraceback("Cython.Compiler.Visitor.RecursiveNodeReplacer.visit_Node", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __Pyx_RefNannyFinishContext();
  return NULL;
  __pyx_L4_argument_unpacking_done:;
  __pyx_r = __pyx_pf_6Cython_8Compiler_7Visitor_21RecursiveNodeReplacer_4visit_Node(((struct __pyx_obj_6Cython_8Compiler_7Visitor_RecursiveNodeReplacer *)__pyx_v_self), __pyx_v_node);
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

static PyObject *__pyx_pf_6Cython_8Compiler_7Visitor_21RecursiveNodeReplacer_4visit_Node(struct __pyx_obj_6Cython_8Compiler_7Visitor_RecursiveNodeReplacer *__pyx_v_self, PyObject *__pyx_v_node) {
  PyObject *__pyx_r = NULL;
/* … */
  /* function exit code */
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_t_1);
  __Pyx_AddTraceback("Cython.Compiler.Visitor.RecursiveNodeReplacer.visit_Node", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_r = NULL;
  __pyx_L0:;
  __Pyx_XGIVEREF(__pyx_r);
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}
/* … */
  __pyx_t_2 = __Pyx_CyFunction_New(&__pyx_mdef_6Cython_8Compiler_7Visitor_21RecursiveNodeReplacer_5visit_Node, __Pyx_CYFUNCTION_CCLASS, __pyx_mstate_global->__pyx_n_u_RecursiveNodeReplacer_visit_Node, NULL, __pyx_mstate_global->__pyx_n_u_Cython_Compiler_Visitor, __pyx_mstate_global->__pyx_d, ((PyObject *)__pyx_mstate_global->__pyx_codeobj_tab[50])); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 728, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  #if CYTHON_COMPILING_IN_CPYTHON && PY_VERSION_HEX >= 0x030E0000
  PyUnstable_Object_EnableDeferredRefcount(__pyx_t_2);
  #endif
  if (__Pyx_SetItemOnTypeDict(__pyx_mstate_global->__pyx_ptype_6Cython_8Compiler_7Visitor_RecursiveNodeReplacer, __pyx_mstate_global->__pyx_n_u_visit_Node, __pyx_t_2) < (0)) __PYX_ERR(0, 728, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
```

</details>

L729  🟡  (score=1)
```python
        self._process_children(node)
```
<details><summary>Show generated C (score=1)</summary>

```c
  __pyx_t_1 = ((struct __pyx_vtabstruct_6Cython_8Compiler_7Visitor_RecursiveNodeReplacer *)__pyx_v_self->__pyx_base.__pyx_base.__pyx_vtab)->__pyx_base._process_children(((struct __pyx_obj_6Cython_8Compiler_7Visitor_VisitorTransform *)__pyx_v_self), __pyx_v_node, NULL); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 729, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
```

</details>

L730  ⚪  (score=0)
```python
        if node is self.orig_node:
```
<details><summary>Show generated C (score=0)</summary>

```c
  __pyx_t_2 = (__pyx_v_node == __pyx_v_self->orig_node);
  if (__pyx_t_2) {
/* … */
  }
```

</details>

L731  🟡  (score=2)
```python
            return self.new_node
```
<details><summary>Show generated C (score=2)</summary>

```c
    __Pyx_XDECREF(__pyx_r);
    __Pyx_INCREF(__pyx_v_self->new_node);
    __pyx_r = __pyx_v_self->new_node;
    goto __pyx_L0;
```

</details>

L732  ⚪  (score=0)
```python
        else:
```
L733  🟡  (score=2)
```python
            return node
```
<details><summary>Show generated C (score=2)</summary>

```c
  /*else*/ {
    __Pyx_XDECREF(__pyx_r);
    __Pyx_INCREF(__pyx_v_node);
    __pyx_r = __pyx_v_node;
    goto __pyx_L0;
  }
```

</details>

L734  ⚪  (score=0)
```python
```
L735  🔴  (score=51)
```python
def recursively_replace_node(tree, old_node, new_node):
```
<details><summary>Show generated C (score=51)</summary>

```c
/* Python wrapper */
static PyObject *__pyx_pw_6Cython_8Compiler_7Visitor_1recursively_replace_node(PyObject *__pyx_self, 
#if CYTHON_METH_FASTCALL
PyObject *const *__pyx_args, Py_ssize_t __pyx_nargs, PyObject *__pyx_kwds
#else
PyObject *__pyx_args, PyObject *__pyx_kwds
#endif
); /*proto*/
PyDoc_STRVAR(__pyx_doc_6Cython_8Compiler_7Visitor_recursively_replace_node, "File: Cython/Compiler/Visitor.py (starting at line 735)");
static PyMethodDef __pyx_mdef_6Cython_8Compiler_7Visitor_1recursively_replace_node = {"recursively_replace_node", (PyCFunction)(void(*)(void))(__Pyx_PyCFunction_FastCallWithKeywords)__pyx_pw_6Cython_8Compiler_7Visitor_1recursively_replace_node, __Pyx_METH_FASTCALL|METH_KEYWORDS, __pyx_doc_6Cython_8Compiler_7Visitor_recursively_replace_node};
static PyObject *__pyx_pw_6Cython_8Compiler_7Visitor_1recursively_replace_node(PyObject *__pyx_self, 
#if CYTHON_METH_FASTCALL
PyObject *const *__pyx_args, Py_ssize_t __pyx_nargs, PyObject *__pyx_kwds
#else
PyObject *__pyx_args, PyObject *__pyx_kwds
#endif
) {
  PyObject *__pyx_v_tree = 0;
  PyObject *__pyx_v_old_node = 0;
  PyObject *__pyx_v_new_node = 0;
  #if !CYTHON_METH_FASTCALL
  CYTHON_UNUSED Py_ssize_t __pyx_nargs;
  #endif
  CYTHON_UNUSED PyObject *const *__pyx_kwvalues;
  PyObject *__pyx_r = 0;
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("recursively_replace_node (wrapper)", 0);
  #if !CYTHON_METH_FASTCALL
  #if CYTHON_ASSUME_SAFE_SIZE
  __pyx_nargs = PyTuple_GET_SIZE(__pyx_args);
  #else
  __pyx_nargs = PyTuple_Size(__pyx_args); if (unlikely(__pyx_nargs < 0)) return NULL;
  #endif
  #endif
  __pyx_kwvalues = __Pyx_KwValues_FASTCALL(__pyx_args, __pyx_nargs);
  {
    PyObject ** const __pyx_pyargnames[] = {&__pyx_mstate_global->__pyx_n_u_tree,&__pyx_mstate_global->__pyx_n_u_old_node,&__pyx_mstate_global->__pyx_n_u_new_node,0};
  PyObject* values[3] = {0,0,0};
    const Py_ssize_t __pyx_kwds_len = (__pyx_kwds) ? __Pyx_NumKwargs_FASTCALL(__pyx_kwds) : 0;
    if (unlikely(__pyx_kwds_len) < 0) __PYX_ERR(0, 735, __pyx_L3_error)
    if (__pyx_kwds_len > 0) {
      switch (__pyx_nargs) {
        case  3:
        values[2] = __Pyx_ArgRef_FASTCALL(__pyx_args, 2);
        if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[2])) __PYX_ERR(0, 735, __pyx_L3_error)
        CYTHON_FALLTHROUGH;
        case  2:
        values[1] = __Pyx_ArgRef_FASTCALL(__pyx_args, 1);
        if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[1])) __PYX_ERR(0, 735, __pyx_L3_error)
        CYTHON_FALLTHROUGH;
        case  1:
        values[0] = __Pyx_ArgRef_FASTCALL(__pyx_args, 0);
        if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[0])) __PYX_ERR(0, 735, __pyx_L3_error)
        CYTHON_FALLTHROUGH;
        case  0: break;
        default: goto __pyx_L5_argtuple_error;
      }
      const Py_ssize_t kwd_pos_args = __pyx_nargs;
      if (__Pyx_ParseKeywords(__pyx_kwds, __pyx_kwvalues, __pyx_pyargnames, 0, values, kwd_pos_args, __pyx_kwds_len, "recursively_replace_node", 0) < (0)) __PYX_ERR(0, 735, __pyx_L3_error)
      for (Py_ssize_t i = __pyx_nargs; i < 3; i++) {
        if (unlikely(!values[i])) { __Pyx_RaiseArgtupleInvalid("recursively_replace_node", 1, 3, 3, i); __PYX_ERR(0, 735, __pyx_L3_error) }
      }
    } else if (unlikely(__pyx_nargs != 3)) {
      goto __pyx_L5_argtuple_error;
    } else {
      values[0] = __Pyx_ArgRef_FASTCALL(__pyx_args, 0);
      if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[0])) __PYX_ERR(0, 735, __pyx_L3_error)
      values[1] = __Pyx_ArgRef_FASTCALL(__pyx_args, 1);
      if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[1])) __PYX_ERR(0, 735, __pyx_L3_error)
      values[2] = __Pyx_ArgRef_FASTCALL(__pyx_args, 2);
      if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[2])) __PYX_ERR(0, 735, __pyx_L3_error)
    }
    __pyx_v_tree = values[0];
    __pyx_v_old_node = values[1];
    __pyx_v_new_node = values[2];
  }
  goto __pyx_L6_skip;
  __pyx_L5_argtuple_error:;
  __Pyx_RaiseArgtupleInvalid("recursively_replace_node", 1, 3, 3, __pyx_nargs); __PYX_ERR(0, 735, __pyx_L3_error)
  __pyx_L6_skip:;
  goto __pyx_L4_argument_unpacking_done;
  __pyx_L3_error:;
  for (Py_ssize_t __pyx_temp=0; __pyx_temp < (Py_ssize_t)(sizeof(values)/sizeof(values[0])); ++__pyx_temp) {
    Py_XDECREF(values[__pyx_temp]);
  }
  __Pyx_AddTraceback("Cython.Compiler.Visitor.recursively_replace_node", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __Pyx_RefNannyFinishContext();
  return NULL;
  __pyx_L4_argument_unpacking_done:;
  __pyx_r = __pyx_pf_6Cython_8Compiler_7Visitor_recursively_replace_node(__pyx_self, __pyx_v_tree, __pyx_v_old_node, __pyx_v_new_node);
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

static PyObject *__pyx_pf_6Cython_8Compiler_7Visitor_recursively_replace_node(CYTHON_UNUSED PyObject *__pyx_self, PyObject *__pyx_v_tree, PyObject *__pyx_v_old_node, PyObject *__pyx_v_new_node) {
  struct __pyx_obj_6Cython_8Compiler_7Visitor_RecursiveNodeReplacer *__pyx_v_replace_in = NULL;
  PyObject *__pyx_r = NULL;
/* … */
  /* function exit code */
  __pyx_r = Py_None; __Pyx_INCREF(Py_None);
  goto __pyx_L0;
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_t_1);
  __Pyx_XDECREF(__pyx_t_2);
  __Pyx_XDECREF(__pyx_t_4);
  __Pyx_AddTraceback("Cython.Compiler.Visitor.recursively_replace_node", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_r = NULL;
  __pyx_L0:;
  __Pyx_XDECREF((PyObject *)__pyx_v_replace_in);
  __Pyx_XGIVEREF(__pyx_r);
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}
/* … */
  __pyx_t_2 = __Pyx_CyFunction_New(&__pyx_mdef_6Cython_8Compiler_7Visitor_1recursively_replace_node, 0, __pyx_mstate_global->__pyx_n_u_recursively_replace_node, NULL, __pyx_mstate_global->__pyx_n_u_Cython_Compiler_Visitor, __pyx_mstate_global->__pyx_d, ((PyObject *)__pyx_mstate_global->__pyx_codeobj_tab[53])); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 735, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  #if CYTHON_COMPILING_IN_CPYTHON && PY_VERSION_HEX >= 0x030E0000
  PyUnstable_Object_EnableDeferredRefcount(__pyx_t_2);
  #endif
  if (PyDict_SetItem(__pyx_mstate_global->__pyx_d, __pyx_mstate_global->__pyx_n_u_recursively_replace_node, __pyx_t_2) < (0)) __PYX_ERR(0, 735, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
```

</details>

L736  🟡  (score=3)
```python
    replace_in = RecursiveNodeReplacer(old_node, new_node)
```
<details><summary>Show generated C (score=3)</summary>

```c
  __pyx_t_2 = NULL;
  __pyx_t_3 = 1;
  {
    PyObject *__pyx_callargs[3] = {__pyx_t_2, __pyx_v_old_node, __pyx_v_new_node};
    __pyx_t_1 = __Pyx_PyObject_FastCall((PyObject*)__pyx_mstate_global->__pyx_ptype_6Cython_8Compiler_7Visitor_RecursiveNodeReplacer, __pyx_callargs+__pyx_t_3, (3-__pyx_t_3) | (__pyx_t_3*__Pyx_PY_VECTORCALL_ARGUMENTS_OFFSET));
    __Pyx_XDECREF(__pyx_t_2); __pyx_t_2 = 0;
    if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 736, __pyx_L1_error)
    __Pyx_GOTREF((PyObject *)__pyx_t_1);
  }
  __pyx_v_replace_in = ((struct __pyx_obj_6Cython_8Compiler_7Visitor_RecursiveNodeReplacer *)__pyx_t_1);
  __pyx_t_1 = 0;
```

</details>

L737  🔴  (score=16)
```python
    replace_in(tree)
```
<details><summary>Show generated C (score=16)</summary>

```c
  __pyx_t_2 = NULL;
  __Pyx_INCREF((PyObject *)__pyx_v_replace_in);
  __pyx_t_4 = ((PyObject *)__pyx_v_replace_in); 
  __pyx_t_3 = 1;
  #if CYTHON_UNPACK_METHODS
  if (unlikely(PyMethod_Check(__pyx_t_4))) {
    __pyx_t_2 = PyMethod_GET_SELF(__pyx_t_4);
    assert(__pyx_t_2);
    PyObject* __pyx__function = PyMethod_GET_FUNCTION(__pyx_t_4);
    __Pyx_INCREF(__pyx_t_2);
    __Pyx_INCREF(__pyx__function);
    __Pyx_DECREF_SET(__pyx_t_4, __pyx__function);
    __pyx_t_3 = 0;
  }
  #endif
  {
    PyObject *__pyx_callargs[2] = {__pyx_t_2, __pyx_v_tree};
    __pyx_t_1 = __Pyx_PyObject_FastCall((PyObject*)__pyx_t_4, __pyx_callargs+__pyx_t_3, (2-__pyx_t_3) | (__pyx_t_3*__Pyx_PY_VECTORCALL_ARGUMENTS_OFFSET));
    __Pyx_XDECREF(__pyx_t_2); __pyx_t_2 = 0;
    __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
    if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 737, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_1);
  }
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
```

</details>

L738  ⚪  (score=0)
```python
```
L739  ⚪  (score=0)
```python
```
L740  ⚪  (score=0)
```python
class NodeFinder(TreeVisitor):
```
<details><summary>Show generated C (score=0)</summary>

```c
struct __pyx_vtabstruct_6Cython_8Compiler_7Visitor_NodeFinder {
  struct __pyx_vtabstruct_6Cython_8Compiler_7Visitor_TreeVisitor __pyx_base;
};
static struct __pyx_vtabstruct_6Cython_8Compiler_7Visitor_NodeFinder *__pyx_vtabptr_6Cython_8Compiler_7Visitor_NodeFinder;
```

</details>

L741  ⚪  (score=0)
```python
    """
```
L742  ⚪  (score=0)
```python
    Find out if a node appears in a subtree.
```
L743  ⚪  (score=0)
```python
    """
```
L744  🔴  (score=29)
```python
    def __init__(self, node):
```
<details><summary>Show generated C (score=29)</summary>

```c
/* Python wrapper */
static int __pyx_pw_6Cython_8Compiler_7Visitor_10NodeFinder_1__init__(PyObject *__pyx_v_self, PyObject *__pyx_args, PyObject *__pyx_kwds); /*proto*/
PyDoc_STRVAR(__pyx_doc_6Cython_8Compiler_7Visitor_10NodeFinder___init__, "File: Cython/Compiler/Visitor.py (starting at line 744)");
#if CYTHON_UPDATE_DESCRIPTOR_DOC
struct wrapperbase __pyx_wrapperbase_6Cython_8Compiler_7Visitor_10NodeFinder___init__;
#endif
static int __pyx_pw_6Cython_8Compiler_7Visitor_10NodeFinder_1__init__(PyObject *__pyx_v_self, PyObject *__pyx_args, PyObject *__pyx_kwds) {
  PyObject *__pyx_v_node = 0;
  CYTHON_UNUSED Py_ssize_t __pyx_nargs;
  CYTHON_UNUSED PyObject *const *__pyx_kwvalues;
  int __pyx_r;
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("__init__ (wrapper)", 0);
  #if CYTHON_ASSUME_SAFE_SIZE
  __pyx_nargs = PyTuple_GET_SIZE(__pyx_args);
  #else
  __pyx_nargs = PyTuple_Size(__pyx_args); if (unlikely(__pyx_nargs < 0)) return -1;
  #endif
  __pyx_kwvalues = __Pyx_KwValues_VARARGS(__pyx_args, __pyx_nargs);
  {
    PyObject ** const __pyx_pyargnames[] = {&__pyx_mstate_global->__pyx_n_u_node,0};
  PyObject* values[1] = {0};
    const Py_ssize_t __pyx_kwds_len = (__pyx_kwds) ? __Pyx_NumKwargs_VARARGS(__pyx_kwds) : 0;
    if (unlikely(__pyx_kwds_len) < 0) __PYX_ERR(0, 744, __pyx_L3_error)
    if (__pyx_kwds_len > 0) {
      switch (__pyx_nargs) {
        case  1:
        values[0] = __Pyx_ArgRef_VARARGS(__pyx_args, 0);
        if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[0])) __PYX_ERR(0, 744, __pyx_L3_error)
        CYTHON_FALLTHROUGH;
        case  0: break;
        default: goto __pyx_L5_argtuple_error;
      }
      const Py_ssize_t kwd_pos_args = __pyx_nargs;
      if (__Pyx_ParseKeywords(__pyx_kwds, __pyx_kwvalues, __pyx_pyargnames, 0, values, kwd_pos_args, __pyx_kwds_len, "__init__", 0) < (0)) __PYX_ERR(0, 744, __pyx_L3_error)
      for (Py_ssize_t i = __pyx_nargs; i < 1; i++) {
        if (unlikely(!values[i])) { __Pyx_RaiseArgtupleInvalid("__init__", 1, 1, 1, i); __PYX_ERR(0, 744, __pyx_L3_error) }
      }
    } else if (unlikely(__pyx_nargs != 1)) {
      goto __pyx_L5_argtuple_error;
    } else {
      values[0] = __Pyx_ArgRef_VARARGS(__pyx_args, 0);
      if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[0])) __PYX_ERR(0, 744, __pyx_L3_error)
    }
    __pyx_v_node = values[0];
  }
  goto __pyx_L6_skip;
  __pyx_L5_argtuple_error:;
  __Pyx_RaiseArgtupleInvalid("__init__", 1, 1, 1, __pyx_nargs); __PYX_ERR(0, 744, __pyx_L3_error)
  __pyx_L6_skip:;
  goto __pyx_L4_argument_unpacking_done;
  __pyx_L3_error:;
  for (Py_ssize_t __pyx_temp=0; __pyx_temp < (Py_ssize_t)(sizeof(values)/sizeof(values[0])); ++__pyx_temp) {
    Py_XDECREF(values[__pyx_temp]);
  }
  __Pyx_AddTraceback("Cython.Compiler.Visitor.NodeFinder.__init__", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __Pyx_RefNannyFinishContext();
  return -1;
  __pyx_L4_argument_unpacking_done:;
  __pyx_r = __pyx_pf_6Cython_8Compiler_7Visitor_10NodeFinder___init__(((struct __pyx_obj_6Cython_8Compiler_7Visitor_NodeFinder *)__pyx_v_self), __pyx_v_node);
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

static int __pyx_pf_6Cython_8Compiler_7Visitor_10NodeFinder___init__(struct __pyx_obj_6Cython_8Compiler_7Visitor_NodeFinder *__pyx_v_self, PyObject *__pyx_v_node) {
  int __pyx_r;
/* … */
  /* function exit code */
  __pyx_r = 0;
  goto __pyx_L0;
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_t_1);
  __Pyx_XDECREF(__pyx_t_2);
  __Pyx_XDECREF(__pyx_t_3);
  __Pyx_XDECREF(__pyx_t_4);
  __Pyx_AddTraceback("Cython.Compiler.Visitor.NodeFinder.__init__", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_r = -1;
  __pyx_L0:;
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}
```

</details>

L745  🟠  (score=9)
```python
        super().__init__()
```
<details><summary>Show generated C (score=9)</summary>

```c
  __pyx_t_4 = NULL;
  __pyx_t_5 = 1;
  {
    PyObject *__pyx_callargs[3] = {__pyx_t_4, ((PyObject *)__pyx_mstate_global->__pyx_ptype_6Cython_8Compiler_7Visitor_NodeFinder), ((PyObject *)__pyx_v_self)};
    __pyx_t_3 = __Pyx_PyObject_FastCall((PyObject*)__pyx_builtin_super, __pyx_callargs+__pyx_t_5, (3-__pyx_t_5) | (__pyx_t_5*__Pyx_PY_VECTORCALL_ARGUMENTS_OFFSET));
    __Pyx_XDECREF(__pyx_t_4); __pyx_t_4 = 0;
    if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 745, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_3);
  }
  __pyx_t_2 = __pyx_t_3;
  __Pyx_INCREF(__pyx_t_2);
  __pyx_t_5 = 0;
  {
    PyObject *__pyx_callargs[2] = {__pyx_t_2, NULL};
    __pyx_t_1 = __Pyx_PyObject_FastCallMethod((PyObject*)__pyx_mstate_global->__pyx_n_u_init, __pyx_callargs+__pyx_t_5, (1-__pyx_t_5) | (1*__Pyx_PY_VECTORCALL_ARGUMENTS_OFFSET));
    __Pyx_XDECREF(__pyx_t_2); __pyx_t_2 = 0;
    __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
    if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 745, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_1);
  }
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
```

</details>

L746  🟡  (score=2)
```python
        self.node = node
```
<details><summary>Show generated C (score=2)</summary>

```c
  __Pyx_INCREF(__pyx_v_node);
  __Pyx_GIVEREF(__pyx_v_node);
  __Pyx_GOTREF(__pyx_v_self->node);
  __Pyx_DECREF(__pyx_v_self->node);
  __pyx_v_self->node = __pyx_v_node;
```

</details>

L747  ⚪  (score=0)
```python
        self.found = False
```
<details><summary>Show generated C (score=0)</summary>

```c
  __pyx_v_self->found = 0;
```

</details>

L748  ⚪  (score=0)
```python
```
L749  🔴  (score=37)
```python
    def visit_Node(self, node):
```
<details><summary>Show generated C (score=37)</summary>

```c
/* Python wrapper */
static PyObject *__pyx_pw_6Cython_8Compiler_7Visitor_10NodeFinder_3visit_Node(PyObject *__pyx_v_self, 
#if CYTHON_METH_FASTCALL
PyObject *const *__pyx_args, Py_ssize_t __pyx_nargs, PyObject *__pyx_kwds
#else
PyObject *__pyx_args, PyObject *__pyx_kwds
#endif
); /*proto*/
PyDoc_STRVAR(__pyx_doc_6Cython_8Compiler_7Visitor_10NodeFinder_2visit_Node, "File: Cython/Compiler/Visitor.py (starting at line 749)");
static PyMethodDef __pyx_mdef_6Cython_8Compiler_7Visitor_10NodeFinder_3visit_Node = {"visit_Node", (PyCFunction)(void(*)(void))(__Pyx_PyCFunction_FastCallWithKeywords)__pyx_pw_6Cython_8Compiler_7Visitor_10NodeFinder_3visit_Node, __Pyx_METH_FASTCALL|METH_KEYWORDS, __pyx_doc_6Cython_8Compiler_7Visitor_10NodeFinder_2visit_Node};
static PyObject *__pyx_pw_6Cython_8Compiler_7Visitor_10NodeFinder_3visit_Node(PyObject *__pyx_v_self, 
#if CYTHON_METH_FASTCALL
PyObject *const *__pyx_args, Py_ssize_t __pyx_nargs, PyObject *__pyx_kwds
#else
PyObject *__pyx_args, PyObject *__pyx_kwds
#endif
) {
  PyObject *__pyx_v_node = 0;
  #if !CYTHON_METH_FASTCALL
  CYTHON_UNUSED Py_ssize_t __pyx_nargs;
  #endif
  CYTHON_UNUSED PyObject *const *__pyx_kwvalues;
  PyObject *__pyx_r = 0;
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("visit_Node (wrapper)", 0);
  #if !CYTHON_METH_FASTCALL
  #if CYTHON_ASSUME_SAFE_SIZE
  __pyx_nargs = PyTuple_GET_SIZE(__pyx_args);
  #else
  __pyx_nargs = PyTuple_Size(__pyx_args); if (unlikely(__pyx_nargs < 0)) return NULL;
  #endif
  #endif
  __pyx_kwvalues = __Pyx_KwValues_FASTCALL(__pyx_args, __pyx_nargs);
  {
    PyObject ** const __pyx_pyargnames[] = {&__pyx_mstate_global->__pyx_n_u_node,0};
  PyObject* values[1] = {0};
    const Py_ssize_t __pyx_kwds_len = (__pyx_kwds) ? __Pyx_NumKwargs_FASTCALL(__pyx_kwds) : 0;
    if (unlikely(__pyx_kwds_len) < 0) __PYX_ERR(0, 749, __pyx_L3_error)
    if (__pyx_kwds_len > 0) {
      switch (__pyx_nargs) {
        case  1:
        values[0] = __Pyx_ArgRef_FASTCALL(__pyx_args, 0);
        if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[0])) __PYX_ERR(0, 749, __pyx_L3_error)
        CYTHON_FALLTHROUGH;
        case  0: break;
        default: goto __pyx_L5_argtuple_error;
      }
      const Py_ssize_t kwd_pos_args = __pyx_nargs;
      if (__Pyx_ParseKeywords(__pyx_kwds, __pyx_kwvalues, __pyx_pyargnames, 0, values, kwd_pos_args, __pyx_kwds_len, "visit_Node", 0) < (0)) __PYX_ERR(0, 749, __pyx_L3_error)
      for (Py_ssize_t i = __pyx_nargs; i < 1; i++) {
        if (unlikely(!values[i])) { __Pyx_RaiseArgtupleInvalid("visit_Node", 1, 1, 1, i); __PYX_ERR(0, 749, __pyx_L3_error) }
      }
    } else if (unlikely(__pyx_nargs != 1)) {
      goto __pyx_L5_argtuple_error;
    } else {
      values[0] = __Pyx_ArgRef_FASTCALL(__pyx_args, 0);
      if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[0])) __PYX_ERR(0, 749, __pyx_L3_error)
    }
    __pyx_v_node = values[0];
  }
  goto __pyx_L6_skip;
  __pyx_L5_argtuple_error:;
  __Pyx_RaiseArgtupleInvalid("visit_Node", 1, 1, 1, __pyx_nargs); __PYX_ERR(0, 749, __pyx_L3_error)
  __pyx_L6_skip:;
  goto __pyx_L4_argument_unpacking_done;
  __pyx_L3_error:;
  for (Py_ssize_t __pyx_temp=0; __pyx_temp < (Py_ssize_t)(sizeof(values)/sizeof(values[0])); ++__pyx_temp) {
    Py_XDECREF(values[__pyx_temp]);
  }
  __Pyx_AddTraceback("Cython.Compiler.Visitor.NodeFinder.visit_Node", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __Pyx_RefNannyFinishContext();
  return NULL;
  __pyx_L4_argument_unpacking_done:;
  __pyx_r = __pyx_pf_6Cython_8Compiler_7Visitor_10NodeFinder_2visit_Node(((struct __pyx_obj_6Cython_8Compiler_7Visitor_NodeFinder *)__pyx_v_self), __pyx_v_node);
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

static PyObject *__pyx_pf_6Cython_8Compiler_7Visitor_10NodeFinder_2visit_Node(struct __pyx_obj_6Cython_8Compiler_7Visitor_NodeFinder *__pyx_v_self, PyObject *__pyx_v_node) {
  PyObject *__pyx_r = NULL;
/* … */
  /* function exit code */
  __pyx_r = Py_None; __Pyx_INCREF(Py_None);
  goto __pyx_L0;
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_t_2);
  __Pyx_AddTraceback("Cython.Compiler.Visitor.NodeFinder.visit_Node", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_r = NULL;
  __pyx_L0:;
  __Pyx_XGIVEREF(__pyx_r);
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}
/* … */
  __pyx_t_2 = __Pyx_CyFunction_New(&__pyx_mdef_6Cython_8Compiler_7Visitor_10NodeFinder_3visit_Node, __Pyx_CYFUNCTION_CCLASS, __pyx_mstate_global->__pyx_n_u_NodeFinder_visit_Node, NULL, __pyx_mstate_global->__pyx_n_u_Cython_Compiler_Visitor, __pyx_mstate_global->__pyx_d, ((PyObject *)__pyx_mstate_global->__pyx_codeobj_tab[54])); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 749, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  #if CYTHON_COMPILING_IN_CPYTHON && PY_VERSION_HEX >= 0x030E0000
  PyUnstable_Object_EnableDeferredRefcount(__pyx_t_2);
  #endif
  if (__Pyx_SetItemOnTypeDict(__pyx_mstate_global->__pyx_ptype_6Cython_8Compiler_7Visitor_NodeFinder, __pyx_mstate_global->__pyx_n_u_visit_Node, __pyx_t_2) < (0)) __PYX_ERR(0, 749, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
```

</details>

L750  ⚪  (score=0)
```python
        if self.found:
```
<details><summary>Show generated C (score=0)</summary>

```c
  if (__pyx_v_self->found) {
    goto __pyx_L3;
  }
```

</details>

L751  ⚪  (score=0)
```python
            pass  # short-circuit
```
L752  ⚪  (score=0)
```python
        elif node is self.node:
```
<details><summary>Show generated C (score=0)</summary>

```c
  __pyx_t_1 = (__pyx_v_node == __pyx_v_self->node);
  if (__pyx_t_1) {
/* … */
    goto __pyx_L3;
  }
```

</details>

L753  ⚪  (score=0)
```python
            self.found = True
```
<details><summary>Show generated C (score=0)</summary>

```c
    __pyx_v_self->found = 1;
```

</details>

L754  ⚪  (score=0)
```python
        else:
```
L755  🟡  (score=1)
```python
            self._visitchildren(node, None, None)
```
<details><summary>Show generated C (score=1)</summary>

```c
  /*else*/ {
    __pyx_t_2 = ((struct __pyx_vtabstruct_6Cython_8Compiler_7Visitor_NodeFinder *)__pyx_v_self->__pyx_base.__pyx_vtab)->__pyx_base._visitchildren(((struct __pyx_obj_6Cython_8Compiler_7Visitor_TreeVisitor *)__pyx_v_self), __pyx_v_node, Py_None, Py_None); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 755, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_2);
    __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  }
  __pyx_L3:;
```

</details>

L756  ⚪  (score=0)
```python
```
L757  🔴  (score=45)
```python
def tree_contains(tree, node):
```
<details><summary>Show generated C (score=45)</summary>

```c
/* Python wrapper */
static PyObject *__pyx_pw_6Cython_8Compiler_7Visitor_3tree_contains(PyObject *__pyx_self, 
#if CYTHON_METH_FASTCALL
PyObject *const *__pyx_args, Py_ssize_t __pyx_nargs, PyObject *__pyx_kwds
#else
PyObject *__pyx_args, PyObject *__pyx_kwds
#endif
); /*proto*/
PyDoc_STRVAR(__pyx_doc_6Cython_8Compiler_7Visitor_2tree_contains, "File: Cython/Compiler/Visitor.py (starting at line 757)");
static PyMethodDef __pyx_mdef_6Cython_8Compiler_7Visitor_3tree_contains = {"tree_contains", (PyCFunction)(void(*)(void))(__Pyx_PyCFunction_FastCallWithKeywords)__pyx_pw_6Cython_8Compiler_7Visitor_3tree_contains, __Pyx_METH_FASTCALL|METH_KEYWORDS, __pyx_doc_6Cython_8Compiler_7Visitor_2tree_contains};
static PyObject *__pyx_pw_6Cython_8Compiler_7Visitor_3tree_contains(PyObject *__pyx_self, 
#if CYTHON_METH_FASTCALL
PyObject *const *__pyx_args, Py_ssize_t __pyx_nargs, PyObject *__pyx_kwds
#else
PyObject *__pyx_args, PyObject *__pyx_kwds
#endif
) {
  PyObject *__pyx_v_tree = 0;
  PyObject *__pyx_v_node = 0;
  #if !CYTHON_METH_FASTCALL
  CYTHON_UNUSED Py_ssize_t __pyx_nargs;
  #endif
  CYTHON_UNUSED PyObject *const *__pyx_kwvalues;
  PyObject *__pyx_r = 0;
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("tree_contains (wrapper)", 0);
  #if !CYTHON_METH_FASTCALL
  #if CYTHON_ASSUME_SAFE_SIZE
  __pyx_nargs = PyTuple_GET_SIZE(__pyx_args);
  #else
  __pyx_nargs = PyTuple_Size(__pyx_args); if (unlikely(__pyx_nargs < 0)) return NULL;
  #endif
  #endif
  __pyx_kwvalues = __Pyx_KwValues_FASTCALL(__pyx_args, __pyx_nargs);
  {
    PyObject ** const __pyx_pyargnames[] = {&__pyx_mstate_global->__pyx_n_u_tree,&__pyx_mstate_global->__pyx_n_u_node,0};
  PyObject* values[2] = {0,0};
    const Py_ssize_t __pyx_kwds_len = (__pyx_kwds) ? __Pyx_NumKwargs_FASTCALL(__pyx_kwds) : 0;
    if (unlikely(__pyx_kwds_len) < 0) __PYX_ERR(0, 757, __pyx_L3_error)
    if (__pyx_kwds_len > 0) {
      switch (__pyx_nargs) {
        case  2:
        values[1] = __Pyx_ArgRef_FASTCALL(__pyx_args, 1);
        if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[1])) __PYX_ERR(0, 757, __pyx_L3_error)
        CYTHON_FALLTHROUGH;
        case  1:
        values[0] = __Pyx_ArgRef_FASTCALL(__pyx_args, 0);
        if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[0])) __PYX_ERR(0, 757, __pyx_L3_error)
        CYTHON_FALLTHROUGH;
        case  0: break;
        default: goto __pyx_L5_argtuple_error;
      }
      const Py_ssize_t kwd_pos_args = __pyx_nargs;
      if (__Pyx_ParseKeywords(__pyx_kwds, __pyx_kwvalues, __pyx_pyargnames, 0, values, kwd_pos_args, __pyx_kwds_len, "tree_contains", 0) < (0)) __PYX_ERR(0, 757, __pyx_L3_error)
      for (Py_ssize_t i = __pyx_nargs; i < 2; i++) {
        if (unlikely(!values[i])) { __Pyx_RaiseArgtupleInvalid("tree_contains", 1, 2, 2, i); __PYX_ERR(0, 757, __pyx_L3_error) }
      }
    } else if (unlikely(__pyx_nargs != 2)) {
      goto __pyx_L5_argtuple_error;
    } else {
      values[0] = __Pyx_ArgRef_FASTCALL(__pyx_args, 0);
      if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[0])) __PYX_ERR(0, 757, __pyx_L3_error)
      values[1] = __Pyx_ArgRef_FASTCALL(__pyx_args, 1);
      if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[1])) __PYX_ERR(0, 757, __pyx_L3_error)
    }
    __pyx_v_tree = values[0];
    __pyx_v_node = values[1];
  }
  goto __pyx_L6_skip;
  __pyx_L5_argtuple_error:;
  __Pyx_RaiseArgtupleInvalid("tree_contains", 1, 2, 2, __pyx_nargs); __PYX_ERR(0, 757, __pyx_L3_error)
  __pyx_L6_skip:;
  goto __pyx_L4_argument_unpacking_done;
  __pyx_L3_error:;
  for (Py_ssize_t __pyx_temp=0; __pyx_temp < (Py_ssize_t)(sizeof(values)/sizeof(values[0])); ++__pyx_temp) {
    Py_XDECREF(values[__pyx_temp]);
  }
  __Pyx_AddTraceback("Cython.Compiler.Visitor.tree_contains", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __Pyx_RefNannyFinishContext();
  return NULL;
  __pyx_L4_argument_unpacking_done:;
  __pyx_r = __pyx_pf_6Cython_8Compiler_7Visitor_2tree_contains(__pyx_self, __pyx_v_tree, __pyx_v_node);
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

static PyObject *__pyx_pf_6Cython_8Compiler_7Visitor_2tree_contains(CYTHON_UNUSED PyObject *__pyx_self, PyObject *__pyx_v_tree, PyObject *__pyx_v_node) {
  struct __pyx_obj_6Cython_8Compiler_7Visitor_NodeFinder *__pyx_v_finder = NULL;
  PyObject *__pyx_r = NULL;
/* … */
  /* function exit code */
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_t_1);
  __Pyx_XDECREF(__pyx_t_2);
  __Pyx_AddTraceback("Cython.Compiler.Visitor.tree_contains", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_r = NULL;
  __pyx_L0:;
  __Pyx_XDECREF((PyObject *)__pyx_v_finder);
  __Pyx_XGIVEREF(__pyx_r);
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}
/* … */
  __pyx_t_2 = __Pyx_CyFunction_New(&__pyx_mdef_6Cython_8Compiler_7Visitor_3tree_contains, 0, __pyx_mstate_global->__pyx_n_u_tree_contains, NULL, __pyx_mstate_global->__pyx_n_u_Cython_Compiler_Visitor, __pyx_mstate_global->__pyx_d, ((PyObject *)__pyx_mstate_global->__pyx_codeobj_tab[57])); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 757, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  #if CYTHON_COMPILING_IN_CPYTHON && PY_VERSION_HEX >= 0x030E0000
  PyUnstable_Object_EnableDeferredRefcount(__pyx_t_2);
  #endif
  if (PyDict_SetItem(__pyx_mstate_global->__pyx_d, __pyx_mstate_global->__pyx_n_u_tree_contains, __pyx_t_2) < (0)) __PYX_ERR(0, 757, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
```

</details>

L758  🟡  (score=3)
```python
    finder = NodeFinder(node)
```
<details><summary>Show generated C (score=3)</summary>

```c
  __pyx_t_2 = NULL;
  __pyx_t_3 = 1;
  {
    PyObject *__pyx_callargs[2] = {__pyx_t_2, __pyx_v_node};
    __pyx_t_1 = __Pyx_PyObject_FastCall((PyObject*)__pyx_mstate_global->__pyx_ptype_6Cython_8Compiler_7Visitor_NodeFinder, __pyx_callargs+__pyx_t_3, (2-__pyx_t_3) | (__pyx_t_3*__Pyx_PY_VECTORCALL_ARGUMENTS_OFFSET));
    __Pyx_XDECREF(__pyx_t_2); __pyx_t_2 = 0;
    if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 758, __pyx_L1_error)
    __Pyx_GOTREF((PyObject *)__pyx_t_1);
  }
  __pyx_v_finder = ((struct __pyx_obj_6Cython_8Compiler_7Visitor_NodeFinder *)__pyx_t_1);
  __pyx_t_1 = 0;
```

</details>

L759  🟡  (score=1)
```python
    finder.visit(tree)
```
<details><summary>Show generated C (score=1)</summary>

```c
  __pyx_t_1 = ((struct __pyx_vtabstruct_6Cython_8Compiler_7Visitor_NodeFinder *)__pyx_v_finder->__pyx_base.__pyx_vtab)->__pyx_base.visit(((struct __pyx_obj_6Cython_8Compiler_7Visitor_TreeVisitor *)__pyx_v_finder), __pyx_v_tree, 0); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 759, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
```

</details>

L760  🟡  (score=3)
```python
    return finder.found
```
<details><summary>Show generated C (score=3)</summary>

```c
  __Pyx_XDECREF(__pyx_r);
  __pyx_t_1 = __Pyx_PyBool_FromLong(__pyx_v_finder->found); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 760, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __pyx_r = __pyx_t_1;
  __pyx_t_1 = 0;
  goto __pyx_L0;
```

</details>

L761  ⚪  (score=0)
```python
```
L762  ⚪  (score=0)
```python
```
L763  ⚪  (score=0)
```python
# Utils
```
L764  🔴  (score=50)
```python
def replace_node(ptr, value):
```
<details><summary>Show generated C (score=50)</summary>

```c
/* Python wrapper */
static PyObject *__pyx_pw_6Cython_8Compiler_7Visitor_5replace_node(PyObject *__pyx_self, 
#if CYTHON_METH_FASTCALL
PyObject *const *__pyx_args, Py_ssize_t __pyx_nargs, PyObject *__pyx_kwds
#else
PyObject *__pyx_args, PyObject *__pyx_kwds
#endif
); /*proto*/
PyDoc_STRVAR(__pyx_doc_6Cython_8Compiler_7Visitor_4replace_node, "File: Cython/Compiler/Visitor.py (starting at line 764)\nReplaces a node. ptr is of the form used on the access path stack\n    (parent, attrname, listidx|None)\n    ");
static PyMethodDef __pyx_mdef_6Cython_8Compiler_7Visitor_5replace_node = {"replace_node", (PyCFunction)(void(*)(void))(__Pyx_PyCFunction_FastCallWithKeywords)__pyx_pw_6Cython_8Compiler_7Visitor_5replace_node, __Pyx_METH_FASTCALL|METH_KEYWORDS, __pyx_doc_6Cython_8Compiler_7Visitor_4replace_node};
static PyObject *__pyx_pw_6Cython_8Compiler_7Visitor_5replace_node(PyObject *__pyx_self, 
#if CYTHON_METH_FASTCALL
PyObject *const *__pyx_args, Py_ssize_t __pyx_nargs, PyObject *__pyx_kwds
#else
PyObject *__pyx_args, PyObject *__pyx_kwds
#endif
) {
  PyObject *__pyx_v_ptr = 0;
  PyObject *__pyx_v_value = 0;
  #if !CYTHON_METH_FASTCALL
  CYTHON_UNUSED Py_ssize_t __pyx_nargs;
  #endif
  CYTHON_UNUSED PyObject *const *__pyx_kwvalues;
  PyObject *__pyx_r = 0;
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("replace_node (wrapper)", 0);
  #if !CYTHON_METH_FASTCALL
  #if CYTHON_ASSUME_SAFE_SIZE
  __pyx_nargs = PyTuple_GET_SIZE(__pyx_args);
  #else
  __pyx_nargs = PyTuple_Size(__pyx_args); if (unlikely(__pyx_nargs < 0)) return NULL;
  #endif
  #endif
  __pyx_kwvalues = __Pyx_KwValues_FASTCALL(__pyx_args, __pyx_nargs);
  {
    PyObject ** const __pyx_pyargnames[] = {&__pyx_mstate_global->__pyx_n_u_ptr,&__pyx_mstate_global->__pyx_n_u_value,0};
  PyObject* values[2] = {0,0};
    const Py_ssize_t __pyx_kwds_len = (__pyx_kwds) ? __Pyx_NumKwargs_FASTCALL(__pyx_kwds) : 0;
    if (unlikely(__pyx_kwds_len) < 0) __PYX_ERR(0, 764, __pyx_L3_error)
    if (__pyx_kwds_len > 0) {
      switch (__pyx_nargs) {
        case  2:
        values[1] = __Pyx_ArgRef_FASTCALL(__pyx_args, 1);
        if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[1])) __PYX_ERR(0, 764, __pyx_L3_error)
        CYTHON_FALLTHROUGH;
        case  1:
        values[0] = __Pyx_ArgRef_FASTCALL(__pyx_args, 0);
        if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[0])) __PYX_ERR(0, 764, __pyx_L3_error)
        CYTHON_FALLTHROUGH;
        case  0: break;
        default: goto __pyx_L5_argtuple_error;
      }
      const Py_ssize_t kwd_pos_args = __pyx_nargs;
      if (__Pyx_ParseKeywords(__pyx_kwds, __pyx_kwvalues, __pyx_pyargnames, 0, values, kwd_pos_args, __pyx_kwds_len, "replace_node", 0) < (0)) __PYX_ERR(0, 764, __pyx_L3_error)
      for (Py_ssize_t i = __pyx_nargs; i < 2; i++) {
        if (unlikely(!values[i])) { __Pyx_RaiseArgtupleInvalid("replace_node", 1, 2, 2, i); __PYX_ERR(0, 764, __pyx_L3_error) }
      }
    } else if (unlikely(__pyx_nargs != 2)) {
      goto __pyx_L5_argtuple_error;
    } else {
      values[0] = __Pyx_ArgRef_FASTCALL(__pyx_args, 0);
      if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[0])) __PYX_ERR(0, 764, __pyx_L3_error)
      values[1] = __Pyx_ArgRef_FASTCALL(__pyx_args, 1);
      if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[1])) __PYX_ERR(0, 764, __pyx_L3_error)
    }
    __pyx_v_ptr = values[0];
    __pyx_v_value = values[1];
  }
  goto __pyx_L6_skip;
  __pyx_L5_argtuple_error:;
  __Pyx_RaiseArgtupleInvalid("replace_node", 1, 2, 2, __pyx_nargs); __PYX_ERR(0, 764, __pyx_L3_error)
  __pyx_L6_skip:;
  goto __pyx_L4_argument_unpacking_done;
  __pyx_L3_error:;
  for (Py_ssize_t __pyx_temp=0; __pyx_temp < (Py_ssize_t)(sizeof(values)/sizeof(values[0])); ++__pyx_temp) {
    Py_XDECREF(values[__pyx_temp]);
  }
  __Pyx_AddTraceback("Cython.Compiler.Visitor.replace_node", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __Pyx_RefNannyFinishContext();
  return NULL;
  __pyx_L4_argument_unpacking_done:;
  __pyx_r = __pyx_pf_6Cython_8Compiler_7Visitor_4replace_node(__pyx_self, __pyx_v_ptr, __pyx_v_value);
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

static PyObject *__pyx_pf_6Cython_8Compiler_7Visitor_4replace_node(CYTHON_UNUSED PyObject *__pyx_self, PyObject *__pyx_v_ptr, PyObject *__pyx_v_value) {
  PyObject *__pyx_v_parent = NULL;
  PyObject *__pyx_v_attrname = NULL;
  PyObject *__pyx_v_listidx = NULL;
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
  __Pyx_AddTraceback("Cython.Compiler.Visitor.replace_node", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_r = NULL;
  __pyx_L0:;
  __Pyx_XDECREF(__pyx_v_parent);
  __Pyx_XDECREF(__pyx_v_attrname);
  __Pyx_XDECREF(__pyx_v_listidx);
  __Pyx_XGIVEREF(__pyx_r);
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}
/* … */
  __pyx_t_2 = __Pyx_CyFunction_New(&__pyx_mdef_6Cython_8Compiler_7Visitor_5replace_node, 0, __pyx_mstate_global->__pyx_n_u_replace_node, NULL, __pyx_mstate_global->__pyx_n_u_Cython_Compiler_Visitor, __pyx_mstate_global->__pyx_d, ((PyObject *)__pyx_mstate_global->__pyx_codeobj_tab[58])); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 764, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  #if CYTHON_COMPILING_IN_CPYTHON && PY_VERSION_HEX >= 0x030E0000
  PyUnstable_Object_EnableDeferredRefcount(__pyx_t_2);
  #endif
  if (PyDict_SetItem(__pyx_mstate_global->__pyx_d, __pyx_mstate_global->__pyx_n_u_replace_node, __pyx_t_2) < (0)) __PYX_ERR(0, 764, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
```

</details>

L765  ⚪  (score=0)
```python
    """Replaces a node. ptr is of the form used on the access path stack
```
L766  ⚪  (score=0)
```python
    (parent, attrname, listidx|None)
```
L767  ⚪  (score=0)
```python
    """
```
L768  🔴  (score=54)
```python
    parent, attrname, listidx = ptr
```
<details><summary>Show generated C (score=54)</summary>

```c
  if ((likely(PyTuple_CheckExact(__pyx_v_ptr))) || (PyList_CheckExact(__pyx_v_ptr))) {
    PyObject* sequence = __pyx_v_ptr;
    Py_ssize_t size = __Pyx_PySequence_SIZE(sequence);
    if (unlikely(size != 3)) {
      if (size > 3) __Pyx_RaiseTooManyValuesError(3);
      else if (size >= 0) __Pyx_RaiseNeedMoreValuesError(size);
      __PYX_ERR(0, 768, __pyx_L1_error)
    }
    #if CYTHON_ASSUME_SAFE_MACROS && !CYTHON_AVOID_BORROWED_REFS
    if (likely(PyTuple_CheckExact(sequence))) {
      __pyx_t_1 = PyTuple_GET_ITEM(sequence, 0);
      __Pyx_INCREF(__pyx_t_1);
      __pyx_t_2 = PyTuple_GET_ITEM(sequence, 1);
      __Pyx_INCREF(__pyx_t_2);
      __pyx_t_3 = PyTuple_GET_ITEM(sequence, 2);
      __Pyx_INCREF(__pyx_t_3);
    } else {
      __pyx_t_1 = __Pyx_PyList_GetItemRefFast(sequence, 0, __Pyx_ReferenceSharing_SharedReference);
      if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 768, __pyx_L1_error)
      __Pyx_XGOTREF(__pyx_t_1);
      __pyx_t_2 = __Pyx_PyList_GetItemRefFast(sequence, 1, __Pyx_ReferenceSharing_SharedReference);
      if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 768, __pyx_L1_error)
      __Pyx_XGOTREF(__pyx_t_2);
      __pyx_t_3 = __Pyx_PyList_GetItemRefFast(sequence, 2, __Pyx_ReferenceSharing_SharedReference);
      if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 768, __pyx_L1_error)
      __Pyx_XGOTREF(__pyx_t_3);
    }
    #else
    __pyx_t_1 = __Pyx_PySequence_ITEM(sequence, 0); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 768, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_1);
    __pyx_t_2 = __Pyx_PySequence_ITEM(sequence, 1); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 768, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_2);
    __pyx_t_3 = __Pyx_PySequence_ITEM(sequence, 2); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 768, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_3);
    #endif
  } else {
    Py_ssize_t index = -1;
    __pyx_t_4 = PyObject_GetIter(__pyx_v_ptr); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 768, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_4);
    __pyx_t_5 = (CYTHON_COMPILING_IN_LIMITED_API) ? PyIter_Next : __Pyx_PyObject_GetIterNextFunc(__pyx_t_4);
    index = 0; __pyx_t_1 = __pyx_t_5(__pyx_t_4); if (unlikely(!__pyx_t_1)) goto __pyx_L3_unpacking_failed;
    __Pyx_GOTREF(__pyx_t_1);
    index = 1; __pyx_t_2 = __pyx_t_5(__pyx_t_4); if (unlikely(!__pyx_t_2)) goto __pyx_L3_unpacking_failed;
    __Pyx_GOTREF(__pyx_t_2);
    index = 2; __pyx_t_3 = __pyx_t_5(__pyx_t_4); if (unlikely(!__pyx_t_3)) goto __pyx_L3_unpacking_failed;
    __Pyx_GOTREF(__pyx_t_3);
    if (__Pyx_IternextUnpackEndCheck(__pyx_t_5(__pyx_t_4), 3) < (0)) __PYX_ERR(0, 768, __pyx_L1_error)
    __pyx_t_5 = NULL;
    __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
    goto __pyx_L4_unpacking_done;
    __pyx_L3_unpacking_failed:;
    __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
    __pyx_t_5 = NULL;
    if (__Pyx_IterFinish() == 0) __Pyx_RaiseNeedMoreValuesError(index);
    __PYX_ERR(0, 768, __pyx_L1_error)
    __pyx_L4_unpacking_done:;
  }
  __pyx_v_parent = __pyx_t_1;
  __pyx_t_1 = 0;
  __pyx_v_attrname = __pyx_t_2;
  __pyx_t_2 = 0;
  __pyx_v_listidx = __pyx_t_3;
  __pyx_t_3 = 0;
```

</details>

L769  ⚪  (score=0)
```python
    if listidx is None:
```
<details><summary>Show generated C (score=0)</summary>

```c
  __pyx_t_6 = (__pyx_v_listidx == Py_None);
  if (__pyx_t_6) {
/* … */
    goto __pyx_L5;
  }
```

</details>

L770  🟠  (score=5)
```python
        setattr(parent, attrname, value)
```
<details><summary>Show generated C (score=5)</summary>

```c
    __pyx_t_7 = PyObject_SetAttr(__pyx_v_parent, __pyx_v_attrname, __pyx_v_value); if (unlikely(__pyx_t_7 == ((int)-1))) __PYX_ERR(0, 770, __pyx_L1_error)
```

</details>

L771  ⚪  (score=0)
```python
    else:
```
L772  🟠  (score=8)
```python
        getattr(parent, attrname)[listidx] = value
```
<details><summary>Show generated C (score=8)</summary>

```c
  /*else*/ {
    __pyx_t_3 = __Pyx_GetAttr(__pyx_v_parent, __pyx_v_attrname); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 772, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_3);
    if (unlikely((PyObject_SetItem(__pyx_t_3, __pyx_v_listidx, __pyx_v_value) < 0))) __PYX_ERR(0, 772, __pyx_L1_error)
    __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
  }
  __pyx_L5:;
```

</details>

L773  ⚪  (score=0)
```python
```
L774  ⚪  (score=0)
```python
```
L775  🔴  (score=27)
```python
class PrintTree(TreeVisitor):
```
<details><summary>Show generated C (score=27)</summary>

```c
  __pyx_t_2 = PyTuple_Pack(1, ((PyObject *)__pyx_mstate_global->__pyx_ptype_6Cython_8Compiler_7Visitor_TreeVisitor)); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 775, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __pyx_t_5 = __Pyx_PEP560_update_bases(__pyx_t_2); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 775, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_5);
  __pyx_t_4 = __Pyx_CalculateMetaclass(NULL, __pyx_t_5); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 775, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_4);
  __pyx_t_6 = __Pyx_Py3MetaclassPrepare(__pyx_t_4, __pyx_t_5, __pyx_mstate_global->__pyx_n_u_PrintTree, __pyx_mstate_global->__pyx_n_u_PrintTree, (PyObject *) NULL, __pyx_mstate_global->__pyx_n_u_Cython_Compiler_Visitor, __pyx_mstate_global->__pyx_kp_u_File_Cython_Compiler_Visitor_py_3); if (unlikely(!__pyx_t_6)) __PYX_ERR(0, 775, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_6);
  if (__pyx_t_5 != __pyx_t_2) {
    if (unlikely((PyDict_SetItemString(__pyx_t_6, "__orig_bases__", __pyx_t_2) < 0))) __PYX_ERR(0, 775, __pyx_L1_error)
  }
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
/* … */
  __pyx_t_2 = __Pyx_Py3ClassCreate(__pyx_t_4, __pyx_mstate_global->__pyx_n_u_PrintTree, __pyx_t_5, __pyx_t_6, NULL, 0, 0); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 775, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  #if CYTHON_COMPILING_IN_CPYTHON && PY_VERSION_HEX >= 0x030E0000
  PyUnstable_Object_EnableDeferredRefcount(__pyx_t_2);
  #endif
  if (PyDict_SetItem(__pyx_mstate_global->__pyx_d, __pyx_mstate_global->__pyx_n_u_PrintTree, __pyx_t_2) < (0)) __PYX_ERR(0, 775, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __Pyx_DECREF(__pyx_t_6); __pyx_t_6 = 0;
  __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
  __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
```

</details>

L776  ⚪  (score=0)
```python
    """Prints a representation of the tree to standard output.
```
L777  ⚪  (score=0)
```python
    Subclass and override repr_of to provide more information
```
L778  ⚪  (score=0)
```python
    about nodes. """
```
L779  🔴  (score=57)
```python
    def __init__(self, start=None, end=None):
```
<details><summary>Show generated C (score=57)</summary>

```c
/* Python wrapper */
static PyObject *__pyx_pw_6Cython_8Compiler_7Visitor_9PrintTree_1__init__(PyObject *__pyx_self, 
#if CYTHON_METH_FASTCALL
PyObject *const *__pyx_args, Py_ssize_t __pyx_nargs, PyObject *__pyx_kwds
#else
PyObject *__pyx_args, PyObject *__pyx_kwds
#endif
); /*proto*/
PyDoc_STRVAR(__pyx_doc_6Cython_8Compiler_7Visitor_9PrintTree___init__, "File: Cython/Compiler/Visitor.py (starting at line 779)");
static PyMethodDef __pyx_mdef_6Cython_8Compiler_7Visitor_9PrintTree_1__init__ = {"__init__", (PyCFunction)(void(*)(void))(__Pyx_PyCFunction_FastCallWithKeywords)__pyx_pw_6Cython_8Compiler_7Visitor_9PrintTree_1__init__, __Pyx_METH_FASTCALL|METH_KEYWORDS, __pyx_doc_6Cython_8Compiler_7Visitor_9PrintTree___init__};
static PyObject *__pyx_pw_6Cython_8Compiler_7Visitor_9PrintTree_1__init__(PyObject *__pyx_self, 
#if CYTHON_METH_FASTCALL
PyObject *const *__pyx_args, Py_ssize_t __pyx_nargs, PyObject *__pyx_kwds
#else
PyObject *__pyx_args, PyObject *__pyx_kwds
#endif
) {
  PyObject *__pyx_v_self = 0;
  PyObject *__pyx_v_start = 0;
  PyObject *__pyx_v_end = 0;
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
    PyObject ** const __pyx_pyargnames[] = {&__pyx_mstate_global->__pyx_n_u_self,&__pyx_mstate_global->__pyx_n_u_start,&__pyx_mstate_global->__pyx_n_u_end,0};
  PyObject* values[3] = {0,0,0};
    const Py_ssize_t __pyx_kwds_len = (__pyx_kwds) ? __Pyx_NumKwargs_FASTCALL(__pyx_kwds) : 0;
    if (unlikely(__pyx_kwds_len) < 0) __PYX_ERR(0, 779, __pyx_L3_error)
    if (__pyx_kwds_len > 0) {
      switch (__pyx_nargs) {
        case  3:
        values[2] = __Pyx_ArgRef_FASTCALL(__pyx_args, 2);
        if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[2])) __PYX_ERR(0, 779, __pyx_L3_error)
        CYTHON_FALLTHROUGH;
        case  2:
        values[1] = __Pyx_ArgRef_FASTCALL(__pyx_args, 1);
        if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[1])) __PYX_ERR(0, 779, __pyx_L3_error)
        CYTHON_FALLTHROUGH;
        case  1:
        values[0] = __Pyx_ArgRef_FASTCALL(__pyx_args, 0);
        if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[0])) __PYX_ERR(0, 779, __pyx_L3_error)
        CYTHON_FALLTHROUGH;
        case  0: break;
        default: goto __pyx_L5_argtuple_error;
      }
      const Py_ssize_t kwd_pos_args = __pyx_nargs;
      if (__Pyx_ParseKeywords(__pyx_kwds, __pyx_kwvalues, __pyx_pyargnames, 0, values, kwd_pos_args, __pyx_kwds_len, "__init__", 0) < (0)) __PYX_ERR(0, 779, __pyx_L3_error)
      if (!values[1]) values[1] = __Pyx_NewRef(((PyObject *)Py_None));
      if (!values[2]) values[2] = __Pyx_NewRef(((PyObject *)Py_None));
      for (Py_ssize_t i = __pyx_nargs; i < 1; i++) {
        if (unlikely(!values[i])) { __Pyx_RaiseArgtupleInvalid("__init__", 0, 1, 3, i); __PYX_ERR(0, 779, __pyx_L3_error) }
      }
    } else {
      switch (__pyx_nargs) {
        case  3:
        values[2] = __Pyx_ArgRef_FASTCALL(__pyx_args, 2);
        if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[2])) __PYX_ERR(0, 779, __pyx_L3_error)
        CYTHON_FALLTHROUGH;
        case  2:
        values[1] = __Pyx_ArgRef_FASTCALL(__pyx_args, 1);
        if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[1])) __PYX_ERR(0, 779, __pyx_L3_error)
        CYTHON_FALLTHROUGH;
        case  1:
        values[0] = __Pyx_ArgRef_FASTCALL(__pyx_args, 0);
        if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[0])) __PYX_ERR(0, 779, __pyx_L3_error)
        break;
        default: goto __pyx_L5_argtuple_error;
      }
      if (!values[1]) values[1] = __Pyx_NewRef(((PyObject *)Py_None));
      if (!values[2]) values[2] = __Pyx_NewRef(((PyObject *)Py_None));
    }
    __pyx_v_self = values[0];
    __pyx_v_start = values[1];
    __pyx_v_end = values[2];
  }
  goto __pyx_L6_skip;
  __pyx_L5_argtuple_error:;
  __Pyx_RaiseArgtupleInvalid("__init__", 0, 1, 3, __pyx_nargs); __PYX_ERR(0, 779, __pyx_L3_error)
  __pyx_L6_skip:;
  goto __pyx_L4_argument_unpacking_done;
  __pyx_L3_error:;
  for (Py_ssize_t __pyx_temp=0; __pyx_temp < (Py_ssize_t)(sizeof(values)/sizeof(values[0])); ++__pyx_temp) {
    Py_XDECREF(values[__pyx_temp]);
  }
  __Pyx_AddTraceback("Cython.Compiler.Visitor.PrintTree.__init__", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __Pyx_RefNannyFinishContext();
  return NULL;
  __pyx_L4_argument_unpacking_done:;
  __pyx_r = __pyx_pf_6Cython_8Compiler_7Visitor_9PrintTree___init__(__pyx_self, __pyx_v_self, __pyx_v_start, __pyx_v_end);

  /* function exit code */
  for (Py_ssize_t __pyx_temp=0; __pyx_temp < (Py_ssize_t)(sizeof(values)/sizeof(values[0])); ++__pyx_temp) {
    Py_XDECREF(values[__pyx_temp]);
  }
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}

static PyObject *__pyx_pf_6Cython_8Compiler_7Visitor_9PrintTree___init__(CYTHON_UNUSED PyObject *__pyx_self, PyObject *__pyx_v_self, PyObject *__pyx_v_start, PyObject *__pyx_v_end) {
  PyObject *__pyx_r = NULL;
/* … */
  /* function exit code */
  __pyx_r = Py_None; __Pyx_INCREF(Py_None);
  goto __pyx_L0;
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_t_1);
  __Pyx_XDECREF(__pyx_t_2);
  __Pyx_XDECREF(__pyx_t_6);
  __Pyx_AddTraceback("Cython.Compiler.Visitor.PrintTree.__init__", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_r = NULL;
  __pyx_L0:;
  __Pyx_XGIVEREF(__pyx_r);
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}
/* … */
  __pyx_t_2 = __Pyx_CyFunction_New(&__pyx_mdef_6Cython_8Compiler_7Visitor_9PrintTree_1__init__, 0, __pyx_mstate_global->__pyx_n_u_PrintTree___init, NULL, __pyx_mstate_global->__pyx_n_u_Cython_Compiler_Visitor, __pyx_mstate_global->__pyx_d, ((PyObject *)__pyx_mstate_global->__pyx_codeobj_tab[59])); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 779, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  #if CYTHON_COMPILING_IN_CPYTHON && PY_VERSION_HEX >= 0x030E0000
  PyUnstable_Object_EnableDeferredRefcount(__pyx_t_2);
  #endif
  __Pyx_CyFunction_SetDefaultsTuple(__pyx_t_2, __pyx_mstate_global->__pyx_tuple[7]);
  if (__Pyx_SetNameInClass(__pyx_t_6, __pyx_mstate_global->__pyx_n_u_init, __pyx_t_2) < (0)) __PYX_ERR(0, 779, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
```

</details>

L780  🟠  (score=5)
```python
        TreeVisitor.__init__(self)
```
<details><summary>Show generated C (score=5)</summary>

```c
  __pyx_t_2 = ((PyObject *)__pyx_mstate_global->__pyx_ptype_6Cython_8Compiler_7Visitor_TreeVisitor);
  __Pyx_INCREF(__pyx_t_2);
  __pyx_t_3 = 0;
  {
    PyObject *__pyx_callargs[2] = {__pyx_t_2, __pyx_v_self};
    __pyx_t_1 = __Pyx_PyObject_FastCallMethod((PyObject*)__pyx_mstate_global->__pyx_n_u_init, __pyx_callargs+__pyx_t_3, (2-__pyx_t_3) | (1*__Pyx_PY_VECTORCALL_ARGUMENTS_OFFSET));
    __Pyx_XDECREF(__pyx_t_2); __pyx_t_2 = 0;
    if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 780, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_1);
  }
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
```

</details>

L781  🟡  (score=2)
```python
        self._indent = ""
```
<details><summary>Show generated C (score=2)</summary>

```c
  if (__Pyx_PyObject_SetAttrStr(__pyx_v_self, __pyx_mstate_global->__pyx_n_u_indent, __pyx_mstate_global->__pyx_kp_u__7) < (0)) __PYX_ERR(0, 781, __pyx_L1_error)
```

</details>

L782  ⚪  (score=0)
```python
        if start is not None or end is not None:
```
<details><summary>Show generated C (score=0)</summary>

```c
  __pyx_t_5 = (__pyx_v_start != Py_None);
  if (!__pyx_t_5) {
  } else {
    __pyx_t_4 = __pyx_t_5;
    goto __pyx_L4_bool_binop_done;
  }
  __pyx_t_5 = (__pyx_v_end != Py_None);
  __pyx_t_4 = __pyx_t_5;
  __pyx_L4_bool_binop_done:;
  if (__pyx_t_4) {
/* … */
    goto __pyx_L3;
  }
```

</details>

L783  🔴  (score=22)
```python
            self._line_range = (start or 0, end or 2**30)
```
<details><summary>Show generated C (score=22)</summary>

```c
    __pyx_t_4 = __Pyx_PyObject_IsTrue(__pyx_v_start); if (unlikely((__pyx_t_4 < 0))) __PYX_ERR(0, 783, __pyx_L1_error)
    if (!__pyx_t_4) {
    } else {
      __Pyx_INCREF(__pyx_v_start);
      __pyx_t_1 = __pyx_v_start;
      goto __pyx_L6_bool_binop_done;
    }
    __pyx_t_2 = __Pyx_PyLong_From_long(0); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 783, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_2);
    __pyx_t_1 = __pyx_t_2;
    __pyx_t_2 = 0;
    __pyx_L6_bool_binop_done:;
    __pyx_t_4 = __Pyx_PyObject_IsTrue(__pyx_v_end); if (unlikely((__pyx_t_4 < 0))) __PYX_ERR(0, 783, __pyx_L1_error)
    if (!__pyx_t_4) {
    } else {
      __Pyx_INCREF(__pyx_v_end);
      __pyx_t_2 = __pyx_v_end;
      goto __pyx_L8_bool_binop_done;
    }
    __pyx_t_6 = __Pyx_PyLong_From_long(0x40000000); if (unlikely(!__pyx_t_6)) __PYX_ERR(0, 783, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_6);
    __pyx_t_2 = __pyx_t_6;
    __pyx_t_6 = 0;
    __pyx_L8_bool_binop_done:;
    __pyx_t_6 = PyTuple_New(2); if (unlikely(!__pyx_t_6)) __PYX_ERR(0, 783, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_6);
    __Pyx_GIVEREF(__pyx_t_1);
    if (__Pyx_PyTuple_SET_ITEM(__pyx_t_6, 0, __pyx_t_1) != (0)) __PYX_ERR(0, 783, __pyx_L1_error);
    __Pyx_GIVEREF(__pyx_t_2);
    if (__Pyx_PyTuple_SET_ITEM(__pyx_t_6, 1, __pyx_t_2) != (0)) __PYX_ERR(0, 783, __pyx_L1_error);
    __pyx_t_1 = 0;
    __pyx_t_2 = 0;
    if (__Pyx_PyObject_SetAttrStr(__pyx_v_self, __pyx_mstate_global->__pyx_n_u_line_range, __pyx_t_6) < (0)) __PYX_ERR(0, 783, __pyx_L1_error)
    __Pyx_DECREF(__pyx_t_6); __pyx_t_6 = 0;
```

</details>

L784  ⚪  (score=0)
```python
        else:
```
L785  🟡  (score=2)
```python
            self._line_range = None
```
<details><summary>Show generated C (score=2)</summary>

```c
  /*else*/ {
    if (__Pyx_PyObject_SetAttrStr(__pyx_v_self, __pyx_mstate_global->__pyx_n_u_line_range, Py_None) < (0)) __PYX_ERR(0, 785, __pyx_L1_error)
  }
  __pyx_L3:;
```

</details>

L786  ⚪  (score=0)
```python
```
L787  🔴  (score=38)
```python
    def indent(self):
```
<details><summary>Show generated C (score=38)</summary>

```c
/* Python wrapper */
static PyObject *__pyx_pw_6Cython_8Compiler_7Visitor_9PrintTree_3indent(PyObject *__pyx_self, 
#if CYTHON_METH_FASTCALL
PyObject *const *__pyx_args, Py_ssize_t __pyx_nargs, PyObject *__pyx_kwds
#else
PyObject *__pyx_args, PyObject *__pyx_kwds
#endif
); /*proto*/
PyDoc_STRVAR(__pyx_doc_6Cython_8Compiler_7Visitor_9PrintTree_2indent, "File: Cython/Compiler/Visitor.py (starting at line 787)");
static PyMethodDef __pyx_mdef_6Cython_8Compiler_7Visitor_9PrintTree_3indent = {"indent", (PyCFunction)(void(*)(void))(__Pyx_PyCFunction_FastCallWithKeywords)__pyx_pw_6Cython_8Compiler_7Visitor_9PrintTree_3indent, __Pyx_METH_FASTCALL|METH_KEYWORDS, __pyx_doc_6Cython_8Compiler_7Visitor_9PrintTree_2indent};
static PyObject *__pyx_pw_6Cython_8Compiler_7Visitor_9PrintTree_3indent(PyObject *__pyx_self, 
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
  __Pyx_RefNannySetupContext("indent (wrapper)", 0);
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
    if (unlikely(__pyx_kwds_len) < 0) __PYX_ERR(0, 787, __pyx_L3_error)
    if (__pyx_kwds_len > 0) {
      switch (__pyx_nargs) {
        case  1:
        values[0] = __Pyx_ArgRef_FASTCALL(__pyx_args, 0);
        if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[0])) __PYX_ERR(0, 787, __pyx_L3_error)
        CYTHON_FALLTHROUGH;
        case  0: break;
        default: goto __pyx_L5_argtuple_error;
      }
      const Py_ssize_t kwd_pos_args = __pyx_nargs;
      if (__Pyx_ParseKeywords(__pyx_kwds, __pyx_kwvalues, __pyx_pyargnames, 0, values, kwd_pos_args, __pyx_kwds_len, "indent", 0) < (0)) __PYX_ERR(0, 787, __pyx_L3_error)
      for (Py_ssize_t i = __pyx_nargs; i < 1; i++) {
        if (unlikely(!values[i])) { __Pyx_RaiseArgtupleInvalid("indent", 1, 1, 1, i); __PYX_ERR(0, 787, __pyx_L3_error) }
      }
    } else if (unlikely(__pyx_nargs != 1)) {
      goto __pyx_L5_argtuple_error;
    } else {
      values[0] = __Pyx_ArgRef_FASTCALL(__pyx_args, 0);
      if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[0])) __PYX_ERR(0, 787, __pyx_L3_error)
    }
    __pyx_v_self = values[0];
  }
  goto __pyx_L6_skip;
  __pyx_L5_argtuple_error:;
  __Pyx_RaiseArgtupleInvalid("indent", 1, 1, 1, __pyx_nargs); __PYX_ERR(0, 787, __pyx_L3_error)
  __pyx_L6_skip:;
  goto __pyx_L4_argument_unpacking_done;
  __pyx_L3_error:;
  for (Py_ssize_t __pyx_temp=0; __pyx_temp < (Py_ssize_t)(sizeof(values)/sizeof(values[0])); ++__pyx_temp) {
    Py_XDECREF(values[__pyx_temp]);
  }
  __Pyx_AddTraceback("Cython.Compiler.Visitor.PrintTree.indent", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __Pyx_RefNannyFinishContext();
  return NULL;
  __pyx_L4_argument_unpacking_done:;
  __pyx_r = __pyx_pf_6Cython_8Compiler_7Visitor_9PrintTree_2indent(__pyx_self, __pyx_v_self);
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

static PyObject *__pyx_pf_6Cython_8Compiler_7Visitor_9PrintTree_2indent(CYTHON_UNUSED PyObject *__pyx_self, PyObject *__pyx_v_self) {
  PyObject *__pyx_r = NULL;
/* … */
  /* function exit code */
  __pyx_r = Py_None; __Pyx_INCREF(Py_None);
  goto __pyx_L0;
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_t_1);
  __Pyx_XDECREF(__pyx_t_2);
  __Pyx_AddTraceback("Cython.Compiler.Visitor.PrintTree.indent", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_r = NULL;
  __pyx_L0:;
  __Pyx_XGIVEREF(__pyx_r);
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}
/* … */
  __pyx_t_2 = __Pyx_CyFunction_New(&__pyx_mdef_6Cython_8Compiler_7Visitor_9PrintTree_3indent, 0, __pyx_mstate_global->__pyx_n_u_PrintTree_indent, NULL, __pyx_mstate_global->__pyx_n_u_Cython_Compiler_Visitor, __pyx_mstate_global->__pyx_d, ((PyObject *)__pyx_mstate_global->__pyx_codeobj_tab[60])); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 787, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  #if CYTHON_COMPILING_IN_CPYTHON && PY_VERSION_HEX >= 0x030E0000
  PyUnstable_Object_EnableDeferredRefcount(__pyx_t_2);
  #endif
  if (__Pyx_SetNameInClass(__pyx_t_6, __pyx_mstate_global->__pyx_n_u_indent_2, __pyx_t_2) < (0)) __PYX_ERR(0, 787, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
```

</details>

L788  🔴  (score=11)
```python
        self._indent += "  "
```
<details><summary>Show generated C (score=11)</summary>

```c
  __pyx_t_1 = __Pyx_PyObject_GetAttrStr(__pyx_v_self, __pyx_mstate_global->__pyx_n_u_indent); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 788, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __pyx_t_2 = PyNumber_InPlaceAdd(__pyx_t_1, __pyx_mstate_global->__pyx_kp_u__11); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 788, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  if (__Pyx_PyObject_SetAttrStr(__pyx_v_self, __pyx_mstate_global->__pyx_n_u_indent, __pyx_t_2) < (0)) __PYX_ERR(0, 788, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
```

</details>

L789  ⚪  (score=0)
```python
```
L790  🔴  (score=38)
```python
    def unindent(self):
```
<details><summary>Show generated C (score=38)</summary>

```c
/* Python wrapper */
static PyObject *__pyx_pw_6Cython_8Compiler_7Visitor_9PrintTree_5unindent(PyObject *__pyx_self, 
#if CYTHON_METH_FASTCALL
PyObject *const *__pyx_args, Py_ssize_t __pyx_nargs, PyObject *__pyx_kwds
#else
PyObject *__pyx_args, PyObject *__pyx_kwds
#endif
); /*proto*/
PyDoc_STRVAR(__pyx_doc_6Cython_8Compiler_7Visitor_9PrintTree_4unindent, "File: Cython/Compiler/Visitor.py (starting at line 790)");
static PyMethodDef __pyx_mdef_6Cython_8Compiler_7Visitor_9PrintTree_5unindent = {"unindent", (PyCFunction)(void(*)(void))(__Pyx_PyCFunction_FastCallWithKeywords)__pyx_pw_6Cython_8Compiler_7Visitor_9PrintTree_5unindent, __Pyx_METH_FASTCALL|METH_KEYWORDS, __pyx_doc_6Cython_8Compiler_7Visitor_9PrintTree_4unindent};
static PyObject *__pyx_pw_6Cython_8Compiler_7Visitor_9PrintTree_5unindent(PyObject *__pyx_self, 
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
  __Pyx_RefNannySetupContext("unindent (wrapper)", 0);
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
    if (unlikely(__pyx_kwds_len) < 0) __PYX_ERR(0, 790, __pyx_L3_error)
    if (__pyx_kwds_len > 0) {
      switch (__pyx_nargs) {
        case  1:
        values[0] = __Pyx_ArgRef_FASTCALL(__pyx_args, 0);
        if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[0])) __PYX_ERR(0, 790, __pyx_L3_error)
        CYTHON_FALLTHROUGH;
        case  0: break;
        default: goto __pyx_L5_argtuple_error;
      }
      const Py_ssize_t kwd_pos_args = __pyx_nargs;
      if (__Pyx_ParseKeywords(__pyx_kwds, __pyx_kwvalues, __pyx_pyargnames, 0, values, kwd_pos_args, __pyx_kwds_len, "unindent", 0) < (0)) __PYX_ERR(0, 790, __pyx_L3_error)
      for (Py_ssize_t i = __pyx_nargs; i < 1; i++) {
        if (unlikely(!values[i])) { __Pyx_RaiseArgtupleInvalid("unindent", 1, 1, 1, i); __PYX_ERR(0, 790, __pyx_L3_error) }
      }
    } else if (unlikely(__pyx_nargs != 1)) {
      goto __pyx_L5_argtuple_error;
    } else {
      values[0] = __Pyx_ArgRef_FASTCALL(__pyx_args, 0);
      if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[0])) __PYX_ERR(0, 790, __pyx_L3_error)
    }
    __pyx_v_self = values[0];
  }
  goto __pyx_L6_skip;
  __pyx_L5_argtuple_error:;
  __Pyx_RaiseArgtupleInvalid("unindent", 1, 1, 1, __pyx_nargs); __PYX_ERR(0, 790, __pyx_L3_error)
  __pyx_L6_skip:;
  goto __pyx_L4_argument_unpacking_done;
  __pyx_L3_error:;
  for (Py_ssize_t __pyx_temp=0; __pyx_temp < (Py_ssize_t)(sizeof(values)/sizeof(values[0])); ++__pyx_temp) {
    Py_XDECREF(values[__pyx_temp]);
  }
  __Pyx_AddTraceback("Cython.Compiler.Visitor.PrintTree.unindent", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __Pyx_RefNannyFinishContext();
  return NULL;
  __pyx_L4_argument_unpacking_done:;
  __pyx_r = __pyx_pf_6Cython_8Compiler_7Visitor_9PrintTree_4unindent(__pyx_self, __pyx_v_self);
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

static PyObject *__pyx_pf_6Cython_8Compiler_7Visitor_9PrintTree_4unindent(CYTHON_UNUSED PyObject *__pyx_self, PyObject *__pyx_v_self) {
  PyObject *__pyx_r = NULL;
/* … */
  /* function exit code */
  __pyx_r = Py_None; __Pyx_INCREF(Py_None);
  goto __pyx_L0;
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_t_1);
  __Pyx_XDECREF(__pyx_t_2);
  __Pyx_AddTraceback("Cython.Compiler.Visitor.PrintTree.unindent", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_r = NULL;
  __pyx_L0:;
  __Pyx_XGIVEREF(__pyx_r);
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}
/* … */
  __pyx_t_2 = __Pyx_CyFunction_New(&__pyx_mdef_6Cython_8Compiler_7Visitor_9PrintTree_5unindent, 0, __pyx_mstate_global->__pyx_n_u_PrintTree_unindent, NULL, __pyx_mstate_global->__pyx_n_u_Cython_Compiler_Visitor, __pyx_mstate_global->__pyx_d, ((PyObject *)__pyx_mstate_global->__pyx_codeobj_tab[61])); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 790, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  #if CYTHON_COMPILING_IN_CPYTHON && PY_VERSION_HEX >= 0x030E0000
  PyUnstable_Object_EnableDeferredRefcount(__pyx_t_2);
  #endif
  if (__Pyx_SetNameInClass(__pyx_t_6, __pyx_mstate_global->__pyx_n_u_unindent, __pyx_t_2) < (0)) __PYX_ERR(0, 790, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
```

</details>

L791  🔴  (score=13)
```python
        self._indent = self._indent[:-2]
```
<details><summary>Show generated C (score=13)</summary>

```c
  __pyx_t_1 = __Pyx_PyObject_GetAttrStr(__pyx_v_self, __pyx_mstate_global->__pyx_n_u_indent); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 791, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __pyx_t_2 = __Pyx_PyObject_GetSlice(__pyx_t_1, 0, -2L, NULL, NULL, &__pyx_mstate_global->__pyx_slice[1], 0, 1, 1); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 791, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  if (__Pyx_PyObject_SetAttrStr(__pyx_v_self, __pyx_mstate_global->__pyx_n_u_indent, __pyx_t_2) < (0)) __PYX_ERR(0, 791, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
/* … */
  __pyx_mstate_global->__pyx_slice[1] = PySlice_New(Py_None, __pyx_mstate_global->__pyx_int_neg_2, Py_None); if (unlikely(!__pyx_mstate_global->__pyx_slice[1])) __PYX_ERR(0, 791, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_mstate_global->__pyx_slice[1]);
  __Pyx_GIVEREF(__pyx_mstate_global->__pyx_slice[1]);
```

</details>

L792  ⚪  (score=0)
```python
```
L793  🔴  (score=52)
```python
    def __call__(self, tree, phase=None):
```
<details><summary>Show generated C (score=52)</summary>

```c
/* Python wrapper */
static PyObject *__pyx_pw_6Cython_8Compiler_7Visitor_9PrintTree_7__call__(PyObject *__pyx_self, 
#if CYTHON_METH_FASTCALL
PyObject *const *__pyx_args, Py_ssize_t __pyx_nargs, PyObject *__pyx_kwds
#else
PyObject *__pyx_args, PyObject *__pyx_kwds
#endif
); /*proto*/
PyDoc_STRVAR(__pyx_doc_6Cython_8Compiler_7Visitor_9PrintTree_6__call__, "File: Cython/Compiler/Visitor.py (starting at line 793)");
static PyMethodDef __pyx_mdef_6Cython_8Compiler_7Visitor_9PrintTree_7__call__ = {"__call__", (PyCFunction)(void(*)(void))(__Pyx_PyCFunction_FastCallWithKeywords)__pyx_pw_6Cython_8Compiler_7Visitor_9PrintTree_7__call__, __Pyx_METH_FASTCALL|METH_KEYWORDS, __pyx_doc_6Cython_8Compiler_7Visitor_9PrintTree_6__call__};
static PyObject *__pyx_pw_6Cython_8Compiler_7Visitor_9PrintTree_7__call__(PyObject *__pyx_self, 
#if CYTHON_METH_FASTCALL
PyObject *const *__pyx_args, Py_ssize_t __pyx_nargs, PyObject *__pyx_kwds
#else
PyObject *__pyx_args, PyObject *__pyx_kwds
#endif
) {
  PyObject *__pyx_v_self = 0;
  PyObject *__pyx_v_tree = 0;
  PyObject *__pyx_v_phase = 0;
  #if !CYTHON_METH_FASTCALL
  CYTHON_UNUSED Py_ssize_t __pyx_nargs;
  #endif
  CYTHON_UNUSED PyObject *const *__pyx_kwvalues;
  PyObject *__pyx_r = 0;
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("__call__ (wrapper)", 0);
  #if !CYTHON_METH_FASTCALL
  #if CYTHON_ASSUME_SAFE_SIZE
  __pyx_nargs = PyTuple_GET_SIZE(__pyx_args);
  #else
  __pyx_nargs = PyTuple_Size(__pyx_args); if (unlikely(__pyx_nargs < 0)) return NULL;
  #endif
  #endif
  __pyx_kwvalues = __Pyx_KwValues_FASTCALL(__pyx_args, __pyx_nargs);
  {
    PyObject ** const __pyx_pyargnames[] = {&__pyx_mstate_global->__pyx_n_u_self,&__pyx_mstate_global->__pyx_n_u_tree,&__pyx_mstate_global->__pyx_n_u_phase,0};
  PyObject* values[3] = {0,0,0};
    const Py_ssize_t __pyx_kwds_len = (__pyx_kwds) ? __Pyx_NumKwargs_FASTCALL(__pyx_kwds) : 0;
    if (unlikely(__pyx_kwds_len) < 0) __PYX_ERR(0, 793, __pyx_L3_error)
    if (__pyx_kwds_len > 0) {
      switch (__pyx_nargs) {
        case  3:
        values[2] = __Pyx_ArgRef_FASTCALL(__pyx_args, 2);
        if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[2])) __PYX_ERR(0, 793, __pyx_L3_error)
        CYTHON_FALLTHROUGH;
        case  2:
        values[1] = __Pyx_ArgRef_FASTCALL(__pyx_args, 1);
        if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[1])) __PYX_ERR(0, 793, __pyx_L3_error)
        CYTHON_FALLTHROUGH;
        case  1:
        values[0] = __Pyx_ArgRef_FASTCALL(__pyx_args, 0);
        if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[0])) __PYX_ERR(0, 793, __pyx_L3_error)
        CYTHON_FALLTHROUGH;
        case  0: break;
        default: goto __pyx_L5_argtuple_error;
      }
      const Py_ssize_t kwd_pos_args = __pyx_nargs;
      if (__Pyx_ParseKeywords(__pyx_kwds, __pyx_kwvalues, __pyx_pyargnames, 0, values, kwd_pos_args, __pyx_kwds_len, "__call__", 0) < (0)) __PYX_ERR(0, 793, __pyx_L3_error)
      if (!values[2]) values[2] = __Pyx_NewRef(((PyObject *)Py_None));
      for (Py_ssize_t i = __pyx_nargs; i < 2; i++) {
        if (unlikely(!values[i])) { __Pyx_RaiseArgtupleInvalid("__call__", 0, 2, 3, i); __PYX_ERR(0, 793, __pyx_L3_error) }
      }
    } else {
      switch (__pyx_nargs) {
        case  3:
        values[2] = __Pyx_ArgRef_FASTCALL(__pyx_args, 2);
        if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[2])) __PYX_ERR(0, 793, __pyx_L3_error)
        CYTHON_FALLTHROUGH;
        case  2:
        values[1] = __Pyx_ArgRef_FASTCALL(__pyx_args, 1);
        if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[1])) __PYX_ERR(0, 793, __pyx_L3_error)
        values[0] = __Pyx_ArgRef_FASTCALL(__pyx_args, 0);
        if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[0])) __PYX_ERR(0, 793, __pyx_L3_error)
        break;
        default: goto __pyx_L5_argtuple_error;
      }
      if (!values[2]) values[2] = __Pyx_NewRef(((PyObject *)Py_None));
    }
    __pyx_v_self = values[0];
    __pyx_v_tree = values[1];
    __pyx_v_phase = values[2];
  }
  goto __pyx_L6_skip;
  __pyx_L5_argtuple_error:;
  __Pyx_RaiseArgtupleInvalid("__call__", 0, 2, 3, __pyx_nargs); __PYX_ERR(0, 793, __pyx_L3_error)
  __pyx_L6_skip:;
  goto __pyx_L4_argument_unpacking_done;
  __pyx_L3_error:;
  for (Py_ssize_t __pyx_temp=0; __pyx_temp < (Py_ssize_t)(sizeof(values)/sizeof(values[0])); ++__pyx_temp) {
    Py_XDECREF(values[__pyx_temp]);
  }
  __Pyx_AddTraceback("Cython.Compiler.Visitor.PrintTree.__call__", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __Pyx_RefNannyFinishContext();
  return NULL;
  __pyx_L4_argument_unpacking_done:;
  __pyx_r = __pyx_pf_6Cython_8Compiler_7Visitor_9PrintTree_6__call__(__pyx_self, __pyx_v_self, __pyx_v_tree, __pyx_v_phase);

  /* function exit code */
  for (Py_ssize_t __pyx_temp=0; __pyx_temp < (Py_ssize_t)(sizeof(values)/sizeof(values[0])); ++__pyx_temp) {
    Py_XDECREF(values[__pyx_temp]);
  }
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}

static PyObject *__pyx_pf_6Cython_8Compiler_7Visitor_9PrintTree_6__call__(CYTHON_UNUSED PyObject *__pyx_self, PyObject *__pyx_v_self, PyObject *__pyx_v_tree, PyObject *__pyx_v_phase) {
  PyObject *__pyx_r = NULL;
/* … */
  /* function exit code */
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_t_1);
  __Pyx_XDECREF(__pyx_t_2);
  __Pyx_XDECREF(__pyx_t_3);
  __Pyx_AddTraceback("Cython.Compiler.Visitor.PrintTree.__call__", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_r = NULL;
  __pyx_L0:;
  __Pyx_XGIVEREF(__pyx_r);
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}
/* … */
  __pyx_t_2 = __Pyx_CyFunction_New(&__pyx_mdef_6Cython_8Compiler_7Visitor_9PrintTree_7__call__, 0, __pyx_mstate_global->__pyx_n_u_PrintTree___call, NULL, __pyx_mstate_global->__pyx_n_u_Cython_Compiler_Visitor, __pyx_mstate_global->__pyx_d, ((PyObject *)__pyx_mstate_global->__pyx_codeobj_tab[62])); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 793, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  #if CYTHON_COMPILING_IN_CPYTHON && PY_VERSION_HEX >= 0x030E0000
  PyUnstable_Object_EnableDeferredRefcount(__pyx_t_2);
  #endif
  __Pyx_CyFunction_SetDefaultsTuple(__pyx_t_2, __pyx_mstate_global->__pyx_tuple[9]);
  if (__Pyx_SetNameInClass(__pyx_t_6, __pyx_mstate_global->__pyx_n_u_call, __pyx_t_2) < (0)) __PYX_ERR(0, 793, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
```

</details>

L794  🟠  (score=7)
```python
        print("Parse tree dump at phase '%s'" % phase)
```
<details><summary>Show generated C (score=7)</summary>

```c
  __pyx_t_2 = NULL;
  __pyx_t_3 = __Pyx_PyUnicode_FormatSafe(__pyx_mstate_global->__pyx_kp_u_Parse_tree_dump_at_phase_s, __pyx_v_phase); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 794, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_3);
  __pyx_t_4 = 1;
  {
    PyObject *__pyx_callargs[2] = {__pyx_t_2, __pyx_t_3};
    __pyx_t_1 = __Pyx_PyObject_FastCall((PyObject*)__pyx_builtin_print, __pyx_callargs+__pyx_t_4, (2-__pyx_t_4) | (__pyx_t_4*__Pyx_PY_VECTORCALL_ARGUMENTS_OFFSET));
    __Pyx_XDECREF(__pyx_t_2); __pyx_t_2 = 0;
    __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
    if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 794, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_1);
  }
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
```

</details>

L795  🟠  (score=5)
```python
        self.visit(tree)
```
<details><summary>Show generated C (score=5)</summary>

```c
  __pyx_t_3 = __pyx_v_self;
  __Pyx_INCREF(__pyx_t_3);
  __pyx_t_4 = 0;
  {
    PyObject *__pyx_callargs[2] = {__pyx_t_3, __pyx_v_tree};
    __pyx_t_1 = __Pyx_PyObject_FastCallMethod((PyObject*)__pyx_mstate_global->__pyx_n_u_visit_2, __pyx_callargs+__pyx_t_4, (2-__pyx_t_4) | (1*__Pyx_PY_VECTORCALL_ARGUMENTS_OFFSET));
    __Pyx_XDECREF(__pyx_t_3); __pyx_t_3 = 0;
    if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 795, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_1);
  }
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
```

</details>

L796  🟡  (score=2)
```python
        return tree
```
<details><summary>Show generated C (score=2)</summary>

```c
  __Pyx_XDECREF(__pyx_r);
  __Pyx_INCREF(__pyx_v_tree);
  __pyx_r = __pyx_v_tree;
  goto __pyx_L0;
```

</details>

L797  ⚪  (score=0)
```python
```
L798  ⚪  (score=0)
```python
    # Don't do anything about process_list, the defaults gives
```
L799  ⚪  (score=0)
```python
    # nice-looking name[idx] nodes which will visually appear
```
L800  ⚪  (score=0)
```python
    # under the parent-node, not displaying the list itself in
```
L801  ⚪  (score=0)
```python
    # the hierarchy.
```
L802  🔴  (score=41)
```python
    def visit_Node(self, node):
```
<details><summary>Show generated C (score=41)</summary>

```c
/* Python wrapper */
static PyObject *__pyx_pw_6Cython_8Compiler_7Visitor_9PrintTree_9visit_Node(PyObject *__pyx_self, 
#if CYTHON_METH_FASTCALL
PyObject *const *__pyx_args, Py_ssize_t __pyx_nargs, PyObject *__pyx_kwds
#else
PyObject *__pyx_args, PyObject *__pyx_kwds
#endif
); /*proto*/
PyDoc_STRVAR(__pyx_doc_6Cython_8Compiler_7Visitor_9PrintTree_8visit_Node, "File: Cython/Compiler/Visitor.py (starting at line 802)");
static PyMethodDef __pyx_mdef_6Cython_8Compiler_7Visitor_9PrintTree_9visit_Node = {"visit_Node", (PyCFunction)(void(*)(void))(__Pyx_PyCFunction_FastCallWithKeywords)__pyx_pw_6Cython_8Compiler_7Visitor_9PrintTree_9visit_Node, __Pyx_METH_FASTCALL|METH_KEYWORDS, __pyx_doc_6Cython_8Compiler_7Visitor_9PrintTree_8visit_Node};
static PyObject *__pyx_pw_6Cython_8Compiler_7Visitor_9PrintTree_9visit_Node(PyObject *__pyx_self, 
#if CYTHON_METH_FASTCALL
PyObject *const *__pyx_args, Py_ssize_t __pyx_nargs, PyObject *__pyx_kwds
#else
PyObject *__pyx_args, PyObject *__pyx_kwds
#endif
) {
  PyObject *__pyx_v_self = 0;
  PyObject *__pyx_v_node = 0;
  #if !CYTHON_METH_FASTCALL
  CYTHON_UNUSED Py_ssize_t __pyx_nargs;
  #endif
  CYTHON_UNUSED PyObject *const *__pyx_kwvalues;
  PyObject *__pyx_r = 0;
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("visit_Node (wrapper)", 0);
  #if !CYTHON_METH_FASTCALL
  #if CYTHON_ASSUME_SAFE_SIZE
  __pyx_nargs = PyTuple_GET_SIZE(__pyx_args);
  #else
  __pyx_nargs = PyTuple_Size(__pyx_args); if (unlikely(__pyx_nargs < 0)) return NULL;
  #endif
  #endif
  __pyx_kwvalues = __Pyx_KwValues_FASTCALL(__pyx_args, __pyx_nargs);
  {
    PyObject ** const __pyx_pyargnames[] = {&__pyx_mstate_global->__pyx_n_u_self,&__pyx_mstate_global->__pyx_n_u_node,0};
  PyObject* values[2] = {0,0};
    const Py_ssize_t __pyx_kwds_len = (__pyx_kwds) ? __Pyx_NumKwargs_FASTCALL(__pyx_kwds) : 0;
    if (unlikely(__pyx_kwds_len) < 0) __PYX_ERR(0, 802, __pyx_L3_error)
    if (__pyx_kwds_len > 0) {
      switch (__pyx_nargs) {
        case  2:
        values[1] = __Pyx_ArgRef_FASTCALL(__pyx_args, 1);
        if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[1])) __PYX_ERR(0, 802, __pyx_L3_error)
        CYTHON_FALLTHROUGH;
        case  1:
        values[0] = __Pyx_ArgRef_FASTCALL(__pyx_args, 0);
        if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[0])) __PYX_ERR(0, 802, __pyx_L3_error)
        CYTHON_FALLTHROUGH;
        case  0: break;
        default: goto __pyx_L5_argtuple_error;
      }
      const Py_ssize_t kwd_pos_args = __pyx_nargs;
      if (__Pyx_ParseKeywords(__pyx_kwds, __pyx_kwvalues, __pyx_pyargnames, 0, values, kwd_pos_args, __pyx_kwds_len, "visit_Node", 0) < (0)) __PYX_ERR(0, 802, __pyx_L3_error)
      for (Py_ssize_t i = __pyx_nargs; i < 2; i++) {
        if (unlikely(!values[i])) { __Pyx_RaiseArgtupleInvalid("visit_Node", 1, 2, 2, i); __PYX_ERR(0, 802, __pyx_L3_error) }
      }
    } else if (unlikely(__pyx_nargs != 2)) {
      goto __pyx_L5_argtuple_error;
    } else {
      values[0] = __Pyx_ArgRef_FASTCALL(__pyx_args, 0);
      if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[0])) __PYX_ERR(0, 802, __pyx_L3_error)
      values[1] = __Pyx_ArgRef_FASTCALL(__pyx_args, 1);
      if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[1])) __PYX_ERR(0, 802, __pyx_L3_error)
    }
    __pyx_v_self = values[0];
    __pyx_v_node = values[1];
  }
  goto __pyx_L6_skip;
  __pyx_L5_argtuple_error:;
  __Pyx_RaiseArgtupleInvalid("visit_Node", 1, 2, 2, __pyx_nargs); __PYX_ERR(0, 802, __pyx_L3_error)
  __pyx_L6_skip:;
  goto __pyx_L4_argument_unpacking_done;
  __pyx_L3_error:;
  for (Py_ssize_t __pyx_temp=0; __pyx_temp < (Py_ssize_t)(sizeof(values)/sizeof(values[0])); ++__pyx_temp) {
    Py_XDECREF(values[__pyx_temp]);
  }
  __Pyx_AddTraceback("Cython.Compiler.Visitor.PrintTree.visit_Node", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __Pyx_RefNannyFinishContext();
  return NULL;
  __pyx_L4_argument_unpacking_done:;
  __pyx_r = __pyx_pf_6Cython_8Compiler_7Visitor_9PrintTree_8visit_Node(__pyx_self, __pyx_v_self, __pyx_v_node);
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

static PyObject *__pyx_pf_6Cython_8Compiler_7Visitor_9PrintTree_8visit_Node(CYTHON_UNUSED PyObject *__pyx_self, PyObject *__pyx_v_self, PyObject *__pyx_v_node) {
  PyObject *__pyx_r = NULL;
/* … */
  /* function exit code */
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_t_1);
  __Pyx_XDECREF(__pyx_t_2);
  __Pyx_AddTraceback("Cython.Compiler.Visitor.PrintTree.visit_Node", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_r = NULL;
  __pyx_L0:;
  __Pyx_XGIVEREF(__pyx_r);
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}
/* … */
  __pyx_t_2 = __Pyx_CyFunction_New(&__pyx_mdef_6Cython_8Compiler_7Visitor_9PrintTree_9visit_Node, 0, __pyx_mstate_global->__pyx_n_u_PrintTree_visit_Node, NULL, __pyx_mstate_global->__pyx_n_u_Cython_Compiler_Visitor, __pyx_mstate_global->__pyx_d, ((PyObject *)__pyx_mstate_global->__pyx_codeobj_tab[63])); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 802, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  #if CYTHON_COMPILING_IN_CPYTHON && PY_VERSION_HEX >= 0x030E0000
  PyUnstable_Object_EnableDeferredRefcount(__pyx_t_2);
  #endif
  if (__Pyx_SetNameInClass(__pyx_t_6, __pyx_mstate_global->__pyx_n_u_visit_Node, __pyx_t_2) < (0)) __PYX_ERR(0, 802, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
```

</details>

L803  🟠  (score=5)
```python
        self._print_node(node)
```
<details><summary>Show generated C (score=5)</summary>

```c
  __pyx_t_2 = __pyx_v_self;
  __Pyx_INCREF(__pyx_t_2);
  __pyx_t_3 = 0;
  {
    PyObject *__pyx_callargs[2] = {__pyx_t_2, __pyx_v_node};
    __pyx_t_1 = __Pyx_PyObject_FastCallMethod((PyObject*)__pyx_mstate_global->__pyx_n_u_print_node, __pyx_callargs+__pyx_t_3, (2-__pyx_t_3) | (1*__Pyx_PY_VECTORCALL_ARGUMENTS_OFFSET));
    __Pyx_XDECREF(__pyx_t_2); __pyx_t_2 = 0;
    if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 803, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_1);
  }
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
```

</details>

L804  🟠  (score=5)
```python
        self.indent()
```
<details><summary>Show generated C (score=5)</summary>

```c
  __pyx_t_2 = __pyx_v_self;
  __Pyx_INCREF(__pyx_t_2);
  __pyx_t_3 = 0;
  {
    PyObject *__pyx_callargs[2] = {__pyx_t_2, NULL};
    __pyx_t_1 = __Pyx_PyObject_FastCallMethod((PyObject*)__pyx_mstate_global->__pyx_n_u_indent_2, __pyx_callargs+__pyx_t_3, (1-__pyx_t_3) | (1*__Pyx_PY_VECTORCALL_ARGUMENTS_OFFSET));
    __Pyx_XDECREF(__pyx_t_2); __pyx_t_2 = 0;
    if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 804, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_1);
  }
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
```

</details>

L805  🟠  (score=5)
```python
        self.visitchildren(node)
```
<details><summary>Show generated C (score=5)</summary>

```c
  __pyx_t_2 = __pyx_v_self;
  __Pyx_INCREF(__pyx_t_2);
  __pyx_t_3 = 0;
  {
    PyObject *__pyx_callargs[2] = {__pyx_t_2, __pyx_v_node};
    __pyx_t_1 = __Pyx_PyObject_FastCallMethod((PyObject*)__pyx_mstate_global->__pyx_n_u_visitchildren, __pyx_callargs+__pyx_t_3, (2-__pyx_t_3) | (1*__Pyx_PY_VECTORCALL_ARGUMENTS_OFFSET));
    __Pyx_XDECREF(__pyx_t_2); __pyx_t_2 = 0;
    if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 805, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_1);
  }
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
```

</details>

L806  🟠  (score=5)
```python
        self.unindent()
```
<details><summary>Show generated C (score=5)</summary>

```c
  __pyx_t_2 = __pyx_v_self;
  __Pyx_INCREF(__pyx_t_2);
  __pyx_t_3 = 0;
  {
    PyObject *__pyx_callargs[2] = {__pyx_t_2, NULL};
    __pyx_t_1 = __Pyx_PyObject_FastCallMethod((PyObject*)__pyx_mstate_global->__pyx_n_u_unindent, __pyx_callargs+__pyx_t_3, (1-__pyx_t_3) | (1*__Pyx_PY_VECTORCALL_ARGUMENTS_OFFSET));
    __Pyx_XDECREF(__pyx_t_2); __pyx_t_2 = 0;
    if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 806, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_1);
  }
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
```

</details>

L807  🟡  (score=2)
```python
        return node
```
<details><summary>Show generated C (score=2)</summary>

```c
  __Pyx_XDECREF(__pyx_r);
  __Pyx_INCREF(__pyx_v_node);
  __pyx_r = __pyx_v_node;
  goto __pyx_L0;
```

</details>

L808  ⚪  (score=0)
```python
```
L809  🔴  (score=46)
```python
    def visit_CloneNode(self, node):
```
<details><summary>Show generated C (score=46)</summary>

```c
/* Python wrapper */
static PyObject *__pyx_pw_6Cython_8Compiler_7Visitor_9PrintTree_11visit_CloneNode(PyObject *__pyx_self, 
#if CYTHON_METH_FASTCALL
PyObject *const *__pyx_args, Py_ssize_t __pyx_nargs, PyObject *__pyx_kwds
#else
PyObject *__pyx_args, PyObject *__pyx_kwds
#endif
); /*proto*/
PyDoc_STRVAR(__pyx_doc_6Cython_8Compiler_7Visitor_9PrintTree_10visit_CloneNode, "File: Cython/Compiler/Visitor.py (starting at line 809)");
static PyMethodDef __pyx_mdef_6Cython_8Compiler_7Visitor_9PrintTree_11visit_CloneNode = {"visit_CloneNode", (PyCFunction)(void(*)(void))(__Pyx_PyCFunction_FastCallWithKeywords)__pyx_pw_6Cython_8Compiler_7Visitor_9PrintTree_11visit_CloneNode, __Pyx_METH_FASTCALL|METH_KEYWORDS, __pyx_doc_6Cython_8Compiler_7Visitor_9PrintTree_10visit_CloneNode};
static PyObject *__pyx_pw_6Cython_8Compiler_7Visitor_9PrintTree_11visit_CloneNode(PyObject *__pyx_self, 
#if CYTHON_METH_FASTCALL
PyObject *const *__pyx_args, Py_ssize_t __pyx_nargs, PyObject *__pyx_kwds
#else
PyObject *__pyx_args, PyObject *__pyx_kwds
#endif
) {
  PyObject *__pyx_v_self = 0;
  PyObject *__pyx_v_node = 0;
  #if !CYTHON_METH_FASTCALL
  CYTHON_UNUSED Py_ssize_t __pyx_nargs;
  #endif
  CYTHON_UNUSED PyObject *const *__pyx_kwvalues;
  PyObject *__pyx_r = 0;
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("visit_CloneNode (wrapper)", 0);
  #if !CYTHON_METH_FASTCALL
  #if CYTHON_ASSUME_SAFE_SIZE
  __pyx_nargs = PyTuple_GET_SIZE(__pyx_args);
  #else
  __pyx_nargs = PyTuple_Size(__pyx_args); if (unlikely(__pyx_nargs < 0)) return NULL;
  #endif
  #endif
  __pyx_kwvalues = __Pyx_KwValues_FASTCALL(__pyx_args, __pyx_nargs);
  {
    PyObject ** const __pyx_pyargnames[] = {&__pyx_mstate_global->__pyx_n_u_self,&__pyx_mstate_global->__pyx_n_u_node,0};
  PyObject* values[2] = {0,0};
    const Py_ssize_t __pyx_kwds_len = (__pyx_kwds) ? __Pyx_NumKwargs_FASTCALL(__pyx_kwds) : 0;
    if (unlikely(__pyx_kwds_len) < 0) __PYX_ERR(0, 809, __pyx_L3_error)
    if (__pyx_kwds_len > 0) {
      switch (__pyx_nargs) {
        case  2:
        values[1] = __Pyx_ArgRef_FASTCALL(__pyx_args, 1);
        if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[1])) __PYX_ERR(0, 809, __pyx_L3_error)
        CYTHON_FALLTHROUGH;
        case  1:
        values[0] = __Pyx_ArgRef_FASTCALL(__pyx_args, 0);
        if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[0])) __PYX_ERR(0, 809, __pyx_L3_error)
        CYTHON_FALLTHROUGH;
        case  0: break;
        default: goto __pyx_L5_argtuple_error;
      }
      const Py_ssize_t kwd_pos_args = __pyx_nargs;
      if (__Pyx_ParseKeywords(__pyx_kwds, __pyx_kwvalues, __pyx_pyargnames, 0, values, kwd_pos_args, __pyx_kwds_len, "visit_CloneNode", 0) < (0)) __PYX_ERR(0, 809, __pyx_L3_error)
      for (Py_ssize_t i = __pyx_nargs; i < 2; i++) {
        if (unlikely(!values[i])) { __Pyx_RaiseArgtupleInvalid("visit_CloneNode", 1, 2, 2, i); __PYX_ERR(0, 809, __pyx_L3_error) }
      }
    } else if (unlikely(__pyx_nargs != 2)) {
      goto __pyx_L5_argtuple_error;
    } else {
      values[0] = __Pyx_ArgRef_FASTCALL(__pyx_args, 0);
      if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[0])) __PYX_ERR(0, 809, __pyx_L3_error)
      values[1] = __Pyx_ArgRef_FASTCALL(__pyx_args, 1);
      if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[1])) __PYX_ERR(0, 809, __pyx_L3_error)
    }
    __pyx_v_self = values[0];
    __pyx_v_node = values[1];
  }
  goto __pyx_L6_skip;
  __pyx_L5_argtuple_error:;
  __Pyx_RaiseArgtupleInvalid("visit_CloneNode", 1, 2, 2, __pyx_nargs); __PYX_ERR(0, 809, __pyx_L3_error)
  __pyx_L6_skip:;
  goto __pyx_L4_argument_unpacking_done;
  __pyx_L3_error:;
  for (Py_ssize_t __pyx_temp=0; __pyx_temp < (Py_ssize_t)(sizeof(values)/sizeof(values[0])); ++__pyx_temp) {
    Py_XDECREF(values[__pyx_temp]);
  }
  __Pyx_AddTraceback("Cython.Compiler.Visitor.PrintTree.visit_CloneNode", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __Pyx_RefNannyFinishContext();
  return NULL;
  __pyx_L4_argument_unpacking_done:;
  __pyx_r = __pyx_pf_6Cython_8Compiler_7Visitor_9PrintTree_10visit_CloneNode(__pyx_self, __pyx_v_self, __pyx_v_node);
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

static PyObject *__pyx_pf_6Cython_8Compiler_7Visitor_9PrintTree_10visit_CloneNode(CYTHON_UNUSED PyObject *__pyx_self, PyObject *__pyx_v_self, PyObject *__pyx_v_node) {
  PyObject *__pyx_v_line = NULL;
  PyObject *__pyx_r = NULL;
/* … */
  /* function exit code */
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_t_1);
  __Pyx_XDECREF(__pyx_t_2);
  __Pyx_XDECREF(__pyx_t_6);
  __Pyx_XDECREF(__pyx_t_7);
  __Pyx_XDECREF(__pyx_t_8);
  __Pyx_XDECREF(__pyx_t_9);
  __Pyx_AddTraceback("Cython.Compiler.Visitor.PrintTree.visit_CloneNode", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_r = NULL;
  __pyx_L0:;
  __Pyx_XDECREF(__pyx_v_line);
  __Pyx_XGIVEREF(__pyx_r);
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}
/* … */
  __pyx_t_2 = __Pyx_CyFunction_New(&__pyx_mdef_6Cython_8Compiler_7Visitor_9PrintTree_11visit_CloneNode, 0, __pyx_mstate_global->__pyx_n_u_PrintTree_visit_CloneNode, NULL, __pyx_mstate_global->__pyx_n_u_Cython_Compiler_Visitor, __pyx_mstate_global->__pyx_d, ((PyObject *)__pyx_mstate_global->__pyx_codeobj_tab[64])); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 809, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  #if CYTHON_COMPILING_IN_CPYTHON && PY_VERSION_HEX >= 0x030E0000
  PyUnstable_Object_EnableDeferredRefcount(__pyx_t_2);
  #endif
  if (__Pyx_SetNameInClass(__pyx_t_6, __pyx_mstate_global->__pyx_n_u_visit_CloneNode, __pyx_t_2) < (0)) __PYX_ERR(0, 809, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
```

</details>

L810  🟠  (score=5)
```python
        self._print_node(node)
```
<details><summary>Show generated C (score=5)</summary>

```c
  __pyx_t_2 = __pyx_v_self;
  __Pyx_INCREF(__pyx_t_2);
  __pyx_t_3 = 0;
  {
    PyObject *__pyx_callargs[2] = {__pyx_t_2, __pyx_v_node};
    __pyx_t_1 = __Pyx_PyObject_FastCallMethod((PyObject*)__pyx_mstate_global->__pyx_n_u_print_node, __pyx_callargs+__pyx_t_3, (2-__pyx_t_3) | (1*__Pyx_PY_VECTORCALL_ARGUMENTS_OFFSET));
    __Pyx_XDECREF(__pyx_t_2); __pyx_t_2 = 0;
    if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 810, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_1);
  }
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
```

</details>

L811  🟠  (score=5)
```python
        self.indent()
```
<details><summary>Show generated C (score=5)</summary>

```c
  __pyx_t_2 = __pyx_v_self;
  __Pyx_INCREF(__pyx_t_2);
  __pyx_t_3 = 0;
  {
    PyObject *__pyx_callargs[2] = {__pyx_t_2, NULL};
    __pyx_t_1 = __Pyx_PyObject_FastCallMethod((PyObject*)__pyx_mstate_global->__pyx_n_u_indent_2, __pyx_callargs+__pyx_t_3, (1-__pyx_t_3) | (1*__Pyx_PY_VECTORCALL_ARGUMENTS_OFFSET));
    __Pyx_XDECREF(__pyx_t_2); __pyx_t_2 = 0;
    if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 811, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_1);
  }
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
```

</details>

L812  🟠  (score=5)
```python
        line = node.pos[1]
```
<details><summary>Show generated C (score=5)</summary>

```c
  __pyx_t_1 = __Pyx_PyObject_GetAttrStr(__pyx_v_node, __pyx_mstate_global->__pyx_n_u_pos); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 812, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __pyx_t_2 = __Pyx_GetItemInt(__pyx_t_1, 1, long, 1, __Pyx_PyLong_From_long, 0, 0, 1, 1, __Pyx_ReferenceSharing_OwnStrongReference); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 812, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __pyx_v_line = __pyx_t_2;
  __pyx_t_2 = 0;
```

</details>

L813  🔴  (score=31)
```python
        if self._line_range is None or self._line_range[0] <= line <= self._line_range[1]:
```
<details><summary>Show generated C (score=31)</summary>

```c
  __pyx_t_2 = __Pyx_PyObject_GetAttrStr(__pyx_v_self, __pyx_mstate_global->__pyx_n_u_line_range); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 813, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __pyx_t_5 = (__pyx_t_2 == Py_None);
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  if (!__pyx_t_5) {
  } else {
    __pyx_t_4 = __pyx_t_5;
    goto __pyx_L4_bool_binop_done;
  }
  __pyx_t_2 = __Pyx_PyObject_GetAttrStr(__pyx_v_self, __pyx_mstate_global->__pyx_n_u_line_range); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 813, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __pyx_t_1 = __Pyx_GetItemInt(__pyx_t_2, 0, long, 1, __Pyx_PyLong_From_long, 0, 0, 1, 1, __Pyx_ReferenceSharing_OwnStrongReference); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 813, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __pyx_t_2 = PyObject_RichCompare(__pyx_t_1, __pyx_v_line, Py_LE); __Pyx_XGOTREF(__pyx_t_2); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 813, __pyx_L1_error)
  if (__Pyx_PyObject_IsTrue(__pyx_t_2)) {
    __Pyx_DECREF(__pyx_t_2);
    __pyx_t_6 = __Pyx_PyObject_GetAttrStr(__pyx_v_self, __pyx_mstate_global->__pyx_n_u_line_range); if (unlikely(!__pyx_t_6)) __PYX_ERR(0, 813, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_6);
    __pyx_t_7 = __Pyx_GetItemInt(__pyx_t_6, 1, long, 1, __Pyx_PyLong_From_long, 0, 0, 1, 1, __Pyx_ReferenceSharing_OwnStrongReference); if (unlikely(!__pyx_t_7)) __PYX_ERR(0, 813, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_7);
    __Pyx_DECREF(__pyx_t_6); __pyx_t_6 = 0;
    __pyx_t_2 = PyObject_RichCompare(__pyx_v_line, __pyx_t_7, Py_LE); __Pyx_XGOTREF(__pyx_t_2); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 813, __pyx_L1_error)
    __Pyx_DECREF(__pyx_t_7); __pyx_t_7 = 0;
  }
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __pyx_t_5 = __Pyx_PyObject_IsTrue(__pyx_t_2); if (unlikely((__pyx_t_5 < 0))) __PYX_ERR(0, 813, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __pyx_t_4 = __pyx_t_5;
  __pyx_L4_bool_binop_done:;
  if (__pyx_t_4) {
/* … */
  }
```

</details>

L814  🔴  (score=43)
```python
            print("%s- %s: %s" % (self._indent, 'arg', self.repr_of(node.arg)))
```
<details><summary>Show generated C (score=43)</summary>

```c
    __pyx_t_1 = NULL;
    __pyx_t_7 = __Pyx_PyObject_GetAttrStr(__pyx_v_self, __pyx_mstate_global->__pyx_n_u_indent); if (unlikely(!__pyx_t_7)) __PYX_ERR(0, 814, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_7);
    __pyx_t_6 = __Pyx_PyObject_FormatSimpleAndDecref(PyObject_Str(__pyx_t_7), __pyx_mstate_global->__pyx_empty_unicode); if (unlikely(!__pyx_t_6)) __PYX_ERR(0, 814, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_6);
    __Pyx_DECREF(__pyx_t_7); __pyx_t_7 = 0;
    __pyx_t_7 = __Pyx_PyObject_GetAttrStr(__pyx_v_self, __pyx_mstate_global->__pyx_n_u_repr_of); if (unlikely(!__pyx_t_7)) __PYX_ERR(0, 814, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_7);
    __pyx_t_8 = __Pyx_PyObject_GetAttrStr(__pyx_v_node, __pyx_mstate_global->__pyx_n_u_arg); if (unlikely(!__pyx_t_8)) __PYX_ERR(0, 814, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_8);
    __pyx_t_9 = __Pyx_PyObject_CallOneArg(__pyx_t_7, __pyx_t_8); if (unlikely(!__pyx_t_9)) __PYX_ERR(0, 814, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_9);
    __Pyx_DECREF(__pyx_t_7); __pyx_t_7 = 0;
    __Pyx_DECREF(__pyx_t_8); __pyx_t_8 = 0;
    __pyx_t_8 = __Pyx_PyObject_FormatSimpleAndDecref(PyObject_Str(__pyx_t_9), __pyx_mstate_global->__pyx_empty_unicode); if (unlikely(!__pyx_t_8)) __PYX_ERR(0, 814, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_8);
    __Pyx_DECREF(__pyx_t_9); __pyx_t_9 = 0;
    __pyx_t_10[0] = __pyx_t_6;
    __pyx_t_10[1] = __pyx_mstate_global->__pyx_kp_u_arg_2;
    __pyx_t_10[2] = __pyx_t_8;
    __pyx_t_9 = __Pyx_PyUnicode_Join(__pyx_t_10, 3, __Pyx_PyUnicode_GET_LENGTH(__pyx_t_6) + 7 + __Pyx_PyUnicode_GET_LENGTH(__pyx_t_8), 127 | __Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_6) | __Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_8));
    if (unlikely(!__pyx_t_9)) __PYX_ERR(0, 814, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_9);
    __Pyx_DECREF(__pyx_t_6); __pyx_t_6 = 0;
    __Pyx_DECREF(__pyx_t_8); __pyx_t_8 = 0;
    __pyx_t_3 = 1;
    {
      PyObject *__pyx_callargs[2] = {__pyx_t_1, __pyx_t_9};
      __pyx_t_2 = __Pyx_PyObject_FastCall((PyObject*)__pyx_builtin_print, __pyx_callargs+__pyx_t_3, (2-__pyx_t_3) | (__pyx_t_3*__Pyx_PY_VECTORCALL_ARGUMENTS_OFFSET));
      __Pyx_XDECREF(__pyx_t_1); __pyx_t_1 = 0;
      __Pyx_DECREF(__pyx_t_9); __pyx_t_9 = 0;
      if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 814, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_2);
    }
    __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
```

</details>

L815  🟠  (score=5)
```python
        self.indent()
```
<details><summary>Show generated C (score=5)</summary>

```c
  __pyx_t_9 = __pyx_v_self;
  __Pyx_INCREF(__pyx_t_9);
  __pyx_t_3 = 0;
  {
    PyObject *__pyx_callargs[2] = {__pyx_t_9, NULL};
    __pyx_t_2 = __Pyx_PyObject_FastCallMethod((PyObject*)__pyx_mstate_global->__pyx_n_u_indent_2, __pyx_callargs+__pyx_t_3, (1-__pyx_t_3) | (1*__Pyx_PY_VECTORCALL_ARGUMENTS_OFFSET));
    __Pyx_XDECREF(__pyx_t_9); __pyx_t_9 = 0;
    if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 815, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_2);
  }
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
```

</details>

L816  🟠  (score=8)
```python
        self.visitchildren(node.arg)
```
<details><summary>Show generated C (score=8)</summary>

```c
  __pyx_t_9 = __pyx_v_self;
  __Pyx_INCREF(__pyx_t_9);
  __pyx_t_1 = __Pyx_PyObject_GetAttrStr(__pyx_v_node, __pyx_mstate_global->__pyx_n_u_arg); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 816, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __pyx_t_3 = 0;
  {
    PyObject *__pyx_callargs[2] = {__pyx_t_9, __pyx_t_1};
    __pyx_t_2 = __Pyx_PyObject_FastCallMethod((PyObject*)__pyx_mstate_global->__pyx_n_u_visitchildren, __pyx_callargs+__pyx_t_3, (2-__pyx_t_3) | (1*__Pyx_PY_VECTORCALL_ARGUMENTS_OFFSET));
    __Pyx_XDECREF(__pyx_t_9); __pyx_t_9 = 0;
    __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
    if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 816, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_2);
  }
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
```

</details>

L817  🟠  (score=5)
```python
        self.unindent()
```
<details><summary>Show generated C (score=5)</summary>

```c
  __pyx_t_1 = __pyx_v_self;
  __Pyx_INCREF(__pyx_t_1);
  __pyx_t_3 = 0;
  {
    PyObject *__pyx_callargs[2] = {__pyx_t_1, NULL};
    __pyx_t_2 = __Pyx_PyObject_FastCallMethod((PyObject*)__pyx_mstate_global->__pyx_n_u_unindent, __pyx_callargs+__pyx_t_3, (1-__pyx_t_3) | (1*__Pyx_PY_VECTORCALL_ARGUMENTS_OFFSET));
    __Pyx_XDECREF(__pyx_t_1); __pyx_t_1 = 0;
    if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 817, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_2);
  }
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
```

</details>

L818  🟠  (score=5)
```python
        self.unindent()
```
<details><summary>Show generated C (score=5)</summary>

```c
  __pyx_t_1 = __pyx_v_self;
  __Pyx_INCREF(__pyx_t_1);
  __pyx_t_3 = 0;
  {
    PyObject *__pyx_callargs[2] = {__pyx_t_1, NULL};
    __pyx_t_2 = __Pyx_PyObject_FastCallMethod((PyObject*)__pyx_mstate_global->__pyx_n_u_unindent, __pyx_callargs+__pyx_t_3, (1-__pyx_t_3) | (1*__Pyx_PY_VECTORCALL_ARGUMENTS_OFFSET));
    __Pyx_XDECREF(__pyx_t_1); __pyx_t_1 = 0;
    if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 818, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_2);
  }
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
```

</details>

L819  🟡  (score=2)
```python
        return node
```
<details><summary>Show generated C (score=2)</summary>

```c
  __Pyx_XDECREF(__pyx_r);
  __Pyx_INCREF(__pyx_v_node);
  __pyx_r = __pyx_v_node;
  goto __pyx_L0;
```

</details>

L820  ⚪  (score=0)
```python
```
L821  🔴  (score=51)
```python
    def _print_node(self, node):
```
<details><summary>Show generated C (score=51)</summary>

```c
/* Python wrapper */
static PyObject *__pyx_pw_6Cython_8Compiler_7Visitor_9PrintTree_13_print_node(PyObject *__pyx_self, 
#if CYTHON_METH_FASTCALL
PyObject *const *__pyx_args, Py_ssize_t __pyx_nargs, PyObject *__pyx_kwds
#else
PyObject *__pyx_args, PyObject *__pyx_kwds
#endif
); /*proto*/
PyDoc_STRVAR(__pyx_doc_6Cython_8Compiler_7Visitor_9PrintTree_12_print_node, "File: Cython/Compiler/Visitor.py (starting at line 821)");
static PyMethodDef __pyx_mdef_6Cython_8Compiler_7Visitor_9PrintTree_13_print_node = {"_print_node", (PyCFunction)(void(*)(void))(__Pyx_PyCFunction_FastCallWithKeywords)__pyx_pw_6Cython_8Compiler_7Visitor_9PrintTree_13_print_node, __Pyx_METH_FASTCALL|METH_KEYWORDS, __pyx_doc_6Cython_8Compiler_7Visitor_9PrintTree_12_print_node};
static PyObject *__pyx_pw_6Cython_8Compiler_7Visitor_9PrintTree_13_print_node(PyObject *__pyx_self, 
#if CYTHON_METH_FASTCALL
PyObject *const *__pyx_args, Py_ssize_t __pyx_nargs, PyObject *__pyx_kwds
#else
PyObject *__pyx_args, PyObject *__pyx_kwds
#endif
) {
  PyObject *__pyx_v_self = 0;
  PyObject *__pyx_v_node = 0;
  #if !CYTHON_METH_FASTCALL
  CYTHON_UNUSED Py_ssize_t __pyx_nargs;
  #endif
  CYTHON_UNUSED PyObject *const *__pyx_kwvalues;
  PyObject *__pyx_r = 0;
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("_print_node (wrapper)", 0);
  #if !CYTHON_METH_FASTCALL
  #if CYTHON_ASSUME_SAFE_SIZE
  __pyx_nargs = PyTuple_GET_SIZE(__pyx_args);
  #else
  __pyx_nargs = PyTuple_Size(__pyx_args); if (unlikely(__pyx_nargs < 0)) return NULL;
  #endif
  #endif
  __pyx_kwvalues = __Pyx_KwValues_FASTCALL(__pyx_args, __pyx_nargs);
  {
    PyObject ** const __pyx_pyargnames[] = {&__pyx_mstate_global->__pyx_n_u_self,&__pyx_mstate_global->__pyx_n_u_node,0};
  PyObject* values[2] = {0,0};
    const Py_ssize_t __pyx_kwds_len = (__pyx_kwds) ? __Pyx_NumKwargs_FASTCALL(__pyx_kwds) : 0;
    if (unlikely(__pyx_kwds_len) < 0) __PYX_ERR(0, 821, __pyx_L3_error)
    if (__pyx_kwds_len > 0) {
      switch (__pyx_nargs) {
        case  2:
        values[1] = __Pyx_ArgRef_FASTCALL(__pyx_args, 1);
        if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[1])) __PYX_ERR(0, 821, __pyx_L3_error)
        CYTHON_FALLTHROUGH;
        case  1:
        values[0] = __Pyx_ArgRef_FASTCALL(__pyx_args, 0);
        if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[0])) __PYX_ERR(0, 821, __pyx_L3_error)
        CYTHON_FALLTHROUGH;
        case  0: break;
        default: goto __pyx_L5_argtuple_error;
      }
      const Py_ssize_t kwd_pos_args = __pyx_nargs;
      if (__Pyx_ParseKeywords(__pyx_kwds, __pyx_kwvalues, __pyx_pyargnames, 0, values, kwd_pos_args, __pyx_kwds_len, "_print_node", 0) < (0)) __PYX_ERR(0, 821, __pyx_L3_error)
      for (Py_ssize_t i = __pyx_nargs; i < 2; i++) {
        if (unlikely(!values[i])) { __Pyx_RaiseArgtupleInvalid("_print_node", 1, 2, 2, i); __PYX_ERR(0, 821, __pyx_L3_error) }
      }
    } else if (unlikely(__pyx_nargs != 2)) {
      goto __pyx_L5_argtuple_error;
    } else {
      values[0] = __Pyx_ArgRef_FASTCALL(__pyx_args, 0);
      if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[0])) __PYX_ERR(0, 821, __pyx_L3_error)
      values[1] = __Pyx_ArgRef_FASTCALL(__pyx_args, 1);
      if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[1])) __PYX_ERR(0, 821, __pyx_L3_error)
    }
    __pyx_v_self = values[0];
    __pyx_v_node = values[1];
  }
  goto __pyx_L6_skip;
  __pyx_L5_argtuple_error:;
  __Pyx_RaiseArgtupleInvalid("_print_node", 1, 2, 2, __pyx_nargs); __PYX_ERR(0, 821, __pyx_L3_error)
  __pyx_L6_skip:;
  goto __pyx_L4_argument_unpacking_done;
  __pyx_L3_error:;
  for (Py_ssize_t __pyx_temp=0; __pyx_temp < (Py_ssize_t)(sizeof(values)/sizeof(values[0])); ++__pyx_temp) {
    Py_XDECREF(values[__pyx_temp]);
  }
  __Pyx_AddTraceback("Cython.Compiler.Visitor.PrintTree._print_node", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __Pyx_RefNannyFinishContext();
  return NULL;
  __pyx_L4_argument_unpacking_done:;
  __pyx_r = __pyx_pf_6Cython_8Compiler_7Visitor_9PrintTree_12_print_node(__pyx_self, __pyx_v_self, __pyx_v_node);
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

static PyObject *__pyx_pf_6Cython_8Compiler_7Visitor_9PrintTree_12_print_node(CYTHON_UNUSED PyObject *__pyx_self, PyObject *__pyx_v_self, PyObject *__pyx_v_node) {
  PyObject *__pyx_v_line = NULL;
  PyObject *__pyx_v_name = NULL;
  CYTHON_UNUSED PyObject *__pyx_v_parent = NULL;
  PyObject *__pyx_v_attr = NULL;
  PyObject *__pyx_v_idx = NULL;
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
  __Pyx_XDECREF(__pyx_t_8);
  __Pyx_XDECREF(__pyx_t_11);
  __Pyx_AddTraceback("Cython.Compiler.Visitor.PrintTree._print_node", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_r = NULL;
  __pyx_L0:;
  __Pyx_XDECREF(__pyx_v_line);
  __Pyx_XDECREF(__pyx_v_name);
  __Pyx_XDECREF(__pyx_v_parent);
  __Pyx_XDECREF(__pyx_v_attr);
  __Pyx_XDECREF(__pyx_v_idx);
  __Pyx_XGIVEREF(__pyx_r);
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}
/* … */
  __pyx_t_2 = __Pyx_CyFunction_New(&__pyx_mdef_6Cython_8Compiler_7Visitor_9PrintTree_13_print_node, 0, __pyx_mstate_global->__pyx_n_u_PrintTree__print_node, NULL, __pyx_mstate_global->__pyx_n_u_Cython_Compiler_Visitor, __pyx_mstate_global->__pyx_d, ((PyObject *)__pyx_mstate_global->__pyx_codeobj_tab[65])); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 821, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  #if CYTHON_COMPILING_IN_CPYTHON && PY_VERSION_HEX >= 0x030E0000
  PyUnstable_Object_EnableDeferredRefcount(__pyx_t_2);
  #endif
  if (__Pyx_SetNameInClass(__pyx_t_6, __pyx_mstate_global->__pyx_n_u_print_node, __pyx_t_2) < (0)) __PYX_ERR(0, 821, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
```

</details>

L822  🟠  (score=5)
```python
        line = node.pos[1]
```
<details><summary>Show generated C (score=5)</summary>

```c
  __pyx_t_1 = __Pyx_PyObject_GetAttrStr(__pyx_v_node, __pyx_mstate_global->__pyx_n_u_pos); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 822, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __pyx_t_2 = __Pyx_GetItemInt(__pyx_t_1, 1, long, 1, __Pyx_PyLong_From_long, 0, 0, 1, 1, __Pyx_ReferenceSharing_OwnStrongReference); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 822, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __pyx_v_line = __pyx_t_2;
  __pyx_t_2 = 0;
```

</details>

L823  🔴  (score=31)
```python
        if self._line_range is None or self._line_range[0] <= line <= self._line_range[1]:
```
<details><summary>Show generated C (score=31)</summary>

```c
  __pyx_t_2 = __Pyx_PyObject_GetAttrStr(__pyx_v_self, __pyx_mstate_global->__pyx_n_u_line_range); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 823, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __pyx_t_4 = (__pyx_t_2 == Py_None);
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  if (!__pyx_t_4) {
  } else {
    __pyx_t_3 = __pyx_t_4;
    goto __pyx_L4_bool_binop_done;
  }
  __pyx_t_2 = __Pyx_PyObject_GetAttrStr(__pyx_v_self, __pyx_mstate_global->__pyx_n_u_line_range); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 823, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __pyx_t_1 = __Pyx_GetItemInt(__pyx_t_2, 0, long, 1, __Pyx_PyLong_From_long, 0, 0, 1, 1, __Pyx_ReferenceSharing_OwnStrongReference); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 823, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __pyx_t_2 = PyObject_RichCompare(__pyx_t_1, __pyx_v_line, Py_LE); __Pyx_XGOTREF(__pyx_t_2); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 823, __pyx_L1_error)
  if (__Pyx_PyObject_IsTrue(__pyx_t_2)) {
    __Pyx_DECREF(__pyx_t_2);
    __pyx_t_5 = __Pyx_PyObject_GetAttrStr(__pyx_v_self, __pyx_mstate_global->__pyx_n_u_line_range); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 823, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_5);
    __pyx_t_6 = __Pyx_GetItemInt(__pyx_t_5, 1, long, 1, __Pyx_PyLong_From_long, 0, 0, 1, 1, __Pyx_ReferenceSharing_OwnStrongReference); if (unlikely(!__pyx_t_6)) __PYX_ERR(0, 823, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_6);
    __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
    __pyx_t_2 = PyObject_RichCompare(__pyx_v_line, __pyx_t_6, Py_LE); __Pyx_XGOTREF(__pyx_t_2); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 823, __pyx_L1_error)
    __Pyx_DECREF(__pyx_t_6); __pyx_t_6 = 0;
  }
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __pyx_t_4 = __Pyx_PyObject_IsTrue(__pyx_t_2); if (unlikely((__pyx_t_4 < 0))) __PYX_ERR(0, 823, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __pyx_t_3 = __pyx_t_4;
  __pyx_L4_bool_binop_done:;
  if (__pyx_t_3) {
/* … */
  }
```

</details>

L824  🟠  (score=8)
```python
            if len(self.access_path) == 0:
```
<details><summary>Show generated C (score=8)</summary>

```c
    __pyx_t_2 = __Pyx_PyObject_GetAttrStr(__pyx_v_self, __pyx_mstate_global->__pyx_n_u_access_path); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 824, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_2);
    __pyx_t_7 = PyObject_Length(__pyx_t_2); if (unlikely(__pyx_t_7 == ((Py_ssize_t)-1))) __PYX_ERR(0, 824, __pyx_L1_error)
    __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
    __pyx_t_3 = (__pyx_t_7 == 0);
    if (__pyx_t_3) {
/* … */
      goto __pyx_L6;
    }
```

</details>

L825  🟡  (score=1)
```python
                name = "(root)"
```
<details><summary>Show generated C (score=1)</summary>

```c
      __Pyx_INCREF(__pyx_mstate_global->__pyx_kp_u_root_2);
      __pyx_v_name = __pyx_mstate_global->__pyx_kp_u_root_2;
```

</details>

L826  ⚪  (score=0)
```python
            else:
```
L827  🔴  (score=61)
```python
                parent, attr, idx = self.access_path[-1]
```
<details><summary>Show generated C (score=61)</summary>

```c
    /*else*/ {
      __pyx_t_2 = __Pyx_PyObject_GetAttrStr(__pyx_v_self, __pyx_mstate_global->__pyx_n_u_access_path); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 827, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_2);
      __pyx_t_1 = __Pyx_GetItemInt(__pyx_t_2, -1L, long, 1, __Pyx_PyLong_From_long, 0, 1, 1, 1, __Pyx_ReferenceSharing_OwnStrongReference); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 827, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_1);
      __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
      if ((likely(PyTuple_CheckExact(__pyx_t_1))) || (PyList_CheckExact(__pyx_t_1))) {
        PyObject* sequence = __pyx_t_1;
        Py_ssize_t size = __Pyx_PySequence_SIZE(sequence);
        if (unlikely(size != 3)) {
          if (size > 3) __Pyx_RaiseTooManyValuesError(3);
          else if (size >= 0) __Pyx_RaiseNeedMoreValuesError(size);
          __PYX_ERR(0, 827, __pyx_L1_error)
        }
        #if CYTHON_ASSUME_SAFE_MACROS && !CYTHON_AVOID_BORROWED_REFS
        if (likely(PyTuple_CheckExact(sequence))) {
          __pyx_t_2 = PyTuple_GET_ITEM(sequence, 0);
          __Pyx_INCREF(__pyx_t_2);
          __pyx_t_6 = PyTuple_GET_ITEM(sequence, 1);
          __Pyx_INCREF(__pyx_t_6);
          __pyx_t_5 = PyTuple_GET_ITEM(sequence, 2);
          __Pyx_INCREF(__pyx_t_5);
        } else {
          __pyx_t_2 = __Pyx_PyList_GetItemRefFast(sequence, 0, __Pyx_ReferenceSharing_SharedReference);
          if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 827, __pyx_L1_error)
          __Pyx_XGOTREF(__pyx_t_2);
          __pyx_t_6 = __Pyx_PyList_GetItemRefFast(sequence, 1, __Pyx_ReferenceSharing_SharedReference);
          if (unlikely(!__pyx_t_6)) __PYX_ERR(0, 827, __pyx_L1_error)
          __Pyx_XGOTREF(__pyx_t_6);
          __pyx_t_5 = __Pyx_PyList_GetItemRefFast(sequence, 2, __Pyx_ReferenceSharing_SharedReference);
          if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 827, __pyx_L1_error)
          __Pyx_XGOTREF(__pyx_t_5);
        }
        #else
        __pyx_t_2 = __Pyx_PySequence_ITEM(sequence, 0); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 827, __pyx_L1_error)
        __Pyx_GOTREF(__pyx_t_2);
        __pyx_t_6 = __Pyx_PySequence_ITEM(sequence, 1); if (unlikely(!__pyx_t_6)) __PYX_ERR(0, 827, __pyx_L1_error)
        __Pyx_GOTREF(__pyx_t_6);
        __pyx_t_5 = __Pyx_PySequence_ITEM(sequence, 2); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 827, __pyx_L1_error)
        __Pyx_GOTREF(__pyx_t_5);
        #endif
        __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
      } else {
        Py_ssize_t index = -1;
        __pyx_t_8 = PyObject_GetIter(__pyx_t_1); if (unlikely(!__pyx_t_8)) __PYX_ERR(0, 827, __pyx_L1_error)
        __Pyx_GOTREF(__pyx_t_8);
        __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
        __pyx_t_9 = (CYTHON_COMPILING_IN_LIMITED_API) ? PyIter_Next : __Pyx_PyObject_GetIterNextFunc(__pyx_t_8);
        index = 0; __pyx_t_2 = __pyx_t_9(__pyx_t_8); if (unlikely(!__pyx_t_2)) goto __pyx_L7_unpacking_failed;
        __Pyx_GOTREF(__pyx_t_2);
        index = 1; __pyx_t_6 = __pyx_t_9(__pyx_t_8); if (unlikely(!__pyx_t_6)) goto __pyx_L7_unpacking_failed;
        __Pyx_GOTREF(__pyx_t_6);
        index = 2; __pyx_t_5 = __pyx_t_9(__pyx_t_8); if (unlikely(!__pyx_t_5)) goto __pyx_L7_unpacking_failed;
        __Pyx_GOTREF(__pyx_t_5);
        if (__Pyx_IternextUnpackEndCheck(__pyx_t_9(__pyx_t_8), 3) < (0)) __PYX_ERR(0, 827, __pyx_L1_error)
        __pyx_t_9 = NULL;
        __Pyx_DECREF(__pyx_t_8); __pyx_t_8 = 0;
        goto __pyx_L8_unpacking_done;
        __pyx_L7_unpacking_failed:;
        __Pyx_DECREF(__pyx_t_8); __pyx_t_8 = 0;
        __pyx_t_9 = NULL;
        if (__Pyx_IterFinish() == 0) __Pyx_RaiseNeedMoreValuesError(index);
        __PYX_ERR(0, 827, __pyx_L1_error)
        __pyx_L8_unpacking_done:;
      }
      __pyx_v_parent = __pyx_t_2;
      __pyx_t_2 = 0;
      __pyx_v_attr = __pyx_t_6;
      __pyx_t_6 = 0;
      __pyx_v_idx = __pyx_t_5;
      __pyx_t_5 = 0;
```

</details>

L828  ⚪  (score=0)
```python
                if idx is not None:
```
<details><summary>Show generated C (score=0)</summary>

```c
      __pyx_t_3 = (__pyx_v_idx != Py_None);
      if (__pyx_t_3) {
/* … */
        goto __pyx_L9;
      }
```

</details>

L829  🔴  (score=23)
```python
                    name = "%s[%d]" % (attr, idx)
```
<details><summary>Show generated C (score=23)</summary>

```c
        __pyx_t_1 = __Pyx_PyObject_FormatSimpleAndDecref(PyObject_Str(__pyx_v_attr), __pyx_mstate_global->__pyx_empty_unicode); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 829, __pyx_L1_error)
        __Pyx_GOTREF(__pyx_t_1);
        __pyx_t_5 = __Pyx_PyObject_FormatAndDecref(__Pyx_PyNumber_Long(__pyx_v_idx), __pyx_mstate_global->__pyx_n_u_d_3); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 829, __pyx_L1_error)
        __Pyx_GOTREF(__pyx_t_5);
        __pyx_t_10[0] = __pyx_t_1;
        __pyx_t_10[1] = __pyx_mstate_global->__pyx_kp_u__12;
        __pyx_t_10[2] = __pyx_t_5;
        __pyx_t_10[3] = __pyx_mstate_global->__pyx_kp_u__13;
        __pyx_t_6 = __Pyx_PyUnicode_Join(__pyx_t_10, 4, __Pyx_PyUnicode_GET_LENGTH(__pyx_t_1) + 1 * 2 + __Pyx_PyUnicode_GET_LENGTH(__pyx_t_5), 127 | __Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_1) | __Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_5));
        if (unlikely(!__pyx_t_6)) __PYX_ERR(0, 829, __pyx_L1_error)
        __Pyx_GOTREF(__pyx_t_6);
        __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
        __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
        __pyx_v_name = __pyx_t_6;
        __pyx_t_6 = 0;
```

</details>

L830  ⚪  (score=0)
```python
                else:
```
L831  🟡  (score=1)
```python
                    name = attr
```
<details><summary>Show generated C (score=1)</summary>

```c
      /*else*/ {
        __Pyx_INCREF(__pyx_v_attr);
        __pyx_v_name = __pyx_v_attr;
      }
      __pyx_L9:;
    }
    __pyx_L6:;
```

</details>

L832  🔴  (score=52)
```python
            print("%s- %s: %s" % (self._indent, name, self.repr_of(node)))
```
<details><summary>Show generated C (score=52)</summary>

```c
    __pyx_t_5 = NULL;
    __pyx_t_1 = __Pyx_PyObject_GetAttrStr(__pyx_v_self, __pyx_mstate_global->__pyx_n_u_indent); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 832, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_1);
    __pyx_t_2 = __Pyx_PyObject_FormatSimpleAndDecref(PyObject_Str(__pyx_t_1), __pyx_mstate_global->__pyx_empty_unicode); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 832, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_2);
    __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
    __pyx_t_1 = __Pyx_PyObject_FormatSimpleAndDecref(PyObject_Str(__pyx_v_name), __pyx_mstate_global->__pyx_empty_unicode); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 832, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_1);
    __pyx_t_8 = __Pyx_PyObject_GetAttrStr(__pyx_v_self, __pyx_mstate_global->__pyx_n_u_repr_of); if (unlikely(!__pyx_t_8)) __PYX_ERR(0, 832, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_8);
    __pyx_t_11 = __Pyx_PyObject_CallOneArg(__pyx_t_8, __pyx_v_node); if (unlikely(!__pyx_t_11)) __PYX_ERR(0, 832, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_11);
    __Pyx_DECREF(__pyx_t_8); __pyx_t_8 = 0;
    __pyx_t_8 = __Pyx_PyObject_FormatSimpleAndDecref(PyObject_Str(__pyx_t_11), __pyx_mstate_global->__pyx_empty_unicode); if (unlikely(!__pyx_t_8)) __PYX_ERR(0, 832, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_8);
    __Pyx_DECREF(__pyx_t_11); __pyx_t_11 = 0;
    __pyx_t_12[0] = __pyx_t_2;
    __pyx_t_12[1] = __pyx_mstate_global->__pyx_kp_u__14;
    __pyx_t_12[2] = __pyx_t_1;
    __pyx_t_12[3] = __pyx_mstate_global->__pyx_kp_u__9;
    __pyx_t_12[4] = __pyx_t_8;
    __pyx_t_11 = __Pyx_PyUnicode_Join(__pyx_t_12, 5, __Pyx_PyUnicode_GET_LENGTH(__pyx_t_2) + 2 * 2 + __Pyx_PyUnicode_GET_LENGTH(__pyx_t_1) + __Pyx_PyUnicode_GET_LENGTH(__pyx_t_8), 127 | __Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_2) | __Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_1) | __Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_8));
    if (unlikely(!__pyx_t_11)) __PYX_ERR(0, 832, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_11);
    __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
    __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
    __Pyx_DECREF(__pyx_t_8); __pyx_t_8 = 0;
    __pyx_t_13 = 1;
    {
      PyObject *__pyx_callargs[2] = {__pyx_t_5, __pyx_t_11};
      __pyx_t_6 = __Pyx_PyObject_FastCall((PyObject*)__pyx_builtin_print, __pyx_callargs+__pyx_t_13, (2-__pyx_t_13) | (__pyx_t_13*__Pyx_PY_VECTORCALL_ARGUMENTS_OFFSET));
      __Pyx_XDECREF(__pyx_t_5); __pyx_t_5 = 0;
      __Pyx_DECREF(__pyx_t_11); __pyx_t_11 = 0;
      if (unlikely(!__pyx_t_6)) __PYX_ERR(0, 832, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_6);
    }
    __Pyx_DECREF(__pyx_t_6); __pyx_t_6 = 0;
```

</details>

L833  ⚪  (score=0)
```python
```
L834  🔴  (score=47)
```python
    def repr_of(self, node):
```
<details><summary>Show generated C (score=47)</summary>

```c
/* Python wrapper */
static PyObject *__pyx_pw_6Cython_8Compiler_7Visitor_9PrintTree_15repr_of(PyObject *__pyx_self, 
#if CYTHON_METH_FASTCALL
PyObject *const *__pyx_args, Py_ssize_t __pyx_nargs, PyObject *__pyx_kwds
#else
PyObject *__pyx_args, PyObject *__pyx_kwds
#endif
); /*proto*/
PyDoc_STRVAR(__pyx_doc_6Cython_8Compiler_7Visitor_9PrintTree_14repr_of, "File: Cython/Compiler/Visitor.py (starting at line 834)");
static PyMethodDef __pyx_mdef_6Cython_8Compiler_7Visitor_9PrintTree_15repr_of = {"repr_of", (PyCFunction)(void(*)(void))(__Pyx_PyCFunction_FastCallWithKeywords)__pyx_pw_6Cython_8Compiler_7Visitor_9PrintTree_15repr_of, __Pyx_METH_FASTCALL|METH_KEYWORDS, __pyx_doc_6Cython_8Compiler_7Visitor_9PrintTree_14repr_of};
static PyObject *__pyx_pw_6Cython_8Compiler_7Visitor_9PrintTree_15repr_of(PyObject *__pyx_self, 
#if CYTHON_METH_FASTCALL
PyObject *const *__pyx_args, Py_ssize_t __pyx_nargs, PyObject *__pyx_kwds
#else
PyObject *__pyx_args, PyObject *__pyx_kwds
#endif
) {
  CYTHON_UNUSED PyObject *__pyx_v_self = 0;
  PyObject *__pyx_v_node = 0;
  #if !CYTHON_METH_FASTCALL
  CYTHON_UNUSED Py_ssize_t __pyx_nargs;
  #endif
  CYTHON_UNUSED PyObject *const *__pyx_kwvalues;
  PyObject *__pyx_r = 0;
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("repr_of (wrapper)", 0);
  #if !CYTHON_METH_FASTCALL
  #if CYTHON_ASSUME_SAFE_SIZE
  __pyx_nargs = PyTuple_GET_SIZE(__pyx_args);
  #else
  __pyx_nargs = PyTuple_Size(__pyx_args); if (unlikely(__pyx_nargs < 0)) return NULL;
  #endif
  #endif
  __pyx_kwvalues = __Pyx_KwValues_FASTCALL(__pyx_args, __pyx_nargs);
  {
    PyObject ** const __pyx_pyargnames[] = {&__pyx_mstate_global->__pyx_n_u_self,&__pyx_mstate_global->__pyx_n_u_node,0};
  PyObject* values[2] = {0,0};
    const Py_ssize_t __pyx_kwds_len = (__pyx_kwds) ? __Pyx_NumKwargs_FASTCALL(__pyx_kwds) : 0;
    if (unlikely(__pyx_kwds_len) < 0) __PYX_ERR(0, 834, __pyx_L3_error)
    if (__pyx_kwds_len > 0) {
      switch (__pyx_nargs) {
        case  2:
        values[1] = __Pyx_ArgRef_FASTCALL(__pyx_args, 1);
        if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[1])) __PYX_ERR(0, 834, __pyx_L3_error)
        CYTHON_FALLTHROUGH;
        case  1:
        values[0] = __Pyx_ArgRef_FASTCALL(__pyx_args, 0);
        if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[0])) __PYX_ERR(0, 834, __pyx_L3_error)
        CYTHON_FALLTHROUGH;
        case  0: break;
        default: goto __pyx_L5_argtuple_error;
      }
      const Py_ssize_t kwd_pos_args = __pyx_nargs;
      if (__Pyx_ParseKeywords(__pyx_kwds, __pyx_kwvalues, __pyx_pyargnames, 0, values, kwd_pos_args, __pyx_kwds_len, "repr_of", 0) < (0)) __PYX_ERR(0, 834, __pyx_L3_error)
      for (Py_ssize_t i = __pyx_nargs; i < 2; i++) {
        if (unlikely(!values[i])) { __Pyx_RaiseArgtupleInvalid("repr_of", 1, 2, 2, i); __PYX_ERR(0, 834, __pyx_L3_error) }
      }
    } else if (unlikely(__pyx_nargs != 2)) {
      goto __pyx_L5_argtuple_error;
    } else {
      values[0] = __Pyx_ArgRef_FASTCALL(__pyx_args, 0);
      if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[0])) __PYX_ERR(0, 834, __pyx_L3_error)
      values[1] = __Pyx_ArgRef_FASTCALL(__pyx_args, 1);
      if (!CYTHON_ASSUME_SAFE_MACROS && unlikely(!values[1])) __PYX_ERR(0, 834, __pyx_L3_error)
    }
    __pyx_v_self = values[0];
    __pyx_v_node = values[1];
  }
  goto __pyx_L6_skip;
  __pyx_L5_argtuple_error:;
  __Pyx_RaiseArgtupleInvalid("repr_of", 1, 2, 2, __pyx_nargs); __PYX_ERR(0, 834, __pyx_L3_error)
  __pyx_L6_skip:;
  goto __pyx_L4_argument_unpacking_done;
  __pyx_L3_error:;
  for (Py_ssize_t __pyx_temp=0; __pyx_temp < (Py_ssize_t)(sizeof(values)/sizeof(values[0])); ++__pyx_temp) {
    Py_XDECREF(values[__pyx_temp]);
  }
  __Pyx_AddTraceback("Cython.Compiler.Visitor.PrintTree.repr_of", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __Pyx_RefNannyFinishContext();
  return NULL;
  __pyx_L4_argument_unpacking_done:;
  __pyx_r = __pyx_pf_6Cython_8Compiler_7Visitor_9PrintTree_14repr_of(__pyx_self, __pyx_v_self, __pyx_v_node);
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

static PyObject *__pyx_pf_6Cython_8Compiler_7Visitor_9PrintTree_14repr_of(CYTHON_UNUSED PyObject *__pyx_self, CYTHON_UNUSED PyObject *__pyx_v_self, PyObject *__pyx_v_node) {
  PyObject *__pyx_v_result = NULL;
  PyObject *__pyx_v_t = NULL;
  PyObject *__pyx_v_pos = NULL;
  PyObject *__pyx_v_path = NULL;
  PyObject *__pyx_r = NULL;
/* … */
  /* function exit code */
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_t_2);
  __Pyx_XDECREF(__pyx_t_3);
  __Pyx_XDECREF(__pyx_t_4);
  __Pyx_XDECREF(__pyx_t_8);
  __Pyx_AddTraceback("Cython.Compiler.Visitor.PrintTree.repr_of", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_r = NULL;
  __pyx_L0:;
  __Pyx_XDECREF(__pyx_v_result);
  __Pyx_XDECREF(__pyx_v_t);
  __Pyx_XDECREF(__pyx_v_pos);
  __Pyx_XDECREF(__pyx_v_path);
  __Pyx_XGIVEREF(__pyx_r);
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}
/* … */
  __pyx_t_2 = __Pyx_CyFunction_New(&__pyx_mdef_6Cython_8Compiler_7Visitor_9PrintTree_15repr_of, 0, __pyx_mstate_global->__pyx_n_u_PrintTree_repr_of, NULL, __pyx_mstate_global->__pyx_n_u_Cython_Compiler_Visitor, __pyx_mstate_global->__pyx_d, ((PyObject *)__pyx_mstate_global->__pyx_codeobj_tab[66])); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 834, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  #if CYTHON_COMPILING_IN_CPYTHON && PY_VERSION_HEX >= 0x030E0000
  PyUnstable_Object_EnableDeferredRefcount(__pyx_t_2);
  #endif
  if (__Pyx_SetNameInClass(__pyx_t_6, __pyx_mstate_global->__pyx_n_u_repr_of, __pyx_t_2) < (0)) __PYX_ERR(0, 834, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
```

</details>

L835  ⚪  (score=0)
```python
        if node is None:
```
<details><summary>Show generated C (score=0)</summary>

```c
  __pyx_t_1 = (__pyx_v_node == Py_None);
  if (__pyx_t_1) {
/* … */
  }
```

</details>

L836  🟡  (score=2)
```python
            return "(none)"
```
<details><summary>Show generated C (score=2)</summary>

```c
    __Pyx_XDECREF(__pyx_r);
    __Pyx_INCREF(__pyx_mstate_global->__pyx_kp_u_none);
    __pyx_r = __pyx_mstate_global->__pyx_kp_u_none;
    goto __pyx_L0;
```

</details>

L837  ⚪  (score=0)
```python
        else:
```
L838  🟠  (score=5)
```python
            result = node.__class__.__name__
```
<details><summary>Show generated C (score=5)</summary>

```c
  /*else*/ {
    __pyx_t_2 = __Pyx_PyObject_GetAttrStr(__pyx_v_node, __pyx_mstate_global->__pyx_n_u_class); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 838, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_2);
    __pyx_t_3 = __Pyx_PyObject_GetAttrStr(__pyx_t_2, __pyx_mstate_global->__pyx_n_u_name); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 838, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_3);
    __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
    __pyx_v_result = __pyx_t_3;
    __pyx_t_3 = 0;
```

</details>

L839  🔴  (score=11)
```python
            if isinstance(node, ExprNodes.NameNode):
```
<details><summary>Show generated C (score=11)</summary>

```c
    __Pyx_GetModuleGlobalName(__pyx_t_3, __pyx_mstate_global->__pyx_n_u_ExprNodes); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 839, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_3);
    __pyx_t_2 = __Pyx_PyObject_GetAttrStr(__pyx_t_3, __pyx_mstate_global->__pyx_n_u_NameNode); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 839, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_2);
    __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
    __pyx_t_1 = PyObject_IsInstance(__pyx_v_node, __pyx_t_2); if (unlikely(__pyx_t_1 == ((int)-1))) __PYX_ERR(0, 839, __pyx_L1_error)
    __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
    if (__pyx_t_1) {
/* … */
      goto __pyx_L4;
    }
```

</details>

L840  🔴  (score=40)
```python
                result += "(type=%s, name=\"%s\")" % (repr(node.type), node.name)
```
<details><summary>Show generated C (score=40)</summary>

```c
      __pyx_t_2 = __Pyx_PyObject_GetAttrStr(__pyx_v_node, __pyx_mstate_global->__pyx_n_u_type); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 840, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_2);
      __pyx_t_3 = PyObject_Repr(__pyx_t_2); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 840, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_3);
      __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
      __pyx_t_2 = __Pyx_PyUnicode_Unicode(__pyx_t_3); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 840, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_2);
      __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
      __pyx_t_3 = __Pyx_PyObject_GetAttrStr(__pyx_v_node, __pyx_mstate_global->__pyx_n_u_name_2); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 840, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_3);
      __pyx_t_4 = __Pyx_PyObject_FormatSimpleAndDecref(PyObject_Str(__pyx_t_3), __pyx_mstate_global->__pyx_empty_unicode); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 840, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_4);
      __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
      __pyx_t_5[0] = __pyx_mstate_global->__pyx_kp_u_type_2;
      __pyx_t_5[1] = __pyx_t_2;
      __pyx_t_5[2] = __pyx_mstate_global->__pyx_kp_u_name_3;
      __pyx_t_5[3] = __pyx_t_4;
      __pyx_t_5[4] = __pyx_mstate_global->__pyx_kp_u__15;
      __pyx_t_3 = __Pyx_PyUnicode_Join(__pyx_t_5, 5, 6 + __Pyx_PyUnicode_GET_LENGTH(__pyx_t_2) + 8 + __Pyx_PyUnicode_GET_LENGTH(__pyx_t_4) + 2, 127 | __Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_2) | __Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_4));
      if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 840, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_3);
      __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
      __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
      __pyx_t_4 = PyNumber_InPlaceAdd(__pyx_v_result, __pyx_t_3); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 840, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_4);
      __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
      __Pyx_DECREF_SET(__pyx_v_result, __pyx_t_4);
      __pyx_t_4 = 0;
```

</details>

L841  🔴  (score=11)
```python
            elif isinstance(node, Nodes.DefNode):
```
<details><summary>Show generated C (score=11)</summary>

```c
    __Pyx_GetModuleGlobalName(__pyx_t_4, __pyx_mstate_global->__pyx_n_u_Nodes); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 841, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_4);
    __pyx_t_3 = __Pyx_PyObject_GetAttrStr(__pyx_t_4, __pyx_mstate_global->__pyx_n_u_DefNode); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 841, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_3);
    __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
    __pyx_t_1 = PyObject_IsInstance(__pyx_v_node, __pyx_t_3); if (unlikely(__pyx_t_1 == ((int)-1))) __PYX_ERR(0, 841, __pyx_L1_error)
    __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
    if (__pyx_t_1) {
/* … */
      goto __pyx_L4;
    }
```

</details>

L842  🔴  (score=12)
```python
                result += "(name=\"%s\")" % node.name
```
<details><summary>Show generated C (score=12)</summary>

```c
      __pyx_t_3 = __Pyx_PyObject_GetAttrStr(__pyx_v_node, __pyx_mstate_global->__pyx_n_u_name_2); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 842, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_3);
      __pyx_t_4 = __Pyx_PyUnicode_FormatSafe(__pyx_mstate_global->__pyx_kp_u_name_s, __pyx_t_3); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 842, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_4);
      __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
      __pyx_t_3 = PyNumber_InPlaceAdd(__pyx_v_result, __pyx_t_4); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 842, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_3);
      __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
      __Pyx_DECREF_SET(__pyx_v_result, __pyx_t_3);
      __pyx_t_3 = 0;
```

</details>

L843  🔴  (score=11)
```python
            elif isinstance(node, Nodes.CFuncDefNode):
```
<details><summary>Show generated C (score=11)</summary>

```c
    __Pyx_GetModuleGlobalName(__pyx_t_3, __pyx_mstate_global->__pyx_n_u_Nodes); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 843, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_3);
    __pyx_t_4 = __Pyx_PyObject_GetAttrStr(__pyx_t_3, __pyx_mstate_global->__pyx_n_u_CFuncDefNode); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 843, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_4);
    __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
    __pyx_t_1 = PyObject_IsInstance(__pyx_v_node, __pyx_t_4); if (unlikely(__pyx_t_1 == ((int)-1))) __PYX_ERR(0, 843, __pyx_L1_error)
    __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
    if (__pyx_t_1) {
/* … */
      goto __pyx_L4;
    }
```

</details>

L844  🔴  (score=19)
```python
                result += "(name=\"%s\", type=\"%s\")" % (
```
<details><summary>Show generated C (score=19)</summary>

```c
      __pyx_t_3 = __Pyx_PyUnicode_Join(__pyx_t_5, 5, 7 + __Pyx_PyUnicode_GET_LENGTH(__pyx_t_4) + 9 + __Pyx_PyUnicode_GET_LENGTH(__pyx_t_2) + 2, 127 | __Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_4) | __Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_2));
      if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 844, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_3);
      __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
      __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
      __pyx_t_2 = PyNumber_InPlaceAdd(__pyx_v_result, __pyx_t_3); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 844, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_2);
      __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
      __Pyx_DECREF_SET(__pyx_v_result, __pyx_t_2);
      __pyx_t_2 = 0;
```

</details>

L845  🔴  (score=21)
```python
                    node.declared_name(), getattr(node, "type", None))
```
<details><summary>Show generated C (score=21)</summary>

```c
      __pyx_t_4 = __Pyx_PyObject_GetAttrStr(__pyx_v_node, __pyx_mstate_global->__pyx_n_u_declared_name); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 845, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_4);
      __pyx_t_3 = __Pyx_PyObject_CallNoArg(__pyx_t_4); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 845, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_3);
      __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
      __pyx_t_4 = __Pyx_PyObject_FormatSimpleAndDecref(PyObject_Str(__pyx_t_3), __pyx_mstate_global->__pyx_empty_unicode); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 845, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_4);
      __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
      __pyx_t_3 = __Pyx_GetAttr3(__pyx_v_node, __pyx_mstate_global->__pyx_n_u_type, Py_None); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 845, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_3);
      __pyx_t_2 = __Pyx_PyObject_FormatSimpleAndDecref(PyObject_Str(__pyx_t_3), __pyx_mstate_global->__pyx_empty_unicode); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 845, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_2);
      __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
      __pyx_t_5[0] = __pyx_mstate_global->__pyx_kp_u_name_4;
      __pyx_t_5[1] = __pyx_t_4;
      __pyx_t_5[2] = __pyx_mstate_global->__pyx_kp_u_type_3;
      __pyx_t_5[3] = __pyx_t_2;
      __pyx_t_5[4] = __pyx_mstate_global->__pyx_kp_u__15;
```

</details>

L846  🔴  (score=11)
```python
            elif isinstance(node, ExprNodes.AttributeNode):
```
<details><summary>Show generated C (score=11)</summary>

```c
    __Pyx_GetModuleGlobalName(__pyx_t_2, __pyx_mstate_global->__pyx_n_u_ExprNodes); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 846, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_2);
    __pyx_t_3 = __Pyx_PyObject_GetAttrStr(__pyx_t_2, __pyx_mstate_global->__pyx_n_u_AttributeNode); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 846, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_3);
    __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
    __pyx_t_1 = PyObject_IsInstance(__pyx_v_node, __pyx_t_3); if (unlikely(__pyx_t_1 == ((int)-1))) __PYX_ERR(0, 846, __pyx_L1_error)
    __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
    if (__pyx_t_1) {
/* … */
      goto __pyx_L4;
    }
```

</details>

L847  🔴  (score=40)
```python
                result += "(type=%s, attribute=\"%s\")" % (repr(node.type), node.attribute)
```
<details><summary>Show generated C (score=40)</summary>

```c
      __pyx_t_3 = __Pyx_PyObject_GetAttrStr(__pyx_v_node, __pyx_mstate_global->__pyx_n_u_type); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 847, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_3);
      __pyx_t_2 = PyObject_Repr(__pyx_t_3); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 847, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_2);
      __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
      __pyx_t_3 = __Pyx_PyUnicode_Unicode(__pyx_t_2); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 847, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_3);
      __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
      __pyx_t_2 = __Pyx_PyObject_GetAttrStr(__pyx_v_node, __pyx_mstate_global->__pyx_n_u_attribute); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 847, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_2);
      __pyx_t_4 = __Pyx_PyObject_FormatSimpleAndDecref(PyObject_Str(__pyx_t_2), __pyx_mstate_global->__pyx_empty_unicode); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 847, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_4);
      __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
      __pyx_t_5[0] = __pyx_mstate_global->__pyx_kp_u_type_2;
      __pyx_t_5[1] = __pyx_t_3;
      __pyx_t_5[2] = __pyx_mstate_global->__pyx_kp_u_attribute_2;
      __pyx_t_5[3] = __pyx_t_4;
      __pyx_t_5[4] = __pyx_mstate_global->__pyx_kp_u__15;
      __pyx_t_2 = __Pyx_PyUnicode_Join(__pyx_t_5, 5, 6 + __Pyx_PyUnicode_GET_LENGTH(__pyx_t_3) + 13 + __Pyx_PyUnicode_GET_LENGTH(__pyx_t_4) + 2, 127 | __Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_3) | __Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_4));
      if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 847, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_2);
      __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
      __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
      __pyx_t_4 = PyNumber_InPlaceAdd(__pyx_v_result, __pyx_t_2); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 847, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_4);
      __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
      __Pyx_DECREF_SET(__pyx_v_result, __pyx_t_4);
      __pyx_t_4 = 0;
```

</details>

L848  🔴  (score=22)
```python
            elif isinstance(node, (ExprNodes.ConstNode, ExprNodes.PyConstNode)):
```
<details><summary>Show generated C (score=22)</summary>

```c
    __Pyx_GetModuleGlobalName(__pyx_t_4, __pyx_mstate_global->__pyx_n_u_ExprNodes); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 848, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_4);
    __pyx_t_2 = __Pyx_PyObject_GetAttrStr(__pyx_t_4, __pyx_mstate_global->__pyx_n_u_ConstNode); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 848, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_2);
    __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
    __Pyx_GetModuleGlobalName(__pyx_t_4, __pyx_mstate_global->__pyx_n_u_ExprNodes); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 848, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_4);
    __pyx_t_3 = __Pyx_PyObject_GetAttrStr(__pyx_t_4, __pyx_mstate_global->__pyx_n_u_PyConstNode); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 848, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_3);
    __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
    __pyx_t_6 = PyObject_IsInstance(__pyx_v_node, __pyx_t_2); 
    if (!__pyx_t_6) {
    } else {
      __pyx_t_1 = __pyx_t_6;
      goto __pyx_L5_bool_binop_done;
    }
    __pyx_t_6 = PyObject_IsInstance(__pyx_v_node, __pyx_t_3); 
    __pyx_t_1 = __pyx_t_6;
    __pyx_L5_bool_binop_done:;
    __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
    __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
    if (__pyx_t_1) {
/* … */
      goto __pyx_L4;
    }
```

</details>

L849  🔴  (score=40)
```python
                result += "(type=%s, value=%r)" % (repr(node.type), node.value)
```
<details><summary>Show generated C (score=40)</summary>

```c
      __pyx_t_2 = __Pyx_PyObject_GetAttrStr(__pyx_v_node, __pyx_mstate_global->__pyx_n_u_type); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 849, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_2);
      __pyx_t_3 = PyObject_Repr(__pyx_t_2); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 849, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_3);
      __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
      __pyx_t_2 = __Pyx_PyUnicode_Unicode(__pyx_t_3); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 849, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_2);
      __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
      __pyx_t_3 = __Pyx_PyObject_GetAttrStr(__pyx_v_node, __pyx_mstate_global->__pyx_n_u_value); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 849, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_3);
      __pyx_t_4 = __Pyx_PyObject_FormatSimpleAndDecref(PyObject_Repr(__pyx_t_3), __pyx_mstate_global->__pyx_empty_unicode); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 849, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_4);
      __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
      __pyx_t_5[0] = __pyx_mstate_global->__pyx_kp_u_type_2;
      __pyx_t_5[1] = __pyx_t_2;
      __pyx_t_5[2] = __pyx_mstate_global->__pyx_kp_u_value_2;
      __pyx_t_5[3] = __pyx_t_4;
      __pyx_t_5[4] = __pyx_mstate_global->__pyx_kp_u__6;
      __pyx_t_3 = __Pyx_PyUnicode_Join(__pyx_t_5, 5, 6 + __Pyx_PyUnicode_GET_LENGTH(__pyx_t_2) + 8 + __Pyx_PyUnicode_GET_LENGTH(__pyx_t_4) + 1, 127 | __Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_2) | __Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_4));
      if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 849, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_3);
      __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
      __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
      __pyx_t_4 = PyNumber_InPlaceAdd(__pyx_v_result, __pyx_t_3); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 849, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_4);
      __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
      __Pyx_DECREF_SET(__pyx_v_result, __pyx_t_4);
      __pyx_t_4 = 0;
```

</details>

L850  🔴  (score=11)
```python
            elif isinstance(node, ExprNodes.ExprNode):
```
<details><summary>Show generated C (score=11)</summary>

```c
    __Pyx_GetModuleGlobalName(__pyx_t_4, __pyx_mstate_global->__pyx_n_u_ExprNodes); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 850, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_4);
    __pyx_t_3 = __Pyx_PyObject_GetAttrStr(__pyx_t_4, __pyx_mstate_global->__pyx_n_u_ExprNode); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 850, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_3);
    __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
    __pyx_t_1 = PyObject_IsInstance(__pyx_v_node, __pyx_t_3); if (unlikely(__pyx_t_1 == ((int)-1))) __PYX_ERR(0, 850, __pyx_L1_error)
    __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
    if (__pyx_t_1) {
/* … */
      goto __pyx_L4;
    }
```

</details>

L851  🟡  (score=2)
```python
                t = node.type
```
<details><summary>Show generated C (score=2)</summary>

```c
      __pyx_t_3 = __Pyx_PyObject_GetAttrStr(__pyx_v_node, __pyx_mstate_global->__pyx_n_u_type); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 851, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_3);
      __pyx_v_t = __pyx_t_3;
      __pyx_t_3 = 0;
```

</details>

L852  🔴  (score=18)
```python
                result += "(type=%s)" % repr(t)
```
<details><summary>Show generated C (score=18)</summary>

```c
      __pyx_t_3 = PyObject_Repr(__pyx_v_t); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 852, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_3);
      __pyx_t_4 = PyUnicode_Format(__pyx_mstate_global->__pyx_kp_u_type_s, __pyx_t_3); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 852, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_4);
      __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
      __pyx_t_3 = PyNumber_InPlaceAdd(__pyx_v_result, __pyx_t_4); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 852, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_3);
      __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
      __Pyx_DECREF_SET(__pyx_v_result, __pyx_t_3);
      __pyx_t_3 = 0;
```

</details>

L853  🟠  (score=5)
```python
            elif node.pos:
```
<details><summary>Show generated C (score=5)</summary>

```c
    __pyx_t_3 = __Pyx_PyObject_GetAttrStr(__pyx_v_node, __pyx_mstate_global->__pyx_n_u_pos); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 853, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_3);
    __pyx_t_1 = __Pyx_PyObject_IsTrue(__pyx_t_3); if (unlikely((__pyx_t_1 < 0))) __PYX_ERR(0, 853, __pyx_L1_error)
    __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
    if (__pyx_t_1) {
/* … */
    }
    __pyx_L4:;
```

</details>

L854  🟡  (score=2)
```python
                pos = node.pos
```
<details><summary>Show generated C (score=2)</summary>

```c
      __pyx_t_3 = __Pyx_PyObject_GetAttrStr(__pyx_v_node, __pyx_mstate_global->__pyx_n_u_pos); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 854, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_3);
      __pyx_v_pos = __pyx_t_3;
      __pyx_t_3 = 0;
```

</details>

L855  🟠  (score=7)
```python
                path = pos[0].get_description()
```
<details><summary>Show generated C (score=7)</summary>

```c
      __pyx_t_2 = __Pyx_GetItemInt(__pyx_v_pos, 0, long, 1, __Pyx_PyLong_From_long, 0, 0, 1, 1, __Pyx_ReferenceSharing_OwnStrongReference); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 855, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_2);
      __pyx_t_4 = __pyx_t_2;
      __Pyx_INCREF(__pyx_t_4);
      __pyx_t_7 = 0;
      {
        PyObject *__pyx_callargs[2] = {__pyx_t_4, NULL};
        __pyx_t_3 = __Pyx_PyObject_FastCallMethod((PyObject*)__pyx_mstate_global->__pyx_n_u_get_description, __pyx_callargs+__pyx_t_7, (1-__pyx_t_7) | (1*__Pyx_PY_VECTORCALL_ARGUMENTS_OFFSET));
        __Pyx_XDECREF(__pyx_t_4); __pyx_t_4 = 0;
        __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
        if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 855, __pyx_L1_error)
        __Pyx_GOTREF(__pyx_t_3);
      }
      __pyx_v_path = __pyx_t_3;
      __pyx_t_3 = 0;
```

</details>

L856  🟡  (score=2)
```python
                if '/' in path:
```
<details><summary>Show generated C (score=2)</summary>

```c
      __pyx_t_1 = (__Pyx_PySequence_ContainsTF(__pyx_mstate_global->__pyx_kp_u__16, __pyx_v_path, Py_EQ)); if (unlikely((__pyx_t_1 < 0))) __PYX_ERR(0, 856, __pyx_L1_error)
      if (__pyx_t_1) {
/* … */
      }
```

</details>

L857  🟠  (score=8)
```python
                    path = path.split('/')[-1]
```
<details><summary>Show generated C (score=8)</summary>

```c
        __pyx_t_2 = __pyx_v_path;
        __Pyx_INCREF(__pyx_t_2);
        __pyx_t_7 = 0;
        {
          PyObject *__pyx_callargs[2] = {__pyx_t_2, __pyx_mstate_global->__pyx_kp_u__16};
          __pyx_t_3 = __Pyx_PyObject_FastCallMethod((PyObject*)__pyx_mstate_global->__pyx_n_u_split, __pyx_callargs+__pyx_t_7, (2-__pyx_t_7) | (1*__Pyx_PY_VECTORCALL_ARGUMENTS_OFFSET));
          __Pyx_XDECREF(__pyx_t_2); __pyx_t_2 = 0;
          if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 857, __pyx_L1_error)
          __Pyx_GOTREF(__pyx_t_3);
        }
        __pyx_t_2 = __Pyx_GetItemInt(__pyx_t_3, -1L, long, 1, __Pyx_PyLong_From_long, 0, 1, 1, 1, __Pyx_ReferenceSharing_OwnStrongReference); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 857, __pyx_L1_error)
        __Pyx_GOTREF(__pyx_t_2);
        __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
        __Pyx_DECREF_SET(__pyx_v_path, __pyx_t_2);
        __pyx_t_2 = 0;
```

</details>

L858  🟡  (score=2)
```python
                if '\\' in path:
```
<details><summary>Show generated C (score=2)</summary>

```c
      __pyx_t_1 = (__Pyx_PySequence_ContainsTF(__pyx_mstate_global->__pyx_kp_u__17, __pyx_v_path, Py_EQ)); if (unlikely((__pyx_t_1 < 0))) __PYX_ERR(0, 858, __pyx_L1_error)
      if (__pyx_t_1) {
/* … */
      }
```

</details>

L859  🟠  (score=8)
```python
                    path = path.split('\\')[-1]
```
<details><summary>Show generated C (score=8)</summary>

```c
        __pyx_t_3 = __pyx_v_path;
        __Pyx_INCREF(__pyx_t_3);
        __pyx_t_7 = 0;
        {
          PyObject *__pyx_callargs[2] = {__pyx_t_3, __pyx_mstate_global->__pyx_kp_u__17};
          __pyx_t_2 = __Pyx_PyObject_FastCallMethod((PyObject*)__pyx_mstate_global->__pyx_n_u_split, __pyx_callargs+__pyx_t_7, (2-__pyx_t_7) | (1*__Pyx_PY_VECTORCALL_ARGUMENTS_OFFSET));
          __Pyx_XDECREF(__pyx_t_3); __pyx_t_3 = 0;
          if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 859, __pyx_L1_error)
          __Pyx_GOTREF(__pyx_t_2);
        }
        __pyx_t_3 = __Pyx_GetItemInt(__pyx_t_2, -1L, long, 1, __Pyx_PyLong_From_long, 0, 1, 1, 1, __Pyx_ReferenceSharing_OwnStrongReference); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 859, __pyx_L1_error)
        __Pyx_GOTREF(__pyx_t_3);
        __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
        __Pyx_DECREF_SET(__pyx_v_path, __pyx_t_3);
        __pyx_t_3 = 0;
```

</details>

L860  🔴  (score=51)
```python
                result += "(pos=(%s:%s:%s))" % (path, pos[1], pos[2])
```
<details><summary>Show generated C (score=51)</summary>

```c
      __pyx_t_3 = __Pyx_PyObject_FormatSimpleAndDecref(PyObject_Str(__pyx_v_path), __pyx_mstate_global->__pyx_empty_unicode); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 860, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_3);
      __pyx_t_2 = __Pyx_GetItemInt(__pyx_v_pos, 1, long, 1, __Pyx_PyLong_From_long, 0, 0, 1, 1, __Pyx_ReferenceSharing_OwnStrongReference); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 860, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_2);
      __pyx_t_4 = __Pyx_PyObject_FormatSimpleAndDecref(PyObject_Str(__pyx_t_2), __pyx_mstate_global->__pyx_empty_unicode); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 860, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_4);
      __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
      __pyx_t_2 = __Pyx_GetItemInt(__pyx_v_pos, 2, long, 1, __Pyx_PyLong_From_long, 0, 0, 1, 1, __Pyx_ReferenceSharing_OwnStrongReference); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 860, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_2);
      __pyx_t_8 = __Pyx_PyObject_FormatSimpleAndDecref(PyObject_Str(__pyx_t_2), __pyx_mstate_global->__pyx_empty_unicode); if (unlikely(!__pyx_t_8)) __PYX_ERR(0, 860, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_8);
      __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
      __pyx_t_9[0] = __pyx_mstate_global->__pyx_kp_u_pos_2;
      __pyx_t_9[1] = __pyx_t_3;
      __pyx_t_9[2] = __pyx_mstate_global->__pyx_kp_u_;
      __pyx_t_9[3] = __pyx_t_4;
      __pyx_t_9[4] = __pyx_mstate_global->__pyx_kp_u_;
      __pyx_t_9[5] = __pyx_t_8;
      __pyx_t_9[6] = __pyx_mstate_global->__pyx_kp_u__18;
      __pyx_t_2 = __Pyx_PyUnicode_Join(__pyx_t_9, 7, 6 + __Pyx_PyUnicode_GET_LENGTH(__pyx_t_3) + 1 * 2 + __Pyx_PyUnicode_GET_LENGTH(__pyx_t_4) + __Pyx_PyUnicode_GET_LENGTH(__pyx_t_8) + 2, 127 | __Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_3) | __Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_4) | __Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_8));
      if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 860, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_2);
      __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
      __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
      __Pyx_DECREF(__pyx_t_8); __pyx_t_8 = 0;
      __pyx_t_8 = PyNumber_InPlaceAdd(__pyx_v_result, __pyx_t_2); if (unlikely(!__pyx_t_8)) __PYX_ERR(0, 860, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_8);
      __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
      __Pyx_DECREF_SET(__pyx_v_result, __pyx_t_8);
      __pyx_t_8 = 0;
```

</details>

L861  ⚪  (score=0)
```python
```
L862  🟡  (score=2)
```python
            return result
```
<details><summary>Show generated C (score=2)</summary>

```c
    __Pyx_XDECREF(__pyx_r);
    __Pyx_INCREF(__pyx_v_result);
    __pyx_r = __pyx_v_result;
    goto __pyx_L0;
  }
```

</details>

L863  ⚪  (score=0)
```python
```
L864  🟠  (score=5)
```python
if __name__ == "__main__":
```
<details><summary>Show generated C (score=5)</summary>

```c
  __Pyx_GetModuleGlobalName(__pyx_t_5, __pyx_mstate_global->__pyx_n_u_name); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 864, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_5);
  __pyx_t_7 = (__Pyx_PyUnicode_Equals(__pyx_t_5, __pyx_mstate_global->__pyx_n_u_main, Py_EQ)); if (unlikely((__pyx_t_7 < 0))) __PYX_ERR(0, 864, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
  if (__pyx_t_7) {
/* … */
  }
```

</details>

L865  🟠  (score=8)
```python
    import doctest
```
<details><summary>Show generated C (score=8)</summary>

```c
    __pyx_t_1 = __Pyx_Import(__pyx_mstate_global->__pyx_n_u_doctest, 0, 0, NULL, 0); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 865, __pyx_L1_error)
    __pyx_t_5 = __pyx_t_1;
    __Pyx_GOTREF(__pyx_t_5);
    if (PyDict_SetItem(__pyx_mstate_global->__pyx_d, __pyx_mstate_global->__pyx_n_u_doctest, __pyx_t_5) < (0)) __PYX_ERR(0, 865, __pyx_L1_error)
    __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
```

</details>

L866  🔴  (score=10)
```python
    doctest.testmod()
```
<details><summary>Show generated C (score=10)</summary>

```c
    __pyx_t_4 = NULL;
    __Pyx_GetModuleGlobalName(__pyx_t_6, __pyx_mstate_global->__pyx_n_u_doctest); if (unlikely(!__pyx_t_6)) __PYX_ERR(0, 866, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_6);
    __pyx_t_2 = __Pyx_PyObject_GetAttrStr(__pyx_t_6, __pyx_mstate_global->__pyx_n_u_testmod); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 866, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_2);
    __Pyx_DECREF(__pyx_t_6); __pyx_t_6 = 0;
    __pyx_t_8 = 1;
    {
      PyObject *__pyx_callargs[2] = {__pyx_t_4, NULL};
      __pyx_t_5 = __Pyx_PyObject_FastCall((PyObject*)__pyx_t_2, __pyx_callargs+__pyx_t_8, (1-__pyx_t_8) | (__pyx_t_8*__Pyx_PY_VECTORCALL_ARGUMENTS_OFFSET));
      __Pyx_XDECREF(__pyx_t_4); __pyx_t_4 = 0;
      __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
      if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 866, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_5);
    }
    __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
```

</details>

