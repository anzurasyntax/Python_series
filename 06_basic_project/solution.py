# Student Info & Marks System

# INPUT SECTION WITH TYPE CONVERSION
name = input("Enter student name: ")
age = int(input("Enter age: "))
math_marks = int(input("Enter Math marks: "))
english_marks = int(input("Enter English marks: "))
science_marks = int(input("Enter Science marks: "))

# VARIABLES 
total_marks = math_marks + english_marks + science_marks
average_marks = total_marks / 3
is_pass = average_marks >= 50

# OUTPUT SECTION
print("STUDENT REPORT")
print("Name:", name)
print("Age:", age)
print("Total Marks:", total_marks)
print("Average Marks:", average_marks)
print("Pass Status:", is_pass)

# TYPE CHECK (for learning)
print("DATA TYPES")
print("Type of name:", type(name))
print("Type of age:", type(age))
print("Type of average:", type(average_marks))
