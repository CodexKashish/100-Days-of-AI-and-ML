class SmartDrone:
    def __init__(self, drone_id):
        self.drone_id = drone_id
        # The underscore _ means "Internal" (Please don't touch directly)
        self._battery_level = 100 

    # Getter: To see the battery
    def get_battery(self):
        return self._battery_level

    # Setter: To change the battery safely
    def set_battery(self, value):
        if 0 <= value <= 100:
            self._battery_level = value
            print(f"Battery updated to {self._battery_level}%")
        else:
            print("Invalid Battery Level! Must be between 0 and 100.")

    def launch_mission(self, cost):
        if self._battery_level - cost >= 20:
            self._battery_level -= cost
            print(f"Mission Launch Successful. Remaining: {self._battery_level}%")
        else:
            print("Mission Aborted: Battery too low for safe return!")

# --- Execution ---
my_drone = SmartDrone("ALPHA-1")

# Trying to set an impossible battery level
my_drone.set_battery(150) 

# Successful mission
my_drone.launch_mission(30)

# Dangerous mission
my_drone.launch_mission(60) # Should be blocked (30 - 60 < 20)
