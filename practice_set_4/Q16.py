# Implement a program that uses inheritance to represent a hierarchy of vehicles (Car, Bike, Truck, etc.)

class Vehicles:
    def __init__(self):
        pass
    
class Car(Vehicles):
    def info(self):
        print('i have four wheels')
        
class Bike(Vehicles):
    def info(self):
        print('i have 2 wheels')

class Truck(Vehicles):
    def info(self):
        print('i have 10 wheels')
        
