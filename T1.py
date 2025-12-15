# Write a Python program to calculate the area of a rectangle given its length and width


try:
    length = int(input("Enter length of rectangle: "))
    width = int(input("Enter width of rectangle: "))

    area = length * width
    print("area of rectangle is: ", area)

except ValueError:
    print("invalid input ,please enter numeric values only")
