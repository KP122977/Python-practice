# Write a Python program to check if a given number is a prime number

num=int(input("enter a number : "))
if num<=0:
    print("not a prime numebr")
else:
    for i in range(2,num):
        if num%i==0:
            print("this is not a prime number")
            break
    else:
        print("this is a prime numebr")
         