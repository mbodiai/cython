#if !CYTHON_COMPILING_IN_PYPY
static PyObject* __Pyx_Fallback___Pyx_PyLong_AndObjC(PyObject *op1, PyObject *op2, int inplace) {
    return (inplace ? PyNumber_InPlaceAnd : PyNumber_And)(op1, op2);
}
#if CYTHON_USE_PYLONG_INTERNALS
static PyObject* __Pyx_Unpacked___Pyx_PyLong_AndObjC(PyObject *op1, PyObject *op2, long intval, int inplace, int zerodivision_check) {
    CYTHON_MAYBE_UNUSED_VAR(inplace);
    CYTHON_UNUSED_VAR(zerodivision_check);
    const long b = intval;
    long a, x;
#ifdef HAVE_LONG_LONG
    const PY_LONG_LONG llb = intval;
    PY_LONG_LONG lla, llx;
#endif
    if (unlikely(__Pyx_PyLong_IsZero(op1))) {
        return __Pyx_NewRef(op1);
    }
    if ((intval & PyLong_MASK) == intval) {
        long last_digit = (long) __Pyx_PyLong_Digits(op1)[0];
        long result = intval & (likely(__Pyx_PyLong_IsPos(op1)) ? last_digit : (PyLong_MASK - last_digit + 1));
        return PyLong_FromLong(result);
    }
    if (likely(__Pyx_PyLong_IsCompact(op1))) {
        a = __Pyx_PyLong_CompactValue(op1);
    } else {
        const digit* digits = __Pyx_PyLong_Digits(op1);
        const Py_ssize_t size = __Pyx_PyLong_SignedDigitCount(op1);
        switch (size) {
            case -2:
                if (8 * sizeof(long) - 1 > 2 * PyLong_SHIFT) {
                    a = -(long) (((((unsigned long)digits[1]) << PyLong_SHIFT) | (unsigned long)digits[0]));
                    break;
                #ifdef HAVE_LONG_LONG
                } else if (8 * sizeof(PY_LONG_LONG) - 1 > 2 * PyLong_SHIFT) {
                    lla = -(PY_LONG_LONG) (((((unsigned PY_LONG_LONG)digits[1]) << PyLong_SHIFT) | (unsigned PY_LONG_LONG)digits[0]));
                    goto long_long;
                #endif
                }
                CYTHON_FALLTHROUGH;
            case 2:
                if (8 * sizeof(long) - 1 > 2 * PyLong_SHIFT) {
                    a = (long) (((((unsigned long)digits[1]) << PyLong_SHIFT) | (unsigned long)digits[0]));
                    break;
                #ifdef HAVE_LONG_LONG
                } else if (8 * sizeof(PY_LONG_LONG) - 1 > 2 * PyLong_SHIFT) {
                    lla = (PY_LONG_LONG) (((((unsigned PY_LONG_LONG)digits[1]) << PyLong_SHIFT) | (unsigned PY_LONG_LONG)digits[0]));
                    goto long_long;
                #endif
                }
                CYTHON_FALLTHROUGH;
            case -3:
                if (8 * sizeof(long) - 1 > 3 * PyLong_SHIFT) {
                    a = -(long) (((((((unsigned long)digits[2]) << PyLong_SHIFT) | (unsigned long)digits[1]) << PyLong_SHIFT) | (unsigned long)digits[0]));
                    break;
                #ifdef HAVE_LONG_LONG
                } else if (8 * sizeof(PY_LONG_LONG) - 1 > 3 * PyLong_SHIFT) {
                    lla = -(PY_LONG_LONG) (((((((unsigned PY_LONG_LONG)digits[2]) << PyLong_SHIFT) | (unsigned PY_LONG_LONG)digits[1]) << PyLong_SHIFT) | (unsigned PY_LONG_LONG)digits[0]));
                    goto long_long;
                #endif
                }
                CYTHON_FALLTHROUGH;
            case 3:
                if (8 * sizeof(long) - 1 > 3 * PyLong_SHIFT) {
                    a = (long) (((((((unsigned long)digits[2]) << PyLong_SHIFT) | (unsigned long)digits[1]) << PyLong_SHIFT) | (unsigned long)digits[0]));
                    break;
                #ifdef HAVE_LONG_LONG
                } else if (8 * sizeof(PY_LONG_LONG) - 1 > 3 * PyLong_SHIFT) {
                    lla = (PY_LONG_LONG) (((((((unsigned PY_LONG_LONG)digits[2]) << PyLong_SHIFT) | (unsigned PY_LONG_LONG)digits[1]) << PyLong_SHIFT) | (unsigned PY_LONG_LONG)digits[0]));
                    goto long_long;
                #endif
                }
                CYTHON_FALLTHROUGH;
            case -4:
                if (8 * sizeof(long) - 1 > 4 * PyLong_SHIFT) {
                    a = -(long) (((((((((unsigned long)digits[3]) << PyLong_SHIFT) | (unsigned long)digits[2]) << PyLong_SHIFT) | (unsigned long)digits[1]) << PyLong_SHIFT) | (unsigned long)digits[0]));
                    break;
                #ifdef HAVE_LONG_LONG
                } else if (8 * sizeof(PY_LONG_LONG) - 1 > 4 * PyLong_SHIFT) {
                    lla = -(PY_LONG_LONG) (((((((((unsigned PY_LONG_LONG)digits[3]) << PyLong_SHIFT) | (unsigned PY_LONG_LONG)digits[2]) << PyLong_SHIFT) | (unsigned PY_LONG_LONG)digits[1]) << PyLong_SHIFT) | (unsigned PY_LONG_LONG)digits[0]));
                    goto long_long;
                #endif
                }
                CYTHON_FALLTHROUGH;
            case 4:
                if (8 * sizeof(long) - 1 > 4 * PyLong_SHIFT) {
                    a = (long) (((((((((unsigned long)digits[3]) << PyLong_SHIFT) | (unsigned long)digits[2]) << PyLong_SHIFT) | (unsigned long)digits[1]) << PyLong_SHIFT) | (unsigned long)digits[0]));
                    break;
                #ifdef HAVE_LONG_LONG
                } else if (8 * sizeof(PY_LONG_LONG) - 1 > 4 * PyLong_SHIFT) {
                    lla = (PY_LONG_LONG) (((((((((unsigned PY_LONG_LONG)digits[3]) << PyLong_SHIFT) | (unsigned PY_LONG_LONG)digits[2]) << PyLong_SHIFT) | (unsigned PY_LONG_LONG)digits[1]) << PyLong_SHIFT) | (unsigned PY_LONG_LONG)digits[0]));
                    goto long_long;
                #endif
                }
                CYTHON_FALLTHROUGH;
            default: return PyLong_Type.tp_as_number->nb_and(op1, op2);
        }
    }
            x = a & b;
        return PyLong_FromLong(x);
#ifdef HAVE_LONG_LONG
    long_long:
            llx = lla & llb;
        return PyLong_FromLongLong(llx);
#endif
    return __Pyx_Fallback___Pyx_PyLong_AndObjC(op1, op2, inplace);
    
    
}
#endif
static CYTHON_INLINE PyObject* __Pyx_PyLong_AndObjC(PyObject *op1, PyObject *op2, long intval, int inplace, int zerodivision_check) {
    CYTHON_MAYBE_UNUSED_VAR(intval);
    CYTHON_UNUSED_VAR(zerodivision_check);
    #if CYTHON_USE_PYLONG_INTERNALS
    if (likely(PyLong_CheckExact(op1))) {
        return __Pyx_Unpacked___Pyx_PyLong_AndObjC(op1, op2, intval, inplace, zerodivision_check);
    }
    #endif
    return __Pyx_Fallback___Pyx_PyLong_AndObjC(op1, op2, inplace);
}
#endif

