"""Click exception hook and Rich traceback installer for DexImitate CLIs."""

import functools
from collections.abc import Callable
from typing import Any, TypeVar

import click
from rich.traceback import install as install_rich_traceback

from .console import get_console

F = TypeVar("F", bound=Callable[..., Any])


def setup_error_handling() -> None:
    """Install Rich traceback handler for unhandled exceptions.

    Call once at CLI entry point startup (e.g. in ``standalone_app()``).
    """
    install_rich_traceback(show_locals=False, width=120)


def handle_cli_error(func: F) -> F:
    """Decorator that catches exceptions and renders them with Rich.

    Catches ``click.Abort`` and prints a warning, then catches all other
    exceptions, prints a Rich traceback, and exits with code 1.

    Args:
        func: The Click command function to wrap.

    Returns:
        The wrapped function.
    """
    @functools.wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        try:
            return func(*args, **kwargs)
        except click.Abort:
            get_console().print("\n[warning]Aborted.[/]")
            return None
        except Exception as exc:
            get_console().print_exception(show_locals=False)
            raise SystemExit(1) from exc

    return wrapper  # type: ignore[return-value]
