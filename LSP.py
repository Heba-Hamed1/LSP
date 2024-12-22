#Remarks on the LSP
#his violates the LSP
class Shape:
    def area(self):
        pass

class Rectangle(Shape):
    def area(self, width, height):
        return width * height

class Square(Rectangle):
    def area(self, side):
        return side * side  
   
    
# how we can solve using LSP
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side **2
shapes = [
    Rectangle(7,8),
    Square(5)
]

for shape in shapes:
    print(f"Area: {shape.area()}")
