import sqlite3

connection = sqlite3.connect("campus.db")
cursor = connection.cursor()

cursor.execute("SELECT COUNT(*) FROM students")
total_students = cursor.fetchone()[0]

cursor.execute("SELECT AVG(gpa) FROM students")
avg_gpa = cursor.fetchone()[0]

cursor.execute("SELECT MAX(gpa), MIN(gpa) FROM students")
high_low = cursor.fetchone()

print("--- Day 63: Campus Data Insights ---")
print(f"Total Student Strength: {total_students}")
print(f"Batch Average GPA:      {avg_gpa:.2f}")
print(f"Highest GPA:           {high_low[0]}")
print(f"Lowest GPA:            {high_low[1]}")

connection.close()
