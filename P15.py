# Given a list of dictionaries, find the dictionary with the highest value for a specific key

list=[
    {'name':'krish','age':20},
    {'name':'tanish','age':21},
    {'name':'paraj','age':19},
]

max=list[0]

for i in list:
    if i['age'] > max['age']:
        max=i
    
print(max)