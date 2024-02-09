user_input = input("Enter a number: ")
if user_input.isdigit():
    number = int(user_input)
    if number % 2 == 0:
        print(f"{number} is even.")
    else:
        print(f"{number} is odd.")
else:
    print("Invalid input. Please enter a valid integer.")