from program20a import get_valid_input
# Get a valid integer input
age = get_valid_input("Enter your age: ", int)
print(f"Your age is: {age}")
 
# Get a valid float input within a specific range
height = get_valid_input("Enter your height (in meters, between 1.0 and 2.5): ", float, "Invalid height. Please enter a number between 1.0 and 2.5.")
print(f"Your height is: {height} meters")
 
# Get a valid string input with a specific length
name = get_valid_input("Enter your name (must be at least 3 characters): ", str, "Invalid name. Please enter a valid string.")
while len(name) < 3:
    name = get_valid_input("Name must be at least 3 characters. Enter your name: ", str, "Invalid name. Please enter a valid string.")
print(f"Your name is: {name}")