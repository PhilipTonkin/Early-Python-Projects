#ask user for exam score 
score = int(input("enter your exam score"))

#Determine the grade
if score >=90:
    print("Your grde is A.")
elif score >=80:
    print("Your grde is B.")
elif score >=70:
    print("Your grde is C.")
elif score >=60:
    print("Your grde is D.")
else:
    print("Your grde is F.")   