# Lab 2-1-1 Question 2
# Flynn Stevens
# fas0265@arastudent.ac.nz

# Get the users first and last name.

first_name = input('Please enter your first name: ').strip() # Strip any leading or trailing whitespace.
last_name = input('Please enter your last name: ').strip()

# Concatenate the first and last name together using title case.

full_name = f'{first_name.title()} {last_name.title()}'

# Const variable for the class name.

CLASS_CODE = 'BCDE101'

# Print the output.

print(f'Pleased to meet you {full_name}, welcome to {CLASS_CODE}.')
