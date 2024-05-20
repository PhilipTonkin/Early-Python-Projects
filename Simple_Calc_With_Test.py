def main():
  while True:  # Keep showing the main menu until the user decides to exit.
      print("\nWelcome to the Educational Calculator!")
      mode = input("\nDo you wish to use calculator mode or test mode?\n\nEnter 'c' or 't', or 'q' to quit: ").strip().lower()

      if mode == 'c':
          calculator_mode()
      elif mode == 't':
          test_mode()
      elif mode == 'q':
          print("Thank you for using the Educational Calculator. Goodbye!")
          break  # Break the loop to exit the program.
      else:
          print("\nInvalid mode selected. Please choose again.")

def calculator_mode():
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
          break  # Exit this function and return to the main menu.

      num1 = float(input("Enter first number: "))
      num2 = float(input("Enter second number: "))
      result = perform_operation(num1, num2, operation)
      if result is not None:
          print(f"The result is: {result}")

def test_mode():
    print("\nWelcome to the test mode!")
    while True:
        operation = input("Enter choice (+, -, *, /, or Q to return): ").strip().upper()
        if operation == 'Q':
            print("Returning to main menu...")
            break

        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        print(f"\nWhat is {num1} {operation} {num2}?")
        
        user_answer = float(input("Enter your answer: "))
        correct_answer = perform_operation(num1, num2, operation)
        
        if user_answer == correct_answer:
            print("Correct! Well done, you're doing great!")
        else:
            print(f"Incorrect! The correct answer is {correct_answer}.") 
            print ("Keep trying, you'll get it!")

def perform_operation(num1, num2, operation):
    if operation == '+':
        return num1 + num2
    elif operation == '-':
        return num1 - num2
    elif operation == '*':
        return num1 * num2
    elif operation == '/':
        if num2 == 0:
            print("Cannot divide by zero!")
            return None
        return num1 / num2
    else:
        print("Invalid operation.")
        return None

if __name__ == "__main__":
    main()
