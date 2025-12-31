# Implement a class hierarchy to represent different types of employees (Manager, Engineer) with their attributes.

class Employee:
    def __init__(self,company_name):
        self.company_name=company_name
    
class Manager(Employee):
    def __init__(self,company_name,role):
        super().__init__(company_name)
        self.role=role
        
    def show(self):
        return f'i have joined {self.company_name} as {self.role}'
    
class Engineer(Employee):
    def __init__(self,company_name,role):
        super().__init__(company_name)
        self.role=role
        
    def show(self):
        return f'i have joined {self.company_name} as {self.role}'
    

try:
    company_name=input('enter name of the company : ')
    role=input('enter your role : ')
    
    
    manager=Manager(company_name,role)
    print(manager.show())
    
    
   
    
    
except ValueError as e:
    print(e)