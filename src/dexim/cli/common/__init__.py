"""dexim-cli-common — Shared Rich UI/UX library for DexImitate CLI applications.

Public API
----------
- :data:`DEXIM_THEME` — Rich :class:`~rich.theme.Theme` with DexImitate brand styles.
- :func:`get_console` — Singleton :class:`~rich.console.Console` factory.
- :func:`print_banner` — Render the DexImitate app banner.
- :func:`make_table` — Build a uniformly styled :class:`~rich.table.Table`.
- :func:`status_badge` — Rich-markup ONLINE / OFFLINE badge string.
- :func:`setup_error_handling` — Install Rich traceback handler.
- :func:`handle_cli_error` — Decorator for Click commands; catches and renders errors.
"""

from .banner import print_banner
from .console import get_console
from .error_handler import handle_cli_error, setup_error_handling
from .formatting import make_table, status_badge
from .logging import configure_logging
from .theme import DEXIM_THEME

__all__ = [
    "DEXIM_THEME",
    "configure_logging",
    "get_console",
    "handle_cli_error",
    "make_table",
    "print_banner",
    "setup_error_handling",
    "status_badge",
]
