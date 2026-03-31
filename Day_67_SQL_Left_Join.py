import sqlite3

connection = sqlite3.connect("campus.db")
cursor = connection.cursor()

# Adding a Day-Scholar student who is NOT in the hostels table
cursor.execute("INSERT INTO students VALUES (4, 'Aditi', 8.9, 'CSE-AIML')")

# The LEFT JOIN ensures 'Aditi' shows up even without a room
query = """
SELECT students.name, hostels.room_no
FROM students
LEFT JOIN hostels ON students.id = hostels.student_id
"""

cursor.execute(query)
results = cursor.fetchall()

print("--- Day 67: Full Enrollment Report (Including Day-Scholars) ---")
print(f"{'Name':<10} | {'Room Number':<12}")
print("-" * 25)

for row in results:
    room = row[1] if row[1] else "Day-Scholar"
    print(f"{row[0]:<10} | {room:<12}")

connection.close()
