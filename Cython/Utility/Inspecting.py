"""Inspecting utilities."""
import ast
import builtins
import dis
import importlib
import linecache
import os
import re
import sys
import tokenize
import types
import warnings
from collections import namedtuple
from collections.abc import Callable, Iterable, Mapping
from contextlib import suppress
from dataclasses import asdict
from functools import lru_cache
from inspect import Signature
from itertools import islice, zip_longest
from operator import attrgetter
from pathlib import Path
from types import BuiltinFunctionType, MethodDescriptorType, SimpleNamespace
from typing import TYPE_CHECKING, Any, Final, Literal, NoReturn, ParamSpec, TypeVar, cast, overload

from typing_extensions import NamedTuple, TypeIs

try:
    from Cython.Utility.ImportUtils import smart_import as _smart_import
except Exception:  # pragma: no cover - fallback for bootstrapping
    def _smart_import(name: str, /, *, mode: str = "eager"):
        import importlib
        return importlib.import_module(name)

if TYPE_CHECKING:
    import cython
else:
    try:
        import cython
    except ImportError:
        import dataclasses
        cython = SimpleNamespace(
            ccall=(lambda f: f),
            locals=(lambda **_: (lambda f: f)),
            cfunc=(lambda f: f),
            dataclasses=SimpleNamespace(dataclass=dataclasses.dataclass, field=dataclasses.field),
            declare=(lambda **_: None),
            bint=bool,
        )

cython.declare(_getbound_cache=object)


cython.declare(_modulesbyfile=dict[Path | str, str], _filesbymodname=dict[str, Path])



_modulesbyfile: dict[Path | str, str] = {}
_filesbymodname: dict[str, Path] = {}


def raise_(exception: Exception) -> NoReturn:
    raise exception


U = TypeVar("U")
P = ParamSpec("P")
T = TypeVar("T")



def getmodule(obj, path: str | Path | None = None, resolve_main: bool = False) -> types.ModuleType | None:
    """Return the module an object was defined in, or None if not found."""
    if ismodule(obj):
        return obj
    if isinstance(obj, (str, Path)) and Path(str(obj)).exists():
        tmp = path
        path = obj
        obj = tmp
    if hasattr(obj, "__module__") and isinstance(obj.__module__, str):
        name = obj.__module__

    # Try the filename to modulename cache
    elif path is not None and path in _modulesbyfile:
        name = _modulesbyfile[path]
    elif isinstance(obj, str):
        name = obj
    elif not isbuiltin(obj):
        name = type(obj).__module__
    elif resolve_main:
        return resolve_main_module()
    else:
        return None

    # Try the cache again with the absolute file name
    try:
        file = getabsfile(obj, path)
    except (TypeError, FileNotFoundError):
        from importlib.util import module_from_spec, spec_from_file_location

        spec = spec_from_file_location(name, path)
        if spec is not None and spec.loader is not None:
            return spec.loader.exec_module(module_from_spec(spec))
        return None

    if file in _modulesbyfile:
        return sys.modules.get(_modulesbyfile[file])
    # Update the filename to module name cache and check yet again
    # Copy sys.modules in order to cope with changes while iterating
    for modname, module in sys.modules.copy().items():
        if ismodule(module) and hasattr(module, "__file__"):
            f = module.__file__
            if f == str(_filesbymodname.get(modname)):
                # Have already mapped this module, so skip it
                continue
            _filesbymodname[modname] = Path(str(f)).resolve()
            f = getabsfile(module)
            # Always map to the name the module knows itself by
            _modulesbyfile[f] = _modulesbyfile[os.path.realpath(f)] = module.__name__
    if file in _modulesbyfile:
        return sys.modules.get(_modulesbyfile[file])
    # Check the main module
    main = sys.modules["__main__"]
    if not hasattr(obj, "__name__"):
        return None
    if hasattr(main, obj.__name__):
        mainobject = getattr(main, obj.__name__)
        if mainobject is obj:
            return main
    # Check builtins
    builtin = sys.modules["builtins"]
    if hasattr(builtin, obj.__name__):
        builtinobject = getattr(builtin, obj.__name__)
        if builtinobject is obj:
            return builtin
    return None


def isclass(obj: Any) -> TypeIs[type]:
    return isinstance(obj, type)


def ismethod(obj) -> TypeIs[types.MethodType]:
    return isinstance(obj, types.MethodType) or hasattr(obj, "__self__")


def isfunction(obj) -> TypeIs[types.FunctionType]:
    return isinstance(obj, types.FunctionType)


def get_last_frame_module() -> str:
    while not (f := sys._getframe(1)).f_back and not f.f_globals.get("__name__"):
        f = f.f_back
    return f.f_globals.get("__name__", "__main__")

def is_method_like(obj: Any) -> TypeIs[types.MethodType]:
    return ismethod(obj)


def isimport(obj, module: str | None = None) -> TypeIs[types.ModuleType | types.FunctionType | type]:
    """Check if object is imported by module from another module."""

    mod = module or get_last_frame_module()
    if isbuiltin(obj):
        return False
    if ismodule(obj):
        return obj.__name__ != mod
    mod = _smart_import(mod)
    name = obj.__name__ if isinstance(obj, types.ModuleType | types.FunctionType | type) else type(obj).__name__
    file = getsourcefile(mod)
    if file is None:
        raise OSError(f"Source code not available for object:{name} of type:{type(obj).__name__}")
    parsed = ast.parse(Path(file).read_text())
    for node in ast.walk(parsed):
        if isinstance(node, ast.Import) and name in [alias.name for alias in node.names]:
            return True
        if isinstance(node, ast.ImportFrom) and name in [alias.name for alias in node.names]:
            return True
    return False


BuiltinType = type[str] | type[int] | type[float] | type[complex] | type[bool] | type[tuple] | type[list] | type[dict] | type[set] | types.NoneType
BuiltinTypes = (
    type(str),
    type(int),
    type(float),
    type(complex),
    type(bool),
    type(tuple),
    type(list),
    type(dict),
    type(set),
    type(None),
    types.BuiltinFunctionType,
    types.BuiltinMethodType,
)
BUILTIN_MODULES = {"builtins"} | set(sys.stdlib_module_names)


@lru_cache(maxsize=1)
def builtin_modules() -> set[str]:
    import collections
    import collections.abc

    return BUILTIN_MODULES | set(dir(builtins)) | set(dir(collections.abc)) | set(dir(collections))


def isbuiltin(obj) -> TypeIs[types.BuiltinFunctionType | types.BuiltinMethodType | None | BuiltinType]:  # noqa: F821
    if obj is None:
        return True
    if ismethodwrapper(obj) or ismethoddescriptor(obj) or isdatadescriptor(obj) or ismemberdescriptor(obj) or isbuiltinmethod(obj):
        return True
    if isinstance(obj, str):
        name = obj.strip("'\"")  # remove any surrounding quotes
        return name in builtin_modules()
    # Treat user-defined classes as non-builtin even though all classes are instances of 'type'
    if isinstance(obj, type) and getattr(obj, "__module__", None) != "builtins":
        return False
    return isinstance(obj, BuiltinTypes) or getattr(obj, "__module__", None) in BUILTIN_MODULES


def ismethodwrapper(obj) -> TypeIs[types.MethodWrapperType]:
    return isinstance(obj, types.MethodWrapperType)


def isbuiltinmethod(obj) -> TypeIs[types.BuiltinMethodType]:
    return isinstance(obj, types.BuiltinMethodType)


def ismethoddescriptor(obj) -> TypeIs[types.MethodDescriptorType]:
    return isinstance(obj, types.MethodDescriptorType)


def isdatadescriptor(obj) -> TypeIs[types.GetSetDescriptorType]:
    """Return true if the object is a data descriptor.

    Data descriptors have a __set__ or a __delete__ attribute.  Examples are
    properties (defined in Python) and getsets and members (defined in C).
    Typically, data descriptors will also have __name__ and __doc__ attributes
    (properties, getsets, and members have both of these attributes), but this
    is not guaranteed.
    """
    if isclass(obj) or ismethod(obj) or isfunction(obj):
        # mutual exclusion
        return False
    tp = type(obj)
    return hasattr(tp, "__set__") or hasattr(tp, "__delete__")


def ismemberdescriptor(obj) -> TypeIs[types.MemberDescriptorType]:
    return isinstance(obj, types.MemberDescriptorType)


def ismodule(obj) -> TypeIs[types.ModuleType]:
    return isinstance(obj, types.ModuleType)


def iscode(obj) -> TypeIs[types.CodeType]:
    return isinstance(obj, types.CodeType)


def isframe(obj) -> TypeIs[types.FrameType]:
    return isinstance(obj, types.FrameType)


def istraceback(obj) -> TypeIs[types.TracebackType]:
    return isinstance(obj, types.TracebackType)


def unwrap(func: types.MethodWrapperType | types.FunctionType | classmethod | staticmethod, *, stop=None):
    """Get the object wrapped by *func*.

    Follows the chain of :attr:`__wrapped__` attributes returning the last
    object in the chain.

    *stop* is an optional callback accepting an object in the wrapper chain
    as its sole argument that allows the unwrapping to be terminated early if
    the callback returns a true value. If the callback never returns a true
    value, the last object in the chain is returned as usual. For example,
    :func:`signature` uses this to stop unwrapping if any object in the
    chain has a ``__signature__`` attribute defined.

    :exc:`ValueError` is raised if a cycle is encountered.

    """
    f = func  # remember the original func for error reporting
    # Memoise by id to tolerate non-hashable objects, but store objects to
    # ensure they aren't destroyed, which would allow their IDs to be reused.
    memo = {id(f): f}
    recursion_limit = sys.getrecursionlimit()
    while not isinstance(func, type) and hasattr(func, "__wrapped__"):
        if stop is not None and stop(func):
            break
        func = func.__wrapped__
        id_func = id(func)
        if (id_func in memo) or (len(memo) >= recursion_limit):
            raise ValueError(f"wrapper loop when unwrapping {f!r}")
        memo[id_func] = func
    return func


# -------------------------------------------------- source code extraction
def indentsize(line: str) -> int:
    """Return the indent size, in spaces, at the start of a line of text."""
    expline = line.expandtabs()
    return len(expline) - len(expline.lstrip())


def _findclass(func):
    cls = sys.modules.get(func.__module__)
    if cls is None:
        return None
    for name in func.__qualname__.split(".")[:-1]:
        cls = getattr(cls, name)
    if not isclass(cls):
        return None
    return cls


def getname(obj) -> str:
    with suppress(AttributeError):
        return obj.__name__
    if isinstance(obj, dict):
        return obj.get("name", "Dynamic")
    stringified = str(obj)
    if "<" in stringified:
        stringified = stringified[stringified.rfind("<") + 1 : stringified.rfind(">")].strip()
    if "class " in stringified:
        stringified = stringified[stringified.rfind("class ") + len("class ") :].strip()
    return stringified.replace("'", "").strip()


def _finddoc(obj):
    if isclass(obj):
        for base in obj.__mro__:
            if base is not object:
                try:
                    doc = base.__doc__
                except AttributeError:
                    continue
                if doc is not None:
                    return doc
        return None

    if ismethod(obj):
        name = obj.__func__.__name__
        self = obj.__self__
        cls = self if isclass(self) and getattr(self, name, None).__func__ is obj.__func__ else self.__class__
    elif isfunction(obj):
        name = obj.__name__
        cls = _findclass(obj)
        if cls is None or getattr(cls, name) is not obj:
            return None
    elif isbuiltin(obj):
        name = getname(obj)
        self = obj.__self__
        cls = self if isclass(self) and self.__qualname__ + "." + name == obj.__qualname__ else self.__class__
    # Should be tested before isdatadescriptor().
    elif isinstance(obj, property):
        func = obj.fget
        name = func.__name__ if func else ""
        cls = _findclass(func)
        if cls is None or getattr(cls, name) is not obj:
            return None
    elif ismethoddescriptor(obj) or isdatadescriptor(obj):
        name = obj.__name__
        cls = obj.__objclass__
        if getattr(cls, name) is not obj:
            return None
        if ismemberdescriptor(obj):
            slots = getattr(cls, "__slots__", None)
            if isinstance(slots, dict) and name in slots:
                return slots[name]
    else:
        return None
    for base in cls.__mro__:
        try:
            doc = getattr(base, name).__doc__
        except AttributeError:
            continue
        if doc is not None:
            return doc
    return None


def getdoc(obj) -> str | None:
    """Get the documentation string for an object.

    All tabs are expanded to spaces.  To clean up docstrings that are
    indented to line up with blocks of code, any whitespace than can be
    uniformly removed from the second line onwards is removed.
    """
    try:
        doc = obj.__doc__
    except AttributeError:
        return None
    if doc is None:
        try:
            doc = _finddoc(obj)
        except (AttributeError, TypeError):
            return None
    if not isinstance(doc, str):
        return None
    return cleandoc(doc)


def cleandoc(doc: str) -> str | None:
    """Clean up indentation from docstrings.

    Any whitespace that can be uniformly removed from the second line
    onwards is removed.
    """
    try:
        lines = doc.expandtabs().split("\n")
    except UnicodeError:
        return None
    else:
        # Find minimum indentation of any non-blank lines after first line.
        margin = sys.maxsize
        for line in lines[1:]:
            content = len(line.lstrip())
            if content:
                indent = len(line) - content
                margin = min(margin, indent)
        # Remove indentation.
        if lines:
            lines[0] = lines[0].lstrip()
        if margin < sys.maxsize:
            for i in range(1, len(lines)):
                lines[i] = lines[i][margin:]
        # Remove any trailing or leading blank lines.
        while lines and not lines[-1]:
            lines.pop()
        while lines and not lines[0]:
            lines.pop(0)
        return "\n".join(lines)


PackageRoot = Path
MainFile = Path


@lru_cache(maxsize=1)
def resolve_root_and_main() -> tuple[PackageRoot, MainFile]:
    f = get_first_frame()
    main_file = f.f_code.co_filename
    if not main_file or main_file.startswith("<") or main_file.endswith(">") or main_file == "string" or not Path(main_file).exists():
        warnings.warn(
            f"Could not resolve the __main__ module for {main_file!r}; returning __main__ and the main file path",
            stacklevel=2,
        )
        return Path.cwd(), Path(main_file)
    path = Path(main_file).resolve()
    # If pointing at a file, start from its parent
    start = path.parent if path.is_file() else path

    cur = start
    # Walk up while the parent still looks like a package (__init__.py present)
    while cur.parent and (cur.parent / "__init__.py").exists():
        cur = cur.parent
    return cur, Path(main_file)


def resolve_main_file() -> MainFile:
    return resolve_root_and_main()[1]


def resolve_main_module_name() -> str:
    pkg_path, root_path = resolve_root_and_main()
    if not isinstance(pkg_path, Path) or not isinstance(root_path, Path):
        return "__main__"
    try:
        relative_path = root_path.relative_to(pkg_path.parent)
    except Exception:
        return "__main__"
    return str(relative_path.with_suffix("")).replace(os.sep, ".") or "__main__"


def resolve_main_module() -> types.ModuleType:  #
    return importlib.import_module(resolve_main_module_name())


def fix_module_main_name(name: str) -> str:
    if "__main__" in name:
        return name.replace("__main__", resolve_main_module_name())
    return name


def get_first_frame() -> types.FrameType:
    f = sys._getframe()
    # Walk back until the next frame is the runpy bootstrap (if present)
    while f and f.f_back and "<frozen runpy>" not in f.f_back.f_code.co_filename:
        f = f.f_back
    return f


def get_module_file(obj) -> Path:
    return getfile(getmodule(obj))


def getfile(obj=None, resolve_main: bool = False) -> Path:
    """Work out which source or compiled file an object was defined in."""
    f = sys._getframe(1)
    if obj is None:
        return Path(f.f_code.co_filename)
    if isbuiltin(obj):
        raise_(TypeError(f"{obj!r} is a built-in module"))
    if ismodule(obj):
        from importlib.util import find_spec

        # Normal module: return its file
        file_attr = getattr(obj, "__file__", None)
        if isinstance(file_attr, str) and file_attr:
            return Path(file_attr)
        # Namespace/built-in modules may lack __file__. Try spec.origin.
        spec = find_spec(obj.__name__)
        origin = getattr(spec, "origin", None) if spec is not None else None
        if isinstance(origin, str) and origin:
            return Path(origin)
        # As a last resort, return a sentinel namespace path instead of raising,
        # so callers can handle modules without a real file gracefully.
        return Path(f"namespace:{obj.__name__}")
    if isclass(obj):
        if hasattr(obj, "__module__"):
            module = sys.modules[obj.__module__]
            if (f := getattr(module, "__file__", None)) is not None:
                return Path(f)
            if resolve_main and obj.__module__ == "__main__":
                return resolve_main_file()
        raise TypeError(f"{obj!r} is a built-in class")
    if ismethod(obj):
        obj = obj.__func__
    if isfunction(obj):
        obj = obj.__code__
    if istraceback(obj):
        obj = obj.tb_frame
    if isframe(obj):
        obj = obj.f_code
    if iscode(obj):
        return Path(obj.co_filename)
    raise TypeError(f"module, class, method, function, traceback, frame, or code object was expected, got {type(obj).__name__}")


@overload
def getmodulename(obj: Any, path: str | Path, resolve_main: Literal[True]) -> str: ...
@overload
def getmodulename(obj: Any, path: str | Path, resolve_main: Literal[False]) -> str | None: ...
@overload
def getmodulename(path: str, resolve_main: Literal[True]) -> str: ...
@overload
def getmodulename(path: str, resolve_main: Literal[False]) -> str | None: ...
@overload
def getmodulename(obj: Any, resolve_main: bool = False) -> str: ...
def getmodulename(*args, **kwargs) -> str | None:
    """Return the module name for an object or a file path.

    Accepts either:
    - getmodulename(obj, resolve_main: bool = False)
    - getmodulename(path: str|Path, resolve_main: bool = False)
    - getmodulename(path=..., obj=..., resolve_main=...)

    Never clobbers a provided object with the path; prefers object-based
    resolution when both are available. Falls back to filename-based module
    detection if only a path is provided.
    """
    arglist = list(args)
    # Extract positional path if present as first argument
    path = kwargs.get("path", arglist.pop(0)) if arglist and isinstance(arglist[0], (str, Path)) else kwargs.get("path")
    obj = kwargs.get("obj",arglist.pop(0) if arglist and not isinstance(arglist[0], (str, Path)) else None)
    resolve_main = kwargs.get("resolve_main", arglist.pop(0) if arglist and isinstance(arglist[0], bool) else False)

    # Prefer resolving from the object if provided
    if obj is not None:
        mod = getmodule(obj, path, resolve_main)
        if mod is not None:
            name = mod.__name__
            if "__main__" in name and resolve_main:
                name = name.replace("__main__", resolve_main_module_name())
            # Derive a fully-qualified path for test modules invoked directly
            if resolve_main and "." not in name and (f := getattr(mod, "__file__", None)) is not None:
                file = Path(f).resolve()
                stem = file.with_suffix("")
                parts = stem.parts
                if "tests" in parts:
                    idx = parts.index("tests")
                    dotted = ".".join(parts[idx:])
                    if dotted:
                        name = dotted
            return name
        # Fallback: many builtins/C-API callables have no module object but do
        # expose a stable __module__ string (e.g., math.sin, builtins.len).
        module_str = getattr(obj, "__module__", None)
        if isinstance(module_str, str) and module_str:
            if module_str == "__main__" and resolve_main:
                module_str = resolve_main_module_name()
            return module_str
        raise ValueError("getmodulename: unable to determine module for object")

    # Fallback: detect from a path (if provided)
    if path is None:
        return None
    import importlib.machinery

    path_str = str(path)
    fname = Path(path_str).name
    # Check for paths that look like an actual module file
    suffixes = [(-len(suffix), suffix) for suffix in importlib.machinery.all_suffixes()]
    suffixes.sort()  # try longest suffixes first, in case they overlap
    for neglen, suffix in suffixes:
        if fname.endswith(suffix):
            return fname[:neglen]
    return None


def getsourcefile(obj) -> str | None:
    """Return the filename that can be used to locate an object's source.

    Return None if no way can be identified to get the source.
    """
    import importlib.machinery

    if isinstance(obj, types.ModuleType):
        if obj.__name__ == "__main__" and not hasattr(obj, "__file__"):
            return str(resolve_main_file())
        return obj.__file__
    if isinstance(obj, type):
        # Resolve without calling getmodule(obj) to avoid recursion through getabsfile().
        modname = getattr(obj, "__module__", None)
        if isinstance(modname, str):
            mod = sys.modules.get(modname)
            if mod and hasattr(mod, "__file__"):
                return str(mod.__file__)
        if isbuiltin(obj):
            return None
    if isinstance(obj, types.FunctionType):
        # Convert module name to module file path when available.
        modname = obj.__module__
        if isinstance(modname, str):
            mod = sys.modules.get(modname)
            if mod and hasattr(mod, "__file__"):
                return str(mod.__file__)
    try:
        filename = str(getfile(obj))
    except (TypeError, OSError):
        return None
    if filename is None:
        return None
    all_bytecode_suffixes = importlib.machinery.DEBUG_BYTECODE_SUFFIXES[:]
    all_bytecode_suffixes += importlib.machinery.OPTIMIZED_BYTECODE_SUFFIXES[:]
    if any(filename.endswith(s) for s in all_bytecode_suffixes):
        filename = Path(filename).with_suffix(importlib.machinery.SOURCE_SUFFIXES[0])
    elif any(filename.endswith(s) for s in importlib.machinery.EXTENSION_SUFFIXES):
        return None
    if Path(filename).exists():
        return str(filename)
    # only return a non-existent filename if the module has a PEP 302 loader
    module = getmodule(obj, filename)
    if getattr(module, "__loader__", None) is not None or getattr(getattr(module, "__spec__", None), "loader", None) is not None or filename in linecache.cache:
        return str(filename)
    return None


def getabsfile(obj, path: str | Path | None = None) -> str:
    """Return an absolute path to the source or compiled file for an object.

    The idea is for each object to have a unique origin, so this routine
    normalizes the result as much as possible.
    """
    fn = path or getsourcefile(obj) or getfile(obj)
    return os.path.normcase(Path(fn).resolve()) if fn else raise_(FileNotFoundError(f"Could not find file for object: {obj}"))


class ClassFoundError(IndexError):...

class _ClassFinder(ast.NodeVisitor):
    def __init__(self, qualname):
        self.stack = []
        self.qualname = qualname

    def visit_FunctionDef(self, node):
        self.stack.append(node.name)
        self.stack.append("<locals>")
        self.generic_visit(node)
        self.stack.pop()
        self.stack.pop()

    def visit_AsyncFunctionDef(self, node):
        self.visit_FunctionDef(node)

    def visit_ClassDef(self, node):
        self.stack.append(node.name)
        if self.qualname == ".".join(self.stack):
            # Return the decorator for the class if present
            line_number = node.decorator_list[0].lineno if node.decorator_list else node.lineno

            # decrement by one since lines starts with indexing by zero
            line_number -= 1
            raise ClassFoundError(line_number)
        self.generic_visit(node)
        self.stack.pop()


def findsource(obj):
    """Return the entire source file and starting line number for an object.

    The argument may be a module, class, method, function, traceback, frame,
    or code object.  The source code is returned as a list of all the lines
    in the file and the line number indexes a line in that list.  An OSError
    is raised if the source code cannot be retrieved.
    """
    if isbuiltin(obj):
        raise OSError("source code not available")
    file = getsourcefile(obj)
    if file:
        # Invalidate cache if needed.
        linecache.checkcache(file)
    else:
        file = getfile(obj)
        if file is None:
            raise OSError("source code not available")
        # Allow filenames in form of "<something>" to pass through.
        # `doctest` monkeypatches `linecache` module to enable
        # inspection, so let `linecache.getlines` to be called.
        if not (str(file).startswith("<") and str(file).endswith(">")):
            raise OSError("source code not available")

    module = getmodule(obj, file)
    lines = linecache.getlines(file, module.__dict__) if module else linecache.getlines(file)
    if not lines:
        raise OSError(f"Could not get source code for {obj.__qualname__} of type({type(obj).__name__}) in {file}")

    if ismodule(obj):
        return lines, 0

    if isclass(obj):
        qualname = obj.__qualname__
        source = "".join(lines)
        tree = ast.parse(source)
        class_finder = _ClassFinder(qualname)
        try:
            class_finder.visit(tree)
        except ClassFoundError as e:
            line_number = e.args[0]
            return lines, line_number
        else:
            raise OSError(f"could not find class definition for {obj.__qualname__} in {file}")

    if ismethod(obj):
        obj = obj.__func__
    if isfunction(obj):
        obj = obj.__code__
    if istraceback(obj):
        obj = obj.tb_frame
    if isframe(obj):
        obj = obj.f_code
    if iscode(obj):
        if not hasattr(obj, "co_firstlineno"):
            raise OSError("could not find function definition")
        lnum = obj.co_firstlineno - 1
        pat = re.compile(r"^(\s*def\s)|(\s*async\s+def\s)|(.*(?<!\w)lambda(:|\s))|^(\s*@)")
        while lnum > 0:
            try:
                line = lines[lnum]
            except IndexError as e:
                raise OSError(f"lineno is out of bounds: {lnum}") from e
            if pat.match(line):
                break
            lnum = lnum - 1
        return lines, lnum
    raise OSError("could not find code object")


def getcomments(obj):
    """Get lines of comments immediately preceding an object's source code.

    Returns None when source can't be found.
    """
    try:
        lines, lnum = findsource(obj)
    except (OSError, TypeError):
        return None

    if ismodule(obj):
        # Look for a comment block at the top of the file.
        start = 0
        if lines and lines[0][:2] == "#!":
            start = 1
        while start < len(lines) and lines[start].strip() in ("", "#"):
            start = start + 1
        if start < len(lines) and lines[start][:1] == "#":
            comments = []
            end = start
            while end < len(lines) and lines[end][:1] == "#":
                comments.append(lines[end].expandtabs())
                end = end + 1
            return "".join(comments)

    # Look for a preceding block of comments at the same indentation.
    elif lnum > 0:
        indent = indentsize(lines[lnum])
        end = lnum - 1
        if end >= 0 and lines[end].lstrip()[:1] == "#" and indentsize(lines[end]) == indent:
            comments = [lines[end].expandtabs().lstrip()]
            if end > 0:
                end = end - 1
                comment = lines[end].expandtabs().lstrip()
                while comment[:1] == "#" and indentsize(lines[end]) == indent:
                    comments[:0] = [comment]
                    end = end - 1
                    if end < 0:
                        break
                    comment = lines[end].expandtabs().lstrip()
            while comments and comments[0].strip() == "#":
                comments[:1] = []
            while comments and comments[-1].strip() == "#":
                comments[-1:] = []
            return "".join(comments)
    return None


class EndOfBlockError(Exception): ...


class BlockFinder:
    """Provide a tokeneater() method to detect the end of a code block."""

    def __init__(self):
        self.indent = 0
        self.islambda = False
        self.started = False
        self.passline = False
        self.indecorator = False
        self.last = 1
        self.body_col0 = None

    def tokeneater(self, type, token, srowcol, erowcol, line):
        if not self.started and not self.indecorator:
            # skip any decorators
            if token == "@":
                self.indecorator = True
            # look for the first "def", "class" or "lambda"
            elif token in ("def", "class", "lambda"):
                if token == "lambda":
                    self.islambda = True
                self.started = True
            self.passline = True  # skip to the end of the line
        elif type == tokenize.NEWLINE:
            self.passline = False  # stop skipping when a NEWLINE is seen
            self.last = srowcol[0]
            if self.islambda:  # lambdas always end at the first NEWLINE
                raise EndOfBlockError
            # hitting a NEWLINE when in a decorator without args
            # ends the decorator
            if self.indecorator:
                self.indecorator = False
        elif self.passline:
            pass
        elif type == tokenize.INDENT:
            if self.body_col0 is None and self.started:
                self.body_col0 = erowcol[1]
            self.indent = self.indent + 1
            self.passline = True
        elif type == tokenize.DEDENT:
            self.indent = self.indent - 1
            # the end of matching indent/dedent pairs end a block
            # (note that this only works for "def"/"class" blocks,
            #  not e.g. for "if: else:" or "try: finally:" blocks)
            if self.indent <= 0:
                raise EndOfBlockError
        elif type == tokenize.COMMENT:
            if self.body_col0 is not None and srowcol[1] >= self.body_col0:
                # Include comments if indented at least as much as the block
                self.last = srowcol[0]
        elif self.indent == 0 and type not in (tokenize.COMMENT, tokenize.NL):
            # any other token on the same indentation level end the previous
            # block as well, except the pseudo-tokens COMMENT and NL.
            raise EndOfBlockError


def getblock(lines):
    """Extract the block of code at the top of the given list of lines."""
    blockfinder = BlockFinder()
    with suppress(IndentationError, EndOfBlockError):
        tokens = tokenize.generate_tokens(iter(lines).__next__)
        for _token in tokens:
            blockfinder.tokeneater(*_token)

    return lines[: blockfinder.last]


def getsourcelines(obj):
    """Return a list of source lines and starting line number for an object.

    The argument may be a module, class, method, function, traceback, frame,
    or code object.  The source code is returned as a list of the lines
    corresponding to the object and the line number indicates where in the
    original source file the first line of code was found.  An OSError is
    raised if the source code cannot be retrieved.
    """
    if isbuiltin(obj):
        raise OSError(f"Source code not available for object:{obj!r} of type:{type(obj).__name__}")
    obj = unwrap(obj)
    lines, lnum = findsource(obj)

    if istraceback(obj):
        obj = obj.tb_frame

    # for module or frame that corresponds to module, return all source lines
    if ismodule(obj) or (isframe(obj) and obj.f_code.co_name == "<module>"):
        return lines, 0
    return getblock(lines[lnum:]), lnum + 1


def getsource(obj):
    """Return the text of the source code for an object.

    The argument may be a module, class, method, function, traceback, frame,
    or code object.  The source code is returned as a single string.  An
    OSError is raised if the source code cannot be retrieved.
    """
    while hasattr(obj, "__wrapped__"):
        obj = obj.__wrapped__
    while hasattr(obj, "__func__"):
        obj = obj.__func__
    lines, _ = getsourcelines(obj)
    return "".join(lines)


# --------------------------------------------------- class tree extraction
def walktree(classes: list[type], children: dict[type, list[type]], parent: type | None = None) -> list[tuple[type, tuple[type, ...]]]:
    """Recursive helper function for getclasstree()."""
    results = []
    classes.sort(key=attrgetter("__module__", "__name__"))
    for c in classes:
        results.append((c, c.__bases__))
        if c in children:
            results.append(walktree(children[c], children, c))
    return results


def getclasstree(classes, unique=False):
    """Arrange the given list of classes into a hierarchy of nested lists.

    Where a nested list appears, it contains classes derived from the class
    whose entry immediately precedes the list.  Each entry is a 2-tuple
    containing a class and a tuple of its base classes.  If the 'unique'
    argument is true, exactly one entry appears in the returned structure
    for each class in the given list.  Otherwise, classes using multiple
    inheritance and their descendants will appear multiple times.
    """
    children = {}
    roots = []
    for c in classes:
        if c.__bases__:
            for parent in c.__bases__:
                if parent not in children:
                    children[parent] = []
                if c not in children[parent]:
                    children[parent].append(c)
                if unique and parent in classes:
                    break
        elif c not in roots:
            roots.append(c)
    for parent in children:
        if parent not in classes:
            roots.append(parent)
    return walktree(roots, children, None)


# ------------------------------------------------ argument list extraction
@cython.dataclasses.dataclass
class Arguments(NamedTuple):
    args: list[str]
    varargs: str | None
    varkw: str | None


CO_OPTIMIZED: Final = 1
CO_NEWLOCALS: Final = 2
CO_VARARGS: Final = 4
CO_VARKEYWORDS: Final = 8
CO_NESTED: Final = 16
CO_GENERATOR: Final = 32
CO_NOFREE: Final = 64
CO_COROUTINE: Final = 128
CO_ITERABLE_COROUTINE: Final = 256
CO_ASYNC_GENERATOR: Final = 512
TPFLAGS_IS_ABSTRACT: Final = 1048576
if sys.version_info >= (3, 14):
    CO_HAS_DOCSTRING: Final = 67108864
    CO_METHOD: Final = 134217728

modulesbyfile: dict[str, Any]

def _signature_is_functionlike(obj):
    """Private helper to test if `obj` is a duck type of FunctionType.

    A good example of such objects are functions compiled with
    Cython, which have all attributes that a pure Python function
    would have, but have their code statically compiled.
    """
    from inspect import _void
    if not callable(obj) or isclass(obj):
        # All function-like objects are obviously callables,
        # and not classes.
        return False

    name = getattr(obj, '__name__', None)
    code = getattr(obj, '__code__', None)
    defaults = getattr(obj, '__defaults__', _void) # Important to use _void ...
    kwdefaults = getattr(obj, '__kwdefaults__', _void) # ... and not None here
    annotations = getattr(obj, '__annotations__', None)

    return (isinstance(code, types.CodeType) and
            isinstance(name, str) and
            (defaults is None or isinstance(defaults, tuple)) and
            (kwdefaults is None or isinstance(kwdefaults, dict)) and
            (isinstance(annotations, (dict)) or annotations is None) )

def _signature_strip_non_python_syntax(signature: str) -> tuple[str, int | None, int | None]:
    """Private helper function. Takes a signature in Argument Clinic's extended signature format.

    Returns a tuple of three things:
      * that signature re-rendered in standard Python syntax,
      * the index of the "self" parameter (generally 0), or None if
        the function does not have a "self" parameter, and
      * the index of the last "positional only" parameter,
        or None if the signature has no positional-only parameters.
    """
    import token

    if not signature:
        return signature, None, None

    self_parameter = None
    last_positional_only = None

    lines = [l.encode('ascii') for l in signature.split('\n') if l]
    tokens = tokenize.tokenize(iter(lines).__next__)

    delayed_comma = False
    skip_next_comma = False
    text = []
    add = text.append

    current_parameter = 0
    OP = token.OP
    ERRORTOKEN = token.ERRORTOKEN

    # token stream always starts with ENCODING token, skip it
    t = next(tokens)
    if t.type != tokenize.ENCODING:
        raise ValueError(f"Invalid signature: {signature}")

    for t in tokens:
        type, string = t.type, t.string # noqa

        if type == OP:
            if string == ',':
                if skip_next_comma:
                    skip_next_comma = False
                else:
                    assert not delayed_comma
                    delayed_comma = True
                    current_parameter += 1
                continue

            if string == '/':
                assert not skip_next_comma
                assert last_positional_only is None
                skip_next_comma = True
                last_positional_only = current_parameter - 1
                continue

        if (type == ERRORTOKEN) and (string == '$'):
            assert self_parameter is None
            self_parameter = current_parameter
            continue

        if delayed_comma:
            delayed_comma = False
            if not ((type == OP) and (string == ')')):
                add(', ')
        add(string)
        if (string == ','):
            add(' ')
    clean_signature = ''.join(text)
    return clean_signature, self_parameter, last_positional_only


def _signature_fromstr(cls, obj, s, skip_bound_arg=True):
    """Private helper to parse content of '__text_signature__' and return a Signature based on it."""
    from inspect import _empty
    Parameter: type[InspectParameter] = cls._parameter_cls

    clean_signature, self_parameter, last_positional_only = \
        _signature_strip_non_python_syntax(s)

    program = "def foo" + clean_signature + ": pass"

    try:
        module = ast.parse(program)
    except SyntaxError:
        module = None

    if not isinstance(module, ast.Module):
        raise ValueError(f"{obj!r} builtin has invalid signature")

    f =cast(ast.FunctionDef, module.body[0])

    parameters = []
    empty = Parameter.empty

    module = None
    module_dict = {}
    module_name = getattr(obj, '__module__', None)
    if module_name:
        module = sys.modules.get(module_name, None)
        if module:
            module_dict = module.__dict__
    sys_module_dict = sys.modules.copy()

    def parse_name(node):
        assert isinstance(node, ast.arg)
        if node.annotation is not None:
            raise ValueError("Annotations are not currently supported")
        return node.arg

    def wrap_value(s):
        try:
            value = eval(s, module_dict)
        except NameError:
            try:
                value = eval(s, sys_module_dict)
            except NameError:
                raise ValueError

        if isinstance(value, (str, int, float, bytes, bool, type(None))):
            return ast.Constant(value)
        raise ValueError

    class RewriteSymbolics(ast.NodeTransformer):
        def visit_Attribute(self, node):
            a = []
            n = node
            while isinstance(n, ast.Attribute):
                a.append(n.attr)
                n = n.value
            if not isinstance(n, ast.Name):
                raise ValueError
            a.append(n.id)
            value = ".".join(reversed(a))
            return wrap_value(value)

        def visit_Name(self, node):
            if not isinstance(node.ctx, ast.Load):
                raise ValueError()
            return wrap_value(node.id)

        def visit_BinOp(self, node):
            # Support constant folding of a couple simple binary operations
            # commonly used to define default values in text signatures
            left = self.visit(node.left)
            right = self.visit(node.right)
            if not isinstance(left, ast.Constant) or not isinstance(right, ast.Constant):
                raise ValueError
            if isinstance(node.op, ast.Add):
                return ast.Constant(left.value + right.value) # type: ignore
            if isinstance(node.op, ast.Sub):
                return ast.Constant(left.value - right.value) # type: ignore
            if isinstance(node.op, ast.BitOr):
                return ast.Constant(left.value | right.value) # type: ignore
            raise ValueError

    def p(name_node, default_node, default=empty):
        name = parse_name(name_node)
        if default_node and default_node is not _empty:
            try:
                default_node = RewriteSymbolics().visit(default_node)
                default = ast.literal_eval(default_node)
            except ValueError:
                raise ValueError(f"{obj!r} builtin has invalid signature") from None
        parameters.append(Parameter(name, kind, default=default, annotation=empty))

    # non-keyword-only parameters
    args = reversed(f.args.args)
    defaults = reversed(f.args.defaults)
    zipped = zip_longest(args, defaults, fillvalue=None)
    kind = Parameter.POSITIONAL_ONLY if last_positional_only is not None else Parameter.POSITIONAL_OR_KEYWORD
    for i, (name, default) in enumerate(reversed(list(zipped))):
        p(name, default)
        if i == last_positional_only:
            kind = Parameter.POSITIONAL_OR_KEYWORD

    # *args
    if f.args.vararg:
        kind = Parameter.VAR_POSITIONAL
        p(f.args.vararg, empty)

    # keyword-only arguments
    kind = Parameter.KEYWORD_ONLY
    for name, default in zip(f.args.kwonlyargs, f.args.kw_defaults,strict=False):
        p(name, default)

    # **kwargs
    if f.args.kwarg:
        kind = Parameter.VAR_KEYWORD
        p(f.args.kwarg, empty)

    if self_parameter is not None:
        # Possibly strip the bound argument:
        #    - We *always* strip first bound argument if
        #      it is a module.
        #    - We don't strip first bound argument if
        #      skip_bound_arg is False.
        assert parameters
        _self = getattr(obj, '__self__', None)
        self_isbound = _self is not None
        self_ismodule = ismodule(_self)
        if self_isbound and (self_ismodule or skip_bound_arg):
            parameters.pop(0)
        else:
            # for builtins, self parameter is always positional-only!
            p = parameters[0].replace(kind=Parameter.POSITIONAL_ONLY)
            parameters[0] = p

    return cls(parameters, return_annotation=cls.empty)


_NonUserDefinedCallables = (types.WrapperDescriptorType,
                            types.MethodWrapperType,
                            types.ClassMethodDescriptorType,
                            types.BuiltinFunctionType)


def _signature_is_builtin(obj) -> TypeIs[BuiltinType | BuiltinFunctionType] | bool | TypeIs[MethodDescriptorType]:
    """Private helper to test if `obj` is a callable that might support Argument Clinic's __text_signature__ protocol."""
    return (isbuiltin(obj) or
            ismethoddescriptor(obj) or
            isinstance(obj, _NonUserDefinedCallables) or
            # Can't test 'isinstance(type)' here, as it would
            # also be True for regular python classes
            obj in (type, object))

def _signature_from_builtin(cls, func, skip_bound_arg=True) -> Any:
    """Private helper function to get signature for builtin callables."""
    if not _signature_is_builtin(func):
        raise TypeError(f"{func!r} is not a Python builtin "
                        "function")

    s = getattr(func, "__text_signature__", None)
    if not s:
        raise ValueError(f"no signature found for builtin {func!r}")

    return _signature_fromstr(cls, func, s, skip_bound_arg)


def _signature_from_function(cls, func, skip_bound_arg=True, # type: ignore # noqa
                             globalns=None, localns=None, eval_str=False):
    """Construct a Signature for the given python function."""
    is_duck_function = False
    if not isfunction(func):
        if _signature_is_functionlike(func):
            is_duck_function = True
        else:
            # If it's not a pure Python function, and not a duck type
            # of pure function:
            raise TypeError(f'{func!r} is not a Python function')

    s = getattr(func, "__text_signature__", None)
    if s:
        return _signature_fromstr(cls, func, s, skip_bound_arg)

    Parameter: type[InspectParameter] = cls._parameter_cls
    _POSITIONAL_ONLY: int = Parameter.POSITIONAL_ONLY
    _POSITIONAL_OR_KEYWORD: int = Parameter.POSITIONAL_OR_KEYWORD
    _VAR_POSITIONAL: int = Parameter.VAR_POSITIONAL
    _KEYWORD_ONLY: int = Parameter.KEYWORD_ONLY
    _VAR_KEYWORD: int = Parameter.VAR_KEYWORD
    _empty: Any = Parameter.empty

    # Parameter information.
    func_code = func.__code__
    pos_count = func_code.co_argcount
    arg_names = func_code.co_varnames
    posonly_count = func_code.co_posonlyargcount
    positional = arg_names[:pos_count]
    keyword_only_count = func_code.co_kwonlyargcount
    keyword_only = arg_names[pos_count:pos_count + keyword_only_count]
    annotations = get_annotations(func, globalns=globalns, localns=localns, eval_str=eval_str)
    defaults = func.__defaults__ or ()
    kwdefaults = func.__kwdefaults__ or {}

    pos_default_count = len(defaults) if defaults else 0

    parameters = []

    non_default_count = pos_count - pos_default_count
    posonly_left = posonly_count

    # Non-keyword-only parameters w/o defaults.
    for name in positional[:non_default_count]:
        kind = _POSITIONAL_ONLY if posonly_left else _POSITIONAL_OR_KEYWORD
        annotation = annotations.get(name, _empty)
        parameters.append(Parameter(name, annotation=annotation,
                                    kind=kind))
        if posonly_left:
            posonly_left -= 1

    # ... w/ defaults.
    for offset, name in enumerate(positional[non_default_count:]):
        kind = _POSITIONAL_ONLY if posonly_left else _POSITIONAL_OR_KEYWORD
        annotation = annotations.get(name, _empty)
        parameters.append(Parameter(name, annotation=annotation,
                                    kind=kind,
                                    default=defaults[offset]))
        if posonly_left:
            posonly_left -= 1

    # *args
    if func_code.co_flags & CO_VARARGS:
        name = arg_names[pos_count + keyword_only_count]
        annotation = annotations.get(name, _empty)
        parameters.append(Parameter(name, annotation=annotation,
                                    kind=_VAR_POSITIONAL))

    # Keyword-only parameters.
    for name in keyword_only:
        default = _empty
        if kwdefaults is not None:
            default = kwdefaults.get(name, _empty)

        annotation = annotations.get(name, _empty)
        parameters.append(Parameter(name, annotation=annotation,
                                    kind=_KEYWORD_ONLY,
                                    default=default))
    # **kwargs
    if func_code.co_flags & CO_VARKEYWORDS:
        index = pos_count + keyword_only_count
        if func_code.co_flags & CO_VARARGS:
            index += 1

        name = arg_names[index]
        annotation = annotations.get(name, _empty)
        parameters.append(Parameter(name, annotation=annotation,
                                    kind=_VAR_KEYWORD))

    # Is 'func' is a pure Python function - don't validate the
    # parameters list (for correct order and defaults), it should be OK.
    return cls(parameters,
               return_annotation=annotations.get('return', _empty),
               __validate_parameters__=is_duck_function)


def getargs(co):
    """Get information about the arguments accepted by a code object.

    Three things are returned: (args, varargs, varkw), where
    'args' is the list of argument names. Keyword-only arguments are
    appended. 'varargs' and 'varkw' are the names of the * and **
    arguments or None.
    """
    if not iscode(co):
        raise TypeError(f"{co!r} is not a code object")

    names = co.co_varnames
    nargs = co.co_argcount
    nkwargs = co.co_kwonlyargcount
    args = list(names[:nargs])
    kwonlyargs = list(names[nargs : nargs + nkwargs])

    nargs += nkwargs
    varargs = None
    if co.co_flags & CO_VARARGS:
        varargs = co.co_varnames[nargs]
        nargs = nargs + 1
    varkw = None
    if co.co_flags & CO_VARKEYWORDS:
        varkw = co.co_varnames[nargs]
    return Arguments(args + kwonlyargs, varargs, varkw)



if TYPE_CHECKING:
    from inspect import get_annotations as _get_annotations



    def get_annotations(
        func: types.FunctionType | types.MethodType | types.FunctionType,
        globalns: Mapping[str, Any] | None = None,
        localns: Mapping[str, Any] | None = None,
        eval_str: bool = False,
    ) -> dict[str, Any]:
        return _get_annotations(func, globals=globalns, locals=localns or {}, eval_str=eval_str)
else:
    def get_annotations(func, globalns=None, localns=None, eval_str=False):
        inspect_mod = _smart_import("inspect")
        return inspect_mod.get_annotations(func, globals=globalns, locals=localns or {}, eval_str=eval_str)

PosOnlyNames = tuple[str, ...]
PosOrKwNames = tuple[str, ...]
KwOnlyNames = tuple[str, ...]
VarArgs = str | None
Varkw = str | None
PosOnlyDefaults = tuple[Any, ...] | None
PosOrKwDefaults = tuple[Any, ...] | None
KwOnlyDefaults = dict[str, Any] | None
Annotations = dict[str, Any] | None

@cython.dataclasses.dataclass
class FullArgSpec:
    posonly: tuple[str, ...]
    pos_or_kw: tuple[str, ...]
    kw_only: tuple[str, ...]

    varargs: str | None = None
    varkw: str | None = None
    posonly_defaults: tuple[Any, ...] | None = None
    pos_or_kw_defaults: tuple[Any, ...] | None = None
    kw_only_defaults: dict[str, Any] | None = None
    annotations: dict[str, Any] | None = None

    def __iter__(self):
        return iter(asdict(self).values())

@cython.cfunc
def getfullargspec(
    func: types.FunctionType | types.MethodType | types.FunctionType,
    annotated: bool = False,
    *,
    globalns: dict[str, Any] | None = None,
    localns: dict[str, Any] | None = None,
    eval_str: bool = False,
) -> FullArgSpec:
    """Get the names and default values of a callable object's parameters.

    A tuple of nine things is returned:
    (posonly, posonlydefaults, args, argsdefaults, kwonlyargs, kwonlydefaults, varargs, varkw, annotations).
    'posonly' and 'args' are lists of positional parameter names.
    'varargs' and 'varkw' are the names of the * and ** parameters or None.
    'posonlydefaults' and 'argsdefaults' are n-tuples for positional-only and positional-or-keyword defaults.
    'kwonlyargs' is a list of keyword-only parameter names.
    'kwonlydefaults' is a dictionary mapping names from kwonlyargs to defaults.
    'annotations' is a dictionary mapping parameter names to annotations.

    Notable differences from inspect.signature():
      - the "self" parameter is always reported, even for bound methods
      - wrapper chains defined by __wrapped__ *not* unwrapped automatically
    """
    # Re: `skip_bound_arg=False`
    #
    # There is a notable difference in behaviour between getfullargspec
    # and Signature: the former always returns 'self' parameter for bound
    # methods, whereas the Signature always shows the actual calling
    # signature of the passed object.
    #
    # To simulate this behaviour, we "unbind" bound methods, to trick
    # inspect.signature to always return their first parameter ("self",
    # usually)

    # Re: `follow_wrapper_chains=False`
    #
    # getfullargspec() historically ignored __wrapped__ attributes,
    # so we ensure that remains the case in 3.3+
    if not hasattr(func, "__code__"):
        if hasattr(func, "__text_signature__"):
            sig = _signature_from_builtin(Signature, func)
            params = tuple(sig.parameters.values())
            posonly = tuple(p.name for p in params if p.kind.name == "POSITIONAL_ONLY")
            pos_or_kw = tuple(p.name for p in params if p.kind.name == "POSITIONAL_OR_KEYWORD")
            kwonlyargs = tuple(p.name for p in params if p.kind.name == "KEYWORD_ONLY")
            vararg = next((p.name for p in params if p.kind.name == "VAR_POSITIONAL"), None)
            varkw = next((p.name for p in params if p.kind.name == "VAR_KEYWORD"), None)
            defs = tuple(p.default for p in params if p.kind.name in ("POSITIONAL_ONLY","POSITIONAL_OR_KEYWORD") and p.default is not p.empty)
            n_def = len(defs)
            n_pos_or_kw = len(pos_or_kw)
            posonly_defaults = defs[:max(0, n_def - n_pos_or_kw)]
            pos_or_kw_defaults = defs[max(0, n_def - n_pos_or_kw):]
            kwonlydefaults = {p.name: p.default for p in params if p.kind.name == "KEYWORD_ONLY" and p.default is not p.empty}
            return FullArgSpec(posonly, pos_or_kw, kwonlyargs, vararg, varkw, posonly_defaults, pos_or_kw_defaults, kwonlydefaults, {})
        raise ValueError("Function has no __code__ or __text_signature__")

    # Parameter information.
    func_code = func.__code__
    pos_count = func_code.co_argcount
    arg_names = func_code.co_varnames
    posonly_count = func_code.co_posonlyargcount
    posonly = arg_names[:posonly_count]
    keyword_only_count = func_code.co_kwonlyargcount
    annotations = {} if not annotated else get_annotations(func, globalns=globalns, localns=localns, eval_str=eval_str)
    defaults = func.__defaults__ or ()
    kwdefaults = func.__kwdefaults__ if not is_method_like(func) else None
    n_def = len(defaults)
    n_pos_or_kw = pos_count - posonly_count
    posonly_defaults = defaults[: max(0, n_def - n_pos_or_kw)]
    vararg = None
    varkw = None
    kwonlyargs = arg_names[pos_count : pos_count + keyword_only_count]

    # *args
    if func_code.co_flags & CO_VARARGS:
        vararg = arg_names[pos_count + keyword_only_count]

    # **kwargs
    if func_code.co_flags & CO_VARKEYWORDS:
        index = pos_count + keyword_only_count
        if func_code.co_flags & CO_VARARGS:
            index += 1

        varkw = arg_names[index]
    pos_or_kw = arg_names[posonly_count : pos_count]


    kwonly_defaults = {} if not kwdefaults else {kw: kwdefaults[kw] for kw in kwonlyargs}
    pos_or_kw_defaults = defaults[max(0, n_def - n_pos_or_kw) : ]
    return FullArgSpec(posonly,
                        pos_or_kw,
                        kwonlyargs,
                        vararg,
                        varkw,
        posonly_defaults,
        pos_or_kw_defaults,
        kwonly_defaults,
        annotations,
    )


ArgInfo = namedtuple("ArgInfo", "args varargs keywords locals")


def getargvalues(frame: types.FrameType):
    """Get information about arguments passed into a particular frame.

    A tuple of four things is returned: (args, varargs, varkw, locals).
    'args' is a list of the argument names.
    'varargs' and 'varkw' are the names of the * and ** arguments or None.
    'locals' is the locals dictionary of the given frame.
    """
    args, varargs, varkw = getargs(frame.f_code)
    return ArgInfo(args, varargs, varkw, frame.f_locals)


def formatannotation(annotation: Any, base_module: str | None = None) -> str:
    if getattr(annotation, "__module__", None) == "typing":

        def repl(match):
            text = match.group()
            return text.removeprefix("typing.")

        return re.sub(r"[\w\.]+", repl, repr(annotation))
    if isinstance(annotation, types.GenericAlias):
        return str(annotation)
    if isinstance(annotation, type):
        if annotation.__module__ in ("builtins", base_module):
            return annotation.__qualname__
        return annotation.__module__ + "." + annotation.__qualname__
    return repr(annotation)


def formatannotationrelativeto(obj: Any) -> Callable[[Any], str]:
    module = getattr(obj, "__module__", None)

    def _formatannotation(annotation):
        return formatannotation(annotation, module)

    return _formatannotation


def formatargvalues(
    args: list[str],
    varargs: str | None,
    varkw: str | None,
    localns: dict[str, Any],
    formatarg: Callable[[str], str] = str,
    formatvarargs: Callable[[str], str] = lambda name: "*" + name,
    formatvarkw: Callable[[str], str] = lambda name: "**" + name,
    formatvalue: Callable[[Any], str] = lambda value: "=" + repr(value),
) -> str:
    """Format an argument spec from the 4 values returned by getargvalues.

    The first four arguments are (args, varargs, varkw, locals).  The
    next four arguments are the corresponding optional formatting functions
    that are called to turn names and values into strings.  The ninth
    argument is an optional function to format the sequence of arguments.
    """

    def convert(name: str, localns=localns, formatarg=formatarg, formatvalue=formatvalue):
        return formatarg(name) + formatvalue(localns[name])

    specs = []
    for i in range(len(args)):
        specs.append(convert(args[i]))
    if varargs:
        specs.append(formatvarargs(varargs) + formatvalue(localns[varargs]))
    if varkw:
        specs.append(formatvarkw(varkw) + formatvalue(localns[varkw]))
    return "(" + ", ".join(specs) + ")"


def _missing_arguments(f_name: str, argnames: Iterable[str], pos: bool, values: Mapping[str, Any]):
    names = [repr(name) for name in argnames if name not in values]
    missing = len(names)
    if missing == 1:
        s = names[0]
    elif missing == 2:
        s = "{} and {}".format(*names)
    else:
        tail = ", {} and {}".format(*names[-2:])
        del names[-2:]
        s = ", ".join(names) + tail
    raise TypeError(f"{f_name}() missing {missing} required {'' if missing == 1 else 's'} argument{'' if missing == 1 else 's'}: {s}")


def _too_many(f_name, args, kwonly, varargs, defcount, given, values):
    atleast = len(args) - defcount
    kwonly_given = len([arg for arg in kwonly if arg in values])
    if varargs:
        plural = atleast != 1
        sig = f"at least {atleast}"
    elif defcount:
        plural = True
        sig = f"from {atleast} to {len(args)}"
    else:
        plural = len(args) != 1
        sig = str(len(args))
    kwonly_sig = ""
    if kwonly_given:
        msg = " positional argument%s (and %d keyword-only argument%s)"
        kwonly_sig = msg % ("s" if given != 1 else "", kwonly_given, "s" if kwonly_given != 1 else "")
    raise TypeError(
        f"{f_name}() takes {sig} positional argument{'' if plural else 's'} but {given}{kwonly_sig} {'' if given == 1 and not kwonly_given else 'were'} given",
    )


def getcallargs(func: types.FunctionType | types.MethodType | types.FunctionType, /, *positional: Any, **named: Any) -> dict[str, Any]:
    """Get the mapping of arguments to values.

    A dict is returned, with keys the function argument names (including the
    names of the * and ** arguments, if any), and values the respective bound
    values from 'positional' and 'named'.
    """
    posonly, pos_or_kw, kwonlyargs, varargs, varkw, posonly_defaults, pos_or_kw_defaults, kwonlydefaults, annotations = getfullargspec(func)
    f_name = func.__name__
    arg2value = {}

    if ismethod(func) and func.__self__ is not None:
        # implicit 'self' (or 'cls' for classmethods) argument
        positional = (func.__self__,) + positional
    num_pos = len(positional)
    num_args = len(args := positional + kwonlyargs)
    defaults = (posonly_defaults or ()) + (pos_or_kw_defaults or ())
    num_defaults = len(defaults)

    n = min(num_pos, num_args)
    for i in range(n):
        arg2value[args[i]] = positional[i]
    if varargs:
        arg2value[varargs] = tuple(positional[n:])
    possible_kwargs = set(args[len(posonly):] + kwonlyargs)
    if varkw:
        arg2value[varkw] = {}
    for kw, value in named.items():
        if kw not in possible_kwargs:
            if not varkw:
                raise TypeError(f"{f_name}() got an unexpected keyword argument {kw!r}")
            arg2value[varkw][kw] = value
            continue
        if kw in arg2value:
            raise TypeError(f"{f_name}() got multiple values for argument {kw!r}")
        arg2value[kw] = value
    if num_pos > num_args and not varargs:
        _too_many(f_name, args, kwonlyargs, varargs, num_defaults, num_pos, arg2value)
    if num_pos < num_args:
        req = args[: num_args - num_defaults]
        for arg in req:
            if arg not in arg2value:
                _missing_arguments(f_name, req, True, arg2value)
        for i, arg in enumerate(args[num_args - num_defaults :]):
            if arg not in arg2value:
                if defaults is None:
                    raise TypeError(f"{f_name}() missing {len(req) - num_pos} required positional argument{'' if len(req) - num_pos == 1 else 's'}")
                arg2value[arg] = defaults[i]
    missing = 0
    for kwarg in kwonlyargs:
        if kwarg not in arg2value:
            if kwonlydefaults and kwarg in kwonlydefaults:
                arg2value[kwarg] = kwonlydefaults[kwarg]
            else:
                missing += 1
    if missing:
        _missing_arguments(f_name, kwonlyargs, False, arg2value)
    return arg2value


ClosureVars = namedtuple("ClosureVars", "nonlocals globals builtins unbound")


def getclosurevars(func):
    """Get the mapping of free variables to their current values.

    Returns a named tuple of dicts mapping the current nonlocal, global
    and builtin references as seen by the body of the function. A final
    set of unbound names that could not be resolved is also provided.
    """
    if ismethod(func):
        func = func.__func__

    if not isfunction(func):
        raise TypeError(f"{func!r} is not a Python function")

    code = func.__code__
    # Nonlocal references are named in co_freevars and resolved
    # by looking them up in __closure__ by positional index
    nonlocal_vars = {} if func.__closure__ is None else {var: cell.cell_contents for var, cell in zip(code.co_freevars, func.__closure__, strict=False)}

    # Global and builtin references are named in co_names and resolved
    # by looking them up in __globals__ or __builtins__
    global_ns = func.__globals__
    builtin_ns = global_ns.get("__builtins__", builtins.__dict__)
    if ismodule(builtin_ns):
        builtin_ns = builtin_ns.__dict__
    global_vars = {}
    builtin_vars = {}
    unbound_names = set()
    for name in code.co_names:
        if name in ("None", "True", "False"):
            # Because these used to be builtins instead of keywords, they
            # may still show up as name references. We ignore them.
            continue
        try:
            global_vars[name] = global_ns[name]
        except KeyError:
            try:
                builtin_vars[name] = builtin_ns[name]
            except KeyError:
                unbound_names.add(name)

    return ClosureVars(nonlocal_vars, global_vars, builtin_vars, unbound_names)


# -------------------------------------------------- stack frame extraction
def is_classmethod(obj: "classmethod[type[U], P, T]|Any") -> "TypeIs[classmethod[type[U], P, T]]":
    return isinstance(obj, classmethod)


class _Traceback(NamedTuple):
    filename: str | None
    lineno: int
    function: str | None
    code_context: list[str] | None
    index: Any
    positions: tuple[int | None, int | None, int | None, int | None] = (None, None, None, None)


class Traceback(_Traceback):
    def __new__(
        cls, filename: str | None, lineno: int, function: str | None, code_context: list[str] | None, index: int | None, *, positions=(None, None, None, None),
    ):
        return super().__new__(cls, filename, lineno, function, code_context, index, positions=positions)


def _get_code_position_from_tb(tb: types.TracebackType) -> tuple[int | None, int | None, int | None, int | None]:
    code, instruction_index = tb.tb_frame.f_code, tb.tb_lasti
    return _get_code_position(code, instruction_index)


def _get_code_position(code: types.CodeType, instruction_index: int) -> tuple[int | None, int | None, int | None, int | None]:
    if instruction_index < 0:
        return (None, None, None, None)
    positions_gen = code.co_positions()
    # The nth entry in code.co_positions() corresponds to instruction (2*n)th since Python 3.10+
    return next(islice(positions_gen, instruction_index // 2, None))


def getframeinfo(frame: "types.FrameType|types.TracebackType", context=1) -> "Traceback":
    """Get information about a frame or traceback object.

    A tuple of five things is returned: the filename, the line number of
    the current line, the function name, a list of lines of context from
    the source code, and the index of the current line within that list.
    The optional second argument specifies the number of lines of context
    to return, which are centered around the current line.
    """
    if istraceback(frame):
        positions = _get_code_position_from_tb(frame)
        lineno = frame.tb_lineno
        frame = frame.tb_frame
    else:
        lineno = frame.f_lineno
        positions = _get_code_position(frame.f_code, frame.f_lasti)

    if positions[0] is None:
        frame, *positions = (frame, lineno, *positions[1:])

    lineno = positions[0]
    if not isinstance(lineno, int):
        raise TypeError(f"lineno is not an integer: {lineno!r}")

    if not isframe(frame):
        raise TypeError(f"{frame!r} is not a frame or traceback object")

    filename = getsourcefile(frame) or str(getfile(frame))
    if context > 0:
        start = lineno - 1 - context // 2
        try:
            lines, lnum = findsource(frame)
        except OSError:
            lines = index = None
        else:
            start = max(0, min(start, len(lines) - context))
            lines = lines[start : start + context]
            index = lineno - 1 - start
    else:
        lines = index = None

    return Traceback(filename, lineno, frame.f_code.co_name, lines, index, positions=dis.Positions(*positions))


class FrameInfo(Traceback):
    frame: types.FrameType

    def __new__(
        cls,
        frame: types.FrameType,
        filename: str | None,
        lineno: int,
        function: str | None,
        code_context: list[str] | None,
        index: int | None,
        *,
        positions=None,
    ):
        instance = super().__new__(cls, frame, filename, lineno, function, code_context, index)
        instance.positions = positions
        return instance

    def __repr__(self):
        return (
            f"FrameInfo(frame={self.frame!r}, filename={self.filename!r}, lineno={self.lineno!r}, function={self.function!r}, "
            f"code_context={self.code_context!r}, index={self.index!r}, positions={self.positions!r})"
        )


def getouterframes(frame, context=1):
    """Get a list of records for a frame and all higher (calling) frames.

    Each record contains a frame object, filename, line number, function
    name, a list of lines of context, and index within the context.
    """
    framelist = []
    while frame:
        traceback_info = getframeinfo(frame, context)
        frameinfo = (frame,) + traceback_info
        framelist.append(FrameInfo(*frameinfo, positions=traceback_info.positions))
        frame = frame.f_back
    return framelist


def getinnerframes(tb, context=1):
    """Get a list of records for a traceback's frame and all lower frames.

    Each record contains a frame object, filename, line number, function
    name, a list of lines of context, and index within the context.
    """
    framelist = []
    while tb:
        traceback_info = getframeinfo(tb, context)
        frameinfo = (tb.tb_frame,) + traceback_info
        framelist.append(FrameInfo(*frameinfo, positions=traceback_info.positions))
        tb = tb.tb_next
    return framelist


def currentframe():
    """Return the frame of the caller or None if this is not possible."""
    return sys._getframe(1) if hasattr(sys, "_getframe") else None


def stack(context=1):
    """Return a list of records for the stack above the caller's frame."""
    return getouterframes(sys._getframe(1), context)


def trace(context=1):
    """Return a list of records for the stack below the current exception."""
    return getinnerframes(sys.exc_info()[2], context)


# ------------------------------------------------ static version of getattr

_sentinel = object()


def _static_getmro(klass):
    return type.__dict__["__mro__"].__get__(klass)  # type: ignore


def _check_instance(obj, attr):
    instance_dict = {}
    with suppress(AttributeError):
        instance_dict = object.__getattribute__(obj, "__dict__")
    return dict.get(instance_dict, attr, _sentinel)


def _check_class(klass, attr):
    for entry in _static_getmro(klass):
        if _shadowed_dict(type(entry)) is _sentinel:
            try:
                return entry.__dict__[attr]
            except KeyError:
                pass
    return _sentinel


def _is_type(obj):
    try:
        _static_getmro(obj)
    except TypeError:
        return False
    return True


def _shadowed_dict(klass):
    dict_attr = cast(type[Any], type).__dict__["__dict__"]
    for entry in _static_getmro(klass):
        try:
            class_dict = dict_attr.__get__(entry)["__dict__"]
        except KeyError:
            pass
        else:
            if not (type(class_dict) is types.GetSetDescriptorType and class_dict.__name__ == "__dict__" and class_dict.__objclass__ is entry):
                return class_dict
    return _sentinel


def getattr_static(obj, attr, default=_sentinel):
    """Retrieve attributes without triggering dynamic lookup via the descriptor protocol,  __getattr__ or __getattribute__.

    Note: this function may not be able to retrieve all attributes
    that getattr can fetch (like dynamically created attributes)
    and may find attributes that getattr can't (like descriptors
    that raise AttributeError). It can also return descriptor objects
    instead of instance members in some cases. See the
    documentation for details.
    """
    instance_result = _sentinel
    if not _is_type(obj):
        klass = type(obj)
        dict_attr = _shadowed_dict(klass)
        if dict_attr is _sentinel or type(dict_attr) is types.MemberDescriptorType:
            instance_result = _check_instance(obj, attr)
    else:
        klass = obj

    klass_result = _check_class(klass, attr)

    if (
        instance_result is not _sentinel
        and klass_result is not _sentinel
        and _check_class(type(klass_result), "__get__") is not _sentinel
        and (_check_class(type(klass_result), "__set__") is not _sentinel or _check_class(type(klass_result), "__delete__") is not _sentinel)
    ):
        return klass_result

    if instance_result is not _sentinel:
        return instance_result
    if klass_result is not _sentinel:
        return klass_result

    if obj is klass:
        # for types we check the metaclass too
        for entry in _static_getmro(type(klass)):
            if _shadowed_dict(type(entry)) is _sentinel:
                try:
                    return entry.__dict__[attr]
                except KeyError:
                    pass
    if default is not _sentinel:
        return default
    raise AttributeError(attr)


def _getmembers(obj, predicate, getter):
    from inspect import getmro

    results = []
    processed = set()
    names = dir(obj)
    if isclass(obj):
        mro = (obj,) + getmro(obj)
        # add any DynamicClassAttributes to the list of names if object is a class;
        # this may result in duplicate entries if, for example, a virtual
        # attribute with the same name as a DynamicClassAttribute exists
        try:
            for base in obj.__bases__:
                for k, v in base.__dict__.items():
                    if isinstance(v, types.DynamicClassAttribute):
                        names.append(k)
        except AttributeError:
            pass
    else:
        mro = ()
    for key in names:
        # First try to get the value via getattr.  Some descriptors don't
        # like calling their __get__ (see bug #1785), so fall back to
        # looking in the __dict__.
        try:
            value = getter(obj, key)
            # handle the duplicate key
            if key in processed:
                raise AttributeError
        except AttributeError:
            for base in mro:
                if key in base.__dict__:
                    value = base.__dict__[key]
                    break
            else:
                # could be a (currently) missing slot member, or a buggy
                # __dir__; discard and move on
                continue
        if not predicate or predicate(value):
            results.append((key, value))
        processed.add(key)
    results.sort(key=lambda pair: pair[0])
    return results


def getmembers(obj: Any, predicate: Callable[[Any], bool] | None = None) -> list[tuple[str, Any]]:
    """Return all members of an object as (name, value) pairs sorted by name.

    Optionally, only return members that satisfy a given predicate.
    """
    return _getmembers(obj, predicate, getattr)


def getmembers_static(obj, predicate=None):
    """Return all members of an object as (name, value) pairs sorted by name without triggering dynamic lookup via the descriptor protocol.

    Optionally, only return members that satisfy a given predicate.

    Note: this function may not be able to retrieve all members
       that getmembers can fetch (like dynamically created attributes)
       and may find members that getmembers can't (like descriptors
       that raise AttributeError). It can also return descriptor objects
       instead of instance members in some cases.
    """
    return _getmembers(obj, predicate, getattr_static)

def lineno(obj: Any) -> int:
    f = getabsfile(obj)
    sourcelines = getsource(obj).splitlines()
    file_lines = Path(f).read_text().splitlines()
    return file_lines.index(sourcelines[0]) + 1
