# Create a function to reverse a given string

def rev():
    word=input("enter a string to reverse ")
    
    s=word.replace(" ","")
    rev=""
    for ch in s:
        rev= ch+rev
    print(rev)

rev()
    