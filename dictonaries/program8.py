def count_letters(input_string):
    letter_counts = {}
    for char in input_string:
        if char.isalpha():
            char = char.lower()
            letter_counts[char] = letter_counts.get(char, 0) + 1
    return letter_counts
input_string = input("Enter a string: ")
result = count_letters(input_string)
print("Dictionary with letter counts:", result)

