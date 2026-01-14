# ---------------------------------------------------------
# Project: The Explorer's Regional Logbook 🏔️🧭
# Day 8/100: Mastering Nested Data (Dictionary of Lists)
# Goal: Categorize multiple nature spots under specific regions.
# ---------------------------------------------------------

def main():
    print("--- 📔 WELCOME TO YOUR DIGITAL LOGBOOK ---")
    print("Documenting your journey through the wild... 🌲✨\n")

    # 1. 📂 The Data Structure: A Dictionary containing Lists
    # This allows us to map ONE state to MANY locations.
    expedition_log = {
        "Maharashtra": ["Lonavala Trek", "Raigad Fort", "Kalsubai Peak"],
        "Himachal": ["Spiti Valley", "Solang Valley", "Kasol Trails"],
        "Goa": ["Dudhsagar Falls", "Palolem Beach"]
    }

    # 2. ➕ Adding New Discoveries
    # Let's say we found a new spot in Maharashtra!
    print("📝 Update: Adding 'Mahabaleshwar' to Maharashtra log...")
    expedition_log["Maharashtra"].append("Mahabaleshwar")

    # 3. 🔍 Search & Explorer Interface
    print("\n--- 📍 SEARCH BY REGION ---")
    region = input("Enter the State to see your discoveries (e.g., Maharashtra): ").strip().capitalize()

    if region in expedition_log:
        print(f"\n🌟 Discoveries found in {region}:")
        # We loop through the LIST inside the dictionary
        for index, spot in enumerate(expedition_log[region], 1):
            print(f"  {index}. {spot} 🗺️")
    else:
        print(f"❌ No log entry found for '{region}'. Time for a new adventure?")

    # 4. 📊 Professional Summary
    print("\n" + "="*40)
    print(f"✅ Total Regions Explored: {len(expedition_log)}")
    print("Keep exploring and documenting! 🥾⛰️")

if __name__ == "__main__":
    main()
