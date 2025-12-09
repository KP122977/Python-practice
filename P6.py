# Write a Python program to count the occurrences of each element in a given list

list=[1,2,2,3,4,5,5]

dict={}
for i in list:
    if i in dict:
        dict[i]+=1
    else:
        dict[i]=1
print(dict)