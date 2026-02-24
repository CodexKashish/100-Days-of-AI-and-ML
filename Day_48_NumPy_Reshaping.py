import numpy as np

# 1. A raw 'stream' of data (12 readings)
raw_readings = np.array([22, 25, 28, 20, 24, 29, 31, 22, 19, 21, 26, 18])
print("--- Raw Sensor Stream (1x12) ---")
print(raw_readings)

# 2. Reshaping: Morphing 12 numbers into a 3x4 Grid
# (3 Days of data, 4 time-slots per day)
weather_grid = raw_readings.reshape(3, 4)
print("\n--- Structured Weather Report (3 Days x 4 Time-slots) ---")
print(weather_grid)

# 3. Transposing: Flipping the Matrix (Rows become Columns)
# Now each row represents a 'Time-slot' across 3 days
flipped_view = weather_grid.T
print("\nFlipped View (Time-slots vs Days)")
print(flipped_view)

# 4. Flattening: Turning it back into a stream
back_to_stream = weather_grid.flatten()
print("\nBack to Flat Stream")
print(back_to_stream)
