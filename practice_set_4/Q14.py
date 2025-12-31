# Create a class hierarchy to represent different types of animals (Birds, Fish) with their attributes and methods.


class Animal:
    def __init__(self):
        pass
    
class Bird(Animal):

        
    def move(self):
        print('birds can fly')
        
class Fish(Animal):
    
        
    def move(self):
        print('Fish can swim')
    
    
b=Bird()
b.move()
f=Fish()
f.move()