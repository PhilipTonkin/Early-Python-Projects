total_cost = 0.00
sugar_tax = 0.50
Print("any extra sauce?")
sauce = input("Enter your choice: ").upper()
if sauce == "YES":
    total_cost = total_cost + 0.50
Print("any extra salad?")
salad = input("Enter your choice: ").upper()
if salad == "YES":
    total_cost = total_cost + 0.50
    
# Function to validate user input
def get_input(prompt, valid_options):
    while True:
        user_input = input(prompt).upper()
        if user_input in valid_options:
            return user_input
        else:
            print(f"Invalid input. Please enter one of the following: {', '.join(valid_options)}")

# Prompting user for their choices with validation
print("Sandwich or Wrap?")
bread_type = get_input("Enter your choice: ", ["SANDWICH", "WRAP"])

print("Meat, Vegetarian or Vegan?")
filling_type = get_input("Enter your choice: ", ["MEAT", "VEGETARIAN", "VEGAN"])

print("Cookie, Crisps, Fruit or None")
pudding = get_input("Enter your choice: ", ["COOKIE", "CRISPS", "FRUIT", "NONE"])

print("Fizzy drink, Water, Juice or None")
drink = get_input("Enter your choice: ", ["FIZZY DRINK", "WATER", "JUICE", "NONE"])

# Calculate the total cost based on user inputs
if bread_type != "SANDWICH":
    total_cost = 2.00
else:
    total_cost = 3.00

if filling_type == "VEGETARIAN" or filling_type == "VEGAN":
    total_cost = total_cost + 1.00
else:
    total_cost = total_cost + 1.50

if pudding == "COOKIE" and drink == "FIZZY DRINK":
    total_cost = total_cost + sugar_tax

if pudding == "NONE" or drink == "NONE":
    total_cost = total_cost - 0.50

# Print the total cost
print(f"Your total cost is: £{total_cost}")
