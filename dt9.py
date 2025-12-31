#  collections

# import collections
# a = {'a': 1, 'b': 2, 'c': 3}
# b = {'c': 4, 'd': 5, 'e': 6}

# combined = collections.ChainMap(b, a)


# combined['c'] = 10
# print(list(combined))
# print(b['c'])

# for item in combined.items():
#     print(item)

# a = {'a': 1, 'b': 2, 'c': 3}
# b = {'c': 4, 'd': 5, 'e': 6}

# combined = collections.ChainMap(a, b)

# # print(list(combined))
# # print(combined['c'])


# combined['c'] = 10
# for item in combined.items():
#     print(item)
# print(a['c'])

# print(b['c'])

# print(combined.items())


# c = collections.Counter(['eggs', 'ham', 'eggs'])
# print(c['eggs'])



# cnt = collections.Counter()

# list_of_colors = ['red', 'blue', 'red', 'green', 'blue', 'blue'] 

# for word in list_of_colors:
#     cnt[word] += 1
# cnt


# # find the most common color in the list

# print(collections.Counter(list_of_colors).most_common(1))


# c = collections.Counter(a=2, b=4, c=0,d=-2)

# print(list(c.elements()))


# c = collections.Counter(a=4, b=2, c=0, d=2)
# d = collections.Counter(a=1, b=2, c=3, d=4, e=5)
# c.subtract(d)
# print(c)


# from itertools import dropwhile

# def should_drop(x):
#     return x < 1

# for i in dropwhile(should_drop, [-1, 0, 1, 2, -2]):
#     print(i, end=' ')
import collections

# c = collections.Counter({'red': 4, 'blue': 2})  
# print(c)

# c=collections.Counter('put anything in this').most_common(3)
# print(c)



# c = collections.ChainMap({'a': 1,'b': 2, 'c': 3})

# d = c.new_child({'d': 4,'e': 5, 'f': 6})

# print(d)
# print(d.new_child({'g': 'a', 'h': 'b', 'i': 'c'}))

# e = c.new_child({'j': 7,'k': 8,'l': 9})

# f = e.new_child()

# print(e.new_child())

# print(c)


# c = collections.Counter(a=2, b=4, c=0, d=-2)

# print(list(c.elements()))

c = collections.Counter(a=3, b=1)
d = collections.Counter(a=4, b=2,c=3)

print(f"c + d: {c + d}")                       # add two counters together:  c[x] + d[x]


print(f"c - d: {c - d}")                       # subtract (keeping only positive counts)


print(f"c & d: {c & d}")                       # intersection:  min(c[x], d[x]) 


print(f"c | d: {c | d}")  