def add_two_integers():
    try:
        first_value = int(input("Enter First Value: "))
        second_value = int(input("Enter Second Value: "))
 
        if second_value == 0:
            raise ValueError("Second Number Should Not Be Zero")
 
        result = first_value / second_value
        print(result)
 
    except ValueError as ve:
        print(f"Pls Input Integer Only {ve}")
    except ZeroDivisionError:
        print("Second Number Should Not Be Zero")
 
# Run 1
add_two_integers() 
# Run 2
add_two_integers() 
# Run 3
add_two_integers()