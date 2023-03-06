# Lab 3-1-1 Question 5
# Flynn Stevens
# fas0265@arastudent.ac.nz

# Should we go to the beach?

# Get the user name
user_name = input('Please enter your first name: ').strip().title()

# Does the user want to go to the beach, strip whitespace and convert to lowercase for validation
user_wants = input(f'Hi {user_name}, should we go to the beach? (y/n): ').strip().lower()

if user_wants[0] == 'y': # If the first character of the user input is 'y'
    # Move on to the temperature question
    temp = (input(f'{user_name}, what is the current temperature: ')).strip()
    # Verify the user input is a number
    if temp.isnumeric():
        # get the minimum temperature
        min_temp = (input('What is the minimum temperature for going to the beach? ')).strip()
    # Verify that the user input is a number
    if temp.isnumeric() and min_temp.isnumeric():
        # Convert the user input to a float
        temp = float(temp)
        min_temp = float(min_temp)
        # Check if the temperature is above the minimum
        if temp >= min_temp:
            print(f'You can go to the beach because it is {temp} degrees.')
        else:
            print(f'It\'s not warm enough, stay at home.')
    else: # The user input is not a number
        print('The temperature needs to be numeric.')


else:
    print('Ok, enjoy your time at home.')

