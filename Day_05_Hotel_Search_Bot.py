# ---------------------------------------------------------
# Project: Hotel Discovery Bot 🗺️
# Day 5/100: Mastering Lists + Dictionaries
# ---------------------------------------------------------

def start_hotel_bot():
    print("--- 👋 WELCOME TO THE SEARCH BOT ---")
    print("I'll help you find the perfect stay in India!\n")

    # 1. This is our 'Database'. 
    # It's a LIST [] of many DICTIONARIES {}
    hotels_database = [
        {
            "name": "The Shahi Mahal Palace",
            "city": "Mumbai",
            "price": 25000,
            "rating": 5
        },
        {
            "name": "Goa Sunny Sands",
            "city": "Goa",
            "price": 12000,
            "rating": 4
        },
        {
            "name": "Snow Peaks Resort",
            "city": "Manali",
            "price": 9500,
            "rating": 4
        },
        {
            "name": "The Royal Heritage",
            "city": "Delhi",
            "price": 18000,
            "rating": 5
        }
    ]

    # 2. Ask the user what they are looking for
    user_city = input("🔍 Which city are you planning to visit? ").strip().capitalize()
    
    # We use this 'found' variable to check if our search worked
    found = False

    print("\n" + "="*30)
    print("📍 SEARCHING OUR RECORDS...")
    print("="*30)

    # 3. The Search Logic: Postman walking through the list
    for hotel in hotels_database:
        # Check if the current hotel matches the user's city
        if hotel["city"] == user_city:
            print(f"✅ MATCH FOUND: {hotel['name']}")
            print(f"⭐ Rating: {'⭐' * hotel['rating']}")
            print(f"💰 Price: INR {hotel['price']} per night")
            
            # 4. Calculation Part (Like Day 4)
            try:
                nights = int(input(f"\nHow many nights would you like to stay at {hotel['name']}? "))
                total_bill = nights * hotel['price']
                print(f"💳 YOUR ESTIMATED BILL: INR {total_bill}")
                print("Hope you have a wonderful trip! ✈️")
            except ValueError:
                print("❌ Oops! Please enter a number for the days.")
            
            found = True
            break # We found it, so we stop looking!

    # 5. If we finished the loop and found nothing
    if found == False:
        print(f"❌ Sorry, we don't have any hotels in '{user_city}' yet.")
        print("Maybe try Mumbai, Goa, or Manali? 😊")

# Run the program
if __name__ == "__main__":
    start_hotel_bot()
