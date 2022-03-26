from dataclasses import dataclass, field

from numpy import ndarray

from src.tracker import Tracker
from src.utils import get_book_id_from_title


@dataclass
class Session:

    title: str
    page_goal: int

    book_id: int = field(init=False)
    complete: bool = field(init=False, default=False)
    overload: bool = field(init=False, default=False)
    _tracker: Tracker = field(init=False, default_factory=Tracker, repr=False)

    def __post_init__(self) -> None:
        self.book_id = get_book_id_from_title(self.title)
        self._tracker.start()

    def load(self) -> None:
        """"
        TODO: Load previous sessions
        Depends on save()
        """

        pass

    def save(self) -> None:
        """
        TODO: Save sessions
        Overload is stored as surplus (when not in debit).
        It is used to compensate missing/unfinished sessions in Reverse Jenga.
        """

        pass

    def update(self) -> None:
        self._tracker.update()
        if self._tracker.page_count == self.page_goal:
            self.complete = True

    def get_tracker_tail_array(self, rows: int = 5) -> ndarray:
        return self._tracker.data.tail(n=rows).to_numpy()
