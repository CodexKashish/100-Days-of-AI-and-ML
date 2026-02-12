class Drone:
    def __init__(self, drone_id):
        self.drone_id = drone_id

    def perform_mission(self):
        # General mission behavior
        print(f"Drone {self.drone_id} is powering up...")

class DeliveryDrone(Drone):
    def perform_mission(self):
        super().perform_mission()
        print(f"Action: Delivering a package to Sector 7. Dropping altitude...")

class SecurityDrone(Drone):
    def perform_mission(self):
        super().perform_mission()
        print(f"Action: Scanning perimeter for intruders. Thermal sensors ON.")

# --- The Command Center (Polymorphism) ---
# A fleet of different drones
fleet = [
    DeliveryDrone("DEL-101"),
    SecurityDrone("SEC-505"),
    DeliveryDrone("DEL-102")
]

print("--- SMART CITY DRONE FLEET ACTIVE ---")

# The same command triggers completely different specialized actions
for drone in fleet:
    drone.perform_mission()
    print("-" * 20)
