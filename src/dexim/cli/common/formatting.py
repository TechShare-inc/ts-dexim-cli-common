"""Tables, panels, and status renderers for DexImitate CLI applications."""

from rich.table import Table


def make_table(
    title: str,
    columns: list[tuple[str, str]],
    rows: list[list[str]],
) -> Table:
    """Create a uniformly styled Rich table.

    Args:
        title: Table title rendered above the table.
        columns: List of ``(column_name, style)`` tuples.
        rows: List of row value lists; each inner list must have the same
            length as ``columns``.

    Returns:
        A configured ``rich.table.Table`` ready to be printed.
    """
    table = Table(
        title=title,
        title_style="table.header",
        border_style="brand.dim",
    )
    for name, style in columns:
        table.add_column(name, style=style)
    for row in rows:
        table.add_row(*row)
    return table


def status_badge(ok: bool) -> str:
    """Return a Rich-markup status badge string.

    Args:
        ok: ``True`` for an ONLINE/OK state, ``False`` for OFFLINE/error.

    Returns:
        A Rich markup string such as ``"[success]● ONLINE[/]"``.
    """
    return "[success]● ONLINE[/]" if ok else "[error]● OFFLINE[/]"
