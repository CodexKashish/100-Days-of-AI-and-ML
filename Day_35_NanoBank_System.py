class BankAccount:
    def __init__(self, account_number, owner_name, balance=0):
        self.account_number = account_number
        self.owner_name = owner_name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Yay! Added {amount}. New balance: {self.balance}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Spent {amount}. Remaining: {self.balance}")
        else:
            print("Oh no! Not enough money in the piggy bank!")

    def check_balance(self):
        print(f"{self.owner_name}'s Balance: {self.balance}")

my_bank = BankAccount("123", "Little Coder Kashish", 100)
my_bank.check_balance()
my_bank.deposit(50)
my_bank.withdraw(30)
