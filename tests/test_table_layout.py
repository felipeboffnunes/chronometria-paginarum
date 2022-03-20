from src.layout import get_table


def test_get_table_layout():
    table = get_table()
    assert len(table.columns) == 3
    assert table.row_count == 0
    assert table.title == "Chronometria Paginarum"
