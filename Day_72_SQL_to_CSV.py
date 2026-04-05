import sqlite3
import csv

connection = sqlite3.connect("campus.db")
cursor = connection.cursor()

cursor.execute("SELECT * FROM students")
rows = cursor.fetchall()

column_names = [description[0] for description in cursor.description]

with open("campus_report.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(column_names)
    writer.writerows(rows)

print("--- Day 72: Report Generated ---")
print("File 'campus_report.csv' is ready to be shared!")

connection.close()
