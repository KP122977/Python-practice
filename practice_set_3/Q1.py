# Write a Python program to copy the contents of one text file into another

try:
    source = input("enter source file name: ")
    destination = input("enter destination file name: ")

    with open(source, "r") as file1:
        content = file1.read()

    with open(destination, "w") as file2:
        file2.write(content)

    print("File copied successfully")

except FileNotFoundError:
    print("source file not found")
