# General Class (The Parent)
class UniversityMember:
    def __init__(self, name, id_number):
        self.name = name
        self.id_number = id_number
        self.campus_access = True

    def show_profile(self):
        print(f"Name: {self.name} | ID: {self.id_number}")

# Specialized Class (The Child) - Inherits from UniversityMember
class Student(UniversityMember):
    def __init__(self, name, id_number, sgpa):
        # super() links this to the Parent class
        super().__init__(name, id_number)
        self.sgpa = sgpa

    def access_library(self):
        print(f"Access Granted to Library for Student {self.name}")

# Another Specialized Class (The Child)
class Professor(UniversityMember):
    def __init__(self, name, id_number, department):
        super().__init__(name, id_number)
        self.department = department

    def access_research_lab(self):
        print(f"Access Granted to High-Tech Lab for Prof. {self.name}")

# --- System Execution ---
# A Student instance
s1 = Student("Kashish", "STU101", 9.0)
s1.show_profile() # Inherited from Parent
s1.access_library()

print("-" * 30)

# A Professor instance
p1 = Professor("Dr. Sharma", "PROF505", "AI/ML")
p1.show_profile() # Inherited from Parent
p1.access_research_lab()
