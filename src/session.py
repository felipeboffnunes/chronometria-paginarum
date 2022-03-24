from dataclasses import dataclass

from src.tracker import Tracker
from src.utils import get_book_id_from_title


@dataclass
class Session:

    title: str
    page_goal: int

    complete: bool = False

    def __post_init__(self) -> None:
        self.book_id = get_book_id_from_title(self.title)
        self.tracker = Tracker()

    def load(self) -> None:
        """"
        TODO: Load previous sessions
        """
        pass
