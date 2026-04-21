import numpy as np
import matplotlib.pyplot as plt

# 1. Let's create a "Gradient" image to see the inversion clearly
# A 300x300 image where colors fade from dark to light
image = np.linspace(0, 255, 300*300*3).reshape(300, 300, 3).astype(np.uint8)

# 2. THE TRANSFORMATION: Inverting the colors
# Subtracting every pixel from 255 (The "Negative" operation)
negative_image = 255 - image

# 3. Displaying Side-by-Side
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5))

ax1.imshow(image)
ax1.set_title("Original Gradient")
ax1.axis('off')

ax2.imshow(negative_image)
ax2.set_title("Inverted (Negative)")
ax2.axis('off')

plt.show()
