# Lab 2-2-1 Question 2
# Flynn Stevens
# fas0265@arastudent.ac.nz

# Ask the user to enter a word ending in 's'
# Display a message saying it is true or false that the word they entered ended with s (case insensitive)

# CONST for the letter to check for
LETTER = "s"

# Get the user input
word = input(f'Please enter a word that ends with {LETTER}: ').strip()

# Check the word ends with the letter s
result = str(word.lower().endswith(LETTER)).lower() # returns true or false in lower case

# Display the result
print(f'It is {result} that {word} ends with {LETTER}.')