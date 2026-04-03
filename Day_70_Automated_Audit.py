import sqlite3

connection = sqlite3.connect("campus.db")
cursor = connection.cursor()

cursor.execute("ALTER TABLE students ADD COLUMN attendance INTEGER DEFAULT 100")
cursor.execute("UPDATE students SET attendance = 65 WHERE name = 'Rahul'")
cursor.execute("UPDATE students SET attendance = 95 WHERE name = 'Kashish'")

cursor.execute("SELECT name, attendance FROM students WHERE attendance < 75")
shortage_list = cursor.fetchall()

print("--- Day 70: Attendance Shortage Report ---")
print(f"{'Student':<10} | {'Attendance':<12} | {'Fine (INR)':<10}")
print("-" * 40)

for student in shortage_list:
    name, attendance = student
    fine = (75 - attendance) * 100  # ₹100 for every 1% below 75
    print(f"{name:<10} | {attendance:<12}% | ₹{fine:<10}")

connection.close()
