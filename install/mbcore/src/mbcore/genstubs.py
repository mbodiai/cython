# import importlib
# import inspect
# import json
# import os
# import sys
# from pathlib import Path
# from typing_extensions import Any, Dict, List, Set, TypedDict, TYPE_CHECKING
# from mbcore.import_utils import smart_import
# from mbcore.log import error, info, warning
# from mbcore.traverse import find_file as find
# from mypy.nodes import ClassDef, FuncDef, MypyFile
# from mypy.options import Options as MypyOptions
# from mypy.stubgen import Options as StubgenOptions
# from mypy.stubgen import generate_asts_for_modules, generate_stubs, StubSource
# class TreeNode(TypedDict):
#     name: str
#     kind: str  # 'module', 'class', 'function', 'variable'
#     signature: str | None
#     docstring: str | None
#     source: str | None
#     children: List['TreeNode']
#     decorators: List[str]
#     is_private: bool


# if TYPE_CHECKING:
#     class BuildSource:
#         """A single source file."""

#         def __init__(
#             self,
#             path: str | None,
#             module: str | None,
#             text: str | None = None,
#             base_dir: str | None = None,
#             followed: bool = False,
#         ) -> None:
#             self.path = path  # File where it's found (e.g. 'xxx/yyy/foo/bar.py')
#             self.module = module or "__main__"  # Module name (e.g. 'foo.bar')
#             self.text = text  # Source code, if initially supplied, else None
#             self.base_dir = base_dir  # Directory where the package is rooted (e.g. 'xxx/yyy')
#             self.followed = followed  # Was this found by following imports?

#         def __repr__(self) -> str:
#             return (
#                 f"BuildSource(path={self.path!r}, module={self.module!r}, has_text={self.text is not None}, base_dir={self.base_dir!r}, followed={self.followed})"
#             )
# class StubGenerator:
#     def __init__(
#         self,
#         modules: List[str],
#         output_dir: str = "typings",
#         include_private: bool = True,
#         include_source: bool = True,
#     ):
#         self.modules = modules
#         self.imported = []
#         self.output_dir = Path(output_dir)
#         self.include_source = include_source

#         # Get Python version tuple
#         version_info = sys.version_info[:2]

#         # Create minimal mypy options - only use essential attributes
#         mypy_opts = MypyOptions()
#         mypy_opts.python_version = version_info
#         mypy_opts.show_traceback = True
#         mypy_opts.follow_imports = "silent"  # Don't complain about missing imports
#         mypy_opts.ignore_missing_imports = True
#         mypy_opts.platform = sys.platform

#         # Add paths to mypy search path
#         cwd = str(Path.cwd())
#         if not hasattr(mypy_opts, 'mypy_path'):
#             mypy_opts.mypy_path = []
#         mypy_opts.mypy_path.append(cwd)
#         self.mypy_opts = mypy_opts

#         # Create stubgen options with proper search path
#         search_paths = [cwd]
#         if "PYTHONPATH" in os.environ:
#             search_paths.extend(os.environ["PYTHONPATH"].split(os.pathsep))

#         self.opts = StubgenOptions(
#             pyversion=version_info,
#             no_import=False,
#             inspect=True,
#             doc_dir="",
#             search_path=search_paths,
#             interpreter=sys.executable,
#             parse_only=False,
#             ignore_errors=True,  # Changed to True to handle errors gracefully
#             include_private=include_private,
#             output_dir=str(self.output_dir),
#             modules=self.modules,
#             packages=[],
#             files=[],
#             verbose=True,
#             quiet=False,
#             export_less=False,
#             include_docstrings=True,
#         )
#         self.output_dir.mkdir(parents=True, exist_ok=True)
#         self.processed_modules: Set[str] = set()

#     def extract_signature(self, node: Any) -> str | None:
#         try:
#             if isinstance(node, (ClassDef | FuncDef)):
#                 return str(node.type.signature()) if hasattr(node, 'type') else None
#             return None
#         except Exception:
#             return None

#     def process_node(self, node: Any, module: Any) -> TreeNode:
#         name = getattr(node, 'name', '')
#         kind = self._get_node_kind(node)
#         docstring = inspect.getdoc(node) if inspect.ismodule(module) else None

#         tree_node = TreeNode(
#             name=name,
#             kind=kind,
#             signature=self.extract_signature(node),
#             docstring=docstring,
#             source=self._get_source(node) if self.include_source else None,
#             children=[],
#             decorators=self._get_decorators(node),
#             is_private=name.startswith('_'),
#         )

#         if hasattr(node, 'defs'):
#             for child in node.defs:
#                 if self._should_include_node(child):
#                     tree_node['children'].append(self.process_node(child, module))

#         return tree_node

#     def _get_node_kind(self, node: Any) -> str:
#         if isinstance(node, MypyFile):
#             return 'module'
#         if isinstance(node, ClassDef):
#             return 'class'
#         if isinstance(node, FuncDef):
#             return 'function'
#         return 'variable'

#     def _should_include_node(self, node: Any) -> bool:
#         if not hasattr(node, 'name'):
#             return False
#         return (self.opts.include_private or
#                 not node.name.startswith('_'))

#     def _get_source(self, node: Any) -> str | None:
#         try:
#             return inspect.getsource(node)
#         except Exception:
#             return None

#     def _get_decorators(self, node: Any) -> List[str]:
#         if hasattr(node, 'decorators'):
#             return [d.name for d in node.decorators]
#         return []

#     def _import_module(self, module_name: str) -> bool:
#         """Safely import a module and return success status."""
#         info(f"Importing module {module_name} in {Path.cwd()}")
#         try:
#             if module_name not in sys.modules:

#                self.imported.append(smart_import(module_name))
#             return True
#         except ImportError as e:
#             warning(f"Warning: Could not import module {module_name}: {e}")
#             import traceback
#             traceback.print_exc()
#             return False

#     def generate_for_modules(self) -> Dict[str, List[TreeNode]]:
#         result = {}
#         for module_name in self.modules:
#             if not self._import_module(module_name):
#                 continue

#             if module_name in self.processed_modules:
#                 continue

#             self.processed_modules.add(module_name)
#             try:
#                 # Find the module file path
#                 module = sys.modules.get(module_name)
#                 if not module:
#                     warning(f"Could not find module {module_name}")
#                     continue

#                 module_path = getattr(module, '__file__', None)
#                 if not module_path:
#                     warning(f"No file path found for module {module_name}")
#                     continue

#                 # Create StubSource with proper path
#                 stub_sources = [StubSource(module=module_name, path=module_path)]
#                 asts = generate_asts_for_modules(
#                     stub_sources,
#                     parse_only=True,
#                     mypy_options=self.mypy_opts,
#                     verbose=True
#                 )
#                 if not asts:
#                     continue

#                 module_trees = []
#                 for ast_node in asts:
#                     tree = self.process_node(ast_node, sys.modules.get(module_name))
#                     module_trees.append(tree)

#                 result[module_name] = module_trees

#             except Exception as e:
#                 error(f"Error processing module {module_name}: {e}")
#                 import traceback
#                 traceback.print_exc()

#         return result

#     def save_trees(self, trees: Dict[str, List[TreeNode]], output_file: str = 'ast_trees.json') -> None:
#         output_path = self.output_dir / output_file
#         output_path.write_text(json.dumps(trees, indent=2), encoding='utf-8')

#     def generate_stubs(self) -> None:
#         try:
#             # Create StubSource instead of BuildSource
#             stub_sources = [StubSource(module=m) for m in self.modules]
#             asts = generate_asts_for_modules(
#                 stub_sources,
#                 parse_only=True,
#                 mypy_options=self.mypy_opts,
#                 verbose=True
#             )
#             if not asts:
#                 warning("No ASTs generated")
#                 return

#             stubs = generate_stubs(asts, self.opts)
#             if not stubs:
#                 warning("No stubs generated")
#                 return

#             for stub in stubs:
#                 if stub.path:
#                     stub_path = self.output_dir / f"{stub.module}.pyi"
#                     stub_path.parent.mkdir(parents=True, exist_ok=True)
#                     stub_path.write_text(stub.output)
#         except Exception as e:
#             error(f"Error generating stubs: {e}")

# def main() -> None:
#     # First test with just the test module
#     test_module_path = "tmp.test_module"

#     # Create test module if it doesn't exist
#     test_module_file = "tmp/test_module.py"
#     test_module_file = Path(test_module_file)
#     test_module_file.parent.mkdir(parents=True, exist_ok=True)

#     if not test_module_file.exists():
#         test_module_content = '''
# class BaseClass:
#     """Base test class."""
#     pass

# class TestClass(BaseClass):
#     """Test class for stub generation."""
#     PUBLIC_CONSTANT = 1
#     _private_var = 2

#     def standalone_function(self, arg1: str, arg2: int = 0) -> bool:
#         """Test standalone function."""
#         return True

#     async def async_function(self) -> None:
#         """Test async function."""
#         pass
# '''
#         test_module_file.write_text(test_module_content)
#     i = test_module_file.parent / "__init__.py"
#     i.touch(exist_ok=True)
#     project_root = test_module_file.parent

#     # Create test stubs directory next to the package
#     test_stubs_dir = Path(project_root) / "test_stubs"

#     generator = StubGenerator(
#         modules=["mbcore"],
#         output_dir=str(test_stubs_dir),
#         include_private=True,
#         include_source=True,
#     )

#     trees = generator.generate_for_modules()
#     generator.save_trees(trees)
#     generator.generate_stubs()

# if __name__ == "__main__":
#     main()
