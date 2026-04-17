import sqlite3
import matplotlib.pyplot as plt

connection = sqlite3.connect("campus.db")
cursor = connection.cursor()

# 1. Fetching Data for the Bar Chart (GPA)
cursor.execute("SELECT name, gpa FROM students ORDER BY gpa DESC")
perf_data = cursor.fetchall()
names = [row[0] for row in perf_data]
gpas = [row[1] for row in perf_data]

# 2. Fetching Data for the Pie Chart (Research Domains)
cursor.execute("SELECT domain, COUNT(*) FROM research_data GROUP BY domain")
domain_data = cursor.fetchall()
labels = [row[0] for row in domain_data]
sizes = [row[1] for row in domain_data]

# 3. Creating the Dashboard (1 Row, 2 Columns)
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

# Left Plot: Bar Chart
ax1.bar(names, gpas, color='teal')
ax1.set_title('Academic Performance')
ax1.set_ylabel('GPA')

# Right Plot: Pie Chart
ax2.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
ax2.set_title('Research Domain Focus')

plt.suptitle('Day 80: Comprehensive Data Dashboard', fontsize=16)
plt.tight_layout(rect=[0, 0.03, 1, 0.95])
plt.show()

connection.close()
