"""
Cython compiler directive options system.

This module defines all the compiler directives available in Cython,
using the typed_dataclass system for proper type checking and documentation.
"""

import os
from typing import Any, Dict, List, Optional, Literal, Callable, Union, Type
from dataclasses import field,dataclass as typed_dataclass


# Utility functions for directive validation
def one_of(*args, map=None):
    """Validate that a value is one of the given options."""
    def validate(name, value):
        if map is not None:
            value = map.get(value, value)
        if value not in args:
            raise ValueError(f"{name} directive must be one of {args}, got '{value}'")
        return value
    return validate


def normalise_encoding_name(option_name, encoding):
    """Normalize encoding names to a standard form."""
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
    
    import codecs
    try:
        decoder = codecs.getdecoder(encoding)
    except LookupError:
        return encoding  # may exists at runtime
    
    for name in ("ascii", "utf8"):
        if codecs.getdecoder(name) == decoder:
            return name
    
    return encoding


# Create a sentinel value for directives that need deferred analysis
class DEFER_ANALYSIS:
    """Sentinel for directives that need deferred analysis."""
    pass
DEFER_ANALYSIS = DEFER_ANALYSIS()


@typed_dataclass
class DirectiveOption:
    """Represents a compiler directive with its metadata."""
    
    name: str
    """The name of the directive as used in code."""
    
    type: Any
    """The expected type of the directive value."""
    
    default: Any
    """The default value of the directive."""
    
    doc: str
    """Documentation describing what the directive does."""
    
    scope: List[str] = field(default_factory=list)
    """Scopes where this directive is valid (module, function, class)."""


# Define all compiler directives with proper documentation
def define_compiler_directives() -> Dict[str, DirectiveOption]:
    """Define all compiler directives with their documentation and metadata."""
    directives = {}
    
    def add_directive(name, type_value, default, doc, scope=None):
        """Helper to add a directive to the collection."""
        if scope is None:
            scope = ["module", "function", "class", "with_statement"]
        directives[name] = DirectiveOption(name, type_value, default, doc, scope)
    
    # Language and behavior directives
    add_directive(
        "language_level", 
        str, 
        "3", 
        "Python language compatibility level. Values can be 2, 3, '3str', or '2'.",
        ["module"]
    )
    
    add_directive(
        "binding", 
        bool, 
        True, 
        "Whether to generate Python binding code. Was False before Cython 3.0.",
        ["module", "cclass", "function"]
    )
    
    add_directive(
        "boundscheck", 
        bool, 
        True, 
        "If set to False, Cython is allowed to skip bounds checking on array accesses.",
        ["module", "function", "class"]
    )
    
    add_directive(
        "nonecheck", 
        bool, 
        False, 
        "If set to True, Cython will insert checks for None at C attributes.",
        ["module", "function", "class"]
    )
    
    add_directive(
        "initializedcheck", 
        bool, 
        True, 
        "If set to True, Cython will insert checks that raise the appropriate exception when using uninitialized variables.",
        ["module", "function", "class"]
    )
    
    add_directive(
        "embedsignature", 
        bool, 
        False, 
        "If set to True, Cython will embed a signature string in docstrings.",
        ["module", "class", "function"]
    )
    
    add_directive(
        "cdivision", 
        bool, 
        False, 
        "If set to True, Cython will use C semantics for division (truncation). Was True before Cython 0.12.",
        ["module", "function", "class"]
    )
    
    add_directive(
        "cdivision_warnings", 
        bool, 
        False, 
        "If set to True, Cython will emit a runtime warning whenever division is performed with negative operands.",
        ["module", "function", "class"]
    )
    
    add_directive(
        "cpow", 
        bool, 
        None,  # None means not set by user
        "If set to True, Cython will use C semantics for power operator. Was True before Cython 3.0.",
        ["module", "function", "class"]
    )
    
    add_directive(
        "c_api_binop_methods", 
        bool, 
        False, 
        "If set to True, Cython will generate C API implementations for arithmetic special methods. Was True before Cython 3.0.",
        ["module"]
    )
    
    add_directive(
        "wraparound", 
        bool, 
        True, 
        "If set to False, Cython will not check for negative indices at array boundaries.",
        ["module", "function", "class"]
    )
    
    add_directive(
        "overflowcheck", 
        bool, 
        False, 
        "If set to True, Cython will generate code that checks for arithmetic overflows.",
        ["module", "function", "class"]
    )
    
    add_directive(
        "overflowcheck.fold", 
        bool, 
        True, 
        "If set to True with overflowcheck=True, Cython will check for overflow in constant expressions at compile time.",
        ["module", "function", "class"]
    )
    
    add_directive(
        "always_allow_keywords", 
        bool, 
        True, 
        "If set to True, a function with positional-only arguments in C will translate to a Python function that also accepts those arguments as keywords.",
        ["module", "function"]
    )
    
    add_directive(
        "profile", 
        bool, 
        False, 
        "If set to True, Cython will embed Python profiling hooks for Python code.",
        ["module", "function", "class"]
    )
    
    add_directive(
        "linetrace", 
        bool, 
        False, 
        "If set to True, Cython will generate code that enables line tracing and coverage reporting.",
        ["module", "function", "class"]
    )
    
    # Memory and type directives
    add_directive(
        "auto_pickle", 
        bool, 
        None,  # None means not set by user
        "If set to True, Cython will automatically generate pickle support for extension types.",
        ["module", "cclass"]
    )
    
    add_directive(
        "auto_cpdef", 
        bool, 
        False, 
        "If set to True, Cython functions will become cpdef by default, allowing them to be called from Python.",
        ["module"]
    )
    
    add_directive(
        "ccomplex", 
        bool, 
        False, 
        "If set to True, Cython will use C99/C++ for complex types and arithmetic.",
        ["module"]
    )
    
    add_directive(
        "c_string_type", 
        one_of('bytes', 'bytearray', 'str', 'unicode', map={'unicode': 'str'}), 
        "bytes", 
        "The type that C strings are converted to when coercing to a Python object.",
        ["module"]
    )
    
    add_directive(
        "c_string_encoding", 
        normalise_encoding_name, 
        "", 
        "The encoding to use when converting C strings to Python objects.",
        ["module"]
    )
    
    add_directive(
        "type_version_tag", 
        bool, 
        True, 
        "Enables Py_TPFLAGS_HAVE_VERSION_TAG on extension types.",
        ["module", "cclass"]
    )
    
    add_directive(
        "unraisable_tracebacks", 
        bool, 
        True, 
        "Whether to report tracebacks for unraisable exceptions.",
        ["module"]
    )
    
    add_directive(
        "freelist", 
        int, 
        0, 
        "Number of instances to keep for reuse. 0 means no freelist.",
        ["cclass"]
    )
    
    add_directive(
        "emit_code_comments", 
        bool, 
        True, 
        "Copy original source code into C code comments.",
        ["module"]
    )
    
    add_directive(
        "annotation_typing", 
        bool, 
        True, 
        "Read type declarations from Python function annotations.",
        ["module"]
    )
    
    add_directive(
        "infer_types", 
        bool, 
        True, 
        "Infer types of variables from their usage.",
        ["module"]
    )
    
    # Optimizations and warnings
    add_directive(
        "optimize.use_switch", 
        bool, 
        True, 
        "Use C switch statements for if/elif chains with integer literals.",
        ["module"]
    )
    
    add_directive(
        "optimize.unpack_method_calls", 
        bool, 
        True, 
        "Optimize method calls to reduce Python C-API call overhead.",
        ["module"]
    )
    
    add_directive(
        "optimize.unpack_method_calls_in_pyinit", 
        bool, 
        False, 
        "Optimize method calls in module initialization. Increases code size.",
        ["module"]
    )
    
    add_directive(
        "warn.undeclared", 
        bool, 
        False, 
        "Warn about undeclared variables being used.",
        ["module"]
    )
    
    add_directive(
        "warn.unreachable", 
        bool, 
        True, 
        "Warn about unreachable code.",
        ["module"]
    )
    
    add_directive(
        "warn.maybe_uninitialized", 
        bool, 
        False, 
        "Warn about potentially uninitialized variables.",
        ["module"]
    )
    
    add_directive(
        "warn.unused", 
        bool, 
        False, 
        "Warn about unused variables.",
        ["module"]
    )
    
    add_directive(
        "warn.unused_arg", 
        bool, 
        False, 
        "Warn about unused function arguments.",
        ["module"]
    )
    
    add_directive(
        "warn.unused_result", 
        bool, 
        False, 
        "Warn about unused result of function call.",
        ["module"]
    )
    
    add_directive(
        "warn.multiple_declarators",
        bool,
        True,
        "Warn about multiple declarators in a single declaration (e.g., 'cdef int a, b').",
        ["module"]
    )
    
    # Special directives
    add_directive(
        "final", 
        bool, 
        False, 
        "Declare a class or method as final (not overridable).",
        ["cclass", "function"]
    )
    
    add_directive(
        "nogil", 
        DEFER_ANALYSIS, 
        False, 
        "Declare that a function can be called without the GIL, or release the GIL in a with statement.",
        ["function", "with_statement"]
    )
    
    add_directive(
        "gil", 
        DEFER_ANALYSIS, 
        False, 
        "Acquire the GIL in a with statement.",
        ["with_statement"]
    )
    
    add_directive(
        "with_gil", 
        None, 
        None, 
        "Declare that a nogil function can acquire the GIL.",
        ["function"]
    )
    
    add_directive(
        "returns", 
        type, 
        None, 
        "Specify the return type of a function.",
        ["function"]
    )
    
    add_directive(
        "exceptval", 
        type, 
        None, 
        "Specify the exception return value of a function, with optional checking.",
        ["function"]
    )
    
    add_directive(
        "locals", 
        dict, 
        {}, 
        "Declare local variables with types.",
        ["module", "function", "cclass"]
    )
    
    add_directive(
        "np_pythran", 
        bool, 
        False, 
        "Use Pythran for NumPy expressions (optimized indexing).",
        ["module"]
    )
    
    add_directive(
        "cpp_locals", 
        bool, 
        False, 
        "Uses std::optional for C++ locals, so they work more like Python locals.",
        ["module", "function", "cclass"]
    )
    
    return directives


# Get the dictionary of all directives
compiler_directives = define_compiler_directives()


# Get just the default values for all directives
def get_directive_defaults():
    """Get a dictionary of all directive defaults."""
    return {name: directive.default for name, directive in compiler_directives.items()}


# Function to process directive options
def process_directive_option(directive_name, value):
    """Process a directive option and validate its value."""
    if directive_name not in compiler_directives:
        raise ValueError(f"Unknown directive: {directive_name}")
    
    directive = compiler_directives[directive_name]
    
    # Handle special types
    if directive.type is DEFER_ANALYSIS:
        return value  # Just pass through, will be handled later
    
    if directive.type is bool:
        if not isinstance(value, bool):
            if isinstance(value, str):
                if value.lower() in ('true', 'yes', '1'):
                    return True
                elif value.lower() in ('false', 'no', '0'):
                    return False
            raise ValueError(f"{directive_name} directive must be a boolean, got {value!r}")
        return value
    
    if directive.type is int:
        if not isinstance(value, int):
            try:
                return int(value)
            except (ValueError, TypeError):
                raise ValueError(f"{directive_name} directive must be an integer, got {value!r}")
        return value
    
    if directive.type is str:
        return str(value)
    
    if directive.type is dict:
        if not isinstance(value, dict):
            raise ValueError(f"{directive_name} directive must be a dictionary, got {value!r}")
        return value
    
    if directive.type is type:
        return value  # Should be a type object, validated later
    
    # Use callable validator like one_of
    if callable(directive.type):
        return directive.type(directive_name, value)
    
    # Default fallback
    return value


# Demo/test the module
if __name__ == "__main__":
    # Print directive information
    for name, directive in sorted(compiler_directives.items()):
        print(f"Directive: {name}")
        print(f"  Type: {directive.type}")
        print(f"  Default: {directive.default}")
        print(f"  Scope: {', '.join(directive.scope)}")
        print(f"  Doc: {directive.doc}")
        print()
    
    # Get directive defaults
    defaults = get_directive_defaults()
    print("Default directives:", len(defaults))
    
    # Test directive validation
    try:
        print(process_directive_option("boundscheck", False))
        print(process_directive_option("language_level", "3"))
        print(process_directive_option("c_string_type", "str"))
        
        # Should fail
        # print(process_directive_option("c_string_type", "invalid"))
    except ValueError as e:
        print(f"Validation error (expected): {e}")
        
    # Type checking demo with Dict and Kwargs
    # This would be checked by a type checker
    directive_dict: DirectiveOption.Dict = {
        "name": "new_directive",
        "type": bool, 
        "default": False,
        "doc": "A new directive",
        "scope": ["module"]
    }
    
    # Kwargs version (optional fields)
    directive_kwargs: DirectiveOption.Kwargs = {
        "name": "minimal_directive",
        "type": str,
        "default": "",
        "doc": "Minimal directive"
    }
    
    print("Dict version:", directive_dict)
    print("Kwargs version:", directive_kwargs) 