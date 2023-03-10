# Week 4 Lesson 1

# Introduction to Programming
# Loops 1

# Looping through a list
fruits = ['apple', 'banana', 'cherry']
for x in fruits: 
    print(x)
# This loops through the list of fruits and prints each fruit in the list.

#Loop through a string
for x in 'onomatopoeia':
    print(x)
# This loops through the string and prints each letter in the string.

# Using a break statement
class_mates = ['John', 'Jane', 'Joe', 'Jill', 'Jack', 'Flynn', 'Finn', 'Fiona', 'Finnegan', 'Finnley']
for x in class_mates:
    if x == 'Flynn':
        print(x)
        break
# This loops through the list of class_mates and prints each name until it reaches 'Flynn' and then stops.
# The final output will be 'Flynn' because the break statement stops the loop.
# If the break statement was before the print statement, the final output would be 'John' because the loop would stop before it reached 'Flynn'. 