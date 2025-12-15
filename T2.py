# Create a program that takes a user's name and age as input and prints a greeting message
try:
    
    name=input("enter your name : ")
    age=int(input("enter your age : "))
    print(f"welcome {name} !,your age is {age}")
except ValueError:
    print("invalid input ,please enter proper input only")