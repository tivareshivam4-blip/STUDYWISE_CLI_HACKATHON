from rich.prompt import Prompt
from rich.panel import Panel
from rich.table import Table
from rich.columns import Columns
from rich.align import Align
from ui import console, clear, title, menu, footer, stat_card, APP_CYAN, APP_GREEN, APP_YELLOW, APP_MAGENTA, APP_RED
from database.db import init_db, query_one, backup_db
from modules.study import study_menu
from modules.expenses import expense_menu
from modules.flashcards import flashcard_menu
from modules.dashboard import show_dashboard, metrics, productivity_score
from modules.gamification import get_level


def show_home():
    clear()
    m = metrics()
    score = productivity_score(m)
    profile = m["profile"]
    title("⚡ STUDYWISE", "OFFLINE PERSONAL PRODUCTIVITY OS")
    console.print(Columns([
        stat_card("PRODUCTIVITY", f"{score}/100", "Today's score", APP_CYAN),
        stat_card("STUDY", f"{m['study_today']} min", f"{m['pending']} pending tasks", APP_CYAN),
        stat_card("SPENDING", f"₹{m['spent']:.0f}", "This month", APP_GREEN),
        stat_card("STREAK", f"🔥 {profile['streak']}", f"Level {m['level']}", APP_YELLOW),
    ], equal=True, expand=True))

    console.print(Panel(
        "[bold white]Track[/bold white]  your study & spending     "
        "[bold white]Plan[/bold white]  your day     "
        "[bold white]Learn[/bold white]  with spaced repetition     "
        "[bold white]Grow[/bold white]  with XP & streaks",
        border_style=APP_MAGENTA, padding=(1, 2), title="YOUR COMMAND CENTER"))

    menu({
        "1": "📚  Study Planner",
        "2": "💰  Expense Tracker",
        "3": "🧠  Flashcards",
        "4": "📊  Full Dashboard",
        "5": "🏆  Gamification",
        "6": "💾  Database Backup",
        "0": "🚪  Exit",
    })
    footer("Choose a module")


def show_gamification():
    clear()
    row = query_one("SELECT xp, streak, last_active, name FROM profile WHERE id=1")
    level, current, needed = get_level(row["xp"])
    title("🏆 GAMIFICATION", "TURN CONSISTENCY INTO PROGRESS", APP_YELLOW)
    console.print(Columns([
        stat_card("LEVEL", str(level), "Current level", APP_YELLOW),
        stat_card("TOTAL XP", str(row["xp"]), f"{current}/{needed} to next level", APP_CYAN),
        stat_card("STREAK", f"🔥 {row['streak']}", "Consecutive active days", APP_GREEN),
    ], equal=True, expand=True))
    table = Table(title="XP Rewards", header_style="bold yellow")
    table.add_column("Action"); table.add_column("XP", justify="right")
    table.add_row("Complete a study task", "+20")
    table.add_row("Complete a study session", "+20")
    table.add_row("Review a flashcard", "+5")
    table.add_row("Stay within budget", "+10")
    console.print(Panel(table, border_style=APP_YELLOW))
    footer("Press Enter to return")
    Prompt.ask("", default="")


def main():
    init_db()
    while True:
        show_home()
        choice = Prompt.ask("", choices=["1","2","3","4","5","6","0"], default="1", show_default=False)
        if choice == "1": study_menu()
        elif choice == "2": expense_menu()
        elif choice == "3": flashcard_menu()
        elif choice == "4":
            clear(); show_dashboard(); footer("Press Enter to return"); Prompt.ask("", default="")
        elif choice == "5": show_gamification()
        elif choice == "6":
            clear(); title("💾 DATABASE BACKUP", "SAFE OFFLINE SQLITE SNAPSHOT", APP_GREEN)
            path = backup_db()
            console.print(Panel(f"[green]✓ Backup created successfully[/green]\n\n{path}", border_style=APP_GREEN))
            footer("Press Enter to return"); Prompt.ask("", default="")
        else:
            clear()
            console.print(Panel(Align.center("[bold cyan]Thanks for using STUDYWISE![/bold cyan]\n[dim]Your data is stored locally in SQLite.[/dim]"), border_style=APP_CYAN))
            break


if __name__ == "__main__":
    main()
