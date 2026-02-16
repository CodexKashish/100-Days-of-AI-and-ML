class VibeCheck:
    def __init__(self, user_name):
        self.user_name = user_name
        # Mapping moods to playlists (No emojis in code)
        self.mood_map = {
            "focus": ["Lofi Hip Hop", "Interstellar Soundtrack", "Classical Piano"],
            "energetic": ["Blinding Lights", "Power", "Uptown Funk"],
            "peaceful": ["Weightless", "Nature Sounds", "River Flows In You"],
            "bollywood": ["Tum Hi Ho", "Jai Ho", "Dil Chahta Hai"]
        }

    def get_recommendation(self, mood):
        # Normalize the input
        mood = mood.lower()
        songs = self.mood_map.get(mood)

        if songs:
            print(f"Hey {self.user_name}, I see you are feeling {mood}!")
            print("Here is your curated Day 41 playlist:")
            for i, song in enumerate(songs, 1):
                print(f"{i}. {song}")
        else:
            print(f"Hmm, I do not have a playlist for {mood} yet. Try 'Focus' or 'Energetic'!")

# --- Execution ---
my_vibe = VibeCheck("Kashish")

print("--- Welcome to the Day 41 Vibe-Sync ---")
current_mood = input("How is the vibe today? (Focus/Energetic/Peaceful/Bollywood): ")
my_vibe.get_recommendation(current_mood)
