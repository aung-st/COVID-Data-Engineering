import database
from double_check_jsons import check_json_is_inserted
from fetch_data import get_data
from process_json import process_json,create_list_of_dicts,create_list_of_tuples,bulk_process_json
from dump_json import dump_json
from database import create_main_table
import time
from multiprocessing import Process

if __name__ == "__main__":
    raw_json = get_data()
    id = dump_json(raw_json)
    #process_json(raw_json,id)
    create_main_table()
    t0 = time.time()
    dump_json(get_data())
    
    #process = Process(target=check_json_is_inserted)
    #process.start()
    #process.join()

    bulk_process_json(raw_json,id)
    t1 = time.time()

    print(t1-t0)    

