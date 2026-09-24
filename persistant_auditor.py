def load_inventory():
    with open("inventory.txt", "a+") as file:
        inventory_data = file.read()
        print(inventory_data)

load_inventory()