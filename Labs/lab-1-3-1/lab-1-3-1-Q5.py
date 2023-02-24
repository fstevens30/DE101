# Lab 1-3-1 Q5
# Flynn Stevens
# fas0265@arastudent.ac.nz

# Write a program to ask the user to enter their first name followed by two integers. 
# Display the integer division and remainder results of the integers.

# get the users name
first_name = input('Please enter your first name: ')

# greet the user
print(f'Hi {first_name}.')

# get the first integer
first_integer = int(input('Please enter the first integer: '))

# get the second integer
second_integer = int(input('Please enter the second integer: '))

# calculate the integer division and remainder results
integer_division = first_integer // second_integer
remainder = first_integer % second_integer

# display the results
print(f'{first_name}, the answer to {first_integer} divided by {second_integer} is {integer_division} with a remainder of {remainder}.')