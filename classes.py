""" Employee is a class that represents an employee with attributes (name, age, salary)
 and a method (display_info()) to display employee information."""
class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def display_info(self):
        print("Name: ", self.name)
        print("Age: ", self.age)
        print("Salary: ", self.salary)

employee1 = Employee("John", 30, 5000)
employee2 = Employee("Jane", 28, 4500)

employee1.display_info()
# Output:
# Name:  John
# Age:  30
# Salary:  5000

employee2.display_info()
# Output:
# Name:  Jane
# Age:  28
# Salary:  4500