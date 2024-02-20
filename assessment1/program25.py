def count_occurrences(tup):
    occurrences = {}
    for element in tup:
        occurrences[element] = occurrences.get(element, 0) + 1
    return occurrences

if __name__ == "__main__":
    tup = tuple(input("Enter the elements of the tuple separated by spaces: ").split())
    
    occurrences = count_occurrences(tup)
    print("Occurrences of each element in the tuple:")
    for element, count in occurrences.items():
        print(f"{element}: {count}")
