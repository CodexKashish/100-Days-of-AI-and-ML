# ---------------------------------------------------------
# Project: The Wilderness Explorer Toolkit 🏔️🌲
# Day 7/100: Modular Architecture using Functions (def)
# Goal: Build reusable tools for exploration logic.
# ---------------------------------------------------------

# Tool 1: Safety Checker
def check_trek_safety(weather_condition: str):
    """Checks if the environment is safe for trekking."""
    if weather_condition.lower() == "clear":
        return "✅ Conditions are perfect! The mountains are calling. 🏔️"
    elif weather_condition.lower() == "rainy":
        return "⚠️ Caution: Trails might be slippery. Wear waterproof gear! 🌧️"
    else:
        return "❌ Warning: Extreme weather. Stay in the base camp! 🛑"

# Tool 2: Gear Recommender
def get_essential_gear(trip_type: str):
    """Provides a gear list based on the nature of the trip."""
    gear_map = {
        "Hiking": "🥾 Boots, 🎒 Backpack, 💧 Water Bottle",
        "Camping": "⛺ Tent, 🔦 Torch, 🛌 Sleeping Bag",
        "Climbing": "🧗 Harness, ⛑️ Helmet, 🪢 Ropes"
    }
    return gear_map.get(trip_type, "🧥 Warm clothes and a good map!")

# Tool 3: Expense Calculator
def calculate_trip_cost(days: int, rate_per_day: int):
    """Calculates the total investment for the expedition."""
    return days * rate_per_day

# --- MAIN PROGRAM (The Expedition Console) ---
print("--- 🌲 WELCOME TO THE DIGITAL EXPLORER TOOLKIT 🌲 ---")

user_name = "Kashish" # You can use input() here too!
print(f"Hello {user_name}, let's plan your next adventure.\n")

# Using our Tools (Calling Functions)
weather = "Clear"
print(f"Weather Report: {check_trek_safety(weather)}")

trip = "Hiking"
print(f"Packing List for {trip}: {get_essential_gear(trip)}")

days_planned = 5
cost = calculate_trip_cost(days_planned, 3000)
print(f"💰 Total Expedition Budget: INR {cost}")

print("\n--- ✨ WEEK 1 COMPLETE: MISSION ACCOMPLISHED! ---")
