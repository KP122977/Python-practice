# Write a program that finds the most frequent element in a list

list=[1,2,2,3,4,5,6,6,6]

most_frequent = max(list, key=list.count)

print("Most frequent element:", most_frequent)
