import numpy as np

temp_readings = np.array([24, 25, 26, 200, 25, 24, -99, 26, 25, 27])

mean = np.mean(temp_readings)
std_dev = np.std(temp_readings)

z_scores = (temp_readings - mean) / std_dev

threshold = 2
clean_data = temp_readings[np.abs(z_scores) < threshold]
outliers = temp_readings[np.abs(z_scores) >= threshold]

print("Original Readings:", temp_readings)
print("Cleaned Readings: ", clean_data)
print("Outliers Detected:", outliers)
