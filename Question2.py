"""Design a Person class that represents a person with attributes like
name, age, and address, along with methods to get and set these attributes."""

class Person:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_age(self):
        return self.age

    def set_age(self, age):
        self.age = age

    def get_address(self):
        return self.address

    def set_address(self, address):
        self.address = address


# Create Person objects
person1 = Person("Raj", 30, "Delhi")

# Get and set attributes of person1
print("Name:", person1.get_name())
print("Age:", person1.get_age())
print("Address:", person1.get_address())

person1.set_name("Raj")
person1.set_age(28)
person1.set_address("Lucknow")

print("Updated Name:", person1.get_name())
print("Updated Age:", person1.get_age())
print("Updated Address:", person1.get_address())