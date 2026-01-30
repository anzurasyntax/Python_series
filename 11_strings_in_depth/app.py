# String Methods Examples

# 1) strip() - removes Extra spaces
city = "  Multan  "
print("Before strip:", city)
print("After strip:", city.strip())

# 2) lower() - converts string to lowercase
name = "MULTAN"
print("Lowercase:", name.lower())

# 3) upper() - converts string to uppercase
print("Uppercase:", name.upper())

# 4) replace() - replaces substring with another
text = "I love Python"
print("Original Text:", text)
print("After Replace:", text.replace("Python", "Data Analysis"))

# 5) split() - splits string into list based on a separator
sentence = "apple,banana,cherry"
fruits = sentence.split(",")
print("Split Fruits:", fruits)

# 6) join() - joins list elements into a string
joined_fruits = " & ".join(fruits)
print("Joined Fruits:", joined_fruits)

# 7) startswith() - checks if string starts with a substring
print("Starts with 'I'? ", text.startswith("I"))
print("Starts with 'You'? ", text.startswith("You"))

# 8) endswith() - checks if string ends with a substring
print("Ends with 'Python'? ", text.endswith("Python"))
print("Ends with 'Java'? ", text.endswith("Java"))

# 9) Regex basics - using re module
import re

sample_text = "My phone number is 123-456-7890"
# Find all digits in the string
digits = re.findall(r'\d+', sample_text)
print("Digits found using regex:", digits)

# Check if string contains 'phone'
contains_phone = re.search(r'phone', sample_text)
print("Contains 'phone'? ", bool(contains_phone))
