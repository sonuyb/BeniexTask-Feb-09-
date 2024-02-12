def fact_number(number):
    if number==0 or number==1:
        return 1
    else:
        return number*fact_number(number-1)
    
a=int(input('enter the number'))
print(fact_number(a))
