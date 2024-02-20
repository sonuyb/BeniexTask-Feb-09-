#password creation  

password = input("Enter your password: ")
if len(password) < 8:
    print("Invalid Password: Password must be at least 8 characters long")
else:
    if not any(char.isupper() for char in password):
        print("Invalid Password: Password must contain at least one uppercase letter")
    elif not any(char.islower() for char in password):
        print("Invalid Password: Password must contain at least one lowercase letter")
    elif not any(char.isdigit() for char in password):
        print("Invalid Password: Password must contain at least one digit")
    elif not any(char in ['_', '@', '$'] for char in password):
        print("Invalid Password: Password must contain at least one of the special characters (_@$)")
    else:
        print("Valid Password")
