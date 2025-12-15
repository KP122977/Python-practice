# Write a program that converts a given number of days into years, weeks, and days
try:
    days=int(input("Enter number of days : " ))

    years=days//365
    rem_days=days%365

    months=rem_days//12
    rem_days=rem_days%12

    weeks=rem_days//7
    rem_days=rem_days%7

    print("years : ",years)
    print("months : ",months)
    print("weeks : ",weeks)
    print("days : ",rem_days)
except ValueError:
    print("invalid input ,please enter proper input only")