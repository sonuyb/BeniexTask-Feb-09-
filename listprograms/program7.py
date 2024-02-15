original_tuple = (5, 1, 5, 3, 3, 8, 6, 9)
repeated_items = []
for i in range(len(original_tuple)):
    for j in range(i + 1, len(original_tuple)):
        if original_tuple[i] == original_tuple[j] and original_tuple[i] not in repeated_items:
            repeated_items.append(original_tuple[i])
print("Original Tuple:", original_tuple)
print("Repeated Items:", repeated_items)
