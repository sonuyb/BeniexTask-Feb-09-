def reverse_words(sentence):
    words = sentence.split()  
    reversed_words = [word[::-1] for word in words]  
    new_sentence = ' '.join(reversed_words)  
    return new_sentence
 
original_sentence = "Python is awesome"
reversed_sentence = reverse_words(original_sentence)
print("Reversed sentence:", reversed_sentence)