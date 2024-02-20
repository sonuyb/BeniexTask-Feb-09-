def sum_of_even_numbers(lst):
    return sum(num for num in lst if num % 2 == 0)

if __name__ == "__main__":
    lst = input("Enter the elements of the list separated by spaces: ").split()
    lst = [int(x) for x in lst]

    sum_even = sum_of_even_numbers(lst)
    print("Sum of even numbers in the list:", sum_even)
