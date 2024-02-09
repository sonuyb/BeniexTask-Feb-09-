number = int(input("Enter the number for multiplication table: "))
end_limit = int(input("Enter the end limit of the table: "))
print(f"Multiplication table of {number} up to {end_limit}:")
for i in range(1, end_limit + 1):
    result = number * i
    print(f"{number} x {i} = {result}")