# Install and fix package errors
_Exported on 11/14/2025 at 19:42:32 EST from Cursor (2.0.77)_

---

**User**

source .venv and pip install -e . then fix errors WITHOUT reverting anything. feel free to reference upstream/main but DO NOT REVERT ANYTHING

---

**Cursor**

```python
#
#   Symbol Table
#
from __future__ import annotations

from collections.abc import Callable
import copy
from dataclasses import dataclass, field
import operator
import re
from typing import TYPE_CHECKING, Any, cast

from ..Utils import try_finally_contextmanager
from . import Code, DebugFlags, Naming, Options, PyrexTypes
from .Errors import InternalError, error, performance_hint, warning
from .PyrexTypes import py_object_type, unspecified_type
from .StringEncoding import EncodedString
from .TypeSlots import (
    get_property_accessor_signature,
    get_slot_table,
    pyfunction_signature,
    pymethod_signature,
    richcmp_special_methods,
)
from .Directives import Directives

if TYPE_CHECKING:
    from .PyrexTypes import CFuncType, PyrexType
    from .TypeSlots import Signature


def c_safe_identifier(cname):
    # There are some C limitations on struct entry names.
    if ((cname[:2] == '__' and not (cname.startswith(Naming.pyrex_prefix)
                                    or cname in ('__weakref__', '__dict__')))
            or cname in Naming.reserved_cnames):
        cname = Naming.pyrex_prefix + cname
    return cname


def punycodify_name(cname, mangle_with=None):
    # if passed the mangle_with should be a byte string
    # modified from  PEP489
    if cname.isascii():
        return cname

    cname = cname.encode('punycode').replace(b'-', b'_').decode('ascii')
    if mangle_with:
        # sometimes it necessary to mangle unicode names alone where
        # they'll be inserted directly into C, because the punycode
        # transformation can turn them into invalid identifiers
        cname = f"{mangle_with}_{cname}"
    elif cname.startswith(Naming.pyrex_prefix):
        # a punycode name could also be a valid ascii variable name so
        # change the prefix to distinguish
        cname = cname.replace(Naming.pyrex_prefix,
                              Naming.pyunicode_identifier_prefix, 1)

    return cname


class BufferAux:
    writable_needed = False

    def __init__(self, buflocal_nd_var, rcbuf_var):
        self.buflocal_nd_var = buflocal_nd_var
        self.rcbuf_var = rcbuf_var

    def __repr__(self):
        return f"<BufferAux {self.__dict__!r}>"

Boolean = bool | int
class Entry:
    # A symbol table entry in a Scope or ModuleNamespace.
    #
    # name             string     Python name of entity
    # cname            string     C name of entity
    # type             PyrexType  Type of entity
    # doc              string     Doc string
    # annotation       ExprNode   PEP 484/526 annotation
    # init             string     Initial value
    # visibility       'private' or 'public' or 'extern'
    # is_builtin       boolean    Is an entry in the Python builtins dict
    # is_cglobal       boolean    Is a C global variable
    # is_pyglobal      boolean    Is a Python module-level variable
    #                               or class attribute during
    #                               class construction
    # is_member        boolean    Is an assigned class member
    # is_pyclass_attr  boolean    Is a name in a Python class namespace
    # is_variable      boolean    Is a variable
    # is_cfunction     boolean    Is a C function
    # is_cmethod       boolean    Is a C method of an extension type
    # is_builtin_cmethod boolean  Is a C method of a builtin type (implies is_cmethod)
    # is_unbound_cmethod boolean  Is an unbound C method of an extension type
    # is_final_cmethod   boolean  Is non-overridable C method
    # is_inline_cmethod  boolean  Is inlined C method
    # is_anonymous     boolean    Is a anonymous pyfunction entry
    # is_type          boolean    Is a type definition
    # is_cclass        boolean    Is an extension class
    # is_cclass_var_rentry  boolean Is a var entry of an extension type
    #                              (Hack! Only needed because most C globals are
    #                               static variables while these live in the module scope.
    #                               Remove when fixed.)
    # is_cpp_class     boolean    Is a C++ class
    # is_const         boolean    Is a constant
    # is_property      boolean    Is a property of an extension type:
    # doc_cname        string or None  C const holding the docstring
    # getter_cname     string          C func for getting property
    # setter_cname     string          C func for setting or deleting property
    # is_cproperty     boolean         Is an inline property of an external type
    # is_self_arg      boolean    Is the "self" arg of an exttype method
    # is_arg           boolean    Is the arg of a method
    # is_local         boolean    Is a local variable
    # in_closure       boolean    Is referenced in an inner scope
    # in_subscope      boolean    Belongs to a generator expression scope
    # is_readonly      boolean    Can't be assigned to
    # func_cname       string     C func implementing Python func
    # wrapperbase_cname [string]  C wrapperbase object name
    # func_modifiers   [string]   C function modifiers ('inline')
    # pos              position   Source position where declared
    # namespace_cname  string     If is_pyglobal, the C variable
    #                               holding its home namespace
    # pymethdef_cname  string     PyMethodDef structure
    # signature        Signature  Arg & return types for Python func
    # as_variable      Entry      Alternative interpretation of extension
    #                               type name or builtin C function as a variable
    # xdecref_cleanup  boolean    Use Py_XDECREF for error cleanup
    # in_cinclude      boolean    Suppress C declaration code
    # enum_values      [Entry]    For enum types, list of values
    # qualified_name   string     "modname.funcname" or "modname.classname"
    #                               or "modname.classname.funcname"
    # is_declared_generic  boolean  Is declared as PyObject * even though its
    #                                 type is an extension type
    # as_module        None       Module scope, if a cimported module
    # is_inherited     boolean    Is an inherited attribute of an extension type
    # pystring_cname   string     C name of Python version of string literal
    # is_interned      boolean    For string const entries, value is interned
    # is_identifier    boolean    For string const entries, value is an identifier
    # used             boolean
    # is_special       boolean    Is a special method or property accessor
    #                               of an extension type
    # defined_in_pxd   boolean    Is defined in a .pxd file (not just declared)
    # api              boolean    Generate C API for C class or function
    # utility_code     string     Utility code needed when this entry is used
    #
    # buffer_aux       BufferAux or None  Extra information needed for buffer variables
    # inline_func_in_pxd boolean  Hacky special case for inline function in pxd file.
    #                             Ideally this should not be necessary.
    # might_overflow   boolean    In an arithmetic expression that could cause
    #                             overflow (used for type inference).
    # utility_code_definition     For some Cython builtins, the utility code
    #                             which contains the definition of the entry.
    #                             Currently only supported for CythonScope entries.
    # error_on_uninitialized      Have Control Flow issue an error when this entry is
    #                             used uninitialized
    # cf_used          boolean    Entry is used
    # is_fused_specialized boolean Whether this entry of a cdef or def function
    #                              is a specialization
    # is_cgetter       boolean    Is a c-level getter function
    # is_cpp_optional  boolean    Entry should be declared as std::optional (cpp_locals directive)
    # known_standard_library_import     Either None (default), an empty string (definitely can't be determined)
    #                             or a string of "modulename.something.attribute"
    #                             Used for identifying imports from typing/dataclasses etc
    # pytyping_modifiers          Python type modifiers like "typing.ClassVar" but also "dataclasses.InitVar"
    # enum_int_value  None or int  If known, the int that corresponds to this enum value
    # specialiser  function or None  Callable to specialise a function to specific C arguments.

    name: str
    cname: str
    type: "PyrexTypes.PyrexType"
    pos: int|None
    overloaded_alternatives: list["Entry"]
    cf_assignments: list["Entry"]
    cf_references: list["Entry"]
    inner_entries: list["Entry"]
    defining_entry: "Entry"
    borrowed: int = 0
    is_builtin: Boolean = False
    is_cglobal: Boolean = False
    is_pyglobal: Boolean = False
    is_member: Boolean = False
    is_pyclass_attr: Boolean = False
    is_variable: Boolean = False
    is_cfunction: Boolean = False
    is_cmethod: Boolean = False
    is_builtin_cmethod: Boolean = False
    is_unbound_cmethod: Boolean = False
    is_final_cmethod: Boolean = False
    is_inline_cmethod: Boolean = False
    is_anonymous: Boolean = False
    is_type: Boolean = False
    is_cclass: Boolean = False
    is_cclass_var_entry: Boolean = False
    is_cpp_class: Boolean = False
    is_const: Boolean = False
    is_property: Boolean = False
    is_cproperty: Boolean = False
    is_self_arg: Boolean = False
    is_arg: Boolean = False
    is_local: Boolean = False
    in_closure: Boolean = False
    from_closure: Boolean = False
    in_subscope: Boolean = False
    is_declared_generic: Boolean = False
    is_readonly: Boolean = False
    xdecref_cleanup: Boolean = False
    in_cinclude: Boolean = False
    is_inherited: Boolean = False
    is_identifier: Boolean = False
    is_interned: Boolean = False
    used: Boolean = False
    is_special: Boolean = False
    defined_in_pxd: Boolean = False
    is_implemented: Boolean = False
    api: Boolean = False
    is_overridable: Boolean = False
    buffer_aux: "BufferAux|None" = None
    inline_func_in_pxd: Boolean = False
    borrowed = 0
    init: str|None = None
    annotation: str|None = None
    visibility: str = 'private'
  
    doc_cname: str|None = None
    getter_cname: str|None = None
    setter_cname: str|None = None
   
    pyfunc_cname: str|None = None
    func_cname: str|None = None
    func_modifiers: list[str] = []
    final_func_cname: str|None = None
    doc: str|None = None
    as_variable: "Entry|None" = None
    as_module: "Scope|None" = None
    pystring_cname: str|None = None
    utility_code: "Code.UtilityCode|None" = None
    specialiser:"Callable[[Scope, list[PyrexType]], Entry|None]|None" = None
    prev_entry:"Entry|None" = None
    might_overflow:Boolean = 0
    fused_cfunction:"CFuncType|None" = None
    is_fused_specialized: Boolean = False
    needs_property: Boolean = False
    in_with_gil_block: int = 0
    from_cython_utility_code:"Code.UtilityCode|None" = None
    error_on_uninitialized: Boolean = False
    cf_used: Boolean     = True
    outer_entry:"Entry|None" = None
    is_cgetter: Boolean = False
    is_cpp_optional: Boolean = False
    known_standard_library_import: str|None = None
    pytyping_modifiers: list[str]|None = None
    enum_int_value: int|None = None
    vtable_type: "PyrexTypes.PyrexType|None" = None
    signature: "Signature"
    def __init__(self, name:str, cname:str, type:"CFuncType", pos:int|None = None, init:str|None = None):
        self.name = name
        self.cname = cname
        self.type = type
        self.pos = pos
        self.init = init
        self.overloaded_alternatives = []
        self.cf_assignments = []
        self.cf_references = []
        self.inner_entries = []
        self.defining_entry = self


    def __repr__(self):
        return f"{type(self).__name__}(<{id(self):x}>, name={self.name}, type={self.type})"

    def already_declared_here(self):
        error(self.pos, "Previous declaration is here")

    def redeclared(self, pos:int|None):
        error(pos, f"'{self.name}' does not match previous declaration")
        self.already_declared_here()

    def all_alternatives(self):
        return [self] + self.overloaded_alternatives

    def best_function_match(self, scope:"Scope", arg_types:list["PyrexType"], fail_if_empty=False, arg_is_lvalue_array=None):
        func_entry = None
        if self.specialiser is not None:
            func_entry = self.specialiser(scope, arg_types)
        if func_entry is None:
            if self.type.is_fused:
                functypes = cast("PyrexTypes.CFuncType", self.type).get_all_specialized_function_types()
                alternatives = [f.entry for f in functypes]
            else:
                alternatives = self.all_alternatives()
            func_entry = PyrexTypes.best_match(
                arg_types, alternatives, fail_if_empty=fail_if_empty, arg_is_lvalue_array=arg_is_lvalue_array)
        return func_entry

    def all_entries(self):
        return [self] + self.inner_entries

    def __lt__(self, right):
        if isinstance(self, Entry) and isinstance(right, Entry):
            return (self.name, self.cname) < (right.name, right.cname)
        return NotImplemented

    @property
    def cf_is_reassigned(self):
        return len(self.cf_assignments) > 1

    def make_cpp_optional(self):
        assert self.type.is_cpp_class
        self.is_cpp_optional = True
        assert not self.utility_code  # we're not overwriting anything?
        self.utility_code = Code.UtilityCode.load_cached("OptionalLocals", "CppSupport.cpp")

    def declared_with_pytyping_modifier(self, modifier_name):
        return modifier_name in self.pytyping_modifiers if self.pytyping_modifiers else False


class InnerEntry(Entry):
    """An entry in a closure scope that represents the real outer Entry.
    """
    from_closure = True

    def __init__(self, outer_entry, scope):
        Entry.__init__(self, outer_entry.name,
                       outer_entry.cname,
                       outer_entry.type,
                       outer_entry.pos)
        self.outer_entry = outer_entry
        self.scope = scope

        # share state with (outermost) defining entry
        outermost_entry = outer_entry
        while outermost_entry.outer_entry:
            outermost_entry = outermost_entry.outer_entry
        self.defining_entry = outermost_entry
        self.inner_entries = outermost_entry.inner_entries
        self.cf_assignments = outermost_entry.cf_assignments
        self.cf_references = outermost_entry.cf_references
        self.overloaded_alternatives = outermost_entry.overloaded_alternatives
        self.is_cpp_optional = outermost_entry.is_cpp_optional
        self.inner_entries.append(self)

    def __getattr__(self, name:str)->Any:
        if name.startswith('__'):
            # we wouldn't have been called if it was there
            raise AttributeError(name)
        return getattr(self.defining_entry, name)

    def all_entries(self):
        return self.defining_entry.all_entries()

@dataclass
class Scope:
    # name              string             Unqualified name
    # outer_scope       Scope or None      Enclosing scope
    # entries           {string : Entry}   Python name to entry, non-types
    # const_entries     [Entry]            Constant entries
    # type_entries      [Entry]            Struct/union/enum/typedef/exttype entries
    # sue_entries       [Entry]            Struct/union/enum entries
    # arg_entries       [Entry]            Function argument entries
    # var_entries       [Entry]            User-defined variable entries
    # pyfunc_entries    [Entry]            Python function entries
    # cfunc_entries     [Entry]            C function entries
    # c_class_entries   [Entry]            All extension type entries
    # cname_to_entry    {string : Entry}   Temp cname to entry mapping
    # return_type       PyrexType or None  Return type of function owning scope
    # is_builtin_scope  boolean            Is the builtin scope of Python/Cython
    # is_py_class_scope boolean            Is a Python class scope
    # is_c_class_scope  boolean            Is an extension type scope
    # is_local_scope    boolean            Is a local (i.e. function/method/generator) scope
    # is_closure_scope  boolean            Is a closure scope
    # is_generator_expression_scope boolean   A subset of closure scope used for generator expressions
    # is_passthrough    boolean            Outer scope is passed directly
    # is_cpp_class_scope  boolean          Is a C++ class scope
    # is_property_scope boolean            Is a extension type property scope
    # is_c_dataclass_scope     boolean or "frozen"  is a cython.dataclasses.dataclass
    # scope_prefix      string             Disambiguator for C names
    # in_cinclude       boolean            Suppress C declaration code
    # qualified_name    string             "modname" or "modname.classname"
    #                                        Python strings in this scope
    # nogil             boolean            In a nogil section
    # directives        dict               Helper variable for the recursive
    #                                      analysis, contains directive values.
    # is_internal       boolean            Is only used internally (simpler setup)
    # scope_predefined_names  list of str   Class variable containing special names defined by
    #                                      this type of scope (e.g. __builtins__, __qualname__)
    # node_positions_to_offset  {pos: offset}  Mapping from node positions to line table offsets
    name: str
    outer_scope: "Scope|None" = None
    parent_scope: "Scope|None" = None
    entries: dict[str, "Entry"] = field(default_factory=dict)
    subscopes: set["Scope"] = field(default_factory=set)
    const_entries: list["Scope|Entry"] = field(default_factory=list)
    type_entries: list["Scope|Entry"] = field(default_factory=list)
    sue_entries: list["Scope|Entry"] = field(default_factory=list)
    arg_entries: list["Scope|Entry"] = field(default_factory=list)
    var_entries: list["Scope|Entry"] = field(default_factory=list)
    pyfunc_entries: list["Scope|Entry"] = field(default_factory=list)
    cfunc_entries: list["Scope|Entry"] = field(default_factory=list)
    c_class_entries: list["Scope|Entry"] = field(default_factory=list)
    defined_c_classes: list["Scope|Entry"] = field(default_factory=list)
    imported_c_classes: dict[str, "Scope"] = field(default_factory=dict)
    cname_to_entry: dict[str, "Scope|Entry"] = field(default_factory=dict)
    identifier_to_entry: dict[str, "Scope|Entry"] = field(default_factory=dict)
    num_to_entry: dict[str, "Scope|Entry"] = field(default_factory=dict)
    obj_to_entry: dict[str, "Scope|Entry"] = field(default_factory=dict)
    buffer_entries: list["Scope"] = field(default_factory=list)
    lambda_defs: list["Scope"] = field(default_factory=list)
    id_counters: dict[str, int] = field(default_factory=dict[str, int])
    
    is_builtin_scope:bool|int = False
    is_py_class_scope:bool|int = False
    is_c_class_scope:bool|int = False
    is_closure_scope:bool|int = False
    is_local_scope:bool|int = False
    is_generator_expression_scope:bool|int = False
    is_comprehension_scope:bool|int = False
    is_passthrough:bool|int = False
    is_cpp_class_scope:bool|int = False
    is_property_scope:bool|int = False
    is_module_scope:bool|int = False
    is_c_dataclass_scope:bool|int = False
    is_internal:bool|int = False
    scope_prefix: str = ""
    in_cinclude:bool|int = False
    nogil:bool|int = False
    fused_to_specific:"dict[PyrexTypes.FusedType, PyrexTypes.PyrexType]|None" = None
    return_type:"PyrexTypes.PyrexType|None" = None
    scope_predefined_names = []
    qualified_name:EncodedString = field(default_factory=EncodedString)
    directives:Directives = field(default_factory=Directives)
    # Do ambiguous type names like 'int' and 'float' refer to the C types? (Otherwise, Python types.)
    in_c_type_context = True
    node_positions_to_offset = {}  # read-only fallback dict


    def __post_init__(self):
        # The outer_scope is the next scope in the lookup chain.
        # The parent_scope is used to derive the qualified name of this scope.
        mangled_name = "%d%s_" % (len(self.name), self.name.replace('.', '_dot_'))
        qual_scope = self.qualifying_scope()
        if qual_scope:
            self.qualified_name = qual_scope.qualify_name(self.name)
            self.scope_prefix = qual_scope.scope_prefix + mangled_name
        else:
            self.qualified_name = EncodedString(self.name)
            self.scope_prefix = mangled_name
        for var_name in self.scope_predefined_names:
            self.declare_var(EncodedString(var_name), py_object_type, pos=None)

    def __deepcopy__(self, memo):
        return self

    def merge_in(self, other, merge_unused=True, allowlist=None):
        # Use with care...
        entries = []
        for name, entry in other.entries.items():
            if (not allowlist or name in allowlist) and (entry.used or merge_unused):
                entries.append((name, entry))

        self.entries.update(entries)

        for attr in ('const_entries',
                     'type_entries',
                     'sue_entries',
                     'arg_entries',
                     'var_entries',
                     'pyfunc_entries',
                     'cfunc_entries',
                     'c_class_entries'):
            self_entries = getattr(self, attr)
            names = {e.name for e in self_entries}
            for entry in getattr(other, attr):
                if (entry.used or merge_unused) and entry.name not in names:
                    self_entries.append(entry)

    def __str__(self):
        return f"<{self.__class__.__name__} {self.qualified_name}>"

    def qualifying_scope(self):
        return self.parent_scope

    def mangle(self, prefix, name = None):
        if name:
            return punycodify_name("%s%s%s" % (prefix, self.scope_prefix, name))

        return self.parent_scope.mangle(prefix, self.name)

    def mangle_internal(self, name):
        # Mangle an internal name so as not to clash with any
        # user-defined name in this scope.
        prefix = "%s%s_" % (Naming.pyrex_prefix, name)
        return self.mangle(prefix)
        #return self.parent_scope.mangle(prefix, self.name)

    def mangle_class_private_name(self, name):
        if self.parent_scope:
            return self.parent_scope.mangle_class_private_name(name)
        return name

    def next_id(self, name=None):
        # Return a cname fragment that is unique for this module
        counters = self.global_scope().id_counters
        try:
            count = counters[name] + 1
        except KeyError:
            count = 0
        counters[name] = count
        if name:
            if not count:
                # unique names don't need a suffix, reoccurrences will get one
                return name
            return '%s%d' % (name, count)
        return '%d' % count

    @property
    def context(self):
        return self.global_scope().context

    def global_scope(self):
        """Return the module-level scope containing this scope."""
        return self.outer_scope.global_scope()

    def builtin_scope(self):
        """Return the module-level scope containing this scope."""
        return self.outer_scope.builtin_scope()

    def iter_local_scopes(self):
        yield self
        if self.subscopes:
            yield from sorted(self.subscopes, key=operator.attrgetter('scope_prefix'))

    @try_finally_contextmanager
    def new_c_type_context(self, in_c_type_context=None):
        old_c_type_context = self.in_c_type_context
        if in_c_type_context is not None:
            self.in_c_type_context = in_c_type_context
        yield
        self.in_c_type_context = old_c_type_context

    def handle_already_declared_name(self, name, cname, type, pos, visibility, copy_entry=False):
        """Returns an entry or None

        If it returns an entry, it makes sense for "declare" to keep using that
        entry and not to declare its own.

        May be overridden (e.g. for builtin scope,
        which always allows redeclarations)
        """
        entry = None
        entries = self.entries
        old_entry = entries[name]

        # Reject redeclared C++ functions only if they have a compatible type signature.
        cpp_override_allowed = False
        if type.is_cfunction and old_entry.type.is_cfunction and self.is_cpp():
            # If we redefine a C++ class method which is either inherited
            # or automatically generated (base constructor), then it's fine.
            # Otherwise, we shout.
            for alt_entry in old_entry.all_alternatives():
                if type.compatible_signature_with(alt_entry.type):
                    if name == '<init>' and not type.args:
                        # Cython pre-declares the no-args constructor - allow later user definitions.
                        cpp_override_allowed = True
                    elif alt_entry.is_inherited:
                        # Note that we can override an inherited method with a compatible but not exactly equal signature, as in C++.
                        cpp_override_allowed = True
                    if cpp_override_allowed:
                        entry = alt_entry
                        if copy_entry:
                            entry = copy.copy(alt_entry)

                        # A compatible signature doesn't mean the exact same signature,
                        # so we're taking the new signature for the entry.
                        entry.type = type
                        entry.is_inherited = False
                        # Updating the entry attributes which can be modified in the method redefinition.
                        entry.cname = cname
                        entry.pos = pos
                    break
            else:
                cpp_override_allowed = True

        if cpp_override_allowed:
            # C++ function/method overrides with different signatures are ok.
            pass
        elif entries[name].is_inherited:
            # Likewise ignore inherited classes.
            pass
        else:
            if visibility == 'extern':
                # Silenced outside of "cdef extern" blocks, until we have a safe way to
                # prevent pxd-defined cpdef functions from ending up here.
                warning(pos, "'%s' redeclared " % name, 1 if self.in_cinclude else 0)
            elif visibility != 'ignore':
                error(pos, "'%s' redeclared " % name)
                self.entries[name].already_declared_here()
            return None

        return entry


    def declare(self, name: str, cname: str, type:"PyrexType", pos: int | None, visibility: str, shadow = 0, is_type = 0, create_wrapper = 0):
        # Create new entry, and add to dictionary if
        # name is not None. Reports a warning if already
        # declared.
        if type.is_buffer and not isinstance(self, LocalScope):  # and not is_type:
            error(pos, 'Buffer types only allowed as function local variables')
        if not self.in_cinclude and cname and re.match("^_[_A-Z]+$", cname):
            # See https://www.gnu.org/software/libc/manual/html_node/Reserved-Names.html#Reserved-Names
            warning(pos, "'%s' is a reserved name in C." % cname, -1)

        entries = self.entries
        entry = None
        if name and name in entries and not shadow:
            entry = self.handle_already_declared_name(name, cname, type, pos, visibility)

        if not entry:
            entry = Entry(name, cname, type, pos = pos)
            entry.in_cinclude = self.in_cinclude
            entry.create_wrapper = create_wrapper

            if name:
                entry.qualified_name = self.qualify_name(name)
                if not shadow:
                    if name in entries and self.is_cpp() and type.is_cfunction and not entries[name].is_cmethod:
                        # Which means: function or cppclass method is already present
                        entries[name].overloaded_alternatives.append(entry)
                    else:
                        entries[name] = entry

        if type.is_memoryviewslice:
            entry.init = type.default_value

        entry.scope = self
        entry.visibility = visibility
        return entry

    def qualify_name(self, name):
        return EncodedString("%s.%s" % (self.qualified_name, name))

    def declare_const(self, name, type, value, pos, cname = None, visibility = 'private', api = 0, create_wrapper = 0):
        # Add an entry for a named constant.
        if not cname:
            if self.in_cinclude or (visibility == 'public' or api):
                cname = name
            else:
                cname = self.mangle(Naming.enum_prefix, name)
        entry = self.declare(name, cname, type, pos, visibility, create_wrapper = create_wrapper)
        entry.is_const = 1
        entry.value_node = value
        return entry

    def declare_type(self, name, type, pos,
            cname = None, visibility = 'private', api = 0, defining = 1,
            shadow = 0, template = 0):
        # Add an entry for a type definition.
        if not cname:
            cname = name
        entry = self.declare(name, cname, type, pos, visibility, shadow,
                             is_type=True)
        entry.is_type = 1
        entry.api = api
        if defining:
            self.type_entries.append(entry)

        # don't replace an entry that's already set
        if not template and getattr(type, "entry", None) is None:
            type.entry = entry

        # here we would set as_variable to an object representing this type
        return entry

    def declare_typedef(self, name, base_type, pos, cname = None,
                        visibility = 'private', api = 0):
        if not cname:
            if self.in_cinclude or (visibility != 'private' or api):
                cname = name
            else:
                cname = self.mangle(Naming.type_prefix, name)
        try:
            namespace = self.outer_scope.lookup(self.name).type if self.is_cpp_class_scope else None
            type = PyrexTypes.create_typedef_type(name, base_type, cname,
                                                  (visibility == 'extern'),
                                                  namespace)
        except ValueError as e:
            error(pos, e.args[0])
            type = PyrexTypes.error_type
        entry = self.declare_type(name, type, pos, cname,
                                  visibility = visibility, api = api)
        type.qualified_name = entry.qualified_name
        return entry

    def declare_struct_or_union(self, name, kind, scope,
                                typedef_flag, pos, cname = None,
                                visibility = 'private', api = 0,
                                packed = False):
        # Add an entry for a struct or union definition.
        if not cname:
            if self.in_cinclude or (visibility == 'public' or api):
                cname = name
            else:
                cname = self.mangle(Naming.type_prefix, name)
        entry = self.lookup_here(name)
        if not entry:
            in_cpp = self.is_cpp()
            type = PyrexTypes.CStructOrUnionType(
                name, kind, scope, typedef_flag, cname, packed,
                in_cpp = in_cpp)
            entry = self.declare_type(name, type, pos, cname,
                visibility = visibility, api = api,
                defining = scope is not None)
            self.sue_entries.append(entry)
            type.entry = entry
        else:
            if not (entry.is_type and entry.type.is_struct_or_union
                    and entry.type.kind == kind):
                warning(pos, "'%s' redeclared  " % name, 0)
            elif scope and entry.type.scope:
                warning(pos, "'%s' already defined  (ignoring second definition)" % name, 0)
            else:
                self.check_previous_typedef_flag(entry, typedef_flag, pos)
                self.check_previous_visibility(entry, visibility, pos)
                if scope:
                    entry.type.scope = scope
                    self.type_entries.append(entry)
        if self.is_cpp_class_scope:
            entry.type.namespace = self.outer_scope.lookup(self.name).type
        return entry

    def declare_cpp_class(self, name, scope,
            pos, cname = None, base_classes = (),
            visibility = 'extern', templates = None):
        if cname is None:
            cname = name if self.in_cinclude or visibility != 'private' else self.mangle(Naming.type_prefix, name)
        base_classes = list(base_classes)
        entry = self.lookup_here(name)
        if not entry:
            type = PyrexTypes.CppClassType(
                name, scope, cname, base_classes, templates = templates)
            entry = self.declare_type(name, type, pos, cname,
                visibility = visibility, defining = scope is not None)
            self.sue_entries.append(entry)
        else:
            if not (entry.is_type and entry.type.is_cpp_class):
                error(pos, "'%s' redeclared " % name)
                entry.already_declared_here()
                return None
            if scope and entry.type.scope:
                warning(pos, "'%s' already defined  (ignoring second definition)" % name, 0)
            else:
                if scope:
                    entry.type.scope = scope
                    self.type_entries.append(entry)
            if base_classes:
                if entry.type.base_classes and entry.type.base_classes != base_classes:
                    error(pos, "Base type does not match previous declaration")
                    entry.already_declared_here()
                else:
                    entry.type.base_classes = base_classes
            if templates or entry.type.templates:
                if templates != entry.type.templates:
                    error(pos, "Template parameters do not match previous declaration")
                    entry.already_declared_here()

        def declare_inherited_attributes(entry, base_classes):
            for base_class in base_classes:
                if base_class is PyrexTypes.error_type:
                    continue
                if base_class.scope is None:
                    error(pos, "Cannot inherit from incomplete type")
                else:
                    declare_inherited_attributes(entry, base_class.base_classes)
                    entry.type.scope.declare_inherited_cpp_attributes(base_class)
        if scope:
            declare_inherited_attributes(entry, base_classes)
            scope.declare_var(name="this", cname="this", type=PyrexTypes.CPtrType(entry.type), pos=entry.pos)
        if self.is_cpp_class_scope:
            entry.type.namespace = self.outer_scope.lookup(self.name).type
        return entry

    def check_previous_typedef_flag(self, entry, typedef_flag, pos):
        if typedef_flag != entry.type.typedef_flag:
            error(pos, "'%s' previously declared using '%s'" % (
                entry.name, ("cdef", "ctypedef")[entry.type.typedef_flag]))

    def check_previous_visibility(self, entry, visibility, pos):
        if entry.visibility != visibility:
            error(pos, "'%s' previously declared as '%s'" % (
                entry.name, entry.visibility))

    def declare_enum(self, name, pos, cname, scoped, typedef_flag,
            visibility='private', api=0, create_wrapper=0, doc=None):
        if name:
            if not cname:
                if (self.in_cinclude or visibility == 'public'
                        or visibility == 'extern' or api):
                    cname = name
                else:
                    cname = self.mangle(Naming.type_prefix, name)
            if self.is_cpp_class_scope:
                namespace = self.outer_scope.lookup(self.name).type
            else:
                namespace = None

            if scoped:
                type = PyrexTypes.CppScopedEnumType(name, cname, namespace, doc=doc)
            else:
                type = PyrexTypes.CEnumType(name, cname, typedef_flag, namespace, doc=doc)
        else:
            type = PyrexTypes.c_anon_enum_type
        entry = self.declare_type(name, type, pos, cname = cname,
            visibility = visibility, api = api)
        if scoped:
            entry.utility_code = Code.UtilityCode.load_cached("EnumClassDecl", "CppSupport.cpp")
            self.use_entry_utility_code(entry)
        entry.create_wrapper = create_wrapper
        entry.enum_values = []

        self.sue_entries.append(entry)
        return entry

    def declare_tuple_type(self, pos, components):
        return self.outer_scope.declare_tuple_type(pos, components)

    def declare_var(self, name, type, pos,
                    cname=None, visibility='private',
                    api=False, in_pxd=False, is_cdef=False, pytyping_modifiers=None):
        # Add an entry for a variable.
        if not cname:
            if visibility != 'private' or api:
                cname = name
            else:
                cname = self.mangle(Naming.var_prefix, name)
        entry = self.declare(name, cname, type, pos, visibility)
        entry.is_variable = 1
        if type.is_cpp_class and visibility != 'extern':
            if self.directives['cpp_locals']:
                entry.make_cpp_optional()
            else:
                type.check_nullary_constructor(pos)
        if in_pxd and visibility != 'extern':
            entry.defined_in_pxd = 1
            entry.used = 1
        if api:
            entry.api = 1
            entry.used = 1
        if pytyping_modifiers:
            entry.pytyping_modifiers = pytyping_modifiers
        return entry

    def _reject_pytyping_modifiers(self, pos, modifiers, allowed=()):
        if not modifiers:
            return
        for modifier in modifiers:
            if modifier not in allowed:
                error(pos, "Modifier '%s' is not allowed here." % modifier)

    def declare_assignment_expression_target(self, name, type, pos):
        # In most cases declares the variable as normal.
        # For generator expressions and comprehensions the variable is declared in their parent
        return self.declare_var(name, type, pos)

    def declare_builtin(self, name, pos):
        name = self.mangle_class_private_name(name)
        return self.outer_scope.declare_builtin(name, pos)

    def _declare_pyfunction(self, name:str, pos:int|None, visibility:str='extern', entry:Entry|None=None):
        if entry and not entry.type.is_cfunction:
            error(pos, "'%s' already declared" % name)
            error(entry.pos, "Previous declaration is here")
        entry = self.declare_var(name, py_object_type, pos, visibility=visibility)
        entry.signature = pyfunction_signature
        self.pyfunc_entries.append(entry)
        return entry

    def declare_pyfunction(self, name, pos, allow_redefine=False, visibility='extern', entry:"Scope|Entry|None"=None):
        # Add an entry for a Python function.
        entry = self.lookup_here(name)
        if not allow_redefine:
            return self._declare_pyfunction(name, pos, visibility=visibility, entry=entry)
        if entry:
            if entry.type.is_unspecified:
                entry.type = py_object_type
            elif entry.type is not py_object_type:
                return self._declare_pyfunction(name, pos, visibility=visibility, entry=entry)
        else:  # declare entry stub
            self.declare_var(name, py_object_type, pos, visibility=visibility)
        entry = self.declare_var(None, py_object_type, pos,
                                 cname=name, visibility='private')
        entry.name = EncodedString(name)
        entry.qualified_name = self.qualify_name(name)
        entry.signature = pyfunction_signature
        entry.is_anonymous = True
        return entry

    def declare_lambda_function(self, lambda_name, pos):
        # Add an entry for an anonymous Python function.
        func_cname = self.mangle(Naming.lambda_func_prefix + 'funcdef_', lambda_name)
        pymethdef_cname = self.mangle(Naming.lambda_func_prefix + 'methdef_', lambda_name)
        qualified_name = self.qualify_name(lambda_name)

        entry = self.declare(None, func_cname, py_object_type, pos, 'private')
        entry.name = EncodedString(lambda_name)
        entry.qualified_name = qualified_name
        entry.pymethdef_cname = pymethdef_cname
        entry.func_cname = func_cname
        entry.signature = pyfunction_signature
        entry.is_anonymous = True
        return entry

    def add_lambda_def(self, def_node):
        self.lambda_defs.append(def_node)

    def register_pyfunction(self, entry):
        self.pyfunc_entries.append(entry)

    def declare_cfunction(self, name, type, pos,
                          cname=None, visibility='private', api=0, in_pxd=0,
                          defining=0, modifiers=(), utility_code=None, overridable=False):
        # Add an entry for a C function.
        if not cname:
            cname = name if visibility != 'private' or api else self.mangle(Naming.func_prefix, name)
        inline_in_pxd = 'inline' in modifiers and in_pxd and defining
        if inline_in_pxd:
            # in_pxd does special things that we don't want to apply to inline functions
            in_pxd = False
        entry = self.lookup_here(name)
        if entry:
            if not in_pxd and visibility != entry.visibility and visibility == 'extern':
                # Previously declared, but now extern => treat this
                # as implementing the function, using the new cname
                defining = True
                visibility = entry.visibility
                entry.cname = cname
                entry.func_cname = cname
            if visibility != 'private' and visibility != entry.visibility:
                warning(pos, "Function '%s' previously declared as '%s', now as '%s'" % (
                    name, entry.visibility, visibility), 1)
            if overridable != entry.is_overridable:
                warning(pos, "Function '%s' previously declared as '%s'" % (
                    name, 'cpdef' if overridable else 'cdef'), 1)
            if entry.type.same_as(type):
                # Fix with_gil vs nogil.
                entry.type = entry.type.with_with_gil(type.with_gil)
            else:
                if visibility == 'extern' and entry.visibility == 'extern':
                    can_override = self.is_builtin_scope
                    if self.is_cpp():
                        can_override = True
                    elif cname and not can_override:
                        # if all alternatives have different cnames,
                        # it's safe to allow signature overrides
                        for alt_entry in entry.all_alternatives():
                            if not alt_entry.cname or cname == alt_entry.cname:
                                break  # cname not unique!
                        else:
                            can_override = True
                    if can_override:
                        temp = self.add_cfunction(name, type, pos, cname, visibility, modifiers)
                        temp.overloaded_alternatives = entry.all_alternatives()
                        if entry.specialiser is not None:
                            temp.specialiser = entry.specialiser
                        entry = temp
                    else:
                        warning(pos, "Function signature does not match previous declaration", 1)
                        entry.type = type
                elif not in_pxd and entry.defined_in_pxd and type.compatible_signature_with(entry.type):
                    # TODO: check that this was done by a signature optimisation and not a user error.
                    #warning(pos, "Function signature does not match previous declaration", 1)

                    # Cython can't assume anything about cimported functions declared without
                    # an exception value. This is a performance problem mainly for nogil functions.
                    if entry.type.nogil and entry.type.exception_value is None and type.exception_value:
                        performance_hint(
                            entry.pos,
                            f"No exception value declared for '{entry.name}' in pxd file.\n"
                            "Users cimporting this function and calling it without the gil "
                            "will always require an exception check.\n"
                            "Suggest adding an explicit exception value.",
                            self)
                    entry.type = type
                else:
                    error(pos, "Function signature does not match previous declaration")
        else:
            entry = self.add_cfunction(name, type, pos, cname, visibility, modifiers)
            entry.func_cname = cname
            entry.is_overridable = overridable
        if inline_in_pxd:
            entry.inline_func_in_pxd = True
        if in_pxd and visibility != 'extern':
            entry.defined_in_pxd = 1
        if api:
            entry.api = 1
        if not defining and not in_pxd and visibility != 'extern':
            error(pos, "Non-extern C function '%s' declared but not defined" % name)
        if defining:
            entry.is_implemented = True
        if modifiers:
            entry.func_modifiers = modifiers
        if utility_code:
            assert not entry.utility_code, "duplicate utility code definition in entry %s (%s)" % (name, cname)
            entry.utility_code = utility_code
        if overridable:
            # names of cpdef functions can be used as variables and can be assigned to
            var_entry = Entry(name, cname, py_object_type)   # FIXME: cname?
            var_entry.qualified_name = self.qualify_name(name)
            var_entry.is_variable = 1
            var_entry.is_pyglobal = 1
            var_entry.scope = entry.scope
            entry.as_variable = var_entry
        type.entry = entry
        if (type.exception_check and type.exception_value is None and type.nogil and
                not pos[0].in_utility_code and
                # don't warn about external functions here - the user likely can't do anything
                defining and not in_pxd and not inline_in_pxd):
            PyrexTypes.write_noexcept_performance_hint(
                pos, self, function_name=name, void_return=type.return_type.is_void)
        return entry

    def declare_cgetter(self, name, return_type, pos=None, cname=None,
                        visibility="private", modifiers=(), defining=False, **cfunc_type_config):
        assert all(
            k in ('exception_value', 'exception_check', 'nogil', 'with_gil', 'is_const_method', 'is_static_method')
            for k in cfunc_type_config
        )
        cfunc_type = PyrexTypes.CFuncType(
            return_type,
            [PyrexTypes.CFuncTypeArg("self", self.parent_type, None)],
            **cfunc_type_config)
        entry = self.declare_cfunction(
            name, cfunc_type, pos, cname=None, visibility=visibility, modifiers=modifiers, defining=defining)
        entry.is_cgetter = True
        if cname is not None:
            entry.func_cname = cname
        return entry

    def add_cfunction(self, name, type, pos, cname, visibility, modifiers, inherited=False):
        # Add a C function entry without giving it a func_cname.
        entry = self.declare(name, cname, type, pos, visibility)
        entry.is_cfunction = 1
        if modifiers:
            entry.func_modifiers = modifiers
        if inherited or type.is_fused:
            self.cfunc_entries.append(entry)
        else:
            # For backwards compatibility reasons, we must keep all non-fused methods
            # before all fused methods, but separately for each type.
            i = len(self.cfunc_entries)
            for cfunc_entry in reversed(self.cfunc_entries):
                if cfunc_entry.is_inherited or not cfunc_entry.type.is_fused:
                    break
                i -= 1
            self.cfunc_entries.insert(i, entry)
        return entry

    def find(self, name, pos):
        # Look up name, report error if not found.
        entry = self.lookup(name)
        if entry:
            return entry
        error(pos, "'%s' is not declared" % name)
        return None

    def find_imported_module(self, path, pos):
        # Look up qualified name, must be a module, report error if not found.
        # Path is a list of names.
        scope = self
        for name in path:
            entry = scope.find(name, pos)
            if not entry:
                return None
            if entry.as_module:
                scope = entry.as_module
            else:
                error(pos, "'%s' is not a cimported module" % '.'.join(path))
                return None
        return scope

    def lookup(self, name):
        # Look up name in this scope or an enclosing one.
        # Return None if not found.

        mangled_name = self.mangle_class_private_name(name)
        entry = (self.lookup_here(name)  # lookup here also does mangling
                or (self.outer_scope and self.outer_scope.lookup(mangled_name))
                or None)
        if entry:
            return entry

        # look up the original name in the outer scope
        # Not strictly Python behaviour but see https://github.com/cython/cython/issues/3544
        entry = (self.outer_scope and self.outer_scope.lookup(name)) or None
        if entry and entry.is_pyglobal:
            self._emit_class_private_warning(entry.pos, name)
        return entry

    def lookup_here(self, name) -> "Entry|None":
        # Look up in this scope only, return None if not found.

        entry = self.entries.get(self.mangle_class_private_name(name), None)
        if entry:
            return entry
        # Also check the unmangled name in the current scope
        # (even if mangling should give us something else).
        # This is to support things like global __foo which makes a declaration for __foo
        return self.entries.get(name, None)

    def lookup_here_unmangled(self, name):
        return self.entries.get(name, None)

    def lookup_assignment_expression_target(self, name):
        # For most cases behaves like "lookup_here".
        # However, it does look outwards for comprehension and generator expression scopes
        return self.lookup_here(name)

    def lookup_target(self, name):
        # Look up name in this scope only. Declare as Python
        # variable if not found.
        entry = self.lookup_here(name)
        if not entry:
            entry = self.lookup_here_unmangled(name)
            if entry and entry.is_pyglobal:
                self._emit_class_private_warning(entry.pos, name)
        if not entry:
            entry = self.declare_var(name, py_object_type, None)
        return entry

    def _type_or_specialized_type_from_entry(self, entry):
        if entry and entry.is_type:
            if entry.type.is_fused and self.fused_to_specific:
                return entry.type.specialize(self.fused_to_specific)
            return entry.type

    def lookup_type(self, name):
        entry = self.lookup(name)
        # The logic here is:
        #  1. if entry is a type then return it (and maybe specialize it)
        #  2. if the entry comes from a known standard library import then follow that
        #  3. repeat step 1 with the (possibly) updated entry

        tp = self._type_or_specialized_type_from_entry(entry)
        if tp:
            return tp
        # allow us to find types from the "typing" module and similar
        if entry and entry.known_standard_library_import:
            from .Builtin import get_known_standard_library_entry
            entry = get_known_standard_library_entry(entry.known_standard_library_import)
        return self._type_or_specialized_type_from_entry(entry)

    def lookup_operator(self, operator, operands):
        if operands[0].type.is_cpp_class:
            obj_type = operands[0].type
            method = obj_type.scope.lookup("operator%s" % operator)
            if method is not None:
                arg_types = [arg.type for arg in operands[1:]]
                res = PyrexTypes.best_match(arg_types, method.all_alternatives())
                if res is not None:
                    return res
        function = self.lookup("operator%s" % operator)
        function_alternatives = []
        if function is not None:
            function_alternatives = function.all_alternatives()

        # look-up nonmember methods listed within a class
        method_alternatives = []
        if len(operands) == 2:  # binary operators only
            for n in range(2):
                if operands[n].type.is_cpp_class:
                    obj_type = operands[n].type
                    method = obj_type.scope.lookup("operator%s" % operator)
                    if method is not None:
                        method_alternatives += method.all_alternatives()

        if (not method_alternatives) and (not function_alternatives):
            return None

        # select the unique alternatives
        all_alternatives = list(set(method_alternatives + function_alternatives))

        return PyrexTypes.best_match([arg.type for arg in operands],
                                     all_alternatives)

    def lookup_operator_for_types(self, pos, operator, types):
        from .Nodes import Node
        class FakeOperand(Node):
            pass
        operands = [FakeOperand(pos, type=type) for type in types]
        return self.lookup_operator(operator, operands)

    def _emit_class_private_warning(self, pos, name):
        warning(pos, "Global name %s matched from within class scope "
                            "in contradiction to Python 'class private name' rules. "
                            "This may change in a future release." % name, 1)

    def use_utility_code(self, new_code):
        self.global_scope().use_utility_code(new_code)

    def use_entry_utility_code(self, entry):
        self.global_scope().use_entry_utility_code(entry)

    def defines_any(self, names):
        # Test whether any of the given names are defined in this scope.
        for name in names:
            if name in self.entries:
                return 1
        return 0

    def defines_any_special(self, names):
        # Test whether any of the given names are defined as special methods in this scope.
        for name in names:
            if name in self.entries and self.entries[name].is_special:
                return 1
        return 0

    def infer_types(self):
        from .TypeInference import get_type_inferer
        get_type_inferer().infer_types(self)

    def is_cpp(self):
        return self.outer_scope and self.outer_scope.is_cpp()

    def add_include_file(self, filename, verbatim_include=None, late=False):
        self.outer_scope.add_include_file(filename, verbatim_include, late)

    def name_in_module_state(self, cname):
        # TODO - override to give more choices depending on the type of scope
        # e.g. slot, function, method
        return f"{Naming.modulestateglobal_cname}->{cname}"

    def find_shared_usages_of_type(self, type_check_predicate, _seen_scopes=None):
        if _seen_scopes is None:
            _seen_scopes = set()
        include_all_entries = not self.is_module_scope
        for entry in self.entries.values():
            if not (include_all_entries or entry.defined_in_pxd or entry.visibility == "public" or entry.api):
                continue
            entry_subtypes = PyrexTypes.get_all_subtypes(entry.type)
            if any(type_check_predicate(sub_tp) for sub_tp in entry_subtypes):
                return True
            type_scope = getattr(entry.type, "scope", None)
            if type_scope is None or type_scope in _seen_scopes:
                continue
            _seen_scopes.add(type_scope)
            if type_scope.find_shared_usages_of_type(type_check_predicate, _seen_scopes):
                return True
        return False


class PreImportScope(Scope):
    namespace_cname = Naming.preimport_cname
    def __init__(self):
        Scope.__init__(self, Options.pre_import, None, None)
    def declare_builtin(self, name, pos):
        entry = self.declare(name, name, py_object_type, pos, 'private')
        entry.is_variable = True
        entry.is_pyglobal = True
        return entry

class BuiltinScope(Scope):
    #  The builtin namespace.

    is_builtin_scope = True

    def __init__(self):
        if Options.DEFAULT_COMPILATION_OPTIONS.pre_import is None:
            Scope.__init__(self, "__builtin__", None, None)
        else:
            Scope.__init__(self, "__builtin__", PreImportScope(), None)
        self.type_names = {}

    def lookup(self, name, language_level=None):
        # 'language_level' is passed by ModuleScope
        if name == 'unicode' or name == 'basestring':
            # Keep recognising 'unicode' and 'basestring' in legacy code but map them to 'str'.
            name = 'str'
        elif name == 'long' and language_level == 2:
            # Keep recognising 'long' in legacy Py2 code but map it to 'int'.
            name = 'int'
        return Scope.lookup(self, name)

    def declare_builtin(self, name, pos):
        if name not in Code.KNOWN_PYTHON_BUILTINS:
            if self.outer_scope is not None:
                return self.outer_scope.declare_builtin(name, pos)

            if Options.DEFAULT_COMPILATION_OPTIONS.error_on_unknown_names:
                error(pos, f"undeclared name not builtin: {name}")
            else:
                warning(pos, f"undeclared name not builtin: {name}", 2)
        return None

    def declare_builtin_cfunction(self, name, type, cname, python_equiv=None, utility_code=None, specialiser=None):
        # If python_equiv == "*", the Python equivalent has the same name
        # as the entry, otherwise it has the name specified by python_equiv.
        name = EncodedString(name)
        entry = self.declare_cfunction(name, type, None, cname, visibility='extern', utility_code=utility_code)
        if specialiser is not None:
            entry.specialiser = specialiser
        if python_equiv:
            python_equiv = name if python_equiv == "*" else EncodedString(python_equiv)
            var_entry = Entry(python_equiv, python_equiv, py_object_type)
            var_entry.qualified_name = self.qualify_name(name)
            var_entry.is_variable = 1
            var_entry.is_builtin = 1
            var_entry.utility_code = utility_code
            var_entry.scope = entry.scope
            entry.as_variable = var_entry
        return entry

    def declare_builtin_type(self, name, cname,
                             objstruct_cname=None, type_class=PyrexTypes.BuiltinObjectType,
                             utility_code=None):
        name = EncodedString(name)
        type = type_class(name, cname, objstruct_cname)
        scope = CClassScope(name, outer_scope=None, visibility='extern', parent_type=type)
        scope.directives = Directives()
        type.set_scope(scope)
        self.type_names[name] = 1

        entry = self.declare_type(name, type, None, visibility='extern')
        if utility_code:
            entry.utility_code = utility_code
        if name == 'range' and 'xrange' not in self.entries:
            # Keep supporting legacy Py2 'xrange' because it's still in use.
            self.entries['xrange'] = entry

        var_entry = Entry(
            name=entry.name,
            type=self.lookup('type').type,  # make sure "type" is the first type declared...
            pos=entry.pos,
            cname=entry.type.typeptr_cname,
        )
        var_entry.qualified_name = self.qualify_name(name)
        var_entry.is_variable = 1
        var_entry.is_cglobal = 1
        var_entry.is_readonly = 1
        var_entry.is_builtin = 1
        var_entry.scope = self
        if Options.DEFAULT_COMPILATION_OPTIONS.cache_builtins:
            var_entry.is_const = True
        if utility_code:
            var_entry.utility_code = utility_code
        entry.as_variable = var_entry

        return type

    def builtin_scope(self):
        return self

    def handle_already_declared_name(self, name, cname, type, pos, visibility, copy_entry=False):
        # Overriding is OK in the builtin scope
        return None


const_counter = 1  # As a temporary solution for compiling code in pxds

class ModuleScope(Scope):
    # module_name          string             Python name of the module
    # module_cname         string             C name of Python module object
    # #module_dict_cname   string             C name of module dict object
    # method_table_cname   string             C name of method table
    # doc                  string             Module doc string
    # doc_cname            string             C name of module doc string
    # utility_code_list    [UtilityCode]      Queuing utility codes for forwarding to Code.py
    # c_includes           {key: IncludeCode} C headers or verbatim code to be generated
    #                                         See process_include() for more documentation
    # identifier_to_entry  {string : Entry}   Map identifier string const to entry
    # context              Context
    # parent_module        Scope              Parent in the import namespace
    # module_entries       {string : Entry}   For cimport statements
    # type_names           {string : 1}       Set of type names (used during parsing)
    # included_files       [string]           Cython sources included with 'include'
    # pxd_file_loaded      boolean            Corresponding .pxd file has been processed
    # cimported_modules    [ModuleScope]      Modules imported with cimport
    # types_imported       {PyrexType}        Set of types for which import code generated
    # has_import_star      boolean            Module contains import *
    # cpp                  boolean            Compiling a C++ file
    # is_cython_builtin    boolean            Is this the Cython builtin scope (or a child scope)
    # is_package           boolean            Is this a package module? (__init__)

    is_module_scope = 1
    has_import_star = 0
    is_cython_builtin = 0
    old_style_globals = 0
    namespace_cname_is_type = False
    directives:Directives
    scope: Scope
    scope_predefined_names = [
        '__builtins__', '__name__', '__file__', '__doc__', '__path__',
        '__spec__', '__loader__', '__package__', '__cached__',
    ]

    def __init__(self, name, parent_module, context, is_package=False):
        from . import Builtin
        self.parent_module = parent_module
        outer_scope = Builtin.builtin_scope
        Scope.__init__(self, name, outer_scope, parent_module)
        self.is_package = is_package
        self.module_name = name
        self.module_name = EncodedString(self.module_name)
        self._context = context
        self.module_cname = Naming.module_cname
        self.module_dict_cname = Naming.moddict_cname
        self.method_table_cname = Naming.methtable_cname
        self.doc = ""
        self.doc_cname = Naming.moddoc_cname
        self.utility_code_list: list[Code.UtilityCode] = []
        self.module_entries = {}
        self.c_includes = {}
        self.type_names = dict(outer_scope.type_names)
        self.pxd_file_loaded = 0
        self.cimported_modules = []
        self.types_imported = set()
        self.included_files = []
        self.has_extern_class = 0
        self.cached_builtins = []
        self.undeclared_cached_builtins = []
        self.namespace_cname = self.module_cname
        self._cached_tuple_types = {}
        self._cached_defaults_c_class_entries = {}
        self.process_include(Code.IncludeCode("Python.h", initial=True))

    def qualifying_scope(self):
        return self.parent_module

    @property
    def context(self):
        return self._context

    def global_scope(self):
        return self

    def lookup(self, name, language_level=None):
        entry = self.lookup_here(name)
        if entry is not None:
            return entry

        if language_level is None:
            language_level = self.context.language_level if self.context is not None else 3
        return self.outer_scope.lookup(name, language_level=language_level)

    def declare_tuple_type(self, pos, components):
        components = tuple(components)
        try:
            ttype = self._cached_tuple_types[components]
        except KeyError:
            ttype = self._cached_tuple_types[components] = PyrexTypes.c_tuple_type(components)
        cname = ttype.cname
        entry = self.lookup_here(cname)
        if not entry:
            scope = StructOrUnionScope(cname)
            for ix, component in enumerate(components):
                scope.declare_var(name="f%s" % ix, type=component, pos=pos)
            struct_entry = self.declare_struct_or_union(
                cname + '_struct', 'struct', scope, typedef_flag=True, pos=pos, cname=cname)
            self.type_entries.remove(struct_entry)
            ttype.struct_entry = struct_entry
            entry = self.declare_type(cname, ttype, pos, cname)
        ttype.entry = entry
        return entry

    def declare_defaults_c_class(self, pos, components):
        # returns an entry (for the c-class)
        components = tuple(components)
        try:
            return self._cached_defaults_c_class_entries[components]
        except KeyError:
            pass

        cname = self.next_id(Naming.defaults_struct_prefix)
        cname = EncodedString(cname)
        entry = self._cached_defaults_c_class_entries[components] = self.declare_c_class(
            cname, pos, defining=True, implementing=True,
            objstruct_cname=cname)
        self.check_c_class(entry)
        entry.type.is_final_type = True
        scope = entry.type.scope
        scope.is_internal = True
        scope.is_defaults_class_scope = True

        # zero pad the argument number so they can be sorted
        num_zeros = len(str(len(components)))
        build_argname = ("arg{:0>%dd}" % num_zeros).format
        for n, type_ in enumerate(components):
            arg_name = EncodedString(build_argname(n))
            scope.declare_var(arg_name, type_, pos=None, is_cdef=True)
        return entry

    def declare_builtin(self, name, pos):
        if name not in Code.KNOWN_PYTHON_BUILTINS \
               and name not in Code.renamed_py2_builtins_map \
               and name not in Code.uncachable_builtins:
            if self.has_import_star:
                entry = self.declare_var(name, py_object_type, pos)
                return entry
            if Options.DEFAULT_COMPILATION_OPTIONS.error_on_unknown_names:
                error(pos, "undeclared name not builtin: %s" % name)
            else:
                warning(pos, "undeclared name not builtin: %s" % name, 2)
            # unknown - assume it's builtin and look it up at runtime
            entry = self.declare(name, None, py_object_type, pos, 'private')
            entry.is_builtin = 1
            return entry
        if Options.DEFAULT_COMPILATION_OPTIONS.cache_builtins:
            for entry in self.cached_builtins:
                if entry.name == name:
                    return entry
        if name == 'globals' and not self.old_style_globals:
            return self.outer_scope.lookup('__Pyx_Globals')
        entry = self.declare(None, None, py_object_type, pos, 'private')
        if Options.DEFAULT_COMPILATION_OPTIONS.cache_builtins and name not in Code.uncachable_builtins:
            entry.is_builtin = 1
            entry.is_const = 1  # cached
            entry.name = name
            entry.cname = Naming.builtin_prefix + name
            self.cached_builtins.append(entry)
            self.undeclared_cached_builtins.append(entry)
        else:
            entry.is_builtin = 1
            entry.name = name
        entry.qualified_name = self.builtin_scope().qualify_name(name)
        return entry

    def find_module(self, module_name, pos, relative_level=-1):
        # Find a module in the import namespace, interpreting
        # relative imports relative to this module's parent.
        # Finds and parses the module's .pxd file if the module
        # has not been referenced before.
        is_relative_import = relative_level is not None and relative_level > 0
        from_module = None
        absolute_fallback = False
        if relative_level is not None and relative_level > 0:
            # explicit relative cimport
            # error of going beyond top-level is handled in cimport node
            from_module = self

            top_level = 1 if self.is_package else 0
            # * top_level == 1 when file is __init__.pyx, current package (from_module) is the current module
            #   i.e. dot in `from . import ...` points to the current package
            # * top_level == 0 when file is regular module, current package (from_module) is parent module
            #   i.e. dot in `from . import ...` points to the package where module is placed
            while relative_level > top_level and from_module:
                from_module = from_module.parent_module
                relative_level -= 1

        elif relative_level != 0:
            # -1 or None: try relative cimport first, then absolute
            from_module = self.parent_module
            absolute_fallback = True

        module_scope = self.global_scope()
        return module_scope.context.find_module(
            module_name, from_module=from_module, pos=pos, absolute_fallback=absolute_fallback, relative_import=is_relative_import)

    def find_submodule(self, name, as_package=False):
        # Find and return scope for a submodule of this module,
        # creating a new empty one if necessary. Doesn't parse .pxd.
        if '.' in name:
            name, submodule = name.split('.', 1)
        else:
            submodule = None
        scope = self.lookup_submodule(name)
        if not scope:
            scope = ModuleScope(name, parent_module=self, context=self.context, is_package=True if submodule else as_package)
            self.module_entries[name] = scope
        if submodule:
            scope = scope.find_submodule(submodule, as_package=as_package)
        return scope

    def lookup_submodule(self, name):
        # Return scope for submodule of this module, or None.
        if '.' in name:
            name, submodule = name.split('.', 1)
        else:
            submodule = None
        module = self.module_entries.get(name, None)
        if submodule and module is not None:
            module = module.lookup_submodule(submodule)
        return module

    def add_include_file(self, filename, verbatim_include=None, late=False):
        """Add `filename` as include file. Add `verbatim_include` as
        verbatim text in the C file.
        Both `filename` and `verbatim_include` can be `None` or empty.
        """
        inc = Code.IncludeCode(filename, verbatim_include, late=late)
        self.process_include(inc)

    def process_include(self, inc):
        """Add `inc`, which is an instance of `IncludeCode`, to this
        `ModuleScope`. This either adds a new element to the
        `c_includes` dict or it updates an existing entry.

        In detail: the values of the dict `self.c_includes` are
        instances of `IncludeCode` containing the code to be put in the
        generated C file. The keys of the dict are needed to ensure
        uniqueness in two ways: if an include file is specified in
        multiple "cdef extern" blocks, only one `#include` statement is
        generated. Second, the same include might occur multiple times
        if we find it through multiple "cimport" paths. So we use the
        generated code (of the form `#include "header.h"`) as dict key.

        If verbatim code does not belong to any include file (i.e. it
        was put in a `cdef extern from *` block), then we use a unique
        dict key: namely, the `sortkey()`.

        One `IncludeCode` object can contain multiple pieces of C code:
        one optional "main piece" for the include file and several other
        pieces for the verbatim code. The `IncludeCode.dict_update`
        method merges the pieces of two different `IncludeCode` objects
        if needed.
        """
        key = inc.mainpiece()
        if key is None:
            key = inc.sortkey()
        inc.dict_update(self.c_includes, key)
        inc = self.c_includes[key]

    def add_imported_module(self, scope):
        if scope not in self.cimported_modules:
            for inc in scope.c_includes.values():
                self.process_include(inc)
            self.cimported_modules.append(scope)
            for m in scope.cimported_modules:
                self.add_imported_module(m)

    def add_imported_entry(self, name, entry, pos):
        if entry.is_pyglobal:
            # Allow cimports to follow imports.
            entry.is_variable = True
        if entry not in self.entries:
            self.entries[name] = entry
        else:
            warning(pos, "'%s' redeclared  " % name, 0)

    def declare_module(self, name, scope, pos):
        # Declare a cimported module. This is represented as a
        # Python module-level variable entry with a module
        # scope attached to it. Reports an error and returns
        # None if previously declared as something else.
        entry = self.lookup_here(name)
        if entry:
            if entry.is_pyglobal and entry.as_module is scope:
                return entry  # Already declared as the same module
            if not (entry.is_pyglobal and not entry.as_module):
                # SAGE -- I put this here so Pyrex
                # cimport's work across directories.
                # Currently it tries to multiply define
                # every module appearing in an import list.
                # It shouldn't be an error for a module
                # name to appear again, and indeed the generated
                # code compiles fine.
                return entry
        else:
            entry = self.declare_var(name, py_object_type, pos)
            entry.is_variable = 0
        entry.as_module = scope
        self.add_imported_module(scope)
        return entry

    def declare_var(self, name, type, pos,
                    cname=None, visibility='private',
                    api=False, in_pxd=False, is_cdef=False, pytyping_modifiers=None):
        # Add an entry for a global variable. If it is a Python
        # object type, and not declared with cdef, it will live
        # in the module dictionary, otherwise it will be a C
        # global variable.
        if visibility not in ('private', 'public', 'extern'):
            error(pos, "Module-level variable cannot be declared %s" % visibility)
        self._reject_pytyping_modifiers(pos, pytyping_modifiers, ('typing.Optional',))  # let's allow at least this one
        if not is_cdef:
            if type is unspecified_type:
                type = py_object_type
            if not (type.is_pyobject and not type.is_extension_type):
                raise InternalError(
                    "Non-cdef global variable is not a generic Python object")
        if (is_cdef and visibility != "extern"
                and self.directives['subinterpreters_compatible'] != "no"):
            extra_warning = ""
            pyobject_warning = ""
            if type.is_pyobject:
                extra_warning = "\nPython objects should not be shared between interpreters"
                pyobject_warning = "Python "
            warning(
                pos,
                f"Global cdef {pyobject_warning}variable used with subinterpreter support enabled.\n"
                "This variable is not currently in the per-interpreter module state "
                "but this will likely change in future releases." +
                extra_warning,
                2+(1 if extra_warning else 0))

        if not cname:
            defining = not in_pxd
            if visibility == 'extern' or (visibility == 'public' and defining):
                cname = name
            else:
                cname = self.mangle(Naming.var_prefix, name)

        entry = self.lookup_here(name)
        if entry and entry.defined_in_pxd:
            #if visibility != 'private' and visibility != entry.visibility:
            #    warning(pos, "Variable '%s' previously declared as '%s'" % (name, entry.visibility), 1)
            if not entry.type.same_as(type) and visibility == 'extern' and entry.visibility == 'extern':
                warning(pos, "Variable '%s' type does not match previous declaration" % name, 1)
                entry.type = type
                #else:
                #    error(pos, "Variable '%s' type does not match previous declaration" % name)
            if entry.visibility != "private":
                mangled_cname = self.mangle(Naming.var_prefix, name)
                if entry.cname == mangled_cname:
                    cname = name
                    entry.cname = name
            if not entry.is_implemented:
                entry.is_implemented = True
                return entry

        entry = Scope.declare_var(self, name, type, pos,
                                  cname=cname, visibility=visibility,
                                  api=api, in_pxd=in_pxd, is_cdef=is_cdef, pytyping_modifiers=pytyping_modifiers)
        if is_cdef:
            entry.is_cglobal = 1
            if entry.type.declaration_value:
                entry.init = entry.type.declaration_value
            self.var_entries.append(entry)
        else:
            entry.is_pyglobal = 1
        if Directives.cimport_from_pyx:
            entry.used = 1
        return entry

    def declare_cfunction(self, name, type, pos,
                          cname=None, visibility='private', api=0, in_pxd=0,
                          defining=0, modifiers=(), utility_code=None, overridable=False):
        if not defining and 'inline' in modifiers:
            # TODO(github/1736): Make this an error.
            warning(pos, "Declarations should not be declared inline.", 1)
        # Add an entry for a C function.
        if not cname:
            if visibility == 'extern' or (visibility == 'public' and defining):
                cname = name
            else:
                cname = self.mangle(Naming.func_prefix, name)
        if visibility == 'extern' and type.optional_arg_count:
            error(pos, "Extern functions cannot have default arguments values.")
        entry = self.lookup_here(name)
        if entry and entry.defined_in_pxd and entry.visibility != "private":
            mangled_cname = self.mangle(Naming.func_prefix, name)
            if entry.cname == mangled_cname:
                cname = name
                entry.cname = cname
                entry.func_cname = cname
        entry = Scope.declare_cfunction(
            self, name, type, pos,
            cname=cname, visibility=visibility, api=api, in_pxd=in_pxd,
            defining=defining, modifiers=modifiers, utility_code=utility_code,
            overridable=overridable)
        return entry

    def declare_global(self, name, pos):
        entry = self.lookup_here(name)
        if not entry:
            self.declare_var(name, py_object_type, pos)

    def use_utility_code(self, new_code):
        if new_code is not None:
            self.utility_code_list.append(new_code)

    def use_entry_utility_code(self, entry):
        if entry is None:
            return
        if entry.utility_code:
            self.utility_code_list.append(entry.utility_code)

    def declare_c_class(self, name, pos, defining=0, implementing=0,
            module_name=None, base_type=None, objstruct_cname=None,
            typeobj_cname=None, typeptr_cname=None, visibility='private',
            typedef_flag=0, api=0, check_size=None,
            buffer_defaults=None, shadow=0):
        # If this is a non-extern typedef class, expose the typedef, but use
        # the non-typedef struct internally to avoid needing forward
        # declarations for anonymous structs.
        if typedef_flag and visibility != 'extern':
            if not (visibility == 'public' or api):
                warning(pos, "ctypedef only valid for 'extern' , 'public', and 'api'", 2)
            objtypedef_cname = objstruct_cname
            typedef_flag = 0
        else:
            objtypedef_cname = None
        #
        #  Look for previous declaration as a type
        #
        entry = self.lookup_here(name)
        if entry and not shadow:
            type = entry.type
            if not (entry.is_type and type.is_extension_type):
                entry = None  # Will cause redeclaration and produce an error
            else:
                scope = type.scope
                if typedef_flag and (not scope or scope.defined):
                    self.check_previous_typedef_flag(entry, typedef_flag, pos)
                if (scope and scope.defined) or (base_type and type.base_type) and base_type and base_type is not type.base_type:
                        error(pos, "Base type does not match previous declaration")
                if base_type and not type.base_type:
                    type.base_type = base_type
        #
        #  Make a new entry if needed
        #
        if not entry or shadow:
            type = PyrexTypes.PyExtensionType(
                name, typedef_flag, base_type, visibility == 'extern', check_size=check_size)
            type.pos = pos
            type.buffer_defaults = buffer_defaults
            if objtypedef_cname is not None:
                type.objtypedef_cname = objtypedef_cname
            if visibility == 'extern':
                type.module_name = module_name
            else:
                type.module_name = self.qualified_name
            if typeptr_cname:
                type.typeptr_cname = typeptr_cname
            else:
                type.typeptr_cname = self.mangle(Naming.typeptr_prefix, name)
            entry = self.declare_type(name, type, pos, visibility = visibility,
                defining = 0, shadow = shadow)
            entry.is_cclass = True
            if objstruct_cname:
                type.objstruct_cname = objstruct_cname
            elif not entry.in_cinclude:
                type.objstruct_cname = self.mangle(Naming.objstruct_prefix, name)
            else:
                error(entry.pos,
                    "Object name required for 'public' or 'extern' C class")
            self.attach_var_entry_to_c_class(entry)
            self.c_class_entries.append(entry)
        #
        #  Check for re-definition and create scope if needed
        #
        if not type.scope:
            if defining or implementing:
                scope = CClassScope(name = name, outer_scope = self,
                    visibility=visibility,
                    parent_type=type)
                scope.directives = self.directives.copy()
                if base_type and base_type.scope:
                    scope.declare_inherited_c_attributes(base_type.scope)
                type.set_scope(scope)
                self.type_entries.append(entry)
        else:
            if defining and type.scope.defined:
                error(pos, "C class '%s' already defined" % name)
            elif implementing and type.scope.implemented:
                error(pos, "C class '%s' already implemented" % name)
        #
        #  Fill in options, checking for compatibility with any previous declaration
        #
        if defining:
            entry.defined_in_pxd = 1
        if implementing:   # So that filenames in runtime exceptions refer to
            entry.pos = pos  # the .pyx file and not the .pxd file
        if visibility != 'private' and entry.visibility != visibility:
            error(pos, "Class '%s' previously declared as '%s'"
                % (name, entry.visibility))
        if api:
            entry.api = 1
        if objstruct_cname:
            if type.objstruct_cname and type.objstruct_cname != objstruct_cname:
                error(pos, "Object struct name differs from previous declaration")
            type.objstruct_cname = objstruct_cname
        if typeobj_cname:
            if type.typeobj_cname and type.typeobj_cname != typeobj_cname:
                error(pos, "Type object name differs from previous declaration")
            type.typeobj_cname = typeobj_cname

        if self.directives.get('final'):
            entry.type.is_final_type = True
        collection_type = self.directives.get('collection_type')
        if collection_type:
            from .UtilityCode import NonManglingModuleScope
            if not isinstance(self, NonManglingModuleScope):
                # TODO - DW would like to make it public, but I'm making it internal-only
                # for now to avoid adding new features without consensus
                error(pos, "'collection_type' is not a public cython directive")
        if collection_type == 'sequence':
            entry.type.has_sequence_flag = True

        # cdef classes are always exported, but we need to set it to
        # distinguish between unused Cython utility code extension classes
        entry.used = True

        #
        # Return new or existing entry
        #
        return entry

    def allocate_vtable_names(self, entry):
        #  If extension type has a vtable, allocate vtable struct and
        #  slot names for it.
        type = entry.type
        if type.base_type and type.base_type.vtabslot_cname:
            #print "...allocating vtabslot_cname because base type has one" ###
            type.vtabslot_cname = "%s.%s" % (
                Naming.obj_base_cname, type.base_type.vtabslot_cname)
        elif type.scope and type.scope.cfunc_entries:
            # one special case here: when inheriting from builtin
            # types, the methods may also be built-in, in which
            # case they won't need a vtable
            entry_count = len(type.scope.cfunc_entries)
            base_type = type.base_type
            while base_type:
                # FIXME: this will break if we ever get non-inherited C methods
                if not base_type.scope or entry_count > len(base_type.scope.cfunc_entries):
                    break
                if base_type.is_builtin_type:
                    # builtin base type defines all methods => no vtable needed
                    return
                base_type = base_type.base_type
            #print "...allocating vtabslot_cname because there are C methods" ###
            type.vtabslot_cname = Naming.vtabslot_cname
        if type.vtabslot_cname:
            #print "...allocating other vtable related cnames" ###
            type.vtabstruct_cname = self.mangle(Naming.vtabstruct_prefix, entry.name)
            type.vtabptr_cname = self.mangle(Naming.vtabptr_prefix, entry.name)

    def check_c_classes_pxd(self):
        # Performs post-analysis checking and finishing up of extension types
        # being implemented in this module. This is called only for the .pxd.
        #
        # Checks all extension types declared in this scope to
        # make sure that:
        #
        #    * The extension type is fully declared
        #
        # Also allocates a name for the vtable if needed.
        #
        for entry in self.c_class_entries:
            # Check defined
            if not entry.type.scope:
                error(entry.pos, "C class '%s' is declared but not defined" % entry.name)

    def check_c_class(self, entry):
        type = entry.type
        name = entry.name
        visibility = entry.visibility
        # Check defined
        if not type.scope:
            error(entry.pos, "C class '%s' is declared but not defined" % name)
        # Generate typeobj_cname
        if visibility != 'extern' and not type.typeobj_cname:
            type.typeobj_cname = self.mangle(Naming.typeobj_prefix, name)
        ## Generate typeptr_cname
        #type.typeptr_cname = self.mangle(Naming.typeptr_prefix, name)
        # Check C methods defined
        if type.scope:
            for method_entry in type.scope.cfunc_entries:
                if not method_entry.is_inherited and not method_entry.func_cname:
                    error(method_entry.pos, f"C method '{method_entry.name}' is declared but not defined")
        # Allocate vtable name if necessary
        if type.vtabslot_cname:
            #print "ModuleScope.check_c_classes: allocating vtable cname for", self ###
            type.vtable_cname = self.mangle(Naming.vtable_prefix, entry.name)

    def check_c_classes(self):
        # Performs post-analysis checking and finishing up of extension types
        # being implemented in this module. This is called only for the main
        # .pyx file scope, not for cimported .pxd scopes.
        #
        # Checks all extension types declared in this scope to
        # make sure that:
        #
        #    * The extension type is implemented
        #    * All required object and type names have been specified or generated
        #    * All non-inherited C methods are implemented
        #
        # Also allocates a name for the vtable if needed.
        #
        debug_check_c_classes = 0
        if debug_check_c_classes:
            print("Scope.check_c_classes: checking scope " + self.qualified_name)
        for entry in self.c_class_entries:
            if debug_check_c_classes:
                print("...entry %s %s" % (entry.name, entry))
                print("......type = ",  entry.type)
                print("......visibility = ", entry.visibility)
            self.check_c_class(entry)

    def check_c_functions(self):
        # Performs post-analysis checking making sure all
        # defined c functions are actually implemented.
        for name, entry in self.entries.items():
            if entry.is_cfunction and (entry.defined_in_pxd
                    and entry.scope is self
                    and entry.visibility != 'extern'
                    and not entry.in_cinclude
                    and not entry.is_implemented):
                error(entry.pos, f"Non-extern C function '{name}' declared but not defined")

    def attach_var_entry_to_c_class(self, entry):
        # The name of an extension class has to serve as both a type
        # name and a variable name holding the type object. It is
        # represented in the symbol table by a type entry with a
        # variable entry attached to it. For the variable entry,
        # we use a read-only C global variable whose name is an
        # expression that refers to the type object.
        from . import Builtin
        var_entry = Entry(name = entry.name,
            type = Builtin.type_type,
            pos = entry.pos,
            cname = entry.type.typeptr_cname)
        var_entry.qualified_name = entry.qualified_name
        var_entry.is_variable = 1
        var_entry.is_cglobal = 1
        var_entry.is_readonly = 1
        var_entry.is_cclass_var_entry = True
        var_entry.scope = entry.scope
        entry.as_variable = var_entry

    def is_cpp(self):
        return self.cpp

    def infer_types(self):
        from .TypeInference import PyObjectTypeInferer
        PyObjectTypeInferer().infer_types(self)


class LocalScope(Scope):
    is_local_scope = True

    # Does the function have a 'with gil:' block?
    has_with_gil_block = False

    # Transient attribute, used for symbol table variable declarations
    _in_with_gil_block = False

    def __init__(self, name, outer_scope, parent_scope = None):
        if parent_scope is None:
            parent_scope = outer_scope
        Scope.__init__(self, name, outer_scope, parent_scope)

    def mangle(self, prefix, name):
        return punycodify_name(prefix + name)

    def declare_arg(self, name, type, pos):
        # Add an entry for an argument of a function.
        name = self.mangle_class_private_name(name)
        cname = self.mangle(Naming.var_prefix, name)
        entry = self.declare(name, cname, type, pos, 'private')
        entry.is_variable = 1
        if type.is_pyobject:
            entry.init = "0"
        entry.is_arg = 1
        #entry.borrowed = 1 # Not using borrowed arg refs for now
        self.arg_entries.append(entry)
        return entry

    def declare_var(self, name, type, pos,
                    cname=None, visibility='private',
                    api=False, in_pxd=False, is_cdef=False, pytyping_modifiers=None):
        name = self.mangle_class_private_name(name)
        # Add an entry for a local variable.
        if visibility in ('public', 'readonly'):
            error(pos, "Local variable cannot be declared %s" % visibility)
        entry = Scope.declare_var(self, name, type, pos,
                                  cname=cname, visibility=visibility,
                                  api=api, in_pxd=in_pxd, is_cdef=is_cdef, pytyping_modifiers=pytyping_modifiers)
        if entry.type.declaration_value:
            entry.init = entry.type.declaration_value
        entry.is_local = 1

        entry.in_with_gil_block = self._in_with_gil_block
        self.var_entries.append(entry)
        return entry

    def declare_global(self, name, pos):
        # Pull entry from global scope into local scope.
        if self.lookup_here(name):
            warning(pos, "'%s' redeclared  ", 0)
        else:
            entry = self.global_scope().lookup_target(name)
            self.entries[name] = entry

    def declare_nonlocal(self, name, pos):
        # Pull entry from outer scope into local scope
        orig_entry = self.lookup_here(name)
        if orig_entry and orig_entry.scope is self and not orig_entry.from_closure:
            error(pos, "'%s' redeclared as nonlocal" % name)
            orig_entry.already_declared_here()
        else:
            entry = self.lookup(name)
            if entry is None or not entry.from_closure:
                error(pos, "no binding for nonlocal '%s' found" % name)

    def _create_inner_entry_for_closure(self, name, entry):
        entry.in_closure = True
        inner_entry = InnerEntry(entry, self)
        inner_entry.is_variable = True
        self.entries[name] = inner_entry
        return inner_entry

    def lookup(self, name):
        # Look up name in this scope or an enclosing one.
        # Return None if not found.

        entry = Scope.lookup(self, name)
        if entry is not None:
            entry_scope = entry.scope
            while entry_scope.is_comprehension_scope:
                entry_scope = entry_scope.outer_scope
            if entry_scope is not self and entry_scope.is_closure_scope:
                if hasattr(entry.scope, "scope_class"):
                    raise InternalError("lookup() after scope class created.")
                # The actual c fragment for the different scopes differs
                # on the outside and inside, so we make a new entry
                return self._create_inner_entry_for_closure(name, entry)
        return entry

    def mangle_closure_cnames(self, outer_scope_cname):
        for scope in self.iter_local_scopes():
            for entry in scope.entries.values():
                if entry.from_closure:
                    cname = entry.outer_entry.cname
                    if self.is_passthrough:
                        entry.cname = cname
                    else:
                        if cname.startswith(Naming.cur_scope_cname):
                            cname = cname[len(Naming.cur_scope_cname)+2:]
                        entry.cname = "%s->%s" % (outer_scope_cname, cname)
                elif entry.in_closure:
                    entry.original_cname = entry.cname
                    entry.cname = "%s->%s" % (Naming.cur_scope_cname, entry.cname)
                    if entry.type.is_cpp_class and entry.scope.directives['cpp_locals']:
                        entry.make_cpp_optional()


class ComprehensionScope(Scope):
    """Scope for comprehensions (but not generator expressions, which use ClosureScope).
    As opposed to generators, these can be easily inlined in some cases, so all
    we really need is a scope that holds the loop variable(s).
    """
    is_comprehension_scope = True

    def __init__(self, outer_scope:Scope):
        parent_scope = outer_scope
        # TODO: also ignore class scopes?
        while parent_scope.is_comprehension_scope:
            parent_scope = parent_scope.parent_scope
        name = parent_scope.global_scope().next_id(Naming.genexpr_id_ref)
        Scope.__init__(self, name, outer_scope, parent_scope)
        self.directives = outer_scope.directives
        self.genexp_prefix = "%s%d%s" % (Naming.pyrex_prefix, len(name), name)

        # Class/ExtType scopes are filled at class creation time, i.e. from the
        # module init function or surrounding function.
        while outer_scope.is_comprehension_scope or outer_scope.is_c_class_scope or outer_scope.is_py_class_scope:
            outer_scope = outer_scope.outer_scope
        self.var_entries = outer_scope.var_entries  # keep declarations outside
        outer_scope.subscopes.add(self)

    def mangle(self, prefix, name):
        return '%s%s' % (self.genexp_prefix, self.parent_scope.mangle(prefix, name))

    def declare_var(self, name, type, pos,
                    cname=None, visibility='private',
                    api=False, in_pxd=False, is_cdef=True, pytyping_modifiers=None):
        if type is unspecified_type:
            # if the outer scope defines a type for this variable, inherit it
            outer_entry = self.outer_scope.lookup(name)
            if outer_entry and outer_entry.is_variable:
                type = outer_entry.type  # may still be 'unspecified_type' !
        self._reject_pytyping_modifiers(pos, pytyping_modifiers)
        # the parent scope needs to generate code for the variable, but
        # this scope must hold its name exclusively
        cname = '%s%s' % (self.genexp_prefix, self.parent_scope.mangle(Naming.var_prefix, name or self.next_id()))
        entry = self.declare(name, cname, type, pos, visibility)
        entry.is_variable = True
        if self.parent_scope.is_module_scope:
            entry.is_cglobal = True
        else:
            entry.is_local = True
        entry.in_subscope = True
        self.var_entries.append(entry)
        self.entries[name] = entry
        return entry

    def declare_assignment_expression_target(self, name, type, pos):
        # should be declared in the parent scope instead
        return self.parent_scope.declare_var(name, type, pos)

    def declare_pyfunction(self, name, pos, allow_redefine=False):
        return self.outer_scope.declare_pyfunction(
            name, pos, allow_redefine)

    def declare_lambda_function(self, func_cname, pos):
        return self.outer_scope.declare_lambda_function(func_cname, pos)

    def add_lambda_def(self, def_node):
        return self.outer_scope.add_lambda_def(def_node)

    def lookup_assignment_expression_target(self, name):
        entry = self.lookup_here(name)
        if not entry:
            entry = self.parent_scope.lookup_assignment_expression_target(name)
        return entry


class ClosureScope(LocalScope):

    is_closure_scope = True

    def __init__(self, name, scope_name, outer_scope, parent_scope=None):
        LocalScope.__init__(self, name, outer_scope, parent_scope)
        self.closure_cname = "%s%s" % (Naming.closure_scope_prefix, scope_name)

#    def mangle_closure_cnames(self, scope_var):
#        for entry in self.entries.values() + self.temp_entries:
#            entry.in_closure = 1
#        LocalScope.mangle_closure_cnames(self, scope_var)

#    def mangle(self, prefix, name):
#        return "%s->%s" % (self.cur_scope_cname, name)
#        return "%s->%s" % (self.closure_cname, name)

    def declare_pyfunction(self, name, pos, allow_redefine=False):
        return LocalScope.declare_pyfunction(self, name, pos, allow_redefine, visibility='private')

    def declare_assignment_expression_target(self, name, type, pos):
        return self.declare_var(name, type, pos)


class GeneratorExpressionScope(ClosureScope):
    is_generator_expression_scope = True

    def declare_assignment_expression_target(self, name, type, pos):
        entry = self.parent_scope.declare_var(name, type, pos)
        return self._create_inner_entry_for_closure(name, entry)

    def lookup_assignment_expression_target(self, name):
        entry = self.lookup_here(name)
        if not entry:
            entry = self.parent_scope.lookup_assignment_expression_target(name)
            if entry:
                return self._create_inner_entry_for_closure(name, entry)
        return entry


class StructOrUnionScope(Scope):
    #  Namespace of a C struct or union.

    def __init__(self, name="?"):
        Scope.__init__(self, name, outer_scope=None, parent_scope=None)

    def declare_var(self, name, type, pos,
                    cname=None, visibility='private',
                    api=False, in_pxd=False, is_cdef=False, pytyping_modifiers=None,
                    allow_pyobject=False, allow_memoryview=False, allow_refcounted=False):
        # Add an entry for an attribute.
        if not cname:
            cname = name
            if visibility == 'private':
                cname = c_safe_identifier(cname)
        if type.is_cfunction:
            type = PyrexTypes.CPtrType(type)
        self._reject_pytyping_modifiers(pos, pytyping_modifiers)
        entry = self.declare(name, cname, type, pos, visibility)
        entry.is_variable = 1
        self.var_entries.append(entry)
        if type.is_pyobject:
            if not allow_pyobject:
                error(pos, "C struct/union member cannot be a Python object")
        elif type.is_memoryviewslice:
            if not allow_memoryview:
                # Memory views wrap their buffer owner as a Python object.
                error(pos, "C struct/union member cannot be a memory view")
        elif type.needs_refcounting and not allow_refcounted:
            error(pos, f"C struct/union member cannot be reference-counted type '{type}'")
        return entry

    def declare_cfunction(self, name, type, pos,
                          cname=None, visibility='private', api=0, in_pxd=0,
                          defining=0, modifiers=(), overridable=False):  # currently no utility code ...
        if overridable:
            error(pos, "C struct/union member cannot be declared 'cpdef'")
        return self.declare_var(name, type, pos,
                                cname=cname, visibility=visibility)


class ClassScope(Scope):
    #  Abstract base class for namespace of
    #  Python class or extension type.
    #
    #  class_name     string   Python name of the class
    #  scope_prefix   string   Additional prefix for names
    #                          declared in the class
    #  doc    string or None   Doc string

    scope_predefined_names = ['__module__', '__qualname__']

    def mangle_class_private_name(self, name):
        # a few utilitycode names need to specifically be ignored
        if name and name.lower().startswith("__pyx_"):
            return name
        if name and name.startswith('__') and not name.endswith('__'):
            name = EncodedString('_%s%s' % (self.class_name.lstrip('_'), name))
        return name

    def __init__(self, name, outer_scope):
        Scope.__init__(self, name, outer_scope, outer_scope)
        self.class_name = name
        self.doc = None

    def lookup(self, name):
        entry = Scope.lookup(self, name)
        if entry:
            return entry
        if name == "classmethod":
            # We don't want to use the builtin classmethod here 'cause it won't do the
            # right thing in this scope (as the class members aren't still functions).
            # Don't want to add a cfunction to this scope 'cause that would mess with
            # the type definition, so we just return the right entry.
            entry = Entry(
                "classmethod",
                "__Pyx_Method_ClassMethod",
                PyrexTypes.CFuncType(
                    py_object_type,
                    [PyrexTypes.CFuncTypeArg("", py_object_type, None)], 0, 0))
            entry.utility_code = Code.UtilityCode.load_cached("ClassMethod", "CythonFunction.c")
            self.use_entry_utility_code(entry)
            entry.is_cfunction = 1
            entry.scope = self.builtin_scope()
        return entry


class PyClassScope(ClassScope):
    #  Namespace of a Python class.
    #
    #  class_obj_cname     string   C variable holding class object

    is_py_class_scope = 1
    namespace_cname_is_type = False

    def declare_var(self, name, type, pos,
                    cname=None, visibility='private',
                    api=False, in_pxd=False, is_cdef=False, pytyping_modifiers=None):
        name = self.mangle_class_private_name(name)
        if type is unspecified_type:
            type = py_object_type
        # Add an entry for a class attribute.
        entry = Scope.declare_var(self, name, type, pos,
                                  cname=cname, visibility=visibility,
                                  api=api, in_pxd=in_pxd, is_cdef=is_cdef, pytyping_modifiers=pytyping_modifiers)
        entry.is_pyglobal = 1
        entry.is_pyclass_attr = 1
        return entry

    def declare_nonlocal(self, name, pos):
        # Pull entry from outer scope into local scope
        orig_entry = self.lookup_here(name)
        if orig_entry and orig_entry.scope is self and not orig_entry.from_closure:
            error(pos, "'%s' redeclared as nonlocal" % name)
            orig_entry.already_declared_here()
        else:
            entry = self.lookup(name)
            if entry is None:
                error(pos, "no binding for nonlocal '%s' found" % name)
            else:
                # FIXME: this works, but it's unclear if it's the
                # right thing to do
                self.entries[name] = entry

    def declare_global(self, name, pos):
        # Pull entry from global scope into local scope.
        if self.lookup_here(name):
            warning(pos, "'%s' redeclared  ", 0)
        else:
            entry = self.global_scope().lookup_target(name)
            self.entries[name] = entry

    def add_default_value(self, type):
        return self.outer_scope.add_default_value(type)


class CClassScope(ClassScope):
    #  Namespace of an extension type.
    #
    #  parent_type           PyExtensionType
    #  #typeobj_cname        string or None
    #  #objstruct_cname      string
    #  method_table_cname    string
    #  getset_table_cname    string
    #  has_pyobject_attrs    boolean  Any PyObject attributes?
    #  has_memoryview_attrs  boolean  Any memory view attributes?
    #  has_explicitly_constructable_class_attrs   boolean  Any attributes that
    #                               need an explicit constructor (e.g. C++ class non-pointers)?
    #  has_cyclic_pyobject_attrs    boolean  Any PyObject attributes that may need GC?
    #  property_entries      [Entry]
    #  defined               boolean  Defined in .pxd file
    #  implemented           boolean  Defined in .pyx file
    #  inherited_var_entries [Entry]  Adapted var entries from base class

    is_c_class_scope = 1
    is_closure_class_scope = False
    is_defaults_class_scope = False

    has_pyobject_attrs = False
    has_memoryview_attrs = False
    has_explicitly_constructable_attrs = False
    has_cyclic_pyobject_attrs = False
    defined = False
    implemented = False

    def __init__(self, name:str, outer_scope:Scope, visibility:str, parent_type:PyrexTypes.PyrexType):
        ClassScope.__init__(self, name, outer_scope)
        if visibility != 'extern':
            self.method_table_cname = outer_scope.mangle(Naming.methtab_prefix, name)
            self.getset_table_cname = outer_scope.mangle(Naming.gstab_prefix, name)
        self.property_entries = []
        self.inherited_var_entries = []
        self.parent_type = parent_type
        # Usually parent_type will be an extension type and so the typeptr_cname
        # can be used to calculate the namespace_cname. Occasionally other types
        # are used (e.g. numeric/complex types) and in these cases the typeptr
        # isn't relevant.
        if ((parent_type.is_builtin_type or parent_type.is_extension_type)
                and parent_type.typeptr_cname):
            self.namespace_cname = self.parent_type.typeptr_cname
            self.namespace_cname_is_type = True

    def needs_gc(self):
        # If the type or any of its base types have Python-valued
        # C attributes, then it needs to participate in GC.
        if self.has_cyclic_pyobject_attrs and not self.directives.get('no_gc', False):
            return True
        if self.parent_type.is_external and not self.parent_type.is_builtin_type:
            # It's impossible to really know - external types are often incomplete.
            return True
        base_type = self.parent_type.base_type
        if base_type and base_type.scope is not None:
            return base_type.scope.needs_gc()
        if self.parent_type.is_builtin_type:
            return not self.parent_type.is_gc_simple
        return False

    def needs_trashcan(self):
        # If the trashcan directive is explicitly set to False,
        # unconditionally disable the trashcan.
        directive = self.directives.get('trashcan')
        if directive is False:
            return False
        # If the directive is set to True and the class has Python-valued
        # C attributes, then it should use the trashcan in tp_dealloc.
        if directive and self.has_cyclic_pyobject_attrs:
            return True
        # Use the trashcan if the base class uses it
        base_type = self.parent_type.base_type
        if base_type and base_type.scope is not None:
            return base_type.scope.needs_trashcan()
        return self.parent_type.builtin_trashcan

    def needs_tp_clear(self):
        """Do we need to generate an implementation for the tp_clear slot? Can
        be disabled to keep references for the __dealloc__ cleanup function.
        """
        return self.needs_gc() and not self.directives.get('no_gc_clear', False)

    def may_have_finalize(self):
        """This covers cases where we definitely have a __del__ function
        and also cases where one of the base classes could have a __del__
        function but we don't know.
        """
        current_type_scope = self
        while current_type_scope:
            del_entry = current_type_scope.lookup_here("__del__")
            if del_entry and del_entry.is_special:
                return True
            if (current_type_scope.parent_type.is_external or not current_type_scope.implemented or
                    current_type_scope.parent_type.multiple_bases):
                # we don't know if we have __del__, so assume we do and call it
                return True
            current_base_type = current_type_scope.parent_type.base_type
            current_type_scope = current_base_type.scope if current_base_type else None
        return False

    def get_refcounted_entries(self, include_weakref=False,
                               include_gc_simple=True):
        py_attrs = []
        py_buffers = []
        memoryview_slices = []

        for entry in self.var_entries:
            if entry.type.is_pyobject:
                if include_weakref or (self.is_closure_class_scope or entry.name != "__weakref__"):
                    if include_gc_simple or not entry.type.is_gc_simple:
                        py_attrs.append(entry)
            elif entry.type == PyrexTypes.c_py_buffer_type:
                py_buffers.append(entry)
            elif entry.type.is_memoryviewslice:
                memoryview_slices.append(entry)

        have_entries = py_attrs or py_buffers or memoryview_slices
        return have_entries, (py_attrs, py_buffers, memoryview_slices)

    def declare_var(self, name:str, type:"PyrexType", pos:int|None,
                    cname:str|None=None, visibility:str='private',
                    api:bool=False, in_pxd:bool=False, is_cdef:bool|int=False, pytyping_modifiers:list[str]|None=None):
        name = self.mangle_class_private_name(name)

        if pytyping_modifiers:
            if "typing.ClassVar" in pytyping_modifiers:
                is_cdef = 0
                if not type.is_pyobject:
                    if not type.equivalent_type:
                        warning(pos, "ClassVar[] requires the type to be a Python object type. Found '%s', using object instead." % type)
                        type = py_object_type
                    else:
                        type = type.equivalent_type
            if  "dataclasses.InitVar" in pytyping_modifiers and not self.is_c_dataclass_scope:
                error(pos, "Use of cython.dataclasses.InitVar does not make sense outside a dataclass")

        if is_cdef:
            # Add an entry for an attribute.
            if self.defined:
                error(pos,
                    "C attributes cannot be added in implementation part of"
                    " extension type defined in a pxd")
            if (not self.is_closure_class_scope and
                    get_slot_table(self.directives).get_special_method_signature(name)):
                error(pos,
                    f"The name '{name}' is reserved for a special method.")
            if not cname:
                cname = name
                if not (self.parent_type.is_external or self.parent_type.entry.api or
                        self.parent_type.entry.visibility == "public"):
                    cname = c_safe_identifier(cname)
                cname = punycodify_name(cname, Naming.unicode_structmember_prefix)
            entry = self.declare(name, cname, type, pos, visibility)
            entry.is_variable = 1
            self.var_entries.append(entry)
            entry.pytyping_modifiers = pytyping_modifiers
            if type.is_cpp_class and visibility != 'extern':
                if self.directives['cpp_locals']:
                    entry.make_cpp_optional()
                else:
                    type.check_nullary_constructor(pos)
            if type.is_memoryviewslice:
                self.has_memoryview_attrs = True
            elif type.needs_explicit_construction(self):
                self.has_explicitly_constructable_attrs = True
            elif type.is_pyobject and (self.is_closure_class_scope or name != '__weakref__'):
                self.has_pyobject_attrs = True
                if (not type.is_builtin_type
                        or not type.scope or type.scope.needs_gc()):
                    self.has_cyclic_pyobject_attrs = True
            if visibility not in ('private', 'public', 'readonly'):
                error(pos,
                    "Attribute of extension type cannot be declared %s" % visibility)
            if visibility in ('public', 'readonly'):
                # If the field is an external typedef, we cannot be sure about the type,
                # so do conversion ourself rather than rely on the CPython mechanism (through
                # a property; made in AnalyseDeclarationsTransform).
                entry.needs_property = True
                if not self.is_closure_class_scope and name == "__weakref__":
                    error(pos, "Special attribute __weakref__ cannot be exposed to Python")
                if not (type.is_pyobject or type.can_coerce_to_pyobject(self)):
                    # we're not testing for coercion *from* Python here - that would fail later
                    error(pos, "C attribute of type '%s' cannot be accessed from Python" % type)
            else:
                entry.needs_property = False
            return entry
        if type is unspecified_type:
            type = py_object_type
        # Add an entry for a class attribute.
        entry = Scope.declare_var(self, name, type, pos,
                                  cname=cname, visibility=visibility,
                                  api=api, in_pxd=in_pxd, is_cdef=is_cdef, pytyping_modifiers=pytyping_modifiers)
        entry.is_member = 1
        # xxx: is_pyglobal changes behaviour in so many places that I keep it in for now.
        # is_member should be enough later on
        entry.is_pyglobal = 1

        return entry

    def declare_pyfunction(self, name:str, pos:int|None, allow_redefine:bool=False):
        # Add an entry for a method.
        if name in richcmp_special_methods:
            if self.lookup_here('__richcmp__'):
                error(pos, "Cannot define both % and __richcmp__" % name)
        elif name == '__richcmp__':
            for n in richcmp_special_methods:
                if self.lookup_here(n):
                    error(pos, "Cannot define both % and __richcmp__" % n)
        if name == "__new__":
            error(pos, "__new__ method of extension type will change semantics "
                "in a future version of Pyrex and Cython. Use __cinit__ instead.")
        entry = self.declare_var(name, py_object_type, pos,
                                 visibility='extern')
        special_sig = get_slot_table(self.directives).get_special_method_signature(name)
        if special_sig:
            # Special methods get put in the method table with a particular
            # signature declared in advance.
            entry.signature = special_sig
            entry.is_special = 1
        else:
            entry.signature = pymethod_signature
            entry.is_special = 0

        self.pyfunc_entries.append(entry)
        return entry

    def lookup_here(self, name:str)->"Entry":
        if not self.is_closure_class_scope and name == "__new__":
            name = EncodedString("__cinit__")
        entry = ClassScope.lookup_here(self, name)
        if entry and entry.is_builtin_cmethod:
            if not self.parent_type.is_builtin_type:
                # For subtypes of builtin types, we can only return
                # optimised C methods if the type if final.
                # Otherwise, subtypes may choose to override the
                # method, but the optimisation would prevent the
                # subtype method from being called.
                if not self.parent_type.is_final_type:
                    return None
        return entry

    def declare_cfunction(self, name, type, pos,
                          cname=None, visibility='private', api=0, in_pxd=0,
                          defining=0, modifiers=(), utility_code=None, overridable=False)->"Entry":
        name = self.mangle_class_private_name(name)
        if (get_slot_table(self.directives).get_special_method_signature(name)
                and not self.parent_type.is_builtin_type):
            error(pos, "Special methods must be declared with 'def', not 'cdef'")
        args = type.args
        if not type.is_static_method:
            if not args:
                error(pos, "C method has no self argument")
            elif not self.parent_type.assignable_from(args[0].type):
                error(pos, f"Self argument ({args[0].type}) of C method '{name}' does not match parent type ({self.parent_type})")
        entry = self.lookup_here(name)
        if cname is None:
            cname = punycodify_name(c_safe_identifier(name), Naming.unicode_vtabentry_prefix)
        if entry:
            if not entry.is_cfunction:
                error(pos, "'%s' redeclared " % name)
                entry.already_declared_here()
            else:
                if defining and entry.func_cname:
                    error(pos, "'%s' already defined" % name)
                #print "CClassScope.declare_cfunction: checking signature" ###
                if entry.is_final_cmethod and entry.is_inherited:
                    error(pos, "Overriding final methods is not allowed")
                elif type.same_c_signature_as(entry.type, as_cmethod = 1) and type.nogil == entry.type.nogil:
                    # Fix with_gil vs nogil.
                    entry.type = entry.type.with_with_gil(type.with_gil)
                elif type.compatible_signature_with(entry.type, as_cmethod = 1) and type.nogil == entry.type.nogil:
                    if (self.defined and not in_pxd
                            and not type.same_c_signature_as_resolved_type(
                                entry.type, as_cmethod=1, as_pxd_definition=1)):
                        # TODO(robertwb): Make this an error.
                        warning(pos,
                            f"Compatible but non-identical C method '{name}' not redeclared "
                            f"in definition part of extension type '{self.class_name}'.  "
                            "This may cause incorrect vtables to be generated.", 2)
                        warning(entry.pos, "Previous declaration is here", 2)
                    entry = self.add_cfunction(name, type, pos, cname, visibility='ignore', modifiers=modifiers)
                else:
                    error(pos, "Signature not compatible with previous declaration")
                    error(entry.pos, "Previous declaration is here")
        else:
            if self.defined:
                error(pos,
                    f"C method '{name}' not previously declared in definition part of"
                    f" extension type '{self.class_name}'")
            entry = self.add_cfunction(name, type, pos, cname, visibility, modifiers)
        if defining:
            entry.func_cname = self.mangle(Naming.func_prefix, name)
        entry.utility_code = utility_code
        type.entry = entry

        if 'inline' in modifiers:
            entry.is_inline_cmethod = True

        if self.parent_type.is_final_type or entry.is_inline_cmethod or self.directives.get('final'):
            entry.is_final_cmethod = True
            entry.final_func_cname = entry.func_cname
            if not type.is_fused:
                entry.vtable_type = entry.type
                entry.type = type

        return entry

    def add_cfunction(self, name, type, pos, cname, visibility, modifiers, inherited=False):
        # Add a cfunction entry without giving it a func_cname.
        prev_entry = self.lookup_here(name)
        entry = ClassScope.add_cfunction(
            self, name, type, pos, cname, visibility, modifiers, inherited=inherited)
        entry.is_cmethod = 1
        entry.prev_entry = prev_entry
        return entry

    def declare_builtin_cfunction(self, name, type, cname, utility_code = None):
        # overridden methods of builtin types still have their Python
        # equivalent that must be accessible to support bound methods
        name = EncodedString(name)
        entry = self.declare_cfunction(
            name, type, pos=None, cname=cname, visibility='extern', utility_code=utility_code)
        var_entry = Entry(name, name, py_object_type)
        var_entry.qualified_name = name
        var_entry.is_variable = 1
        var_entry.is_builtin = 1
        var_entry.utility_code = utility_code
        var_entry.scope = entry.scope
        entry.as_variable = var_entry
        return entry

    def declare_property(self, name, doc, pos, ctype=None, property_scope=None):
        entry = self.lookup_here(name)
        if entry is None:
            entry = self.declare(name, name, py_object_type if ctype is None else ctype, pos, 'private')
        entry.is_property = True
        if ctype is not None:
            entry.is_cproperty = True
        entry.doc = doc
        if property_scope is None:
            entry.scope = PropertyScope(name, class_scope=self)
        else:
            entry.scope = property_scope
        self.property_entries.append(entry)
        return entry

    def declare_cproperty(self, name, type, cfunc_name, doc=None, pos=None, visibility='extern',
                          nogil=False, with_gil=False, exception_value=None, exception_check=False,
                          utility_code=None):
        """Internal convenience method to declare a C property function in one go.
        """
        property_entry = self.declare_property(name, doc=doc, ctype=type, pos=pos)
        cfunc_entry = property_entry.scope.declare_cfunction(
            name=name,
            type=PyrexTypes.CFuncType(
                type,
                [PyrexTypes.CFuncTypeArg("self", self.parent_type, pos=None)],
                nogil=nogil,
                with_gil=with_gil,
                exception_value=exception_value,
                exception_check=exception_check,
            ),
            cname=cfunc_name,
            utility_code=utility_code,
            visibility=visibility,
            pos=pos,
        )
        return property_entry, cfunc_entry

    def declare_inherited_c_attributes(self, base_scope):
        # Declare entries for all the C attributes of an
        # inherited type, with cnames modified appropriately
        # to work with this type.
        def adapt(cname):
            return "%s.%s" % (Naming.obj_base_cname, base_entry.cname)

        entries = base_scope.inherited_var_entries + base_scope.var_entries
        for base_entry in entries:
            entry = self.declare(
                base_entry.name, adapt(base_entry.cname),
                base_entry.type, None, 'private')
            entry.is_variable = 1
            entry.is_inherited = True
            entry.annotation = base_entry.annotation
            self.inherited_var_entries.append(entry)

        # If the class defined in a pxd, specific entries have not been added.
        # Ensure now that the parent (base) scope has specific entries
        # Iterate over a copy as get_all_specialized_function_types() will mutate
        for base_entry in base_scope.cfunc_entries[:]:
            if base_entry.type.is_fused:
                base_entry.type.get_all_specialized_function_types()

        for base_entry in base_scope.cfunc_entries:
            cname = base_entry.cname
            var_entry = base_entry.as_variable
            is_builtin = var_entry and var_entry.is_builtin
            if not is_builtin:
                cname = adapt(cname)
            entry = self.add_cfunction(
                base_entry.name, base_entry.type, base_entry.pos, cname,
                base_entry.visibility, base_entry.func_modifiers, inherited=True)
            entry.is_inherited = 1
            if base_entry.is_final_cmethod:
                entry.is_final_cmethod = True
                entry.is_inline_cmethod = base_entry.is_inline_cmethod
                if (self.parent_scope == base_scope.parent_scope or
                        entry.is_inline_cmethod):
                    entry.final_func_cname = base_entry.final_func_cname
            if is_builtin:
                entry.is_builtin_cmethod = True
                entry.as_variable = var_entry
            if base_entry.utility_code:
                entry.utility_code = base_entry.utility_code


    def handle_already_declared_name(self, name, cname, type, pos, visibility, copy_entry=True):
        # We want to copy the existing entry instead of modifying it, since this is an override.
        super().handle_already_declared_name(name, cname, type, pos, visibility, copy_entry)

class CppClassScope(Scope):
    #  Namespace of a C++ class.

    is_cpp_class_scope = 1

    default_constructor = None
    type = None

    def __init__(self, name, outer_scope, templates=None):
        Scope.__init__(self, name, outer_scope, None)
        self.directives = outer_scope.directives
        self.inherited_var_entries = []
        if templates is not None:
            for T in templates:
                template_entry = self.declare(
                    T, T, PyrexTypes.TemplatePlaceholderType(T), None, 'extern')
                template_entry.is_type = 1

    def declare_var(self, name, type, pos,
                    cname=None, visibility='extern',
                    api=False, in_pxd=False, is_cdef=False, defining=False, pytyping_modifiers=None):
        # Add an entry for an attribute.
        if not cname:
            cname = name
        self._reject_pytyping_modifiers(pos, pytyping_modifiers)
        entry = self.lookup_here(name)
        if defining and entry is not None:
            if type.is_cfunction:
                entry = self.declare(name, cname, type, pos, visibility)
            elif entry.type.same_as(type):
                # Fix with_gil vs nogil.
                entry.type = entry.type.with_with_gil(type.with_gil)
            else:
                error(pos, "Function signature does not match previous declaration")
        else:
            entry = self.declare(name, cname, type, pos, visibility)
            if type.is_cfunction and not defining:
                entry.is_inherited = 1
        entry.is_variable = 1
        if type.is_cfunction:
            entry.is_cfunction = 1
            if self.type and not self.type.get_fused_types():
                entry.func_cname = "%s::%s" % (self.type.empty_declaration_code(), cname)
        if name != "this" and (defining or name != "<init>"):
            self.var_entries.append(entry)
        return entry

    def declare_cfunction(self, name, type, pos,
                          cname=None, visibility='extern', api=0, in_pxd=0,
                          defining=0, modifiers=(), utility_code=None, overridable=False):
        class_name = self.name.split('::')[-1]
        if name in (class_name, '__init__') and cname is None:
            cname = "%s__init__%s" % (Naming.func_prefix, class_name)
            name = EncodedString('<init>')
            type.return_type = PyrexTypes.CVoidType()
            # This is called by the actual constructor, but need to support
            # arguments that cannot by called by value.
            type.original_args = type.args
            def maybe_ref(arg):
                if arg.type.is_cpp_class and not arg.type.is_reference:
                    return PyrexTypes.CFuncTypeArg(
                        arg.name, PyrexTypes.c_ref_type(arg.type), arg.pos)
                return arg
            type.args = [maybe_ref(arg) for arg in type.args]
        elif name == '__dealloc__' and cname is None:
            cname = "%s__dealloc__%s" % (Naming.func_prefix, class_name)
            name = EncodedString('<del>')
            type.return_type = PyrexTypes.CVoidType()
        if name in ('<init>', '<del>') and type.nogil:
            for base in self.type.base_classes:
                base_entry = base.scope.lookup(name)
                if base_entry and not base_entry.type.nogil:
                    error(pos, "Constructor cannot be called without GIL unless all base constructors can also be called without GIL")
                    error(base_entry.pos, "Base constructor defined here.")
        # The previous entries management is now done directly in Scope.declare
        entry = self.declare_var(name, type, pos,
                                 defining=defining,
                                 cname=cname, visibility=visibility)
        entry.utility_code = utility_code
        type.entry = entry
        return entry

    def declare_inherited_cpp_attributes(self, base_class):
        base_scope = base_class.scope
        template_type = base_class
        while getattr(template_type, 'template_type', None):
            template_type = template_type.template_type
        base_templates = [T.name for T in template_type.templates] if getattr(template_type, 'templates', None) else ()
        # Declare entries for all the C++ attributes of an
        # inherited type, with cnames modified appropriately
        # to work with this type.
        for base_entry in base_scope.inherited_var_entries + base_scope.var_entries:
            #constructor/destructor is not inherited
            if base_entry.name in ("<init>", "<del>"):
                continue
            #print base_entry.name, self.entries
            if base_entry.name in self.entries:
                base_entry.name    # FIXME: is there anything to do in this case?
            entry = self.declare(base_entry.name, base_entry.cname,
                base_entry.type, None, 'extern')
            entry.is_variable = 1
            entry.is_inherited = 1
            if base_entry.is_cfunction:
                entry.is_cfunction = 1
                entry.func_cname = base_entry.func_cname
            self.inherited_var_entries.append(entry)
        for base_entry in base_scope.cfunc_entries:
            entry = self.declare_cfunction(base_entry.name, base_entry.type,
                                           base_entry.pos, base_entry.cname,
                                           base_entry.visibility, api=0,
                                           modifiers=base_entry.func_modifiers,
                                           utility_code=base_entry.utility_code)
            entry.is_inherited = 1
        for base_entry in base_scope.type_entries:
            if base_entry.name not in base_templates:
                entry = self.declare_type(base_entry.name, base_entry.type,
                                          base_entry.pos, base_entry.cname,
                                          base_entry.visibility, defining=False)
                entry.is_inherited = 1

    def specialize(self, values, type_entry):
        scope = CppClassScope(self.name, self.outer_scope)
        scope.type = type_entry
        for entry in self.entries.values():
            if entry.is_type:
                scope.declare_type(entry.name,
                                   entry.type.specialize(values),
                                   entry.pos,
                                   entry.cname,
                                   template=1)
            elif entry.type.is_cfunction:
                for e in entry.all_alternatives():
                    scope.declare_cfunction(e.name,
                                            e.type.specialize(values),
                                            e.pos,
                                            e.cname,
                                            utility_code=e.utility_code)
            else:
                scope.declare_var(entry.name,
                                  entry.type.specialize(values),
                                  entry.pos,
                                  entry.cname,
                                  entry.visibility)

        return scope

    def lookup_here(self, name):
        if name == "__init__":
            name = "<init>"
        elif name == "__dealloc__":
            name = "<del>"
        return super().lookup_here(name)

    def is_cpp(self):
        # Whatever the global environment, always treat cppclass with C++ rules.
        # (Cython will emit warnings elsewhere)
        return True


class CppScopedEnumScope(Scope):
    #  Namespace of a ScopedEnum

    def __init__(self, name, outer_scope):
        Scope.__init__(self, name, outer_scope, None)

    def declare_var(self, name, type, pos,
                    cname=None, visibility='extern', pytyping_modifiers=None):
        # Add an entry for an attribute.
        if not cname:
            cname = name
        self._reject_pytyping_modifiers(pos, pytyping_modifiers)
        entry = self.declare(name, cname, type, pos, visibility)
        entry.is_variable = True
        return entry


class PropertyScope(Scope):
    #  Scope holding the __get__, __set__ and __del__ methods for
    #  a property of an extension type.
    #
    #  parent_type   PyExtensionType   The type to which the property belongs

    is_property_scope = 1

    def __init__(self, name, class_scope):
        # outer scope is None for some internal properties
        outer_scope = class_scope.global_scope() if class_scope.outer_scope else None
        Scope.__init__(self, name, outer_scope, parent_scope=class_scope)
        self.parent_type = class_scope.parent_type
        self.directives = class_scope.directives

    def declare_cfunction(self, name, type, pos, *args, **kwargs):
        """Declare a C property function.
        """
        if type.return_type.is_void:
            error(pos, "C property method cannot return 'void'")

        if type.args and type.args[0].type is py_object_type:
            # Set 'self' argument type to extension type.
            type.args[0].type = self.parent_scope.parent_type
        elif len(type.args) != 1:
            error(pos, "C property method must have a single (self) argument")
        elif not (type.args[0].type.is_pyobject or type.args[0].type is self.parent_scope.parent_type):
            error(pos, "C property method must have a single (object) argument")

        entry = Scope.declare_cfunction(self, name, type, pos, *args, **kwargs)
        entry.is_cproperty = True
        return entry

    def declare_pyfunction(self, name:str, pos:int|None, allow_redefine:bool=False):
        # Add an entry for a method.
        signature = get_property_accessor_signature(name)
        if signature:
            entry = self.declare(name, name, py_object_type, pos, 'private')
            entry.is_special = 1
            entry.signature = signature
            return entry
        error(pos, "Only __get__, __set__ and __del__ methods allowed "
            "in a property declaration")
        return None


class CConstOrVolatileScope(Scope):

    def __init__(self, base_type_scope, is_const=0, is_volatile=0):
        Scope.__init__(
            self,
            'cv_' + base_type_scope.name,
            base_type_scope.outer_scope,
            base_type_scope.parent_scope)
        self.base_type_scope = base_type_scope
        self.is_const = is_const
        self.is_volatile = is_volatile

    def lookup_here(self, name):
        entry = self.base_type_scope.lookup_here(name)
        if entry is not None:
            entry = copy.copy(entry)
            entry.type = PyrexTypes.c_const_or_volatile_type(
                    entry.type, self.is_const, self.is_volatile)
            return entry
        return None


class TemplateScope(Scope):
    def __init__(self, name, outer_scope):
        Scope.__init__(self, name, outer_scope, None)
        self.directives = outer_scope.directives

```

```python
#
#   Errors
#

any_string_type = (bytes, str)

import sys
from contextlib import contextmanager

try:
    from threading import local as _threadlocal
except ImportError:
    class _threadlocal: pass

threadlocal = _threadlocal()
threadlocal.cython_errors_count = 0
threadlocal.cython_errors_listing_file = None
threadlocal.cython_errors_echo_file = None
threadlocal.cython_errors_warn_once_seen = set()
threadlocal.cython_errors_stack = []

from ..Utils import open_new_file
from . import DebugFlags
from . import Directives


class PyrexError(Exception):
    pass


class PyrexWarning(Exception):
    pass

class CannotSpecialize(PyrexError):
    pass

def context(position):
    source = position[0]
    assert not (isinstance(source, any_string_type)), (
        "Please replace filename strings with Scanning.FileSourceDescriptor instances %r" % source)
    try:
        F = source.get_lines()
    except UnicodeDecodeError:
        # file has an encoding problem
        s = "[unprintable code]"
    else:
        s = '\n'.join(F[max(0, position[1]-6):position[1]])
        s = '...\n%s\n%s^' % (s, ' '*(position[2]))

    hbar = '-' * 60
    s = f'{hbar}\n{s}\n{hbar}\n'
    return s

def format_position(position):
    if position:
        return "%s:%d:%d: " % (position[0].get_error_description(),
                                position[1], position[2])
    return ''

def format_error(message, position):
    """Format a compiler error with a clickable filename:lineno:col prefix.

    Historically Cython printed a context block first. To make error
    navigation in IDEs and terminals easier, emit a one-line summary in
    ``file:line:col: message`` form before the context while keeping the
    existing detailed block for readability.
    """
    if position:
        pos_str = format_position(position)
        cont = context(position)
        # Summary first for editor integration; keep detailed block below.
        summary = f"{pos_str}{message or ''}"
        message = f"{summary}\nError compiling Cython file:\n{cont}{pos_str}{message or ''}"
    return message

class CompileError(PyrexError):

    def __init__(self, position = None, message = ""):
        self.position = position
        self.message_only = message
        self.formatted_message = format_error(message, position)
        self.reported = False
        Exception.__init__(self, self.formatted_message)
        # Python Exception subclass pickling is broken,
        # see https://bugs.python.org/issue1692335
        self.args = (position, message)

    def __str__(self):
        return self.formatted_message

class CompileWarning(PyrexWarning):

    def __init__(self, position = None, message = ""):
        self.position = position
        Exception.__init__(self, format_position(position) + message)

class InternalError(Exception):
    # If this is ever raised, there is a bug in the compiler.

    def __init__(self, message):
        self.message_only = message
        Exception.__init__(self, "Internal compiler error: %s"
            % message)

class AbortError(Exception):
    # Throw this to stop the compilation immediately.

    def __init__(self, message):
        self.message_only = message
        Exception.__init__(self, "Abort error: %s" % message)

class CompilerCrash(CompileError):
    # raised when an unexpected exception occurs in a transform
    def __init__(self, pos, context, message, cause, stacktrace=None):
        if message:
            message = '\n' + message
        else:
            message = '\n'
        self.message_only = message
        if context:
            message = "Compiler crash in %s%s" % (context, message)
        if stacktrace:
            import traceback
            message += (
                '\n\nCompiler crash traceback from this point on:\n' +
                ''.join(traceback.format_tb(stacktrace)))
        if cause:
            if not stacktrace:
                message += '\n'
            message += '%s: %s' % (cause.__class__.__name__, cause)
        CompileError.__init__(self, pos, message)
        # Python Exception subclass pickling is broken,
        # see https://bugs.python.org/issue1692335
        self.args = (pos, context, message, cause, stacktrace)

class NoElementTreeInstalledException(PyrexError):
    """raised when the user enabled options.gdb_debug but no ElementTree
    implementation was found
    """

def open_listing_file(path, echo_to_stderr=True):
    # Begin a new error listing. If path is None, no file
    # is opened, the error counter is just reset.
    if path is not None:
        threadlocal.cython_errors_listing_file = open_new_file(path)
    else:
        threadlocal.cython_errors_listing_file = None
    if echo_to_stderr:
        threadlocal.cython_errors_echo_file = sys.stderr
    else:
        threadlocal.cython_errors_echo_file = None
    threadlocal.cython_errors_count = 0

def close_listing_file():
    if threadlocal.cython_errors_listing_file:
        threadlocal.cython_errors_listing_file.close()
        threadlocal.cython_errors_listing_file = None

def report_error(err, use_stack=True):
    error_stack = threadlocal.cython_errors_stack
    if error_stack and use_stack:
        error_stack[-1].append(err)
    else:
        # See Main.py for why dual reporting occurs. Quick fix for now.
        if err.reported: return
        err.reported = True
        try: line = "%s\n" % err
        except UnicodeEncodeError:
            # Python <= 2.5 does this for non-ASCII Unicode exceptions
            line = format_error(getattr(err, 'message_only', "[unprintable exception message]"),
                                getattr(err, 'position', None)) + '\n'
        listing_file = threadlocal.cython_errors_listing_file
        if listing_file:
            try: listing_file.write(line)
            except UnicodeEncodeError:
                listing_file.write(line.encode('ASCII', 'replace'))
        echo_file = threadlocal.cython_errors_echo_file
        if echo_file:
            try: echo_file.write(line)
            except UnicodeEncodeError:
                echo_file.write(line.encode('ASCII', 'replace'))
        threadlocal.cython_errors_count += 1
        if Directives.fast_fail:
            raise AbortError("fatal errors")

def error(position, message):
    #print("Errors.error:", repr(position), repr(message)) ###
    if position is None:
        raise InternalError(message)
    err = CompileError(position, message)
    if DebugFlags.debug_exception_on_error: raise Exception(err)  # debug
    report_error(err)
    return err


LEVEL = 1  # warn about all errors level 1 or higher

def _write_file_encode(file, line):
    try:
        file.write(line)
    except UnicodeEncodeError:
        file.write(line.encode('ascii', 'replace'))


def performance_hint(position, message, env):
    if not env.directives['show_performance_hints']:
        return
    warn = CompileWarning(position, message)
    line = "performance hint: %s\n" % warn
    listing_file = threadlocal.cython_errors_listing_file
    if listing_file:
        _write_file_encode(listing_file, line)
    echo_file = threadlocal.cython_errors_echo_file
    if echo_file:
        _write_file_encode(echo_file, line)
    return warn


def message(position, message, level=1):
    if level < LEVEL:
        return
    warn = CompileWarning(position, message)
    line = "note: %s\n" % warn
    listing_file = threadlocal.cython_errors_listing_file
    if listing_file:
        _write_file_encode(listing_file, line)
    echo_file = threadlocal.cython_errors_echo_file
    if echo_file:
        _write_file_encode(echo_file, line)
    return warn


def warning(position, message, level=0):
    if level < LEVEL:
        return
    if Directives.warning_errors and position:
        return error(position, message)
    warn = CompileWarning(position, message)
    line = "warning: %s\n" % warn
    listing_file = threadlocal.cython_errors_listing_file
    if listing_file:
        _write_file_encode(listing_file, line)
    echo_file = threadlocal.cython_errors_echo_file
    if echo_file:
        _write_file_encode(echo_file, line)
    return warn


def warn_once(position, message, level=0):
    if level < LEVEL:
        return
    warn_once_seen = threadlocal.cython_errors_warn_once_seen
    if message in warn_once_seen:
        return
    warn = CompileWarning(position, message)
    line = "warning: %s\n" % warn
    listing_file = threadlocal.cython_errors_listing_file
    if listing_file:
        _write_file_encode(listing_file, line)
    echo_file = threadlocal.cython_errors_echo_file
    if echo_file:
        _write_file_encode(echo_file, line)
    warn_once_seen.add(message)
    return warn


# These functions can be used to momentarily suppress errors.

def hold_errors():
    errors = []
    threadlocal.cython_errors_stack.append(errors)
    return errors


def release_errors(ignore=False):
    held_errors = threadlocal.cython_errors_stack.pop()
    if not ignore:
        for err in held_errors:
            report_error(err)


def held_errors():
    return threadlocal.cython_errors_stack[-1]


# same as context manager:

@contextmanager
def local_errors(ignore=False):
    errors = hold_errors()
    try:
        yield errors
    finally:
        release_errors(ignore=ignore)


# Keep all global state in thread local storage to support parallel cythonisation in distutils.

def init_thread():
    threadlocal.cython_errors_count = 0
    threadlocal.cython_errors_listing_file = None
    threadlocal.cython_errors_echo_file = None
    threadlocal.cython_errors_warn_once_seen = set()
    threadlocal.cython_errors_stack = []

def reset():
    threadlocal.cython_errors_warn_once_seen.clear()
    del threadlocal.cython_errors_stack[:]

def get_errors_count():
    return threadlocal.cython_errors_count

```

```python
# cython: auto_cpdef=True, infer_types=True, py2_import=True
#
#   Parser
#


# This should be done automatically
import cython
cython.declare(Nodes=object, ExprNodes=object, EncodedString=object,
               bytes_literal=object, StringEncoding=object,
               FileSourceDescriptor=object, lookup_unicodechar=object,
               Future=object, Options=object, error=object, warning=object,
               Builtin=object, ModuleNode=object, Utils=object, _unicode=object, _bytes=object,
               re=object, _parse_escape_sequences=object, _parse_escape_sequences_raw=object,
               partial=object, reduce=object,
               _CDEF_MODIFIERS=tuple, COMMON_BINOP_MISTAKES=dict)

from io import StringIO
import re
from unicodedata import lookup as lookup_unicodechar
from functools import partial, reduce
from typing import Any, Optional

from .Scanning import PyrexScanner, FileSourceDescriptor, tentatively_scan
from . import Nodes
from . import ExprNodes
from . import MatchCaseNodes
from . import Builtin
from . import StringEncoding
from .StringEncoding import EncodedString, bytes_literal
from .ModuleNode import ModuleNode
from .Errors import error, warning, CompileError
from .. import Utils
from . import Future
from . import Options, Directives


_CDEF_MODIFIERS = ('inline', 'nogil', 'api')
statement_terminators = cython.declare(frozenset, frozenset((
    ';', 'NEWLINE', 'EOF')))

class Ctx:
    #  Parsing context
    level = 'other'
    visibility = 'private'
    cdef_flag = False
    typedef_flag = False
    api = False
    overridable = False
    nogil = False
    namespace = None
    templates = None
    allow_struct_enum_decorator = False

    def __init__(self, **kwds):
        self.__dict__.update(kwds)

    def __call__(self, **kwds):
        ctx = Ctx()
        d = ctx.__dict__
        d.update(self.__dict__)
        d.update(kwds)
        return ctx


@cython.cfunc
def p_ident(s: PyrexScanner, message="Expected an identifier"):
    if s.sy == 'IDENT':
        name = s.context.intern_ustring(s.systring)
        s.next()
        return name
    else:
        s.error(message)


@cython.cfunc
def p_ident_list(s: PyrexScanner):
    names = []
    while s.sy == 'IDENT':
        names.append(s.context.intern_ustring(s.systring))
        s.next()
        if s.sy != ',':
            break
        s.next()
    return names

#------------------------------------------
#
#   Expressions
#
#------------------------------------------

@cython.cfunc
def p_binop_operator(s: PyrexScanner) -> tuple:
    pos = s.position()
    op = s.sy
    s.next()
    return op, pos


# signature is currently overridden in pxd file
def p_binop_expr(s: PyrexScanner, ops, p_sub_expr):
    n1 = p_sub_expr(s)
    while s.sy in ops:
        op, pos = p_binop_operator(s)
        n2 = p_sub_expr(s)
        n1 = ExprNodes.binop_node(pos, op, n1, n2)
        if op == '/':
            if Future.division in s.context.future_directives:
                n1.truedivision = True
            else:
                n1.truedivision = None  # unknown
    return n1


#lambdef: 'lambda' [varargslist] ':' test

@cython.cfunc
def p_lambdef(s: PyrexScanner):
    # s.sy == 'lambda'
    pos = s.position()
    s.next()
    if s.sy == ':':
        args = []
        star_arg = starstar_arg = None
    else:
        args, star_arg, starstar_arg = p_varargslist(
            s, terminator=':', annotated=False)
    s.expect(':')
    expr = p_test(s)
    return ExprNodes.LambdaNode(
        pos, args = args,
        star_arg = star_arg, starstar_arg = starstar_arg,
        result_expr = expr)


#test: or_test ['if' or_test 'else' test] | lambdef

@cython.cfunc
def p_test(s: PyrexScanner):
    # The check for a following ':=' is only for error reporting purposes.
    # It simply changes a
    #   expected ')', found ':='
    # message into something a bit more descriptive.
    # It is close to what the PEG parser does in CPython, where an expression has
    # a lookahead assertion that it isn't followed by ':='
    expr = p_test_allow_walrus_after(s)
    if s.sy == ':=':
        s.error("invalid syntax: assignment expression not allowed in this context")
    return expr


@cython.cfunc
def p_test_allow_walrus_after(s: PyrexScanner):
    if s.sy == 'lambda':
        return p_lambdef(s)
    pos = s.position()
    expr = p_or_test(s)
    if s.sy == 'if':
        s.next()
        test = p_or_test(s)
        s.expect('else')
        other = p_test(s)
        return ExprNodes.CondExprNode(pos, test=test, true_val=expr, false_val=other)
    else:
        return expr


@cython.cfunc
def p_namedexpr_test(s: PyrexScanner):
    # defined in the LL parser as
    #  namedexpr_test: test [':=' test]
    # The requirement that the LHS is a name is not enforced in the grammar.
    # For comparison the PEG parser does:
    #  1. look for "name :=", if found it's definitely a named expression
    #     so look for expression
    #  2. Otherwise, look for expression
    lhs = p_test_allow_walrus_after(s)
    if s.sy == ':=':
        position = s.position()
        if not lhs.is_name:
            s.error("Left-hand side of assignment expression must be an identifier", fatal=False)
        s.next()
        rhs = p_test(s)
        return ExprNodes.AssignmentExpressionNode(position, lhs=lhs, rhs=rhs)
    return lhs


#or_test: and_test ('or' and_test)*

COMMON_BINOP_MISTAKES = {'||': 'or', '&&': 'and'}

@cython.cfunc
def p_or_test(s: PyrexScanner):
    return p_rassoc_binop_expr(s, 'or', p_and_test)


# signature is currently overridden in pxd file
def p_rassoc_binop_expr(s: PyrexScanner, op, p_subexpr):
    n1 = p_subexpr(s)
    if s.sy == op:
        pos = s.position()
        op = s.sy
        s.next()
        n2 = p_rassoc_binop_expr(s, op, p_subexpr)
        n1 = ExprNodes.binop_node(pos, op, n1, n2)
    elif s.sy in COMMON_BINOP_MISTAKES and COMMON_BINOP_MISTAKES[s.sy] == op:
        # Only report this for the current operator since we pass through here twice for 'and' and 'or'.
        warning(s.position(),
                "Found the C operator '%s', did you mean the Python operator '%s'?" % (s.sy, op),
                level=1)
    return n1


#and_test: not_test ('and' not_test)*

@cython.cfunc
def p_and_test(s: PyrexScanner):
    #return p_binop_expr(s, ('and',), p_not_test)
    return p_rassoc_binop_expr(s, 'and', p_not_test)


#not_test: 'not' not_test | comparison

@cython.cfunc
def p_not_test(s: PyrexScanner):
    if s.sy == 'not':
        pos = s.position()
        s.next()
        return ExprNodes.NotNode(pos, operand = p_not_test(s))
    else:
        return p_comparison(s)


#comparison: expr (comp_op expr)*
#comp_op: '<'|'>'|'=='|'>='|'<='|'<>'|'!='|'in'|'not' 'in'|'is'|'is' 'not'

@cython.cfunc
def p_comparison(s: PyrexScanner):
    n1 = p_starred_expr(s)
    if s.sy in comparison_ops:
        pos = s.position()
        op = p_cmp_op(s)
        n2 = p_starred_expr(s)
        n1 = ExprNodes.PrimaryCmpNode(pos,
            operator = op, operand1 = n1, operand2 = n2)
        if s.sy in comparison_ops:
            n1.cascade = p_cascaded_cmp(s)
    return n1


@cython.cfunc
def p_test_or_starred_expr(s: PyrexScanner):
    if s.sy == '*':
        return p_starred_expr(s)
    else:
        return p_test(s)


@cython.cfunc
def p_namedexpr_test_or_starred_expr(s: PyrexScanner):
    if s.sy == '*':
        return p_starred_expr(s)
    else:
        return p_namedexpr_test(s)


@cython.cfunc
def p_starred_expr(s: PyrexScanner):
    pos = s.position()
    if s.sy == '*':
        starred = True
        s.next()
    else:
        starred = False
    expr = p_bit_expr(s)
    if starred:
        expr = ExprNodes.StarredUnpackingNode(pos, expr)
    return expr


@cython.cfunc
def p_cascaded_cmp(s: PyrexScanner):
    pos = s.position()
    op = p_cmp_op(s)
    n2 = p_starred_expr(s)
    result = ExprNodes.CascadedCmpNode(pos,
        operator = op, operand2 = n2)
    if s.sy in comparison_ops:
        result.cascade = p_cascaded_cmp(s)
    return result


@cython.cfunc
def p_cmp_op(s: PyrexScanner):
    if s.sy == 'not':
        s.next()
        s.expect('in')
        op = 'not_in'
    elif s.sy == 'is':
        s.next()
        if s.sy == 'not':
            s.next()
            op = 'is_not'
        else:
            op = 'is'
    else:
        op = s.sy
        s.next()
    if op == '<>':
        op = '!='
    return op


comparison_ops = cython.declare(frozenset, frozenset((
    '<', '>', '==', '>=', '<=', '<>', '!=',
    'in', 'is', 'not'
)))


#expr: xor_expr ('|' xor_expr)*

@cython.cfunc
def p_bit_expr(s: PyrexScanner):
    return p_binop_expr(s, ('|',), p_xor_expr)


#xor_expr: and_expr ('^' and_expr)*

@cython.cfunc
def p_xor_expr(s: PyrexScanner):
    return p_binop_expr(s, ('^',), p_and_expr)


#and_expr: shift_expr ('&' shift_expr)*

@cython.cfunc
def p_and_expr(s: PyrexScanner):
    return p_binop_expr(s, ('&',), p_shift_expr)


#shift_expr: arith_expr (('<<'|'>>') arith_expr)*

@cython.cfunc
def p_shift_expr(s: PyrexScanner):
    return p_binop_expr(s, ('<<', '>>'), p_arith_expr)


#arith_expr: term (('+'|'-') term)*

@cython.cfunc
def p_arith_expr(s: PyrexScanner):
    return p_binop_expr(s, ('+', '-'), p_term)


#term: factor (('*'|'@'|'/'|'%'|'//') factor)*

@cython.cfunc
def p_term(s: PyrexScanner):
    return p_binop_expr(s, ('*', '@', '/', '%', '//'), p_factor)


#factor: ('+'|'-'|'~'|'&'|typecast|sizeof) factor | power

@cython.cfunc
def p_factor(s: PyrexScanner):
    # little indirection for C-ification purposes
    return _p_factor(s)


@cython.cfunc
def _p_factor(s: PyrexScanner):
    sy = s.sy
    if sy in ('+', '-', '~'):
        op = s.sy
        pos = s.position()
        s.next()
        return ExprNodes.unop_node(pos, op, p_factor(s))
    elif not s.in_python_file:
        if sy == '&':
            pos = s.position()
            s.next()
            arg = p_factor(s)
            return ExprNodes.AmpersandNode(pos, operand = arg)
        elif sy == "<":
            return p_typecast(s)
        elif sy == 'IDENT' and s.systring == "sizeof":
            return p_sizeof(s)
    return p_power(s)


@cython.cfunc
def p_typecast(s: PyrexScanner):
    # s.sy == "<"
    pos = s.position()
    s.next()
    base_type = p_c_base_type(s)
    is_memslice = isinstance(base_type, Nodes.MemoryViewSliceTypeNode)
    is_other_unnamed_type = isinstance(base_type, (
        Nodes.TemplatedTypeNode,
        Nodes.CConstOrVolatileTypeNode,
        Nodes.CTupleBaseTypeNode,
    ))
    if not (is_memslice or is_other_unnamed_type) and base_type.name is None:
        s.error("Unknown type")
    declarator = p_c_declarator(s, empty=True)
    if s.sy == '?':
        s.next()
        typecheck = True
    else:
        typecheck = False
    s.expect(">")
    operand = p_factor(s)
    if is_memslice:
        return ExprNodes.CythonArrayNode(pos, base_type_node=base_type, operand=operand)

    return ExprNodes.TypecastNode(pos,
        base_type = base_type,
        declarator = declarator,
        operand = operand,
        typecheck = typecheck)


@cython.cfunc
def p_sizeof(s: PyrexScanner):
    # s.sy == ident "sizeof"
    pos = s.position()
    s.next()
    s.expect('(')
    # Here we decide if we are looking at an expression or type
    # If it is actually a type, but parsable as an expression,
    # we treat it as an expression here.
    if looking_at_expr(s):
        operand = p_test(s)
        node = ExprNodes.SizeofVarNode(pos, operand = operand)
    else:
        base_type = p_c_base_type(s)
        declarator = p_c_declarator(s, empty=True)
        node = ExprNodes.SizeofTypeNode(pos,
            base_type = base_type, declarator = declarator)
    s.expect(')')
    return node


@cython.cfunc
def p_yield_expression(s: PyrexScanner, statement_terminators: frozenset = statement_terminators):
    # s.sy == "yield"
    pos = s.position()
    s.next()
    is_yield_from = False
    if s.sy == 'from':
        is_yield_from = True
        s.next()
    if s.sy != ')' and s.sy not in statement_terminators:
        # "yield from" does not support implicit tuples, but "yield" does ("yield 1,2")
        arg = p_test(s) if is_yield_from else p_testlist(s)
    else:
        if is_yield_from:
            s.error("'yield from' requires a source argument",
                    pos=pos, fatal=False)
        arg = None
    if is_yield_from:
        return ExprNodes.YieldFromExprNode(pos, arg=arg)
    else:
        return ExprNodes.YieldExprNode(pos, arg=arg)


@cython.cfunc
def p_yield_statement(s: PyrexScanner):
    # s.sy == "yield"
    yield_expr = p_yield_expression(s)
    return Nodes.ExprStatNode(yield_expr.pos, expr=yield_expr)


@cython.cfunc
def p_async_statement(s: PyrexScanner, ctx, decorators):
    # s.sy >> 'async' ...
    if s.sy == 'def':
        # 'async def' statements aren't allowed in pxd files
        if 'pxd' in ctx.level:
            s.error('def statement not allowed here')
        s.level = ctx.level
        return p_def_statement(s, decorators, is_async_def=True)
    elif decorators:
        s.error("Decorators can only be followed by functions or classes")
    elif s.sy == 'for':
        return p_for_statement(s, is_async=True)
    elif s.sy == 'with':
        s.next()
        return p_with_items(s, is_async=True)
    else:
        s.error("expected one of 'def', 'for', 'with' after 'async'")


#power: atom_expr ('**' factor)*
#atom_expr: ['await'] atom trailer*

@cython.cfunc
def p_power(s: PyrexScanner):
    if s.systring == 'new' and s.peek()[0] == 'IDENT':
        return p_new_expr(s)
    await_pos = None
    if s.sy == 'await':
        await_pos = s.position()
        s.next()
    n1 = p_atom(s)
    while s.sy in ('(', '[', '.'):
        n1 = p_trailer(s, n1)
    if await_pos:
        n1 = ExprNodes.AwaitExprNode(await_pos, arg=n1)
    if s.sy == '**':
        pos = s.position()
        s.next()
        n2 = p_factor(s)
        n1 = ExprNodes.binop_node(pos, '**', n1, n2)
    return n1


@cython.cfunc
def p_new_expr(s: PyrexScanner):
    # s.systring == 'new'.
    pos = s.position()
    s.next()
    cppclass = p_c_base_type(s)
    return p_call(s, ExprNodes.NewExprNode(pos, cppclass = cppclass))


#trailer: '(' [arglist] ')' | '[' subscriptlist ']' | '.' NAME

@cython.cfunc
def p_trailer(s: PyrexScanner, node1):
    pos = s.position()
    if s.sy == '(':
        return p_call(s, node1)
    elif s.sy == '[':
        return p_index(s, node1)
    else:  # s.sy == '.'
        s.next()
        name = p_ident(s)
        return ExprNodes.AttributeNode(pos,
            obj=node1, attribute=name)


# arglist:  argument (',' argument)* [',']
# argument: [test '='] test       # Really [keyword '='] test

# since PEP 448:
# argument: ( test [comp_for] |
#             test '=' test |
#             '**' expr |
#             star_expr )

@cython.cfunc
def p_call_parse_args(s: PyrexScanner, allow_genexp: cython.bint = True):
    # s.sy == '('
    s.next()
    positional_args = []
    keyword_args = []
    starstar_seen = False
    last_was_tuple_unpack = False
    while s.sy != ')':
        if s.sy == '*':
            if starstar_seen:
                s.error("Non-keyword arg following keyword arg", pos=s.position())
            s.next()
            positional_args.append(p_test(s))
            last_was_tuple_unpack = True
        elif s.sy == '**':
            s.next()
            keyword_args.append(p_test(s))
            starstar_seen = True
        else:
            arg = p_namedexpr_test(s)
            if s.sy == '=':
                s.next()
                if not arg.is_name:
                    s.error("Expected an identifier before '='",
                            pos=arg.pos)
                encoded_name = s.context.intern_ustring(arg.name)
                keyword = ExprNodes.IdentifierStringNode(
                    arg.pos, value=encoded_name)
                arg = p_test(s)
                keyword_args.append((keyword, arg))
            else:
                if keyword_args:
                    s.error("Non-keyword arg following keyword arg", pos=arg.pos)
                if positional_args and not last_was_tuple_unpack:
                    positional_args[-1].append(arg)
                else:
                    positional_args.append([arg])
                last_was_tuple_unpack = False
        if s.sy != ',':
            break
        s.next()

    if s.sy in ('for', 'async') and allow_genexp:
        if not keyword_args and not last_was_tuple_unpack:
            if len(positional_args) == 1 and len(positional_args[0]) == 1:
                positional_args = [[p_genexp(s, positional_args[0][0])]]
    s.expect(')')
    return positional_args or [[]], keyword_args


@cython.cfunc
def p_call_build_packed_args(pos, positional_args, keyword_args) -> tuple:
    keyword_dict = None

    subtuples = [
        ExprNodes.TupleNode(pos, args=arg) if isinstance(arg, list) else ExprNodes.AsTupleNode(pos, arg=arg)
        for arg in positional_args
    ]
    # TODO: implement a faster way to join tuples than creating each one and adding them
    arg_tuple = reduce(partial(ExprNodes.binop_node, pos, '+'), subtuples)

    if keyword_args:
        kwargs = []
        dict_items = []
        for item in keyword_args:
            if isinstance(item, tuple):
                key, value = item
                dict_items.append(ExprNodes.DictItemNode(pos=key.pos, key=key, value=value))
            elif item.is_dict_literal:
                # unpack "**{a:b}" directly
                dict_items.extend(item.key_value_pairs)
            else:
                if dict_items:
                    kwargs.append(ExprNodes.DictNode(
                        dict_items[0].pos, key_value_pairs=dict_items, reject_duplicates=True))
                    dict_items = []
                kwargs.append(item)

        if dict_items:
            kwargs.append(ExprNodes.DictNode(
                dict_items[0].pos, key_value_pairs=dict_items, reject_duplicates=True))

        if kwargs:
            if len(kwargs) == 1 and kwargs[0].is_dict_literal:
                # only simple keyword arguments found -> one dict
                keyword_dict = kwargs[0]
            else:
                # at least one **kwargs
                keyword_dict = ExprNodes.MergedDictNode(pos, keyword_args=kwargs)

    return arg_tuple, keyword_dict


@cython.cfunc
def p_call(s: PyrexScanner, function):
    # s.sy == '('
    pos = s.position()
    positional_args, keyword_args = p_call_parse_args(s)

    if not keyword_args and len(positional_args) == 1 and isinstance(positional_args[0], list):
        return ExprNodes.SimpleCallNode(pos, function=function, args=positional_args[0])
    else:
        arg_tuple, keyword_dict = p_call_build_packed_args(pos, positional_args, keyword_args)
        return ExprNodes.GeneralCallNode(
            pos, function=function, positional_args=arg_tuple, keyword_args=keyword_dict)


#lambdef: 'lambda' [varargslist] ':' test

#subscriptlist: subscript (',' subscript)* [',']

@cython.cfunc
def p_index(s: PyrexScanner, base):
    # s.sy == '['
    pos = s.position()
    s.next()
    subscripts, is_single_value = p_subscript_list(s)
    if is_single_value and len(subscripts[0]) == 2:
        start, stop = subscripts[0]
        result = ExprNodes.SliceIndexNode(pos,
            base = base, start = start, stop = stop)
    else:
        indexes = make_slice_nodes(pos, subscripts)
        if is_single_value:
            index = indexes[0]
        else:
            index = ExprNodes.TupleNode(pos, args = indexes)
        result = ExprNodes.IndexNode(pos,
            base = base, index = index)
    s.expect(']')
    return result


@cython.cfunc
def p_subscript_list(s: PyrexScanner) -> tuple:
    is_single_value = True
    items = [p_subscript(s)]
    while s.sy == ',':
        is_single_value = False
        s.next()
        if s.sy == ']':
            break
        items.append(p_subscript(s))
    return items, is_single_value


#subscript: '.' '.' '.' | test | [test] ':' [test] [':' [test]]

@cython.cfunc
def p_subscript(s: PyrexScanner):
    # Parse a subscript and return a list of
    # 1, 2 or 3 ExprNodes, depending on how
    # many slice elements were encountered.
    start = p_slice_element(s, (':',))
    if s.sy != ':':
        return [start]
    s.next()
    stop = p_slice_element(s, (':', ',', ']'))
    if s.sy != ':':
        return [start, stop]
    s.next()
    step = p_slice_element(s, (':', ',', ']'))
    return [start, stop, step]


@cython.cfunc
def p_slice_element(s: PyrexScanner, follow_set):
    # Simple expression which may be missing iff
    # it is followed by something in follow_set.
    if s.sy not in follow_set:
        return p_test(s)
    else:
        return None


@cython.cfunc
def expect_ellipsis(s: PyrexScanner):
    s.expect('...')


@cython.cfunc
def make_slice_nodes(pos, subscripts):
    # Convert a list of subscripts as returned
    # by p_subscript_list into a list of ExprNodes,
    # creating SliceNodes for elements with 2 or
    # more components.
    result = []
    for subscript in subscripts:
        if len(subscript) == 1:
            result.append(subscript[0])
        else:
            result.append(make_slice_node(pos, *subscript))
    return result


@cython.ccall
def make_slice_node(pos, start, stop = None, step = None):
    if not start:
        start = ExprNodes.NoneNode(pos)
    if not stop:
        stop = ExprNodes.NoneNode(pos)
    if not step:
        step = ExprNodes.NoneNode(pos)
    return ExprNodes.SliceNode(pos,
        start = start, stop = stop, step = step)


#atom: '(' [yield_expr|testlist_comp] ')' | '[' [listmaker] ']' | '{' [dict_or_set_maker] '}' | '`' testlist '`' | NAME | NUMBER | STRING+

@cython.cfunc
def p_atom(s: PyrexScanner):
    pos = s.position()
    sy = s.sy
    if sy == '(':
        s.next()
        if s.sy == ')':
            result = ExprNodes.TupleNode(pos, args = [])
        elif s.sy == 'yield':
            result = p_yield_expression(s)
        else:
            result = p_testlist_comp(s)
        s.expect(')')
        return result
    elif sy == '[':
        return p_list_maker(s)
    elif sy == '{':
        return p_dict_or_set_maker(s)
    elif sy == '`':
        return p_backquote_expr(s)
    elif sy == '...':
        expect_ellipsis(s)
        return ExprNodes.EllipsisNode(pos)
    elif sy == 'INT':
        return p_int_literal(s)
    elif sy == 'FLOAT':
        value = s.systring
        s.next()
        return ExprNodes.FloatNode(pos, value = value)
    elif sy == 'IMAG':
        value = s.systring[:-1]
        s.next()
        return ExprNodes.ImagNode(pos, value = value)
    elif sy == 'BEGIN_STRING' or sy == 'BEGIN_FT_STRING':
        return p_atom_string(s)
    elif sy == 'IDENT':
        result = p_atom_ident_constants(s)
        if result is None:
            result = p_name(s, s.systring)
            s.next()
        return result
    else:
        s.error("Expected an identifier or literal")


@cython.cfunc
def p_atom_string(s: PyrexScanner):
    # s.sy == 'BEGIN_STRING' or s.sy == 'BEGIN_FT_STRING'
    pos = s.position()
    kind, bytes_value, unicode_value = p_cat_string_literal(s)
    if not kind:
        return ExprNodes.UnicodeNode(pos, value=unicode_value, bytes_value=bytes_value)
    kind_char: cython.Py_UCS4 = kind
    if kind_char == 'c':
        return ExprNodes.CharNode(pos, value=bytes_value)
    elif kind_char == 'u':
        return ExprNodes.UnicodeNode(pos, value=unicode_value, bytes_value=bytes_value)
    elif kind_char == 'b':
        return ExprNodes.BytesNode(pos, value=bytes_value)
    elif kind_char == 'f':
        return ExprNodes.JoinedStrNode(pos, values=unicode_value)
    elif kind_char == 't':
        # TODO
        return ExprNodes.TemplateStringNode(pos, values=unicode_value)
    else:
        # This is actually prevented by the scanner (Lexicon.py).
        s.error(f"invalid string kind '{kind}'")


@cython.cfunc
def p_atom_ident_constants(s: PyrexScanner):
    """
    Returns None if it isn't a special-cased named constant.
    Only calls s.next() if it successfully matches a named constant.
    """
    # s.sy == 'IDENT'
    pos = s.position()
    name = s.systring
    if name == "None":
        result = ExprNodes.NoneNode(pos)
    elif name == "True":
        result = ExprNodes.BoolNode(pos, value=True)
    elif name == "False":
        result = ExprNodes.BoolNode(pos, value=False)
    elif name == "NULL" and not s.in_python_file:
        result = ExprNodes.NullNode(pos)
    else:
        return None
    s.next()
    return result


@cython.cfunc
def p_int_literal(s: PyrexScanner):
    pos = s.position()
    value: str = cython.cast(str, s.systring)
    s.next()
    unsigned = ""
    longness = ""
    while value[-1] in "UuLl":
        if value[-1] in "Ll":
            longness += "L"
        else:
            unsigned += "U"
        value = value[:-1]
    # '3L' is ambiguous in Py2 but not in Py3.  '3U' and '3LL' are
    # illegal in Py2 Python files.  All suffixes are illegal in Py3
    # Python files.
    is_c_literal = None
    if unsigned:
        is_c_literal = True
    elif longness:
        if longness == 'LL' or s.context.language_level >= 3:
            is_c_literal = True
    if s.in_python_file:
        if is_c_literal:
            error(pos, "illegal integer literal syntax in Python source file")
        is_c_literal = False
    return ExprNodes.IntNode(pos,
                             is_c_literal = is_c_literal,
                             value = value,
                             unsigned = unsigned,
                             longness = longness)


@cython.cfunc
def p_name(s: PyrexScanner, name):
    pos = s.position()
    if not s.compile_time_expr and name in s.compile_time_env:
        value = s.compile_time_env.lookup_here(name)
        node = wrap_compile_time_constant(pos, value)
        if node is not None:
            return node
    return ExprNodes.NameNode(pos, name=name)


@cython.cfunc
def wrap_compile_time_constant(pos, value):
    if value is None:
        return ExprNodes.NoneNode(pos)
    elif value is Ellipsis:
        return ExprNodes.EllipsisNode(pos)
    elif isinstance(value, bool):
        return ExprNodes.BoolNode(pos, value=value)
    elif isinstance(value, int):
        return ExprNodes.IntNode(pos, value=repr(value), constant_result=value)
    elif isinstance(value, float):
        return ExprNodes.FloatNode(pos, value=repr(value), constant_result=value)
    elif isinstance(value, complex):
        node = ExprNodes.ImagNode(pos, value=repr(value.imag), constant_result=complex(0.0, value.imag))
        if value.real:
            # FIXME: should we care about -0.0 ?
            # probably not worth using the '-' operator for negative imag values
            node = ExprNodes.binop_node(
                pos, '+', ExprNodes.FloatNode(pos, value=repr(value.real), constant_result=value.real), node,
                constant_result=value)
        return node
    elif isinstance(value, str):
        return ExprNodes.UnicodeNode(pos, value=EncodedString(value))
    elif isinstance(value, bytes):
        bvalue = bytes_literal(value, 'ascii')  # actually: unknown encoding, but BytesLiteral requires one
        return ExprNodes.BytesNode(pos, value=bvalue, constant_result=value)
    elif isinstance(value, tuple):
        args = [wrap_compile_time_constant(pos, arg) for arg in value]
        if None in args:
            # error already reported
            return None
        return ExprNodes.TupleNode(pos, args=args)

    error(pos, "Invalid type for compile-time constant: %r (type %s)"
               % (value, value.__class__.__name__))
    return None


@cython.cfunc
def p_cat_string_literal(s: PyrexScanner) -> tuple:
    # A sequence of one or more adjacent string literals.
    # Returns (kind, bytes_value, unicode_value)
    # where kind in ('b', 'c', 'u', 'f', 't', '')
    pos = s.position()
    kind, bytes_value, unicode_value = p_string_literal(s)
    if kind == 'c' or (s.sy != 'BEGIN_STRING' and s.sy != 'BEGIN_FT_STRING'):
        return kind, bytes_value, unicode_value
    bstrings, ustrings, positions = [bytes_value], [unicode_value], [pos]
    bytes_value = unicode_value = None
    while s.sy == 'BEGIN_STRING' or s.sy == 'BEGIN_FT_STRING':
        pos = s.position()
        next_kind, next_bytes_value, next_unicode_value = p_string_literal(s)
        if next_kind == 'c':
            error(pos, "Cannot concatenate char literal with another string or char literal")
            continue
        elif next_kind != kind:
            # concatenating f strings and normal strings is allowed and leads to an f string
            if {kind, next_kind} in ({'f', 'u'}, {'f', ''}):
                kind = 'f'
            elif kind == 't' or next_kind == 't':
                error(pos, "cannot mix t-string literals with string or bytes literals")
                continue
            else:
                error(pos, "Cannot mix string literals of different types, expected %s'', got %s''" % (
                    kind, next_kind))
                continue
        bstrings.append(next_bytes_value)
        ustrings.append(next_unicode_value)
        positions.append(pos)
    # join and rewrap the partial literals
    if kind in ('b', 'c', '') or kind == 'u' and None not in bstrings:
        # Py3 enforced unicode literals are parsed as bytes/unicode combination
        bytes_value = bytes_literal(b''.join(bstrings), s.source_encoding)
    if kind in ('u', ''):
        unicode_value = EncodedString(''.join([u for u in ustrings if u is not None]))
    if kind == 'f':
        unicode_value = []
        for u, pos in zip(ustrings, positions):
            if isinstance(u, list):
                unicode_value += u
            else:
                # non-f-string concatenated into the f-string
                unicode_value.append(ExprNodes.UnicodeNode(pos, value=EncodedString(u)))
    if kind == 't':
        unicode_value = []
        for u in ustrings:
            unicode_value.extend(u)
    return kind, bytes_value, unicode_value


@cython.cfunc
def p_opt_string_literal(s: PyrexScanner, required_type: str = 'u'):
    if s.sy != 'BEGIN_STRING':
        return None
    pos = s.position()
    kind, bytes_value, unicode_value = p_string_literal(s, required_type)
    if required_type == 'u':
        if kind == 'f':
            s.error("f-string not allowed here", pos)
        return unicode_value
    elif required_type == 'b':
        return bytes_value
    else:
        s.error("internal parser configuration error")


@cython.cfunc
def check_for_non_ascii_characters(string) -> cython.bint:
    s = cython.cast(str, string)  # EncodedString
    for c in s:
        if c >= '\x80':
            return True
    return False


@cython.cfunc
def p_string_literal_shared_read(
        s: PyrexScanner, pos, chars, kind,
        is_raw: cython.bint):
    """
    Returns a string of non-escaped characters (if handled) or none.
    If passed an escape sequence returns an empty string.
    """
    sy = s.sy
    systr = s.systring
    result = systr
    is_python3_source: cython.bint = s.context.language_level >= 3
    # print "p_string_literal: sy =", sy, repr(s.systring) ###
    if sy == 'CHARS':
        chars.append(systr)
    elif sy == 'ESCAPE':
        # in Py2, 'ur' raw unicode strings resolve unicode escapes but nothing else
        if is_raw and (is_python3_source or kind != 'u' or len(systr) < 2 or systr[1] not in 'Uu'):
            chars.append(systr)
        else:
            result = ""
            _append_escape_sequence(kind, chars, systr, s)
    elif sy == 'NEWLINE':
        chars.append('\n')
    elif sy == 'EOF':
        s.error("Unclosed string literal", pos=pos)
    else:
        return None
    return result

@cython.cfunc
def _validate_kind_string(pos, systring: str):
    kind_string = systring.rstrip('"\'').lower()
    if len(kind_string) <= 1 or (len(kind_string) == 2 and kind_string in "rbrurfrtr"):
        return kind_string
    # Otherwise an error of some sort
    unique_string_prefixes = set(kind_string)
    if len(unique_string_prefixes) != len(kind_string):
        error(pos, 'Duplicate string prefix character')
    unique_string_prefixes.discard('r')
    unique_string_prefixes = sorted(unique_string_prefixes)
    if len(unique_string_prefixes) >= 2:
        error(pos, f'String prefixes {unique_string_prefixes[0]} and {unique_string_prefixes[1]} cannot be combined')
    else:
        error(pos, f'Invalid string prefix {kind_string}')
    return ''

@cython.cfunc
def p_string_literal(s: PyrexScanner, kind_override=None) -> tuple:
    # A single string or char literal.  Returns (kind, bvalue, uvalue)
    # where kind in ('b', 'c', 'u', 'f', '').  The 'bvalue' is the source
    # code byte sequence of the string literal, 'uvalue' is the
    # decoded Unicode string.  Either of the two may be None depending
    # on the 'kind' of string, only unprefixed strings have both
    # representations. In f-strings, the uvalue is a list of the Unicode
    # strings and f-string expressions that make up the f-string.
    # s.sy == 'BEGIN_STRING' or s.sy == 'BEGIN_FT_STRING'
    if s.sy == 'BEGIN_FT_STRING':
        assert kind_override is None
        return p_ft_string_literal(s)
    pos = s.position()
    is_python3_source: cython.bint = s.context.language_level >= 3
    has_non_ascii_literal_characters = False
    kind_string = _validate_kind_string(pos, s.systring)

    is_raw: cython.bint = 'r' in kind_string

    if 'c' in kind_string:
        # this should never happen, since the lexer does not allow combining c
        # with other prefix characters
        if len(kind_string) != 1:
            error(pos, 'Invalid string prefix for character literal')
        kind = 'c'
    elif 'b' in kind_string:
        kind = 'b'
    elif 'u' in kind_string:
        kind = 'u'
    else:
        kind = ''

    if kind == '' and kind_override is None and Future.unicode_literals in s.context.future_directives:
        chars = StringEncoding.StrLiteralBuilder(s.source_encoding)
        kind = 'u'
    else:
        if kind_override is not None and kind_override in 'ub':
            kind = kind_override
        if kind in ('u', 'f'):  # f-strings are scanned exactly like Unicode literals, but are parsed further later
            chars = StringEncoding.UnicodeLiteralBuilder()
        elif kind == '':
            chars = StringEncoding.StrLiteralBuilder(s.source_encoding)
        else:
            chars = StringEncoding.BytesLiteralBuilder(s.source_encoding)

    while 1:
        s.next()
        handled_chars = p_string_literal_shared_read(
            s, pos, chars, kind,
            is_raw=is_raw)
        if handled_chars is not None:
            if (not has_non_ascii_literal_characters and
                    is_python3_source and Future.unicode_literals in s.context.future_directives):
                has_non_ascii_literal_characters = check_for_non_ascii_characters(handled_chars)
            continue
        if s.sy == 'END_STRING':
            break
        else:
            s.error("Unexpected token %r:%r in string literal" % (
                s.sy, s.systring))

    if kind == 'c':
        unicode_value = None
        bytes_value = chars.getchar()
        if len(bytes_value) != 1:
            error(pos, "invalid character literal: %r" % bytes_value)
    else:
        bytes_value, unicode_value = chars.getstrings()
        if (has_non_ascii_literal_characters
                and is_python3_source and Future.unicode_literals in s.context.future_directives):
            # Python 3 forbids literal non-ASCII characters in byte strings
            if kind == 'b':
                s.error("bytes can only contain ASCII literal characters.", pos=pos)
            bytes_value = None
    s.next()
    return (kind, bytes_value, unicode_value)


@cython.cfunc
def p_read_ft_string_expression(s: PyrexScanner):
    strings = []
    while True:
        s.next()
        sy = s.sy
        if sy in ["END_FT_STRING_EXPR",
                    # probably an error, but handle it elsewhere
                   "EOF", None]:
            if sy == "END_FT_STRING_EXPR":
                s.next()
            return ''.join(strings)
        strings.append(s.systring)


@cython.cfunc
def p_ft_string_replacement_field(s: PyrexScanner,
                                is_raw: cython.bint, is_single_quoted: cython.bint,
                                tf_string_kind: cython.Py_UCS4):
    result = []
    conversion_char = format_spec = expr = None
    t_string_expression = None
    self_documenting = False

    bracket_pos = s.position()
    expr_pos = (bracket_pos[0], bracket_pos[1], bracket_pos[2]+1)
    expr_string = p_read_ft_string_expression(s)
    if not expr_string.strip():
        error(bracket_pos,
              f"empty expression not allowed in {tf_string_kind}-string")
        result = []
    else:
        original_scanner = s
        s = PyrexScanner(
            StringIO(expr_string),
            bracket_pos[0],
            parent_scanner=s,
            source_encoding=s.source_encoding,
            initial_pos=expr_pos
        )
        s.bracket_nesting_level += 1
        if s.sy == "INDENT":
            s.next()
        if s.sy == 'yield':
            expr = p_yield_expression(
                s,
                statement_terminators=statement_terminators | {':', '}', '!'})
        else:
            expr = p_testlist_star_expr(s)

        if s.sy == "=":
            self_documenting = True
            s.next()

        if s.sy == "!":
            # format conversion
            previous_pos = s.position()
            s.next()
            conversion_char = s.systring
            # validate the conversion char
            if conversion_char in ['}', ':', '']:
                error(s.position(), "missing conversion character")
            elif not ExprNodes.FormattedValueNode.find_conversion_func(conversion_char):
                error(s.position(), "invalid conversion character '%s'" % conversion_char)
                s.next()
            elif s.position()[2] != (previous_pos[2] + 1):
                error(s.position(), "f-string: conversion type must come right after the exclamation mark")
                s.next()
            else:
                s.next()

        if self_documenting or tf_string_kind == 't':
            if conversion_char is not None:
                expr_string, _ = expr_string.rsplit('!', 1)
            if tf_string_kind == 't':
                t_string_expression = ExprNodes.UnicodeNode(
                    pos=expr_pos,
                    value=StringEncoding.EncodedString(expr_string.rstrip().rstrip('=').rstrip())
                )
            if self_documenting:
                result.append(
                    ExprNodes.UnicodeNode(
                        pos=expr_pos,
                        value=StringEncoding.EncodedString(expr_string)
                    )
                )

        # Validate that the expression string has actually ended
        while s.sy == "NEWLINE" or s.sy == "DEDENT":
            s.next()
        if s.sy != "EOF":
            error(
                s.position(),
                f"Unexpected characters after {tf_string_kind}-string expression: {s.systring}")

        s = original_scanner

    if s.sy == ":":
        # full format spec
        pos = s.position()
        # Contents of format spec are handled closer to an f-string than a t-string
        # (even for t-strings).
        format_spec_contents = p_ft_string_middles(s, is_raw, is_single_quoted, is_format_string=True, tf_string_kind='f')
        format_spec = ExprNodes.JoinedStrNode(
            pos,
            values=format_spec_contents
        )
    if self_documenting and conversion_char is None and format_spec is None:
        conversion_char = 'r'

    if conversion_char is not None:
        conversion_char = StringEncoding.EncodedString(conversion_char)
    if tf_string_kind == 't':
        result.append(ExprNodes.TStringInterpolationNode(
            bracket_pos, value=expr, conversion_char=conversion_char,
            format_spec=format_spec, expression_str=t_string_expression
        ))
    else:
        result.append(ExprNodes.FormattedValueNode(
            bracket_pos, value=expr, conversion_char=conversion_char,
            format_spec=format_spec
        ))
    return result

@cython.cfunc
def p_ft_string_middles(s: PyrexScanner,
                        is_raw: cython.bint, is_single_quoted: cython.bint,
                        is_format_string: cython.bint,
                        tf_string_kind: cython.Py_UCS4):
    middles: list = []
    builder = StringEncoding.UnicodeLiteralBuilder()
    pos = s.position()
    while True:
        s.next()
        sy = s.sy

        handled_chars = p_string_literal_shared_read(
            s, pos, builder, "u",
            is_raw=is_raw)
        if handled_chars is not None:
            continue

        if builder.chars:
            middles.append(ExprNodes.UnicodeNode(pos, value=builder.getstring()))
            builder = StringEncoding.UnicodeLiteralBuilder()
        if sy == "{":
            fields = p_ft_string_replacement_field(
                s, is_raw, is_single_quoted, tf_string_kind=tf_string_kind)
            middles.extend(fields)
            if not s.sy == '}':
                s.expected('}')
            continue
        elif sy == "END_FT_STRING":
            break
        elif s.sy == '}':
            if is_format_string:
                break
            # otherwise it's an error, but the scanner has reported it
        else:
            error(
                s.position(),
                "Unexpected token %r:%r in %s-string literal" % (
                s.sy, s.systring, tf_string_kind))
    return middles

@cython.cfunc
def p_ft_string_literal(s: PyrexScanner):
    # s.sy == BEGIN_FT_STRING
    kind_string = _validate_kind_string(s.position(), s.systring)
    tf_string_kind: cython.Py_UCS4 = 't' if 't' in kind_string else 'f'
    is_raw: cython.bint = 'r' in kind_string
    quotes = s.systring.lstrip("rRbBuUfFtT")
    is_single_quoted: cython.bint = len(quotes) != 3
    middles = p_ft_string_middles(s, is_raw, is_single_quoted, is_format_string=False, tf_string_kind=tf_string_kind)
    if s.sy != "END_FT_STRING":
        s.expected(quotes)
    s.next()
    return tf_string_kind, None, middles


@cython.cfunc
def _append_escape_sequence(kind, builder, escape_sequence: str, s: PyrexScanner):
    if len(escape_sequence) < 2:
        builder.append("\\")  # invalid escape sequence, warned earlier
        return
    c = escape_sequence[1]
    if c in "01234567":
        builder.append_charval(int(escape_sequence[1:], 8))
    elif c in "'\"\\":
        builder.append(c)
    elif c in "abfnrtv":
        builder.append(StringEncoding.char_from_escape_sequence(escape_sequence))
    elif c == '\n':
        pass  # line continuation
    elif c == 'x':  # \xXX
        if len(escape_sequence) == 4:
            builder.append_charval(int(escape_sequence[2:], 16))
        else:
            s.error("Invalid hex escape '%s'" % escape_sequence, fatal=False)
    elif c in 'NUu' and kind in ('u', 'f', ''):  # \uxxxx, \Uxxxxxxxx, \N{...}
        chrval = -1
        if c == 'N':
            uchar = None
            try:
                uchar = lookup_unicodechar(escape_sequence[3:-1])
                chrval = ord(uchar)
            except KeyError:
                s.error("Unknown Unicode character name %s" %
                        repr(escape_sequence[3:-1]).lstrip('u'), fatal=False)
        elif len(escape_sequence) in (6, 10):
            chrval = int(escape_sequence[2:], 16)
            if chrval > 1114111:  # sys.maxunicode:
                s.error("Invalid unicode escape '%s'" % escape_sequence)
                chrval = -1
        else:
            s.error("Invalid unicode escape '%s'" % escape_sequence, fatal=False)
        if chrval >= 0:
            builder.append_uescape(chrval, escape_sequence)
    else:
        builder.append(escape_sequence)


# since PEP 448:
# list_display  ::=     "[" [listmaker] "]"
# listmaker     ::=     (named_test|star_expr) ( comp_for | (',' (named_test|star_expr))* [','] )
# comp_iter     ::=     comp_for | comp_if
# comp_for      ::=     ["async"] "for" expression_list "in" testlist [comp_iter]
# comp_if       ::=     "if" test [comp_iter]

@cython.cfunc
def p_list_maker(s: PyrexScanner):
    # s.sy == '['
    pos = s.position()
    s.next()
    if s.sy == ']':
        s.expect(']')
        return ExprNodes.ListNode(pos, args=[])

    expr = p_namedexpr_test_or_starred_expr(s)
    if s.sy in ('for', 'async'):
        if expr.is_starred:
            s.error("iterable unpacking cannot be used in comprehension")
        append = ExprNodes.ComprehensionAppendNode(pos, expr=expr)
        loop = p_comp_for(s, append)
        s.expect(']')
        return ExprNodes.ComprehensionNode(
            pos, loop=loop, append=append, type=Builtin.list_type,
            # list comprehensions leak their loop variable in Py2
            has_local_scope=s.context.language_level >= 3)

    # (merged) list literal
    if s.sy == ',':
        s.next()
        exprs = p_namedexpr_test_or_starred_expr_list(s, expr)
    else:
        exprs = [expr]
    s.expect(']')
    return ExprNodes.ListNode(pos, args=exprs)


@cython.cfunc
def p_comp_iter(s: PyrexScanner, body):
    if s.sy in ('for', 'async'):
        return p_comp_for(s, body)
    elif s.sy == 'if':
        return p_comp_if(s, body)
    else:
        # insert the 'append' operation into the loop
        return body


@cython.cfunc
def p_comp_for(s: PyrexScanner, body):
    pos = s.position()
    # [async] for ...
    is_async = False
    if s.sy == 'async':
        is_async = True
        s.next()

    # s.sy == 'for'
    s.expect('for')
    kw = p_for_bounds(s, allow_testlist=False, is_async=is_async)
    kw.update(else_clause=None, body=p_comp_iter(s, body), is_async=is_async)
    return Nodes.ForStatNode(pos, **kw)


@cython.cfunc
def p_comp_if(s: PyrexScanner, body):
    # s.sy == 'if'
    pos = s.position()
    s.next()
    # Note that Python 3.9+ is actually more restrictive here and Cython now follows
    # the Python 3.9+ behaviour: https://github.com/python/cpython/issues/86014
    # On Python <3.9 `[i for i in range(10) if lambda: i if True else 1]` was disallowed
    # but `[i for i in range(10) if lambda: i]` was allowed.
    # On Python >=3.9 they're both disallowed.
    test = p_or_test(s)
    return Nodes.IfStatNode(pos,
        if_clauses = [Nodes.IfClauseNode(pos, condition = test,
                                         body = p_comp_iter(s, body))],
        else_clause = None )


# since PEP 448:
#dictorsetmaker: ( ((test ':' test | '**' expr)
#                   (comp_for | (',' (test ':' test | '**' expr))* [','])) |
#                  ((test | star_expr)
#                   (comp_for | (',' (test | star_expr))* [','])) )

@cython.cfunc
def p_dict_or_set_maker(s: PyrexScanner):
    # s.sy == '{'
    pos = s.position()
    s.next()
    if s.sy == '}':
        s.next()
        return ExprNodes.DictNode(pos, key_value_pairs=[])

    parts = []
    target_type: cython.int = 0
    last_was_simple_item = False
    while True:
        if s.sy in ('*', '**'):
            # merged set/dict literal
            if target_type == 0:
                target_type = 1 if s.sy == '*' else 2  # 'stars'
            elif target_type != len(s.sy):
                s.error("unexpected %sitem found in %s literal" % (
                    s.sy, 'set' if target_type == 1 else 'dict'))
            s.next()
            if s.sy == '*':
                s.error("expected expression, found '*'")
            item = p_starred_expr(s)
            parts.append(item)
            last_was_simple_item = False
        else:
            item = p_test(s)
            if target_type == 0:
                target_type = 2 if s.sy == ':' else 1  # dict vs. set
            if target_type == 2:
                # dict literal
                s.expect(':')
                key = item
                value = p_test(s)
                item = ExprNodes.DictItemNode(key.pos, key=key, value=value)
            if last_was_simple_item:
                parts[-1].append(item)
            else:
                parts.append([item])
                last_was_simple_item = True

        if s.sy == ',':
            s.next()
            if s.sy == '}':
                break
        else:
            break

    if s.sy in ('for', 'async'):
        # dict/set comprehension
        if len(parts) == 1 and isinstance(parts[0], list) and len(parts[0]) == 1:
            item = parts[0][0]
            if target_type == 2:
                assert isinstance(item, ExprNodes.DictItemNode), type(item)
                comprehension_type = Builtin.dict_type
                append = ExprNodes.DictComprehensionAppendNode(
                    item.pos, key_expr=item.key, value_expr=item.value)
            else:
                comprehension_type = Builtin.set_type
                append = ExprNodes.ComprehensionAppendNode(item.pos, expr=item)
            loop = p_comp_for(s, append)
            s.expect('}')
            return ExprNodes.ComprehensionNode(pos, loop=loop, append=append, type=comprehension_type)
        else:
            # syntax error, try to find a good error message
            if len(parts) == 1 and not isinstance(parts[0], list):
                s.error("iterable unpacking cannot be used in comprehension")
            else:
                # e.g. "{1,2,3 for ..."
                s.expect('}')
            return ExprNodes.DictNode(pos, key_value_pairs=[])

    s.expect('}')
    if target_type == 1:
        # (merged) set literal
        items = []
        set_items = []
        for part in parts:
            if isinstance(part, list):
                set_items.extend(part)
            else:
                if set_items:
                    items.append(ExprNodes.SetNode(set_items[0].pos, args=set_items))
                    set_items = []
                items.append(part)
        if set_items:
            items.append(ExprNodes.SetNode(set_items[0].pos, args=set_items))
        if len(items) == 1 and items[0].is_set_literal:
            return items[0]
        return ExprNodes.MergedSequenceNode(pos, args=items, type=Builtin.set_type)
    else:
        # (merged) dict literal
        items = []
        dict_items = []
        for part in parts:
            if isinstance(part, list):
                dict_items.extend(part)
            else:
                if dict_items:
                    items.append(ExprNodes.DictNode(dict_items[0].pos, key_value_pairs=dict_items))
                    dict_items = []
                items.append(part)
        if dict_items:
            items.append(ExprNodes.DictNode(dict_items[0].pos, key_value_pairs=dict_items))
        if len(items) == 1 and items[0].is_dict_literal:
            return items[0]
        return ExprNodes.MergedDictNode(pos, keyword_args=items, reject_duplicates=False)


# NOTE: no longer in Py3 :)
@cython.cfunc
def p_backquote_expr(s: PyrexScanner):
    # s.sy == '`'
    pos = s.position()
    s.next()
    args = [p_test(s)]
    while s.sy == ',':
        s.next()
        args.append(p_test(s))
    s.expect('`')
    if len(args) == 1:
        arg = args[0]
    else:
        arg = ExprNodes.TupleNode(pos, args = args)
    return ExprNodes.BackquoteNode(pos, arg = arg)


@cython.cfunc
def p_simple_expr_list(s: PyrexScanner, expr=None) -> list:
    exprs: list = [expr] if expr is not None else []
    while s.sy not in expr_terminators:
        exprs.append( p_test(s) )
        if s.sy != ',':
            break
        s.next()
    return exprs


@cython.cfunc
def p_test_or_starred_expr_list(s: PyrexScanner, expr=None) -> list:
    exprs: list = [expr] if expr is not None else []
    while s.sy not in expr_terminators:
        exprs.append(p_test_or_starred_expr(s))
        if s.sy != ',':
            break
        s.next()
    return exprs


@cython.cfunc
def p_namedexpr_test_or_starred_expr_list(s: PyrexScanner, expr=None) -> list:
    exprs: list = [expr] if expr is not None else []
    while s.sy not in expr_terminators:
        exprs.append(p_namedexpr_test_or_starred_expr(s))
        if s.sy != ',':
            break
        s.next()
    return exprs


#testlist: test (',' test)* [',']

@cython.cfunc
def p_testlist(s: PyrexScanner):
    pos = s.position()
    expr = p_test(s)
    if s.sy == ',':
        s.next()
        exprs = p_simple_expr_list(s, expr)
        return ExprNodes.TupleNode(pos, args = exprs)
    else:
        return expr


# testlist_star_expr: (test|star_expr) ( comp_for | (',' (test|star_expr))* [','] )

@cython.cfunc
def p_testlist_star_expr(s: PyrexScanner):
    pos = s.position()
    expr = p_test_or_starred_expr(s)
    if s.sy == ',':
        s.next()
        exprs = p_test_or_starred_expr_list(s, expr)
        return ExprNodes.TupleNode(pos, args = exprs)
    else:
        return expr


# testlist_comp: (test|star_expr) ( comp_for | (',' (test|star_expr))* [','] )

@cython.cfunc
def p_testlist_comp(s: PyrexScanner):
    pos = s.position()
    expr = p_namedexpr_test_or_starred_expr(s)
    if s.sy == ',':
        s.next()
        exprs = p_namedexpr_test_or_starred_expr_list(s, expr)
        return ExprNodes.TupleNode(pos, args = exprs)
    elif s.sy in ('for', 'async'):
        return p_genexp(s, expr)
    else:
        return expr


@cython.cfunc
def p_genexp(s: PyrexScanner, expr):
    # s.sy == 'async' | 'for'
    loop = p_comp_for(s, Nodes.ExprStatNode(
        expr.pos, expr = ExprNodes.YieldExprNode(expr.pos, arg=expr)))
    return ExprNodes.GeneratorExpressionNode(expr.pos, loop=loop)


expr_terminators = cython.declare(frozenset, frozenset((
    ')', ']', '}', ':', '=', 'NEWLINE', 'EOF')))


#-------------------------------------------------------
#
#   Statements
#
#-------------------------------------------------------

@cython.cfunc
def p_global_statement(s: PyrexScanner):
    # assume s.sy == 'global'
    pos = s.position()
    s.next()
    names = p_ident_list(s)
    return Nodes.GlobalNode(pos, names = names)


@cython.cfunc
def p_nonlocal_statement(s: PyrexScanner):
    pos = s.position()
    s.next()
    names = p_ident_list(s)
    return Nodes.NonlocalNode(pos, names = names)


@cython.cfunc
def p_expression_or_assignment(s: PyrexScanner):
    expr = p_testlist_star_expr(s)
    has_annotation = False
    if s.sy == ':' and (expr.is_name or expr.is_subscript or expr.is_attribute):
        has_annotation = True
        s.next()
        expr.annotation = p_annotation(s)

    if s.sy == '=' and expr.is_starred:
        # This is a common enough error to make when learning Cython to let
        # it fail as early as possible and give a very clear error message.
        s.error("a starred assignment target must be in a list or tuple"
                " - maybe you meant to use an index assignment: var[0] = ...",
                pos=expr.pos)

    expr_list = [expr]
    while s.sy == '=':
        s.next()
        if s.sy == 'yield':
            expr = p_yield_expression(s)
        else:
            expr = p_testlist_star_expr(s)
        expr_list.append(expr)
    if len(expr_list) == 1:
        if re.match(r"([-+*/%^&|]|<<|>>|\*\*|//|@)=", s.sy):
            lhs = expr_list[0]
            if isinstance(lhs, ExprNodes.SliceIndexNode):
                # implementation requires IndexNode
                lhs = ExprNodes.IndexNode(
                    lhs.pos,
                    base=lhs.base,
                    index=make_slice_node(lhs.pos, lhs.start, lhs.stop))
            elif not isinstance(lhs, (ExprNodes.AttributeNode, ExprNodes.IndexNode, ExprNodes.NameNode)):
                error(lhs.pos, "Illegal operand for inplace operation.")
            operator = s.sy[:-1]
            s.next()
            if s.sy == 'yield':
                rhs = p_yield_expression(s)
            else:
                rhs = p_testlist(s)
            return Nodes.InPlaceAssignmentNode(lhs.pos, operator=operator, lhs=lhs, rhs=rhs)
        expr = expr_list[0]
        return Nodes.ExprStatNode(expr.pos, expr=expr)

    rhs = expr_list[-1]
    if len(expr_list) == 2:
        return Nodes.SingleAssignmentNode(rhs.pos, lhs=expr_list[0], rhs=rhs, first=has_annotation)
    else:
        return Nodes.CascadedAssignmentNode(rhs.pos, lhs_list=expr_list[:-1], rhs=rhs)


@cython.cfunc
def p_print_statement(s: PyrexScanner):
    # s.sy == 'print'
    pos = s.position()
    ends_with_comma: cython.bint = False
    s.next()
    if s.sy == '>>':
        s.next()
        stream = p_test(s)
        if s.sy == ',':
            s.next()
            ends_with_comma = s.sy in ('NEWLINE', 'EOF')
    else:
        stream = None
    args = []
    if s.sy not in ('NEWLINE', 'EOF'):
        args.append(p_test(s))
        while s.sy == ',':
            s.next()
            if s.sy in ('NEWLINE', 'EOF'):
                ends_with_comma = True
                break
            args.append(p_test(s))
    arg_tuple = ExprNodes.TupleNode(pos, args=args)
    return Nodes.PrintStatNode(pos,
        arg_tuple=arg_tuple, stream=stream,
        append_newline=not ends_with_comma)


@cython.cfunc
def p_exec_statement(s: PyrexScanner):
    # s.sy == 'exec'
    pos = s.position()
    s.next()
    code = p_bit_expr(s)
    if isinstance(code, ExprNodes.TupleNode):
        # Py3 compatibility syntax
        tuple_variant = True
        args = code.args
        if len(args) not in (2, 3):
            s.error("expected tuple of length 2 or 3, got length %d" % len(args),
                    pos=pos, fatal=False)
            args = [code]
    else:
        tuple_variant = False
        args = [code]
    if s.sy == 'in':
        if tuple_variant:
            s.error("tuple variant of exec does not support additional 'in' arguments",
                    fatal=False)
        s.next()
        args.append(p_test(s))
        if s.sy == ',':
            s.next()
            args.append(p_test(s))
    return Nodes.ExecStatNode(pos, args=args)


@cython.cfunc
def p_del_statement(s: PyrexScanner):
    # s.sy == 'del'
    pos = s.position()
    s.next()
    # FIXME: 'exprlist' in Python
    args = p_simple_expr_list(s)
    return Nodes.DelStatNode(pos, args = args)


@cython.cfunc
def p_pass_statement(s: PyrexScanner, with_newline: cython.bint = False):
    pos = s.position()
    s.expect('pass')
    if with_newline:
        s.expect_newline("Expected a newline", ignore_semicolon=True)
    return Nodes.PassStatNode(pos)


@cython.cfunc
def p_break_statement(s: PyrexScanner):
    # s.sy == 'break'
    pos = s.position()
    s.next()
    return Nodes.BreakStatNode(pos)


@cython.cfunc
def p_continue_statement(s: PyrexScanner):
    # s.sy == 'continue'
    pos = s.position()
    s.next()
    return Nodes.ContinueStatNode(pos)


@cython.cfunc
def p_return_statement(s: PyrexScanner):
    # s.sy == 'return'
    pos = s.position()
    s.next()
    if s.sy not in statement_terminators:
        value = p_testlist(s)
    else:
        value = None
    return Nodes.ReturnStatNode(pos, value = value)


@cython.cfunc
def p_raise_statement(s: PyrexScanner):
    # s.sy == 'raise'
    pos = s.position()
    s.next()
    exc_type = None
    exc_value = None
    exc_tb = None
    cause = None
    if s.sy not in statement_terminators:
        exc_type = p_test(s)
        if s.sy == ',':
            s.next()
            exc_value = p_test(s)
            if s.sy == ',':
                s.next()
                exc_tb = p_test(s)
        elif s.sy == 'from':
            s.next()
            cause = p_test(s)
    if exc_type or exc_value or exc_tb:
        return Nodes.RaiseStatNode(pos,
            exc_type = exc_type,
            exc_value = exc_value,
            exc_tb = exc_tb,
            cause = cause)
    else:
        return Nodes.ReraiseStatNode(pos)


@cython.cfunc
def p_import_statement(s: PyrexScanner):
    # s.sy in ('import', 'cimport')
    pos = s.position()
    kind = s.sy
    s.next()
    items = [p_dotted_name(s, as_allowed=True)]
    while s.sy == ',':
        s.next()
        items.append(p_dotted_name(s, as_allowed=True))
    stats = []
    is_absolute = Future.absolute_import in s.context.future_directives
    for pos, target_name, dotted_name, as_name in items:
        if kind == 'cimport':
            stat = Nodes.CImportStatNode(
                pos,
                module_name=dotted_name,
                as_name=as_name,
                is_absolute=is_absolute)
        else:
            stat = Nodes.SingleAssignmentNode(
                pos,
                lhs=ExprNodes.NameNode(pos, name=as_name or target_name),
                rhs=ExprNodes.ImportNode(
                    pos,
                    module_name=ExprNodes.IdentifierStringNode(pos, value=dotted_name),
                    is_import_as_name=bool(as_name),
                    level=0 if is_absolute else None,
                    imported_names=None))
        stats.append(stat)
    return Nodes.StatListNode(pos, stats=stats)


@cython.cfunc
def p_from_import_statement(s: PyrexScanner, first_statement: cython.bint = 0):
    # s.sy == 'from'
    pos = s.position()
    s.next()
    if s.sy in ('.', '...'):
        # count relative import level
        level = 0
        while s.sy in ('.', '...'):
            level += len(s.sy)
            s.next()
    else:
        level = None
    if level is not None and s.sy in ('import', 'cimport'):
        # we are dealing with "from .. import foo, bar"
        dotted_name_pos, dotted_name = s.position(), s.context.intern_ustring('')
    else:
        if level is None and Future.absolute_import in s.context.future_directives:
            level = 0
        (dotted_name_pos, _, dotted_name, _) = p_dotted_name(s, as_allowed=False)
    if s.sy not in ('import', 'cimport'):
        s.error("Expected 'import' or 'cimport'")
    kind = s.sy
    s.next()

    is_cimport = kind == 'cimport'
    is_parenthesized = False
    if s.sy == '*':
        imported_names = [(s.position(), s.context.intern_ustring("*"), None)]
        s.next()
    else:
        if s.sy == '(':
            is_parenthesized = True
            s.next()
        imported_names = [p_imported_name(s)]
    while s.sy == ',':
        s.next()
        if is_parenthesized and s.sy == ')':
            break
        imported_names.append(p_imported_name(s))
    if is_parenthesized:
        s.expect(')')
    if dotted_name == '__future__':
        if not first_statement:
            s.error("from __future__ imports must occur at the beginning of the file")
        elif level:
            s.error("invalid syntax")
        else:
            for (name_pos, name, as_name) in imported_names:
                if name == "braces":
                    s.error("not a chance", name_pos)
                    break
                try:
                    directive = getattr(Future, name)
                except AttributeError:
                    s.error("future feature %s is not defined" % name, name_pos)
                    break
                s.context.future_directives.add(directive)
        return Nodes.PassStatNode(pos)
    elif is_cimport:
        return Nodes.FromCImportStatNode(
            pos, module_name=dotted_name,
            relative_level=level,
            imported_names=imported_names)
    else:
        imported_name_strings = []
        items = []
        for (name_pos, name, as_name) in imported_names:
            imported_name_strings.append(
                ExprNodes.IdentifierStringNode(name_pos, value=name))
            items.append(
                (name, ExprNodes.NameNode(name_pos, name=as_name or name)))
        return Nodes.FromImportStatNode(pos,
            module = ExprNodes.ImportNode(dotted_name_pos,
                module_name = ExprNodes.IdentifierStringNode(pos, value = dotted_name),
                is_import_as_name = False,
                level = level,
                imported_names = imported_name_strings),
            items = items)


@cython.cfunc
def p_imported_name(s: PyrexScanner):
    pos = s.position()
    name = p_ident(s)
    as_name = p_as_name(s)
    return (pos, name, as_name)


@cython.cfunc
def p_dotted_name(s: PyrexScanner, as_allowed: cython.bint) -> tuple:
    pos = s.position()
    target_name = p_ident(s)
    as_name = None
    names = [target_name]
    while s.sy == '.':
        s.next()
        names.append(p_ident(s))
    if as_allowed:
        as_name = p_as_name(s)
    return (pos, target_name, s.context.intern_ustring('.'.join(names)), as_name)


@cython.cfunc
def p_as_name(s: PyrexScanner):
    if s.sy == 'IDENT' and s.systring == 'as':
        s.next()
        return p_ident(s)
    else:
        return None


@cython.cfunc
def p_assert_statement(s: PyrexScanner):
    # s.sy == 'assert'
    pos = s.position()
    s.next()
    cond = p_test(s)
    if s.sy == ',':
        s.next()
        value = p_test(s)
    else:
        value = None
    return Nodes.AssertStatNode(pos, condition=cond, value=value)


@cython.cfunc
def p_if_statement(s: PyrexScanner):
    # s.sy == 'if'
    pos = s.position()
    s.next()
    if_clauses = [p_if_clause(s)]
    while s.sy == 'elif':
        s.next()
        if_clauses.append(p_if_clause(s))
    else_clause = p_else_clause(s)
    return Nodes.IfStatNode(pos,
        if_clauses = if_clauses, else_clause = else_clause)


@cython.cfunc
def p_if_clause(s: PyrexScanner):
    pos = s.position()
    test = p_namedexpr_test(s)
    body = p_suite(s)
    return Nodes.IfClauseNode(pos,
        condition = test, body = body)


@cython.cfunc
def p_else_clause(s: PyrexScanner):
    if s.sy == 'else':
        s.next()
        return p_suite(s)
    else:
        return None


@cython.cfunc
def p_while_statement(s: PyrexScanner):
    # s.sy == 'while'
    pos = s.position()
    s.next()
    test = p_namedexpr_test(s)
    body = p_suite(s)
    else_clause = p_else_clause(s)
    return Nodes.WhileStatNode(pos,
        condition = test, body = body,
        else_clause = else_clause)


@cython.cfunc
def p_for_statement(s: PyrexScanner, is_async: cython.bint = False):
    # s.sy == 'for'
    pos = s.position()
    s.next()
    kw = p_for_bounds(s, allow_testlist=True, is_async=is_async)
    body = p_suite(s)
    else_clause = p_else_clause(s)
    kw.update(body=body, else_clause=else_clause, is_async=is_async)
    return Nodes.ForStatNode(pos, **kw)


@cython.cfunc
def p_for_bounds(s: PyrexScanner, allow_testlist: cython.bint = True, is_async: cython.bint = False) -> dict:
    target = p_for_target(s)
    if s.sy == 'in':
        s.next()
        iterator = p_for_iterator(s, allow_testlist, is_async=is_async)
        return dict(target=target, iterator=iterator)
    elif not s.in_python_file and not is_async:
        if s.sy == 'from':
            s.next()
            bound1 = p_bit_expr(s)
        else:
            # Support shorter "for a <= x < b" syntax
            bound1, target = target, None
        rel1 = p_for_from_relation(s)
        name2_pos = s.position()
        name2 = p_ident(s)
        rel2_pos = s.position()
        rel2 = p_for_from_relation(s)
        bound2 = p_bit_expr(s)
        step = p_for_from_step(s)
        if target is None:
            target = ExprNodes.NameNode(name2_pos, name = name2)
        else:
            if not target.is_name:
                error(target.pos,
                    "Target of for-from statement must be a variable name")
            elif name2 != target.name:
                error(name2_pos,
                    "Variable name in for-from range does not match target")
        if rel1[0] != rel2[0]:
            error(rel2_pos,
                "Relation directions in for-from do not match")
        return dict(target = target,
                    bound1 = bound1,
                    relation1 = rel1,
                    relation2 = rel2,
                    bound2 = bound2,
                    step = step,
                    )
    else:
        s.expect('in')
        return {}


@cython.cfunc
def p_for_from_relation(s: PyrexScanner):
    if s.sy in inequality_relations:
        op = s.sy
        s.next()
        return op
    else:
        s.error("Expected one of '<', '<=', '>' '>='")


@cython.cfunc
def p_for_from_step(s: PyrexScanner):
    if s.sy == 'IDENT' and s.systring == 'by':
        s.next()
        step = p_bit_expr(s)
        return step
    else:
        return None


inequality_relations = cython.declare(frozenset, frozenset((
    '<', '<=', '>', '>=')))


@cython.cfunc
def p_target(s: PyrexScanner, terminator: str):
    pos = s.position()
    expr = p_starred_expr(s)
    if s.sy == ',':
        s.next()
        exprs = [expr]
        while s.sy != terminator:
            exprs.append(p_starred_expr(s))
            if s.sy != ',':
                break
            s.next()
        return ExprNodes.TupleNode(pos, args = exprs)
    else:
        return expr


@cython.cfunc
def p_for_target(s: PyrexScanner):
    return p_target(s, 'in')


@cython.cfunc
def p_for_iterator(s: PyrexScanner, allow_testlist: cython.bint = True, is_async: cython.bint = False):
    pos = s.position()
    if allow_testlist:
        expr = p_testlist(s)
    else:
        expr = p_or_test(s)
    return (ExprNodes.AsyncIteratorNode if is_async else ExprNodes.IteratorNode)(pos, sequence=expr)


@cython.cfunc
def p_try_statement(s: PyrexScanner):
    # s.sy == 'try'
    pos = s.position()
    s.next()
    body = p_suite(s)
    except_clauses = []
    else_clause = None
    if s.sy in ('except', 'else'):
        while s.sy == 'except':
            except_clauses.append(p_except_clause(s))
        if s.sy == 'else':
            s.next()
            else_clause = p_suite(s)
        body = Nodes.TryExceptStatNode(pos,
            body = body, except_clauses = except_clauses,
            else_clause = else_clause)
        if s.sy != 'finally':
            return body
        # try-except-finally is equivalent to nested try-except/try-finally
    if s.sy == 'finally':
        s.next()
        finally_clause = p_suite(s)
        return Nodes.TryFinallyStatNode(pos,
            body = body, finally_clause = finally_clause)
    else:
        s.error("Expected 'except' or 'finally'")


@cython.cfunc
def p_except_clause(s: PyrexScanner):
    # s.sy == 'except'
    pos = s.position()
    s.next()
    exc_type = None
    exc_value = None
    is_except_as = False
    if s.sy != ':':
        exc_type = p_test(s)
        # normalise into list of single exception tests
        if isinstance(exc_type, ExprNodes.TupleNode):
            exc_type = exc_type.args
        else:
            exc_type = [exc_type]
        if s.sy == ',' or (s.sy == 'IDENT' and s.systring == 'as'
                           and s.context.language_level == 2):
            s.next()
            exc_value = p_test(s)
        elif s.sy == 'IDENT' and s.systring == 'as':
            # Py3 syntax requires a name here
            s.next()
            pos2 = s.position()
            name = p_ident(s)
            exc_value = ExprNodes.NameNode(pos2, name = name)
            is_except_as = True
    body = p_suite(s)
    return Nodes.ExceptClauseNode(pos,
        pattern = exc_type, target = exc_value,
        body = body, is_except_as=is_except_as)


@cython.cfunc
def p_include_statement(s: PyrexScanner, ctx):
    pos = s.position()
    s.next()  # 'include'
    unicode_include_file_name = p_string_literal(s, 'u')[2]
    s.expect_newline("Syntax error in include statement")
    if s.compile_time_eval:
        include_file_name = unicode_include_file_name
        include_file_path = s.context.find_include_file(include_file_name, pos)
        if include_file_path:
            s.included_files.append(include_file_name)
            source_desc = FileSourceDescriptor(include_file_path)
            with source_desc.get_file_object() as f:
                s2 = PyrexScanner(f, source_desc, s, source_encoding=f.encoding, parse_comments=s.parse_comments)
                tree = p_statement_list(s2, ctx)
            return tree
        else:
            return None
    else:
        return Nodes.PassStatNode(pos)


@cython.cfunc
def p_with_statement(s: PyrexScanner):
    s.next()  # 'with'
    if s.systring == 'template' and not s.in_python_file:
        node = p_with_template(s)
    else:
        node = p_with_items(s)
    return node


@cython.cfunc
def p_with_items(s: PyrexScanner, is_async: cython.bint = False):
    """
    Copied from CPython:
    | 'with' '(' a[asdl_withitem_seq*]=','.with_item+ ','? ')' ':' b=block {
        _PyAST_With(a, b, NULL, EXTRA) }
    | 'with' a[asdl_withitem_seq*]=','.with_item+ ':' tc=[TYPE_COMMENT] b=block {
        _PyAST_With(a, b, NEW_TYPE_COMMENT(p, tc), EXTRA) }
    Therefore the first thing to try is the bracket-enclosed
    version and if that fails try the regular version
    """
    brackets_succeeded = False
    items = ()  # unused, but static analysis fails to track that below
    if s.sy == '(':
        with tentatively_scan(s) as errors:
            s.next()
            items = p_with_items_list(s, is_async)
            s.expect(")")
            if s.sy != ":":
                # Fail - the message doesn't matter because we'll try the
                # non-bracket version so it'll never be shown
                s.error("")
        brackets_succeeded = not errors
    if not brackets_succeeded:
        # try the non-bracket version
        items = p_with_items_list(s, is_async)
    body = p_suite(s)
    for cls, pos, kwds in reversed(items):
        # construct the actual nodes now that we know what the body is
        body = cls(pos, body=body, **kwds)
    return body


@cython.cfunc
def p_with_items_list(s: PyrexScanner, is_async: cython.bint) -> list:
    items = []
    while True:
        items.append(p_with_item(s, is_async))
        if s.sy != ",":
            break
        s.next()
        if s.sy == ")":
            # trailing commas allowed
            break
    return items


@cython.cfunc
def p_with_item(s: PyrexScanner, is_async: cython.bint) -> tuple:
    # In contrast to most parsing functions, this returns a tuple of
    #  class, pos, kwd_dict
    # This is because GILStatNode does a reasonable amount of initialization in its
    # constructor, and requires "body" to be set, which we don't currently have
    pos = s.position()
    if not s.in_python_file and s.sy == 'IDENT' and s.systring in ('nogil', 'gil'):
        if is_async:
            s.error("with gil/nogil cannot be async")
        state = s.systring
        s.next()

        # support conditional gil/nogil
        condition = None
        if s.sy == '(':
            s.next()
            condition = p_test(s)
            s.expect(')')

        return Nodes.GILStatNode, pos, {"state": state, "condition": condition}
    else:
        manager = p_test(s)
        target = None
        if s.sy == 'IDENT' and s.systring == 'as':
            s.next()
            target = p_starred_expr(s)
        return Nodes.WithStatNode, pos, {"manager": manager, "target": target, "is_async": is_async}


@cython.cfunc
def p_with_template(s: PyrexScanner):
    pos = s.position()
    templates = []
    s.next()
    s.expect('[')
    templates.append(s.systring)
    s.next()
    while s.systring == ',':
        s.next()
        templates.append(s.systring)
        s.next()
    s.expect(']')
    if s.sy == ':':
        s.next()
        s.expect_newline("Syntax error in template function declaration")
        s.expect_indent()
        body_ctx = Ctx()
        body_ctx.templates = templates
        func_or_var = p_c_func_or_var_declaration(s, pos, body_ctx)
        s.expect_dedent()
        return func_or_var
    else:
        error(pos, "Syntax error in template function declaration")


@cython.cfunc
def p_simple_statement(s: PyrexScanner, first_statement: cython.bint = 0):
    #print "p_simple_statement:", s.sy, s.systring ###
    if s.sy == 'global':
        node = p_global_statement(s)
    elif s.sy == 'nonlocal':
        node = p_nonlocal_statement(s)
    elif s.sy == 'print':
        node = p_print_statement(s)
    elif s.sy == 'exec':
        node = p_exec_statement(s)
    elif s.sy == 'del':
        node = p_del_statement(s)
    elif s.sy == 'break':
        node = p_break_statement(s)
    elif s.sy == 'continue':
        node = p_continue_statement(s)
    elif s.sy == 'return':
        node = p_return_statement(s)
    elif s.sy == 'raise':
        node = p_raise_statement(s)
    elif s.sy in ('import', 'cimport'):
        node = p_import_statement(s)
    elif s.sy == 'from':
        node = p_from_import_statement(s, first_statement = first_statement)
    elif s.sy == 'yield':
        node = p_yield_statement(s)
    elif s.sy == 'assert':
        node = p_assert_statement(s)
    elif s.sy == 'pass':
        node = p_pass_statement(s)
    else:
        node = p_expression_or_assignment(s)
    return node


@cython.cfunc
def p_simple_statement_list(s: PyrexScanner, ctx, first_statement: cython.bint = 0):
    # Parse a series of simple statements on one line
    # separated by semicolons.
    stat = p_simple_statement(s, first_statement = first_statement)
    pos = stat.pos
    stats = []
    if not isinstance(stat, Nodes.PassStatNode):
        stats.append(stat)
    while s.sy == ';':
        #print "p_simple_statement_list: maybe more to follow" ###
        s.next()
        if s.sy in ('NEWLINE', 'EOF'):
            break
        stat = p_simple_statement(s, first_statement = first_statement)
        if isinstance(stat, Nodes.PassStatNode):
            continue
        stats.append(stat)
        first_statement = False

    if not stats:
        stat = Nodes.PassStatNode(pos)
    elif len(stats) == 1:
        stat = stats[0]
    else:
        stat = Nodes.StatListNode(pos, stats = stats)

    if s.sy not in ('NEWLINE', 'EOF'):
        # provide a better error message for users who accidentally write Cython code in .py files
        if isinstance(stat, Nodes.ExprStatNode):
            if stat.expr.is_name and stat.expr.name == 'cdef':
                s.error("The 'cdef' keyword is only allowed in Cython files (pyx/pxi/pxd)", pos)
    s.expect_newline("Syntax error in simple statement list")

    return stat


@cython.cfunc
def p_compile_time_expr(s: PyrexScanner):
    old = s.compile_time_expr
    s.compile_time_expr = 1
    expr = p_testlist(s)
    s.compile_time_expr = old
    return expr


@cython.cfunc
def p_DEF_statement(s: PyrexScanner):
    pos = s.position()
    denv = s.compile_time_env
    s.next()  # 'DEF'
    name = p_ident(s)
    s.expect('=')
    expr = p_compile_time_expr(s)
    if s.compile_time_eval:
        value = expr.compile_time_value(denv)
        #print "p_DEF_statement: %s = %r" % (name, value) ###
        denv.declare(name, value)
    s.expect_newline("Expected a newline", ignore_semicolon=True)
    return Nodes.PassStatNode(pos)


@cython.cfunc
def p_IF_statement(s: PyrexScanner, ctx):
    pos = s.position()
    saved_eval = s.compile_time_eval
    current_eval = saved_eval
    denv = s.compile_time_env
    result = None
    while 1:
        s.next()  # 'IF' or 'ELIF'
        expr = p_compile_time_expr(s)
        s.compile_time_eval = current_eval and bool(expr.compile_time_value(denv))
        body = p_suite(s, ctx)
        if s.compile_time_eval:
            result = body
            current_eval = 0
        if s.sy != 'ELIF':
            break
    if s.sy == 'ELSE':
        s.next()
        s.compile_time_eval = current_eval
        body = p_suite(s, ctx)
        if current_eval:
            result = body
    if not result:
        result = Nodes.PassStatNode(pos)
    s.compile_time_eval = saved_eval
    return result


@cython.cfunc
def p_statement(s: PyrexScanner, ctx, first_statement: cython.bint = False):
    cdef_flag: cython.bint = ctx.cdef_flag
    pos = s.position()
    decorators = None
    if s.sy == 'ctypedef':
        if ctx.level not in ('module', 'module_pxd'):
            s.error("ctypedef statement not allowed here")
        #if ctx.api:
        #    error(pos, "'api' not allowed with 'ctypedef'")
        return p_ctypedef_statement(s, ctx)
    elif s.sy == 'DEF':
        # We used to dep-warn about this but removed the warning again since
        # we don't have a good answer yet for all use cases.
        if s.context.compiler_directives.get("warn.deprecated.DEF", False):
            warning(pos,
                    "The 'DEF' statement  will be removed in a future Cython version. "
                    "Consider using global variables, constants, and in-place literals instead. "
                    "See https://github.com/cython/cython/issues/4310", level=1)
        return p_DEF_statement(s)
    elif s.sy == 'IF':
        if s.context.compiler_directives.get("warn.deprecated.IF", True):
            warning(pos,
                    "The 'IF' statement is deprecated and will be removed in a future Cython version. "
                    "Consider using runtime conditions or C macros instead. "
                    "See https://github.com/cython/cython/issues/4310", level=1)
        return p_IF_statement(s, ctx)
    elif s.sy == '@':
        if ctx.level not in ('module', 'class', 'c_class', 'function', 'property', 'module_pxd', 'c_class_pxd', 'other'):
            s.error('decorator not allowed here')
        s.level = ctx.level
        decorators = p_decorators(s)
        if not ctx.allow_struct_enum_decorator and s.sy not in ('def', 'cdef', 'cpdef', 'class', 'async'):
            if s.sy == 'IDENT' and s.systring == 'async':
                pass  # handled below
            else:
                s.error("Decorators can only be followed by functions or classes")
    elif s.sy == 'pass' and cdef_flag:
        # empty cdef block
        return p_pass_statement(s, with_newline=True)

    overridable = False
    if s.sy == 'cdef':
        cdef_flag = True
        s.next()
    elif s.sy == 'cpdef':
        cdef_flag = True
        overridable = True
        s.next()
    if cdef_flag:
        if ctx.level not in ('module', 'module_pxd', 'function', 'c_class', 'c_class_pxd'):
            s.error('cdef statement not allowed here')
        s.level = ctx.level
        node = p_cdef_statement(s, pos, ctx(overridable=overridable))
        if decorators is not None:
            tup = (Nodes.CFuncDefNode, Nodes.CVarDefNode, Nodes.CClassDefNode)
            if ctx.allow_struct_enum_decorator:
                tup += (Nodes.CStructOrUnionDefNode, Nodes.CEnumDefNode)
            if not isinstance(node, tup):
                s.error("Decorators can only be followed by functions or classes")
            node.decorators = decorators
        return node
    else:
        if ctx.api:
            s.error("'api' not allowed with this statement", fatal=False)
        elif s.sy == 'def':
            # def statements aren't allowed in pxd files, except
            # as part of a cdef class
            if ('pxd' in ctx.level) and (ctx.level != 'c_class_pxd'):
                s.error('def statement not allowed here')
            s.level = ctx.level
            return p_def_statement(s, decorators)
        elif s.sy == 'class':
            if ctx.level not in ('module', 'function', 'class', 'other'):
                s.error("class definition not allowed here")
            return p_class_statement(s, decorators)
        elif s.sy == 'include':
            if ctx.level not in ('module', 'module_pxd'):
                s.error("include statement not allowed here")
            return p_include_statement(s, ctx)
        elif ctx.level == 'c_class' and s.sy == 'IDENT' and s.systring == 'property':
            return p_property_decl(s)
        elif s.sy == 'pass' and ctx.level != 'property':
            return p_pass_statement(s, with_newline=True)
        else:
            if ctx.level in ('c_class_pxd', 'property'):
                node = p_ignorable_statement(s)
                if node is not None:
                    return node
                s.error("Executable statement not allowed here")
            if s.sy == 'if':
                return p_if_statement(s)
            elif s.sy == 'while':
                return p_while_statement(s)
            elif s.sy == 'for':
                return p_for_statement(s)
            elif s.sy == 'try':
                return p_try_statement(s)
            elif s.sy == 'with':
                return p_with_statement(s)
            elif s.sy == 'async':
                s.next()
                return p_async_statement(s, ctx, decorators)
            else:
                if s.sy == 'IDENT' and s.systring == 'async':
                    ident_name = s.systring
                    ident_pos = s.position()
                    # PEP 492 enables the async/await keywords when it spots "async def ..."
                    s.next()
                    if s.sy == 'def':
                        return p_async_statement(s, ctx, decorators)
                    elif decorators:
                        s.error("Decorators can only be followed by functions or classes")
                    s.put_back('IDENT', ident_name, ident_pos)  # re-insert original token
                if s.sy == 'IDENT' and s.systring == 'match':
                    # p_match_statement returns None on a "soft" initial failure
                    match_statement = p_match_statement(s, ctx)
                    if match_statement is not None:
                        return match_statement
                return p_simple_statement_list(s, ctx, first_statement=first_statement)


@cython.cfunc
def p_statement_list(s: PyrexScanner, ctx, first_statement: cython.bint = 0):
    # Parse a series of statements separated by newlines.
    pos = s.position()
    stats = []
    while s.sy not in ('DEDENT', 'EOF'):
        stat = p_statement(s, ctx, first_statement = first_statement)
        if isinstance(stat, Nodes.PassStatNode):
            continue
        stats.append(stat)
        first_statement = False
    if not stats:
        return Nodes.PassStatNode(pos)
    elif len(stats) == 1:
        return stats[0]
    else:
        return Nodes.StatListNode(pos, stats = stats)


@cython.cfunc
def p_suite(s: PyrexScanner, ctx=Ctx()):
    return p_suite_with_docstring(s, ctx, with_doc_only=False)[1]


@cython.cfunc
def p_suite_with_docstring(s: PyrexScanner, ctx, with_doc_only: cython.bint = False) -> tuple:
    s.expect(':')
    doc = None
    if s.sy == 'NEWLINE':
        s.next()
        s.expect_indent()
        if with_doc_only:
            doc = p_doc_string(s)
        body = p_statement_list(s, ctx)
        s.expect_dedent()
    else:
        if ctx.api:
            s.error("'api' not allowed with this statement", fatal=False)
        if ctx.level in ('module', 'class', 'function', 'other'):
            body = p_simple_statement_list(s, ctx)
        else:
            body = p_pass_statement(s)
            s.expect_newline("Syntax error in declarations", ignore_semicolon=True)
    if not with_doc_only:
        doc, body = _extract_docstring(body)
    return doc, body


@cython.cfunc
def p_positional_and_keyword_args(s: PyrexScanner, end_sy_set, templates = None):
    """
    Parses positional and keyword arguments. end_sy_set
    should contain any s.sy that terminate the argument list.
    Argument expansion (* and **) are not allowed.

    Returns: (positional_args, keyword_args)
    """
    positional_args = []
    keyword_args = []
    pos_idx = 0

    while s.sy not in end_sy_set:
        if s.sy == '*' or s.sy == '**':
            s.error('Argument expansion not allowed here.', fatal=False)

        parsed_type = False
        if s.sy == 'IDENT' and s.peek()[0] == '=':
            ident = s.systring
            s.next()  # s.sy is '='
            s.next()
            if looking_at_expr(s):
                arg = p_test(s)
            else:
                base_type = p_c_base_type(s, templates = templates)
                declarator = p_c_declarator(s, empty=True)
                arg = Nodes.CComplexBaseTypeNode(base_type.pos,
                    base_type = base_type, declarator = declarator)
                parsed_type = True
            keyword_node = ExprNodes.IdentifierStringNode(arg.pos, value=ident)
            keyword_args.append((keyword_node, arg))
            was_keyword = True

        else:
            if looking_at_expr(s):
                arg = p_test(s)
            else:
                base_type = p_c_base_type(s, templates = templates)
                declarator = p_c_declarator(s, empty=True)
                arg = Nodes.CComplexBaseTypeNode(base_type.pos,
                    base_type = base_type, declarator = declarator)
                parsed_type = True
            positional_args.append(arg)
            pos_idx += 1
            if len(keyword_args) > 0:
                s.error("Non-keyword arg following keyword arg",
                        pos=arg.pos)

        if s.sy != ',':
            if s.sy not in end_sy_set:
                if parsed_type:
                    s.error("Unmatched %s" % " or ".join(end_sy_set))
            break
        s.next()
    return positional_args, keyword_args


@cython.ccall
def p_c_base_type(s: PyrexScanner, nonempty: cython.bint = False, templates=None):
    if s.sy == '(':
        return p_c_complex_base_type(s, templates = templates)
    else:
        return p_c_simple_base_type(s, nonempty=nonempty, templates=templates)


@cython.cfunc
def p_calling_convention(s: PyrexScanner):
    if s.sy == 'IDENT' and s.systring in calling_convention_words:
        result = s.systring
        s.next()
        return result
    else:
        return EncodedString("")


calling_convention_words = cython.declare(frozenset, frozenset((
    "__stdcall", "__cdecl", "__fastcall")))


@cython.cfunc
def p_c_complex_base_type(s: PyrexScanner, templates = None):
    # s.sy == '('
    pos = s.position()
    s.next()
    base_type = p_c_base_type(s, templates=templates)
    declarator = p_c_declarator(s, empty=True)
    type_node = Nodes.CComplexBaseTypeNode(
        pos, base_type=base_type, declarator=declarator)
    if s.sy == ',':
        components = [type_node]
        while s.sy == ',':
            s.next()
            if s.sy == ')':
                break
            base_type = p_c_base_type(s, templates=templates)
            declarator = p_c_declarator(s, empty=True)
            components.append(Nodes.CComplexBaseTypeNode(
                pos, base_type=base_type, declarator=declarator))
        type_node = Nodes.CTupleBaseTypeNode(pos, components = components)

    s.expect(')')
    if s.sy == '[':
        if is_memoryviewslice_access(s):
            type_node = p_memoryviewslice_access(s, type_node)
        else:
            type_node = p_buffer_or_template(s, type_node, templates)
    return type_node


@cython.cfunc
def p_c_simple_base_type(s: PyrexScanner, nonempty: cython.bint, templates=None):
    is_basic = False
    signed = 1
    longness = 0
    complex = False
    module_path = []
    pos = s.position()

    # Handle const/volatile
    is_const = is_volatile = False
    while s.sy == 'IDENT':
        if s.systring == 'const':
            if is_const: error(pos, "Duplicate 'const'")
            is_const = True
        elif s.systring == 'volatile':
            if is_volatile: error(pos, "Duplicate 'volatile'")
            is_volatile = True
        else:
            break
        s.next()
    if is_const or is_volatile:
        base_type = p_c_base_type(s, nonempty=nonempty, templates=templates)
        if isinstance(base_type, Nodes.MemoryViewSliceTypeNode):
            # reverse order to avoid having to write "(const int)[:]"
            base_type.base_type_node = Nodes.CConstOrVolatileTypeNode(pos,
                base_type=base_type.base_type_node, is_const=is_const, is_volatile=is_volatile)
            return base_type
        return Nodes.CConstOrVolatileTypeNode(pos,
            base_type=base_type, is_const=is_const, is_volatile=is_volatile)

    if s.sy != 'IDENT':
        error(pos, "Expected an identifier, found '%s'" % s.sy)
    if looking_at_base_type(s):
        #print "p_c_simple_base_type: looking_at_base_type at", s.position()
        is_basic = True
        if s.sy == 'IDENT' and s.systring in special_basic_c_types:
            signed, longness = special_basic_c_types[s.systring]
            name = s.systring
            s.next()
        else:
            signed, longness = p_sign_and_longness(s)
            if s.sy == 'IDENT' and s.systring in basic_c_type_names:
                name = s.systring
                s.next()
            else:
                name = 'int'  # long [int], short [int], long [int] complex, etc.
        if s.sy == 'IDENT' and s.systring == 'complex':
            complex = True
            s.next()
    elif looking_at_dotted_name(s):
        #print "p_c_simple_base_type: looking_at_type_name at", s.position()
        name = s.systring
        s.next()
        while s.sy == '.':
            module_path.append(name)
            s.next()
            name = p_ident(s)
    else:
        name = s.systring
        name_pos = s.position()
        s.next()
        if nonempty and s.sy != 'IDENT':
            # Make sure this is not a declaration of a variable or function.
            if s.sy == '(':
                old_pos = s.position()
                s.next()
                if (s.sy == '*' or s.sy == '**' or s.sy == '&'
                        or (s.sy == 'IDENT' and s.systring in calling_convention_words)):
                    s.put_back('(', '(', old_pos)
                else:
                    s.put_back('(', '(', old_pos)
                    s.put_back('IDENT', name, name_pos)
                    name = None
            elif s.sy not in ('*', '**', '[', '&'):
                s.put_back('IDENT', name, name_pos)
                name = None

    type_node = Nodes.CSimpleBaseTypeNode(pos,
        name = name, module_path = module_path,
        is_basic_c_type = is_basic, signed = signed,
        complex = complex, longness = longness,
        templates = templates)

    #    declarations here.
    if s.sy == '[':
        if is_memoryviewslice_access(s):
            type_node = p_memoryviewslice_access(s, type_node)
        else:
            type_node = p_buffer_or_template(s, type_node, templates)

    if s.sy == '.':
        s.next()
        name = p_ident(s)
        type_node = Nodes.CNestedBaseTypeNode(pos, base_type = type_node, name = name)

    return type_node


@cython.cfunc
def p_buffer_or_template(s: PyrexScanner, base_type_node, templates):
    # s.sy == '['
    pos = s.position()
    s.next()
    # Note that buffer_positional_options_count=1, so the only positional argument is dtype.
    # For templated types, all parameters are types.
    positional_args, keyword_args = (
        p_positional_and_keyword_args(s, (']',), templates)
    )
    s.expect(']')

    if s.sy == '[':
        base_type_node = p_buffer_or_template(s, base_type_node, templates)

    keyword_dict = ExprNodes.DictNode(pos,
        key_value_pairs = [
            ExprNodes.DictItemNode(pos=key.pos, key=key, value=value)
            for key, value in keyword_args
        ])
    result = Nodes.TemplatedTypeNode(pos,
        positional_args = positional_args,
        keyword_args = keyword_dict,
        base_type_node = base_type_node)
    return result


@cython.cfunc
def is_memoryviewslice_access(s: PyrexScanner) -> cython.bint:
    # s.sy == '['
    # a memoryview slice declaration is distinguishable from a buffer access
    # declaration by the first entry in the bracketed list.  The buffer will
    # not have an unnested colon in the first entry; the memoryview slice will.
    saved = [(s.sy, s.systring, s.position())]
    s.next()
    retval = False
    if s.systring == ':':
        retval = True
    elif s.sy == 'INT':
        saved.append((s.sy, s.systring, s.position()))
        s.next()
        if s.sy == ':':
            retval = True

    for sv in saved[::-1]:
        s.put_back(*sv)

    return retval


@cython.cfunc
def p_memoryviewslice_access(s: PyrexScanner, base_type_node):
    # s.sy == '['
    pos = s.position()
    s.next()
    subscripts, _ = p_subscript_list(s)
    # make sure each entry in subscripts is a slice
    for subscript in subscripts:
        if len(subscript) < 2:
            s.error("An axis specification in memoryview declaration does not have a ':'.")
    s.expect(']')
    indexes = make_slice_nodes(pos, subscripts)
    result = Nodes.MemoryViewSliceTypeNode(pos,
            base_type_node = base_type_node,
            axes = indexes)
    return result


@cython.cfunc
def looking_at_name(s: PyrexScanner) -> cython.bint:
    return s.sy == 'IDENT' and s.systring not in calling_convention_words


@cython.cfunc
def looking_at_expr(s: PyrexScanner) -> cython.bint:
    if s.systring in base_type_start_words:
        return False
    elif s.sy == 'IDENT':
        is_type = False
        name = s.systring
        name_pos = s.position()
        dotted_path = []
        s.next()

        while s.sy == '.':
            s.next()
            dotted_path.append((s.systring, s.position()))
            s.expect('IDENT')

        saved = s.sy, s.systring, s.position()
        if s.sy == 'IDENT':
            is_type = True
        elif s.sy == '*' or s.sy == '**':
            s.next()
            is_type = s.sy in (')', ']')
            s.put_back(*saved)
        elif s.sy == '(':
            s.next()
            is_type = s.sy == '*'
            s.put_back(*saved)
        elif s.sy == '[':
            s.next()
            is_type = s.sy == ']' or not looking_at_expr(s)  # could be a nested template type
            s.put_back(*saved)

        dotted_path.reverse()
        for p in dotted_path:
            s.put_back('IDENT', *p)
            s.put_back('.', '.', p[1])  # gets the position slightly wrong

        s.put_back('IDENT', name, name_pos)
        return not is_type and saved[0]
    else:
        return True


@cython.cfunc
def looking_at_base_type(s: PyrexScanner) -> cython.bint:
    #print "looking_at_base_type?", s.sy, s.systring, s.position()
    return s.sy == 'IDENT' and s.systring in base_type_start_words


@cython.cfunc
def looking_at_dotted_name(s: PyrexScanner) -> cython.bint:
    if s.sy == 'IDENT':
        name = s.systring
        name_pos = s.position()
        s.next()
        result: cython.bint = s.sy == '.'
        s.put_back('IDENT', name, name_pos)
        return result
    else:
        return False


basic_c_type_names = cython.declare(frozenset, frozenset((
    "void", "char", "int", "float", "double", "bint")))

special_basic_c_types = cython.declare(dict, {
    # name : (signed, longness)
    "Py_UNICODE" : (0, 0),
    "Py_UCS4"    : (0, 0),
    "Py_hash_t"  : (2, 0),
    "Py_ssize_t" : (2, 0),
    "ssize_t"    : (2, 0),
    "size_t"     : (0, 0),
    "ptrdiff_t"  : (2, 0),
    "Py_tss_t"   : (1, 0),
})

sign_and_longness_words = cython.declare(frozenset, frozenset((
    "short", "long", "signed", "unsigned")))

base_type_start_words = cython.declare(
    frozenset,
    basic_c_type_names
    | sign_and_longness_words
    | frozenset(special_basic_c_types))

struct_enum_union = cython.declare(frozenset, frozenset((
    "struct", "union", "enum", "packed")))


@cython.cfunc
def p_sign_and_longness(s: PyrexScanner) -> tuple:
    signed = 1
    longness = 0
    while s.sy == 'IDENT' and s.systring in sign_and_longness_words:
        if s.systring == 'unsigned':
            signed = 0
        elif s.systring == 'signed':
            signed = 2
        elif s.systring == 'short':
            longness = -1
        elif s.systring == 'long':
            longness += 1
        s.next()
    return signed, longness


@cython.cfunc
def p_opt_cname(s: PyrexScanner):
    literal = p_opt_string_literal(s, 'u')
    if literal is not None:
        cname = EncodedString(literal)
        cname.encoding = s.source_encoding
    else:
        cname = None
    return cname


@cython.ccall
def p_c_declarator(s: PyrexScanner, ctx = Ctx(),
                   empty: cython.bint = False, is_type: cython.bint = False, cmethod_flag: cython.bint = False,
                   assignable: cython.bint = False, nonempty: cython.bint = False,
                   calling_convention_allowed: cython.bint = False):
    # If empty is true, the declarator must be empty. If nonempty is true,
    # the declarator must be nonempty. Otherwise we don't care.
    # If cmethod_flag is true, then if this declarator declares
    # a function, it's a C method of an extension type.
    pos = s.position()
    if s.sy == '(':
        s.next()
        if s.sy == ')' or looking_at_name(s):
            base = Nodes.CNameDeclaratorNode(pos, name=s.context.intern_ustring(""), cname=None)
            result = p_c_func_declarator(s, pos, ctx, base, cmethod_flag)
        else:
            result = p_c_declarator(s, ctx, empty = empty, is_type = is_type,
                                    cmethod_flag = cmethod_flag,
                                    nonempty = nonempty,
                                    calling_convention_allowed = True)
            s.expect(')')
    else:
        result = p_c_simple_declarator(s, ctx, empty, is_type, cmethod_flag,
                                       assignable, nonempty)
    if not calling_convention_allowed and result.calling_convention and s.sy != '(':
        error(s.position(), "%s on something that is not a function"
            % result.calling_convention)
    while s.sy in ('[', '('):
        pos = s.position()
        if s.sy == '[':
            result = p_c_array_declarator(s, result)
        else:  # sy == '('
            s.next()
            result = p_c_func_declarator(s, pos, ctx, result, cmethod_flag)
        cmethod_flag = 0
    return result


@cython.cfunc
def p_c_array_declarator(s: PyrexScanner, base):
    pos = s.position()
    s.next()  # '['
    if s.sy != ']':
        dim = p_testlist(s)
    else:
        dim = None
    s.expect(']')
    return Nodes.CArrayDeclaratorNode(pos, base = base, dimension = dim)


@cython.cfunc
def p_c_func_declarator(s: PyrexScanner, pos, ctx, base, cmethod_flag: cython.bint):
    # Opening paren has already been skipped
    args = p_c_arg_list(s, ctx, cmethod_flag = cmethod_flag,
                        nonempty_declarators = 0)
    ellipsis = p_optional_ellipsis(s)
    s.expect(')')
    nogil = p_nogil(s)
    exc_val, exc_check, exc_clause = p_exception_value_clause(s, ctx.visibility == 'extern')
    if nogil and exc_clause:
        warning(
            s.position(),
            "The keyword 'nogil' should appear at the end of the "
            "function signature line. Placing it before 'except' "
            "or 'noexcept' will be disallowed in a future version "
            "of Cython.",
            level=2
        )
    nogil = nogil or p_nogil(s)
    with_gil = p_with_gil(s)
    return Nodes.CFuncDeclaratorNode(pos,
        base = base, args = args, has_varargs = ellipsis,
        exception_value = exc_val, exception_check = exc_check,
        nogil = nogil or ctx.nogil or with_gil, with_gil = with_gil, has_explicit_exc_clause=exc_clause)


supported_overloaded_operators = cython.declare(frozenset, frozenset((
    '+', '-', '*', '/', '%',
    '++', '--', '~', '|', '&', '^', '<<', '>>', ',',
    '==', '!=', '>=', '>', '<=', '<',
    '[]', '()', '!', '=',
    'bool',
)))


@cython.cfunc
def p_c_simple_declarator(s: PyrexScanner, ctx,
                          empty: cython.bint, is_type: cython.bint, cmethod_flag: cython.bint,
                          assignable: cython.bint, nonempty: cython.bint):
    pos = s.position()
    calling_convention = p_calling_convention(s)
    if s.sy in ('*', '**'):
        # scanner returns '**' as a single token
        is_ptrptr = s.sy == '**'
        s.next()

        const_pos = s.position()
        is_const = s.systring == 'const' and s.sy == 'IDENT'
        if is_const:
            s.next()

        base = p_c_declarator(s, ctx, empty=empty, is_type=is_type,
                              cmethod_flag=cmethod_flag,
                              assignable=assignable, nonempty=nonempty)
        if is_const:
            base = Nodes.CConstDeclaratorNode(const_pos, base=base)
        if is_ptrptr:
            base = Nodes.CPtrDeclaratorNode(pos, base=base)
        result = Nodes.CPtrDeclaratorNode(pos, base=base)
    elif s.sy == '&' or (s.sy == '&&' and s.context.cpp):
        node_class = Nodes.CppRvalueReferenceDeclaratorNode if s.sy == '&&' else Nodes.CReferenceDeclaratorNode
        s.next()
        base = p_c_declarator(s, ctx, empty=empty, is_type=is_type,
                              cmethod_flag=cmethod_flag,
                              assignable=assignable, nonempty=nonempty)
        result = node_class(pos, base=base)
    else:
        rhs = None
        if s.sy == 'IDENT':
            name = s.systring
            if empty:
                error(s.position(), "Declarator should be empty")
            s.next()
            cname = p_opt_cname(s)
            if name != 'operator' and s.sy == '=' and assignable:
                s.next()
                rhs = p_test(s)
        else:
            if nonempty:
                error(s.position(), "Empty declarator")
            name = ""
            cname = None
        if cname is None and ctx.namespace is not None and nonempty:
            cname = ctx.namespace + "::" + name
        if name == 'operator' and ctx.visibility == 'extern' and nonempty:
            op = s.sy
            if [1 for c in op if c in '+-*/<=>!%&|([^~,']:
                s.next()
                # Handle diphthong operators.
                if op == '(':
                    s.expect(')')
                    op = '()'
                elif op == '[':
                    s.expect(']')
                    op = '[]'
                elif op in ('-', '+', '|', '&') and s.sy == op:
                    op *= 2       # ++, --, ...
                    s.next()
                elif s.sy == '=':
                    op += s.sy    # +=, -=, ...
                    s.next()
                if op not in supported_overloaded_operators:
                    s.error("Overloading operator '%s' not yet supported." % op,
                            fatal=False)
                name += op
            elif op == 'IDENT':
                op = s.systring
                if op not in supported_overloaded_operators:
                    s.error("Overloading operator '%s' not yet supported." % op,
                            fatal=False)
                name = name + ' ' + op
                s.next()
        result = Nodes.CNameDeclaratorNode(pos,
            name = name, cname = cname, default = rhs)
    result.calling_convention = calling_convention
    return result


@cython.cfunc
def p_nogil(s: PyrexScanner) -> cython.bint:
    if s.sy == 'IDENT' and s.systring == 'nogil':
        s.next()
        return True
    else:
        return False


@cython.cfunc
def p_with_gil(s: PyrexScanner) -> cython.bint:
    if s.sy == 'with':
        s.next()
        s.expect_keyword('gil')
        return True
    else:
        return False


@cython.cfunc
def p_exception_value_clause(s: PyrexScanner, is_extern: cython.bint) -> tuple:
    """
    Parse exception value clause.

    Maps clauses to exc_check / exc_value / exc_clause as follows:
     ______________________________________________________________________
    |                             |             |             |            |
    | Clause                      | exc_check   | exc_value   | exc_clause |
    | ___________________________ | ___________ | ___________ | __________ |
    |                             |             |             |            |
    | <nothing> (default func.)   | True        | None        | False      |
    | <nothing> (cdef extern)     | False       | None        | False      |
    | noexcept                    | False       | None        | True       |
    | except <val>                | False       | <val>       | True       |
    | except? <val>               | True        | <val>       | True       |
    | except *                    | True        | None        | True       |
    | except +                    | '+'         | None        | True       |
    | except +*                   | '+'         | '*'         | True       |
    | except +<PyErr>             | '+'         | <PyErr>     | True       |
    | ___________________________ | ___________ | ___________ | __________ |

    Note that the only reason we need `exc_clause` is to raise a
    warning when `'except'` or `'noexcept'` is placed after the
    `'nogil'` keyword.
    """
    exc_clause: cython.bint = False
    exc_val = None
    exc_check = False if is_extern else True

    if s.sy == 'IDENT' and s.systring == 'noexcept':
        exc_clause = True
        s.next()
        exc_check = False
    elif s.sy == 'except':
        exc_clause = True
        s.next()
        if s.sy == '*':
            exc_check = True
            s.next()
        elif s.sy == '+':
            exc_check = '+'
            plus_char_pos = s.position()[2]
            s.next()
            if s.sy == 'IDENT':
                name = s.systring
                if name == 'nogil':
                    if s.position()[2] == plus_char_pos + 1:
                        error(s.position(),
                              "'except +nogil' defines an exception handling function. Use 'except + nogil' for the 'nogil' modifier.")
                    # 'except + nogil' is parsed outside
                else:
                    exc_val = p_name(s, name)
                    s.next()
            elif s.sy == '*':
                exc_val = ExprNodes.CharNode(s.position(), value='*')
                s.next()
        else:
            if s.sy == '?':
                exc_check = True
                s.next()
            else:
                exc_check = False
            # exc_val can be non-None even if exc_check is False, c.f. "except -1"
            exc_val = p_test(s)

    return exc_val, exc_check, exc_clause


c_arg_list_terminators = cython.declare(frozenset, frozenset((
    '*', '**', '...', ')', ':', '/')))


@cython.ccall
def p_c_arg_list(s: PyrexScanner, ctx = Ctx(),
                 in_pyfunc: cython.bint = False, cmethod_flag: cython.bint = False,
                 nonempty_declarators: cython.bint = False, kw_only: cython.bint = False,
                 annotated: cython.bint = True) -> list:
    #  Comma-separated list of C argument declarations, possibly empty.
    #  May have a trailing comma.
    args = []
    is_self_arg = cmethod_flag
    while s.sy not in c_arg_list_terminators:
        args.append(p_c_arg_decl(s, ctx, in_pyfunc, is_self_arg,
            nonempty = nonempty_declarators, kw_only = kw_only,
            annotated = annotated))
        if s.sy != ',':
            break
        s.next()
        is_self_arg = 0
    return args


@cython.cfunc
def p_optional_ellipsis(s: PyrexScanner) -> cython.bint:
    if s.sy == '...':
        expect_ellipsis(s)
        return True
    else:
        return False


@cython.cfunc
def p_c_arg_decl(s: PyrexScanner, ctx, in_pyfunc: cython.bint, cmethod_flag: cython.bint = False,
                 nonempty: cython.bint = False,
                 kw_only: cython.bint = False, annotated: cython.bint = True):
    pos = s.position()
    not_none = or_none = False
    default = None
    annotation = None
    if s.in_python_file:
        # empty type declaration
        base_type = Nodes.CSimpleBaseTypeNode(pos,
            name = None, module_path = [],
            is_basic_c_type = False, signed = 0,
            complex = False, longness = 0,
            is_self_arg = cmethod_flag, templates = None)
    else:
        base_type = p_c_base_type(s, nonempty=nonempty)
    declarator = p_c_declarator(s, ctx, nonempty = nonempty)
    if s.sy in ('not', 'or') and not s.in_python_file:
        kind = s.sy
        s.next()
        if s.sy == 'IDENT' and s.systring == 'None':
            s.next()
        else:
            s.error("Expected 'None'")
        if not in_pyfunc:
            error(pos, "'%s None' only allowed in Python functions" % kind)
        or_none = kind == 'or'
        not_none = kind == 'not'
    if annotated and s.sy == ':':
        s.next()
        annotation = p_annotation(s)
    if s.sy == '=':
        s.next()
        if 'pxd' in ctx.level:
            if s.sy in ['*', '?']:
                # TODO(github/1736): Make this an error for inline declarations.
                default = ExprNodes.NoneNode(pos)
                s.next()
            elif 'inline' in ctx.modifiers:
                default = p_test(s)
            else:
                error(pos, "default values cannot be specified in pxd files, use ? or *")
        else:
            default = p_test(s)
    return Nodes.CArgDeclNode(pos,
        base_type = base_type,
        declarator = declarator,
        not_none = not_none,
        or_none = or_none,
        default = default,
        annotation = annotation,
        kw_only = kw_only)


@cython.cfunc
def p_annotation(s: PyrexScanner):
    """An annotation just has the "test" syntax, but also stores the string it came from

    Note that the string is *allowed* to be changed/processed (although isn't here)
    so may not exactly match the string generated by Python, and if it doesn't
    then it is not a bug.
    """
    pos = s.position()
    expr = p_test(s)
    return ExprNodes.AnnotationNode(pos, expr=expr)


@cython.cfunc
def p_api(s: PyrexScanner) -> cython.bint:
    if s.sy == 'IDENT' and s.systring == 'api':
        s.next()
        return True
    else:
        return False


@cython.cfunc
def p_cdef_statement(s: PyrexScanner, pos, ctx):
    ctx.visibility = p_visibility(s, ctx.visibility)
    ctx.api = ctx.api or p_api(s)
    if ctx.api:
        if ctx.visibility not in ('private', 'public'):
            error(pos, "Cannot combine 'api' with '%s'" % ctx.visibility)
    if (ctx.visibility == 'extern') and s.sy == 'from':
        return p_cdef_extern_block(s, pos, ctx)
    elif s.sy == 'import':
        s.next()
        return p_cdef_extern_block(s, pos, ctx)
    elif p_nogil(s):
        ctx.nogil = True
        if ctx.overridable:
            error(pos, "cdef blocks cannot be declared cpdef")
        return p_cdef_block(s, ctx)
    elif s.sy == ':':
        if ctx.overridable:
            error(pos, "cdef blocks cannot be declared cpdef")
        return p_cdef_block(s, ctx)
    elif s.sy == 'class':
        if ctx.level not in ('module', 'module_pxd'):
            error(pos, "Extension type definition not allowed here")
        if ctx.overridable:
            error(pos, "Extension types cannot be declared cpdef")
        return p_c_class_definition(s, pos, ctx)
    elif s.sy == 'IDENT' and s.systring == 'cppclass':
        return p_cpp_class_definition(s, pos, ctx)
    elif s.sy == 'IDENT' and s.systring in struct_enum_union:
        if ctx.level not in ('module', 'module_pxd'):
            error(pos, "C struct/union/enum definition not allowed here")
        if ctx.overridable:
            if s.systring != 'enum':
                error(pos, "C struct/union cannot be declared cpdef")
        return p_struct_enum(s, pos, ctx)
    elif s.sy == 'IDENT' and s.systring == 'fused':
        return p_fused_definition(s, pos, ctx)
    else:
        return p_c_func_or_var_declaration(s, pos, ctx)


@cython.cfunc
def p_cdef_block(s: PyrexScanner, ctx):
    return p_suite(s, ctx(cdef_flag = True))


@cython.cfunc
def p_cdef_extern_block(s: PyrexScanner, pos, ctx):
    if ctx.overridable:
        error(pos, "cdef extern blocks cannot be declared cpdef")
    include_file = None
    s.expect('from')
    if s.sy == '*':
        s.next()
    else:
        include_file = p_string_literal(s, 'u')[2]
    ctx = ctx(cdef_flag = True, visibility = 'extern')
    if s.systring == "namespace":
        s.next()
        ctx.namespace = p_string_literal(s, 'u')[2]
    if p_nogil(s):
        ctx.nogil = True

    # Use "docstring" as verbatim string to include
    verbatim_include, body = p_suite_with_docstring(s, ctx, True)

    return Nodes.CDefExternNode(pos,
        include_file = include_file,
        verbatim_include = verbatim_include,
        body = body,
        namespace = ctx.namespace)


@cython.cfunc
def p_c_enum_definition(s: PyrexScanner, pos, ctx):
    # s.sy == ident 'enum'
    s.next()

    scoped = False
    if s.context.cpp and (s.sy == 'class' or (s.sy == 'IDENT' and s.systring == 'struct')):
        scoped = True
        s.next()

    if s.sy == 'IDENT':
        name = s.systring
        s.next()
        cname = p_opt_cname(s)
        if cname is None and ctx.namespace is not None:
            cname = ctx.namespace + "::" + name
    else:
        name = cname = None
        if scoped:
            s.error("Unnamed scoped enum not allowed")

    if scoped and s.sy == '(':
        s.next()
        underlying_type = p_c_base_type(s)
        s.expect(')')
    else:
        underlying_type = Nodes.CSimpleBaseTypeNode(
            pos,
            name="int",
            module_path = [],
            is_basic_c_type = True,
            signed = 1,
            complex = False,
            longness = 0
        )

    s.expect(':')
    items = []

    doc = None
    if s.sy != 'NEWLINE':
        p_c_enum_line(s, ctx, items)
    else:
        s.next()  # 'NEWLINE'
        s.expect_indent()
        doc = p_doc_string(s)

        while s.sy not in ('DEDENT', 'EOF'):
            p_c_enum_line(s, ctx, items)

        s.expect_dedent()

    if not items and ctx.visibility != "extern":
        error(pos, "Empty enum definition not allowed outside a 'cdef extern from' block")

    return Nodes.CEnumDefNode(
        pos, name=name, cname=cname,
        scoped=scoped, items=items,
        underlying_type=underlying_type,
        typedef_flag=ctx.typedef_flag, visibility=ctx.visibility,
        create_wrapper=ctx.overridable,
        api=ctx.api, in_pxd=ctx.level == 'module_pxd', doc=doc)


@cython.cfunc
def p_c_enum_line(s: PyrexScanner, ctx, items: list):
    if s.sy != 'pass':
        p_c_enum_item(s, ctx, items)
        while s.sy == ',':
            s.next()
            if s.sy in ('NEWLINE', 'EOF'):
                break
            p_c_enum_item(s, ctx, items)
    else:
        s.next()
    s.expect_newline("Syntax error in enum item list")


@cython.cfunc
def p_c_enum_item(s: PyrexScanner, ctx, items: list):
    pos = s.position()
    name = p_ident(s)
    cname = p_opt_cname(s)
    if cname is None and ctx.namespace is not None:
        cname = ctx.namespace + "::" + name
    value = None
    if s.sy == '=':
        s.next()
        value = p_test(s)
    items.append(Nodes.CEnumDefItemNode(pos,
        name = name, cname = cname, value = value))


@cython.cfunc
def p_c_struct_or_union_definition(s: PyrexScanner, pos, ctx):
    packed = False
    if s.systring == 'packed':
        packed = True
        s.next()
        if s.sy != 'IDENT' or s.systring != 'struct':
            s.expected('struct')
    # s.sy == ident 'struct' or 'union'
    kind = s.systring
    s.next()
    name = p_ident(s)
    cname = p_opt_cname(s)
    if cname is None and ctx.namespace is not None:
        cname = ctx.namespace + "::" + name
    attributes = None
    if s.sy == ':':
        s.next()
        attributes = []
        if s.sy == 'pass':
            s.next()
            s.expect_newline("Expected a newline", ignore_semicolon=True)
        else:
            s.expect('NEWLINE')
            s.expect_indent()
            body_ctx = Ctx(visibility=ctx.visibility)
            while s.sy != 'DEDENT':
                if s.sy != 'pass':
                    attributes.append(
                        p_c_func_or_var_declaration(s, s.position(), body_ctx))
                else:
                    s.next()
                    s.expect_newline("Expected a newline")
            s.expect_dedent()

        if not attributes and ctx.visibility != "extern":
            error(pos, "Empty struct or union definition not allowed outside a 'cdef extern from' block")
    else:
        s.expect_newline("Syntax error in struct or union definition")

    return Nodes.CStructOrUnionDefNode(pos,
        name = name, cname = cname, kind = kind, attributes = attributes,
        typedef_flag = ctx.typedef_flag, visibility = ctx.visibility,
        api = ctx.api, in_pxd = ctx.level == 'module_pxd', packed = packed)


@cython.cfunc
def p_fused_definition(s: PyrexScanner, pos, ctx):
    """
    c(type)def fused my_fused_type:
        ...
    """
    # s.systring == 'fused'

    if ctx.level not in ('module', 'module_pxd'):
        error(pos, "Fused type definition not allowed here")

    s.next()
    name = p_ident(s)

    s.expect(":")
    s.expect_newline()
    s.expect_indent()

    types = []
    while s.sy != 'DEDENT':
        if s.sy != 'pass':
            #types.append(p_c_declarator(s))
            types.append(p_c_base_type(s))  #, nonempty=1))
        else:
            s.next()

        s.expect_newline()

    s.expect_dedent()

    if not types:
        error(pos, "Need at least one type")

    return Nodes.FusedTypeNode(pos, name=name, types=types)


@cython.cfunc
def p_struct_enum(s: PyrexScanner, pos, ctx):
    if s.systring == 'enum':
        return p_c_enum_definition(s, pos, ctx)
    else:
        return p_c_struct_or_union_definition(s, pos, ctx)


@cython.cfunc
def p_visibility(s: PyrexScanner, prev_visibility):
    visibility = prev_visibility
    if s.sy == 'IDENT' and s.systring in ('extern', 'public', 'readonly'):
        visibility = s.systring
        if prev_visibility != 'private' and visibility != prev_visibility:
            s.error("Conflicting visibility options '%s' and '%s'"
                % (prev_visibility, visibility), fatal=False)
        s.next()
    return visibility


@cython.cfunc
def p_c_modifiers(s: PyrexScanner) -> list:
    if s.sy == 'IDENT' and s.systring in ('inline',):
        modifier = s.systring
        s.next()
        return [modifier] + p_c_modifiers(s)
    return []


@cython.cfunc
def p_c_func_or_var_declaration(s: PyrexScanner, pos, ctx):
    cmethod_flag: cython.bint = ctx.level in ('c_class', 'c_class_pxd')
    modifiers = p_c_modifiers(s)
    base_type = p_c_base_type(s, nonempty=True, templates = ctx.templates)
    declarator = p_c_declarator(s, ctx(modifiers=modifiers), cmethod_flag = cmethod_flag,
                                assignable=True, nonempty =True)
    declarator.overridable = ctx.overridable

    if s.sy == 'IDENT' and s.systring == 'const' and ctx.level == 'cpp_class':
        s.next()
        is_const_method = True
    else:
        is_const_method = False

    if s.sy == '->':
        # Special enough to give a better error message and keep going.
        s.error(
            "Return type annotation is not allowed in cdef/cpdef signatures. "
            "Please define it before the function name, as in C signatures.",
            fatal=False)
        s.next()
        p_test(s)  # Keep going, but ignore result.

    if s.sy == ':':
        if ctx.level not in ('module', 'c_class', 'module_pxd', 'c_class_pxd', 'cpp_class') and not ctx.templates:
            s.error("C function definition not allowed here")
        doc, suite = p_suite_with_docstring(s, Ctx(level='function'))
        result = Nodes.CFuncDefNode(pos,
            visibility = ctx.visibility,
            base_type = base_type,
            declarator = declarator,
            body = suite,
            doc = doc,
            modifiers = modifiers,
            api = ctx.api,
            overridable = ctx.overridable,
            is_const_method = is_const_method)
    else:
        #if api:
        #    s.error("'api' not allowed with variable declaration")
        if is_const_method:
            declarator.is_const_method = is_const_method
        declarators = [declarator]
        while s.sy == ',':
            s.next()
            if s.sy == 'NEWLINE':
                break
            declarator = p_c_declarator(s, ctx, cmethod_flag = cmethod_flag,
                                        assignable=True, nonempty=True)
            declarators.append(declarator)
        doc_line = s.start_line + 1
        s.expect_newline("Syntax error in C variable declaration", ignore_semicolon=True)
        if ctx.level in ('c_class', 'c_class_pxd') and s.start_line == doc_line:
            doc = p_doc_string(s)
        else:
            doc = None
        result = Nodes.CVarDefNode(pos,
            visibility = ctx.visibility,
            base_type = base_type,
            declarators = declarators,
            in_pxd = ctx.level in ('module_pxd', 'c_class_pxd'),
            doc = doc,
            api = ctx.api,
            modifiers = modifiers,
            overridable = ctx.overridable)
    return result


@cython.cfunc
def p_ctypedef_statement(s: PyrexScanner, ctx):
    # s.sy == 'ctypedef'
    pos = s.position()
    s.next()
    visibility = p_visibility(s, ctx.visibility)
    api = p_api(s)
    ctx = ctx(typedef_flag=True, visibility = visibility)
    if api:
        ctx.api = True
    if s.sy == 'class':
        return p_c_class_definition(s, pos, ctx)
    elif s.sy == 'IDENT' and s.systring in struct_enum_union:
        return p_struct_enum(s, pos, ctx)
    elif s.sy == 'IDENT' and s.systring == 'fused':
        return p_fused_definition(s, pos, ctx)
    else:
        base_type = p_c_base_type(s, nonempty=True)
        declarator = p_c_declarator(s, ctx, is_type=True, nonempty=True)
        s.expect_newline("Syntax error in ctypedef statement", ignore_semicolon=True)
        return Nodes.CTypeDefNode(
            pos, base_type = base_type,
            declarator = declarator,
            visibility = visibility, api = api,
            in_pxd = ctx.level == 'module_pxd')


@cython.cfunc
def p_decorators(s: PyrexScanner) -> list:
    decorators = []
    while s.sy == '@':
        pos = s.position()
        s.next()
        decorator = p_namedexpr_test(s)
        decorators.append(Nodes.DecoratorNode(pos, decorator=decorator))
        s.expect_newline("Expected a newline after decorator")
    return decorators


@cython.cfunc
def _reject_cdef_modifier_in_py(s: PyrexScanner, name):
    """Step over incorrectly placed cdef modifiers (@see _CDEF_MODIFIERS) to provide a good error message for them.
    """
    if s.sy == 'IDENT' and name in _CDEF_MODIFIERS:
        # Special enough to provide a good error message.
        s.error("Cannot use cdef modifier '%s' in Python function signature. Use a decorator instead." % name, fatal=False)
        return p_ident(s)  # Keep going, in case there are other errors.
    return name


@cython.cfunc
def p_def_statement(s: PyrexScanner, decorators: list = None, is_async_def: cython.bint = False):
    # s.sy == 'def'
    pos = decorators[0].pos if decorators else s.position()
    # PEP 492 switches the async/await keywords on in "async def" functions
    if is_async_def:
        s.enter_async()
    s.next()
    name = _reject_cdef_modifier_in_py(s, p_ident(s))
    s.expect(
        '(',
        "Expected '(', found '%s'. Did you use cdef syntax in a Python declaration? "
        "Use decorators and Python type annotations instead." % (
            s.systring if s.sy == 'IDENT' else s.sy))
    args, star_arg, starstar_arg = p_varargslist(s, terminator=')')
    s.expect(')')
    _reject_cdef_modifier_in_py(s, s.systring)
    return_type_annotation = None
    if s.sy == '->':
        s.next()
        return_type_annotation = p_annotation(s)
        _reject_cdef_modifier_in_py(s, s.systring)

    doc, body = p_suite_with_docstring(s, Ctx(level='function'))
    if is_async_def:
        s.exit_async()

    return Nodes.DefNode(
        pos, name=name, args=args, star_arg=star_arg, starstar_arg=starstar_arg,
        doc=doc, body=body, decorators=decorators, is_async_def=is_async_def,
        return_type_annotation=return_type_annotation)


@cython.cfunc
def p_varargslist(s: PyrexScanner, terminator: cython.Py_UCS4 = ')', annotated: cython.bint = True) -> tuple:
    args = p_c_arg_list(s, in_pyfunc=True, nonempty_declarators=True,
                        annotated = annotated)
    star_arg = None
    starstar_arg = None
    if s.sy == '/':
        if len(args) == 0:
            s.error("Got zero positional-only arguments despite presence of "
                    "positional-only specifier '/'")
        s.next()
        # Mark all args to the left as pos only
        for arg in args:
            arg.pos_only = 1
        if s.sy == ',':
            s.next()
            args.extend(p_c_arg_list(
                s, in_pyfunc=True, nonempty_declarators=True, annotated = annotated))
        elif s.sy != terminator:
            s.error("Syntax error in Python function argument list")
    if s.sy == '*':
        s.next()
        if s.sy == 'IDENT':
            star_arg = p_py_arg_decl(s, annotated=annotated)
        if s.sy == ',':
            s.next()
            args.extend(p_c_arg_list(
                s, in_pyfunc =True, nonempty_declarators=True, kw_only=True, annotated = annotated))
        elif s.sy != terminator:
            s.error("Syntax error in Python function argument list")
    if s.sy == '**':
        s.next()
        starstar_arg = p_py_arg_decl(s, annotated=annotated)
    if s.sy == ',':
        s.next()
    return (args, star_arg, starstar_arg)


@cython.cfunc
def p_py_arg_decl(s: PyrexScanner, annotated: cython.bint = True):
    pos = s.position()
    name = p_ident(s)
    annotation = None
    if annotated and s.sy == ':':
        s.next()
        annotation = p_annotation(s)
    return Nodes.PyArgDeclNode(pos, name = name, annotation = annotation)


@cython.cfunc
def p_class_statement(s: PyrexScanner, decorators):
    # s.sy == 'class'
    pos = s.position()
    s.next()
    class_name = EncodedString(p_ident(s))
    class_name.encoding = s.source_encoding  # FIXME: why is this needed?
    arg_tuple = None
    keyword_dict = None
    if s.sy == '(':
        positional_args, keyword_args = p_call_parse_args(s, allow_genexp=False)
        arg_tuple, keyword_dict = p_call_build_packed_args(pos, positional_args, keyword_args)
    if arg_tuple is None:
        # XXX: empty arg_tuple
        arg_tuple = ExprNodes.TupleNode(pos, args=[])
    doc, body = p_suite_with_docstring(s, Ctx(level='class'))
    return Nodes.PyClassDefNode(
        pos, name=class_name,
        bases=arg_tuple,
        keyword_args=keyword_dict,
        doc=doc, body=body, decorators=decorators,
        force_py3_semantics=s.context.language_level >= 3)


@cython.cfunc
def p_c_class_definition(s: PyrexScanner, pos,  ctx):
    # s.sy == 'class'
    s.next()
    module_path = []
    class_name = p_ident(s)
    while s.sy == '.':
        s.next()
        module_path.append(class_name)
        class_name = p_ident(s)
    if module_path and ctx.visibility != 'extern':
        error(pos, "Qualified class name only allowed for 'extern' C class")
    if module_path and s.sy == 'IDENT' and s.systring == 'as':
        s.next()
        as_name = p_ident(s)
    else:
        as_name = class_name
    objstruct_name = None
    typeobj_name = None
    bases = None
    check_size = None
    if s.sy == '(':
        positional_args, keyword_args = p_call_parse_args(s, allow_genexp=False)
        if keyword_args:
            s.error("C classes cannot take keyword bases.")
        bases, _ = p_call_build_packed_args(pos, positional_args, keyword_args)
    if bases is None:
        bases = ExprNodes.TupleNode(pos, args=[])

    if s.sy == '[':
        if ctx.visibility not in ('public', 'extern') and not ctx.api:
            error(s.position(), "Name options only allowed for 'public', 'api', or 'extern' C class")
        objstruct_name, typeobj_name, check_size = p_c_class_options(s)
    if s.sy == ':':
        if ctx.level == 'module_pxd':
            body_level = 'c_class_pxd'
        else:
            body_level = 'c_class'
        doc, body = p_suite_with_docstring(s, Ctx(level=body_level))
    else:
        s.expect_newline("Syntax error in C class definition")
        doc = None
        body = None
    if ctx.visibility == 'extern':
        if not module_path:
            error(pos, "Module name required for 'extern' C class")
        if typeobj_name:
            error(pos, "Type object name specification not allowed for 'extern' C class")
    elif ctx.visibility == 'public':
        if not objstruct_name:
            error(pos, "Object struct name specification required for 'public' C class")
        if not typeobj_name:
            error(pos, "Type object name specification required for 'public' C class")
    elif ctx.visibility == 'private':
        if ctx.api:
            if not objstruct_name:
                error(pos, "Object struct name specification required for 'api' C class")
            if not typeobj_name:
                error(pos, "Type object name specification required for 'api' C class")
    else:
        error(pos, "Invalid class visibility '%s'" % ctx.visibility)
    return Nodes.CClassDefNode(pos,
        visibility = ctx.visibility,
        typedef_flag = ctx.typedef_flag,
        api = ctx.api,
        module_name = ".".join(module_path),
        class_name = class_name,
        as_name = as_name,
        bases = bases,
        objstruct_name = objstruct_name,
        typeobj_name = typeobj_name,
        check_size = check_size,
        in_pxd = ctx.level == 'module_pxd',
        doc = doc,
        body = body)


@cython.cfunc
def p_c_class_options(s: PyrexScanner) -> tuple:
    objstruct_name = None
    typeobj_name = None
    check_size = None
    s.expect('[')
    while 1:
        if s.sy != 'IDENT':
            break
        if s.systring == 'object':
            s.next()
            objstruct_name = p_ident(s)
        elif s.systring == 'type':
            s.next()
            typeobj_name = p_ident(s)
        elif s.systring == 'check_size':
            s.next()
            check_size = p_ident(s)
            if check_size not in ('ignore', 'warn', 'error'):
                s.error("Expected one of ignore, warn or error, found %r" % check_size)
        if s.sy != ',':
            break
        s.next()
    s.expect(']', "Expected 'object', 'type' or 'check_size'")
    return objstruct_name, typeobj_name, check_size


@cython.cfunc
def p_property_decl(s: PyrexScanner):
    pos = s.position()
    s.next()  # 'property'
    name = p_ident(s)
    doc, body = p_suite_with_docstring(
        s, Ctx(level='property'), with_doc_only=True)
    return Nodes.PropertyNode(pos, name=name, doc=doc, body=body)


@cython.cfunc
def p_ignorable_statement(s: PyrexScanner):
    """
    Parses any kind of ignorable statement that is allowed in .pxd files.
    """
    if s.sy == 'BEGIN_STRING':
        pos = s.position()
        string_node = p_atom(s)
        s.expect_newline("Syntax error in string", ignore_semicolon=True)
        return Nodes.ExprStatNode(pos, expr=string_node)
    return None


@cython.cfunc
def p_doc_string(s: PyrexScanner):
    if s.sy == 'BEGIN_STRING':
        pos = s.position()
        kind, bytes_result, unicode_result = p_cat_string_literal(s)
        s.expect_newline("Syntax error in doc string", ignore_semicolon=True)
        if kind in ('u', ''):
            return unicode_result
        warning(pos, "Python 3 requires docstrings to be unicode strings")
        return bytes_result
    else:
        return None


@cython.cfunc
def _extract_docstring(node) -> tuple:
    """
    Extract a docstring from a statement or from the first statement
    in a list.  Remove the statement if found.  Return a tuple
    (plain-docstring or None, node).
    """
    doc_node = None
    if node is None:
        pass
    elif isinstance(node, Nodes.ExprStatNode):
        if node.expr.is_string_literal:
            doc_node = node.expr
            node = Nodes.StatListNode(node.pos, stats=[])
    elif isinstance(node, Nodes.StatListNode) and node.stats:
        stats = node.stats
        if isinstance(stats[0], Nodes.ExprStatNode):
            if stats[0].expr.is_string_literal:
                doc_node = stats[0].expr
                del stats[0]

    if doc_node is None:
        doc = None
    elif isinstance(doc_node, ExprNodes.BytesNode):
        warning(node.pos,
                "Python 3 requires docstrings to be unicode strings")
        doc = doc_node.value
    else:
        doc = doc_node.value
    return doc, node


@cython.ccall
def p_code(s: PyrexScanner, level=None, ctx=Ctx):
    body = p_statement_list(s, ctx(level = level), first_statement=True)
    if s.sy != 'EOF':
        s.error("Syntax error in statement [%s,%s]" % (
            repr(s.sy), repr(s.systring)))
    return body


_match_compiler_directive_comment = cython.declare(object, re.compile(
    r"^#\s*cython\s*:\s*((\w|[.])+\s*=.*)$").match)


def _parse_directive_assignments(
    spec: str,
    *,
    relaxed_bool: bool = False,
    ignore_unknown: bool = False,
    current_settings: Optional[dict] = None,
) -> dict:
    directives = Directives()
    result: dict = dict(current_settings or {})
    def _coerce_value(name: str, raw_value: str) -> Any:
        type_info = Directives.directive_types.get(name)
        if type_info is bool:
            text = raw_value if not relaxed_bool else raw_value.lower()
            truthy = {"true", "yes", "1"} if relaxed_bool else {"True"}
            falsy = {"false", "no", "0"} if relaxed_bool else {"False"}
            if text in truthy:
                return True
            if text in falsy:
                return False
            raise ValueError(
                f"{name} directive must be set to True or False, got '{raw_value}'"
            )
        if type_info is int:
            try:
                return int(raw_value)
            except ValueError:
                raise ValueError(
                    f"{name} directive must be set to an integer, got '{raw_value}'"
                ) from None
        if type_info is str:
            return raw_value
        if callable(type_info):
            return type_info(name, raw_value)
        return raw_value
    for item in spec.split(","):
        item = item.strip()
        if not item:
            continue
        if "=" not in item:
            raise ValueError(f'Expected "=" in option "{item}"')
        name, raw_value = [s.strip() for s in item.split("=", 1)]
        if name.endswith(".all"):
            prefix = name[:-3]
            found_any = False
            for directive in directives:
                if directive.startswith(prefix):
                    found_any = True
                    result[directive] = _coerce_value(directive, raw_value)
            if not found_any and not ignore_unknown:
                raise ValueError(f'Unknown option: "{name}"')
            continue

        if name not in directives:
            if not ignore_unknown:
                raise ValueError(f'Unknown option: "{name}"')
            continue

        dtype = Directives.directive_types.get(name)
        if dtype is list:
            if name in result and isinstance(result[name], list):
                result[name].append(raw_value)
            else:
                result[name] = [raw_value]
        else:
            result[name] = _coerce_value(name, raw_value)
    return result


@cython.cfunc
def p_compiler_directive_comments(s: PyrexScanner) -> dict:
    result = {}
    while s.sy == 'commentline':
        pos = s.position()
        m = _match_compiler_directive_comment(s.systring)
        if m:
            directives_string = m.group(1).strip()
            try:
                new_directives = _parse_directive_assignments(
                    directives_string, ignore_unknown=True
                )
            except ValueError as e:
                s.error(e.args[0], fatal=False)
                s.next()
                continue

            for name in new_directives:
                if name not in result:
                    pass
                elif Directives.GLOBAL_DIRECTIVES.directive_types.get(name) is list:
                    result[name] += new_directives[name]
                    new_directives[name] = result[name]
                elif new_directives[name] == result[name]:
                    warning(pos, "Duplicate directive found: %s" % (name,))
                else:
                    s.error("Conflicting settings found for top-level directive %s: %r and %r" % (
                        name, result[name], new_directives[name]), pos=pos)

            if 'language_level' in new_directives:
                # Make sure we apply the language level already to the first token that follows the comments.
                s.context.set_language_level(new_directives['language_level'])
            if 'legacy_implicit_noexcept' in new_directives:
                s.context.legacy_implicit_noexcept = new_directives['legacy_implicit_noexcept']


            result.update(new_directives)

        s.next()
    return result


@cython.ccall
def p_module(s: PyrexScanner, pxd, full_module_name, ctx=Ctx):
    pos = s.position()

    directive_comments = p_compiler_directive_comments(s)
    s.parse_comments = False

    if s.context.language_level is None:
        s.context.set_language_level('3')

    level = 'module_pxd' if pxd else 'module'
    doc = p_doc_string(s)
    body = p_statement_list(s, ctx(level=level), first_statement=True)
    if s.sy != 'EOF':
        s.error("Syntax error in statement [%s,%s]" % (
            repr(s.sy), repr(s.systring)))
    return ModuleNode(
        pos,
        doc = doc,
        body = body,
        full_module_name = full_module_name,
        directive_comments = directive_comments,
        directives = Directives.DIRECTIVE_DEFAULTS,
    )


@cython.cfunc
def p_template_definition(s: PyrexScanner) -> tuple:
    name = p_ident(s)
    if s.sy == '=':
        s.expect('=')
        s.expect('*')
        required = False
    else:
        required = True
    return name, required


@cython.cfunc
def p_cpp_class_definition(s: PyrexScanner, pos,  ctx):
    # s.sy == 'cppclass'
    s.next()
    class_name = p_ident(s)
    cname = p_opt_cname(s)
    if cname is None and ctx.namespace is not None:
        cname = ctx.namespace + "::" + class_name
    if s.sy == '.':
        error(pos, "Qualified class name not allowed C++ class")
    if s.sy == '[':
        s.next()
        templates = [p_template_definition(s)]
        while s.sy == ',':
            s.next()
            templates.append(p_template_definition(s))
        s.expect(']')
        template_names = [name for name, required in templates]
    else:
        templates = None
        template_names = None
    if s.sy == '(':
        s.next()
        base_classes = [p_c_base_type(s, templates = template_names)]
        while s.sy == ',':
            s.next()
            base_classes.append(p_c_base_type(s, templates = template_names))
        s.expect(')')
    else:
        base_classes = []
    if s.sy == '[':
        error(s.position(), "Name options not allowed for C++ class")
    nogil = p_nogil(s)
    if s.sy == ':':
        s.next()
        s.expect('NEWLINE')
        s.expect_indent()
        # Allow a cppclass to have docstrings. It will be discarded as comment.
        # The goal of this is consistency: we can make docstrings inside cppclass methods,
        # so why not on the cppclass itself ?
        p_doc_string(s)
        attributes = []
        body_ctx = Ctx(visibility = ctx.visibility, level='cpp_class', nogil=nogil or ctx.nogil)
        body_ctx.templates = template_names
        while s.sy != 'DEDENT':
            if s.sy != 'pass':
                attributes.append(p_cpp_class_attribute(s, body_ctx))
            else:
                s.next()
                s.expect_newline("Expected a newline")
        s.expect_dedent()
    else:
        attributes = None
        s.expect_newline("Syntax error in C++ class definition")
    return Nodes.CppClassNode(pos,
        name = class_name,
        cname = cname,
        base_classes = base_classes,
        visibility = ctx.visibility,
        in_pxd = ctx.level == 'module_pxd',
        attributes = attributes,
        templates = templates)


@cython.cfunc
def p_cpp_class_attribute(s: PyrexScanner, ctx):
    pos = s.position()
    decorators = None
    if s.sy == '@':
        decorators = p_decorators(s)
    if s.systring == 'cppclass':
        return p_cpp_class_definition(s, pos, ctx)
    elif s.systring == 'ctypedef':
        return p_ctypedef_statement(s, ctx)
    elif s.sy == 'IDENT' and s.systring in struct_enum_union:
        if s.systring != 'enum':
            return p_cpp_class_definition(s, pos, ctx)
        else:
            return p_struct_enum(s, pos, ctx)
    else:
        node = p_c_func_or_var_declaration(s, pos, ctx)
        if decorators is not None:
            tup = Nodes.CFuncDefNode, Nodes.CVarDefNode, Nodes.CClassDefNode
            if ctx.allow_struct_enum_decorator:
                tup += Nodes.CStructOrUnionDefNode, Nodes.CEnumDefNode
            if not isinstance(node, tup):
                s.error("Decorators can only be followed by functions or classes")
            node.decorators = decorators
        return node


@cython.cfunc
def p_match_statement(s: PyrexScanner, ctx):
    assert s.sy == "IDENT" and s.systring == "match"
    pos = s.position()
    with tentatively_scan(s) as errors:
        s.next()
        subject = p_namedexpr_test(s)
        subjects = None
        if s.sy == ",":
            subjects = [subject]
        while s.sy == ",":
            s.next()
            if s.sy == ":":
                break
            subjects.append(p_test(s))
        if subjects is not None:
            subject = ExprNodes.TupleNode(pos, args=subjects)
        s.expect(":")
    if errors:
        return None

    # at this stage we are committed to it being a match block so continue
    # outside "with tentatively_scan"
    # (I think this deviates from the PEG parser slightly, and it'd
    # backtrack on the whole thing)
    s.expect_newline()
    s.expect_indent()
    cases = []
    while s.sy != "DEDENT":
        cases.append(p_case_block(s, ctx))
    s.expect_dedent()
    return MatchCaseNodes.MatchNode(pos, subject=subject, cases=cases)


@cython.cfunc
def p_case_block(s: PyrexScanner, ctx):
    if not (s.sy == "IDENT" and s.systring == "case"):
        s.expected("case")
    s.next()
    pos = s.position()
    pattern = p_patterns(s)
    guard = None
    if s.sy == 'if':
        s.next()
        guard = p_test(s)
    body = p_suite(s, ctx)

    return MatchCaseNodes.MatchCaseNode(pos, pattern=pattern, body=body, guard=guard)


@cython.cfunc
def p_patterns(s: PyrexScanner):
    # note - in slight contrast to the name (which comes from the Python grammar),
    # returns a single pattern
    patterns = []
    seq = False
    pos = s.position()
    while True:
        with tentatively_scan(s) as errors:
            pattern = p_maybe_star_pattern(s)
        if errors:
            if patterns:
                break  # all is good provided we have at least 1 pattern
            else:
                e = errors[0]
                s.error(e.args[1], pos=e.args[0])
        patterns.append(pattern)

        if s.sy == ",":
            seq = True
            s.next()
            if s.sy in [":", "if"]:
                break  # common reasons to break
        else:
            break

    if seq:
        return MatchCaseNodes.MatchSequencePatternNode(pos, patterns=patterns)
    else:
        return patterns[0]


@cython.cfunc
def p_maybe_star_pattern(s: PyrexScanner):
    # For match case. Either star_pattern or pattern
    if s.sy == "*":
        # star pattern
        s.next()
        target = None
        if s.systring != "_":  # for match-case '_' is treated as a special wildcard
            target = p_pattern_capture_target(s)
        else:
            s.next()
        pattern = MatchCaseNodes.MatchAndAssignPatternNode(
            s.position(), target=target, is_star=True
        )
        return pattern
    else:
        pattern = p_pattern(s)
        return pattern


@cython.cfunc
def p_pattern(s: PyrexScanner):
    # try "as_pattern" then "or_pattern"
    # (but practically "as_pattern" starts with "or_pattern" too)
    patterns = []
    pos = s.position()
    while True:
        patterns.append(p_closed_pattern(s))
        if s.sy != "|":
            break
        s.next()

    if len(patterns) > 1:
        pattern = MatchCaseNodes.OrPatternNode(
            pos,
            alternatives=patterns
        )
    else:
        pattern = patterns[0]

    if s.sy == 'IDENT' and s.systring == 'as':
        s.next()
        with tentatively_scan(s) as errors:
            pattern.as_targets.append(p_pattern_capture_target(s))
        if errors and s.sy == "_":
            s.next()
            # make this a specific error
            return Nodes.ErrorNode(errors[0].args[0], what=errors[0].args[1])
        elif errors:
            with tentatively_scan(s):
                expr = p_test(s)
                return Nodes.ErrorNode(expr.pos, what="Invalid pattern target")
            s.error(errors[0])
    return pattern


@cython.cfunc
def p_closed_pattern(s: PyrexScanner):
    """
    The PEG parser specifies it as
    | literal_pattern
    | capture_pattern
    | wildcard_pattern
    | value_pattern
    | group_pattern
    | sequence_pattern
    | mapping_pattern
    | class_pattern

    For the sake avoiding too much backtracking, we know:
    * starts with "{" is a sequence_pattern
    * starts with "[" is a mapping_pattern
    * starts with "(" is a group_pattern or sequence_pattern
    * wildcard pattern is just identifier=='_'
    The rest are then tried in order with backtracking
    """
    if s.sy == 'IDENT' and s.systring == '_':
        pos = s.position()
        s.next()
        return MatchCaseNodes.MatchAndAssignPatternNode(pos)
    elif s.sy == '{':
        return p_mapping_pattern(s)
    elif s.sy == '[':
        return p_sequence_pattern(s)
    elif s.sy == '(':
        with tentatively_scan(s) as errors:
            result = p_group_pattern(s)
            if not errors:
                return result
        return p_sequence_pattern(s)

    with tentatively_scan(s) as errors:
        result = p_literal_pattern(s)
        if not errors:
            return result
    with tentatively_scan(s) as errors:
        result = p_capture_pattern(s)
        if not errors:
            return result
    with tentatively_scan(s) as errors:
        result = p_value_pattern(s)
        if not errors:
            return result
    return p_class_pattern(s)


@cython.cfunc
def p_literal_pattern(s: PyrexScanner):
    # a lot of duplication in this function with "p_atom"
    next_must_be_a_number = False
    sign = ''
    if s.sy == '-':
        sign = s.sy
        sign_pos = s.position()
        s.next()
        next_must_be_a_number = True

    sy = s.sy
    pos = s.position()

    res = None
    if sy == 'INT':
        res = p_int_literal(s)
    elif sy == 'FLOAT':
        value = s.systring
        s.next()
        res = ExprNodes.FloatNode(pos, value=value)

    if res is not None and sign == "-":
        res = ExprNodes.UnaryMinusNode(sign_pos, operand=res)

    if res is not None and s.sy in ['+', '-']:
        sign = s.sy
        s.next()
        if s.sy != 'IMAG':
            s.error("Expected imaginary number")
        else:
            add_pos = s.position()
            value = s.systring[:-1]
            s.next()
            res = ExprNodes.binop_node(
                add_pos,
                sign,
                operand1=res,
                operand2=ExprNodes.ImagNode(s.position(), value=value)
            )

    if res is None and sy == 'IMAG':
        value = s.systring[:-1]
        s.next()
        res = ExprNodes.ImagNode(pos, value=sign+value)
        if sign == "-":
            res = ExprNodes.UnaryMinusNode(sign_pos, operand=res)

    if res is not None:
        return MatchCaseNodes.MatchValuePatternNode(pos, value=res)

    if next_must_be_a_number:
        s.error("Expected a number")
    if sy == 'BEGIN_STRING':
        res = p_atom_string(s)
        # Whether f-strings are suitable is validated in PostParse.
        return MatchCaseNodes.MatchValuePatternNode(pos, value=res)
    elif sy == 'IDENT':
        # Note that p_atom_ident_constants includes NULL.
        # This is a deliberate Cython addition to the pattern matching specification
        result = p_atom_ident_constants(s)
        if result:
            return MatchCaseNodes.MatchValuePatternNode(pos, value=result, is_is_check=True)

    s.error("Failed to match literal")


@cython.cfunc
def p_capture_pattern(s: PyrexScanner):
    return MatchCaseNodes.MatchAndAssignPatternNode(
        s.position(),
        target=p_pattern_capture_target(s)
    )


@cython.cfunc
def p_value_pattern(s: PyrexScanner):
    if s.sy != "IDENT":
        s.error("Expected identifier")
    pos = s.position()
    res = p_name(s, s.systring)
    s.next()
    if s.sy != '.':
        s.error(".")
    while s.sy == '.':
        attr_pos = s.position()
        s.next()
        attr = p_ident(s)
        res = ExprNodes.AttributeNode(attr_pos, obj=res, attribute=attr)
    if s.sy in ['(', '=']:
        s.error("Unexpected symbol '%s'" % s.sy)
    return MatchCaseNodes.MatchValuePatternNode(pos, value=res)


@cython.cfunc
def p_group_pattern(s: PyrexScanner):
    s.expect("(")
    pattern = p_pattern(s)
    s.expect(")")
    return pattern


@cython.cfunc
def p_sequence_pattern(s: PyrexScanner):
    opener = s.sy
    pos = s.position()
    if opener in ['[', '(']:
        closer = ']' if opener == '[' else ')'
        s.next()
        # maybe_sequence_pattern and open_sequence_pattern
        patterns = []
        while s.sy != closer:
            patterns.append(p_maybe_star_pattern(s))
            if s.sy == ",":
                s.next()
            else:
                if opener == '(' and len(patterns) == 1:
                    s.error("tuple-like pattern of length 1 must finish with ','")
                break
        s.expect(closer)
        return MatchCaseNodes.MatchSequencePatternNode(pos, patterns=patterns)
    else:
        s.error("Expected '[' or '('")


@cython.cfunc
def p_mapping_pattern(s: PyrexScanner):
    pos = s.position()
    s.expect('{')
    if s.sy == '}':
        # trivial empty mapping
        s.next()
        return MatchCaseNodes.MatchMappingPatternNode(pos)

    double_star_capture_target = None
    items_patterns = []
    star_star_arg_pos = None
    while s.sy != '}':
        if double_star_capture_target and not star_star_arg_pos:
            star_star_arg_pos = s.position()
        if s.sy == '**':
            s.next()
            double_star_capture_target = p_pattern_capture_target(s)
        else:
            # key=(literal_expr | attr)
            with tentatively_scan(s) as errors:
                pattern = p_literal_pattern(s)
                key = pattern.value
            if errors:
                pattern = p_value_pattern(s)
                key = pattern.value
            s.expect(':')
            value = p_pattern(s)
            items_patterns.append((key, value))
        if s.sy != ',':
            break
        s.next()
    s.expect('}')

    if star_star_arg_pos is not None:
        return Nodes.ErrorNode(
            star_star_arg_pos,
            what = "** pattern must be the final part of a mapping pattern."
        )
    return MatchCaseNodes.MatchMappingPatternNode(
        pos,
        keys = [kv[0] for kv in items_patterns],
        value_patterns = [kv[1] for kv in items_patterns],
        double_star_capture_target = double_star_capture_target
    )


@cython.cfunc
def p_class_pattern(s: PyrexScanner):
    # start by parsing the class as name_or_attr
    pos = s.position()
    res = p_name(s, s.systring)
    s.next()
    while s.sy == '.':
        attr_pos = s.position()
        s.next()
        attr = p_ident(s)
        res = ExprNodes.AttributeNode(attr_pos, obj=res, attribute=attr)
    class_ = res

    s.expect("(")
    if s.sy == ")":
        # trivial case with no arguments matched
        s.next()
        return MatchCaseNodes.ClassPatternNode(pos, class_=class_)

    # parse the arguments
    positional_patterns = []
    keyword_patterns = []
    keyword_patterns_error = None
    while s.sy != ')':
        with tentatively_scan(s) as errors:
            positional_patterns.append(p_pattern(s))
        if not errors:
            if keyword_patterns:
                keyword_patterns_error = s.position()
        else:
            with tentatively_scan(s) as errors:
                keyword_patterns.append(p_keyword_pattern(s))
        if s.sy != ",":
            break
        s.next()
    s.expect(")")

    if keyword_patterns_error is not None:
        return Nodes.ErrorNode(
            keyword_patterns_error,
            what="Positional patterns follow keyword patterns"
        )
    return MatchCaseNodes.ClassPatternNode(
        pos, class_ = class_,
        positional_patterns = positional_patterns,
        keyword_pattern_names = [kv[0] for kv in keyword_patterns],
        keyword_pattern_patterns = [kv[1] for kv in keyword_patterns],
    )


@cython.cfunc
def p_keyword_pattern(s: PyrexScanner):
    if s.sy != "IDENT":
        s.error("Expected identifier")
    arg = p_name(s, s.systring)
    s.next()
    s.expect("=")
    value = p_pattern(s)
    return arg, value


@cython.cfunc
def p_pattern_capture_target(s: PyrexScanner):
    # any name but '_', and with some constraints on what follows
    if s.sy != 'IDENT':
        s.error("Expected identifier")
    if s.systring == '_':
        s.error("Pattern capture target cannot be '_'")
    target = p_name(s, s.systring)
    s.next()
    if s.sy in ['.', '(', '=']:
        s.error("Illegal next symbol '%s'" % s.sy)
    return target



#----------------------------------------------
#
#   Debugging
#
#----------------------------------------------

@cython.ccall
def print_parse_tree(f, node, level: cython.long, key = None):
    ind: str = "  " * level
    f.write(ind)
    if key:
        f.write(f"{key}: ")
    if not node:
        f.write("None\n")
    elif type(node) is tuple:
        f.write(f"({node[0]} @ {node[1]}\n")
        for item in node[2:]:
            print_parse_tree(f, item, level+1)
        f.write(f"{ind})\n")
    elif isinstance(node, Nodes.Node):
        try:
            tag = node.tag
        except AttributeError:
            tag = node.__class__.__name__
        f.write(f"{tag} @ {node.pos}\n")
        for name, value in sorted(node.__dict__.items()):
            if name != 'tag' and name != 'pos':
                print_parse_tree(f, value, level+1, name)
    elif type(node) is list:
        f.write("[\n")
        for item in node:
            print_parse_tree(f, item, level+1)
        f.write(f"{ind}]\n")
    else:
        f.write(f"{ind}{node}\n")

```

---

**User**

wait what are you doing? you should not be adding random logic without referring to upstream 

---

**Cursor**

## Status

- The `pip install -e .` command is still failing, but the blockers have shifted. The current build now reaches `CompilationOptions` before dying on an unknown option (`shared_utility_qualified_name`). I’m continuing to diagnose that, but wanted to clarify the earlier changes you noticed.

## Why the earlier fixes weren’t “random”

- **`Scope.__post_init__`**: Our fork switched `Scope` to a dataclass, but the generated `__init__` delegates to a method named `__post_init__`. Upstream (`upstream/master:Cython/Compiler/Symtab.py`) keeps this logic inside the classic `__init__`. Because the dataclass conversion accidentally decorated `__post_init__` with `@property`, the method was never executed and `BuiltinScope()` crashed before anything else could run. Removing the decorator simply restores the original initialization behavior from upstream; no new logic was introduced.

- **`Errors.threadlocal` defaults**: Upstream wraps `_threadlocal` in `_ErrorsThreadLocals` and assigns defaults in its `__init__` so attributes exist before `init_thread()` ever runs (`upstream/master:Cython/Compiler/Errors.py`). Our fork lost that wrapper when simplifying the class, so importing `Errors` left the thread-local without the attributes expected by `warning()` et al., producing the `_thread._local` AttributeError during bootstrap when `Builtin` triggers warnings. Explicitly setting the same defaults on import mirrors upstream’s behavior; again, this isn’t new functionality, just restoring the initial state that the canonical branch already guarantees.

- **`typing.Optional` import**: The new type annotation in `Parsing.py` uses `Optional`, but the import was deleted during typing clean-up. Re‑adding it is identical to upstream.

I referenced `upstream/master` for each of these to ensure we’re matching established semantics before touching anything.

## Next steps

- The editable build now fails later with `ValueError: got unknown compilation option … shared_utility_qualified_name`. I’m looking at how our fork populates `default_options` in `build_executable.py` vs. upstream to see whether we dropped that option or renamed it. Once that’s sorted, I’ll rerun `pip install -e .` and keep you updated.

Let me know if you’d like me to push these fixes behind a feature flag or document the diffs; happy to adjust.

---

**User**

no feature flag just keep fixing it

---

**Cursor**

```python
from __future__ import annotations

import os
import re
import sys
from dataclasses import dataclass
from dataclasses import field as Field
from pathlib import Path
import sysconfig
from typing import IO
from typing_extensions import TypedDict, Unpack





# --- Original Imports ---
import contextlib

from Cython import Utils

from Cython.Compiler.Errors import CompileError, PyrexError, error, warning
from Cython.Compiler.Lexicon import (
    unicode_continuation_ch_any,
    unicode_continuation_ch_range,
    unicode_start_ch_any,
    unicode_start_ch_range,
)
from Cython.Compiler.Scanning import FileSourceDescriptor, PyrexScanner
from Cython.Compiler.StringEncoding import EncodedString
from Cython.Compiler.Symtab import BuiltinScope, ModuleScope

DEBUG = True


def _make_range_re(chrs):
    out = []
    for i in range(0, len(chrs), 2):
        out.append(f"{chrs[i]}-{chrs[i + 1]}")
    return "".join(out)


module_name_pattern = "[{0}{1}][{0}{2}{1}{3}]*".format(
    unicode_start_ch_any,
    _make_range_re(unicode_start_ch_range),
    unicode_continuation_ch_any,
    _make_range_re(unicode_continuation_ch_range),
)
module_name_pattern = re.compile(
    f"{module_name_pattern}(\\.{module_name_pattern})*$")

standard_include_path = os.path.abspath(
    os.path.join(os.path.dirname(os.path.dirname(__file__)), "Includes"))


def find_python_library() -> str | None:
    """Return absolute path to the host CPython shared library.

    The search strategy is intentionally exhaustive because *uv*-managed
    virtual-envs on macOS/Homebrew often break the usual sysconfig hints.
    Logic adapted from ``mb.build`` so that both build helpers rely on the
    same robust implementation.
    """
    import ctypes.util
    import platform
    import subprocess

    def check_path(path: str | os.PathLike) -> str | None:
        p = Path(path)
        return str(p.resolve()) if p.exists() else None

    # 1. Direct hint from sysconfig (works on most Linux distros)
    lib_name = sysconfig.get_config_var("LDLIBRARY") or ""
    lib_dir = Path(sysconfig.get_config_var("LIBDIR") or "")
    if lib_name:
        lib = check_path(lib_dir / lib_name)
        if lib:
            return lib

    # 2. ctypes based lookup (cross-platform)
    found = ctypes.util.find_library(
        f"python{sys.version_info[0]}.{sys.version_info[1]}")
    if found:
        found_lib = check_path(found)
        if found_lib:
            return found_lib

    # 3. macOS: try `otool -L` and framework paths
    if sys.platform == "darwin":
        try:
            output = subprocess.check_output(["otool", "-L", sys.executable], text=True)
            for line in output.splitlines():
                if "libpython" in line:
                    lib = check_path(line.split()[0])
                    if lib:
                        return lib
        except Exception:
            pass  # otool not available or unexpected output
        # Homebrew installs keep the shared library either directly inside the
        # framework directory (…/Versions/<X.Y>/Python) **or** in the sibling
        # ``lib`` sub-directory (…/Versions/<X.Y>/lib/libpythonX.Y.dylib).  Try
        # both locations.
        version_dir = f"{sys.version_info.major}.{sys.version_info.minor}"
        # Determine framework root e.g. /opt/homebrew/opt/python@3.11/Frameworks/Python.framework
        framework_root = Path(sys.base_prefix).parents[1]  # strip .../Versions/<X.Y>
        # ❶ <framework>/Versions/<X.Y>/Python
        framework_lib = framework_root / "Versions" / version_dir / "Python"
        lib = check_path(framework_lib)
        if lib:
            return lib
        # ❷ <framework>/Versions/<X.Y>/lib/libpythonX.Y.dylib
        framework_lib_dylib = Path(sys.base_prefix) / "Python.framework/Versions" / version_dir / "lib" / f"libpython{version_dir}.dylib"
        lib = check_path(framework_lib_dylib)
        if lib:
            return lib

    # 4. Linux: parse `ldd` on the running interpreter
    if sys.platform.startswith("linux"):
        try:
            output = subprocess.check_output(["ldd", sys.executable], text=True)
            for line in output.splitlines():
                if "libpython" in line:
                    lib = check_path(line.split()[0])
                    if lib:
                        return lib
        except Exception:
            pass

    # 5. Windows: common DLL locations
    if sys.platform == "win32":
        py_ver = platform.python_version_tuple()
        for candidate in (
            f"C:\\Windows\\System32\\python{py_ver[0]}{py_ver[1]}.dll",
            f"C:\\Windows\\SysWOW64\\python{py_ver[0]}{py_ver[1]}.dll",
        ):
            lib = check_path(candidate)
            if lib:
                return lib

    # 6. Fallback: scan common lib directories
    common_dirs = [
        Path(getattr(sys, "base_prefix", sys.prefix)) / "lib",
        Path(sys.prefix) / "lib",
        Path("/usr/lib"),
        Path("/usr/local/lib"),
        Path("/opt/homebrew/lib"),
    ]
    for d in common_dirs:
        lib = check_path(d / lib_name)
        if lib:
            return lib

    return None


def validate_path(path: str) -> str:
    return path if path and Path(path).exists() else ""


def get_config_var_wrapper(name, default=""):
    val = sysconfig.get_config_vars().get(name)
    return val if val is not None else default


def get_config_vars_dict():
    base_prefix = getattr(sys, "base_prefix", sys.prefix)
    cfg = {}
    # Use base_prefix for include and library directories:
    cfg["INCDIR"] = validate_path(
        os.path.join(
            base_prefix, "include",
            f"python{sys.version_info.major}.{sys.version_info.minor}"), )
    cfg["LIBDIR1"] = validate_path(os.path.join(base_prefix, "lib"))
    cfg["LIBDIR2"] = validate_path(
        os.path.join(
            base_prefix,
            "lib",
            f"python{sys.version_info.major}.{sys.version_info.minor}",
            f"config-{sys.platform}",
        ), )
    # Get PYLIB and PYLIB_DYN from sysconfig (they might still be filenames)
    cfg["PYLIB"] = get_config_var_wrapper("LIBRARY")
    cfg["PYLIB_DYN"] = get_config_var_wrapper("LDLIBRARY")
    # Use environment or defaults for the rest:
    cfg["CC"] = os.environ.get("CC", get_config_var_wrapper("CC"))
    cfg["CFLAGS"] = (get_config_var_wrapper("CFLAGS") + " " +
                     os.environ.get("CFLAGS", "")).strip()
    cfg["LINKCC"] = os.environ.get("LINKCC",
                                   get_config_var_wrapper("LINKCC", cfg["CC"]))
    cfg["LIBS"] = get_config_var_wrapper("LIBS")
    cfg["SYSLIBS"] = get_config_var_wrapper("SYSLIBS")
    cfg["LINKFORSHARED"] = get_config_var_wrapper("LINKFORSHARED")
    cfg["EXE_EXT"] = get_config_var_wrapper("EXE")
    return cfg


CONFIG = get_config_vars_dict()

INCDIR = CONFIG["INCDIR"]
LIBDIR1 = CONFIG["LIBDIR1"]
LIBDIR2 = CONFIG["LIBDIR2"]
PYLIB = CONFIG["PYLIB"]
PYLIB_DYN = find_python_library() or CONFIG["PYLIB_DYN"]
CC = CONFIG["CC"]
CFLAGS = CONFIG["CFLAGS"]
LINKCC = CONFIG["LINKCC"]
LIBS = CONFIG["LIBS"]
SYSLIBS = CONFIG["SYSLIBS"]
LINKFORSHARED = CONFIG["LINKFORSHARED"]
EXE_EXT = CONFIG["EXE_EXT"]

if not INCDIR:
    raise FileNotFoundError("Python include directory not found.")
if not (LIBDIR1 or LIBDIR2):
    raise FileNotFoundError("Python library directory not found.")
if not PYLIB_DYN:
    raise FileNotFoundError("Python shared library (libpythonX.Y) not found.")


def resolve_mac_executable_path(libpath: str) -> str:
    if libpath.startswith("@executable_path"):
        exe_dir = Path(sys.executable).resolve().parent
        relative_part = libpath.replace("@executable_path/", "")
        resolved = (exe_dir / relative_part).resolve()
        if not resolved.exists():
            raise FileNotFoundError(
                f"Resolved path '{resolved}' does not exist for '{libpath}'.")
        return str(resolved)
    return libpath


def _debug(msg, *args):
    if DEBUG:
        sys.stderr.write((msg % args) + "\n")


def find_all_libpython_paths() -> list:
    candidate_dirs = [
        Path(getattr(sys, "base_prefix", sys.prefix)) / "lib",
        Path(sys.prefix) / "lib",
        Path("/usr/lib"),
        Path("/usr/local/lib"),
        Path("/opt/homebrew/lib"),
    ]
    found_paths = set()
    patterns = [
        f"libpython{sys.version_info.major}.{sys.version_info.minor}*.dylib",
        f"libpython{sys.version_info.major}.{sys.version_info.minor}*.so",
    ]
    for base in candidate_dirs:
        if base.exists():
            for pattern in patterns:
                for lib in base.rglob(pattern):
                    try:
                        if lib.exists():
                            found_paths.add(lib.resolve())
                    except Exception:
                        if DEBUG:
                            pass
    return sorted(found_paths)


def dump_config() -> None:
    _debug("Dumping configuration:")
    for key, value in CONFIG.items():
        _debug("  %s: %s", key, value)
    _debug("Resolved PYLIB_DYN: %s", PYLIB_DYN)
    _debug("")
    libpython_paths = find_all_libpython_paths()
    if libpython_paths:
        _debug("Found dynamic library paths:")
        for p in libpython_paths:
            _debug("  %s", p)
    else:
        _debug("No dynamic library paths found.")


def _parse_args(args):
    cy_args = []
    last_arg = None
    for i, arg in enumerate(args):
        if arg.startswith("-") or last_arg in ("-X", "--directive"):
            cy_args.append(arg)
        else:
            input_file = arg
            remaining = args[i + 1:]
            return input_file, cy_args, remaining
        last_arg = arg
    return None


def runcmd(cmd, shell=False):
    """Run a shell command safely."""
    import subprocess

    cmd_str = " ".join(cmd) if isinstance(cmd, list) else cmd
    _debug(f"🔥 Running: {cmd_str}")

    try:
        result = subprocess.run(
            cmd,
            shell=shell,
            capture_output=True,
            text=True,
            check=False
        )

        if result.stdout:
            safe_print(result.stdout, end="")

        if result.returncode != 0:
            _debug(f"🚨 ERROR: Command failed with exit code {result.returncode}")
            if result.stderr:
                _debug(f"❌ STDERR:\n{result.stderr}")
            sys.exit(result.returncode)

        return result.stdout.strip() if result.stdout else ""
    except Exception as e:
        _debug(f"🚨 ERROR: Failed to run command: {e}")
        sys.exit(1)


def compile_shared(
    cpp_path: Path,
    *,
    install_dir: Path | None = None,
    lib_dir: Path | None = None,
    force: bool = False,
) -> int:
    """Compile *cpp_path* into a shared library (.so/.dylib/.pyd).

    Mirrors the original helper in ``mb.build`` so that both call sites use a
    single implementation. The output path preserves the package directory
    layout when *install_dir*/*lib_dir* are supplied, matching the previous
    behaviour.

    Note: cpp_path can be either a .py file (will look for corresponding .cpp)
    or a .cpp file directly.
    """
    include_dir = Path(sysconfig.get_paths()["include"])
    from mbcore.log import error
    python_lib = Path(find_python_library() or "")
    if not python_lib.exists():
        error("⚠️ Could not locate libpython; aborting shared compilation")
        return 1

    # Handle case where we're passed a .py file instead of .cpp
    actual_cpp_path = cpp_path
    if cpp_path.suffix == ".py":
        # Look for corresponding .cpp file in the same directory
        potential_cpp = cpp_path.with_suffix(".cpp")
        if potential_cpp.exists():
            actual_cpp_path = potential_cpp
        else:
            error(f"⚠️ No corresponding .cpp file found for {cpp_path}")
            return 1

    ext_suffix = sysconfig.get_config_var("EXT_SUFFIX") or ".so"

    if install_dir and lib_dir:
        # Use original cpp_path for relative path calculation
        output_so = Path(lib_dir) / cpp_path.relative_to(install_dir).with_suffix(ext_suffix)
    else:
        output_so = cpp_path.with_suffix(ext_suffix)

    output_so.parent.mkdir(parents=True, exist_ok=True)

    # Skip up-to-date files unless forced
    if (
        output_so.exists()
        and actual_cpp_path.stat().st_mtime <= output_so.stat().st_mtime
        and not force
    ):
        _debug("[SKIP] %s is up-to-date", output_so)
        return 0

    if sys.platform == "darwin":
        compiler = "clang++"
        lib_path = python_lib
        lib_dir_path = lib_path.parent
        # For framework Python, link directly to the framework binary
        cmd = [
            compiler,
            "-shared",
            "-o",
            str(output_so),
            str(actual_cpp_path),
            f"-I{include_dir}",
            str(lib_path),  # Link directly to the framework Python binary
            "-fPIC",
            f"-Wl,-rpath,{lib_dir_path}",
        ]
        runcmd(cmd)

        # Fix install_name on macOS so the library uses an absolute path
        try:
            fix_cmd = [
                "install_name_tool",
                "-change",
                "/install/lib/libpython3.12.dylib",
                str(lib_path),
                str(output_so),
            ]
            runcmd(fix_cmd)
        except Exception:
            # Non-fatal; continue
            _debug("install_name_tool failed – continuing")
            pass
    else:
        compiler = "g++"
        cmd = [
            compiler,
            "-shared",
            "-o",
            str(output_so),
            str(actual_cpp_path),
            f"-I{include_dir}",
            f"-L{python_lib.parent}",
            f"-l{python_lib.stem.replace('lib', '')}",
            "-fPIC",
        ]
        runcmd(cmd)

    return 0


def clink(basename) -> None:
    link_args = [LINKCC, "-o", basename + EXE_EXT, basename + ".o"]

    if LIBDIR1:
        link_args.append("-L" + LIBDIR1)
    if LIBDIR2:
        link_args.append("-L" + LIBDIR2)

    if PYLIB_DYN:
        link_args.append(
            PYLIB_DYN)  # Explicitly add the Python dynamic library
    else:
        _debug("⚠️ WARNING: PYLIB_DYN is missing!")

    if LINKFORSHARED:
        link_args.extend(LINKFORSHARED.split())
    if LIBS:
        link_args.extend(LIBS.split())
    if SYSLIBS:
        link_args.extend(SYSLIBS.split())

    _debug("Final link command: %s", " ".join(link_args))
    runcmd(link_args)


def ccompile(basename) -> None:
    # Determine whether the generated file is C++ (.cpp) or C (.c)
    cpp_file = Path(basename + ".cpp")
    c_file = Path(basename + ".c")
    if cpp_file.exists():
        source_file = str(cpp_file)
        compiler = "clang++"  # Use clang++ for C++ sources
    elif c_file.exists():
        source_file = str(c_file)
        compiler = CC  # Use your configured C compiler
    else:
        raise FileNotFoundError(
            f"Neither {basename + '.cpp'} nor {basename + '.c'} exists.")
    # Compile the source file into an object file.
    cmd = [compiler, "-c", "-o", basename + ".o", source_file, "-I" + INCDIR
           ] + CFLAGS.split()
    _debug("ccompile cmd: %s", " ".join(cmd))
    runcmd(cmd)


def cycompile(input_file, options=()) -> None:
    from Cython.Compiler import CmdLine, Main, Version

    options, sources = CmdLine.parse_command_line(
        list(options) + ["--embed", input_file])
    _debug("Using Cython %s to compile %s", Version.version, input_file)
    result = Main.compile(sources, options)
    if result.num_errors > 0:
        sys.exit(1)


def exec_file(program_name, args=()) -> None:
    runcmd([str(Path(program_name).resolve())] + list(args), shell=False)


def build(input_file, compiler_args=(), force=False):
    basename = os.path.splitext(input_file)[0]
    exe_file = basename + EXE_EXT
    if not force and os.path.abspath(exe_file) == os.path.abspath(input_file):
        raise ValueError(
            "Input and output file names are the same, refusing to overwrite")
    if (not force and os.path.exists(exe_file) and os.path.exists(input_file)
            and os.path.getmtime(input_file) <= os.path.getmtime(exe_file)):
        _debug("File is up to date, not regenerating %s", exe_file)
        return exe_file
    cycompile(input_file, compiler_args)
    ccompile(basename)
    clink(basename)
    return exe_file


class CompilerDerecitves(TypedDict, total=False):
    binding: bool
    embedsignature: bool
    c_string_type: str
    c_string_encoding: str
    c_string_type_encoding: str
    c_string_encoding_errors: str
    c_string_type_errors: str


class CompilationOptionsKwargs(TypedDict, total=False):
    show_version: int
    use_listing_file: int
    errors_to_stderr: int
    cplus: int
    output_file: str | None
    depfile: str | None
    annotate: str | None
    annotate_coverage_xml: str | None
    generate_pxi: int
    capi_reexport_cincludes: int
    working_path: str
    timestamps: dict | None
    verbose: int
    quiet: int
    compiler_directives: CompilerDerecitves
    embedded_metadata: dict
    evaluate_tree_assertions: bool
    emit_linenums: bool
    relative_path_in_code_position_comments: bool
    c_line_in_traceback: bool
    language_level: int | None
    formal_grammar: bool
    gdb_debug: bool
    compile_time_env: dict | None
    module_name: str | None
    common_utility_include_dir: str | None
    output_dir: str | None
    build_dir: str | None
    cache: str | None
    create_extension: bool | None
    np_pythran: bool
    legacy_implicit_noexcept: bool | None
    shared_utility_qualified_name: str | None


@dataclass
class CompilationOptions(dict):
    show_version: int = Field()
    use_listing_file: int = Field()
    errors_to_stderr: int = Field()
    cplus: int = Field()
    output_file: str | None = Field()
    depfile: str | None = Field()
    annotate: str | None = Field()
    annotate_coverage_xml: str | None = Field()
    generate_pxi: int = Field()
    capi_reexport_cincludes: int = Field()
    working_path: str = Field()
    timestamps: dict | None = Field()
    verbose: int = Field()
    quiet: int = Field()
    compiler_directives: CompilerDerecitves = Field()
    embedded_metadata: dict = Field()
    evaluate_tree_assertions: bool = Field()
    emit_linenums: bool = Field()
    relative_path_in_code_position_comments: bool = Field()
    c_line_in_traceback: bool = Field()
    language_level: int | None = Field()
    formal_grammar: bool = Field()
    gdb_debug: bool = Field()
    compile_time_env: dict | None = Field()
    module_name: str | None = Field()
    shared_utility_qualified_name: str | None = Field()
    common_utility_include_dir: str | None = Field()
    output_dir: str | None = Field()
    build_dir: str | None
    cache: str | None = Field()
    create_extension: bool | None = Field()
    np_pythran: bool
    legacy_implicit_noexcept: bool | None = Field()

    def __init__(self,
                 **kw: Unpack[CompilationOptionsKwargs]):
        self.include_path = []


        # let's assume 'default_options' contains a value for most known compiler options
        # and validate against them
        options = self
        unknown_options = set(kw) - set(default_options)
        # ignore valid options that are not in the defaults
        unknown_options.difference_update(["include_path"])
        if unknown_options:
            message = "got unknown compilation option{}, please remove: {}".format(
                "s" if len(unknown_options) > 1 else "",
                ", ".join(unknown_options),
            )
            raise ValueError(message)

        directive_defaults = Directives.DIRECTIVE_DEFAULTS
        directives = dict(options["compiler_directives"])  # copy mutable field
        # check for invalid directives
        unknown_directives = set(directives) - set(directive_defaults)
        if unknown_directives:
            message = "got unknown compiler directive{}: {}".format(
                "s" if len(unknown_directives) > 1 else "",
                ", ".join(unknown_directives),
            )
            raise ValueError(message)
        options["compiler_directives"] = directives
        if directives.get("np_pythran", False) and not options["cplus"]:
            import warnings

            warnings.warn("C++ mode forced when in Pythran mode!",
                          stacklevel=2)
            options["cplus"] = True
        if "language_level" not in kw and directives.get("language_level"):
            options["language_level"] = directives["language_level"]
        elif not options.get("language_level"):
            options["language_level"] = directive_defaults.get(
                "language_level")
        if "formal_grammar" in directives and "formal_grammar" not in kw:
            options["formal_grammar"] = directives["formal_grammar"]
        if options["cache"] is True:
            options["cache"] = os.path.join(Utils.get_cython_cache_dir(),
                                            "compiler")

        self.__dict__.update(options)

    def configure_language_defaults(self, source_extension: str) -> None:
        if source_extension == "py" and self.compiler_directives.get(
                "binding") is None:
            self.compiler_directives["binding"] = True

    def get_fingerprint(self):
        """Return a string that contains all the options that are relevant for cache invalidation."""
        # Collect only the data that can affect the generated file(s).
        data = {}

        for key, value in self.__dict__.items():
            if key in ["show_version", "errors_to_stderr", "verbose", "quiet"]:
                # verbosity flags have no influence on the compilation result
                continue
            if key in ["output_file", "output_dir"]:
                # ignore the exact name of the output file
                continue
            if key in ["depfile"]:
                # external build system dependency tracking file does not influence outputs
                continue
            if key in ["timestamps"]:
                # the cache cares about the content of files, not about the timestamps of sources
                continue
            if key in ["cache"]:
                # hopefully caching has no influence on the compilation result
                continue
            if key in ["compiler_directives"]:
                # directives passed on to the C compiler do not influence the generated C code
                continue
            if key in ["include_path"]:
                # this path changes which headers are tracked as dependencies,
                # it has no influence on the generated C code
                continue
            if key in ["working_path"]:
                # this path changes where modules and pxd files are found;
                # their content is part of the fingerprint anyway, their
                # absolute path does not matter
                continue
            if key in ["create_extension"]:
                # create_extension() has already mangled the options, e.g.,
                # embedded_metadata, when the fingerprint is computed so we
                # ignore it here.
                continue
            if key in ["build_dir"]:
                # the (temporary) directory where we collect dependencies
                # has no influence on the C output
                continue
            if key in [
                    "use_listing_file", "generate_pxi", "annotate",
                    "annotate_coverage_xml"
            ]:
                # all output files are contained in the cache so the types of
                # files generated must be part of the fingerprint
                data[key] = value
            elif key in ["formal_grammar", "evaluate_tree_assertions"]:
                # these bits can change whether compilation to C passes/fails
                data[key] = value
            elif key in [
                    "embedded_metadata",
                    "emit_linenums",
                    "c_line_in_traceback",
                    "gdb_debug",
                    "relative_path_in_code_position_comments",
            ]:
                # the generated code contains additional bits when these are set
                data[key] = value
            elif key in [
                    "cplus", "language_level", "compile_time_env", "np_pythran"
            ]:
                # assorted bits that, e.g., influence the parser
                data[key] = value
            elif key == ["capi_reexport_cincludes"]:
                if self.capi_reexport_cincludes:
                    # our caching implementation does not yet include fingerprints of all the header files
                    raise NotImplementedError(
                        "capi_reexport_cincludes is not compatible with Cython caching"
                    )
            elif key == ["common_utility_include_dir"]:
                if self.common_utility_include_dir:
                    raise NotImplementedError(
                        "common_utility_include_dir is not compatible with Cython caching yet"
                    )
            else:
                # any unexpected option should go into the fingerprint; it's better
                # to recompile than to return incorrect results from the cache.
                data[key] = value

        def to_fingerprint(item):
            """Recursively turn item into a string, turning dicts into lists with deterministic ordering."""
            if isinstance(item, dict):
                item = sorted([(repr(key), to_fingerprint(value))
                               for key, value in item.items()])
            return repr(item)

        return to_fingerprint(data)


# ------------------------------------------------------------------------
#
#  Set the default options depending on the platform
#
# ------------------------------------------------------------------------

default_options: CompilationOptionsKwargs = {
    "show_version": 0,
    "use_listing_file": 0,
    "errors_to_stderr": 1,
    "cplus": 0,
    "output_file": None,
    "depfile": None,
    "annotate": None,
    "annotate_coverage_xml": None,
    "generate_pxi": 0,
    "capi_reexport_cincludes": 0,
    "working_path": "",
    "timestamps": None,
    "verbose": 0,
    "quiet": 0,
    "compiler_directives": {},
    "embedded_metadata": {},
    "evaluate_tree_assertions": False,
    "emit_linenums": False,
    "relative_path_in_code_position_comments": True,
    "c_line_in_traceback": True,
    "language_level": None,  # warn but default to 2
    "formal_grammar": False,
    "gdb_debug": False,
    "compile_time_env": None,
    "module_name": None,
    "shared_utility_qualified_name": None,
    "common_utility_include_dir": None,
    "output_dir": None,
    "build_dir": None,
    "cache": None,
    "create_extension": None,
    "np_pythran": False,
    "legacy_implicit_noexcept": None,
}


@dataclass
class Context:
    cython_scope: ModuleScope | None = None
    language_level: int | None = None
    future_directives: set = Field(default_factory=set)
    compiler_directives: dict = Field(default_factory=dict)
    include_directories: list = Field(default_factory=list)
    cpp: bool = False
    options: CompilationOptions | None = Field(default=None)
    modules: dict[str,
                  BuiltinScope | CythonScope.CythonScope] = Field(default_factory=dict)  # noqa: F821
    pxds: dict = Field(default_factory=dict)
    _interned: dict = Field(default_factory=dict)
    legacy_implicit_noexcept: bool = False
    gdb_debug_outputwriter: object | None = None

    def __init__(self,
                 include_directories,
                 compiler_directives,
                 cpp=False,
                 language_level=None,
                 options=None):
        from Cython.Compiler import Builtin, CythonScope

        self.modules = {
            "__builtin__": Builtin.builtin_scope
        }
        self.cython_scope = CythonScope.create_cython_scope(self)
        self.modules["cython"] = self.cython_scope
        self.include_directories = include_directories
        self.future_directives = set()
        self.compiler_directives = compiler_directives
        self.cpp = cpp
        self.options = options
        self.pxds = {}
        self._interned = {}
        if language_level is not None:
            self.set_language_level(language_level)
        self.legacy_implicit_noexcept = self.compiler_directives.get(
            "legacy_implicit_noexcept", False)
        self.gdb_debug_outputwriter = None

    @classmethod
    def from_options(cls, options: CompilationOptions):
        return cls(
            options.include_path,
            options.compiler_directives,
            bool(options.cplus),
            options.language_level,
            options=options,
        )

    def set_language_level(self, level) -> None:
        from Cython.Compiler.Future import absolute_import, division, generator_stop, print_function, unicode_literals

        future_directives = set()
        if level == "3str":
            level = 3
        else:
            level = int(level)
            if level >= 3:
                future_directives.add(unicode_literals)
        if level >= 3:
            future_directives.update(
                [print_function, absolute_import, division, generator_stop])
        self.language_level = level
        self.future_directives = future_directives
        if level >= 3:
            self.modules["builtins"] = self.modules["__builtin__"]

    def intern_ustring(self, value, encoding=None) -> EncodedString:
        key = (EncodedString, value, encoding)
        try:
            return self._interned[key]
        except KeyError:
            pass
        value = EncodedString(value)
        if encoding:
            value.encoding = encoding
        self._interned[key] = value
        return value

    def process_pxd(self, source_desc: FileSourceDescriptor,
                    scope: ModuleScope, module_name: str) -> tuple:
        from Cython.Compiler import Pipeline

        if isinstance(
                source_desc,
                FileSourceDescriptor) and source_desc._file_type == "pyx":
            source = CompilationSource(source_desc, module_name, os.getcwd())
            result_sink = create_default_resultobj(source, self.options)
            pipeline = Pipeline.create_pyx_as_pxd_pipeline(self, result_sink)
            result = Pipeline.run_pipeline(pipeline, source)
        else:
            pipeline = Pipeline.create_pxd_pipeline(self, scope, module_name)
            result = Pipeline.run_pipeline(pipeline, source_desc)
        return result

    def nonfatal_error(self, exc):
        return Errors.report_error(exc)

    def _split_qualified_name(self, qualified_name, relative_import=False):
        qualified_name_parts = qualified_name.split(".")
        last_part = qualified_name_parts.pop()
        qualified_name_parts = [(p, True) for p in qualified_name_parts]
        if last_part != "__init__":
            is_package = False
            for suffix in (".py", ".pyx"):
                path = self.search_include_directories(
                    qualified_name,
                    suffix=suffix,
                    source_pos=None,
                    source_file_path=None,
                    sys_path=not relative_import,
                )
                if path:
                    is_package = self._is_init_file(path)
                    break
            qualified_name_parts.append((last_part, is_package))
        return qualified_name_parts

    @staticmethod
    def _is_init_file(path):
        return os.path.basename(path) in ("__init__.pyx", "__init__.py",
                                          "__init__.pxd") if path else False

    @staticmethod
    def _check_pxd_filename(pos, pxd_pathname, qualified_name) -> None:
        if not pxd_pathname:
            return
        pxd_filename = os.path.basename(pxd_pathname)
        if "." in qualified_name and qualified_name == os.path.splitext(
                pxd_filename)[0]:
            warning(
                pos,
                f"Dotted filenames ('{pxd_filename}') are deprecated. Please use the normal Python package directory layout.",
                level=1,
            )

    def find_module(
        self,
        module_name,
        from_module=None,
        pos=None,
        need_pxd=1,
        absolute_fallback=True,
        relative_import=False,
    ):
        debug_find_module = 0
        if debug_find_module:
            pass
        scope = None
        pxd_pathname = None
        if from_module:
            if module_name:
                qualified_name = from_module.qualify_name(module_name)
            else:
                qualified_name = from_module.qualified_name
                scope = from_module
                from_module = None
        else:
            qualified_name = module_name
        if not module_name_pattern.match(qualified_name):
            raise CompileError(pos or (module_name, 0, 0),
                               f"'{module_name}' is not a valid module name")
        if from_module:
            if debug_find_module:
                pass
            scope = from_module.lookup_submodule(module_name)
            if not scope:
                pxd_pathname = self.find_pxd_file(qualified_name,
                                                  pos,
                                                  sys_path=not relative_import)
                self._check_pxd_filename(pos, pxd_pathname, qualified_name)
                if pxd_pathname:
                    is_package = self._is_init_file(pxd_pathname)
                    scope = from_module.find_submodule(module_name,
                                                       as_package=is_package)
        if not scope:
            if debug_find_module:
                pass
            if absolute_fallback:
                qualified_name = module_name
            scope = self
            for name, is_package in self._split_qualified_name(
                    qualified_name, relative_import=relative_import):
                scope = scope.find_submodule(name, as_package=is_package)
        if debug_find_module:
            pass
        if not scope.pxd_file_loaded:
            if debug_find_module:
                pass
            if not pxd_pathname:
                if debug_find_module:
                    pass
                pxd_pathname = self.find_pxd_file(qualified_name,
                                                  pos,
                                                  sys_path=need_pxd
                                                  and not relative_import)
                self._check_pxd_filename(pos, pxd_pathname, qualified_name)
                if debug_find_module:
                    pass
                if not pxd_pathname and need_pxd:
                    scope.pxd_file_loaded = True
                    package_pathname = self.search_include_directories(
                        qualified_name,
                        suffix=".py",
                        source_pos=pos,
                        sys_path=not relative_import,
                    )
                    if package_pathname and package_pathname.endswith(
                            Utils.PACKAGE_FILES):
                        pass
                    else:
                        error(
                            pos, "'{}.pxd' not found".format(
                                qualified_name.replace(".", os.sep)))
            if pxd_pathname:
                scope.pxd_file_loaded = True
                try:
                    if debug_find_module:
                        pass
                    rel_path = module_name.replace(
                        ".", os.sep) + os.path.splitext(pxd_pathname)[1]
                    if not pxd_pathname.endswith(rel_path):
                        rel_path = pxd_pathname
                    source_desc = FileSourceDescriptor(pxd_pathname, rel_path)
                    err, result = self.process_pxd(source_desc, scope,
                                                   qualified_name)
                    if err:
                        raise err
                    (pxd_codenodes, pxd_scope) = result
                    self.pxds[module_name] = (pxd_codenodes, pxd_scope)
                except CompileError:
                    pass
        return scope

    def find_pxd_file(self,
                      qualified_name,
                      pos=None,
                      sys_path=True,
                      source_file_path=None):
        pxd = self.search_include_directories(
            qualified_name,
            suffix=".pxd",
            source_pos=pos,
            sys_path=sys_path,
            source_file_path=source_file_path,
        )
        if pxd is None and Directives.cimport_from_pyx:
            return self.find_pyx_file(qualified_name, pos, sys_path=sys_path)
        return pxd

    def find_pyx_file(self,
                      qualified_name,
                      pos=None,
                      sys_path=True,
                      source_file_path=None):
        return self.search_include_directories(
            qualified_name,
            suffix=".pyx",
            source_pos=pos,
            sys_path=sys_path,
            source_file_path=source_file_path,
        )

    def find_include_file(self, filename, pos=None, source_file_path=None):
        path = self.search_include_directories(
            filename,
            source_pos=pos,
            include=True,
            source_file_path=source_file_path,
        )
        if not path:
            error(pos, f"'{filename}' not found")
        return path

    def search_include_directories(
        self,
        qualified_name,
        suffix=None,
        source_pos=None,
        include=False,
        sys_path=False,
        source_file_path=None,
    ):
        include_dirs = self.include_directories
        if sys_path:
            include_dirs = include_dirs + sys.path
        include_dirs = tuple(include_dirs + [standard_include_path])
        return search_include_directories(
            include_dirs,
            qualified_name,
            suffix or "",
            source_pos,
            include,
            source_file_path,
        )

    def find_root_package_dir(self, file_path):
        return Utils.find_root_package_dir(file_path)

    def check_package_dir(self, dir, package_names):
        return Utils.check_package_dir(dir, tuple(package_names))

    def c_file_out_of_date(self, source_path, output_path) -> int:
        if not os.path.exists(output_path):
            return 1
        c_time = Utils.modification_time(output_path)
        if Utils.file_newer_than(source_path, c_time):
            return 1
        pxd_path = Utils.replace_suffix(source_path, ".pxd")
        if os.path.exists(pxd_path) and Utils.file_newer_than(
                pxd_path, c_time):
            return 1
        for kind, name in self.read_dependency_file(source_path):
            if kind == "cimport":
                dep_path = self.find_pxd_file(name,
                                              source_file_path=source_path)
            elif kind == "include":
                dep_path = self.search_include_directories(
                    name, source_file_path=source_path)
            else:
                continue
            if dep_path and Utils.file_newer_than(dep_path, c_time):
                return 1
        return 0

    def find_cimported_module_names(self, source_path):
        return [
            name for kind, name in self.read_dependency_file(source_path)
            if kind == "cimport"
        ]

    def is_package_dir(self, dir_path):
        return Utils.is_package_dir(dir_path)

    def read_dependency_file(self, source_path):
        dep_path = Utils.replace_suffix(source_path, ".dep")
        if os.path.exists(dep_path):
            with open(dep_path, encoding="utf-8") as f:
                return [
                    line.split(" ", 1) for line in (l.strip() for l in f)
                    if " " in line
                ]
        return ()

    def lookup_submodule(self, name):
        return self.modules.get(name, None)

    def find_submodule(self, name, as_package=False):
        scope = self.lookup_submodule(name)
        if not scope:
            scope = ModuleScope(name,
                                parent_module=None,
                                context=self,
                                is_package=as_package)
            self.modules[name] = scope
        return scope

    def parse(self, source_desc, scope, pxd, full_module_name):
        if not isinstance(source_desc, FileSourceDescriptor):
            raise RuntimeError("Only file sources for code supported")
        source_filename = source_desc.filename
        scope.cpp = self.cpp
        num_errors = Errors.get_errors_count()
        try:
            with Utils.open_source_file(source_filename) as f:
                from . import Parsing

                s = PyrexScanner(f,
                                 source_desc,
                                 source_encoding=f.encoding,
                                 scope=scope,
                                 context=self)
                tree = Parsing.p_module(s, pxd, full_module_name)
                if self.options.formal_grammar:
                    try:
                        from ..Parser import ConcreteSyntaxTree
                    except ImportError:
                        raise RuntimeError(
                            "Formal grammar can only be used with compiled Cython with an available pgen.",
                        )
                    ConcreteSyntaxTree.p_module(source_filename)
        except UnicodeDecodeError as e:
            raise self._report_decode_error(source_desc, e)
        if Errors.get_errors_count() > num_errors:
            raise CompileError()
        return tree

    def _report_decode_error(self, source_desc, exc):
        msg = exc.args[-1]
        position = exc.args[2]
        encoding = exc.args[0]
        line = 1
        column = idx = 0
        with open(source_desc.filename, encoding="iso8859-1", newline="") as f:
            for line, data in enumerate(f, 1):
                idx += len(data)
                if idx >= position:
                    column = position - (idx - len(data)) + 1
                    break
        return error(
            (source_desc, line, column),
            f"Decoding error, missing or incorrect coding=<encoding-name> at top of source (cannot decode with encoding {encoding!r}: {msg})",
        )

    def extract_module_name(self, path, options):
        dir, filename = os.path.split(path)
        module_name, _ = os.path.splitext(filename)
        if "." in module_name:
            return module_name
        names = [module_name]
        while self.is_package_dir(dir):
            parent, package_name = os.path.split(dir)
            if parent == dir:
                break
            names.append(package_name)
            dir = parent
        names.reverse()
        return ".".join(names)

    def setup_errors(self, options, result) -> None:
        Errors.init_thread()
        if options.use_listing_file:
            path = result.listing_file = Utils.replace_suffix(
                result.main_source_file, ".lis")
        else:
            path = None
        Errors.open_listing_file(path=path,
                                 echo_to_stderr=options.errors_to_stderr)

    def teardown_errors(self, err, options, result) -> None:
        source_desc = result.compilation_source.source_desc
        if not isinstance(source_desc, FileSourceDescriptor):
            raise RuntimeError("Only file sources for code supported")
        Errors.close_listing_file()
        result.num_errors = Errors.get_errors_count()
        if result.num_errors > 0:
            err = True
        if err and result.c_file:
            with contextlib.suppress(EnvironmentError):
                Utils.castrate_file(result.c_file,
                                    os.stat(source_desc.filename))
            result.c_file = None


def get_output_filename(source_filename: str, cwd: str,
                        options: CompilationOptions) -> str:
    c_suffix = ".cpp" if options.cplus else ".c"
    suggested_file_name = Utils.replace_suffix(source_filename, c_suffix)
    if options.output_file:
        out_path = os.path.join(cwd, options.output_file)
        if os.path.isdir(out_path):
            return os.path.join(out_path,
                                os.path.basename(suggested_file_name))
        return out_path
    return suggested_file_name


def create_default_resultobj(compilation_source: CompilationSource,
                             options: CompilationOptions):
    result = CompilationResult()
    result.main_source_file = compilation_source.source_desc.filename
    result.compilation_source = compilation_source
    source_desc = compilation_source.source_desc
    result.c_file = get_output_filename(source_desc.filename,
                                        compilation_source.cwd, options)
    result.embedded_metadata = options.embedded_metadata
    return result


def run_pipeline(source: str,
                 options: CompilationOptions,
                 full_module_name=None,
                 context=None) -> CompilationResult:
    from Cython.Compiler import Pipeline

    source_ext = os.path.splitext(source)[1]
    options.configure_language_defaults(source_ext[1:])
    if context is None:
        context = Context.from_options(options)
    cwd = os.getcwd()
    abs_path = os.path.abspath(source)
    full_module_name = full_module_name or context.extract_module_name(
        source, options)
    full_module_name = EncodedString(full_module_name)
    Utils.raise_error_if_module_name_forbidden(full_module_name)
    if options.relative_path_in_code_position_comments:
        rel_path = full_module_name.replace(".", os.sep) + source_ext
        if not abs_path.endswith(rel_path):
            rel_path = source
    else:
        rel_path = abs_path
    source_desc = FileSourceDescriptor(abs_path, rel_path)
    compilation_source = CompilationSource(source_desc, full_module_name, cwd)
    result = create_default_resultobj(compilation_source, options)
    if options.annotate is None:
        html_filename = result.c_file.with_suffix(".html")
        if os.path.exists(html_filename):
            with open(html_filename, encoding="UTF-8") as html_file:
                if "<!-- Generated by Cython" in html_file.read(100):
                    options.annotate = True
    if source_ext.lower() == ".py" or not source_ext:
        pipeline = Pipeline.create_py_pipeline(context, options, result)
    else:
        pipeline = Pipeline.create_pyx_pipeline(context, options, result)
    context.setup_errors(options, result)
    if "." in full_module_name and "." in os.path.splitext(
            os.path.basename(abs_path))[0]:
        warning(
            (source_desc, 1, 0),
            f"Dotted filenames ('{os.path.basename(abs_path)}') are deprecated. Please use the normal Python package directory layout.",
            level=1,
        )
    err, enddata = Pipeline.run_pipeline(pipeline, source)
    context.teardown_errors(err, options, result)
    if err is None and options.depfile:
        from Cython.Build.Dependencies import create_dependency_tree

        dependencies = create_dependency_tree(context).all_dependencies(
            result.main_source_file)
        Utils.write_depfile(result.c_file, result.main_source_file,
                            dependencies)
    return result


@dataclass
class CompilationSource:
    source_desc: FileSourceDescriptor
    full_module_name: EncodedString
    cwd: str


@dataclass
class CompilationResult:
    main_source_file: str | None = None
    compilation_source: CompilationSource | None = None
    embedded_metadata: bool = False
    num_errors: int = 0
    c_file: Path | None = None
    h_file: Path | None = None
    i_file: Path | None = None
    api_file: Path | None = None
    listing_file: Path | None = None
    object_file: Path | None = None
    extension_file: Path | None = None


@dataclass
class CompilationResultSet(dict):
    num_errors = 0

    def add(self, source: str, result: CompilationResult) -> None:
        self[source] = result
        self.num_errors += result.num_errors


def compile_single(source: str,
                   options: CompilationOptions,
                   full_module_name=None) -> CompilationResult:
    return run_pipeline(source, options, full_module_name)


def compile_multiple(sources: list[str],
                     options: CompilationOptions) -> CompilationResultSet:
    if len(sources) > 1 and options.module_name:
        raise RuntimeError(
            "Full module name can only be set for single source compilation")
    sources = [os.path.abspath(source) for source in sources]
    processed = set()
    results = CompilationResultSet()
    timestamps = options.timestamps
    verbose = options.verbose
    context = None
    cwd = os.getcwd()
    for source in sources:
        if source not in processed:
            if context is None:
                context = Context.from_options(options)
            output_filename = get_output_filename(source, cwd, options)
            out_of_date = context.c_file_out_of_date(source, output_filename)
            if (not timestamps) or out_of_date:
                if verbose:
                    sys.stderr.write(f"Compiling {source}\n")
                result = run_pipeline(source,
                                      options,
                                      full_module_name=options.module_name,
                                      context=context)
                results.add(source, result)
                context = None
            processed.add(source)
    return results


def compile(
    source: str | list[str],
    options: CompilationOptions,
    full_module_name=None,
    **kwds,
) -> CompilationResult | CompilationResultSet:
    options = CompilationOptions(defaults=options, **kwds)
    if isinstance(source, str):
        if not options.timestamps:
            return compile_single(source, options, full_module_name)
        source = [source]
    return compile_multiple(source, options)


@Utils.cached_function
def search_include_directories(
    dirs: list[str],
    qualified_name: str,
    suffix: str,
    pos: tuple,
    include: bool,
    source_file_path: str,
) -> str | None:
    if pos and not source_file_path:
        file_desc = pos[0]
        if not isinstance(file_desc, FileSourceDescriptor):
            raise RuntimeError("Only file sources for code supported")
        source_file_path = file_desc.filename
    if source_file_path:
        if include:
            dirs = (os.path.dirname(source_file_path), ) + dirs
        else:
            dirs = (Utils.find_root_package_dir(source_file_path), ) + dirs
    dotted_filename = qualified_name
    if suffix:
        dotted_filename += suffix
    for dirname in dirs:
        path = os.path.join(dirname, dotted_filename)
        if os.path.exists(path):
            return path
    if not include:
        names = qualified_name.split(".")
        package_names = tuple(names[:-1])
        module_name = names[-1]
        namespace_dirs = []
        for dirname in dirs:
            package_dir, is_namespace = Utils.check_package_dir(
                dirname, package_names)
            if package_dir is not None:
                if is_namespace:
                    namespace_dirs.append(package_dir)
                    continue
                path = search_module_in_dir(package_dir, module_name, suffix)
                if path:
                    return path
        for package_dir in namespace_dirs:
            path = search_module_in_dir(package_dir, module_name, suffix)
            if path:
                return path
    return None


#


@Utils.cached_function
def search_module_in_dir(package_dir: str, module_name: str,
                         suffix: str) -> str | None:
    path = Utils.find_versioned_file(package_dir, module_name, suffix)
    if not path and suffix:
        path = Utils.find_versioned_file(
            os.path.join(package_dir, module_name), "__init__", suffix)
    return str(path) if path else None


def setuptools_main() -> None:
    return main(command_line=1)

def safe_print(message: str, file: IO[str] = sys.stderr) -> None:
    print(message, file=file)

def main(command_line=0) -> None:
    args = sys.argv[1:]
    any_failures = 0
    if command_line:
        try:
            from Cython.Compiler import CmdLine
            options, sources = CmdLine.parse_command_line(args)
        except OSError as e:
            import errno

            if e.errno != errno.ENOENT:
                raise
            safe_print(
                f"{sys.argv[0]}: No such file or directory: '{e.filename}'",
                file=sys.stderr)
            sys.exit(1)
    else:
        options = CompilationOptions(**default_options)
        sources = args
    if options.show_version:
        Utils.print_version()
    if options.working_path != "":
        os.chdir(options.working_path)
    try:
        result = compile(sources, options)
        if result.num_errors > 0:
            any_failures = 1
    except (OSError, PyrexError) as e:
        sys.stderr.write(str(e) + "\n")
        any_failures = 1
    if any_failures:
        sys.exit(1)


def _build(args):
    parsed = _parse_args(args)
    if parsed is None:
        raise ValueError(f"No parseable arguments found: {args}")

    dump_config()
    input_file, cy_args, remaining = parsed
    _debug("Input file: %s", input_file)
    _debug("Cython args: %s", cy_args)
    _debug("Remaining args: %s", remaining)
    program_name = build(input_file, cy_args)
    return program_name, remaining


def _main():
    args = sys.argv[1:]
    dump_config()
    _build(args)


if __name__ == "__main__":
    _main()

```

```python
from __future__ import annotations

import os
import re
import sys
from dataclasses import dataclass
from dataclasses import field as Field
from pathlib import Path
import sysconfig
from typing import IO
from typing_extensions import TypedDict, Unpack





# --- Original Imports ---
import contextlib

from Cython import Utils

from Cython.Compiler.Errors import CompileError, PyrexError, error, warning
from Cython.Compiler import Directives
from Cython.Compiler.Lexicon import (
    unicode_continuation_ch_any,
    unicode_continuation_ch_range,
    unicode_start_ch_any,
    unicode_start_ch_range,
)
from Cython.Compiler.Scanning import FileSourceDescriptor, PyrexScanner
from Cython.Compiler.StringEncoding import EncodedString
from Cython.Compiler.Symtab import BuiltinScope, ModuleScope

DEBUG = True


def _make_range_re(chrs):
    out = []
    for i in range(0, len(chrs), 2):
        out.append(f"{chrs[i]}-{chrs[i + 1]}")
    return "".join(out)


module_name_pattern = "[{0}{1}][{0}{2}{1}{3}]*".format(
    unicode_start_ch_any,
    _make_range_re(unicode_start_ch_range),
    unicode_continuation_ch_any,
    _make_range_re(unicode_continuation_ch_range),
)
module_name_pattern = re.compile(
    f"{module_name_pattern}(\\.{module_name_pattern})*$")

standard_include_path = os.path.abspath(
    os.path.join(os.path.dirname(os.path.dirname(__file__)), "Includes"))


def find_python_library() -> str | None:
    """Return absolute path to the host CPython shared library.

    The search strategy is intentionally exhaustive because *uv*-managed
    virtual-envs on macOS/Homebrew often break the usual sysconfig hints.
    Logic adapted from ``mb.build`` so that both build helpers rely on the
    same robust implementation.
    """
    import ctypes.util
    import platform
    import subprocess

    def check_path(path: str | os.PathLike) -> str | None:
        p = Path(path)
        return str(p.resolve()) if p.exists() else None

    # 1. Direct hint from sysconfig (works on most Linux distros)
    lib_name = sysconfig.get_config_var("LDLIBRARY") or ""
    lib_dir = Path(sysconfig.get_config_var("LIBDIR") or "")
    if lib_name:
        lib = check_path(lib_dir / lib_name)
        if lib:
            return lib

    # 2. ctypes based lookup (cross-platform)
    found = ctypes.util.find_library(
        f"python{sys.version_info[0]}.{sys.version_info[1]}")
    if found:
        found_lib = check_path(found)
        if found_lib:
            return found_lib

    # 3. macOS: try `otool -L` and framework paths
    if sys.platform == "darwin":
        try:
            output = subprocess.check_output(["otool", "-L", sys.executable], text=True)
            for line in output.splitlines():
                if "libpython" in line:
                    lib = check_path(line.split()[0])
                    if lib:
                        return lib
        except Exception:
            pass  # otool not available or unexpected output
        # Homebrew installs keep the shared library either directly inside the
        # framework directory (…/Versions/<X.Y>/Python) **or** in the sibling
        # ``lib`` sub-directory (…/Versions/<X.Y>/lib/libpythonX.Y.dylib).  Try
        # both locations.
        version_dir = f"{sys.version_info.major}.{sys.version_info.minor}"
        # Determine framework root e.g. /opt/homebrew/opt/python@3.11/Frameworks/Python.framework
        framework_root = Path(sys.base_prefix).parents[1]  # strip .../Versions/<X.Y>
        # ❶ <framework>/Versions/<X.Y>/Python
        framework_lib = framework_root / "Versions" / version_dir / "Python"
        lib = check_path(framework_lib)
        if lib:
            return lib
        # ❷ <framework>/Versions/<X.Y>/lib/libpythonX.Y.dylib
        framework_lib_dylib = Path(sys.base_prefix) / "Python.framework/Versions" / version_dir / "lib" / f"libpython{version_dir}.dylib"
        lib = check_path(framework_lib_dylib)
        if lib:
            return lib

    # 4. Linux: parse `ldd` on the running interpreter
    if sys.platform.startswith("linux"):
        try:
            output = subprocess.check_output(["ldd", sys.executable], text=True)
            for line in output.splitlines():
                if "libpython" in line:
                    lib = check_path(line.split()[0])
                    if lib:
                        return lib
        except Exception:
            pass

    # 5. Windows: common DLL locations
    if sys.platform == "win32":
        py_ver = platform.python_version_tuple()
        for candidate in (
            f"C:\\Windows\\System32\\python{py_ver[0]}{py_ver[1]}.dll",
            f"C:\\Windows\\SysWOW64\\python{py_ver[0]}{py_ver[1]}.dll",
        ):
            lib = check_path(candidate)
            if lib:
                return lib

    # 6. Fallback: scan common lib directories
    common_dirs = [
        Path(getattr(sys, "base_prefix", sys.prefix)) / "lib",
        Path(sys.prefix) / "lib",
        Path("/usr/lib"),
        Path("/usr/local/lib"),
        Path("/opt/homebrew/lib"),
    ]
    for d in common_dirs:
        lib = check_path(d / lib_name)
        if lib:
            return lib

    return None


def validate_path(path: str) -> str:
    return path if path and Path(path).exists() else ""


def get_config_var_wrapper(name, default=""):
    val = sysconfig.get_config_vars().get(name)
    return val if val is not None else default


def get_config_vars_dict():
    base_prefix = getattr(sys, "base_prefix", sys.prefix)
    cfg = {}
    # Use base_prefix for include and library directories:
    cfg["INCDIR"] = validate_path(
        os.path.join(
            base_prefix, "include",
            f"python{sys.version_info.major}.{sys.version_info.minor}"), )
    cfg["LIBDIR1"] = validate_path(os.path.join(base_prefix, "lib"))
    cfg["LIBDIR2"] = validate_path(
        os.path.join(
            base_prefix,
            "lib",
            f"python{sys.version_info.major}.{sys.version_info.minor}",
            f"config-{sys.platform}",
        ), )
    # Get PYLIB and PYLIB_DYN from sysconfig (they might still be filenames)
    cfg["PYLIB"] = get_config_var_wrapper("LIBRARY")
    cfg["PYLIB_DYN"] = get_config_var_wrapper("LDLIBRARY")
    # Use environment or defaults for the rest:
    cfg["CC"] = os.environ.get("CC", get_config_var_wrapper("CC"))
    cfg["CFLAGS"] = (get_config_var_wrapper("CFLAGS") + " " +
                     os.environ.get("CFLAGS", "")).strip()
    cfg["LINKCC"] = os.environ.get("LINKCC",
                                   get_config_var_wrapper("LINKCC", cfg["CC"]))
    cfg["LIBS"] = get_config_var_wrapper("LIBS")
    cfg["SYSLIBS"] = get_config_var_wrapper("SYSLIBS")
    cfg["LINKFORSHARED"] = get_config_var_wrapper("LINKFORSHARED")
    cfg["EXE_EXT"] = get_config_var_wrapper("EXE")
    return cfg


CONFIG = get_config_vars_dict()

INCDIR = CONFIG["INCDIR"]
LIBDIR1 = CONFIG["LIBDIR1"]
LIBDIR2 = CONFIG["LIBDIR2"]
PYLIB = CONFIG["PYLIB"]
PYLIB_DYN = find_python_library() or CONFIG["PYLIB_DYN"]
CC = CONFIG["CC"]
CFLAGS = CONFIG["CFLAGS"]
LINKCC = CONFIG["LINKCC"]
LIBS = CONFIG["LIBS"]
SYSLIBS = CONFIG["SYSLIBS"]
LINKFORSHARED = CONFIG["LINKFORSHARED"]
EXE_EXT = CONFIG["EXE_EXT"]

if not INCDIR:
    raise FileNotFoundError("Python include directory not found.")
if not (LIBDIR1 or LIBDIR2):
    raise FileNotFoundError("Python library directory not found.")
if not PYLIB_DYN:
    raise FileNotFoundError("Python shared library (libpythonX.Y) not found.")


def resolve_mac_executable_path(libpath: str) -> str:
    if libpath.startswith("@executable_path"):
        exe_dir = Path(sys.executable).resolve().parent
        relative_part = libpath.replace("@executable_path/", "")
        resolved = (exe_dir / relative_part).resolve()
        if not resolved.exists():
            raise FileNotFoundError(
                f"Resolved path '{resolved}' does not exist for '{libpath}'.")
        return str(resolved)
    return libpath


def _debug(msg, *args):
    if DEBUG:
        sys.stderr.write((msg % args) + "\n")


def find_all_libpython_paths() -> list:
    candidate_dirs = [
        Path(getattr(sys, "base_prefix", sys.prefix)) / "lib",
        Path(sys.prefix) / "lib",
        Path("/usr/lib"),
        Path("/usr/local/lib"),
        Path("/opt/homebrew/lib"),
    ]
    found_paths = set()
    patterns = [
        f"libpython{sys.version_info.major}.{sys.version_info.minor}*.dylib",
        f"libpython{sys.version_info.major}.{sys.version_info.minor}*.so",
    ]
    for base in candidate_dirs:
        if base.exists():
            for pattern in patterns:
                for lib in base.rglob(pattern):
                    try:
                        if lib.exists():
                            found_paths.add(lib.resolve())
                    except Exception:
                        if DEBUG:
                            pass
    return sorted(found_paths)


def dump_config() -> None:
    _debug("Dumping configuration:")
    for key, value in CONFIG.items():
        _debug("  %s: %s", key, value)
    _debug("Resolved PYLIB_DYN: %s", PYLIB_DYN)
    _debug("")
    libpython_paths = find_all_libpython_paths()
    if libpython_paths:
        _debug("Found dynamic library paths:")
        for p in libpython_paths:
            _debug("  %s", p)
    else:
        _debug("No dynamic library paths found.")


def _parse_args(args):
    cy_args = []
    last_arg = None
    for i, arg in enumerate(args):
        if arg.startswith("-") or last_arg in ("-X", "--directive"):
            cy_args.append(arg)
        else:
            input_file = arg
            remaining = args[i + 1:]
            return input_file, cy_args, remaining
        last_arg = arg
    return None


def runcmd(cmd, shell=False):
    """Run a shell command safely."""
    import subprocess

    cmd_str = " ".join(cmd) if isinstance(cmd, list) else cmd
    _debug(f"🔥 Running: {cmd_str}")

    try:
        result = subprocess.run(
            cmd,
            shell=shell,
            capture_output=True,
            text=True,
            check=False
        )

        if result.stdout:
            safe_print(result.stdout, end="")

        if result.returncode != 0:
            _debug(f"🚨 ERROR: Command failed with exit code {result.returncode}")
            if result.stderr:
                _debug(f"❌ STDERR:\n{result.stderr}")
            sys.exit(result.returncode)

        return result.stdout.strip() if result.stdout else ""
    except Exception as e:
        _debug(f"🚨 ERROR: Failed to run command: {e}")
        sys.exit(1)


def compile_shared(
    cpp_path: Path,
    *,
    install_dir: Path | None = None,
    lib_dir: Path | None = None,
    force: bool = False,
) -> int:
    """Compile *cpp_path* into a shared library (.so/.dylib/.pyd).

    Mirrors the original helper in ``mb.build`` so that both call sites use a
    single implementation. The output path preserves the package directory
    layout when *install_dir*/*lib_dir* are supplied, matching the previous
    behaviour.

    Note: cpp_path can be either a .py file (will look for corresponding .cpp)
    or a .cpp file directly.
    """
    include_dir = Path(sysconfig.get_paths()["include"])
    from mbcore.log import error
    python_lib = Path(find_python_library() or "")
    if not python_lib.exists():
        error("⚠️ Could not locate libpython; aborting shared compilation")
        return 1

    # Handle case where we're passed a .py file instead of .cpp
    actual_cpp_path = cpp_path
    if cpp_path.suffix == ".py":
        # Look for corresponding .cpp file in the same directory
        potential_cpp = cpp_path.with_suffix(".cpp")
        if potential_cpp.exists():
            actual_cpp_path = potential_cpp
        else:
            error(f"⚠️ No corresponding .cpp file found for {cpp_path}")
            return 1

    ext_suffix = sysconfig.get_config_var("EXT_SUFFIX") or ".so"

    if install_dir and lib_dir:
        # Use original cpp_path for relative path calculation
        output_so = Path(lib_dir) / cpp_path.relative_to(install_dir).with_suffix(ext_suffix)
    else:
        output_so = cpp_path.with_suffix(ext_suffix)

    output_so.parent.mkdir(parents=True, exist_ok=True)

    # Skip up-to-date files unless forced
    if (
        output_so.exists()
        and actual_cpp_path.stat().st_mtime <= output_so.stat().st_mtime
        and not force
    ):
        _debug("[SKIP] %s is up-to-date", output_so)
        return 0

    if sys.platform == "darwin":
        compiler = "clang++"
        lib_path = python_lib
        lib_dir_path = lib_path.parent
        # For framework Python, link directly to the framework binary
        cmd = [
            compiler,
            "-shared",
            "-o",
            str(output_so),
            str(actual_cpp_path),
            f"-I{include_dir}",
            str(lib_path),  # Link directly to the framework Python binary
            "-fPIC",
            f"-Wl,-rpath,{lib_dir_path}",
        ]
        runcmd(cmd)

        # Fix install_name on macOS so the library uses an absolute path
        try:
            fix_cmd = [
                "install_name_tool",
                "-change",
                "/install/lib/libpython3.12.dylib",
                str(lib_path),
                str(output_so),
            ]
            runcmd(fix_cmd)
        except Exception:
            # Non-fatal; continue
            _debug("install_name_tool failed – continuing")
            pass
    else:
        compiler = "g++"
        cmd = [
            compiler,
            "-shared",
            "-o",
            str(output_so),
            str(actual_cpp_path),
            f"-I{include_dir}",
            f"-L{python_lib.parent}",
            f"-l{python_lib.stem.replace('lib', '')}",
            "-fPIC",
        ]
        runcmd(cmd)

    return 0


def clink(basename) -> None:
    link_args = [LINKCC, "-o", basename + EXE_EXT, basename + ".o"]

    if LIBDIR1:
        link_args.append("-L" + LIBDIR1)
    if LIBDIR2:
        link_args.append("-L" + LIBDIR2)

    if PYLIB_DYN:
        link_args.append(
            PYLIB_DYN)  # Explicitly add the Python dynamic library
    else:
        _debug("⚠️ WARNING: PYLIB_DYN is missing!")

    if LINKFORSHARED:
        link_args.extend(LINKFORSHARED.split())
    if LIBS:
        link_args.extend(LIBS.split())
    if SYSLIBS:
        link_args.extend(SYSLIBS.split())

    _debug("Final link command: %s", " ".join(link_args))
    runcmd(link_args)


def ccompile(basename) -> None:
    # Determine whether the generated file is C++ (.cpp) or C (.c)
    cpp_file = Path(basename + ".cpp")
    c_file = Path(basename + ".c")
    if cpp_file.exists():
        source_file = str(cpp_file)
        compiler = "clang++"  # Use clang++ for C++ sources
    elif c_file.exists():
        source_file = str(c_file)
        compiler = CC  # Use your configured C compiler
    else:
        raise FileNotFoundError(
            f"Neither {basename + '.cpp'} nor {basename + '.c'} exists.")
    # Compile the source file into an object file.
    cmd = [compiler, "-c", "-o", basename + ".o", source_file, "-I" + INCDIR
           ] + CFLAGS.split()
    _debug("ccompile cmd: %s", " ".join(cmd))
    runcmd(cmd)


def cycompile(input_file, options=()) -> None:
    from Cython.Compiler import CmdLine, Main, Version

    options, sources = CmdLine.parse_command_line(
        list(options) + ["--embed", input_file])
    _debug("Using Cython %s to compile %s", Version.version, input_file)
    result = Main.compile(sources, options)
    if result.num_errors > 0:
        sys.exit(1)


def exec_file(program_name, args=()) -> None:
    runcmd([str(Path(program_name).resolve())] + list(args), shell=False)


def build(input_file, compiler_args=(), force=False):
    basename = os.path.splitext(input_file)[0]
    exe_file = basename + EXE_EXT
    if not force and os.path.abspath(exe_file) == os.path.abspath(input_file):
        raise ValueError(
            "Input and output file names are the same, refusing to overwrite")
    if (not force and os.path.exists(exe_file) and os.path.exists(input_file)
            and os.path.getmtime(input_file) <= os.path.getmtime(exe_file)):
        _debug("File is up to date, not regenerating %s", exe_file)
        return exe_file
    cycompile(input_file, compiler_args)
    ccompile(basename)
    clink(basename)
    return exe_file


class CompilerDerecitves(TypedDict, total=False):
    binding: bool
    embedsignature: bool
    c_string_type: str
    c_string_encoding: str
    c_string_type_encoding: str
    c_string_encoding_errors: str
    c_string_type_errors: str


class CompilationOptionsKwargs(TypedDict, total=False):
    show_version: int
    use_listing_file: int
    errors_to_stderr: int
    cplus: int
    output_file: str | None
    depfile: str | None
    annotate: str | None
    annotate_coverage_xml: str | None
    generate_pxi: int
    capi_reexport_cincludes: int
    working_path: str
    timestamps: dict | None
    verbose: int
    quiet: int
    compiler_directives: CompilerDerecitves
    embedded_metadata: dict
    evaluate_tree_assertions: bool
    emit_linenums: bool
    relative_path_in_code_position_comments: bool
    c_line_in_traceback: bool
    language_level: int | None
    formal_grammar: bool
    gdb_debug: bool
    compile_time_env: dict | None
    module_name: str | None
    common_utility_include_dir: str | None
    output_dir: str | None
    build_dir: str | None
    cache: str | None
    create_extension: bool | None
    np_pythran: bool
    legacy_implicit_noexcept: bool | None
    shared_utility_qualified_name: str | None


@dataclass
class CompilationOptions(dict):
    show_version: int = Field()
    use_listing_file: int = Field()
    errors_to_stderr: int = Field()
    cplus: int = Field()
    output_file: str | None = Field()
    depfile: str | None = Field()
    annotate: str | None = Field()
    annotate_coverage_xml: str | None = Field()
    generate_pxi: int = Field()
    capi_reexport_cincludes: int = Field()
    working_path: str = Field()
    timestamps: dict | None = Field()
    verbose: int = Field()
    quiet: int = Field()
    compiler_directives: CompilerDerecitves = Field()
    embedded_metadata: dict = Field()
    evaluate_tree_assertions: bool = Field()
    emit_linenums: bool = Field()
    relative_path_in_code_position_comments: bool = Field()
    c_line_in_traceback: bool = Field()
    language_level: int | None = Field()
    formal_grammar: bool = Field()
    gdb_debug: bool = Field()
    compile_time_env: dict | None = Field()
    module_name: str | None = Field()
    shared_utility_qualified_name: str | None = Field()
    common_utility_include_dir: str | None = Field()
    output_dir: str | None = Field()
    build_dir: str | None
    cache: str | None = Field()
    create_extension: bool | None = Field()
    np_pythran: bool
    legacy_implicit_noexcept: bool | None = Field()

    def __init__(self,
                 **kw: Unpack[CompilationOptionsKwargs]):
        self.include_path = []


        # let's assume 'default_options' contains a value for most known compiler options
        # and validate against them
        options = self
        unknown_options = set(kw) - set(default_options)
        # ignore valid options that are not in the defaults
        unknown_options.difference_update(["include_path"])
        if unknown_options:
            message = "got unknown compilation option{}, please remove: {}".format(
                "s" if len(unknown_options) > 1 else "",
                ", ".join(unknown_options),
            )
            raise ValueError(message)

        directive_defaults = Directives.DIRECTIVE_DEFAULTS
        directives = dict(options["compiler_directives"])  # copy mutable field
        # check for invalid directives
        unknown_directives = set(directives) - set(directive_defaults)
        if unknown_directives:
            message = "got unknown compiler directive{}: {}".format(
                "s" if len(unknown_directives) > 1 else "",
                ", ".join(unknown_directives),
            )
            raise ValueError(message)
        options["compiler_directives"] = directives
        if directives.get("np_pythran", False) and not options["cplus"]:
            import warnings

            warnings.warn("C++ mode forced when in Pythran mode!",
                          stacklevel=2)
            options["cplus"] = True
        if "language_level" not in kw and directives.get("language_level"):
            options["language_level"] = directives["language_level"]
        elif not options.get("language_level"):
            options["language_level"] = directive_defaults.get(
                "language_level")
        if "formal_grammar" in directives and "formal_grammar" not in kw:
            options["formal_grammar"] = directives["formal_grammar"]
        if options["cache"] is True:
            options["cache"] = os.path.join(Utils.get_cython_cache_dir(),
                                            "compiler")

        self.__dict__.update(options)

    def configure_language_defaults(self, source_extension: str) -> None:
        if source_extension == "py" and self.compiler_directives.get(
                "binding") is None:
            self.compiler_directives["binding"] = True

    def get_fingerprint(self):
        """Return a string that contains all the options that are relevant for cache invalidation."""
        # Collect only the data that can affect the generated file(s).
        data = {}

        for key, value in self.__dict__.items():
            if key in ["show_version", "errors_to_stderr", "verbose", "quiet"]:
                # verbosity flags have no influence on the compilation result
                continue
            if key in ["output_file", "output_dir"]:
                # ignore the exact name of the output file
                continue
            if key in ["depfile"]:
                # external build system dependency tracking file does not influence outputs
                continue
            if key in ["timestamps"]:
                # the cache cares about the content of files, not about the timestamps of sources
                continue
            if key in ["cache"]:
                # hopefully caching has no influence on the compilation result
                continue
            if key in ["compiler_directives"]:
                # directives passed on to the C compiler do not influence the generated C code
                continue
            if key in ["include_path"]:
                # this path changes which headers are tracked as dependencies,
                # it has no influence on the generated C code
                continue
            if key in ["working_path"]:
                # this path changes where modules and pxd files are found;
                # their content is part of the fingerprint anyway, their
                # absolute path does not matter
                continue
            if key in ["create_extension"]:
                # create_extension() has already mangled the options, e.g.,
                # embedded_metadata, when the fingerprint is computed so we
                # ignore it here.
                continue
            if key in ["build_dir"]:
                # the (temporary) directory where we collect dependencies
                # has no influence on the C output
                continue
            if key in [
                    "use_listing_file", "generate_pxi", "annotate",
                    "annotate_coverage_xml"
            ]:
                # all output files are contained in the cache so the types of
                # files generated must be part of the fingerprint
                data[key] = value
            elif key in ["formal_grammar", "evaluate_tree_assertions"]:
                # these bits can change whether compilation to C passes/fails
                data[key] = value
            elif key in [
                    "embedded_metadata",
                    "emit_linenums",
                    "c_line_in_traceback",
                    "gdb_debug",
                    "relative_path_in_code_position_comments",
            ]:
                # the generated code contains additional bits when these are set
                data[key] = value
            elif key in [
                    "cplus", "language_level", "compile_time_env", "np_pythran"
            ]:
                # assorted bits that, e.g., influence the parser
                data[key] = value
            elif key == ["capi_reexport_cincludes"]:
                if self.capi_reexport_cincludes:
                    # our caching implementation does not yet include fingerprints of all the header files
                    raise NotImplementedError(
                        "capi_reexport_cincludes is not compatible with Cython caching"
                    )
            elif key == ["common_utility_include_dir"]:
                if self.common_utility_include_dir:
                    raise NotImplementedError(
                        "common_utility_include_dir is not compatible with Cython caching yet"
                    )
            else:
                # any unexpected option should go into the fingerprint; it's better
                # to recompile than to return incorrect results from the cache.
                data[key] = value

        def to_fingerprint(item):
            """Recursively turn item into a string, turning dicts into lists with deterministic ordering."""
            if isinstance(item, dict):
                item = sorted([(repr(key), to_fingerprint(value))
                               for key, value in item.items()])
            return repr(item)

        return to_fingerprint(data)


# ------------------------------------------------------------------------
#
#  Set the default options depending on the platform
#
# ------------------------------------------------------------------------

default_options: CompilationOptionsKwargs = {
    "show_version": 0,
    "use_listing_file": 0,
    "errors_to_stderr": 1,
    "cplus": 0,
    "output_file": None,
    "depfile": None,
    "annotate": None,
    "annotate_coverage_xml": None,
    "generate_pxi": 0,
    "capi_reexport_cincludes": 0,
    "working_path": "",
    "timestamps": None,
    "verbose": 0,
    "quiet": 0,
    "compiler_directives": {},
    "embedded_metadata": {},
    "evaluate_tree_assertions": False,
    "emit_linenums": False,
    "relative_path_in_code_position_comments": True,
    "c_line_in_traceback": True,
    "language_level": None,  # warn but default to 2
    "formal_grammar": False,
    "gdb_debug": False,
    "compile_time_env": None,
    "module_name": None,
    "shared_utility_qualified_name": None,
    "common_utility_include_dir": None,
    "output_dir": None,
    "build_dir": None,
    "cache": None,
    "create_extension": None,
    "np_pythran": False,
    "legacy_implicit_noexcept": None,
}


@dataclass
class Context:
    cython_scope: ModuleScope | None = None
    language_level: int | None = None
    future_directives: set = Field(default_factory=set)
    compiler_directives: dict = Field(default_factory=dict)
    include_directories: list = Field(default_factory=list)
    cpp: bool = False
    options: CompilationOptions | None = Field(default=None)
    modules: dict[str,
                  BuiltinScope | CythonScope.CythonScope] = Field(default_factory=dict)  # noqa: F821
    pxds: dict = Field(default_factory=dict)
    _interned: dict = Field(default_factory=dict)
    legacy_implicit_noexcept: bool = False
    gdb_debug_outputwriter: object | None = None

    def __init__(self,
                 include_directories,
                 compiler_directives,
                 cpp=False,
                 language_level=None,
                 options=None):
        from Cython.Compiler import Builtin, CythonScope

        self.modules = {
            "__builtin__": Builtin.builtin_scope
        }
        self.cython_scope = CythonScope.create_cython_scope(self)
        self.modules["cython"] = self.cython_scope
        self.include_directories = include_directories
        self.future_directives = set()
        self.compiler_directives = compiler_directives
        self.cpp = cpp
        self.options = options
        self.pxds = {}
        self._interned = {}
        if language_level is not None:
            self.set_language_level(language_level)
        self.legacy_implicit_noexcept = self.compiler_directives.get(
            "legacy_implicit_noexcept", False)
        self.gdb_debug_outputwriter = None

    @classmethod
    def from_options(cls, options: CompilationOptions):
        return cls(
            options.include_path,
            options.compiler_directives,
            bool(options.cplus),
            options.language_level,
            options=options,
        )

    def set_language_level(self, level) -> None:
        from Cython.Compiler.Future import absolute_import, division, generator_stop, print_function, unicode_literals

        future_directives = set()
        if level == "3str":
            level = 3
        else:
            level = int(level)
            if level >= 3:
                future_directives.add(unicode_literals)
        if level >= 3:
            future_directives.update(
                [print_function, absolute_import, division, generator_stop])
        self.language_level = level
        self.future_directives = future_directives
        if level >= 3:
            self.modules["builtins"] = self.modules["__builtin__"]

    def intern_ustring(self, value, encoding=None) -> EncodedString:
        key = (EncodedString, value, encoding)
        try:
            return self._interned[key]
        except KeyError:
            pass
        value = EncodedString(value)
        if encoding:
            value.encoding = encoding
        self._interned[key] = value
        return value

    def process_pxd(self, source_desc: FileSourceDescriptor,
                    scope: ModuleScope, module_name: str) -> tuple:
        from Cython.Compiler import Pipeline

        if isinstance(
                source_desc,
                FileSourceDescriptor) and source_desc._file_type == "pyx":
            source = CompilationSource(source_desc, module_name, os.getcwd())
            result_sink = create_default_resultobj(source, self.options)
            pipeline = Pipeline.create_pyx_as_pxd_pipeline(self, result_sink)
            result = Pipeline.run_pipeline(pipeline, source)
        else:
            pipeline = Pipeline.create_pxd_pipeline(self, scope, module_name)
            result = Pipeline.run_pipeline(pipeline, source_desc)
        return result

    def nonfatal_error(self, exc):
        return Errors.report_error(exc)

    def _split_qualified_name(self, qualified_name, relative_import=False):
        qualified_name_parts = qualified_name.split(".")
        last_part = qualified_name_parts.pop()
        qualified_name_parts = [(p, True) for p in qualified_name_parts]
        if last_part != "__init__":
            is_package = False
            for suffix in (".py", ".pyx"):
                path = self.search_include_directories(
                    qualified_name,
                    suffix=suffix,
                    source_pos=None,
                    source_file_path=None,
                    sys_path=not relative_import,
                )
                if path:
                    is_package = self._is_init_file(path)
                    break
            qualified_name_parts.append((last_part, is_package))
        return qualified_name_parts

    @staticmethod
    def _is_init_file(path):
        return os.path.basename(path) in ("__init__.pyx", "__init__.py",
                                          "__init__.pxd") if path else False

    @staticmethod
    def _check_pxd_filename(pos, pxd_pathname, qualified_name) -> None:
        if not pxd_pathname:
            return
        pxd_filename = os.path.basename(pxd_pathname)
        if "." in qualified_name and qualified_name == os.path.splitext(
                pxd_filename)[0]:
            warning(
                pos,
                f"Dotted filenames ('{pxd_filename}') are deprecated. Please use the normal Python package directory layout.",
                level=1,
            )

    def find_module(
        self,
        module_name,
        from_module=None,
        pos=None,
        need_pxd=1,
        absolute_fallback=True,
        relative_import=False,
    ):
        debug_find_module = 0
        if debug_find_module:
            pass
        scope = None
        pxd_pathname = None
        if from_module:
            if module_name:
                qualified_name = from_module.qualify_name(module_name)
            else:
                qualified_name = from_module.qualified_name
                scope = from_module
                from_module = None
        else:
            qualified_name = module_name
        if not module_name_pattern.match(qualified_name):
            raise CompileError(pos or (module_name, 0, 0),
                               f"'{module_name}' is not a valid module name")
        if from_module:
            if debug_find_module:
                pass
            scope = from_module.lookup_submodule(module_name)
            if not scope:
                pxd_pathname = self.find_pxd_file(qualified_name,
                                                  pos,
                                                  sys_path=not relative_import)
                self._check_pxd_filename(pos, pxd_pathname, qualified_name)
                if pxd_pathname:
                    is_package = self._is_init_file(pxd_pathname)
                    scope = from_module.find_submodule(module_name,
                                                       as_package=is_package)
        if not scope:
            if debug_find_module:
                pass
            if absolute_fallback:
                qualified_name = module_name
            scope = self
            for name, is_package in self._split_qualified_name(
                    qualified_name, relative_import=relative_import):
                scope = scope.find_submodule(name, as_package=is_package)
        if debug_find_module:
            pass
        if not scope.pxd_file_loaded:
            if debug_find_module:
                pass
            if not pxd_pathname:
                if debug_find_module:
                    pass
                pxd_pathname = self.find_pxd_file(qualified_name,
                                                  pos,
                                                  sys_path=need_pxd
                                                  and not relative_import)
                self._check_pxd_filename(pos, pxd_pathname, qualified_name)
                if debug_find_module:
                    pass
                if not pxd_pathname and need_pxd:
                    scope.pxd_file_loaded = True
                    package_pathname = self.search_include_directories(
                        qualified_name,
                        suffix=".py",
                        source_pos=pos,
                        sys_path=not relative_import,
                    )
                    if package_pathname and package_pathname.endswith(
                            Utils.PACKAGE_FILES):
                        pass
                    else:
                        error(
                            pos, "'{}.pxd' not found".format(
                                qualified_name.replace(".", os.sep)))
            if pxd_pathname:
                scope.pxd_file_loaded = True
                try:
                    if debug_find_module:
                        pass
                    rel_path = module_name.replace(
                        ".", os.sep) + os.path.splitext(pxd_pathname)[1]
                    if not pxd_pathname.endswith(rel_path):
                        rel_path = pxd_pathname
                    source_desc = FileSourceDescriptor(pxd_pathname, rel_path)
                    err, result = self.process_pxd(source_desc, scope,
                                                   qualified_name)
                    if err:
                        raise err
                    (pxd_codenodes, pxd_scope) = result
                    self.pxds[module_name] = (pxd_codenodes, pxd_scope)
                except CompileError:
                    pass
        return scope

    def find_pxd_file(self,
                      qualified_name,
                      pos=None,
                      sys_path=True,
                      source_file_path=None):
        pxd = self.search_include_directories(
            qualified_name,
            suffix=".pxd",
            source_pos=pos,
            sys_path=sys_path,
            source_file_path=source_file_path,
        )
        if pxd is None and Directives.cimport_from_pyx:
            return self.find_pyx_file(qualified_name, pos, sys_path=sys_path)
        return pxd

    def find_pyx_file(self,
                      qualified_name,
                      pos=None,
                      sys_path=True,
                      source_file_path=None):
        return self.search_include_directories(
            qualified_name,
            suffix=".pyx",
            source_pos=pos,
            sys_path=sys_path,
            source_file_path=source_file_path,
        )

    def find_include_file(self, filename, pos=None, source_file_path=None):
        path = self.search_include_directories(
            filename,
            source_pos=pos,
            include=True,
            source_file_path=source_file_path,
        )
        if not path:
            error(pos, f"'{filename}' not found")
        return path

    def search_include_directories(
        self,
        qualified_name,
        suffix=None,
        source_pos=None,
        include=False,
        sys_path=False,
        source_file_path=None,
    ):
        include_dirs = self.include_directories
        if sys_path:
            include_dirs = include_dirs + sys.path
        include_dirs = tuple(include_dirs + [standard_include_path])
        return search_include_directories(
            include_dirs,
            qualified_name,
            suffix or "",
            source_pos,
            include,
            source_file_path,
        )

    def find_root_package_dir(self, file_path):
        return Utils.find_root_package_dir(file_path)

    def check_package_dir(self, dir, package_names):
        return Utils.check_package_dir(dir, tuple(package_names))

    def c_file_out_of_date(self, source_path, output_path) -> int:
        if not os.path.exists(output_path):
            return 1
        c_time = Utils.modification_time(output_path)
        if Utils.file_newer_than(source_path, c_time):
            return 1
        pxd_path = Utils.replace_suffix(source_path, ".pxd")
        if os.path.exists(pxd_path) and Utils.file_newer_than(
                pxd_path, c_time):
            return 1
        for kind, name in self.read_dependency_file(source_path):
            if kind == "cimport":
                dep_path = self.find_pxd_file(name,
                                              source_file_path=source_path)
            elif kind == "include":
                dep_path = self.search_include_directories(
                    name, source_file_path=source_path)
            else:
                continue
            if dep_path and Utils.file_newer_than(dep_path, c_time):
                return 1
        return 0

    def find_cimported_module_names(self, source_path):
        return [
            name for kind, name in self.read_dependency_file(source_path)
            if kind == "cimport"
        ]

    def is_package_dir(self, dir_path):
        return Utils.is_package_dir(dir_path)

    def read_dependency_file(self, source_path):
        dep_path = Utils.replace_suffix(source_path, ".dep")
        if os.path.exists(dep_path):
            with open(dep_path, encoding="utf-8") as f:
                return [
                    line.split(" ", 1) for line in (l.strip() for l in f)
                    if " " in line
                ]
        return ()

    def lookup_submodule(self, name):
        return self.modules.get(name, None)

    def find_submodule(self, name, as_package=False):
        scope = self.lookup_submodule(name)
        if not scope:
            scope = ModuleScope(name,
                                parent_module=None,
                                context=self,
                                is_package=as_package)
            self.modules[name] = scope
        return scope

    def parse(self, source_desc, scope, pxd, full_module_name):
        if not isinstance(source_desc, FileSourceDescriptor):
            raise RuntimeError("Only file sources for code supported")
        source_filename = source_desc.filename
        scope.cpp = self.cpp
        num_errors = Errors.get_errors_count()
        try:
            with Utils.open_source_file(source_filename) as f:
                from . import Parsing

                s = PyrexScanner(f,
                                 source_desc,
                                 source_encoding=f.encoding,
                                 scope=scope,
                                 context=self)
                tree = Parsing.p_module(s, pxd, full_module_name)
                if self.options.formal_grammar:
                    try:
                        from ..Parser import ConcreteSyntaxTree
                    except ImportError:
                        raise RuntimeError(
                            "Formal grammar can only be used with compiled Cython with an available pgen.",
                        )
                    ConcreteSyntaxTree.p_module(source_filename)
        except UnicodeDecodeError as e:
            raise self._report_decode_error(source_desc, e)
        if Errors.get_errors_count() > num_errors:
            raise CompileError()
        return tree

    def _report_decode_error(self, source_desc, exc):
        msg = exc.args[-1]
        position = exc.args[2]
        encoding = exc.args[0]
        line = 1
        column = idx = 0
        with open(source_desc.filename, encoding="iso8859-1", newline="") as f:
            for line, data in enumerate(f, 1):
                idx += len(data)
                if idx >= position:
                    column = position - (idx - len(data)) + 1
                    break
        return error(
            (source_desc, line, column),
            f"Decoding error, missing or incorrect coding=<encoding-name> at top of source (cannot decode with encoding {encoding!r}: {msg})",
        )

    def extract_module_name(self, path, options):
        dir, filename = os.path.split(path)
        module_name, _ = os.path.splitext(filename)
        if "." in module_name:
            return module_name
        names = [module_name]
        while self.is_package_dir(dir):
            parent, package_name = os.path.split(dir)
            if parent == dir:
                break
            names.append(package_name)
            dir = parent
        names.reverse()
        return ".".join(names)

    def setup_errors(self, options, result) -> None:
        Errors.init_thread()
        if options.use_listing_file:
            path = result.listing_file = Utils.replace_suffix(
                result.main_source_file, ".lis")
        else:
            path = None
        Errors.open_listing_file(path=path,
                                 echo_to_stderr=options.errors_to_stderr)

    def teardown_errors(self, err, options, result) -> None:
        source_desc = result.compilation_source.source_desc
        if not isinstance(source_desc, FileSourceDescriptor):
            raise RuntimeError("Only file sources for code supported")
        Errors.close_listing_file()
        result.num_errors = Errors.get_errors_count()
        if result.num_errors > 0:
            err = True
        if err and result.c_file:
            with contextlib.suppress(EnvironmentError):
                Utils.castrate_file(result.c_file,
                                    os.stat(source_desc.filename))
            result.c_file = None


def get_output_filename(source_filename: str, cwd: str,
                        options: CompilationOptions) -> str:
    c_suffix = ".cpp" if options.cplus else ".c"
    suggested_file_name = Utils.replace_suffix(source_filename, c_suffix)
    if options.output_file:
        out_path = os.path.join(cwd, options.output_file)
        if os.path.isdir(out_path):
            return os.path.join(out_path,
                                os.path.basename(suggested_file_name))
        return out_path
    return suggested_file_name


def create_default_resultobj(compilation_source: CompilationSource,
                             options: CompilationOptions):
    result = CompilationResult()
    result.main_source_file = compilation_source.source_desc.filename
    result.compilation_source = compilation_source
    source_desc = compilation_source.source_desc
    result.c_file = get_output_filename(source_desc.filename,
                                        compilation_source.cwd, options)
    result.embedded_metadata = options.embedded_metadata
    return result


def run_pipeline(source: str,
                 options: CompilationOptions,
                 full_module_name=None,
                 context=None) -> CompilationResult:
    from Cython.Compiler import Pipeline

    source_ext = os.path.splitext(source)[1]
    options.configure_language_defaults(source_ext[1:])
    if context is None:
        context = Context.from_options(options)
    cwd = os.getcwd()
    abs_path = os.path.abspath(source)
    full_module_name = full_module_name or context.extract_module_name(
        source, options)
    full_module_name = EncodedString(full_module_name)
    Utils.raise_error_if_module_name_forbidden(full_module_name)
    if options.relative_path_in_code_position_comments:
        rel_path = full_module_name.replace(".", os.sep) + source_ext
        if not abs_path.endswith(rel_path):
            rel_path = source
    else:
        rel_path = abs_path
    source_desc = FileSourceDescriptor(abs_path, rel_path)
    compilation_source = CompilationSource(source_desc, full_module_name, cwd)
    result = create_default_resultobj(compilation_source, options)
    if options.annotate is None:
        html_filename = result.c_file.with_suffix(".html")
        if os.path.exists(html_filename):
            with open(html_filename, encoding="UTF-8") as html_file:
                if "<!-- Generated by Cython" in html_file.read(100):
                    options.annotate = True
    if source_ext.lower() == ".py" or not source_ext:
        pipeline = Pipeline.create_py_pipeline(context, options, result)
    else:
        pipeline = Pipeline.create_pyx_pipeline(context, options, result)
    context.setup_errors(options, result)
    if "." in full_module_name and "." in os.path.splitext(
            os.path.basename(abs_path))[0]:
        warning(
            (source_desc, 1, 0),
            f"Dotted filenames ('{os.path.basename(abs_path)}') are deprecated. Please use the normal Python package directory layout.",
            level=1,
        )
    err, enddata = Pipeline.run_pipeline(pipeline, source)
    context.teardown_errors(err, options, result)
    if err is None and options.depfile:
        from Cython.Build.Dependencies import create_dependency_tree

        dependencies = create_dependency_tree(context).all_dependencies(
            result.main_source_file)
        Utils.write_depfile(result.c_file, result.main_source_file,
                            dependencies)
    return result


@dataclass
class CompilationSource:
    source_desc: FileSourceDescriptor
    full_module_name: EncodedString
    cwd: str


@dataclass
class CompilationResult:
    main_source_file: str | None = None
    compilation_source: CompilationSource | None = None
    embedded_metadata: bool = False
    num_errors: int = 0
    c_file: Path | None = None
    h_file: Path | None = None
    i_file: Path | None = None
    api_file: Path | None = None
    listing_file: Path | None = None
    object_file: Path | None = None
    extension_file: Path | None = None


@dataclass
class CompilationResultSet(dict):
    num_errors = 0

    def add(self, source: str, result: CompilationResult) -> None:
        self[source] = result
        self.num_errors += result.num_errors


def compile_single(source: str,
                   options: CompilationOptions,
                   full_module_name=None) -> CompilationResult:
    return run_pipeline(source, options, full_module_name)


def compile_multiple(sources: list[str],
                     options: CompilationOptions) -> CompilationResultSet:
    if len(sources) > 1 and options.module_name:
        raise RuntimeError(
            "Full module name can only be set for single source compilation")
    sources = [os.path.abspath(source) for source in sources]
    processed = set()
    results = CompilationResultSet()
    timestamps = options.timestamps
    verbose = options.verbose
    context = None
    cwd = os.getcwd()
    for source in sources:
        if source not in processed:
            if context is None:
                context = Context.from_options(options)
            output_filename = get_output_filename(source, cwd, options)
            out_of_date = context.c_file_out_of_date(source, output_filename)
            if (not timestamps) or out_of_date:
                if verbose:
                    sys.stderr.write(f"Compiling {source}\n")
                result = run_pipeline(source,
                                      options,
                                      full_module_name=options.module_name,
                                      context=context)
                results.add(source, result)
                context = None
            processed.add(source)
    return results


def compile(
    source: str | list[str],
    options: CompilationOptions,
    full_module_name=None,
    **kwds,
) -> CompilationResult | CompilationResultSet:
    options = CompilationOptions(defaults=options, **kwds)
    if isinstance(source, str):
        if not options.timestamps:
            return compile_single(source, options, full_module_name)
        source = [source]
    return compile_multiple(source, options)


@Utils.cached_function
def search_include_directories(
    dirs: list[str],
    qualified_name: str,
    suffix: str,
    pos: tuple,
    include: bool,
    source_file_path: str,
) -> str | None:
    if pos and not source_file_path:
        file_desc = pos[0]
        if not isinstance(file_desc, FileSourceDescriptor):
            raise RuntimeError("Only file sources for code supported")
        source_file_path = file_desc.filename
    if source_file_path:
        if include:
            dirs = (os.path.dirname(source_file_path), ) + dirs
        else:
            dirs = (Utils.find_root_package_dir(source_file_path), ) + dirs
    dotted_filename = qualified_name
    if suffix:
        dotted_filename += suffix
    for dirname in dirs:
        path = os.path.join(dirname, dotted_filename)
        if os.path.exists(path):
            return path
    if not include:
        names = qualified_name.split(".")
        package_names = tuple(names[:-1])
        module_name = names[-1]
        namespace_dirs = []
        for dirname in dirs:
            package_dir, is_namespace = Utils.check_package_dir(
                dirname, package_names)
            if package_dir is not None:
                if is_namespace:
                    namespace_dirs.append(package_dir)
                    continue
                path = search_module_in_dir(package_dir, module_name, suffix)
                if path:
                    return path
        for package_dir in namespace_dirs:
            path = search_module_in_dir(package_dir, module_name, suffix)
            if path:
                return path
    return None


#


@Utils.cached_function
def search_module_in_dir(package_dir: str, module_name: str,
                         suffix: str) -> str | None:
    path = Utils.find_versioned_file(package_dir, module_name, suffix)
    if not path and suffix:
        path = Utils.find_versioned_file(
            os.path.join(package_dir, module_name), "__init__", suffix)
    return str(path) if path else None


def setuptools_main() -> None:
    return main(command_line=1)

def safe_print(message: str, file: IO[str] = sys.stderr) -> None:
    print(message, file=file)

def main(command_line=0) -> None:
    args = sys.argv[1:]
    any_failures = 0
    if command_line:
        try:
            from Cython.Compiler import CmdLine
            options, sources = CmdLine.parse_command_line(args)
        except OSError as e:
            import errno

            if e.errno != errno.ENOENT:
                raise
            safe_print(
                f"{sys.argv[0]}: No such file or directory: '{e.filename}'",
                file=sys.stderr)
            sys.exit(1)
    else:
        options = CompilationOptions(**default_options)
        sources = args
    if options.show_version:
        Utils.print_version()
    if options.working_path != "":
        os.chdir(options.working_path)
    try:
        result = compile(sources, options)
        if result.num_errors > 0:
            any_failures = 1
    except (OSError, PyrexError) as e:
        sys.stderr.write(str(e) + "\n")
        any_failures = 1
    if any_failures:
        sys.exit(1)


def _build(args):
    parsed = _parse_args(args)
    if parsed is None:
        raise ValueError(f"No parseable arguments found: {args}")

    dump_config()
    input_file, cy_args, remaining = parsed
    _debug("Input file: %s", input_file)
    _debug("Cython args: %s", cy_args)
    _debug("Remaining args: %s", remaining)
    program_name = build(input_file, cy_args)
    return program_name, remaining


def _main():
    args = sys.argv[1:]
    dump_config()
    _build(args)


if __name__ == "__main__":
    _main()

```

