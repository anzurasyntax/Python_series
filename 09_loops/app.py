# For Loop Example

for char in range(10,20): # Range function is used to generate a sequence of numbers
    print(char)

# While Loop Example
count = 0
while count < 5: # It check the condition before executing the loop body when the condition is true it executes the loop body otherwise it stops
    print("Count is:", count)
    count += 1


# Break Statement Example
for i in range(1, 6):
    if i == 3:
        break #Output will stop when i becomes 3
    print(i) 

# Continue Statement Example
for i in range(1, 6):
    if i == 3:
        continue #It will skip 3 but print all other numbers.
    print(i) 


# pass Statement Example
for i in range(1, 6):
    if i == 3:
        pass #Loop runs normally; pass just fills the place.
    print(i) 