# Implement a program that checks if a given string is a palindrome

string="ABABABABA"
s=string.lower().replace(" ","")
rev=s[::-1]
if s==rev:
    print("string is palindrome")
else:
    print("string is not palindrome")