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

def prepare_json(data):

    for i in range(1):

        continent = data['response'][i]['continent']
        country = data['response'][i]['country']
        population = data['response'][i]['population']
        new_cases = data['response'][i]['cases']['new']
        active_cases = data['response'][i]['cases']['active']
        critical_cases = data['response'][i]['cases']['critical']
        recovered = data['response'][i]['cases']['recovered']
        recovered_1m_pop = data['response'][i]['cases']['1M_pop']
        recovered_total = data['response'][i]['cases']['total']
        new_deaths = data['response'][i]['deaths']['new']
        deaths_1m_pop = data['response'][i]['deaths']['1M_pop']
        deaths_total = data['response'][i]['deaths']['total']
        tests_1m_pop = data['response'][i]['tests']['1M_pop']
        tests_total = data['response'][i]['tests']['total']
        day = data['response'][i]['day']
        time = data['response'][i]['time']

        id = create_key(country)
        print(id)




if __name__ == "__main__":
    prepare_json(get_data())
    

    