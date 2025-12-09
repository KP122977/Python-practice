# Concatenate a list of names into a single string separated by spaces.

# using join

list=["krish","is","an","AI","Engineer"]

string=" ".join(list)

print(string)


# by loop

list=["krish","is","an","AI","Engineer"]
result=" "
for i in list:
    result+=" "+i
    
print(result)