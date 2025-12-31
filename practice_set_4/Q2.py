# Given a CSV file with employee details (name, position, salary), create a class to represent an employee.

class Employee:
    def __init__(self,name,position,salary):
        self.name=name
        self.position =position
        self.salary=salary
        
    
try:
    employee=[]
    filename=input('enter a file name : ')
    with open(filename,'r') as f:
        reads=f.readlines()
        
    for line in reads[1:]:
        name, position, salary = line.split(',')
        employee.append(Employee(name, position, salary))
        
    for p in employee:
        print(f'employee name : {p.name}, position : {p.position}, salary : {p.salary}')
except FileNotFoundError:
    print("File doesn't exist")


