from functools import reduce

def main():
    # Main loop to keep showing the menu until the user exits.
    while True:
        print("\nWelcome to the Educational Calculator!")
        mode = input("\nDo you wish to use calculator mode or test mode?\n\nEnter 'c' or 't', or 'q' to quit: ").strip().lower()

        if mode == 'c':
            calculator_mode()  # Enter calculator mode
        elif mode == 't':
            test_mode()  # Enter test mode
        elif mode == 'q':
            print("Thank you for using the Educational Calculator. Goodbye!")
            break  # Exit the program
        else:
            print("\nInvalid mode selected. Please choose again.")  # Handle invalid input

def calculator_mode():
    # Loop for calculator operations allowing multiple numbers
    print("\nWelcome to the calculator mode!")
    print("Please select your operation by entering the symbol, for example + for addition...")
    print("+ Addition")
    print("- Subtraction")
    print("* Multiplication")
    print("/ Division")
    print("Q to return to main menu")

    while True:
        operation = input("Enter choice (+, -, *, /, or Q to return): ").strip().upper()
        if operation == 'Q':
            print("Returning to main menu...")
            break  # Return to the main menu

        numbers = input("Enter numbers separated by spaces: ").strip().split()
        numbers = [float(num) for num in numbers]  # Convert input to list of floats
        result = perform_operation(numbers, operation)
        if result is not None:
            print(f"The result is: {result}")

def test_mode():
    # Loop for practice problems with multiple numbers
    print("\nWelcome to the test mode!")
    while True:
        operation = input("Enter choice (+, -, *, /, or Q to return): ").strip().upper()
        if operation == 'Q':
            print("Returning to main menu...")
            break

        numbers = input("Enter numbers separated by spaces for testing: ").strip().split()
        numbers = [float(num) for num in numbers]  # Convert input to list of floats
        correct_answer = perform_operation(numbers, operation)

        user_answer = float(input(f"\nWhat is the result of {' '.join(map(str, numbers))} with '{operation}' operation? "))

        if user_answer == correct_answer:
            print("Correct! Well done, you're doing great!")
        else:
            print(f"Incorrect! The correct answer is {correct_answer}.")
            print("Keep trying, you'll get it!")

def perform_operation(numbers, operation):
    # Calculate and return the result of an arithmetic operation on a list of numbers
    if operation == '+':
        return sum(numbers)
    elif operation == '-':
        return reduce(lambda x, y: x - y, numbers)
    elif operation == '*':
        return reduce(lambda x, y: x * y, numbers)
    elif operation == '/':
        try:
            return reduce(lambda x, y: x / y, numbers)
        except ZeroDivisionError:
            print("Cannot divide by zero!")
            return None
    else:
        print("Invalid operation.")
        return None

if __name__ == "__main__":
    main()  # Entry point of the program