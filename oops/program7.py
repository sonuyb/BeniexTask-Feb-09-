class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score
        self.grade = self.calculate_grade()

    def calculate_grade(self):
        if self.score >= 90:
            return "A+"
        elif self.score >= 80:
            return "A"
        elif self.score >= 70:
            return "B+"
        elif self.score >= 60:
            return "B"
        elif self.score >= 50:
            return "C"
        elif self.score >= 40:
            return "D"
        else:
            return "FAILED"

    def display(self):
        print("Name:", self.name)
        print("Score:", self.score)
        print("Grade:", self.grade)

    def as_dict(self):
        return {'name': self.name, 'score': self.score, 'grade': self.grade}

student1 = Student("Alice", 85)
student2 = Student("Bob", 92)

print("Student 1 details:")
student1.display()
print("\nStudent 2 details:")
student2.display()

print("\nStudent 1 as dictionary:")
print(student1.as_dict())
print("\nStudent 2 as dictionary:")
print(student2.as_dict())