# Implement a program that converts a given number of minutes into hours and minutes

minutes=int(input("enter num of minutes : "))

hour=minutes//60
rem_min=minutes%60

print("Hours : ",hour)
print("Minutes : ",rem_min)