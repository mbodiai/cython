import ast
import os
from dataclasses import dataclass
from typing import Any, Dict, List, Optional

try:
    from pydantic import BaseModel
    from pylint.graph import DotBackend
    from pylint.lint import Run as PylintRun
except ImportError:
    raise ImportError("Please install pydantic and pylint to use this module.")


def generate_graph(name: str, tree: ast.AST) -> None:
    """Generate graph from AST tree."""
    DotBackend(name)


@dataclass
class ASTNode:
    type: str
    fields: Dict[str, Any]
    children: List["ASTNode"]
    lineno: Optional[int] = None


class LintResult(BaseModel):
    """Result of linting and AST analysis."""

    lint_results: str
    ast_tree: Dict[str, Any]
    source_map: Dict[int, str]
    errors: Optional[str] = None


def ast_to_dict(node: ast.AST) -> Dict:
    """Convert AST node to comparable dictionary structure."""
    if not isinstance(node, ast.AST):
        return node

    return {
        "type": node.__class__.__name__,
        "fields": {
            field: ast_to_dict(getattr(node, field))
            for field in node._fields
            if hasattr(node, field)
        },
        "lineno": getattr(node, "lineno", None),
    }


def lint_to_ast(code: str) -> "LintResult":
    """Create AST and source mapping for diff comparison."""
    tmp_dir = "tmp"
    os.makedirs(tmp_dir, exist_ok=True)

    tmp_path = os.path.join(tmp_dir, f"lint_{hash(code)}.py")

    try:
        with open(tmp_path, "w") as tmp:
            tmp.write(code)

        # Parse AST
        tree = ast.parse(code)

        # Create source mapping
        source_map = {}
        for node in ast.walk(tree):
            if isinstance(node, ast.stmt):
                source_map[node.lineno] = code.split("\n")[node.lineno - 1]

        # Run pylint
        lint_output = ""
        try:
            (pylint_stdout, _) = PylintRun(tmp_path, return_std=True)
            lint_output = pylint_stdout.getvalue()
        except Exception as e:
            lint_output = f"Lint error: {str(e)}"

        return LintResult(
            lint_results=lint_output,
            ast_tree=ast_to_dict(tree),
            source_map=source_map,
            errors=None,
        )
    except Exception as e:
        return LintResult(lint_results="", ast_tree={}, source_map={}, errors=str(e))
    finally:
        if os.path.exists(tmp_path):
            os.unlink(tmp_path)


__all__ = ["LintResult", "ASTNode", "lint_to_ast"]
