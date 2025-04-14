from mbcore.collect import project
import rich_click as click
from typing_extensions import overload
from mbcore.import_utils import smart_import

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing_extensions import (
        Callable,
        overload,
        ParamSpec,
        TypeVar,
        Any,
        Protocol,
        Concatenate,
        Literal,
        Iterable,
        Coroutine,
        Generic,
        Mapping,
    )
    from inspect import Parameter
    from typing_extensions import TypedDict, NotRequired
    from mbcore.types import T, U
else:

    class Callable:
        @classmethod
        def __class_getitem__(cls, *args: "Any", **kwargs: "Any") -> "Any":
            return cls

        @classmethod
        def __call__(cls, *args: "Any", **kwargs: "Any") -> "Any":
            return args[0] if args else object

        def __new__(cls, *args: "Any", **kwargs: "Any") -> "Any":
            return cls

    ParamSpec = TypeVar = Protocol = Concatenate = Literal = Parameter = Any = Callable
    NotRequired = TypedDict = Iterable = Coroutine = Generic = Mapping = Callable
    Iterable = Callable
    T = object
    U = object

P = ParamSpec("P")
R = TypeVar("R")


def getdefault(name: str, type_hints: "dict[str, Any]", param: "Parameter") -> Any:
    """Get the default value for a parameter based on its type hint."""
    if not TYPE_CHECKING:
        Parameter = smart_import("inspect.Parameter")
    if param.default != Parameter.empty:
        return param.default
    if type_hints[name] == bool:  # noqa
        return False
    if type_hints[name] is int:
        return 0
    if type_hints[name] is float:
        return 0.0
    if type_hints[name] is str:
        return ""
    if type_hints[name] is list:
        return []
    if type_hints[name] is dict:
        return {}
    if type_hints[name] is set:
        return set()
    if type_hints[name] is tuple:
        return tuple()
    if type_hints[name] is Parameter.empty:
        return None
    return None


def first(iterable: Iterable[T], default: U = None) -> T | U:
    return next(iter(iterable), default)


def rest(iterable: Iterable[T]) -> Iterable[T]:
    first, *rest = iterable
    return rest


def gethelp(func: "Callable[...,Any]", name: str) -> str:
    doc = getattr(func, "__doc__", "") or ""
    if not doc or name not in doc:
        return ""
    out = (
        first(
            name.join((rest(str(doc or "").split(name)) if doc else "")).split("\n"), ""
        )
        + "\n"
        if doc
        else ""
    )
    if ":" in out:
        return ":".join(out.split(":")[1:]).strip()
    return out.strip()


class CallableCommand(click.RichCommand, Generic[P, R]):
    def __call__(self, *args: "P.args", **kwargs: "P.kwargs") -> "R": ...


@overload
def to_click_options_args(
    *arg_names: str,
    command_name: str | None = None,
    defaults: "Mapping[str, Any] |None" = None,
    cls: "type[click.Command] | None" = None,
    **param_settings: Literal["multiple"],
) -> "Callable[[Callable[P,R| Coroutine[Any,Any,R]]],CallableCommand[P,R]]": ...
@overload
def to_click_options_args(
    func: "Callable[Concatenate[Any, P], R| Coroutine[Any,Any,R]]",
) -> "CallableCommand[P,R]": ...
def to_click_options_args(*args, **kwargs) -> Any:
    """A decorator to convert a function's type hints to Click options. All arguments not listed in `arg_names` will be converted to options.

    Args:
        *arg_names: Names of arguments to convert to Click arguments
        ** _kwargs: Additional keyword arguments to pass to Click decorators

    Returns:
        Callable: A decorator that converts a function's type hints to Click options

    Example:
    ```python
    @to_click_options_args("text")
    async def parse(text: str) -> Dict:
        \"\"\"Function to parse text.\"\"\"
    ```
    ```
    $ python script.py --help
    Usage: script.py [OPTIONS] TEXT

    Function to parse text.

    Options:
    -h, --help  Show this message and exit.
    ```
    """  # noqa: D401
    command_name = kwargs.pop("command_name", None)
    defaults = kwargs.pop("defaults", None)
    cls = kwargs.pop("cls", None)
    param_settings: dict[str, Literal["multiple"]] = kwargs.pop("param_settings", {})
    arg_names = kwargs.pop("arg_names", args)

    if len(arg_names) > 0 and callable(arg_names[0]):
        return to_click_options_args()(arg_names[0])
    from inspect import Parameter as Param
    from inspect import signature
    from types import UnionType

    import rich_click as click
    from mbpy.cli import get_help_config
    from typing_extensions import Literal, get_args, get_type_hints

    from mbcore.collect import compose
    from mbcore.recipes import unique_everseen
    from inspect import currentframe

    def decorator(func: "Callable[P, R]") -> "Callable[P, R]":
        sig = signature(func).parameters.copy()

      

   
        try:
            type_hints = get_type_hints(func)
        except Exception as e:
            try:
                caller = currentframe().f_back
                caller_parent = caller.f_back
                caller_parent_parent = caller_parent.f_back
                glbls = {**caller_parent.f_globals, **caller.f_globals, **globals()}
                locls = {**caller_parent.f_locals, **caller.f_locals, **locals()}
                type_hints = get_type_hints(func, globalns=glbls, localns=locls)
            except:
                caller_parent = None
                caller_parent_parent = None
                glbls = {**globals()}
                locls = {**locals()}
                type_hints = get_type_hints(func, globalns=glbls, localns=locls)
                
        for k, t in type_hints.copy().items():
            if "Config" in str(t) or "Kwargs" in str(t):
                type_hints.pop(k)
                v = t.__args__[0] if hasattr(t, "__args__") else t
                if hasattr(v, "__annotations__"):
                    anno = v.__annotations__
                    a = {
                        k: eval(v.__forward_arg__)
                        if hasattr(v, "__forward_arg__")
                        else v
                        for k, v in anno.items()
                    }
                else:
                    a = v
                type_hints.update(a)
                sig.update(
                    {
                        k: Param(k, Param.POSITIONAL_OR_KEYWORD, annotation=v[k])
                        for k in a
                    }
                )
                sig.pop(k)

        if defaults:
            for k, v in defaults.items():
                sig[k] = Param(
                    k,
                    Param.POSITIONAL_OR_KEYWORD,
                    default=v,
                    annotation=sig[k].annotation,
                )

        type_hints = {
            x[0]: getattr(
                getattr(x[1], "__orig_bases__", (None,))[0], "__args__", (None,)
            )[0]
            if isinstance(x[1], UnionType)
            and getattr(x[1], "__origin__", getattr(x[1], "__orig_bases__", (None,))[0])
            == Literal
            else click.Choice(get_args(x[1]))
            if getattr(x[1], "__origin__", getattr(x[1], "__orig_bases__", (None,))[0])
            == Literal
            else x[1]
            for x in type_hints.items()
        }

        keys = list(type_hints.keys())
        th = {}
        for k in keys:
            if isinstance(v := type_hints[k], UnionType) or (
                "Union" in str(v) or "Optional" in str(v) or "Literal" in str(v)
            ):
                if "Literal" in str(v):
                    while getattr(getattr(v, "__args__", [None])[0], "__args__", None):
                        v = v.__args__[0]
                    print(v)
                    th[k] = click.Choice(v.__args__)
                else:
                    th[k] = v.__args__[0]
            else:
                th[k] = type_hints[k]

        if not type_hints and not th:
            from mbcore.log import error

            error(f"Function {func.__name__} has no type hints")
            return func
        type_hints = th

        options = []
        args = []
        allnames = set(sig.keys()) - {"self", "cls", "args", "kwargs"} - set(arg_names)

        short = dict(
            zip(allnames, unique_everseen([a[0] for a in allnames]), strict=False)
        )
        optarg_kwargs = {}
        arg_kwargs = {}
        for name, param in sig.items():
            if name not in type_hints and name not in param_settings:
                continue
            if name in param_settings:
                optkw = {name: {k: True for k in param_settings[name]}}
                options.append(
                    click.option(
                        f"--{name}",
                        cls=click.Option,
                        **project(optkw, name),
                        help=gethelp(func, name),
                    ),
                )
                continue
            if name in {"args", "kwargs"}:
                continue
            if name in {"self", "cls"}:
                continue
            if name in arg_names:
                default = getdefault(name, type_hints, param)

                class ArgKwargs(TypedDict):
                    type: click.ParamType
                    default: Any

                argkwargs: ArgKwargs = {
                    "type": type_hints[name],
                    "default": default,
                }
                arg_kwargs[name] = argkwargs
                args.append(
                    click.argument(
                        name,
                        **argkwargs,
                        required=param.default == Param.empty,
                    ),
                )
                continue
            opt_args = (f"--{name}",)
            if name in short:
                opt_args += (f"-{short[name]}",)

            class OptKwargs(TypedDict):
                type: click.ParamType
                is_flag: bool
                default: NotRequired[Any]
                help: NotRequired[str]
                show_choices: bool
                allow_from_autoenv: bool

            if param.default == Param.empty:
                opt_kwargs: OptKwargs = {
                    "type": type_hints[name],
                    "is_flag": type_hints[name] is bool,
                    "show_choices": True,
                    "allow_from_autoenv": True,
                    "help": gethelp(func, name),
                }
                options.append(
                    click.option(
                        *opt_args,
                        **opt_kwargs,
                    ),
                )
            else:
                opt_kwargs: OptKwargs = {
                    "type": type_hints[name],
                    "is_flag": type_hints[name] is bool,
                    "default": getdefault(name, type_hints, param),
                    "show_choices": True,
                    "allow_from_autoenv": True,
                    "help": gethelp(func, name),
                }
                options.append(
                    click.option(
                        *opt_args,
                        **opt_kwargs,
                    ),
                )
            optarg_kwargs[name] = opt_kwargs

        def escape(s):
            from io import StringIO
            from contextlib import redirect_stdout

            stdout = StringIO()

            with redirect_stdout(stdout):
                click.echo(s)
            s = stdout.getvalue()
            return s.replace("\\", r"\\\\")

        help = escape(func.__doc__.split("\n")[0] if func.__doc__ else "")

        wrapper = compose(
            click.command(name=command_name or func.__name__, help=help, cls=cls),
            click.help_option("-h", "--help"),
            *options,
            *args,
            click.rich_config(help_config=get_help_config()),
        )
        return wrapper(getattr(func, "__func__", func))

    return decorator
