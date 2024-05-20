import random

def roll_dice():
    input ("Press enter to roll the dice...")
  
    random_number = random.randint(1, 6)

    print(f"You rolled a {random_number}")

roll_dice()
