# Lab 2-2-1 Question 1
# Flynn Stevens
# fas0265@arastudent.ac.nz

# Ask the user to enter a word starting with the letter 'Q'
# Display a message if it is true or false that the word starts with the letter 'Q' (case senseitive)

# CONST for the letter to check for
Q_LETTER = "Q"

# Get the user input
word = input(f'Please enter a word that starts with upper case {Q_LETTER}: ')

# Check if the word starts with the letter Q
result = str(word.startswith(Q_LETTER)).lower()

# Display the result
print(f'It is {result} that {word} starts with upper case {Q_LETTER}.')