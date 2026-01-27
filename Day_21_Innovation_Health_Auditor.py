# ---------------------------------------------------------
# Project: The Innovation Health Auditor 🕵️‍♀️
# Day 21/100: Data Profiling & Quality Assurance
# Goal: Scan your vault for missing info or formatting errors.
# ---------------------------------------------------------

import os

def run_health_audit():
    print("--- 🕵️‍♀️ SYSTEM AUDIT: INNOVATION VAULT ---")
    vault_path = "academic_leads.txt"

    if not os.path.exists(vault_path):
        print("❌ Audit Failed: Vault file not found.")
        return

    # Metrics to track
    total_entries = 0
    corrupted_entries = 0
    clean_entries = 0

    print("Analyzing data patterns...\n")

    with open(vault_path, "r", encoding="utf-8") as vault:
        for i, line in enumerate(vault, 1):
            total_entries += 1
            # We expect 3 pipes (4 parts) based on our Day 16/17 logic
            parts = line.strip().split(" | ")
            
            # Check for "Empty" values or missing columns
            if len(parts) < 3 or any(field.strip() == "" for field in parts):
                print(f"⚠️  Flagged Line {i}: Missing data or bad format.")
                corrupted_entries += 1
            else:
                clean_entries += 1

    # --- THE AUDIT REPORT ---
    health_score = (clean_entries / total_entries) * 100 if total_entries > 0 else 0
    
    print("-" * 40)
    print(f"📊 FINAL HEALTH REPORT")
    print("-" * 40)
    print(f"✅ Clean Entries:     {clean_entries}")
    print(f"❌ Flagged Entries:   {corrupted_entries}")
    print(f"📈 Overall Health:   {health_score:.1f}%")
    print("-" * 40)

    if health_score == 100:
        print("🏆 Result: Your data is AI-Ready!")
    else:
        print("🛠️ Recommendation: Clean flagged entries before Day 26.")

if __name__ == "__main__":
    run_health_audit()
