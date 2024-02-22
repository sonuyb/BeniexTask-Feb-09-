class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def display(self):
        print("Name:", self.name)
        print("Score:", self.score)

student1 = Student("Aswin", 15)
student2 = Student("Boby", 25)

print("Student 1 details:")
student1.display()
print("\nStudent 2 details:")
student2.display()
