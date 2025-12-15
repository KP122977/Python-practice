# Create a program that takes a sentence as input and counts the number of words in it
try:
    sen=input("enter a sentence : ")

    word=sen.split(" ") 
    count=len(word)

    print(count)
except ValueError:
    print("invalid input ,please enter string  input only")