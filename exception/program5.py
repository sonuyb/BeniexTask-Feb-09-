def copy_file_content(input_file_path, output_file_path):
    try:
        with open(input_file_path, 'r') as input_file:
            file_contents = input_file.read()
        with open(output_file_path, 'w') as output_file:
            output_file.write(file_contents)
 
    except Exception as e:
        print(f"An error occurred: {e}")
 
    finally:
        if 'input_file' in locals() and not input_file.closed:
            input_file.close()
        if 'output_file' in locals() and not output_file.closed:
            output_file.close()
 
input_file_path = 'welcome.txt'
output_file_path = 'output.txt'
 
copy_file_content(input_file_path, output_file_path)