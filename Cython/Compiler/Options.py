#
#  Cython - Compilation-wide options and pragma declarations
#

from dataclasses import dataclass, field, asdict
from typing import Any, Dict, List, Optional, Union, Callable, Type, TypeVar, Set, Tuple, Literal, TypedDict

embedding_file_name: Optional[str]
class DirectivesDict(TypedDict, total=False):
    """TypedDict representing the default values for compiler directives."""
    binding: bool
    boundscheck: bool
    nonecheck: bool
    initializedcheck: bool
    freethreading_compatible: bool
    subinterpreters_compatible: str
    embedsignature: bool
    embedsignature_format: str
    auto_cpdef: bool
    auto_pickle: Optional[bool]
    cdivision: bool
    cdivision_warnings: bool
    cpow: Optional[bool]
    c_api_binop_methods: bool
    overflowcheck: bool
    overflowcheck_fold: bool
    always_allow_keywords: bool
    allow_none_for_extension_args: bool
    wraparound: bool
    ccomplex: bool
    callspec: str
    nogil: bool
    gil: bool
    with_gil: bool
    profile: bool
    linetrace: bool
    emit_code_comments: bool
    annotation_typing: bool
    infer_types: Optional[bool]
    infer_types_verbose: bool
    autotestdict: bool
    autotestdict_cdef: bool
    autotestdict_all: bool
    language_level: Optional[Any]
    fast_getattr: bool
    py2_import: bool
    preliminary_late_includes_cy28: bool
    iterable_coroutine: bool
    c_string_type: str
    c_string_encoding: str
    type_version_tag: bool
    unraisable_tracebacks: bool
    old_style_globals: bool
    np_pythran: bool
    fast_gil: bool
    cpp_locals: bool
    legacy_implicit_noexcept: bool
    c_compile_guard: str
    set_initial_path: Optional[str]
    warn: Optional[Any]
    warn_undeclared: bool
    warn_unreachable: bool
    warn_maybe_uninitialized: bool
    warn_unused: bool
    warn_unused_arg: bool
    warn_unused_result: bool
    warn_multiple_declarators: bool
    warn_deprecated_DEF: bool
    warn_deprecated_IF: bool
    show_performance_hints: bool
    optimize_inline_defnode_calls: bool
    optimize_unpack_method_calls: bool
    optimize_unpack_method_calls_in_pyinit: bool
    optimize_use_switch: bool
    remove_unreachable: bool
    control_flow_dot_output: str
    control_flow_dot_annotate_defs: bool
    test_assert_path_exists: List[str]
    test_fail_if_path_exists: List[str]
    test_assert_c_code_has: List[str]
    test_fail_if_c_code_has: List[str]
    formal_grammar: bool

class DirectiveScopesDict(TypedDict, total=False):
    """TypedDict representing directive scopes mapping directives to their allowed scopes."""
    auto_pickle: Tuple[str, ...]
    final: Tuple[str, ...]
    ccomplex: Tuple[str, ...]
    collection_type: Tuple[str, ...]
    nogil: Tuple[str, ...]
    gil: Tuple[str, ...]
    with_gil: Tuple[str, ...]
    critical_section: Tuple[str, ...]
    inline: Tuple[str, ...]
    cfunc: Tuple[str, ...]
    ccall: Tuple[str, ...]
    returns: Tuple[str, ...]
    exceptval: Tuple[str, ...]
    locals: Tuple[str, ...]
    staticmethod: Tuple[str, ...]
    no_gc_clear: Tuple[str, ...]
    no_gc: Tuple[str, ...]
    internal: Tuple[str, ...]
    cclass: Tuple[str, ...]
    autotestdict: Tuple[str, ...]
    autotestdict_all: Tuple[str, ...]
    autotestdict_cdef: Tuple[str, ...]
    set_initial_path: Tuple[str, ...]
    test_assert_path_exists: Tuple[str, ...]
    test_fail_if_path_exists: Tuple[str, ...]
    test_assert_c_code_has: Tuple[str, ...]
    test_fail_if_c_code_has: Tuple[str, ...]
    freelist: Tuple[str, ...]
    formal_grammar: Tuple[str, ...]
    emit_code_comments: Tuple[str, ...]
    c_string_type: Tuple[str, ...]
    c_string_encoding: Tuple[str, ...]
    type_version_tag: Tuple[str, ...]
    language_level: Tuple[str, ...]
    old_style_globals: Tuple[str, ...]
    np_pythran: Tuple[str, ...]
    preliminary_late_includes_cy28: Tuple[str, ...]
    fast_gil: Tuple[str, ...]
    iterable_coroutine: Tuple[str, ...]
    trashcan: Tuple[str, ...]
    total_ordering: Tuple[str, ...]
    dataclasses_dataclass: Tuple[str, ...]
    cpp_locals: Tuple[str, ...]
    ufunc: Tuple[str, ...]
    legacy_implicit_noexcept: Tuple[str, ...]
    c_compile_guard: Tuple[str, ...]
    control_flow_dot_output: Tuple[str, ...]
    control_flow_dot_annotate_defs: Tuple[str, ...]
    freethreading_compatible: Tuple[str, ...]
    subinterpreters_compatible: Tuple[str, ...]

# Define a DirectiveScopes type for type hints
class DirectiveScopes(Dict[str, Union[Type, Callable[[str, Any], Any], Any]]):
    """Type representing directive types mapping directives to their types or validation functions."""
    pass

# Sentinel for deferred analysis arguments
class _DeferAnalysisOfArgumentsType:
    """Sentinel value to defer analysis of function arguments."""
    def __repr__(self):
        return "DEFER_ANALYSIS_OF_ARGUMENTS"

# Create a singleton instance
DEFER_ANALYSIS_OF_ARGUMENTS = _DeferAnalysisOfArgumentsType()

# ---------------------------------------------------------------------------
# Helper type aliases for directive type mappings
# ---------------------------------------------------------------------------

# Forward reference string avoids the need to define the class before this alias
DirectiveType = Union[Type, Callable[[str, Any], Any], '_DeferAnalysisOfArgumentsType', None]
# Mapping from directive-name strings to their validation/typing helpers
DirectiveTypesMap = Dict[str, DirectiveType]

class ShouldBeFromDirective:

    known_directives = []

    def __init__(self, options_name, directive_name=None, disallow=False):
        self.options_name = options_name
        self.directive_name = directive_name or options_name
        self.disallow = disallow
        self.known_directives.append(self)

    def __bool__(self):
        # Python 3 equivalent of __nonzero__
        self._bad_access()
        return False  # Never reached

    def __nonzero__(self):
        # Python 2 compatibility
        self._bad_access()

    def __int__(self):
        self._bad_access()

    def _bad_access(self):
        raise RuntimeError(
            f"Illegal access of option '{self.options_name}'. "
            f"Use directive '{self.directive_name}' instead."
        )

    def __repr__(self):
        return f"ShouldBeFromDirective(options_name='{self.options_name}', directive_name='{self.directive_name}')"


"""
The members of this module are documented using autodata in
Cython/docs/src/reference/compilation.rst.
See https://www.sphinx-doc.org/en/master/usage/extensions/autodoc.html#directive-autoattribute
for how autodata works.
Descriptions of those members should start with a #:
Donc forget to keep the docs in sync by removing and adding
the members in both this file and the .rst file.
"""

# Global options: these can be accessed directly but also correspond to directives.
# Their default values are defined in _directive_defaults.

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

# Directive-only options: Accessing these directly will raise an error.
# These are placeholders managed by ShouldBeFromDirective.
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

# Extra warning directives
extra_warnings = {
    'warn.maybe_uninitialized': True,
    'warn.unreachable': True,
    'warn.unused': True,
}

@dataclass
class Directives:
    """Dataclass representing all Cython compiler directives with their default values."""
    # Default values for all directives
    binding: bool = True  # was False before 3.0
    boundscheck: bool = True
    nonecheck: bool = False
    initializedcheck: bool = True
    freethreading_compatible: bool = False
    subinterpreters_compatible: str = 'no'
    embedsignature: bool = False
    embedsignature_format: str = 'c'
    auto_cpdef: bool = False
    auto_pickle: Optional[bool] = None
    cdivision: bool = False  # was True before 0.12
    cdivision_warnings: bool = False
    cpow: Optional[bool] = None  # was True before 3.0
    c_api_binop_methods: bool = False  # was True before 3.0
    overflowcheck: bool = False
    overflowcheck_fold: bool = True
    always_allow_keywords: bool = True
    allow_none_for_extension_args: bool = True
    wraparound: bool = True
    ccomplex: bool = False  # use C99/C++ for complex types and arith
    callspec: str = ""
    nogil: bool = False
    gil: bool = False
    with_gil: bool = False
    profile: bool = False
    linetrace: bool = False
    emit_code_comments: bool = True  # copy original source code into C code comments
    annotation_typing: bool = True  # read type declarations from Python function annotations
    infer_types: Optional[bool] = None
    infer_types_verbose: bool = False
    autotestdict: bool = True
    autotestdict_cdef: bool = False
    autotestdict_all: bool = False
    language_level: Optional[Any] = None
    fast_getattr: bool = False  # Undocumented until we come up with a better way to handle this everywhere.
    py2_import: bool = False  # For backward compatibility of Cython's source code in Py3 source mode
    preliminary_late_includes_cy28: bool = False  # Temporary directive in 0.28, to be removed in a later version (see GH#2079).
    iterable_coroutine: bool = False  # Make async coroutines backwards compatible with the old asyncio yield-from syntax.
    c_string_type: str = 'bytes'
    c_string_encoding: str = ''
    type_version_tag: bool = True  # enables Py_TPFLAGS_HAVE_VERSION_TAG on extension types
    unraisable_tracebacks: bool = True
    old_style_globals: bool = False
    np_pythran: bool = False
    fast_gil: bool = False
    cpp_locals: bool = False  # uses std::optional for C++ locals, so that they work more like Python locals
    legacy_implicit_noexcept: bool = False
    c_compile_guard: str = ''
    set_initial_path: Optional[str] = None  # SOURCEFILE or "/full/path/to/module"
    warn: Optional[Any] = None
    warn_undeclared: bool = False
    warn_unreachable: bool = True
    warn_maybe_uninitialized: bool = False
    warn_unused: bool = False
    warn_unused_arg: bool = False
    warn_unused_result: bool = False
    warn_multiple_declarators: bool = True
    warn_deprecated_DEF: bool = False
    warn_deprecated_IF: bool = True
    show_performance_hints: bool = True
    optimize_inline_defnode_calls: bool = True
    optimize_unpack_method_calls: bool = True  # increases code size when True
    optimize_unpack_method_calls_in_pyinit: bool = False  # uselessly increases code size when True
    optimize_use_switch: bool = True
    remove_unreachable: bool = True
    control_flow_dot_output: str = ""  # Graphviz output filename
    control_flow_dot_annotate_defs: bool = False  # Annotate definitions
    test_assert_path_exists: List[str] = field(default_factory=list)
    test_fail_if_path_exists: List[str] = field(default_factory=list)
    test_assert_c_code_has: List[str] = field(default_factory=list)
    test_fail_if_c_code_has: List[str] = field(default_factory=list)
    formal_grammar: bool = False
    
    # Mapping for attribute names with dots
    _attr_mapping: Dict[str, str] = field(default_factory=lambda: {
        'embedsignature.format': 'embedsignature_format',
        'overflowcheck.fold': 'overflowcheck_fold',
        'infer_types.verbose': 'infer_types_verbose',
        'autotestdict.cdef': 'autotestdict_cdef',
        'autotestdict.all': 'autotestdict_all',
        'warn.undeclared': 'warn_undeclared',
        'warn.unreachable': 'warn_unreachable',
        'warn.maybe_uninitialized': 'warn_maybe_uninitialized',
        'warn.unused': 'warn_unused',
        'warn.unused_arg': 'warn_unused_arg',
        'warn.unused_result': 'warn_unused_result',
        'warn.multiple_declarators': 'warn_multiple_declarators',
        'warn.deprecated.DEF': 'warn_deprecated_DEF',
        'warn.deprecated.IF': 'warn_deprecated_IF',
        'optimize.inline_defnode_calls': 'optimize_inline_defnode_calls',
        'optimize.unpack_method_calls': 'optimize_unpack_method_calls',
        'optimize.unpack_method_calls_in_pyinit': 'optimize_unpack_method_calls_in_pyinit',
        'optimize.use_switch': 'optimize_use_switch',
        'control_flow.dot_output': 'control_flow_dot_output',
        'control_flow.dot_annotate_defs': 'control_flow_dot_annotate_defs',
        'dataclasses.dataclass': 'dataclasses_dataclass',
    }, repr=False)
    
    def __post_init__(self):
        """Initialize the reverse mapping for attribute lookup."""
        # Create a reverse mapping for faster lookup
        self._reverse_mapping = {v: k for k, v in self._attr_mapping.items()}
    
    def __getitem__(self, key: str) -> Any:
        """Enable dictionary-like access to directive attributes."""
        # First check if we need to map from dotted name to attribute name
        attr_name = self._attr_mapping.get(key, key)
        
        # Handle special cases for attributes with dots in name
        if hasattr(self, attr_name):
            return getattr(self, attr_name)
        
        # If we have a dot in the key but no mapping, try to split and process
        if '.' in key and key not in self._attr_mapping:
            prefix, suffix = key.split('.', 1)
            if hasattr(self, prefix) and isinstance(getattr(self, prefix), dict):
                return getattr(self, prefix).get(suffix)
                
        # Fall back to the original dictionary (for backward compatibility)
        data_dict = self.as_dict()
        return data_dict.get(key)
    
    def __setitem__(self, key: str, value: Any) -> None:
        """Enable dictionary-like setting of directive attributes."""
        # First check if we need to map from dotted name to attribute name
        attr_name = self._attr_mapping.get(key, key)
        
        # If it's a direct attribute, set it
        if hasattr(self, attr_name):
            setattr(self, attr_name, value)
            return
            
        # Handle dotted names that aren't in our mapping
        if '.' in key and key not in self._attr_mapping:
            prefix, suffix = key.split('.', 1)
            if hasattr(self, prefix) and isinstance(getattr(self, prefix), dict):
                getattr(self, prefix)[suffix] = value
                return
                
        # Fall back to raising an AttributeError for unknown keys
        raise AttributeError(f"No directive named '{key}' in Directives class")
    
    def as_dict(self) -> DirectivesDict:
        """Convert to a DirectivesDict representation."""
        base_dict = asdict(self)
        
        # Remove the internal mappings
        base_dict.pop('_attr_mapping', None)
        base_dict.pop('_reverse_mapping', None)
        
        # Add all dotted-name versions
        for dotted_name, attr_name in self._attr_mapping.items():
            if attr_name in base_dict:
                base_dict[dotted_name] = base_dict[attr_name]
        
        return base_dict  # type: ignore[return-value]

    @classmethod
    def from_dict(cls, directive_dict: 'DirectivesDict') -> 'Directives':
        """Create a Directives instance from a dictionary."""
        # Start with default values
        directives = cls()
        
        # Update with provided values, handling both direct and mapped attributes
        for key, value in directive_dict.items():
            # Handle special field mapping for dotted names
            attr_name = directives._attr_mapping.get(key, key)
            
            if hasattr(directives, attr_name):
                setattr(directives, attr_name, value)
            # Handling for other special cases could be added here
                
        return directives

# Replace _directive_defaults with an instance of the Directives dataclass
_directive_defaults: DirectivesDict = Directives().as_dict()

def get_directive_defaults() -> DirectivesDict:
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
    return _directive_defaults.copy()

def copy_inherited_directives(outer_directives: DirectivesDict,
                              **new_directives: Any) -> DirectivesDict:
    # A few directives are not copied downwards and this function removes them.
    # For example, test_assert_path_exists and test_fail_if_path_exists should not be inherited
    #  otherwise they can produce very misleading test failures
    new_directives_out: DirectivesDict = dict(outer_directives)  # type: ignore[assignment]
    for name in ('test_assert_path_exists', 'test_fail_if_path_exists', 'test_assert_c_code_has', 'test_fail_if_c_code_has',
                 'critical_section'):
        new_directives_out.pop(name, None)
    new_directives_out.update(**new_directives)
    return new_directives_out


def copy_for_internal(outer_directives: DirectivesDict) -> DirectivesDict:
    # Reset some directives that users should not control for internal code.
    return copy_inherited_directives(
        outer_directives,
        binding=False,
        profile=False,
        linetrace=False,
    )

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

    return encoding

# Override types possibilities above, if needed
directive_types: DirectiveTypesMap = {
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
    'subinterpreters_compatible': one_of('no', 'shared_gil', 'own_gil'),
}

for key, val in _directive_defaults.items():
    if key not in directive_types:
        directive_types[key] = type(val)

# For 'with statement' strings in tuples
WithStatement = Literal['with statement']

# Create a mapping for scopes with dots in their names
_scope_name_mapping = {
    'autotestdict.all': 'autotestdict_all',
    'autotestdict.cdef': 'autotestdict_cdef',
    'dataclasses.dataclass': 'dataclasses_dataclass',
    'control_flow.dot_output': 'control_flow_dot_output',
    'control_flow.dot_annotate_defs': 'control_flow_dot_annotate_defs',
}

# Define directive scopes
directive_scopes: Dict[str, Union[Tuple[str, ...], WithStatement, Tuple[str, WithStatement], Tuple[str, str, WithStatement]]] = {  # defaults to available everywhere
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
    'c_compile_guard': ('function',),  # actually C function but this is enforced later
    'control_flow.dot_output': ('module',),
    'control_flow.dot_annotate_defs': ('module',),
    'freethreading_compatible': ('module',),
    'subinterpreters_compatible': ('module',),
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


def parse_directive_list(s: str, relaxed_bool: bool = False,
                          ignore_unknown: bool = False,
                          current_settings: Optional[DirectivesDict] = None) -> DirectivesDict:
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
    # Start with a properly typed result dictionary
    result: DirectivesDict = {} if current_settings is None else current_settings
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


# ------------------------------------------------------------------------
# GlobalDirectives are constructed to manage directive defaults, types and scopes
# ------------------------------------------------------------------------

@dataclass
class GlobalDirectives:
    """
    Global directives and defaults that can be used throughout the compilation process.
    These values can be accessed directly but also correspond to directives.
    """
    #: Whether or not to include docstring in the Python extension. If False, the binary size
    #: will be smaller, but the ``__doc__`` attribute of any class or function will be an
    #: empty string.
    docstrings: bool = True

    #: Embed the source code position in the docstrings of functions and classes.
    embed_pos_in_docstring: bool = False

    # undocumented
    pre_import: Optional[str] = None

    #: Decref global variables in each module on exit for garbage collection.
    #: 0: None, 1+: interned objects, 2+: cdef globals, 3+: types objects
    #: Mostly for reducing noise in Valgrind as it typically executes at process exit
    #: (when all memory will be reclaimed anyways).
    #: Note that directly or indirectly executed cleanup code that makes use of global
    #: variables or types may no longer be safe when enabling the respective level since
    #: there is no guaranteed order in which the (reference counted) objects will
    #: be cleaned up.  The order can change due to live references and reference cycles.
    generate_cleanup_code: Union[bool, int] = False

    #: Should tp_clear() set object fields to None instead of clearing them to NULL?
    clear_to_none: bool = True

    #: Generate an annotated HTML version of the input source files for debugging and optimisation purposes.
    #: This has the same effect as the ``annotate`` argument in :func:`cythonize`.
    annotate: bool = False

    # When annotating source files in HTML, include coverage information from
    # this file.
    annotate_coverage_xml: Optional[str] = None

    #: This will abort the compilation on the first error occurred rather than trying
    #: to keep going and printing further error messages.
    fast_fail: bool = False

    #: Turn all warnings into errors.
    warning_errors: bool = False

    #: Make unknown names an error.  Python raises a NameError when
    #: encountering unknown names at runtime, whereas this option makes
    #: them a compile time error.  If you want full Python compatibility,
    #: you should disable this option and also 'cache_builtins'.
    error_on_unknown_names: bool = True

    #: Make uninitialized local variable reference a compile time error.
    #: Python raises UnboundLocalError at runtime, whereas this option makes
    #: them a compile time error. Note that this option affects only variables
    #: of "python object" type.
    error_on_uninitialized: bool = True

    #: This will convert statements of the form ``for i in range(...)``
    #: to ``for i from ...`` when ``i`` is a C integer type, and the direction
    #: (i.e. sign of step) can be determined.
    #: WARNING: This may change the semantics if the range causes assignment to
    #: i to overflow. Specifically, if this option is set, an error will be
    #: raised before the loop is entered, whereas without this option the loop
    #: will execute until an overflowing value is encountered.
    convert_range: bool = True

    #: Perform lookups on builtin names only once, at module initialisation
    #: time.  This will prevent the module from getting imported if a
    #: builtin name that it uses cannot be found during initialisation.
    #: Default is True.
    #: Note that some legacy builtins are automatically remapped
    #: from their Python 2 names to their Python 3 names by Cython
    #: when building in Python 3.x,
    #: so that they do not get in the way even if this option is enabled.
    cache_builtins: bool = True

    #: Generate branch prediction hints to speed up error handling etc.
    gcc_branch_hints: bool = True

    #: Enable this to allow one to write ``your_module.foo = ...`` to overwrite the
    #: definition if the cpdef function foo, at the cost of an extra dictionary
    #: lookup on every call.
    #: If this is false it generates only the Python wrapper and no override check.
    lookup_module_cpdef: bool = False

    #: Whether or not to embed the Python interpreter, for use in making a
    #: standalone executable or calling from external libraries.
    #: This will provide a C function which initialises the interpreter and
    #: executes the body of this module.
    #: See `this demo <https://github.com/cython/cython/tree/master/Demos/embed>`_
    #: for a concrete example.
    #: If true, the initialisation function is the C main() function, but
    #: this option can also be set to a non-empty string to provide a function name explicitly.
    #: Default is False.
    embed: Optional[Union[bool, str]] = None

    #: Allows cimporting from a pyx file without a pxd file.
    cimport_from_pyx: bool = False

    #: Maximum number of dimensions for buffers -- set lower than number of
    #: dimensions in numpy, as
    #: slices are passed by value and involve a lot of copying.
    buffer_max_dims: int = 8

    #: Number of function closure instances to keep in a freelist (0: no freelists)
    closure_freelist_size: int = 8

    #: Allow old style globals lookup (for backwards compatibility)
    old_style_globals: bool = False

    #: Export C API reexport cincludes
    capi_reexport_cincludes: bool = False

    def __post_init__(self) -> None:
        """Initialize internal directive mappings and default values."""
        # Use the global Directives dataclass for defaults
        self._directives = Directives()
        
        # The directive_defaults should be a dict that works like the old one
        self._directive_defaults = self._directives.as_dict()

        # Define helper for deferred analysis
        self._defer_analysis = DEFER_ANALYSIS_OF_ARGUMENTS
        
        # Define directive types
        self.directive_types: DirectiveTypesMap = {
            'language_level': str,  # values can be None/2/3/'3str', where None == 2+warning
            'auto_pickle': bool,
            'locals': dict,
            'final': bool,  # final cdef classes and methods
            'collection_type': self._one_of('sequence'),
            'nogil': self._defer_analysis,
            'gil': self._defer_analysis,
            'critical_section': self._defer_analysis,
            'with_gil': None,
            'internal': bool,  # cdef class visibility in the module dict
            'infer_types': bool,  # values can be True/None/False
            'binding': bool,
            'cfunc': None,  # decorators do not take directive value
            'ccall': None,
            'ufunc': None,
            'cpow': bool,
            'inline': None,
            'staticmethod': None,
            'cclass': None,
            'no_gc_clear': bool,
            'no_gc': bool,
            'returns': type,
            'exceptval': type,  # actually (type, check=True/False), but has its own parser
            'set_initial_path': str,
            'freelist': int,
            'c_string_type': self._one_of('bytes', 'bytearray', 'str', 'unicode', map={'unicode': 'str'}),
            'c_string_encoding': self._normalise_encoding_name,
            'trashcan': bool,
            'total_ordering': None,
            'dataclasses.dataclass': self._defer_analysis,
            'dataclasses.field': self._defer_analysis,
            'embedsignature.format': self._one_of('c', 'clinic', 'python'),
            'subinterpreters_compatible': self._one_of('no', 'shared_gil', 'own_gil'),
        }

        # Add missing types to directive_types
        for key, val in self._directive_defaults.items():
            if key not in self.directive_types:
                self.directive_types[key] = type(val)

        # Define extra warning directives
        self.extra_warnings = {
            'warn.maybe_uninitialized': True,
            'warn.unreachable': True,
            'warn.unused': True,
        }

        # Set up directive scopes, using the same as global directive_scopes
        self.directive_scopes = directive_scopes

        # A list of directives that (when used as a decorator) are only applied to
        # the object they decorate and not to its children.
        self.immediate_decorator_directives = immediate_decorator_directives
        
    def get_directive_defaults(self) -> DirectivesDict:
        """Return the default directive values."""
        return self._directive_defaults.copy()
        
    def parse_directive_value(self, name: str, value: Any, relaxed_bool: bool = False) -> Any:
        """
        Parse a directive value based on its expected type.
        
        Args:
            name: The directive name
            value: The value to parse
            relaxed_bool: Whether to allow relaxed boolean parsing
            
        Returns:
            The parsed value or None if the directive doesn't exist
        """
        type_info = self.directive_types.get(name)
        if not type_info:
            return None
        orig_value = value
        if type_info is bool:
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
        elif type_info is int:
            try:
                return int(value)
            except ValueError:
                raise ValueError("%s directive must be set to an integer, got '%s'" % (
                    name, orig_value))
        elif type_info is str:
            return str(value)
        elif callable(type_info):
            return type_info(name, value)
        else:
            assert False

    def parse_directive_list(self, s: str, relaxed_bool: bool = False, 
                           ignore_unknown: bool = False,
                           current_settings: Optional[DirectivesDict] = None) -> DirectivesDict:
        """
        Parse a comma-separated list of pragma options.
        
        Args:
            s: The directive string to parse
            relaxed_bool: Whether to allow relaxed boolean parsing
            ignore_unknown: Whether to ignore unknown directives
            current_settings: Existing settings to update
            
        Returns:
            Dictionary of parsed directives
        """
        # Start with a properly typed result dictionary
        result: DirectivesDict = {} if current_settings is None else current_settings
        for item in s.split(','):
            item = item.strip()
            if not item:
                continue
            if '=' not in item:
                raise ValueError('Expected "=" in option "%s"' % item)
            name, value = [s.strip() for s in item.strip().split('=', 1)]
            if name not in self._directive_defaults:
                found = False
                if name.endswith('.all'):
                    prefix = name[:-3]
                    for directive in self._directive_defaults:
                        if directive.startswith(prefix):
                            found = True
                            parsed_value = self.parse_directive_value(directive, value, relaxed_bool=relaxed_bool)
                            result[directive] = parsed_value
                if not found and not ignore_unknown:
                    raise ValueError('Unknown option: "%s"' % name)
            elif self.directive_types.get(name) is list:
                if name in result:
                    result[name].append(value)
                else:
                    result[name] = [value]
            else:
                parsed_value = self.parse_directive_value(name, value, relaxed_bool=relaxed_bool)
                result[name] = parsed_value
        return result

    def parse_variable_value(self, value: str) -> Any:
        """
        Parse a variable value to its appropriate Python type.
        
        Args:
            value: The string value to parse
            
        Returns:
            Parsed value as appropriate type
        """
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
                parsed_value = float(value)
                return parsed_value  # Return the float value, not a string
            except Exception:
                # Not a float
                pass
            return value  # Return the original string value

    def parse_compile_time_env(self, s: str, current_settings: Optional[dict[str, object]] = None) -> dict[str, object]:
        """
        Parse a comma-separated list of pragma options for compile-time environment variables.
        
        Args:
            s: The string to parse
            current_settings: Existing settings to update
            
        Returns:
            Dictionary of parsed compile-time environment variables
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
            result[name] = self.parse_variable_value(value)
        return result

    def _one_of(self, *args: str, map: Optional[Dict[str, str]] = None) -> Callable[[str, Any], Any]:
        """
        Create a validator function for directive values that must be one of a set of values.
        
        Args:
            *args: Allowed values
            map: Optional mapping for value conversion
            
        Returns:
            Validator function
        """
        def validate(name: str, value: Any) -> Any:
            if map is not None:
                value = map.get(value, value)
            if value not in args:
                raise ValueError("%s directive must be one of %s, got '%s'" % (
                    name, args, value))
            return value
        return validate

    def _normalise_encoding_name(self, option_name: str, encoding: str) -> str:
        """
        Normalize encoding names to a standard form.
        
        Args:
            option_name: Name of the option (unused)
            encoding: Encoding name to normalize
            
        Returns:
            Normalized encoding name
        """
        if not encoding:
            return ''
            
        _normalise_common_encoding_name = {
            'utf8': 'utf8',
            'utf-8': 'utf8',
            'default': 'utf8',
            'ascii': 'ascii',
            'us-ascii': 'ascii',
        }.get
        
        encoding_name = _normalise_common_encoding_name(encoding.lower())
        if encoding_name is not None:
            return encoding_name

        return encoding

    def copy_inherited_directives(self, outer_directives: DirectivesDict,
                                  **new_directives: object) -> DirectivesDict:
        """
        Copy directives with inheritance rules.
        
        A few directives are not copied downwards and this function removes them.
        For example, test_assert_path_exists and test_fail_if_path_exists should not be inherited
        otherwise they can produce very misleading test failures.
        
        Args:
            outer_directives: Parent directives dictionary
            **new_directives: New directives to add/override
            
        Returns:
            Updated directives dictionary
        """
        new_directives_out: DirectivesDict = dict(outer_directives)  # type: ignore[assignment]
        for name in ('test_assert_path_exists', 'test_fail_if_path_exists', 'test_assert_c_code_has', 'test_fail_if_c_code_has',
                    'critical_section'):
            new_directives_out.pop(name, None)
        new_directives_out.update(new_directives)
        return new_directives_out

    def copy_for_internal(self, outer_directives: DirectivesDict) -> DirectivesDict:
        """
        Reset some directives that users should not control for internal code.
        
        Args:
            outer_directives: Parent directives dictionary
            
        Returns:
            Updated directives dictionary for internal use
        """
        return self.copy_inherited_directives(
            outer_directives,
            binding=False,
            profile=False,
            linetrace=False,
        )

    def to_dict(self) -> dict[str, object]:
        """
        Convert GlobalDirectives to a dictionary representation.
        
        Returns:
            Dictionary containing important configuration values.
        """
        result = {
            'directive_defaults': self._directive_defaults.copy(),
            'directive_scopes': self.directive_scopes,
            'directive_types': {k: str(v) for k, v in self.directive_types.items()},
            'immediate_decorator_directives': list(self.immediate_decorator_directives),
            'extra_warnings': self.extra_warnings.copy()
        }
        return result

    def get_directive_scopes(self) -> DirectiveScopesDict:
        """
        Return the directive scopes dictionary properly typed.
        
        Returns:
            A DirectiveScopesDict mapping directives to allowed scopes
        """
        typed_scopes = {}
        
        for directive_name, scope_tuple in directive_scopes.items():
            # Handle directive names with dots for TypedDict
            if '.' in directive_name and directive_name in _scope_name_mapping:
                typed_name = _scope_name_mapping[directive_name]
            else:
                typed_name = directive_name
            
            typed_scopes[typed_name] = scope_tuple
        
        return typed_scopes  # type: ignore[return-value]

# ------------------------------------------------------------------------
# CompilationOptions are constructed from user input and are the `option`
#  object passed throughout the compilation pipeline.
# ------------------------------------------------------------------------

# Define a TypedDict version of CompilationOptions for type checking and serialization
class CompilationOptionsDict(TypedDict, total=False):
    """TypedDict representation of CompilationOptions for type checking and serialization."""
    include_path: List[str]
    output_file: Optional[str]
    show_version: bool
    use_listing_file: bool
    errors_to_stderr: bool
    cplus: bool
    depfile: Optional[str]
    make_depfile: bool
    annotate: Optional[bool]
    annotate_coverage_xml: Optional[str]
    generate_pxi: bool
    capi_reexport_cincludes: bool
    working_path: str
    timestamps: Optional[Any]
    verbose: int
    quiet: bool
    compiler_directives: DirectivesDict
    embedded_metadata: dict[str, object]
    evaluate_tree_assertions: bool
    emit_linenums: bool
    relative_path_in_code_position_comments: bool
    embedding_file_name: Optional[str]
    c_line_in_traceback: bool
    language_level: Optional[Any]
    formal_grammar: bool
    gdb_debug: bool
    compile_time_env: dict[str, object]
    module_name: Optional[str]
    common_utility_include_dir: Optional[str]
    output_dir: Optional[str]
    build_dir: Optional[str]
    cache: Optional[Any]
    create_extension: Optional[Any]
    np_pythran: bool
    legacy_implicit_noexcept: bool
    shared_utility_qualified_name: Optional[str]
    docstrings: bool
    embed_pos_in_docstring: bool
    pre_import: Optional[Any]
    generate_cleanup_code: Union[bool, int]
    clear_to_none: bool
    fast_fail: bool
    warning_errors: bool
    error_on_unknown_names: bool
    error_on_uninitialized: bool
    convert_range: bool
    cache_builtins: bool
    gcc_branch_hints: bool
    lookup_module_cpdef: bool
    embed: Optional[Union[bool, str]]
    cimport_from_pyx: bool
    buffer_max_dims: int
    closure_freelist_size: int

@dataclass
class CompilationOptions:
    """
    Options for Cython compilation, used throughout the compilation pipeline.
    See default_options at the end of this module for a list of all possible
    options and CmdLine.usage and CmdLine.parse_command_line() for their meaning.
    """
    # Fields defined based on old CompilationOptionKwargs and default_options
    include_path: List[str] = field(default_factory=list)
    shared_c_file_path: Optional[str] = None
    output_file: Optional[str] = None
    show_version: bool = False
    use_listing_file: bool = False
    errors_to_stderr: bool = True
    cplus: bool = False
    depfile: Optional[str] = None
    make_depfile: bool = False
    annotate: Optional[bool] = None
    annotate_coverage_xml: Optional[str] = None
    generate_pxi: bool = False
    capi_reexport_cincludes: bool = False
    working_path: str = ""
    timestamps: Optional[Any] = None
    verbose: int = 0
    quiet: bool = False
    compiler_directives: DirectivesDict = field(default_factory=DirectivesDict)
    _directives: Optional[Directives] = field(default=None, repr=False)
    embedded_metadata: dict[str, object] = field(default_factory=dict)
    embedding_file_name: Optional[str] = None
    embedding_file_timestamp: Optional[int] = None
    evaluate_tree_assertions: bool = False
    emit_linenums: bool = False
    relative_path_in_code_position_comments: bool = True
    c_line_in_traceback: bool = True
    language_level: Optional[Any] = None
    formal_grammar: bool = False
    gdb_debug: bool = False
    compile_time_env: dict[str, object] = field(default_factory=dict)
    module_name: Optional[str] = None
    common_utility_include_dir: Optional[str] = None
    output_dir: Optional[str] = None
    build_dir: Optional[str] = None
    cache: Optional[Any] = None
    create_extension: Optional[Any] = None
    np_pythran: bool = False
    legacy_implicit_noexcept: bool = False
    shared_utility_qualified_name: Optional[str] = None
    old_style_globals: bool = False
    
    # Options previously defined as globals
    docstrings: bool = True
    embed_pos_in_docstring: bool = False
    pre_import: Optional[Any] = None
    generate_cleanup_code: Union[bool, int] = False
    clear_to_none: bool = True
    fast_fail: bool = False
    warning_errors: bool = False
    error_on_unknown_names: bool = True
    error_on_uninitialized: bool = True
    convert_range: bool = True
    cache_builtins: bool = True
    gcc_branch_hints: bool = True
    lookup_module_cpdef: bool = False
    embed: Optional[Union[bool, str]] = None
    cimport_from_pyx: bool = False
    buffer_max_dims: int = 8
    closure_freelist_size: int = 8

    def __post_init__(self) -> None:
        """Validate options and set defaults for compiler directives."""
        # Create a GlobalDirectives instance to validate directives
        global_directives = GlobalDirectives()
        
        if not isinstance(self.compiler_directives, dict):
            # This case should ideally not happen with the default_factory
            self.compiler_directives = global_directives.get_directive_defaults()

        # Check for unknown directives
        directive_defaults = global_directives.get_directive_defaults()
        unknown_directives = set(self.compiler_directives.keys()) - set(directive_defaults.keys())
        if unknown_directives:
            message = "got unknown compiler directive%s: %s" % (
                's' if len(unknown_directives) > 1 else '',
                ', '.join(map(str, unknown_directives)))
            raise ValueError(message)

        # Handle np_pythran forcing cplus
        if self.compiler_directives.get('np_pythran', False) and not self.cplus:
            import warnings
            warnings.warn("C++ mode forced when in Pythran mode!")
            self.cplus = True
            
        # Initialize the Directives dataclass from compiler_directives dict
        self._directives = Directives.from_dict(self.compiler_directives)

    def configure_language_defaults(self, source_extension: str) -> None:
        """
        Configure language level defaults based on source extension and directives.
        
        Args:
            source_extension: The file extension of the source file
        """
        # Direct access to dataclass fields
        directives = self.compiler_directives

        lang_level = directives.get('language_level')
        if lang_level is None:
            # Auto-detect language level.
            import sys
            lang_level = '3' if sys.version_info[0] >= 3 else '2'
            # Update the directive itself if it was None
            directives['language_level'] = lang_level
            
            # Also update the directives dataclass
            if self._directives is not None:
                self._directives.language_level = lang_level

        # Update the main language_level attribute based on the directive value
        if lang_level == '2':
            self.language_level = 2
        elif str(lang_level).startswith('3'):
            self.language_level = 3
        else:
            # This case should ideally be caught by directive validation earlier
            # but kept here for robustness.
            raise ValueError("Invalid language level: %r" % lang_level)

        # Python files always imply binding=True unless explicitly set to False
        if source_extension == 'py' and directives.get('binding') is not False:
            self.compiler_directives['binding'] = True
            if self._directives is not None:
                self._directives.binding = True

    @property
    def directives(self) -> Directives:
        """Get the directives dataclass."""
        if self._directives is None:
            self._directives = Directives.from_dict(self.compiler_directives)
        return self._directives
    
    def update_directives(self, **directives: object) -> None:
        """
        Update directives with new values.
        
        Args:
            **directives: New directive values to update
        """
        # Create a temporary dict to avoid type issues with TypedDict updates
        temp_dict = dict(self.compiler_directives)
        temp_dict.update(directives)
        self.compiler_directives = temp_dict  # type: ignore[assignment]
        
        # Also update the directives dataclass
        if self._directives is not None:
            for key, value in directives.items():
                if hasattr(self._directives, key):
                    setattr(self._directives, key, value)

    def as_dict(self) -> CompilationOptionsDict:
        """
        Convert to a dictionary representation compatible with CompilationOptionsDict.
        
        Returns:
            A dictionary representation of the compilation options
        """
        return asdict(self)  # type: ignore[return-value]

    def get_fingerprint(self) -> str:
        """
        Generate a fingerprint string containing all options relevant for cache invalidation.
        
        Returns:
            A hexadecimal string fingerprint
        """
        import hashlib
        # compiler directives can contain python objects that are unhashable
        # and lists that are unhashable. Sort dictionary items for consistency.
        # Access attributes directly
        directive_items = sorted(self.compiler_directives.items())
        env_items = sorted(self.compile_time_env.items())
        parts = [
            str(self.language_level),
            str([(k, v) for k, v in directive_items if not callable(v)]),
            str(env_items),
        ]
        fingerprint = hashlib.md5(str(parts).encode('utf-8')).hexdigest()
        return fingerprint

    def get_embedded_main_c_function(self) -> Optional[str]:
        """
        Get the name of the embedded main C function if embedding is enabled.
        
        Returns:
            The function name or None if embedding is not enabled
        """
        if self.embed is True:
            return "main"
        elif isinstance(self.embed, str):
            return self.embed
        else:
            return None


def get_default_options() -> CompilationOptions:
    """Return a new instance of CompilationOptions with default values."""
    # Create a GlobalDirectives instance to provide default directives
    global_directives = GlobalDirectives()
    
    # Create a CompilationOptions instance with default values
    options = CompilationOptions(
        compiler_directives=global_directives.get_directive_defaults(),
        # Copy other default values from GlobalDirectives
        docstrings=global_directives.docstrings,
        embed_pos_in_docstring=global_directives.embed_pos_in_docstring,
        pre_import=global_directives.pre_import,
        generate_cleanup_code=global_directives.generate_cleanup_code,
        clear_to_none=global_directives.clear_to_none,
        annotate=global_directives.annotate,
        annotate_coverage_xml=global_directives.annotate_coverage_xml,
        fast_fail=global_directives.fast_fail,
        warning_errors=global_directives.warning_errors,
        error_on_unknown_names=global_directives.error_on_unknown_names,
        error_on_uninitialized=global_directives.error_on_uninitialized,
        convert_range=global_directives.convert_range,
        cache_builtins=global_directives.cache_builtins,
        gcc_branch_hints=global_directives.gcc_branch_hints,
        lookup_module_cpdef=global_directives.lookup_module_cpdef,
        embed=global_directives.embed,
        cimport_from_pyx=global_directives.cimport_from_pyx,
        buffer_max_dims=global_directives.buffer_max_dims,
        closure_freelist_size=global_directives.closure_freelist_size,
        capi_reexport_cincludes=global_directives.capi_reexport_cincludes,
        make_depfile=False,
        old_style_globals=global_directives.old_style_globals,
    )
    return options

# Create default options dictionary
default_options: CompilationOptionsDict = asdict(get_default_options())  # type: ignore[assignment]

# Create global instances for backward compatibility
GLOBAL_DIRECTIVES = GlobalDirectives()
directive_defaults = GLOBAL_DIRECTIVES.get_directive_defaults()
directive_types = GLOBAL_DIRECTIVES.directive_types
directive_scopes = GLOBAL_DIRECTIVES.directive_scopes
immediate_decorator_directives = GLOBAL_DIRECTIVES.immediate_decorator_directives

# For backward compatibility, expose functions from GlobalDirectives
parse_directive_value = GLOBAL_DIRECTIVES.parse_directive_value
parse_compile_time_env = GLOBAL_DIRECTIVES.parse_compile_time_env
copy_inherited_directives = GLOBAL_DIRECTIVES.copy_inherited_directives
copy_for_internal = GLOBAL_DIRECTIVES.copy_for_internal

# Transform the directive_scopes into a DirectiveScopesDict
def get_directive_scopes() -> DirectiveScopesDict:
    """Return the directive scopes as a properly typed DirectiveScopesDict."""
    typed_scopes = {}
    
    for directive_name, scope_tuple in directive_scopes.items():
        # Handle directive names with dots for TypedDict
        if '.' in directive_name and directive_name in _scope_name_mapping:
            typed_name = _scope_name_mapping[directive_name]
        else:
            typed_name = directive_name
            
        typed_scopes[typed_name] = scope_tuple
        
    return typed_scopes  # type: ignore[return-value]

