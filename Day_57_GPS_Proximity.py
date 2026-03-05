import numpy as np

locations = np.array([
    [28.45, 77.50], 
    [28.52, 77.39], 
    [28.61, 77.23], 
    [28.40, 77.10]  
])

my_coords = np.array([28.47, 77.48])

differences = locations - my_coords

distances = np.sqrt(np.sum(differences**2, axis=1))

closest_index = np.argmin(distances)
closest_location = locations[closest_index]

print(f"My Location: {my_coords}")
print(f"Nearest Facility: {closest_location}")
print(f"Distance Units: {distances[closest_index]:.4f}")
