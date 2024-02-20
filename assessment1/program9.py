def count_occurrences(lst, element):
    count = 0
    for item in lst:
        if item == element:
            count += 1
    return count

if __name__ == "__main__":
    n = int(input("Enter the number of elements in the list: "))
    print("Enter the elements of the list:")
    user_list = [input() for _ in range(n)]

    element_to_count = input("Enter the element to count occurrences: ")

    occurrences = count_occurrences(user_list, element_to_count)

    print(f"The element {element_to_count} occurs {occurrences} times in the list.")
