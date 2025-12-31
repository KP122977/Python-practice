# Given a CSV file with product details (name, price, quantity), create a Product class to manage the data.

class Products:
    def __init__(self,name,price,quantity):
        self.name=name
        self.price=price
        self.quantity=quantity        
    
try:
    products=[]
    filename=input('enter a file name : ')
    with open(filename,'r') as f:
        reads=f.readlines()
        
    for line in reads[1:]:
        name, price,quantity = line.strip().split(',')
        products.append(Products(name, price ,quantity))
        
    for p in products:
        print(f'Product name {p.name}, price {p.price}, quantity {p.quantity}')
except FileNotFoundError:
    print("File doesn't exist")



