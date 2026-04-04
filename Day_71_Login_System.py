import sqlite3

connection = sqlite3.connect("system.db")
cursor = connection.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS users (username TEXT, password TEXT)")

# Adding a test user (In a real app, passwords should be encrypted!)
cursor.execute("INSERT INTO users VALUES ('Kashish_AI', 'Pass9.0')")
connection.commit()

print("--- Day 71: Secure Login Terminal ---")
input_user = input("Enter Username: ")
input_pass = input("Enter Password: ")

query = "SELECT * FROM users WHERE username = ? AND password = ?"
cursor.execute(query, (input_user, input_pass))
result = cursor.fetchone()

if result:
    print(f"\nAccess Granted! Welcome back, {result[0]}.")
else:
    print("\nAccess Denied. Invalid credentials.")

connection.close()
