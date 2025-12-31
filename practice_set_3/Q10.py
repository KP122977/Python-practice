# Given a CSV file with temperature data for each day of the week, find the average temperature for each day.


try:
    filename = input("Enter CSV file name: ")

    with open(filename, "r") as f:
        lines = f.readlines()

    total_temp = 0
    count = 0

    for line in lines[1:]:      
        day,temperature= line.split(",")
        total_temp +=float(temperature)
        count+=1

    
    avg_temp=total_temp/count
    print("avg salary :", avg_temp)

except FileNotFoundError:
    print("File not found")
except ValueError:
    print("Invalid score")
    