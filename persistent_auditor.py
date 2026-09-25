
def load_inventory():
    with open("inventory.txt", "a+") as file:
        file.seek(0)
        inventory_data = file.readlines()
        if inventory_data == "" or inventory_data == []:
            global uid
            uid = 1000
            file.write("Current Orders:\n")
        else:
            file.seek(0)
            inventory_read = file.read()
            print(inventory_read)
            uid = int(inventory_data[-1].split(",")[0].strip().replace('"', ''))

def save_inventory():
    for entry in history:
        with open("inventory.txt", "a") as file:
            file.write(str(entry[0]) + "," + entry[1] + "," + str(entry[2]) + "\n")

uid = 0
history = []
load_inventory()
while True:
    productInput = input("Enter product name: ")
    if productInput.lower() == 'quit':
            save_inventory()
            print("Order successfully saved to inventory.txt.")
            break
    else:
        quantityInput = input("Enter Quantity: ")
        if quantityInput.lower() == 'quit':
                    save_inventory()
                    print("Order successfully saved to inventory.txt.")
                    break
        elif not quantityInput.isdigit():
            print("Invalid input. Please enter a valid stock quantity.")
            continue
        else:
            uid += 1
            history.append((uid, productInput, int(quantityInput)))
            print("New Order Added:\n", uid,",", productInput,",", int(quantityInput))
        
