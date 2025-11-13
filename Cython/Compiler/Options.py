#
#  Cython - Compilation-wide options and pragma declarations
#
import ast
import copy
from collections.abc import Mapping
from dataclasses import dataclass, field
from pathlib import Path
from typing import (
    Any,
    Dict,
    List,
    Optional,
    Self,
    Union,
    Callable,
    Type,
    Tuple,
    Literal,
    TypedDict,
    cast,
    TYPE_CHECKING,
)

from Cython.Abstract import MatchAST, func_def

if TYPE_CHECKING:
    from typing import Unpack
else:
    Unpack = tuple

embedding_file_name: Optional[str]


class DataDict(dict):
    def copy(self) -> Self:
        return type(self)(**self)

    def __deepcopy__(self, memo):
        cls = type(self)
        result = cls.__new__(cls)
        memo[id(self)] = result
        dict.__init__(result)
        for key, value in self.items():
            result[key] = copy.deepcopy(value, memo)
        return result

    def __getattr__(self, name: str) -> Any:
        if dict.__contains__(self, name):
            return dict.__getitem__(self, name)
        raise AttributeError(f"{self.__class__.__name__} has no attribute {name}")

    def __contains__(self, key: object) -> bool:
        if not isinstance(key, str):
            return False
        cur: Any = self
        while "." in key:
            head, key = key.split(".", 1)
            if not dict.__contains__(cur, head):
                return False
            cur = dict.__getitem__(cur, head)
            if not isinstance(cur, dict):
                return False
        return dict.__contains__(cur, key) or key in getattr(type(self), "__dataclass_fields__", [])

    def __setattr__(self, name: str, value: Any) -> None:
        if name in getattr(type(self), "__dataclass_fields__", []):
            object.__setattr__(self, name, value)
            dict.__setitem__(self, name, value)
        else:
            object.__setattr__(self, name, value)

    def __getitem__(self, key: str) -> Any:
        cur: Any = self
        while "." in key:
            head, key = key.split(".", 1)
            if not dict.__contains__(cur, head):
                raise KeyError(head)
            next_val = dict.__getitem__(cur, head)
            if not isinstance(next_val, dict):
                raise KeyError(key)
            cur = next_val
        if dict.__contains__(cur, key):
            val = dict.__getitem__(cur, key)
            # If retrieving a group without a subkey, expose its 'enabled' if present
            if isinstance(val, dict) and "enabled" in val:
                return val["enabled"]
            return val
        raise KeyError(key)

    def __setitem__(self, key: str, value: Any) -> None:
        # Support dotted assignment into nested mappings
        if "." in key:
            head, tail = key.split(".", 1)
            # Use raw dict containment to avoid DataDict.__contains__ semantics here
            if dict.__contains__(self, head) and isinstance(dict.__getitem__(self, head), dict):
                dict.__getitem__(self, head)[tail] = value
                return
        # If setting a group value and it has an 'enabled' toggle, store there
        if dict.__contains__(self, key):
            cur_val = dict.__getitem__(self, key)
            if isinstance(cur_val, dict) and "enabled" in cur_val and not isinstance(value, dict):
                cur_val["enabled"] = value
                if key in getattr(type(self), "__dataclass_fields__", []):
                    object.__setattr__(self, key, cur_val)
                return
        # Prefer dataclass field assignment for local fields
        if key in getattr(type(self), "__dataclass_fields__", []):
            object.__setattr__(self, key, value)
            dict.__setitem__(self, key, value)
            return
        dict.__setitem__(self, key, value)

    def __delattr__(self, name: str) -> None:
        if dict.__contains__(self, name):
            dict.__delitem__(self, name)
        object.__delattr__(self, name)

    def __delitem__(self, key: str) -> None:
        if dict.__contains__(self, key):
            dict.__delitem__(self, key)
        else:
            object.__delattr__(self, key)


DirectiveScopeType = Literal["module", "function", "cclass", "class", "with statement"]


@dataclass
class AutotestdictDirectivesScopes(DataDict):
    all: DirectiveScopeType = "module"
    cdef: DirectiveScopeType = "module"


@dataclass
class DataclassDirectivesScopes(DataDict):
    dataclass: DirectiveScopeType = "class"
    field: DirectiveScopeType = "class"


@dataclass
class AutotestdictDirectives(DataDict):
    all: bool = True
    cdef: bool = True


@dataclass
class EmbedSignatureDirectives(DataDict):
    enabled: bool = False
    format: str = "c"


@dataclass
class OverflowcheckDirectives(DataDict):
    enabled: bool = False
    fold: bool = True


@dataclass
class InferTypesDirectives(DataDict):
    enabled: bool = True
    verbose: bool = False


@dataclass
class LanguageLevelDirectives(DataDict):
    level: str = "3"


@dataclass
class FastGetattrDirectives(DataDict):
    fast: bool = True


@dataclass
class Py2ImportDirectives(DataDict):
    py2: bool = False


@dataclass
class WarnDirectives(DataDict):
    all: bool = False
    undeclared: bool = False
    unreachable: bool = False
    maybe_uninitialized: bool = False
    unused: bool = False
    unused_arg: bool = False
    unused_result: bool = False
    multiple_declarators: bool = False
    deprecated_DEF: bool = False
    deprecated_IF: bool = False


@dataclass
class OptimizeDirectives(DataDict):
    inline_defnode_calls: bool = True
    unpack_method_calls: bool = True
    unpack_method_calls_in_pyinit: bool = True
    use_switch: bool = True


class OptimizeDirectivesDict(TypedDict, total=False):
    inline_defnode_calls: bool
    unpack_method_calls: bool
    unpack_method_calls_in_pyinit: bool
    use_switch: bool


@dataclass
class ControlFlowDirectivesScopes(DataDict):
    output: DirectiveScopeType = "module"
    annotate_defs: DirectiveScopeType = "module"
    dot_output: DirectiveScopeType = "module"
    dot_annotate_defs: DirectiveScopeType = "module"


@dataclass
class ControlFlowDirectives(DataDict):
    output: str = ""
    annotate_defs: bool = False
    dot_output: str = ""
    dot_annotate_defs: bool = False


@dataclass
class TestDirectives(DataDict):
    assert_path_exists: List[str]
    fail_if_path_exists: List[str]
    assert_c_code_has: List[str]
    fail_if_c_code_has: List[str]


@dataclass
class DirectivesDict(TypedDict, total=False):
    """TypedDict representing the default values for compiler directives."""

    binding: bool
    boundscheck: bool
    nonecheck: bool
    initializedcheck: bool
    freethreading_compatible: bool
    subinterpreters_compatible: str
    embedsignature: EmbedSignatureDirectives
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
    infer_types: InferTypesDirectives
    autotestdict: AutotestdictDirectives
    language_level: LanguageLevelDirectives
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
    set_initial_path: str | None
    warn: WarnDirectives
    show_performance_hints: bool
    optimize: OptimizeDirectivesDict
    remove_unreachable: bool
    control_flow: ControlFlowDirectives
    test_assert_path_exists: List[str]
    test_fail_if_path_exists: List[str]
    test_assert_c_code_has: List[str]
    test_fail_if_c_code_has: List[str]
    formal_grammar: bool


class DirectiveDefaultsDict(DirectivesDict, total=True):
    """TypedDict for a complete set of directive defaults.

    This represents the mapping returned by get_directive_defaults(), which
    always contains all directive keys with their default values.
    """


class DirectiveScopesDict(TypedDict, total=False):
    """TypedDict representing directive scopes mapping directives to their allowed scopes."""

    auto_pickle: tuple[DirectiveScopeType, ...]
    final: tuple[DirectiveScopeType, ...]
    ccomplex: tuple[DirectiveScopeType, ...]
    collection_type: tuple[DirectiveScopeType, ...]
    nogil: tuple[DirectiveScopeType, ...]
    gil: tuple[DirectiveScopeType, ...]
    with_gil: tuple[DirectiveScopeType, ...]
    critical_section: tuple[DirectiveScopeType, ...]
    inline: tuple[DirectiveScopeType, ...]
    cfunc: tuple[DirectiveScopeType, ...]
    ccall: tuple[DirectiveScopeType, ...]
    returns: tuple[DirectiveScopeType, ...]
    exceptval: tuple[DirectiveScopeType, ...]
    locals: tuple[DirectiveScopeType, ...]
    staticmethod: tuple[DirectiveScopeType, ...]
    no_gc_clear: tuple[DirectiveScopeType, ...]
    no_gc: tuple[DirectiveScopeType, ...]
    internal: tuple[DirectiveScopeType, ...]
    cclass: tuple[DirectiveScopeType, ...]
    autotestdict: AutotestdictDirectivesScopes
    set_initial_path: tuple[DirectiveScopeType, ...]
    test_assert_path_exists: tuple[DirectiveScopeType, ...]
    test_fail_if_path_exists: tuple[DirectiveScopeType, ...]
    test_assert_c_code_has: tuple[DirectiveScopeType, ...]
    test_fail_if_c_code_has: tuple[DirectiveScopeType, ...]
    freelist: tuple[DirectiveScopeType, ...]
    formal_grammar: tuple[DirectiveScopeType, ...]
    emit_code_comments: tuple[DirectiveScopeType, ...]
    c_string_type: tuple[DirectiveScopeType, ...]
    c_string_encoding: tuple[DirectiveScopeType, ...]
    type_version_tag: tuple[DirectiveScopeType, ...]
    language_level: tuple[DirectiveScopeType, ...]
    old_style_globals: tuple[DirectiveScopeType, ...]
    np_pythran: tuple[DirectiveScopeType, ...]
    preliminary_late_includes_cy28: tuple[DirectiveScopeType, ...]
    fast_gil: tuple[DirectiveScopeType, ...]
    iterable_coroutine: tuple[DirectiveScopeType, ...]
    trashcan: tuple[DirectiveScopeType, ...]
    total_ordering: tuple[DirectiveScopeType, ...]
    dataclasses: DataclassDirectivesScopes
    cpp_locals: tuple[DirectiveScopeType, ...]
    ufunc: tuple[DirectiveScopeType, ...]
    legacy_implicit_noexcept: tuple[DirectiveScopeType, ...]
    c_compile_guard: tuple[DirectiveScopeType, ...]
    control_flow: ControlFlowDirectives
    freethreading_compatible: tuple[DirectiveScopeType, ...]
    subinterpreters_compatible: tuple[DirectiveScopeType, ...]


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
DirectiveType = Union[Type, Callable[[str, Any], Any], "_DeferAnalysisOfArgumentsType", None]
# Mapping from directive-name strings to their validation/typing helpers


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
embed_pos_in_docstring = True

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
annotate = True

# When annotating source files in HTML, include coverage information from
# this file.
annotate_coverage_xml = None

#: This will abort the compilation on the first error occurred rather than trying
#: to keep going and printing further error messages.
fast_fail = True

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

#: When embedding, this allows listing the names of statically linked extension modules
#: to register with Python's inittab mechanism on startup, so that they can be imported.
embed_modules = []

# Directive-only options: Accessing these directly will raise an error.
# These are placeholders managed by ShouldBeFromDirective.
# In previous iterations of Cython, globals() gave the first non-Cython module
# globals in the call stack.  Sage relies on this behavior for variable injection.
old_style_globals = ShouldBeFromDirective("old_style_globals")

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
    "warn.maybe_uninitialized": True,
    "warn.unreachable": True,
    "warn.unused": True,
}


@dataclass
class Directives(DataDict):
    """Dataclass representing all Cython compiler directives with their default values."""

    # Default values for all directives
    binding: bool = True  # was False before 3.0
    boundscheck: bool = False
    nonecheck: bool = False
    initializedcheck: bool = True
    freethreading_compatible: bool = False
    subinterpreters_compatible: str = "no"
    embedsignature: EmbedSignatureDirectives = field(default_factory=EmbedSignatureDirectives)
    auto_cpdef: bool = False
    auto_pickle: Optional[bool] = None
    cdivision: bool = True
    cdivision_warnings: bool = False
    cpow: bool = True
    c_api_binop_methods: bool = True
    overflowcheck: OverflowcheckDirectives = field(default_factory=OverflowcheckDirectives)
    always_allow_keywords: bool = True
    allow_none_for_extension_args: bool = True
    wraparound: bool = False
    ccomplex: bool = False  # use C99/C++ for complex types and arith
    callspec: str = ""
    nogil: bool = False
    gil: bool = False
    with_gil: bool = False
    profile: bool = False
    linetrace: bool = False
    emit_code_comments: bool = True  # copy original source code into C code comments
    annotation_typing: bool = True  # read type declarations from Python function annotations
    infer_types: InferTypesDirectives = field(default_factory=InferTypesDirectives)
    autotestdict: AutotestdictDirectives = field(default_factory=AutotestdictDirectives)
    language_level: str = "3"
    fast_getattr: bool = (
        False  # Undocumented until we come up with a better way to handle this everywhere.
    )
    py2_import: bool = (
        False  # For backward compatibility of Cython's source code in Py3 source mode
    )
    preliminary_late_includes_cy28: bool = (
        False  # Temporary directive in 0.28, to be removed in a later version (see GH#2079).
    )
    iterable_coroutine: bool = (
        False  # Make async coroutines backwards compatible with the old asyncio yield-from syntax.
    )
    c_string_type: str = "bytes"
    c_string_encoding: str = ""
    type_version_tag: bool = True  # enables Py_TPFLAGS_HAVE_VERSION_TAG on extension types
    unraisable_tracebacks: bool = True
    old_style_globals: bool = False
    np_pythran: bool = False
    fast_gil: bool = True
    cpp_locals: bool = (
        False  # uses std::optional for C++ locals, so that they work more like Python locals
    )
    legacy_implicit_noexcept: bool = False
    c_compile_guard: str = ""
    set_initial_path: Optional[str] = None  # SOURCEFILE or "/full/path/to/module"
    warn: WarnDirectives = field(default_factory=WarnDirectives)
    show_performance_hints: bool = True
    optimize: OptimizeDirectives = field(default_factory=OptimizeDirectives)
    remove_unreachable: bool = True
    control_flow: ControlFlowDirectives = field(default_factory=ControlFlowDirectives)
    test_assert_path_exists: List[str] = field(default_factory=list)
    test_fail_if_path_exists: List[str] = field(default_factory=list)
    test_assert_c_code_has: List[str] = field(default_factory=list)
    test_fail_if_c_code_has: List[str] = field(default_factory=list)
    formal_grammar: bool = False
    overload_dispatch: bool = True


def get_directive_defaults() -> Directives:
    """Return a copy of the directive defaults dictionary."""
    return Directives()


def parse_directive_list(
    s: str,
    relaxed_bool: bool = False,
    ignore_unknown: bool = False,
    current_settings: Optional[DirectivesDict] = None,
) -> DirectivesDict:
    """Public wrapper for _parse_directive_list for backward compatibility."""
    return _parse_directive_list(s, relaxed_bool, ignore_unknown, current_settings)


def _copy_inherited_directives(
    outer_directives: DirectivesDict | Directives, **new_directives: Unpack[DirectivesDict]
) -> DirectivesDict:
    # A few directives are not copied downwards and this function removes them.
    # For example, test_assert_path_exists and test_fail_if_path_exists should not be inherited
    #  otherwise they can produce very misleading test failures
    # Start with a shallow copy that preserves runtime DataDict behaviour when available.
    if isinstance(outer_directives, DataDict):
        new_directives_out: DirectivesDict = cast(DirectivesDict, outer_directives.copy())
    else:
        new_directives_out = cast(DirectivesDict, outer_directives.copy())

    removal_keys: Tuple[RemovalKey, ...] = (
        "test_assert_path_exists",
        "test_fail_if_path_exists",
        "test_assert_c_code_has",
        "test_fail_if_c_code_has",
        "critical_section",
    )
    for name in removal_keys:
        if name in new_directives_out:
            new_directives_out.pop(name)
    new_directives_out.update(**new_directives)
    return new_directives_out


copy_inherited_directives = _copy_inherited_directives


def copy_for_internal(outer_directives: DirectivesDict) -> DirectivesDict:
    # Reset some directives that users should not control for internal code.
    return _copy_inherited_directives(
        outer_directives,
        binding=False,
        profile=False,
        linetrace=False,
    )


_copy_for_internal = copy_for_internal


def one_of(*args, map=None):
    def validate(name, value):
        if map is not None:
            value = map.get(value, value)
        if value not in args:
            raise ValueError("%s directive must be one of %s, got '%s'" % (name, args, value))
        return value

    return validate


_normalise_common_encoding_name = {
    "utf8": "utf8",
    "utf-8": "utf8",
    "default": "utf8",
    "ascii": "ascii",
    "us-ascii": "ascii",
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
        return ""
    encoding_name = _normalise_common_encoding_name(encoding.lower())
    if encoding_name is not None:
        return encoding_name

    return encoding


DirectiveTypesMap = Dict[str, DirectiveType]
# Override types possibilities above, if needed
directive_types: DirectiveTypesMap = {
    "language_level": str,  # values can be None/2/3/'3str', where None == 2+warning
    "auto_pickle": bool,
    "locals": dict,
    "final": bool,  # final cdef classes and methods
    "collection_type": one_of("sequence"),
    "nogil": DEFER_ANALYSIS_OF_ARGUMENTS,
    "gil": DEFER_ANALYSIS_OF_ARGUMENTS,
    "critical_section": DEFER_ANALYSIS_OF_ARGUMENTS,
    "with_gil": None,
    "internal": bool,  # cdef class visibility in the module dict
    "infer_types.verbose": DEFER_ANALYSIS_OF_ARGUMENTS,
    "infer_types.enabled": DEFER_ANALYSIS_OF_ARGUMENTS,
    "binding": bool,
    "cfunc": None,  # decorators do not take directive value
    "ccall": None,
    "ufunc": None,
    "cpow": bool,
    "inline": None,
    "staticmethod": None,
    "cclass": None,
    "no_gc_clear": bool,
    "no_gc": bool,
    "returns": type,
    "exceptval": type,  # actually (type, check=True/False), but has its own parser
    "set_initial_path": str,
    "freelist": int,
    "c_string_type": one_of("bytes", "bytearray", "str", "unicode", map={"unicode": "str"}),
    "c_string_encoding": normalise_encoding_name,
    "trashcan": bool,
    "total_ordering": None,
    "dataclasses.dataclass": DEFER_ANALYSIS_OF_ARGUMENTS,
    "dataclasses.field": DEFER_ANALYSIS_OF_ARGUMENTS,
    "embedsignature.format": one_of("c", "clinic", "python"),
    "subinterpreters_compatible": one_of("no", "shared_gil", "own_gil"),
}

for key, val in get_directive_defaults().items():
    if key not in directive_types:
        directive_types[key] = type(val)

# For 'with statement' strings in tuples
WithStatement = Literal["with statement"]

# Create a mapping for scopes with dots in their names


# A list of directives that (when used as a decorator) are only applied to
# the object they decorate and not to its children.
immediate_decorator_directives = {
    "cfunc",
    "ccall",
    "cclass",
    "dataclasses.dataclass",
    "ufunc",
    # function signature directives
    "inline",
    "exceptval",
    "returns",
    "with_gil",  # 'nogil',
    # class directives
    "freelist",
    "no_gc",
    "no_gc_clear",
    "type_version_tag",
    "final",
    "auto_pickle",
    "internal",
    "collection_type",
    "total_ordering",
    # testing directives
    "test_fail_if_path_exists",
    "test_assert_path_exists",
}


def _parse_directive_list(
    s: str,
    relaxed_bool: bool = False,
    ignore_unknown: bool = False,
    current_settings: Optional[DirectivesDict] = None,
) -> DirectivesDict:
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
    directives = Directives()
    result: DirectivesDict = {} if current_settings is None else current_settings
    for item in s.split(","):
        item = item.strip()
        if not item:
            continue
        if "=" not in item:
            raise ValueError('Expected "=" in option "%s"' % item)
        name, value = [s.strip() for s in item.strip().split("=", 1)]
        # Expand "*.all" first, even if it exists as a default key
        if name.endswith(".all"):
            prefix = name[:-3]  # keep trailing dot like upstream for simple startswith()
            found_any = False
            for directive in directives:
                if directive.startswith(prefix):
                    found_any = True
                    parsed_value = _parse_directive_value(
                        directive, value, relaxed_bool=relaxed_bool
                    )
                    result[directive] = parsed_value
            if not found_any and not ignore_unknown:
                raise ValueError('Unknown option: "%s"' % name)
            continue

        if name not in directives:
            if not ignore_unknown:
                raise ValueError('Unknown option: "%s"' % name)
        elif directive_types.get(name) is list:
            if name in result:
                result[name].append(value)
            else:
                result[name] = [value]
        else:
            parsed_value = _parse_directive_value(name, value, relaxed_bool=relaxed_bool)
            result[name] = parsed_value
    return result


RemovalKey = Literal[
    "test_assert_path_exists",
    "test_fail_if_path_exists",
    "test_assert_c_code_has",
    "test_fail_if_c_code_has",
    "critical_section",
]


def parse_compile_time_env(
    s: str, current_settings: DirectivesDict | None = None
) -> DirectivesDict:
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
    result = current_settings or {}
    for item in s.split(","):
        item = item.strip()
        if not item:
            continue
        if "=" not in item:
            raise ValueError('Expected "=" in option "%s"' % item)
        name, value = [s.strip() for s in item.split("=", 1)]
        result[name] = _parse_directive_value(name, value)
    return result


# Mirror upstream: parse a single directive value based on its declared type.
def _parse_directive_value(name: str, value: Any, relaxed_bool: bool = False) -> Any:
    type_info = directive_types.get(name)
    if not type_info:
        return None
    orig_value = value
    if type_info is bool:
        value = str(value)
        if value == "True":
            return True
        if value == "False":
            return False
        if relaxed_bool:
            value = value.lower()
            if value in ("true", "yes"):
                return True
            elif value in ("false", "no"):
                return False
        raise ValueError("%s directive must be set to True or False, got '%s'" % (name, orig_value))
    elif type_info is int:
        try:
            return int(value)
        except ValueError as e:
            raise ValueError(
                "%s directive must be set to an integer, got '%s'" % (name, orig_value)
            ) from e
    elif type_info is str:
        return str(value)
    elif callable(type_info):
        return type_info(name, value)
    else:
        raise ValueError("%s directive must be set to a valid type, got '%s'" % (name, orig_value))


# ------------------------------------------------------------------------
# GlobalDirectives are constructed to manage directive defaults, types and scopes
# ------------------------------------------------------------------------


@dataclass
class GlobalDirectives(DataDict):
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
        """Initialize references to module-level directive configuration.

        Keep behavior identical to upstream by reusing the single
        module-level sources of truth for types/scopes and helpers.
        """
        # Reuse the module-level mappings to avoid divergence.
        self.directive_types = directive_types
        # Use the class method to avoid forward-reference issues during import
        self.directive_scopes = self.get_directive_scopes()
        self.immediate_decorator_directives = immediate_decorator_directives

        # Extra warning toggles remain as lightweight data.
        self.extra_warnings = {
            "warn.maybe_uninitialized": True,
            "warn.unreachable": True,
            "warn.unused": True,
        }

    def get_directive_defaults(self) -> DirectiveDefaultsDict:
        """Return the default directive values."""
        return cast(DirectiveDefaultsDict, self.copy())

    def parse_directive_value(self, name: str, value: Any, relaxed_bool: bool = False) -> Any:
        """Delegate to module-level parser for identical behavior."""
        return _parse_directive_value(name, value, relaxed_bool)

    def parse_directive_list(
        self,
        s: str,
        relaxed_bool: bool = False,
        ignore_unknown: bool = False,
        current_settings: Optional[DirectivesDict] = None,
    ) -> DirectivesDict:
        """Delegate to module-level list parser for identical behavior."""
        return _parse_directive_list(s, relaxed_bool, ignore_unknown, current_settings)

    def parse_variable_value(self, value: str) -> Any:
        return _parse_variable_value(value)

    def parse_compile_time_env(
        self, s: str, current_settings: DirectivesDict | None = None
    ) -> DirectivesDict:
        return _parse_compile_time_env(s, current_settings)

    def _one_of(
        self, *args: str, map: Optional[Dict[str, str]] = None
    ) -> Callable[[str, Any], Any]:
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
                raise ValueError("%s directive must be one of %s, got '%s'" % (name, args, value))
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
            return ""

        _normalise_common_encoding_name = {
            "utf8": "utf8",
            "utf-8": "utf8",
            "default": "utf8",
            "ascii": "ascii",
            "us-ascii": "ascii",
        }.get

        encoding_name = _normalise_common_encoding_name(encoding.lower())
        if encoding_name is not None:
            return encoding_name

        return encoding

    def copy_inherited_directives(
        self, outer_directives: DirectivesDict, **new_directives: Unpack[DirectivesDict]
    ) -> DirectivesDict:
        return _copy_inherited_directives(outer_directives, **new_directives)

    def copy_for_internal(self, outer_directives: DirectivesDict) -> DirectivesDict:
        return _copy_for_internal(outer_directives)

    def to_dict(self) -> dict[str, object]:
        """
        Convert GlobalDirectives to a dictionary representation.

        Returns:
            Dictionary containing important configuration values.
        """
        result = {
            "directive_defaults": self.copy(),
            "directive_scopes": self.directive_scopes,
            "directive_types": {k: str(v) for k, v in self.directive_types.items()},
            "immediate_decorator_directives": list(self.immediate_decorator_directives),
            "extra_warnings": self.extra_warnings.copy(),
        }
        return result

    def get_directive_scopes(self) -> DirectiveScopesDict:
        """
        Return the directive scopes dictionary properly typed.

        Returns:
            A DirectiveScopesDict mapping directives to allowed scopes
        """
        return {
            "auto_pickle": ("module", "cclass"),
            "final": ("cclass", "function"),
            "ccomplex": ("module",),
            "collection_type": ("cclass",),
            "nogil": ("function", "with statement"),
            "gil": ("with statement",),
            "with_gil": ("function",),
            "critical_section": ("function", "with statement"),
            "inline": ("function",),
            "cfunc": ("function", "with statement"),
            "ccall": ("function", "with statement"),
            "returns": ("function",),
            "exceptval": ("function",),
            "locals": ("function",),
            "staticmethod": (
                "function",
            ),  # FIXME: analysis currently lacks more specific function scope
            "no_gc_clear": ("cclass",),
            "no_gc": ("cclass",),
            "internal": ("cclass",),
            "cclass": ("class", "cclass", "with statement"),
            "autotestdict": AutotestdictDirectivesScopes("module", "module"),
            "set_initial_path": ("module",),
            "test_assert_path_exists": ("function", "class", "cclass"),
            "test_fail_if_path_exists": ("function", "class", "cclass"),
            "test_assert_c_code_has": ("module",),
            "test_fail_if_c_code_has": ("module",),
            "freelist": ("cclass",),
            "formal_grammar": ("module",),
            "emit_code_comments": ("module",),
            "overload_dispatch": ("module", "class", "function"),
            # Avoid scope-specific to/from_py_functions for c_string.
            "c_string_type": ("module",),
            "c_string_encoding": ("module",),
            "type_version_tag": ("module", "cclass"),
            "language_level": ("module",),
            # globals() could conceivably be controlled at a finer granularity,
            # but that would complicate the implementation
            "old_style_globals": ("module",),
            "np_pythran": ("module",),
            "preliminary_late_includes_cy28": ("module",),
            "fast_gil": ("module",),
            "iterable_coroutine": ("module", "function"),
            "trashcan": ("cclass",),
            "total_ordering": ("class", "cclass"),
            "dataclasses": DataclassDirectivesScopes("class", "cclass"),
            "cpp_locals": (
                "module",
                "function",
                "cclass",
            ),  # I don't think they make sense in a with_statement
            "ufunc": ("function",),
            "legacy_implicit_noexcept": ("module",),
            "c_compile_guard": ("function",),  # actually C function but this is enforced later
            "control_flow": ControlFlowDirectives("module", "module"),
            "freethreading_compatible": ("module",),
            "subinterpreters_compatible": ("module",),
        }


# ------------------------------------------------------------------------
# CompilationOptions are constructed from user input and are the `option`
#  object passed throughout the compilation pipeline.
# ------------------------------------------------------------------------
CYTHON_COMMON_UTILITY_INCLUDE_DIR = str(Path(__file__).parent.parent / "Common" / "Include")


class CompilationOptionsDict(TypedDict):
    """TypedDict representation of CompilationOptions for type checking and serialization."""

    include_path: List[str]
    output_file: Optional[str]
    show_version: bool
    use_listing_file: bool
    errors_to_stderr: bool
    cplus: bool
    depfile: Optional[bool]
    make_depfile: bool
    annotate: Optional[bool]
    annotate_no_c_link: bool
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


class CompilationOptionsKwargs(TypedDict, total=False):
    include_path: List[str]
    output_file: Optional[str]
    show_version: bool
    use_listing_file: bool
    errors_to_stderr: bool
    cplus: bool
    depfile: Optional[bool]
    make_depfile: bool
    annotate: Optional[bool]
    annotate_no_c_link: bool
    annotate_coverage_xml: Optional[str]
    generate_pxi: bool
    capi_reexport_cincludes: bool
    working_path: str
    timestamps: Optional[Any]
    verbose: int
    quiet: bool
    compiler_directives: DirectivesDict | Directives
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
class CompilationOptions(DataDict):
    """
    Options for Cython compilation, used throughout the compilation pipeline.
    See default_options at the end of this module for a list of all possible
    options and CmdLine.usage and CmdLine.parse_command_line() for their meaning.
    """

    # Fields defined based on old CompilationOptionKwargs and default_options
    include_path: list[str] = field(default_factory=lambda: ["."])
    shared_c_file_path: Optional[str] = None
    output_file: Optional[str] = None
    show_version: bool = False
    use_listing_file: bool = False
    errors_to_stderr: bool = True
    cplus: bool = False
    depfile: Optional[bool] = None
    make_depfile: bool = False
    annotate: Optional[bool] = None
    annotate_no_c_link: bool = False
    annotate_coverage_xml: Optional[str] = None
    generate_pxi: bool = False
    capi_reexport_cincludes: bool = False
    working_path: str = ""
    timestamps: Optional[Any] = None
    verbose: int = 0
    quiet: bool = False
    compiler_directives: Directives | DirectivesDict = field(default_factory=get_directive_defaults)
    embedded_metadata: Mapping[str, Any] = field(default_factory=dict)
    embedding_file_name: Optional[str] = None
    embedding_file_timestamp: Optional[int] = None
    evaluate_tree_assertions: bool = False
    emit_linenums: bool = False
    relative_path_in_code_position_comments: bool = True
    c_line_in_traceback: bool = True
    language_level: Optional[Any] = None
    formal_grammar: bool = False
    gdb_debug: bool = False
    compile_time_env: Mapping[str, Any] = field(default_factory=dict)
    module_name: Optional[str] = None
    common_utility_include_dir: Optional[str] = CYTHON_COMMON_UTILITY_INCLUDE_DIR
    output_dir: Optional[str] = None
    build_dir: Optional[str] = None
    cache: Optional[Any] = None
    cache_size: Optional[int] = None
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
        # Check for unknown directives
        directive_defaults = get_directive_defaults()
        unknown_directives = set(self.compiler_directives.keys()) - set(directive_defaults.keys())
        if unknown_directives:
            message = "got unknown compiler directive%s: %s" % (
                "s" if len(unknown_directives) > 1 else "",
                ", ".join(map(str, unknown_directives)),
            )
            raise ValueError(message)

        # Handle np_pythran forcing cplus
        if self.compiler_directives.get("np_pythran", False) and not self.cplus:
            import warnings

            warnings.warn("C++ mode forced when in Pythran mode!")
            self.cplus = True
        self.compiler_directives = Directives(**self.compiler_directives)

    def configure_language_defaults(self, source_extension: str) -> None:
        """
        Configure language level defaults based on source extension and directives.

        Args:
            source_extension: The file extension of the source file
        """
        # Direct access to dataclass fields
        directives = self.compiler_directives.copy()

        lang_level = directives.get("language_level")
        if lang_level is None:
            # Auto-detect language level.
            import sys

            lang_level = "3" if sys.version_info[0] >= 3 else "2"
            # Update the directive itself if it was None
            directives["language_level"] = lang_level

        # Update the main language_level attribute based on the directive value
        if lang_level in (2, "2"):
            self.language_level = 2
        elif (isinstance(lang_level, int) and lang_level >= 3) or str(lang_level).startswith("3"):
            self.language_level = 3
        else:
            # This case should ideally be caught by directive validation earlier
            # but kept here for robustness.
            raise ValueError("Invalid language level: %r" % lang_level)

        # Python files always imply binding=True unless explicitly set to False
        if source_extension == "py" and directives.get("binding") is not False:
            self.compiler_directives["binding"] = True

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
        fingerprint = hashlib.md5(str(parts).encode("utf-8")).hexdigest()
        return fingerprint

    def get_embedded_main_c_function(self) -> Optional[str]:
        """
        Get the name of the embedded main C function if embedding is enabled.

        Returns:
            The function name or None if embedding is not enabled
        """
        embed = self.embed
        if isinstance(embed, bool):
            return "main" if embed else None
        if MatchAST and hasattr(self, "source") and self.source:
            match = MatchAST[ast.FunctionDef, Literal["node"]](func_def(name=str(embed)), "node")(
                self.source
            )
            if match:
                return match.name
        if isinstance(embed, str):
            return embed
        return None


def get_default_options() -> CompilationOptions:
    """Return a new instance of CompilationOptions with default values."""
    # Create a GlobalDirectives instance to provide default global options
    global_directives = GlobalDirectives()

    # Create a CompilationOptions instance with default values
    options = CompilationOptions(
        compiler_directives=get_directive_defaults(),  # Use module-level function for compiler directives
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
        depfile=False,
        old_style_globals=global_directives.old_style_globals,
    )
    return options.copy()


# Create default options dictionary
default_options: CompilationOptions = get_default_options()  # type: ignore[assignment]

# Create a global wrapper (no overrides) for consumers that expect an object.
GLOBAL_DIRECTIVES = GlobalDirectives()
directive_defaults = GLOBAL_DIRECTIVES.get_directive_defaults()


# Transform the directive_scopes into a DirectiveScopesDict
def get_directive_scopes() -> DirectiveScopesDict:
    """Return the directive scopes as a properly typed DirectiveScopesDict."""
    return DirectiveScopesDict()


directive_scopes = get_directive_scopes()
