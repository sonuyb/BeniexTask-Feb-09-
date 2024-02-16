user_dict = {}
num_pairs = int(input("Enter the number of key-value pairs: "))
for i in range(num_pairs):
    key = input("Enter key: ")
    value = int(input("Enter value: "))
    user_dict[key] = value
max_value = max(user_dict.values())
min_value = min(user_dict.values())
print("Maximum value in the dictionary:", max_value)
print("Minimum value in the dictionary:", min_value)
