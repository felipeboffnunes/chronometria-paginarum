from pathlib import Path

from rich.console import Console
from rich.prompt import IntPrompt

from src.config import PATHS
from src.session import Session


def setup_session() -> Session:
    from src.config import PARAMS
    console = Console()
    console.clear()
    console.print(load_ascii('arson.txt'))
    PARAMS['PAGE_GOAL'] = IntPrompt.ask("Page goal")
    book_id = IntPrompt.ask("Book id")
    session = Session(book_id)
    console.clear()
    console.print("[green]Session initialized![/green]\nGood luck!\n")
    return session


def load_ascii(ascii_asset: str) -> str:
    path = Path(PATHS['ASCII_DIR']) / ascii_asset
    with open(path, 'r', encoding='utf-8') as file:
        ascii_str = file.read()
    return ascii_str
