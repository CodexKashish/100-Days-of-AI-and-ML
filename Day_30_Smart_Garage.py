class SmartGarage:
    def __init__(self, garage_name, total_slots):
        self.name = garage_name
        self.total_slots = total_slots
        self.occupied_slots = 0
        self.vehicles = []

    def enter_vehicle(self, plate_number):
        if self.occupied_slots < self.total_slots:
            self.vehicles.append(plate_number)
            self.occupied_slots += 1
            print(f"Entry Granted: {plate_number}")
            print(f"Available Slots: {self.total_slots - self.occupied_slots}")
        else:
            print(f"Entry Denied: {plate_number}. Garage is FULL.")

    def exit_vehicle(self, plate_number):
        if plate_number in self.vehicles:
            self.vehicles.remove(plate_number)
            self.occupied_slots -= 1
            # Assuming a flat fee of 50 for simplicity
            print(f"Exit Success: {plate_number}. Fee paid: 50")
        else:
            print(f"Error: Vehicle {plate_number} was not found in the system.")

# --- System Execution ---
my_garage = SmartGarage("Greater Noida Tech Park", 3)

my_garage.enter_vehicle("UP-16-AB-1234")
my_garage.enter_vehicle("DL-01-XY-5678")
my_garage.enter_vehicle("RJ-14-CC-9999")
my_garage.enter_vehicle("HR-26-DD-0001") # This should fail as slots = 3

my_garage.exit_vehicle("DL-01-XY-5678")
my_garage.enter_vehicle("HR-26-DD-0001") # This should now work
