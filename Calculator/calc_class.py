# ====> create a class function script here

class Calculator:
    def __init__(self):
        self.result = None   

    def add(self, a, b):
        self.result = a + b
        return f"Addition of {a} + {b} = {self.result}"

    def subtract(self, a, b):
        self.result = a - b
        return f"Subtraction of {a} - {b} = {self.result}"

    def multiply(self, a, b):
        self.result = a * b
        return f"Multiplication of {a} * {b} = {self.result}"

    def divide(self, a, b):
        if b == 0:
            raise ZeroDivisionError("Division by zero is not allowed")
        self.result = a / b
        return f"Division of {a} / {b} = {self.result}"


try:
    calculator = Calculator()  

    while True:
        print("\nCalculator Functionalities")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "5":
            print("Exiting calculator.")
            break

        if choice not in ("1", "2", "3", "4"):
            print("Invalid choice")
            continue

        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))

        if choice == "1":
            print(calculator.add(a, b))

        elif choice == "2":
            print(calculator.subtract(a, b))

        elif choice == "3":
            print(calculator.multiply(a, b))

        elif choice == "4":
            print(calculator.divide(a, b))

except ValueError:
    print("Please enter valid numeric input")

except ZeroDivisionError as e:
    print(e)
