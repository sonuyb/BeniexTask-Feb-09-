start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))
odd_sum = 0
number = start
while number <= end:
    if number % 2 != 0:
        odd_sum += number
    number += 1
print(f"The sum of odd numbers between {start} and {end} is: {odd_sum}")