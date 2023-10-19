from src.database import *

def test_all_jsons_inserted():
    path = "test/test.db"
    assert count_rows(path) % 238 == 0

