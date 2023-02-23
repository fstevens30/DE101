# Lab 1-1-1 Question 5
# Flynn Stevens
# fas0265@arastudent.ac.nz

# Write a program to ask the user to enter their first name and then enter their age  and then display a personalised greeting.
# Use f-strings to display the output

# First get the user's first name.
name = input('Please enter your first name: ')

# Next get the user's age.
age = input(f'Hi {name}. Please enter your age: ')

# Display the message.
print(f'I see you are {age} years old {name}.')