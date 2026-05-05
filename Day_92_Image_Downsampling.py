import numpy as np
import matplotlib.pyplot as plt

image = np.indices((400, 400)).sum(axis=0) % 2
image = (image * 255).astype(np.uint8)

downsampled = image[::4, ::4]

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5))

ax1.imshow(image, cmap='gray')
ax1.set_title(f"Original: {image.shape}")
ax1.axis('off')

ax2.imshow(downsampled, cmap='gray')
ax2.set_title(f"Downsampled: {downsampled.shape}")
ax2.axis('off')

plt.show()
