numberList = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
ansList = []
 
for num in numberList:
    if num == 0 or num == 1:
        continue
    for i in range(2, num // 2 + 1):
        if num % i == 0:
            break
    else:
        ansList.append(num)
 
if len(ansList):
    print("Prime Numbers:", end=" ")
    for ans in ansList:
        print(ans, end=", ")
else:
    print("No prime numbers in the given list.")