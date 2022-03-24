import datetime

from rich.console import Console
from rich.prompt import Confirm

from src.layout import get_table, get_progress, update_progress, add_task
from src.session import Session


def basic_timer_loop() -> None:
    action = Confirm()
    console = Console()
    session = Session(title="test", page_goal=10)
    progress = get_progress(session.page_goal)
    overload = False
    while action.ask("", choices=["", "0"], show_choices=False):
        session.tracker.update()
        update_progress(progress, overload)
        # TODO: simplify this
        if progress.finished:
            add_task(progress)
            overload = True
        table = get_table(session.title)
        # TODO: do this properly
        for idx in range(1, 6):
            try:
                time, page, frame = session.tracker.data.iloc[-idx]

                time = str(datetime.timedelta(seconds=time))[:-4]
                page = str(page)
                frame = str(datetime.timedelta(seconds=frame))[:-4]

                table.add_row(time, page, frame)
            except IndexError:
                pass
        console.clear()
        console.print(progress)
        console.print(table)
