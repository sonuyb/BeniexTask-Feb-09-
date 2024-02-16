user_dict = {}
num_pairs = int(input("Enter the number of key-value pairs: "))
for i in range(num_pairs):
    key = input("Enter key: ")
    value = input("Enter value: ")
    user_dict[key] = value
print("Original dictionary:", user_dict)
keys_to_delete = input("Enter keys to delete (separated by comma): ").split(',')
for key in keys_to_delete:
    if key.strip() in user_dict:
        del user_dict[key.strip()]
print("Updated dictionary after deleting keys:", user_dict)
