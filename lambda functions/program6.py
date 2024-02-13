fibonacci_series = lambda n: [0, 1] + [fibonacci_series(i)[-1] + fibonacci_series(i)[-2] for i in range(2, n)]

# Example usage
n = int(input("Enter a number (n) for Fibonacci series: "))

result = fibonacci_series(n)
print(f"Fibonacci series up to {n}:", result)
