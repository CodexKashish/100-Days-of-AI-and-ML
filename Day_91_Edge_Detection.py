import numpy as np
import matplotlib.pyplot as plt

y, x = np.ogrid[-100:100, -100:100]
mask = x**2 + y**2 <= 80**2
image = np.zeros((200, 200))
image[mask] = 255

# np.diff calculates out[i] = a[i+1] - a[i]
edges = np.abs(np.diff(image, axis=1))

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5))

ax1.imshow(image, cmap='gray')
ax1.set_title("Original Shape")
ax1.axis('off')

ax2.imshow(edges, cmap='gray')
ax2.set_title("Detected Edges (Gradients)")
ax2.axis('off')

plt.show()
