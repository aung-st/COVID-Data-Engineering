from fetch_data import get_data
from generate_hash import generate_hash
from database import add, add_tracking_data, bulk_add
from dump_json import dump_json
import datetime
import logging
    
def create_key(
    id,
    country,
):
       
    # generate a 3-character hash key + country name seperated by a '-' character
    return id+'-'+country

def extract_row(data):

    # extract all keys from 1 dictionary entry
    continent = data['continent']
    country = data['country']
    population = data['population']
    new_cases = data['cases']['new']
    active_cases = data['cases']['active']
    critical_cases = data['cases']['critical']
    recovered = data['cases']['recovered']
    recovered_1m_pop = data['cases']['1M_pop']
    recovered_total = data['cases']['total']
    new_deaths = data['deaths']['new']
    deaths_1m_pop = data['deaths']['1M_pop']
    deaths_total = data['deaths']['total']
    tests_1m_pop = data['tests']['1M_pop']
    tests_total = data['tests']['total']
    date_time = data['time']
    id = create_key(country)

    # return extracted keys
    return {
        "id":id,
        "continent":continent,
        "country":country,
        "population":population,
        "new_cases":new_cases,
        "new_deaths":new_deaths,
        "active_cases":active_cases,
        "critical_cases":critical_cases,
        "recovered":recovered,
        "recovered_1m_pop":recovered_1m_pop,
        "recovered_total":recovered_total,
        "deaths_1m_pop":deaths_1m_pop,
        "deaths_total":deaths_total,
        "tests_1m_pop":tests_1m_pop,
        "tests_total":tests_total,
        "date_time":date_time
    }

def extract_row_tuple(data,id):

    # extract all keys from 1 dictionary entry
    continent = data['continent']
    country = data['country']
    population = data['population']
    new_cases = data['cases']['new']
    active_cases = data['cases']['active']
    critical_cases = data['cases']['critical']
    recovered = data['cases']['recovered']
    recovered_1m_pop = data['cases']['1M_pop']
    recovered_total = data['cases']['total']
    new_deaths = data['deaths']['new']
    deaths_1m_pop = data['deaths']['1M_pop']
    deaths_total = data['deaths']['total']
    tests_1m_pop = data['tests']['1M_pop']
    tests_total = data['tests']['total']
    date_time = data['time']
    primary_key = create_key(id,country)

    # another column to add into the covid_data table in the database
    # this is the time that a json is extracted and placed into a database 
    time_extracted = datetime.datetime.now().strftime("%y%m%d%H%M")

    # return extracted keys
    return (
        primary_key,
        continent,
        country,
        population,
        new_cases,
        new_deaths,
        active_cases,
        critical_cases,
        recovered,
        recovered_1m_pop,
        recovered_total,
        deaths_1m_pop,
        deaths_total,
        tests_1m_pop,
        tests_total,
        date_time,
        time_extracted
    )

def create_list_of_dicts(raw_json):
   
    list_of_dicts = []

    for dict in raw_json['response']:
      
        list_of_dicts.append(extract_row(dict))
    
    return list_of_dicts

def create_list_of_tuples(raw_json,id):
   
    list_of_tuples = []

    for dict in raw_json['response']:
      
        list_of_tuples.append(extract_row_tuple(dict,id))
    
    
    
    return list_of_tuples


def log_id(id):
   
   # keep track of hash id in case of debugging needs
   logging.basicConfig(format="%(asctime)s - %(message)s",level=logging.INFO)
   logging.info('id: '+id+' inserted into covid_data table on id column')

def process_json(
  raw_json,
  id # extract hash id of file
):
  
  # another column to add into the covid_data table in the database
  # this is the time that a json is extracted and placed into a database 
  time_extracted = datetime.datetime.now().strftime("%y%m%d%H%M")

  id = id  

  for dict in raw_json['response']:
    data = extract_row(dict)

    # add all values of a row into the covid_data table
    add(
        id+"-"+data["country"],
        data["continent"],
        data["country"],
        data["population"],
        data["new_cases"],
        data["new_deaths"],
        data["active_cases"],
        data["critical_cases"],
        data["recovered"],
        data["recovered_1m_pop"],
        data["recovered_total"],
        data["deaths_1m_pop"],
        data["deaths_total"],
        data["tests_1m_pop"],
        data["tests_total"],
        data["date_time"],
        time_extracted
    )
    
    log_id(id+"-"+data["country"])

def bulk_process_json(
  raw_json,
  id # extract hash id of file
):
  
  

    id = id  

    data = create_list_of_tuples(raw_json,id)

    # add all values of a row into the covid_data table
    bulk_add(data)

    for row in data:
        log_id(id+"-"+""+row[2])


def extract_tracking_data(raw_json):
   
   # get filename
   filename = dump_json()

   # get hash id of json
   id = filename[-3:]

   # processed is 1 by default, as sqlite does not have a default boolean datatype
   # we opt to take 1 as True and 0 as False
   processed = 1

   # extract datetime of json
   time_processed = filename[:10]

   # return extracted keys
   return [
      id,
      processed,
      time_processed
   ]

def process_tracking_data(
      raw_json
):
   
   # extract tracking data from filename of json
   data = extract_tracking_data(raw_json)

   # insert into json_log table in database
   add_tracking_data(
      data[0],
      data[1],
      data[2]
   )


    