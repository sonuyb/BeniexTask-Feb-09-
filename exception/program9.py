class InvalidAgeError(Exception):
    pass

def get_user_age():
    while True:
        try:
            age = int(input("Please enter your age: "))
            if age < 0 or age > 150:
                raise InvalidAgeError("Age must be between 0 and 150")
            return age
        except ValueError:
            print("Invalid input! Please enter a valid age.")
        except InvalidAgeError as e:
            print(e)
try:
    user_age = get_user_age()
    print("Your age is:", user_age)
except InvalidAgeError as e:
    print("Error:", e)
