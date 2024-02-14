def print_even_length_words(input_string):
    words = input_string.split()
    even_length_words = [word for word in words if len(word) % 2 == 0]
    result = ' , '.join(even_length_words)
    return result
sample_string = input('enter the string :')
result = print_even_length_words(sample_string)
print("Expected Result :", result)
