start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))
if start % 2 != 0:
    start += 1
sum_even = sum(range(start, end + 1, 2))
print("Sum of even numbers within the range:", sum_even)

