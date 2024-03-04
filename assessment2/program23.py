def get_integer_input():
    while True:
        try:
            user_input = input("Enter First Number: ")
            result = int(user_input)
            print(result)
            break 
        except ValueError:
            print("Invalid Input. Please Input Integer Only.")
 
# Run 1
get_integer_input() 
# Run 2
get_integer_input()
# Run 3
get_integer_input()