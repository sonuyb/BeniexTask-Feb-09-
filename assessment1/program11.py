def intersection(list1, list2):
    set1 = set(list1)
    set2 = set(list2)
    return list(set1.intersection(set2))

if __name__ == "__main__":
    n1 = int(input("Enter the number of elements in list 1: "))
    print("Enter the elements of list 1:")
    list1 = [input() for _ in range(n1)]

    n2 = int(input("Enter the number of elements in list 2: "))
    print("Enter the elements of list 2:")
    list2 = [input() for _ in range(n2)]

    intersection_list = intersection(list1, list2)

    print("Intersection of list 1 and list 2:", intersection_list)
