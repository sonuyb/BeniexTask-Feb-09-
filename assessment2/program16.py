def count_uppercase_characters(file_name):
    try:
        with open(file_name, 'r') as file:
            content = file.read()
            uppercase_count = sum(1 for char in content if char.isupper())
            return f"Total uppercase characters in '{file_name}': {uppercase_count}"
    except FileNotFoundError:
        return f"'{file_name}' not found."
 
file_to_read = 'notes.txt'  
result = count_uppercase_characters(file_to_read)
print(result)