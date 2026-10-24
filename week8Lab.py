class Product:
    def __init__(self, product_id, name, price, stock):
        self.__product_id = product_id
        self.__name = name
        self.__price = price
        self.__stock = stock
        
    def update_stock(self, new_quantity):
        self.__stock = new_quantity

    def display_information(self):
        print(f"ID: {self.__product_id} | Name: {self.__name} | Price: ${self.__price:.2f} | Stock: {self.__stock}")

    def get_id(self):
        return self.__product_id
    
class Inventory:
    def __init__(self):
        self.__products = []

    def add_product(self, product):
            self.__products.append(product)

    def search_product(self, target_id):
        for item in self.__products:
            if item.get_id() == target_id:
                item.display_information()
    def display_all(self):
        for item in self.__products:
            item.display_information()

inventory = Inventory()

def load_inventory():
    global inventory
    with open("inventory.json", "a+") as file:
        file.seek(0)
        data = file.read().strip()
        if data == "" or data == "[]":
            print("inventory.json found.")
            print("Starting with empty inventory.\n")
        else:
            print("inventory.json found.")
            print("Inventory loaded successfully.\n")
            clean = data.replace("true", "True").replace("false", "False").replace("null", "None")
            loaded_dicts = eval(clean) 
            
            for item in loaded_dicts:
                raw_id = item["id"]
                raw_name = item["name"]
                raw_price = item["price"]
                raw_stock = item["stock"]
                new_product = Product(raw_id, raw_name, raw_price, raw_stock)
                inventory.add_product(new_product)


def save_inventory():
    global inventory
    print("Saving inventory...")
    with open("inventory.json", "w") as file:
        file.write("[\n")
        index = 0
        total = len(inventory)
        for item in inventory:
            file.write("  {\n")
            file.write('    "id": "' + item["id"] + '",\n')
            file.write('    "name": "' + item["name"] + '",\n')
            file.write('    "price": ' + str(item["price"]) + ",\n")
            file.write('    "stock": ' + str(item["stock"]) + "\n")
            index += 1
            if index < total:
                file.write("  },\n")
            else:
                file.write("  }\n")
        file.write("]\n")
    print("Inventory saved successfully to inventory.json.\n")



def handle_add_product(inv):
    print("Add New Product")
    pid = input("Product ID: ")

    existing_item = inv.search_product(pid)

    if existing_item:
        print("Product already exists!\n")
    else:
        name = input("Product Name: ")
        price = float(input("Price: "))
        stock = int(input("Stock Quantity: "))
        
        new_item = Product(pid, name, price, stock)
        inv.add_product(new_item)
        print("Product added successfully!\n")

def update_stock(inv):
    print("Update Stock")
    pid = input("Enter Product ID: ")

    # Ask the inventory object to find the product
    target = inv.search_product(pid)

    if target:
        print("Product Found:")
        target.display_information() # Tell the object to print its info
        new_stock = int(input("New Stock Quantity: "))
        
        # Tell the object to update its own stock
        target.update_stock(new_stock)
        print("Stock updated successfully!\n")
    else:
        print("Product not found.\n")

    
def search_product(inv):
    print("Search Product")
    pid = input("Enter Product ID: ")

    target = None
    for item in inv:
        if item["id"] == pid:
            target = item

    if target:
        print("Product Found")
        print("------------------------------------------------")
        print("ID: " + target["id"])
        print("Name: " + target["name"])
        print("Price: $" + f"{target['price']:.2f}")
        print("Stock: " + str(target["stock"]))
        print("------------------------------------------------\n")
    else:
        print("Product not found.\n")


# Main Program
print("========================================")
print("INVENTORY MANAGEMENT SYSTEM")
print("========================================\n")

load_inventory()

print("----------- MENU -----------")
print("1. Display All Products")
print("2. Add Product")
print("3. Update Stock")
print("4. Search Product")
print("5. Save Inventory")
print("6. Exit")
print("----------------------------\n")

while True:
    option = input("Enter option: ")
    print()

    if option == "1":
        inventory.display_all()
    elif option == "2":
        handle_add_product(inventory)
    elif option == "3":
        update_stock(inventory)
    elif option == "4":
        search_product(inventory)
    elif option == "5":
        save_inventory()
    elif option == "6":
        print("Saving inventory before exit...")
        save_inventory()
        print("Program terminated.")
        break