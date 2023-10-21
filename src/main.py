from double_check_jsons import check_json_is_inserted
from fetch_data import get_data
from process_json import bulk_process_json
from dump_json import dump_json,create_filename
from database import create_main_table

if __name__ == "__main__":

    # pathing arguements 
    db_path = "data/database/data.db"
    json_path = "data/json_dump/"
    
    # get json response from API
    raw_json = get_data()
   
    # create covid data table for database if it doesn't exist already
    create_main_table(db_path)

    # create a filename for the json file and get id for processing
    filename,id = create_filename(json_path)

    # save json file into data/json_dump/
    dump_json(get_data(),filename)
    
    # insert json entries into database
    bulk_process_json(db_path,raw_json,id)

    # make sure that there are no unadded json files in the json_dump directory
    check_json_is_inserted(db_path)
  



