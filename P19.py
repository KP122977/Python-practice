# Write a program that finds the average value of all the elements in a list of dictionaries

list=[
    {'name':'krish','age':40},
    {'name':'tanish','age':28},
    {'name':'paraj','age':32},
]

avg=sum(i['age'] for i in list)/len(list)

print("avg age : ",avg)