class ExpenseSplitter:
    def __init__(self, occasion_name):
        self.occasion = occasion_name
        self.friends = []
        self.total_bill = 0

    def add_expense(self, friend_name, amount):
        self.friends.append(friend_name)
        self.total_bill += amount
        print(f"Added {amount} paid by {friend_name}")

    def calculate_split(self):
        if not self.friends:
            print("No expenses recorded.")
            return

        num_people = len(self.friends)
        share = self.total_bill / num_people
        
        print(f"\n--- Split Report for {self.occasion} ---")
        print(f"Total Spent: {self.total_bill}")
        print(f"Number of Friends: {num_people}")
        print(f"Each person owes: {share:.2f}")
        print("-------------------------------")

# --- Execution ---
party = ExpenseSplitter("Hostel Dinner")
party.add_expense("Kashish", 1200)
party.add_expense("Ananya", 800)
party.add_expense("Shreya", 500)

party.calculate_split()
