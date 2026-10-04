inventory = []


def load_inventory():
    global inventory
    with open("inventory.json", "a+") as file:
        file.seek(0)
        data = file.read().strip()
        if data == "" or data == "[]":
            print("inventory.json found.")
            print("Starting with empty inventory.\n")
            inventory = []
        else:
            print("inventory.json found.")
            print("Inventory loaded successfully.\n")
            # Parse string structure into Python list of dictionaries
            clean = data.replace("true", "True").replace("false", "False").replace("null", "None")
            inventory = eval(clean)


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


def display_all(inv):
    print("Current Inventory")
    print("------------------------------------------------")
    for item in inv:
        print(
            "ID: "
            + item["id"]
            + " | Name: "
            + item["name"]
            + " | Price: $"
            + f"{item['price']:.2f}"
            + " | Stock: "
            + str(item["stock"])
        )
    print("------------------------------------------------\n")


def add_product(inv):
    print("Add New Product")
    pid = input("Product ID: ")

    found = False
    for item in inv:
        if item["id"] == pid:
            found = True

    if found:
        print("Product already exists!\n")
    else:
        name = input("Product Name: ")
        price = float(input("Price: "))
        stock = int(input("Stock Quantity: "))
        inv.append({"id": pid, "name": name, "price": price, "stock": stock})
        print("Product added successfully!\n")


def update_stock(inv):
    print("Update Stock")
    pid = input("Enter Product ID: ")

    target = None
    for item in inv:
        if item["id"] == pid:
            target = item

    if target:
        print("Product Found:")
        print("Name: " + target["name"])
        print("Current Stock: " + str(target["stock"]))
        new_stock = int(input("New Stock Quantity: "))
        target["stock"] = new_stock
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
        display_all(inventory)
    elif option == "2":
        add_product(inventory)
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