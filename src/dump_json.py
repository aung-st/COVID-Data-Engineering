from json import dump
import datetime 
import os
import sys
sys.path.append(os.path.abspath(os.path.dirname(os.path.dirname("src/")))) 
from src.generate_hash import create_hash

def create_filename(path):
    
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

      # reconstruct the filename with a different set of 3 hash characters
      hash_id = create_hash(3)[:3]
      filename = f"{path}{hash_id}_{name}_{current_datetime}.json"
    
    # return filename to be used in dump json
    # return hash id for use in double check module
    return filename,hash_id
  

def dump_json(raw_json,filename):

  # dump the data to the file, ensuring non-ASCII characters are preserved
  with open(filename, 'w') as f:
    dump(raw_json, f, ensure_ascii=False)
  f.close()

 
 