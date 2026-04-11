import sqlite3

connection = sqlite3.connect("campus.db")
cursor = connection.cursor()

query = """
SELECT project_id, score,
CASE 
    when score >= 90 THEN 'Elite Research'
    when score >= 75 THEN 'High Impact'
    ELSE 'Developing'
END AS impact_status
FROM research_data
ORDER BY score DESC
"""

cursor.execute(query)
results = cursor.fetchall()

print("--- Day 75: Research Impact Analysis ---")
print(f"{'Project ID':<15} | {'Score':<6} | {'Status':<15}")
print("-" * 45)

for row in results:
    print(f"{row[0]:<15} | {row[1]:<6} | {row[2]:<15}")

connection.close()
