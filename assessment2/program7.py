def second_largest(numbers):
    if len(numbers) < 2:
        return "List should have at least two numbers"

    sorted_numbers = sorted(numbers, reverse=True)
 
    return sorted_numbers[1]
 
numbers_list = [10, 5, 8, 20, 15]
result = second_largest(numbers_list)
 
print(f"The second-largest number is: {result}")