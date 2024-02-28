class NegativeBalanceError(Exception):
    pass
 
class BankAccount:
    def __init__(self, initial_balance):
        self.balance = initial_balance

    def withdraw(self, amount):
        if amount > self.balance:
            raise NegativeBalanceError("Insufficient funds: Cannot withdraw more than the available balance.")
        self.balance -= amount
        return amount
 
# Example usage
try:
    initial_balance = float(input("Enter initial balance: "))
    account = BankAccount(initial_balance)
    while True:
        ch=input('enter a choice: ')
        if ch=='1':
            print
            print("\nCurrent balance:", account.balance)
            withdrawal_amount = float(input("Enter withdrawal amount: "))
            withdrawn = account.withdraw(withdrawal_amount)
            print("Withdrawn amount:", withdrawn)
            print("\nCurrent balance:", account.balance)
        elif ch=='2':
            print("\nCurrent balance:", account.balance)
            print('exit')
            break
except ValueError:
    print("Invalid input! Please enter a valid number.")
except NegativeBalanceError as e:
    print("Error:", e)