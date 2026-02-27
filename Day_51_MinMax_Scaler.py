import numpy as np

marks_matrix = np.array([
    [85, 9.2], 
    [70, 7.5], 
    [95, 9.8], 
    [60, 6.5]  
])

column_min = marks_matrix.min(axis=0)
column_max = marks_matrix.max(axis=0)

normalized_matrix = (marks_matrix - column_min) / (column_max - column_min)

print("--- Original Data (Attendance vs GPA) ---")
print(marks_matrix)

print("\n--- Normalized Data (Scaled 0 to 1) ---")
print(normalized_matrix)

# Checking the progress: The best student now has a score of 1.0 in both!
print(f"\nTop Performer Scaled Score: {normalized_matrix[2]}")
