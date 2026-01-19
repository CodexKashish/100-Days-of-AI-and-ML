# ---------------------------------------------------------
# Project: The Modular Innovation Suite 🛠️
# Day 13/100: Structural Design & Menu-Driven Logic
# Goal: Organize persistent data tools into a unified system.
# ---------------------------------------------------------

import os

# --- TOOL 1: THE VAULT WRITER ---
def archive_idea(idea):
    """Encrypts and saves an idea to the permanent vault."""
    secret_data = idea[::-1]
    with open("innovation_vault.txt", "a") as vault:
        vault.write(secret_data + "\n")
    print("✅ Idea safely archived.")

# --- TOOL 2: THE DISCOVERY ENGINE ---
def find_patterns(keyword):
    """Searches the vault for specific keywords."""
    found = False
    if not os.path.exists("innovation_vault.txt"):
        return print("⚠️ Vault empty.")
    
    with open("innovation_vault.txt", "r") as vault:
        for line in vault:
            original = line.strip()[::-1]
            if keyword.lower() in original.lower():
                print(f"✨ Match Found: {original}")
                found = True
    if not found: print("❌ No matches.")

# --- MAIN CONTROL CENTER ---
def main_menu():
    while True:
        print("\n--- 🚀 INNOVATION CONTROL CENTER ---")
        print("1. Archive New Idea")
        print("2. Discover Patterns (Search)")
        print("3. Exit System")
        
        choice = input("\nSelect an action (1-3): ")
        
        if choice == '1':
            idea = input("💡 Enter your innovation: ")
            archive_idea(idea)
        elif choice == '2':
            key = input("🔍 Enter search keyword: ")
            find_patterns(key)
        elif choice == '3':
            print("Shutting down... Keep innovating! 👋")
            break
        else:
            print("❌ Invalid selection.")

if __name__ == "__main__":
    main_menu()
