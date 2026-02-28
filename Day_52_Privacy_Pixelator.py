import numpy as np

high_res_face = np.array([
    [10, 12, 110, 115, 15, 10],
    [15, 18, 120, 125, 18, 15],
    [20, 22, 130, 135, 22, 20],
    [25, 28, 140, 145, 28, 25],
    [30, 32, 150, 155, 32, 30],
    [35, 38, 160, 165, 38, 35]
])

blocks = high_res_face.reshape(3, 2, 3, 2)
anonymized_face = blocks.mean(axis=(1, 3))

print("--- Original High-Res Data ---")
print(high_res_face)

print("\n--- Privacy Masked (Pixelated) Data ---")
print(anonymized_face)

original_size = high_res_face.size
new_size = anonymized_face.size
print(f"\nCompression: Reduced {original_size} data points to {new_size}!")
