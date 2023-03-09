# Lab 3-2-1 Question 1
# Flynn Stevens
# fas0265@arastudent.ac.nz

# Get the name of the user
name = input('Please enter your first name: ').strip().title()

# Get the numbers
first_num = int(input(f'Hi {name}. Please enter the first number: ').strip())
second_num = int(input(f'Thanks {name}. Please enter the second number: ').strip())

# Logic
if first_num > second_num:
    print(f'{first_num} is greater than {second_num}')
elif first_num < second_num:
    print(f'{first_num} is less than {second_num}')
else:
    print(f'{first_num} is equal to {second_num}')