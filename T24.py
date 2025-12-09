# Create a program that generates the Fibonacci sequence up to a given number of terms)

n = int(input("Enter number of terms: "))

a, b = 0, 1

if n <= 0:
    print("Enter a positive number")
else:
    print("Fibonacci sequence:")
    for i in range(n):
        print(a, end=" ")
        a, b = b, a + b
