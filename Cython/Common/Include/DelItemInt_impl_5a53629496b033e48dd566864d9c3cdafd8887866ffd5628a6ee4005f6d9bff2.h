static int __Pyx_DelItem_Generic(PyObject *o, PyObject *j) {
    int r;
    if (unlikely(!j)) return -1;
    r = PyObject_DelItem(o, j);
    Py_DECREF(j);
    return r;
}
static CYTHON_INLINE int __Pyx_DelItemInt_Fast(PyObject *o, Py_ssize_t i,
                                               int is_list, CYTHON_NCP_UNUSED int wraparound) {
#if !CYTHON_USE_TYPE_SLOTS
    if (is_list || !PyMapping_Check(o)) {
        return PySequence_DelItem(o, i);
    }
#else
    PyMappingMethods *mm = Py_TYPE(o)->tp_as_mapping;
    PySequenceMethods *sm = Py_TYPE(o)->tp_as_sequence;
    if ((!is_list) && mm && mm->mp_ass_subscript) {
        PyObject *key = PyLong_FromSsize_t(i);
        return likely(key) ? mm->mp_ass_subscript(o, key, (PyObject *)NULL) : -1;
    }
    if (likely(sm && sm->sq_ass_item)) {
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
        return sm->sq_ass_item(o, i, (PyObject *)NULL);
    }
#endif
    return __Pyx_DelItem_Generic(o, PyLong_FromSsize_t(i));
}

