# Given a list of integers, find all the even numbers and store them in a new list)

list=[1,2,3,4,5,6,7,8,9,10]
eve_list=[]
for i in list:
    if i%2==0:
        eve_list.append(i)
        
print(eve_list)