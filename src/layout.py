from rich.progress import Progress, Task, TaskID
from rich.table import Column
from rich.table import Table


def get_table(title: str = "Chronometria Paginarum") -> Table:
    return Table(
        Column("Time", justify="left"),
        Column("Page", justify="center"),
        Column("Time Frame", justify="right"),
        title=title,
    )


def get_progress(total: int = 100) -> Progress:
    progress = Progress()
    progress.add_task("", total=total)
    return progress


def update_progress(progress: Progress) -> None:
    progress.update(TaskID(0), advance=1)
