import numpy as np
import matplotlib.pyplot as plt

# 1. Create a blank 300x300 RGB image (3 layers: R, G, B)
# All zeros means a pure black canvas
image = np.zeros((300, 300, 3), dtype=np.uint8)

# 2. Manipulate pixels using Slicing
# Let's make a Red square in the top-left
image[0:100, 0:100] = [255, 0, 0]

# Let's make a Green stripe in the middle
image[100:200, :] = [0, 255, 0]

# Let's make a Blue square in the bottom-right
image[200:300, 200:300] = [0, 0, 255]

# Display "NumPy Art"
plt.imshow(image)
plt.title("Day 81: Image as a NumPy Array")
plt.axis('off') # Hide the X and Y coordinates
plt.show()
