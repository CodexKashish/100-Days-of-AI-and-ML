import sqlite3

connection = sqlite3.connect("campus.db")
cursor = connection.cursor()

query = """
SELECT name, gpa 
FROM students 
WHERE gpa > (SELECT AVG(gpa) FROM students)
"""

cursor.execute(query)
results = cursor.fetchall()

print("--- Day 68: Top Performers (Above Average) ---")
print(f"{'Name':<10} | {'GPA':<5}")
print("-" * 20)

for row in results:
    print(f"{row[0]:<10} | {row[1]:.2f}")

connection.close()
