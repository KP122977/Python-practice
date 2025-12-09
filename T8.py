# Given a list of integers, find the sum of all positive numbers

list=[1,2,-3,-4,5,6,-7,8,9,-10,-11,12,13,14,-15]
sum=0
for i in list:
    if i>=0:
        sum+=i
    else:
        continue
print(sum)