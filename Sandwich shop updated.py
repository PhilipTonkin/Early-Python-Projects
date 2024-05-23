total_cost = 0.00
sugar_tax = 0.50

# Function to validate user input and convert it to lowercase
def get_input(prompt, valid_options):
    while True:
        user_input = input(prompt).lower()
        if user_input in valid_options:
            return user_input
        else:
            print(f"Invalid input. Please enter one of the following: {', '.join(valid_options)}")

# Prompting user for their choices with validation
print("Sandwich or Wrap?")
bread_type = get_input("Enter your choice: ", ["sandwich", "wrap"])

print("Meat, Vegetarian or Vegan?")
filling_type = get_input("Enter your choice: ", ["meat", "vegetarian", "vegan"])

print("Cookie, Crisps, Fruit or None")
pudding = get_input("Enter your choice: ", ["cookie", "crisps", "fruit", "none"])

print("Fizzy drink, Water, Juice or None")
drink = get_input("Enter your choice: ", ["fizzy drink", "water", "juice", "none"])

print("Any extra sauce? Yes or No")
sauce = get_input("Enter your choice: ", ["yes", "no"])

print("Any extra salad? Yes or No")
salad = get_input("Enter your choice: ", ["yes", "no"])

# Calculate the total cost based on user inputs
if bread_type != "sandwich":
    total_cost = 2.00
else:
    total_cost = 3.00

if filling_type == "vegetarian" or filling_type == "vegan":
    total_cost = total_cost + 1.00
else:
    total_cost = total_cost + 1.50

if pudding == "cookie" and drink == "fizzy drink":
    total_cost = total_cost + sugar_tax

# Change line 21 to use 'and' instead of 'or'
if pudding == "none" and drink == "none":
    total_cost = total_cost - 0.50

# Add cost for extra sauce
if sauce == "yes":
    total_cost = total_cost + 0.50

# Add cost for extra salad
if salad == "yes":
    total_cost = total_cost + 0.50

# Increase the total cost by £1 if both extra sauce and extra salad are chosen
if sauce == "yes" and salad == "yes":
    total_cost = total_cost + 1.00

# Print the total cost
print(f"Your total cost is: £{total_cost:.2f}")
