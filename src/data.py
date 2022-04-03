
from pathlib import Path

import pandas as pd
from src.config import PATHS


class DataHandler:

    @staticmethod
    def save_session_data(book_id: int, tracker_data: pd.DataFrame) -> None:
        book_id_str = str(book_id).zfill(4)
        path = Path(PATHS['DATA_DIR']) / f'{book_id_str}.csv'
        tracker_data.to_csv(path, mode='a', header=False)
