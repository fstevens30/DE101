# Lab 3-1-1 Question 2
# Flynn Stevens
# fas0265@arastudent.ac.nz

# Const to store the letter we are looking for
LAST_LETTER = 'n'

# Ask the user to input their name
user_name = input('Please enter your first name: ').strip().title()

# Store the last letter of the name in a variable
last_letter = user_name[-1]

# Check if the last letter is the same as what we are looking for
if last_letter == LAST_LETTER:
    print(f'Hi {user_name}, your first name ends with the letter {LAST_LETTER}.')
else:
    print(f'Hi {user_name}, your first name does not end with the letter {LAST_LETTER}.')