# Create a program that checks if two sets have any elements in common

#  by inbuilt intersection method
set1={1,2,3,4,5}
set2={6,7,8}

if set1.intersection(set2):
    print("both sets have some common values")
else:
    print("both sets have unique values")
    
# by & method

set1={1,2,3,4,5}
set2={4,5,6,7,8}

if set1 & set2:
    print("both sets have some common values")
else:
    print("both sets have unique values")