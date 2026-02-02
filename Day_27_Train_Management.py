from random import randint

class Train:
    """A system to manage train bookings and status updates."""
    
    def __init__(self, train_no):
        self.train_no = train_no
        self.is_on_time = True # Default status

    def book_ticket(self, origin, destination):
        print(f"🎫 TICKET CONFIRMED | Train: {self.train_no}")
        print(f"📍 Route: {origin} -> {destination}")

    def get_status(self):
        status = "ON TIME" if self.is_on_time else "DELAYED"
        print(f"🕒 Status for Train {self.train_no}: {status}")

    def calculate_fare(self, origin, destination):
        # In a real app, this would use distance logic
        fare = randint(222, 5555)
        print(f"💰 Fare from {origin} to {destination}: ₹{fare}")

# --- Execution ---
# Modeling a real route (Kota to Jaipur)
my_train = Train(12399)
my_train.book_ticket("Kota", "Jaipur")
my_train.get_status()
my_train.calculate_fare("Kota", "Jaipur")
