from src.fetch_data import get_data 
import sys
import os
from src.dump_json import dump_json,create_filename


def test_response_data_is_fetched():
    assert isinstance(get_data(),dict) 

def test_raw_json_is_dumped():
    json_path = "data/test_json_dump/"
    raw_json = get_data()

    # dump json file
    filename,id = create_filename(json_path)

    dump_json(raw_json,filename)

    filepath = os.listdir(json_path)

    for f in filepath:
        if id in f:
            file = f


    # check that a file exists with the hash id extracted above
    assert id in file

    # TODO: delete file after test



