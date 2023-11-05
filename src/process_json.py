from database import bulk_add
import datetime
import logging
    
def create_key(
    id:str,
    country:str,
) -> str:
    
    """
    Generate a 3-character hash key + country name seperated by a '-' character to be used as primary key.

    Parameters:
    id (str): Hash id of json file
    country (str): Country of json row entry

    Returns:
    id+'-'+country (str): A string concatenation to be used as a primary key in a database
    """
    
    return id+'-'+country

def extract_row_tuple(
    data:dict,
    id:str
) -> tuple:

    """
    Extract all keys from a single dictionary entry and return it as a 17-tuple.

    Parameters:
    data (dict): A raw json file
    id (str): Hash id of raw json file in the first argument

    Returns:
    (
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
    ) (tuple): A 17-tuple to be used in bulk_process_json
    """

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

def create_list_of_tuples(
    raw_json:dict,
    id:str
) -> list:
   
    """
    Create a list of tuples to be used in bulk_process_json to avoid type error when using sqlite execute_many.

    Parameters:
    raw_json (dict): A raw json file
    id (str): Hash id of above json file in argument
    """

    list_of_tuples = []

    for dict in raw_json['response']:
        
        list_of_tuples.append(extract_row_tuple(dict,id))

    return list_of_tuples

def log_id(
    id:str,
    index:int
) -> None:
   
   """
   Log each row insertion into database for debugging purposes.

   Parameters:
   id (str): Hash id of raw json file passed into bulk_process_json
   index (int): An index to track how many rows have been inserted (1-indexing for convenience)
   """
   
   # keep track of hash id in case of debugging needs
   logging.basicConfig(format="%(asctime)s - %(message)s",level=logging.INFO)
   logging.info(f'id: {id} inserted into covid_data table on id column |{index}')

def bulk_process_json(
  path:str,
  raw_json:dict,
  id:str
) -> None:
    
    """
    Add 238 rows of json entries into a database in the specified path in data/database directory.

    Parameters:
    path (str): Database path into data/database/
    raw_json (dict): Raw json response fetched from API call
    id (str): Hash id of raw json file
    """
  
    data = create_list_of_tuples(raw_json,id)

    # add all values of a row into the covid_data table
    bulk_add(path,data)

    index = 1
    for row in data:
        log_id(id+"-"+""+row[2],index)
        index+=1 