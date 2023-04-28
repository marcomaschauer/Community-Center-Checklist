# Import required libraries
import sqlite3
import pandas as pd
  
# Connect to SQLite database
conn = sqlite3.connect(r'C:/Users/marco.maschauer/Documents/GitHub/Community Center Checklist/data/community_center_data.db')
  
# Load CSV data into Pandas DataFrame
stud_data = pd.read_csv('C:/Users/marco.maschauer/Documents/GitHub/Community Center Checklist/data/data.csv')
# Write the data to a sqlite table
stud_data.to_sql('community_center', conn, if_exists='replace', index=False)
  
# Create a cursor object
cur = conn.cursor()
# Fetch and display result
for row in cur.execute('SELECT * FROM community_center'):
    print(row)
# Close connection to SQLite database
conn.close()