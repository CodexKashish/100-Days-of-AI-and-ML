import sqlite3

connection = sqlite3.connect("campus.db")
cursor = connection.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS hostels (student_id INTEGER, room_no TEXT, block TEXT)")

hostel_data = [
    (1, 'A-101', 'Boys'),
    (2, 'B-205', 'Boys'),
    (3, 'C-302', 'Boys')
]
cursor.executemany("INSERT INTO hostels VALUES (?, ?, ?)", hostel_data)

query = """
SELECT students.name, students.branch, hostels.room_no
FROM students
INNER JOIN hostels ON students.id = hostels.student_id
"""

cursor.execute(query)
results = cursor.fetchall()

print("--- Day 66: Unified Student & Hostel Report ---")
print(f"{'Name':<10} | {'Branch':<12} | {'Room':<8}")
print("-" * 35)

for row in results:
    print(f"{row[0]:<10} | {row[1]:<12} | {row[2]:<8}")

connection.close()
