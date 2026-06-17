import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)
base_image = np.full((300, 300), 128, dtype=np.uint8)
probability_map = np.random.rand(300, 300)
base_image[probability_map < 0.02] = 0    
base_image[probability_map > 0.98] = 255  

# A 3x3 Gaussian Kernel matrix with weighted importance
kernel = np.array([[1, 2, 1],
                   [2, 4, 2],
                   [1, 2, 1]], dtype=np.float32) / 16.0

padded = np.pad(base_image, 1, mode='edge')
blurred_image = np.zeros_like(base_image)

for y in range(300):
    for x in range(300):
        neighborhood = padded[y:y+3, x:x+3]
        blurred_image[y, x] = np.sum(neighborhood * kernel)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5))
ax1.imshow(base_image, cmap='gray')
ax1.set_title("Noisy Input")
ax2.imshow(blurred_image, cmap='gray')
ax2.set_title("Gaussian Blur Output")
for ax in [ax1, ax2]: ax.axis('off')
plt.show()
