# import collections

# s = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
# d = collections.defaultdict(list)
# for k, v in s:
#     d[k].append(v)

# print(d["blue"])
# sorted(d.items())

# from collections import deque

# d = deque('ghi')                 # make a new deque with three items
# print("Iterating over deque: \n")
# for elem in d:                   # iterate over the deque's elements
#     print(elem.upper(), end=' ')



# d.append('j')                    # add a new entry to the right side
# print(f"\nd.append('j'): {d}\n")
# d.appendleft('f')                # add a new entry to the left side
# print(f"\nd.appendleft('j'): {d}\n")                                # show the representation of the deque


# d.pop()                          # return and remove the rightmost item
# print(f"\nd.pop(): {d}\n")
# d.popleft()                      # return and remove the leftmost item
# print(f"\nd.popleft(): {list(d)}\n")  # list the contents of the deque
                          

# print(f"\nd[0]: {d[0]}\n")                             # peek at leftmost item

# print(f"\nd[0]: {d[-1]}\n")                            # peek at rightmost item


# print(f"\nlist(reversed(d)): {list(reversed(d))}\n")                # list the contents of a deque in reverse

# print(f'\n"h" in d: {"h" in d}\n')                                # search the deque

# print(f"\nd.extend('jkl'): {d.extend('jkl')}\n")                  # add multiple elements at once

# print(d)
# print(f"\nd.rotate(1): {d.rotate(1)}\n")                      # right rotation
# print(d)

# print(f"\nd.rotate(-1): {d.rotate(-1)}\n")                     # left rotation
# print(d)


# print(f"\ndeque(reversed(d)): {deque(reversed(d))}\n")               # make a new deque in reverse order

# print(f"\nd.clear(): {d.clear()}\n")  # empty the deque
# try:
    
#     print(f"\nd.pop(): {d.pop()}\n") 
# except IndexError :
#     print("empty deque can't pop")        
    
    
    
from collections import ChainMap 
a = {'x': 1, 'z': 2} 
b = {'y': 3, 'z': 4} 
c = ChainMap(a, b)
print(c['y'])
print(c)
# del c['y']
print(list(c))

# a={'x':1}
# b={'z':2}
# c=ChainMap(a,b)
# print(c)
# del c['z']
# print(c)