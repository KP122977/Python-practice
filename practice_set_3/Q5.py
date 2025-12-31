# Given a CSV file with employee details (name, age, salary), calculate the average salary of all employees


try:
    filename = input("Enter CSV file name: ")

    with open(filename, "r") as f:
        lines = f.readlines()

    salary_sum = 0
    count = 0

    for line in lines[1:]:      
        name,age,salary= line.split(",")
        salary_sum +=int(salary)
        count+=1

    
    avg_salary=salary_sum/count
    print("avg salary :", avg_salary)

except FileNotFoundError:
    print("File not found")
except ValueError:
    print("Invalid score")
    