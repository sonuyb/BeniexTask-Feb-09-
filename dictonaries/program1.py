# Take input for the first dictionary
dict1 = {}
input1 = int(input("Enter the number of entries for the first dictionary: "))
for i in range(input1):
    key = input("Enter key: ")
    value = input("Enter value: ")
    dict1[key] = value

# Take input for the second dictionary
dict2 = {}
input2 = int(input("Enter the number of entries for the second dictionary: "))
for i in range(input2):
    key = input("Enter key: ")
    value = input("Enter value: ")
    dict2[key] = value

# Merge the dictionaries
merged_dict = {}
for key, value in dict1.items():
    merged_dict[key] = value
for key, value in dict2.items():
    merged_dict[key] = value

# Print the merged dictionary
print("Merged dictionary:", merged_dict)
