with open('welcome.txt', 'r') as firstfile, open('sample.txt', 'a') as secondfile:
    for line in firstfile:
        secondfile.write(line)