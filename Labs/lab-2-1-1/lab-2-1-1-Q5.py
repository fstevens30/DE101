# Lab 2-1-1 Question 5
# Flynn Stevens
# fas0265@arastudent.ac.nz

# Get the users first and last name.
# Get the users 1 digit area code.
# Get the users 7 digit phone number.
# Print the users national phone number & international phone number. 

# First declaring the const variables.

NATIONAL_PREFIX = "0"
INTERNATIONAL_PREFIX = "+64"

# Get the users first and last name.
first_name = input("Please enter your first name: ").strip().capitalize()
last_name= input(f'{first_name}, please enter your last name: ').strip().title()
full_name = f'{first_name} {last_name}'

# Get the users 1 digit area code.
area_code = input(f'Next, please enter your 1 digit area code: ').strip()

# Get the users 7 digit phone number.
phone_number = input(f'Lastly {first_name}, please enter your 7 landline number: ').replace(" ", "")

# National number
national_number = f'{NATIONAL_PREFIX}{area_code}{phone_number}'
# International number
international_number = f'{INTERNATIONAL_PREFIX}{area_code}{phone_number}'

# Print the users national phone number & international phone number.
print(f'Full name: {full_name}.  National number: {national_number} International number: {international_number}')