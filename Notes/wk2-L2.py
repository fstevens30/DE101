# Week 2 Lesson 2

# Intro to Programming
# Logic & Comparison Operators

# Example of assignment
a = 5
# We are assigning the value 5 to the variable a

# Boolean values
# True or False | 1 or 0 | Yes or No | On or Off
# Boolean values are used to represent the truth of a statement

# Example of a boolean value
b = True
# We are assigning the value True to the variable b

# Boolean is a primitive data type which means it has no methods or attributes
# a bool is also case sensitive so True and False are different than true and false

doctor_suess_ism = True
print(f'It is {doctor_suess_ism} that {doctor_suess_ism} is {doctor_suess_ism}.')
# RETURNS: "It is True that True is True."

# Comparison Operators

# == is equal to
# != is not equal to
# > is greater than
# < is less than
# >= is greater than or equal to
# <= is less than or equal to
# === is equal to and of the same type

# Keep in mind that = is assignment and == is comparison

# Membership Operators

# 'in' is a membership operator
# 'not' in is a membership operator

# Comparison Operators EXAMPLE

num_1 = 1
num_2 = 2
print(num_1 < num_2)
# RETURNS: True because 1 is less than 2

another_num_1 = 1
another_num_2 = 1
print(another_num_1 < another_num_2)
# RETURNS: False because 1 is not less than 1

this_num_1 = 1
this_str_1 = '1'
print(this_num_1 == this_str_1)
# RETURNS: False because you cannot compare a number to a string

# More string methods and membership operators

# islower() 
# Is the string all lower case letters?

# isupper()
# Is the string all upper case letters?

# isalpha()
# Is the string all letters?

# isalnum()
# Is the string all letters and numbers?

# isdigit()
# Is the string all numbers?

# isspace()
# Is the string all spaces?

# isdecimal()
# Is the string all decimal numbers?

# isnumeric()
# Is the string all numeric characters?

# Using 'in' membership operator
# EXAMPLE 
question = 'This is a question?'
is_question = '?' in question
print(is_question) # RETURNS: True