import numpy as np

# Happy Half-Century! Let's turn numbers into a visual canvas.

# 1. Create a 100x100 grid of random 'Noise'
# This looks like digital static or 'snow' on a TV screen
random_noise = np.random.randint(0, 255, (100, 100))

# 2. Create a smooth 'Gradient' 
# We use linspace to get 100 numbers from 0 to 255
gradient_line = np.linspace(0, 255, 100)

# Now, we stack that line 100 times to create a 2D canvas
# This is where the 'Broadcasting' we learned really shines!
smooth_gradient = np.tile(gradient_line, (100, 1))

print("--- Day 50 Digital Art Report ---")

# Let's peek at a small corner of our random noise (5x5)
print("\nA corner of our Random Noise Canvas:")
print(random_noise[:5, :5])

# Let's see how our gradient starts and ends
print("\nThe gradient starts dark (left):", smooth_gradient[0, 0])
print("The gradient ends light (right):", smooth_gradient[0, -1])

# Fun Fact: If you were using a library like Matplotlib or OpenCV, 
# these arrays would literally show up as pictures on your screen!
print("\nCanvas Generation Complete. We just built 20,000 pixels of math!")
