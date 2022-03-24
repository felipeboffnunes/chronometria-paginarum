from rich.console import Console
from rich.prompt import Confirm

from src.layout import get_table, get_progress, update_progress
from src.session import Session


def basic_timer_loop() -> None:
    action = Confirm()
    console = Console()
    session = Session(title="test", page_goal=10)
    progress = get_progress(session.page_goal)
    while action.ask("", choices=["", "0"], show_choices=False):
        session.tracker.update()
        update_progress(progress)
        table = get_table(session.title)
        # TODO: do this properly
        for idx in range(1, 6):
            try:
                time, page, frame = session.tracker.data.iloc[-idx]
                table.add_row(f"{time:.2f}", f"{page}", f"{frame:.2f}")
            except IndexError:
                pass
        console.clear()
        console.print(progress)
        console.print(table)
