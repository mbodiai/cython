#
#  Cython - Compilation-wide options and pragma declarations
#
from __future__ import annotations

from dataclasses import dataclass, field
from typing import (
    Any,
    List,
    Optional,
    Union,
    Callable,
    Type,
    Tuple,
    Literal,
    Unpack,
    TYPE_CHECKING,
)
from typing_extensions import TypedDict
from Cython.DataDict import DataDict


embedding_file_name: Optional[str]


DirectiveScopeType = Literal["module", "function", "cclass", "class", "with statement"]




@dataclass
class AutotestdictDirectives(DataDict):
    all: bool = True
    cdef: bool = True

    class Dict(TypedDict):
        all: bool
        cdef: bool


@dataclass
class EmbedSignatureDirectives(DataDict):
    enabled: bool = False
    format: str = "c"

    class Dict(TypedDict):
        enabled: bool
        format: str

@dataclass
class OverflowCheckDirectives(DataDict):
    enabled: bool = False
    fold: bool = True

    class Dict(TypedDict):
        enabled: bool
        fold: bool


@dataclass
class InferTypesDirectives(DataDict):
    enabled: bool = True
    verbose: bool = False

    class Dict(TypedDict):
        enabled: bool
        verbose: bool


@dataclass
class FastGetattrDirectives(DataDict):
    fast: bool = True

    class Dict(TypedDict):
        fast: bool


@dataclass
class Py2ImportDirectives(DataDict):
    py2: bool = False

    class Dict(TypedDict):
        py2: bool


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
    deprecated_DEF: bool = False # noqa: N815
    deprecated_IF: bool = False # noqa: N815

    class Dict(TypedDict):
        all: bool
        undeclared: bool
        unreachable: bool
        maybe_uninitialized: bool
        unused: bool
        unused_arg: bool
        unused_result: bool
        multiple_declarators: bool
        deprecated_DEF: bool
        deprecated_IF: bool

@dataclass
class OptimizeDirectives(DataDict):
    inline_defnode_calls: bool = True
    unpack_method_calls: bool = True
    unpack_method_calls_in_pyinit: bool = True
    use_switch: bool = True

    class Dict(TypedDict):
        inline_defnode_calls: bool
        unpack_method_calls: bool
        unpack_method_calls_in_pyinit: bool
        use_switch: bool


@dataclass
class ControlFlowDirectives(DataDict):
    output: str = ""
    annotate_defs: bool = False
    dot_output: str = ""
    dot_annotate_defs: bool = False

    class Dict(TypedDict):
        output: str
        annotate_defs: bool
        dot_output: str
        dot_annotate_defs: bool

@dataclass
class TestDirectives(DataDict):
    assert_path_exists: List[str]
    fail_if_path_exists: List[str]
    assert_c_code_has: List[str]
    fail_if_c_code_has: List[str]

    class Dict(TypedDict):
        assert_path_exists: List[str]
        fail_if_path_exists: List[str]
        assert_c_code_has: List[str]
        fail_if_c_code_has: List[str]


@dataclass
class AutotestdictDirectiveScopes(DataDict):
    all: DirectiveScopeType = "module"
    cdef: DirectiveScopeType = "module"

    class Dict(TypedDict):
        all: DirectiveScopeType
        cdef: DirectiveScopeType


@dataclass
class DataclassDirectiveScopes(DataDict):
    dataclass: DirectiveScopeType = "class"
    field: DirectiveScopeType = "class"

    class Dict(TypedDict):
        dataclass: DirectiveScopeType
        field: DirectiveScopeType

@dataclass
class ControlFlowDirectiveScopes(DataDict):
    output: DirectiveScopeType = "module"
    annotate_defs: DirectiveScopeType = "module"
    dot_output: DirectiveScopeType = "module"
    dot_annotate_defs: DirectiveScopeType = "module"


    class Dict(TypedDict):
        output: DirectiveScopeType
        annotate_defs: DirectiveScopeType
        dot_output: DirectiveScopeType
        dot_annotate_defs: DirectiveScopeType
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
        return (
            "ShouldBeFromDirective("
            f"options_name='{self.options_name}', "
            f"directive_name='{self.directive_name}')"
        )


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

#: Whether or not to include docstring in the Python extension. If False, the
#: binary size will be smaller, but the ``__doc__`` attribute of any class or
#: function will be an
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

#: Generate an annotated HTML version of the input source files for debugging
#: and optimisation purposes.
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
    auto_pickle: bool = False
    cdivision: bool = True
    cdivision_warnings: bool = False
    cpow: bool = True
    c_api_binop_methods: bool = True
    overflowcheck: OverflowCheckDirectives = field(default_factory=OverflowCheckDirectives)
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
    language_level: int | str = 3
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
    set_initial_path: str | None = None  # SOURCEFILE or "/full/path/to/module"
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

    def __post_init__(self) -> None:
        nested_fields = (
            "overflowcheck",
            "infer_types",
            "autotestdict",
            "warn",
            "optimize",
            "control_flow",
            "embedsignature",
        )
        for name in nested_fields:
            annotation = type(self).__annotations__[name]
            if isinstance(annotation, str):
                annotation = eval(annotation, globals(), locals())
            value = getattr(self, name)
            if isinstance(value, bool):
                defaults = {field_name: value for field_name in annotation.__annotations__}
                setattr(self, name, annotation(**defaults))
            else:
                setattr(self, name, annotation(**value))

    class Dict(TypedDict):
        binding: bool
        boundscheck: bool
        nonecheck: bool
        initializedcheck: bool
        freethreading_compatible: bool
        subinterpreters_compatible: str
        embedsignature: EmbedSignatureDirectives.Dict
        auto_cpdef: bool
        auto_pickle: bool
        cdivision: bool
        cdivision_warnings: bool
        cpow: bool
        c_api_binop_methods: bool
        overflowcheck: OverflowCheckDirectives.Dict
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
        infer_types: InferTypesDirectives.Dict
        autotestdict: AutotestdictDirectives.Dict
        language_level: int | str
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
        warn: WarnDirectives.Dict
        show_performance_hints: bool
        optimize: OptimizeDirectives.Dict
        remove_unreachable: bool
        control_flow: ControlFlowDirectives.Dict

    class Kwargs(TypedDict, total=False):
        binding: bool
        boundscheck: bool
        nonecheck: bool
        initializedcheck: bool
        freethreading_compatible: bool
        subinterpreters_compatible: str
        embedsignature: EmbedSignatureDirectives.Dict
        auto_cpdef: bool
        auto_pickle: bool
        cdivision: bool
        cdivision_warnings: bool
        cpow: bool
        c_api_binop_methods: bool
        overflowcheck: OverflowCheckDirectives.Dict
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
        infer_types: InferTypesDirectives.Dict
        autotestdict: AutotestdictDirectives.Dict
        language_level: int | str
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
        warn: WarnDirectives.Dict
        show_performance_hints: bool
        optimize: OptimizeDirectives.Dict
        remove_unreachable: bool
        control_flow: ControlFlowDirectives.Dict
        test_assert_path_exists: List[str]
        test_fail_if_path_exists: List[str]
        test_assert_c_code_has: List[str]
        test_fail_if_c_code_has: List[str]
        formal_grammar: bool
        overload_dispatch: bool

class DirectivesDict(Directives.Dict):...
class DirectivesKwargs(Directives.Kwargs):...


def _copy_inherited_directives(
    outer_directives: Directives, **new_directives: Unpack[Directives.Kwargs]
) -> Directives:
    new_directives_out = Directives(**outer_directives.dict())

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


def copy_for_internal(outer_directives: Directives) -> Directives:
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


RemovalKey = Literal[
    "test_assert_path_exists",
    "test_fail_if_path_exists",
    "test_assert_c_code_has",
    "test_fail_if_c_code_has",
    "critical_section",
]





class DirectiveScopes(DataDict):
    auto_pickle: tuple[DirectiveScopeType, ...] = ("module", "cclass")
    final: tuple[DirectiveScopeType, ...] = ("cclass", "function")
    ccomplex: tuple[DirectiveScopeType, ...] = ("module",)
    collection_type: tuple[DirectiveScopeType, ...] = ("cclass",)
    nogil: tuple[DirectiveScopeType, ...] = ("function", "with statement")
    gil: tuple[DirectiveScopeType, ...] = ("with statement",)
    with_gil: tuple[DirectiveScopeType, ...] = ("function",)
    critical_section: tuple[DirectiveScopeType, ...] = ("function", "with statement")
    inline: tuple[DirectiveScopeType, ...] = ("function",)
    cfunc: tuple[DirectiveScopeType, ...] = ("function", "with statement")
    ccall: tuple[DirectiveScopeType, ...] = ("function", "with statement")
    returns: tuple[DirectiveScopeType, ...] = ("function",)
    exceptval: tuple[DirectiveScopeType, ...] = ("function",)
    locals: tuple[DirectiveScopeType, ...] = ("function",)
    staticmethod: tuple[DirectiveScopeType, ...] = ("function",)
    no_gc_clear: tuple[DirectiveScopeType, ...] = ("cclass",)
    no_gc: tuple[DirectiveScopeType, ...] = ("cclass",)
    internal: tuple[DirectiveScopeType, ...]
    cclass: tuple[DirectiveScopeType, ...]
    autotestdict: AutotestdictDirectiveScopes = field(default_factory=AutotestdictDirectiveScopes)
    set_initial_path: tuple[DirectiveScopeType, ...]
    test_assert_path_exists: tuple[DirectiveScopeType, ...] = ("function", "class", "cclass")
    test_fail_if_path_exists: tuple[DirectiveScopeType, ...] = ("function", "class", "cclass")
    test_assert_c_code_has: tuple[DirectiveScopeType, ...] = ("module",)
    test_fail_if_c_code_has: tuple[DirectiveScopeType, ...] = ("module",)
    freelist: tuple[DirectiveScopeType, ...] = ("cclass",)  
    formal_grammar: tuple[DirectiveScopeType, ...] = ("module",)
    emit_code_comments: tuple[DirectiveScopeType, ...] = ("module",)
    c_string_type: tuple[DirectiveScopeType, ...] = ("module",)
    c_string_encoding: tuple[DirectiveScopeType, ...] = ("module",)
    type_version_tag: tuple[DirectiveScopeType, ...] = ("module",)
    language_level: tuple[DirectiveScopeType, ...] = ("module",)
    old_style_globals: tuple[DirectiveScopeType, ...] = ("module",)
    np_pythran: tuple[DirectiveScopeType, ...] = ("module",)
    preliminary_late_includes_cy28: tuple[DirectiveScopeType, ...] = ("module",)
    fast_gil: tuple[DirectiveScopeType, ...] = ("module",)
    iterable_coroutine: tuple[DirectiveScopeType, ...] = ("module",)
    trashcan: tuple[DirectiveScopeType, ...] = ("module",)
    total_ordering: tuple[DirectiveScopeType, ...] = ("module",)
    dataclasses: DataclassDirectiveScopes = field(default_factory=DataclassDirectiveScopes)
    cpp_locals: tuple[DirectiveScopeType, ...] = ("module",)
    ufunc: tuple[DirectiveScopeType, ...] = ("module",)
    legacy_implicit_noexcept: tuple[DirectiveScopeType, ...] = ("module",)
    c_compile_guard: tuple[DirectiveScopeType, ...] = ("module",)
    control_flow: tuple[DirectiveScopeType, ...] = ("module",)
     


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

    #: Generate an annotated HTML version of the input source files for
    #: debugging and optimisation purposes.
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
        self.directive_types = type(Directives()).__annotations__
        # Use the class method to avoid forward-reference issues during import
        self.directive_scopes = DirectiveScopes()
        self.immediate_decorator_directives = immediate_decorator_directives

        # Extra warning toggles remain as lightweight data.
        self.extra_warnings = {
            "warn.maybe_uninitialized": True,
            "warn.unreachable": True,
            "warn.unused": True,
        }

    


# Create a global wrapper (no overrides) for consumers that expect an object.
GLOBAL_DIRECTIVES = GlobalDirectives()

DIRECTIVE_DEFAULTS = Directives()


if not TYPE_CHECKING:
    DirectiveScopesDict = DirectiveScopes
    AutotestdictDirectivesScopesDict = AutotestdictDirectives
    ControlFlowDirectivesScopesDict = ControlFlowDirectives
    DataclassDirectiveScopesDict = DataclassDirectiveScopes
    AutotestdictDirectivesDict = AutotestdictDirectives
    ControlFlowDirectivesDict = ControlFlowDirectives
    DirectiveScopesDict = DirectiveScopesDict
    EmbedSignatureDirectivesDict = EmbedSignatureDirectives
    InferTypesDirectivesDict = InferTypesDirectives
    OptimizeDirectivesDict = OptimizeDirectives
    OverflowCheckDirectivesDict = OverflowCheckDirectives
    WarnDirectivesDict = WarnDirectives
    DirectivesDict = Directives
