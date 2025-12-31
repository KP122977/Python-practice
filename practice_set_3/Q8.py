# Implement a program that reads a CSV file and generates a bar chart to represent the data using matplotlib

import matplotlib.pyplot as plt

try:
    filename = input("Enter CSV file name: ")

    with open(filename, "r") as file:
        data = file.read()

    lines = data.splitlines()

    products = []
    sales = []

    for line in lines[1:]:            
        parts = line.split(",")
        product = parts[0]
        sale = int(parts[2])

        products.append(product)
        sales.append(sale)

    plt.bar(products, sales)
    plt.xlabel("Products")
    plt.ylabel("Sales")
    plt.title("Product Sales Chart")
    plt.show()

except FileNotFoundError:
    print("File not found")
except ValueError:
    print("Invalid sales value in file")

