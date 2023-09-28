import sqlite3
from generate_hash import generate_hash

def connect():
        # establish a connection to the SQLite database "data.db"
        connection = sqlite3.connect("data.db")
        return connection

def create_key():
       # generate a 3-character hash key
       return generate_hash(4)[:3]

def create_main_table(): 
        # create the "covid_data" table in the database
        connection = connect()
        with connection:
            connection.execute("""
                               CREATE TABLE IF NOT EXISTS covid_data(
                               id TEXT PRIMARY KEY, 
                               continent TEXT,  
                               country TEXT, 
                               day TEXT, 
                               time TEXT,
                               population INTEGER,
                               cases_new INTEGER,
                               cases_active INTEGER,
                               deaths_new INTEGER,
                               deaths_active INTEGER,
                               tests_new INTEGER,
                               tests_active INTEGER
                               );""")
