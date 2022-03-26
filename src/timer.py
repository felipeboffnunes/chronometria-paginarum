import datetime

from rich.console import Console
from rich.layout import Layout
from rich.progress import Progress
from rich.prompt import Confirm
from rich.table import Table

from src.layout import get_table, get_progress, update_progress, add_task, setup_layout
from src.session import Session


def basic_timer_loop() -> None:
    action = Confirm()
    console = Console()
    session = Session(title="test", page_goal=50)
    progress = get_progress(session.page_goal)
    while action.ask("", choices=["", "0"], show_choices=False):
        session.update()
        refresh_output(console, progress, session)

        if session.complete and not session.overload:
            # TODO: autosave
            if action.ask(
                "You have reached your page goal for this session.\n"
                "Do you want to continue on overload?"
            ):
                session.overload = True
                add_task(progress)
            else:
                break

        # TODO: Allow extending overload
        if progress.finished:
            print("Good bye, Tony Hawk.")
            break

    # TODO: Dialogue dictionary
    if not session.complete:
        # TODO: Save session dialogue
        print("Well, you have tried. Right? Forget it... Go.")


def refresh_console(console: Console, layout: Layout) -> None:
    console.clear()
    console.print(layout)


def refresh_table(session: Session) -> Table:
    table = get_table(session.title)
    for time, page, frame in session.get_tracker_tail_array()[::-1]:
        table.add_row(
            str(datetime.timedelta(seconds=time))[:-4],
            str(page),
            str(datetime.timedelta(seconds=frame))[:-4]
        )
    return table


def refresh_output(console: Console, progress: Progress, session: Session) -> None:
    table = refresh_table(session)
    update_progress(progress, session.overload)
    layout = setup_layout(progress, table)
    refresh_console(console, layout)
