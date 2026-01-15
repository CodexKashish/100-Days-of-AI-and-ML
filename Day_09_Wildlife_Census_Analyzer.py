# ---------------------------------------------------------
# Project: Eco-Guard Wildlife Census Tracker 🌿🛡️
# Day 9/100: Data Analysis & Classification Logic
# Goal: Automatically classify species status based on population.
# ---------------------------------------------------------

def run_wildlife_census():
    print("--- 🦁 ECO-GUARD: CONSERVATION DECISION ENGINE ---")
    print("Analyzing species population data for priority flagging...\n")

    # 1. 📂 The 'Dataset': A List of Dictionaries
    # Representing real-world biodiversity data
    wildlife_census = [
        {"species": "Bengal Tiger", "population": 3100, "habitat": "Forests"},
        {"species": "Snow Leopard", "population": 450, "habitat": "Mountains"},
        {"species": "Indian Rhino", "population": 2200, "habitat": "Grasslands"},
        {"species": "Ganges Dolphin", "population": 1200, "habitat": "Rivers"},
        {"species": "Asiatic Lion", "population": 670, "habitat": "Dry Forests"}
    ]

    print(f"{'SPECIES':<20} | {'POPULATION':<12} | {'CONSERVATION STATUS'}")
    print("-" * 60)

    # 2. 🧠 The Analysis Engine: Classification Logic
    # In AI, this is the start of 'Feature-based Labeling'
    for animal in wildlife_census:
        name = animal["species"]
        count = animal["population"]
        
        # Determining Status based on numerical thresholds
        if count < 500:
            status = "🆘 CRITICAL (Immediate Action)"
        elif count < 2500:
            status = "⚠️ VULNERABLE (High Monitoring)"
        else:
            status = "✅ STABLE (Routine Protection)"

        # Displaying the analyzed result
        print(f"{name:<20} | {count:<12} | {status}")

    print("-" * 60)
    print("\n✅ Analysis Complete: 5 Species Processed.")
    print("💡 Intelligence Note: Lower population counts triggered 'Critical' flags.")

if __name__ == "__main__":
    run_wildlife_census()
