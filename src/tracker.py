
from dataclasses import dataclass, field
from timeit import default_timer

import pandas as pd


def get_tracker_dataframe() -> pd.DataFrame:
    return pd.DataFrame({
        'page': pd.Series(dtype='int64'),
        'frame': pd.Series(dtype='timedelta64[s]'),
        'time': pd.Series(dtype='timedelta64[s]')
    })


@dataclass
class Tracker:

    first_frame: float = field(init=False)
    current_frame: float = field(init=False)

    page_count: int = 0
    data: pd.DataFrame = field(init=False, default_factory=get_tracker_dataframe, repr=False)

    def start(self) -> None:
        self.first_frame = self.current_frame = default_timer()

    def update(self) -> None:
        frame = default_timer()

        data_row = pd.DataFrame([{
            'page': self.page_count,
            'frame': frame - self.current_frame,
            'time': frame - self.first_frame,
        }])

        self.page_count += 1
        self.current_frame = frame

        self.data = pd.concat([self.data, data_row], ignore_index=True)
