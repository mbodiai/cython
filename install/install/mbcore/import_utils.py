import os
import sys
from pathlib import Path

TYPE_CHECKING = False
if TYPE_CHECKING:
    from io import TextIOWrapper
    from collections.abc import Callable
    from pathlib import Path
    from types import FrameType, ModuleType

    from typing_extensions import Any, Protocol, TypeVar, ParamSpec, overload, Literal
    from typing import Iterable

    T = TypeVar("T", covariant=True)
    U = TypeVar("U", covariant=True)
    P = ParamSpec("P")

    class Object(Protocol[T, U]):
        ...
else:
    Protocol = type(tuple[int, ...].__origin__)
    Literal = Protocol
    Any = object
    class ParamSpec:
        args: type[tuple[str, ...]]
        kwargs: type[tuple[str, ...]]

        def __init__(self, *args, **kwargs):
            self.args = args
            self.kwargs = kwargs

    class TypeVar:

        def __init__(self, *args, **kwargs):
            pass

    def overload(*args, **kwargs):
        return lambda f: f
    


    TextIOWrapper = object

    T = TypeVar("T")
    U = TypeVar("U")
    P = ParamSpec("P")

    Object = Protocol
    ModuleType = type(sys)
    Callable = Protocol
    Iterable = type(list[str].__origin__)

def files(path: str) -> "Path":
    from importlib.resources import files
    from pathlib import Path

    from typing_extensions import cast

    return cast(Path, files(path))





class ErrorDuringImport(Exception):
    """Errors that occurred while trying to import something to document it."""

    def __init__(self, filename, exc_info):
        self.filename = filename
        self.exc, self.value, self.tb = exc_info

    def __str__(self):
        exc = self.exc.__name__
        return "problem in %s - %s: %s" % (self.filename, exc, self.value)


def importfile(path):
    """Import a Python source file or compiled file given its path."""
    import importlib._bootstrap
    import importlib._bootstrap_external
    import importlib.util
    import os
    import sys

    magic = importlib.util.MAGIC_NUMBER
    with open(path, "rb") as file:
        is_bytecode = magic == file.read(len(magic))
    filename = os.path.basename(path)
    name, ext = os.path.splitext(filename)
    if is_bytecode:
        loader = importlib._bootstrap_external.SourcelessFileLoader(name, path)
    else:
        loader = importlib._bootstrap_external.SourceFileLoader(name, path)
    # XXX We probably don't need to pass in the loader here.
    spec = importlib.util.spec_from_file_location(name, path, loader=loader)
    try:
        return importlib._bootstrap._load(spec)
    except:
        raise ErrorDuringImport(path, sys.exc_info())


def safe_import(path: str,
                forceload: int = 0,
                frame: "FrameType|None" = None) -> ModuleType | None:
    """Import a module; handle errors; return None if the module isn't found.

    If the module *is* found but an exception occurs, it's wrapped in an
    ErrorDuringImport exception and reraised.  Unlike __import__, if a
    package path is specified, the module at the end of the path is returned,
    not the package at the beginning.  If the optional 'forceload' argument
    is 1, we reload the module from disk (unless it's a dynamic extension).
    """
    import sys

    try:
        # Attempt to explicitly load typing_extensions from the environment first
        import typing_extensions
    except ImportError:
        # If it's not installed in the env, that's okay, proceed anyway
        pass
    cache = _cached
    try:
        # If forceload is 1 and the module has been previously loaded from
        # disk, we always have to reload the module.  Checking the file's
        # mtime isn't good enough (e.g. the module could contain a class
        # that inherits from another module that has changed).
        if forceload and path in sys.modules:
            if path not in sys.builtin_module_names:
                # Remove the module from sys.modules and re-import to try
                # and avoid problems with partially loaded modules.
                # Also remove any submodules because they won't appear
                # in the newly loaded module's namespace if they're already
                # in sys.modules.
                subs = [m for m in sys.modules if m.startswith(path + ".")]
                for key in [path] + subs:
                    # Prevent garbage collection.
                    cache[key] = sys.modules[key]
                    del sys.modules[key]
        module = import_module(path)
    except Exception:

        # Did the error occur before or after the module was found?
        (exc, value, tb) = info = sys.exc_info()
        if path in sys.modules:
            # An error occurred while executing the imported module.
            raise ErrorDuringImport(sys.modules[path].__file__, info)
        if exc is SyntaxError and tb:
            # A SyntaxError occurred before we could execute the module.
            raise ErrorDuringImport((tb.tb_next
                                     or tb).tb_frame.f_code.co_filename, info)
        if isinstance(exc, ImportError) and getattr(value, "name",
                                                    None) == path:
            # No such module in the path.
            return None
        # Some other error occurred during the importing process.
        raise ErrorDuringImport(path, sys.exc_info())
    for part in path.split(".")[1:]:
        try:
            module = getattr(module, part)
        except AttributeError:
            return None
    return module


# -----
def locate(path, forceload=0):
    """Locate an object by name or dotted path, importing as necessary."""
    import builtins

    parts = [part for part in path.split(".") if part]
    module, n = None, 0
    while n < len(parts):
        nextmodule = safe_import(".".join(parts[:n + 1]), forceload)
        if nextmodule:
            module, n = nextmodule, n + 1
        else:
            break
    if module:
        object = module
    else:
        object = builtins
    for part in parts[n:]:
        try:
            object = getattr(object, part)
        except AttributeError:
            return None
    return object


def resolve(thing, forceload=0):
    """Given an object or a path to an object, get the object and its name."""
    import os
    import sys

    if os.sep in thing:
        from importlib import import_module
        from pathlib import Path

        mod, path = Path(thing).stem, thing
        return import_module(mod), mod
    if isinstance(thing, str):
        import os
        import sys

        thing = thing.replace(":", ".").replace("-", "_")
        if thing in sys.modules:
            return sys.modules[thing], thing
        if thing in _cached:
            return _cached[thing], thing

        object = locate(thing, forceload)
        return object, thing
    name = getattr(thing, "__name__", None)
    return thing, name if isinstance(name, str) else None


def import_module(name: str, package: str | None = None):
    import importlib

    name = name.replace(":", ".").replace("-", "_")
    try:
        if "." in name:
            name, obj = name.rsplit(".", 1)
            return getattr(import_module(name, package), obj)
        return importlib.import_module(name, package)
    except Exception as e:
        if "." in name:
            name, obj = name.rsplit(".", 1)

            if "." in name:
                package, name = name.rsplit(".", 1)
                return getattr(import_module(name, package), obj)
        raise e


def reload(module: ModuleType):
    from importlib import reload
    import sys
    del sys.modules[module.__name__]
    del globals()[module.__name__]
    package = getattr(module, "__qualname__", "").rsplit(".", 1)[0]
    if package:
        module = import_module(module.__name__, package)
    else:
        module = import_module(module.__name__)
    return reload(module)


_cached: "dict[ModulePackage, Any]" = {}

def first_true(iterable: "Iterable[T]", default: "T | None" = None, pred: "Callable[[T], bool] | None" = None) -> "T | None":
    """Return the first true value in the iterable.
    
    If no true value is found, return the default.
    """
    return next(filter(pred, iterable), default)

class LazyModule(ModuleType):
    name: str
    obj: Any
    def __new__(cls, name: str):
        self = super().__new__(cls)
        self.__init__(name)
        return self
    def __init__(self, name: str):
        object.__setattr__(self, "name", name)
        object.__setattr__(self, "obj", None)

    def __call__(self, *args: Any, **kwargs: Any) -> Any:
        if (obj:=object.__getattribute__(self, "obj")) is  None:
            object.__setattr__(self, "obj", ModulePackage(self.name).target)
        return object.__getattribute__(self, "obj")(*args,**kwargs)
    def __getattr__(self, item:str):
        if (obj:=object.__getattribute__(self, "obj")) is  None:
            object.__setattr__(self, "obj", ModulePackage(self.name).target)
        return getattr(object.__getattribute__(self, "obj"), item)
    
    def __setattr__(self, key: str, value: Any) -> None:
        if key == "obj":
            super().__setattr__(key, value)
            return
        if object.__getattribute__(self, "obj") is  None:
            object.__setattr__(self, "obj", ModulePackage(self.name).target)
        setattr(object.__getattribute__(self, "obj"), key, value)

    def __getitem__(self, key: Any) -> Any:
        """Handle subscript access (e.g., module[key] or Class[key])."""
        if (obj := object.__getattribute__(self, "obj")) is None:
            object.__setattr__(self, "obj", ModulePackage(self.name).target)
            obj = object.__getattribute__(self, "obj")
            
        # Try regular __getitem__ first
        try:
            # Directly attempt subscripting on the loaded object
            return obj[key]
        except TypeError as e_getitem:
            # If regular __getitem__ fails, check for __class_getitem__
            if isinstance(obj, type):
                 # Get the __class_getitem__ method explicitly
                 class_getitem_method = getattr(obj, "__class_getitem__", None)
                 if class_getitem_method is not None and callable(class_getitem_method):
                     try:
                         # Call the resolved __class_getitem__ method
                         return class_getitem_method(key)
                     except Exception as e_classgetitem:
                         # If __class_getitem__ itself raises an error
                         raise TypeError(f"Object {type(obj).__name__} failed on __class_getitem__({key!r}): {e_classgetitem}") from e_classgetitem
                 else:
                     # No __class_getitem__ found or not callable
                     raise TypeError(f"'{type(obj).__name__}' object is not subscriptable (no valid __getitem__ or __class_getitem__)") from e_getitem
            else:
                 # Not a type, so re-raise the original TypeError from __getitem__ attempt
                 raise e_getitem

    # Ensure __hash__ and __eq__ are handled appropriately if needed, 
    # though inheriting from ModuleType might cover this.
    # Consider adding __repr__ and __str__ for better debugging.
    def __repr__(self) -> str:
        obj = object.__getattribute__(self, "obj")
        status = "loaded" if obj is not None else "lazy"
        target = repr(obj) if obj is not None else self.name
        return f"<LazyModule {status} for '{target}'>"




class ModulePackage:
    """
    Loads:
      - A file path (/path/to/module.py)
      - A dotted module path (some.pkg.subpkg)
      - Fallback: final dotted segment is an attribute
    """
    name: str
    package_name: str
    module_name: str
    attr_name: str | None
    attr: Any | None
    target: Any
    module: ModuleType
    path: Path | None

    def __hash__(self):
        return hash(
            frozenset((self.name, self.package_name, self.module_name,
                       self.attr_name)))

    @overload
    def __init__(self, package: str | ModuleType, module: str | ModuleType,
                 attr: Any, path: Path):
        ...

    @overload
    def __init__(self, name: str):
        ...

    @overload
    def __init__(self, path: Path):
        ...

    def __init__(self, *args: Any, **kwargs: Any):
        self.name = ""
        self.package_name = ""
        self.module_name = ""
        self.attr_name = None
        self.attr = None
        self.target = None
        self.module = None
        self.path = None
       

        if len(args) == 1 and isinstance(args[0], (str, Path)):
            raw = str(args[0])
            if os.path.sep in raw:
                self._init_from_file(raw)
            else:
                self._init_from_dotted(raw)
        else:
            dotted = ".".join(str(a) for a in args)
            self._init_from_dotted(dotted)

    def _init_from_file(self, file_path: str):
        import importlib.util
        from importlib.util import spec_from_file_location, module_from_spec
        p = Path(file_path).resolve()
        if not p.is_file():
            raise FileNotFoundError(f"Cannot find module file: {p}")

        mod_name = p.stem
        spec = spec_from_file_location(mod_name, str(p))
        if not spec or not spec.loader:
            raise ImportError(f"Could not create import spec for {p}")

        mod = module_from_spec(spec)
        sys.modules[mod_name] = mod
        spec.loader.exec_module(mod)  # type: ignore

        self.module = mod
        self.module_name = mod_name
        self.target = mod
        self.name = mod_name
        self.path = p
        self.package_name = ""

    def _init_from_dotted(self, dotted: str):
        """
        If import_module(dotted) fails with "No module named..." or partial-init, re-raise.
        Otherwise fallback to the final dotted piece as an attribute in the parent module.
        """
        try:
            mod = import_module(dotted)
            self.module = mod
            self.target = mod
            self.name = dotted.rsplit('.', 1)[-1]
            self.module_name = self.name
            self.package_name = dotted.rsplit('.',
                                              1)[0] if '.' in dotted else ''
            if hasattr(mod, '__file__'):
                self.path = Path(mod.__file__).resolve()  # type: ignore
            return
        except ImportError as e:
            msg = str(e)
            if "No module named" in msg or "partially initialized module" in msg:
                raise

        # fallback for final piece as attribute
        if '.' not in dotted:
            raise ImportError(
                f"Cannot import '{dotted}' and no fallback attribute possible."
            )

        *parts, last = dotted.split('.')
        parent_str = ".".join(parts)
        parent_mod = import_module(parent_str)
        if not hasattr(parent_mod, last):
            raise ImportError(
                f"Module '{parent_str}' has no attribute '{last}'.")

        self.module = parent_mod
        self.module_name = parts[-1] if parts else parent_str
        self.package_name = ".".join(parts[:-1])
        if hasattr(parent_mod, '__file__'):
            self.path = Path(parent_mod.__file__).resolve()  # type: ignore

        self.attr_name = last
        self.attr = getattr(parent_mod, last)
        self.target = self.attr
        self.name = last


class FileLock:
    f: "TextIOWrapper"
    path: Path

    def __init__(self, path: Path):
        self.path = path

    def __enter__(self):
        """Exclusive file lock with fcntl, for concurrency safety."""

        self.path.touch(exist_ok=True)
        f = self.path.open("r+")
        if sys.platform == "win32":
            import msvcrt
            msvcrt.locking(f.fileno(), msvcrt.LK_NBLCK, 1)
        else:
            import fcntl
            fcntl.flock(f, fcntl.LOCK_EX)
        self.f = f
        return self

    def close(self):
        if sys.platform == "win32":
            import msvcrt
            msvcrt.locking(self.f.fileno(), msvcrt.LK_UNLCK, 1)
        else:

            import fcntl
            fcntl.flock(self.f, fcntl.LOCK_UN)
            self.f.close()

    def __exit__(self, exc_type, exc_value, traceback):
        self.close()


def _insert_before_first_nonimport(lines: list[str],
                                   lines_to_add: list[str]) -> list[str]:
    """
    Parse the AST, find the first top-level statement that isn't an Import/ImportFrom,
    then insert `lines_to_add` *before* that statement.

    If everything is imports or file is empty, append at the end.
    """
    import ast
    code = "\n".join(lines)
    try:
        mod = ast.parse(code)
    except SyntaxError:
        # If the file is invalid, just append
        return lines + lines_to_add

    insertion_line: int | None = None
    for node in mod.body:
        if not isinstance(node, (ast.Import, ast.ImportFrom)):
            # This is the first top-level statement that's not an import
            insertion_line = node.lineno
            break

    # If we never found a non-import statement, we do it at the end
    if insertion_line is None:
        insertion_line = len(lines)  # append

    # The node's lineno is 1-based. We'll treat it as an index in 0-based array
    # and insert *before* that line => insertion_line - 1
    insertion_idx = insertion_line - 1
    if insertion_idx < 0:
        insertion_idx = 0

    new_lines = []
    new_lines.extend(lines[:insertion_idx])
    new_lines.extend(lines_to_add)
    new_lines.extend(lines[insertion_idx:])
    return new_lines


def _modify_same_file(func: Callable[..., T], packages: dict[str,
                                                             ModulePackage]):
    """
    - Lock .py
    - Insert "from typing import TYPE_CHECKING", "TYPE_CHECKING = False",
      and a block "if TYPE_CHECKING: ..." *before* the first non-import
      top-level statement in the file.
    """
    import inspect

    src_file = inspect.getsourcefile(func)
    if not src_file:
        return
    p = Path(src_file).resolve()
    lockp = p.with_name(p.name + ".lock")

    # lines to go inside the `if TYPE_CHECKING:` block
    needed_imports = set()
    for varname, mp in packages.items():
        if "." in varname:
            alias = varname.rsplit('.', 1)[-1]
        else:
            alias = varname

        if mp.package_name and mp.attr_name:
            needed_imports.add(
                f"    from {mp.package_name}.{mp.module_name} import {mp.attr_name}"
            )
        elif mp.package_name:
            dotted = (mp.package_name + "." + mp.module_name).strip(".")
            if alias != mp.module_name:
                needed_imports.add(f"    import {dotted} as {alias}")
            else:
                needed_imports.add(f"    import {dotted}")
        else:
            if mp.module_name and alias != mp.module_name:
                needed_imports.add(f"    import {mp.module_name} as {alias}")
            else:
                needed_imports.add(f"    import {mp.module_name or alias}")

    overhead_lines = []
    overhead_lines.append("TYPE_CHECKING = False")
    overhead_lines.append("if TYPE_CHECKING:")

    # we'll unify them into a single list, something like:
    final_block = list(overhead_lines) + list(needed_imports)

    with FileLock(lockp):
        original = p.read_text(encoding="utf-8").splitlines()

        # We'll ensure we don't re-inject if lines are already present
        # (the lazy approach: we can check if "if TYPE_CHECKING:" is there and the needed lines, but let's keep it simpler).
        # We'll just do a minimal check:
        if all(line in original for line in final_block):
            # everything is already present
            return

        # Insert them right before the first non-import statement
        updated = _insert_before_first_nonimport(original, final_block)

        p.write_text("\n".join(updated) + "\n", encoding="utf-8")


def imports(*modules: str,
            **aliases: str) -> Callable[[Callable[P, T]], Callable[P, T]]:
    """
    Lazy decorator that merges *modules + **aliases => var->dotted import path
    On first call:
      1) do ModulePackage(...) for each
      2) modifies the .py => inserts code before the 1st non-import statement
      3) sets them in func.__globals__
    """

    def decorator(func: Callable[P, T]) -> Callable[P, T]:
        injected = False
        pkgs: dict[str, ModulePackage] = {}

        def wrapper(*args: P.args, **kwargs: P.kwargs) -> T:
            nonlocal injected, pkgs
            if not injected:
                # build var->path from *modules
                final_map: dict[str, str] = {}
                for m in modules:
                    alias = m.rsplit(".", 1)[-1] if "." in m else m
                    final_map[alias] = m
                # plus user-specified aliases
                for var, path in aliases.items():
                    final_map[var] = path

                loaded: dict[str, ModulePackage] = {}
                for var, path in final_map.items():
                    mp = ModulePackage(path)
                    loaded[var] = mp

                _modify_same_file(func, loaded)

                # inject into func globals
                for var, mp in loaded.items():
                    func.__globals__[var] = mp.target

                pkgs = loaded
                injected = True
            return func(*args, **kwargs)

        return wrapper

    return decorator


def smart_import(name: str, mode: Literal["lazy", "reload"] = "lazy") -> Any:
    """Import a module and return the resolved object. Supports . and : delimeters for classes and functions."""
    original_name = name
    name = name.replace(":", ".").replace("-", "_")

    if mode == "lazy":
        return LazyModule(name)
    mp = ModulePackage(name)
    if mode == "reload":
        mp.module = reload(mp.module)
        _cached[mp] = mp.target
        return mp.target

    if mp in _cached:
        return _cached[mp]
    _cached[mp] = mp.target
    return mp.target


def default_export(
    obj: object,
    *,
    key: str | None = None,
) -> object:
    """Assign a function to a module's __call__ attr.

    Args:
        obj: function to be made callable
        key (str): module name as it would appear in sys.modules

    Returns:
        Callable[..., T]: the function passed in

    Raises:
        AttributeError: if key is None and exported obj no __module__ attr
        ValueError: if key is not in sys.modules

    """
    import sys

    try:
        _module: str = key or obj.__module__
    except AttributeError as e:
        msg = f"Object {obj} has no __module__ attribute. Please provide module key"
        raise AttributeError(msg) from e
    from types import ModuleType
    from typing import Any, cast

    class ModuleCls(ModuleType):

        def __call__(self, *args: Any, **kwargs: Any) -> "object":
            return cast(T, obj(*args, **kwargs))  # type: ignore[operator]

    class ModuleClsStaticValue(ModuleCls):

        def __call__(self, *args: Any, **kwargs: Any) -> "object":
            return obj

    mod_cls = ModuleCls if callable(obj) else ModuleClsStaticValue

    try:
        sys.modules[_module].__class__ = mod_cls
    except KeyError as e:
        msg = f"{_module} not found in sys.modules"
        raise ValueError(msg) from e
    return obj


@default_export
def make_callable(obj: "Callable[..., T]",
                  *,
                  key: str | None = None) -> "Callable[..., T]":
    """Assign a function to a module's __call__ attr.

    Args:
        obj: function to be made callable
        key (str): module name as it would appear in sys.modules

    Returns:
        Callable[..., T]: the function passed in

    """
    from typing import cast

    return cast(Callable[..., T], default_export(obj=obj, key=key))


def bootstrap_third_party(modname: str, location: str) -> ModuleType:
    """Bootstrap third-party libraries with debugging."""
    import sys
    from importlib import import_module
    from importlib.util import find_spec, module_from_spec

    try:
        # Find the module spec
        spec = find_spec(modname)
        if not spec:
            msg = f"Module {modname} not found"
            raise ImportError(msg)  # noqa: TRY301

        # Load the module
        mod = module_from_spec(spec)
        assert spec.loader is not None  # Add assertion for loader
        spec.loader.exec_module(mod)

        # Import the parent module at the given location
        new_parent = import_module(location)
        qualified_name = f"{location}.{modname.split('.')[-1]}"

        # Debugging: print information about module and parent
        print(f"Loading module {modname} into {qualified_name}")

        # Attach the module to the parent
        setattr(new_parent, modname.split(".")[-1], mod)
        sys.modules[qualified_name] = mod

        # Update the globals with the new module
        globals().update({qualified_name: mod})
        globals().update({modname: mod})

        # # Recursively bootstrap submodules if necessary, skipping non-modules
        # for k, v in mod.__dict__.items():
        #     if isinstance(v, ModuleType) and k not in sys.modules and v.__name__.startswith(modname):
        #         bootstrap_third_party(k, qualified_name)

        return mod
    except Exception as e:
        # Debugging: Catch any errors and print the module causing issues
        print(f"Error loading module {modname} into {location}: {str(e)}")
        raise
