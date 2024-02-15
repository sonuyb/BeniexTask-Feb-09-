sample_list = ['abc', 'xyz', 'aba', '1']
count = 0
for string in sample_list:
    if len(string) >= 2:
        count += 1
print("Number of strings with length 2 or more:", count)


