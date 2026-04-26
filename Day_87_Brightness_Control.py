import numpy as np
import matplotlib.pyplot as plt

image = np.full((300, 300), 127, dtype=np.uint8)

brighter = np.clip(image.astype(np.int16) + 50, 0, 255).astype(np.uint8)
darker = np.clip(image.astype(np.int16) - 50, 0, 255).astype(np.uint8)

fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(15, 5))

ax1.imshow(image, cmap='gray', vmin=0, vmax=255)
ax1.set_title("Original (127)")
ax1.axis('off')

ax2.imshow(brighter, cmap='gray', vmin=0, vmax=255)
ax2.set_title("Brighter (+50)")
ax2.axis('off')

ax3.imshow(darker, cmap='gray', vmin=0, vmax=255)
ax3.set_title("Darker (-50)")
ax3.axis('off')

plt.show()
