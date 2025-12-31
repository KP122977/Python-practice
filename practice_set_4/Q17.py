# Write a Python program that uses encapsulation to protect sensitive information in a User class.

class User:
    def __init__(self, username, password):
        self.username = username
        self.__password = password

    def check_password(self, pwd):
        return pwd == self.__password

try :
    username=input("enter username  : ")
    my_pass=int(input("enter password : "))
    org_pass=int(input('enter original password : '))
    
    password_check=User(username,my_pass)
    print(password_check.check_password(org_pass))
    
    
except ValueError as e:
    print(e)