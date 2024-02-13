# Original list
original_list = ['Python', 3, 2, 4, 5, 'version']

# Lambda function to filter numeric values
is_numeric = lambda x: isinstance(x, int) or isinstance(x, float)

# Get the maximum numeric value using the lambda function
max_value = max(filter(is_numeric, original_list), default=None)

# Print the result
print("Original list:", original_list)
print("Maximum value in the list using lambda:", max_value)
