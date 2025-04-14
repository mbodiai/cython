from abc import abstractmethod
from dataclasses import dataclass, field
from enum import Enum
from functools import partial
import sys
import json
from io import StringIO
from pathlib import Path
from typing import cast, Any, Dict, Union, Optional, List, Tuple
from mbcore.display import safe_print
from mbcore.more import first, second, split_at
from mbcore.collect import equals
from mbcore.tree import tree_nodes
from typing_extensions import (
    IO,
    Any,
    Generic,
    Iterable,
    List,
    Optional,
    Protocol,
    TypeVar,
    TypedDict,
)
import re

# PDF parsing imports - will need to be installed
try:
    from pymupdf import Page, TextPage, open as pymupdf_open, TEXT_OUTPUT_JSON
    PDF_SUPPORT = True
except ImportError:
    PDF_SUPPORT = False

T = TypeVar("T")
TagT = TypeVar("TagT")
TagT_co = TypeVar("TagT_co", covariant=True)
TagT_contra = TypeVar("TagT_contra", contravariant=True)

T_contra = TypeVar("T_contra", contravariant=True)
T_co = TypeVar("T_co", covariant=True)


class Classifier(Protocol, Generic[T_co, TagT_co]):
    """What kind of tag should we use for this entity?"""

    @abstractmethod
    def classify(self: "Classifier[T,TagT]", entity: T) -> TagT_co: ...


class Partitioner(Protocol[T_co]):
    """How should we partition the input stream into entities?"""

    @abstractmethod
    def partition(self, input_stream: Any) -> Iterable[T_co]: ...


class HierarchyRule(Protocol[T, TagT]):
    """How should we determine the parent of an entity?"""

    @abstractmethod
    def find_parent(
        self, entity: T, stack: List[tuple[T, 'Node[T, TagT]']], context: List[T]
    ) -> Optional[tuple[T, 'Node[T, TagT]']]: ...


class Node(TypedDict, Generic[T, TagT]):
    """Represents a node in the hierarchical structure."""

    tag: TagT
    content: List[T]
    children: List["Node[T, TagT]"]


class StructureBuilder(Generic[T, TagT]):
    """Generic builder for constructing hierarchical structures from entities."""

    def __init__(
        self,
        classifier: Classifier[T, TagT],
        partitioner: Partitioner[T],
        hierarchy_rule: HierarchyRule[T, TagT],
    ):
        self.classifier = classifier
        self.partitioner = partitioner
        self.hierarchy_rule = hierarchy_rule
        self.stack: List[tuple[T, Node[T, TagT]]] = []
        self.root: List[Node[T, TagT]] = []

    def process(self, input_stream: Any) -> List[Node[T, TagT]]:
        """Processes the input stream and returns the hierarchical structure."""  # noqa: D401
        entities = self.partitioner.partition(input_stream)
        history: List[T] = []
        for entity in entities:
            self._process_entity(entity, history)
            history.append(entity)
        return self.root

    def _process_entity(self, entity: T, history: List[T]) -> None:
        parent_tuple = self.hierarchy_rule.find_parent(entity, self.stack, history)

        parent_index = -1
        if parent_tuple is not None:
            try:
                parent_index = self.stack.index(parent_tuple)
            except ValueError:
                parent_index = -1

        self.stack = self.stack[: parent_index + 1] if parent_index != -1 else []

        tag = self.classifier.classify(entity)
        new_node: Node[T, TagT] = {"tag": tag, "content": [entity], "children": []}

        if self.stack:
            self.stack[-1][1]["children"].append(new_node)
        else:
            self.root.append(new_node)

        self.stack.append((entity, new_node))


class FirstCharTag(Enum):
    """Tags based on the first non-whitespace character of a line."""

    WHITESPACE = "whitespace"
    UPPERCASE = "allcaps"
    LOWERCASE = "lowercase"
    BULLET = "bullet"
    HEADER = "header"
    SYMBOL = "symbol"
    BOLD = "bold"
    ITALICIZED = "italicized"
    ENUMERATED = "enumerated"
    NULL = "null"


class PDFElementTag(Enum):
    """Tags for PDF document elements."""
    
    TITLE = "title"
    HEADING = "heading"
    PARAGRAPH = "paragraph"
    LIST_ITEM = "list_item"
    IMAGE = "image"
    TABLE = "table"
    METADATA = "metadata"
    BLOCK = "block"
    PAGE = "page"


@dataclass
class LineClassifier(Classifier[str, FirstCharTag]):
    """Classifies lines based on their first non-whitespace character (Original)."""
    def classify(self, entity: str, context: Any = None) -> FirstCharTag:
        stripped = entity.lstrip()
        if not stripped:
            return FirstCharTag.WHITESPACE
        first_char = first(stripped)
        if not first_char: return FirstCharTag.NULL
        # Simplified original logic for brevity
        if stripped.startswith("# "): return FirstCharTag.HEADER
        if first_char in "*-•" and len(stripped) > 1 and stripped[1].isspace(): return FirstCharTag.BULLET
        if first_char.isdigit() and stripped[1:].lstrip().startswith('.'): return FirstCharTag.ENUMERATED
        if stripped.isupper() and any(c.isalpha() for c in stripped): return FirstCharTag.UPPERCASE
        if first_char.isalpha(): return FirstCharTag.LOWERCASE
        return FirstCharTag.SYMBOL


@dataclass
class ParameterizedLineClassifier(Classifier[str, FirstCharTag]):
    """Classifies lines based on configurable markers and patterns."""
    # Match headers like #, ##, ### etc. followed by a space
    header_pattern: str = r"^\s*(#+)\s+" 
    bullet_markers: List[str] = field(default_factory=lambda: ["* ", "- ", "• "])
    enum_pattern: str = r"^\s*\d+\.\s+"
    bold_pattern: str = r"^\*\*.*\*\*$"
    italic_pattern: str = r"^__.*__$"
    allcaps_min_len: int = 5

    def classify(self, entity: str, context: Any = None) -> FirstCharTag:
        stripped = entity.lstrip()
        if not stripped:
            return FirstCharTag.WHITESPACE

        # Check patterns first
        if re.match(self.bold_pattern, stripped): return FirstCharTag.BOLD
        if re.match(self.italic_pattern, stripped): return FirstCharTag.ITALICIZED
        
        # Check header pattern (using re.match for start of string)
        if re.match(self.header_pattern, stripped):
             return FirstCharTag.HEADER

        # Check bullet markers
        for marker in self.bullet_markers:
             if stripped.startswith(marker):
                 return FirstCharTag.BULLET
                 
        # Check enum pattern (using re.search as indent might precede it)
        if re.search(self.enum_pattern, entity):
             return FirstCharTag.ENUMERATED

        # Check content characteristics
        first_char = first(stripped)
        if not first_char: return FirstCharTag.NULL

        if (len(stripped) >= self.allcaps_min_len and
            stripped.isupper() and
            any(c.isalpha() for c in stripped)):
            return FirstCharTag.UPPERCASE
            
        # Default text classification - Fixed fallback
        if first_char.isalpha():
             return FirstCharTag.LOWERCASE # Includes mixed/sentence case
        else:
             # Includes lines starting ONLY with numbers (not matching enum), symbols etc.
             return FirstCharTag.SYMBOL


@dataclass
class LinePartitioner(Partitioner[str]):
    """Partitions input streams into lines."""

    def partition(self, input_stream: IO) -> Iterable[str]:
        if isinstance(input_stream, StringIO):
            # Reset position to beginning of file
            input_stream.seek(0)
            lines = input_stream.readlines()
            # Remove trailing newlines but preserve indentation
            lines = [line.rstrip('\n') for line in lines]
            return lines
        else:
            # Fallback to original method
            content = input_stream.read()
            lines = content.splitlines()
            return lines


@dataclass
class IndentationHierarchyRule(HierarchyRule[str, FirstCharTag]):
    """Determines parentage based on indentation levels."""

    def find_parent(
        self, entity: str, stack: List[tuple[str, 'Node[str, FirstCharTag]']], context: List[str]
    ) -> Optional[tuple[str, 'Node[str, FirstCharTag]']]:
        """Find the parent tuple based on indentation level."""
        if not entity:
            return None
            
        current_indent = len(entity) - len(entity.lstrip())
        if not stack:
            return None
        
        # Simplified logic: Find the last item on the stack with less indentation.
        for candidate_tuple in reversed(stack):
            candidate_entity = candidate_tuple[0] # Get the string entity
            if not candidate_entity:
                continue
                
            candidate_indent = len(candidate_entity) - len(candidate_entity.lstrip())
            if candidate_indent < current_indent:
                return candidate_tuple # Return the matching tuple
                
        # If no parent with less indentation is found, it's a root-level item for this context
        return None 


@dataclass
class PDFPartitioner(Partitioner[str]):
    """Partitions PDF documents into text lines."""
    
    def partition(self, input_stream: IO | str | Path) -> Iterable[str]:
        """Extract text from PDF document and split into lines.
        
        Args:
            input_stream: Path to PDF file or file-like object
            
        Returns:
            Iterable of text lines from the PDF
        """
        if not PDF_SUPPORT:
            raise ImportError("PDF support requires pymupdf. Install with: pip install pymupdf")
            
        # Handle different input types
        if isinstance(input_stream, (str, Path)):
            path = Path(input_stream)
            if not path.exists():
                raise FileNotFoundError(f"PDF file not found: {path}")
                
            # Extract text from PDF
            try:
                pdf_doc = pymupdf_open(path)
                lines = []
                
                # Extract text from each page
                for i in range(pdf_doc.page_count):
                    page = pdf_doc.load_page(i)
                    text = page.get_textpage().extractTEXT()
                    page_lines = text.split("\n")
                    
                    # Add page marker
                    lines.append(f"[PAGE {i+1}]")
                    lines.extend(page_lines)
                    
                return lines
            except Exception as e:
                raise RuntimeError(f"Error parsing PDF: {str(e)}")
        else:
            # For non-path inputs, fall back to regular line partitioning
            if hasattr(input_stream, 'read'):
                content = input_stream.read()
                return content.splitlines()
            else:
                raise ValueError("Input must be a path to a PDF file or a file-like object")


@dataclass
class PDFClassifier(Classifier[str, Union[FirstCharTag, PDFElementTag]]):
    """Classifies lines from PDF documents."""
    
    def classify(self, entity: str, context: Any = None) -> Union[FirstCharTag, PDFElementTag]:
        """Classify a line from a PDF document.
        
        Uses heuristics to determine the type of content.
        
        Args:
            entity: A line of text from a PDF
            context: Optional context information
            
        Returns:
            The appropriate tag for the line
        """
        # Check for page markers
        if entity.startswith("[PAGE ") and entity.endswith("]"):
            return PDFElementTag.PAGE
            
        # Use line classifier for regular text
        line_classifier = LineClassifier()
        line_tag = line_classifier.classify(entity)
        
        # Map certain line tags to PDF-specific tags
        if line_tag == FirstCharTag.HEADER:
            return PDFElementTag.HEADING
        elif line_tag == FirstCharTag.BULLET or line_tag == FirstCharTag.ENUMERATED:
            return PDFElementTag.LIST_ITEM
        elif line_tag == FirstCharTag.UPPERCASE and len(entity.strip()) > 20:
            # Long all-caps lines might be headings
            return PDFElementTag.HEADING
            
        # Default handling
        if entity and len(entity.strip()) > 0:
            return PDFElementTag.PARAGRAPH
        else:
            return FirstCharTag.WHITESPACE


@dataclass
class TagBasedHierarchyRule(HierarchyRule[str, Union[FirstCharTag, PDFElementTag]]):
    """Determines parentage based on semantic tags (e.g., Header, List Item)."""
    classifier: Classifier[str, Union[FirstCharTag, PDFElementTag]]

    def find_parent(
        self, 
        entity: str, 
        stack: List[tuple[str, Node[str, FirstCharTag | PDFElementTag]]],
        context: List[str]
    ) -> Optional[tuple[str, Node[str, FirstCharTag | PDFElementTag]]]:
        """Find parent based on the entity's tag and the stack context."""
        
        current_tag = self.classifier.classify(entity)

        # Simple Rules (can be expanded significantly):
        # 1. Headers clear the stack below them (become children of the root or previous higher-level header)
        if current_tag in [FirstCharTag.HEADER, PDFElementTag.HEADING, PDFElementTag.TITLE]:
            # Find the last header on the stack that is of a higher or equal level (e.g. H1 for H2)
            # For simplicity now, just find the last header/title.
            for i in range(len(stack) - 1, -1, -1):
                 parent_entity, parent_node = stack[i]
                 parent_tag = parent_node['tag']
                 # Basic check: parent is also a header/title
                 if parent_tag in [FirstCharTag.HEADER, PDFElementTag.HEADING, PDFElementTag.TITLE]:
                     # Simplistic level check: H2 follows H1, H3 follows H2 etc.
                     # Assumes headers are like '# title', '## title'
                     # This needs refinement for PDF tags or more complex headers.
                     current_level = entity.lstrip().find(' ')
                     parent_level = parent_entity.lstrip().find(' ')
                     if parent_tag == PDFElementTag.TITLE or current_level > parent_level:
                          return stack[i] # Return the found parent tuple
                     else:
                          continue # Keep searching up stack for appropriate header parent
                 # If we encounter non-header before finding suitable header parent, stop search for parent header
                 # break # Optional: stop searching if non-header encountered?

            return None # No suitable header parent found, becomes root or child of root header

        # 2. List items attach to the previous list item or the paragraph/header they follow
        elif current_tag in [FirstCharTag.BULLET, FirstCharTag.ENUMERATED, PDFElementTag.LIST_ITEM]:
            # Look for the most recent compatible parent
            for candidate_tuple in reversed(stack):
                candidate_tag = candidate_tuple[1]['tag']
                # List items can be children of other list items, paragraphs, or headers
                if candidate_tag in [
                    FirstCharTag.BULLET, FirstCharTag.ENUMERATED, PDFElementTag.LIST_ITEM,
                    FirstCharTag.LOWERCASE, PDFElementTag.PARAGRAPH,
                    FirstCharTag.HEADER, PDFElementTag.HEADING, PDFElementTag.TITLE
                ]:
                    # Add indentation check? Maybe list items must have >= indent than parent?
                    return candidate_tuple
            return None # Should ideally always find a parent unless it's the first element

        # 3. Paragraphs/Lowercase attach to the most recent item (header, list, paragraph)
        elif current_tag in [FirstCharTag.LOWERCASE, PDFElementTag.PARAGRAPH, FirstCharTag.SYMBOL, FirstCharTag.BOLD, FirstCharTag.ITALICIZED]:
             if stack:
                 return stack[-1] # Attach to the immediately preceding item
             else:
                 return None # First item
        
        # 4. Whitespace/Null: Attach to previous, or ignore?
        # For now, attach to previous like paragraph.
        elif current_tag in [FirstCharTag.WHITESPACE, FirstCharTag.NULL]:
             if stack:
                 return stack[-1]
             else:
                 return None

        # Default: Attach to the last item on the stack if available
        return stack[-1] if stack else None


@dataclass
class ConfigurableHierarchyRule(HierarchyRule[str, Union[FirstCharTag, PDFElementTag]]):
    """Determines parentage based on configurable markers and indentation."""
    classifier: Classifier[str, Union[FirstCharTag, PDFElementTag]]
    
    # Configurable Parameters
    header_tags: List[Union[FirstCharTag, PDFElementTag]] = field(
        default_factory=lambda: [FirstCharTag.HEADER, PDFElementTag.HEADING, PDFElementTag.TITLE])
    key_tags: List[Union[FirstCharTag, PDFElementTag]] = field(
        default_factory=lambda: [FirstCharTag.UPPERCASE]) # E.g., Man page options
    value_indent_threshold: int = 2 # Minimum indent increase to be considered a value/description
    list_item_tags: List[Union[FirstCharTag, PDFElementTag]] = field(
        default_factory=lambda: [FirstCharTag.BULLET, FirstCharTag.ENUMERATED, PDFElementTag.LIST_ITEM])
    # Tags that generally attach to the previous item
    follow_tags: List[Union[FirstCharTag, PDFElementTag]] = field(
        default_factory=lambda: [
            FirstCharTag.LOWERCASE, PDFElementTag.PARAGRAPH, FirstCharTag.SYMBOL, 
            FirstCharTag.BOLD, FirstCharTag.ITALICIZED,
            FirstCharTag.WHITESPACE, FirstCharTag.NULL # Treat whitespace/null as following previous
        ])

    def find_parent(
        self, entity: str, stack: List[tuple[str, 'Node[str, Union[FirstCharTag, PDFElementTag]]']], context: List[str]
    ) -> Optional[tuple[str, 'Node[str, Union[FirstCharTag, PDFElementTag]]']]:
        """Find parent based on the entity's tag and configurable rules."""

        current_tag = self.classifier.classify(entity)
        current_indent = len(entity) - len(entity.lstrip())

        if not stack:
            return None

        last_entity, last_node = stack[-1]
        last_tag = last_node['tag']
        last_indent = len(last_entity) - len(last_entity.lstrip())

        # 1. Header Rule: If current is a header tag
        if current_tag in self.header_tags:
            # Search for the nearest ancestor header it should belong to
            for i in range(len(stack) - 1, -1, -1):
                parent_entity, parent_node = stack[i]
                parent_tag = parent_node['tag']
                if parent_tag in self.header_tags:
                    # Simple level check (assumes #, ## etc or Title is highest)
                    # This is heuristic and might need refinement
                    def get_level(tag, text): 
                        if tag == PDFElementTag.TITLE: return 0
                        if tag in [FirstCharTag.HEADER, PDFElementTag.HEADING]: return text.lstrip().find(' ')
                        return float('inf') # Other tags aren't headers
                    
                    current_level = get_level(current_tag, entity)
                    parent_level = get_level(parent_tag, parent_entity)

                    if current_level > parent_level:
                        return stack[i] # Found suitable parent header
                    else:
                        continue # Keep searching up stack
            return None # No suitable parent header found

        # 2. Key-Value Rule: If previous was a key_tag and current is indented
        if last_tag in self.key_tags and current_indent > last_indent and (current_indent - last_indent) >= self.value_indent_threshold:
            return stack[-1] # Parent is the previous line (the key)

        # 3. List Item Rule: 
        if current_tag in self.list_item_tags:
             # Attach to previous list item at same/less indent, or parent paragraph/header
             for candidate_tuple in reversed(stack):
                 candidate_entity, candidate_node = candidate_tuple
                 candidate_tag = candidate_node['tag']
                 candidate_indent = len(candidate_entity) - len(candidate_entity.lstrip())
                 # Parent can be another list item (at same/less indent) or non-list container
                 if candidate_tag in self.list_item_tags and candidate_indent <= current_indent:
                      return candidate_tuple
                 elif candidate_tag not in self.list_item_tags:
                      # Found potential non-list parent, ensure it's not too indented?
                      # Basic: attach if parent indent is less than current
                      if candidate_indent < current_indent:
                          return candidate_tuple
                      # Otherwise, continue search for suitable parent
             return None # No suitable parent found
        
        # 4. Follower Rule: Attach to previous item if tag matches follow_tags
        if current_tag in self.follow_tags:
             # Check if the current indent makes sense following the last item
             # e.g., don't attach significantly less indented item to much more indented one
             if current_indent >= last_indent:
                  return stack[-1]
             else:
                  # Current item is less indented than last, search for appropriate parent
                  pass # Fall through to indentation decrease rule

        # 5. Indentation Decrease Rule (Fallback)
        # Find the last item on the stack with strictly less indentation
        for candidate_tuple in reversed(stack):
            candidate_entity = candidate_tuple[0]
            candidate_indent = len(candidate_entity) - len(candidate_entity.lstrip())
            if candidate_indent < current_indent:
                return candidate_tuple

        # Default: No parent found
        return None


def build_text_hierarchy(
    input_stream: IO, 
    hierarchy_rule: Optional[HierarchyRule[str, FirstCharTag]] = None
) -> List[Node[str, FirstCharTag]]:
    """Builds a hierarchical structure from text lines using a specified rule."""
    classifier = LineClassifier()
    # Default to Indentation rule if none provided
    rule = hierarchy_rule if hierarchy_rule is not None else IndentationHierarchyRule()
    
    builder = StructureBuilder(
        classifier=classifier,
        partitioner=LinePartitioner(),
        hierarchy_rule=rule, # Pass the chosen rule
    )
    return builder.process(input_stream)


def build_pdf_hierarchy(
    input_path: str | Path, 
    hierarchy_rule: Optional[HierarchyRule[str, Union[FirstCharTag, PDFElementTag]]] = None
) -> List[Node[str, Union[FirstCharTag, PDFElementTag]]]:
    """Builds a hierarchical structure from a PDF document using a specified rule."""
    if not PDF_SUPPORT:
        raise ImportError("PDF support requires pymupdf. Install with: pip install pymupdf")
        
    classifier = PDFClassifier()
    # Default to TagBased rule for PDF if none provided, as indentation is less reliable
    rule = hierarchy_rule if hierarchy_rule is not None else TagBasedHierarchyRule(classifier=classifier)
        
    builder = StructureBuilder(
        classifier=classifier,
        partitioner=PDFPartitioner(),
        hierarchy_rule=rule, # Pass the chosen rule
    )
    return builder.process(input_path)


def is_pdf_file(path: str | Path) -> bool:
    """Check if a file is a PDF based on extension."""
    return str(path).lower().endswith('.pdf')


# CLI needs to know about tags for argparse
TAG_CHOICES = [tag.value for tag in FirstCharTag] + [tag.value for tag in PDFElementTag]

def cli(input_path: str | None = None, 
        rule_name: str = 'indentation', 
        rule_params: Dict[str, Any] = {}) -> None:
    """Command line interface for parsing text/PDF into a hierarchical JSON structure.

    Reads input from a specified file path or standard input (stdin).
    Outputs a JSON representation of the hierarchical structure to standard output (stdout).

    Allows choosing different hierarchy building rules:
      - indentation: Based purely on changes in line indentation (Default for text).
      - tagbased: Uses hardcoded logic based on semantic tags (HEADER, LIST_ITEM etc.).
      - configurable: Uses semantic tags, but behavior is controlled by CLI parameters 
                      (like --key-tags, --value-indent). (Default for PDF).

    Examples:

    1. Process text file using default indentation rule:
       $ python mbpy/parse/online.py input.txt

    2. Process text from stdin using default indentation rule:
       $ cat input.txt | python mbpy/parse/online.py
    
    3. Process PDF file using default configurable rule (suitable for PDFs):
       $ python mbpy/parse/online.py document.pdf 
       # Equivalent to: python mbpy/parse/online.py --rule configurable document.pdf

    4. Process text file explicitly using the tagbased rule:
       $ python mbpy/parse/online.py --rule tagbased input.txt

    5. Process PDF explicitly using the indentation rule (may be less accurate):
       $ python mbpy/parse/online.py --rule indentation document.pdf

    6. Process text using the configurable rule, treating UPPERCASE lines as keys 
       and requiring >= 4 spaces indent for values:
       $ cat input.txt | python mbpy/parse/online.py --rule configurable --key-tags UPPERCASE --value-indent 4

    7. Process text using configurable rule, defining specific header tags:
       $ python mbpy/parse/online.py --rule configurable --header-tags HEADER TITLE input.txt
    """
    hierarchy: List[Node[Any, Any]] = []
    selected_rule: HierarchyRule[Any, Any] | None = None
    classifier: Classifier[str, Any] | None = None # Hold the classifier instance
    is_pdf = False
    
    try:
        # Determine input source and type
        input_source: IO | Path | None = None
        if input_path:
            input_path_obj = Path(input_path)
            if not input_path_obj.exists():
                print(f"Error: File '{input_path}' not found.", file=sys.stderr)
                sys.exit(1)
            is_pdf = is_pdf_file(input_path_obj)
            input_source = input_path_obj
        elif not sys.stdin.isatty():
            input_source = StringIO(sys.stdin.read()) # Read from stdin
        else:
            print("No input provided. Pipe content or provide a file path.", file=sys.stderr)
            sys.exit(1)

        # Instantiate the appropriate Classifier first
        if is_pdf:
            if not PDF_SUPPORT:
                print("PDF support requires pymupdf. Install with: pip install pymupdf", file=sys.stderr)
                sys.exit(1)
            # Use ParameterizedLineClassifier within PDFClassifier?
            # For now, keep PDFClassifier simpler
            classifier = PDFClassifier()
        else:
            # Use ParameterizedLineClassifier for text, potentially with CLI args later
            # For now, use defaults
            classifier = ParameterizedLineClassifier() 

        # Instantiate the selected HierarchyRule, passing the classifier
        if rule_name == 'configurable':
            # Pass rule parameters from CLI/defaults
            selected_rule = ConfigurableHierarchyRule(classifier=classifier, **rule_params) 
        elif rule_name == 'tagbased':
            selected_rule = TagBasedHierarchyRule(classifier=classifier)
        elif rule_name == 'indentation':
            selected_rule = IndentationHierarchyRule()
        else: # Default (should match argparse default)
            if is_pdf:
                 selected_rule = ConfigurableHierarchyRule(classifier=classifier, **rule_params)
                 # selected_rule = TagBasedHierarchyRule(classifier=classifier) # Original PDF default
            else:
                 selected_rule = IndentationHierarchyRule()

        # --- Process Input --- 
        if is_pdf:
            hierarchy = build_pdf_hierarchy(cast(Path, input_source), hierarchy_rule=selected_rule)
        else: # Text input (from file handle or StringIO)
            if isinstance(input_source, Path):
                 with open(input_source, "r") as f:
                     hierarchy = build_text_hierarchy(f, hierarchy_rule=selected_rule)
            elif isinstance(input_source, StringIO):
                 hierarchy = build_text_hierarchy(input_source, hierarchy_rule=selected_rule)
            else:
                 raise TypeError("Invalid input source type for text processing")

        # --- Output --- 
        def convert_hierarchy(nodes):
            if isinstance(nodes, list): return [convert_node(node) for node in nodes]
            return convert_node(nodes)
        def convert_node(node):
            if not isinstance(node, dict): return str(node)
            tag = node["tag"]
            tag_value = tag.value if hasattr(tag, 'value') else str(tag)
            content = "".join(node["content"]).rstrip()
            children = [convert_node(child) for child in node["children"]]
            return {"tag": tag_value, "content": content, "children": children}
        
        json_structure = convert_hierarchy(hierarchy)
        json.dump(json_structure, sys.stdout, indent=2)
        print()
        
    except Exception as e:
        import traceback
        traceback.print_exc()
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    import argparse
    
    # Hardcode default values in help strings for simplicity
    default_header_tags_str = ['header', 'heading', 'title'] 
    default_key_tags_str = ['allcaps']
    default_value_indent = 2 # Default from ConfigurableHierarchyRule
    default_list_tags_str = ['bullet', 'enumerated', 'list_item']
    default_follow_tags_str = ['lowercase', 'paragraph', 'symbol', 'bold', 'italicized', 'whitespace', 'null']
    
    parser = argparse.ArgumentParser(description="Parse text or PDF into a hierarchical JSON structure.")
    parser.add_argument("input_path", nargs='?', help="Path to the input text or PDF file. Reads from stdin if omitted.")
    parser.add_argument("--rule", choices=['indentation', 'tagbased', 'configurable'], default=None, 
                        help="Hierarchy rule ('indentation', 'tagbased', 'configurable'). Default: 'indentation' for text, 'configurable' for PDF.")
    
    # Arguments for ConfigurableHierarchyRule with hardcoded defaults in help
    parser.add_argument("--header-tags", nargs='+', default=None, choices=TAG_CHOICES, 
                        help=f"Tags indicating a header (default: {default_header_tags_str})")
    parser.add_argument("--key-tags", nargs='+', default=None, choices=TAG_CHOICES, 
                        help=f"Tags indicating a key/option (default: {default_key_tags_str})")
    parser.add_argument("--value-indent", type=int, default=None, 
                        help=f"Min indent increase for value following key (default: {default_value_indent})")
    parser.add_argument("--list-item-tags", nargs='+', default=None, choices=TAG_CHOICES, 
                        help=f"Tags indicating list items (default: {default_list_tags_str})")
    parser.add_argument("--follow-tags", nargs='+', default=None, choices=TAG_CHOICES, 
                        help=f"Tags that follow previous item (default: {default_follow_tags_str})")

    args = parser.parse_args()

    # Determine input type and default rule
    is_pdf = args.input_path and is_pdf_file(args.input_path)
    rule_to_use = args.rule
    if rule_to_use is None:
        rule_to_use = 'configurable' if is_pdf else 'indentation' # Default to configurable for PDF

    # Collect parameters for ConfigurableHierarchyRule from args
    rule_params = {}
    if rule_to_use == 'configurable':
        def get_tag_enum(tag_str):
            for enum_cls in [FirstCharTag, PDFElementTag]:
                try: return enum_cls(tag_str) 
                except ValueError: pass
            print(f"Warning: Unknown tag '{tag_str}' specified, ignoring.", file=sys.stderr)
            return None 

        if args.header_tags:
             rule_params['header_tags'] = [t for t in (get_tag_enum(tag) for tag in args.header_tags) if t is not None]
        if args.key_tags:
             rule_params['key_tags'] = [t for t in (get_tag_enum(tag) for tag in args.key_tags) if t is not None]
        if args.value_indent is not None: 
             rule_params['value_indent_threshold'] = args.value_indent
        if args.list_item_tags: 
             rule_params['list_item_tags'] = [t for t in (get_tag_enum(tag) for tag in args.list_item_tags) if t is not None]
        if args.follow_tags: 
             rule_params['follow_tags'] = [t for t in (get_tag_enum(tag) for tag in args.follow_tags) if t is not None]

    cli(input_path=args.input_path, rule_name=rule_to_use, rule_params=rule_params)

# --- Simplified Builder --- 

class SimpleNode(TypedDict):
    """Simplified node structure for the SimpleIndentationBuilder."""
    tag: Union[FirstCharTag, PDFElementTag] # Use existing tags
    content: str # Store the single line content
    indent: int
    children: List['SimpleNode']

@dataclass
class SimpleIndentationBuilder:
    """Builds hierarchy based purely on indentation changes."""
    classifier: Classifier[str, Union[FirstCharTag, PDFElementTag]]
    # Stack stores tuples of (indent_level, node_reference)
    stack: List[Tuple[int, SimpleNode]] = field(default_factory=list)
    root_nodes: List[SimpleNode] = field(default_factory=list)

    def _get_indent(self, line: str) -> int:
        return len(line) - len(line.lstrip(' \t')) # Ignore only space/tab for indent

    def build(self, input_stream: IO) -> List[SimpleNode]:
        """Processes the stream and returns the list of root nodes."""
        partitioner = LinePartitioner()
        lines = partitioner.partition(input_stream)

        for line in lines:
            stripped_line = line.strip()
            # Skip lines that are purely whitespace
            if not stripped_line:
                continue 

            current_indent = self._get_indent(line)
            current_tag = self.classifier.classify(line)
            
            new_node = SimpleNode(
                tag=current_tag, 
                content=line, # Store original line with indent
                indent=current_indent, 
                children=[]
            )

            # Pop stack while current indent is less than or equal to top indent
            while self.stack and self.stack[-1][0] >= current_indent:
                self.stack.pop()

            # Now stack top indent is < current_indent (or stack is empty)
            if self.stack:
                parent_node = self.stack[-1][1] # Get parent node from stack top
                parent_node['children'].append(new_node)
            else:
                # No suitable parent on stack, add to root
                self.root_nodes.append(new_node)

            # Push the new node and its indent level onto the stack
            self.stack.append((current_indent, new_node))
            
        return self.root_nodes

def build_simple_indentation_hierarchy(
    input_stream: IO, 
    classifier: Optional[Classifier[str, Union[FirstCharTag, PDFElementTag]]] = None
) -> List[SimpleNode]:
    """Helper function to build hierarchy using SimpleIndentationBuilder."""
    # Default to ParameterizedLineClassifier if none provided
    clf = classifier if classifier is not None else ParameterizedLineClassifier()
    builder = SimpleIndentationBuilder(classifier=clf)
    return builder.build(input_stream)
