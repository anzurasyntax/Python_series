# Simple Function Example
def greet():
    print("Welcome to Data Analysis")

greet()


# Function with Parameters
def add_numbers(a, b):
    print("Sum is:", a + b)

add_numbers(5, 10)


# Function with Return Value
def calculate_average(total, count):
    return total / count

avg = calculate_average(100, 4)
print("Average is:", avg)


# Function with Default Parameter
def clean_city_name(city="Unknown"):
    print("City:", city)

clean_city_name("multan")
clean_city_name()


# Lambda Function Example
square = lambda x: x * x
print("Square of 5 is:", square(5))

