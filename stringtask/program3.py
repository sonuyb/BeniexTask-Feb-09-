def remove_characters_except(input_string, target_character):
    result = ''
    for char in input_string:
        if char == target_character:
            result = result + char
    return result
sample_string = input('enter the character')
target_character = 'e'
result = remove_characters_except(sample_string, target_character)
print("Expected Result:", result)
