from tkinter import Menu


print("Welcome to the pizza calculator!")   

# Validate crust type
print("Would you like thin or thick crust pizza?")
while True:
    crust = input().lower().strip()
    if crust == "thin" or crust == "thick":
        break
    else:
        print("Please enter a valid choice: 'thin' or 'thick'.")

# Validate pizza size
print("What size pizza would you like? (8, 10, 12, 14, or 18 inches)")
valid_sizes = [8, 10, 12, 14, 18]
while True:
    try:
        size = int(input().strip())
        if size in valid_sizes:
            break
        else:
            print("Please enter a valid size: 8, 10, 12, 14, or 18.")
    except ValueError:
        print("Invalid input. Please enter a number.")

# Validate cheese preference
print("Would you like cheese on your pizza? (y/n)")
while True:
    cheese = input().lower().strip()
    if cheese == "y" or cheese == "n":
        break
    else:
        print("Please enter a valid choice: 'y' or 'n'.")

# Validate pizza type
print("What type of pizza would you like: margherita, vegetable, vegan, hawaiian, meat feast")
while True:
    pizza_type = input().lower().strip()
    if pizza_type in ["margherita", "vegetable", "vegan", "hawaiian", "meat feast"]:
        break
    else:
        print("Please enter a valid choice: margherita, vegetable, vegan, hawaiian, meat feast.")

# Validate discount code
print("Do you have a discount code? If so, please enter it now. Press Enter to skip.")
voucher_code = input().lower().strip()

# Initialize the total cost with the base cost
if crust == "thin":
    total_cost = 10
else:
    total_cost = 8

# Add additional charges based on the pizza size
if size > 10:
    total_cost += 2

# Apply the discount if cheese is not chosen
if cheese == "n":
    total_cost -= 0.50

# Add additional charges based on the type of pizza
if pizza_type in ["vegetable", "vegan"]:
    total_cost += 1
elif pizza_type in ["hawaiian", "meat feast"]:
    total_cost += 2

# Apply the voucher code discount if applicable
if voucher_code == "funfriday" and size == 18:
    total_cost -= 2

# Output the final summary
print("Thank you for your order! Please check your order summary below:")
print(f"Crust: {crust}, Size: {size}, Cheese: {'yes' if cheese == 'y' else 'no'}, Type: {pizza_type}, Discount: £{2 if voucher_code == 'funfriday' and size == 18 else 0}, Total Cost: £{total_cost:.2f}")

print("Enjoy your pizza!")
