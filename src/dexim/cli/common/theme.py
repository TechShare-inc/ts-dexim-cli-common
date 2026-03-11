"""Rich Theme for DexImitate CLI applications."""

from rich.theme import Theme

DEXIM_THEME = Theme(
    {
        "brand": "bold cyan",
        "brand.dim": "dim cyan",
        "success": "bold green",
        "warning": "bold yellow",
        "error": "bold red",
        "info": "blue",
        "header": "bold white on dark_blue",
        "key": "bold magenta",
        "value": "white",
        "muted": "dim white",
        "table.header": "bold cyan",
        "table.row": "white",
        "category": "bold yellow",
        "command": "bold white",
        "param": "green",
    }
)
