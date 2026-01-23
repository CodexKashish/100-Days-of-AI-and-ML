# ---------------------------------------------------------
# Project: The Insight Retrieval System 🔍
# Day 17/100: File Querying & Search Logic
# Goal: Find specific global leads instantly using keywords.
# ---------------------------------------------------------

import os

def search_vault():
    print("--- 🔍 INSIGHT RETRIEVAL SYSTEM: ONLINE ---")
    file_path = "academic_leads.txt"

    if not os.path.exists(file_path):
        print("⚠️ Your vault is empty. No data to search.")
        return

    # 1. Capture the search query
    query = input("🔎 Enter a University or Focus Area to find: ").strip().lower()
    
    found_matches = []

    # 2. Scanning the persistent storage
    with open(file_path, "r", encoding="utf-8") as vault:
        for line in vault:
            # We convert to lower to make the search 'case-insensitive'
            if query in line.lower():
                found_matches.append(line.strip())

    # 3. Displaying Results
    print(f"\nScanning for: '{query.title()}'...")
    print("-" * 50)

    if found_matches:
        print(f"✅ Found {len(found_matches)} matching insights:")
        for i, match in enumerate(found_matches, 1):
            print(f"{i}. {match}")
    else:
        print(f"❌ No matches found for '{query}'. Time to expand your network!")

    print("-" * 50)

if __name__ == "__main__":
    search_vault()
