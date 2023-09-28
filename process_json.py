from fetch_data import get_data
from generate_hash import generate_hash


def load_json():

    # load and return json data
    return get_data()
    
def create_key(
    country,
):
       
    # generate a 3-character hash key
    return generate_hash(4)[:3]+'-'+country

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
    return [
        id,
        continent,
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
        date_time
    ]




if __name__ == "__main__":
    print(extract_row(get_data()))

    

    