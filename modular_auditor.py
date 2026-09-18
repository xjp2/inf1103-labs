inventory = 0
failcount = 0

def calculate_tax(amount):
     tax_rate = 0.10 
     return amount * tax_rate

def process_delivery(current_total, new_value):
    global inventory
    inventory = current_total + new_value
    print("Current Inventory: ", inventory)
    if inventory >= 500:
        print("Inventory limit reached. No more stock can be added.")
        return True
    return False
     
def get_valid_input():
    global failcount
    while True:
        userInput = input("Enter a stock quantity to add (or type 'quit' to quit): ")
        if userInput.lower() == 'quit':
            print("Total Delivery Units Processed: ", inventory)
            print("Failed entries: ", failcount)
            tax = calculate_tax(inventory)
            print("Total Tax: ", tax)
            break
        elif not userInput.isdigit():
                print("Invalid input. Please enter a valid stock quantity.")
                failcount += 1
                continue
        else:
            process_delivery(inventory, int(userInput))
            

     
     
get_valid_input()