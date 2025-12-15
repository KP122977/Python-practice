# Given a list of numbers, create a function to find the sum of all positive numbers.

def sum_positive(list):
    try:
        sum=0
        for i in list:
            if i>=0:
                sum+=i
            else:
                continue
        print(sum)
    except ValueError:
        print("invalid input ,please enter integer input only")
    
sum_positive([1,2,-3,-4,5,6,-7,8,9,-10,-11,12,13,14,-15])
