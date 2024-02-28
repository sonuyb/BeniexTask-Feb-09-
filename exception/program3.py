try:
    numerator = float(input("Enter the numerator: "))
    denominator = float(input("Enter the denominator: "))
    result = numerator / denominator

    print(f"Result of {numerator} / {denominator} = {result:.2f}")

except ZeroDivisionError:
    print("Error: Cannot divide by zero. Please enter a non-zero denominator.")
except ValueError:
    print("Error: Please enter valid numeric values for the numerator and denominator.")
