# Implement a program that swaps the values of two variables.

try:
    a = int(input("Enter value for a: "))
    b = int(input("Enter value for b: "))

    
    temp = a
    a = b
    b = temp

    print("After swapping:")
    print("a:", a)
    print("b:", b)

except ValueError:
    print("Invalid input! Please enter only integers.")


# method 2

a,b=b,a
print('a',a)
print('b',b)