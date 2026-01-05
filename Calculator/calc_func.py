# =============> create function based script here

def add(a, b):
    return f"Addition of {a} + {b} = {a + b}"


def subtract(a, b):
    return f"Subtraction of {a} - {b} = {a - b}"


def multiply(a, b):
    return f"Multiplication of {a} * {b} = {a * b}"


def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Division by zero is not allowed")
    return f"Division of {a} / {b} = {a / b}"


try:
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
            print("Please enter a valid choice")
            continue

        
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))

        if choice == "1":
            print(add(a, b))

        elif choice == "2":
            print(subtract(a, b))

        elif choice == "3":
            print(multiply(a, b))

        elif choice == "4":
            print(divide(a, b))

except ValueError:
    print("Please enter valid numeric input")

except ZeroDivisionError as e:
    print(e)
