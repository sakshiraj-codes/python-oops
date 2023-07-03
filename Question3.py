"""Design a class Student with attributes name, age, and marks.
Implement methods get_name(), get_age(), get_marks(), and display() to get and display the details of a student."""


class Student:
    def __init__(self, name, age, marks):
        self.name = name
        self.age = age
        self.marks = marks

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def get_marks(self):
        return self.marks

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Marks:", self.marks)


# Create Student objects
student1 = Student("Sakshi", 21, 95)
student2 = Student("Raj", 22, 88)

print(student1.get_name())  # Output: Sakshi
print(student2.get_age())  # Output: 22
print(student1.get_marks())  # Output: 95

student2.display()
# Output:
# Name: Raj
# Age: 22
# Marks: 88