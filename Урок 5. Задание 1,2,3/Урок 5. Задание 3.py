def investment_decision(X, A, B):
    can_mike = A >= X
    can_ivaн = B >= X

    if can_mike and can_ivaн:
        return 2
    elif can_mike:
        return "Mike"
    elif can_ivaн:
        return "Ivan"
    elif A + B >= X:
        return 1
    else:
        return 0
    
print(investment_decision(100, 80, 70))  # Output: 1 (вместе хватает)
print(investment_decision(100, 120, 50)) # Output: Mike
print(investment_decision(100, 50, 120)) # Output: Ivan
print(investment_decision(100, 150, 150))# Output: 2
print(investment_decision(100, 30, 40))  # Output: 0 (не хватает даже вместе)