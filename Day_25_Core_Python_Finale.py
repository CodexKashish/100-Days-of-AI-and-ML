# ---------------------------------------------------------
# Project: The Innovation Ecosystem Architect 🌍
# Day 25/100: Grand Finale of Core Python Integration
# Goal: The most advanced version of your vault yet.
# ---------------------------------------------------------

import os

def final_grand_system():
    print("--- 🌍 WELCOME TO THE INNOVATION ECOSYSTEM (FINAL V1) ---")
    vault_file = "academic_leads.txt"

    try:
        # 1. Loading and Cleaning with List Comprehensions (Day 24 logic)
        if not os.path.exists(vault_file):
            print("📝 Initializing vault... add your first lead to start.")
            raw_leads = []
        else:
            with open(vault_file, "r") as f:
                # Cleaning every line in the file in one high-speed step
                raw_leads = [line.strip() for line in f.readlines() if line.strip()]

        # 2. Interactive Menu (Day 13/20 logic)
        while True:
            print(f"\nCurrently managing: {len(raw_leads)} Global Leads")
            print("1. Add New Lead (with Auto-Cleaning)")
            print("2. Search Leads (with Case-Insensitivity)")
            print("3. Exit System")
            
            choice = input("\nAction: ")

            if choice == '1':
                name = input("Institution: ").strip().title()
                focus = input("Focus (AI/ML/Analytics): ").strip().upper()
                # 3. Validation & Persistence (Day 16/22 logic)
                if name and focus:
                    new_entry = f"{name} | {focus}"
                    raw_leads.append(new_entry)
                    with open(vault_file, "a") as f:
                        f.write(new_entry + "\n")
                    print(f"✅ {name} added to the ecosystem.")
                
            elif choice == '2':
                # 4. Smart Retrieval (Day 17 logic)
                query = input("🔍 Search Keyword: ").lower()
                results = [item for item in raw_leads if query in item.lower()]
                print(f"Results: {results if results else 'No matches found.'}")

            elif choice == '3':
                print("🏁 Core Python Phase Complete. Ready for AI Libraries tomorrow!")
                break

    except Exception as e:
        print(f"🛡️ The Safety Shield caught an error: {e}")

if __name__ == "__main__":
    final_grand_system()
