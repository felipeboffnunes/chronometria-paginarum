from rich.prompt import Confirm

from src.layout import LayoutHandler
from src.session import Session


def basic_timer_loop() -> None:
    title = "Test"

    session = Session(title=title)
    main_layout = LayoutHandler()

    action = Confirm()
    while action.ask("", choices=["", "0"], show_choices=False):
        session.update()

        data = session.get_tracker_tail_array()
        main_layout.refresh_output(data, session.overload)

        if session.complete and not session.overload:
            # TODO: autosave
            if action.ask(
                "You have reached your page goal for this session.\n"
                "Do you want to continue on overload?"
            ):
                session.overload = True
                main_layout.add_progress_task()
            else:
                break

        # TODO: Allow extending overload
        if main_layout.progress.finished:
            print("Good bye, Tony Hawk.")
            break

    # TODO: Dialogue dictionary
    if not session.complete:
        # TODO: Save session dialogue
        print("Well, you have tried. Right? Forget it... Go.")
