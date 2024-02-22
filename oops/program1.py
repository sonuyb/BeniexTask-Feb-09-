class Sdetails:
    
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

student1 = Sdetails("jerry", 8, "c")
student2 = Sdetails("anandhu", 23, "B")

print("Student 1:")
print("Name:", student1.name)
print("Age:", student1.age)
print("Grade:", student1.grade)

print("\nStudent 2:")
print("Name:", student2.name)
print("Age:", student2.age)
print("Grade:", student2.grade)