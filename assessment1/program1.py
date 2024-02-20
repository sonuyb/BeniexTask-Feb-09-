#arithemetic operations
def perform_arithmetic_operations(num1, num2):
    addition = num1 + num2
    subtraction = num1 - num2
    multiplication = num1 * num2
    
    if num2 != 0:
        division = num1 / num2
        floor_division = num1 // num2
        modulus = num1 % num2
    else:
        division = "Division by zero is not allowed"
        floor_division = "Division by zero is not allowed"
        modulus = "Division by zero is not allowed"
    exponentiation = num1 ** num2
    
    return addition, subtraction, multiplication, division, floor_division, modulus, exponentiation

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Perform arithmetic operations
add, sub, mul, div, floo, mod, expo = perform_arithmetic_operations(num1, num2)


print(f"Addition: {add}")
print(f"Subtraction: {sub}")
print(f"Multiplication: {mul}")
print(f"Division: {div}")
print(f"Floor Division: {floo}")
print(f"Modulus: {mod}")
print(f"Exponentiation: {expo}")