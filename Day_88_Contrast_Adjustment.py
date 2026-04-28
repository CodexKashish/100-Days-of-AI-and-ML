import numpy as np
import matplotlib.pyplot as plt

image = np.random.randint(80, 160, (300, 300), dtype=np.uint8)

# Formula: New_Pixel = Gain * (Pixel - 128) + 128
gain = 2.0  
contrast_image = np.clip(128 + gain * (image.astype(np.float32) - 128), 0, 255).astype(np.uint8)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

ax1.imshow(image, cmap='gray', vmin=0, vmax=255)
ax1.set_title("Low Contrast (Original)")
ax1.axis('off')

ax2.imshow(contrast_image, cmap='gray', vmin=0, vmax=255)
ax2.set_title("High Contrast (Stretched)")
ax2.axis('off')

plt.show()
