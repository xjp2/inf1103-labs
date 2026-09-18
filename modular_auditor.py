inventory = 0
failcount = 0
def get_valid_input():
    while True:
        userInput = input("Enter a stock quantity to add (or type 'quit' to quit): ")
        if userInput.lower() == 'quit':
            print("Total Units Processed: ", inventory)
            print("Failed entries: ", failcount)
            continue
        elif not userInput.isdigit():
                print("Invalid input. Please enter a valid stock quantity.")
                continue
    

get_valid_input()
    
