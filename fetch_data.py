import requests
import pandas as pd
import datetime 
import hashlib
from json import dump
import os

def get_data():

  # get the RapidAPI key from the environment variable
  rapid_api_key = os.getenv("RAPID_API_KEY")

  # set the headers for the API request
  headers = {'X-RapidAPI-Key': rapid_api_key,
             'X-RapidAPI-Host': 'covid-193.p.rapidapi.com'}

  # make the API request
  response = requests.get("https://covid-193.p.rapidapi.com/statistics",headers=headers)
  data = response.json()

  # return response data
  return data['response']

def dump_json():

  #standardise file names 
  name = "data"  
  current_datetime = datetime.datetime.now().strftime("%y%m%d%H%M")
  
  # generate a hash object for the name variable
  hash_object = hashlib.md5(name.encode())
  # get the hexadecimal representation of the hash and take the first 6 characters
  hash_id = hash_object.hexdigest()[:6]

  # construct the filename using the standardized format
  filename = f"json_dump/{name}_{current_datetime}_{hash_id}.json"
  
  # dump the data to the file, ensuring non-ASCII characters are preserved
  with open(filename, 'w') as f:
    dump(get_data(), f, ensure_ascii=False)
  f.close()

   

def get_dataframe():

  # convert and return the response data into a pandas DataFrame
  data = pd.DataFrame.from_dict(get_data())
  return data


