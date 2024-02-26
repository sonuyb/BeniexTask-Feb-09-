class Emp:
    def __init__(self, name):
        self.name = name
        self.salary = 0  
    def update_salary(self, hours):
        self.salary = hours * 200
    def __str__(self):
        return f"Employee: {self.name}, Salary: ${self.salary}"
 

class PartTimeEmployee(Emp):
    def update_salary(self, hours):
        self.salary = hours * 150
 
  
emp1 = Emp(name="Aswin")
emp1.update_salary(hours=6)
emp2 = Emp(name="Jerry")
emp2.update_salary(hours=8)
 
pemp1 = PartTimeEmployee(name="Joseph")
pemp1.update_salary(hours=8)
pemp2 = PartTimeEmployee(name="Sujith")
pemp2.update_salary(hours=4)
pemp3 = PartTimeEmployee(name="Sachin")
pemp3.update_salary(hours=5)
 
print(emp1)
print(emp2)
print(pemp1)
print(pemp2)
print(pemp3)
 
employees = [emp1,emp2 ,pemp1,pemp2,pemp3]
total_expense = sum(employee.salary for employee in employees)
print(f"\nTotal Salary Expense: ${total_expense}")