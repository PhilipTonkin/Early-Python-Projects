# Task 1: Basic To-Do List Operations

# Step 1: Initialise an empty list to store tasks
tasks = []

# Step 2: Prompt the user to enter a task
while True:
    task = input("Enter a task (or type 'done' to finish): ")
    if task.lower() == 'done':
        break
    priority = input("Enter the priority (high, medium, low): ").lower()
    tasks.append((task, priority))
    
print("Your current To-Do List:")
for i, (task, priority) in enumerate(tasks, 1):
    print(f"{i}. {task} ({priority})")



