"""
For every year, for every weather station, calculate:

\* Average maximum temperature (in degrees Celsius)

\* Average minimum temperature (in degrees Celsius)

\* Total accumulated precipitation (in centimeters)

Ignore missing data when calculating these statistics.

Design a new data model to store the results. Use NULL for statistics that cannot be calculated.

Your answer should include the new model definition as well as the code used to calculate the new values and store them in the database.
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


#--------Data Analysis----------

# create a new SQLite database and connecting to it
conn = sqlite3.connect(DATABASE_PATH)

# sql query for data analysis
query_create_table = '''
CREATE TABLE weather_data_analysis (
    year INTEGER NOT NULL,
    station_id INTEGER NOT NULL,
    avg_max_temp REAL,
    avg_min_temp REAL,
    total_precipitation REAL,
    PRIMARY KEY (year, station_id)
);
'''

query_insert = '''
INSERT INTO weather_data_analysis
SELECT
    substr(date, 1, 4) AS year,
    station_id,
    AVG(CASE WHEN max_temp != -9999 THEN max_temp/10.0 ELSE NULL END) AS avg_max_temp,
    AVG(CASE WHEN min_temp != -9999 THEN min_temp/10.0 ELSE NULL END) AS avg_min_temp,
    SUM(CASE WHEN precipitation != -9999 THEN precipitation/10.0 ELSE NULL END) AS total_precipitation
FROM weather_data
GROUP BY year, station_id;
'''

# Execute the queries
execute_sql(conn, query_create_table)
execute_sql(conn, query_insert)

# Close the connection
conn.close()


#------------End------------