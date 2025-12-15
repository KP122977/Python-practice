a=[1,2,3]
print(id(a))
a.append(4)
print(a)
print(id(a))  


b=(1,2,3)
print(id(b))
b=b+(4,)
print(b)
print(id(b))

a={1,2,3,4}
print(id(a))
b={5,6,7,8}
a.update(b)
print(a)
print(id(a))