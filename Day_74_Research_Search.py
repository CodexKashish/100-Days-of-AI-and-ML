import sqlite3

connection = sqlite3.connect("campus.db")
cursor = connection.cursor()

# 1. Searching using the % wildcard (matches any characters)
keyword = "%AI%" 
query = "SELECT project_id, domain FROM research_data WHERE domain LIKE ?"

cursor.execute(query, (keyword,))
results = cursor.fetchall()

print("--- Day 74: IEEE Research Search Results ---")
print(f"{'Project ID':<15} | {'Research Domain':<20}")
print("-" * 40)

if results:
    for row in results:
        print(f"{row[0]:<15} | {row[1]:<20}")
else:
    print("No matching research papers found.")

connection.close()
