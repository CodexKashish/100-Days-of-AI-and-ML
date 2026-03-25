import numpy as np

# Let's hide a secret code: 9, 0, 7, 5 (Representing your 9.0 goal and a pin)
secret_message = np.array([9, 0, 7, 5])

# We need a 2x2 'Key' matrix to scramble the data
# This is like the password to your data
key_matrix = np.array([
    [3, 1],
    [2, 2]
])

# We reshape our message into a 2x2 to match the key
message_matrix = secret_message.reshape(2, 2)

# ENCODING: The Dot Product scrambles the numbers
encoded_message = np.dot(message_matrix, key_matrix)

# DECODING: To get it back, we need the Inverse of the key
inverse_key = np.linalg.inv(key_matrix)
decoded_matrix = np.dot(encoded_message, inverse_key)

# Rounding because computers sometimes have tiny decimal errors (0.0000001)
final_message = np.round(decoded_matrix).flatten()

print("Original Secret:", secret_message)
print("\nEncoded (Scrambled) Matrix:")
print(encoded_message)
print("\nDecoded Message:", final_message)
