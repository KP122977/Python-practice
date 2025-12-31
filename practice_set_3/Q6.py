# Write a program that reads a CSV file and finds the total sales revenue for a specific product


try:
    filename = input("Enter CSV file name: ")

    with open(filename, "r") as f:
        lines = f.readlines()

    product_name='orange'
    total_sales=0

    for line in lines[1:]:      
        product,price,sales=line.split(',')
    
        if product==product_name:
            total_sales+=int(price)*int(sales)

    
    
    print(f'total sales revenue of {product_name} is {total_sales}')

except FileNotFoundError:
    print("File not found")
except ValueError:
    print("Invalid score")