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

# Types of loops
# In Python there are two types of loops - for loops and while loops.

# Example of a for loop
for number in 1, 2, 3, 4, 5:
    print(number)
# This loop will print the numbers 1 through 5.

# Using the range() function
for number in range(1, 6):
    print(number)
# This loop will print the numbers 1 through 5. It doesn't include the last number in the range as it is exclusive.

# Using the range() function with a step
for number in range(1, 6, 2):
    print(number)
# This loop will print the numbers 1, 3, and 5 as it is stepping by 2.

for number in 1,2,3,4,5:
	print(number)

# For loop without enumerator
message = "Hello World"
counter = 1
for char in message:
	print(f'{counter:<2}: {char}')
	counter = counter + 1

print() # Line break

# For loop with enumerate
enum_msg = "Enumerate"
iterator = 1
for msg_char, each_char in enumerate(enum_msg, start=1):
	print(f'{msg_char:<2}: {each_char}')
        


# While loop
# While the condition is true, the loop will continue to run.

# Example of a while loop
print('While loop')
loop_counter = 1
end = 5
while loop_counter <= end:
    print(loop_counter)
    loop_counter = loop_counter + 1
# This loop will print the numbers 1 through 5.


# Validating inputs with a while loop
# This loop will continue to run until the user enters a valid input.

MIN_VALUE = 1
MAX_VALUE = 10
value = 11 # Set to an invalid value to start the loop

while value < MIN_VALUE or value > MAX_VALUE:
    value = int(input(f'Enter a number between {MIN_VALUE} and {MAX_VALUE}: '))
    if value < MIN_VALUE or value > MAX_VALUE:
        print(f'Sorry, {value} is not between {MIN_VALUE} and {MAX_VALUE}.')
print('Thank you.')

print('Here be \U0001F409') # This prints a dragon emoji :D

