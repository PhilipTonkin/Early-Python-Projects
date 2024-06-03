def calculate_discount(is_member, amount_spent, age):
    discount = 0
    
    if is_member:
        if amount_spent >= 100:
            discount = 15
        else:
            if amount_spent >= 50:
                discount = 10
            else:
                discount = 0
        
        if age >= 60:
            discount += 5
    else:
        discount = 0
    
    return discount

#Test cases for calculate_discount
print(calculate_discount(True, 120, 65))  # output 20 member,spend > 100 - >60
print(calculate_discount(True, 70, 45))   # output 10 member,spend > 50 - <60
print(calculate_discount(False, 100, 30)) # output 0 Not member,spend > 100 - <60
print(calculate_discount(True, 40, 70))   # Output 5 member,spend < 50 - > 60
print(calculate_discount(True, 50, 60))   # Output: 15 member,spend > 50 - >60


