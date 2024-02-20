def is_perfect_number(n):
    if n <= 0:
        return False

    divisors_sum = sum(i for i in range(1, n) if n % i == 0)
    
    return divisors_sum == n

if __name__ == "__main__":
    num = int(input("Enter a number: "))

    if is_perfect_number(num):
        print(f"{num} is a perfect number.")
    else:
        print(f"{num} is not a perfect number.")
