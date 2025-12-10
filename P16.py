# Write a Python program that counts the number of occurrences of each character in a given string using a dictionary

s = input("Enter a string: ")

char = {}

for ch in s:
    if ch in char:
        char[ch] += 1
    else:
        char[ch] = 1


print(char)

max = max(char, key=char.get)
print("maximum accurance : ",max)

