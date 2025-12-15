# Given a list of integers, find the sum of all positive numbers

try:
    elements=int(input("enter number of element you want to add : "))
    list=[]
    sum=0
    for i in range(elements):
        value=int(input("enter a element :"))
        list.append(value)

    else:
        for i in list:
            if i>=0:
                sum+=i
        
        print(sum)
except  ValueError:
    print("invalid input ,please enter integer input only")