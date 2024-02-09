
def perform_operations(input_number):
    add = input_number + 2
    sub = input_number - 2
    mul = input_number * 4
    div = input_number / 3
    mod = input_number % 2
    expo = input_number ** 2
    floo = input_number // 2

    Individual_results = {
         'addition': add,
         'substraction': sub,
         'multiplication': mul,
         'divison': div,
         'modulus': mod,
         'exponentiation': expo,
         'floor division': floo,

   }
    return Individual_results
input_value = 3
Individual_results = perform_operations(input_value)
print("Individual Results:", Individual_results)
