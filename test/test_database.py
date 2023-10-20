from src.database import count_rows

def test_all_jsons_inserted():
    path = "test/test.db"
    assert count_rows(path) % 238 == 0

