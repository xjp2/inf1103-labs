uid = 0
def load_inventory():
    with open("inventory.txt", "a+") as file:
        file.seek(0)
        inventory_data = file.readlines()
        if inventory_data == "":
            global uid
            uid = 1000
            file.write("Current Orders:")
        else:
            uid = int(inventory_data[-1].split(",")[0].strip().replace('"', ''))
        
history = []
load_inventory()
while True:
    productInput = input("Enter product name: ")
    QuantityInput = input("Enter Quantity: ")
    if not QuantityInput.isdigit():
        print("Invalid input. Please enter a valid stock quantity.")
        continue
    else:
        uid += 1
        history.append((uid,productInput, int(QuantityInput)))
    print("Current Inventory: ", history)
