# Calculate the compound interest for a given principal amount, interest rate, and time period

P=1000
R=5
T=2

print("compound interest : ",(P*(1+R/100)**T)-P)
print("total amount after interest : ",P*(1+R/100)**T)