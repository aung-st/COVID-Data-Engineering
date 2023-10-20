from src.fetch_data import get_data 
from src.dump_json import dump_json
import os

def test_response_data_is_fetched():
    assert isinstance(get_data(),dict) 

def test_raw_json_is_dumped():
    json_path = "test_data/test_json_dump/"
    raw_json = get_data()

    # get hash id
    id = dump_json(raw_json,json_path)

    filename = os.listdir(json_path)
        
    # extract filename
    f = os.path.join(json_path, filename)

    # check that a file exists with the hash id extracted above
    assert id in f
    
    # TODO: delete file after test


