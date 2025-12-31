# Write a function that reads a JSON file and extracts specific information from it

import json

try:
    filename = input("Enter JSON file name: ")

    with open(filename, "r") as f:
        data = json.loads(f.read())

    print("Name:", data["name"])
    print("Age:", data["age"])

except FileNotFoundError:
    print("File not found")
except KeyError:
    print("Missing key")
