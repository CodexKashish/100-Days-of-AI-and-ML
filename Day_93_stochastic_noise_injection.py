import numpy as np
import matplotlib.pyplot as plt

image = np.full((300, 300), 128, dtype=np.uint8)

probability_map = np.random.rand(300, 300)

image[probability_map < 0.02] = 0    # Pepper noise
image[probability_map > 0.98] = 255  # Salt noise

plt.figure(figsize=(6, 6))
plt.imshow(image, cmap='gray')
plt.title("Day 93: Stochastic Noise Injection (Robustness Training)")
plt.axis('off')
plt.show()
