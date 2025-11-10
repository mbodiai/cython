static int __Pyx_SetItemInt_Generic(PyObject *o, PyObject *j, PyObject *v) {
    int r;
    if (unlikely(!j)) return -1;
    r = PyObject_SetItem(o, j, v);
    Py_DECREF(j);
    return r;
}
static CYTHON_INLINE int __Pyx_SetItemInt_Fast(PyObject *o, Py_ssize_t i, PyObject *v, int is_list,
                                               int wraparound, int boundscheck, int unsafe_shared) {
    CYTHON_MAYBE_UNUSED_VAR(unsafe_shared);
#if CYTHON_ASSUME_SAFE_MACROS && CYTHON_ASSUME_SAFE_SIZE && !CYTHON_AVOID_BORROWED_REFS
    if (is_list || PyList_CheckExact(o)) {
        Py_ssize_t n = (!wraparound) ? i : ((likely(i >= 0)) ? i : i + PyList_GET_SIZE(o));
        if ((CYTHON_AVOID_THREAD_UNSAFE_BORROWED_REFS && !__Pyx_IS_UNIQUELY_REFERENCED(o, unsafe_shared))) {
            Py_INCREF(v);
            return PyList_SetItem(o, n, v);
        } else if ((!boundscheck) || likely(__Pyx_is_valid_index(n, PyList_GET_SIZE(o)))) {
            PyObject* old;
            Py_INCREF(v);
            old = PyList_GET_ITEM(o, n);
            PyList_SET_ITEM(o, n, v);
            Py_DECREF(old);
            return 0;
        }
    } else
#endif
#if CYTHON_USE_TYPE_SLOTS && !CYTHON_COMPILING_IN_PYPY
    {
        PyMappingMethods *mm = Py_TYPE(o)->tp_as_mapping;
        PySequenceMethods *sm = Py_TYPE(o)->tp_as_sequence;
        if (!is_list && mm && mm->mp_ass_subscript) {
            int r;
            PyObject *key = PyLong_FromSsize_t(i);
            if (unlikely(!key)) return -1;
            r = mm->mp_ass_subscript(o, key, v);
            Py_DECREF(key);
            return r;
        }
        if (is_list || likely(sm && sm->sq_ass_item)) {
            if (wraparound && unlikely(i < 0) && likely(sm->sq_length)) {
                Py_ssize_t l = sm->sq_length(o);
                if (likely(l >= 0)) {
                    i += l;
                } else {
                    if (!PyErr_ExceptionMatches(PyExc_OverflowError))
                        return -1;
                    PyErr_Clear();
                }
            }
            return sm->sq_ass_item(o, i, v);
        }
    }
#else
    if (is_list || !PyMapping_Check(o)) {
        return PySequence_SetItem(o, i, v);
    }
#endif
    (void)wraparound;
    (void)boundscheck;
    return __Pyx_SetItemInt_Generic(o, PyLong_FromSsize_t(i), v);
}

