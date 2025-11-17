/* Helper for deciding how to treat the first argument in vectorcalls of
 * CyFunction objects.  We intentionally keep this small and header-only so
 * that it can be inlined into the generated C code.
 */
#if CYTHON_METH_FASTCALL && CYTHON_VECTORCALL
static CYTHON_INLINE int __Pyx_CyFunction_Vectorcall_CheckArgs(
    __pyx_CyFunctionObject *cyfunc,
    Py_ssize_t nargs,
    PyObject *kwnames)
{
    (void)kwnames;  /* currently unused, but part of the ABI */
    /* For plain functions (no METH_METHOD flag), there is no implicit
     * ``self`` and we never steal the first positional argument.
     */
    if (!(cyfunc->flags & __Pyx_CYFUNCTION_CCLASS) &&
        !(cyfunc->flags & __Pyx_CYFUNCTION_CLASSMETHOD)) {
        return 0;
    }
    /* Cython's methods always require an explicit "self" argument in the
     * signature.  If the call did not pass any positional arguments, we
     * cannot treat args[0] as self.
     */
    if (nargs <= 0) {
        return 0;
    }
    /* For now, keep this simple and conservative: if we have at least one
     * positional argument, treat it as an explicit "self".  This matches the
     * common pattern ``Class.method(obj, ...)`` while keeping normal bound
     * method calls fast – they still go through the same branch but the
     * extra self argument is cheap to handle.
     */
    return 1;
}
#endif


