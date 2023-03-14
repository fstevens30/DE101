# Lab 4-1-1 Question 5
# Flynn Stevens
# fas0265@arastudent.ac.nz

# Get the message 
message = input('Please enter a message: ').strip()

# Function to determine the character type
def char_type(character): return 'digit' if character.isdigit() else 'lower alpha' if character.isalpha() and character.islower() else 'upper alpha' if character.isalpha() and character.isupper() else 'space' if character.isspace() else 'symbol'

if message != '': 
    for index, character in enumerate(message): print(f'{(index + 1):<2} {character} - {char_type(character)}')
else: print('You did not enter a message.')