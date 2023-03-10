# Week 3 Lesson 2

# Introduction to Programming
# Conditional statements 2

# Logical operators review

# Example of "and" operator
if (x > 0) and (y > 0):
    print("Both x and y are positive")
# This only prints if both x AND y are positive

# Example of "or" operator
if (x > 0) or (y > 0):
    print("At least one of x and y is positive")
# This prints if either x OR y is positive

# Example of "not" operator
if not (x > 0):
    print("x is not positive")
# This prints if x is NOT positive


# elif statements
# elif is short for "else if"
if (x > 0):
    print("x is positive")
elif (x < 0):
    print("x is negative")
else:
    print("x is zero")

# The elif statement is only checked if the if statement is false

# if all()
# all() returns True if all elements in the iterable are true
if all([x > 0, y > 0]):
    print("Both x and y are positive")
# This only prints if both x AND y are positive

# if any()
# any() returns True if any element in the iterable is true
if any([x > 0, y > 0]):
    print("At least one of x and y is positive")
# This prints if either x OR y is positive

# CLASS CHALLENGE EXAMPLE Logical Errors

today = "Friday"

if today == ('saturday' or 'sunday'):
    print("It's the weekend!")
else:
    print("It's a weekday.")
# This doesnt work because the 'or' operator is evaluated first meaning that 

# This is the correct way to do it
if today == 'saturday' or today == 'sunday':
    print("It's the weekend!")
else:
    print("It's a weekday.")


# Writing faster and simpler code

a = 1
b = 2
if a > b:
    a = biggest
else:
    b = biggest

print(biggest)

# This can be written as
a = 1
b = 2
if a > b:
    print(a)
else:
    print(b)

# Even shorter

a = 1
b = 2
print(a if a > b else b)


a = 1
b = 2
if a == b:
    print("a and b are equal")
elif a > b:
    print(a)
else:
    print(b)

# This can be written as

a = 1
b = 2
print("a and b are equal" if a == b else a if a > b else b)