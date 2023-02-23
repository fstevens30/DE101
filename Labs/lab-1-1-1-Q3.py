# Lab 1-1-1 Question 3
# Flynn Stevens
# fas0265@arastudent.ac.nz

# Personalised greeting with first and last name.

# First get the first name and last name variables.

first_name = input('Please enter your first name: ')
last_name = input('Please enter your last name: ')

# Now print the greeting with the first and last name.

print('''Hi
{}
{}
Pleased to meet you.
'''.format(first_name, last_name))

# This used the format method to print the first and last name in the greeting.