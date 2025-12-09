# Write a Python program to check if a given string is a pangram (contains all letters of the alphabet)
import string
import re

def pangram():
    s=input("enter a sentence : ")
    # s=s.lower()
    pan=re.findall(r"[a-z]",s.lower())
    unique=set(pan)
    return unique==set(string.ascii_lowercase)

print(pangram())