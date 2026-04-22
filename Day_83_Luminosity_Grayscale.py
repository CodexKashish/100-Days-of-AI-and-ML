import numpy as np
import matplotlib.pyplot as plt

# 1. Create a colorful synthetic image
image = np.zeros((300, 300, 3), dtype=np.uint8)
image[:, 0:100] = [255, 0, 0]    # Red Section
image[:, 100:200] = [0, 255, 0]  # Green Section
image[:, 200:300] = [0, 0, 255]  # Blue Section

# 2. THE TRANSFORMATION: Weighted Average (Luminosity Method)
# We multiply each channel by its scientific weight
weights = [0.299, 0.587, 0.114]
grayscale_image = np.dot(image[...,:3], weights)

# 3. Display the result
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5))

ax1.imshow(image)
ax1.set_title("Original RGB")
ax1.axis('off')

ax2.imshow(grayscale_image, cmap='gray')
ax2.set_title("Scientific Grayscale")
ax2.axis('off')

plt.show()
