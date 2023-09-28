import sqlite3
from generate_hash import generate_hash

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
                                date_time TEXT
                               );""")
 
def add(
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
):  
    # insertion data
    data = (
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
            )
    # query
    sqlite_insert = """INSERT INTO covid_data(
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
                            date_time)
                           VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)
                           ;"""
    # insert data into the "covid_data" table
    connection = connect()
    with connection:
        connection.execute(
              sqlite_insert,
              data
              )
    connection.close()

create_main_table()