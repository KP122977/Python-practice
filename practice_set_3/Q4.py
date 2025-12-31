# Create a function that takes a list of sentences and writes them to a new text file, each on a new line


try:
    n = int(input("number of sentences you want to write : "))
    filename = input("enter output file name : ")

    with open(filename, "w") as f:
        for i in range(n):
            sentence = input("Enter sentence: ")
            f.write(sentence + "\n")

    print("data written successfully")

except ValueError:
    print("Invalid input")
