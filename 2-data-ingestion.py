"""
Write code to ingest the weather data from the raw text files supplied into your database, using the model you designed. Check for duplicates: if your code is run twice, you should not end up with multiple rows with the same data in your database. Your code should also produce log output indicating start and end times and number of records ingested.
"""

#-----------Imports------------

import sqlite3
import os
import time


#-----------Parameters----------

# Path to the directory containing the weather data files
DATA_DIR = "./data"

# Path to the sqlite database
DATABASE_PATH = 'weather.db'


#--------Data Ingestion--------

# Connect to the database
conn = sqlite3.connect(DATABASE_PATH)

# start time of the data ingestion process
start_time = time.time()

# Iterate through the data files and insert data into the database
for filename in os.listdir(DATA_DIR):
    if filename.startswith("USC"):
        station_id = filename[3:6]
        with open(os.path.join(DATA_DIR, filename), "r") as f:
            for line in f:
                date, max_temp, min_temp, precipitation = line.strip().split("\t")
                # Skip lines with missing data
                if max_temp == "-9999" or min_temp == "-9999" or precipitation == "-9999":
                    continue
                insert_sql = """
                INSERT OR IGNORE INTO weather_data
                (station_id, date, max_temp, min_temp, precipitation)
                VALUES (?, ?, ?, ?, ?)
                """
                conn.execute(insert_sql, (int(station_id), int(date), int(max_temp)/10, int(min_temp)/10, int(precipitation)/10))
conn.commit()

# Print the number of records ingested
select_count_sql = "SELECT COUNT(*) FROM weather_data"
print(f"Number of records ingested: {conn.execute(select_count_sql).fetchone()[0]}")

# Close the connection
conn.close()
end_time = time.time()
print(f'Records were ingested in {end_time - start_time:.2f} seconds')


#------------End------------