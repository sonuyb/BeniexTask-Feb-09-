def recursive_list_sum(lst):
    if not lst:
        return 0
    else:
        return lst[0] + recursive_list_sum(lst[1:])

if __name__ == "__main__":
    lst = [int(x) for x in input("Enter the elements of the list separated by spaces: ").split()]
    total_sum = recursive_list_sum(lst)
    print("Sum of all elements in the list:", total_sum)
