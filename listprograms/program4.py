list_numbers = [24, 34, 53, 65, 78, 93, 23, 42]
odd_numbers = []
for num in list_numbers:
    if num % 2 != 0:
        odd_numbers.append(num)
print("Original List:", list_numbers)
print("List after removing even numbers:", odd_numbers)
