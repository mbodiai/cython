#if !CYTHON_COMPILING_IN_PYPY
static PyObject* __Pyx_Fallback___Pyx_PyLong_MultiplyObjC(PyObject *op1, PyObject *op2, int inplace) {
    return (inplace ? PyNumber_InPlaceMultiply : PyNumber_Multiply)(op1, op2);
}
#if CYTHON_USE_PYLONG_INTERNALS
static PyObject* __Pyx_Unpacked___Pyx_PyLong_MultiplyObjC(PyObject *op1, PyObject *op2, long intval, int inplace, int zerodivision_check) {
    CYTHON_MAYBE_UNUSED_VAR(inplace);
    CYTHON_UNUSED_VAR(zerodivision_check);
    const long b = intval;
    long a;
    const PY_LONG_LONG llb = intval;
    PY_LONG_LONG lla;
    if (unlikely(__Pyx_PyLong_IsZero(op1))) {
        return __Pyx_NewRef(op1);
    }
    const int is_positive = __Pyx_PyLong_IsPos(op1);
    const digit* digits = __Pyx_PyLong_Digits(op1);
    const Py_ssize_t size = __Pyx_PyLong_DigitCount(op1);
    if (likely(size == 1)) {
        a = (long) digits[0];
        if (!is_positive) a *= -1;
    } else {
        switch (size) {
            case 2:
                if (8 * sizeof(long) - 1 > 2 * PyLong_SHIFT+30) {
                    a = (long) (((((unsigned long)digits[1]) << PyLong_SHIFT) | (unsigned long)digits[0]));
                    if (!is_positive) a *= -1;
                    goto calculate_long;
                } else if (8 * sizeof(PY_LONG_LONG) - 1 > 2 * PyLong_SHIFT+30) {
                    lla = (PY_LONG_LONG) (((((unsigned PY_LONG_LONG)digits[1]) << PyLong_SHIFT) | (unsigned PY_LONG_LONG)digits[0]));
                    if (!is_positive) lla *= -1;
                    goto calculate_long_long;
                }
                break;
            case 3:
                if (8 * sizeof(long) - 1 > 3 * PyLong_SHIFT+30) {
                    a = (long) (((((((unsigned long)digits[2]) << PyLong_SHIFT) | (unsigned long)digits[1]) << PyLong_SHIFT) | (unsigned long)digits[0]));
                    if (!is_positive) a *= -1;
                    goto calculate_long;
                } else if (8 * sizeof(PY_LONG_LONG) - 1 > 3 * PyLong_SHIFT+30) {
                    lla = (PY_LONG_LONG) (((((((unsigned PY_LONG_LONG)digits[2]) << PyLong_SHIFT) | (unsigned PY_LONG_LONG)digits[1]) << PyLong_SHIFT) | (unsigned PY_LONG_LONG)digits[0]));
                    if (!is_positive) lla *= -1;
                    goto calculate_long_long;
                }
                break;
            case 4:
                if (8 * sizeof(long) - 1 > 4 * PyLong_SHIFT+30) {
                    a = (long) (((((((((unsigned long)digits[3]) << PyLong_SHIFT) | (unsigned long)digits[2]) << PyLong_SHIFT) | (unsigned long)digits[1]) << PyLong_SHIFT) | (unsigned long)digits[0]));
                    if (!is_positive) a *= -1;
                    goto calculate_long;
                } else if (8 * sizeof(PY_LONG_LONG) - 1 > 4 * PyLong_SHIFT+30) {
                    lla = (PY_LONG_LONG) (((((((((unsigned PY_LONG_LONG)digits[3]) << PyLong_SHIFT) | (unsigned PY_LONG_LONG)digits[2]) << PyLong_SHIFT) | (unsigned PY_LONG_LONG)digits[1]) << PyLong_SHIFT) | (unsigned PY_LONG_LONG)digits[0]));
                    if (!is_positive) lla *= -1;
                    goto calculate_long_long;
                }
                break;
        }
        return PyLong_Type.tp_as_number->nb_multiply(op1, op2);
    }
    calculate_long:
        CYTHON_UNUSED_VAR(a);
        CYTHON_UNUSED_VAR(b);
        lla = a;
        goto calculate_long_long;
    calculate_long_long:
        {
            PY_LONG_LONG llx;
            llx = lla * llb;
            return PyLong_FromLongLong(llx);
        }
    
}
#endif
static PyObject* __Pyx_Float___Pyx_PyLong_MultiplyObjC(PyObject *float_val, long intval, int zerodivision_check) {
    CYTHON_UNUSED_VAR(zerodivision_check);
    const long b = intval;
    double a = __Pyx_PyFloat_AS_DOUBLE(float_val);
        double result;
        
        result = ((double)a) * (double)b;
        return PyFloat_FromDouble(result);
}
static CYTHON_INLINE PyObject* __Pyx_PyLong_MultiplyObjC(PyObject *op1, PyObject *op2, long intval, int inplace, int zerodivision_check) {
    CYTHON_MAYBE_UNUSED_VAR(intval);
    CYTHON_UNUSED_VAR(zerodivision_check);
    #if CYTHON_USE_PYLONG_INTERNALS
    if (likely(PyLong_CheckExact(op1))) {
        return __Pyx_Unpacked___Pyx_PyLong_MultiplyObjC(op1, op2, intval, inplace, zerodivision_check);
    }
    #endif
    if (PyFloat_CheckExact(op1)) {
        return __Pyx_Float___Pyx_PyLong_MultiplyObjC(op1, intval, zerodivision_check);
    }
    return __Pyx_Fallback___Pyx_PyLong_MultiplyObjC(op1, op2, inplace);
}
#endif

