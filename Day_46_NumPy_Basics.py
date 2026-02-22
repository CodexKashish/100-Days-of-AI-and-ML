import numpy as np
# 0 = Black, 255 = White
pixels = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])

print(" Original Pixel Matrix")
print(pixels)

#2 NumPy Broadcasting 
# Instead of a 'for loop', adding 50 to every pixel in one step!
bright_pixels = pixels + 50

print("\n--- Brightened Pixel Matrix (+50 Brightness) ---")
print(bright_pixels)

#3 Basic Stats 
print(f"\nMax Brightness: {np.max(bright_pixels)}")
print(f"Average Light Level: {np.mean(bright_pixels)}")
print(f"Total Light Intensity: {np.sum(bright_pixels)}")
