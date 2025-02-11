#
#  Cython - Compilation-wide options and pragma declarations
#


from dataclasses import dataclass
from typing import Any, Dict, List, Optional


class ShouldBeFromDirective:

    known_directives = []

    def __init__(self, options_name, directive_name=None, disallow=False):
        self.options_name = options_name
        self.directive_name = directive_name or options_name
        self.disallow = disallow
        self.known_directives.append(self)

    def __nonzero__(self):
        self._bad_access()

    def __int__(self):
        self._bad_access()

    def _bad_access(self):
        raise RuntimeError(repr(self))

    def __repr__(self):
        return f"Illegal access of '{self.options_name}' from Options module rather than directive '{self.directive_name}'"


"""
The members of this module are documented using autodata in
Cython/docs/src/reference/compilation.rst.
See https://www.sphinx-doc.org/en/master/usage/extensions/autodoc.html#directive-autoattribute
for how autodata works.
Descriptions of those members should start with a #:
Donc forget to keep the docs in sync by removing and adding
the members in both this file and the .rst file.
"""

#: Whether or not to include docstring in the Python extension. If False, the binary size
#: will be smaller, but the ``__doc__`` attribute of any class or function will be an
#: empty string.
docstrings = True

#: Embed the source code position in the docstrings of functions and classes.
embed_pos_in_docstring = False

# undocumented
pre_import = None

#: Decref global variables in each module on exit for garbage collection.
#: 0: None, 1+: interned objects, 2+: cdef globals, 3+: types objects
#: Mostly for reducing noise in Valgrind as it typically executes at process exit
#: (when all memory will be reclaimed anyways).
#: Note that directly or indirectly executed cleanup code that makes use of global
#: variables or types may no longer be safe when enabling the respective level since
#: there is no guaranteed order in which the (reference counted) objects will
#: be cleaned up.  The order can change due to live references and reference cycles.
generate_cleanup_code = False

#: Should tp_clear() set object fields to None instead of clearing them to NULL?
clear_to_none = True

#: Generate an annotated HTML version of the input source files for debugging and optimisation purposes.
#: This has the same effect as the ``annotate`` argument in :func:`cythonize`.
annotate = False

# When annotating source files in HTML, include coverage information from
# this file.
annotate_coverage_xml = None

#: This will abort the compilation on the first error occurred rather than trying
#: to keep going and printing further error messages.
fast_fail = False

#: Turn all warnings into errors.
warning_errors = False

#: Make unknown names an error.  Python raises a NameError when
#: encountering unknown names at runtime, whereas this option makes
#: them a compile time error.  If you want full Python compatibility,
#: you should disable this option and also 'cache_builtins'.
error_on_unknown_names = True

#: Make uninitialized local variable reference a compile time error.
#: Python raises UnboundLocalError at runtime, whereas this option makes
#: them a compile time error. Note that this option affects only variables
#: of "python object" type.
error_on_uninitialized = True

#: This will convert statements of the form ``for i in range(...)``
#: to ``for i from ...`` when ``i`` is a C integer type, and the direction
#: (i.e. sign of step) can be determined.
#: WARNING: This may change the semantics if the range causes assignment to
#: i to overflow. Specifically, if this option is set, an error will be
#: raised before the loop is entered, whereas without this option the loop
#: will execute until an overflowing value is encountered.
convert_range = True

#: Perform lookups on builtin names only once, at module initialisation
#: time.  This will prevent the module from getting imported if a
#: builtin name that it uses cannot be found during initialisation.
#: Default is True.
#: Note that some legacy builtins are automatically remapped
#: from their Python 2 names to their Python 3 names by Cython
#: when building in Python 3.x,
#: so that they do not get in the way even if this option is enabled.
cache_builtins = True

#: Generate branch prediction hints to speed up error handling etc.
gcc_branch_hints = True

#: Enable this to allow one to write ``your_module.foo = ...`` to overwrite the
#: definition if the cpdef function foo, at the cost of an extra dictionary
#: lookup on every call.
#: If this is false it generates only the Python wrapper and no override check.
lookup_module_cpdef = False

#: Whether or not to embed the Python interpreter, for use in making a
#: standalone executable or calling from external libraries.
#: This will provide a C function which initialises the interpreter and
#: executes the body of this module.
#: See `this demo <https://github.com/cython/cython/tree/master/Demos/embed>`_
#: for a concrete example.
#: If true, the initialisation function is the C main() function, but
#: this option can also be set to a non-empty string to provide a function name explicitly.
#: Default is False.
embed = None

# In previous iterations of Cython, globals() gave the first non-Cython module
# globals in the call stack.  Sage relies on this behavior for variable injection.
old_style_globals = ShouldBeFromDirective('old_style_globals')

#: Allows cimporting from a pyx file without a pxd file.
cimport_from_pyx = False

#: Maximum number of dimensions for buffers -- set lower than number of
#: dimensions in numpy, as
#: slices are passed by value and involve a lot of copying.
buffer_max_dims = 8

#: Number of function closure instances to keep in a freelist (0: no freelists)
closure_freelist_size = 8


def get_directive_defaults():
    # To add an item to this list, all accesses should be changed to use the new
    # directive, and the global option itself should be set to an instance of
    # ShouldBeFromDirective.
    for old_option in ShouldBeFromDirective.known_directives:
        value = globals().get(old_option.options_name)
        assert old_option.directive_name in _directive_defaults
        if not isinstance(value, ShouldBeFromDirective):
            if old_option.disallow:
                raise RuntimeError(
                    "Option '%s' must be set from directive '%s'" % (
                    old_option.option_name, old_option.directive_name))
            else:
                # Warn?
                _directive_defaults[old_option.directive_name] = value
    return _directive_defaults

def copy_inherited_directives(outer_directives, **new_directives):
    # A few directives are not copied downwards and this function removes them.
    # For example, test_assert_path_exists and test_fail_if_path_exists should not be inherited
    #  otherwise they can produce very misleading test failures
    new_directives_out = dict(outer_directives)
    for name in ('test_assert_path_exists', 'test_fail_if_path_exists', 'test_assert_c_code_has', 'test_fail_if_c_code_has',
                 'critical_section'):
        new_directives_out.pop(name, None)
    new_directives_out.update(new_directives)
    return new_directives_out


def copy_for_internal(outer_directives):
    # Reset some directives that users should not control for internal code.
    return copy_inherited_directives(
        outer_directives,
        binding=False,
        profile=False,
        linetrace=False,
    )


# Declare compiler directives
_directive_defaults: "CompilationOptions" = {
    'binding': True,  # was False before 3.0
    'boundscheck' : True,
    'nonecheck' : False,
    'initializedcheck' : True,
    'freethreading_compatible': False,
    'embedsignature': False,
    'embedsignature.format': 'c',
    'auto_cpdef': False,
    'auto_pickle': None,
    'cdivision': False,  # was True before 0.12
    'cdivision_warnings': False,
    'cpow': None,  # was True before 3.0
    # None (not set by user) is treated as slightly different from False
    'c_api_binop_methods': False,  # was True before 3.0
    'overflowcheck': False,
    'overflowcheck.fold': True,
    'always_allow_keywords': True,
    'allow_none_for_extension_args': True,
    'wraparound' : True,
    'ccomplex' : False,  # use C99/C++ for complex types and arith
    'callspec' : "",
    'nogil' : False,
    'gil' : False,
    'with_gil' : False,
    'profile': False,
    'linetrace': False,
    'emit_code_comments': True,  # copy original source code into C code comments
    'annotation_typing': True,  # read type declarations from Python function annotations
    'infer_types': None,
    'infer_types.verbose': False,
    'autotestdict': True,
    'autotestdict.cdef': False,
    'autotestdict.all': False,
    'language_level': None,
    'fast_getattr': False,  # Undocumented until we come up with a better way to handle this everywhere.
    'py2_import': False,  # For backward compatibility of Cython's source code in Py3 source mode
    'preliminary_late_includes_cy28': False,  # Temporary directive in 0.28, to be removed in a later version (see GH#2079).
    'iterable_coroutine': False,  # Make async coroutines backwards compatible with the old asyncio yield-from syntax.
    'c_string_type': 'bytes',
    'c_string_encoding': '',
    'type_version_tag': True,  # enables Py_TPFLAGS_HAVE_VERSION_TAG on extension types
    'unraisable_tracebacks': True,
    'old_style_globals': False,
    'np_pythran': False,
    'fast_gil': False,
    'cpp_locals': False,  # uses std::optional for C++ locals, so that they work more like Python locals
    'legacy_implicit_noexcept': False,

    # set __file__ and/or __path__ to known source/target path at import time (instead of not having them available)
    'set_initial_path' : None,  # SOURCEFILE or "/full/path/to/module"

    'warn': None,
    'warn.undeclared': False,
    'warn.unreachable': True,
    'warn.maybe_uninitialized': False,
    'warn.unused': False,
    'warn.unused_arg': False,
    'warn.unused_result': False,
    'warn.multiple_declarators': True,
    'warn.deprecated.DEF': False,
    'warn.deprecated.IF': True,
    'show_performance_hints': True,

# optimizations
    'optimize.inline_defnode_calls': True,
    'optimize.unpack_method_calls': True,  # increases code size when True
    'optimize.unpack_method_calls_in_pyinit': False,  # uselessly increases code size when True
    'optimize.use_switch': True,

# remove unreachable code
    'remove_unreachable': True,

# control flow debug directives
    'control_flow.dot_output': "",  # Graphviz output filename
    'control_flow.dot_annotate_defs': False,  # Annotate definitions

# test support
    'test_assert_path_exists' : [],
    'test_fail_if_path_exists' : [],
    'test_assert_c_code_has' : [],
    'test_fail_if_c_code_has' : [],

# experimental, subject to change
    'formal_grammar': False,
}

# Extra warning directives
extra_warnings = {
    'warn.maybe_uninitialized': True,
    'warn.unreachable': True,
    'warn.unused': True,
}

def one_of(*args, map=None):
    def validate(name, value):
        if map is not None:
            value = map.get(value, value)
        if value not in args:
            raise ValueError("%s directive must be one of %s, got '%s'" % (
                name, args, value))
        return value
    return validate


_normalise_common_encoding_name = {
    'utf8': 'utf8',
    'utf-8': 'utf8',
    'default': 'utf8',
    'ascii': 'ascii',
    'us-ascii': 'ascii',
}.get


def normalise_encoding_name(option_name, encoding):
    """>>> normalise_encoding_name('c_string_encoding', 'ascii')
    'ascii'
    >>> normalise_encoding_name('c_string_encoding', 'AsCIi')
    'ascii'
    >>> normalise_encoding_name('c_string_encoding', 'us-ascii')
    'ascii'
    >>> normalise_encoding_name('c_string_encoding', 'utF8')
    'utf8'
    >>> normalise_encoding_name('c_string_encoding', 'utF-8')
    'utf8'
    >>> normalise_encoding_name('c_string_encoding', 'deFAuLT')
    'utf8'
    >>> normalise_encoding_name('c_string_encoding', 'default')
    'utf8'
    >>> normalise_encoding_name('c_string_encoding', 'SeriousLyNoSuch--Encoding')
    'SeriousLyNoSuch--Encoding'.
    """  # noqa: D205, D402
    if not encoding:
        return ''
    encoding_name = _normalise_common_encoding_name(encoding.lower())
    if encoding_name is not None:
        return encoding_name

    import codecs
    try:
        decoder = codecs.getdecoder(encoding)
    except LookupError:
        return encoding  # may exists at runtime ...
    for name in ('ascii', 'utf8'):
        if codecs.getdecoder(name) == decoder:
            return name
    return encoding

# use as a sential value to defer analysis of the arguments
# instead of analysing them in InterpretCompilerDirectives. The dataclass directives are quite
# complicated and it's easier to deal with them at the point the dataclass is created
class DEFER_ANALYSIS_OF_ARGUMENTS:
    pass
DEFER_ANALYSIS_OF_ARGUMENTS = DEFER_ANALYSIS_OF_ARGUMENTS()

@dataclass
class DirectiveScopes(dict):
    #: Compiler directives used during compilation
    language_level: str                   # values can be None/2/3/'3str', where None == 2+warning
    auto_pickle: bool                     # Enable auto pickling
    locals: dict                         # Local variable declarations
    final: bool                          # Final cdef classes and methods
    collection_type: str                 # Collection type ("sequence" only)
    nogil: Any                          # No GIL directives 
    gil: Any                            # GIL acquisition directives
    critical_section: Any                # Critical section directives
    with_gil: Any                        # With GIL directives
    internal: bool                       # cdef class visibility in module dict
    infer_types: bool                    # Type inference (True/None/False)
    binding: bool                        # Enable binding
    cfunc: Any                          # C function decorator (no value)
    ccall: Any                          # C call decorator (no value) 
    ufunc: Any                          # UFuncs (no value)
    cpow: bool                          # Enable C power operations
    inline: Any                         # Function inlining
    staticmethod: Any                    # Static method decorator
    cclass: Any                         # cdef class decorator
    no_gc_clear: bool                    # Disable GC clearing 
    no_gc: bool                         # Disable GC completely
    returns: type                        # Return type annotation
    exceptval: type                      # Exception value type
    set_initial_path: str                # Initial module path
    freelist: int                        # Freelist size
    c_string_type: str                   # C string type
    c_string_encoding: str               # C string encoding
    trashcan: bool                       # Enable trashcan support
    total_ordering: Any                  # Total ordering support
    dataclasses_dataclass: Any           # Dataclass decorator support
    dataclasses_field: Any               # Dataclass field support 
    embedsignature_format: str           # Signature format

# Override types possibilities above, if needed
directive_types: "DirectiveScopes" = {
    'language_level': str,  # values can be None/2/3/'3str', where None == 2+warning
    'auto_pickle': bool,
    'locals': dict,
    'final' : bool,  # final cdef classes and methods
    'collection_type': one_of('sequence'),
    'nogil' : DEFER_ANALYSIS_OF_ARGUMENTS,
    'gil' : DEFER_ANALYSIS_OF_ARGUMENTS,
    'critical_section' : DEFER_ANALYSIS_OF_ARGUMENTS,
    'with_gil' : None,
    'internal' : bool,  # cdef class visibility in the module dict
    'infer_types' : bool,  # values can be True/None/False
    'binding' : bool,
    'cfunc' : None,  # decorators do not take directive value
    'ccall' : None,
    'ufunc': None,
    'cpow' : bool,
    'inline' : None,
    'staticmethod' : None,
    'cclass' : None,
    'no_gc_clear' : bool,
    'no_gc' : bool,
    'returns' : type,
    'exceptval': type,  # actually (type, check=True/False), but has its own parser
    'set_initial_path': str,
    'freelist': int,
    'c_string_type': one_of('bytes', 'bytearray', 'str', 'unicode', map={'unicode': 'str'}),
    'c_string_encoding': normalise_encoding_name,
    'trashcan': bool,
    'total_ordering': None,
    'dataclasses.dataclass': DEFER_ANALYSIS_OF_ARGUMENTS,
    'dataclasses.field': DEFER_ANALYSIS_OF_ARGUMENTS,
    'embedsignature.format': one_of('c', 'clinic', 'python'),
}

for key, val in _directive_defaults.items():
    if key not in directive_types:
        directive_types[key] = type(val)

directive_scopes: "DirectiveScopes" = {  # defaults to available everywhere
    # 'module', 'function', 'class', 'with statement'
    'auto_pickle': ('module', 'cclass'),
    'final' : ('cclass', 'function'),
    'ccomplex' : ('module',),
    'collection_type': ('cclass',),
    'nogil' : ('function', 'with statement'),
    'gil' : ('with statement'),
    'with_gil' : ('function',),
    'critical_section': ('function', 'with statement'),
    'inline' : ('function',),
    'cfunc' : ('function', 'with statement'),
    'ccall' : ('function', 'with statement'),
    'returns' : ('function',),
    'exceptval' : ('function',),
    'locals' : ('function',),
    'staticmethod' : ('function',),  # FIXME: analysis currently lacks more specific function scope
    'no_gc_clear' : ('cclass',),
    'no_gc' : ('cclass',),
    'internal' : ('cclass',),
    'cclass' : ('class', 'cclass', 'with statement'),
    'autotestdict' : ('module',),
    'autotestdict.all' : ('module',),
    'autotestdict.cdef' : ('module',),
    'set_initial_path' : ('module',),
    'test_assert_path_exists' : ('function', 'class', 'cclass'),
    'test_fail_if_path_exists' : ('function', 'class', 'cclass'),
    'test_assert_c_code_has' : ('module',),
    'test_fail_if_c_code_has' : ('module',),
    'freelist': ('cclass',),
    'formal_grammar': ('module',),
    'emit_code_comments': ('module',),
    # Avoid scope-specific to/from_py_functions for c_string.
    'c_string_type': ('module',),
    'c_string_encoding': ('module',),
    'type_version_tag': ('module', 'cclass'),
    'language_level': ('module',),
    # globals() could conceivably be controlled at a finer granularity,
    # but that would complicate the implementation
    'old_style_globals': ('module',),
    'np_pythran': ('module',),
    'preliminary_late_includes_cy28': ('module',),
    'fast_gil': ('module',),
    'iterable_coroutine': ('module', 'function'),
    'trashcan' : ('cclass',),
    'total_ordering': ('class', 'cclass'),
    'dataclasses.dataclass' : ('class', 'cclass'),
    'cpp_locals': ('module', 'function', 'cclass'),  # I don't think they make sense in a with_statement
    'ufunc': ('function',),
    'legacy_implicit_noexcept': ('module', ),
    'control_flow.dot_output': ('module',),
    'control_flow.dot_annotate_defs': ('module',),
    'freethreading_compatible': ('module',)
}


# A list of directives that (when used as a decorator) are only applied to
# the object they decorate and not to its children.
immediate_decorator_directives = {
    'cfunc', 'ccall', 'cclass', 'dataclasses.dataclass', 'ufunc',
    # function signature directives
    'inline', 'exceptval', 'returns', 'with_gil',  # 'nogil',
    # class directives
    'freelist', 'no_gc', 'no_gc_clear', 'type_version_tag', 'final',
    'auto_pickle', 'internal', 'collection_type', 'total_ordering',
    # testing directives
    'test_fail_if_path_exists', 'test_assert_path_exists',
}


def parse_directive_value(name, value, relaxed_bool=False):
    """Parses value as an option value for the given name and returns
    the interpreted value. None is returned if the option does not exist.

    >>> print(parse_directive_value('nonexisting', 'asdf asdfd'))
    None
    >>> parse_directive_value('boundscheck', 'True')
    True
    >>> parse_directive_value('boundscheck', 'true')
    Traceback (most recent call last):
       ...
    ValueError: boundscheck directive must be set to True or False, got 'true'

    >>> parse_directive_value('c_string_encoding', 'us-ascii')
    'ascii'
    >>> parse_directive_value('c_string_type', 'str')
    'str'
    >>> parse_directive_value('c_string_type', 'bytes')
    'bytes'
    >>> parse_directive_value('c_string_type', 'bytearray')
    'bytearray'
    >>> parse_directive_value('c_string_type', 'unicode')
    'str'
    >>> parse_directive_value('c_string_type', 'unnicode')
    Traceback (most recent call last):
    ValueError: c_string_type directive must be one of ('bytes', 'bytearray', 'str', 'unicode'), got 'unnicode'
    """  # noqa: D205, D401
    type = directive_types.get(name)
    if not type:
        return None
    orig_value = value
    if type is bool:
        value = str(value)
        if value == 'True':
            return True
        if value == 'False':
            return False
        if relaxed_bool:
            value = value.lower()
            if value in ("true", "yes"):
                return True
            elif value in ("false", "no"):
                return False
        raise ValueError("%s directive must be set to True or False, got '%s'" % (
            name, orig_value))
    elif type is int:
        try:
            return int(value)
        except ValueError:
            raise ValueError("%s directive must be set to an integer, got '%s'" % (
                name, orig_value))
    elif type is str:
        return str(value)
    elif callable(type):
        return type(name, value)
    else:
        assert False


def parse_directive_list(s, relaxed_bool=False, ignore_unknown=False,
                         current_settings=None):
    """Parses a comma-separated list of pragma options. Whitespace
    is not considered.

    >>> parse_directive_list('      ')
    {}
    >>> (parse_directive_list('boundscheck=True') ==
    ... {'boundscheck': True})
    True
    >>> parse_directive_list('  asdf')
    Traceback (most recent call last):
       ...
    ValueError: Expected "=" in option "asdf"
    >>> parse_directive_list('boundscheck=hey')
    Traceback (most recent call last):
       ...
    ValueError: boundscheck directive must be set to True or False, got 'hey'
    >>> parse_directive_list('unknown=True')
    Traceback (most recent call last):
       ...
    ValueError: Unknown option: "unknown"
    >>> warnings = parse_directive_list('warn.all=True')
    >>> len(warnings) > 1
    True
    >>> sum(warnings.values()) == len(warnings)  # all true.
    True
    """  # noqa: D205, D401
    if current_settings is None:
        result = {}
    else:
        result = current_settings
    for item in s.split(','):
        item = item.strip()
        if not item:
            continue
        if '=' not in item:
            raise ValueError('Expected "=" in option "%s"' % item)
        name, value = [s.strip() for s in item.strip().split('=', 1)]
        if name not in _directive_defaults:
            found = False
            if name.endswith('.all'):
                prefix = name[:-3]
                for directive in _directive_defaults:
                    if directive.startswith(prefix):
                        found = True
                        parsed_value = parse_directive_value(directive, value, relaxed_bool=relaxed_bool)
                        result[directive] = parsed_value
            if not found and not ignore_unknown:
                raise ValueError('Unknown option: "%s"' % name)
        elif directive_types.get(name) is list:
            if name in result:
                result[name].append(value)
            else:
                result[name] = [value]
        else:
            parsed_value = parse_directive_value(name, value, relaxed_bool=relaxed_bool)
            result[name] = parsed_value
    return result


def parse_variable_value(value):
    """Parses value as an option value for the given name and returns
    the interpreted value.

    >>> parse_variable_value('True')
    True
    >>> parse_variable_value('true')
    'true'
    >>> parse_variable_value('us-ascii')
    'us-ascii'
    >>> parse_variable_value('str')
    'str'
    >>> parse_variable_value('123')
    123
    >>> parse_variable_value('1.23')
    1.23

    """  # noqa: D205, D401
    if value == "True":
        return True
    elif value == "False":
        return False
    elif value == "None":
        return None
    elif value.isdigit():
        return int(value)
    else:
        try:
            value = float(value)
        except Exception:
            # Not a float
            pass
        return value


def parse_compile_time_env(s, current_settings=None):
    """Parse a comma-separated list of pragma options. Whitespace is not considered.

    >>> parse_compile_time_env('      ')
    {}
    >>> (parse_compile_time_env('HAVE_OPENMP=True') ==
    ... {'HAVE_OPENMP': True})
    True
    >>> parse_compile_time_env('  asdf')
    Traceback (most recent call last):
       ...
    ValueError: Expected "=" in option "asdf"
    >>> parse_compile_time_env('NUM_THREADS=4') == {'NUM_THREADS': 4}
    True
    >>> parse_compile_time_env('unknown=anything') == {'unknown': 'anything'}
    True
    """
    if current_settings is None:
        result = {}
    else:
        result = current_settings
    for item in s.split(','):
        item = item.strip()
        if not item:
            continue
        if '=' not in item:
            raise ValueError('Expected "=" in option "%s"' % item)
        name, value = [s.strip() for s in item.split('=', 1)]
        result[name] = parse_variable_value(value)
    return result

@dataclass
class CompileDirectives:
    #: Whether or not to include docstring in the Python extension. If False, the binary size
    #: will be smaller, but the ``__doc__`` attribute of any class or function will be an
    #: empty string.
    docstrings = True

    #: Embed the source code position in the docstrings of functions and classes.
    embed_pos_in_docstring = False

    # undocumented
    pre_import = None

    #: Decref global variables in each module on exit for garbage collection.
    #: 0: None, 1+: interned objects, 2+: cdef globals, 3+: types objects
    #: Mostly for reducing noise in Valgrind as it typically executes at process exit
    #: (when all memory will be reclaimed anyways).
    #: Note that directly or indirectly executed cleanup code that makes use of global
    #: variables or types may no longer be safe when enabling the respective level since
    #: there is no guaranteed order in which the (reference counted) objects will
    #: be cleaned up.  The order can change due to live references and reference cycles.
    generate_cleanup_code = False

    #: Should tp_clear() set object fields to None instead of clearing them to NULL?
    clear_to_none = True

    #: Generate an annotated HTML version of the input source files for debugging and optimisation purposes.
    #: This has the same effect as the ``annotate`` argument in :func:`cythonize`.
    annotate = False

    # When annotating source files in HTML, include coverage information from
    # this file.
    annotate_coverage_xml = None

    #: This will abort the compilation on the first error occurred rather than trying
    #: to keep going and printing further error messages.
    fast_fail = False

    #: Turn all warnings into errors.
    warning_errors = False

    #: Make unknown names an error.  Python raises a NameError when
    #: encountering unknown names at runtime, whereas this option makes
    #: them a compile time error.  If you want full Python compatibility,
    #: you should disable this option and also 'cache_builtins'.
    error_on_unknown_names = True

    #: Make uninitialized local variable reference a compile time error.
    #: Python raises UnboundLocalError at runtime, whereas this option makes
    #: them a compile time error. Note that this option affects only variables
    #: of "python object" type.
    error_on_uninitialized = True

    #: This will convert statements of the form ``for i in range(...)``
    #: to ``for i from ...`` when ``i`` is a C integer type, and the direction
    #: (i.e. sign of step) can be determined.
    #: WARNING: This may change the semantics if the range causes assignment to
    #: i to overflow. Specifically, if this option is set, an error will be
    #: raised before the loop is entered, whereas without this option the loop
    #: will execute until an overflowing value is encountered.
    convert_range = True

    #: Perform lookups on builtin names only once, at module initialisation
    #: time.  This will prevent the module from getting imported if a
    #: builtin name that it uses cannot be found during initialisation.
    #: Default is True.
    #: Note that some legacy builtins are automatically remapped
    #: from their Python 2 names to their Python 3 names by Cython
    #: when building in Python 3.x,
    #: so that they do not get in the way even if this option is enabled.
    cache_builtins = True

    #: Generate branch prediction hints to speed up error handling etc.
    gcc_branch_hints = True

    #: Enable this to allow one to write ``your_module.foo = ...`` to overwrite the
    #: definition if the cpdef function foo, at the cost of an extra dictionary
    #: lookup on every call.
    #: If this is false it generates only the Python wrapper and no override check.
    lookup_module_cpdef = False

    #: Whether or not to embed the Python interpreter, for use in making a
    #: standalone executable or calling from external libraries.
    #: This will provide a C function which initialises the interpreter and
    #: executes the body of this module.
    #: See `this demo <https://github.com/cython/cython/tree/master/Demos/embed>`_
    #: for a concrete example.
    #: If true, the initialisation function is the C main() function, but
    #: this option can also be set to a non-empty string to provide a function name explicitly.
    #: Default is False.
    embed = None

    # In previous iterations of Cython, globals() gave the first non-Cython module
    # globals in the call stack.  Sage relies on this behavior for variable injection.
    old_style_globals = ShouldBeFromDirective('old_style_globals')

    #: Allows cimporting from a pyx file without a pxd file.
    cimport_from_pyx = False

    #: Maximum number of dimensions for buffers -- set lower than number of
    #: dimensions in numpy, as
    #: slices are passed by value and involve a lot of copying.
    buffer_max_dims = 8

    #: Number of function closure instances to keep in a freelist (0: no freelists)
    closure_freelist_size = 8

# ------------------------------------------------------------------------
# CompilationOptions are constructed from user input and are the `option`
#  object passed throughout the compilation pipeline.

@dataclass
class CompilationOptions(dict):
    """See default_options at the end of this module for a list of all possible
    options and CmdLine.usage and CmdLine.parse_command_line() for their 
    meaning.
    """  # noqa: D205

    include_path: List[str] = None
    show_version: int = 0
    use_listing_file: int = 0
    errors_to_stderr: int = 1
    cplus: int = 0
    output_file: Optional[str] = None
    depfile: Optional[str] = None
    annotate: Optional[bool] = None
    annotate_coverage_xml: Optional[str] = None
    generate_pxi: int = 0
    capi_reexport_cincludes: int = 0
    working_path: str = ""
    timestamps: Optional[Any] = None
    verbose: int = 0
    quiet: int = 0
    compiler_directives: Dict[str, Any] = None
    embedded_metadata: Dict[str, Any] = None
    evaluate_tree_assertions: bool = False
    emit_linenums: bool = False
    relative_path_in_code_position_comments: bool = True
    c_line_in_traceback: Optional[bool] = None
    language_level: Optional[Any] = None
    formal_grammar: bool = False
    gdb_debug: bool = False
    compile_time_env: Optional[Dict[str, Any]] = None
    module_name: Optional[str] = None
    common_utility_include_dir: Optional[str] = None
    output_dir: Optional[str] = None
    build_dir: Optional[str] = None
    cache: Optional[Any] = None
    create_extension: Optional[Any] = None
    np_pythran: bool = False
    legacy_implicit_noexcept: Optional[bool] = None


    def __post_init__(self):
        if self.include_path is None:
            self.include_path = []
        if self.compiler_directives is None:
            self.compiler_directives = {}
        if self.embedded_metadata is None:
            self.embedded_metadata = {}

        # Validate compiler directives
        directive_defaults = get_directive_defaults()
        unknown_directives = set(self.compiler_directives) - set(directive_defaults)
        if unknown_directives:
            message = f"got unknown compiler directive{'s' if len(unknown_directives) > 1 else ''}: {', '.join(unknown_directives)}"
            raise ValueError(message)

        if self.compiler_directives.get('np_pythran', False) and not self.cplus:
            import warnings
            warnings.warn("C++ mode forced when in Pythran mode!")
            self.cplus = True

        if not self.language_level:
            self.language_level = directive_defaults.get('language_level')

    def configure_language_defaults(self, source_extension):
        if source_extension == 'py' and self.compiler_directives.get('binding') is None:
            self.compiler_directives['binding'] = True

    def get_fingerprint(self):
        """Return a string that contains all the options that are relevant for cache invalidation."""
        exclude_keys = {
            'show_version', 'errors_to_stderr', 'verbose', 'quiet',
            'output_file', 'output_dir', 'depfile', 'timestamps',
            'cache', 'compiler_directives', 'include_path', 'working_path',
            'create_extension', 'build_dir'
        }

        data = {}
        for key, value in self.__dict__.items():
            if key in exclude_keys:
                continue
            if key == 'capi_reexport_cincludes' and value:
                raise NotImplementedError('capi_reexport_cincludes is not compatible with Cython caching')
            if key == 'common_utility_include_dir' and value:
                raise NotImplementedError('common_utility_include_dir is not compatible with Cython caching yet')
            data[key] = value

        def to_fingerprint(item):
            """Recursively convert item to string with deterministic dict ordering."""
            if isinstance(item, dict):
                item = sorted([(repr(key), to_fingerprint(value)) for key, value in item.items()])
            return repr(item)

        return to_fingerprint(data)


# ------------------------------------------------------------------------
#
#  Set the default options depending on the platform
#
# ------------------------------------------------------------------------

default_options: CompilationOptions = CompilationOptions(
    include_path=[],
    show_version=0,
    use_listing_file=0,
    errors_to_stderr=1,
    cplus=0,
    output_file=None,
    depfile=None,
    annotate=None,
    annotate_coverage_xml=None,
    generate_pxi=0,
    capi_reexport_cincludes=0,
    working_path="",
    timestamps=None,
    verbose=0,
    quiet=0,
    compiler_directives={},
    embedded_metadata={},
    evaluate_tree_assertions=False,
    emit_linenums=False,
    relative_path_in_code_position_comments=True,
    c_line_in_traceback=None,
    language_level=None,
    formal_grammar=False,
    gdb_debug=False,
    compile_time_env=None,
    module_name=None,
    common_utility_include_dir=None,
    output_dir=None,
    build_dir=None,
    cache=None,
    create_extension=None,
    np_pythran=False,
    legacy_implicit_noexcept=None,
)




OPTIMIZED_OPTIONS: CompilationOptions = {
    'binding': True,  # Needed for Python attribute access optimization
    'boundscheck': False,  # Disable bounds checking for speed
    'nonecheck': False,  # Disable None checks for performance
    'initializedcheck': False,  # Avoid unnecessary initialization checks
    'embedsignature': True,  # Reduce binary size
    'auto_cpdef': True,  # Generate C functions automatically for performance
    'auto_pickle': None,  # Control pickle behavior explicitly
    'cdivision': True,  # Enable C-style division for efficiency
    'cdivision_warnings': False,  # Avoid unnecessary warnings
    'cpow': True,  # Optimize power operations
    'c_api_binop_methods': True,  # Use optimized C-level binary operations
    'overflowcheck': False,  # Disable Python integer overflow checks
    'overflowcheck.fold': True,  # Optimize folding for overflow checking
    'always_allow_keywords': False,  # Avoid overhead of keyword argument checking
    'allow_none_for_extension_args': False,  # Strict type safety
    'wraparound': False,  # Disable negative indexing checks
    'ccomplex': True,  # Use C99/C++ complex number arithmetic
    'profile': False,  # Disable profiling to remove performance overhead
    'linetrace': False,  # Disable line tracing
    'emit_code_comments': False,  # Reduce generated C code size
    'annotation_typing': True,  # Enable type annotations
    'infer_types': True,  # Allow Cython to infer types for better performance
    'infer_types.verbose': False,  # Avoid extra debugging output
    'autotestdict': False,  # Reduce object dictionary overhead
    'autotestdict.cdef': False,
    'autotestdict.all': False,
    'language_level': '3',  # Ensure Python 3 compatibility
    'fast_getattr': True,  # Optimize attribute access
    'py2_import': False,  # Disable Python 2 compatibility
    'iterable_coroutine': False,  # Disable legacy coroutine behavior
    'c_string_type': 'bytes',  # Use efficient byte-based string storage
    'c_string_encoding': 'utf8',  # Standardize encoding for better performance
    'type_version_tag': True,  # Enable type versioning optimizations
    'unraisable_tracebacks': False,  # Avoid extra traceback handling
    'old_style_globals': False,
    'np_pythran': True,  # Enable NumPy/Pythran optimizations
    'fast_gil': True,  # Optimize GIL handling
    'cpp_locals': True,  # Use std::optional for local variables in C++
    'legacy_implicit_noexcept': False,  # Avoid legacy exception handling

    # Set __file__ and/or __path__ to known values at runtime
    'set_initial_path': None,

    # Optimization-specific warnings
    'warn': None,
    'warn.undeclared': False,
    'warn.unreachable': False,  # Disable unreachable code warnings
    'warn.maybe_uninitialized': False,  # Avoid unnecessary init warnings
    'warn.unused': False,  # Disable unused variable warnings
    'warn.unused_arg': False,  # Disable unused argument warnings
    'warn.unused_result': False,  # Ignore unused return values
    'warn.multiple_declarators': False,  # Allow multiple C declarations
    'warn.deprecated.DEF': False,
    'warn.deprecated.IF': False,
    'show_performance_hints': True,  # Enable performance warnings

    # Advanced optimization flags
    'optimize.inline_defnode_calls': True,  # Inline small function calls
    'optimize.unpack_method_calls': True,  # Reduce method call overhead
    'optimize.unpack_method_calls_in_pyinit': False,  # Avoid extra size increase
    'optimize.use_switch': True,  # Use switch statements where applicable

    # Control flow optimizations
    'remove_unreachable': True,  # Eliminate dead code

    # Experimental features
    'formal_grammar': False,  # Avoid experimental grammar parsing

    # Enable parallelism optimizations
    'freethreading_compatible': True,
}

# Apply optimized options globally
_directive_defaults.update(OPTIMIZED_OPTIONS)