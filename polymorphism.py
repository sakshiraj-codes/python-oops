# Parent class
class Vehicle:
    def drive(self):
        print("Driving a generic vehicle.")

# Child class
class Car(Vehicle):
    def drive(self):
        print("Driving a car.")

# Child class
class Motorcycle(Vehicle):
    def drive(self):
        print("Driving a motorcycle.")


vehicle = Vehicle()
vehicle.drive()  # Output: "Driving a generic vehicle."

car = Car()
car.drive()  # Output: "Driving a car."

motorcycle = Motorcycle()
motorcycle.drive()  # Output: "Driving a motorcycle."