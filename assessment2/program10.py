def sum_divisible_by_3_or_5(number_list):
    total_sum = 0
    for num in number_list:
        if num % 3 == 0 or num % 5 == 0:
            total_sum += num
    return total_sum
 
numbers = [10, 15, 20, 25, 30, 35, 40]
result = sum_divisible_by_3_or_5(numbers)
print(f"Sum of numbers divisible by 3 or 5: {result}")