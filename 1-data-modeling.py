"""
Choose a database to use for this coding exercise (SQLite, Postgres, etc.). Design a data model to represent the weather data records. If you use an ORM, your answer should be in the form of that ORM's data definition format. If you use pure SQL, your answer should be in the form of DDL statements.
"""

#-----------Imports------------

import sqlite3


#-----------Parameters----------

# Path to the sqlite database
DATABASE_PATH = 'weather.db'


#-----------Functions-----------

def execute_sql(conn, query):
    """function that executes the given sql query in provided connection database
    Args:
        conn (sqlite3.Connection): Connection object
        query (str): SQL query to be executed
    Returns:
        None
    Raise:
        NA
    """
    # create a cursor to the connection
    c = conn.cursor()

    # Execute the query
    c.execute(query)

    # Save (commit) the changes
    conn.commit()


#---------Data Modeling---------

# create a new SQLite database and connecting to it
conn = sqlite3.connect(DATABASE_PATH)

# DDL to create the table
query = '''
CREATE TABLE weather_data (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    station_id INTEGER NOT NULL,
    date INTEGER NOT NULL,
    max_temp REAL NOT NULL,
    min_temp REAL NOT NULL,
    precipitation REAL NOT NULL
)
'''

# execute the query
execute_sql(conn, query)

# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
conn.close()


#------------End------------