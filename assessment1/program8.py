def reverse_list(lst):
    return lst[::-1]

if __name__ == "__main__":
    n = int(input("Enter the number of elements in the list: "))
    print("Enter the elements of the list:")
    user_list = [input() for _ in range(n)]

    reversed_list = reverse_list(user_list)

    print("Original list:", user_list)
    print("Reversed list:", reversed_list)
