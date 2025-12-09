# Implement a program that swaps the values of two variables.

a = int(input("Enter value for a : "))
b = int(input("Enter value for b : "))

temp = a
a = b
b = temp

print("After swapping : ")
print("a : ", a)
print("b : ", b)
