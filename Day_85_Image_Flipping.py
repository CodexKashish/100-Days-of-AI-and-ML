import numpy as np
import matplotlib.pyplot as plt

# 1. Create a "Directional" image (A gradient that points right)
image = np.linspace(0, 255, 300*300).reshape(300, 300).astype(np.uint8)
# Add a small white square on the top-left to track movement
image[20:80, 20:80] = 255

# 2. THE TRANSFORMATION: Flipping
# [::-1, :] flips rows (Vertical Flip)
# [:, ::-1] flips columns (Horizontal/Mirror Flip)
horizontal_flip = image[:, ::-1]
vertical_flip = image[::-1, :]

# 3. Display the Results
fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(15, 5))

ax1.imshow(image, cmap='gray')
ax1.set_title("Original (Square at Top-Left)")
ax1.axis('off')

ax2.imshow(horizontal_flip, cmap='gray')
ax2.set_title("Horizontal Flip (Mirror)")
ax2.axis('off')

ax3.imshow(vertical_flip, cmap='gray')
ax3.set_title("Vertical Flip (Reflection)")
ax3.axis('off')

plt.show()
