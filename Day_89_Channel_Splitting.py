import numpy as np
import matplotlib.pyplot as plt

image = np.zeros((300, 300, 3), dtype=np.uint8)
image[:150, :150] = [255, 0, 0]   # Red block
image[:150, 150:] = [0, 255, 0]   # Green block
image[150:, :150] = [0, 0, 255]   # Blue block
image[150:, 150:] = [255, 255, 0] # Yellow (Red + Green)

red_channel = image[:, :, 0]
green_channel = image[:, :, 1]
blue_channel = image[:, :, 2]

fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(10, 10))

ax1.imshow(image)
ax1.set_title("Original RGB")

ax2.imshow(red_channel, cmap='Reds')
ax2.set_title("Red Channel Intensity")

ax3.imshow(green_channel, cmap='Greens')
ax3.set_title("Green Channel Intensity")

ax4.imshow(blue_channel, cmap='Blues')
ax4.set_title("Blue Channel Intensity")

for ax in [ax1, ax2, ax3, ax4]:
    ax.axis('off')

plt.show()
