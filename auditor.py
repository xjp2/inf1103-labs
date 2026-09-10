inventory = 0
failcount = 0
while True:
    userInput = input("Enter a stock quantity to add (or type 'exit' to quit): ")
    if userInput.lower() == 'quit':
        print("Total Units Processed: ", inventory)
        print("Failed entries: ", failcount)
        break
    elif not userInput.isdigit():
            print("Invalid input. Please enter a valid stock quantity.")
            failcount += 1
            continue
    else:
        inventory += int(userInput)
        print(f"Current Inventory: {inventory}")
        if inventory >= 500:
            print("Inventory limit reached. No more stock can be added.")
            break