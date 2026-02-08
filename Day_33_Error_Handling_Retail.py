class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class Shop:
    def __init__(self):
        self.products = []

    def add_prod(self, prod_obj):
        self.products.append(prod_obj)

# Setup inventory
p1 = Product("Saree", 5000)
p2 = Product("Suit", 4000)
my_shop = Shop()
my_shop.add_prod(p1)
my_shop.add_prod(p2)

print("--- Ghoomar Mahal Premium Portal ---")
for i, p in enumerate(my_shop.products, 1):
    print(f"{i}. {p.name} - Price: {p.price}")

# The Day 33 Innovation: The Try-Except Block
try:
    user_choice = int(input("\nEnter item number to buy: "))
    index = user_choice - 1
    
    # Selecting the item
    selected_item = my_shop.products[index]
    
    print("\n--- Processing Bill ---")
    print(f"Item: {selected_item.name}")
    print(f"Total: {selected_item.price}")

except ValueError:
    print("\nError: Please enter a valid number, not text.")
except IndexError:
    print("\nError: That item number does not exist in our inventory.")
except Exception as e:
    print(f"\nAn unexpected error occurred: {e}")
finally:
    print("\nThank you for using the Ghoomar Mahal System.")
