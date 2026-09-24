def load_inventory():
    with open("inventory.txt", "a+") as file:
        file.seek(0)
        inventory_data = file.read()
        if inventory_data == "":
            file.write("Current Orders:\n")
        
history = []
load_inventory()
while True:
    productInput = input("Enter product name: ")
    QuantityInput = input("Enter Quantity: ")
    if not QuantityInput.isdigit():
        print("Invalid input. Please enter a valid stock quantity.")
        continue
    else:
        history.append((productInput, int(QuantityInput)))
    print("Current Inventory: ", history)
