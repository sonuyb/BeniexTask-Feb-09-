user_dict = {}
num_pairs = int(input("Enter the number of key-value pairs: "))
for i in range(num_pairs):
    key = input("Enter key: ")
    value = input("Enter value: ")
    user_dict[key] = value
keys_list = list(user_dict.keys())
print("Dictionary keys as a list:", keys_list)
