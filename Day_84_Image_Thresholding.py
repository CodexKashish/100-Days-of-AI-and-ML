import numpy as np
import matplotlib.pyplot as plt

# 1. Create a "Shadowy" Gradient (Simulating real-world lighting)
image = np.linspace(0, 255, 300*300).reshape(300, 300).astype(np.uint8)

# 2. THE TRANSFORMATION: Thresholding
# Logic: If pixel > 127, it becomes 255 (White), else 0 (Black)
threshold_value = 127
binary_image = np.where(image > threshold_value, 255, 0)

# 3. Display the Results
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5))

ax1.imshow(image, cmap='gray')
ax1.set_title("Original Grayscale")
ax1.axis('off')

ax2.imshow(binary_image, cmap='gray')
ax2.set_title("Binary Thresholding")
ax2.axis('off')

plt.show()
