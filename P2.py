# Write a program that finds the largest and smallest elements in a list

# by inbuilt max,min method
 
list=[1,2,7,4,9,10]

maximum=max(list)
minimum=min(list)

print('maximum :' ,maximum)
print('minimum : ',minimum)



# by loop 

list=[1,2,3,8,9,10]

max_val=list[0]
min_val=list[0]

for i in list:
    if i>max_val:
        max_val=i
    if i<min_val:
        min_val=i
        
print('maximum :' ,max_val)
print('minimum : ',min_val)