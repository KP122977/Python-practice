# Implement a function that takes a list of numbers and returns a new list with the squared values

list=[1,2,3,4,5,6,7,8]
sqr_list=[]

for i in list:
    if i>=0:
        i=i*i
    sqr_list.append(i)
print(sqr_list)