import pytest
from io import StringIO
from typing import List, Dict, Any

# Assuming online.py is in ../mbpy/parse relative to the tests directory
# Adjust the import path if your structure is different
try:
    from mbpy.parse.online import (
        FirstCharTag,
        ParameterizedLineClassifier,
        IndentationHierarchyRule,
        TagBasedHierarchyRule, # Import this even if not tested yet
        ConfigurableHierarchyRule,
        LinePartitioner,
        StructureBuilder,
        Node,
        build_text_hierarchy # Use this for integration tests
    )
except ImportError:
    pytest.fail("Could not import modules from mbpy.parse.online. Check PYTHONPATH or file location.", pytrace=False)


# --- Test ParameterizedLineClassifier ---

@pytest.fixture
def default_classifier():
    # Use the parameterized one for most tests now
    return ParameterizedLineClassifier()

@pytest.mark.parametrize("line, expected_tag", [
    ("# Header 1", FirstCharTag.HEADER),
    ("## Header 2", FirstCharTag.HEADER), # Assumes default prefix "# "
    ("* Bullet point", FirstCharTag.BULLET),
    ("- Another bullet", FirstCharTag.BULLET),
    ("  • Indented bullet", FirstCharTag.BULLET),
    ("1. Enum item", FirstCharTag.ENUMERATED),
    ("  2. Indented enum", FirstCharTag.ENUMERATED),
    ("10. Double digit enum", FirstCharTag.ENUMERATED),
    ("Just some text", FirstCharTag.LOWERCASE),
    ("UPPERCASE LINE", FirstCharTag.UPPERCASE),
    ("UPPER", FirstCharTag.UPPERCASE), # Test min length (default 5)
    ("UPPE", FirstCharTag.LOWERCASE), # Test min length (default 5) -> lowercase/symbol? Check logic. Parameterized classifies as lowercase
    ("123 Symbol starts", FirstCharTag.SYMBOL),
    ("   ", FirstCharTag.WHITESPACE),
    ("", FirstCharTag.WHITESPACE), # Empty string
    ("**Bold Text**", FirstCharTag.BOLD),
    ("__Italic Text__", FirstCharTag.ITALICIZED),
    ("Not an enum 1. fake", FirstCharTag.LOWERCASE),
    ("Not a bullet * fake", FirstCharTag.LOWERCASE),
    ("-No space bullet", FirstCharTag.SYMBOL), # Requires space after marker
    ("1.No space enum", FirstCharTag.SYMBOL), # Requires space after dot
])
def test_parameterized_classifier_defaults(default_classifier, line, expected_tag):
    assert default_classifier.classify(line) == expected_tag

def test_parameterized_classifier_custom():
    classifier = ParameterizedLineClassifier(
        header_prefixes=["> ", "H: "],
        bullet_markers=["+ "],
        enum_pattern=r'^\s*\w\)\s+', # e.g., a) item
        allcaps_min_len=3
    )
    assert classifier.classify("> Header") == FirstCharTag.HEADER
    assert classifier.classify("H: Header") == FirstCharTag.HEADER
    assert classifier.classify("+ Bullet") == FirstCharTag.BULLET
    assert classifier.classify("a) Enum") == FirstCharTag.ENUMERATED
    assert classifier.classify("ABC") == FirstCharTag.UPPERCASE
    assert classifier.classify("AB") == FirstCharTag.LOWERCASE # length < 3
    assert classifier.classify("# Not Header") == FirstCharTag.SYMBOL # Default prefix doesn't match
    assert classifier.classify("* Not Bullet") == FirstCharTag.LOWERCASE # Default marker doesn't match


# --- Test IndentationHierarchyRule ---

# Helper to create a dummy node for testing rules
def _create_node(tag=FirstCharTag.LOWERCASE) -> Node[str, FirstCharTag]:
    # Adjust if Node definition changes
    return {'tag': tag, 'content': [], 'children': []}

@pytest.mark.parametrize("entity, stack_entities, expected_parent_index", [
    # Simple indent
    ("  indented", ["root"], 0),
    # Deeper indent
    ("    deeper", ["root", "  indented"], 1),
    # Same indent (should attach to parent with less indent -> root)
    ("  sibling", ["root", "  indented"], 0),
    # Outdent
    # Entity " less indented" (indent 1). Search stack [root(0), "  indented"(2), "    deeper"(4)] backwards.
    # First item with less indent is "root" (index 0).
    (" less indented", ["root", "  indented", "    deeper"], 0), # Corrected expectation
    # Outdent to root
    ("back to root", ["root", "  indented", "    deeper"], None),
    # Empty stack
    ("first item", [], None),
    # Entity not indented
    ("unindented sibling", ["root"], None),
    # Indent after unindented
    ("  indent again", ["root", "unindented sibling"], 1), # Attaches to 'unindented sibling'
])
def test_indentation_rule(entity, stack_entities, expected_parent_index):
    rule = IndentationHierarchyRule()
    stack = [(s_entity, _create_node()) for s_entity in stack_entities]
    parent_tuple = rule.find_parent(entity, stack, [])
    if expected_parent_index is None:
        assert parent_tuple is None
    else:
        assert parent_tuple is not None
        assert parent_tuple == stack[expected_parent_index]


# --- Test build_text_hierarchy (Integration) ---

def assert_hierarchy(input_text: str, expected_json: List[Dict[str, Any]], rule_name: str = 'indentation', rule_params: Dict[str, Any] = {}):
    """Helper function to test build_text_hierarchy and compare JSON output."""

    selected_rule: HierarchyRule[Any, Any] | None = None
    # Use parameterized classifier for integration test flexibility
    # We might need specific classifiers depending on the rule being tested
    if rule_name == 'indentation':
         classifier = ParameterizedLineClassifier() # Indentation rule doesn't use tags heavily
         selected_rule = IndentationHierarchyRule()
    elif rule_name == 'tagbased':
         classifier = ParameterizedLineClassifier() # TagBased needs tags
         selected_rule = TagBasedHierarchyRule(classifier=classifier)
    elif rule_name == 'configurable':
         classifier = ParameterizedLineClassifier() # Configurable needs tags
         selected_rule = ConfigurableHierarchyRule(classifier=classifier, **rule_params)
    else:
         pytest.fail(f"Unknown rule name: {rule_name}")

    hierarchy = build_text_hierarchy(StringIO(input_text), hierarchy_rule=selected_rule)

    # Convert result to comparable dict structure
    def convert_node_for_test(node):
        tag_value = node["tag"].value if hasattr(node["tag"], 'value') else str(node["tag"])
        # Join content lines for simplicity in comparison
        content = "\n".join(node["content"])
        children = [convert_node_for_test(child) for child in node["children"]]
        # Sort children by content? No, order likely matters.
        return {"tag": tag_value, "content": content.rstrip(), "children": children} # rstrip content

    result_json = [convert_node_for_test(node) for node in hierarchy]

    # Use pytest's dict comparison
    assert result_json == expected_json

def test_build_text_indentation_simple():
    text = """
Root 1
  Child 1.1
  Child 1.2
    Grandchild 1.2.1
Root 2
  Child 2.1
"""
    expected = [
        {'tag': 'lowercase', 'content': 'Root 1', 'children': [
            {'tag': 'lowercase', 'content': '  Child 1.1', 'children': []},
            {'tag': 'lowercase', 'content': '  Child 1.2', 'children': [
                {'tag': 'lowercase', 'content': '    Grandchild 1.2.1', 'children': []}
            ]}
        ]},
        {'tag': 'lowercase', 'content': 'Root 2', 'children': [
            {'tag': 'lowercase', 'content': '  Child 2.1', 'children': []}
        ]}
    ]
    assert_hierarchy(text.strip(), expected, rule_name='indentation') # Use strip() for cleaner input

def test_build_text_indentation_man_page_snippet():
    # Simplified snippet focusing on option/description structure
    text = """
OPTIONS
     -l      (The lowercase letter "ell".) List in long format. (See below.) If the
             output is to a terminal, a total sum for all the file sizes is
             output on a line before the long listing.
     -a      Include directory entries whose names begin with a dot (.).
     -h      When used with the -l option, use unit suffixes: Byte,
             Kilobyte, Megabyte, Gigabyte, Terabyte and Petabyte in order to
             reduce the number of digits to three or fewer using base 2 for
             sizes.
"""
    # Expected output with pure INDENTATION rule
    expected_indentation = [
        {'tag': 'allcaps', 'content': 'OPTIONS', 'children': [
            # All subsequent lines become children because OPTIONS has 0 indent
            {'tag': 'symbol', 'content': '     -l      (The lowercase letter "ell".) List in long format. (See below.) If the', 'children': []},
            {'tag': 'lowercase', 'content': '             output is to a terminal, a total sum for all the file sizes is', 'children': []},
            {'tag': 'lowercase', 'content': '             output on a line before the long listing.', 'children': []},
            {'tag': 'symbol', 'content': '     -a      Include directory entries whose names begin with a dot (.).', 'children': []},
            {'tag': 'symbol', 'content': '     -h      When used with the -l option, use unit suffixes: Byte,', 'children': []},
            {'tag': 'lowercase', 'content': '             Kilobyte, Megabyte, Gigabyte, Terabyte and Petabyte in order to', 'children': []},
            {'tag': 'lowercase', 'content': '             reduce the number of digits to three or fewer using base 2 for', 'children': []},
            {'tag': 'lowercase', 'content': '             sizes.', 'children': []}
        ]}
    ]
    assert_hierarchy(text.strip(), expected_indentation, rule_name='indentation')

# --- Tests for ConfigurableHierarchyRule ---

def test_build_text_configurable_man_page_snippet_defaults():
    # Uses --rule configurable with its default parameters
    # Default key_tags = [UPPERCASE], value_indent_threshold = 2
    text = """
OPTIONS
     -l      List long format.
             More details for -l.
     -a      Include dot entries.
             More details for -a.
UPPERCASE_KEY
  Value for uppercase key line 1
  Value line 2
Another option
"""
    # Expected output with CONFIGURABLE rule (defaults)
    expected_configurable = [
        {'tag': 'allcaps', 'content': 'OPTIONS', 'children': [
             # -l is key (SYMBOL), description follows (LOWERCASE, indent > 0) -> Follower rule or fallback?
             # Current ConfigurableRule might attach based on follow_tags or indent fallback.
             # Let's assume follow_tags attaches indented lowercase to previous.
            {'tag': 'symbol', 'content': '     -l      List long format.', 'children': [
                 {'tag': 'lowercase', 'content': '             More details for -l.', 'children': []}
            ]},
            {'tag': 'symbol', 'content': '     -a      Include dot entries.', 'children': [
                 {'tag': 'lowercase', 'content': '             More details for -a.', 'children': []}
            ]},
        ]},
        # UPPERCASE_KEY explicitly matches key_tags
        {'tag': 'allcaps', 'content': 'UPPERCASE_KEY', 'children': [
             # These should attach due to rule #2 (key_tag + indent increase >= threshold)
            {'tag': 'lowercase', 'content': '  Value for uppercase key line 1', 'children': []},
             # This should attach to previous value line via follow_tags rule or fallback?
             # Let's assume follow_tags
            {'tag': 'lowercase', 'content': '  Value line 2', 'children': []}
        ]},
        {'tag': 'lowercase', 'content': 'Another option', 'children': []}
    ]
    assert_hierarchy(text.strip(), expected_configurable, rule_name='configurable')

def test_build_text_configurable_man_page_snippet_custom_params():
    # Uses --rule configurable with custom parameters
    text = """
MY_KEY
    Value for my key (indent 4)
ANOTHER_KEY
      Value for another key (indent 6)
"""
    expected_configurable = [
        {'tag': 'allcaps', 'content': 'MY_KEY', 'children': [
            # Value attaches because indent diff (4) >= threshold (3)
            {'tag': 'lowercase', 'content': '    Value for my key (indent 4)', 'children': []}
        ]},
        {'tag': 'allcaps', 'content': 'ANOTHER_KEY', 'children': [
             # Value attaches because indent diff (6) >= threshold (3)
            {'tag': 'lowercase', 'content': '      Value for another key (indent 6)', 'children': []}
        ]}
    ]
    rule_params = {
        'key_tags': [FirstCharTag.UPPERCASE],
        'value_indent_threshold': 3 # Require indent of at least 3
    }
    assert_hierarchy(text.strip(), expected_configurable, rule_name='configurable', rule_params=rule_params)

# TODO: Add tests for TagBasedHierarchyRule (if its logic differs significantly)
# TODO: Add tests for partitioners
# TODO: Add tests for PDF processing (requires setting up PDF files or mocking pymupdf)
