# from typing import TYPE_CHECKING

# from mbcore.import_utils import smart_import
# from typing_extensions import Callable, ParamSpec, TypeVar

# if TYPE_CHECKING:
#         import logging

#         import rich_click as click

#         from mbpy.cli import AsyncGroup, get_help_config
# else:

#     click = smart_import('rich_click')
#     logging = smart_import('logging')

#     AsyncGroup = smart_import('mbpy.cli.AsyncGroup')
#     get_help_config = smart_import('mbpy.cli.get_help_config')
# P = ParamSpec("P")
# R = TypeVar("R")


# def wraps(func: Callable[P, R]) -> Callable[...,Callable[P, R]]:
#     """Preserve function metadata when wrapping a function.

#     Args:
#         func (Callable[P, R]): Function to be wrapped.

#     Returns:
#         Callable[...,Callable[P, R]]: Decorator function preserving metadata.

#     Examples:
#         ```python
#         @wraps(func)
#         def my_decorator(func):
#             # Decorator implementation
#             pass
#         ```

#     Notes:
#         - Preserves function metadata when wrapping a function
#         - Useful for decorators that wrap other functions

#     """
#     def decorator(wrapper: Callable[...,Callable[P, R]]) -> Callable[P, R]:
#         wrapper.__name__ = func.__name__
#         wrapper.__module__ = func.__module__
#         wrapper.__doc__ = func.__doc__
#         wrapper.__annotations__ = func.__annotations__
#         return wrapper
#     return decorator


# @click.group(invoke_without_command=True)
# @click.rich_config(help_config=get_help_config())
# @click.help_option("-h", "--help")
# @click.pass_context
# def cli(ctx: click.RichContext,**kwargs):
#     """CLI for mbpy"""
#     if ctx.invoked_subcommand is None:
#         click.echo(ctx.get_help() + "\n" + "Available commands:" + "\n" + "\n".join(
#             f"  {name}" for name in cli.list_commands(ctx)
#         ))


# if __name__ == '__main__':
#         cli()
