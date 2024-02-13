is_palindrome = lambda s: s == s[::-1]
def find_palindromes(strings):
    return list(filter(is_palindrome, strings))
words = ["level", "hello", "radar", "python", "madam", "noon"]
palindromes = find_palindromes(words)

print("Palindromes in the list:")
print(palindromes)
