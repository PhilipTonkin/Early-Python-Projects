import tkinter as tk
from tkinter import messagebox

def calculate_slices():
    try:
        slices = int(slices_entry.get())
        people = int(people_entry.get())
        if slices < 0 or people <= 0:
            raise ValueError("Please enter positive numbers where required.")
        slices_per_person = slices // people
        slices_left = slices % people
        result_label.config(text=f"Slices per person: {slices_per_person}\nSlices left: {slices_left}")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid numbers for slices and people.")

def split_bill():
    try:
        bill = float(bill_entry.get())
        tip = float(tip_entry.get())
        people = int(people_entry.get())
        if bill < 0 or tip < 0 or tip > 100 or people <= 0:
            raise ValueError("Please enter positive values for bill, tip (0-100%), and people.")
        bill_with_tip = (tip / 100 * bill) + bill
        final_amount = round(bill_with_tip / people, 2)
        bill_result_label.config(text=f"Each person should pay: £{final_amount}")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid values for bill, tip, and people.")

# Main window setup
root = tk.Tk()
root.title("Split My Pizza App")

# Labels and Entries for Slices and People
tk.Label(root, text="How Many Slices Are There in Total?").pack()
slices_entry = tk.Entry(root)
slices_entry.pack()

tk.Label(root, text="How Many People Are Sharing the Pizza?").pack()
people_entry = tk.Entry(root)
people_entry.pack()

# Button to calculate slices
calc_button = tk.Button(root, text="Calculate Slices", command=calculate_slices)
calc_button.pack()

# Label to show the result of slices calculation
result_label = tk.Label(root, text="")
result_label.pack()

# Additional fields for bill splitting
tk.Label(root, text="\nHow much is the bill?").pack()
bill_entry = tk.Entry(root)
bill_entry.pack()

tk.Label(root, text="How much tip would you like to give (as a percentage)?").pack()
tip_entry = tk.Entry(root)
tip_entry.pack()

# Button to split the bill
bill_button = tk.Button(root, text="Split the Bill", command=split_bill)
bill_button.pack()

# Label to show the result of bill splitting
bill_result_label = tk.Label(root, text="")
bill_result_label.pack()

# Run the main loop
root.mainloop()
