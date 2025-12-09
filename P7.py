# Given a list of names, remove all duplicate names and print the unique names

list=['krish','tanish','krish','paraj','jigar']
unique=[]

for i in list:
    if i not in unique:
        unique.append(i)
    
print(unique)
        