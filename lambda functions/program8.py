original_list = [2, 4, 6, 9, 11]
given_number = 2
multiply_with_given_number = lambda x: x * given_number
result = list(map(multiply_with_given_number, original_list))
print("Original list:", original_list)
print("Given number:", given_number)
print("Result:")
print(" ".join(map(str, result)))
