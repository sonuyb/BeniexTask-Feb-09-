# Pattern a)
print("a)")
for i in range(1, 5):
    for j in range(i):
        print("0", end=" ")
    print()

# Pattern b)
print("b)")
for i in range(0,4):
    for j in range(0,4-i-1):
        print(" ", end=" ")
    for k in range(0, 2 * i +1 ):   
        print("*", end=" ")
    print()

# Pattern c)
print("c)")
for i in range(6):
    for j in range(i+1):
        print(i, end=" ")
    print()

# Pattern d)
print("d)")
for i in range(1, 6):
    for j in range(1, i+1):
        print(j, end=" ")
    print()

# Pattern e)
print("e)")
for i in range(6, 0, -1):
    for j in range(i):
        print("*", end=" ")
    print()

# Pattern f)
print("f)")
for i in range(4):
    for j in range(7):
        print("@", end=" ")
    print()
