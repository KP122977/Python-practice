# Create a base class Shape with methods to calculate area and perimeter and derive classes Circle and Square.

class Shape:
    def __init__(self):
        pass
    
class Circle(Shape):
    def __init__(self,radius):
        self.radius=radius
        
    def area(self):
        return f'Area of a circle is {3.14*self.radius*self.radius}'
    
    def perimeter(self):
        return f'perimeter of circle is {2*3.14*self.radius}'
    
class Square(Shape):
    def __init__(self,sides):
        self.sides=sides
        
    def area(self):
        return f'Area of a square is {self.sides*self.sides}'
    
    def perimeter(self):
        return f'perimeter of square is {4*self.sides}'
    
try:
    radius=int(input('enter radius of circle : '))
    sides=int(input('enter sides of square : '))
    
    circle=Circle(radius)
    print(circle.area)
    print(circle.perimeter)
    
    square=Square(sides)
    print(square.area)
    print(square.perimeter)
    
    
except ValueError as e:
    print(e)