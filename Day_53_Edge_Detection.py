import numpy as np

sensor_data = np.array([10, 11, 10, 100, 105, 102, 11, 10, 12])

edges = np.diff(sensor_data)

print("Raw Sensor Data:", sensor_data)
print("Detected Edges: ", edges)

threshold = 50
edge_indices = np.where(np.abs(edges) > threshold)[0]

print(f"\nSignificant Edges found at positions: {edge_indices}")
print(f"Total Objects Detected: {len(edge_indices) // 2}")
