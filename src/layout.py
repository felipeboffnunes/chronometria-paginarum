from rich.progress import Progress, TaskID
from rich.table import Column
from rich.table import Table

# TODO: Parameter config file
OVERLOAD_TASK_SIZE = 10


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
    progress.add_task(task_name, total=100)
