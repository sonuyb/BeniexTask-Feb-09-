# Lambda function to check if a string is a number
check_if_number = lambda s: s.isdigit()
test_string = input('enter the string')
if check_if_number(test_string):
    print(f"The string '{test_string}' is a number.")
else:
    print(f"The string '{test_string}' is not a number.")
