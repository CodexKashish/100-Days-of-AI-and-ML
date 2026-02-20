class StealthCipher:
    def __init__(self, shift_key):
        self.shift = shift_key

    def encrypt(self, plain_text):
        result = ""
        for char in plain_text:
            if char.isalpha():
                # Shift the character and wrap around the alphabet
                start = ord('a') if char.islower() else ord('A')
                # The math: (Original Position + Shift) % 26
                new_char = chr(start + (ord(char) - start + self.shift) % 26)
                result += new_char
            else:
                result += char
        return result

    def decrypt(self, secret_text):
        # To decrypt, we just shift backwards
        original_shift = self.shift
        self.shift = -original_shift
        decrypted_text = self.encrypt(secret_text)
        self.shift = original_shift # Reset shift
        return decrypted_text

# --- Execution ---
my_key = 4
cipher = StealthCipher(my_key)

original_msg = "Python is Fun"
secret = cipher.encrypt(original_msg)
decoded = cipher.decrypt(secret)

print(f"Original: {original_msg}")
print(f"Encrypted: {secret}")
print(f"Decrypted: {decoded}")
