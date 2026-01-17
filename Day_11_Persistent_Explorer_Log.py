# ---------------------------------------------------------
# Project: The Persistent Explorer’s Log 🏔️
# Day 11/100: Mastering File Handling (Write & Append)
# Goal: Save nature discoveries to a permanent text file.
# ---------------------------------------------------------

def save_discovery():
    print("--- 📔 DIGITAL EXPEDITION LOGBOOK ---")
    
    # 1. Get discovery details from the user
    location = input("📍 Where did you explore? ").strip()
    observation = input("🐾 What did you observe? (e.g., Rare Bird, Waterfall): ").strip()
    
    # 2. File Handling: The 'a' mode means 'Append' 
    # It adds new data to the end of the file without deleting the old data.
    try:
        with open("expedition_log.txt", "a", encoding="utf-8") as file:
            entry = f"Location: {location} | Observation: {observation}\n"
            file.write(entry)
        print("\n✅ Discovery successfully synced to your permanent log!")
    except Exception as e:
        print(f"❌ An error occurred while saving: {e}")

def view_logs():
    print("\n--- 📖 READING YOUR PAST DISCOVERIES ---")
    try:
        with open("expedition_log.txt", "r") as file:
            content = file.read()
            if content:
                print(content)
            else:
                print("Your logbook is currently empty. Start exploring!")
    except FileNotFoundError:
        print("⚠️ No log file found yet. Create your first entry first!")

if __name__ == "__main__":
    save_discovery()
    view_logs()
    print("\n✨ Day 11: Data Persistence Achieved! ✨")
