number = int(input("Enter a number to find its factorial: "))
factorial = 1
i = 1
while i <= number:
    factorial *= i
    i += 1
print(f"The factorial of {number} is: {factorial}")