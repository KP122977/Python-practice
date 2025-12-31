# Write a Python program that uses inheritance to represent a hierarchy of shapes (Triangle, Rectangle, etc.)


class Shape:
    def __init__(self):
        pass
    
class Triangle(Shape):
    def __init__(self,base,side):
        super().__init__()
        self.base=base
        self.side=side
        
        
    def area(self):
        return f'are of  traiangle {0.5*self.base*self.side}'
        
        
class Rectangle(Shape):
    def __init__(self,length,width):
        super().__init__()
        self.length=length
        self.width=width
    
    def area(self):
        return f'area of rectengle {self.length*self.width}'
 
        

try:
    base=int(input('enter base of triangle : '))
    sides=int(input('enter sides of triangle : '))
    
    
    
    triangle=Triangle(base,sides)
    print(triangle.area())
    
    length = int(input("Enter length: "))
    width= int(input("Enter width: "))
    
    rectangle=Rectangle(length,width)
    print(rectangle.area())
    
    
    
except ValueError as e:
    print(e)



