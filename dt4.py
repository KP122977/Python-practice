d={1:'hetvi',2:'patoliya',1:'1',True:'2'}
print(d)


a={1,0,10,True,False,()}
print(a)



s = 'foo'
print(id(s))
s += 'bar'
print(s) # foobar
print(id(s))


x = 'foo'
y = x
print(x) # foo
y += 'bar'
print (x)# foo

x = [1, 2, 3]
y = x
print (x) # [1, 2, 3]
y += [3, 2, 1]
print (x)# [1, 2, 3, 3, 2, 1]

