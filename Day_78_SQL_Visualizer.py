import sqlite3
import matplotlib.pyplot as plt

connection = sqlite3.connect("campus.db")
cursor = connection.cursor()

# 1. Fetching the data
cursor.execute("SELECT name, gpa FROM students ORDER BY gpa ASC")
data = cursor.fetchall()

names = [row[0] for row in data]
gpas = [row[1] for row in data]

# 2. Creating the Visualization
plt.figure(figsize=(8, 5))
plt.bar(names, gpas, color='skyblue')

# 3. Customizing the chart
plt.xlabel('Student Name')
plt.ylabel('GPA Score')
plt.title('Campus Academic Performance Overview')
plt.ylim(0, 10) 
plt.grid(axis='y', linestyle='--', alpha=0.7)

plt.show()

connection.close()
