class Emp:
    def __init__(self, name):
        self.name = name
        self.salary = 0
    def update_salary(self, hours, rate=200):
        self.salary = hours * rate
    def __str__(self):
        return f"Employee: {self.name}, Salary: ${self.salary}"
 
class PartTimeEmp(Emp):
    def __init__(self, name):
        super().__init__(name)
        self.rate = 150
    def update_salary(self, hours):
        super().update_salary(hours, self.rate)

class TrackEmployees:
    employees = []
 
    def __init__(self, Employee):
        self.employees.append(Employee)
 
    @classmethod
    def average_expense_per_employee(cls):
        total_expense = sum(Employee.salary for Employee in cls.employees)
        return total_expense / len(cls.employees)
 
emp1 = Emp(name=input("enter the first employee name"))
emp1.update_salary(hours=int(input("enter the hours")))
emp2 = Emp(name=input("enter the second employee name"))
emp2.update_salary(hours=int(input("enter the  hours")))
emp3 = Emp(name=input("enter the third employee name"))
emp3.update_salary(hours=int(input("enter the hours")))
 
pemp1 = PartTimeEmp(name=input("enter the first partime employee name"))
pemp1.update_salary(hours=int(input("enter the hours")))
pemp2 = PartTimeEmp(name=input("enter the second partime employee name"))
pemp2.update_salary(hours=int(input("enter the hours")))
pemp3 = PartTimeEmp(name=input("enter the third partime employee name"))
pemp3.update_salary(hours=int(input("enter the hours")))
 
print(emp1)
print(emp2)
print(pemp1)
print(pemp2)
print(pemp3)
 
employees = [emp1, emp2, pemp1, pemp2, pemp3]
total_expense = sum(employee.salary for employee in employees)
print(f"\nTotal Salary Expense: ${total_expense}")
 
te1 = TrackEmployees(emp1)
te2 = TrackEmployees(emp2)
te3 = TrackEmployees(pemp1)
te4 = TrackEmployees(pemp2)
te5 = TrackEmployees(pemp3)
 
average_expense = TrackEmployees.average_expense_per_employee()
print("Average expense per employee:", average_expense)