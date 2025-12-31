# Given a text file with a list of numbers, write a function that finds the sum of all numbers in the file


try:
    filename = input("Enter CSV file name: ")

    with open(filename, "r") as f:
        lines = f.readlines()

    sum=0

    for line in lines[1:]:      
        num=line.strip()
        sum+=int(num)

    
    print("sum of the numbers : ", sum)

except FileNotFoundError:
    print("File not found")
except ValueError:
    print("Invalid score")
