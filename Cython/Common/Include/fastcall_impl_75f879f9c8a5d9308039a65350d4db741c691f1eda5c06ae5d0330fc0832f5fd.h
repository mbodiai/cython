#if CYTHON_METH_FASTCALL
static CYTHON_INLINE PyObject * __Pyx_GetKwValue_FASTCALL(PyObject *kwnames, PyObject *const *kwvalues, PyObject *s)
{
    Py_ssize_t i, n = __Pyx_PyTuple_GET_SIZE(kwnames);
    #if !CYTHON_ASSUME_SAFE_SIZE
    if (unlikely(n == -1)) return NULL;
    #endif
    for (i = 0; i < n; i++)
    {
        PyObject *namei = __Pyx_PyTuple_GET_ITEM(kwnames, i);
        #if !CYTHON_ASSUME_SAFE_MACROS
        if (unlikely(!namei)) return NULL;
        #endif
        if (s == namei) return kwvalues[i];
    }
    for (i = 0; i < n; i++)
    {
        PyObject *namei = __Pyx_PyTuple_GET_ITEM(kwnames, i);
        #if !CYTHON_ASSUME_SAFE_MACROS
        if (unlikely(!namei)) return NULL;
        #endif
        int eq = __Pyx_PyUnicode_Equals(s, namei, Py_EQ);
        if (unlikely(eq != 0)) {
            if (unlikely(eq < 0)) return NULL;
            return kwvalues[i];
        }
    }
    return NULL;
}
#if CYTHON_COMPILING_IN_CPYTHON && PY_VERSION_HEX >= 0x030d0000 || CYTHON_COMPILING_IN_LIMITED_API
CYTHON_UNUSED static PyObject *__Pyx_KwargsAsDict_FASTCALL(PyObject *kwnames, PyObject *const *kwvalues) {
    Py_ssize_t i, nkwargs;
    PyObject *dict;
#if !CYTHON_ASSUME_SAFE_SIZE
    nkwargs = PyTuple_Size(kwnames);
    if (unlikely(nkwargs < 0)) return NULL;
#else
    nkwargs = PyTuple_GET_SIZE(kwnames);
#endif
    dict = PyDict_New();
    if (unlikely(!dict))
        return NULL;
    for (i=0; i<nkwargs; i++) {
#if !CYTHON_ASSUME_SAFE_MACROS
        PyObject *key = PyTuple_GetItem(kwnames, i);
        if (!key) goto bad;
#else
        PyObject *key = PyTuple_GET_ITEM(kwnames, i);
#endif
        if (unlikely(PyDict_SetItem(dict, key, kwvalues[i]) < 0))
            goto bad;
    }
    return dict;
bad:
    Py_DECREF(dict);
    return NULL;
}
#endif
#endif
#if CYTHON_METH_FASTCALL
static CYTHON_INLINE Py_ssize_t __Pyx_FastArg_FindKeyword(
    PyObject *name,
    const __Pyx_ParamMeta *params,
    Py_ssize_t param_count)
{
    /* Resolve parameter names lazily from the module string table.  The
     * metadata only stores integer indices, which keeps the tables
     * initialisable as plain data.  __pyx_string_tab is wired to the module
     * state string table during module initialisation.
     */
    extern PyObject **__pyx_string_tab;
    PyObject **stringtab = __pyx_string_tab;
    Py_ssize_t i;
    for (i = 0; i < param_count; i++) {
        unsigned short name_index = params[i].name_index;
        if (name_index == __PYX_PARAM_DEFAULT_MISSING)
            continue;
        PyObject *param_name = stringtab[name_index];
        if (param_name == name) {
            return i;
        }
    }
    for (i = 0; i < param_count; i++) {
        unsigned short name_index = params[i].name_index;
        if (name_index == __PYX_PARAM_DEFAULT_MISSING)
            continue;
        PyObject *param_name = stringtab[name_index];
        if (param_name && param_name != name) {
            int eq = __Pyx_PyUnicode_Equals(param_name, name, Py_EQ);
            if (unlikely(eq != 0)) {
                if (unlikely(eq < 0)) return -2;
                return i;
            }
        }
    }
    return -1;
}
/* Error helpers used by the fast-arg parser.
 * Older runtimes might not provide concrete implementations for these,
 * so we define them here as static helpers when missing.
 */
#if CYTHON_METH_FASTCALL
#ifndef __PYX_FASTARG_ERROR_HELPERS
#define __PYX_FASTARG_ERROR_HELPERS 1
static void __Pyx_RaiseUnexpectedKeywordError(const char* func_name, PyObject* kw_name) {
    PyErr_Format(PyExc_TypeError,
        "%s() got an unexpected keyword argument '%U'",
        func_name, kw_name);
}

static void __Pyx_RaiseKeywordRequired(const char* func_name, PyObject* kw_name) {
    PyErr_Format(PyExc_TypeError,
        "%s() needs keyword-only argument %U", func_name, kw_name);
}
#endif
#endif

static int __Pyx_FastParseKeywords(
    const __Pyx_FastArgInfo *info,
    PyObject *const *args,
    Py_ssize_t nargs,
    PyObject *kwnames,
    PyObject **const *localslots)
{
    Py_ssize_t i;
    Py_ssize_t positional_args = nargs;
    const __Pyx_ParamMeta *params = info->params;
    if (unlikely(positional_args < info->required_pos || positional_args > info->max_pos)) {
        __Pyx_RaiseArgtupleInvalid(
            info->func_name,
            0,
            info->required_pos,
            info->max_pos,
            positional_args);
        return __PYX_FASTPARSE_ERROR;
    }
    Py_ssize_t pos_index = 0;
    for (i = 0; i < info->param_count && pos_index < positional_args; i++) {
        const __Pyx_ParamMeta *param = params + i;
        if (!(param->flags & __PYX_PARAM_ACCEPTS_POS))
            continue;
        PyObject *value = args[pos_index++];
        PyObject **slot = localslots[i];
        Py_INCREF(value);
        *slot = value;
    }
    if (unlikely(pos_index != positional_args)) {
        __Pyx_RaiseArgtupleInvalid(
            info->func_name,
            0,
            info->required_pos,
            info->max_pos,
            positional_args);
        goto bad;
    }
    Py_ssize_t required_kwonly = info->required_kwonly;
    if (kwnames && __Pyx_PyTuple_GET_SIZE(kwnames)) {
        Py_ssize_t nkwargs = __Pyx_PyTuple_GET_SIZE(kwnames);
#if !CYTHON_ASSUME_SAFE_SIZE
        if (unlikely(nkwargs < 0)) goto bad;
#endif
        for (Py_ssize_t kw = 0; kw < nkwargs; kw++) {
            PyObject *name = __Pyx_PyTuple_GET_ITEM(kwnames, kw);
#if !CYTHON_ASSUME_SAFE_MACROS
            if (unlikely(!name)) goto bad;
#endif
            Py_ssize_t param_index = __Pyx_FastArg_FindKeyword(name, params, info->param_count);
            if (param_index == -2) goto bad;
            if (param_index < 0) {
                __Pyx_RaiseUnexpectedKeywordError(info->func_name, name);
                goto bad;
            }
            const __Pyx_ParamMeta *param = params + param_index;
            if (!(param->flags & __PYX_PARAM_ACCEPTS_KW)) {
                __Pyx_RaiseUnexpectedKeywordError(info->func_name, name);
                goto bad;
            }
            PyObject **slot = localslots[param_index];
            if (*slot) {
                __Pyx_RaiseDoubleKeywordsError(info->func_name, name);
                goto bad;
            }
            PyObject *value = args[positional_args + kw];
            Py_INCREF(value);
            *slot = value;
            if ((param->flags & __PYX_PARAM_IS_KWONLY) &&
                param->default_index == __PYX_PARAM_DEFAULT_MISSING) {
                required_kwonly--;
            }
        }
    }
    if (unlikely(required_kwonly > 0)) {
        extern PyObject **__pyx_string_tab;
        PyObject **stringtab = __pyx_string_tab;
        for (i = 0; i < info->param_count; i++) {
            const __Pyx_ParamMeta *param = params + i;
            if ((param->flags & __PYX_PARAM_IS_KWONLY) &&
                param->default_index == __PYX_PARAM_DEFAULT_MISSING &&
                !*localslots[i]) {
                unsigned short name_index = param->name_index;
                PyObject *param_name = name_index == __PYX_PARAM_DEFAULT_MISSING ?
                    NULL : stringtab[name_index];
                __Pyx_RaiseKeywordRequired(info->func_name, param_name);
                goto bad;
            }
        }
    }
    for (i = 0; i < info->param_count; i++) {
        PyObject **slot = localslots[i];
        if (*slot)
            continue;
        const __Pyx_ParamMeta *param = params + i;
        if (param->default_index != __PYX_PARAM_DEFAULT_MISSING) {
            if (info->defaults) {
                if (unlikely(param->default_index >= info->default_count)) {
                    goto bad;
                }
                PyObject *value = info->defaults[param->default_index];
                Py_INCREF(value);
                *slot = value;
            }
            continue;
        }
        if (param->flags & __PYX_PARAM_IS_KWONLY) {
            extern PyObject **__pyx_string_tab;
            PyObject **stringtab = __pyx_string_tab;
            unsigned short name_index = param->name_index;
            PyObject *param_name = name_index == __PYX_PARAM_DEFAULT_MISSING ?
                NULL : stringtab[name_index];
            __Pyx_RaiseKeywordRequired(info->func_name, param_name);
            goto bad;
        }
        __Pyx_RaiseArgtupleInvalid(
            info->func_name,
            0,
            info->required_pos,
            info->max_pos,
            positional_args);
        goto bad;
    }
    return __PYX_FASTPARSE_SUCCESS;
bad:
    for (i = 0; i < info->param_count; i++) {
        PyObject **slot = localslots[i];
        if (slot && *slot) {
            Py_DECREF(*slot);
            *slot = NULL;
        }
    }
    return __PYX_FASTPARSE_ERROR;
}
#endif

