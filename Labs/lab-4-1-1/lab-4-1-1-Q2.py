# Lab 4-1-1 Question 2
# Flynn Stevens
# fas0265@arastudent.ac.nz

# This is the same as the previous lab but instead we decrement the line number.

# Constants
LINE = ('Line ')

# Get the line number from the user
line_request = input('Please enter the number of lines you would like displayed: ').strip()

# Make sure it is int and greater than 0
if line_request.isdigit() and int(line_request) > 0:
    # Convert to int
    line_request = int(line_request)
    for line_request in range(line_request, 0, -1):
        print(LINE + str(line_request))
    print('Loop finished.')
elif line_request == '0':
    print('No loop requested.')
else:
    # If it is not int
    print('Integers only please.')

# Final line
print("Bye.")