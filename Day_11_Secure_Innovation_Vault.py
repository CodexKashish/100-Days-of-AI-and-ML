# ---------------------------------------------------------
# Project: The Cyber-Secure Innovation Vault 🔐
# Day 11/100: Persistent Storage & Data Transformation
# Goal: Save "Encrypted" innovation ideas to a permanent file.
# ---------------------------------------------------------

import os

def secure_vault():
    print("--- 🛡️  WELCOME TO THE CYBER-SECURE VAULT ---")
    print("Innovation is power. Keep your ideas protected.\n")

    # 1. The Innovation Input
    idea = input("💡 Enter your Innovation Idea: ").strip()
    
    # 2. Basic Innovation "Encryption" (Reversing the text)
    # This shows you can manipulate data before saving it!
    secret_data = idea[::-1] 

    # 3. File I/O: Writing to the Vault
    with open("innovation_vault.txt", "a") as vault:
        vault.write(secret_data + "\n")
    
    print("✅ Idea encrypted and synced to the secure vault.")

def read_vault():
    print("\n--- 🔓 DECRYPTING THE INNOVATION VAULT ---")
    if not os.path.exists("innovation_vault.txt"):
        print("Vault empty. No ideas found.")
        return

    with open("innovation_vault.txt", "r") as vault:
        for line in vault:
            # Reversing it back to original for the authorized user
            original_idea = line.strip()[::-1]
            print(f"✨ Decrypted Idea: {original_idea}")

if __name__ == "__main__":
    secure_vault()
    read_vault()
    print("\n🚀 Day 11 Complete: Permanent Security Achieved.")
