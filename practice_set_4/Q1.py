# Create a class representing a Student with attributes like name, age, and grades.

class Student:
    def __init__(self, name, age, grades):
        self.name = name
        self.age = age
        self.grades = grades
    
    def display(self):
        return f'my name is {self.name} , my age is {self.age}, I have got {self.grades} grade'   
        

try:
    name = input("Enter name : ")
    age = int(input("Enter age : "))
    grades = input("enter a grade :")

    student_details= Student(name, age, grades)
    print(student_details.display())
    

except ValueError:
    print("Invalid input")
