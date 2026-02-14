class UniversalTranslator:
    # Our "Brain" - mapping language codes to actual greetings
    # No emojis here, just pure data mapping
    LANGUAGES = {
        "hindi": "Namaste! Kaise hain aap?",
        "spanish": "Hola! Como estas?",
        "french": "Bonjour! Comment allez-vous?",
        "japanese": "Konnichiwa! Genki desu ka?",
        "german": "Guten Tag! Wie geht es dir?"
    }

    def __init__(self, user_name):
        self.user_name = user_name

    def greet(self, lang_code):
        # We look up the language in our dictionary
        greeting = self.LANGUAGES.get(lang_code.lower())
        
        if greeting:
            print(f"User: {self.user_name}")
            print(f"Translation: {greeting}")
        else:
            print(f"Sorry, I am still learning {lang_code}!")

# --- Execution ---
my_bot = UniversalTranslator("Kashish")

# Test different languages
my_bot.greet("Hindi")
my_bot.greet("Spanish")
my_bot.greet("Korean") # This language isn't in our 'brain' yet
