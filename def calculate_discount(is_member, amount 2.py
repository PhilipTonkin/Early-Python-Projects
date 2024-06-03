def calculate_discount(is_member, amount_spent, age):
    discount = 0

    if is_member:
        if amount_spent >= 100:
            discount = 15
        elif amount_spent >= 50:
            discount = 10
        else:
            discount = 0

        if age >= 60:
            discount += 5

    return discount

# Test cases
def test_calculate_discount():
    # Test case 1: Non-member
    result = calculate_discount(False, 200, 30)
    print(f"Test case 1: expected 0, got {result}")
    assert result == 0, "Test case 1 failed"
    
    # Test case 2: Member, spends less than $50, age less than 60
    result = calculate_discount(True, 40, 30)
    print(f"Test case 2: expected 0, got {result}")
    assert result == 0, "Test case 2 failed"
    
    # Test case 3: Member, spends exactly $50, age less than 60
    result = calculate_discount(True, 50, 30)
    print(f"Test case 3: expected 10, got {result}")
    assert result == 10, "Test case 3 failed"
    
    # Test case 4: Member, spends exactly $100, age less than 60
    result = calculate_discount(True, 100, 30)
    print(f"Test case 4: expected 15, got {result}")
    assert result == 15, "Test case 4 failed"
    
    # Test case 5: Member, spends $150, age less than 60
    result = calculate_discount(True, 150, 30)
    print(f"Test case 5: expected 15, got {result}")
    assert result == 15, "Test case 5 failed"
    
    # Test case 6: Member, spends $150, age 60 (senior)
    result = calculate_discount(True, 150, 60)
    print(f"Test case 6: expected 20, got {result}")
    assert result == 20, "Test case 6 failed"
    
    # Test case 7: Member, spends exactly $50, age 60 (senior)
    result = calculate_discount(True, 50, 60)
    print(f"Test case 7: expected 15, got {result}")
    assert result == 15, "Test case 7 failed"
    
    # Test case 8: Member, spends exactly $100, age 60 (senior)
    result = calculate_discount(True, 100, 60)
    print(f"Test case 8: expected 20, got {result}")
    assert result == 20, "Test case 8 failed"
    
    # Test case 9: Member, spends less than $50, age 60 (senior)
    result = calculate_discount(True, 30, 60)
    print(f"Test case 9: expected 5, got {result}")
    assert result == 5, "Test case 9 failed"
    
    # Test case 10: Member, spends $200, age 59 (not senior)
    result = calculate_discount(True, 200, 59)
    print(f"Test case 10: expected 15, got {result}")
    assert result == 15, "Test case 10 failed"

    print("All test cases passed")

# Run the test cases
test_calculate_discount()