fibonacci_for = [0, 1]  
for _ in range(8):  
    next_num = fibonacci_for[-1] + fibonacci_for[-2]  
    fibonacci_for.append(next_num)  
print("First 10 Fibonacci numbers using for loop:", fibonacci_for)
fibonacci_while = [0, 1]
count = 2  
while count < 10:  
    next_num = fibonacci_while[-1] + fibonacci_while[-2] 
    fibonacci_while.append(next_num)  
    count += 1 
print("First 10 Fibonacci numbers using while loop:", fibonacci_while)
