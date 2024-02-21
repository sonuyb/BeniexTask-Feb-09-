file = open('welcome.txt','r')
a = file.readlines()
for line in a:
    print (line.strip())