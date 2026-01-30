# 1) CSV Reading/Writing
import csv

# Writing to CSV
with open("data.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Name", "Age", "City"])
    writer.writerow(["Ali", 23, "Multan"])
    writer.writerow(["Sara", 25, "Lahore"])

# Reading from CSV
with open("data.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

print("-" * 40)

# 2) TXT Handling
# Writing to TXT
with open("notes.txt", "w") as file:
    file.write("Python is easy!\n")
    file.write("File handling is easy.\n")

# Reading from TXT
with open("notes.txt", "r") as file:
    content = file.read()
    print(content)

print("-" * 40)

# 3) JSON Basics
import json

# Python dictionary
student = {"name": "Ali", "age": 23, "city": "Multan"}

# Writing JSON to file
with open("student.json", "w") as file:
    json.dump(student, file)

# Reading JSON from file
with open("student.json", "r") as file:
    data = json.load(file)
    print(data)

print("-" * 40)

# 4) Working with Large Files
# Read line by line to avoid memory issues
with open("notes.txt", "r") as file:
    for line in file:
        print("Line:", line.strip())
