my_str='SPAM AND EGGS'

def return_hello(name):
    say="Hello "+ name
    return say
    
class spam :
    eggs=42
    def describe_meal(self):
        egg_str=str(self.eggs)+' eggs'
        return 'SPAM AND '+ egg_str 
c=spam()
print(c.describe_meal())
print(return_hello('krish'))


def sum_subtract(a, b, operation="sum"):
    """
    Return sum or difference between the numbers 'a' and 'b'.
    The type of operation is defined by the 'operation' argument.
    If the operation is not supported, print 'Incorrect operation.'
    """
    if operation == "sum":
        return a + b
    elif operation == "subtract":
        return a - b
    else:
        print("Incorrect operation.")
        
print(help(sum_subtract))