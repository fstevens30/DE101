# Lab 3-1-1 Question 1
# Flynn Stevens
# fas0265@arastudent.ac.nz

# Const to store the letter we are looking for
FIRST_LETTER = 'A'

# Ask the user to input their name
user_name = input('Please enter your first name: ').strip().capitalize()

# Store the first letter of the name in a variable
first_letter = user_name[0] 

# Check if the first letter is the same as what we are looking for
if first_letter == FIRST_LETTER:
    print(f'Hi {user_name}, your first name starts with the letter {FIRST_LETTER}.')
else:
    print(f'Hi {user_name}, your first name does not start with the letter {FIRST_LETTER}.')