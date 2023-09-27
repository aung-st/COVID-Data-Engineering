from fetch_data import get_data
from json import dump
import datetime 
import hashlib

def dump_json():

  #standardise file names 
  name = "data"  
  current_datetime = datetime.datetime.now().strftime("%y%m%d%H%M")
  
  # generate a hash object for the name variable
  hash_object = hashlib.sha1(name.encode("UTF-8")).hexdigest()
  # get the hexadecimal representation of the hash and take the first 3 characters
  hash_id = hash_object[:3]

  # construct the filename using the standardized format
  filename = f"json_dump/{hash_id}_{name}_{current_datetime}.json"
  
  # dump the data to the file, ensuring non-ASCII characters are preserved
  with open(filename, 'w') as f:
    dump(get_data(), f, ensure_ascii=False)
  f.close()

if __name__ == "__main__":
    dump_json()
    