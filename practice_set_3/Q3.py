# Implement a program that reads a text file and counts the number of words and lines in it



try:
    filename = input("Enter CSV file name: ")

    with open(filename, "r") as f:
        row=f.readlines()
        

    lines=0
    words_count=0


    for line in row:
        lines +=1
        words=line.split()
        words_count += len(words)
    

    print("num of lines:", lines)
    print("num of words:", words_count)

except FileNotFoundError:
    print("File not found")
except ValueError:
    print("Invalid score")