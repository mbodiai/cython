#if !CYTHON_COMPILING_IN_PYPY
static PyObject* __Pyx_PyFloat_SubtractObjC(PyObject *op1, PyObject *op2, double floatval, int inplace, int zerodivision_check) {
    const double b = floatval;
    double a, result;
    CYTHON_UNUSED_VAR(inplace);
    CYTHON_UNUSED_VAR(zerodivision_check);
    if (likely(PyFloat_CheckExact(op1))) {
        a = __Pyx_PyFloat_AS_DOUBLE(op1);
        
    } else
    if (likely(PyLong_CheckExact(op1))) {
        #if CYTHON_USE_PYLONG_INTERNALS
        if (__Pyx_PyLong_IsZero(op1)) {
            a = 0.0;
            
        } else if (__Pyx_PyLong_IsCompact(op1)) {
            a = (double) __Pyx_PyLong_CompactValue(op1);
        } else {
            const digit* digits = __Pyx_PyLong_Digits(op1);
            const Py_ssize_t size = __Pyx_PyLong_SignedDigitCount(op1);
            switch (size) {
                case -2:
                case 2:
                    if (8 * sizeof(unsigned long) > 2 * PyLong_SHIFT && ((8 * sizeof(unsigned long) < 53) || (1 * PyLong_SHIFT < 53))) {
                        a = (double) (((((unsigned long)digits[1]) << PyLong_SHIFT) | (unsigned long)digits[0]));
                        if ((8 * sizeof(unsigned long) < 53) || (2 * PyLong_SHIFT < 53) || (a < (double) ((PY_LONG_LONG)1 << 53))) {
                            if (size == -2)
                                a = -a;
                            break;
                        }
                    }
                    CYTHON_FALLTHROUGH;
                case -3:
                case 3:
                    if (8 * sizeof(unsigned long) > 3 * PyLong_SHIFT && ((8 * sizeof(unsigned long) < 53) || (2 * PyLong_SHIFT < 53))) {
                        a = (double) (((((((unsigned long)digits[2]) << PyLong_SHIFT) | (unsigned long)digits[1]) << PyLong_SHIFT) | (unsigned long)digits[0]));
                        if ((8 * sizeof(unsigned long) < 53) || (3 * PyLong_SHIFT < 53) || (a < (double) ((PY_LONG_LONG)1 << 53))) {
                            if (size == -3)
                                a = -a;
                            break;
                        }
                    }
                    CYTHON_FALLTHROUGH;
                case -4:
                case 4:
                    if (8 * sizeof(unsigned long) > 4 * PyLong_SHIFT && ((8 * sizeof(unsigned long) < 53) || (3 * PyLong_SHIFT < 53))) {
                        a = (double) (((((((((unsigned long)digits[3]) << PyLong_SHIFT) | (unsigned long)digits[2]) << PyLong_SHIFT) | (unsigned long)digits[1]) << PyLong_SHIFT) | (unsigned long)digits[0]));
                        if ((8 * sizeof(unsigned long) < 53) || (4 * PyLong_SHIFT < 53) || (a < (double) ((PY_LONG_LONG)1 << 53))) {
                            if (size == -4)
                                a = -a;
                            break;
                        }
                    }
                    CYTHON_FALLTHROUGH;
                default:
        #endif
                    a = PyLong_AsDouble(op1);
                    if (unlikely(a == -1.0 && PyErr_Occurred())) return NULL;
        #if CYTHON_USE_PYLONG_INTERNALS
            }
        }
        #endif
    } else {
        return (inplace ? PyNumber_InPlaceSubtract : PyNumber_Subtract)(op1, op2);
    }
        result = a - b;
        return PyFloat_FromDouble(result);
}
#endif

