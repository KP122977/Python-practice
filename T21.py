# Create a program that takes a year as input and checks if it is a leap year or not

year=int(input("enter a year : "))

if year>0:
    if year%4==0 and year%100!=0 or year%400==0:
        print(year,"is leap year")
    else:
        print(year,"is not a leap year")
