import sqlite3

connection = sqlite3.connect("campus.db")
cursor = connection.cursor()

query = """
SELECT branch, AVG(gpa) 
FROM students 
GROUP BY branch 
HAVING AVG(gpa) >= 8.0
"""

cursor.execute(query)
results = cursor.fetchall()

print("--- Day 65: Elite Performance Report ---")
print(f"{'Branch':<12} | {'Avg GPA':<8}")
print("-" * 25)

if not results:
    print("No departments met the elite criteria yet.")
else:
    for row in results:
        print(f"{row[0]:<12} | {row[2]:.2f}")

connection.close()
