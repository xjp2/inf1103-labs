from abc import ABC, abstractmethod

class Product(ABC):
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
    
    def get_name(self):
        return self.__name

    def get_price(self):
        return self.__price

    def get_stock(self):
        return self.__stock

    @abstractmethod
    def get_fulfilment_info(self):
        pass


class CanBeShipped(ABC):
    @abstractmethod
    def calculate_shipping_cost(self):
        pass

class PhysicalProduct(Product, CanBeShipped):
    def __init__(self, product_id, name, price, stock, weight):
        super().__init__(product_id, name, price, stock)
        self.weight = weight

    def display_information(self):
        super().display_information()
        print(f"Weight: {self.weight} kg")

    def get_fulfilment_info(self):
        print("product requires physical shipping.")

    def calculate_shipping_cost(self):
        shipping_cost = self.weight * 5.0
        print(f"Shipping Cost: ${shipping_cost:.2f}")

class DigitalProduct(Product):
    def __init__(self, product_id, name, price, stock, file_size):
        super().__init__(product_id, name, price, stock)
        self.file_size = file_size

    def display_information(self):
        super().display_information()
        print(f"File Size: {self.file_size} MB")
        
    def get_fulfilment_info(self):
        print("product is available for digital download.")

class Inventory:
    def __init__(self):
        self.__products = []

    def add_product(self, product):
            self.__products.append(product)

    def search_product(self, target_id):
        for item in self.__products:
            if item.get_id() == target_id:
                return item
        return None

    def display_all(self):
        for item in self.__products:
            item.display_information()

    def get_all_products(self):
        return self.__products
    
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
                if "weight" in item:
                    raw_id = item["id"]
                    raw_name = item["name"]
                    raw_price = item["price"]
                    raw_stock = item["stock"]
                    raw_weight = item["weight"]
                    new_product = PhysicalProduct(raw_id, raw_name, raw_price, raw_stock, raw_weight)
                    inventory.add_product(new_product)
                elif "file_size" in item:
                    raw_id = item["id"]
                    raw_name = item["name"]
                    raw_price = item["price"]
                    raw_stock = item["stock"]
                    raw_file_size = item["file_size"]
                    new_product = DigitalProduct(raw_id, raw_name, raw_price, raw_stock, raw_file_size)
                    inventory.add_product(new_product)
         


def save_inventory():
    global inventory
    print("Saving inventory...")
    product_list = inventory.get_all_products()
    with open("inventory.json", "w") as file:
        file.write("[\n")
        index = 0
        total = len(product_list)
        for item in product_list:
            file.write("  {\n")
            file.write('    "id": "' + item.get_id() + '",\n')
            file.write('    "name": "' + item.get_name() + '",\n')
            file.write('    "price": ' + str(item.get_price()) + ",\n")
            file.write('    "stock": ' + str(item.get_stock()) + "\n")
            index += 1
            if index < total:
                file.write("  },\n")
            else:
                file.write("  }\n")
        file.write("]\n")
    print("Inventory saved successfully to inventory.json.\n")



def handle_add_product(inv):
    print("Add New Product")
    selection = input("Is this a Physical Product (P) or Digital Product (D)? ").strip().upper()
    if selection not in ["P", "D"]:
        print("Invalid selection. Please choose 'P' for Physical or 'D' for Digital.\n")
        return
    else:
        pid = input("Product ID: ")

        existing_item = inv.search_product(pid)

        if existing_item:
            print("Product already exists!\n")
        else:
            name = input("Product Name: ")
            price = float(input("Price: "))
            stock = int(input("Stock Quantity: "))
            if selection == "P":
                weight = float(input("Weight (kg): "))
                new_item = PhysicalProduct(pid, name, price, stock, weight)
            else:
                file_size = float(input("File Size (MB): "))
                new_item = DigitalProduct(pid, name, price, stock, file_size)
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

    target = inv.search_product(pid)

    if target:
        print("Product Found")
        print("------------------------------------------------")
        target.display_information() # Tell the object to print itself
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