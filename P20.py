# Implement a function that takes a list of strings and returns a set of unique characters in all strings.

list=['krish','tanish','paraj']

def unique_char(list):
    char = set()
    
    for s in list:
        for ch in s:
            char.add(ch)
    
    print(char)

unique_char(list)