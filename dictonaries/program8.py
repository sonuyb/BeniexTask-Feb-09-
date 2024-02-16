letter_counts = {}
input_string = input("Enter a string: ")
for char in input_string:
    if char.isalpha():
        char = char.lower()
        letter_counts[char] = letter_counts.get(char, 0) + 1
print("Dictionary with letter counts:", letter_counts)
