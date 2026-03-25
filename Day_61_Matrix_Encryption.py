import numpy as np

secret_message = np.array([9, 0, 7, 5])

key_matrix = np.array([
    [3, 1],
    [2, 2]
])

message_matrix = secret_message.reshape(2, 2)

encoded_message = np.dot(message_matrix, key_matrix)

inverse_key = np.linalg.inv(key_matrix)
decoded_matrix = np.dot(encoded_message, inverse_key)

final_message = np.round(decoded_matrix).flatten()

print("Original Secret:", secret_message)
print("\nEncoded (Scrambled) Matrix:")
print(encoded_message)
print("\nDecoded Message:", final_message)
