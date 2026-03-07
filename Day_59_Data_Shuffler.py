import numpy as np

dataset = np.array([
    [2, 7.2],
    [4, 8.1],
    [6, 9.2],
    [3, 7.5],
    [5, 8.8]
])

indices = np.random.permutation(len(dataset))
shuffled_data = dataset[indices]

print("--- Original Order ---")
print(dataset)

print("\n--- Shuffled Order ---")
print(shuffled_data)
