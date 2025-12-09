# Create a Python function to check if a given string is a palindrome

# using loop

def palindrome(s):
    s = s.lower().replace(" ", "")
    rev = ""
    for char in s:
        rev = char + rev   

    return s == rev

print(palindrome("krish"))
print(palindrome("madam"))

# using slicing

def palindrome(s):
    s=s.lower().replace(" ","")
    rev=s[::-1]
    if s==rev:
        print("given string in palindrome")
    else:
        print("given string is not palindrome")

print(palindrome("ABBA"))


    