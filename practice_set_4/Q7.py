# Write a program that uses a Person class to keep track of a person's name, age, and address.

class Person :
    def __init__(self,name,age,address):
        self.name=name
        self.age=age
        self.address=address
    
    def display(self):
        return f'name of person : {self.name} , age of person : {self.age} , address : {self.address}'
    
try:
    name = input("Enter person's  name : ")
    age= int(input("Enter person's age : "))
    address=input("Enter person's address : ")
    person_details = Person(name,age,address)
    print(person_details.display())
    
except ValueError as e:
    print(e)