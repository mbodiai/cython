# """
# MBPy Parse Module - Tools for parsing and analyzing structured text and documents.
# """

# from mbpy.parse.online import (
#     # Core classes
#     Classifier,
#     Partitioner,
#     HierarchyRule,
#     Node,
#     StructureBuilder,
    
#     # Text parsing
#     FirstCharTag,
#     LineClassifier,
#     LinePartitioner,
#     IndentationHierarchyRule,
#     build_text_hierarchy,
    
#     # PDF parsing (may require additional dependencies)
#     PDF_SUPPORT,
# )

# # Conditionally expose PDF parsing functionality
# try:
#     from mbpy.parse.online import (
#         PDFElementTag,
#         PDFPartitioner,
#         PDFClassifier,
#         build_pdf_hierarchy,
#         is_pdf_file,
#     )
# except ImportError:
#     # PDF support not available
#     pass

# __all__ = [
#     # Core classes
#     "Classifier",
#     "Partitioner",
#     "HierarchyRule",
#     "Node",
#     "StructureBuilder",
    
#     # Text parsing
#     "FirstCharTag",
#     "LineClassifier",
#     "LinePartitioner", 
#     "IndentationHierarchyRule",
#     "build_text_hierarchy",
    
#     # PDF parsing flag
#     "PDF_SUPPORT",
# ]

# # Add PDF parsing exports if available
# if PDF_SUPPORT:
#     __all__ += [
#         "PDFElementTag",
#         "PDFPartitioner",
#         "PDFClassifier",
#         "build_pdf_hierarchy",
#         "is_pdf_file",
#     ]
