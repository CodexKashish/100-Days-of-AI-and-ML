# ---------------------------------------------------------
# Project: The Innovation Super-Processor ⚡
# Day 24/100: List Comprehensions & Data Mapping
# Goal: Filter and format data using high-speed Pythonic logic.
# ---------------------------------------------------------

def super_process():
    print("--- ⚡ INNOVATION SUPER-PROCESSOR: ACTIVE ---")
    
    # Let's imagine these are your focus areas from the vault
    raw_data = [" ai ", "  machine learning", "business analytics ", "stem", " AI"]

    # --- THE MAGIC ONE-LINER ---
    # This cleans, uppercases, and filters out 'STEM' all at once!
    processed_leads = [item.strip().upper() for item in raw_data if "stem" not in item.lower()]

    print(f"📥 Raw Data: {raw_data}")
    print(f"📤 Processed AI Leads: {processed_leads}")

    # Another example: Adding a 'Priority' tag to everything
    priority_list = [f"🔥 HIGH: {lead}" for lead in processed_leads]
    
    print("\n--- 📈 PRIORITY REPORT ---")
    for report in priority_list:
        print(report)

if __name__ == "__main__":
    super_process()
