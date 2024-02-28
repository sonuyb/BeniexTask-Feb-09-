file_path = input("Enter the path to the file: ")
try:
    with open(file_path, 'r') as file:
        contents = file.read()                          
        print("File contents:")
        print(contents)                                 
        
except FileNotFoundError:                               
    print(f"Error: The file '{file_path}' does not exist.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")