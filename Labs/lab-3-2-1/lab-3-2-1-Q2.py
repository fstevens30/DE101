# Lab 3-2-1 Question 2
# Flynn Stevens
# fas0265@arastudent.ac.nz

# Get the users name
name = input('Please enter your first name: ').strip().title()

# Get the users age
age = int(input(f'Hi {name}, please enter your age in years: ').strip())

# Logic
# If the age is an even number
if age % 2 == 0: # We can use the modulus operator to check if the number is even
    print(f'{name}, {age} is an even number of years.')
else:
    print(f'{name}, {age} is an odd age.')

# Refactor

refname = input('Please enter your first name: ').strip().title()
refage = int(input(f'Hi {refname}, please enter your age in years: ').strip())

TRUE = print(f'{name}, {age} is an even number of years.')
FALSE = print(f'{name}, {age} is an odd age.')

if age % 2 == 0:
    TRUE
else:
    FALSE
