import sqlite3

connection = sqlite3.connect("campus.db")
cursor = connection.cursor()

# SQL Logic: Group by branch, calculate average GPA, and sort descending
query = """
SELECT branch, COUNT(*), AVG(gpa) 
FROM students 
GROUP BY branch 
ORDER BY AVG(gpa) DESC
"""

cursor.execute(query)
results = cursor.fetchall()

print("--- Day 64: Departmental Performance Report ---")
print(f"{'Branch':<12} | {'Students':<8} | {'Avg GPA':<8}")
print("-" * 35)

for row in results:
    print(f"{row[0]:<12} | {row[1]:<8} | {row[2]:.2f}")

connection.close()
