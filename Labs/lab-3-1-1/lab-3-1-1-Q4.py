# Lab 3-1-1 Question 4
# Flynn Stevens
# fas02652@arastudent.ac.nz

# Number validator
# Validate if the input is a valid number (int or float)

# Get user input
input_num = input('Please enter the number: ').strip()

# Check if input is a valid number
# Remove the first occurance of a decimal point and check if the remaining string is a digit
if input_num.replace('.', '', 1).isdigit(): 
    if input_num.count('.') == 1: # If the input has a decimal point, it is a float
        print(f'{float(input_num)} is a valid number.') 
    else: # If the input does not have a decimal point, it is an integer
        print(f'{int(input_num)} is a valid number.')
else: # If the input is not a digit, it is not a valid number
    print(f'{input_num} is not a valid number.')