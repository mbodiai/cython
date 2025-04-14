# MBPy Parse Module

The `parse` module provides tools for parsing and analyzing different types of structured text, including plain text and PDF documents.

## Features

### Text Parsing

- Hierarchical text structure analysis based on indentation and text characteristics
- Classification of text elements (headers, bullets, paragraphs, etc.)
- Customizable partitioning and classification rules

### PDF Parsing

- Extract text content from PDF documents
- Preserve page structure with page markers
- Classify PDF content into semantic elements (headings, paragraphs, lists)
- Convert PDF structure to hierarchical JSON representation

## Requirements

Basic text parsing has no external dependencies. PDF parsing requires:

```
pymupdf>=1.24.11
```

## Usage

### Command Line

Process a text file:
```bash
python -m mbpy.parse.online path/to/textfile.txt
```

Process a PDF file:
```bash
python -m mbpy.parse.online path/to/document.pdf
```

Process text from stdin:
```bash
cat file.txt | python -m mbpy.parse.online
```

### API Usage

```python
from io import StringIO
from mbpy.parse.online import build_text_hierarchy, build_pdf_hierarchy

# Parse text
with open("document.txt", "r") as f:
    text_content = f.read()
    hierarchy = build_text_hierarchy(StringIO(text_content))

# Parse PDF
pdf_hierarchy = build_pdf_hierarchy("document.pdf")
```

## Architecture

The module uses a flexible architecture with three main components:

1. **Partitioner**: Splits input into entities (e.g., lines of text)
2. **Classifier**: Tags entities with their semantic role
3. **Hierarchy Rule**: Determines parent-child relationships between entities

This architecture allows for extending the parser to handle different document types while maintaining a consistent output format. 