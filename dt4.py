# # d={1:'hetvi',2:'patoliya',1:'1',True:'2'}
# # print(d)


# # a={1,0,10,True,False,()}
# # print(a)



# # s = 'foo'
# # print(id(s))
# # s += 'bar'
# # print(s) # foobar
# # print(id(s))


# # x = 'foo'
# # y = x
# # print(x) # foo
# # y += 'bar'
# # print (x)# foo

# # x = [1, 2, 3]
# # y = x
# # print (x) # [1, 2, 3]
# # y += [3, 2, 1]
# # print (x)# [1, 2, 3, 3, 2, 1]

# # methods

# set={1,'a',2,3,4,(5,6,7)}
# set.add('added')
# print(set)
# set.update(['b',9,8,'false'])
# print(set)
# set.remove('added')
# set.discard('added')
# # set.remove('added')
# d = {'a': 1}
# d.update({'a': 10})
# print(d)


# list=[1,2,2,3,4]
# list.append([5,9]) 
# list.extend([6,7,8])
# list.insert(1,'inserted')
# list.remove(2)
# list.reverse()
# list.clear()
# # list.index(2)      # index of 3
# # list.count(2)     # 2
# print(list)


# s = "  Hello Python  "
# s.upper()        # '  HELLO PYTHON  '
# s.lower()        # '  hello python  '
# s.title()        # '  Hello Python  '
# s.capitalize()   # '  hello python  '
# s.strip()        # 'Hello Python'
# s.lstrip()       # 'Hello Python  '
# s.rstrip()       # '  Hello Python'
# s.find("Python")     # 8
# s.count("o")         # 2
# s.startswith("  H")  # True
# s.endswith("  ")     # True
# s.replace("Python", "Java")   # '  Hello Java  '
# s.split()                     # ['Hello', 'Python']


# t = (1, 2,2, 3, 2)
# t.count(2) # 3
# t.index(3) # 3


# d = {'a': 1, 'b': 2}
# d.get('a')        # 1
# d.get('x')        # None
# d.keys()          # dict_keys(['a','b'])
# d.values()        # dict_values([1,2])
# d.items()         # dict_items([('a',1),('b',2)])
# d.update({'c':3})   # {'a':1,'b':2,'c':3}
# print(d)
# d.pop('a')          # removes 'a'
# d.clear()           # {}


s="Hello"
print(id(s))
s = "J" + s[1:]
print(id(s))  # Jellow



# if []:
#     print("here")
# else:
#     print("there")
    
    
dict = {x: x*x for x in range(0, 10)}
set = {x*x for x in range(0,10)}
print(dict)
print(list(dict))
print(set)


# Source - https://stackoverflow.com/a
# Posted by Bite code, modified by community. See post 'Timeline' for change history
# Retrieved 2025-12-23, License - CC BY-SA 4.0

a = [1, 2]
b = [3, 4]
a.append(b)
print(a)
a.extend(b)
print(a)
# [1, 2, 3, 4]
