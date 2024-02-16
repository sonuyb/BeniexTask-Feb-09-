user_dict = {}
num_pairs = int(input("Enter the number of key-value pairs: "))
for i in range(num_pairs):
    key = input("Enter key: ")
    value = int(input("Enter value: "))
    user_dict[key] = value
total_sum = 0
for value in user_dict.values():
    total_sum += value
print("Total sum of all values in the dictionary:", total_sum)
 
