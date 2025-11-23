"""Import utilities for mbcore."""
import os
import sys
from typing import Any

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Callable
    from dataclasses import InitVar, dataclass, field, replace
    from io import TextIOWrapper
    from pathlib import Path
    from types import FrameType, ModuleType
    from typing import Iterable, cast

    from typing_extensions import Any, Literal, Never, ParamSpec, Protocol, TypeVar
    lazy = "lazy"
    eager = "eager"
    
else:
    Any = Path = object

    class TypeVar:
        args = ()
        kwargs = {}
        def __init__(self, name: str, covariant: bool = False,bound:type|None=None):
            self.name = name
            self.covariant = covariant
            self.bound = bound
            
        def __or__(self, other):
            return self
        def __ror__(self, other):
            return self
        def __class_getitem__(cls, *args):
            return cls
    InitVar = Literal = Callable = ParamSpec = Protocol = TypeVar
    NoReturn = object
    
    def field(default=None,repr=True,init=True,alias=None):
        return type("Field",(),{"default":default,"repr":repr,"init":init,"alias":alias})
    _sentinel = object()
    def dataclass(cls):
        def __init__(self,*args,**kwargs):
            argidx = 0
            initvars = []
            for name, value in cls.__annotations__.items():
                if not getattr(getattr(cls,name,None),"init",True):
                    continue
                if value == InitVar:
                    initvars.append(name)
                    continue
                alias = getattr(getattr(cls,name,None),"alias",_sentinel)
                if name in kwargs or alias in kwargs:
                    setattr(self,name,kwargs[name] if name in kwargs else kwargs[alias])
                elif argidx < len(args):
                    setattr(self,name,args[argidx])
                    argidx += 1
                elif name in cls.__dict__:
                    f = getattr(cls,name)
                    setattr(self,name,getattr(f,"default",f))
                else:
                    raise ValueError(f"{name} is a required field. Got: {args} {kwargs}")
            if hasattr(self,"__post_init__"):
                self.__post_init__(*initvars)
        cls.__init__ = __init__
        cls.__repr__ = lambda self: f"{self.__class__.__name__}({self.name})"
        cls.__hash__ = lambda self: hash((self.name, self.package_name, self.module_name, self.attr_name))  
        return cls
    
    def cast(cls, value):
        return value

    def replace(instance, **kwargs):
        for name, value in kwargs.items():
            setattr(instance, name, value)
        return instance
    

T = TypeVar("T", covariant=True)
U = TypeVar("U", covariant=True)
P = ParamSpec("P")
CallableT = TypeVar("CallableT", bound=Callable)

class Object(Protocol[T, U]): ...
if TYPE_CHECKING:
    from functools import _lru_cache_wrapper
else:
    from _functools import _lru_cache_wrapper

WRAPPER_ASSIGNMENTS = ('__module__', '__name__', '__qualname__', '__doc__',
                       '__annotations__')
WRAPPER_UPDATES = ('__dict__',)

def update_wrapper(wrapper,
                   wrapped,
                   assigned = WRAPPER_ASSIGNMENTS,
                   updated = WRAPPER_UPDATES):
    """Update a wrapper function to look like the wrapped function.

    wrapper is the function to be updated
    wrapped is the original function
    assigned is a tuple naming the attributes assigned directly
    from the wrapped function to the wrapper function (defaults to
    functools.WRAPPER_ASSIGNMENTS)
    updated is a tuple naming the attributes of the wrapper that
    are updated with the corresponding attribute from the wrapped
    function (defaults to functools.WRAPPER_UPDATES)
    """
    for attr in assigned:
        try:
            value = getattr(wrapped, attr)
        except AttributeError:
            pass
        else:
            setattr(wrapper, attr, value)
    for attr in updated:
        getattr(wrapper, attr).update(getattr(wrapped, attr, {}))
    # Issue #17482: set __wrapped__ last so we don't inadvertently copy it
    # from the wrapped function when updating __dict__
    wrapper.__wrapped__ = wrapped
    # Return the wrapper so this can be used as a decorator via partial()
    return wrapper

def cache(maxsize:int|CallableT=128,typed:bool|None=None)->CallableT:
    from collections import namedtuple
    _CacheInfo = namedtuple("CacheInfo", ["hits", "misses", "maxsize", "currsize"])
    if isinstance(maxsize, int):
        # Negative maxsize is treated as 0
        if maxsize < 0:
            maxsize = 0
    elif callable(maxsize):
        func = maxsize
        maxsize = 128
        typed = False

        wrapper = _lru_cache_wrapper(func, maxsize, typed, _CacheInfo)
        wrapper.cache_parameters = lambda : {'maxsize': maxsize, 'typed': typed}
        return update_wrapper(wrapper, func)
   
    def decorating_function(fn):
        wrapper = _lru_cache_wrapper(fn, maxsize, typed, _CacheInfo)
        wrapper.cache_parameters = lambda : {'maxsize': maxsize, 'typed': typed}
        return update_wrapper(wrapper, fn)
    return decorating_function

def files(path: str) -> "Path":
    from importlib.resources import files
    from pathlib import Path

    from typing_extensions import cast

    return cast(Path, files(path))




def reload(module: "ModuleType"):
    import sys
    from importlib import import_module, reload

    del sys.modules[module.__name__]
    del globals()[module.__name__]
    package = getattr(module, "__qualname__", "").rsplit(".", 1)[0]
    module = import_module(module.__name__, package) if package else import_module(module.__name__)
    return reload(module)


def first_true(
    iterable: "Iterable[T]", default: "T | None" = None, pred: "Callable[[T], bool] | None" = None,
) -> "T | None":
    """Return the first true value in the iterable.

    If no true value is found, return the default.
    """
    return next(filter(pred, iterable), default)

class UnsetType:...
Unset = UnsetType()


def raise_chained(*excs: BaseException) -> "Never":
    """Raise all exceptions in `excs` as a single error chain.

    • Py ≥ 3.11 → ExceptionGroup
    • older     → manual __context__/__cause__ chain
    """
    excs = (*(e for es in excs for e in (es if isinstance(es,list|tuple) else (es,))),)
    if not excs:
        raise RuntimeError("raise_chained() called with empty list")

    if len(excs) == 1:
        raise excs[0]

    # if sys.version_info >= (3, 11):
    #     raise ExceptionGroup("Multiple exceptions", list(excs)) # type: ignore #noqa

    prev = excs[0]
    for exc in excs[1:]:
        exc.__cause__ = prev
        exc.__context__ = prev
        prev = exc
    raise prev

def maybe_set_module_attribute(obj: Any, name: str, value: Any):
    if (current := getattr(obj, "__module__", None)) is not None and isinstance(current, LazyModule):
        # Avoid noisy stdout in hot paths; silently set attribute in module
        sys.modules[current.__module__].__dict__[name] = value

NO_PROXY_ATTRIBUTES = (
    "__getattribute__", "__call__", "__getattr__", "__setattr__",
    "_resolve_target",
    "_name", "_obj", "_default", "_errors", "_replace", "_original_module","obj",
    "__repr__", "__str__", "__mro_entries__", "__mro__", "mro", "__bases__", "__subclasses__",
    "__instancecheck__", "__subclasscheck__", "__hash__", "__eq__", "__ne__",
    "__file__", "__package__","__dict__","get_attribute",
)

class _LazyMeta(type):
    def __getitem__(cls, *args: Any, **kwargs: Any) -> Any:
        return cls
class LazyModule(_LazyMeta):
    __type__ = "lazy_module"
    _replace: bool
    _name: str
    _default: type|None
    _errors: list[Exception]
    _mp: "ModulePackage|None"
    _obj: Any|None
    _original_module: "str"

    if TYPE_CHECKING:
        def __getitem__(cls, *args: Any, **kwargs: Any) -> Any:
            return cls.obj.__getitem__(*args, **kwargs)

    def get_attribute(cls,name:str)->Any:
        if name in NO_PROXY_ATTRIBUTES:
            return type.__getattribute__(cls, name)
        # Resolve target without touching cls.obj to avoid proxy re-entry
        current = LazyModule._resolve_target(cls,cls._name)
        if cls._replace:
            setattr(sys.modules[cls._original_module], cls._name, current)
        return getattr(current, name)


    @staticmethod
    def _resolve_target(value:"Any|LazyModule",name:str) -> Any:
        seen: set[int] = set()
        steps = 0
        while type(value) is LazyModule:
            oid = id(value)
            if oid in seen or steps > 128:
                name = type.__getattribute__(value, "_name")
                raise RuntimeError(f"LazyModule target resolution cycle detected for {name}")
            seen.add(oid)
            steps += 1
            target = type.__getattribute__(value, "_obj")
            if target is None:
                name = type.__getattribute__(value, "_name")
                default = type.__getattribute__(value, "_default")
                mp = ModulePackage(name, default=default)
                type.__setattr__(value, "_mp", mp)
                type.__setattr__(value, "_obj", mp.target)
                target = type.__getattribute__(value, "_obj")
            value = target

        return value

    @property
    def obj(cls)->Any:
        # Avoid proxy lookups while resolving the underlying object to prevent recursion
        current = type.__getattribute__(cls, "_obj")
        if current is None:
            default = type.__getattribute__(cls, "_default")
            mp = ModulePackage(cls._name, default=default)
            # Cache the ModulePackage and its target; do not overwrite
            # our local reference with the return value of __setattr__ (which is None).
            type.__setattr__(cls, "_mp", mp)
            type.__setattr__(cls, "_obj", mp.target)
            current = mp.target
        # Unwrap nested LazyModule targets so _obj stabilizes to the real object
        resolved = LazyModule._resolve_target(current,cls._name)
        if resolved is not current:
            type.__setattr__(cls, "_obj", resolved)
        maybe_set_module_attribute(resolved,cls._name,resolved)
        return resolved
    
    @obj.setter
    def obj(cls, value: Any):
        type.__setattr__(cls, "_obj",value)
    
    def __new__(cls, name: str,bases: tuple[type, ...] = (), namespace: dict[str, Any] | None = None, frame: "FrameType|None"=None,default: type|None=None,replace:bool=False):
        if frame is None:
            raise ValueError("frame is required")
        original_module = frame.f_globals.get("__name__", "__main__")
        namespace = namespace or {}
        namespace.update({"_name": name, "_default": default, "_obj": None, "_errors": [], "_replace": replace, "_original_module": original_module})
        return super().__new__(cls, "LazyModule", bases, namespace)

    def __init__(cls, name: str, bases: tuple[type, ...] = (), namespace: dict[str, Any] | None = None, frame: "FrameType|None"=None,**_kwargs: Any):
        _ = frame
        type.__init__(cls, name, bases, {} if namespace is None else namespace)

    def __call__(cls, *args: Any, **kwargs: Any) -> Any:
        return cls.obj(*args, **kwargs)

    def __getattribute__(cls, name: str, /) -> Any:
        if name in NO_PROXY_ATTRIBUTES:
            return type.__getattribute__(cls, name)
        return cls.get_attribute(name)
    
    def __getattr__(cls, item: str):
        return cls.get_attribute(item)

    def __setattr__(cls, key: str, value: Any) -> None:
        if key == "get_attribute":
            type.__setattr__(cls, key, value)
            return
        setattr(cls.get_attribute("obj"), key, value)

                        
        
    def __eq__(cls, other: Any) -> bool:
        target = type.__getattribute__(cls, "obj")
        return target == other
    
    def __ne__(cls, other: Any) -> bool:
        return cls.obj != other
    
    def __hash__(cls) -> int:
        target = type.__getattribute__(cls, "obj")
        return hash(target)

    def __repr__(cls) -> str:
        return f"<LazyModule {cls._name}>"
    
    def __str__(cls) -> str:
        return f"LazyModule({cls._name})"

    def __instancecheck__(cls, other: Any) -> bool:
        target = type.__getattribute__(cls, "obj")
        return isinstance(other, target)

    def __subclasscheck__(cls, other: Any) -> bool:
        target = type.__getattribute__(cls, "obj")
        return issubclass(other, target)

    def __mro_entries__(cls, bases: tuple[type, ...]) -> tuple[type, ...]:
        obj = type.__getattribute__(cls, "obj")
        if isinstance(obj, type):
            return (obj,)
        raise TypeError(f"Lazy base {cls._name!r} resolved to non-type {type(obj).__name__}")

    @property
    def __file__(cls) -> str | None:
        return type.__getattribute__(cls, "obj").__file__

    @property
    def __package__(cls) -> str | None:
        return type.__getattribute__(cls, "obj").__package__


def resolve_default(default: Any | type, parts: list[str], dotted: str) -> Any:
    name = parts[-1] if parts else dotted
    if isinstance(default, type) and issubclass(default, type):
        return default(name, (), {})
    if callable(default) and not isinstance(default, type):
        return default(name)
    return default
  
@cache
def resolve_dotted(dotted: str,package_name:str|None=None,default:Any|type=Unset) -> Any:
    import sys
    from importlib import import_module
    from pathlib import Path
    out:dict[str,Any] = {}
    from Cython.Utility.Inspecting import resolve_main_module_name as resolve_main
    # Try full module import fast-path
    if not dotted:
        if not isinstance(default, UnsetType):
            out["attr"] = out["target"] = resolve_default(default, dotted.split("."), dotted)
            out["name"] = out["target_name"] = dotted
            return out
        from types import SimpleNamespace
        out["module"] = sys.modules.get("__main__")
        out["target"] = SimpleNamespace
        out["name"] = dotted
        out["module_name"] = ""
        out["package_name"] = ""
        out["attr_name"] = "SimpleNamespace"
        out["attr"] = SimpleNamespace
        return out
    errors: list[BaseException] = []

    try:
        mod = import_module(dotted, package_name) if dotted.startswith(".") else import_module(dotted) if dotted not in sys.modules else sys.modules[dotted]
        out["module"] = mod
        out["target"] = mod
        out["name"] = dotted
        out["module_name"] = dotted
        out["package_name"] = dotted.rsplit(".", 1)[0] if "." in dotted else ""
        out["attr_name"] = ""
        out["attr"] = None
        file_attr = getattr(mod, "__file__", None)
        if file_attr is not None:
            out["path"] = Path(file_attr).resolve()
        return out
    except ImportError as e:
        errors.append(e)
    
    parts = dotted.split(".")
    for i in range(len(parts), 0, -1):  
        mod_name = ".".join(parts[:i])
        try:
            mod = import_module(mod_name) if mod_name not in sys.modules else sys.modules[mod_name]
        except ImportError as e:
            try:
                mod = import_module(mod_name, package_name)
            except ImportError as e:
                errors.append(e)
            else:
                errors.append(e)
            continue

        target = mod
        try:
            for attr in parts[i:]:
                target = getattr(target, attr)
        except AttributeError as e:
            errors.append(e)
            if "__main__" in dotted:
                return resolve_dotted(dotted.replace("__main__", resolve_main()),package_name,default)
            if not isinstance(default, UnsetType):
                out["attr"] = out["target"] = resolve_default(default,parts,dotted)
                out["name"] = out["target_name"] = dotted
                return out
            raise_chained(*errors)
        # Success: populate fields and return
        out["module"] = mod
        out["target"] = target
        out["name"] = dotted
        out["module_name"] = mod_name
        out["package_name"] = mod_name.rsplit(".", 1)[0] if "." in mod_name else ""
        out["attr_name"] = parts[-1] if i < len(parts) else ""
        out["attr"] = target if i < len(parts) else None
        file_attr = getattr(mod, "__file__", None)
        if file_attr is not None:
            out["path"] = Path(file_attr).resolve()
        return out 

    if "__main__" in dotted:
        return resolve_dotted(dotted.replace("__main__", resolve_main()),package_name,default)

    # No importable prefix found
    if not isinstance(default, UnsetType):
        out["attr"] = out["target"] = resolve_default(default,parts,dotted)
        out["name"] = out["target_name"] = dotted
        return out
        
    return raise_chained(*errors)

   

    
@dataclass
class ModulePackage:
    """Load a module or object from a file path, a dotted module path, or a dotted attribute path.
    
    - A file path (/path/to/module.py)
    - A dotted module path (some.pkg.subpkg)
    - A dotted attribute path (some.pkg.subpkg.attr)
    - A default object to use if the import fails.

    Attributes:
        name: The name provided to the constructor. Can be a file path, a dotted module path, or a dotted attribute path.
        package_name: The actual package name of the imported module.
        module_name: The actual module name of the imported module.
        attr_name: The actual attribute name of the imported module. None if the imported module is a module.
        attr: The function,class, or submodule that was imported. None if the imported module is a module.
        path: The path to the imported module or object.
        target: The actual module or object that was imported. Set to `attr` or `module` depending on the request.
        target_name: The name of the target object. Set to `attr_name` or `module_name` depending on the request.
        default: The default object to use if the import fails.
        module: The module that was imported.
        _hashvalue: The hash value of the module package.

    """

    name: str | Path
    package_name: str | None = field(default=None,alias="package")
    module_name: str|None = field(default=None,alias="module")
    attr_name: str|None = field(default=None,alias="attr")
    attr: Any | None = field(init=False)
    path: "Path | None" = field(default=None)
    target: Any = field(default=None,init=False)
    target_name: str = field(init=False)
    default: type | UnsetType = Unset   
    module: "ModuleType" = field(default=None,repr=False,init=False)

    _hashvalue: int | None = field(repr=False,init=False, default=None)
    
    
    def __hash__(self):
        if self._hashvalue is None:
            self._hashvalue = hash((self.name, self.package_name, self.module_name, self.attr_name))
        return self._hashvalue
    
    def __post_init__(self):
        self.load()
        self._hashvalue = hash((self.name, self.package_name, self.module_name, self.attr_name))
        
    def load(self):
        from pathlib import Path
        self.name = getattr(self,"name",str(self.name).replace(":", ".").replace("-", "_"))
        if Path(str(self.name)).is_file():
            self.path = Path(str(self.name))
        
        if self.name and not any((self.module, self.attr,self.path)) and isinstance(self.name,str | Path):
            name = str(self.name)
            self._init_from_dotted(name) if os.path.sep not in name else self._init_from_file(name)
        elif self.path is not None:
            self._init_from_file(self.path)
        else:
            # Build a safe dotted path only from known string components
            parts: list[str] = []
            if isinstance(self.name, str) and self.name:
                parts.append(self.name)
            if isinstance(self.module_name, str) and self.module_name:
                parts.append(self.module_name)
            if isinstance(self.attr_name, str) and self.attr_name:
                parts.append(self.attr_name)
            dotted = ".".join(parts)
            self._init_from_dotted(dotted)
    
    

    def _init_from_file(self, file_path: "str|Path"):
        from importlib.util import module_from_spec, spec_from_file_location
        from pathlib import Path

        p = Path(str(file_path)).resolve()
        if not p.is_file():
            raise FileNotFoundError(f"Cannot find module file: {p}")

        mod_name = p.stem
        if mod_name in sys.modules:
            mod = sys.modules[mod_name]
        else:
            
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
        self.attr_name = ""
        self.attr = None

    def _init_from_dotted(self, dotted: str):
        """Resolve dotted path by importing the longest module prefix, then getattr-walking the rest."""
        replace(self,**resolve_dotted(dotted,self.package_name,self.default))


class FileLock:
    f: "TextIOWrapper"
    path: "Path"

    def __init__(self, path: "Path"):
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

    def close(self) -> None:
        if sys.platform == "win32":
            import msvcrt

            msvcrt.locking(self.f.fileno(), msvcrt.LK_UNLCK, 1)
        else:
            import fcntl

            fcntl.flock(self.f, fcntl.LOCK_UN)
            self.f.close()

    def __exit__(self, exc_type, exc_value, traceback):
        self.close()


def _insert_before_first_nonimport(lines: list[str], lines_to_add: list[str]) -> list[str]:
    """Parse the AST, find the first top-level statement that isn't an Import/ImportFrom,
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
        if not isinstance(node, ast.Import | ast.ImportFrom):
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


def _modify_same_file(func: Callable[..., T], packages: dict[str, ModulePackage]):
    """- Lock .py
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
        alias = varname.rsplit(".", 1)[-1] if "." in varname else varname

        if mp.package_name and mp.attr_name:
            needed_imports.add(
                f"    from {mp.package_name}.{mp.module_name} import {mp.attr_name}",
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


def imports(*modules: str, **aliases: str) -> Callable[[Callable[P, T]], Callable[P, T]]:
    """Lazy decorator that merges *modules + **aliases => var->dotted import path.
    
    On first call:
      1) do ModulePackage(...) for each
      2) modifies the .py => inserts code before the 1st non-import statement
      3) sets them in func.__globals__.
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

@cache
def smart_import(name: str, mode: Literal["lazy", "reload", "eager"] = "lazy",default:Any=Unset,replace:bool=False) -> Any:
    """Import a module and return the resolved object. Supports . and : delimeters for classes and functions."""
    frame = sys._getframe(1)
    package_name = frame.f_globals.get("__package__",None)
    if mode == "lazy":
        return LazyModule(name,frame=frame,default=default,replace=replace)
    
    mp = ModulePackage(name,default=default,package=package_name)
    if mode == "reload":
        mp.module = reload(mp.module)
        return mp.target
    if isinstance(mp.target,UnsetType):
        raise ValueError(f"Module {name} not found")
    return mp.target

_P = ParamSpec("_P")
_T = TypeVar("_T")
def default_export(
    obj: Callable[_P, _T] ,
    *,
    key: str | None = None,
) -> Callable[_P, _T]:
    """Assign a function to a module's __call__ attr.

    Args:
    ----
        obj: function to be made callable
        key (str): module name as it would appear in sys.modules

    Returns:
    -------
        Callable[..., T]: the function passed in

    Raises:
    ------
        AttributeError: if key is None and exported obj no __module__ attr
        ValueError: if key is not in sys.modules

    """
    import sys

    try:
        _module: str = key or obj.__module__
    except AttributeError as e:
        msg = f"Object {obj} has no __module__ attribute. Please provide module key"
        raise AttributeError(msg) from e
    from contextlib import suppress
    from types import ModuleType
    from typing import cast

    class ModuleCls(ModuleType):
        def __call__(self, *args: _P.args, **kwargs: _P.kwargs) -> _T:
            return cast(_T, obj(*args, **kwargs))  # type: ignore[operator]

    class ModuleClsStaticValue(ModuleCls):
        def __call__(self, *args: _P.args, **kwargs: _P.kwargs) -> _T:
            return cast(_T, obj)

    mod_cls = ModuleCls if callable(obj) else ModuleClsStaticValue

    with suppress(KeyError):
        sys.modules[_module].__class__ = mod_cls
        return obj
    with suppress(ValueError,AttributeError):
        module = smart_import(_module,mode="eager")
        sys.modules[_module] = module
        module.__class__ = mod_cls
        return obj
    msg = f"{_module} not found in sys.modules"
    raise ValueError(msg)


@default_export
def main(obj: "Callable[P, T]",/,*,key:str|None=None) -> "Callable[P, T]":
    """Assign a function to a module's __call__ attr.

    Usage:
    ```python
    @main
    def my_function(a: int, b: int) -> int:
        return a + b
    ```

    Args:
    ----
        obj: function to be made callable
        key (str): module name as it would appear in sys.modules

    Returns:
    -------
        Callable[..., T]: the function passed in

    """
    return cast("Callable[P, T]",default_export(obj=obj,key=key))


def unshadow_builtins() -> str:
    import os
    import sys

    from Cython.Utility.Inspecting import resolve_main_file

    # NOTE:
    # When this module is executed directly as a script, e.g.
    #     python embdata/sample.py
    # the directory containing this file (the `embdata` package) ends up on
    # `sys.path` ahead of the standard library. Because this package contains a
    # `types` subpackage, that can accidentally shadow Python's stdlib
    # `types` module, which in turn breaks imports inside the standard library
    # (e.g. `enum` / `dataclasses` doing `from types import MappingProxyType`).
    #
    # To avoid that, we:
    #   1. Ensure the project root (parent of this file's directory) is on
    #      `sys.path` so that `embdata.*` imports work.
    #   2. Remove this file's directory from `sys.path` if present, so that
    #      top-level imports like `import types` resolve to the stdlib.
    _here = os.path.dirname(sys._getframe(1).f_globals.get("__file__",resolve_main_file()))
    _project_root = os.path.dirname(_here)
    if _project_root not in sys.path:
        sys.path.insert(0, _project_root)
    if _here in sys.path:
        sys.path.remove(_here)



if __name__ == "__main__":
    
    mod = smart_import("mbcore.display")
    mod.safe_print(dict(mod.__dict__))

    cls = smart_import("mbcore.deque.AsyncDeque")
    assert not  isinstance([], cls | None)

    assert isinstance(cls(), cls),f"Expected {cls}, got {type(cls())}"
