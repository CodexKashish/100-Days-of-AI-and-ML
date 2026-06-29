import numpy as np
import matplotlib.pyplot as plt

# 1. Create a slightly blurry base image (a soft square)
base_image = np.full((300, 300), 100, dtype=np.uint8)
base_image[100:200, 100:200] = 180

# Apply a quick blur to make it soft before sharpening
padded_blur = np.pad(base_image, 1, mode='edge')
for y in range(300):
    for x in range(300):
        base_image[y, x] = np.mean(padded_blur[y:y+3, x:x+3])

# 2. THE TRANSFORMATION: High-Pass Sharpening Kernel
kernel = np.array([[ 0, -1,  0],
                   [-1,  5, -1],
                   [ 0, -1,  0]], dtype=np.float32)

padded = np.pad(base_image, 1, mode='edge')
sharpened_image = np.zeros_like(base_image)

for y in range(300):
    for x in range(300):
        neighborhood = padded[y:y+3, x:x+3]
        sharpened_image[y, x] = np.clip(np.sum(neighborhood * kernel), 0, 255)

# 3. Plot the results
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5))
ax1.imshow(base_image, cmap='gray', vmin=0, vmax=255)
ax1.set_title("Soft/Blurry Input")
ax2.imshow(sharpened_image, cmap='gray', vmin=0, vmax=255)
ax2.set_title("Crisp Sharpened Output")
for ax in [ax1, ax2]: ax.axis('off')
plt.show()
