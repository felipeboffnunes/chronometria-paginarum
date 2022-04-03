
from rich.prompt import Confirm

from src.layout import LayoutHandler
from src.utils import setup_session


def basic_timer_loop() -> None:

    layout = LayoutHandler()
    session = setup_session()

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
