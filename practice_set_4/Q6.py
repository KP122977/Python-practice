# Given a JSON file with customer data, create a Customer class to store and manipulate the data.

import json
class Customer:
    def __init__(self,name,age,city):
        self.name=name
        self.age=age
        self.city=city
    
try:
    filename=input('Enter a json file name : ')
    with open(filename,'r') as f:
        reads=json.load(f)
        customer=Customer(reads['name'],reads['age'],reads['city'])
        print(f'customer  name : {customer.name} , age : {customer.age} , city : {customer.city} ')
        
except FileNotFoundError:
    print('file not found ')
except KeyError:
    print('Invalid JSON structure')
        
        
