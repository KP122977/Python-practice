# Implement a program that simulates a basic bank account using a BankAccount class.

class BankAccount:
    def __init__(self,user,balance):
        self.user=user
        self.balance=balance
        
        
    def deposite(self,amount):
        if amount<0:
            raise ValueError("amount should be in positive numbers")
        self.balance+=amount
        return f'updated balance {self.balance}'
        
    def withdraw(self,amount):
        if amount>self.balance:
            raise ValueError('non withdrawable amount')
        self.balance-=amount
        return f'updated balance {self.balance}'
    

try:
    name = input("Enter account holder name: ")
    balance = int(input("Enter initial balance: "))
    acc = BankAccount(name, balance)

    amount = int(input("Enter deposit amount: "))
    acc.deposite(amount)

    amount = int(input("Enter withdrawal amount: "))
    acc.withdraw(amount)

    print("Final Balance:", acc.balance)

except ValueError as e:
    print(e)
        