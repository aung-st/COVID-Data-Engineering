import os 
from database import extract_id
from process_json import bulk_process_json
import json

def check_json_is_inserted():

    # check if a json file has been inserted into the database
    # if it has not then insert into the database
    
    directory = "data/json_dump/"

    # iterate over files in that directory
    for filename in os.listdir(directory):
        
        # extract filename
        f = os.path.join(directory, filename)

        # extract hash id of file
        id = f[-8:-5]
        id_list = make_id_list()
        if id not in id_list:

            print(f+" not in database")
            print("now adding "+f+" to database")

            # load json
            with open(f) as file:
                raw_json = json.load(file)
                bulk_process_json(raw_json,id)



def make_id_list():

    # get all primary keys from the covid_data table
    ids = extract_id()

    id_list = []

    # extract the hash id from the primary keys and add to an id list
    for id in ids:
        id_list.append(id[0][:3])

    # return a list of hash ids
    return id_list



