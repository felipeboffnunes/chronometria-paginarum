from dataclasses import dataclass
from timeit import default_timer

import pandas as pd


def get_tracker_dataframe() -> pd.DataFrame:
    return pd.DataFrame({
        "time": pd.Series(dtype="timedelta64[s]"),
        "page": pd.Series(dtype="int64"),
        "frame": pd.Series(dtype="timedelta64[s]"),
    })


@dataclass
class Tracker:

    start: float = default_timer()
    current_frame: float = default_timer()

    page: int = 0
    data: pd.DataFrame = get_tracker_dataframe()

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
