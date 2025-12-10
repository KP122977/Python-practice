# Create a function that takes a list of dictionaries and sorts them based on a specified key

list=[
    {'name':'krish','age':20},
    {'name':'tanish','age':21},
    {'name':'paraj','age':19},
]

def sort_dicts(list, key):
    list.sort(key=lambda x: x[key])
    print(list)

sort_dicts(list,'age')