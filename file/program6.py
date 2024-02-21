#to read a random line from a file.

import random
def randomlines(a):
    file = open(a,'r')
    c = file.read().splitlines()
    return random.choice(c)
a=input("enterfile name")
b=randomlines(a)
print(b)