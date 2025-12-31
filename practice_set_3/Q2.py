# Given a CSV file with student names and scores, find the student with the highest score

try:
    filename = input("Enter CSV file name: ")

    with open(filename, "r") as f:
        lines = f.readlines()

    max_score = 0
    top_student = ""

    for line in lines[1:]:      
        name, score = line.split(",")
        score = int(score)

        if score > max_score:
            max_score = score
            top_student = name

    print("Top Student:", top_student)
    print("Highest Score:", max_score)

except FileNotFoundError:
    print("File not found")
except ValueError:
    print("Invalid score")
