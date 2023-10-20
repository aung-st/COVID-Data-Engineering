from json import dump
import datetime 
import os
import sys
sys.path.append(os.path.abspath(os.path.dirname(os.path.dirname("src/")))) 
from src.generate_hash import create_hash

  
def dump_json(raw_json,path):

  # standardise file names 
  name = "data"  

  # time of json dump
  current_datetime = datetime.datetime.now().strftime("%y%m%d%H%M")
  
  
  hash_id = create_hash(3)[:3]
  
  # construct the filename using the standardized format
  filename = f"{path}{current_datetime}_{name}_{hash_id}.json"
  
  # prevent conflicts in json dumps
  if os.path.exists(filename):
    print("Potential conflict detected")

    # reconstruct the filename with one hash character sliced off 
    hash_id = create_hash(3)[:3]
    filename = f"{path}{hash_id}_{name}_{current_datetime}.json"



  # dump the data to the file, ensuring non-ASCII characters are preserved
  with open(filename, 'w') as f:
    dump(raw_json, f, ensure_ascii=False)
  f.close()

  # to commit: return hash id for use in double check module
  return hash_id
  
 