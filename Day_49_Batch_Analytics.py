import numpy as np

# Hey! Day 50 is finally here. Let's build a real-world batch analyzer.

# Marks for Section A (5 students, 3 subjects: Python, Math, Stats)
section_a = np.array([
    [85, 78, 92],
    [90, 88, 85],
    [70, 65, 75],
    [95, 92, 98],
    [82, 80, 84]
])

# Marks for Section B (3 more students)
section_b = np.array([
    [88, 85, 90],
    [75, 70, 80],
    [99, 96, 95]
])

# STEP 1: Merge the sections into one big batch matrix
# We're using vstack to put one section under the other
whole_batch = np.vstack((section_a, section_b))

# STEP 2: Calculate the performance metrics
# Axis 0 means we're looking down the columns (subject averages)
subject_averages = np.mean(whole_batch, axis=0)

# STEP 3: Identify the Batch Topper
# We sum the marks for each student (across the rows)
total_scores = np.sum(whole_batch, axis=1)
max_score = np.max(total_scores)

# Finding which student index actually got that top score
topper_index = np.argmax(total_scores)

print(f"--- Day 50: Batch Analytics Report ---")
print(f"Total Students Analyzed: {len(whole_batch)}")
print("-" * 35)

# Showing subject-wise averages with a bit of formatting
print(f"Average in Python: {subject_averages[0]:.2f}")
print(f"Average in Math:   {subject_averages[1]:.2f}")
print(f"Average in Stats:  {subject_averages[2]:.2f}")

print("-" * 35)
print(f"Highest Total Score: {max_score}")
print(f"The Batch Topper is Student #{topper_index + 1}!")

# STEP 4: Advanced Filter - Who scored above 90 in Python?
python_stars = whole_batch[whole_batch[:, 0] > 90]
print(f"\nThere are {len(python_stars)} students who scored >90 in Python!")
