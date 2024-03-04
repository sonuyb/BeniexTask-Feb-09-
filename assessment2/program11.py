class InvalidDiscountError(Exception):
    def __init__(self, message="Invalid discount percentage. Discount must be between 0 and 100."):
        super().__init__(message)
 
def calculate_discounted_price(original_price, discount_percentage):
    if not (0 <= discount_percentage <= 100):
        raise InvalidDiscountError()
 
    discount_amount = original_price * (discount_percentage / 100)
    discounted_price = original_price - discount_amount
    return discounted_price
 
try:
    original_price = float(input("Enter the original price: "))
    discount_percentage = float(input("Enter the discount percentage: "))
    final_price = calculate_discounted_price(original_price, discount_percentage)
    print(f"Discounted price: {final_price:.2f}")
except ValueError:
    print("Invalid input. Please enter valid numeric values.")
except InvalidDiscountError as e:
    print(f"Error: {e}")