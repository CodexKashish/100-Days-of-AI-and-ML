import numpy as np
import matplotlib.pyplot as plt

base = np.linspace(0, 255, 300*300).reshape(300, 300).astype(np.uint8)

# Strategy: Strong Red, Low Green, High Blue
red_channel = np.clip(base * 1.0, 0, 255).astype(np.uint8)
green_channel = np.clip(base * 0.2, 0, 255).astype(np.uint8)
blue_channel = np.clip(base * 0.9, 0, 255).astype(np.uint8)

cyberpunk_image = np.dstack((red_channel, green_channel, blue_channel))

# Strategy: High Red, Medium Green, Low Blue
sepia_r = np.clip(base * 1.0, 0, 255).astype(np.uint8)
sepia_g = np.clip(base * 0.8, 0, 255).astype(np.uint8)
sepia_b = np.clip(base * 0.4, 0, 255).astype(np.uint8)
sepia_image = np.dstack((sepia_r, sepia_g, sepia_b))

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))
ax1.imshow(cyberpunk_image)
ax1.set_title("Cyberpunk Tint (R+B Focus)")
ax2.imshow(sepia_image)
ax2.set_title("Vintage Sepia (R+G Focus)")
for ax in [ax1, ax2]: ax.axis('off')
plt.show()
