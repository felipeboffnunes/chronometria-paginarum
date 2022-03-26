import datetime
from dataclasses import dataclass, field
from functools import cached_property

from numpy import ndarray
from rich.console import Console
from rich.layout import Layout
from rich.progress import Progress, TaskID
from rich.table import Column, Table

from src.parameters import PARAMS

# TODO: use Path instead of string, save somewhere instead of here
TAICO_MAIN = './assets/ascii/taico.txt'


@dataclass
class LayoutHandler:

    layout: Layout = field(init=False)
    progress: Progress = field(init=False)
    console: Console = field(init=False, default_factory=Console)
    table: Table = field(init=False)

    def __post_init__(self) -> None:
        self.setup_layout()

    def set_table_layout(self) -> None:
        self.table = Table(
            Column("Time", justify="left"),
            Column("Page", justify="center"),
            Column("Time Frame", justify="right")
        )

    def refresh_table(self, tracker_tail_array: ndarray) -> None:
        self.set_table_layout()
        for time, page, frame in tracker_tail_array:
            self.table.add_row(
                str(datetime.timedelta(seconds=time))[:-4],
                str(page),
                str(datetime.timedelta(seconds=frame))[:-4]
            )

    def set_progress_layout(self) -> None:
        self.progress = Progress()
        self.progress.add_task("[green]Progress...", total=PARAMS["PAGE_GOAL"])

    def add_progress_task(self) -> None:
        self.progress.add_task("[red]Overload...", total=PARAMS["OVERLOAD_TASK_SIZE"])

    def update_progress(self, overload: bool = False) -> None:
        self.progress.update(TaskID(1 if overload else 0), advance=1)

    def refresh_output(self, tracker_tail_array: ndarray, overload: bool) -> None:
        self.refresh_table(tracker_tail_array)
        self.update_layout()
        self.update_progress(overload)
        self.refresh_console()

    def setup_layout(self) -> None:
        self.set_progress_layout()
        self.set_table_layout()

        self.layout = Layout()
        self.layout.split_row(
            Layout(self.table, name='tracker', ratio=3),
            Layout(name="main", ratio=6),
        )
        self.layout['main'].split_column(
            Layout(self.ascii_str, name='ascii', ratio=10),
            Layout(self.progress, name='progress', ratio=2),
        )

    def update_layout(self) -> None:
        self.layout['tracker'].update(self.table)

    def refresh_console(self) -> None:
        self.console.clear()
        self.console.print(self.layout)

    @cached_property
    def ascii_str(self) -> str:
        with open(TAICO_MAIN, "r", encoding='utf-8') as file:
            ascii_str = file.read()
        return ascii_str
