# Lab 4-1-1 Question 4
# Flynn Stevens
# fas0265@arastudent.ac.nz

firstname = input('Please enter your first name: ').strip().title()

# Ignore the hyphens and spaces in the name and check if it isalpha()

if firstname.replace('-', '').replace(' ', '').isalpha():
    for i in range(0, len(firstname)):
        i = i + 1
        print(f'{str(i)} {firstname[i - 1]}')
        total_letters = len(firstname.replace('-', '').replace(' ', ''))
    if total_letters == 1:
        print(f'There is {total_letters} letter in {firstname}.')
    else:
        print(f'There are {total_letters} letters in {firstname}.')

elif firstname == '': # If the user enters nothing
    print('You did not enter any characters.')
else:
    print('Non alphabetic characters were entered.')