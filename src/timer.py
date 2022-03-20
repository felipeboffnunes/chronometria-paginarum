from timeit import default_timer

from rich.live import Live
from rich.prompt import Confirm

from layout import get_table


def basic_timer_loop() -> None:
    action = Confirm()
    table = get_table()
    start = default_timer()
    current_time_frame = start
    page_idx = 0
    with Live(table):
        while action.ask("Next Page / Quit (0)", choices=["", "0"], show_choices=False):
            new_time_frame = default_timer() - current_time_frame
            table.add_row(f"{(default_timer() - start):.2f}", str(page_idx), f"{new_time_frame:.2f}")
            current_time_frame = default_timer()
            page_idx += 1
    end = default_timer()
    print(f"Time elapsed: {end - start}")

