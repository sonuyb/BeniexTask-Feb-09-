main_list = [1, 2, 3, 4, 2, 3, 5, 6, 7, 7, 8]
unique_list = []
for item in main_list:
    if item not in unique_list:
        unique_list.append(item)
print("Original list:", main_list)
print("List with duplicates removed:", unique_list)
