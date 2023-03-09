# Lab 3-2-1 Question 3
# Flynn Stevens
# fas0265@arastudent.ac.nz

# Start 
print('Integer comparator.')

# Get first name
name = input('Please enter your first name: ').strip().title()

# Get first num
first_num = input(f'Hi {name}, please enter the first number: ').strip()

# Get second num
second_num = input('Please enter the second number: ').strip()

# Get third num
third_num = input('Please enter the third number: ').strip()

# Logic

# First check if there is an invalid number
if first_num.isnumeric() and second_num.isnumeric() and third_num.isnumeric():
    # Convert to int
    first_num = int(first_num)
    second_num = int(second_num)
    third_num = int(third_num)
    # Check if all numbers are the same
    if first_num == second_num == third_num:
        print('All the numbers are the same.')
    # Check if all numbers are different
    elif first_num != second_num and first_num != third_num and second_num != third_num:
        print('All the numbers are different.')
    # Must be two numbers the same
    else: print('Two of the numbers are the same.')
# Invalid number
else: print('One or more of the numbers are invalid.')