import sqlite3
import csv

connection = sqlite3.connect("campus.db")
cursor = connection.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS research_data (project_id TEXT, score REAL, domain TEXT)")

with open("research_projects.csv", "r") as file:
    reader = csv.reader(file)
    next(reader) 
    
    cursor.executemany("INSERT INTO research_data VALUES (?, ?, ?)", reader)

connection.commit()

cursor.execute("SELECT COUNT(*) FROM research_data")
print(f"Total Research Records Imported: {cursor.fetchone()[0]}")

connection.close()
