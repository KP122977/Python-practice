# Write a Python program that uses a Rectangle class to calculate the area and perimeter of a rectangle

class Rectangle :
    def __init__(self,length,width):
        self.length=length
        self.width=width
        
    def area(self):
        area=self.length*self.width
        print("area of rectangle is : ",area)
        
    def perimeter(self):
        perimeter=2*(self.length+self.width)
        print("perimeter of rectangle is : ",perimeter)
        
try:
    length = int(input("Enter length: "))
    width= int(input("Enter width: "))
    rectangle = Rectangle(length, width)

    rectangle.area()
    rectangle.perimeter()

except ValueError:
    print("Invalid input")