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
    if temp.replace('.', '', 1).isnumeric(): # If the user input is a number

        # get the minimum temperature
        min_temp = (input('What is the minimum temperature for going to the beach? ')).strip()

        # Verify that the user input is a number
        if min_temp.replace('.', '', 1).isnumeric(): 
        # Convert the user input to a float
            temp = float(temp)
            min_temp = float(min_temp)
        # Check if the temperature is above the minimum
            if temp >= min_temp:
                print(f'You can go to the beach because it is {temp} degrees.')

            # Check if they would like an ice cream
                ice_cream = input(f'Would you like to buy an ice cream {user_name}? (y/n): ').strip().lower()
                if ice_cream[0] == 'y': # Work out the cash
                    cash = input('How much cash do you have? ')
                    # check that the cash is a valid amount of cash
                    if cash.replace('.', '', 1).isdigit() == False:
                        print(f'{cash} is not a valid amount of cash.')
                        print('Enjoy your time at the beach.')
                    # Else if the cash amount is 0
                    elif cash == 0:
                        print('Please remember to bring cash next time.')
                        print('Enjoy your time at the beach.')
                    else:
                        ice_cream_cost = input('How much is an ice cream? ')
                        # Error if ice cream cost is not a number
                        if ice_cream_cost.replace('.', '', 1).isdigit() == False:
                            print(f'{ice_cream_cost} is not a valid cost for an ice cream.')
                        else:
                            remainder_cash = cash - ice_cream_cost
                            if cash >= ice_cream_cost:
                                print(f'You can buy an ice cream and you will have ${remainder_cash:.2f} left.')
                                print('Enjoy your time at the beach.')
                            else:
                                print(f'Sorry {user_name}, no ice cream today.')
                                print('Enjoy your time at the beach.')

                    

                else: # They don't want an ice cream
                    print('Enjoy your time at the beach.')

            else: # Its not warm enough
                print(f'It\'s not warm enough, stay at home.')
        else: # The user input is not a number
            print('The temperature needs to be numeric.')
else:
    print('Ok, enjoy your time at home.')