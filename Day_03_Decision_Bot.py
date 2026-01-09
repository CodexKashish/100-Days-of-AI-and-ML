# Project: The Explorer Decision Bot
# Goal: Master Conditional Logic (if-elif-else)

def main():
    print("--- 🤖 Explorer Decision Bot ---")
    print("I will help you choose your next destination based on your preferences!")

    # 1. Gathering inputs (Data)
    budget = int(input("\nWhat is your budget for the trip (in INR)? "))
    weather = input("Do you prefer 'Mountains' or 'Beaches'? ").strip().capitalize()
    
  # 2. Making Decisions (The Logic)
    print("\n--- 📍 Bot Suggestion ---")
    
    if budget >= 50000:
        if weather == "Mountains":
            print("Recommendation: Switzerland 🏔️ (Luxury Alpine Experience)")
        elif weather == "Beaches":
            print("Recommendation: Maldives 🏝️ (Premium Beach Villa)")
        else:
            print("Recommendation: Japan 🌸 (A mix of everything!)")
            
    elif 10000 <= budget < 50000:
        if weather == "Mountains":
            print("Recommendation: Manali, India ❄️ (Beautiful Himalayas)")
        elif weather == "Beaches":
            print("Recommendation: Goa, India 🌊 (Vibrant Coastal Vibes)")
        else:
            print("Recommendation: Rishikesh, India ✨")

    else:
        print("Recommendation: A local weekend getaway! 🚗 (Great for saving budget)")

    print("\nDay 3 Complete: Logic Building and Nested If-Else mastered.")

if __name__ == "__main__":
    main();
