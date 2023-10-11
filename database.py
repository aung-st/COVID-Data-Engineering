import sqlite3

def connect():
        
        # establish a connection to the SQLite database "data.db"
        connection = sqlite3.connect("data.db")
        return connection

def create_main_table(): 
        
        # create the "covid_data" table in the database
        connection = connect()
        with connection:
            connection.execute("""
                                CREATE TABLE IF NOT EXISTS covid_data(
                                id TEXT PRIMARY KEY,
                                continent TEXT,
                                country TEXT,
                                population INTEGER,
                                new_cases INTEGER,
                                new_deaths INTEGER,
                                active_cases INTEGER,
                                critical_cases INTEGER,
                                recovered INTEGER,
                                recovered_1m_pop INTEGER,
                                recovered_total INTEGER,
                                deaths_1m_pop INTEGER,
                                deaths_total INTEGER,
                                tests_1m_pop INTEGER,
                                tests_total INTEGER,
                                date_time TEXT,
                                time_extracted TEXT
                               );""")
        connection.close()
 
def add(
    id,
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

):  
    
    # insertion data
    data = (
            id,
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
    
    # query
    sqlite_insert = """INSERT INTO covid_data(
                            id,
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
                            time_extracted)
                           VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)
                           ;"""
    
    # insert data into the "covid_data" table
    connection = connect()
    with connection:
        connection.execute(
              sqlite_insert,
              data
              )
    connection.close()

def bulk_add(data):

        sqlite_insert = """INSERT INTO covid_data(
                id,
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
                time_extracted)
                VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)
                ;"""
        
        # insert data into the "covid_data" table
        connection = connect()
        with connection:
                connection.executemany(
                sqlite_insert,
                data
                )
        connection.close()
      



def extract_id():
      
      #query
      sqlite_insert = """SELECT id 
                         FROM
                         covid_data
                        ;"""
      
      connection = connect()
      with connection:
            ids = connection.execute(
                  sqlite_insert,
            )

      return ids


