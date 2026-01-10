# Project: The Luxury Hotel Profile
# Goal: Master Dictionaries, User Input, and Math Calculations

# 1. Introduction
print("--- 🏨 THE SHAHI MAHAL PALACE ---")
print("Experience royalty in the heart of Mumbai! ✨\n")

# 2. Creating the Data (The Dictionary)
# Note: Cost is now a number (25000) so we can do math with it
hotel = {
    "Name": "The Shahi Mahal Palace",
    "Location": "Mumbai, India 📍",
    "Rating": 4,
    "Price_Per_Night": 25000,
    "Meal_Cost_Per_Day": 3500  # Added meal cost
}

# 3. Displaying Information
print(f"🏢 Hotel Name: {hotel['Name']}")
print(f"📍 Location: {hotel['Location']}")
print(f"⭐ Rating: {'⭐' * hotel['Rating']} ({hotel['Rating']}/5)")
print(f"💰 Room Price: INR {hotel['Price_Per_Night']} per night")
print(f"🍽️ Meal Plan: INR {hotel['Meal_Cost_Per_Day']} per day")

# 4. Updating the Data
print("\n--- 📣 BREAKING NEWS: New Reviews Received! ---")
hotel['Rating'] = 5 
print(f"✅ Current Rating: {'⭐' * hotel['Rating']} (A Perfect Score!)")

# 5. Customer Interaction & Billing
print("\n--- 🛎️ RECEPTION DESK ---")
customer_name = input("Please enter your name: ")
days = int(input("How many days will you be staying with us? "))

# 6. The Calculation Logic
total_room_cost = hotel['Price_Per_Night'] * days
total_meal_cost = hotel['Meal_Cost_Per_Day'] * days
grand_total = total_room_cost + total_meal_cost

# 7. Final Personalized Receipt
print(f"\nHello, {customer_name}! 👋")
print(f"A Heartiest Welcome to the grand '{hotel['Name']}'!")
print(f"🗓️ Stay Duration: {days} Days")
print("-" * 30)
print(f"🏨 Total Room Cost: INR {total_room_cost}")
print(f"🍱 Total Meal Cost: INR {total_meal_cost}")
print(f"💳 GRAND TOTAL TO PAY: INR {grand_total}")
print("-" * 30)
print("Thank you for choosing us for your stay! 🙏")

print("\n--- ✨ END OF PROGRAM ---")
