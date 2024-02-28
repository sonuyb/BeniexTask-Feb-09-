try:
    user_input = input("Please enter an integer: ")
    user_integer = int(user_input)
    print(f"User entered: {user_integer}")
except ValueError:
    print("Oops! That's not a valid integer. Please try again.")
