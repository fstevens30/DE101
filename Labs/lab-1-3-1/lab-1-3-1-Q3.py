# Lab 1-3-1 Q1
# Flynn Stevens
# fas0265@arastudent.ac.nz

# Write a program which asks the user to enter an integer and then by using augmented assignment statements, display the results as per the output below.

first_int = int(input('Please enter the first integer: '))
second_int = int(input('Please enter the second integer: '))

sum_result = first_int 
sum_result += second_int

difference_result = first_int
difference_result -= second_int

multiply_result = first_int
multiply_result *= second_int

div_result = first_int
div_result /= second_int

print(f'{first_int} + {second_int} is {sum_result}')
print(f'{first_int} - {second_int} is {difference_result}')
print(f'{first_int} * {second_int} is {multiply_result}')
print(f'{first_int} / {second_int} is {div_result}')