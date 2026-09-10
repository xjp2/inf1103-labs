inventory = 0

while True:
    userInput = input("Enter a stock quantity to add (or type 'exit' to quit): ")
    if not userInput.isdigit():
        print("Invalid input. Please enter a valid stock quantity.")
        continue