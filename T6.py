# Calculate the compound interest for a given principal amount, interest rate, and time period
try:
    P=int(input("enter amount : "))
    R=int(input("enter interest rate : "))
    T=int(input("enter time period : "))

    print("compound interest : ",(P*(1+R/100)**T)-P)
    print("total amount after interest : ",P*(1+R/100)**T)
except ValueError:
    print("invalid input ,please enter integer input only")