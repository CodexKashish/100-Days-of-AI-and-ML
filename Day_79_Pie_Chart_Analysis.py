import sqlite3
import matplotlib.pyplot as plt

connection = sqlite3.connect("campus.db")
cursor = connection.cursor()

# 1. Get counts per domain (using the research data from the IEEE days)
query = "SELECT domain, COUNT(*) FROM research_data GROUP BY domain"
cursor.execute(query)
data = cursor.fetchall()

labels = [row[0] for row in data]
sizes = [row[1] for row in data]

# 2. Creating the Pie Chart
plt.figure(figsize=(7, 7))
plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140, colors=['#ff9999','#66b3ff','#99ff99','#ffcc99'])

# 3. Adding a title
plt.title('Research Focus Distribution (IEEE Conference Data)')
plt.axis('equal') 

plt.show()
connection.close()
