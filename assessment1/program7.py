def binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1

if __name__ == "__main__":
    sorted_list = []
    n = int(input("Enter the number of elements in the sorted list: "))
    print("Enter the sorted list:")
    for _ in range(n):
        element = int(input())
        sorted_list.append(element)

    target = int(input("Enter the number to search: "))
    index = binary_search(sorted_list, target)

    if index != -1:
        print(f"Element {target} found at index {index}.")
    else:
        print(f"Element {target} not found in the list.")
