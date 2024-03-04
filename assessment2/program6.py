def sort_by_length_descending(strings):
 return sorted(strings, key=len, reverse=True)
 
string_list = ["apple", "banana", "cherry", "date", "strawberry"]
sorted_list = sort_by_length_descending(string_list)
print(sorted_list)