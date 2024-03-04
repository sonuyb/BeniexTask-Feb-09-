import math
 
def is_perfect_square(num):
    return int(num ** 0.5) ** 2 == num
 
def find_perfect_squares(number_list):
    perfect_squares = [num for num in number_list if is_perfect_square(num)]
    return perfect_squares
 
numbers = [4, 16, 17, 11, 36, 82, 81, 49, 110, 120, 100]
perfect_squares_list = find_perfect_squares(numbers)
print("Perfect squares in the list:", perfect_squares_list)
 