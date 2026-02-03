class Train:
    # A 'Class Variable' to store distances from Kota (our hub)
    # Distance in KM from Kota
    DISTANCE_MAP = {
        "Jaipur": 250,
        "Delhi": 500,
        "Mumbai": 900,
        "Udaipur": 280
    }
    RATE_PER_KM = 2.5  # Fixed rate in Rupees

    def __init__(self, train_no):
        self.train_no = train_no
        self.passengers = []

    def get_fare(self, destination):
        # Using .get() to avoid errors if the city isn't in our map
        distance = self.DISTANCE_MAP.get(destination)
        
        if distance:
            fare = distance * self.RATE_PER_KM
            print(f"🎫 Train {self.train_no} | Destination: {destination}")
            print(f"🛤️  Distance: {distance}km | Total Fare: ₹{fare}")
            return fare
        else:
            print(f"❌ Sorry, we don't currently have a route to {destination}.")
            return None

# --- Execution ---
t = Train(12399)
t.get_fare("Jaipur")  # Should calculate 250 * 2.5
t.get_fare("Mumbai")  # Should calculate 900 * 2.5
t.get_fare("Chennai") # Should trigger the error message
