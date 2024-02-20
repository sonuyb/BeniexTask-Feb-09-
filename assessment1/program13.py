def contains_only_digits(s):
    return s.isdigit()

if __name__ == "__main__":
    string = input("Enter a string: ")
    if contains_only_digits(string):
        print("The string contains only digits.")
    else:
        print("The string does not contain only digits.")
