import string
def letters_file_line(n):
    alphabet = string.ascii_uppercase
    letters = [alphabet[i:i + n] + "\n" for i in range(0, len(alphabet), n)]
 
    with open("string.txt", "w") as f:
        f.writelines(letters)
letters_file_line(4)