"""
Tests for PDF parsing functionality in the online module.
"""

import os
import sys
import json
from io import StringIO
from pathlib import Path
import pytest

try:
    from mbpy.parse.online import (
        build_pdf_hierarchy,
        is_pdf_file,
        PDFPartitioner,
        PDFClassifier,
        PDF_SUPPORT,
    )
except ImportError:
    # Skip tests if module not available
    pytestmark = pytest.mark.skip("PDF parsing module not available")

# Skip all tests if pymupdf is not installed
pytestmark = pytest.mark.skipif(
    not PDF_SUPPORT, reason="pymupdf is not installed"
)

def test_is_pdf_file():
    """Test PDF file detection."""
    assert is_pdf_file("test.pdf") is True
    assert is_pdf_file("test.PDF") is True
    assert is_pdf_file("test.txt") is False
    assert is_pdf_file("test") is False

@pytest.mark.skipif(
    not os.path.exists("../minspect/findings.pdf"),
    reason="Test PDF file not found"
)
def test_pdf_partitioner():
    """Test PDF partitioning functionality."""
    # This test relies on a sample PDF file
    sample_pdf = Path("../minspect/findings.pdf")
    if not sample_pdf.exists():
        pytest.skip(f"Test PDF file not found: {sample_pdf}")
    
    partitioner = PDFPartitioner()
    lines = list(partitioner.partition(sample_pdf))
    
    # Basic checks
    assert len(lines) > 0
    # First line should be a page marker
    assert lines[0].startswith("[PAGE ")
    
    # Check that content was extracted
    text_lines = [line for line in lines if not line.startswith("[PAGE ")]
    assert len(text_lines) > 0

@pytest.mark.skipif(
    not os.path.exists("../minspect/findings.pdf"),
    reason="Test PDF file not found"
)
def test_build_pdf_hierarchy():
    """Test building PDF hierarchy."""
    sample_pdf = Path("../minspect/findings.pdf")
    if not sample_pdf.exists():
        pytest.skip(f"Test PDF file not found: {sample_pdf}")
    
    hierarchy = build_pdf_hierarchy(sample_pdf)
    
    # Basic structure checks
    assert isinstance(hierarchy, list)
    assert len(hierarchy) > 0
    
    # Check node structure
    first_node = hierarchy[0]
    assert "tag" in first_node
    assert "content" in first_node
    assert "children" in first_node
    
    # Redirect stdout to capture JSON output
    orig_stdout = sys.stdout
    sys.stdout = StringIO()
    
    # Run the CLI function on the PDF
    from mbpy.parse.online import cli
    cli(str(sample_pdf))
    
    # Get the captured output
    output = sys.stdout.getvalue()
    sys.stdout = orig_stdout
    
    # Verify JSON output
    assert output.strip()
    try:
        json_data = json.loads(output.strip())
        assert isinstance(json_data, list)
    except json.JSONDecodeError:
        assert False, "CLI did not produce valid JSON" 