#
#  Cython - Compilation-wide options and pragma declarations
#
from __future__ import annotations

import ast
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Literal
from typing_extensions import TypedDict
from contextlib import suppress
import Cython.Compiler.Directives
from Cython.Abstract import MatchAST, func_def
from Cython.DataDict import DataDict



# ------------------------------------------------------------------------
# CompilationOptions are constructed from user input and are the `option`
#  object passed throughout the compilation pipeline.
# ------------------------------------------------------------------------
CYTHON_COMMON_UTILITY_INCLUDE_DIR = str(Path(__file__).parent.parent / "Common" / "Include")


def parse_option(arg: str) -> Any:
    arg = arg.strip().lstrip("-").lower().capitalize()
    with suppress(ValueError):
        return eval(arg)
    return arg


Directives = Cython.Compiler.Directives.Directives
DirectivesType = (
    Cython.Compiler.Directives.Directives
    | Cython.Compiler.Directives.DirectivesDict
    | Cython.Compiler.Directives.DirectivesKwargs
)
@dataclass
class CompilationOptions(DataDict):
    """Options for Cython compilation, used throughout the compilation pipeline.

    See ``DEFAULT_COMPILATION_OPTIONS`` at the end of this module for a list of all
    possible options and CmdLine.usage / CmdLine.parse_command_line() for their meaning.
    """

    # Fields defined based on old CompilationOptionKwargs and default_options
    include_path: list[str] = field(default_factory=lambda: ["."])
    shared_c_file_path: str | None = None
    output_file: str = ""
    show_version: bool = False
    use_listing_file: bool = False
    errors_to_stderr: bool = True
    cplus: bool = False
    depfile: bool | None = None
    make_depfile: bool = False
    annotate: bool | None = None
    annotate_no_c_link: bool = False
    annotate_coverage_xml: str | None = None
    generate_pxi: bool = False
    capi_reexport_cincludes: bool = False
    working_path: str = ""
    timestamps: Any | None = None
    verbose: int = 0
    quiet: bool = False
    compiler_directives: DirectivesType = field(default_factory=Cython.Compiler.Directives.Directives)
    embedded_metadata: dict[str, Any] = field(default_factory=dict)
    embedding_file_name: str | None = None
    embedding_file_timestamp: int | None = None
    evaluate_tree_assertions: bool = False
    emit_linenums: bool = False
    relative_path_in_code_position_comments: bool = True
    c_line_in_traceback: bool = True
    language_level: Any | None = None
    formal_grammar: bool = False
    gdb_debug: bool = False
    compile_time_env: dict[str, Any] = field(default_factory=dict)
    module_name: str | None = None
    common_utility_include_dir: str | None = CYTHON_COMMON_UTILITY_INCLUDE_DIR
    output_dir: str | None = None
    build_dir: str | None = None
    cache: Any | None = None
    cache_size: int | None = None
    create_extension: Any | None = None
    np_pythran: bool = False
    legacy_implicit_noexcept: bool = False
    shared_utility_qualified_name: str | None = None
    old_style_globals: bool = False

    # Options previously defined as globals
    docstrings: bool = True
    extra_warnings: dict[str, Any] = field(default_factory=lambda: {
        "warn.maybe_uninitialized": True,
        "warn.unreachable": True,
        "warn.unused": True,
    })
    embed_pos_in_docstring: bool = False
    pre_import: Any | None = None
    generate_cleanup_code: bool | int = False
    clear_to_none: bool = True
    fast_fail: bool = False
    warning_errors: bool = False
    error_on_unknown_names: bool = True
    error_on_uninitialized: bool = True
    convert_range: bool = True
    cache_builtins: bool = True
    gcc_branch_hints: bool = True
    lookup_module_cpdef: bool = False
    embed: bool | str | None = None
    cimport_from_pyx: bool = False
    buffer_max_dims: int = 8
    closure_freelist_size: int = 8

    def __post_init__(self) -> None:
        """Validate options and set defaults for compiler directives."""
        # Check for unknown directives
        directive_defaults = Cython.Compiler.Directives.Directives()
        unknown_directives = set(self.compiler_directives.keys()) - set(directive_defaults.keys())
        if unknown_directives:
            message = f"got unknown compiler directive{'' if len(unknown_directives) > 1 else 's'}: {', '.join(map(str, unknown_directives))}"
            raise ValueError(message)

        # Handle np_pythran forcing cplus
        if self.compiler_directives.get("np_pythran", False) and not self.cplus:
            import warnings

            warnings.warn("C++ mode forced when in Pythran mode!")
            self.cplus = True
        self.compiler_directives =  Cython.Compiler.Directives.Directives(**self.compiler_directives)

    def configure_language_defaults(self, source_extension: str) -> None:
        """Configure language level defaults based on source extension and directives.

        Args:
            source_extension: The file extension of the source file
        """
        # Direct access to dataclass fields
        directives = self.compiler_directives.copy()
        # Python files always imply binding=True unless explicitly set to False
        if source_extension == "py" and directives.get("binding") is not False:
            self.compiler_directives["binding"] = True

    def get_fingerprint(self) -> str:
        """Generate a fingerprint string containing all options relevant for cache invalidation.

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
        return hashlib.md5(str(parts).encode("utf-8"), usedforsecurity=False).hexdigest()

    def get_embedded_main_c_function(self) -> str | None:
        """Get the name of the embedded main C function if embedding is enabled.

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
        raise ValueError(f"Invalid embed value: {embed}. Source not available.")

    @classmethod
    def parse_args(cls, args: tuple[str, ...]) -> "CompilationOptions":
        arglist = []
        kwargs = {}
        for arg in args:
            if "=" in arg:
                key, value = arg.split("=", 1)
                kwargs[key] = parse_option(value)
            else:
                arglist.append(parse_option(arg))
        return cls(*arglist, **kwargs)
    class Dict(TypedDict):
        include_path: list[str]
        shared_c_file_path: str | None
        output_file: str
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
        compiler_directives: Cython.Compiler.Directives.DirectivesDict
        embedded_metadata: dict[str, Any]
        embedding_file_name: str | None
        embedding_file_timestamp: int | None
        evaluate_tree_assertions: bool
        emit_linenums: bool
        relative_path_in_code_position_comments: bool
        c_line_in_traceback: bool
        language_level: Any | None
        formal_grammar: bool
        gdb_debug: bool
        compile_time_env: dict[str, Any]
        module_name: str | None
        common_utility_include_dir: str | None
        output_dir: str | None
        build_dir: str | None
        cache: Any | None
        cache_size: int | None
        create_extension: Any | None
        np_pythran: bool
        legacy_implicit_noexcept: bool
        shared_utility_qualified_name: str | None
        old_style_globals: bool
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

    class Kwargs(TypedDict, total=False):
        include_path: list[str]
        shared_c_file_path: str | None
        output_file: str
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
        timestamps: dict | None
        verbose: int
        quiet: bool
        compiler_directives: Cython.Compiler.Directives.DirectivesKwargs
        embedded_metadata: dict
        evaluate_tree_assertions: bool
        emit_linenums: bool
        relative_path_in_code_position_comments: bool
        c_line_in_traceback: bool
        language_level: Any | None
        formal_grammar: bool
        gdb_debug: bool
        compile_time_env: dict[str, Any]
        module_name: str | None
        common_utility_include_dir: str | None
        output_dir: str | None
        build_dir: str | None
        cache: Any | None
        cache_size: int | None
        create_extension: Any | None
        np_pythran: bool
        legacy_implicit_noexcept: bool
        shared_utility_qualified_name: str | None
        old_style_globals: bool
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

class CompilationOptionsDict(CompilationOptions.Dict):...
class CompilationOptionsKwargs(CompilationOptions.Kwargs):...


DEFAULT_COMPILATION_OPTIONS = CompilationOptions()
directive_types =DEFAULT_COMPILATION_OPTIONS.compiler_directives.__annotations__

# Options previously defined as globals
docstrings: bool = DEFAULT_COMPILATION_OPTIONS.docstrings   
annotate: bool | None = DEFAULT_COMPILATION_OPTIONS.annotate
annotate_coverage_xml: str | None = DEFAULT_COMPILATION_OPTIONS.annotate_coverage_xml
annotate_no_c_link: bool = DEFAULT_COMPILATION_OPTIONS.annotate_no_c_link
generate_pxi: bool = DEFAULT_COMPILATION_OPTIONS.generate_pxi
capi_reexport_cincludes: bool = DEFAULT_COMPILATION_OPTIONS.capi_reexport_cincludes
working_path: str = DEFAULT_COMPILATION_OPTIONS.working_path
timestamps: Any | None = DEFAULT_COMPILATION_OPTIONS.timestamps
verbose: int = DEFAULT_COMPILATION_OPTIONS.verbose
quiet: bool = DEFAULT_COMPILATION_OPTIONS.quiet
compiler_directives: DirectivesType = DEFAULT_COMPILATION_OPTIONS.compiler_directives
embedded_metadata: dict[str, Any] = DEFAULT_COMPILATION_OPTIONS.embedded_metadata
embedding_file_name: str | None = DEFAULT_COMPILATION_OPTIONS.embedding_file_name
embedding_file_timestamp: int | None = DEFAULT_COMPILATION_OPTIONS.embedding_file_timestamp
evaluate_tree_assertions: bool = DEFAULT_COMPILATION_OPTIONS.evaluate_tree_assertions
emit_linenums: bool = DEFAULT_COMPILATION_OPTIONS.emit_linenums
relative_path_in_code_position_comments: bool = DEFAULT_COMPILATION_OPTIONS.relative_path_in_code_position_comments
embed_pos_in_docstring: bool = DEFAULT_COMPILATION_OPTIONS.embed_pos_in_docstring
pre_import: str | None = DEFAULT_COMPILATION_OPTIONS.pre_import
generate_cleanup_code: bool | int = DEFAULT_COMPILATION_OPTIONS.generate_cleanup_code
clear_to_none: bool = DEFAULT_COMPILATION_OPTIONS.clear_to_none
fast_fail: bool = DEFAULT_COMPILATION_OPTIONS.fast_fail
warning_errors: bool = DEFAULT_COMPILATION_OPTIONS.warning_errors
error_on_unknown_names: bool = DEFAULT_COMPILATION_OPTIONS.error_on_unknown_names
error_on_uninitialized: bool = DEFAULT_COMPILATION_OPTIONS.error_on_uninitialized
convert_range: bool = DEFAULT_COMPILATION_OPTIONS.convert_range
cache_builtins: bool = DEFAULT_COMPILATION_OPTIONS.cache_builtins
gcc_branch_hints: bool = DEFAULT_COMPILATION_OPTIONS.gcc_branch_hints
lookup_module_cpdef: bool = DEFAULT_COMPILATION_OPTIONS.lookup_module_cpdef
embed: bool | str | None = DEFAULT_COMPILATION_OPTIONS.embed
cimport_from_pyx: bool = DEFAULT_COMPILATION_OPTIONS.cimport_from_pyx
buffer_max_dims: int = DEFAULT_COMPILATION_OPTIONS.buffer_max_dims
closure_freelist_size: int = DEFAULT_COMPILATION_OPTIONS.closure_freelist_size
old_style_globals: bool = DEFAULT_COMPILATION_OPTIONS.old_style_globals
np_pythran: bool = DEFAULT_COMPILATION_OPTIONS.np_pythran
legacy_implicit_noexcept: bool = DEFAULT_COMPILATION_OPTIONS.legacy_implicit_noexcept
shared_utility_qualified_name: str | None = DEFAULT_COMPILATION_OPTIONS.shared_utility_qualified_name
output_dir: str | None = DEFAULT_COMPILATION_OPTIONS.output_dir
build_dir: str | None = DEFAULT_COMPILATION_OPTIONS.build_dir
cache: Any | None = DEFAULT_COMPILATION_OPTIONS.cache
cache_size: int | None = DEFAULT_COMPILATION_OPTIONS.cache_size
create_extension: Any | None = DEFAULT_COMPILATION_OPTIONS.create_extension
extra_warnings: dict[str, Any] = DEFAULT_COMPILATION_OPTIONS.extra_warnings