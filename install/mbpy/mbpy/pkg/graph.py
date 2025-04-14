from __future__ import annotations

import ast
import asyncio
import importlib
import inspect
import os
import sys
from collections import deque
from collections.abc import Iterable, Mapping, MutableMapping, Reversible, Sequence
from dataclasses import asdict, dataclass
from dataclasses import field as Field  # noqa: N812
from functools import reduce
from importlib.util import find_spec, spec_from_file_location
from pathlib import Path
from itertools import count
from site import getsitepackages
from types import ModuleType

from mbcore import ctx
from mbcore._traceback import link_fp
from mbcore.proto import Is
from mbcore.collect import merge, notnone
from mbpy.decorators.cli import to_click_options_args
from mbcore.display import safe_print, NO_BOX
from mbcore.more import collapse, ilen, intersperse
from mbcore.resolve import module_package
from rich.panel import Panel
from rich.syntax import Syntax
from rich.table import Table
from rich.text import Text
from rich.tree import Tree
from typing_extensions import (
    TYPE_CHECKING,
    Any,
    Callable,
    Dict,
    Generic,
    Iterator,
    Literal,
    NotRequired,
    ParamSpec,
    Self,
    Set,
    TypeAlias,
    TypedDict,
    TypeVar,
    Unpack,
    cast,
    get_overloads,
    get_type_hints,
    overload,
    Annotated,
)

from mbpy.cli import check_install_prompt

if TYPE_CHECKING:
    from networkx import DiGraph
    from pydantic.json_schema import SkipJsonSchema



class ASTNodeDict(TypedDict):
    name: str
    qualname: str
    type: Literal[
        "module",
        "function",
        "class",
        "method",
        "doc",
        "imports",
        "signature",
        "args",
        "kwargs",
    ]
    doc: str
    code: Sequence[str]
    lineno: int
    path: Path
    module: str


class Arg(TypedDict):
    default: str
    name: str
    type: str


class Kwarg(Arg): ...


class SignatureDict(TypedDict):
    return_type: str
    args: list[Arg]
    kwargs: Mapping[str, Kwarg]
    lineno: int
    code: list[str]


class FunctionDict(ASTNodeDict):
    lineno: int
    signature: SignatureDict


class ClassDict(ASTNodeDict):
    methods: MutableMapping[str, FunctionDict]
    bases: list[ClassDict]


class ImportDict(TypedDict):
    name: str
    qualname: str
    type: Literal[
        "module",
        "function",
        "class",
        "method",
        "doc",
        "imports",
        "signature",
        "args",
        "kwargs",
    ]
    doc: str
    code: list[str]
    lineno: int
    importedby: NotRequired[set[str]]


class ModuleDict(ASTNodeDict):
    functions: MutableMapping[str, FunctionDict]
    classes: MutableMapping[str, ClassDict]
    submodules: MutableMapping[str, ModuleDict]
    module_object: Annotated[ModuleType, SkipJsonSchema]
    package: str
    imports: MutableMapping[str, ImportDict]
    broken_imports: NotRequired[Dict[str, ImportDict]]


STYLES = {
    "module": "bold cyan",
    "function": "yellow",
    "class": "magenta",
    "method": "blue",
    "doc": "green italic",
    "imports": "light_goldenrod2",
    "signature": "red",
}


class ConfigKwargs(TypedDict, total=False):
    doc: bool
    code: bool
    signatures: bool
    site_packages: bool
    functions: bool
    classes: bool
    ignore: list[str]
    include: list[str]
    maxdepth: int


class Config(TypedDict):
    doc: bool
    code: bool
    signatures: bool
    site_packages: bool
    functions: bool
    classes: bool
    ignore: list[str]
    include: list[str]
    maxdepth: int


def default_config() -> Config:
    return {
        "doc": False,
        "code": False,
        "signatures": False,
        "site_packages": False,
        "functions": False,
        "classes": False,
        "ignore": [],
        "include": [],
        "maxdepth": 40,
    }


class GraphError(Exception): ...


def visit_args(node: "ast.FunctionDef | ast.AsyncFunctionDef") -> list[Arg]:
    return [
        {
            "name": arg.arg,
            "type": getattr(arg.annotation, "id", "Any"),
            "default": str(default) if default else "None",
        }
        for arg, default in zip(
            node.args.args,
            [None] * (len(node.args.args) - len(node.args.defaults))
            + node.args.defaults,
            strict=False,
        )
    ]


def visit_kwargs(node: "ast.FunctionDef | ast.AsyncFunctionDef") -> Mapping[str, Kwarg]:
    return {
        kw.arg: {
            "name": kw.arg,
            "type": getattr(kw.annotation, "id", "Any"),
            "default": str(default) if default else "None",
        }
        for kw, default in zip(
            node.args.kwonlyargs,
            [None] * (len(node.args.kwonlyargs) - len(node.args.kw_defaults))
            + node.args.kw_defaults,
            strict=False,
        )
    }


def visit_function(
    node: "ast.FunctionDef | ast.AsyncFunctionDef",
    source_code: list[str],
    parent: str,
    path: Path,
    config: Config,
) -> FunctionDict:
    func_code = source_code[node.lineno - 1 : node.end_lineno]
    args = visit_args(node)
    kwargs: Mapping[str, Kwarg] = visit_kwargs(node)
    signautre: SignatureDict = {
        "code": func_code if config.get("code", False) else [],
        "lineno": node.lineno or 1,
        "return_type": str(node.returns),
        "args": args,
        "kwargs": kwargs,
    }

    # Respect doc parameter
    doc_value = ""
    if config.get("doc", False):
        doc_value = ast.get_docstring(node) or ""

    return {
        "lineno": node.lineno or 1,
        "signature": signautre,
        "name": node.name,
        "qualname": f"{(parent + '.') if parent else ''}{node.name}",
        "type": "function",
        "doc": doc_value,  # Only include docstring if doc=True
        "code": func_code if config.get("code", False) else [],
        "path": path,
        "module": parent or "",
    }


def visit_class(
    node: "ast.ClassDef",
    source_code: list[str],
    parent: str,
    path: Path,
    config: Config,
) -> ClassDict:
    name = parent
    class_name = node.name

    methods = {}
    for body_item in node.body:
        if isinstance(body_item, ast.FunctionDef):
            method_name = body_item.name
            methods[method_name] = visit_function(
                body_item, source_code, f"{name}.{class_name}", path, config
            )

    bases = []
    for base in node.bases:
        if isinstance(base, ast.Name):
            # Get docstring if doc is enabled
            doc_value = ""
            if config.get("doc", False):
                doc_value = ast.get_docstring(node) or ""

            bases.append(
                {
                    "name": base.id,
                    "qualname": base.id,
                    "type": "class",
                    "doc": doc_value,
                    "code": source_code[node.lineno - 1 : node.end_lineno]
                    if config.get("code", False)
                    else [],
                    "lineno": base.lineno or 1,
                    "path": path,
                    "module": name,
                },
            )

    # Get class docstring if doc is enabled
    doc_value = ""
    if config.get("doc", False):
        doc_value = ast.get_docstring(node) or ""

    return {
        "lineno": node.lineno or 1,
        "type": "class",
        "doc": doc_value,
        "code": source_code[node.lineno - 1 : node.end_lineno]
        if config.get("code", False)
        else [],
        "methods": methods,
        "bases": bases,
        "path": path,
        "module": name,
        "name": class_name,
        "qualname": f"{name}.{class_name}",
    }


def normalize(name: str) -> str:
    return name.replace("-", "_")


@overload
def extract(
    node: "ast.Import",
    name: str,
    path: Path,
    source_code: list[str],
    config: Config,
) -> ModuleDict | FunctionDict | ClassDict: ...
@overload
def extract(
    node: "ast.ImportFrom",
    name: str,
    path: Path,
    source_code: list[str],
    config: Config,
) -> ModuleDict | FunctionDict | ClassDict: ...
@overload
def extract(
    node: "ast.FunctionDef",
    name: str,
    path: Path,
    source_code: list[str],
    config: Config,
) -> ModuleDict | FunctionDict | ClassDict: ...
@overload
def extract(
    node: "ast.ClassDef",
    name: str,
    path: Path,
    source_code: list[str],
    config: Config,
) -> ModuleDict | FunctionDict | ClassDict: ...


@overload
def extract(
    node: "ast.AST",
    name: str,
    path: Path,
    source_code: list[str],
    config: Config,
) -> ModuleDict | FunctionDict | ClassDict | dict[str, ImportDict]: ...
def extract(
    node: "ast.AST",
    name: str,
    path: Path,
    source_code: list[str],
    config: Config,
) -> ModuleDict | FunctionDict | ClassDict | dict[str, ImportDict] | None:
    """Extract information from an AST node."""
    imports: dict[str, ImportDict] = {}
    if isinstance(node, ast.Import):
        for alias in node.names:
            imports[normalize(alias.name)] = {
                "name": normalize(alias.name),
                "qualname": normalize(alias.name),
                "type": "module",
                "doc": "",
                "lineno": node.lineno,
                "path": path,
                "module": name,
                "code": source_code[node.lineno - 1 : node.end_lineno]
                if config.get("code", False)
                else [],
            }
        if any(imp is None for imp in imports):
            raise ValueError(f"None in imports: {imports}")
    if isinstance(node, ast.ImportFrom):
        for alias in node.names:
            mod = f"{node.module}.{alias.name}"
            if mod in sys.modules:
                imports[normalize(mod)] = {
                    "name": normalize(mod),
                    "qualname": normalize(mod),
                    "type": "module",
                    "doc": "",
                    "lineno": node.lineno,
                    "path": path,
                    "module": normalize(name),
                    "code": source_code[node.lineno - 1 : node.end_lineno]
                    if config.get("code", False)
                    else [],
                }
        if any(imp is None for imp in imports):
            raise ValueError(f"None in imports: {imports}")
    elif isinstance(node, ast.ClassDef) and config.get("classes", False):
        return visit_class(node, source_code, name, path, config)
    elif isinstance(node, ast.FunctionDef | ast.AsyncFunctionDef) and config.get(
        "functions", False
    ):
        return visit_function(node, source_code, name, path, config)
    return imports


SkipType = Literal["SKIP"]
SKIP = "SKIP"


def find_source_code_from_path_guess(path: Path) -> str | SkipType:
    try:
        if path.is_file() and "__init__.py" not in str(path):
            return path.read_text()
        orig = path
        orig_stem = normalize(orig.stem)
        if not path.is_file():
            path = orig / "__init__.py"

            if not path.exists() and (orig / "pyproject.toml").exists():
                path = orig / orig_stem
                if not path.exists():
                    path = orig / "src" / orig_stem
                    if not path.exists():
                        # error(f"File {path} is not a file.")
                        return SKIP

            if path.is_dir():
                path = path / "__init__.py"
                if not path.exists():
                    # error(f"File {path} is not a file.")
                    return SKIP
        return path.read_text()
    except Exception:
        # verbose_error(f"Failed to read {path}")
        return SKIP


def find_path_from_module(path: Path) -> Path | SkipType:
    from mbcore.log import debug

    try:
        path = Path(str(path).replace(".", os.path.sep))
        orig = path
        orig_stem = orig.stem
        if not path.exists():
            path = path.with_suffix(".py")
            if not path.exists():
                path = orig
        if not path.exists():
            path = orig / "__init__.py"

            if not path.exists() and (orig / "pyproject.toml").exists():
                path = orig / orig_stem
                if not path.exists():
                    path = orig / "src" / orig_stem
                    if not path.exists():
                        debug(f"File {path} is not a file.")
                        return SKIP
        if not path.exists():
            path = Path(getsitepackages()[0]) / str(orig).replace(".", os.path.sep)
            path = path.with_suffix(".py")
            if not path.exists():
                path = orig / "__init__.py"
                if not path.exists():
                    path = Path(getsitepackages()[0]) / str(orig).replace(
                        ".", os.path.sep
                    )
                    if not path.exists():
                        path = path.with_suffix(".py")
                        debug(f"File {path} is not a file.")
                        return SKIP

        return path
    except Exception:
        # debug(f"Failed to read {path}")
        return SKIP


def extract_node_info(
    path: Path | str | ModuleType | type | Callable, **config: Unpack[Config]
) -> ModuleDict | SkipType:
    """Extract and import function definitions, class definitions, docstrings, and signatures from a Python file."""
    from mbcore.log import verbose_error, debug as log_debug

    # Get debug flag from config
    debug_mode = config.get("debug", False)

    if isinstance(path, ModuleType):
        path = Path(str(path.__file__))
    if isinstance(path, str):
        path = Path(path)
    if not isinstance(path, Path | str):
        path = Path(inspect.getfile(path))
    if isexcluded(path, **config):
        return SKIP

    if (source_code := find_source_code_from_path_guess(path)) == SKIP:
        return SKIP
    try:
        tree = ast.parse(source=source_code, filename=path)
    except Exception as e:
        if debug_mode:
            verbose_error(f"Failed to parse {path}: {e}")
        from mbpy.cmd import run

        out = run(f"{sys.executable} -m pip show {path.stem}", show=False)
        try:
            imps = out.split("Requires:")[1].split("\n")[0].split(", ")
            return ModuleDict(
                **{
                    "name": path.stem,
                    "qualname": path.stem,
                    "type": "module",
                    "doc": "" if not config.get("doc", False) else "",
                    "code": source_code.split("\n")
                    if config.get("code", False)
                    else [],
                    "lineno": 1,
                    "imports": {
                        imp: ImportDict(
                            **{
                                "name": normalize(imp),
                                "qualname": normalize(imp),
                                "type": "module",
                                "doc": "",
                                "lineno": 1,
                                "path": path,
                                "module": normalize(imp),
                                "code": [],
                            }
                        )
                        for imp in imps
                    },
                    "path": path,
                    "module": path.stem,
                    "package": "",
                    "functions": {},
                    "classes": {},
                    "module_object": {},
                    "submodules": {},
                }
            )
        except Exception:
            return SKIP

    imports: dict[str, ImportDict] = {}
    functions: dict[str, FunctionDict] = {}
    classes: dict[str, ClassDict] = {}
    type = "module"
    lineno = 1
    try:
        module, package = module_package(path)
    except Exception as e:
        if debug_mode:
            import traceback

            traceback.print_exc()
            log_debug(f"Import failed for {path}: {e}")
        return SKIP
    if module is None:
        if debug_mode:
            verbose_error(f"Failed to module_package returned None for {path}")
        return SKIP
    name = module.__name__
    qualname = getattr(module, "__qualname__", name)

    for node in ast.iter_child_nodes(tree):
        extracted = extract(
            node=node,
            name=name,
            path=path,
            source_code=source_code.split("\n"),
            config=config,
        )
        if isinstance(node, ast.Import | ast.ImportFrom):
            imports.update(cast(MutableMapping[str, ImportDict], extracted))
        elif isinstance(node, ast.FunctionDef):
            functions[node.name] = cast(FunctionDict, extracted)
        elif isinstance(node, ast.ClassDef):
            classes[node.name] = cast(ClassDict, extracted)

    # Respect the doc flag when extracting docstrings
    doc_value = ""
    if config.get("doc", False):
        doc_value = ast.get_docstring(tree) or ""

    return {
        "name": name,
        "qualname": qualname,
        "type": type,
        "doc": ast.get_docstring(tree) or "",
        "code": source_code.split("\n") if config.get("code", False) else [],
        "lineno": lineno,
        "imports": imports,
        "path": path,
        "module": name,
        "package": package or "",
        "functions": functions if config.get("functions", False) else {},
        "classes": classes if config.get("classes", False) else {},
        "module_object": module,
        "submodules": {},
    }


def attempt_import(module_name, path: Path, debug: bool = False) -> bool:
    """Return True if a module can be imported."""
    fp = Path(path) if path else Path.cwd()
    if module_name in sys.modules:
        return True
    try:
        spec = find_spec(module_name) or spec_from_file_location(module_name, str(path))
        if spec is not None:
            importlib.import_module(module_name)
            return True
    except Exception as e:
        if debug:
            from mbcore.log import debug as log_debug

            log_debug(f"Failed to import {module_name}: {e}")
        try:
            spec = find_spec(module_name) or spec_from_file_location(
                module_name, str(path)
            )
            if spec is not None:
                importlib.import_module(module_name)
                return True
            try:
                with ctx.chdir(fp.parent):
                    spec = spec_from_file_location(module_name, path)
                    if spec is not None:
                        importlib.import_module(module_name)
                        return True
            except Exception as e2:
                if debug:
                    from mbcore.log import debug as log_debug

                    log_debug(f"Failed second attempt to import {module_name}: {e2}")
                return False
        except Exception as e3:
            if debug:
                from mbcore.log import debug as log_debug

                log_debug(f"Failed fallback import for {module_name}: {e3}")
            return False
    return False


if sys.version_info >= (3, 11):
    from typing_extensions import dataclass_transform
else:

    def dataclass_transform(cls):
        return cls


def compose(*funcs: Callable) -> Callable:
    """Composes a series of functions into a single function."""

    def compose2(f, g):
        def compose3(x=None):
            if x is None:
                return f(g())
            return f(g(x))

        return compose3

    return reduce(compose2, funcs, lambda x: x)


_shortid = count(1).__next__


T = TypeVar("T")
ContentT = TypeVar(
    "ContentT",
    bound=MutableMapping | ModuleDict | FunctionDict | ClassDict | ImportDict,
)


def write_imports_to_file(paths: Iterable[str | Path], output_file, **config):
    """Writes import statements from modules in topological order to a file."""  # noqa: D401
    # Generate dependency ModuleGraph and sort topologically
    sorted_graphs = graph(paths, topological=True, **config)
    nodes = merge(*(m.nodes for m in sorted_graphs))
    seen_imports = set()
    sorted_imports = []

    for module in sorted_graphs:
        imports = module.content.get("imports", {})

        for imp, imp_data in imports.items():
            if imp not in seen_imports:
                seen_imports.add(imp)
                if imp in nodes:
                    code = nodes[imp].content["code"]
                    sorted_imports.extend(
                        [
                            "\n\n",
                            f"{'#' * len(imp)}\n# {imp}\n{'#' * len(imp)}\n\n",
                            *code,
                        ]
                    )
                else:
                    sorted_imports.extend(imp_data["code"])

    # Write imports to file
    with Path(str(output_file)).open("w") as f:
        f.write("\n".join(sorted_imports))

    return Path(str(output_file)).resolve()


@dataclass
class TreeNode(dict, Generic[T]):
    """A tree node with a name, parent, status, importance, and report."""

    name: str = Field()
    content: T = Field()
    parent: "Self|RootNode[T]" = Field()

    status: Literal["waiting", "running", "done"] | None = None

    importance: float = 1.0
    report: str | None = None
    """A report on the status of the subtree."""
    children: MutableMapping[str, TreeNode[T]] = Field(default_factory=dict)
    adjacents: set[str] = Field(default_factory=set)
    reverse_adjacents: set[str] = Field(default_factory=set)
    adjacency_matrix: dict[str, dict[str, int]] = Field(init=False)
    Type: type[T] | tuple[type[T], ...] | None = Field(
        default=None, init=False, repr=False
    )
    id: int = Field(default_factory=_shortid)
    _nodes_map: "dict[str, TreeNode[T]]" = Field(
        default_factory=dict, init=False, repr=False
    )
    _root: "Self|RootNode[T]|None" = Field(default=None, init=False, repr=False)

    @property
    def root(self) -> "Self|RootNode[T]":
        if self._root is None:
            raise ValueError("Root node not set")
        return self._root

    @root.setter
    def root(self, value: "Self|RootNode[T]"):
        self._root = value

    def __post_init__(self, *args, **kwargs):
        self.adjacency_matrix = self.parent.adjacency_matrix
        self.parent.children[self.name] = self
        self.parent.adjacents.add(self.name)
        self.reverse_adjacents.add(self.parent.name)
        self.root = self.parent.root
        self.root.nodes[self.name] = self
        self.adjacency_matrix.setdefault(self.parent.name, {}).setdefault(self.name, 0)
        self.adjacency_matrix[self.parent.name][self.name] += 1

        self._nodes_map = {}

    @property
    def nodes(self) -> "dict[str, TreeNode[T]]":
        """Return a dictionary of all nodes in the tree."""
        if self._nodes_map:
            return self._nodes_map
        self._nodes_map.update({m.name: m for m in self.iter_nodes()})
        return self._nodes_map

    def iter_nodes(
        self, mode: Literal["depth", "breadth"] = "depth"
    ) -> "Iterator[TreeNode[T]]":
        """Iterate over all nodes in the tree.

        Args:
            mode (str): The iteration mode, either 'depth' or 'breadth'.

        """
        root = self.root or self
        if mode == "depth":
            yield root
            yield from root.iter_children()
        elif mode == "breadth":
            yield root
            for child in root.children.values():
                yield child
            for child in root.children.values():
                yield from child.iter_children(mode="breadth")

    def iter_children(
        self, mode: Literal["depth", "breadth"] = "depth"
    ) -> "Iterator[TreeNode[T]]":
        """Iterate over all children in the tree.

        Args:
            mode (str): The iteration mode, either 'depth' or 'breadth'.

        """
        if mode == "depth":
            for child in self.children.values():
                yield child
                yield from child.iter_children()
        elif mode == "breadth":
            for child in self.children.values():
                yield child
            for child in self.children.values():
                yield from child.iter_children(mode="breadth")

    @classmethod
    def __class_getitem__(cls, *value_type: "type[ContentT]") -> "type[Self]":
        if len(list(value_type)) != 1:
            raise TypeError("TreeNode only supports a single type argument.")
        cls.Type = next(iter(value_type))
        return cls

    @property
    def graph(self) -> "DiGraph":
        return self.tograph()

    def tograph(
        self, g: "DiGraph | None" = None, key: str | None = "name"
    ) -> "DiGraph":
        """Recursively adds nodes and edges to a NetworkX ModuleGraph."""
        from networkx import DiGraph

        if not DiGraph:
            raise GraphError(
                "NetworkX is required for this function. Install it with 'pip install networkx'."
            )
        G = g if g is not None else DiGraph()  # noqa

        # Store adjacency matrix in ModuleGraph.ModuleGraph attribute for reference
        if not hasattr(G, "graph") or G.graph is None:
            G.graph = {}
        G.graph["adjacency_matrix"] = self.adjacency_matrix

        # Add this node
        node_id = getattr(self, key, self.get(key, self.name)) if key else self.name
        if node_id not in G:
            # --- CORRECTED FIX v2 --- 
            # Manually build attribute dictionary, skipping non-serializable fields
            node_attrs = {}
            import dataclasses
            from types import ModuleType
            # We need ModuleType for the check below

            for f in dataclasses.fields(self):
                field_name = f.name
                # Skip fields internal to the graph structure or potentially problematic
                if field_name in ['parent', 'root', '_nodes_map', '_root', 'Type', 
                                  'children', 'adjacents', 'reverse_adjacents', 
                                  'adjacency_matrix']: 
                    continue
                
                # Get the value, handle potential AttributeError if field isn't set
                try:
                    value = getattr(self, field_name)
                except AttributeError:
                    continue # Skip if attribute doesn't exist for some reason

                # Specifically check the 'content' field for a 'module_object'
                if field_name == 'content' and isinstance(value, dict) and isinstance(value.get('module_object'), ModuleType):
                    # If content has a module object, exclude the module object itself
                    # but keep the rest of the 'content' dictionary if it's serializable
                    content_copy = {k: v for k, v in value.items() if k != 'module_object'}
                    node_attrs[field_name] = content_copy # Store the modified dict
                    continue # Go to next field
                
                # General check for ModuleType in other fields (less likely but safe)
                if isinstance(value, ModuleType):
                    continue # Skip module objects entirely
                
                # Add other serializable values
                # Add more checks here if other non-serializable types are possible
                try:
                     # Quick check if value itself is serializable by attempting asdict
                     # This isn't perfect but catches common dataclass/dict issues.
                     # A full check would involve trying pickle.dumps, but that's slower.
                     if dataclasses.is_dataclass(value):
                          _ = dataclasses.asdict(value) # Test serializability
                     elif isinstance(value, dict):
                          pass # Assume dicts are okay unless they contain modules (handled above)
                     node_attrs[field_name] = value
                except TypeError:
                     # If asdict fails, the value isn't easily serializable, skip it
                     print(f"Warning: Skipping non-serializable attribute '{field_name}' of type {type(value)} in graph node {node_id}")
                     continue 

            G.add_node(node_id, **node_attrs) # Use the manually built attributes
            # --- END FIX ---

        # Add edges to children with weights
        for child in self.children.values():
            child_id = (
                getattr(child, key, child.get(key, child.name)) if key else child.name
            )

            # Calculate weight from adjacency matrix
            weight = 1
            if (
                self.name in self.adjacency_matrix
                and child.name in self.adjacency_matrix[self.name]
            ):
                weight = self.adjacency_matrix[self.name][child.name]

            # Add edge with weight
            G.add_edge(node_id, child_id, weight=weight)

            # Recurse to child
            child.tograph(G, key=key)

        # Handle import edges with weights
        for imp in self.get("imports", []):
            if imp in G:
                imp_id = imp  # The import name is the node ID

                # Calculate weight from adjacency matrix
                weight = 1
                if (
                    self.name in self.adjacency_matrix
                    and imp in self.adjacency_matrix[self.name]
                ):
                    weight = self.adjacency_matrix[self.name][imp]

                # Add edge with weight
                G.add_edge(node_id, imp_id, weight=weight)

        return G

    __iter__ = iter_children

    def __getitem__(self, key: str | int) -> "Any":
        if (
            isinstance(self.content, Mapping)
            and key in self.content
            and key not in self.keys()
        ):
            return self.content[key]
        if isinstance(key, int):
            index = key
            return list(self.children.values())[index]
        return self.children[key]

    model_config = {"arbitrary_types_allowed": True}

    def topo_sort(self, key: str | None = None) -> Reversible["TreeNode[T]"]:
        """Topologically sort the tree."""
        return [n for t in topo_sort(self, key) for n in t]


@dataclass
class RootNode(TreeNode[T]):
    """A root node for a tree."""

    parent: None = None
    content: T | None = Field(default=None)
    children: MutableMapping[str, TreeNode[T]] = Field(default_factory=lambda: {})
    root: "Self" = Field(init=False, repr=False)

    def __post_init__(self):
        self.root = self
        self.adjacency_matrix = {}

    def __hash__(self):
        return self.id


ImportToBrokenMap: TypeAlias = dict[str, ImportDict]

ModuleNode: TypeAlias = TreeNode[ModuleDict]

_ContentT = TypeVar(
    "_ContentT",
    bound=MutableMapping | ModuleDict | FunctionDict | ClassDict | ImportDict,
)

ModuleGraph: TypeAlias = TreeNode[_ContentT]
Graph: TypeAlias = TreeNode[T]

# Define excluded directories
EXCLUDED_DIRS = {"site-packages", "vendor", "venv", ".venv", "env", ".env"}


def isexcluded(path: "Path", **config: Unpack[Config]) -> bool:
    """Return True if a path should be excluded.

    This function determines if a path should be excluded based on:
    1. Standard exclusion rules (site-packages, tests, etc.)
    2. User-provided 'ignore' patterns
    3. User-provided 'include' patterns (overrides ignore)

    Args:
        path: The path to check
        **config: Configuration including ignore/include patterns

    Returns:
        bool: True if the path should be excluded, False otherwise
    """
    # Convert to string for easier pattern matching
    path_str = str(path)

    # Get configuration
    root_path = Path(config.get("root_path", ".")).resolve()
    path_resolved = path.resolve()
    ignore_patterns = config.get("ignore", [])
    include_patterns = config.get("include", [])
    debug_mode = config.get("debug", False)

    # Normalize patterns to list if they're not already
    if not isinstance(ignore_patterns, list):
        ignore_patterns = [ignore_patterns]
    if not isinstance(include_patterns, list):
        include_patterns = [include_patterns]

    # Process patterns to ensure they're strings
    ignore_patterns = [str(p) for p in ignore_patterns if p]
    include_patterns = [str(p) for p in include_patterns if p]

    # Debug logging
    from mbcore.log import debug

    if debug_mode:
        debug(f"Checking exclusion for path: {path_str}")
        debug(f"Ignore patterns: {ignore_patterns}")
        debug(f"Include patterns: {include_patterns}")

    # ✅ Never exclude the root directory
    if path_resolved == root_path:
        if debug_mode:
            debug(f"Path {path_str} is root directory, not excluding")
        return False

    # Check include patterns first - if specified, only include matching paths
    if include_patterns:
        # Check if any include pattern is in the path
        included = False
        for pattern in include_patterns:
            # Convert module name patterns (with dots) to path patterns for matching
            path_pattern = pattern.replace(".", os.path.sep)

            # Check if pattern is in path or if path starts with pattern
            if (
                path_pattern in path_str
                or pattern in path_str
                or path_str.startswith(path_pattern)
                or path.name == pattern
                or path.stem == pattern
            ):
                included = True
                if debug_mode:
                    debug(
                        f"Path {path_str} matches include pattern {pattern}, including"
                    )
                break

        if not included:
            if debug_mode:
                debug(f"Path {path_str} doesn't match any include pattern, excluding")
            return True

    # Standard exclusions
    path_lower = path_str.lower()

    # ✅ Standard directories to exclude
    if any(
        x in path_lower
        for x in ("jupyter", "ipython", "ipykernel", "clang_repl", "__main__")
    ):
        if debug_mode:
            debug(f"Path {path_str} contains excluded directory, excluding")
        return True

    # ✅ Exclude .git directories
    if ".git" in path_str:
        if debug_mode:
            debug(f"Path {path_str} contains .git, excluding")
        return True

    # ✅ Exclude test directories
    if any(p == "tests" for p in path.parts):
        if debug_mode:
            debug(f"Path {path_str} is in tests directory, excluding")
        return True

    # ✅ Exclude hidden directories/files (unless in site-packages or python)
    if (
        any(p.startswith(".") for p in path.parts)
        and "site-packages" not in path_str
        and "python" not in path_str
    ):
        if debug_mode:
            debug(f"Path {path_str} is in hidden directory, excluding")
        return True

    if path.name.startswith("."):
        return True

    if str(path).endswith("__init__.py") and not any(
        p in EXCLUDED_DIRS for p in path.parts
    ):
        return False

    if "site-packages" in str(path_resolved):
        return not config.get("site_packages", False)

    ignore = config.get("ignore", [])
    if not isinstance(ignore, list):
        ignore = [ignore]
    if any(ig == part for ig in ignore for part in path_resolved.parts):
        return True

    includes = config.get("include", [])
    if includes:

        def matches_include(inc: str) -> bool:
            inc_path = Path(inc).resolve()
            return str(path_resolved).startswith(str(inc_path))

        if not any(matches_include(inc) for inc in includes):
            return True

    # If we get here, the path passed all exclusion checks
    if debug_mode:
        debug(f"Path {path_str} passed all exclusion checks, including")
    return False


async def build_dependency_graph(
    directory_or_files: "list[str|Path]",
    **config: Unpack[ConfigKwargs],
) -> "list[ModuleGraph]":
    """Build a module dependency ModuleGraph by parsing Python files."""
    gs: list[ModuleGraph] = await asyncio.gather(
        *[
            asyncio.to_thread(
                lambda df: _build_dependency_graph(df, **config), directory_or_file
            )
            for directory_or_file in directory_or_files
        ]
    )
    return gs


visited: dict[str, TreeNode[ModuleDict] | SkipType] = {}


def handle_imports(
    current_node: ModuleNode,
    module_node: ModuleNode,
    queue: deque,
    seen: dict[Path, int],
    broken_imports: ImportToBrokenMap,
    adjacency_matrix: dict[str, dict[str, int]],
    depth: int,
    **config: Unpack[Config],
) -> None:
    from mbcore.log import debug

    module_name = module_node.name
    debug_mode = config.get("debug", False)

    for i, imp_node in module_node.content.get("imports", {}).items():
        imp = imp_node["qualname"] if imp_node.get("qualname") else i
        imp_node.setdefault("importedby", set()).add(module_name)
        if module_name not in str(imp):
            path = Path(getsitepackages()[0]) / imp.replace(".", os.path.sep)
        else:
            path = current_node.content["path"].parent / imp.replace(".", os.path.sep)
        if not attempt_import(imp, path.parent, debug=debug_mode):
            broken_imports.setdefault(current_node.name, imp_node)
        else:
            if not path.exists():
                path = path.with_suffix(".py")
            if not path.exists() and imp in sys.modules:
                path = getattr(sys.modules[imp], "__file__", path)
            if (path := Path(str(path))).exists():
                if seen.get(path, 0) <= 1:
                    seen[path] = seen.get(path, 0) + 1
                    node_info = extract_node_info(path, **config)
                    if node_info != SKIP:
                        ip = TreeNode(
                            name=imp,
                            content=node_info,
                            parent=current_node,
                        )
                        queue.append((ip, depth + 1))
                        current_node.children[imp] = ip
                    else:
                        if debug_mode:
                            debug(f"Skipping {path}")
            else:
                if debug_mode:
                    debug(f"Path {path} does not exist.")

        current_node.adjacents.add(imp)
        current_node.reverse_adjacents.add(imp)

        adjacency_matrix.setdefault(current_node.name, {})
        adjacency_matrix[current_node.name][imp] = (
            adjacency_matrix[current_node.name].get(imp, 0) + 1
        )


def _build_dependency_graph(
    directory: str | Path,
    **config: Unpack[ConfigKwargs],
) -> ModuleNode:
    """Build a module dependency ModuleGraph by parsing Python files and directories.

    This version uses BFS internally but preserves all original functionality,
    including:
      - Handling site-packages
      - Checking sys.modules
      - Looking for __init__.py
      - isexcluded() checks
      - adjacency_matrix population
      - SKIP logic
      - node_info extraction.
    """
    from mbcore.log import debug

    config = {**default_config(), **config}
    if directory is None:
        raise ValueError("Directory cannot be None.")
    if isinstance(directory, str):
        directory = Path(directory)

    root_path = directory.resolve()
    root_module_name = root_path.stem.replace(os.path.sep, ".") or "root"
    content = extract_node_info(root_path, **config)
    if content == SKIP:
        content = ModuleDict(path=root_path, name=root_module_name)  # type: ignore
    root_node = RootNode[ModuleDict](
        name=root_module_name,
        content=content,
    )
    maxdepth = config.get("maxdepth", 30)
    visited: dict[str, TreeNode[ModuleDict] | SkipType] = {root_module_name: root_node}
    adjacency_matrix: dict[str, dict[str, int]] = {}
    broken_imports: ImportToBrokenMap = {}
    seen = {}
    queue: deque[tuple[TreeNode[ModuleDict], int]] = deque([(root_node, 0)])
    while queue:
        current_node, depth = queue.popleft()
        current_path = current_node.content["path"]
        if depth > maxdepth:
            break

        if isexcluded(current_path, **config) or depth > maxdepth:
            debug(f"Checking {current_path}")
            debug(f"isexcluded={isexcluded(current_path, **config)}")
            debug(f"extract_node_info -> {extract_node_info(current_path, **config)}")
            continue
        else:
            debug(f"Processing {current_path}")
        if current_path.stem == "__init__" and current_path.parent not in seen:
            current_path = current_path.parent

        seen[current_path] = seen.get(current_path, 0) + 1

        if current_path.is_dir():
            children = list(current_path.iterdir())

            src_path = current_path / "src"
            if src_path.exists() and src_path.is_dir():
                children.extend(
                    sum(
                        (list(c.iterdir()) for c in src_path.iterdir() if c.is_dir()),
                        [],
                    )
                )

            for item in children:
                if isexcluded(item, **config):
                    debug(f"Checking {item}")
                    debug(f"isexcluded={isexcluded(item, **config)}")
                    debug(f"extract_node_info -> {extract_node_info(item, **config)}")
                    continue

                if item.is_dir():
                    submodule_name = (
                        (
                            f"{Path(item).resolve().relative_to(Path(getsitepackages()[0]).resolve())}".removeprefix(
                                "."
                            )
                            .removesuffix(".py")
                            .replace(os.path.sep, ".")
                            .replace("..", ".")
                            .replace("src.", "")
                            .replace("src", "")
                        )
                        if "site-packages" in str(item)
                        else (
                            f"{current_node.name}.{item.stem}".removeprefix(".")
                            .removesuffix(".py")
                            .replace(os.path.sep, ".")
                            .replace("..", ".")
                            .replace("src.", "")
                            .replace("src", "")
                            .removesuffix(".")
                        )
                    )

                    if "__pycache__" in submodule_name or "dist-info" in submodule_name:
                        continue

                    if submodule_name in sys.modules:
                        item = Path(sys.modules[submodule_name].__file__ or item)
                    else:
                        mod = submodule_name
                        while "." in mod:
                            mod = mod.rsplit(".", 1)[-1]
                            if mod in sys.modules:
                                try:
                                    item = Path(sys.modules[mod].__file__ or item)
                                    submodule_name = submodule_name[
                                        submodule_name.rfind(mod) :
                                    ]
                                except (AttributeError, TypeError):
                                    submodule_name = submodule_name[
                                        submodule_name.rfind(mod) :
                                    ]
                                break

                    itm = (
                        item / "__init__.py"
                        if (item / "__init__.py").exists()
                        else item
                    )

                    node_info = extract_node_info(itm, **config)

                    sub_node = TreeNode(
                        name=submodule_name,
                        content=node_info
                        if node_info != SKIP
                        else ModuleDict(
                            {"path": itm, "name": submodule_name, "imports": {}}
                        ),
                        parent=current_node,
                    )

                    visited[submodule_name] = sub_node
                    current_node.children[submodule_name] = sub_node

                    adjacency_matrix.setdefault(current_node.name, {})
                    adjacency_matrix[current_node.name][submodule_name] = (
                        adjacency_matrix[current_node.name].get(submodule_name, 0) + 1
                    )
                    module_name = submodule_name
                    module_node = sub_node
                    queue.append((sub_node, depth + 1))
                    handle_imports(
                        current_node,
                        module_node,
                        queue,
                        seen,
                        broken_imports,
                        adjacency_matrix,
                        depth,
                        **config,
                    )
                elif item.suffix == ".py":
                    module_name = f"{current_node.name}.{item.stem}"
                    mod = extract_node_info(item, **config)
                    if module_name not in visited:
                        module_node = TreeNode(
                            name=module_name,
                            content=mod
                            if mod != SKIP
                            else ModuleDict(
                                {"path": item, "name": module_name, "imports": {}}
                            ),
                            parent=current_node,
                        )
                    else:
                        module_node = visited[module_name]

                    if module_node == SKIP:
                        continue

                    visited[module_name] = module_node
                    current_node.children[module_name] = module_node

                    queue.append((module_node, depth + 1))

                    adjacency_matrix.setdefault(current_node.name, {})
                    adjacency_matrix[current_node.name][module_name] = (
                        adjacency_matrix[current_node.name].get(module_name, 0) + 1
                    )
                    handle_imports(
                        current_node,
                        module_node,
                        queue,
                        seen,
                        broken_imports,
                        adjacency_matrix,
                        depth,
                        **config,
                    )
                elif item.stem not in visited:
                    module_name = f"{current_node.name}.{item.stem}"
                    mod = extract_node_info(item, **config)

                    module_node = TreeNode(
                        name=module_name,
                        content=mod
                        if mod != SKIP
                        else ModuleDict(
                            {"path": item, "name": module_name, "imports": {}}
                        ),
                        parent=current_node,
                    )
                    queue.append((module_node, depth + 1))
                    handle_imports(
                        current_node,
                        module_node,
                        queue,
                        seen,
                        broken_imports,
                        adjacency_matrix,
                        depth,
                        **config,
                    )
                else:
                    module_name = current_node.name
                    mod = extract_node_info(item, **config)
                    module_node = TreeNode(
                        name=module_name,
                        content=mod
                        if mod != SKIP
                        else ModuleDict(
                            {"path": item, "name": module_name, "imports": {}}
                        ),
                        parent=current_node,
                    )
                    queue.append((module_node, depth + 1))
                    handle_imports(
                        current_node,
                        module_node,
                        queue,
                        seen,
                        broken_imports,
                        adjacency_matrix,
                        depth,
                        **config,
                    )

                visited[module_name] = module_node
        else:
            node_info = extract_node_info(current_node.content["path"], **config)

            if node_info == SKIP:
                debug(f"Skipping {current_node.name}")
                continue

            current_node.content.update(node_info)
            module_name = current_node.name

            if (
                node_info.get("module") in sys.modules
                and module_name not in sys.modules
            ):
                try:
                    alt_file = getattr(
                        sys.modules[node_info["module"]], "__file__", None
                    )
                    if alt_file:
                        current_node.content["path"] = Path(alt_file)
                except (AttributeError, TypeError):
                    pass
                module_name = node_info["module"]

            handle_imports(
                current_node,
                current_node,
                queue,
                seen,
                broken_imports,
                adjacency_matrix,
                depth,
                **config,
            )

    root_node.content["broken_imports"] = broken_imports
    return root_node


def reinforce_dependency(graph: Graph[Any], module: str, dependency: str):
    """Strengthens the relationship between a module and its dependency."""
    if dependency in graph.adjacents:
        graph.adjacency_matrix[module][dependency] += 1
    else:
        graph.adjacents.add(dependency)
        graph.adjacency_matrix[module][dependency] = 1


def bfs_traverse(graph: Graph[Any], start_module: str) -> list[str]:
    """Performs BFS traversal while reinforcing dependencies."""
    from collections import deque

    visited = set()
    queue = deque([start_module])
    result = []

    while queue:
        module = queue.popleft()
        if module not in visited:
            visited.add(module)
            result.append(module)

            for dep in graph.adjacents:
                reinforce_dependency(graph, module, dep)
                queue.append(dep)

    return result


def print_graph(
    node: Graph[Any],
    topological=True,
    **config: Unpack[ConfigKwargs],
) -> None:
    """Print formatted module dependency ModuleGraph."""

    def strip_src(s: str) -> str:
        return s.replace("src.", "").replace("src", "").replace("..", ".")

    visited = set()
    root = node
    imports = True
    functions = signatures = config.get("signatures", False)
    classes = config.get("classes", False)
    doc = config.get("doc", False)
    code = config.get("code", False)

    def create_tree(node: ModuleNode, parent: Tree | None = None) -> Tree:
        """Recursive function to create tree structure for visualization."""
        tree = (
            Tree(
                link_fp(
                    strip_src(node.name),
                    node.content["path"],
                    node.content.get("lineno", 1),
                    showpath=False,
                    style=STYLES["module"],
                ),
                style=STYLES["module"],
                guide_style="",
                hide_root=True,
            )
            if parent is None
            else parent.add(
                link_fp(
                    strip_src(node.name),
                    node.content.get("path"),
                    node.content.get("lineno"),
                    style=STYLES["module"],
                    showpath=False,
                ),
            )
        )

        # Add imports
        if imports and node.content.get("imports"):
            imps = tree.add("[dim yellow]Imports")
            linked_imports = []
            for imp in node.content.get("imports", []):
                if imp in root.nodes:
                    child = root.nodes[imp]
                    linked_imports.append(
                        link_fp(
                            imp or "",
                            child.content.get("path"),
                            child.content.get("lineno"),
                            showpath=False,
                            style=STYLES["imports"],
                            markup=False,
                        )
                        if child.content.get("path")
                        else Text(imp or "", style=STYLES["imports"]),
                    )

                    if imp not in visited and child.content.get("path"):
                        visited.add(imp)
                        safe_print(
                            Panel(
                                create_tree(child),
                                border_style="",
                                box=NO_BOX,
                                title=link_fp(
                                    imp,
                                    child.content["path"],
                                    1,
                                    style=STYLES["module"],
                                    showpath=False,
                                ),
                            ),
                        )
                else:
                    linked_imports.append(Text(imp or "", style=STYLES["imports"]))

            imps.add(
                Text.assemble(
                    *intersperse(
                        Text(", "), map(compose(Text.from_markup, str), linked_imports)
                    )
                ),
                style=STYLES["imports"],
            )

        # Add functions
        if functions and node.content.get("functions"):
            funcs = tree.add("[yellow]Functions")
            for fname, finfo in node.content.setdefault("functions", {}).items():
                sig = [
                    Text(
                        f"def {finfo['name']}({', '.join([a['name'] + ': ' + a['type'] for a in finfo['signature']['args']])})"
                    )
                ]
                from rich.highlighter import ReprHighlighter

                repr_highlighter = ReprHighlighter()
                repr_highlighter.highlight(sig[0])

                if doc and finfo["doc"]:
                    sig.append(Text(finfo["doc"], style=STYLES["doc"]))
                funcs.add(Text.assemble(*sig))

        # Add classes
        if classes and node.content.get("classes"):
            cs = tree.add("[magenta]Classes")
            for cname, cinfo in node.content.setdefault("classes", {}).items():
                class_branch = cs.add(
                    link_fp(
                        cname,
                        node.content["path"],
                        node.content["lineno"],
                        style=STYLES["class"],
                        showpath=False,
                    ),
                )

                if doc and cinfo.get("doc"):
                    class_branch.add(Text(cinfo["doc"], style=STYLES["doc"]))

                if cinfo.get("methods"):
                    methods = class_branch.add("[blue]Methods")
                    for mname, minfo in cinfo.setdefault("methods", {}).items():
                        method = methods.add(
                            link_fp(
                                mname,
                                node.content["path"],
                                node.content["lineno"],
                                style=STYLES["method"],
                                showpath=False,
                            ),
                        )
                        if signatures and node.content.get("signature", {}).get(mname):
                            method.add(
                                Text(
                                    f"↪ {node.content['functions'].get(mname, {}).get('signature', '')}",
                                    style=STYLES["signature"],
                                ),
                            )
                        if doc and minfo.get("doc"):
                            method.add(Text(minfo["doc"], style=STYLES["doc"]))

        # Add source code
        if code and node.content.get("code"):
            node_code = node.content["code"]
            tree.add(
                Panel(
                    Syntax(
                        "\n".join(node_code),
                        "python",
                        theme="monokai",
                        line_numbers=True,
                        word_wrap=True,
                    ),
                    title="Source Code",
                    border_style="",
                    box=NO_BOX,
                ),
            )
        if doc and node.content.get("doc"):
            tree.add(Text(node.content["doc"], style=STYLES["doc"]))
        # Add children recursively
        for child in node.children.values():
            if child.name in visited:
                continue
            visited.add(child.name)
            create_tree(child, tree)

        return tree

    # Handle Topological Sorting
    children = root.children
    if children is None:
        raise ValueError(f"No valid nodes found for topological sorting: {root}")
    if topological:
        nodes = topo_sort(node)
        if not nodes:
            raise ValueError("No valid nodes found for topological sorting.")
        sorted_nodes = [
            children.get(name.name)
            for name in (name for sublist in nodes for name in sublist)
            if name.name in children
        ]

        if not sorted_nodes:
            safe_print(
                "[bold red]Error:[/bold red] No valid nodes found for topological sorting."
            )
            return

        first = sorted_nodes[0]
        if not first:
            safe_print(
                "[bold red]Error:[/bold red] No valid nodes found for topological sorting."
            )
            return
        safe_print(
            Panel(
                create_tree(first),
                border_style="",
                box=NO_BOX,
                title=link_fp(
                    first.name,
                    first.content.get("path", "."),
                    1,
                    style=STYLES["module"],
                    showpath=False,
                ),
            ),
        )

        for n in filter(None, sorted_nodes[1:]):
            safe_print(
                Panel(
                    create_tree(n),
                    border_style="",
                    box=NO_BOX,
                    title=link_fp(
                        n.name,
                        n.content.get("path", "."),
                        1,
                        style=STYLES["module"],
                        showpath=False,
                    ),
                ),
            )

    else:
        tree = create_tree(node)
        safe_print(
            Panel(
                tree,
                border_style="",
                box=NO_BOX,
                title=link_fp(
                    node.name,
                    node.content.get("path", "."),
                    1,
                    style=STYLES["module"],
                    showpath=False,
                ),
            ),
        )


def break_cycles(G: DiGraph):
    """Removes cycles by deleting edges with lowest importance/weight."""  # noqa: D401
    from networkx import NetworkXUnfeasible, find_cycle

    while True:
        try:
            cycle = find_cycle(G, orientation="original")
        except NetworkXUnfeasible:
            break  # No cycles left, exit

        # Find the edge with minimum weight in this cycle
        min_weight = float("inf")
        min_edge = None

        for u, v, _ in cycle:
            # Check if edge has a weight attribute
            if "weight" in G[u][v]:
                weight = G[u][v]["weight"]
            # Otherwise check if the adjacency matrix has a weight entry
            elif (
                hasattr(G, "graph")
                and hasattr(G.graph, "adjacency_matrix")
                and u in G.graph.adjacency_matrix
                and v in G.graph.adjacency_matrix[u]
            ):
                weight = G.graph.adjacency_matrix[u][v]
            # Fall back to data dictionary if available
            elif (
                hasattr(G, "graph")
                and "adjacency_matrix" in G.graph
                and u in G.graph["adjacency_matrix"]
                and v in G.graph["adjacency_matrix"][u]
            ):
                weight = G.graph["adjacency_matrix"][u][v]
            # Default to 1 if no weight information is found
            else:
                weight = 1

            if weight < min_weight:
                min_weight = weight
                min_edge = (u, v)

        # If we couldn't determine weights, fall back to removing the last edge
        if min_edge is None:
            u, v, *_ = cycle[-1]
            min_edge = (u, v)

        G.remove_edge(*min_edge)


def topo_sort(graph: Graph[Any], key: str | None = None) -> list[list[Graph[Any]]]:
    """Return topologically sorted trees from the DAG forest after cycle removal."""
    from networkx import topological_sort, weakly_connected_components

    G = graph.tograph(key=key)

    # Ensure the ModuleGraph is a DAG by breaking cycles
    break_cycles(G)

    # Process each connected component separately
    sorted_trees = []
    for component in weakly_connected_components(G):
        subgraph = G.subgraph(component)
        sorted_names = list(topological_sort(subgraph))

        # Convert names back to TreeNode objects
        sorted_nodes = [
            graph.nodes[name] for name in sorted_names if name in graph.nodes
        ]
        sorted_trees.append(sorted_nodes)

    return sorted_trees


class ModuleGraphStats(TypedDict):
    num_modules: int
    num_imports: int
    num_functions: int
    num_classes: int
    avg_degree: float
    scc: Sequence[set[str]]
    size_importance: Sequence[tuple[str, Mapping[str, float]]]
    pagerank: Mapping[str, float]
    name: str


async def get_stats(
    module_nodes: ModuleNode,
) -> ModuleGraphStats:
    scipy = await check_install_prompt("scipy")
    if scipy:
        return _get_stats(module_nodes)
    else:
        return {
            "num_modules": 0,
            "num_imports": 0,
            "num_functions": 0,
            "num_classes": 0,
            "avg_degree": 0,
            "scc": [],
            "size_importance": [],
            "pagerank": {},
            "name": "",
        }


def _get_stats(
    modnode: ModuleGraph[ContentT],
) -> ModuleGraphStats:
    """Computes statistics for the dependency ModuleGraph."""  # noqa: D401
    if TYPE_CHECKING:
        import networkx as nx
        import numpy as np

        DiGraph = nx.DiGraph
        pagerank = nx.pagerank
    import networkx as nx
    import numpy as np
    from networkx import DiGraph, pagerank

    module_nodes = modnode.nodes

    num_modules = ilen(module_nodes)
    num_imports = sum(
        ilen(node.content.get("imports", [])) for node in module_nodes.values()
    )
    num_functions = sum(
        ilen(node.content.get("functions", {})) for node in module_nodes.values()
    )
    num_classes = sum(
        ilen(node.content.get("classes", {})) for node in module_nodes.values()
    )
    # Build the ModuleGraph
    G = DiGraph()

    for name, node in module_nodes.items():
        for neighbor in modnode.adjacents:
            G.add_edge(node.name, neighbor)
    # Add standalone nodes
    for node in module_nodes:
        if node not in G:
            G.add_node(node)
    # Compute PageRank
    try:
        pg = pagerank(G)
        pg = {k: round(v, 4) for k, v in pg.items()}
    except Exception as e:
        from mbcore.log import error

        error(f"PageRank computation failed: {e}")
        pg = {node: 0.0 for node in G.nodes()}

    # Strongly Connected Components
    # scc = list(nx.strongly_connected_components(G))
    # scc = sorted(scc, key=lambda x: len(x), reverse=True)
    # ef = nx.effective_size(G)
    # Compute Effective Size
    size_importance = {
        k: {
            "neighbors": len(module_nodes[k].adjacents),
            "reverse_neighbors": len(module_nodes[k].reverse_adjacents),
            "pagerank": pg[k],
            # "effective_size": ef.get(k),
            # "efficiency": ef.get(k) / len(module_nodes[k].adjacents) if len(module_nodes[k].adjacents) > 0 else 0,
        }
        for k in module_nodes
    }

    return {
        "num_modules": num_modules,
        "num_imports": num_imports,
        "num_functions": num_functions,
        "num_classes": num_classes,
        "scc": [],
        "pagerank": pg,
        "size_importance": [
            (node, size_importance[node])
            for node in sorted(
                module_nodes,
                key=lambda x: size_importance[x]["neighbors"]
                + size_importance[x]["reverse_neighbors"],
                reverse=True,
            )
        ],
        "avg_degree": float(
            np.mean([len(module_nodes[node].adjacents) for node in G.nodes()])
        ),
        "name": modnode.name,
    }


def display_stats(stats: ModuleGraphStats, exclude: Set[str] | None = None) -> None:
    """Displays statistics for the dependency ModuleGraph."""  # noqa: D401
    exclude = exclude or set()
    title = "Dependency ModuleGraph Statistics"
    safe_print(f"\n[bold light_goldenrod2]{title}[/bold light_goldenrod2]\n")

    for key, value in stats.items():
        if isinstance(value, list):
            # Assuming this is the 'size_importance' list of tuples
            if not value:
                safe_print(f"{key}: No data available.\n")
                continue

            # Create a table for list-type statistics
            safe_print(f"[bold]{key}[/bold]")
            table = Table(title=key, style="light_goldenrod2", box=NO_BOX)

            # Extract column headers from the first item's dictionary
            _, first_dict = value[0]
            for column in first_dict:
                table.add_column(column.replace("_", " ").capitalize())
            table.add_column("Node")

            # Add rows to the table
            for node, metrics in value[:30]:  # Display top 10 entries
                row = [
                    f"{metrics[col]:.2f}"
                    if isinstance(metrics[col], float)
                    else str(metrics[col])
                    for col in first_dict
                ]
                row.append(node)
                table.add_row(*row)

            safe_print(table)
            safe_print("")  # Add an empty line for better readability
        else:
            # Display scalar statistics
            if isinstance(value, float):
                safe_print(f"[bold]{key.capitalize()}[/bold]: {value:.2f}\n")
            else:
                safe_print(f"[bold]{key.capitalize()}[/bold]: {value}\n")

    # Specifically display average degree if it's not already included
    if "avg_degree" not in exclude and "avg_degree" in stats:
        avg_degree = stats["avg_degree"]
        safe_print(f"[bold]Average Degree[/bold]: {avg_degree:.2f}\n")


def display_broken(broken_imports: dict[str, ImportDict]) -> None:
    safe_print("\n[bold red]Broken Imports:[/bold red]")
    for imp, node in broken_imports.items():
        paths = node.get("importedby", [])
        safe_print(f"\nModule: {imp}")
        for path in paths:
            p = find_path_from_module(Path(path.replace(os.path.sep, ".")))
            if p != SKIP:
                try:
                    safe_print(
                        " - Imported by:",
                        link_fp(path, p, node["lineno"], showpath=False, style="red"),
                    )
                except Exception:
                    safe_print(" - Imported by:", f"{path} (path not found)")


@to_click_options_args(
    "directory_files_or_modules",
    ignore="multiple",
    exclude="multiple",
    include="multiple",
    defaults=default_config(),
)
async def generate(
    directory_files_or_modules: str = ".",
    broken: Literal["omit", "show", "repair"] = "show",
    debug: bool = False,
    topological: bool = False,
    importedby: bool = False,
    stats: bool = False,
    **config: Unpack[ConfigKwargs],
) -> ModuleGraph:
    """Build a dependency ModuleGraph for a directory, file, or module.

    Args:
        directory_files_or_modules (str): The directory, file, or module to analyze.
        broken (str): How to handle broken imports. Options: 'omit', 'show', 'repair'.
        debug (bool): Display debug information.
        topological (bool): Display the dependency ModuleGraph in topological order.
        importedby (bool): Show modules that import the given module.
        stats (bool): Display statistics for the dependency ModuleGraph.
        doc (bool): Include docstrings in the output.
        code (bool): Include source code in the output.
        site_packages (bool): Include site-packages in the analysis.
        ignore (list): List of directories to ignore.
        include (list): List of directories to include.
        maxdepth (int): Maximum depth to traverse.
        classes (bool): Include classes in the output.
        functions (bool): Include functions in the output.
        signatures (bool): Include function signatures in the output.
    """
    await check_install_prompt("scipy")
    return _generate(
        **notnone(
            {
                "directory_files_or_modules": directory_files_or_modules,
                "broken": broken,
                "debug": debug,
                "topological": topological,
                "importedby": importedby,
                "stats": stats,
                **config,
            },
        ),  # type: ignore
    )  # type: ignore


@overload
def graph(
    path: Path,
    topological: bool,
    key: Literal["path"] = "path",
    **config: Unpack[ConfigKwargs],
) -> list[Graph[T]]: ...
@overload
def graph(
    paths: Iterable[str | Path],
    topological: Literal[True] = True,
    key: None = None,
    **config: Unpack[ConfigKwargs],
) -> list[Graph[T]]: ...
def graph(
    *args: Any,
    **kwargs: Any,
) -> Graph[T] | list[Graph[T]]:
    path: Path | None = None
    paths: list[Path] | None = None
    topological: bool = False
    key: str | None = None
    config: ConfigKwargs = {}
    for func in get_overloads(graph):
        sig = inspect.signature(func)
        try:
            bound = sig.bind(*args, **kwargs)
            bound.apply_defaults()
            path = bound.arguments.get("path")
            paths = bound.arguments.get("paths")
            topological = bound.arguments.get("topological", False)
            key = bound.arguments.get("key", None)
            config = bound.arguments.get("config", {})
            break
        except TypeError:
            continue

    if path is not None:
        g = _build_dependency_graph(path, **config)
        if topological:
            return cast(
                list[Graph[T]], collapse(topo_sort(g, key=key), isscalar=Is[Graph[T]])
            )
        return g
    if paths is not None:
        graphs: list[Graph[Any]] = [_build_dependency_graph(p, **config) for p in paths]

    if topological:
        return [
            c
            for graph in graphs
            for sorted_graph in topo_sort(graph, key=key)
            for c in sorted_graph
        ]

    return graphs


def _generate(
    path: str | Path = ".",
    broken: Literal["omit", "show", "repair"] = "show",
    topological: bool = False,
    stats: bool = False,
    importedby: bool = False,
    debug: bool = False,
    **config: Unpack[ConfigKwargs],
) -> Graph[T]:
    """Build a dependency ModuleGraph for a directory, file, or module.

    Args:
        directory_files_or_modules (str): The directory, file, or module to analyze.
        sigs (bool): Include function signatures in the output.
        doc (bool): Include docstrings in the output.
        code (bool): Include source code in the output.
        importedby (bool): Show modules that import the given module.
        stats (bool): Display statistics for the dependency ModuleGraph.
        site_packages (bool): Include site-packages in the analysis.
        broken (str): How to handle broken imports. Options: 'omit', 'show', 'repair'.
    """
    from mbcore import log

    # Ensure debug flag is passed through config
    cfg: Config = {**default_config(), **config, "debug": debug}

    if debug:
        log.debug(f"Generating dependency Graph for '{path}'")
    result = _build_dependency_graph(path, **cfg)
    root_node = result
    broken_imports = result.content.get("broken_imports", {})
    print_graph(root_node, topological=topological, **cfg)
    if stats:
        display_stats(_get_stats(root_node))
    # Display importers if requested
    if importedby:
        for module_name in root_node.children:
            _who_imports(
                module_name,
                root_node.content["path"],
                site_packages=cfg.get("site_packages"),
                debug=debug,
                show=True,
            )

    # Display broken imports with file paths
    if broken == "show" and broken_imports:
        display_broken(broken_imports)
    return result


@to_click_options_args("module_name", "path")
async def who_imports(
    module_name: str,
    path: "Path | str",
    site_packages: bool = False,
    debug: bool = False,
) -> set[str]:
    return set(
        _who_imports(
            module_name, path, site_packages=site_packages, debug=debug, show=True
        )
    )


def _who_imports(
    module_name: str,
    path: "Path | str",
    *,
    site_packages: bool,
    debug: bool = False,
    show: bool = False,
) -> Sequence[str]:
    """Find modules that import the given module."""
    result = _build_dependency_graph(
        path,
        site_packages=site_packages,
        code=False,
        doc=False,
        functions=False,
        classes=False,
        maxdepth=1,
        ignore=[],
        include=[],
        signatures=False,
        debug=debug,
    )
    # Get modules that import the given module
    importers = result.nodes[module_name].content["imports"]
    if importers and show:
        safe_print(
            f"\n[bold light_goldenrod2]Modules that import '{module_name}':[/bold light_goldenrod2]"
        )
        for importer in importers:
            safe_print(f" - {importer}")
    elif show:
        safe_print(
            f"\n[bold red]No modules found that import '{module_name}'.[/bold red]"
        )
    return list(importers)


P = ParamSpec("P")
R = TypeVar("R")


def get_validated_params(func: Callable[P, R], *args: str, **kwargs: str):
    """Validate and convert string arguments to the appropriate types based on the callable's annotations."""
    sig = inspect.signature(func)
    params = sig.parameters
    converted_kwargs = {}
    converted_args = []
    arg_idx = 0

    # Convert positional arguments
    for p_name, p in params.items():
        if p.kind in (
            inspect.Parameter.POSITIONAL_ONLY,
            inspect.Parameter.POSITIONAL_OR_KEYWORD,
        ):
            if arg_idx < len(args):
                raw_value = args[arg_idx]
                if p.annotation != inspect.Parameter.empty and isinstance(
                    p.annotation, type
                ):
                    try:
                        converted_value = p.annotation(raw_value)
                    except (ValueError, TypeError) as e:
                        raise ValueError(
                            f"Error converting argument '{p_name}': {e}"
                        ) from e
                else:
                    converted_value = raw_value
                converted_args.append(converted_value)
                arg_idx += 1
            elif p_name in kwargs:
                raw_value = kwargs.pop(p_name)
                if p.annotation != inspect.Parameter.empty and isinstance(
                    p.annotation, type
                ):
                    try:
                        converted_value = p.annotation(raw_value)
                    except (ValueError, TypeError) as e:
                        raise ValueError(
                            f"Error converting argument '{p_name}': {e}"
                        ) from e
                else:
                    converted_value = raw_value
                converted_kwargs[p_name] = converted_value
            elif p.default != inspect.Parameter.empty:
                converted_kwargs[p_name] = p.default
            else:
                raise TypeError(f"Missing required argument '{p_name}'")

    # Convert remaining keyword arguments
    for key, raw_value in kwargs.items():
        if key in params:
            param = params[key]
            if param.annotation != inspect.Parameter.empty and isinstance(
                param.annotation, type
            ):
                try:
                    converted_value = param.annotation(raw_value)
                except (ValueError, TypeError) as e:
                    raise ValueError(f"Error converting argument '{key}': {e}") from e
            else:
                converted_value = raw_value
            converted_kwargs[key] = converted_value
        else:
            raise TypeError(f"Unexpected keyword argument '{key}'")

    # Return validated arguments
    return converted_args, converted_kwargs


def validate_params(func: Callable[P, R]) -> Callable[P, R]:
    """A decorator to validate and convert inputs dynamically based on the type hints of the wrapped function."""  # noqa: D401

    def wrapper(*args, **kwargs):
        # Retrieve the function's signature and type hints
        sig = inspect.signature(func)
        type_hints = get_type_hints(func)

        # Bind the provided arguments to the function's signature
        bound_args = sig.bind(*args, **kwargs)
        bound_args.apply_defaults()

        # Validate and convert arguments
        for name, value in bound_args.arguments.items():
            expected_type = type_hints.get(name)

            # Skip validation if no type hint is provided
            if expected_type is None:
                continue

            # Convert the value to the expected type, if necessary
            if not isinstance(value, expected_type):
                try:
                    # Special handling for booleans
                    if expected_type is bool and isinstance(value, str):
                        bound_args.arguments[name] = value.lower() in (
                            "true",
                            "1",
                            "yes",
                        )
                    else:
                        bound_args.arguments[name] = expected_type(value)
                except (ValueError, TypeError) as e:
                    raise ValueError(
                        f"Argument '{name}' must be of type {expected_type}, "
                        f"but got value '{value}' of type {type(value)}",
                    ) from e

        # Call the original function with validated arguments
        return func(*bound_args.args, **bound_args.kwargs)

    return wrapper


""" 
with click.progressbar(
        length=total_size,
        label='Unzipping archive',
        item_show_func=lambda a: a.filename
    ) as bar:
        for archive in zip_file:
            archive.extract()
            bar.update(archive.size, archive)
"""

# from typing import Callable, Dict


if __name__ == "__main__":
    generate()
