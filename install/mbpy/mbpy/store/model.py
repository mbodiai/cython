from functools import WRAPPER_ASSIGNMENTS, WRAPPER_UPDATES, update_wrapper
from pathlib import Path

from mbcore.display import safe_print, to_click_options_args
from mbcore.types import wrapafter

try:
    from datamodel_code_generator import generate
    from datamodel_code_generator.__main__ import Config, _get_pyproject_toml_config
except ImportError:
    safe_print(
        "Please install the datamodel-code-generator package to use this module."
    )
    raise

from pydantic.json_schema import JsonSchemaValue
from pydantic_core import Url
from typing_extensions import (
    Any,
    Callable,
    ParamSpec,
    Protocol,
    TypeVar,
    overload,
    runtime_checkable,
    Type,
)

P = ParamSpec("P")
U = TypeVar("U")
T = TypeVar("T")
R = TypeVar("R")


@runtime_checkable
class JsonSchema(Protocol):
    def __getitem__(self, key: str) -> JsonSchemaValue | Any: ...


@overload
def wraps(
    cls: Callable[P, T], returns: Type[R]
) -> Callable[[Callable[P, Any]], Callable[P, R]]: ...
@overload
def wraps(
    cls: Callable[P, T], returns: None = None
) -> Callable[[Callable[P, T]], Callable[P, T]]: ...
def wraps(*_args, **_kwargs) -> Callable[[Callable[P, Any]], Callable[P, Any]]:
    args = list(_args)
    if not args:
        raise ValueError("Expected a type or a callable as an argument.")
    if not callable(args[0]):
        raise ValueError("Expected a callable as an argument.")
    cls = _kwargs.get("cls", args[0])

    def wraps_decorator(func: Callable[P, T]) -> Callable[P, T]:
        return update_wrapper(
            func, cls, assigned=WRAPPER_ASSIGNMENTS, updated=WRAPPER_UPDATES
        )

    return wraps_decorator


@wraps(Config, returns=JsonSchemaValue)
@overload
def generate_models(*args, **kwargs) -> Any: ...
@overload
def generate_models(
    cfg: Config, input: Url | JsonSchema, out: Path, **kwargs
) -> None: ...
def generate_models(*args, **kwargs) -> Any:
    args = list(args)
    p = kwargs.get("toml_project_path")
    c = kwargs.get("config")

    p = args.pop(
        args.index(
            next(
                filter(
                    lambda x: isinstance(x, Path | str) and str(x).endswith(".toml"),
                    args,
                )
            ),
            -1,
        )
    )
    c = args.pop(args.index(next(filter(lambda x: isinstance(x, Config | dict), args))))
    if p:
        config = Config(**_get_pyproject_toml_config(p) or {})
    elif c:
        config = Config(**c)
    else:
        raise ValueError(
            f"Invalid arguments: {args}, {kwargs}. Expected either a path to a pyproject.toml file or a Config instance."
        )

    kwargs.get(
        "out",
        args.pop(
            args.index(next(filter(lambda x: isinstance(x, Path | str), args)), -1)
        ),
    )
    kwargs.get(
        "input",
        args.pop(
            args.index(
                next(filter(lambda x: isinstance(x, Url | JsonSchema), args)), -1
            )
        ),
    )
    generate(*args, **config.model_dump())
    return None


@to_click_options_args("config", "input", "out")
@wrapafter(generate)
def cli(config: Config, input: Url | JsonSchema, out: Path, **kwargs) -> None:
    generate_models(config, input, out, **kwargs)


if __name__ == "__main__":
    generate_models()
