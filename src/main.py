from double_check_jsons import check_json_is_inserted
from fetch_data import get_data
from process_json import bulk_process_json
from dump_json import dump_json,create_filename
from database import create_main_table
from os.path import abspath
from os.path import exists
from os import mkdir
from dotenv import load_dotenv

if __name__ == "__main__":
    
    # load .env file in the root 
    load_dotenv()

    # make directories 
    db_directory = abspath("./data/database/")
    json_directory = abspath("./data/json_dump/")

    # pathing arguements 
    db_path = abspath("data/database/data.db")
    json_path = abspath("data/json_dump/")

    # create directories if they do not already exist
    if not exists(db_path):
        mkdir(db_path)
    if not exists(json_path):
        mkdir(json_path)

    # get json response from API
    raw_json = get_data()
   
    # create covid data table for database if it doesn't exist already
    create_main_table(db_path)

    # create a filename for the json file and get id for processing
    filename,id = create_filename()

    # save json file into data/json_dump/
    dump_json(raw_json,filename,json_path)
    
    # insert json entries into database
    bulk_process_json(db_path,raw_json,id)

    # make sure that there are no unadded json files in the json_dump directory
    check_json_is_inserted(db_path)
  



