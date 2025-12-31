# Given a JSON file with product details (name, price, quantity), create a Product class with encapsulated attributes.

class Product:
    def __init__(self,name,price,quantity):
        self.__name=name
        self.__price=price
        self.__quantity=quantity
        
    def show(self):
        return f'name pf the product : {self.__name}'
    
try :
    name=input("enter name of the product : ")
    price=int(input("enter price of the product : "))
    quantity=int(input('enter quanity of the product :  '))
    
    product_details=Product(name,price,quantity)
    print(product_details.show())
    
    
except ValueError as e:
    print(e)