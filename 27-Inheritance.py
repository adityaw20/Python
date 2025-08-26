# INheritance allows a classs (child) to use featuresof another class (parent).

class vehicle:
    def __init__(self,brand):
        self.brand = brand
    
    def show_brand(self):
        print(f"brand : {self.brand}")

# Car class inherits vehicle
class car(vehicle):
    def __init__(self,brand,model):
        #Call parent constructor
        super().__init__(brand)
        self.model = model

    def show_details(self):
        print(f"Car : {self.brand}, Model :  {self.model}")

# Objects of child class 
car1 = car("BMW" , "Porche")
car1.show_brand()
car1.show_details()