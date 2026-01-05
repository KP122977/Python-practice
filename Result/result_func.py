def validate_mark(mark):
    if mark < 0 or mark > 70:
        raise ValueError
    return mark


def calculate_result(marks):
    for mark in marks:
        if mark < 23:
            return "Fail"
    return "Pass"


try:
    print("Enter marks for 5 subjects (out of 70)")

    marks = []

    marks.append(validate_mark(int(input("Enter marks for subject 1: "))))
    marks.append(validate_mark(int(input("Enter marks for subject 2: "))))
    marks.append(validate_mark(int(input("Enter marks for subject 3: "))))
    marks.append(validate_mark(int(input("Enter marks for subject 4: "))))
    marks.append(validate_mark(int(input("Enter marks for subject 5: "))))

    result = calculate_result(marks)
    print("Result:", result)

except ValueError:
    print("Invalid marks entered (must be between 0 and 70)")
