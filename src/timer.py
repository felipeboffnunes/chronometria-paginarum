
from rich.prompt import Confirm

from src.layout import LayoutHandler
from src.session import Session


def basic_timer_loop() -> None:

    session = Session()
    layout = LayoutHandler()

    layout.session_started()

    action = Confirm()
    while action.ask("Next page [Enter] / Quit [0]", choices=['', '0'], show_choices=False):
        session.update()

        data = session.get_tracker_tail_array()
        layout.refresh_output(data, session.overload)

        if session.complete and not session.overload:
            session.save()
            if action.ask(
                "You have reached your page goal for this session.\n"
                "Do you want to continue on overload?"
            ):
                session.overload = True
                # TODO - ask initial overload size
                layout.add_progress_task()
            else:
                break

        # TODO: Allow extending overload
        if layout.progress.finished:
            print("Good bye, Tony Hawk.")
            break

    # TODO: Dialogue dictionary
    if not session.complete:
        # TODO: Save session dialogue
        print("Well, you have tried. Right? Forget it... Go.")
