class Staff:
    def __init__(self, role, department, salary):
        self.role = role
        self.department = department
        self.salary = salary

    def print_details(self):
        print("Role:", self.role)
        print("Department:", self.department)
        print("Salary:", self.salary)

class Teacher(Staff):
    def __init__(self, name, age, role, department, salary):
        super().__init__(role, department, salary)
        self.name = name
        self.age = age

    def print_details(self):
        print("Name:", self.name)
        print("Age:", self.age)
        super().print_details()

name = input("Enter name: ")
age = input("Enter age: ")
role = input("Enter role: ")
department = input("Enter department: ")
salary = input("Enter salary: ")

teacher = Teacher(name, age, role, department, salary)
teacher.print_details()