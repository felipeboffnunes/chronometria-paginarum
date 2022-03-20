from rich.table import Table
from rich.table import Column


def get_table() -> Table:
    # TODO: Add argument for title as book title
    # TODO: Load previous sessions
    return Table(
        Column("Time", justify="left"),
        Column("Page", justify="center"),
        Column("Time Frame", justify="right"),
        title="Chronometria Paginarum",
    )
