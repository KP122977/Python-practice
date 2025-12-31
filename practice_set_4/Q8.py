# Implement a program that uses a Circle class to calculate the area and circumference of multiple circles3

class Circle :
    def __init__(self,radius):
        self.radius=radius
        
    def area(self):
        return f'Area of a circle is {3.14*self.radius*self.radius}'
    
    def circumference(self):
        return f'Circumference of circle is {2*3.14*self.radius}'
    
try:
    n = int(input(" number of circle's details you want : "))
    for i in range(n):
        radius = int(input("Enter radius: "))
        circle = Circle(radius)
        print("Area:", circle.area(), "Circumference:", circle.circumference())

except ValueError:
    print("Invalid input")
