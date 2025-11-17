from typing import Any, List, TypedDict
from dataclasses import dataclass
from Cython.Compiler.Directives import DirectivesDict, Directives, DirectivesKwargs
from Cython.DataDict import DataDict

@dataclass
class CompilationOptions(DataDict):
    include_path: List[str]
    output_file: str | None
    show_version: bool
    use_listing_file: bool
    errors_to_stderr: bool
    cplus: bool
    depfile: bool | None
    make_depfile: bool
    annotate: bool | None
    annotate_no_c_link: bool
    annotate_coverage_xml: str | None
    generate_pxi: bool
    capi_reexport_cincludes: bool
    working_path: str
    timestamps: Any | None
    verbose: int
    quiet: bool
    compiler_directives: Directives|DirectivesDict|DirectivesKwargs
    embedded_metadata: dict[str, object]
    evaluate_tree_assertions: bool
    emit_linenums: bool
    relative_path_in_code_position_comments: bool
    embedding_file_name: str | None
    c_line_in_traceback: bool
    language_level: Any | None
    formal_grammar: bool
    gdb_debug: bool
    compile_time_env: dict[str, object]
    module_name: str | None
    common_utility_include_dir: str | None
    output_dir: str | None
    build_dir: str | None
    cache: Any | None
    create_extension: Any | None
    np_pythran: bool
    legacy_implicit_noexcept: bool
    shared_utility_qualified_name: str | None
    docstrings: bool
    embed_pos_in_docstring: bool
    pre_import: Any | None
    generate_cleanup_code: bool | int
    clear_to_none: bool
    fast_fail: bool
    warning_errors: bool
    error_on_unknown_names: bool
    error_on_uninitialized: bool
    convert_range: bool
    cache_builtins: bool
    gcc_branch_hints: bool
    lookup_module_cpdef: bool
    embed: bool | str | None
    cimport_from_pyx: bool
    buffer_max_dims: int
    closure_freelist_size: int

    def copy(self) -> "CompilationOptions": ...


    class Dict(TypedDict):
        include_path: List[str]
        output_file: str | None
        show_version: bool
        use_listing_file: bool
        errors_to_stderr: bool
        cplus: bool
        depfile: bool | None
        make_depfile: bool
        annotate: bool | None
        annotate_no_c_link: bool
        annotate_coverage_xml: str | None
        generate_pxi: bool
        capi_reexport_cincludes: bool
        working_path: str
        timestamps: Any | None
        verbose: int
        quiet: bool
        compiler_directives: DirectivesDict
        embedded_metadata: dict[str, object]
        evaluate_tree_assertions: bool
        emit_linenums: bool
        relative_path_in_code_position_comments: bool
        embedding_file_name: str | None
        c_line_in_traceback: bool
        language_level: Any | None
        formal_grammar: bool
        gdb_debug: bool
        compile_time_env: dict[str, object]
        module_name: str | None
        common_utility_include_dir: str | None
        output_dir: str | None
        build_dir: str | None
        cache: Any | None
        create_extension: Any | None
        np_pythran: bool
        legacy_implicit_noexcept: bool
        shared_utility_qualified_name: str | None
        docstrings: bool
        embed_pos_in_docstring: bool
        pre_import: Any | None
        generate_cleanup_code: bool | int
        clear_to_none: bool
        fast_fail: bool
        warning_errors: bool
        error_on_unknown_names: bool
        error_on_uninitialized: bool
        convert_range: bool
        cache_builtins: bool
        gcc_branch_hints: bool
        lookup_module_cpdef: bool
        embed: bool | str | None
        cimport_from_pyx: bool
        buffer_max_dims: int
        closure_freelist_size: int

    class Kwargs(TypedDict, total=False):
        include_path: list[str]
        output_file: str | None
        show_version: bool
        use_listing_file: bool
        errors_to_stderr: bool
        cplus: bool
        depfile: bool | None
        make_depfile: bool
        annotate: bool | None
        annotate_no_c_link: bool
        annotate_coverage_xml: str | None
        generate_pxi: bool
        capi_reexport_cincludes: bool
        working_path: str
        timestamps: Any | None
        verbose: int
        quiet: bool
        compiler_directives: DirectivesDict
        embedded_metadata: dict[str, object]
        evaluate_tree_assertions: bool
        emit_linenums: bool
        relative_path_in_code_position_comments: bool
        embedding_file_name: str | None
        c_line_in_traceback: bool
        language_level: Any | None
        formal_grammar: bool
        gdb_debug: bool
        compile_time_env: dict[str, object]
        module_name: str | None
        common_utility_include_dir: str | None
        output_dir: str | None
        build_dir: str | None
        cache: Any | None
        create_extension: Any | None
        np_pythran: bool
        legacy_implicit_noexcept: bool
        shared_utility_qualified_name: str | None
        docstrings: bool
        embed_pos_in_docstring: bool
        pre_import: Any | None
        generate_cleanup_code: bool | int
        clear_to_none: bool
        fast_fail: bool
        warning_errors: bool
        error_on_unknown_names: bool
        error_on_uninitialized: bool
        convert_range: bool
        cache_builtins: bool
        gcc_branch_hints: bool
        lookup_module_cpdef: bool
        embed: bool | str | None
        cimport_from_pyx: bool
        buffer_max_dims: int
        closure_freelist_size: int
        
class CompilationOptionsDict(CompilationOptions.Dict):...
class CompilationOptionsKwargs(CompilationOptions.Kwargs):...
DEFAULT_COMPILATION_OPTIONS: CompilationOptions
directive_types: dict[str, Any]
docstrings: bool
annotate: bool | None
annotate_coverage_xml: str | None
annotate_no_c_link: bool
generate_pxi: bool
capi_reexport_cincludes: bool
working_path: str
timestamps: Any | None
verbose: int
quiet: bool
compiler_directives: Directives
embedded_metadata: dict[str, object]
evaluate_tree_assertions: bool
emit_linenums: bool
relative_path_in_code_position_comments: bool
embedding_file_name: str | None
c_line_in_traceback: bool
language_level: Any | None
formal_grammar: bool
gdb_debug: bool
compile_time_env: dict[str, object]
module_name: str | None
common_utility_include_dir: str | None
output_dir: str | None
build_dir: str | None
cache: Any | None
create_extension: Any | None
np_pythran: bool
legacy_implicit_noexcept: bool
shared_utility_qualified_name: str | None
error_on_unknown_names: bool