# Lab 3-1-1 Question 3
# Flynn Stevens
# fas0265@arastudent.ac.nz

# Verify if the users first name is valid

# Ask the user to input their name
first_name = input('Please enter your first name: ').strip().title()

# Valid characters include letters, hyphens and spaces only

# Check if the first name is valid
if first_name.isalpha() or first_name.replace('-', '').replace(' ', '').isalpha():
    print(f'{first_name} is a valid name.')
else:
    print(f'{first_name} is not a valid name.')