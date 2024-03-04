def copy_odd_lines(input_file, output_file):
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        for line_number, line in enumerate(infile, 1):
            if line_number % 2 != 0:
                outfile.write(line)
 
input_file_name = 'welcome.txt'
output_file_name = 'output.txt'
copy_odd_lines(input_file_name, output_file_name)