try:
    print("Enter marks for 5 subjects (out of 70)")

    marks = []

    mark1 = int(input("Enter marks for subject 1: "))
    if mark1 < 0 or mark1 > 70:
        raise ValueError
    marks.append(mark1)

    mark2 = int(input("Enter marks for subject 2: "))
    if mark2 < 0 or mark2 > 70:
        raise ValueError
    marks.append(mark2)

    mark3 = int(input("Enter marks for subject 3: "))
    if mark3 < 0 or mark3 > 70:
        raise ValueError
    marks.append(mark3)

    mark4 = int(input("Enter marks for subject 4: "))
    if mark4 < 0 or mark4 > 70:
        raise ValueError
    marks.append(mark4)

    mark5 = int(input("Enter marks for subject 5: "))
    if mark5 < 0 or mark5 > 70:
        raise ValueError
    marks.append(mark5)


    result = "Pass"
    for mark in marks:
        if mark < 23:
            result = "Fail"
            break

    print("Result:", result)

except ValueError:
    print("Invalid marks entered (must be between 0 and 70)")
