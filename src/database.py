import sqlite3

def connect(path:str) -> None:
        
        """
        Establish a connection to the database in the specified path.

        Parameters:
        path (str): A path into a database in the data/database/ directory
        """

        connection = sqlite3.connect(path)

        return connection

def create_main_table(path:str) -> None: 
        
        """
        Creates a covid_data table with the schema defined the execution sequence for the specified database path in the argument.

        Parameters:
        path (str): A path into a database in the data/database/ directory
        """

        # create the "covid_data" table in the database
        connection = connect(path)
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

def bulk_add(
    path:str,
    data:dict
) -> None:

        """
        Adds 238 entries from a raw json file into the covid_data table of a database in the data/database/ path.

        Parameters:
        path (str): A path into a database in the data/database/ directory
        data (dict): A raw json file that is fetched from the API call in fetch_data.py
        """

        # sqlite query to be inserted into the execution sequence
        sqlite_insert = """
                INSERT INTO covid_data(
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
        connection = connect(path)
        with connection:
                connection.executemany(
                sqlite_insert,
                data
                )
        connection.close()
      
def extract_id(path: str) -> None:
      
	"""
    Read all primary key rows from the database specified in the path leading to the data/database directory and extract the hash id.
    
    Paramaters:
    path (str): A path into a database in the data/database/ directory
    """
      
	# sqlite query to be inserted into the execution sequence
	sqlite_insert = """
        			SELECT id 
					FROM
					covid_data
					;"""
	
	connection = connect(path)
	with connection:
		ids = connection.execute(
				sqlite_insert,
		)

	return ids

def count_rows(path:str) -> None:
	
	"""
	Count the number of rows that the database specified in the path leading to the data/database directory has.

	Parameters:
	path (str): A path into a database in the data/database/ directory
	"""
		
	# sqlite query to be inserted into the execution sequence
	sqlite_insert = """
					SELECT COUNT(*) 
					FROM
					covid_data
					;"""

	connection = connect(path)
	with connection:
		query = connection.execute(
				sqlite_insert,
		)

	# fetching the 0th index of this tuple gets you the number of rows
	# the other value in the tuple is not useful in this context
	number_of_rows = query.fetchone()[0]

	return number_of_rows


