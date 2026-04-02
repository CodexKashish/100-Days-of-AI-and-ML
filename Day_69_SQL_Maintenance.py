import sqlite3

connection = sqlite3.connect("campus.db")
cursor = connection.cursor()

cursor.execute("UPDATE students SET gpa = 9.1 WHERE name = 'Shashank'")

cursor.execute("DELETE FROM students WHERE id = 3")

connection.commit()

cursor.execute("SELECT * FROM students")
final_list = cursor.fetchall()

print("--- Day 69: Updated Database State ---")
for student in final_list:
    print(student)

connection.close()
