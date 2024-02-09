start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))
print(f"\nAll even numbers between {start} and {end}:")
for number in range(start, end + 1):
    if number % 2 == 0:
        print(number)
print(f"\nAll odd numbers between {start} and {end}:")
for number in range(start, end + 1):
    if number % 2 != 0:
        print(number)