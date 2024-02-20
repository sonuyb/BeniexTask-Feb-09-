def remove_element(lst, element):
    return [x for x in lst if x != element]

if __name__ == "__main__":
    lst = input("Enter the elements of the list separated by spaces: ").split()
    lst = [int(x) for x in lst]

    element = int(input("Enter the element to remove: "))

    updated_list = remove_element(lst, element)
    print("List after removing all occurrences of the element:", updated_list)
