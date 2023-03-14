# Lab 4-2-1 Challenge
# Flynn Stevens 
# fas0265@arastudent.ac.nz

is_valid = False

while not is_valid:
    user_name = input('Please enter your full name: ').strip().title()
    if user_name.replace(" ", "").replace("-", "").replace("`", "").isalpha() and user_name[0].isalpha() and user_name[-1].isalpha():
        print(f'Your full name has been validated.  It is: {user_name}')
        is_valid = True
    else:
        print('Your full name is not valid.')

# Below is my original code, but I have since changed it to the above code.  I have left it here for reference.

# user_name = input('Please enter your full name: ').strip().title()

# if user_name.replace(" ", "").replace("-", "").replace("`", "").isalpha() and user_name[0].isalpha() and user_name[-1].isalpha():
#     print(f'Your full name has been validated.  It is: {user_name}')
# else:
#     while user_name.replace(" ", "").replace("-", "").replace("`", "").isalpha() and user_name[0].isalpha() and user_name[-1].isalpha() == False:
#         print('Your full name is not valid.')
#         user_name = input('Please enter your full name: ').strip().title()