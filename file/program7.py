fname = 'sample.txt'  
with open(fname, 'r') as file:
    if not file.closed:
        print(f"The file '{fname}' is open.")
    else:
        print(f"The file '{fname}' is closed.")