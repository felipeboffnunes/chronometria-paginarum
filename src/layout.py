from rich.layout import Layout
from rich.progress import Progress, TaskID
from rich.table import Column
from rich.table import Table

# TODO: Parameter config file
OVERLOAD_TASK_SIZE = 10
TAICO_MAIN = './assets/ascii/taico.txt'


def load_ascii(file_name: str) -> str:
    with open(file_name, "r", encoding='utf-8') as file:
        return file.read()


def setup_layout(progress: Progress, tracker_table: Table) -> Layout:
    layout = Layout()
    layout.split_row(
        Layout(tracker_table, name='tracker', ratio=3),
        Layout(name="main", ratio=6),
    )
    layout['main'].split_column(
        Layout(load_ascii(TAICO_MAIN), name='ascii', ratio=10),
        Layout(progress, ratio=2),
    )

    return layout


def get_table(title: str = "Chronometria Paginarum") -> Table:
    return Table(
        Column("Time", justify="left"),
        Column("Page", justify="center"),
        Column("Time Frame", justify="right"),
        title=title,
    )


def get_progress(total: int = 100) -> Progress:
    progress = Progress()
    progress.add_task("[green]Progress...", total=total)
    return progress


def update_progress(progress: Progress, overload: bool = False) -> None:
    task_id = 1 if overload else 0
    progress.update(TaskID(task_id), advance=1)


def add_task(progress: Progress, task_name: str = "[red]Overload...") -> None:
    progress.add_task(task_name, total=OVERLOAD_TASK_SIZE)
