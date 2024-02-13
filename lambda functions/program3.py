check_start_with_char = lambda string, char: string.startswith(char)
# Example usage
given_string =input('enter a string')
given_char = input('ente a character')
if check_start_with_char(given_string, given_char):
    print(f"The string '{given_string}' starts with the character '{given_char}'.")
else:
    print(f"The string '{given_string}' does not start with the character '{given_char}'.")
