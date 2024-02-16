user_dict = {}
num_pairs = int(input("Enter the number of key-value pairs: "))
for i in range(num_pairs):
    key = input("Enter key: ")
    value = int(input("Enter value: "))
    user_dict[key] = value
total = 1
for value in user_dict.values():
    total *= value 
print("Result of multiplying all values in the dictionary:", total)