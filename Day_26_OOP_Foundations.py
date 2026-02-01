# ---------------------------------------------------------
# Project: The Innovation Lead Architect 🏗️
# Day 26/100: Intro to Object-Oriented Programming (OOP)
# Goal: Create a blueprint for academic leads.
# ---------------------------------------------------------

# 1. Defining the Blueprint (The Class)
class AcademicLead:
    def __init__(self, university, program):
        # These are the 'Attributes' (Data)
        self.university = university
        self.program = program
        self.status = "New"

    # This is a 'Method' (Action)
    def update_status(self, new_status):
        self.status = new_status
        print(f"✅ Status updated for {self.university}!")

    def display_info(self):
        print(f"🏛️  {self.university} | 🎓 {self.program} | 🏷️  Status: {self.status}")

# 2. Creating the Actual Object (The Instance)
# We are 'instantiating' a lead for Drexel
lead1 = AcademicLead("Drexel University", "Business Analytics")

# 3. Using the Object
lead1.display_info()
lead1.update_status("Contacted")
lead1.display_info()
