import os 
from database import add,extract_id
from process_json import process_json
def check_json_is_inserted():

    # check if a json file has been inserted into the database
    # if it has not then insert into the database
    
    directory = "json_dump/"

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
            process_json(f)


def make_id_list():
    ids = extract_id()

    id_list = []
    for id in ids:
        id_list.append(id[0][:3])

    return id_list

check_json_is_inserted()


