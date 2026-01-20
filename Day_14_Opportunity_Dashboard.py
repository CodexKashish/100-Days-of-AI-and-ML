# ---------------------------------------------------------
# Project: Opportunity Intelligence Dashboard 📈
# Day 14/100: Structured Data Persistence
# Goal: Log and categorize professional outreach and leads.
# ---------------------------------------------------------

import os

def log_lead():
    print("--- 💼 NEW CAREER OPPORTUNITY DETECTED ---")
    
    # Capturing structured metadata
    name = input("🏢 Organization/Sender Name: ").strip()
    opportunity_type = input("🎯 Type (Internship/Academic/Networking): ").strip()
    priority = input("🔥 Priority (High/Medium/Low): ").strip()

    # Saving in a 'CSV-style' format for future Data Science use
    entry = f"{name} | {opportunity_type} | {priority} | Status: Pending\n"

    try:
        with open("career_opportunities.txt", "a", encoding="utf-8") as vault:
            vault.write(entry)
        print(f"\n✅ Lead from {name} successfully archived!")
    except Exception as e:
        print(f"❌ System Error: {e}")

def view_dashboard():
    print("\n--- 📊 YOUR OPPORTUNITY DASHBOARD ---")
    if not os.path.exists("career_opportunities.txt"):
        print("Your dashboard is empty. Keep networking!")
        return

    print(f"{'ORGANIZATION':<20} | {'TYPE':<15} | {'PRIORITY'}")
    print("-" * 50)
    
    with open("career_opportunities.txt", "r") as vault:
        for line in vault:
            parts = line.strip().split(" | ")
            if len(parts) >= 3:
                print(f"{parts[0]:<20} | {parts[1]:<15} | {parts[2]}")

if __name__ == "__main__":
    log_lead()
    view_dashboard()
    print("\n🚀 Day 14: Turning Outreach into Organized Data.")
