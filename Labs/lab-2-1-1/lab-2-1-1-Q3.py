# Lab 2-1-1 Question 3
# Flynn Stevens
# fas0265@arastudent.ac.nz  

# Get the users first and last name.
# Format the names to title case and store in a variable.
# Get the user to enter a sentence.

first_name = input('Please enter your first name: ').strip().title()
last_name = input(f'{first_name}, please enter your last name: ').strip().title()

full_name = f'{first_name} {last_name}'

sentence = input(f'{first_name}, please enter a sentence: ')

# Remove all spaces from the sentence and store in a variable.

sentence_no_spaces = sentence.strip()

# Count the number of characters in the sentence and store in a variable.

sentence_length = len(sentence_no_spaces)

# Find the first and last character of the sentence and store in a variable.

first_char = sentence_no_spaces[0]
last_char = sentence_no_spaces[-1]

# Print the results to the user.
print(f"Report for {full_name}'s sentence of {sentence_length} characters.")
print(f'First character: {first_char}')
print(f'Last character: {last_char}')