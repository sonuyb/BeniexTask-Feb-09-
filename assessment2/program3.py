file_path = 'testing.txt'
search_string = 'C'
 
with open(file_path, 'r') as file:
    for line_number, line in enumerate(file, start=1):
        if search_string in line:
            print(f"Found '{search_string}' in line {line_number}: {line.strip()}")
        else:
            print("This character not found")