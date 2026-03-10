"""App banner / header for DexImitate CLI applications."""

from rich.panel import Panel
from rich.text import Text

from .console import get_console
from .constants import PRODUCT_SUBTITLE


def print_banner(
    app_name: str = "DexImitate",
    subtitle: str = "",
    version: str = "",
) -> None:
    """Print a styled app banner.

    Args:
        app_name: Application name displayed in the panel title.
        subtitle: Optional subtitle shown in the panel body.
            Defaults to the product subtitle if not provided.
        version: Optional version string appended to the title.

    Example output::

        ╭──────────── DexImitate  v0.1.0 ─────────────╮
        │                                               │
        │  Real-time Bimanual Robot Control Framework   │
        │                                               │
        ╰───────────────────────────────────────────────╯
    """
    console = get_console()
    title = Text(app_name, style="brand")
    if version:
        title.append(f"  v{version}", style="brand.dim")
    body = subtitle or PRODUCT_SUBTITLE
    console.print(
        Panel(
            body,
            title=title,
            border_style="brand",
            padding=(1, 2),
        )
    )
