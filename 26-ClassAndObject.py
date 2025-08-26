# Class and object 
# A class is a blueprint. An object is an instance of a class

class car:
    # Constructor (Special method that runs when object is created)
    def __init__(self,brand,model):
        self.brand = brand # Instance Varible
        self.model = model # Instance Varible

    # Instance method(Work with object data)
    def show_info(self):
        return f"car: {self.brand} {self.model}"

# CReating objects (Instance)
car1 =car("Toyota","BMW")
car2 = car("Lambo","Porche")

print(car1.show_info())  # car: Toyota BMW
print(car2.show_info())  # car: Lambo Porche

