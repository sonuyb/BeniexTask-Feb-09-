def merge_files(filenames, output_filename):
  with open(output_filename, 'w') as out_file:
    for filename in filenames:
      with open(filename, 'r') as f:
        out_file.write(f.read())
 
filenames = ["testing.txt", "welcome.txt",]
output_filename = "merged_file.txt"
print('file is merged')
merge_files(filenames, output_filename)