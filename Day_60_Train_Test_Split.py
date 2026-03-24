import numpy as np

# We're back! Let's build the final gatekeeper of AI: The Train-Test Split.

# 10 students with [Study Hours, Attendance %] and their final [GPA]
data = np.array([
    [2, 85, 7.2], [3, 90, 7.8], [5, 95, 8.5], [1, 70, 6.5], [6, 98, 9.2],
    [4, 88, 8.0], [2.5, 80, 7.4], [5.5, 92, 9.0], [3.5, 85, 7.9], [4.5, 89, 8.3]
])

# 1. Shuffle first so the model doesn't learn any patterns in the order
np.random.shuffle(data)

# 2. Set our split ratio (80% for training, 20% for testing)
split_index = int(0.8 * len(data))

# 3. Slicing the matrix 
train_set = data[:split_index]
test_set = data[split_index:]

print(f" Day 60: Dataset Split Complete ")
print(f"Total Records: {len(data)}")
print(f"Training Samples (The Textbook): {len(train_set)}")
print(f"Testing Samples (The Final Exam): {len(test_set)}")

# Just a quick peek at the test set
print("\nUnseen data for testing:")
print(test_set)
