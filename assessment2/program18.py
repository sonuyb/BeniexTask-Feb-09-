class Student:
    def __init__(self, name, height):
        self.name = name
        self.height = height
 
    def getheight(self):
        return self.height
 
    def __str__(self):
        return f"{self.name}: {self.getheight()}"
 

def HeightRecord(rec, name, height):
    rec.append(Student(name, height))
    return rec
Record = []
 
x = 'y'
while x == 'y':
    name = input("Enter the name of the student: ")
    height = input("Enter the height recorded: ")
    Record = HeightRecord(Record, name, height)
    x = input("Add another student? (y/n): ")
 
n = 1
for el in Record:
    print(f"{n}. {el}")
    n += 1
 