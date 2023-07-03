class Person:
    def __init__(self,n,o):
        self.name = n
        self.occupation = o
        networth = 10000

    def info(self):
        print(f"{self.name} is a {self.occupation}")
a = Person("Harry", "SD")

a.info()

