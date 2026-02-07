class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    
class Shop:
    def __init__(self):
        self.products = []

    def add_prod(self, prod_obj):
        self.products.append(prod_obj)

p1 = Product("SAREE 1_000-50_000 ", 5000)
p2 = Product("SUIT  1_000-10_000", 4000)
p3 = Product("LEHENGA  20_000-10_00_000 ", 50000)
p4 = Product("COORD-SET  800-5_000", 2000)
p5 = Product("GOWN 3_000-2_00_000", 5000)
p6 = Product("JUMPSUIT 600-30_000", 6000)
p7 = Product("SHORT DRESS 1_000-8_000", 3000)
p8 = Product("CARDIGANS 4_000-50_000", 5000)

my_shop = Shop()
my_shop.add_prod(p1)
my_shop.add_prod(p2)
my_shop.add_prod(p3)
my_shop.add_prod(p4)
my_shop.add_prod(p5)
my_shop.add_prod(p6)
my_shop.add_prod(p7)
my_shop.add_prod(p8)

print("Welcome to Ghoomar Mahal!")

for i, p in enumerate(my_shop.products, 1):
    print(f"{i}. Item with range: {p.name} and its price is {p.price}")

user_choice = int(input("\nEnter the number of the item you want to buy: "))

index = user_choice - 1

selected_item = my_shop.products[index]
discount = selected_item.price * 0.10
final_price = selected_item.price - discount

print("\n--- YOUR BILL ---")
print(f"Item: {selected_item.name}")
print(f"Original Price: {selected_item.price}")
print(f"Discounted Price (10% off): {final_price}")
