# Lab 1-3-1 Q6
# Flynn Stevens
# fas0265@arastudent.ac.nz


# get the users name
first_name = input('Please enter your first name: ')

# greet the user
print(f'Hi {first_name}.')

# get the first integer
first_integer = int(input('Please enter the first integer: '))

# get the second integer
second_integer = int(input('Please enter the second integer: '))

# calculate the difference using abs()
diff = abs(first_integer - second_integer)

# display the results
print(f'{first_name}, the absolute difference between {first_integer} and {second_integer} is {diff}.')