# # Oops


# class MyClass:
#     a = "abc"
#     b = "def"
    
# obj =MyClass()
# print(obj.a)
# print(obj.b)

# obj1=MyClass()
# obj1.a='absbjs'
# print(obj1.a)
# print(obj.a)




# class Student:
#     college = "ABC University"   # class attribute

# s1 = Student()
# s2 = Student()

# s1.college = "XYZ University"   # instance attribute

# print(s1.college)
# print(s2.college)



class A:
    def method_a(self):
        print(f"memory addr of obj in A: {id(self)}")
        print("method_a from A")

    def method_b(self):
        self.method_a()

class B(A):
    def method_a(self):
        print(f"memory addr of obj in B: {id(self)}")
        print("method_a from B")
        # A.method_a(self)
        super().method_a()
        
b=B()
b.method_a()
print(isinstance(b,A))
print(issubclass(A,B))
print(issubclass(B,A))



# class Employee:

#     num_of_emps = 0          # Always same for all the instances of class
#     raise_amount = 1.04      # May differ from employee to employee

#     def __init__(self, first_name, last_name, salary):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.salary = salary
# #         self.email = first_name + '.' + last_name + "@reversebits.com"

#         Employee.num_of_emps +=  1


class Employee:

    num_of_emps = 0          # Always same for all the instances of class
    raise_amount = 1.04      # May differ from employee to employee

    def __init__(self, first_name, last_name, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary
        self.email = first_name + '.' + last_name + "@reversebits.com"

        Employee.num_of_emps +=  1


    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def apply_raise(self):
        print(f"Raising the salary with amount: {self.raise_amount}")
        self.salary = int(self.salary*self.raise_amount)

    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount

    @classmethod
    def from_string(cls, string):
        first_name, last_name, salary = string.split('-')
        return cls(first_name, last_name, int(salary))

    @staticmethod
    def is_weekend(day):
        
        return day.weekday() == 5 or day.weekday() == 6
    
import datetime

my_date = datetime.date(2020, 1, 12)

print(Employee.is_weekend(my_date))


# #     def full_name(self):
# #         return f"{self.first_name} {self.last_name}"

#     def apply_raise(self):
#         print(f"Raising the salary with amount: {self.raise_amount}")
#         self.salary = int(self.salary*self.raise_amount)

#     @classmethod
#     def set_raise_amount(cls, amount):
#         cls.raise_amount = amount

#     @classmethod
#     def from_string(cls, string):
#         first_name, last_name, salary = string.split('-')
#         return cls(first_name, last_name, int(salary))

#     @staticmethod
#     def is_weekend(day):
#         return day.weekday() == 5 or day.weekday() == 6

#     def __repr__(self):
#         return f"Employee('{self.first_name}', '{self.last_name}', {self.salary})"

#     def __str__(self):
#         return f"{self.full_name()} : {self.email}"

#     def __add__(self, other):
#         return self.salary + other.salary

#     @property
#     def email(self):
#         return f"{self.first_name}.{self.last_name}@reversebits.com"

#     @property
#     def full_name(self):
#         return f"{self.first_name} {self.last_name}"

#     @full_name.setter
#     def full_name(self, name):
#         self.first_name, self.last_name = name.split(" ")

#     @full_name.deleter
#     def full_name(self):
#         print("You just deleted the name of employee!!!")
#         self.first_name = None
#         self.last_name = None
# emp_1 = Employee("Jerry", "Mouse", 60000)
# print(emp_1.email)
# emp_1.full_name = "Tom Cat"
# print(emp_1.full_name)
# print(emp_1.email)
# # del emp_1.full_name


# class Rectangle:
#     def __init__(self, l, w):
#         self.l = l
#         self.w = w

#     # @property
#     def area(self):
#         return self.l * self.w
# r = Rectangle(4, 5)
# print(r.area)
