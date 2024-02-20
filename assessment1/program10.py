def remove_duplicates(lst):
    return list(set(lst))

if __name__ == "__main__":
    n = int(input("Enter the number of elements in the list: "))
    print("Enter the elements of the list:")
    user_list = [input() for _ in range(n)]

    unique_list = remove_duplicates(user_list)

    print("Original list:", user_list)
    print("List after removing duplicates:", unique_list)
