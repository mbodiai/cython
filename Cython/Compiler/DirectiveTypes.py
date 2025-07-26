"""
Type definitions for Cython compiler directives.

This module contains common type definitions used for directives across Cython,
reducing duplication and providing clear, reusable type annotations.
"""

from typing import Any, Callable, Dict, List, Literal, Optional, Type, TypeVar, Union, TypedDict

# Define string constants for directive scopes
MODULE_SCOPE = "module"
FUNCTION_SCOPE = "function" 
CLASS_SCOPE = "class"
WITH_STATEMENT_SCOPE = "with_statement"
CCLASS_SCOPE = "cclass"

# Define a TypeVar for validators
T = TypeVar("T")

# Types for directive values
DirectiveValue = Union[bool, int, str, None, Dict[str, Any], List[str]]

# Type for directive validators
ValidatorFunc = Callable[[str, Any], Any]

# Base TypedDict for directives
class BaseDirectiveDict(TypedDict, total=False):
    """Base dictionary type for directives"""
    pass


# Define directive types
class DirectiveScopeDict(BaseDirectiveDict):
    """Dict for directive scopes with test fields."""
    test_assert_path_exists: List[str]
    test_fail_if_path_exists: List[str]
    test_assert_c_code_has: List[str]
    test_fail_if_c_code_has: List[str]
    critical_section: Union[bool, str]


class DirectiveScopeKwargs(DirectiveScopeDict, total=False):
    """Dict for directive scopes with optional fields."""
    language_level: Literal["2", "3", 2, 3]
    auto_pickle: Optional[bool]
    locals: Dict[str, Any]
    final: Optional[bool]
    collection_type: Optional[str]
    nogil: Optional[bool]
    gil: Optional[bool]
    with_gil: Optional[bool]
    internal: Optional[bool]
    infer_types: Optional[bool]
    binding: Optional[bool]
    cpow: Optional[bool]
    inline: Optional[bool]
    staticmethod: Optional[bool]
    cclass: Optional[Union[bool, str]]
    no_gc_clear: Optional[Union[bool, str]]
    no_gc: Optional[Union[bool, str]]
    boundscheck: Optional[bool]
    nonecheck: Optional[bool]
    initializedcheck: Optional[bool]
    freethreading_compatible: Optional[bool]
    embedsignature: Optional[bool]
    embedsignature_format: Optional[str]
    auto_cpdef: Optional[bool]
    cdivision: Optional[bool]
    cdivision_warnings: Optional[bool]
    c_api_binop_methods: Optional[bool]
    overflowcheck: Optional[bool]
    overflowcheck_fold: Optional[bool]
    emit_code_comments: Optional[bool]
    annotation_typing: Optional[bool]
    infer_types_verbose: Optional[bool]
    autotestdict_cdef: Optional[bool]
    autotestdict_all: Optional[bool]
    embedsignature__dot__format: Optional[str]
    returns: Optional[Type[Any]]
    exceptval: Optional[Type[Any]]
    set_initial_path: Optional[str]
    freelist: Optional[int]
    c_string_type: Optional[str]
    c_string_encoding: Optional[str]
    trashcan: Optional[bool]
    total_ordering: Optional[bool]
    dataclasses__dot__dataclass: Optional[Union[bool, str]]
    dataclasses__dot__field: Optional[Union[bool, str]]
    subinterpreters_compatible: Optional[str]
    control_flow__dot__output: Optional[str]
    warn__dot__deprecated__dot__DEF: Optional[bool]
    warn__dot__deprecated__dot__IF: Optional[Union[bool, str]]
    show_performance_hints: Optional[Union[bool, str]]
    optimize__dot__inline_defnode_calls: Optional[Union[bool, str]]
    optimize__dot__unpack_method_calls: Optional[Union[bool, str]]
    optimize__dot__unpack_method_calls_in_pyinit: Optional[Union[bool, str]]
    optimize__dot__use_switch: Optional[bool]
    remove_unreachable: Optional[Union[bool, str]]
    c_compile_guard: Optional[str]
    always_allow_keywords: Optional[Union[bool, str]]
    allow_none_for_extension_args: Optional[Union[bool, str]]
    wraparound: Optional[Union[bool, str]]
    ccomplex: Optional[Union[bool, str]]
    callspec: Optional[str]
    check: Optional[Union[bool, str]]
    warn: Optional[Union[bool, str]]
    warn_undeclared: Optional[bool]
    warn_unreachable: Optional[bool]
    warn_maybe_uninitialized: Optional[bool]
    warn_unused: Optional[bool]
    warn_unused_arg: Optional[bool]
    warn_unused_result: Optional[bool]
    profile: Optional[bool]
    linetrace: Optional[bool]
    py2_import: Optional[Union[bool, str]]
    preliminary_late_includes_cy28: Optional[Union[bool, str]]
    iterable_coroutine: Optional[Union[bool, str]]
    type_version_tag: Optional[Union[bool, str]]
    unraisable_tracebacks: Optional[Union[bool, str]]
    old_style_globals: Optional[Union[bool, str]]
    np_pythran: Optional[Union[bool, str]]
    fast_gil: Optional[Union[bool, str]]
    cpp_locals: Optional[Union[bool, str]]
    legacy_implicit_noexcept: Optional[Union[bool, str]]
    control_flow__dot__annotate_defs: Optional[Union[bool, str]]
    overflowcheck__dot__fold: Optional[Union[bool, str]]
    infer_types__dot__verbose: Optional[Union[bool, str]]
    autotestdict: Optional[Union[bool, str]]
    autotestdict__dot__cdef: Optional[Union[bool, str]]
    autotestdict__dot__all: Optional[Union[bool, str]]
    fast_getattr: Optional[Union[bool, str]]
    warn_multiple_declarators: Optional[Union[bool, str]]
    formal_grammar: Optional[Union[bool, str]]


class ReducedDirectiveScopeKwargs(BaseDirectiveDict, total=False):
    """Dict for directive scopes with required fields."""
    # Same fields as DirectiveScopeKwargs but without test fields
    language_level: Literal["2", "3", 2, 3]
    auto_pickle: Optional[bool]
    locals: Dict[str, Any]
    final: Optional[bool]
    collection_type: Optional[str]
    nogil: Optional[bool]
    gil: Optional[bool]
    with_gil: Optional[bool]
    internal: Optional[bool]
    infer_types: Optional[bool]
    binding: Optional[bool]
    cpow: Optional[bool]
    inline: Optional[bool]
    staticmethod: Optional[bool]
    cclass: Optional[Union[bool, str]]
    no_gc_clear: Optional[Union[bool, str]]
    no_gc: Optional[Union[bool, str]]
    boundscheck: Optional[bool]
    nonecheck: Optional[bool]
    initializedcheck: Optional[bool]
    freethreading_compatible: Optional[bool]
    embedsignature: Optional[bool]
    embedsignature_format: Optional[str]
    auto_cpdef: Optional[bool]
    cdivision: Optional[bool]
    cdivision_warnings: Optional[bool]
    c_api_binop_methods: Optional[bool]
    overflowcheck: Optional[bool]
    overflowcheck_fold: Optional[bool]
    emit_code_comments: Optional[bool]
    annotation_typing: Optional[bool]
    infer_types_verbose: Optional[bool]
    autotestdict_cdef: Optional[bool]
    autotestdict_all: Optional[bool]
    embedsignature__dot__format: Optional[str]
    returns: Optional[Type[Any]]
    exceptval: Optional[Type[Any]]
    set_initial_path: Optional[str]
    freelist: Optional[int]
    c_string_type: Optional[str]
    c_string_encoding: Optional[str]
    trashcan: Optional[bool]
    total_ordering: Optional[bool]
    dataclasses__dot__dataclass: Optional[Union[bool, str]]
    dataclasses__dot__field: Optional[Union[bool, str]]
    subinterpreters_compatible: Optional[str]
    warn__dot__deprecated__dot__DEF: Optional[bool]
    warn__dot__deprecated__dot__IF: Optional[Union[bool, str]]
    show_performance_hints: Optional[Union[bool, str]]
    optimize__dot__inline_defnode_calls: Optional[Union[bool, str]]
    optimize__dot__unpack_method_calls: Optional[Union[bool, str]]
    optimize__dot__unpack_method_calls_in_pyinit: Optional[Union[bool, str]]
    optimize__dot__use_switch: Optional[bool]
    remove_unreachable: Optional[Union[bool, str]]
    c_compile_guard: Optional[str]
    always_allow_keywords: Optional[Union[bool, str]]
    allow_none_for_extension_args: Optional[Union[bool, str]]
    wraparound: Optional[Union[bool, str]]
    ccomplex: Optional[Union[bool, str]]
    callspec: Optional[str]
    check: Optional[Union[bool, str]]
    warn: Optional[Union[bool, str]]
    warn_undeclared: Optional[bool]
    warn_unreachable: Optional[bool]
    warn_maybe_uninitialized: Optional[bool]
    warn_unused: Optional[bool]
    warn_unused_arg: Optional[bool]
    warn_unused_result: Optional[bool]
    profile: Optional[bool]
    linetrace: Optional[bool]
    py2_import: Optional[Union[bool, str]]
    preliminary_late_includes_cy28: Optional[Union[bool, str]]
    iterable_coroutine: Optional[Union[bool, str]]
    c_string_type: Optional[str]
    c_string_encoding: Optional[str]
    type_version_tag: Optional[Union[bool, str]]
    unraisable_tracebacks: Optional[Union[bool, str]]
    old_style_globals: Optional[Union[bool, str]]
    np_pythran: Optional[Union[bool, str]]
    fast_gil: Optional[Union[bool, str]]
    cpp_locals: Optional[Union[bool, str]]
    legacy_implicit_noexcept: Optional[Union[bool, str]]


# Define node directive types 
class NodeDirectiveScopeDict(TypedDict, total=False):
    """TypedDict for node directive scopes with optional fields."""
    auto_pickle: bool
    final: bool
    ccomplex: bool
    collection_type: str
    nogil: bool
    gil: bool
    with_gil: bool
    critical_section: bool
    inline: bool
    cfunc: bool
    ccall: bool
    returns: Optional[Type[Any]]
    exceptval: Optional[Type[Any]]
    locals: Dict[str, Any]


# Class for directive scope mapping
class DirectiveScopeMap(Dict[str, List[str]]):
    """Dict type for mapping directives to allowed scopes."""
    pass


# CompilationOptions types
class CompilationOptionsDict(TypedDict, total=False):
    """Dict for CompilationOptions values."""
    cimport_from_pyx: bool
    language_level: Optional[int]
    docstrings: bool
    cache: bool
    annotate: Optional[str]
    emit_linenums: bool
    c_line_in_traceback: bool
    gdb_debug: bool
    output_dir: Optional[str]
    generate_cleanup_code: Optional[int]
    generate_pxi: bool
    optimize: Dict[str, Any]
    compiler_directives: Dict[str, Any]
    embed_pos_in_docstring: bool
    generate_pxd_c_file_for_shared_module: bool
    separate_source_files: bool
    fast_fail: bool
    warning_errors: bool
    extra_warnings: List[str]
    autotestdict: bool
    capi_reexport_cincludes: bool
    common_utility_include_dir: Optional[str]
    module_name: Optional[str]
    timestamps: Dict[str, float]
    verbose: int
    output_file: Optional[str]
    depfile: bool
    cplus: bool
    working_path: Optional[str]
    np_pythran: bool
    compile_time_env: Dict[str, Any]
    legacy_implicit_noexcept: Optional[bool]
    shared_c_file_path: Optional[str]
    shared_utility_qualified_name: Optional[str]
    show_version: bool
    use_listing_file: bool
    include_path: List[str]
    initial_file: Optional[str]
    annotate_coverage_xml: Optional[str]
    error_on_unknown_names: bool
    error_on_uninitialized: bool
    convert_range: bool
    embedded_metadata: Dict[str, Any]


# TypedDict for CompilationOptions kwargs
class CompilationOptionsKwargs(CompilationOptionsDict, total=False):
    """Dict for CompilationOptions initialization kwargs."""
    pass


# Sentinel class for directives that need deferred analysis
class DeferAnalysisType:
    """Sentinel class for directives that need deferred analysis."""
    pass


# Create singleton instance
DEFER_ANALYSIS = DeferAnalysisType() 