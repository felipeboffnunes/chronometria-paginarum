from dataclasses import dataclass, field

from numpy import ndarray

from src.config import PARAMS
from src.data import DataHandler
from src.tracker import Tracker


@dataclass
class Session:

    book_id: int

    page_goal: int = field(init=False, default=PARAMS['PAGE_GOAL'])
    complete: bool = field(init=False, default=False)
    overload: bool = field(init=False, default=False)

    _tracker: Tracker = field(init=False, default_factory=Tracker, repr=False)

    def __post_init__(self) -> None:
        self._tracker.start()

    def load(self) -> None:
        """
        TODO: Load previous sessions
        Depends on save()
        """

        pass

    def save(self) -> None:
        DataHandler.save_session_data(self.book_id, self._tracker.data)

    def update(self) -> None:
        self._tracker.update()
        if self._tracker.page_count == self.page_goal:
            self.complete = True

    def get_tracker_tail_array(self, rows: int = 25) -> ndarray:
        return self._tracker.data.tail(n=rows).to_numpy()[::-1]



