#
#  Cython - Compilation-wide options and pragma declarations
#
from __future__ import annotations

import ast
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Literal, Optional

import Cython.Compiler.Directives
from Cython.Abstract import MatchAST, func_def
from Cython.DataDict import DataDict

embedding_file_name: Optional[str]


# ------------------------------------------------------------------------
# CompilationOptions are constructed from user input and are the `option`
#  object passed throughout the compilation pipeline.
# ------------------------------------------------------------------------
CYTHON_COMMON_UTILITY_INCLUDE_DIR = str(Path(__file__).parent.parent / "Common" / "Include")


@dataclass
class CompilationOptions(DataDict):
    """Options for Cython compilation, used throughout the compilation pipeline.

    See default_options at the end of this module for a list of all possible
    options and CmdLine.usage and CmdLine.parse_command_line() for their meaning.
    """

    # Fields defined based on old CompilationOptionKwargs and default_options
    include_path: list[str] = field(default_factory=lambda: ["."])
    shared_c_file_path: str | None = None
    output_file: str | None = None
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
    compiler_directives: Cython.Compiler.Directives.Directives = field(default_factory=Cython.Compiler.Directives.Directives)
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


DEFAULT_COMPILATION_OPTIONS = CompilationOptions()