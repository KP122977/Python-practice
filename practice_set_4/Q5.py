# Create a class representing a Car with attributes like make, model, and year.

class Car:
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year
        
    def show(self):
        return f"car is made by {self.make} , model {self.model} and year is {self.year}"
    
    
try:
    make = input("Enter car's maker : ")
    model= input("Enter car's model : ")
    year=int(input("Enter car's buying year : "))
    car_details = Car(make,model,year)
    print(car_details.show())
    
except ValueError as e:
    print(e)