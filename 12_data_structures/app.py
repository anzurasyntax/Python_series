# 1) Lists - ordered, mutable collection
fruits = ["apple", "banana", "cherry", "banana", "date"]
print("Original List:", fruits)

# Filtering - get only 'banana'
bananas = [fruit for fruit in fruits if fruit == "banana"]
print("Filtered List (bananas):", bananas)

# Slicing - get first three fruits
first_three = fruits[0:3]
print("Sliced List (first 3):", first_three)

# Adding and removing items
fruits.append("elderberry")
print("After append:", fruits)
fruits.remove("banana")  # removes first occurrence
print("After remove:", fruits)

# 2) Tuples - ordered, immutable collection
person = ("Ali", 23, "Multan")
print("Tuple:", person)
print("Name from Tuple:", person[0])
# person[1] = 24  # ❌ This will raise an error

# 3) Sets - unordered collection, no duplicates
numbers = [1, 2, 3, 2, 4, 1, 5]
unique_numbers = set(numbers)
print("Unique Numbers using set:", unique_numbers)

# Add or remove elements
unique_numbers.add(6)
print("After adding 6:", unique_numbers)
unique_numbers.discard(2)
print("After discarding 2:", unique_numbers)

# 4) Dictionaries - key-value pairs
student = {
    "name": "Ali",
    "age": 23,
    "city": "Multan"
}
print("Dictionary:", student)
print("Student Name:", student["name"])

# Adding/updating key-value
student["grade"] = "A"
student["age"] = 24
print("Updated Dictionary:", student)

# Looping through dictionary
for key, value in student.items():
    print(key, ":", value)
