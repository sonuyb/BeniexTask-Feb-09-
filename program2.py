def bank_transaction(balance):
    min_balance = 500
    withdraw_amount = float(input("Enter amount to withdraw: "))
    if withdraw_amount > balance:
        print("Insufficient balance.")
    else:
        balance -= withdraw_amount
        if balance < min_balance:
            print(f"Your account balance is {balance}. Please keep your account balance above Rs.500 to avoid unwanted charges.")
        else:
            print(f"Balance after withdrawal: {balance}")
initial_balance = 1200
bank_transaction(initial_balance)