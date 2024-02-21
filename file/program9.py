def count_all_words(fname):
    try:
        with open(fname, 'r') as file:
            data = file.read()
            words = data.split()
            total_words = len(words)
            print(f"Total words in '{fname}': {total_words}")
    except FileNotFoundError:
        print(f"File '{fname}' not found.")
 
# Example usage:
count_all_words("Sample.txt")