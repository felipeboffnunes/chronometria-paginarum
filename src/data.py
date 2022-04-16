
from pathlib import Path

import pandas as pd
from src.config import PATHS


class DataHandler:

    @staticmethod
    def save_session_data(book_id: int, tracker_data: pd.DataFrame) -> None:
        path = Path(PATHS['DATA_DIR']) / f'{book_id:04d}.csv'
        if path.exists():
            previous_tracker_data = pd.read_csv(path, index_col=0)
            tracker_data = pd.concat([previous_tracker_data, tracker_data], ignore_index=True)
        tracker_data.to_csv(path, float_format='%.3f')
