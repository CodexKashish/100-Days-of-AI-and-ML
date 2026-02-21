import random

class OneTimePad:
    def __init__(self):
        self.last_key = []

    def encrypt(self, message):
        encrypted_text = ""
        self.last_key = []
        
        for char in message:
            # Generate a random shift for EVERY single letter
            shift = random.randint(1, 25)
            self.last_key.append(shift)
            
            # Apply the shift logic from yesterday
            start = ord('a') if char.islower() else ord('A')
            if char.isalpha():
                new_char = chr(start + (ord(char) - start + shift) % 26)
                encrypted_text += new_char
            else:
                encrypted_text += char
                
        return encrypted_text, self.last_key

    def decrypt(self, ciphertext, key):
        decrypted_text = ""
        for i in range(len(ciphertext)):
            char = ciphertext[i]
            shift = key[i]
            
            start = ord('a') if char.islower() else ord('A')
            if char.isalpha():
                # Subtracting the specific shift for this specific letter
                new_char = chr(start + (ord(char) - start - shift) % 26)
                decrypted_text += new_char
            else:
                decrypted_text += char
        return decrypted_text

# --- Execution ---
vault = OneTimePad()
msg = "Meet at the Lab"

secret_msg, secret_key = vault.encrypt(msg)

print(f"Message: {msg}")
print(f"Key used: {secret_key}")
print(f"Cipher: {secret_msg}")

# Decrypting using the unique key
original = vault.decrypt(secret_msg, secret_key)
print(f"Decoded: {original}")
