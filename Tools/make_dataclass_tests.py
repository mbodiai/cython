# Used to generate tests/run/test_dataclasses.pyx but translating the CPython test suite
# dataclass file. Initially run using Python 3.10 - this file is not designed to be
# backwards compatible since it will be run manually and infrequently.

import ast
import os.path
import sys

unavailable_functions = frozenset(
    {
        "dataclass_textanno",  # part of CPython test module
        "dataclass_module_1",  # part of CPython test module
        "make_dataclass",  # not implemented in Cython dataclasses (probably won't be implemented)
    }
)

skip_tests = frozenset(
    {
        # needs Cython compile
        # ====================
        ("TestCase", "test_field_default_default_factory_error"),
        ("TestCase", "test_two_fields_one_default"),
        ("TestCase", "test_overwrite_hash"),
        ("TestCase", "test_eq_order"),
        ("TestCase", "test_no_unhashable_default"),
        ("TestCase", "test_disallowed_mutable_defaults"),
        ("TestCase", "test_classvar_default_factory"),
        ("TestCase", "test_field_metadata_mapping"),
        ("TestFieldNoAnnotation", "test_field_without_annotation"),
        (
            "TestFieldNoAnnotation",
            "test_field_without_annotation_but_annotation_in_base",
        ),
        (
            "TestFieldNoAnnotation",
            "test_field_without_annotation_but_annotation_in_base_not_dataclass",
        ),
        ("TestOrdering", "test_overwriting_order"),
        ("TestHash", "test_hash_rules"),
        ("TestHash", "test_hash_no_args"),
        ("TestFrozen", "test_inherit_nonfrozen_from_empty_frozen"),
        ("TestFrozen", "test_inherit_nonfrozen_from_frozen"),
        ("TestFrozen", "test_inherit_frozen_from_nonfrozen"),
        ("TestFrozen", "test_overwriting_frozen"),
        ("TestSlots", "test_add_slots_when_slots_exists"),
        ("TestSlots", "test_cant_inherit_from_iterator_slots"),
        ("TestSlots", "test_weakref_slot_without_slot"),
        ("TestKeywordArgs", "test_no_classvar_kwarg"),
        ("TestKeywordArgs", "test_KW_ONLY_twice"),
        ("TestKeywordArgs", "test_defaults"),
        # uses local variable in class definition
            # Also: difficulty lining up correct repr string when converting tests
        ("TestCase", "test_default_factory"),
            # Also: Mock unassignable to list - legitimate for Cython to raise an error
        ("TestCase", "test_default_factory_with_no_init"),
            # Also: attributes not available on class itself, only instances
        ("TestCase", "test_field_default"),
        ("TestCase", "test_function_annotations"),
        ("TestDescriptors", "test_lookup_on_instance"),
            # Also: Mock unassignable to int - legitimate for Cython to raise an error
        ("TestCase", "test_default_factory_not_called_if_value_given"),
            # Also: cdef classes never don't have the attribute
        ("TestCase", "test_class_attrs"),
        ("TestCase", "test_hash_field_rules"),
        ("TestStringAnnotations",),  # almost all the texts here use local variables
        ("TestMatchArgs", "test_explicit_match_args"),
        # Currently unsupported
        # =====================
        (
            "TestOrdering",
            "test_functools_total_ordering",
        ),  # combination of cython dataclass and total_ordering
        ("TestCase", "test_missing_default_factory"),  # we're MISSING MISSING
        ("TestCase", "test_missing_default"),  # MISSING
        ("TestCase", "test_missing_repr"),  # MISSING
        ("TestSlots",),  # __slots__ isn't understood
        ("TestKeywordArgs", "test_field_marked_as_kwonly"),
        ("TestKeywordArgs", "test_match_args"),
        ("TestKeywordArgs", "test_KW_ONLY"),
        ("TestKeywordArgs", "test_KW_ONLY_as_string"),
        ("TestKeywordArgs", "test_post_init"),
        (
            "TestCase",
            "test_class_var_frozen",
        ),  # __annotations__ not present on cdef classes https://github.com/cython/cython/issues/4519
        ("TestCase", "test_dont_include_other_annotations"),  # __annotations__
        ("TestCase", "test_class_marker"),  # __annotations__
        ("TestDocString",),  # don't think cython dataclasses currently set __doc__
        # either cython.dataclasses.field or cython.dataclasses.dataclass called directly as functions
        # (will probably never be supported)
        ("TestCase", "test_field_repr"),
        ("TestCase", "test_dynamic_class_creation"),
        ("TestCase", "test_dynamic_class_creation_using_field"),
        # Requires inheritance from non-cdef class
        ("TestCase", "test_is_dataclass_genericalias"),
        ("TestCase", "test_generic_extending"),
        ("TestCase", "test_generic_dataclasses"),
        ("TestCase", "test_generic_dynamic"),
        ("TestInit", "test_inherit_from_protocol"),
        ("TestAbstract", "test_abc_implementation"),
        ("TestAbstract", "test_maintain_abc"),
        # Requires multiple inheritance from extension types
        ("TestCase", "test_post_init_not_auto_added"),
        # Refers to nonlocal from enclosing function
        (
            "TestCase",
            "test_post_init_staticmethod",
        ),  # TODO replicate the gist of the test elsewhere
        # PEP487 isn't support in Cython
        ("TestDescriptors", "test_non_descriptor"),
        ("TestDescriptors", "test_set_name"),
        ("TestDescriptors", "test_setting_field_calls_set"),
        ("TestDescriptors", "test_setting_uninitialized_descriptor_field"),
        # Looks up __dict__, which cdef classes don't typically have
        ("TestCase", "test_init_false_no_default"),
        ("TestCase", "test_init_var_inheritance"),  # __dict__ again
        ("TestCase", "test_base_has_init"),
        ("TestInit", "test_base_has_init"),  # needs __dict__ for vars
        # Requires arbitrary attributes to be writeable
        ("TestCase", "test_post_init_super"),
        ('TestCase', 'test_init_in_order'),
        # Cython being strict about argument types - expected difference
        ("TestDescriptors", "test_getting_field_calls_get"),
        ("TestDescriptors", "test_init_calls_set"),
        ("TestHash", "test_eq_only"),
        # I think an expected difference with cdef classes - the property will be in the dict
        ("TestCase", "test_items_in_dicts"),
        # These tests are probably fine, but the string substitution in this file doesn't get it right
        ("TestRepr", "test_repr"),
        ("TestCase", "test_not_in_repr"),
        ('TestRepr', 'test_no_repr'),
        # class variable doesn't exist in Cython so uninitialized variable appears differently - for now this is deliberate
        ('TestInit', 'test_no_init'),
        # I believe the test works but the ordering functions do appear in the class dict (and default slot wrappers which
        # just raise NotImplementedError
        ('TestOrdering', 'test_no_order'),
        # not possible to add attributes on extension types
        ("TestCase", "test_post_init_classmethod"),
        # Cannot redefine the same field in a base dataclass (tested in dataclass_e6)
        ("TestCase", "test_field_order"),
        (
            "TestCase",
            "test_overwrite_fields_in_derived_class",
        ),
        # Bugs
        #======
        # not specifically a dataclass issue - a C int crashes classvar
        ("TestCase", "test_class_var"),
        (
            "TestFrozen",
        ),  # raises AttributeError, not FrozenInstanceError (may be hard to fix)
        ('TestCase', 'test_post_init'),  # Works except for AttributeError instead of FrozenInstanceError
        ("TestReplace", "test_frozen"),  # AttributeError not FrozenInstanceError
        (
            "TestCase",
            "test_dataclasses_qualnames",
        ),  # doesn't define __setattr__ and just relies on Cython to enforce readonly properties
        (
            "TestCase",
            "test_field_named_self",
        ),  # I think just an error in inspecting the signature
        (
            "TestCase",
            "test_init_var_default_factory",
        ),  # should be raising a compile error
        ("TestCase", "test_init_var_no_default"),  # should be raising a compile error
        ("TestCase", "test_init_var_with_default"),  # not sure...
        ("TestReplace", "test_initvar_with_default_value"),  # needs investigating
        # Maybe bugs?
        # ==========
        # cython.dataclasses.field parameter 'metadata' must be a literal value - possibly not something we can support?
        ("TestCase", "test_field_metadata_custom_mapping"),
        (
            "TestCase",
            "test_class_var_default_factory",
        ),  # possibly to do with ClassVar being assigned a field
        (
            "TestCase",
            "test_class_var_with_default",
        ),  # possibly to do with ClassVar being assigned a field
        (
            "TestDescriptors",
        ),  # mostly don't work - I think this may be a limitation of cdef classes but needs investigating
    }
)

version_specific_skips = {
    # The version numbers are the first version that the test should be run on
    ("TestCase", "test_init_var_preserve_type"): (
        3,
        10,
    ),  # needs language support for | operator on types
}

class DataclassInDecorators(ast.NodeVisitor):
    found = False

    def visit_Name(self, node):
        if node.id == "dataclass":
            self.found = True
        return self.generic_visit(node)

    def generic_visit(self, node):
        if self.found:
            return  # skip
        return super().generic_visit(node)


def dataclass_in_decorators(decorator_list):
    finder = DataclassInDecorators()
    for dec in decorator_list:
        finder.visit(dec)
        if finder.found:
            return True
    return False


class SubstituteNameString(ast.NodeTransformer):
    def __init__(self, substitutions):
        super().__init__()
        self.substitutions = substitutions

    def visit_Constant(self, node):
        # attempt to handle some difference in class names
        # (note: requires Python>=3.8)
        if isinstance(node.value, str):
            if node.value.find("<locals>") != -1:
                import re

                new_value = new_value2 = re.sub("[\w.]*<locals>", "", node.value)
                for key, value in self.substitutions.items():
                    new_value2 = re.sub(f"(?<![\w])[.]{key}(?![\w])", value, new_value2)
                if new_value != new_value2:
                    node.value = new_value2
        return node


class SubstituteName(SubstituteNameString):
    def visit_Name(self, node):
        if isinstance(node.ctx, ast.Store):  # don't reassign lhs
            return node
        replacement = self.substitutions.get(node.id, None)
        if replacement is not None:
            return ast.Name(id=replacement, ctx=node.ctx)
        else:
            return node


class IdentifyCdefClasses(ast.NodeVisitor):
    def __init__(self):
        super().__init__()
        self.top_level_class = True
        self.classes = {}
        self.cdef_classes = set()

    def visit_ClassDef(self, node):
        top_level_class, self.top_level_class = self.top_level_class, False
        try:
            if not top_level_class:
                self.classes[node.name] = node
                if dataclass_in_decorators(node.decorator_list):
                    self.handle_cdef_class(node)
                self.generic_visit(node)  # any nested classes in it?
            else:
                self.generic_visit(node)
        finally:
            self.top_level_class = top_level_class

    def visit_FunctionDef(self, node):
        classes, self.classes = self.classes, {}
        self.generic_visit(node)
        self.classes = classes

    def handle_cdef_class(self, cls_node):
        if cls_node not in self.cdef_classes:
            self.cdef_classes.add(cls_node)
            # go back through previous classes we've seen and pick out any first bases
            if cls_node.bases and isinstance(cls_node.bases[0], ast.Name):
                base0_node = self.classes.get(cls_node.bases[0].id)
                if base0_node:
                    self.handle_cdef_class(base0_node)


class ExtractDataclassesToTopLevel(ast.NodeTransformer):
    def __init__(self, cdef_classes_set):
        super().__init__()
        self.nested_name = []
        self.current_function_global_classes = []
        self.global_classes = []
        self.cdef_classes_set = cdef_classes_set
        self.used_names = set()
        self.collected_substitutions = {}
        self.uses_unavailable_name = False
        self.top_level_class = True

    def visit_ClassDef(self, node):
        if not self.top_level_class:
            # Include any non-toplevel class in this to be able
            # to test inheritance.

            self.generic_visit(node)  # any nested classes in it?
            if not node.body:
                node.body.append(ast.Pass)

            # First, make it a C class.
            if node in self.cdef_classes_set:
                node.decorator_list.append(ast.Name(id="cclass", ctx=ast.Load()))
            # otherwise move it to the global scope, but don't make it cdef
            # change the name
            old_name = node.name
            new_name = "_".join([node.name] + self.nested_name)
            while new_name in self.used_names:
                new_name = new_name + "_"
            node.name = new_name
            self.current_function_global_classes.append(node)
            self.used_names.add(new_name)
            # hmmmm... possibly there's a few cases where there's more than one name?
            self.collected_substitutions[old_name] = node.name

            return ast.Assign(
                targets=[ast.Name(id=old_name, ctx=ast.Store())],
                value=ast.Name(id=new_name, ctx=ast.Load()),
                lineno=-1,
            )
        else:
            top_level_class, self.top_level_class = self.top_level_class, False
            self.nested_name.append(node.name)
            if tuple(self.nested_name) in skip_tests:
                self.top_level_class = top_level_class
                self.nested_name.pop()
                return None
            self.generic_visit(node)
            self.nested_name.pop()
            if not node.body:
                node.body.append(ast.Pass())
            self.top_level_class = top_level_class
            return node

    def visit_FunctionDef(self, node):
        self.nested_name.append(node.name)
        if tuple(self.nested_name) in skip_tests:
            self.nested_name.pop()
            return None
        if tuple(self.nested_name) in version_specific_skips:
            version = version_specific_skips[tuple(self.nested_name)]
            decorator = ast.parse(
                f"skip_on_versions_below({version})", mode="eval"
            ).body
            node.decorator_list.append(decorator)
        collected_subs, self.collected_substitutions = self.collected_substitutions, {}
        uses_unavailable_name, self.uses_unavailable_name = (
            self.uses_unavailable_name,
            False,
        )
        current_func_globs, self.current_function_global_classes = (
            self.current_function_global_classes,
            [],
        )

        # visit once to work out what the substitutions should be
        self.generic_visit(node)
        if self.collected_substitutions:
            # replace strings in this function
            node = SubstituteNameString(self.collected_substitutions).visit(node)
            replacer = SubstituteName(self.collected_substitutions)
            # replace any base classes
            for global_class in self.current_function_global_classes:
                global_class = replacer.visit(global_class)
        self.global_classes.append(self.current_function_global_classes)

        self.nested_name.pop()
        self.collected_substitutions = collected_subs
        if self.uses_unavailable_name:
            node = None
        self.uses_unavailable_name = uses_unavailable_name
        self.current_function_global_classes = current_func_globs
        return node

    def visit_Name(self, node):
        if node.id in unavailable_functions:
            self.uses_unavailable_name = True
        return self.generic_visit(node)

    def visit_Import(self, node):
        return None  # drop imports, we add these into the text ourself

    def visit_ImportFrom(self, node):
        return None  # drop imports, we add these into the text ourself

    def visit_Call(self, node):
        if (
            isinstance(node.func, ast.Attribute)
            and node.func.attr == "assertRaisesRegex"
        ):
            # we end up with a bunch of subtle name changes that are very hard to correct for
            # therefore, replace with "assertRaises"
            node.func.attr = "assertRaises"
            node.args.pop()
        return self.generic_visit(node)

    def visit_Module(self, node):
        self.generic_visit(node)
        node.body[0:0] = self.global_classes
        return node

    def visit_AnnAssign(self, node):
        # string annotations are forward declarations but the string will be wrong
        # (because we're renaming the class)
        if (isinstance(node.annotation, ast.Constant) and
                isinstance(node.annotation.value, str)):
            # although it'd be good to resolve these declarations, for the
            # sake of the tests they only need to be "object"
            node.annotation = ast.Name(id="object", ctx=ast.Load)

        return node


def main():
    script_path = os.path.split(sys.argv[0])[0]
    filename = "test_dataclasses.py"
    py_module_path = os.path.join(script_path, "dataclass_test_data", filename)
    with open(py_module_path, "r") as f:
        tree = ast.parse(f.read(), filename)

    cdef_class_finder = IdentifyCdefClasses()
    cdef_class_finder.visit(tree)
    transformer = ExtractDataclassesToTopLevel(cdef_class_finder.cdef_classes)
    tree = transformer.visit(tree)

    # the directive doesn't get applied outside the include if it's put
    # in the pxi file
    # any extras Cython needs to add go in this include file
    print('include "test_dataclasses.pxi"')
    print(ast.unparse(tree))
    output_path = os.path.join(script_path, "..", "tests", "run", filename + "x")
    with open(output_path, "w") as f:
        print("# AUTO-GENERATED BY Tools/make_dataclass_tests.py", file=f)
        print("# DO NOT EDIT", file=f)
        print(file=f)
        # the directive doesn't get applied outside the include if it's put
        # in the pxi file
        print("# cython: language_level=3", file=f)
        # any extras Cython needs to add go in this include file
        print('include "test_dataclasses.pxi"', file=f)
        print(file=f)
        print(ast.unparse(tree), file=f)


if __name__ == "__main__":
    main()
##### START: GENERATED LIST OF GENERATED TYPES #####
# Generated by "Tools/cython-generate-shadow-pyi.py" on 2025-02-08 19:38:30.143312

const_bint : TypeAlias = const[bint]
p_const_bint = pointer[const[bint]]
pp_const_bint = pointer[pointer[const[bint]]]
ppp_const_bint = pointer[pointer[pointer[const[bint]]]]
p_bint = pointer[bint]
pp_bint = pointer[pointer[bint]]
ppp_bint = pointer[pointer[pointer[bint]]]
char : TypeAlias = py_int
const_char : TypeAlias = const[py_int]
p_const_char = pointer[const[py_int]]
pp_const_char = pointer[pointer[const[py_int]]]
ppp_const_char = pointer[pointer[pointer[const[py_int]]]]
p_char = pointer[py_int]
pp_char = pointer[pointer[py_int]]
ppp_char = pointer[pointer[pointer[py_int]]]
complex : TypeAlias = py_complex
const_complex : TypeAlias = const[py_complex]
p_const_complex = pointer[const[py_complex]]
pp_const_complex = pointer[pointer[const[py_complex]]]
ppp_const_complex = pointer[pointer[pointer[const[py_complex]]]]
p_complex = pointer[py_complex]
pp_complex = pointer[pointer[py_complex]]
ppp_complex = pointer[pointer[pointer[py_complex]]]
double : TypeAlias = py_float
const_double : TypeAlias = const[py_float]
p_const_double = pointer[const[py_float]]
pp_const_double = pointer[pointer[const[py_float]]]
ppp_const_double = pointer[pointer[pointer[const[py_float]]]]
p_double = pointer[py_float]
pp_double = pointer[pointer[py_float]]
ppp_double = pointer[pointer[pointer[py_float]]]
doublecomplex : TypeAlias = py_complex
const_doublecomplex : TypeAlias = const[py_complex]
p_const_doublecomplex = pointer[const[py_complex]]
pp_const_doublecomplex = pointer[pointer[const[py_complex]]]
ppp_const_doublecomplex = pointer[pointer[pointer[const[py_complex]]]]
p_doublecomplex = pointer[py_complex]
pp_doublecomplex = pointer[pointer[py_complex]]
ppp_doublecomplex = pointer[pointer[pointer[py_complex]]]
float : TypeAlias = py_float
const_float : TypeAlias = const[py_float]
p_const_float = pointer[const[py_float]]
pp_const_float = pointer[pointer[const[py_float]]]
ppp_const_float = pointer[pointer[pointer[const[py_float]]]]
p_float = pointer[py_float]
pp_float = pointer[pointer[py_float]]
ppp_float = pointer[pointer[pointer[py_float]]]
floatcomplex : TypeAlias = py_complex
const_floatcomplex : TypeAlias = const[py_complex]
p_const_floatcomplex = pointer[const[py_complex]]
pp_const_floatcomplex = pointer[pointer[const[py_complex]]]
ppp_const_floatcomplex = pointer[pointer[pointer[const[py_complex]]]]
p_floatcomplex = pointer[py_complex]
pp_floatcomplex = pointer[pointer[py_complex]]
ppp_floatcomplex = pointer[pointer[pointer[py_complex]]]
int : TypeAlias = py_int
const_int : TypeAlias = const[py_int]
p_const_int = pointer[const[py_int]]
pp_const_int = pointer[pointer[const[py_int]]]
ppp_const_int = pointer[pointer[pointer[const[py_int]]]]
p_int = pointer[py_int]
pp_int = pointer[pointer[py_int]]
ppp_int = pointer[pointer[pointer[py_int]]]
long : TypeAlias = py_int
const_long : TypeAlias = const[py_int]
p_const_long = pointer[const[py_int]]
pp_const_long = pointer[pointer[const[py_int]]]
ppp_const_long = pointer[pointer[pointer[const[py_int]]]]
p_long = pointer[py_int]
pp_long = pointer[pointer[py_int]]
ppp_long = pointer[pointer[pointer[py_int]]]
py_long : TypeAlias = py_int
longdouble : TypeAlias = py_float
const_longdouble : TypeAlias = const[py_float]
p_const_longdouble = pointer[const[py_float]]
pp_const_longdouble = pointer[pointer[const[py_float]]]
ppp_const_longdouble = pointer[pointer[pointer[const[py_float]]]]
p_longdouble = pointer[py_float]
pp_longdouble = pointer[pointer[py_float]]
ppp_longdouble = pointer[pointer[pointer[py_float]]]
longdoublecomplex : TypeAlias = py_complex
const_longdoublecomplex : TypeAlias = const[py_complex]
p_const_longdoublecomplex = pointer[const[py_complex]]
pp_const_longdoublecomplex = pointer[pointer[const[py_complex]]]
ppp_const_longdoublecomplex = pointer[pointer[pointer[const[py_complex]]]]
p_longdoublecomplex = pointer[py_complex]
pp_longdoublecomplex = pointer[pointer[py_complex]]
ppp_longdoublecomplex = pointer[pointer[pointer[py_complex]]]
longlong : TypeAlias = py_int
const_longlong : TypeAlias = const[py_int]
p_const_longlong = pointer[const[py_int]]
pp_const_longlong = pointer[pointer[const[py_int]]]
ppp_const_longlong = pointer[pointer[pointer[const[py_int]]]]
p_longlong = pointer[py_int]
pp_longlong = pointer[pointer[py_int]]
ppp_longlong = pointer[pointer[pointer[py_int]]]
schar : TypeAlias = py_int
const_schar : TypeAlias = const[py_int]
p_const_schar = pointer[const[py_int]]
pp_const_schar = pointer[pointer[const[py_int]]]
ppp_const_schar = pointer[pointer[pointer[const[py_int]]]]
p_schar = pointer[py_int]
pp_schar = pointer[pointer[py_int]]
ppp_schar = pointer[pointer[pointer[py_int]]]
short : TypeAlias = py_int
const_short : TypeAlias = const[py_int]
p_const_short = pointer[const[py_int]]
pp_const_short = pointer[pointer[const[py_int]]]
ppp_const_short = pointer[pointer[pointer[const[py_int]]]]
p_short = pointer[py_int]
pp_short = pointer[pointer[py_int]]
ppp_short = pointer[pointer[pointer[py_int]]]
sint : TypeAlias = py_int
const_sint : TypeAlias = const[py_int]
p_const_sint = pointer[const[py_int]]
pp_const_sint = pointer[pointer[const[py_int]]]
ppp_const_sint = pointer[pointer[pointer[const[py_int]]]]
p_sint = pointer[py_int]
pp_sint = pointer[pointer[py_int]]
ppp_sint = pointer[pointer[pointer[py_int]]]
slong : TypeAlias = py_int
const_slong : TypeAlias = const[py_int]
p_const_slong = pointer[const[py_int]]
pp_const_slong = pointer[pointer[const[py_int]]]
ppp_const_slong = pointer[pointer[pointer[const[py_int]]]]
p_slong = pointer[py_int]
pp_slong = pointer[pointer[py_int]]
ppp_slong = pointer[pointer[pointer[py_int]]]
slonglong : TypeAlias = py_int
const_slonglong : TypeAlias = const[py_int]
p_const_slonglong = pointer[const[py_int]]
pp_const_slonglong = pointer[pointer[const[py_int]]]
ppp_const_slonglong = pointer[pointer[pointer[const[py_int]]]]
p_slonglong = pointer[py_int]
pp_slonglong = pointer[pointer[py_int]]
ppp_slonglong = pointer[pointer[pointer[py_int]]]
sshort : TypeAlias = py_int
const_sshort : TypeAlias = const[py_int]
p_const_sshort = pointer[const[py_int]]
pp_const_sshort = pointer[pointer[const[py_int]]]
ppp_const_sshort = pointer[pointer[pointer[const[py_int]]]]
p_sshort = pointer[py_int]
pp_sshort = pointer[pointer[py_int]]
ppp_sshort = pointer[pointer[pointer[py_int]]]
Py_hash_t : TypeAlias = py_int
const_Py_hash_t : TypeAlias = const[py_int]
p_const_Py_hash_t = pointer[const[py_int]]
pp_const_Py_hash_t = pointer[pointer[const[py_int]]]
ppp_const_Py_hash_t = pointer[pointer[pointer[const[py_int]]]]
p_Py_hash_t = pointer[py_int]
pp_Py_hash_t = pointer[pointer[py_int]]
ppp_Py_hash_t = pointer[pointer[pointer[py_int]]]
ptrdiff_t : TypeAlias = py_int
const_ptrdiff_t : TypeAlias = const[py_int]
p_const_ptrdiff_t = pointer[const[py_int]]
pp_const_ptrdiff_t = pointer[pointer[const[py_int]]]
ppp_const_ptrdiff_t = pointer[pointer[pointer[const[py_int]]]]
p_ptrdiff_t = pointer[py_int]
pp_ptrdiff_t = pointer[pointer[py_int]]
ppp_ptrdiff_t = pointer[pointer[pointer[py_int]]]
size_t : TypeAlias = py_int
const_size_t : TypeAlias = const[py_int]
p_const_size_t = pointer[const[py_int]]
pp_const_size_t = pointer[pointer[const[py_int]]]
ppp_const_size_t = pointer[pointer[pointer[const[py_int]]]]
p_size_t = pointer[py_int]
pp_size_t = pointer[pointer[py_int]]
ppp_size_t = pointer[pointer[pointer[py_int]]]
ssize_t : TypeAlias = py_int
const_ssize_t : TypeAlias = const[py_int]
p_const_ssize_t = pointer[const[py_int]]
pp_const_ssize_t = pointer[pointer[const[py_int]]]
ppp_const_ssize_t = pointer[pointer[pointer[const[py_int]]]]
p_ssize_t = pointer[py_int]
pp_ssize_t = pointer[pointer[py_int]]
ppp_ssize_t = pointer[pointer[pointer[py_int]]]
Py_ssize_t : TypeAlias = py_int
const_Py_ssize_t : TypeAlias = const[py_int]
p_const_Py_ssize_t = pointer[const[py_int]]
pp_const_Py_ssize_t = pointer[pointer[const[py_int]]]
ppp_const_Py_ssize_t = pointer[pointer[pointer[const[py_int]]]]
p_Py_ssize_t = pointer[py_int]
pp_Py_ssize_t = pointer[pointer[py_int]]
ppp_Py_ssize_t = pointer[pointer[pointer[py_int]]]
Py_tss_t : TypeAlias = Any
const_Py_tss_t : TypeAlias = const[Any]
p_Py_tss_t = pointer[Any]
pp_Py_tss_t = pointer[pointer[Any]]
ppp_Py_tss_t = pointer[pointer[pointer[Any]]]
uchar : TypeAlias = py_int
const_uchar : TypeAlias = const[py_int]
p_const_uchar = pointer[const[py_int]]
pp_const_uchar = pointer[pointer[const[py_int]]]
ppp_const_uchar = pointer[pointer[pointer[const[py_int]]]]
p_uchar = pointer[py_int]
pp_uchar = pointer[pointer[py_int]]
ppp_uchar = pointer[pointer[pointer[py_int]]]
Py_UCS4 : TypeAlias = py_int
const_Py_UCS4 : TypeAlias = const[py_int]
p_const_Py_UCS4 = pointer[const[py_int]]
pp_const_Py_UCS4 = pointer[pointer[const[py_int]]]
ppp_const_Py_UCS4 = pointer[pointer[pointer[const[py_int]]]]
p_Py_UCS4 = pointer[py_int]
pp_Py_UCS4 = pointer[pointer[py_int]]
ppp_Py_UCS4 = pointer[pointer[pointer[py_int]]]
uint : TypeAlias = py_int
const_uint : TypeAlias = const[py_int]
p_const_uint = pointer[const[py_int]]
pp_const_uint = pointer[pointer[const[py_int]]]
ppp_const_uint = pointer[pointer[pointer[const[py_int]]]]
p_uint = pointer[py_int]
pp_uint = pointer[pointer[py_int]]
ppp_uint = pointer[pointer[pointer[py_int]]]
ulong : TypeAlias = py_int
const_ulong : TypeAlias = const[py_int]
p_const_ulong = pointer[const[py_int]]
pp_const_ulong = pointer[pointer[const[py_int]]]
ppp_const_ulong = pointer[pointer[pointer[const[py_int]]]]
p_ulong = pointer[py_int]
pp_ulong = pointer[pointer[py_int]]
ppp_ulong = pointer[pointer[pointer[py_int]]]
ulonglong : TypeAlias = py_int
const_ulonglong : TypeAlias = const[py_int]
p_const_ulonglong = pointer[const[py_int]]
pp_const_ulonglong = pointer[pointer[const[py_int]]]
ppp_const_ulonglong = pointer[pointer[pointer[const[py_int]]]]
p_ulonglong = pointer[py_int]
pp_ulonglong = pointer[pointer[py_int]]
ppp_ulonglong = pointer[pointer[pointer[py_int]]]
Py_UNICODE : TypeAlias = py_int
const_Py_UNICODE : TypeAlias = const[py_int]
p_const_Py_UNICODE = pointer[const[py_int]]
pp_const_Py_UNICODE = pointer[pointer[const[py_int]]]
ppp_const_Py_UNICODE = pointer[pointer[pointer[const[py_int]]]]
p_Py_UNICODE = pointer[py_int]
pp_Py_UNICODE = pointer[pointer[py_int]]
ppp_Py_UNICODE = pointer[pointer[pointer[py_int]]]
ushort : TypeAlias = py_int
const_ushort : TypeAlias = const[py_int]
p_const_ushort = pointer[const[py_int]]
pp_const_ushort = pointer[pointer[const[py_int]]]
ppp_const_ushort = pointer[pointer[pointer[const[py_int]]]]
p_ushort = pointer[py_int]
pp_ushort = pointer[pointer[py_int]]
ppp_ushort = pointer[pointer[pointer[py_int]]]
void : TypeAlias = Any
const_void : TypeAlias = const[Any]
p_void = pointer[Any]
pp_void = pointer[pointer[Any]]
ppp_void = pointer[pointer[pointer[Any]]]

##### END: GENERATED LIST OF GENERATED TYPES #####
