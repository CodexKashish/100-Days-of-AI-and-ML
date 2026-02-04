class SmartCafe:
    # Our menu with prices
    MENU = {
        "Cold Coffee": 120,
        "Masala Chai": 40,
        "Paneer Wrap": 150,
        "Cookie": 60
    }

    def __init__(self, customer_name):
        self.customer = customer_name
        self.cart = []  # To store items ordered
        self.bill = 0   # Total amount

    def add_to_order(self, item):
        price = self.MENU.get(item)
        if price:
            self.cart.append(item)
            self.bill += price
            print(f"✅ Added {item} for ₹{price}. Current Total: ₹{self.bill}")
        else:
            print(f"❌ Sorry, we don't serve '{item}' yet!")

    def show_final_bill(self):
        print(f"\n--- 🧾 BILL FOR {self.customer.upper()} ---")
        if not self.cart:
            print("Your cart is empty!")
        else:
            for item in self.cart:
                print(f"- {item}: ₹{self.MENU[item]}")
            print(f"💰 FINAL TOTAL: ₹{self.bill}")
            print("--- Thank you for visiting! ---")

# --- Interactive Part ---
cafe = SmartCafe("Kashish")
cafe.add_to_order("Cold Coffee")
cafe.add_to_order("Cookie")
cafe.add_to_order("Pizza") # Not in menu
cafe.show_final_bill()
