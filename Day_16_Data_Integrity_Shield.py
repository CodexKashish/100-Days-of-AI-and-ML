# ---------------------------------------------------------
# Project: The Data Integrity Shield 🛡️
# Day 16/100: Data Cleaning & Input Validation
# Goal: Ensure your global leads are clean, uniform, and accurate.
# ---------------------------------------------------------

def clean_and_log():
    print("--- 🛡️  DATA INTEGRITY SHIELD: INITIALIZED ---")
    
    # 1. Capture and immediately "Sanitize" the data
    # .title() makes "business analytics" look like "Business Analytics"
    # .upper() makes "ai" look like "AI"
    institution = input("🏛️  University Name: ").strip().title()
    program = input("🎓  Program: ").strip().title()
    focus = input("🔍  Focus (AI/ML/Analytics/STEM): ").strip().upper()

    # 2. Validation: Ensure no empty fields are saved
    if not institution or not program or not focus:
        print("❌ Error: All fields are required to maintain data integrity!")
        return

    # 3. Standardizing categories
    # If the user types 'ML', we can ensure it's logged correctly
    if focus == "ML" or focus == "MACHINE LEARNING":
        focus = "AI/ML"

    entry = f"{institution} | {program} | {focus} | Status: Verified\n"

    try:
        with open("academic_leads.txt", "a", encoding="utf-8") as vault:
            vault.write(entry)
        print(f"\n✅ Verified data for {institution} synced to vault!")
    except Exception as e:
        print(f"❌ Storage Error: {e}")

if __name__ == "__main__":
    clean_and_log()
    print("\n🚀 Day 16: Better Data leads to Better Insights.")
