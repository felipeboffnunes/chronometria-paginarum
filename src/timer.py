from dataclasses import dataclass
from timeit import default_timer

import pandas as pd
from rich.console import Console
from rich.prompt import Confirm

from layout import get_table, get_progress, update_progress


class PageTimer:
    pass


@dataclass
class Tracker:
    start: float
    data: pd.DataFrame

    def __init__(self) -> None:
        self._set_data()
        self.start = default_timer()
        self.current_frame = default_timer()
        self.page = 0

    def _set_data(self) -> None:
        self.data = pd.DataFrame({
            "time": pd.Series(dtype="timedelta64[s]"),
            "page": pd.Series(dtype="int64"),
            "frame": pd.Series(dtype="timedelta64[s]"),
        })

    def update(self) -> None:
        frame = default_timer()

        data_row = pd.DataFrame([{
            "time": frame - self.start,
            "page": self.page,
            "frame": frame - self.current_frame,
        }])
        self.page += 1
        self.current_frame = frame

        self.data = pd.concat([self.data, data_row], ignore_index=True)


# TODO: Load previous sessions
@dataclass
class Session:

    title: str
    book_id: int
    page_goal: int

    track: Tracker
    complete: bool = False

    def __init__(self, title: str, page_goal: int) -> None:
        self.title = title
        self.book_id = get_book_id_from_title(title)
        self.page_goal = page_goal
        self.track = Tracker()


# TODO: BOOK Catalog and insert
def get_book_id_from_title(title: str) -> int:
    return 1


def basic_timer_loop() -> None:
    action = Confirm()
    console = Console()
    session = Session(title="test", page_goal=10)
    print("Timer started")
    progress = get_progress(session.page_goal)
    while action.ask("", choices=["", "0"], show_choices=False):
        session.track.update()
        update_progress(progress)
        table = get_table(session.title)
        # TODO: do this properly
        for idx in range(1, 6):
            try:
                time, page, frame = session.track.data.iloc[-idx]
                table.add_row(f"{time:.2f}", f"{page}", f"{frame:.2f}")
            except IndexError:
                continue
        console.clear()
        console.print(progress)
        console.print(table)


basic_timer_loop()