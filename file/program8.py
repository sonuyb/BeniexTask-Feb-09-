list = ['item1', 'item2', 'item3', 'item4']
fname = 'mainlist.txt'
with open(fname, 'w') as file:
    file.writelines('\n'.join(list))
print(f"The list has been written to {fname}.")