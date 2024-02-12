def prime_number(n):
   if n<2:
      return False
   for i in range(2,n):
      if n%i == 0:
         return False
   return True
n= int (input('enter a number'))
result = prime_number(n)
if result:
    print(f"{n} is a prime number")
else:
   print(f"{n} is not a prime number")
    
