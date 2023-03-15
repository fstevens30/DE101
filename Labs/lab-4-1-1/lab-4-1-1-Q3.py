# Lab 4-1-1 Question 3
# Flynn Stevens
# fas0265@arastudent.ac.nz

# Ask a user to enter an increment value and a number of lines to display.

# Constants
COUNTER = 'Counter: '
VALUE = 'value: '
COUNTER_START = 1

# Get the counter value from the user
counter_request = input('Please enter how many numbers you would like displayed: ').strip()

if counter_request.isdigit() and int(counter_request) > 0:
    # Get the increment value from the user
    increment_request = input('Please enter the increment value: ').strip()

    if counter_request.isdigit() and increment_request.isdigit() and int(counter_request) > 0 and int(increment_request) > 0:
        # Convert to int
        counter_request = int(counter_request)
        increment_request = int(increment_request)
        # Start at COUNTER_START and increment by increment_request
        for i in range(1, counter_request + 1):
            if i == 1:
                print(f'{COUNTER}{i} {VALUE}{(i - 1) * increment_request + 1}')
            else:
                print(f'{COUNTER}{i} {VALUE}{(i - 1) * increment_request + 1}')
        print('Bye.')

    elif increment_request == '0':
        print('The increment value needs to be > 0.')
    else:
        print('Positive non zero integers only.')

elif counter_request == '0':
    print('There is nothing to count.')
else:
    print('Positive non zero integers only.')