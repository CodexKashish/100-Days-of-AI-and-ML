# Project: Travel Bucket List Manager
# Goal: Master Python Lists and Loops

# 1. Create an empty list to store destinations
bucket_list = []

print("--- ✈️ My Travel Bucket List Manager ---")
print("Enter the places you want to visit. Type 'done' when finished.")

# 2. Use a loop to keep asking for destinations
while True:
    destination = input("Add a destination: ")
    
    if destination.lower() == 'done':
        break  # Exit the loop
    
    # 3. Add the item to our list
    bucket_list.append(destination)

# 4. Display the final list professionally
print("\n--- 📍 My Expedition Map ---")
if not bucket_list:
    print("Your bucket list is empty. Time to dream big!")
else:
    # Sorting the list alphabetically makes it look professional
    bucket_list.sort()
    for i, place in enumerate(bucket_list, 1):
        print(f"{i}. {place}")

print(f"\nTotal Destinations: {len(bucket_list)}")
print("Day 2 Complete: Lists and Loops mastered.")
