import sqlite3
import pandas as pd


def connect():
    # create connection.
    return sqlite3.connect('data.db')


def get_dataframe(connection):
    df = pd.read_sql_query("SELECT * FROM covid_data", connection)
    connection.close()
    return df 

if __name__ == "__main__":
    connection = connect()
    df = get_dataframe(connection)

    print(df.head(238))


