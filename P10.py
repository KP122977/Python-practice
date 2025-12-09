# Implement a function that takes two lists and returns their union (all unique elements from both lists).


list1=[1,2,3,4,5,6,]
list2=[4,5,6,7,8,9]

# by loop


result = []
    
for i in list1:
    if i not in result:
        result.append(i)
    
for j in list2:
    if j not in result:
        result.append(j)
    
print(result)

# by converting to set

def list_union(list1, list2):
    return list(set(list1) | set(list2))


print(list_union([1, 2, 3], [3, 4, 5]))


