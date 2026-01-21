# ---------------------------------------------------------
# Project: Innovation Analytics Engine 📉
# Day 15/100: Data Categorization & Summary Logic
# Goal: Automatically count and summarize your global leads.
# ---------------------------------------------------------

import os

def generate_report():
    print("--- 📊 GENERATING INNOVATION INSIGHTS ---")
    file_path = "academic_leads.txt"

    if not os.path.exists(file_path):
        print("⚠️ No data found to analyze.")
        return

    total_leads = 0
    focus_counts = {} # A dictionary to store counts (e.g., 'AI': 2)

    with open(file_path, "r") as vault:
        for line in vault:
            total_leads += 1
            parts = line.strip().split(" | ")
            
            if len(parts) >= 3:
                focus = parts[2] # Getting the 'Focus' area
                # If focus is already in our dictionary, add 1. If not, start at 1.
                focus_counts[focus] = focus_counts.get(focus, 0) + 1

    # --- THE ANALYTICS DISPLAY ---
    print(f"\n✅ Total Global Leads: {total_leads}")
    print("-" * 30)
    print(f"{'FOCUS AREA':<20} | {'COUNT'}")
    print("-" * 30)

    for area, count in focus_counts.items():
        print(f"{area:<20} | {count}")
    
    print("-" * 30)
    print("🚀 Insights Complete: Focus on your high-growth areas!")

if __name__ == "__main__":
    generate_report()
