# Implement a program that prints the multiplication table of a given number

num=int(input("enter a num : "))
for i in range(1,11):
    multi=i*num
    print(f"{num}*{i} = {multi}")
    
    