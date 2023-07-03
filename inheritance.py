"""Vehicle is a base class, and Car is a derived class that inherits from the Vehicle class.
The Car class inherits the attributes and methods of the Vehicle class,
 and also has its own unique attributes and method."""

class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def display_info(self):
        print("Brand: ", self.brand)
        print("Model: ", self.model)

class Car(Vehicle):
    def __init__(self, brand, model, num_wheels):
        super().__init__(brand, model)
        self.num_wheels = num_wheels

    def display_info(self):
        super().display_info()
        print("Number of Wheels: ", self.num_wheels)

car1 = Car("Toyota", "Camry", 4)
car2 = Car("Honda", "Civic", 4)

car1.display_info()  # Output:
# Brand:  Toyota
# Model:  Camry
# Number of Wheels:  4

car2.display_info()  # Output:
# Brand:  Honda
# Model:  Civic
# Number of Wheels:  4