from src.database import count_rows

def test_all_jsons_inserted():
    path = "data/database/test.db"
    assert count_rows(path) % 238 == 0

