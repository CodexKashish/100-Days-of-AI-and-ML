import numpy as np

database = np.array([10.5, 22.1, 35.8, 48.2, 55.9, 72.3, 89.1, 95.5])
target_value = 50.0

differences = np.abs(database - target_value)
closest_index = np.argmin(differences)
closest_value = database[closest_index]

print(f"Target: {target_value}")
print(f"Closest Match: {closest_value}")
print(f"Found at Index: {closest_index}")
