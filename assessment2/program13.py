def add(x, y):
    return x + y
 
def subtract(x, y):
    return x - y
 
def multiply(x, y):
    return x * y
 
def divide(x, y):
    if y == 0:
        raise ValueError("Cannot divide by zero")
    return x / y
 
def calculator():
    try:
        num1 = float(input("Enter the first number: "))
        operation = input("Enter the operation (+, -, *, /): ")
        num2 = float(input("Enter the second number: "))
 
        if operation == '+':
            result = add(num1, num2)
        elif operation == '-':
            result = subtract(num1, num2)
        elif operation == '*':
            result = multiply(num1, num2)
        elif operation == '/':
            result = divide(num1, num2)
        else:
            print("Invalid operation. Please enter +, -, *, or /.")
            return
 
        print(f"The result is: {result:.2f}")
 
    except ValueError:
        print("Invalid input. Please enter valid numerical values.")
    except ZeroDivisionError as e:
        print(f"Error: {e}")

calculator()
 