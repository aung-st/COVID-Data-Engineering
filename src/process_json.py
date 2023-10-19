from database import bulk_add
import datetime
import logging
    
def create_key(
    id,
    country,
):
       
    # generate a 3-character hash key + country name seperated by a '-' character
    return id+'-'+country

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

def create_list_of_tuples(raw_json,id):
   
    list_of_tuples = []

    for dict in raw_json['response']:
      
        list_of_tuples.append(extract_row_tuple(dict,id))
    
    
    
    return list_of_tuples


def log_id(id):
   
   # keep track of hash id in case of debugging needs
   logging.basicConfig(format="%(asctime)s - %(message)s",level=logging.INFO)
   logging.info('id: '+id+' inserted into covid_data table on id column')

def bulk_process_json(
  path,
  raw_json,
  id # extract hash id of file
):
  
    data = create_list_of_tuples(raw_json,id)

    # add all values of a row into the covid_data table
    bulk_add(path,data)

    for row in data:
        log_id(id+"-"+""+row[2])





    