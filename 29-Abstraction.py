# # Abstraction = Hinding implemenatation details, showing only essential features.
# # Done using abstraction base class (ABC)

from abc import ABC, abstractmethod

class Shape(ABC):  # Abstract class
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):  
    def __init__(self, w, h):
        self.w = w
        self.h = h
    
    def area(self):
        return self.w * self.h

class Circle(Shape):
    def __init__(self, r):
        self.r = r

    def area(self):
        return 3.14 * self.r * self.r

shapes = [Rectangle(5, 10), Circle(7)]

for s in shapes:  
    print(s.area())  # Output: 50 , 153.86


