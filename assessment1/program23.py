def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

if __name__ == "__main__":
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))

    result_gcd = gcd(num1, num2)
    print(f"GCD of {num1} and {num2} is:", result_gcd)
