def letters(a):
    uppercount=0
    lowercount=0
    for character in a:
        if character.isupper():
            uppercount+=1
        elif character.islower():
            lowercount+=1         
    return uppercount,lowercount      
b=input('enter the string')
upper,lower=letters(b)
print(f'uppercase {upper}, lowercase {lower}')
 
