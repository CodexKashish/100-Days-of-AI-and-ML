import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)
base_image = np.full((300, 300), 128, dtype=np.uint8)
probability_map = np.random.rand(300, 300)
base_image[probability_map < 0.02] = 0    
base_image[probability_map > 0.98] = 255  

padded = np.pad(base_image, 1, mode='edge')
smoothed_image = np.zeros_like(base_image)

for y in range(300):
    for x in range(300):
        neighborhood = padded[y:y+3, x:x+3]
        smoothed_image[y, x] = np.mean(neighborhood)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5))
ax1.imshow(base_image, cmap='gray')
ax1.set_title("Noisy Input")
ax2.imshow(smoothed_image, cmap='gray')
ax2.set_title("Smoothed Output")
for ax in [ax1, ax2]: ax.axis('off')
plt.show()
