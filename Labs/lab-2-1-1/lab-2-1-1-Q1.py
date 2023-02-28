# Lab 2-1-1 Q1
# Flynn Stevens
# fas0265@arastudent.ac.nz

# Get the user to input their name.

user_name = input('Please enter your first name: ')

# Format the user's name to be all uppercase.

UPPERCASE_NAME = user_name.upper()

# Format the user's name to be all lowercase.

LOWERCASE_NAME = user_name.lower()

# Format the user's name to be in title case.

TITLECASE_NAME = user_name.title()

# The title() method will only capitalise the first letter of the first word in the string.

# Display the user's name in uppercase, lowercase and title case.

print(f'{TITLECASE_NAME}, your first name in lower case is {LOWERCASE_NAME} and in upper case is {UPPERCASE_NAME}.')
