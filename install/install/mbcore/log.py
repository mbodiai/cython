"""Initialize or log a message.

Usage:
    `from mbcore.log import debug`
    1. Check level: `if debug()`
    2. Set level: `debug.set()`
    3. Log message: `debug("Processing file")`

Examples:
```python
    from mbcore.log import debug, info, warning, error, fatal, log

    >>> debug("Processing file")  # Log a message
    >>> if debug():  # Check if debug level is enabled
    ...     print("Will only print if debug level is enabled")
    >>> debug.set()  # Set logging level to DEBUG
    >>> debug.log("Processing file")  # Log a message
    DEBUG: Processing file
```

"""

import sys
from logging import Formatter, getLogger
from logging import debug as pydebug
from logging import log as pylog
from os import getenv

from mbcore.config import LOG_CONFIG, LogConfig
from mbcore.traverse import has_error

TYPE_CHECKING = False
if TYPE_CHECKING:
    from datetime import datetime
    from pathlib import Path
    from re import Pattern
    from types import FrameType, ModuleType

    from rich.text import Text
    from typing_extensions import (
        Any,
        Callable,
        ClassVar,
        Concatenate,
        Final,
        Generic,
        Literal,
        Mapping,
        ParamSpec,
        Self,
        Type,
        TypeAlias,
        TypedDict,
        TypeVar,
        cast,
        overload,
    )

    log: Final = getLogger("default").log
    from mbcore.types import  wrapafter, wraps,wrapcatafter

    _T = TypeVar("_T")
    _P = ParamSpec("_P")
    _R_co = TypeVar("_R_co", covariant=True)

else:

    def cast(x, y):
        return y

    def overload(*args, **kwargs):
        return lambda f: f

    def wrapafter(f, *args, **kwargs):
        return lambda f: f

    def log(*args, **kwargs):
        return getLogger("default").log(
            *args,
            **{
                **kwargs, "stacklevel": 2 + kwargs.get("stacklevel", 0)
            },
        ) or getLogger("verbose").log(
            *args, **{
                **kwargs, "stacklevel": 2 + kwargs.get("stacklevel", 0)
            })

    TypeAlias = type(type)
    TypedDict = type(type)
    Final = type(type)
    Type = type
    Any = object
    Self = object
    ClassVar = type(type)
    datetime = object
    FrameType = object
    Path = object
    Pattern = object
    ModuleType = type(sys)
    wraps = overload
    Literal = type(tuple[str | int, ...].__origin__)
    Mapping = type(dict[str, Any].__origin__)
    TypeVar = lambda *args, **kwargs: type

    class Generic:

        @classmethod
        def __class_getitem__(cls, item):
            return cls

    Concatenate = lambda *args, **kwargs: object
    TypeIs = lambda *args, **kwargs: object

    def wrapafter(*args, **kwargs):
        return lambda f: f

    def wrapcatafter(*args, **kwargs):
        return lambda f: f

    class AsyncGenerator:

        @classmethod
        def __class_getitem__(cls, *items):
            return object

        def __getitem__(self, *items):
            return object

    class Generator:

        @classmethod
        def __class_getitem__(cls, *items):
            return object

        def __getitem__(self, *items):
            return object

    class Coroutine:

        @classmethod
        def __class_getitem__(cls, *items):
            return object

        def __getitem__(self, *items):
            return object

    class Iterable:

        @classmethod
        def __class_getitem__(cls, *items):
            return object

        def __getitem__(self, *items):
            return object

    class Callable:

        @classmethod
        def __class_getitem__(cls, *items):
            return object

        def __getitem__(self, *items):
            return object

        def __call__(self, *args, **kwargs):
            return object

    def wrapafter(*args, **kwargs):
        return lambda f: f

    _T = _R_co = _R = _P = object


class dynamic(Generic[_T, _P, _R_co]):
    """A descriptor that can be used as both a classmethod and instance method.

    Usage:
    ```python
    class MyClass:
        @dynamic()
        def my_method(self_or_cls, arg1, arg2):
            if self_or_cls is MyClass:
                print("Called as class method")
            else:
                print("Called as instance method")

        @dynamic
        def my_property(self_or_cls):
            if self_or_cls is MyClass:
                print("Class property")
            else:
                print("Instance property")

    >>> MyClass.my_method(1, 2)
    Called as class method
    >>> MyClass().my_method(1, 2)
    Called as instance method
    >>> MyClass.my_property
    'Class property'
    >>> MyClass().my_property
    'Instance property'
    ```
    """

    setter: "Callable[[_T, _R_co], Any]"
    getter: "Callable[..., Callable[[_T, _R_co], _R_co]]"
    __wrapped__: "Callable[Concatenate[_T, _P], _R_co] | Callable[Concatenate[type[_T], _P], _R_co] | Callable[Concatenate[_T | type[_T], _P], _R_co]"
    __func__: "Callable[Concatenate[_T, _P], _R_co] | Callable[Concatenate[type[_T], _P], _R_co] | Callable[Concatenate[_T | type[_T], _P], _R_co]"
    __name__: str
    __qualname__: str
    __doc__: str | None
    __module__: str

    def __call__(
        self,
        wrapped:
        "Callable[Concatenate[_T | Type[_T], _P], _R_co] | Callable[Concatenate[_T, _P], _R_co] | Callable[Concatenate[type[_T], _P], _R_co] | None" = None,
    ) -> "dynamic[_T, _P, _R_co]":
        """Dynamic member access. Use @dynamic for properties and @dynamic() for methods.

        Note that properties will return the same class-level object for all instances.
        """
        if wrapped is None:
            raise ValueError("Must provide a callable to @dynamic()")
        self.__prop__ = wrapped
        self.__name__ = getattr(wrapped, "__name__", type(wrapped).__name__)
        self.__qualname__ = getattr(wrapped, "__qualname__",
                                    type(wrapped).__name__)
        self.__doc__ = wrapped.__doc__
        self.__module__ = wrapped.__module__
        self.__wrapped__ = wrapped
        self.__func__ = wrapped
        self.__isabstractmethod__ = bool(
            getattr(wrapped, "__isabstractmethod__", False))
        self._property = False
        return self

    @overload
    def __init__(self,
                 f: "Callable[Concatenate[type[_T], _P], _R_co]") -> None:
        ...

    @overload
    def __init__(self, f: "Callable[Concatenate[_T, _P], _R_co]") -> None:
        ...

    @overload
    def __init__(self, f: None = None) -> None:
        ...

    def __init__(
        self,
        f: " Callable[Concatenate[type[_T], _P], _R_co] | None" = None
    ) -> None:
        """Dynamic member access. Use @dynamic for methods and @dynamic() for properties."""
        if f is None:
            return
        self.__func__ = f
        self.__name__ = f.__name__
        self.__qualname__ = f.__qualname__
        self.__doc__ = f.__doc__
        self.__module__ = f.__module__
        self.__wrapped__ = f
        self.__isabstractmethod__ = bool(
            getattr(f, "__isabstractmethod__", False))
        self._property = True
        self.setter = lambda self, func: setattr(self, "__set__", func)
        self.getter = lambda self, *args, **kwargs: self.__get__(
            *args, **kwargs)

    @overload
    def __get__(self, instance: "_T", owner: "type[_T]") -> "_R_co":
        ...

    @overload
    def __get__(self, instance: None, owner: "type[_T]") -> "_R_co":
        ...

    def __get__(self,
                instance: "_T | None",
                owner: "type[_T] | None" = None) -> "_R_co":
        if self._property:
            if instance is None:
                return self.__func__.__get__(owner, type(owner))()
            return self.__func__.__get__(instance, owner)()
        if instance is None:
            return self.__func__.__get__(owner, type(owner))
        return self.__func__.__get__(instance, owner)


def callstack(depth=0):
    from inspect import getframeinfo

    from mbcore.more import take

    def walk_stack(frame: FrameType | None):
        first = False
        while frame:
            if not first:
                first = True
                frame = frame.f_back
            yield getframeinfo(frame, 5)
            frame = frame.f_back

    return list(take(depth, walk_stack(sys._getframe(1))))


def getframeinfo(
    frame: "FrameType",
    context: int = 10,
    mode: 'Literal["frame", "name", "file"]' = "frame",
) -> "Text|str":
    from inspect import getframeinfo
    from pathlib import Path

    from rich.text import Text

    from mbcore._traceback import Frame, link_fp

    res = getframeinfo(frame, context=context)
    rend = Frame(
        filename=res.filename,
        lineno=res.lineno,
        name=res.function,
        line="\n".join(res.code_context or []),
        module=Path(res.filename).stem,
    )

    code_context = list(filter(None, res.code_context or []))
    if mode == "frame":
        return Text.assemble(
            "\n\n",
            link_fp(
                rend.module + "." +
                rend.name if rend.module != "__main__" else "__main__",
                res.filename,
                res.lineno,
                showpath=False,
                style="bold cyan",
            ),
            "\n\n",
            *code_context[:-1],
            link_fp(code_context[-1],
                    rend.filename,
                    rend.lineno,
                    showpath=False,
                    style="bold yellow"),
        )

    return (link_fp(rend.filename,
                    rend.filename,
                    rend.lineno,
                    showpath=False,
                    style="bold yellow")
            if mode == "file" else link_fp(f"{rend.module}.{rend.name}",
                                           rend.filename,
                                           rend.lineno,
                                           showpath=False,
                                           style="bold cyan"))


@overload
def caller(mode: 'Literal["frame"]' = "frame",
           depth: int = 0,
           context: int = 10,
           *args) -> "list[Text] | Text":
    ...


@overload
def caller(mode: 'Literal["name"]' = "name",
           depth: int = 0,
           n: int = 1,
           *args) -> "list[str] | str":
    ...


@overload
def caller(mode: 'Literal["file"]' = "file",
           depth: int = 0,
           n: int = 1) -> "list[Path] | Path":
    ...


def caller(
    *args, **kwargs
) -> "list[Text | str] | list[str] | list[Path] | Text | str | list[Text] | Path":
    import inspect
    import sys

    from rich.text import Text

    args = list(args)
    mode = kwargs.pop(
        "mode",
        args.pop(0)
        if args and args[0] in ("frame", "name", "file") else "frame")
    depth = kwargs.pop(
        "depth",
        next(iter(args),
             args.pop(0) if args and isinstance(args[0], int) else 0)) + 1
    n = kwargs.pop(
        "n",
        next(iter(args),
             args.pop(0) if args and isinstance(args[0], int) else 1))
    context = kwargs.pop(
        "context",
        next(iter(args),
             args.pop(0) if args and isinstance(args[0], int) else 10))

    try:
        return sys._getframemodulename(depth + 2) or "Unknown"
    except AttributeError:  # For platforms without _getframemodulename()
        pass
    try:
        frame = inspect.currentframe()

        while depth > 0 or "log.py" in frame.f_code.co_filename or "<" in frame.f_code.co_filename:
            frame = frame.f_back
            depth -= 1
        fs = []
        while n > 0:
            fs.append(frame)
            frame = frame.f_back
            n -= 1

        out = [getframeinfo(frame, context=context, mode=mode) for frame in fs]
        return out if len(out) > 1 else out[0]
    except (AttributeError, ValueError):  # For platforms without _getframe()
        import traceback

        traceback.print_exc()
        return Text("Unknown")


def callername(depth=0) -> str:
    return str(Text.from_markup(str(caller(mode="name", depth=depth + 1))))


def callerfile(depth=0) -> "Path":
    from pathlib import Path

    from rich.text import Text

    out = caller(mode="file", depth=depth + 1)
    if isinstance(out, list):
        f = Path(str(Text.from_markup(str(out[0]))))
    else:
        f = Path(str(Text.from_markup(str(out))))
    if "__init__" in f.stem:
        return f.parent.resolve()
    return f


def callermodule(depth=0) -> "ModuleType":
    return sys.modules[callername(depth=depth + 1)]


def callerframe(depth=0) -> "Text":
    out = caller(mode="frame", depth=depth + 1)
    if isinstance(out, list):
        return out[0]
    return out


VVerboseType: TypeAlias = Literal["vverbose"]
VerboseType: TypeAlias = Literal["verbose"]
DebugType: TypeAlias = Literal["debug"]
InfoType: TypeAlias = Literal["info"]
WarningType: TypeAlias = Literal["warning"]
ErrorType: TypeAlias = Literal["error"]
FatalType: TypeAlias = Literal["fatal"]
VVerboseLevelType: TypeAlias = Literal[1]
VerboseLevelType: TypeAlias = Literal[5]
DebugLevelType: TypeAlias = Literal[10]
InfoLevelType: TypeAlias = Literal[20]
WarningLevelType: TypeAlias = Literal[30]
ErrorLevelType: TypeAlias = Literal[40]
FatalLevelType: TypeAlias = Literal[50]

VVERBOSE_LEVEL: Final = 1
VERBOSE_LEVEL: Final = 5
DEBUG_LEVEL: Final = 10
INFO_LEVEL: Final = 20
WARNING_LEVEL: Final = 30
ERROR_LEVEL: Final = 40
FATAL_LEVEL: Final = 50

VVERBOSE = "VVERBOSE"
VERBOSE = "VERBOSE"
DEBUG = "DEBUG"
INFO = "INFO"
WARNING = "WARNING"
ERROR = "ERROR"
FATAL = "FATAL"

LevelStr = VerboseType | DebugType | InfoType | WarningType | ErrorType | FatalType | VVerboseType
LevelInt = (VerboseLevelType
            | DebugLevelType
            | InfoLevelType
            | WarningLevelType
            | ErrorLevelType
            | FatalLevelType
            | VVerboseLevelType)
LevelType: TypeAlias = (LevelStr | LevelInt
                        | Literal["VVERBOSE", "VERBOSE", "DEBUG", "INFO",
                                  "WARNING", "ERROR", "FATAL"])
LevelIntOrStrT = TypeVar("LevelIntOrStrT", bound=LevelType)
_LevelT = TypeVar("_LevelT", bound=LevelType)


def getlogpath() -> "Path":
    import logging
    import shutil
    from pathlib import Path

    from mbcore.traverse import find_file

    LOGLEVEL = 1

    # Create log path in ~/.mb/logs/
    home_log_dir = Path.home().resolve() / ".mb" / "logs"
    cf = callerfile()
    logging.getLogger("default").log(LOGLEVEL, f"Caller file: {cf}")

    ff, err = find_file("pyproject.toml", cf)
    ff = Path.cwd() if not ff else ff.parent.resolve()

    try:
        log_file = home_log_dir / cf.resolve().relative_to(ff).with_suffix(
            ".log")
    except:
        getLogger("default").log(LOGLEVEL,
                                 f"Failed to resolve {cf} relative to {ff}")
        log_file = home_log_dir / cf.with_suffix(".log")

    try:
        # Ensure log directory exists
        home_log_dir.mkdir(parents=True, exist_ok=True)
        log_file.parent.mkdir(parents=True, exist_ok=True)
        log_file.touch(exist_ok=True)
        return log_file

    except PermissionError:
        import tempfile

        from mbcore.display import safe_print

        safe_print(f"Permission denied: {home_log_dir}, using temp directory")
        return Path(tempfile.gettempdir()) / f"mb-{Path.cwd().name}.log"
    except Exception:
        # If there's an error with the existing log file, backup and recreate
        if log_file.exists():
            backup = log_file.with_suffix(".log.bak")
            shutil.copyfile(log_file, backup)
            log_file.unlink()
        log_file.touch()

        return log_file


LOG_PATH = getlogpath()


def get_workspace_config() -> "LogConfig":
    """Get workspace logging configuration from mb.toml or pyproject.toml."""
    import tomlkit

    from mbcore.traverse import search_parents_for_file

    try:
        # Try mb.toml first
        result = search_parents_for_file("mb.toml")
        if has_error(result):
            raise result.error
        mb_toml = result.result

        if mb_toml and mb_toml.exists():
            return tomlkit.loads(mb_toml.read_text()).get("logs", {})

        # Fallback to pyproject.toml
        pyproject, err = search_parents_for_file("pyproject.toml")
        if pyproject and pyproject.exists():
            with Path(pyproject).open() as f:
                config = tomlkit.load(f)
                return {
                    **LOG_CONFIG,
                    **cast(
                        LogConfig,
                        config.get("tool", {}).get("mb", {}).get("logs", {})),
                }
    except BaseException:
        return LOG_CONFIG

    return LOG_CONFIG


WS_CONFIG = get_workspace_config()


def isverbose() -> bool:
    import sys

    return any(arg in sys.argv
               for arg in ("-V", "--verbose", "--v",
                           "-v")) or WS_CONFIG["level"].lower() == "verbose"


def isvverbose() -> bool:
    import sys

    return (any(
        arg in sys.argv
        for arg in ("-vv", "--vverbose", "--VV",
                    "-VV"))) or WS_CONFIG["level"].lower() == "vverbose"


def isdebug() -> bool:
    import sys

    return (any(arg in sys.argv
                for arg in ("-d", "--debug", "-D", "--DD", "-DD"))
            or WS_CONFIG["level"].lower() == "debug")


def isquiet() -> bool:
    import sys

    return any(arg in sys.argv
               for arg in ("-q", "--quiet",
                           "-Q")) or WS_CONFIG["level"].lower() == "quiet"


def isvquiet() -> bool:
    import sys

    return (any(arg in sys.argv
                for arg in ("-qq", "--vquiet", "-vq", "-VQ", "-QQ"))
            or WS_CONFIG["level"].lower() == "vquiet")


global _last_level
_last_level = None


def getlevel() -> "LevelInt":
    global _last_level

    if _last_level:
        return _last_level
    if isvverbose():
        _last_level = VVERBOSE_LEVEL
    if isverbose():
        _last_level = VERBOSE_LEVEL
    if isdebug():
        _last_level = DEBUG_LEVEL
    if isquiet():
        _last_level = WARNING_LEVEL
    if isvquiet():
        _last_level = ERROR_LEVEL
    if not _last_level:
        _last_level = INFO_LEVEL
    return _last_level


class CustomFormatter(Formatter):

    def handleError(self, ei) -> str:
        return super().formatException(ei)

    def formatStack(self, stack_info) -> str:  # noqa
        if stack_info or WS_CONFIG["show_stack"]:
            return super().formatStack(stack_info)
        return super().formatStack(stack_info)

    def formatMessage(self, record) -> str:
        if WS_CONFIG["exclude_modules"]:
            for module in WS_CONFIG["exclude_modules"]:
                if module in record.module:
                    return ""
        record.funcName = "__main__" if record.funcName == "<module>" else record.funcName
        return super().formatMessage(record)

    def format(self, record) -> str:
        if WS_CONFIG["exclude_modules"]:
            for module in WS_CONFIG["exclude_modules"]:
                if module in record.module:
                    return ""
        record.funcName = "__main__" if record.funcName == "<module>" else record.funcName
        if record.levelno <= FATAL_LEVEL:
            record.levelname = "FATAL"
        if record.levelno <= ERROR_LEVEL:
            record.levelname = "ERROR"
        if record.levelno <= WARNING_LEVEL:
            record.levelname = "WARNING"
        if record.levelno <= INFO_LEVEL:
            record.levelname = "INFO"
        if record.levelno <= DEBUG_LEVEL:
            record.levelname = "DEBUG"
        if record.levelno <= VERBOSE_LEVEL:
            record.levelname = "VERBOSE"
        if record.levelno == VERBOSE_LEVEL + 1:
            record.levelname = "VVERBOSE_ERROR"
        if record.levelno == VVERBOSE_LEVEL + 1:
            record.levelname = "VVERBOSE_ERROR"
        if record.levelno == DEBUG_LEVEL + 1:
            record.levelname = "DEBUG_ERROR"

        try:
            return super().format(record)
        except Exception as e:
            return str(e)


def setup_logging(show_locals: bool | None = None,
                  ignore_third_party: bool | None = None) -> "dict[str, Any]":

    import logging.config
    from os import getenv

    if getenv("LOG_OFF") or WS_CONFIG["log_off"]:
        return {}
    cfg = {
        "version": 1,
        "disable_existing_loggers": False,
        "formatters": {
            "default": {
                "()": CustomFormatter,
                "format": "%(asctime)s - %(module)s - %(message)s",
                "datefmt": "[%X]",
            },
            # "python": {
            #     "format": "%(levelname)s - %(message)s",
            #     "datefmt": "[%X]",
            # },
            "file": {
                "()": CustomFormatter,
                "format":
                "%(asctime)s - %(module)s:%(funcName)s - %(message)s [file://%(pathname)s:%(lineno)d]",
                "datefmt": "[%D %X]",
            },
        },
        "handlers": {
            "rich": {
                "class":
                "mbcore._logging.RichHandler",
                "level":
                getlevel(),
                "show_time":
                True,
                "show_path":
                True,
                "rich_tracebacks":
                True,
                "show_locals":
                show_locals or WS_CONFIG["show_locals"],
                "formatter":
                "default",
                "markup":
                True,
                "ignore_third_party":
                ignore_third_party or WS_CONFIG["ignore_third_party"],
            },
            "file": {
                "class": "logging.FileHandler",
                "filename": getlogpath(),
                "level": VVERBOSE_LEVEL if isvverbose() else VERBOSE_LEVEL,
                "formatter": "file",
            },
        },
        "loggers": {
            "default": {
                "handlers": ["rich"],
                "level": getlevel(),
                "propagate": False,
                "formatter": "default",
            },
            "verbose": {
                "handlers": ["file"],
                "level": VVERBOSE_LEVEL if isvverbose() else VERBOSE_LEVEL,
                "propagate": False,
                "formatter": "file",
            },
        },
    }

    logging.config.dictConfig(cfg)
    return cfg


def setup_traceback(ignore_third_party: bool | None = None,
                    show_locals: bool | None = None,
                    full_trace: bool | None = None):

    from mbcore._traceback import install

    install(
        show_locals=show_locals or WS_CONFIG["show_locals"],
        ignore_third_party=ignore_third_party
        or WS_CONFIG["ignore_third_party"],
    )



LOGGING_CONFIG = {}

if isvverbose() and not getenv("LOG_OFF") and not WS_CONFIG["log_off"]:
    print("Setting up logging for vverbose")
    import logging.config

    SHOW_LOCALS = True

    _last_level = VVERBOSE_LEVEL

    logging.getLogger("default").setLevel(_last_level)

    logging.config.dictConfig(setup_logging())
if isverbose() and not getenv("LOG_OFF") and not WS_CONFIG["log_off"]:
    print("Setting up logging for verbose")
    import logging.config

    _last_level = VERBOSE_LEVEL
    logging.getLogger("default").setLevel(_last_level)
    logging.config.dictConfig(setup_logging())
if isdebug() and not getenv("LOG_OFF") and not WS_CONFIG["log_off"]:
    print("Setting up logging for debug")
    import logging.config

    _last_level = DEBUG_LEVEL
    logging.getLogger("default").setLevel(_last_level)
    logging.config.dictConfig(setup_logging())
if isquiet() and not getenv("LOG_OFF") and not WS_CONFIG["log_off"]:
    print("Setting up logging for quiet")
    import logging.config

    _last_level = WARNING_LEVEL
    logging.getLogger("default").setLevel(_last_level)
    logging.config.dictConfig(setup_logging())
if isvquiet() and not getenv("LOG_OFF") and not WS_CONFIG["log_off"]:
    print("Setting up logging for vquiet")
    import logging.config

    _last_level = ERROR_LEVEL
    logging.getLogger("default").setLevel(_last_level)
    logging.config.dictConfig(setup_logging())

setup_logging()
setup_traceback()


class LevelIntMap(dict):

    @overload
    def __getitem__(
        self,
        level: Literal["vverbose"] | VVerboseLevelType | Literal["VVERBOSE"],
    ) -> VVerboseLevelType:
        ...

    @overload
    def __getitem__(
        self, level: Literal["verbose"] | VerboseLevelType | Literal["VERBOSE"]
    ) -> VerboseLevelType:
        ...

    @overload
    def __getitem__(
        self, level: Literal["debug"] | DebugLevelType | Literal["DEBUG"]
    ) -> DebugLevelType:
        ...

    @overload
    def __getitem__(
        self, level: Literal["info"] | InfoLevelType | Literal["INFO"]
    ) -> InfoLevelType:
        ...

    @overload
    def __getitem__(
        self, level: Literal["warning"] | WarningLevelType | Literal["WARNING"]
    ) -> WarningLevelType:
        ...

    @overload
    def __getitem__(
        self, level: Literal["error"] | ErrorLevelType | Literal["ERROR"]
    ) -> ErrorLevelType:
        ...

    @overload
    def __getitem__(
        self, level: Literal["fatal"] | FatalLevelType | Literal["FATAL"]
    ) -> FatalLevelType:
        ...

    def __getitem__(self, level):
        return super().__getitem__(level)


class LevelStrMap(dict):

    @overload
    def __getitem__(self, level: VerboseLevelType) -> Literal["verbose"]:
        ...

    @overload
    def __getitem__(
            self, level: VerboseLevelType | VerboseType) -> Literal["verbose"]:
        ...

    @overload
    def __getitem__(self,
                    level: DebugLevelType | DebugType) -> Literal["debug"]:
        ...

    @overload
    def __getitem__(self, level: InfoLevelType | InfoType) -> Literal["info"]:
        ...

    @overload
    def __getitem__(
            self, level: WarningLevelType | WarningType) -> Literal["warning"]:
        ...

    @overload
    def __getitem__(self,
                    level: ErrorLevelType | ErrorType) -> Literal["error"]:
        ...

    @overload
    def __getitem__(self,
                    level: FatalLevelType | FatalType) -> Literal["fatal"]:
        ...

    def __getitem__(self, level):
        return super().__getitem__(level)


to_level_int: "LevelIntMap" = LevelIntMap(
    {
        "vverbose": VVERBOSE_LEVEL,
        "verbose": VERBOSE_LEVEL,
        "debug": DEBUG_LEVEL,
        "info": INFO_LEVEL,
        "warning": WARNING_LEVEL,
        "error": ERROR_LEVEL,
        "fatal": FATAL_LEVEL,
        "VVERBOSE": VVERBOSE_LEVEL,
        "VERBOSE": VERBOSE_LEVEL,
        "DEBUG": DEBUG_LEVEL,
        "INFO": INFO_LEVEL,
        "WARNING": WARNING_LEVEL,
        "ERROR": ERROR_LEVEL,
        "FATAL": FATAL_LEVEL,
        VVERBOSE_LEVEL: VVERBOSE_LEVEL,
        VERBOSE_LEVEL: VERBOSE_LEVEL,
        DEBUG_LEVEL: DEBUG_LEVEL,
        INFO_LEVEL: INFO_LEVEL,
        WARNING_LEVEL: WARNING_LEVEL,
        ERROR_LEVEL: ERROR_LEVEL,
        FATAL_LEVEL: FATAL_LEVEL,
    }, )

to_level_str: "LevelStrMap" = LevelStrMap(
    {
        "vverbose": "vverbose",
        "verbose": "verbose",
        "debug": "debug",
        "info": "info",
        "warning": "warning",
        "error": "error",
        "fatal": "fatal",
        "VVERBOSE": "vverbose",
        "VERBOSE": "verbose",
        "DEBUG": "debug",
        "INFO": "info",
        "WARNING": "warning",
        "ERROR": "error",
        "FATAL": "fatal",
        VVERBOSE_LEVEL: "vverbose",
        DEBUG_LEVEL - 5: "verbose",
        DEBUG_LEVEL: "debug",
        INFO_LEVEL: "info",
        WARNING_LEVEL: "warning",
        ERROR_LEVEL: "error",
        FATAL_LEVEL: "fatal",
    }, )


class Log(Generic[LevelIntOrStrT]):
    """Initialize or log a message.

    Usage:
        `from mbcore.log import debug`
        1. Check level: `if debug()`
        2. Set level: `debug.set()`
        3. Log message: `debug("Processing file")`

    Examples:
    ```python
        from mbcore.log import debug, info, warning, error, fatal, log

        >>> debug("Processing file")  # Log a message
        >>> if debug():  # Check if debug level is enabled
        ...     print("Will only print if debug level is enabled")
        >>> debug.set()  # Set logging level to DEBUG
        >>> debug.log("Processing file")  # Log a message
        DEBUG: Processing file
    ```

    """

    @dynamic
    def level(self_or_cls: "Type[Self] | Self") -> "LevelType":  # noqa: N805
        level = self_or_cls._level
        if level is None:
            raise ValueError(f"Invalid log level: {self_or_cls._level}")
        return to_level_int[level]

    _level: "ClassVar[LevelType] | None" = None

    @classmethod
    def set(cls) -> "Type[Self]":
        """Set logging level to the specified level."""
        import logging.config

        global _last_level
        _last_level = to_level_int[cls.level]
        import logging

        logging.getLogger("default").setLevel(to_level_int[cls.level])
        logging.getLogger("verbose").setLevel(to_level_int[cls.level])
        logging.config.dictConfig(setup_logging())

        return cls

    @overload
    @wrapcatafter(pylog, ret=Self)
    @classmethod
    def log(cls, *args, **kwargs):
        ...

    @overload
    @classmethod
    def log(cls) -> bool:
        ...

    @overload
    @wraps(pydebug)
    @classmethod
    def log(cls, *args, **kwargs) -> Type[Self] | bool:
        ...

    @classmethod
    def log(cls, *args, **kwargs) -> Type[Self] | bool:
        """Initialize or log a message.

        Usage:
            `from mbcore.log import debug`
            1. Check level: `if debug()`
            2. Set level: `debug.set()`
            3. Log message: `debug("Processing file")`

        Examples:
        ```python
            from mbcore.log import debug, info, warning, error, fatal, log

            >>> debug("Processing file")  # Log a message
            >>> if debug():  # Check if debug level is enabled
            ...     print("Will only print if debug level is enabled")
            >>> debug.set()  # Set logging level to DEBUG
            >>> debug.log("Processing file")  # Log a message
            DEBUG: Processing file

        ```

        """
        if not args and not kwargs:
            return bool(cls())
        import logging

        arglist = list(args)
        lvl = cast(
            LevelType,
            kwargs.pop(
                "level",
                arglist.pop(0) if arglist and isinstance(arglist[0], int)
                and arglist[0] in to_level_str else None,
            ),
        )
        level = to_level_int[lvl] if lvl else cls.level
        argtup = tuple(args)
        calller = kwargs.pop("caller", None)
        stacklevel = kwargs.pop("stacklevel", 3)
        stack_info = kwargs.pop("stack_info", WS_CONFIG["show_stack"])
        if calller:
            stacklevel += 1
        if isinstance(next(iter(args), None), str):
            msg, *rest = args
            # Only add formatting if we have additional arguments
            if rest and "%" not in msg:
                msg = msg + " " + " ".join(["%s"] * len(rest))
            argtup = (msg, ) + tuple(rest)
        else:
            # Handle non-string first argument

            msg = " ".join(["%s"] * (len(arglist)))
            argtup = (msg, ) + tuple(arglist)
        level = to_level_int[lvl or cls.level]
        logging.getLogger("default").log(level,
                                         *argtup,
                                         **kwargs,
                                         stack_info=stack_info,
                                         stacklevel=stacklevel + 1)
        logging.getLogger("verbose").log(level,
                                         *argtup,
                                         **kwargs,
                                         stack_info=stack_info,
                                         stacklevel=stacklevel + 1)
        return cls

    @classmethod
    def __class_getitem__(cls,
                          level: LevelType | _LevelT) -> "Type[Log[_LevelT]]":
        if isinstance(level, int):
            return type(cls)(cls.__name__, (cls, ), {"level": level})
        if level.lower() not in to_level_int:
            raise ValueError(f"Invalid log level: {level}")
        cls._level = to_level_int[level]

        newcls = type(cls)(cls.__name__, (cls, ), {"level": cls.level})
        return newcls

    def __getitem__(self, level: _LevelT) -> "Log[_LevelT]":
        return self.__class_getitem__(level)()

    def __init__(self, level: "LevelType|None |Any" = None, *args, **kwargs):
        if level is not None and level in to_level_int:
            self._level = to_level_int[level]
        elif level is not None or args or kwargs:
            self.log(self._level, level, *args, **kwargs)

    def __bool__(self=None, *args, **kwargs) -> bool:
        """Check if the log level is enabled."""
        return getLogger("default").getEffectiveLevel() <= to_level_int[
            self.level]

    if TYPE_CHECKING:

        def __new__(cls,
                    level: "LevelType|None| Any" = None,
                    *args,
                    **kwargs) -> "Log[LevelIntOrStrT]":
            cls = super().__new__(cls, *args, **kwargs)
            if cls.level is None:
                return cls
            return cls.__call__(*args, **kwargs)

    if TYPE_CHECKING:
        __call__ = log
    else:

        def __call__(
            self=None,
            *messages: object,
            level: Literal["DEBUG", "INFO", "WARNING", "ERROR", "FATAL"]
            | None = None,
            caller=None,
            stacklevel: int = 2,
            stack_info: bool = WS_CONFIG["show_stack"],
        ) -> "Log[LevelType]":
            """Log messages with proper formatting."""
            if self.level is None:
                return self.__new__(self)

            if messages:
                from pprint import pformat

                from mbcore.display import getspinner

                getspinner().stop()
                messages = map(
                    lambda s: f"{pformat(s)}\n" if not isinstance(s, str) else
                    f"{s}\n".removesuffix("\n\n"),
                    messages,
                )
                # messages = [s.removesuffix("\n") if isinstance(s, str) else s for s in formatted_messages]
                if level is None:
                    level = self.level

                self.log(
                    level=to_level_int[level],
                    *messages,
                    caller=caller,
                    stack_info=stack_info,
                    stacklevel=stacklevel,
                )

            return self


T = TypeVar("T", bound=Mapping[str, Any])


def sanitize_for_toml(obj: "T") -> "T":
    """Recursively convert all dict keys to strings and ensure all values are TOML-compatible."""
    from pathlib import Path

    if isinstance(obj, dict):
        return {str(k): sanitize_for_toml(v) for k, v in obj.items()}
    if isinstance(obj, list):
        return [sanitize_for_toml(v) for v in obj]
    if isinstance(obj, Path):
        try:
            # Try to make path relative to the current working directory
            cwd = Path.cwd()
            if obj.is_absolute():
                try:
                    return str(obj.relative_to(cwd))
                except ValueError:
                    # If path is not relative to cwd, just convert to string
                    return str(obj)
            return str(obj)
        except Exception:
            return str(obj)
    return obj


def save_workspace_config(settings: LogConfig | None = None,
                          workspace: bool = False) -> None:
    """Save workspace logging config to appropriate TOML file.

    Args:
        settings: LogConfig to save.
        current: Whether to save as a current workspace config or project config.

    """
    from pathlib import Path

    import tomlkit

    from mbcore.traverse import find_file, find_mb_toml, find_mb_toml_path

    settings = sanitize_for_toml(settings) if settings else LOG_CONFIG
    make_config = False

    try:
        # Try mb.toml first
        result = find_mb_toml()
        if has_error(result):
            raise result.error
        config = result.result
        toml_path = find_mb_toml_path().result
        if not toml_path:
            raise FileNotFoundError("mb.toml not found")
        if sanitize_for_toml(config.get("logs",
                                        {})) != sanitize_for_toml(settings):
            Log["INFO"]("Log settings updated.")
        config["logs"] = sanitize_for_toml(settings)
        with toml_path.open("w") as f:
            tomlkit.dump(config, f)
        return
    except Exception:
        make_config = True

    try:
        # Fallback to pyproject.toml
        result = find_file("pyproject.toml")
        if has_error(result):
            raise result.error
        pyproject = result.result
        if pyproject and pyproject.exists():
            try:
                with pyproject.open() as f:
                    config = tomlkit.load(f)
            except Exception:
                config = tomlkit.document()

            # Ensure the tool.mb section exists
            config = cast(dict[str, Any], config)
            if "tool" not in config:
                config["tool"] = {}
            if "mb" not in config["tool"]:
                config["tool"]["mb"] = {}

            # Update the logs section
            if sanitize_for_toml(config["tool"]["mb"].get("logs",
                                                          {})) != settings:
                Log["INFO"]("Log settings updated.")
            config["tool"]["mb"]["logs"] = sanitize_for_toml(settings)
            # input(f"config: {config}")
            with pyproject.open("w") as f:
                tomlkit.dump(config, f)

        # Create mb.toml if needed
        if make_config:
            with Path("mb.toml").open("w") as f:
                f.write(tomlkit.dumps({"logs": sanitize_for_toml(settings)}))
    except Exception as e:
        from traceback import print_exc

        print_exc()
        error(f"Failed to save log settings: {e}")


class LogSearch:
    """Smart log search functionality."""

    def __init__(self, log_path: "Path | None " = None):
        self.log_path = log_path or getlogpath()
        self.query_cache = {}

    def search(
        self,
        pattern: str | None = None,
        level: LevelType | None = None,
        start_time: "datetime | None" = None,
        end_time: "datetime | None" = None,
        context_lines: int = 2,
        max_results: int | None = 100,
    ) -> "list[dict[str, Any]]":
        """Smart log search with context and pattern matching."""
        import re
        from collections import deque
        from datetime import datetime

        # Initialize context buffer
        context_buffer = deque(maxlen=context_lines)
        matches = []

        try:
            with self.log_path.open() as f:
                for line in f:
                    # Parse log entry
                    try:
                        entry_time = None
                        log_level = None

                        timestamp_str = re.search(r"\[(\d{2}:\d{2}:\d{2})\]",
                                                  line)
                        if timestamp_str:
                            try:
                                entry_time = datetime.strptime(
                                    timestamp_str.group(1), "%H:%M:%S")

                                # Time filtering
                                if start_time and entry_time < start_time:
                                    continue
                                if end_time and entry_time > end_time:
                                    continue
                            except ValueError:
                                # Skip invalid timestamps
                                pass

                        # Level filtering
                        if level:
                            level_match = re.search(
                                r"(VERBOSE|DEBUG|INFO|WARNING|ERROR|FATAL)",
                                line)
                            if not level_match or level_match.group(
                                    1).lower() != str(level).lower():
                                continue
                            log_level = level_match.group(1)

                        # Pattern matching
                        if pattern and not re.search(pattern, line,
                                                     re.IGNORECASE):
                            context_buffer.append(line)
                            continue

                        # Match found - include context
                        match = {
                            "line": line,
                            "timestamp": entry_time,
                            "level": log_level,
                            "context_before": list(context_buffer),
                            "context_after": [],
                        }
                        matches.append(match)

                        # Reset context buffer
                        context_buffer.clear()

                        if max_results is not None and len(
                                matches) >= max_results:
                            break

                    except Exception as e:
                        error(f"Error parsing log line: {e}")
                        continue

        except Exception as e:
            error(f"Error reading log file: {e}")
            return []

        return matches or [{"line": "No matches found"}]


def search(
    query: str,
    log_path: "Path | None" = None,
    show=True,
    include: "Pattern|str|None" = None,
    exclude: "Pattern|str|None" = None,
) -> "list[dict[str, Any]]":
    import re
    from datetime import datetime

    from mbcore.display import safe_print

    level = re.search(
        r"(VERBOSE|DEBUG|INFO|WARNING|ERROR|FATAL|verbose|debug|info|warning|error|fatal)",
        query)
    start_time = re.search(r"start=(\d{2}:\d{2}:\d{2})", query)
    end_time = re.search(r"end=(\d{2}:\d{2}:\d{2})", query)
    context_lines = re.search(r"ctx=(\d+)", query)
    max_results = re.search(r"n=(\d+)", query)

    if level:
        level = level.group(1)
    if start_time:
        start_time = datetime.strptime(start_time.group(1), "%H:%M:%S")
    if end_time:
        end_time = datetime.strptime(end_time.group(1), "%H:%M:%S")
    if context_lines:
        context_lines = int(context_lines.group(1))
    if max_results:
        max_results = int(max_results.group(1))

    ex_pattern = f"(?!.*{getattr(exclude, 'pattern', exclude)})" if exclude else ""
    inc_pattern = f"(?=.*{getattr(include, 'pattern', include)})" if include else ""

    # Remove any regex-related special terms from the query if needed
    safe_query = query  # You might want to escape regex special chars

    # Combine patterns
    combined_pattern = f"{ex_pattern}{inc_pattern}{safe_query}"

    # Remove any regex-related special terms from the query if needed
    safe_query = query  # You might want to escape regex special chars

    # Combine patterns
    combined_pattern = f"{ex_pattern}{inc_pattern}{safe_query}"
    s = LogSearch(log_path)
    results = s.search(
        pattern=combined_pattern,
        level=to_level_str.get(level),
        start_time=start_time,
        end_time=end_time,
        context_lines=context_lines or 2,
        max_results=max_results,
    )
    if show:
        for match in results:
            for line in match.get("context_before", []):
                safe_print(f"[dim]{line}[/dim]", end="")
            safe_print(f"[bold]{match.get('line', 'No matches.')}[/bold]",
                       end="")
            for line in match.get("context_after", []):
                safe_print(f"[dim]{line}[/dim]", end="")

    return results


vverbose = Log[VVERBOSE_LEVEL]()
verbose: Final = Log[VERBOSE]()
debug: Final = Log[DEBUG]()
info: Final = Log[INFO]()
warning: Final = Log[WARNING]()
error: Final = Log[ERROR]()
fatal: Final = Log[FATAL]()


@wrapafter(Log.log)
def verbose_error(*args, **kwargs):
    return log(VERBOSE_LEVEL + 1, *args, **{
        k: v
        for k, v in kwargs.items() if k not in ("level", )
    })


@wrapafter(Log.log)
def vverbose_error(*args, **kwargs):
    return log(VVERBOSE_LEVEL + 1, *args, **{
        k: v
        for k, v in kwargs.items() if k not in ("level", )
    })


