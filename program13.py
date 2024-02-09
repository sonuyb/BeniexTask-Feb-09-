print("(a)")
n = 4
for i in range(1, n+1):
    print(" "*(n-i) + "* "*i)

print("\n(b)")
num = 0
for i in range(1, 5):
    for j in range(i):
        print(num, end=" ")
        num += 1
    print()

print("\n(c)")
for i in range(0, 4):
    for j in range(-1,i):
        print(i, end=" ")
    print()

print("\n(d)")
for i in range(1, 5):
    print("* " * i)
