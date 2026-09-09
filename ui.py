from rich.console import Console, Group
from rich.panel import Panel
from rich.table import Table
from rich.text import Text
from rich.progress import Progress, BarColumn, TextColumn
from rich.align import Align
from rich.box import ROUNDED, HEAVY, SIMPLE
from rich.columns import Columns
from rich.style import Style

console = Console()

APP_CYAN = "bright_cyan"
APP_BLUE = "dodger_blue1"
APP_GREEN = "bright_green"
APP_YELLOW = "bright_yellow"
APP_MAGENTA = "bright_magenta"
APP_RED = "bright_red"
DIM = "grey70"


def clear():
    console.clear()


def title(text, subtitle=None, color=APP_CYAN):
    body = Text(text, style=f"bold {color}", justify="center")
    if subtitle:
        body.append(f"\n{subtitle}", style=f"{DIM}")
    console.print(Panel(body, border_style=color, box=HEAVY, padding=(1, 2)))


def section(text, color=APP_CYAN):
    console.print(f"\n[bold {color}]◆ {text.upper()}[/bold {color}]")


def menu(options, color=APP_CYAN):
    table = Table(show_header=False, box=None, padding=(0, 1), expand=False)
    table.add_column("Key", style=f"bold {color}", width=4, justify="center")
    table.add_column("Action", style="white")
    for key, label in options.items():
        table.add_row(f"[{key}]", label)
    console.print(Panel(table, border_style=color, box=ROUNDED, padding=(1, 2)))


def stat_card(label, value, detail="", color=APP_CYAN):
    body = Text()
    body.append(f"{value}\n", style=f"bold {color}")
    body.append(label, style="bold white")
    if detail:
        body.append(f"\n{detail}", style=DIM)
    return Panel(Align.center(body), border_style=color, box=ROUNDED, padding=(1, 2), expand=True)


def progress_panel(label, value, total=100, color=APP_CYAN):
    total = max(total, 1)
    pct = max(0, min(100, value / total * 100))
    progress = Progress(
        TextColumn("{task.description}"),
        BarColumn(bar_width=24),
        TextColumn("[bold]{task.percentage:>3.0f}%[/bold]"),
        expand=False,
    )
    progress.add_task(label, total=total, completed=value)
    return Panel(progress, border_style=color, box=ROUNDED, padding=(1, 2))


def footer(message="Enter a number to continue"):
    console.print(f"\n[dim]────────────────────────────────────────────────────────[/dim]")
    console.print(f"[bold {APP_CYAN}]›[/bold {APP_CYAN}] {message}")
