from dataclasses import dataclass, field
from typing import (
    Any,
    Callable,
    Dict,
    List,
    Literal,
    Optional,
    Tuple,
    Type,
    Union,
    TypedDict,
    Unpack,
)

from Cython.DataDict import DataDict   
DirectiveScopeType = Literal["module", "function", "cclass", "class", "with statement"]

embedding_file_name: Optional[str]

@dataclass
class AutotestdictDirectives(DataDict):
    all: bool = field(default=True)
    cdef: bool = field(default=True)

    class Dict(TypedDict):
        all: bool
        cdef: bool

    class Kwargs(TypedDict, total=False):
        all: bool
        cdef: bool


class AutotestdictDirectivesDict(AutotestdictDirectives.Dict):...

class AutotestdictDirectivesKwargs(AutotestdictDirectives.Kwargs):...

@dataclass
class ControlFlowDirectives(DataDict):
    output: DirectiveScopeType = field(default="module")
    annotate_defs: DirectiveScopeType = field(default="module")
    dot_output: DirectiveScopeType = field(default="module")
    dot_annotate_defs: DirectiveScopeType = field(default="module")

    class Dict(TypedDict):
        output: DirectiveScopeType
        annotate_defs: DirectiveScopeType
        dot_output: DirectiveScopeType
        dot_annotate_defs: DirectiveScopeType

    class Kwargs(TypedDict, total=False):
        output: DirectiveScopeType
        annotate_defs: DirectiveScopeType
        dot_output: DirectiveScopeType
        dot_annotate_defs: DirectiveScopeType

class ControlFlowDirectivesDict(ControlFlowDirectives.Dict):...
class ControlFlowDirectivesKwargs(ControlFlowDirectives.Kwargs):...

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
        fail_if_c_code_has: List[str]

    class Kwargs(TypedDict, total=False):
        assert_path_exists: List[str]
        fail_if_path_exists: List[str]
        assert_c_code_has: List[str]
        fail_if_c_code_has: list[str]

class TestDirectivesDict(TestDirectives.Dict):...

class TestDirectivesKwargs(TestDirectives.Kwargs):...

@dataclass
class OptimizeDirectives(DataDict):
    inline_defnode_calls: bool = field(default=False)
    unpack_method_calls: bool = field(default=False)
    unpack_method_calls_in_pyinit: bool = field(default=False)  
    use_switch: bool = field(default=False)

    class Dict(TypedDict):
        inline_defnode_calls: bool
        unpack_method_calls: bool
        unpack_method_calls_in_pyinit: bool
        use_switch: bool        

    class Kwargs(TypedDict, total=False):
        inline_defnode_calls: bool
        unpack_method_calls: bool
        unpack_method_calls_in_pyinit: bool
        use_switch: bool

class OptimizeDirectivesDict(OptimizeDirectives.Dict):...
class OptimizeDirectivesKwargs(OptimizeDirectives.Kwargs):...

@dataclass
class FastGetattrDirectives(DataDict):
    fast: bool = field(default=True)
    
    class Dict(TypedDict):
        fast: bool

    class Kwargs(TypedDict, total=False):
        fast: bool

class FastGetattrDirectivesDict(FastGetattrDirectives.Dict):...

class FastGetattrDirectivesKwargs(FastGetattrDirectives.Kwargs):...

@dataclass
class EmbedSignatureDirectives(DataDict):
    enabled: bool = field(default=True)
    format: str = "python"

    class Dict(TypedDict):
        enabled: bool
        format: str

    class Kwargs(TypedDict, total=False):
        enabled: bool
        format: str


class EmbedSignatureDirectivesDict(EmbedSignatureDirectives.Dict):...
class EmbedSignatureDirectivesKwargs(EmbedSignatureDirectives.Kwargs):...

@dataclass
class Py2ImportDirectives(DataDict):
    py2: bool = field(default=False)

    class Dict(TypedDict):
        py2: bool

    class Kwargs(TypedDict, total=False):
        py2: bool

class Py2ImportDirectivesDict(Py2ImportDirectives.Dict):...

class Py2ImportDirectivesKwargs(Py2ImportDirectives.Kwargs):...

@dataclass
class WarnDirectives(DataDict):
    all: bool = field(default=True) 
    undeclared: bool = field(default=True)     
    unreachable: bool = field(default=True)
    maybe_uninitialized: bool = field(default=True)
    unused: bool = field(default=True)
    unused_arg: bool = field(default=True)
    unused_result: bool = field(default=True)
    multiple_declarators: bool = field(default=True)
    deprecated_DEF: bool = field(default=True)
    deprecated_IF: bool = field(default=True)

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

    class Kwargs(TypedDict, total=False):
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

class WarnDirectivesDict(WarnDirectives.Dict):...
class WarnDirectivesKwargs(WarnDirectives.Kwargs):...


@dataclass
class InferTypesDirectives(DataDict):
    enabled: bool = field(default=True)
    verbose: bool = False

    class Dict(TypedDict):
        enabled: bool
        verbose: bool

    class Kwargs(TypedDict, total=False):
        enabled: bool
        verbose: bool


class InferTypesDirectivesDict(InferTypesDirectives.Dict):...
class InferTypesDirectivesKwargs(InferTypesDirectives.Kwargs):...



@dataclass
class OverflowCheckDirectives(DataDict):
    enabled: bool = field(default=True)
    fold: bool = False

    class Dict(TypedDict):
        enabled: bool
        fold: bool

    class Kwargs(TypedDict, total=False):
        enabled: bool
        fold: bool

class OverflowCheckDirectivesDict(OverflowCheckDirectives.Dict):...
class OverflowCheckDirectivesKwargs(OverflowCheckDirectives.Kwargs):...

@dataclass
class Directives(DataDict):
    binding: bool = True
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
    ccomplex: bool = False
    callspec: str = ""  
    nogil: bool = False
    gil: bool = False
    with_gil: bool = False
    profile: bool = False
    linetrace: bool = False
    emit_code_comments: bool = True
    annotation_typing: bool = True
    cfunc: bool = False
    ccall: bool = False
    ufunc: bool = False
    inline: bool = False
    exceptval: Any | None = None
    returns: Any | None = None
    infer_types: InferTypesDirectives = field(default_factory=InferTypesDirectives)
    autotestdict: AutotestdictDirectives = field(default_factory=AutotestdictDirectives)
    language_level: int | str = 3
    fast_getattr: bool = False
    py2_import: bool = False
    preliminary_late_includes_cy28: bool = False
    iterable_coroutine: bool = False
    c_string_type: str = "bytes"
    c_string_encoding: str = ""
    type_version_tag: bool = True
    unraisable_tracebacks: bool = True
    old_style_globals: bool = False
    np_pythran: bool = False
    fast_gil: bool = False
    cpp_locals: bool = False
    legacy_implicit_noexcept: bool = False
    internal: bool = False
    collection_type: str | None = None
    total_ordering: bool = False
    c_compile_guard: str = ""
    set_initial_path: str | None = None
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



    class Dict(TypedDict, total=False):
        binding: bool
        boundscheck: bool
        nonecheck: bool
        initializedcheck: bool
        freethreading_compatible: bool
        subinterpreters_compatible: str
        embedsignature: EmbedSignatureDirectives
        auto_cpdef: bool
        auto_pickle: bool
        cdivision: bool
        cdivision_warnings: bool
        cpow: bool
        c_api_binop_methods: bool
        overflowcheck: OverflowCheckDirectives
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
        infer_types: InferTypesDirectives
        autotestdict: AutotestdictDirectives
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
        warn: WarnDirectivesDict
        show_performance_hints: bool
        optimize: OptimizeDirectives
        remove_unreachable: bool
        control_flow: ControlFlowDirectives
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
        embedsignature: EmbedSignatureDirectivesKwargs
        auto_cpdef: bool
        auto_pickle: bool
        cdivision: bool
        cdivision_warnings: bool
        cpow: bool
        c_api_binop_methods: bool
        overflowcheck: OverflowCheckDirectivesKwargs
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
        infer_types: InferTypesDirectivesKwargs
        autotestdict: AutotestdictDirectivesKwargs
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
        warn: WarnDirectivesKwargs
        show_performance_hints: bool
        optimize: OptimizeDirectivesKwargs
        remove_unreachable: bool
        control_flow: ControlFlowDirectivesKwargs
        test_assert_path_exists: list[str]
        test_fail_if_path_exists: list[str]
        test_assert_c_code_has: list[str]
        test_fail_if_c_code_has: list[str]
        test_body_needs_exception_handling: bool
        formal_grammar: bool
        overload_dispatch: bool 

class DirectivesDict(Directives.Dict):...

class DirectivesKwargs(Directives.Kwargs):...

class DirectiveDefaultsDict(DirectivesDict, total=True):
    ...


def _copy_inherited_directives(
    outer_directives: Directives, **new_directives: Unpack[Directives.Kwargs]
) -> Directives: ...


copy_inherited_directives = _copy_inherited_directives


def copy_for_internal(outer_directives: Directives) -> Directives: ...


_copy_for_internal = copy_for_internal


def one_of(*args: str, map: Optional[Dict[str, str]] = ...) -> Callable[[str, Any], Any]: ...


_normalise_common_encoding_name: Callable[[str], Optional[str]]

WithStatement = Literal["with statement"]

immediate_decorator_directives: set[str]

RemovalKey = Literal[
    "test_assert_path_exists",
    "test_fail_if_path_exists",
    "test_assert_c_code_has",
    "test_fail_if_c_code_has",
    "critical_section",
]


def _parse_compile_time_env(
    s: str, current_settings: Optional[Directives] = ...
) -> Directives: ...


class AutotestdictDirectiveScopes(DataDict):
    cdef: DirectiveScopeType
    all: DirectiveScopeType

    class Dict(TypedDict):
        cdef: DirectiveScopeType
        all: DirectiveScopeType

    class Kwargs(TypedDict, total=False):
        cdef: DirectiveScopeType
        all: DirectiveScopeType

class AutotestdictDirectiveScopesKwargs(AutotestdictDirectiveScopes.Kwargs):...
class AutotestdictDirectiveScopesDict(AutotestdictDirectiveScopes.Dict):...

class ControlFlowDirectiveScopes(DataDict):
    output: DirectiveScopeType
    annotate_defs: DirectiveScopeType
    dot_output: DirectiveScopeType
    dot_annotate_defs: DirectiveScopeType

    class Dict(TypedDict):
        output: DirectiveScopeType
        annotate_defs: DirectiveScopeType
        dot_output: DirectiveScopeType
        dot_annotate_defs: DirectiveScopeType

    class Kwargs(TypedDict, total=False):
        output: DirectiveScopeType
        annotate_defs: DirectiveScopeType
        dot_output: DirectiveScopeType
        dot_annotate_defs: DirectiveScopeType

class ControlFlowDirectiveScopesKwargs(ControlFlowDirectiveScopes.Kwargs):...
class ControlFlowDirectiveScopesDict(ControlFlowDirectiveScopes.Dict):...

class _DeferAnalysisOfArgumentsType:
    def __repr__(self) -> str: ...


DEFER_ANALYSIS_OF_ARGUMENTS: _DeferAnalysisOfArgumentsType

DirectiveType = Union[
    Type,
    Callable[[str, Any], Any],
    "_DeferAnalysisOfArgumentsType",
    None,
]


class ShouldBeFromDirective:
    known_directives: List["ShouldBeFromDirective"]

    def __init__(
        self, options_name: str, directive_name: Optional[str] = ..., disallow: bool = ...
    ) -> None: ...

    def __bool__(self) -> bool: ...
    def __nonzero__(self) -> bool: ...
    def __int__(self) -> int: ...
    def _bad_access(self) -> None: ...
    def __repr__(self) -> str: ...

class DataclassDirectiveScopes(DataDict):
    dataclass: DirectiveScopeType
    field: DirectiveScopeType
    
    class Dict(TypedDict):
        dataclass: DirectiveScopeType
        field: DirectiveScopeType

    class Kwargs(TypedDict, total=False):
        dataclass: DirectiveScopeType
        field: DirectiveScopeType

class DataclassDirectiveScopesKwargs(DataclassDirectiveScopes.Kwargs):...
class DataclassDirectiveScopesDict(DataclassDirectiveScopes.Dict):...


class DirectiveScopes(DataDict):
    auto_pickle: Tuple[DirectiveScopeType, ...]
    final: Tuple[DirectiveScopeType, ...]
    ccomplex: Tuple[DirectiveScopeType, ...]
    collection_type: Tuple[DirectiveScopeType, ...]
    nogil: Tuple[DirectiveScopeType, ...]
    gil: Tuple[DirectiveScopeType, ...]
    with_gil: Tuple[DirectiveScopeType, ...]
    critical_section: Tuple[DirectiveScopeType, ...]
    inline: Tuple[DirectiveScopeType, ...]
    cfunc: Tuple[DirectiveScopeType, ...]
    ccall: Tuple[DirectiveScopeType, ...]
    returns: Tuple[DirectiveScopeType, ...]
    exceptval: Tuple[DirectiveScopeType, ...]
    locals: Tuple[DirectiveScopeType, ...]
    staticmethod: Tuple[DirectiveScopeType, ...]
    no_gc_clear: Tuple[DirectiveScopeType, ...]
    no_gc: Tuple[DirectiveScopeType, ...]
    internal: Tuple[DirectiveScopeType, ...]
    cclass: Tuple[DirectiveScopeType, ...]
    autotestdict: AutotestdictDirectiveScopes
    set_initial_path: Tuple[DirectiveScopeType, ...]
    test_assert_path_exists: Tuple[DirectiveScopeType, ...]
    test_fail_if_path_exists: Tuple[DirectiveScopeType, ...]
    test_assert_c_code_has: Tuple[DirectiveScopeType, ...]
    test_fail_if_c_code_has: Tuple[DirectiveScopeType, ...]
    freelist: Tuple[DirectiveScopeType, ...]
    formal_grammar: Tuple[DirectiveScopeType, ...]
    emit_code_comments: Tuple[DirectiveScopeType, ...]
    c_string_type: Tuple[DirectiveScopeType, ...]
    c_string_encoding: Tuple[DirectiveScopeType, ...]
    type_version_tag: Tuple[DirectiveScopeType, ...]
    language_level: Tuple[DirectiveScopeType, ...]
    old_style_globals: Tuple[DirectiveScopeType, ...]
    np_pythran: Tuple[DirectiveScopeType, ...]
    preliminary_late_includes_cy28: Tuple[DirectiveScopeType, ...]
    fast_gil: Tuple[DirectiveScopeType, ...]
    iterable_coroutine: Tuple[DirectiveScopeType, ...]
    trashcan: Tuple[DirectiveScopeType, ...]
    total_ordering: Tuple[DirectiveScopeType, ...]
    dataclasses: DataclassDirectiveScopes
    cpp_locals: Tuple[DirectiveScopeType, ...]
    ufunc: Tuple[DirectiveScopeType, ...]
    legacy_implicit_noexcept: Tuple[DirectiveScopeType, ...]
    c_compile_guard: Tuple[DirectiveScopeType, ...]
    control_flow: ControlFlowDirectiveScopes
    freethreading_compatible: Tuple[DirectiveScopeType, ...]
    subinterpreters_compatible: Tuple[DirectiveScopeType, ...]

    class Dict(TypedDict):
        auto_pickle: Tuple[DirectiveScopeType, ...]
        final: Tuple[DirectiveScopeType, ...]
        ccomplex: Tuple[DirectiveScopeType, ...]
        collection_type: Tuple[DirectiveScopeType, ...]
        nogil: Tuple[DirectiveScopeType, ...]
        gil: Tuple[DirectiveScopeType, ...]
        with_gil: Tuple[DirectiveScopeType, ...]
        critical_section: Tuple[DirectiveScopeType, ...]
        inline: Tuple[DirectiveScopeType, ...]
        cfunc: Tuple[DirectiveScopeType, ...]
        ccall: Tuple[DirectiveScopeType, ...]
        returns: Tuple[DirectiveScopeType, ...]
        exceptval: Tuple[DirectiveScopeType, ...]
        locals: Tuple[DirectiveScopeType, ...]
        staticmethod: Tuple[DirectiveScopeType, ...]
        no_gc_clear: Tuple[DirectiveScopeType, ...]
        no_gc: Tuple[DirectiveScopeType, ...]
        internal: Tuple[DirectiveScopeType, ...]
        cclass: Tuple[DirectiveScopeType, ...]
        autotestdict: AutotestdictDirectiveScopes.Dict
        set_initial_path: Tuple[DirectiveScopeType, ...]
        test_assert_path_exists: Tuple[DirectiveScopeType, ...]
        test_fail_if_path_exists: Tuple[DirectiveScopeType, ...]
        test_assert_c_code_has: Tuple[DirectiveScopeType, ...]
        test_fail_if_c_code_has: Tuple[DirectiveScopeType, ...]
        freelist: Tuple[DirectiveScopeType, ...]
        formal_grammar: Tuple[DirectiveScopeType, ...]
        emit_code_comments: Tuple[DirectiveScopeType, ...]
        c_string_type: Tuple[DirectiveScopeType, ...]
        c_string_encoding: Tuple[DirectiveScopeType, ...]
        type_version_tag: Tuple[DirectiveScopeType, ...]
        language_level: Tuple[DirectiveScopeType, ...]
        old_style_globals: Tuple[DirectiveScopeType, ...]
        np_pythran: Tuple[DirectiveScopeType, ...]
        preliminary_late_includes_cy28: Tuple[DirectiveScopeType, ...]
        fast_gil: Tuple[DirectiveScopeType, ...]
        iterable_coroutine: Tuple[DirectiveScopeType, ...]
        trashcan: Tuple[DirectiveScopeType, ...]
        total_ordering: Tuple[DirectiveScopeType, ...]
        dataclasses: DataclassDirectiveScopes.Dict
        cpp_locals: Tuple[DirectiveScopeType, ...]
        ufunc: Tuple[DirectiveScopeType, ...]
        legacy_implicit_noexcept: Tuple[DirectiveScopeType, ...]
        c_compile_guard: Tuple[DirectiveScopeType, ...]
        control_flow: ControlFlowDirectiveScopes.Dict
        freethreading_compatible: Tuple[DirectiveScopeType, ...]
        subinterpreters_compatible: Tuple[DirectiveScopeType, ...]

    class Kwargs(TypedDict, total=False):
        auto_pickle: Tuple[DirectiveScopeType, ...]
        final: Tuple[DirectiveScopeType, ...]
        ccomplex: Tuple[DirectiveScopeType, ...]
        collection_type: Tuple[DirectiveScopeType, ...]
        nogil: Tuple[DirectiveScopeType, ...]
        gil: Tuple[DirectiveScopeType, ...]
        with_gil: Tuple[DirectiveScopeType, ...]
        critical_section: Tuple[DirectiveScopeType, ...]
        inline: Tuple[DirectiveScopeType, ...]
        cfunc: Tuple[DirectiveScopeType, ...]
        ccall: Tuple[DirectiveScopeType, ...]
        returns: Tuple[DirectiveScopeType, ...]
        exceptval: Tuple[DirectiveScopeType, ...]
        locals: Tuple[DirectiveScopeType, ...]
        staticmethod: Tuple[DirectiveScopeType, ...]
        no_gc_clear: Tuple[DirectiveScopeType, ...]
        no_gc: Tuple[DirectiveScopeType, ...]
        internal: Tuple[DirectiveScopeType, ...]
        cclass: Tuple[DirectiveScopeType, ...]
        autotestdict: AutotestdictDirectiveScopes.Kwargs
        set_initial_path: Tuple[DirectiveScopeType, ...]
        test_assert_path_exists: Tuple[DirectiveScopeType, ...]
        test_fail_if_path_exists: Tuple[DirectiveScopeType, ...]
        test_assert_c_code_has: Tuple[DirectiveScopeType, ...]
        test_fail_if_c_code_has: Tuple[DirectiveScopeType, ...]
        freelist: Tuple[DirectiveScopeType, ...]
        formal_grammar: Tuple[DirectiveScopeType, ...]
        emit_code_comments: Tuple[DirectiveScopeType, ...]
        c_string_type: Tuple[DirectiveScopeType, ...]
        c_string_encoding: Tuple[DirectiveScopeType, ...]
        type_version_tag: Tuple[DirectiveScopeType, ...]
        language_level: Tuple[DirectiveScopeType, ...]
        old_style_globals: Tuple[DirectiveScopeType, ...]
        np_pythran: Tuple[DirectiveScopeType, ...]
        preliminary_late_includes_cy28: Tuple[DirectiveScopeType, ...]
        fast_gil: Tuple[DirectiveScopeType, ...]
        iterable_coroutine: Tuple[DirectiveScopeType, ...]
        trashcan: Tuple[DirectiveScopeType, ...]
        total_ordering: Tuple[DirectiveScopeType, ...]
        dataclasses: DataclassDirectiveScopes.Kwargs
        cpp_locals: Tuple[DirectiveScopeType, ...]
        ufunc: Tuple[DirectiveScopeType, ...]
        legacy_implicit_noexcept: Tuple[DirectiveScopeType, ...]
        c_compile_guard: Tuple[DirectiveScopeType, ...]
        control_flow: ControlFlowDirectiveScopes.Kwargs
        freethreading_compatible: Tuple[DirectiveScopeType, ...]
        subinterpreters_compatible: Tuple[DirectiveScopeType, ...]


class DirectiveScopesDict(DirectiveScopes.Dict): ...
class DirectiveScopesKwargs(DirectiveScopes.Kwargs): ...

# Extra warning directives
extra_warnings = {
    "warn.maybe_uninitialized": True,
    "warn.unreachable": True,
    "warn.unused": True,
}


class GlobalDirectives(DataDict):
    docstrings: bool
    embed_pos_in_docstring: bool
    pre_import: Optional[str]
    generate_cleanup_code: Union[bool, int]
    clear_to_none: bool
    annotate: bool
    annotate_coverage_xml: Optional[str]
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
    old_style_globals: bool
    capi_reexport_cincludes: bool

    def __post_init__(self) -> None: ...


# Create a global wrapper (no overrides) for consumers that expect an object.
GLOBAL_DIRECTIVES: GlobalDirectives

DIRECTIVE_DEFAULTS: Directives


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


