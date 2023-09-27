import requests
import pandas as pd
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
  # dump the data to the file, ensuring non-ASCII characters are preserved
  with open('json_dump/data.txt', 'w') as f:
    dump(get_data(), f, ensure_ascii=False)
  f.close()

def get_dataframe():

  # convert and return the response data into a pandas DataFrame
  data = pd.DataFrame.from_dict(get_data())
  return data


