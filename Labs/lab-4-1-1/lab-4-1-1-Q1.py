# Lab 4-1-1 Question 1
# Flynn Stevens
# fas0265@arastudent.ac.nz

# Displaying a specified amount of lines.

# Constants
LINE = ('Line ')

# Get the line number from the user
line_request = input('Please enter the number of lines you would like displayed: ')

# Make sure it is int and greater than 0
if line_request.isdigit() and int(line_request) > 0:
    # Convert to int
    line_request = int(line_request)
    for line_request in range(1, line_request + 1):
        print(LINE + str(line_request))
else:
    # If it is not int
    print('Integers only please.')

# Ending string
print('Bye.')