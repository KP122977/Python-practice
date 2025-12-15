# Create a program that takes a temperature in Celsius and converts it to Kelvin.
try:
    
    cel=float(input("enter celcius : "))
    kelvin=cel+273.15
    print(kelvin)
except ValueError:
    print("invalid input ,please enter float input only")