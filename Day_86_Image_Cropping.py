import numpy as np
import matplotlib.pyplot as plt

image = np.zeros((400, 400), dtype=np.uint8)
for i in range(0, 400, 40):
    image[i:i+20, :] = 150 

image[180:220, 180:220] = 255

cropped_roi = image[150:250, 150:250]

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5))

ax1.imshow(image, cmap='gray')
ax1.set_title("Original Image (Wide View)")
ax1.axis('off')

ax2.imshow(cropped_roi, cmap='gray')
ax2.set_title("Cropped ROI (Zoomed View)")
ax2.axis('off')

plt.show()
