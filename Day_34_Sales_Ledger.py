class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class Shop:
    def __init__(self):
        self.products = []

    def add_prod(self, prod_obj):
        self.products.append(prod_obj)

# Initialize Shop
my_shop = Shop()
my_shop.add_prod(Product("Saree", 5000))
my_shop.add_prod(Product("Suit", 4000))

print("--- Ghoomar Mahal Sales Portal ---")
for i, p in enumerate(my_shop.products, 1):
    print(f"{i}. {p.name} - {p.price}")

try:
    choice = int(input("\nEnter item number sold: "))
    selected = my_shop.products[choice - 1]
    
    # Day 34 Innovation: Writing to a file
    # 'a' means 'append' - it adds to the file without deleting old data
    with open("sales_report.txt", "a") as file:
        file.write(f"Item: {selected.name} | Price: {selected.price} | Status: SOLD\n")
    
    print(f"Success! Sale of {selected.name} has been recorded in the ledger.")

except Exception as e:
    print(f"Error recording sale: {e}")
