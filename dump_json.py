from fetch_data import get_data
from json import dump
import datetime 
import os
from generate_hash import generate_hash

def dump_json():

  # standardise file names 
  name = "data"  
  current_datetime = datetime.datetime.now().strftime("%y%m%d%H%M")
  
  
  hash_id = generate_hash(3)[:3]
  
  # construct the filename using the standardized format
  filename = f"json_dump/{current_datetime}_{name}_{hash_id}.json"
  
  # prevent conflicts in json dumps
  if os.path.exists(filename):
    print("Potential conflict detected")

    # reconstruct the filename with one hash character sliced off 
    hash_id = generate_hash()[:3]
    filename = f"json_dump/{hash_id}_{name}_{current_datetime}.json"



  # dump the data to the file, ensuring non-ASCII characters are preserved
  with open(filename, 'w') as f:
    dump(get_data(), f, ensure_ascii=False)
  f.close()

if __name__ == "__main__":
    dump_json()
    