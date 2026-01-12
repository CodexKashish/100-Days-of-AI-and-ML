# ---------------------------------------------------------
# Project: Smart Budget Hotel Finder 🤖💰
# Day 6/100: Mastering Multi-Condition Logic (AND)
# ---------------------------------------------------------

def main():
    print("--- 🏨 WELCOME TO THE SMART FINDER ---")
    print("Finding the perfect stay that fits your pocket... ✨\n")

    # 1. 📂 Our 'Database' (Expanded with more options)
    # We have multiple hotels in the same city with different prices!
    hotels = [
        {"name": "Luxury Taj Palace", "city": "Mumbai", "price": 25000, "stars": "⭐⭐⭐⭐⭐"},
        {"name": "Zostel Backpacker", "city": "Mumbai", "price": 2000, "stars": "⭐⭐⭐"},
        {"name": "Goa Heritage Resort", "city": "Goa", "price": 15000, "stars": "⭐⭐⭐⭐"},
        {"name": "Beach-Side Shack", "city": "Goa", "price": 1500, "stars": "⭐⭐"},
        {"name": "Delhi Comfort Inn", "city": "Delhi", "price": 5000, "stars": "⭐⭐⭐"},
        {"name": "The Imperial Delhi", "city": "Delhi", "price": 35000, "stars": "⭐⭐⭐⭐⭐"}
    ]

    # 2. 📝 Getting User Preferences
    print("💬 Tell us where you want to go and your budget:")
    target_city = input("🔍 City Name (Mumbai/Goa/Delhi): ").strip().capitalize()
    
    try:
        max_budget = int(input("💰 Max Budget per night (in INR): "))
    except ValueError:
        print("❌ Please enter a valid number for the budget!")
        return

    print(f"\n🔎 Searching for hotels in {target_city} under ₹{max_budget}...")
    print("=" * 45)

    found_count = 0 # 🧮 Counter to track matches

    # 3. ⚙️ The Search Engine (Multi-Condition Logic)
    for hotel in hotels:
        # We check TWO things: City AND Price at the same time!
        if hotel["city"] == target_city and hotel["price"] <= max_budget:
            found_count += 1
            print(f"📍 Option {found_count}: {hotel['name']}")
            print(f"   💸 Rate: INR {hotel['price']} per night")
            print(f"   ✨ Rating: {hotel['stars']}")
            print("-" * 30)

    # 4. 🏁 Final Results
    if found_count == 0:
        print(f"😔 Oops! No hotels found in {target_city} within your budget.")
        print("💡 Tip: Try increasing your budget or changing the city!")
    else:
        print(f"🎉 Success! We found {found_count} great options for you.")

if __name__ == "__main__":
    main()
