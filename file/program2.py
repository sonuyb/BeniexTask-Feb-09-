a = 'welcome.txt'
n = 3
file = open('welcome.txt', 'r')
linelist = file.readlines()
for textline in linelist[:n]:
    print(textline)
file.close()
