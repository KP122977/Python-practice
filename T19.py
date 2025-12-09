# Create a function to count the number of vowels in a given string

def count_vowel():
    s=input("enter a string : ")
    vowels='aeiou'
    count=0
    for i in s:
        if i in vowels:
            count+=1
    print(count)

count_vowel()