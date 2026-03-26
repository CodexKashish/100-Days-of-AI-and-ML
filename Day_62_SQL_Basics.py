import sqlite3

connection = sqlite3.connect("campus.db")
cursor = connection.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS students (id INTEGER, name TEXT, gpa REAL, branch TEXT)")

students_list = [
    (1, 'Kashish', 9.0, 'CSE-AIML'),
    (2, 'Shashank', 8.5, 'CSE'),
    (3, 'Rahul', 7.8, 'ECE')
]
cursor.executemany("INSERT INTO students VALUES (?, ?, ?, ?)", students_list)

cursor.execute("SELECT name, gpa FROM students WHERE gpa >= 8.5")
results = cursor.fetchall()

print(" Day 62: SQL Query Results ")
for row in results:
    print(f"Student: {row[0]} | GPA: {row[1]}")

connection.close()
