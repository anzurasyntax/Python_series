# 1) try / except - handle errors

try:
    num = int(input("Enter a number: "))
    print("You entered:", num)
except ValueError:
    print("Error: That is not a valid number!")

print("-" * 40)

# 2) Custom error messages
def divide(a, b):
    try:
        result = a / b
        print("Result:", result)
    except ZeroDivisionError:
        print("Error: Cannot divide by zero!")

divide(10, 2)  # works
divide(5, 0)   # custom error message

print("-" * 40)

# 3) Validating Emails
import re

def validate_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    if re.match(pattern, email):
        print("Valid email:", email)
    else:
        print("Invalid email:", email)

validate_email("test@gmail.com")
validate_email("test@@gmail..com")

print("-" * 40)

# 4) Validating Numbers
def validate_number(number):
    if str(number).isdigit():
        print("Valid number:", number)
    else:
        print("Invalid number:", number)

validate_number(12345)
validate_number("12a45")

print("-" * 40)

# 5) Validating Dates (simple format YYYY-MM-DD)
from datetime import datetime

def validate_date(date_text):
    try:
        datetime.strptime(date_text, "%Y-%m-%d")
        print("Valid date:", date_text)
    except ValueError:
        print("Invalid date (expected YYYY-MM-DD):", date_text)

validate_date("2026-01-30")
validate_date("30-01-2026")
