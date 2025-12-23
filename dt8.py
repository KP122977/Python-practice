# # Encapsulation

# class BankAccount:
#     def __init__(self, balance):
#         self.__balance = balance   # private data

#     def deposit(self, amount):
#         if amount > 0:
#             self.__balance += amount

#     def get_balance(self):
#         return self.__balance
    
# acc = BankAccount(1000)
# acc.deposit(500)
# print(acc.get_balance())


# # Polymorphism

# class Dog:
#     def speak(self):
#         return "Bark"

# class Cat:
#     def speak(self):
#         return "Meow"
# animals = [Dog(), Cat()]

# for a in animals:
#     print(a.speak())


# # Abstract method

# from abc import ABC, abstractmethod

# class Shape(ABC):

#     @abstractmethod
#     def area(self):
#         pass
    
# class Rectangle(Shape):
#     def area(self):
#         return 10 * 5
    
# r = Rectangle()
# print(r.area())

# os

# import os
# print(dir(os))
# print(help(os))

# # globe

# import glob
# print(glob.glob('*.py'))

# # argparse 

# import argparse

# parser = argparse.ArgumentParser(
#     prog='top',
#     description='Show top lines from each file')
# parser.add_argument('filenames', nargs='+')
# parser.add_argument('-l', '--lines', type=int, default=10)
# args = parser.parse_args()
# print(args)


# from urllib.request import urlopen
# with urlopen('https://docs.python.org/3/') as response:
#     for line in response:
#         line = line.decode()             # Convert bytes to a str
#         if 'updated' in line:
#             print(line.rstrip())         # Remove trailing newline



# import smtplib
# server = smtplib.SMTP('localhost')
# server.sendmail('soothsayer@example.org', 'jcaesar@example.org',
# """To: jcaesar@example.org
# From: soothsayer@example.org

# Beware the Ides of March.
# """)
# server.quit()


# import zlib
# s = b'witch which has which witches wrist watch'
# print(len(s))
# # 41
# t = zlib.compress(s)
# print(t)
# print(len(t))
# # 37
# print(zlib.decompress(t))
# # b'witch which has which witches wrist watch'
# print(zlib.crc32(s))
# # 226805979


# from timeit import Timer
# Timer('t=a; a=b; b=t', 'a=1; b=2').timeit()
# # 0.57535828626024577
# Timer('a,b = b,a', 'a=1; b=2').timeit()
# # 0.54962537085770791



# generators

# def numbers(n):
#     for i in range(n):
#         yield i
# for num in numbers(10):
#     print(num)
    
    

# def numbers(n):
#     for i in range(n):
#         return i
        
# numbers(10)



#  decorators

def null_decorator(func):
    return func

@null_decorator
def greet():
    return 'Hello!'

print(greet())


def strong(func):
    def wrapper():
        return '<strong>' + func() + '</strong>'
    return wrapper

def emphasis(func):
    def wrapper():
        return '<em>' + func() + '</em>'
    return wrapper

@strong
@emphasis
def greet():
    return 'Hello!'

print(greet())