def sort_sequence(sequence): 
    result_sequence = '-'.join(sorted(input_sequence.split('-')))
    return result_sequence
input_sequence = input("Enter hyphen-separated sequence of words: ")
print(sort_sequence(input_sequence))
   


