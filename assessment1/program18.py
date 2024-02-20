def find_second_largest(lst):
    if len(lst) < 2:
        return "List should have at least two elements"
    
    max_num = float('-inf')
    second_max_num = float('-inf')
    
    for num in lst:
        if num > max_num:
            second_max_num = max_num
            max_num = num
        elif num > second_max_num and num != max_num:
            second_max_num = num
    
    if second_max_num == float('-inf'):
        return "There is no second largest number in the list"
    else:
        return second_max_num

if __name__ == "__main__":
    lst = input("Enter the elements of the list separated by spaces: ").split()
    lst = [int(x) for x in lst]

    second_largest = find_second_largest(lst)
    print("Second largest number in the list:", second_largest)
