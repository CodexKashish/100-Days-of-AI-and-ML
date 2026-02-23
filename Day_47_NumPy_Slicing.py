import numpy as np

# A 4x3 Matrix: 4 Students, 3 Subjects each
# Columns: [Python, Electronics, Math]
marks = np.array([
    [85, 90, 78],  # Student 0
    [92, 88, 95],  # Student 1
    [70, 75, 80],  # Student 2
    [99, 95, 98]   # Student 3
])

print("--- Full Grade Ledger ---")
print(marks)

# 1. Row Slicing: Get all marks for Student 1
student_1_marks = marks[1, :] 
print(f"\nMarks for Student 1: {student_1_marks}")

# 2. Column Slicing: Get all marks for the first subject (Python)
# [All rows, column 0]
python_marks = marks[:, 0]
print(f"All Python Marks: {python_marks}")

# 3. Sub-matrix Slicing: Get a 2x2 corner (Top 2 students, first 2 subjects)
top_performers = marks[0:2, 0:2]
print("\nTop 2 Students (First 2 Subjects):")
print(top_performers)

# 4. Logical Check: Who scored above 90 in Python?
high_achievers = python_marks[python_marks > 90]
print(f"\nScores above 90 in Python: {high_achievers}")
