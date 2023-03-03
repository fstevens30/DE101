# Lab 2-2-1 Question 3
# Flynn Stevens
# fas0265@arastudent.ac.nz

# Get the user to input their name
name = input("Please enter your name: ").strip().title()

# Get the user to input the first integer
first_int = int(input(f'Hi {name}, please enter the first integer: '))
# Get the user to input the second integer
second_int = int(input('Thanks. Please enter the second integer: '))

# Logic
equal_to = str(first_int == second_int).lower()
not_equal_to = str(first_int != second_int).lower()
less_than = str(first_int < second_int).lower()
greater_than = str(first_int > second_int).lower()
less_than_or_equal_to = str(first_int <= second_int).lower()
greater_than_or_equal_to = str(first_int >= second_int).lower()

# Display the results
print() # blank line
print(f'It is {equal_to} that {first_int} is equal to {second_int}.')
print(f'It is {not_equal_to} that {first_int} is not equal to {second_int}.')
print() # blank line
print(f'It is {less_than} that {first_int} is less than {second_int}.')
print(f'It is {greater_than} that {first_int} is greater than {second_int}.')
print() # blank line
print(f'It is {less_than_or_equal_to} that {first_int} is less than or equal to {second_int}.')
print(f'It is {greater_than_or_equal_to} that {first_int} is greater than or equal to {second_int}.')