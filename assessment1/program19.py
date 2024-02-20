def count_vowels(s):
    vowels = 'aeiouAEIOU'
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count

if __name__ == "__main__":
    string = input("Enter a string: ")

    num_vowels = count_vowels(string)
    print("Number of vowels in the string:", num_vowels)
