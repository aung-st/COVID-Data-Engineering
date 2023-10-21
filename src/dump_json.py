from json import dump
import datetime 
import os
import sys
# sys pathing is used to avoid import errors in unit testing
sys.path.append(os.path.abspath(os.path.dirname(os.path.dirname("src/")))) 
from src.generate_hash import create_hash

def create_filename(path:str) -> tuple:
    
    """
   	Construct a filename in the format YYMMDDHHmm_data_xxx where YY is year, MM is months DD is day, HH is hour, mm is minute and xxx is a 3 character unique hash id.
    In the case of hash id conflicts a new hash will be generated. The filename is then inserted into a specified json_dump directory from the data/ directory.
    
    Parameters:
    path (str): A json_dump directory path 
    
    Returns:
    (filename,hash_id) (tuple): A 2-tuple with the filename and hash_id attached
   	"""
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
  
def dump_json(
	raw_json:dict,
	filename:str
) -> None:
      
	"""
    Save a raw json file as the specified filename in the function arguement. It will save into a directory which is already attached in the filename arguement.
    
    Parameters:
    raw_json (dict): A raw json file fetched from the API call in fetch_data.py
    filename (str): A filename with a path attached generated from the create_filename function
    """
	# dump the data to the file, ensuring non-ASCII characters are preserved
	with open(filename, 'w') as f:
		dump(raw_json, f, ensure_ascii=False)
	f.close()