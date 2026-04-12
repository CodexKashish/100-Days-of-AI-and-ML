import sqlite3

connection = sqlite3.connect("campus.db")
cursor = connection.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS researcher_labs (name TEXT, domain TEXT, project_title TEXT)")

labs_data = [
    ('Kashish', 'AI/ML', 'Neural Nets'),
    ('Arjun', 'AI/ML', 'Computer Vision'),
    ('Priya', 'Cybersecurity', 'Blockchain'),
    ('Aman', 'AI/ML', 'Natural Language'),
    ('Sneha', 'Cybersecurity', 'Ethical Hacking')
]
cursor.executemany("INSERT INTO researcher_labs VALUES (?, ?, ?)", labs_data)

query = """
SELECT a.name, b.name, a.domain
FROM researcher_labs a, researcher_labs b
WHERE a.domain = b.domain 
AND a.name < b.name
"""

cursor.execute(query)
results = cursor.fetchall()

print("--- Day 76: Potential Research Collaborations ---")
print(f"{'Researcher 1':<12} | {'Researcher 2':<12} | {'Shared Domain'}")
print("-" * 45)

for row in results:
    print(f"{row[0]:<12} | {row[1]:<12} | {row[2]}")

connection.close()
