# Parent Class
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        # This is a placeholder; it will be changed by children
        print("This animal makes a sound.")

# Child Class 1 (Inheritance + Polymorphism)
class Dog(Animal):
    def speak(self):
        print(f"{self.name} says: Woof Woof!")

# Child Class 2 (Inheritance + Polymorphism)
class Cat(Animal):
    def speak(self):
        print(f"{self.name} says: Meow!")

# Child Class 3 (Inheritance + Polymorphism)
class Lion(Animal):
    def speak(self):
        print(f"{self.name} says: Roar!")

# --- The Power of Polymorphism ---
# We create a list of different animals
zoo = [Dog("Buddy"), Cat("Luna"), Lion("Simba")]

print("--- The Animal Symphony Begins ---")
for animal in zoo:
    # Polymorphism in action: 
    # One command 'speak()', but multiple different results!
    animal.speak()
