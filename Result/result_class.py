class Student:
    def __init__(self):
        self.marks = []

    def add_mark(self, mark):
        if mark < 0 or mark > 70:
            raise ValueError
        self.marks.append(mark)

    def get_result(self):
        for mark in self.marks:
            if mark < 23:
                return "Fail"
        return "Pass"


try:
    print("Enter marks for 5 subjects (out of 70)")

    student = Student()

    student.add_mark(int(input("Enter marks for subject 1: ")))
    student.add_mark(int(input("Enter marks for subject 2: ")))
    student.add_mark(int(input("Enter marks for subject 3: ")))
    student.add_mark(int(input("Enter marks for subject 4: ")))
    student.add_mark(int(input("Enter marks for subject 5: ")))

    print("Result:", student.get_result())

except ValueError:
    print("Invalid marks entered (must be between 0 and 70)")
