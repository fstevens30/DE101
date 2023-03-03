# Lab 2-2-1 Question 5
# Flynn Stevens
# fas0265@arastudent.ac.nz

# Get user inputs
lower_word = input('Please enter a word whose letters are all lower case: ').strip()
upper_word = input('Please enter a word whose letters are all upper case: ').strip()

lower_word_lower = lower_word.lower() # Convert the lower case word to lower case
upper_word_upper = upper_word.upper() # Convert the upper case word to upper case

is_lower = str(lower_word == lower_word_lower).lower() # Is the lower case word the same as the lower case word? (True or False) This is also formatted to lower case for printing.
is_upper = str(upper_word == upper_word_upper).lower() # Is the upper case word the same as the upper case word? (True or False) This is also formatted to lower case for printing.

# Print the results
print(f'It is {is_lower} that {lower_word} is in all lower case letters.')
print(f'It is {is_upper} that {upper_word} is in all upper case letters.')