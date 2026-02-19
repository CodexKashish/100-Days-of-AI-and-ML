class AcademicTracker:
    def __init__(self, subject_name, target_attendance=75):
        self.subject = subject_name
        self.target = target_attendance
        self.attended = 0
        self.total_classes = 0

    def log_class(self, attended_today):
        self.total_classes += 1
        if attended_today:
            self.attended += 1
        
        current_percent = (self.attended / self.total_classes) * 100
        print(f"Update for {self.subject}: {current_percent:.1f}% Attendance")
        
        if current_percent < self.target:
            print("Alert: Below 75%! You must attend the next few lectures.")
        else:
            print("Good job! You are in the safe zone.")

    def predict_status(self, upcoming_classes):
        # Predict what happens if you attend all upcoming classes
        potential_total = self.total_classes + upcoming_classes
        potential_attended = self.attended + upcoming_classes
        future_percent = (potential_attended / potential_total) * 100
        print(f"Prediction: If you attend next {upcoming_classes} classes, you will be at {future_percent:.1f}%")

# --- Execution ---
# Tracking a core B.Tech subject like Python or Electronics
my_tracker = AcademicTracker("Data Structures")

# Simulating 5 days of classes
my_tracker.log_class(True)
my_tracker.log_class(True)
my_tracker.log_class(False) # Missed one
my_tracker.log_class(False) # Missed another
my_tracker.log_class(True)

# Look into the future
my_tracker.predict_status(10)
