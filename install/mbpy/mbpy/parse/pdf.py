"""
PDF parsing functionality for extracting structured content from PDF files.
"""

import json
import sys
from io import StringIO
from pathlib import Path
from typing import Dict, List, Optional, Any, Union, Iterator

try:
    from pymupdf import Page, TextPage, open as pymupdf_open
    PDF_SUPPORT = True
except ImportError:
    PDF_SUPPORT = False


class PDFParseError(Exception):
    """Exception raised for errors during PDF parsing."""
    pass


class PDFDocument:
    """Representation of a PDF document with extracted content."""
    
    def __init__(self, path: Union[str, Path]):
        """Initialize a PDF document from a file path.
        
        Args:
            path: Path to the PDF file
        
        Raises:
            PDFParseError: If the file doesn't exist or can't be parsed
            ImportError: If pymupdf is not installed
        """
        if not PDF_SUPPORT:
            raise ImportError("PDF support requires pymupdf. Install with: pip install pymupdf>=1.24.11")
        
        self.path = Path(path)
        if not self.path.exists():
            raise PDFParseError(f"PDF file not found: {self.path}")
        
        try:
            self._doc = pymupdf_open(self.path)
            self.page_count = self._doc.page_count
            self.metadata = self._doc.metadata or {}
            self.title = self.metadata.get("title", self.path.stem)
            self._pages = []
        except Exception as e:
            raise PDFParseError(f"Error opening PDF: {str(e)}")
    
    def extract_text(self) -> str:
        """Extract all text from the PDF document.
        
        Returns:
            The full text content of the PDF
        """
        text_parts = []
        for i in range(self.page_count):
            text_parts.append(self.extract_page_text(i))
        return "\n\n".join(text_parts)
    
    def extract_page_text(self, page_num: int) -> str:
        """Extract text from a specific page.
        
        Args:
            page_num: Zero-based page number
            
        Returns:
            The text content of the page
            
        Raises:
            PDFParseError: If the page can't be accessed
        """
        if page_num < 0 or page_num >= self.page_count:
            raise PDFParseError(f"Invalid page number: {page_num}")
        
        try:
            page = self._doc.load_page(page_num)
            text = page.get_textpage().extractTEXT()
            return text
        except Exception as e:
            raise PDFParseError(f"Error extracting text from page {page_num}: {str(e)}")
    
    def extract_pages(self) -> List[Dict[str, Any]]:
        """Extract content from all pages.
        
        Returns:
            List of page dictionaries with text, blocks, and other information
        """
        if not self._pages:
            self._pages = [self._extract_page_content(i) for i in range(self.page_count)]
        return self._pages
    
    def _extract_page_content(self, page_num: int) -> Dict[str, Any]:
        """Extract detailed content from a page.
        
        Args:
            page_num: Zero-based page number
            
        Returns:
            Dictionary with page content details
        """
        page = self._doc.load_page(page_num)
        text = page.get_textpage().extractTEXT()
        
        return {
            "page_number": page_num + 1,
            "text": text,
            "lines": text.split("\n"),
            "blocks": page.get_textpage().extractBLOCKS(),
            "has_images": bool(page.get_images(full=False))
        }
    
    def extract_lines(self) -> List[str]:
        """Extract all text lines from the document.
        
        Returns:
            List of text lines from all pages
        """
        lines = []
        for i in range(self.page_count):
            page_text = self.extract_page_text(i)
            page_lines = page_text.split("\n")
            lines.extend(page_lines)
        return lines
    
    def extract_structure(self) -> Dict[str, Any]:
        """Extract the document structure including metadata and content.
        
        Returns:
            Dictionary with document structure
        """
        return {
            "metadata": self.metadata,
            "title": self.title,
            "page_count": self.page_count,
            "pages": self.extract_pages(),
            "text": self.extract_text()
        }


def parse_pdf(pdf_path: Union[str, Path]) -> Dict[str, Any]:
    """Parse a PDF file and return its structure.
    
    Args:
        pdf_path: Path to the PDF file
        
    Returns:
        Dictionary with document structure
        
    Raises:
        PDFParseError: If the PDF can't be parsed
        ImportError: If pymupdf is not installed
    """
    doc = PDFDocument(pdf_path)
    return doc.extract_structure()


def pdf_to_text(pdf_path: Union[str, Path]) -> str:
    """Extract all text from a PDF file.
    
    Args:
        pdf_path: Path to the PDF file
        
    Returns:
        The full text content of the PDF
        
    Raises:
        PDFParseError: If the PDF can't be parsed
        ImportError: If pymupdf is not installed
    """
    doc = PDFDocument(pdf_path)
    return doc.extract_text()


def pdf_to_lines(pdf_path: Union[str, Path]) -> List[str]:
    """Extract all text lines from a PDF file.
    
    Args:
        pdf_path: Path to the PDF file
        
    Returns:
        List of text lines from the PDF
        
    Raises:
        PDFParseError: If the PDF can't be parsed
        ImportError: If pymupdf is not installed
    """
    doc = PDFDocument(pdf_path)
    return doc.extract_lines()


def main():
    """Command-line interface for PDF parsing."""
    if not PDF_SUPPORT:
        print("Error: PDF support requires pymupdf.")
        print("Install with: pip install pymupdf>=1.24.11")
        return 1
    
    if len(sys.argv) < 2:
        print("Usage: python -m mbpy.parse.pdf <pdf_file> [output_file]")
        return 1
    
    pdf_path = sys.argv[1]
    output_format = "text"
    
    if len(sys.argv) > 2:
        output_file = sys.argv[2]
        if output_file.endswith(".json"):
            output_format = "json"
    else:
        output_file = None
    
    try:
        doc = PDFDocument(pdf_path)
        print(f"PDF: {pdf_path}")
        print(f"Pages: {doc.page_count}")
        print(f"Title: {doc.title}")
        
        if output_format == "json":
            result = doc.extract_structure()
            if output_file:
                with open(output_file, "w") as f:
                    json.dump(result, f, indent=2)
                print(f"JSON output saved to {output_file}")
            else:
                print(json.dumps(result, indent=2))
        else:
            text = doc.extract_text()
            if output_file:
                with open(output_file, "w") as f:
                    f.write(text)
                print(f"Text output saved to {output_file}")
            else:
                print(text)
        
        return 0
        
    except (PDFParseError, ImportError) as e:
        print(f"Error: {str(e)}")
        return 1


if __name__ == "__main__":
    sys.exit(main()) 