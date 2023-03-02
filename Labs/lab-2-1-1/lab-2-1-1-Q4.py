# Lab 2-1-1 Question 4
# Flynn Stevens
# fas0265@arastudent.ac.nz

# Get the users first and last name.
# Get the user to enter a message.
# Get the user to enter the start and end indexes of a substring they want to create from the message.
# Print the substring.


# Get the users first and last name.
first_name = input("Please enter your first name: ").strip().capitalize()
last_name= input(f'{first_name}, please enter your last name: ').strip().title()
full_name = f'{first_name} {last_name}'

# Get the user to enter a message.
message = input(f'{first_name}, please enter a message: ').strip()
# Get the character count of the message.
message_length = len(message)

# Get the indexes of the substring.
start_index = int(input('Please enter the start position: '))
end_index = int(input('Please enter the end position: '))

substring = message[start_index-1 : end_index]
# Minus 1 to account for the 0 index as the users wont know this. However the end index is inclusive so no need to minus 1.

# Print outcomes
print(f"Report for {full_name}'s sentence of {message_length} characters.")
print(f"The characters '{substring}' can be found in position {start_index} to position {end_index} inclusively.")