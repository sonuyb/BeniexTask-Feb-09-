def perform_operation(my_list, index):
    try:
        result = my_list[index] ** 2  
        print(f"Result: {result}")
    except IndexError:
        print("Error: Index is out of range. Please provide a valid index.")
 
my_list = [1, 2, 3, 4, 5]
 
perform_operation(my_list, 2)
perform_operation(my_list, 4)