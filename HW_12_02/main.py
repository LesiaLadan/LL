class Item:

    def __init__(self, name, brand, price, description, dimensions):
        self.price = price
        self.description = description
        self.dimensions = dimensions
        self.name = name
        self.brand = brand

    def __str__(self):
        return f"{self.name}, Brand: {self.brand}, description: {self.description}, dimensions - {self.dimensions}, cost: {self.price}"


class User:

    def __init__(self, name, surname, numberphone, delivery_address):
        self.name = name
        self.surname = surname
        self.numberphone = numberphone
        self.delivery_address = delivery_address

    def __str__(self):
        return(f"User: {self.name} {self.surname}, Phone number: {self.numberphone}, Address: {self.delivery_address}")


class Purchase:

    def __init__(self, user):
        self.products = {}
        self.user = user
        self.total = 0

    def add_item(self, item, cnt):
        if item in self.products:
            self.products[item] += cnt
        else:
            self.products[item] = cnt

    def __str__(self):
        items_list = []
        for item, count in self.products.items():
            line = f"{item.name}: {count} pcs."
            items_list.append(line)
        
        items_in_text = "\n".join(items_list)
        total = sum(item.price * count for item, count in self.products.items())

        return f"{self.user.name} {self.user.surname}\nItems:\n{items_in_text}\nTotal cost:\n{total}"

    def get_total(self):
        return sum(item.price * count for item, count in self.products.items())
        

microwave = Item("Microwave", "Samsung", 300, "Awesome!!!", "30x45x60")
tv = Item("TV", "LG", 800, "4K Smart TV", "120x70x10")
fridge = Item("Refrigerator", "Bosch", 1200, "No Frost system", "200x60x60")
laptop = Item("Laptop", "Dell", 1500, "Gaming laptop", "35x25x2")

print(microwave)
print(tv)
print(fridge)
print(laptop)

expected_str_MW = "Microwave, Brand: Samsung, description: Awesome!!!, dimensions - 30x45x60, cost: 300"
expected_str_TV = "TV, Brand: LG, description: 4K Smart TV, dimensions - 120x70x10, cost: 800"
expected_str_FR = "Refrigerator, Brand: Bosch, description: No Frost system, dimensions - 200x60x60, cost: 1200"
expected_str_LT = "Laptop, Brand: Dell, description: Gaming laptop, dimensions - 35x25x2, cost: 1500"

assert str(microwave) == expected_str_MW
assert str(tv) == expected_str_TV
assert str(fridge) == expected_str_FR
assert str(laptop) == expected_str_LT

buyer = User("Ivan", "Ivanov", "+380671234567", "Kyiv, Shevchenka St. 15, apt. 23")

print(buyer)

cart = Purchase(buyer)
cart.add_item(microwave, 4) 
cart.add_item(tv, 2)

print(cart)

assert isinstance(cart.user, User) is True, 'Екземпляр класу User'

for key in cart.products.keys():
    assert isinstance(key, Item), "Ключи для дікта products є екзампляри класу Item "

assert cart.get_total() == 2800
assert cart.get_total() == 2800

cart.add_item(laptop, 10)
cart.add_item(fridge, 1)
cart.add_item(microwave, 1)

print(cart)

assert cart.get_total() == 19300
