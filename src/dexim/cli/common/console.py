"""Singleton Rich Console factory for DexImitate CLI applications."""

from rich.console import Console

from .theme import DEXIM_THEME

_console: Console | None = None


def get_console() -> Console:
    """Return the shared Rich console with DexImitate theme.

    Returns:
        The singleton Console instance configured with DEXIM_THEME.
    """
    global _console
    if _console is None:
        _console = Console(theme=DEXIM_THEME)
    return _console
