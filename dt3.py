

# a=10.0
# b=10
# print(a == b)


# a=10.0
# b=10
# print(a is b)


# a=407
# b=407
# print(a is b)


# a=100
# b=10
# print(a == b)


# a=10.0
# b=100.0
# print(a is b)


# a=100.0
# b=10.0
# print(a == b)

# a={1,2}
# b={2,1}
# print(a == b)

# a={1,2}
# b={2,1}
# print(a is b)

# a=(1,2)
# b=[1,2]
# print(a == b)

# a=[1,2]
# b=(1,2)
# print(a is b)


# a=1
# b='1'
# print(a == b)

# a,b=10,10.0
# print (a is b)
# a,b=10,10.0
# print (a == b)


# a_list = [34,  'sdg', '#dfs', '100', 407]
# b_list = [1, '#dfs', 'python', 'sdg', 407, 34]

# # checking 34
# print(f"a_list[0] is b_list[5]: {a_list[0] is b_list[5]}")

# # checking sdg
# print(f"a_list[1] is b_list[3]: {a_list[1] is b_list[3]}")

# # checking #dfs
# print(f"a_list[2] is b_list[1]: {a_list[2] is b_list[1]}")

# # checking 407
# print(f"a_list[4] is b_list[4]: {a_list[4] is b_list[4]}")

# a = 407
# b = 407

# print(a == b)   # True
# print(a is b)   # may be True (optimization)

# a = int("407")
# b = int("407")

# print(a == b)   # True
# print(a is b)   # ❌ False



# a=256
# b=256
# print(a is b)

# a=257
# b=257
# print(a is b)


# a = []
# b = []
# print(a is b)

# a = ()
# b = ()
# print(a is b)
# print(type(a))


# a = []
# b = []

# print("a is b:", a is b)
# print("id(a):", id(a))
# print("id(b):", id(b))

# a.append(100)

# print("After modifying a:")
# print("a:", a)
# print("b:", b)

a = tuple()
b = a
print(id(a))
print(id(b))

a = a + (10,)
print(id(a))
print(id(b))
print("a:", a)
print("b:", b)




# a = "hello world b hghggf gf gf zxcvbnmasdfghjklqwertyuiop!"
# b = "hello world b hghggf gf gfczxcvbnmasdfghjklqwertyuiop!"
# print(id(a))
# print(id(b))


# krish=400
# print(id(krish))
# krish+=100
# print(krish)
# print(id(krish))

# k=[400]
# print(id(k))
# k.append(100)
# print(k)
# print(id(k))


a=[1,2,3,4]
b=a
print(id(a))
print(id(b))
a.append([5,3,4])
a.append(6)
a.append(7)
print(a)
print(b)


a=1
b=a
print(id(a))
print(id(b))
