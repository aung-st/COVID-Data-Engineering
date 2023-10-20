from double_check_jsons import check_json_is_inserted
from fetch_data import get_data
from process_json import bulk_process_json
from dump_json import dump_json
from database import create_main_table
import time

if __name__ == "__main__":
    db_path = "data/data.db"
    json_path = "data/json_dump/"
    raw_json = get_data()
    id = dump_json(raw_json,json_path)
    print(id)
    """
    create_main_table(db_path)
    t0 = time.time()
    dump_json(get_data(),json_path)
    
    check_json_is_inserted(db_path)
  

    t1 = time.time()

    print(t1-t0)    """

