def remove_whitespace(s):
    return ''.join(s.split())

if __name__ == "__main__":
    string = input("Enter a string: ")

    updated_string = remove_whitespace(string)
    print("String after removing whitespace characters:", updated_string)
