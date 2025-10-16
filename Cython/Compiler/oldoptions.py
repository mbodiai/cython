#
#  Cython - Compilation-wide options and pragma declarations
#
from dataclasses import dataclass, field, asdict, replace
from typing import Any, Callable, Dict, List, Literal, Optional, Type, TypeVar, Union, cast
import os

# Import common type definitions from DirectiveTypes
from .DirectiveTypes import (
    MODULE_SCOPE, FUNCTION_SCOPE, CLASS_SCOPE, WITH_STATEMENT_SCOPE, CCLASS_SCOPE,
    DirectiveScopeDict, DirectiveScopeKwargs, ReducedDirectiveScopeKwargs,
    NodeDirectiveScopeDict, DirectiveScopeMap, CompilationOptionsDict,
    CompilationOptionsKwargs, ValidatorFunc, DEFER_ANALYSIS, T
)

# Define a warning function needed for directive parsing
def warning(pos: Optional[Any], message: str, level: int = 0) -> None:
    """Issue a warning."""
    if pos:
        pos_str = f"{pos}: "
    else:
        pos_str = ""
    print(f"Warning: {pos_str}{message}")

"""
The members of this module are documented using autodata in
Cython/docs/src/reference/compilation.rst.
See https://www.sphinx-doc.org/en/master/usage/extensions/autodoc.html#directive-autoattribute
for how autodata works.
Descriptions of those members should start with a #:
Dont forget to keep the docs in sync by removing and adding
the members in both this file and the .rst file.
"""

@dataclass
class CompilerDirectives:
    """Main dataclass for all compiler directives."""
    # Global options
    docstrings: bool = True  # Whether to include docstrings in the Python extension
    embed_pos_in_docstring: bool = False  # Embed the source code position in docstrings
    pre_import: Optional[Any] = None  # (undocumented)
    generate_cleanup_code: bool = False  # Decref global variables on exit for garbage collection
    clear_to_none: bool = True  # Should tp_clear() set object fields to None instead of clearing them to NULL?
    annotate: bool = False  # Generate an annotated HTML version of the input source files
    annotate_coverage_xml: Optional[str] = None  # When annotating, include coverage information from this file
    fast_fail: bool = False  # Abort compilation on the first error
    warning_errors: bool = False  # Turn all warnings into errors
    error_on_unknown_names: bool = True  # Make unknown names an error
    error_on_uninitialized: bool = True  # Make uninitialized local variable reference a compile time error
    convert_range: bool = True  # Convert `for i in range(...)` to `for i from ...` when possible
    cache_builtins: bool = True  # Perform lookups on builtin names only once
    gcc_branch_hints: bool = True  # Generate branch prediction hints
    lookup_module_cpdef: bool = False  # Allow overwriting cpdef functions
    embed: Optional[Union[bool, str]] = None  # Whether to embed the Python interpreter
    old_style_globals: bool = False  # Previously, globals() gave the first non-Cython module globals in the call stack
    cimport_from_pyx: bool = False  # Allows cimporting from a pyx file without a pxd file
    buffer_max_dims: int = 8  # Maximum number of dimensions for buffers
    closure_freelist_size: int = 8  # Number of function closure instances to keep in a freelist

    # Standard directives
    binding: bool = True  # was False before 3.0
    boundscheck: bool = True
    nonecheck: bool = False
    initializedcheck: bool = True
    freethreading_compatible: bool = False
    subinterpreters_compatible: str = "no"
    embedsignature: bool = False
    embedsignature__dot__format: str = "c"
    auto_cpdef: bool = False
    auto_pickle: Optional[bool] = None
    cdivision: bool = False  # was True before 0.12
    cdivision_warnings: bool = False
    cpow: Optional[bool] = None  # was True before 3.0
    c_api_binop_methods: bool = False  # was True before 3.0
    overflowcheck: bool = False
    overflowcheck__dot__fold: bool = True
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
    infer_types: bool = True
    infer_types__dot__verbose: bool = False
    autotestdict: bool = True
    autotestdict__dot__cdef: bool = False
    autotestdict__dot__all: bool = False
    language_level: str = "3"
    fast_getattr: bool = True  # Undocumented until we come up with a better way to handle this everywhere.
    py2_import: bool = False  # For backward compatibility of Cython's source code in Py3 source mode
    preliminary_late_includes_cy28: bool = False  # Temporary directive in 0.28, to be removed in a later version (see GH#2079).
    iterable_coroutine: bool = False  # Make async coroutines backwards compatible with the old asyncio yield-from syntax.
    c_string_type: str = "bytes"
    c_string_encoding: str = ""
    type_version_tag: bool = True  # enables Py_TPFLAGS_HAVE_VERSION_TAG on extension types
    unraisable_tracebacks: bool = True
    np_pythran: bool = False
    fast_gil: bool = True
    cpp_locals: bool = False  # uses std::optional for C++ locals, so that they work more like Python locals
    legacy_implicit_noexcept: bool = False
    c_compile_guard: str = ""
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

    # Optimization directives
    optimize__dot__inline_defnode_calls: bool = True
    optimize__dot__unpack_method_calls: bool = True  # increases code size when True
    optimize__dot__unpack_method_calls_in_pyinit: bool = False  # uselessly increases code size when True
    optimize__dot__use_switch: bool = True

    # Remove unreachable code
    remove_unreachable: bool = True

    # Control flow debug directives
    control_flow_dot_output: str = ""  # Graphviz output filename
    control_flow_dot_annotate_defs: bool = False  # Annotate definitions

    # Test support
    test_assert_path_exists: List[str] = field(default_factory=list)
    test_fail_if_path_exists: List[str] = field(default_factory=list)
    test_assert_c_code_has: List[str] = field(default_factory=list)
    test_fail_if_c_code_has: List[str] = field(default_factory=list)

    # Experimental directives
    formal_grammar: bool = False

    # Special directive for node-specific settings
    critical_section: bool = False

    def to_dict(self) -> Dict[str, Any]:
        """Convert the dataclass to a dictionary."""
        return asdict(self)

    def copy(self) -> "CompilerDirectives":
        """Create a copy of the directives."""
        return replace(self)

    def update(self, **kwargs) -> "CompilerDirectives":
        """Create a new instance with updated values."""
        return replace(self, **kwargs)

# Create a global instance for the default directives
DEFAULT_DIRECTIVES = CompilerDirectives()

# Expose specific directives as module-level variables for backward compatibility
docstrings = DEFAULT_DIRECTIVES.docstrings
embed_pos_in_docstring = DEFAULT_DIRECTIVES.embed_pos_in_docstring
pre_import = DEFAULT_DIRECTIVES.pre_import
generate_cleanup_code = DEFAULT_DIRECTIVES.generate_cleanup_code
clear_to_none = DEFAULT_DIRECTIVES.clear_to_none
annotate = DEFAULT_DIRECTIVES.annotate
annotate_coverage_xml = DEFAULT_DIRECTIVES.annotate_coverage_xml
fast_fail = DEFAULT_DIRECTIVES.fast_fail
warning_errors = DEFAULT_DIRECTIVES.warning_errors
error_on_unknown_names = DEFAULT_DIRECTIVES.error_on_unknown_names
error_on_uninitialized = DEFAULT_DIRECTIVES.error_on_uninitialized
convert_range = DEFAULT_DIRECTIVES.convert_range
cache_builtins = DEFAULT_DIRECTIVES.cache_builtins
gcc_branch_hints = DEFAULT_DIRECTIVES.gcc_branch_hints
lookup_module_cpdef = DEFAULT_DIRECTIVES.lookup_module_cpdef
embed = DEFAULT_DIRECTIVES.embed
old_style_globals = DEFAULT_DIRECTIVES.old_style_globals
cimport_from_pyx = DEFAULT_DIRECTIVES.cimport_from_pyx
buffer_max_dims = DEFAULT_DIRECTIVES.buffer_max_dims
closure_freelist_size = DEFAULT_DIRECTIVES.closure_freelist_size

# Extra warning directives
extra_warnings: Dict[str, bool] = {
    "warn.maybe_uninitialized": True,
    "warn.unreachable": True,
    "warn.unused": True,
}

def get_directive_defaults() -> Dict[str, Any]:
    """Return a copy of the directive defaults dictionary."""
    return DEFAULT_DIRECTIVES.to_dict()

def copy_inherited_directives(
    outer_directives: Union[Dict[str, Any], CompilerDirectives], **new_directives
) -> Dict[str, Any]:
    """
    Create a new directives dictionary by starting with outer_directives and applying new_directives.
    Some directives are not inherited and are removed from the result.
    """
    # Convert to dict if it's a CompilerDirectives instance
    if isinstance(outer_directives, CompilerDirectives):
        directives_dict = outer_directives.to_dict()
    else:
        directives_dict = dict(outer_directives)

    # Create a new dict removing non-inherited directives
    result = directives_dict.copy()
    for name in (
        "test_assert_path_exists",
        "test_fail_if_path_exists",
        "test_assert_c_code_has",
        "test_fail_if_c_code_has",
        "critical_section",
    ):
        result.pop(name, None)

    # Apply new directives
    result.update(new_directives)
    return result

def copy_for_internal(outer_directives: Union[Dict[str, Any], CompilerDirectives]) -> Dict[str, Any]:
    """Reset some directives that users should not control for internal code."""
    return copy_inherited_directives(
        outer_directives,
        binding=False,
        profile=False,
        linetrace=False,
    )

def one_of(*args: str, map: Optional[Dict[str, str]] = None) -> ValidatorFunc:
    """Create a validator function that ensures a value is one of the given values."""
    def validate(name: str, value: Any) -> Any:
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

def normalise_encoding_name(option_name: str, encoding: str) -> str:
    """Normalize common encoding names to a standard form.

    >>> normalise_encoding_name('c_string_encoding', 'ascii')
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

    import codecs
    try:
        decoder = codecs.getdecoder(encoding)
    except LookupError:
        return encoding  # may exists at runtime ...
    for name in ("ascii", "utf8"):
        if codecs.getdecoder(name) == decoder:
            return name
    return encoding

@dataclass
class NodeDirective:
    """Dataclass for node directives."""
    auto_pickle: bool = False
    final: bool = False
    ccomplex: bool = False
    collection_type: str = ""
    nogil: bool = False
    gil: bool = False
    with_gil: bool = False
    critical_section: bool = False
    inline: bool = False
    cfunc: bool = False
    ccall: bool = False
    returns: Optional[type] = None
    exceptval: Optional[type] = None

# Define TypedDict for node directive scopes
try:
    from typing import TypedDict as _TypedDict
    class NodeDirectiveScopeDict(_TypedDict, total=False):
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
        returns: Optional[type]
        exceptval: Optional[type]
        locals: Dict[str, Any]
except (ImportError, TypeError):
    # Fallback for older Python versions
    pass

# Map indicating which directives are valid in which scopes
directive_scopes = {
    "auto_pickle": [MODULE_SCOPE, CCLASS_SCOPE],
    "final": [CCLASS_SCOPE, FUNCTION_SCOPE],
    "ccomplex": [MODULE_SCOPE],
    "collection_type": [CCLASS_SCOPE],
    "nogil": [FUNCTION_SCOPE, WITH_STATEMENT_SCOPE],
    "gil": [WITH_STATEMENT_SCOPE],
    "with_gil": [FUNCTION_SCOPE],
    "critical_section": [FUNCTION_SCOPE, WITH_STATEMENT_SCOPE],
    "inline": [FUNCTION_SCOPE],
    "cfunc": [FUNCTION_SCOPE, WITH_STATEMENT_SCOPE],
    "ccall": [FUNCTION_SCOPE, WITH_STATEMENT_SCOPE],
    "returns": [FUNCTION_SCOPE],
    "exceptval": [FUNCTION_SCOPE],
}

def parse_directive_list(
    text: str,
    relaxed_bool: bool = False,
    ignore_unknown: bool = False,
    current_settings: Optional[Union[Dict[str, Any], CompilerDirectives]] = None,
    scope: str = MODULE_SCOPE,
) -> Dict[str, Any]:
    """
    Parses a comma-separated list of directive-value combinations.
    scope should be one of: 'module', 'function', 'class', 'with statement'
    """
    if not text:
        return {}

    # Start with current settings or empty dict
    if current_settings is None:
        result = {}
    elif isinstance(current_settings, CompilerDirectives):
        result = current_settings.to_dict()
    else:
        result = dict(current_settings)

    # Parse directives from text
    for item in text.split(","):
        if not item.strip():
            continue

        if "=" not in item:
            name = item.strip()
            value = True
        else:
            name, value = [s.strip() for s in item.split("=", 1)]

        # Convert value to appropriate type
        if value is True or value is False or value is None:
            # Already a Python value, no conversion needed
            pass
        elif isinstance(value, str):
            if value == "True":
                value = True
            elif value == "False":
                value = False
            elif value == "None":
                value = None
            elif len(value) >= 2 and value[0] == value[-1] and value[0] in "'\"":
                value = value[1:-1]
            elif relaxed_bool and value in ("True", "False"):
                value = value == "True"
            else:
                try:
                    value = int(value)
                except ValueError:
                    # Keep as string
                    pass

        # Normalize key with dots
        normalized_key = name.replace(".", "__dot__") if "." in name else name

        # Check if directive is valid for this scope
        if not ignore_unknown and normalized_key in directive_scopes:
            if scope not in directive_scopes.get(normalized_key, []):
                expected = directive_scopes.get(normalized_key, [])
                if len(expected) == 1:
                    warning(
                        None,
                        f"The '{name}' directive is only allowed in {expected[0]} scope",
                        1,
                    )
                else:
                    warning(
                        None,
                        f"The '{name}' directive is only allowed in {', '.join(expected)} scopes",
                        1,
                    )

        # Add to result
        result[normalized_key] = value

    return result

@dataclass
class CompilationOptions:
    """Options for the Cython compiler."""
    # Core options
    cimport_from_pyx: bool = False
    language_level: Optional[int] = None
    docstrings: bool = True
    annotate: Optional[str] = None
    annotate_coverage_xml: Optional[str] = None
    # Initialized with default directives in post_init
    compiler_directives: Dict[str, Any] = field(default_factory=dict)
    embed_pos_in_docstring: bool = False
    generate_pxi: bool = False
    cache: bool = True
    output_dir: Optional[str] = None
    gdb_debug: bool = False
    compile_time_env: Dict[str, Any] = field(default_factory=dict)
    common_utility_include_dir: Optional[str] = None
    timestamps: Dict[str, float] = field(default_factory=dict)
    cplus: bool = False
    np_pythran: bool = False
    module_name: Optional[str] = None
    generate_cleanup_code: Optional[int] = None

    # Embedding support
    embed: Optional[Union[bool, str]] = None  # Whether to embed the Python interpreter

    # Additional options
    emit_linenums: bool = False
    c_line_in_traceback: bool = True
    fast_fail: bool = False
    warning_errors: bool = False
    error_on_unknown_names: bool = True
    error_on_uninitialized: bool = True
    convert_range: bool = True
    extra_warnings: List[str] = field(default_factory=list)
    verbose: int = 0
    working_path: Optional[str] = None
    output_file: Optional[str] = None
    show_version: bool = False
    use_listing_file: bool = False
    include_path: List[str] = field(default_factory=list)
    initial_file: Optional[str] = None
    embedded_metadata: Dict[str, Any] = field(default_factory=dict)
    depfile: bool = False
    generate_pxd_c_file_for_shared_module: bool = False
    separate_source_files: bool = False

    def __post_init__(self):
        """Initialize compiler_directives if empty."""
        if not self.compiler_directives:
            self.compiler_directives = DEFAULT_DIRECTIVES.to_dict()

    def to_dict(self) -> Dict[str, Any]:
        """Convert the dataclass to a dictionary."""
        return asdict(self)

    def configure_language_defaults(self, source_extension):
        """Configure language defaults based on the source file extension.

        Args:
            source_extension (str): Source file extension (e.g. 'py', 'pyx')
        """
        if self.language_level is None:
            if source_extension == 'py':
                self.language_level = 3  # Python 3 for .py files
            else:
                self.language_level = 3  # Default is Python 3

        if source_extension == 'py' and self.compiler_directives.get('binding') is None:
            # Python files imply binding=True
            new_directives = self.compiler_directives.copy()
            new_directives['binding'] = True
            self.compiler_directives = new_directives

    def get_fingerprint(self) -> str:
        """Generate a fingerprint for caching purposes."""
        import hashlib
        parts = [
            str(self.language_level),
            str(self.compiler_directives),
            str(self.compile_time_env),
        ]
        fingerprint = hashlib.md5(str(parts).encode()).hexdigest()
        return fingerprint

    @classmethod
    def from_default(cls) -> "CompilationOptions":
        """Create CompilationOptions with default values."""
        return cls(compiler_directives=DEFAULT_DIRECTIVES.to_dict())

    def create_context(self):
        """Create a compilation context from these options."""
        from . import Main
        return Main.Context.from_options(self)

@dataclass
class Context:
    """Compilation context containing options and state.

    This class maintains the state needed during a compilation run,
    particularly important for embedding Python.
    """
    options: CompilationOptions = field(default_factory=CompilationOptions.from_default)
    cython_scope: Any = None
    pxds: Dict[str, Any] = field(default_factory=dict)
    utility_pxds: Dict[str, Any] = field(default_factory=dict)

    # Special functions for embedding
    def embed_py_code(self, code, py_file_name):
        """Embed Python code for interpreter execution."""
        if self.options.embed:
            # The actual implementation would be more complex
            print(f"Embedding Python code from {py_file_name}")
            return True
        return False

    @property
    def compiler_directives(self) -> Dict[str, Any]:
        """Shortcut to access compiler directives through the options."""
        return self.options.compiler_directives

    @classmethod
    def from_options(cls, options: CompilationOptions) -> "Context":
        """Create a Context with the given options."""
        return cls(options=options)

# For backward compatibility - used in Main.py
default_options = CompilationOptions.from_default().to_dict()
