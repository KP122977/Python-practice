# Write a program that calculates the factorial of a given number

num=int(input("enter a number : "))
fact=1
if num<0:
    print("enter a positive numer")
else:
    for i in range(1,num+1):
        fact*=i
    print(fact)
    
    