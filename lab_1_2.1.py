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
 
class Triangle(Shape): 
    def __init__(self, base, height): 
        self.base = base 
        self.height = height 
 
    def area(self): 
        return 0.5 * self.base * self.height

a = int(input('значение 1:'))
b = int(input('значение 2:'))

rec = Rectangle(a, b)
tri = Triangle(a, b)

print(rec.area())
print(tri.area())