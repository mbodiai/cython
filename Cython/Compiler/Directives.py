#
#  Cython - Compilation-wide options and pragma declarations
#
from __future__ import annotations

from collections.abc import Mapping, Callable
from dataclasses import dataclass, field, asdict, is_dataclass
from typing import Any, Literal, TYPE_CHECKING, get_type_hints
from typing_extensions import TypedDict, Unpack
from Cython.DataDict import DataDict


embedding_file_name: str | None


DirectiveScopeType = Literal["module", "function", "cclass", "class", "with statement"]




@dataclass
class AutotestdictDirectives(DataDict):
    all: bool = field(default=True)
    cdef: bool = field(default=True)

    class Dict(TypedDict):
        all: bool
        cdef: bool


@dataclass
class EmbedSignatureDirectives(DataDict):
    enabled: bool = field(default=False)
    format: str = field(default="c")

    class Dict(TypedDict):
        enabled: bool
        format: str

@dataclass
class OverflowCheckDirectives(DataDict):
    enabled: bool = field(default=False)
    fold: bool = field(default=True)    

    class Dict(TypedDict):
        enabled: bool
        fold: bool


@dataclass
class InferTypesDirectives(DataDict):
    enabled: bool = field(default=True)
    verbose: bool = field(default=False)

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
    all: bool = field(default=False)
    undeclared: bool = field(default=False)
    unreachable: bool = field(default=False)
    maybe_uninitialized: bool = field(default=False)
    unused: bool = field(default=False)
    unused_arg: bool = field(default=False)
    unused_result: bool = False
    multiple_declarators: bool = field(default=False)
    deprecated_DEF: bool = field(default=False)
    deprecated_IF: bool = field(default=False)

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
    inline_defnode_calls: bool = field(default=True)    
    unpack_method_calls: bool = field(default=True)
    unpack_method_calls_in_pyinit: bool = field(default=True)
    use_switch: bool = field(default=True)
    # When True (default), DefNode wrappers that support fast-arg parsing still
    # generate a legacy dict-based ParseKeywords/RejectKeywords fallback for
    # non-fastcall runtimes.  When False, such wrappers rely solely on the
    # fast-arg path and do not emit the older dict-based parsing code at all.
    fast_arg_fallback: bool = field(default=False)

    class Dict(TypedDict):
        inline_defnode_calls: bool
        unpack_method_calls: bool
        unpack_method_calls_in_pyinit: bool
        use_switch: bool
        fast_arg_fallback: bool


@dataclass
class ControlFlowDirectives(DataDict):
    output: str = field(default="")
    annotate_defs: bool = field(default=False)
    dot_output: str = field(default="")     
    dot_annotate_defs: bool = field(default=False)

    class Dict(TypedDict):
        output: str
        annotate_defs: bool
        dot_output: str
        dot_annotate_defs: bool

@dataclass
class TestDirectives(DataDict):
    assert_path_exists: list[str] = field(default_factory=list)
    fail_if_path_exists: list[str] = field(default_factory=list)
    assert_c_code_has: list[str] = field(default_factory=list)
    fail_if_c_code_has: list[str] = field(default_factory=list) 

    class Dict(TypedDict):
        assert_path_exists: list[str]
        fail_if_path_exists: list[str]
        assert_c_code_has: list[str]
        fail_if_c_code_has: list[str]


@dataclass
class AutotestdictDirectiveScopes(DataDict):
    all: DirectiveScopeType = field(default="module")  
    cdef: DirectiveScopeType = field(default="module")

    class Dict(TypedDict):
        all: DirectiveScopeType
        cdef: DirectiveScopeType


@dataclass
class DataclassDirectiveScopes(DataDict):
    dataclass: DirectiveScopeType = field(default="class")
    field: DirectiveScopeType = field(default="class")

    class Dict(TypedDict):
        dataclass: DirectiveScopeType
        field: DirectiveScopeType

@dataclass
class ControlFlowDirectiveScopes(DataDict):
    output: DirectiveScopeType = field(default="module")    
    annotate_defs: DirectiveScopeType = field(default="module")
    dot_output: DirectiveScopeType = field(default="module")
    dot_annotate_defs: DirectiveScopeType = field(default="module")


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
DirectiveType = type | Callable[[str, Any], Any] | _DeferAnalysisOfArgumentsType | None
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
    # decorator-style directives (accepted but mainly handled at parse/transform time)
    cfunc: bool = False
    ccall: bool = False
    ufunc: bool = False
    inline: bool = False
    exceptval: Any | None = None
    returns: Any | None = None
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
    internal: bool = False
    collection_type: str | None = None
    total_ordering: bool = False
    c_compile_guard: str = ""
    set_initial_path: str | None = None  # SOURCEFILE or "/full/path/to/module"
    warn: WarnDirectives = field(default_factory=WarnDirectives)
    show_performance_hints: bool = True
    optimize: OptimizeDirectives = field(default_factory=OptimizeDirectives)
    remove_unreachable: bool = True
    control_flow: ControlFlowDirectives = field(default_factory=ControlFlowDirectives)
    test_assert_path_exists: list[str] = field(default_factory=list)
    test_fail_if_path_exists: list[str] = field(default_factory=list)
    test_assert_c_code_has: list[str] = field(default_factory=list)
    test_fail_if_c_code_has: list[str] = field(default_factory=list)
    test_body_needs_exception_handling: bool = False
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
                continue

            nested_value: dict[str, Any]
            if is_dataclass(value):
                nested_value = asdict(value)
            elif isinstance(value, Mapping):
                nested_value = dict(value)
            else:
                nested_value = {}
                for field_name in annotation.__annotations__:
                    if hasattr(value, field_name):
                        nested_value[field_name] = getattr(value, field_name)

            setattr(self, name, annotation(**nested_value))

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
        cfunc: bool
        ccall: bool
        ufunc: bool
        inline: bool
        exceptval: Any | None
        returns: Any | None
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
        internal: bool
        collection_type: str | None
        total_ordering: bool
        c_compile_guard: str
        set_initial_path: str | None
        warn: WarnDirectives.Dict
        show_performance_hints: bool
        optimize: OptimizeDirectives.Dict
        remove_unreachable: bool
        control_flow: ControlFlowDirectives.Dict
        test_assert_path_exists: list[str]
        test_fail_if_path_exists: list[str]
        test_assert_c_code_has: list[str]
        test_fail_if_c_code_has: list[str]
        test_body_needs_exception_handling: bool
        formal_grammar: bool

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
        cfunc: bool
        ccall: bool
        ufunc: bool
        inline: bool
        exceptval: Any | None
        returns: Any | None
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
        internal: bool
        collection_type: str | None
        total_ordering: bool
        c_compile_guard: str
        set_initial_path: str | None
        warn: WarnDirectives.Dict
        show_performance_hints: bool
        optimize: OptimizeDirectives.Dict
        remove_unreachable: bool
        control_flow: ControlFlowDirectives.Dict
        test_assert_path_exists: list[str]
        test_fail_if_path_exists: list[str]
        test_assert_c_code_has: list[str]
        test_fail_if_c_code_has: list[str]
        test_body_needs_exception_handling: bool
        formal_grammar: bool
        overload_dispatch: bool

class DirectivesDict(Directives.Dict):...
class DirectivesKwargs(Directives.Kwargs):...


def _copy_inherited_directives(
    outer_directives: Directives, **new_directives: Unpack[Directives.Kwargs]
) -> Directives:
    new_directives_out = Directives(**outer_directives)

    removal_keys: tuple[RemovalKey, ...] = (
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
    docstrings: bool

    #: Embed the source code position in the docstrings of functions and classes.
    embed_pos_in_docstring: bool

    # undocumented
    pre_import: str | None

    #: Decref global variables in each module on exit for garbage collection.
    #: 0: None, 1+: interned objects, 2+: cdef globals, 3+: types objects
    #: Mostly for reducing noise in Valgrind as it typically executes at process exit
    #: (when all memory will be reclaimed anyways).
    #: Note that directly or indirectly executed cleanup code that makes use of global
    #: variables or types may no longer be safe when enabling the respective level since
    #: there is no guaranteed order in which the (reference counted) objects will
    #: be cleaned up.  The order can change due to live references and reference cycles.
    generate_cleanup_code: bool | int

    #: Should tp_clear() set object fields to None instead of clearing them to NULL?
    clear_to_none: bool

    #: Generate an annotated HTML version of the input source files for
    #: debugging and optimisation purposes.
    #: This has the same effect as the ``annotate`` argument in :func:`cythonize`.
    annotate: bool

    # When annotating source files in HTML, include coverage information from
    # this file.
    annotate_coverage_xml: str | None

    #: This will abort the compilation on the first error occurred rather than trying
    #: to keep going and printing further error messages.
    fast_fail: bool

    #: Turn all warnings into errors.
    warning_errors: bool

    #: Make unknown names an error.  Python raises a NameError when
    #: encountering unknown names at runtime, whereas this option makes
    #: them a compile time error.  If you want full Python compatibility,
    #: you should disable this option and also 'cache_builtins'.
    error_on_unknown_names: bool

    #: Make uninitialized local variable reference a compile time error.
    #: Python raises UnboundLocalError at runtime, whereas this option makes
    #: them a compile time error. Note that this option affects only variables
    #: of "python object" type.
    error_on_uninitialized: bool

    #: This will convert statements of the form ``for i in range(...)``
    #: to ``for i from ...`` when ``i`` is a C integer type, and the direction
    #: (i.e. sign of step) can be determined.
    #: WARNING: This may change the semantics if the range causes assignment to
    #: i to overflow. Specifically, if this option is set, an error will be
    #: raised before the loop is entered, whereas without this option the loop
    #: will execute until an overflowing value is encountered.
    convert_range: bool

    #: Perform lookups on builtin names only once, at module initialisation
    #: time.  This will prevent the module from getting imported if a
    #: builtin name that it uses cannot be found during initialisation.
    #: Default is True.
    #: Note that some legacy builtins are automatically remapped
    #: from their Python 2 names to their Python 3 names by Cython
    #: when building in Python 3.x,
    #: so that they do not get in the way even if this option is enabled.
    cache_builtins: bool

    #: Generate branch prediction hints to speed up error handling etc.
    gcc_branch_hints: bool

    #: Enable this to allow one to write ``your_module.foo = ...`` to overwrite the
    #: definition if the cpdef function foo, at the cost of an extra dictionary
    #: lookup on every call.
    #: If this is false it generates only the Python wrapper and no override check.
    lookup_module_cpdef: bool

    #: Whether or not to embed the Python interpreter, for use in making a
    #: standalone executable or calling from external libraries.
    #: This will provide a C function which initialises the interpreter and
    #: executes the body of this module.
    #: See `this demo <https://github.com/cython/cython/tree/master/Demos/embed>`_
    #: for a concrete example.
    #: If true, the initialisation function is the C main() function, but
    #: this option can also be set to a non-empty string to provide a function name explicitly.
    #: Default is False.
    embed: bool | str | None

    #: Allows cimporting from a pyx file without a pxd file.
    cimport_from_pyx: bool

    #: Maximum number of dimensions for buffers -- set lower than number of
    #: dimensions in numpy, as
    #: slices are passed by value and involve a lot of copying.
    buffer_max_dims: int

    #: Number of function closure instances to keep in a freelist (0: no freelists)
    closure_freelist_size: int

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
        # Use evaluated type hints so that annotations from
        # ``from __future__ import annotations`` are resolved to real
        # runtime types (e.g. ``bool`` instead of the string ``\"bool\"``).
        self.directive_types = get_type_hints(Directives)
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
GLOBAL_DIRECTIVES = GlobalDirectives(
    docstrings=docstrings,
    embed_pos_in_docstring=embed_pos_in_docstring,
    pre_import=pre_import,
    generate_cleanup_code=generate_cleanup_code,
    clear_to_none=clear_to_none,
    annotate=annotate,
    annotate_coverage_xml=annotate_coverage_xml,
    fast_fail=fast_fail,
    warning_errors=warning_errors,
    error_on_unknown_names=error_on_unknown_names,
    error_on_uninitialized=error_on_uninitialized,
    convert_range=convert_range,
    cache_builtins=cache_builtins,
    gcc_branch_hints=gcc_branch_hints,
    lookup_module_cpdef=lookup_module_cpdef,
    embed=embed,
    cimport_from_pyx=cimport_from_pyx,
    buffer_max_dims=buffer_max_dims,
    closure_freelist_size=closure_freelist_size,
)

DIRECTIVE_DEFAULTS = Directives()
directive_types = GLOBAL_DIRECTIVES.directive_types
directive_scopes = GLOBAL_DIRECTIVES.directive_scopes


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

if __name__ == "__main__":
    d = AutotestdictDirectives()